# Source: https://braintrust.dev/docs/guides/attachments.md

# Attachments

You can log arbitrary binary data, like images, audio, video, PDFs, and large JSON objects, as attachments.
Attachments are useful for building multimodal evaluations, handling large data structures, and can enable advanced scenarios like summarizing visual content or analyzing document metadata.

## Upload attachments

You can upload attachments from either your code or the UI. Your files are securely stored in an object store and associated with the uploading user’s organization. Only you can access your attachments.

### Via code

To upload an attachment, create a new `Attachment` object to represent the file path or in-memory buffer that you want to upload:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Attachment, initLogger } from "braintrust";

  const logger = initLogger();

  logger.log({
    input: {
      question: "What is this?",
      context: new Attachment({
        data: "path/to/input_image.jpg",
        filename: "user_input.jpg",
        contentType: "image/jpeg",
      }),
    },
    output: "Example response.",
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import Attachment, init_logger

  logger = init_logger()

  logger.log(
      {
          "input": {
              "question": "What is this?",
              "context": Attachment(
                  data="path/to/input_image.jpg",
                  filename="user_input.jpg",
                  content_type="image/jpeg",
              ),
          },
          "output": "Example response.",
      }
  )
  ```
</CodeGroup>

You can place the `Attachment` anywhere in a log, dataset, or feedback log.

Behind the scenes, the Braintrust SDK automatically detects and uploads attachments in the background, in parallel to the original logs. This ensures that the latency of your logs isn't affected by any additional processing.

### Use external files as attachments

<Note>
  The `ExternalAttachment` feature is supported only in [self-hosted deployments](https://www.braintrust.dev/docs/guides/self-hosting). It is not supported in Braintrust-hosted environments.
</Note>

Braintrust also supports references to files in external object stores with the `ExternalAttachment` object. You can use this anywhere you would use an `Attachment`. Currently S3 is the only supported option for external files.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { ExternalAttachment, initLogger } from "braintrust";

  const logger = initLogger({ projectName: "ExternalAttachment Example" });

  logger.log({
    input: {
      question: "What is this?",
      additional_context: new ExternalAttachment({
        url: "s3://an_existing_bucket/path/to/file.pdf",
        filename: "file.pdf",
        contentType: "application/pdf",
      }),
    },
    output: "Example response.",
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import ExternalAttachment, init_logger

  logger = init_logger("ExternalAttachment Example")

  logger.log(
      input={
          "question": "What is this?",
          "additional_context": ExternalAttachment(
              url="s3://an_existing_bucket/path/to/file.pdf",
              filename="file.pdf",
              content_type="application/pdf",
          ),
      },
      output="Example response.",
  )
  ```
</CodeGroup>

Just like attachments uploaded to Braintrust, external attachments can be previewed and downloaded for local viewing.

### JSON attachments

For large JSON objects that would bloat your trace size, you can use `JSONAttachment`. This is particularly useful for:

* Lengthy conversation transcripts
* Extensive document collections or knowledge bases
* Complex nested data structures with embeddings
* Large evaluation datasets
* Any JSON data that exceeds the 6MB trace limit

`JSONAttachment` automatically serializes your JSON data and stores it as an attachment with content type `application/json`. The data is:

* Uploaded separately as an attachment, bypassing the 6MB trace limit
* Not indexed, which saves storage space and speeds up ingestion
* Still fully viewable in the UI with all the features of the JSON viewer (collapsible nodes, syntax highlighting, search, etc.)

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { JSONAttachment, initLogger } from "braintrust";

  const logger = initLogger();

  // Example: Large conversation transcript
  const transcript = Array.from({ length: 100 }, (_, i) => ({
    role: i % 2 === 0 ? "user" : "assistant",
    content: `Message content ${i}...`,
    timestamp: new Date().toISOString(),
  }));

  logger.log({
    input: {
      type: "chat_completion",
      // Store large transcript as an attachment
      transcript: new JSONAttachment(transcript, {
        filename: "conversation_transcript.json",
        pretty: true, // Optional: pretty-print the JSON
      }),
      config: {
        temperature: 0.7,
        model: "gpt-5-mini",
      },
    },
    output: "Completed conversation successfully",
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from datetime import datetime

  from braintrust import JSONAttachment, init_logger

  logger = init_logger()

  # Example: Large conversation transcript
  transcript = [
      {
          "role": "user" if i % 2 == 0 else "assistant",
          "content": f"Message content {i}...",
          "timestamp": datetime.now().isoformat(),
      }
      for i in range(100)
  ]

  logger.log(
      {
          "input": {
              "type": "chat_completion",
              # Store large transcript as an attachment
              "transcript": JSONAttachment(
                  transcript,
                  filename="conversation_transcript.json",
                  pretty=True,  # Optional: pretty-print the JSON
              ),
              "config": {
                  "temperature": 0.7,
                  "model": "gpt-4",
              },
          },
          "output": "Completed conversation successfully",
      }
  )
  ```
</CodeGroup>

Just like other attachments, JSON attachments can be previewed directly in the UI and downloaded for local viewing. Check out the [Upload large traces](/guides/traces/customize#upload-large-traces) section for more examples and details.

### Upload attachments in the UI

You can upload attachments directly through the UI for any editable span field. This includes:

* Any dataset fields, including datasets in playgrounds
* Log span fields
* Experiment span fields

You can also include attachments in prompt messages when using models that support multimodal inputs.

## Inline attachments

Sometimes your attachments are pre-hosted files which you do not want to upload explicitly, but would like
to display as if they were attachments. Inline attachments allow you to do this, by specifying the URL and content
type of the file. Create a JSON object anywhere in the log data with `type: "inline_attachment"` and `src` and
`content_type` fields. The `filename` field is optional.

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "file": {
    "type": "inline_attachment",
    "src": "https://robohash.org/example",
    "content_type": "image/png",
    "filename": "A robot"
  }
}
```

<img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/inline-attachment.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=604b9eeaacd49cf0aa30a96efbf1d42b" alt="Screenshot of inline attachment" width="625" height="313" data-og-width="1104" data-og-height="984" data-path="images/guides/inline-attachment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/inline-attachment.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=752fbdd28904d24046b35515388fa073 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/inline-attachment.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=f11e919d3c3a8dd94bb7886f2f2e0757 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/inline-attachment.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=ea8a2366409d107a9f7aed4100a5abdf 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/inline-attachment.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=1cdc5ba68881fdfaa6740015afd19bb6 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/inline-attachment.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=103ba56246e25a1ca6e2f38b5e672e75 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/inline-attachment.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=e8dac0cfe0c25da1e37078cd0cb75ef2 2500w" />

## View attachments in the UI

You can preview images, audio files, videos, PDFs, and JSON files in the Braintrust UI. You can also download any file to view it locally.
We provide built-in support to preview attachments directly in playground input cells and traces.

In the playground, you can preview attachments in an inline embedded view for easy visual verification during experimentation:

<img src="https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/attachment-in-playground.png?fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=efd62c2563a801249da20c8cd220fae3" alt="Screenshot of attachment inline in a playground" width="625" height="313" data-og-width="738" data-og-height="504" data-path="images/guides/attachment-in-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/attachment-in-playground.png?w=280&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=ffc5cb2285cfa94b6f7b19bce2905af4 280w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/attachment-in-playground.png?w=560&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=f4df52ff5c717d07c30d769e10415d0f 560w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/attachment-in-playground.png?w=840&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=48509a62df8f0bbeb18a517a807e94bf 840w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/attachment-in-playground.png?w=1100&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=820fdf2158c053e1ae991068846ba153 1100w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/attachment-in-playground.png?w=1650&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=f0ab6fca83f3fa27752ed885c74ef181 1650w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/attachment-in-playground.png?w=2500&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=cca006295780fa558f5cfeeab7056e92 2500w" />

In the trace pane, attachments appear as an additional list under the data viewer:

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/traces/attachment-list-one-image.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=0ecbc0ac1591d51861a2a543c6000b78" alt="Screenshot of attachment list in Braintrust" width="625" height="313" data-og-width="1250" data-og-height="626" data-path="images/guides/traces/attachment-list-one-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/traces/attachment-list-one-image.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=267df2f2030e457dd4226059a06eb918 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/traces/attachment-list-one-image.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=60af362f40f7f27cc96f4cb0e256f505 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/traces/attachment-list-one-image.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=0719364f1d262e321774d00a8b52934d 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/traces/attachment-list-one-image.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=63201f5a8bf612573cffdeb53d0db0b1 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/traces/attachment-list-one-image.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=ea2da3d44a1bcb5f9cf4418ddffeba4b 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/traces/attachment-list-one-image.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=4053eb2e3f62c21c06a45cf1936f544d 2500w" />

## Read attachments via SDK

You can programmatically read and process attachments using the Braintrust SDK. This allows you to access attachment data in your code for analysis, processing, or integration with other systems.

When accessing a dataset or experiment, the TypeScript and Python SDKs automatically create a `ReadonlyAttachment` object for each attachment.

For attachments in scorers or logs, use the `ReadonlyAttachment` class to access attachment data, check metadata, and process different content types.

### Access attachments from a dataset

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initDataset } from "braintrust";
  import { Buffer } from "buffer";

  async function processDatasetWithAttachments() {
    // Load a dataset that contains attachments
    const dataset = initDataset({
      project: "my-project",
      dataset: "my-dataset-with-images",
    });

    // Get the single row from the dataset
    const records = dataset.fetch();
    const row = await records.next();
    const record = row.value;

    // The record contains attachment references that are automatically converted to ReadonlyAttachment objects
    const imageAttachment = record.input.image;
    const documentAttachment = record.input.document;

    // Access image attachment data
    const imageData = await imageAttachment.data();

    // Process the image data
    const arrayBuffer = await imageData.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);

    // Access document attachment data
    const documentData = await documentAttachment.data();
    const documentText = await documentData.text();
  }

  processDatasetWithAttachments();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_dataset


  def process_dataset_with_attachments():
      # Load a dataset that contains attachments
      dataset = init_dataset(project="my-project", dataset="my-dataset-with-images")

      # Get the single row from the dataset
      records = dataset.fetch()
      record = next(records)

      # The record contains attachment references that are automatically converted to ReadonlyAttachment objects
      image_attachment = record.input["image"]
      document_attachment = record.input["document"]

      # Access image attachment data
      image_data = image_attachment.data

      # Access document attachment data
      document_data = document_attachment.data
      document_text = document_data.decode("utf-8")


  if __name__ == "__main__":
      process_dataset_with_attachments()
  ```
</CodeGroup>

### Create ReadonlyAttachment from raw logs data

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { ReadonlyAttachment } from "braintrust";
  import { Buffer } from "buffer";

  async function processRawLogsWithAttachments() {
    // Example raw log data that contains attachment references
    const rawLogData = {
      id: "log-123",
      input: {
        question: "What is in this image?",
        image: {
          type: "braintrust_attachment" as const,
          key: "attachments/abc123def456",
          filename: "sample_image.jpg",
          content_type: "image/jpeg",
        },
        document: {
          type: "braintrust_attachment" as const,
          key: "attachments/xyz789ghi012",
          filename: "context.pdf",
          content_type: "application/pdf",
        },
      },
      output: "This image shows a cat sitting on a windowsill.",
    };

    // Manually create ReadonlyAttachment objects from raw attachment references
    const imageAttachment = new ReadonlyAttachment(rawLogData.input.image);
    const documentAttachment = new ReadonlyAttachment(rawLogData.input.document);

    // Access image attachment data
    const imageData = await imageAttachment.data();

    // Process the image data
    const arrayBuffer = await imageData.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);

    // Access document attachment data
    const documentData = await documentAttachment.data();
    const documentText = await documentData.text();
  }

  processRawLogsWithAttachments();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import ReadonlyAttachment


  def process_raw_logs_with_attachments():
      # Example raw log data that contains attachment references
      raw_log_data = {
          "id": "log-123",
          "input": {
              "question": "What is in this image?",
              "image": {
                  "type": "braintrust_attachment",
                  "key": "attachments/abc123def456",
                  "filename": "sample_image.jpg",
                  "content_type": "image/jpeg",
              },
              "document": {
                  "type": "braintrust_attachment",
                  "key": "attachments/xyz789ghi012",
                  "filename": "context.pdf",
                  "content_type": "application/pdf",
              },
          },
          "output": "This image shows a cat sitting on a windowsill.",
      }

      # Manually create ReadonlyAttachment objects from raw attachment references
      image_attachment = ReadonlyAttachment(raw_log_data["input"]["image"])
      document_attachment = ReadonlyAttachment(raw_log_data["input"]["document"])

      # Access image attachment data
      image_data = image_attachment.data

      # Access document attachment data
      document_data = document_attachment.data
      document_text = document_data.decode("utf-8")


  if __name__ == "__main__":
      process_raw_logs_with_attachments()
  ```
</CodeGroup>

### Handle external attachments

Work with external attachments (like S3 files) using the same patterns.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { ReadonlyAttachment } from "braintrust";
  import { Buffer } from "buffer";

  async function processExternalAttachment() {
    // Example external attachment reference
    const externalAttachment = new ReadonlyAttachment({
      type: "external_attachment" as const,
      url: "s3://bucket/path/to/file.pdf",
      filename: "document.pdf",
      content_type: "application/pdf",
    });

    // Access external attachment data
    const data = await externalAttachment.data();
    console.log(`External file size: ${data.size} bytes`);

    // Convert Blob to Buffer for file writing
    const arrayBuffer = await data.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);

    // Save to local file
    console.log("External attachment ready for processing");
  }

  processExternalAttachment();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import ReadonlyAttachment


  def process_external_attachment():
      # Example external attachment reference
      external_attachment = ReadonlyAttachment(
          {
              "type": "external_attachment",
              "url": "s3://bucket/path/to/file.pdf",
              "filename": "document.pdf",
              "content_type": "application/pdf",
          }
      )

      # Access external attachment data
      data = external_attachment.data
      print(f"External file size: {len(data)} bytes")

      # Save to local file
      print("External attachment ready for processing")


  if __name__ == "__main__":
      process_external_attachment()
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt