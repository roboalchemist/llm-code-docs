# Source: https://trigger.dev/docs/guides/frameworks/supabase-edge-functions-database-webhooks.md

# Triggering tasks from Supabase Database Webhooks

> This guide shows you how to trigger a transcribing task when a row is added to a table in a Supabase database, using a Database Webhook and Edge Function.

## Overview

Supabase and Trigger.dev can be used together to create powerful workflows triggered by real-time changes in your database tables:

* A Supabase Database Webhook triggers an Edge Function when a row including a video URL is inserted into a table
* The Edge Function triggers a Trigger.dev task, passing the `video_url` column data from the new table row as the payload
* The Trigger.dev task then:

  * Uses [FFmpeg](https://www.ffmpeg.org/) to extract the audio track from a video URL
  * Uses [Deepgram](https://deepgram.com) to transcribe the extracted audio
  * Updates the original table row using the `record.id` in Supabase with the new transcription using `update`

## Prerequisites

* Ensure you have the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) installed
* Since Supabase CLI version 1.123.4, you must have [Docker Desktop installed](https://supabase.com/docs/guides/functions/deploy#deploy-your-edge-functions) to deploy Edge Functions
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project
* [Create a new Deepgram account](https://deepgram.com/) and get your API key from the dashboard

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/supabase-edge-functions">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Initial setup

<Steps>
  <Step title="Optional step 1: create a new Supabase project">
    <Info> If you already have a Supabase project on your local machine you can skip this step.</Info>

    You can create a new project by running the following command in your terminal using the Supabase CLI:

    ```bash  theme={null}
    supabase init
    ```

    <Note>
      If you are using VS Code, ensure to answer 'y' when asked to generate VS Code settings for Deno,
      and install any recommended extensions.
    </Note>
  </Step>

  <Step title="Optional step 2: create a package.json file">
    If your project does not already have `package.json` file (e.g. if you are using Deno), create it manually in your project's root folder.

    <Info> If your project has a `package.json` file you can skip this step.</Info>

    This is required for the Trigger.dev SDK to work correctly.

    ```ts package.json theme={null}
    {
      "devDependencies": {
        "typescript": "^5.6.2"
      }
    }
    ```

    <Note> Update your Typescript version to the latest version available. </Note>
  </Step>

  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={null}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={null}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={null}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    1. Log you into the CLI if you're not already logged in.
    2. Create a `trigger.config.ts` file in the root of your project.
    3. Ask where you'd like to create the `/trigger` directory.
    4. Create the `/trigger` directory with an example task, `/trigger/example.[ts/js]`.

    Choose "None" when prompted to install an example task. We will create a new task for this guide.
  </Step>
</Steps>

## Create a new table in your Supabase database

First, in the Supabase project dashboard, you'll need to create a new table to store the video URL and transcription.

To do this, click on 'Table Editor' <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" /> in the left-hand menu and create a new table. <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" />

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-1.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4b7630a86b91ac5f942ac31538ad401d" alt="How to create a new Supabase table" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-new-table-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-1.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=cb8f066d063d37ba77150315e852ce86 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-1.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=e6826c90fe6a0b9ade20f16e343bffc8 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-1.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=f502bf263b08fb57a28095131987eef5 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-1.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=bda96d83c7276830f239d7a1773cf379 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-1.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=0db75386570571a94a218936a250c737 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-1.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=0a2bbf11537f694d5e8888c590d8a22b 2500w" />

Call your table `video_transcriptions`. <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" />

Add two new columns, one called `video_url` with the type `text` <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" />, and another called `transcription`, also with the type `text` <Icon icon="circle-3" iconType="solid" size={20} color="A8FF53" />.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-2.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=a1c1f36b91edf8538ae33cc465f9ec47" alt="How to create a new Supabase table 2" data-og-width="3224" width="3224" data-og-height="1824" height="1824" data-path="images/supabase-new-table-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-2.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=a1a99d222b35bd675f86b37cd83e14b4 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-2.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=6189562ca9bebf649c074db28126c3ed 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-2.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=73262a6abaa2851fbabed87f3200b930 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-2.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=53054702bf0efbd27e3920cb8957d1aa 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-2.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4efb3c0cbaa50ed4611f62fc537ca04b 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-2.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=78d48f7f37128ea37b494a76a824f511 2500w" />

## Create and deploy the Trigger.dev task

### Generate the Database type definitions

To allow you to use TypeScript to interact with your table, you need to [generate the type definitions](https://supabase.com/docs/guides/api/rest/generating-types) for your Supabase table using the Supabase CLI.

```bash  theme={null}
supabase gen types --lang=typescript --project-id <project-ref> --schema public > database.types.ts
```

<Note> Replace `<project-ref>` with your Supabase project reference ID. This can be found in your Supabase project settings under 'General'. </Note>

### Create the transcription task

Create a new task file in your `/trigger` folder. Call it `videoProcessAndUpdate.ts`.

This task takes a video from a public video url, extracts the audio using FFmpeg and transcribes the audio using Deepgram. The transcription summary will then be updated back to the original row in the `video_transcriptions` table in Supabase.

You will need to install some additional dependencies for this task:

<CodeGroup>
  ```bash npm theme={null}
  npm install @deepgram/sdk @supabase/supabase-js fluent-ffmpeg
  ```

  ```bash pnpm theme={null}
  pnpm install @deepgram/sdk @supabase/supabase-js fluent-ffmpeg
  ```

  ```bash yarn theme={null}
  yarn install @deepgram/sdk @supabase/supabase-js fluent-ffmpeg
  ```
</CodeGroup>

These dependencies will allow you to interact with the Deepgram and Supabase APIs and extract audio from a video using FFmpeg.

<Warning>
  When updating your tables from a Trigger.dev task which has been triggered by a database change,
  be extremely careful to not cause an infinite loop. Ensure you have the correct conditions in
  place to prevent this.
</Warning>

```ts /trigger/videoProcessAndUpdate.ts theme={null}
// Install any missing dependencies below
import { createClient as createDeepgramClient } from "@deepgram/sdk";
import { createClient as createSupabaseClient } from "@supabase/supabase-js";
import { logger, task } from "@trigger.dev/sdk";
import ffmpeg from "fluent-ffmpeg";
import fs from "fs";
import { Readable } from "node:stream";
import os from "os";
import path from "path";
import { Database } from "../../database.types";

// Create a single Supabase client for interacting with your database
// 'Database' supplies the type definitions to supabase-js
const supabase = createSupabaseClient<Database>(
  // These details can be found in your Supabase project settings under `API`
  process.env.SUPABASE_PROJECT_URL as string, // e.g. https://abc123.supabase.co - replace 'abc123' with your project ID
  process.env.SUPABASE_SERVICE_ROLE_KEY as string // Your service role secret key
);

// Your DEEPGRAM_SECRET_KEY can be found in your Deepgram dashboard
const deepgram = createDeepgramClient(process.env.DEEPGRAM_SECRET_KEY);

export const videoProcessAndUpdate = task({
  id: "video-process-and-update",
  run: async (payload: { videoUrl: string; id: number }) => {
    const { videoUrl, id } = payload;

    logger.log(`Processing video at URL: ${videoUrl}`);

    // Generate temporary file names
    const tempDirectory = os.tmpdir();
    const outputPath = path.join(tempDirectory, `audio_${Date.now()}.wav`);

    const response = await fetch(videoUrl);

    // Extract the audio using FFmpeg
    await new Promise((resolve, reject) => {
      if (!response.body) {
        return reject(new Error("Failed to fetch video"));
      }

      ffmpeg(Readable.from(response.body))
        .outputOptions([
          "-vn", // Disable video output
          "-acodec pcm_s16le", // Use PCM 16-bit little-endian encoding
          "-ar 44100", // Set audio sample rate to 44.1 kHz
          "-ac 2", // Set audio channels to stereo
        ])
        .output(outputPath)
        .on("end", resolve)
        .on("error", reject)
        .run();
    });

    logger.log(`Audio extracted from video`, { outputPath });

    // Transcribe the audio using Deepgram
    const { result, error } = await deepgram.listen.prerecorded.transcribeFile(
      fs.readFileSync(outputPath),
      {
        model: "nova-2", // Use the Nova 2 model
        smart_format: true, // Automatically format the transcription
        diarize: true, // Enable speaker diarization
      }
    );

    if (error) {
      throw error;
    }

    const transcription = result.results.channels[0].alternatives[0].paragraphs?.transcript;

    logger.log(`Transcription: ${transcription}`);

    // Delete the temporary audio file
    fs.unlinkSync(outputPath);
    logger.log(`Temporary audio file deleted`, { outputPath });

    const { error: updateError } = await supabase
      .from("video_transcriptions")
      // Update the transcription column
      .update({ transcription: transcription })
      // Find the row by its ID
      .eq("id", id);

    if (updateError) {
      throw new Error(`Failed to update transcription: ${updateError.message}`);
    }

    return {
      message: `Summary of the audio: ${transcription}`,
      result,
    };
  },
});
```

<Warning>
  This task uses your service role secret key to bypass Row Level Security. This is not recommended
  for production use as it has unlimited access and bypasses all security checks.
</Warning>

<Note>
  To learn more about how to properly configure Supabase auth for Trigger.dev tasks, please refer to
  our [Supabase Authentication guide](/guides/frameworks/supabase-authentication). It demonstrates
  how to use JWT authentication for user-specific operations or your service role key for
  admin-level access.
</Note>

### Adding the FFmpeg build extension

Before you can deploy the task, you'll need to add the FFmpeg build extension to your `trigger.config.ts` file.

```ts trigger.config.ts theme={null}
// Add this import
import { ffmpeg } from "@trigger.dev/build/extensions/core";
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>", // Replace with your project ref
  // Your other config settings...
  build: {
    // Add the FFmpeg build extension
    extensions: [ffmpeg()],
  },
});
```

<Note>
  [Build extensions](/config/extensions/overview) allow you to hook into the build system and
  customize the build process or the resulting bundle and container image (in the case of
  deploying). You can use pre-built extensions or create your own.
</Note>

<Note>
  You'll also need to add `@trigger.dev/build` to your `package.json` file under `devDependencies`
  if you don't already have it there.
</Note>

If you are modifying this example and using popular FFmpeg libraries like `fluent-ffmpeg` you'll also need to add them to [`external`](/config/config-file#external) in your `trigger.config.ts` file.

### Add your Deepgram and Supabase environment variables to your Trigger.dev project

You will need to add your `DEEPGRAM_SECRET_KEY`, `SUPABASE_PROJECT_URL` and `SUPABASE_SERVICE_ROLE_KEY` as environment variables in your Trigger.dev project. This can be done in the 'Environment Variables' page in your project dashboard.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=af652254781808a35c2bcefd4b61b59f" alt="Adding environment variables" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/environment-variables-page.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fd6487833d9c659f8a514c7cc86cf84d 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=1758721fd84f5040b88997db401f7391 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=4416f51b1528ae14285a03b560f22389 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=12b90b89f7662aadaea07df17d9d3898 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=28e6921620cda10d335a095dbfa85806 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=4f6c67a030b20699bde25c22d68e57af 2500w" />

### Deploying your task

Now you can now deploy your task using the following command:

<CodeGroup>
  ```bash npm theme={null}
  npx trigger.dev@latest deploy
  ```

  ```bash pnpm theme={null}
  pnpm dlx trigger.dev@latest deploy
  ```

  ```bash yarn theme={null}
  yarn dlx trigger.dev@latest deploy
  ```
</CodeGroup>

## Create and deploy the Supabase Edge Function

### Add your Trigger.dev prod secret key to the Supabase dashboard

Go to your Trigger.dev [project dashboard](https://cloud.trigger.dev) and copy the `prod` secret key from the API keys page.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=0733b8d37ded28dfc8eb55cfbbf8d1de" alt="How to find your prod secret key" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/api-key-prod.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b6322b1c7486febaa68d044cdcee166a 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5a9c86949e65af4e51e105f3e3a6bcc9 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=0b8cd9edac7b0f133e8790c302a64269 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5f86de1e7348b781d66bd13737b0dd37 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5f2fc6b58d2ed8d6d6a1653bb840bd67 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=aed3fb7368091c0ee12cac472e02fc07 2500w" />

Then, in [Supabase](https://supabase.com/dashboard/projects), select the project you want to use, navigate to 'Project settings' <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" />, click 'Edge Functions' <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" /> in the configurations menu, and then click the 'Add new secret' <Icon icon="circle-3" iconType="solid" size={20} color="A8FF53" /> button.

Add `TRIGGER_SECRET_KEY` <Icon icon="circle-4" iconType="solid" size={20} color="A8FF53" /> with the pasted value of your Trigger.dev `prod` secret key.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=70842bf838bc1ea9e1f195c9926bb746" alt="Add secret key in Supabase" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-keys-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=1b893de3a516863384e77179c709a631 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=ba9cab56f377dc72898cd388a3280901 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=37d7d313be698f7015fe490fc01cad30 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=73a7d40712c7a889bbe6af3803b86df7 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=0c62e86405a9e23947ed073be6c5fca4 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=30c4316db62c7820dd5c513c922b2976 2500w" />

### Create a new Edge Function using the Supabase CLI

Now create an Edge Function using the Supabase CLI. Call it `video-processing-handler`. This function will be triggered by the Database Webhook.

```bash  theme={null}
supabase functions new video-processing-handler
```

```ts functions/video-processing-handler/index.ts theme={null}
// Setup type definitions for built-in Supabase Runtime APIs
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { tasks } from "npm:@trigger.dev/sdk@latest";
// Import the videoProcessAndUpdate task from the trigger folder
import type { videoProcessAndUpdate } from "../../../src/trigger/videoProcessAndUpdate.ts";
//     👆 type only import

// Sets up a Deno server that listens for incoming JSON requests
Deno.serve(async (req) => {
  const payload = await req.json();

  // This payload will contain the video url and id from the new row in the table
  const videoUrl = payload.record.video_url;
  const id = payload.record.id;

  // Trigger the videoProcessAndUpdate task with the videoUrl payload
  await tasks.trigger<typeof videoProcessAndUpdate>("video-process-and-update", { videoUrl, id });
  console.log(payload ?? "No name provided");

  return new Response("ok");
});
```

<Note>
  Tasks in the `trigger` folder use Node, so they must stay in there or they will not run,
  especially if you are using a different runtime like Deno. Also do not add "`npm:`" to imports
  inside your task files, for the same reason.
</Note>

### Deploy the Edge Function

Now deploy your new Edge Function with the following command:

```bash  theme={null}
supabase functions deploy video-processing-handler
```

Follow the CLI instructions, selecting the same project you added your `prod` secret key to, and once complete you should see your new Edge Function deployment in your Supabase Edge Functions dashboard.

There will be a link to the dashboard in your terminal output.

## Create the Database Webhook

In your Supabase project dashboard, click 'Project settings' <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" />, then the 'API' tab <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" />, and copy the `anon` `public` API key from the table <Icon icon="circle-3" iconType="solid" size={20} color="A8FF53" />.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-api-key.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7d842b953497f2819e64abd2497e0f25" alt="How to find your Supabase API keys" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-api-key.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=1b09ec34e37b4569f6ffae7b41100bad 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-api-key.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a205e60a3d33fae2ff4f719287df05c4 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-api-key.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c9ba5c95634b152931fab0d43f75778c 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-api-key.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=736ebe39bec4eec64ac11e0ca03e6d09 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-api-key.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6483cb22bbbed8fbaf29d05f5ed50580 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-api-key.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=569ff35cadfacd0d89408e4be2f336b6 2500w" />

Then, go to 'Database' <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" /> click on 'Webhooks' <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" />, and then click 'Create a new hook' <Icon icon="circle-3" iconType="solid" size={20} color="A8FF53" />.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-1.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=b14ffc5195561195ba824430fd5b3566" alt="How to create a new webhook" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-create-webhook-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-1.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f388b147fed1a3e4e68015d4b56e54e5 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-1.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=94e5f71acebb513862c8855c1500e57b 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-1.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=962d9b080e507d5af564fabd6db53f1a 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-1.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=693a3b514e1e1dac9787e78c1bbe7aea 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-1.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=46f027cf03b1b286f375848ee81d7a94 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-1.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=d9af95ddd3d3f6be3ecd08d20ad4604c 2500w" />

<Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" /> Call the hook `edge-function-hook`.

<Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" /> Select the new table you have created:
`public` `video_transcriptions`.

<Icon icon="circle-3" iconType="solid" size={20} color="A8FF53" /> Choose the `insert` event.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-2.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=9e7e86e98234a3bb4a852e7c1f429381" alt="How to create a new webhook 2" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-create-webhook-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-2.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ca6621f024688dd564ad99e0fdb0ffb7 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-2.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=0a13a85ad5879e439acbe6dc8b5310c8 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-2.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=2cd3eec702d6b89fbc3f7864244ff903 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-2.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=062d31b161b8ae0c7e5ecda295da4369 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-2.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3664d62d87ac15550a882d1c223fa9fb 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/supabase-create-webhook-2.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=4a6e4965d3dce81b2f305cc1e265d172 2500w" />

<Icon icon="circle-4" iconType="solid" size={20} color="A8FF53" /> Under 'Webhook configuration', select
'Supabase Edge Functions'{" "}

<Icon icon="circle-5" iconType="solid" size={20} color="A8FF53" /> Under 'Edge Function', choose `POST`
and select the Edge Function you have created: `video-processing-handler`.{" "}

<Icon icon="circle-6" iconType="solid" size={20} color="A8FF53" /> Under 'HTTP Headers', add a new header with the key `Authorization` and the value `Bearer <your-api-key>` (replace `<your-api-key>` with the `anon` `public` API key you copied earlier).

<Info>
  Supabase Edge Functions require a JSON Web Token [JWT](https://supabase.com/docs/guides/auth/jwts)
  in the authorization header. This is to ensure that only authorized users can access your edge
  functions.
</Info>

<Icon icon="circle-7" iconType="solid" size={20} color="A8FF53" /> Click 'Create webhook'.{" "}

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-create-webhook-3.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=ef4b8d91417d1e923063a9f599537f1f" alt="How to create a new webhook 3" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-create-webhook-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-create-webhook-3.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=d1f574a056c46ecca8e8facc2c7f11d3 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-create-webhook-3.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=e141e894768eadb53174d283e8bb7864 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-create-webhook-3.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=c38276204880ba27b452b0a9eccf8696 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-create-webhook-3.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=aa04b198f2fb191a288a4f8b37f02e31 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-create-webhook-3.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=d4dccfa32030a493caecab6383c8a6af 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-create-webhook-3.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=9afd89ffa262e871ee3b1864bbb8b95e 2500w" />

Your Database Webhook is now ready to use.

## Triggering the entire workflow

Your `video-processing-handler` Edge Function is now set up to trigger the `videoProcessAndUpdate` task every time a new row is inserted into your `video_transcriptions` table.

To do this, go back to your Supabase project dashboard, click on 'Table Editor' <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" /> in the left-hand menu, click on the `video_transcriptions` table <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" /> , and then click 'Insert', 'Insert Row' <Icon icon="circle-3" iconType="solid" size={20} color="A8FF53" />.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-3.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=018a4b143a7e610ef85fe630cb5f3942" alt="How to insert a new row 1" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-new-table-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-3.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=fc1cee2d21ace6b3ba5a879a6be235c3 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-3.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=190c3f6352ca9ea4f47dc7122ecf0fc9 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-3.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=20e488fddd2a02db28ef49b3205a3a02 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-3.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=cdab5cdbb858decd062c5e0d8ba4f13c 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-3.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=6dd9a76d09f9a9edd2238ee72b92d98c 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-3.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=cb14e79904fdd5dc076fc3ea24816621 2500w" />

Add a new item under `video_url`, with a public video url. <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" />.

You can use the following public video URL for testing: `https://content.trigger.dev/Supabase%20Edge%20Functions%20Quickstart.mp4`.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-4.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4f12c856f8e921c287e2d3d45c4db397" alt="How to insert a new row 2" data-og-width="3224" width="3224" data-og-height="1824" height="1824" data-path="images/supabase-new-table-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-4.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=c5737feb6cf79dd20606c52f9a3733b0 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-4.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=15aa16b5e45cae5189960db92ca6bec4 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-4.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=f115634df16843b498ac988f966494f8 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-4.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=7733ad6bd8f283a808616182a5a0aee3 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-4.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=13987e360ef986d88a454526b834f227 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-new-table-4.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=d17d016e9c0d2c213839932e56b5d600 2500w" />

Once the new table row has been inserted, check your [cloud.trigger.dev](http://cloud.trigger.dev) project 'Runs' list <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" /> and you should see a processing `videoProcessAndUpdate` task <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" /> which has been triggered when you added a new row with the video url to your `video_transcriptions` table.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-run-result.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=845a8ec72040ad8cdab18b905cf52096" alt="Supabase successful run" data-og-width="3224" width="3224" data-og-height="1824" height="1824" data-path="images/supabase-run-result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-run-result.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4905e76d9f60762b4b91cd41d6964e44 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-run-result.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=e98ab82fe22ea3c04f4907ff673bfbe3 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-run-result.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=559ef31d145b622f9881499b74c628c4 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-run-result.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=003369ca97e1241b1ee739b45def2bf5 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-run-result.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=78039d0ebf7cf5338e0c18846057c191 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-run-result.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=8373b7a03955d029487eee841aa6fdcd 2500w" />

Once the run has completed successfully, go back to your Supabase `video_transcriptions` table, and you should see that in the row containing the original video URL, the transcription has now been added to the `transcription` column.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-table-result.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=9d53cd6ba016677b7a8ad6eea4f9c58e" alt="Supabase successful table update" data-og-width="3224" width="3224" data-og-height="1824" height="1824" data-path="images/supabase-table-result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-table-result.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=1719d1347851ea2f54d620c897e9b057 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-table-result.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=15a9901f3cccbdf20700dec20638744d 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-table-result.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=e900a2cfbfe4544448d048ec34bc107e 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-table-result.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=730b4c94f32134794e13863de70c4e42 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-table-result.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=6b5616e3a599e1a3e4a983d24beaf37a 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-table-result.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=146d83c0d05046987d297578ff5f5124 2500w" />

**Congratulations! You have completed the full workflow from Supabase to Trigger.dev and back again.**

## Learn more about Supabase and Trigger.dev

### Full walkthrough guides from development to deployment

<CardGroup cols={1}>
  <Card title="Edge function hello world guide" icon="book" href="/guides/frameworks/supabase-edge-functions-basic">
    Learn how to trigger a task from a Supabase edge function when a URL is visited.
  </Card>

  <Card title="Database webhooks guide" icon="book" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>

  <Card title="Supabase authentication guide" icon="book" href="/guides/frameworks/supabase-authentication">
    Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role
    keys for admin access.
  </Card>
</CardGroup>

### Task examples with code you can copy and paste

<CardGroup cols={2}>
  <Card title="Supabase database operations" icon="bolt" href="/guides/examples/supabase-database-operations">
    Run basic CRUD operations on a table in a Supabase database using Trigger.dev.
  </Card>

  <Card title="Supabase Storage upload" icon="bolt" href="/guides/examples/supabase-storage-upload">
    Download a video from a URL and upload it to Supabase Storage using S3.
  </Card>
</CardGroup>
