Source: https://docs.slack.dev/tools/deno-slack-sdk/tutorials/workflows-with-ai-integrations

# Design Slack workflows with AI integrations

This tutorial teaches you how to harness generative AI to automate customer email responses within Slack. The goal is to improve response efficiency by leveraging AI to draft email responses and enable human review and approval before sending.

How the workflow operates:

1. **Receive an email in Slack:** Emails sent to a dedicated Slack channel trigger a workflow, automatically forwarding customer inquiries to Slack.
2. **Notify User & Generate Response:** The workflow posts a notification to Slack, informing the user that the system is generating a response. At the same time, it sends the email’s content to the AI to create a draft response.
3. **AI Drafts Response:** The AI generates a response and posts it back in the same Slack thread. The user can edit and finalize the response directly within Slack before sending it to the customer.

## Project setup {#project-setup}

Before diving into code, it’s essential to understand the components at play. We are using the [Slack CLI](/tools/slack-cli) and [Deno Slack SDK](/tools/deno-slack-sdk) to create an app that listens to Slack events and reacts accordingly. The AI integration will use external API calls (e.g., OpenAI) to process customer emails and return responses.

At this point you should be familiar with the Slack CLI and how it works. If this is new for you we recommend starting with the [Hello world app](/tools/deno-slack-sdk/tutorials/hello-world-app) first.

### Create a new Slack project {#create-a-new-slack-project}

Open your terminal and navigate to a directory where you have permission to create files. Use the following command to scaffold a new Slack project then change into the project directory:

```text
slack create my-app --template slack-samples/deno-blank-templatecd my-app
```

Open your project in VS Code.

```text
code .
```

### Set up OpenAI keys {#set-up-openai-keys}

Generative AI services (like OpenAI and Anthropic) require an API key to authenticate requests. Let’s get set up with OpenAI.

If you haven't already, create an account on OpenAI's platform. After signing in, go to the API settings page and generate an API key.

* Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
* Click **API Keys**
* Click **\+ Create Key**

Copy the key's value, then go back to VS Code. Create a file in the project called `.env` and put your API key there, assigned to a variable like this:

```html
OPENAI_API_KEY=<your_API_key>
```

Save the file.

Before we add any code to the project, we also need to let the app know where to find the OpenAI dependency. Open the `deno.jsonc` file of the project and add this line to it in the `imports` section:

```text
"openai/": "https://deno.land/x/openai@v4.20.1/"
```

### Prepare your Slack channel {#prepare-your-slack-channel}

Slack allows you to forward emails into channels, and we’ll use this to simulate customer inquiries.

1. Create a Slack channel: In your testing workspace, create a new channel specifically for customer emails, e.g., #customer-support.
2. Set up email forwarding: In the Slack sidebar, right-click on your test channel name and go to **View channel details**, then head to the **Integrations** tab. Click on **Send emails to this channel** and generate a new channel email. This is where we'll forward customer inquiries.

## Implement code {#implement-code}

In this section, we'll create the necessary project files.

### Configure the event trigger {#configure-the-event-trigger}

Back in VS Code, create a folder in your project called `triggers`, then add a file to it named `email_trigger.ts`. Copy and paste this code into the file, then save it.

```python
import { Trigger } from "deno-slack-sdk/types.ts";import { TriggerEventTypes, TriggerTypes } from "deno-slack-api/mod.ts";import EmailWorkflow from "../workflows/email_workflow.ts";const emailTrigger: Trigger<typeof EmailWorkflow.definition> = {  type: TriggerTypes.Event,  name: "Email message trigger",  description:    "A email trigger, responds only to emails being sent via a channel email",  workflow: `#/workflows/${EmailWorkflow.definition.callback_id}`,  event: {    event_type: TriggerEventTypes.MessagePosted,    channel_ids: ["C000000000"], // TODO: Must set this to an internal channel    filter: {      version: 1,      root: {        statement: "{{data.user_id}} == USLACKBOT", // Messages that come in via a channel e-mail have this as their user      },    },  },  inputs: {    message_ts: {      value: "{{data.message_ts}}",    },    channel_id: {      value: "{{data.channel_id}}",    },  },};export default emailTrigger;
```

Triggers come in a variety of forms in Slack workflows, such as message events, shortcuts, or scheduled events. For this use case, we’ll focus on an event trigger—specifically, a message event trigger. However, we don’t want every message in the channel to trigger our workflow, as that would quickly become overwhelming. Instead, we’ll filter the trigger to respond only to messages from `USLACKBOT`. Here’s what this means in practice:

* The trigger will activate only when a message is sent by `USLACKBOT`, ensuring that only email-based messages kick off the workflow.
* Inside the trigger event, we will extract some key inputs, including the `message_ts` (timestamp of the message) and `channel_id`. These values will be used in later steps when interacting with Slack messages (e.g., replying in a thread).

We’re going to set the channel that we want to listen on by setting the `channel_ids` parameter. Follow these steps to get that channel ID.

1. Right-click on your test channel name in the sidebar.
2. Click on **View channel details**.
3. At the bottom of the modal, notice the channel ID. Copy the channel ID.
4. Paste this value in the `channel_ids` parameter within your `email_trigger.ts` file.

### Create the EmailWorkflow {#create-the-emailworkflow}

Once the trigger is tripped, it’ll set a particular workflow into motion. Create another folder in your project, this one called `workflows`, then add a file to it. Name this file `email_workflow.ts`, copy and paste the following code in it, then save it.

```python
import { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { EmailListenerFunction } from "../functions/email_listener_function.ts";const EmailWorkflow = DefineWorkflow({  callback_id: "email_workflow",  title: "Email workflow",  description: "Workflow listens for emails and creates responses to them",  input_parameters: {    properties: {      message_ts: {        type: Schema.types.string,      },      channel_id: {        type: Schema.types.string,      },    },    required: ["message_ts", "channel_id"],  },});EmailWorkflow.addStep(EmailListenerFunction, {  message_ts: EmailWorkflow.inputs.message_ts,  channel_id: EmailWorkflow.inputs.channel_id,});export default EmailWorkflow;
```

You will see that it’s workflow containing only one step. The majority of the functionality will be housed in a function file.

Triggers can offer context that we can use in the following steps of our workflow. Note that we are passing in the variables from the trigger to the function (`message_ts` and `channel_id`).

### Create the email listener function {#create-the-email-listener-function}

Create a folder in your project, named `functions`, then add a new file to it named it `email_listener_function.ts`. Here we will implement the code for the `EmailListenerFunction` we added as a step in the workflow in the previous section. Copy and paste this code in the new `email_listener_function.ts` file and save it.

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import OpenAI from "openai/mod.ts";import { TriggerEventTypes, TriggerTypes } from "deno-slack-api/mod.ts";import ThreadWorkflow from "../workflows/thread_workflow.ts";export const EmailListenerFunction = DefineFunction({  callback_id: "email_listener_function",  title: "Email Listener Function",  description:    "A function that listens for email on a particular channel and uses AI to generate a response",  source_file: "functions/email_listener_function.ts",  input_parameters: {    properties: {      message_ts: {        type: Schema.types.string,        description: "The timestamp of the email message.",      },      channel_id: {        type: Schema.types.string,        description: "The channel that the email was posted.",      },    },    required: ["message_ts", "channel_id"],  },});export default SlackFunction(  EmailListenerFunction,  async ({ client, inputs, env }) => {    // 1. Send a message in thread to the e-mail message,    //    confirming that the AI model is "thinking"    const ackResponse = await client.chat.postMessage({      channel: inputs.channel_id,      thread_ts: inputs.message_ts,      text:        "Just a moment while I think of a response :hourglass_flowing_sand:",    });    if (!ackResponse.ok) {      console.error(ackResponse.error);    }    // 2. Send email contents to AI model and generate a response for us    // Since the event doesn't contain the file itself, must call    // `conversations.history` to get that info    const historyResponse = await client.conversations.history({      channel: inputs.channel_id,      oldest: inputs.message_ts,      inclusive: true,      limit: 1,    });    if (!historyResponse.ok) {      console.error(historyResponse.error);    }    const email_text = historyResponse.messages[0].files[0].plain_text;    const openai = new OpenAI({      apiKey: env.OPENAI_API_KEY,    });    const chatCompletion = await openai.chat.completions.create({      messages: [        {          "role": "system",          "content":            `You are a helpful assistant. Please write a response to the following email in 100 words:`,        },        { "role": "user", "content": `${email_text}` },      ],      model: "gpt-3.5-turbo",    });    const completionContent = chatCompletion.choices[0].message.content;    // 3. Update the "thinking" message to the AI model's response    const updateResponse = await client.chat.update({      channel: inputs.channel_id,      ts: ackResponse.ts,      text: `${completionContent}`,      mrkdwn: true,    });    if (!updateResponse.ok) {      console.log(updateResponse.error);    }    // 4. Create trigger to listen for new messages on the email message thread    const authResponse = await client.auth.test();    const botId = authResponse.user_id;    const triggerResponse = await client.workflows.triggers.create({      type: TriggerTypes.Event,      name: `Thread Listener response for ts: ${inputs.message_ts}`,      description: "Listens on the thread for the message in the name",      workflow: `#/workflows/${ThreadWorkflow.definition.callback_id}`,      event: {        event_type: TriggerEventTypes.MessagePosted,        channel_ids: [`${inputs.channel_id}`],        filter: {          version: 1,          root: {            operator: "AND",            inputs: [{              statement: `{{data.thread_ts}} == ${inputs.message_ts}`,            }, {              operator: "NOT",              inputs: [{                statement: `{{data.user_id}} == ${botId}`,              }],            }],          },        },      },      inputs: {        thread_ts: {          value: inputs.message_ts,        },        channel_id: {          value: "{{data.channel_id}}",        },        bot_id: {          value: botId,        },      },    });    if (!triggerResponse.ok) {      console.error(triggerResponse.error);    }    return {      outputs: {},    };  },);
```

In this file, we use one of the most popular Slack Web API methods, [`chat.postMessage`](/reference/methods/chat.postMessage), to send a message to a Slack channel. To do this, we utilize the `client` object available within the function definition. In this case, we send a short message to inform the user that our workflow has started and we’re waiting for a response, as seen noted in step 1 in the code comments.

```text
    // 1. Send a message in thread to the e-mail message,    //    confirming that the AI model is "thinking"    const ackResponse = await client.chat.postMessage({      channel: inputs.channel_id,      thread_ts: inputs.message_ts,      text:        "Just a moment while I think of a response :hourglass_flowing_sand:",    });    if (!ackResponse.ok) {      console.error(ackResponse.error);    }
```

This sends a message letting the user know that something is happening while they wait. Next comes the exciting part: we send the contents of the email to our AI model and wait for its response. There are a few key steps to achieve this. Since the message event itself doesn’t contain file data (as that would be too large), we need to call the [`conversations.history`](/reference/methods/conversations.history) API method to retrieve the message and extract its content.

After getting the email content, we send it to our AI model and follow the model’s method to process the information and retrieve the response.

```text
    // 2. Send email contents to AI model and generate a response for us    // Since the event doesn't contain the file itself, must call    // `conversations.history` to get that info    const historyResponse = await client.conversations.history({      channel: inputs.channel_id,      oldest: inputs.message_ts,      inclusive: true,      limit: 1,    });    if (!historyResponse.ok) {      console.error(historyResponse.error);    }    const email_text = historyResponse.messages[0].files[0].plain_text;    const openai = new OpenAI({      apiKey: env.OPENAI_API_KEY,    });    const chatCompletion = await openai.chat.completions.create({      messages: [        {          "role": "system",          "content":            `You are a helpful assistant. Please write a response to the following email in 100 words:`,        },        { "role": "user", "content": `${email_text}` },      ],      model: "gpt-3.5-turbo",    });    const completionContent = chatCompletion.choices[0].message.content;
```

Next, we post the AI’s response back to Slack so the user can see it! We update the initial “thinking” message by using the [`chat.update`](/reference/methods/chat.update) API method, ensuring we reference the same timestamp (`ts`) as the original message.

```javascript
    // 3. Update the "thinking" message to the AI model's response    const updateResponse = await client.chat.update({      channel: inputs.channel_id,      ts: ackResponse.ts,      text: `${completionContent}`,      mrkdwn: true,    });    if (!updateResponse.ok) {      console.log(updateResponse.error);    }
```

With that, we’ve completed the first part of our workflow!

Next, we set up a listener for replies in the message thread. While this isn’t strictly necessary, it helps make the app feel more cohesive. To achieve this, we’ll recreate the earlier logic but make it work specifically for listening to thread messages posted by users (not by the bot itself). To prevent the bot from triggering its own workflow and causing an endless loop, we use the [`auth.test`](/reference/methods/auth.test) API method to retrieve the bot’s user ID.

Using the `triggers.create` method, we can define all the necessary parameters, making sure to filter out the bot’s own messages and only trigger the workflow for user replies within the thread.

```javascript
    // 4. Create trigger to listen for new messages on the email message thread    const authResponse = await client.auth.test();    const botId = authResponse.user_id;    const triggerResponse = await client.workflows.triggers.create({      type: TriggerTypes.Event,      name: `Thread Listener response for ts: ${inputs.message_ts}`,      description: "Listens on the thread for the message in the name",      workflow: `#/workflows/${ThreadWorkflow.definition.callback_id}`,      event: {        event_type: TriggerEventTypes.MessagePosted,        channel_ids: [`${inputs.channel_id}`],        filter: {          version: 1,          root: {            operator: "AND",            inputs: [{              statement: `{{data.thread_ts}} == ${inputs.message_ts}`,            }, {              operator: "NOT",              inputs: [{                statement: `{{data.user_id}} == ${botId}`,              }],            }],          },        },      },      inputs: {        thread_ts: {          value: inputs.message_ts,        },        channel_id: {          value: "{{data.channel_id}}",        },        bot_id: {          value: botId,        },      },    });    if (!triggerResponse.ok) {      console.error(triggerResponse.error);    }    return {      outputs: {},    };  },);
```

The trigger we create trips another workflow, the `ThreadWorkflow`, so let's create that now.

### Create the ThreadWorkflow {#create-the-threadworkflow}

Create a new file within the `workflows` folder and name it `thread_workflow.ts`. Copy and paste the following code into it and save.

```python
import { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { ListenerDefinition } from "../functions/thread_listener_function.ts";const ThreadWorkflow = DefineWorkflow({  callback_id: "thread_workflow",  title: "Thread workflow",  description:    "A workflow that listens for messages on a thread and responds with AI.",  input_parameters: {    properties: {      thread_ts: {        type: Schema.types.string,      },      channel_id: {        type: Schema.types.string,      },      bot_id: {        type: Schema.types.string,      },    },    required: ["thread_ts", "channel_id", "bot_id"],  },});ThreadWorkflow.addStep(ListenerDefinition, {  thread_ts: ThreadWorkflow.inputs.thread_ts,  channel_id: ThreadWorkflow.inputs.channel_id,  bot_id: ThreadWorkflow.inputs.bot_id,});export default ThreadWorkflow;
```

Here we have another short workflow, also with one step. Note that we use the `thread_ts`, `channel_id`, and `bot_id`, passed in from the trigger. Next, we create the `ListenerDefinition`.

### Create the thread listener function {#create-the-thread-listener-function}

Finally, let’s take a look at the second function. Create a new file within the `functions` folder of your project and name it `thread_listener_function.ts`. This function is similar to what we just covered, but the methods are adjusted to work with thread messages instead of channel messages. Copy and paste the code below into the new file then save it.

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import OpenAI from "openai/mod.ts";import { ChatCompletionMessageParam } from "openai/resources/mod.ts";export const ListenerDefinition = DefineFunction({  callback_id: "listener_function",  title: "listener text using AI",  description:    "A function that listens on a thread, pulls in the contents and uses AI to respond.",  source_file: "functions/thread_listener_function.ts",  input_parameters: {    properties: {      bot_id: {        type: Schema.types.string,        description: "User ID of the bot",      },      thread_ts: {        type: Schema.types.string,        description: "The thread timestamp",      },      channel_id: {        type: Schema.types.string,        description: "The channel Id",      },    },    required: ["thread_ts", "channel_id", "bot_id"],  },});export default SlackFunction(  ListenerDefinition,  async ({ client, inputs, env }) => {    // 1. Acknowledge user input and response with "thinking" message    const ackResponse = await client.chat.postMessage({      channel: inputs.channel_id,      thread_ts: inputs.thread_ts,      text:        "Just a moment while I think of a response :hourglass_flowing_sand:",    });    console.log(ackResponse);    if (!ackResponse.ok) {      console.error(ackResponse.error);    }    // 2. Get message contents by pulling in all conversations in the thread    //    and feed contents to AI model    const conversationResponse = await client.conversations.replies({      channel: inputs.channel_id,      ts: inputs.thread_ts,    });    if (!conversationResponse.ok) {      console.error(conversationResponse.error);    }    const openai = new OpenAI({      apiKey: env.OPENAI_API_KEY,    });    let messages: ChatCompletionMessageParam[] = [      {        "role": "system",        "content": `You are a helpful assistant.`,      },    ];    for (let i = 1; i < conversationResponse.messages.length; i++) { // Start at 1, the first message is the file      if (conversationResponse.messages[i] != inputs.bot_id) {        messages.push({          "role": "user",          "content": `${conversationResponse.messages[i].text}`,        });      } else {        messages.push({          "role": "assistant",          "content": `${conversationResponse.messages[i].text}`,        });      }    }    const chatCompletion = await openai.chat.completions.create({      messages: messages,      model: "gpt-3.5-turbo",    });    // 3. Update "thinking" message with AI model contents    const completionContent = chatCompletion.choices[0].message.content;    const updateResponse = await client.chat.update({      channel: inputs.channel_id,      ts: ackResponse.ts,      text: `${completionContent}`,      mrkdwn: true,    });    if (!updateResponse.ok) {      console.log(updateResponse.error);    }    return {      outputs: {},    };  },);
```

## Update the manifest {#update-the-manifest}

Before we can run the app, we have to ensure that all objects we've created for the app are reflected in the app manifest. Open the `manifest.ts` file and replace its contents with the following:

```python
import { Manifest } from "deno-slack-sdk/mod.ts";import { EmailListenerFunction } from "./functions/email_listener_function.ts";import { ListenerDefinition } from "./functions/thread_listener.ts";import EmailWorkflow from "./workflows/email_workflow.ts";import ThreadWorkflow from "./workflows/thread_workflow.ts";export default Manifest({  name: "email-response-generator",  description:    "An app that creates responses to emails automatically within a thread.",  icon: "assets/robot-emoji.png",  workflows: [EmailWorkflow, ThreadWorkflow],  outgoingDomains: ["api.openai.com"],  functions: [    EmailListenerFunction,    ListenerDefinition  ],  datastores: [],  botScopes: [    "commands",    "chat:write",    "chat:write.public",    "channels:history",    "triggers:write",    "reactions:read",  ],});
```

## Run the app locally and test {#run-the-app-locally-and-test}

Let’s run the workflow locally. Navigate back to your terminal and run the `slack run` command. Once the app is up and running, important logs will appear to let us know what’s happening with the app, such as which functions were executed and whether they succeeded.

A helpful feature of this setup is that whenever you update your project code, the app is automatically reinstalled and updated. This means you can see code changes reflected in your app immediately, without the need to restart any development server.

Next, invite your app to your channel. Your app cannot read events from a channel unless it’s actually in the channel, so invite your bot to the testing channel by typing `/invite` into the message composer and then selecting the name of your app. After that, test your setup by sending an email to the channel email address you created earlier.

## Deploy and uninstall {#deploy-and-uninstall}

If you want to use your app without needing to run it from your local machine, you’d need to deploy your app.

Run the `slack deploy` command in your terminal. This will package your app, and make your functions available in Slack at any time.

Once your app is deployed, you can remove the local version. To uninstall, run the `slack delete` command in your project’s root directory. You’ll be prompted to choose whether you want to remove the local version or the deployed version.
