# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/sdk-jsts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript/TypeScript SDK

<Note>
  The following information applies to the legacy Unstructured Partition Endpoint.

  Unstructured recommends that you use the
  [on-demand jobs](/api-reference/workflow/overview#run-an-on-demand-job) functionality in the
  [Unstructured API](/api-reference/overview) instead. Unstructured's on-demand jobs provide
  many benefits over the legacy Unstructured Partition Endpoint, including support for:

  * Production-level usage.
  * Multiple local input files in batches.
  * The latest and highest-performing models.
  * Post-transform enrichments.
  * All of Unstructured's chunking strategies.
  * The generation of vector embeddings.

  The Unstructured API also provides support for processing files and data in remote locations.
</Note>

The [Unstructured JavaScript/TypeScript SDK](https://github.com/Unstructured-IO/unstructured-js-client) client allows you to send one file at a time for processing by the Unstructured Partition Endpoint.

To use the JavaScript/TypeScript SDK, you'll first need to set an environment variable named `UNSTRUCTURED_API_KEY`,
representing your Unstructured API key. To get your API key, do the following:

1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
   After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
   </Note>

2. If you have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
     or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
   </Note>

3. Get your Unstructured API key:<br />

   a. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

   <Note>
     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).
   </Note>

   b. Click **Generate API Key**.<br />
   c. Follow the on-screen instructions to finish generating the key.<br />
   d. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

## Installation

Before using the SDK to interact with Unstructured, install the library:

<CodeGroup>
  ```bash JavaScript/TypeScript theme={null}
  npm install unstructured-client
  ```
</CodeGroup>

<Note>
  The SDK uses semantic versioning and major bumps could bring breaking changes. It is advised to
  pin your installed version.
</Note>

## Basics

Let's start with a simple example in which you send a PDF document to the Unstructured Partition Endpoint to be partitioned by Unstructured.

<Warning>
  The JavaScript/TypeScript SDK has the following breaking changes in v0.11.0:

  * Imports under the `dist` path have moved up a level
  * Enums are now used for parameters with a set of options
    * This includes `chunkingStrategy`, `outputFormat`, and `strategy`
  * All parameters to `partition` have moved to a `partitionParameters` object
</Warning>

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { UnstructuredClient } from "unstructured-client";
  import { PartitionResponse } from "unstructured-client/sdk/models/operations";
  import { Strategy } from "unstructured-client/sdk/models/shared";
  import * as fs from "fs";

  const key = process.env.UNSTRUCTURED_API_KEY;
  const url = process.env.UNSTRUCTURED_API_URL;

  const client = new UnstructuredClient({
      serverURL: url,
      security: {
          apiKeyAuth: key,
      },
  });

  const filename = "PATH_TO_INPUT_FILE";
  const data = fs.readFileSync(filename);

  client.general.partition({
      partitionParameters: {
          files: {
              content: data,
              fileName: filename,
          },
          strategy: Strategy.HiRes,
          splitPdfPage: true,
          splitPdfAllowFailed: true,
          splitPdfConcurrencyLevel: 15
          languages: ['eng']
      }
  }).then((res: PartitionResponse) => {
      if (res.statusCode == 200) {
          // Print the processed data's first element only.
          console.log(res.elements?.[0])

          // Write the processed data to a local file.
          const jsonElements = JSON.stringify(res, null, 2)

          fs.writeFileSync("PATH_TO_OUTPUT_FILE", jsonElements)
      }
  }).catch((e) => {
      if (e.statusCode) {
        console.log(e.statusCode);
        console.log(e.body);
      } else {
        console.log(e);
      }
  });
  ```

  ```typescript TypeScript (SDK <=v0.10.6) theme={null}
  import { UnstructuredClient } from "unstructured-client";
  import { PartitionResponse } from "unstructured-client/dist/sdk/models/operations";
  import * as fs from "fs";

  const key = process.env.UNSTRUCTURED_API_KEY;
  const url = process.env.UNSTRUCTURED_API_URL;

  const client = new UnstructuredClient({
      serverURL: url,
      security: {
          apiKeyAuth: key,
      },
  });

  const filename = "PATH_TO_FILE";
  const data = fs.readFileSync(filename);

  client.general.partition({
      files: {
          content: data,
          fileName: filename,
      },
      strategy: 'hi_res',
      languages: ['eng']
  }).then((res: PartitionResponse) => {
      if (res.statusCode == 200) {
          console.log(res.elements?.[0]);
      }
  }).catch((e) => {
    if (e.statusCode) {
      console.log(e.statusCode);
      console.log(e.body);
    } else {
      console.log(e);
    }
  });
  ```
</CodeGroup>

For a code example that works with an entire directory of files instead of just a single PDF, see the [Processing multiple files](#processing-multiple-files) section.

## Page splitting

In order to speed up processing of large PDF files, the `splitPdfPage`[\*](#parameter-names) parameter is `true` by default. This
causes the PDF to be split into small batches of pages before sending requests to the API. The client
awaits all parallel requests and combines the responses into a single response object. This is specific to PDF files and other
filetypes are ignored.

The number of parallel requests is controlled by `splitPdfConcurrencyLevel`[\*](#parameter-names).
The default is 8 and the max is set to 15 to avoid high resource usage and costs.

If at least one request is successful, the responses are combined into a single response object. An
error is returned only if all requests failed or there was an error during splitting.

<Note>
  This feature may lead to unexpected results when chunking because the server does not see the entire
  document context at once. If you'd like to chunk across the whole document and still get the speedup from
  parallel processing, you can:

  * Partition the PDF with `splitPdfPage` set to `true`, without any chunking parameters.
  * Store the returned elements in `results.json`.
  * Partition this JSON file with the desired chunking parameters.
</Note>

```typescript TypeScript theme={null}
client.general.partition({
    partitionParameters: {
        files: {
            content: data,
            fileName: filename,
        },
        strategy: Strategy.HiRes,
        // Set to `false` to disable PDF splitting
        splitPdfPage: true,
        // Continue PDF splitting even if some earlier split operations fail.
        splitPdfAllowFailed: true,
        // Modify splitPdfConcurrencyLevel to set the number of parallel requests
        splitPdfConcurrencyLevel: 10,
    }
})
```

## Customizing the client

### Retries

You can also change the defaults for retries through the `retryConfig`[\*](#parameter-names)
when initializing the client. If a request to the API fails, the client will retry the
request with an exponential backoff strategy up to a maximum interval of one minute. The
function keeps retrying until the total elapsed time exceeds `maxElapsedTime`[\*](#parameter-names),
which defaults to one hour:

```typescript TypeScript theme={null}
const key = process.env.UNSTRUCTURED_API_KEY;
const url = process.env.UNSTRUCTURED_API_URL;    

const client = new UnstructuredClient({
    security: { apiKeyAuth: key },
    serverURL: url,
    retryConfig: {
        strategy: "backoff",
        retryConnectionErrors: true,
        backoff: {
            initialInterval: 500,
            maxInterval: 60000,
            exponent: 1.5,
            maxElapsedTime: 900000, // 15min*60sec*1000ms = 15 minutes
        },
    };
});
```

## Processing multiple files

The code example in the [Basics](#basics) section processes a single PDF file. But what if you want to process
multiple files inside a directory with a mixture of subdirectories and files with different file types?

The following example takes an input directory path to read files from and an output directory path to
write the processed data to, processing one file at a time.

```typescript TypeScript theme={null}
import { UnstructuredClient } from "unstructured-client";
import * as fs from "fs";
import * as path from "path";
import { Strategy } from "unstructured-client/sdk/models/shared/index.js";
import { PartitionResponse } from "unstructured-client/sdk/models/operations";

// Send all files in the source path to Unstructured for processing.
// Send the processed data to the destination path.
function processFiles(
    client: UnstructuredClient,
    sourcePath: string,
    destinationPath: string
): void {

    // If an output directory does not exist for the corresponding input
    // directory, then create it.
    if (!fs.existsSync(destinationPath)) {
        fs.mkdirSync(destinationPath, { recursive: true });
    }

    // Get all folders and files at the current level of the input directory.
    const items = fs.readdirSync(sourcePath);

    // For each folder and file in the input directory...
    for (const item of items) {
        const inputPath = path.join(sourcePath, item);
        const outputPath = path.join(destinationPath, item)

        // If it's a folder, call this function recursively.
        if (fs.statSync(inputPath).isDirectory()) {
            processFiles(client, inputPath, outputPath);
        } else {
            // If it's a file, send it to Unstructured for processing.
            const data = fs.readFileSync(inputPath);

            client.general.partition({
                partitionParameters: {
                    files: {
                        content: data,
                        fileName: inputPath
                    },
                    strategy: Strategy.HiRes,
                    splitPdfPage: true,
                    splitPdfConcurrencyLevel: 15,
                    splitPdfAllowFailed: true
                }
            }).then((res: PartitionResponse) => {
                // If successfully processed, write the processed data to
                // the destination directory.
                if (res.statusCode == 200) {
                    const jsonElements = JSON.stringify(res, null, 2)
                    fs.writeFileSync(outputPath + ".json", jsonElements)
                }
            }).catch((e) => {
                if (e.statusCode) {
                    console.log(e.statusCode);
                    console.log(e.body);
                } else {
                    console.log(e);
                }
            });
        }
    }
}

const client = new UnstructuredClient({
    security: { apiKeyAuth: process.env.UNSTRUCTURED_API_KEY },
    serverURL: process.env.UNSTRUCTURED_API_URL
});

processFiles(
    client,
    process.env.LOCAL_FILE_INPUT_DIR,
    process.env.LOCAL_FILE_OUTPUT_DIR
);
```

## Parameters & examples

The parameter names used in this document are for the JavaScript/TypeScript SDK, which follows the `camelCase`
convention. The Python SDK follows the `snake_case` convention. Other than this difference in naming convention,
the names used in the SDKs are the same across all methods.

* Refer to the [API parameters](/api-reference/legacy-api/partition/api-parameters) page for the full list of available parameters.
* Refer to the [Examples](/api-reference/legacy-api/partition/examples) page for some inspiration on using the parameters.
