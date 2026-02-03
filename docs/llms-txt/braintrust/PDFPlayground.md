# Source: https://braintrust.dev/docs/cookbook/recipes/PDFPlayground.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using PDF attachments in playgrounds

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/PDFPlayground/PDFPlayground.mdx) by [Carlos Esteban](https://www.linkedin.com/in/cmesteban/), [Ornella Altunyan](https://twitter.com/ornelladotcom) on 2025-05-22</div>

[Logging with attachments](https://braintrust.dev/blog/attachments) allows you to capture user-provided files like images, PDFs, and other documents, but you might also want to leverage these attachments directly within datasets for testing prompts in playgrounds. This cookbook guides you step-by-step through two primary methods—using the paperclip UI button or public URLs—to attach PDFs and quickly iterate on prompts in playgrounds. By the end of this guide, you'll know how to emit spans containing embedded attachments, log prompts into organized spans within a single trace, save these spans into datasets, and seamlessly move them into playgrounds. We'll demonstrate these techniques using earnings report transcripts as illustrative PDF files.

## Getting started

To get started, you'll need [Braintrust](https://www.braintrust.dev/signup) and [OpenAI](https://platform.openai.com/) accounts, along with their corresponding API keys. Plug your OpenAI API key into your Braintrust account's [AI providers](https://www.braintrust.dev/app/settings?subroute=secrets) configuration. You can also add an API key for any other AI provider you'd like, but be sure to change the code to use that model. Lastly, add your `BRAINTRUST_API_KEY` to your `.env.local` file:

```
BRAINTRUST_API_KEY=<your-api-key>
```

To install the necessary dependencies, start by downloading [pnpm](https://pnpm.io/installation) or a package manager of your choice. Then, use the following `package.json` file:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "name": "pdf-attachment-demo",
  "version": "1.0.0",
  "description": "PDF Attachment Demo",
  "scripts": {
    "logging": "ts-node log_pdfs.ts"
  },
  "devDependencies": {
    "@types/node": "^22.15.14",
    "@types/dotenv": "^8.2.0",
    "ts-node": "^10.9.2",
    "typescript": "^5.4.2"
  },
  "dependencies": {
    "dotenv": "^16.1.4",
    "braintrust": "^0.0.201",
    "openai": "^4.97.0"
  }
}
```

And install dependencies by running:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pnpm install
```

To follow along with this cookbook, create a file called `log_pdfs.ts` and add each of the code snippets below to the file as we go through each step. Alternatively, you can download the complete file [on GitHub](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/PDFPlayground/log_pdfs.ts).

## Initializing the logger and OpenAI client

The first thing we'll do is import the modules we need and initialize our OpenAI client. We're wrapping the client so that we have access to Braintrust features.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import {
  initLogger,
  wrapOpenAI,
  wrapTraced,
  currentSpan,
  Attachment,
} from "braintrust";
import { OpenAI } from "openai";
import dotenv from "dotenv";
dotenv.config();

// Braintrust + OpenAI setup
const logger = initLogger({
  projectName: "pdf-attachment-demo",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

const client = wrapOpenAI(
  new OpenAI({
    baseURL: "https://braintrustproxy.com/v1",
    apiKey: process.env.BRAINTRUST_API_KEY,
  }),
);
```

## Defining the PDFs

In this cookbook, we'll use PDFs of various earning calls from public companies. We'll create a list of objects that contain the filenames and their corresponding URLs:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// PDF list with URLs
const pdfFiles = [
  {
    filename: "META-Q4-2024-Earnings-Call-Transcript.pdf",
    url: "https://s21.q4cdn.com/399680738/files/doc_financials/2024/q4/META-Q4-2024-Earnings-Call-Transcript.pdf",
  },
  {
    filename: "Citi-4Q24-Earnings-Transcript.pdf",
    url: "https://www.citigroup.com/rcs/citigpa/storage/public/Earnings/Q42024/4Q24-Earnings-Transcript.pdf",
  },
  {
    filename: "jpmc-4q24-earnings-transcript.pdf",
    url: "https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2024/4th-quarter/4q24-earnings-transcript.pdf",
  },
  {
    filename: "att-4q24-transcript.pdf",
    url: "https://investors.att.com/~/media/Files/A/ATT-IR-V2/financial-reports/quarterly-earnings/2024/4Q24/t-usq-transcript-2025-01-27.pdf",
  },
  {
    filename: "Qualcomm_Q1FY25EC_Transcript_2-5-24.pdf",
    url: "https://s204.q4cdn.com/645488518/files/doc_events/2025/Feb/05/QCOM_Q1FY25EC_Transcript_2-5-24.pdf",
  },
  {
    filename: "host-hotels-4q24-transcript.pdf",
    url: "https://www.hosthotels.com/-/media/HostHotels/Files/DownloadLinksAssets/Earnings-Call-Transcript/Host_Hotels_Resorts_Inc_Earnings_Call_Transcript.pdf",
  },
  {
    filename: "homedepot-4q24-transcript.pdf",
    url: "https://ir.homedepot.com/~/media/Files/H/HomeDepot-IR/documents/hd-4q24-transcript.pdf",
  },
];
```

## Defining the system prompt

Next, we'll define the system prompt that instructs the LLM on how to analyze the PDFs. We want to use specific analysis criteria to make sure we get the desired output:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// System prompt for the assistant
const SYSTEM_PROMPT = `
You are a financial analyst specializing in earnings call analysis. Your task is to provide a quick, bullet-point summary of the key points from earnings call transcripts.

Focus ONLY on these 3-5 key points:
• Revenue and EPS figures vs expectations
• Major business highlights or challenges
• Forward guidance for next quarter

Keep each point to 1-2 sentences maximum. Be extremely concise and focus only on the most important information.
Only output the key points, no other text.
`;
```

## Processing the PDF files

Now, we need to implement a function to handle the PDF processing. This function fetches the PDF file from the URL, converts it to a base64 string, and passes it to the LLM for processing:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// Helper function to process a single PDF
const processPdf = wrapTraced(
  async (pdfFile: { filename: string; url: string }) => {
    console.log(`Processing ${pdfFile.filename}...`);

    // Fetch and encode the PDF file from URL (with error handling)
    let pdfData: Buffer;
    let base64String: string;
    try {
      const response = await fetch(pdfFile.url);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status} ${response.statusText}`);
      }
      const arrayBuffer = await response.arrayBuffer();
      pdfData = Buffer.from(arrayBuffer);
      base64String = pdfData.toString("base64");
    } catch (err: any) {
      console.error(`Failed to download ${pdfFile.url}:`, err);
      return; // Skip this PDF and continue with the next
    }

    const userPrompt = "Please analyze this earnings call transcript";
    const rootSpan = currentSpan();
    rootSpan.setAttributes({ name: pdfFile.filename });
    const rootSpanSlug = currentSpan().export();

    // Create chat completion with file data
    const completion = await client.chat.completions.create({
      model: "gpt-4o",
      messages: [
        {
          role: "system",
          content: SYSTEM_PROMPT,
        },
        {
          role: "user",
          content: [
            {
              type: "file",
              file: {
                filename: pdfFile.filename,
                file_data: `data:application/pdf;base64,${base64String}`,
              },
            },
            {
              type: "text",
              text: userPrompt,
            },
          ],
        },
      ],
      max_tokens: 500,
    });

    const summary = completion.choices[0]?.message?.content;

    // if no summary is generated, log an error and return
    if (!summary) {
      console.warn("No summary generated");
      return;
    }
    // Console log that the summary was created
    console.log(
      `\nEarnings Summary for ${pdfFile.filename}: Summary Created! View in the Braintrust UI!\n`,
    );

    // log the output of the LLM call to the root span
    rootSpan.log({
      output: summary,
    });

    // Log system prompt span
    await logSystemPrompt(pdfFile.filename, pdfFile.url, summary, rootSpanSlug);

    // Log user prompt span
    await logUserPrompt(
      pdfFile.filename,
      pdfFile.url,
      userPrompt,
      summary,
      rootSpanSlug,
      base64String,
    );
  },
  logger,
);
```

## Logging spans

We'll create separate functions to log the system and user spans.

The system prompt span contains the instructions given to the LLM. This function creates a child span related to the root span and captures the system prompt along with the resulting summary:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// Helper function to log system prompt span
async function logSystemPrompt(
  filename: string,
  url: string,
  summary: string,
  rootSpan: Promise<string>,
) {
  const systemSpan = wrapTraced(async () => {
    const span = currentSpan();
    span.setAttributes({
      name: "system_prompt",
      type: "llm",
      parent: (await rootSpan).toString(),
    });

    span.log({
      input: [
        {
          role: "system",
          content: SYSTEM_PROMPT,
        },
      ],
      output: summary,
    });
  }, logger);
  await systemSpan();
}
```

We want to create and log the user prompt span as well, since it includes the actual PDF attachment. We'll reconstruct the PDF data from the base64 string and attach it to the span, which will make it available for use in the playground:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// Helper function to log user prompt span
async function logUserPrompt(
  filename: string,
  url: string,
  userPrompt: string,
  summary: string,
  rootSpan: Promise<string>,
  base64String: string,
) {
  const userPromptSpan = wrapTraced(async () => {
    const span = currentSpan();
    span.setAttributes({
      name: "user_prompt",
      type: "llm",
      parent: (await rootSpan).toString(),
    });

    // Reconstruct PDF data from base64
    const pdfData = Buffer.from(base64String, "base64");

    const attachment = new Attachment({
      data: pdfData,
      filename,
      contentType: "application/pdf",
    });

    span.log({
      input: [{ role: "user", content: userPrompt }],
      output: summary,
      metadata: {
        filename,
        url,
        base64String,
        attachment,
      },
    });
  }, logger);
  await userPromptSpan();
}
```

## Executing the main process

Finally, we create and execute the main function that processes all the PDFs in our list. This function loops through each PDF file, processes it individually, and handles any errors that may occur:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// Main function to process all PDFs
const generateSummary = async () => {
  console.log(`Found ${pdfFiles.length} PDFs to process`);

  try {
    for (const pdfFile of pdfFiles) {
      await processPdf(pdfFile);
    }
  } catch (err: any) {
    console.error("Error in main:", err);
    if (err?.response?.data) {
      console.error("Response data:", err.response.data);
    }
  }
};

generateSummary();
```

## Running your file

To execute the script, you can run one of the following commands, depending on how you've set up your environment. If you used the provided `package.json` file and named your file `log_pdfs.ts`, you can run:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pnpm logging
```

You can also use this command with your file name:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pnpm ts-node {file_name}
```

## Using the Braintrust UI

Once your traces have been logged, you can use the Braintrust UI to manage your spans and experiment with different prompts.

### Creating a dataset

You can store the user spans from your PDF traces into a dataset. Select the span, and then select **Add span to dataset**, or use the hotkey `D` to speed this up.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PDFPlayground/add-span-to-dataset.gif?s=b3b87dab557d81b84d4b7431b26cbf27" alt="add span to dataset" data-og-width="2000" width="2000" data-og-height="1241" height="1241" data-path="cookbook/assets/PDFPlayground/add-span-to-dataset.gif" data-optimize="true" data-opv="3" />

### Trying system prompts in a playground

Select a system prompt span, and then select **Try prompt** to:

1. Save the prompt (for example, "system1") to your library by selecting **Save as custom prompt**
2. Launch a playground using the saved prompt by selecting **Create playground with prompt**

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PDFPlayground/try-prompt.gif?s=68daecbe770415e38792d3f98e5180c2" alt="try prompt from span" data-og-width="2000" width="2000" data-og-height="1243" height="1243" data-path="cookbook/assets/PDFPlayground/try-prompt.gif" data-optimize="true" data-opv="3" />

### File attachment methods

There are two ways to attach PDF files in playgrounds: using the paperclip button in the UI, or specifying a public URL. Let's walk through each method:

* To upload files directly from your local machine, start by selecting **+ Message** to add a user prompt. Then, select **+ Message Part** > **File**. This will display a paperclip icon on the right side. Select it to upload a file from your local machine.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PDFPlayground/paperclip.gif?s=203759a999ec1c72c927ccb7c93b8e54" alt="paperclip UI method" data-og-width="2000" width="2000" data-og-height="1214" height="1214" data-path="cookbook/assets/PDFPlayground/paperclip.gif" data-optimize="true" data-opv="3" />

This method is particularly useful when you're working with local files that aren't accessible via public URL.

* To use the public URL method, paste the URL directly into the file message input field. You can also use mustache syntax to extract the URL from metadata.

This method streamlines the process when you're working with publicly available PDFs, like the earnings call transcripts we're using in this cookbook.

Both methods result in the PDF being attached to your prompt, allowing the LLM to analyze its contents. Choose the approach that best fits your workflow based on where your files are stored.

## Next steps

Now that you understand the process of converting spans with PDF attachments into a dataset and executing the PDFs in the playground, you can:

* Learn more about [multimodal prompts in playgrounds](/evaluate/playgrounds#multimodal-prompts)
* Read more about [logging with attachments](https://braintrust.dev/blog/attachments)
