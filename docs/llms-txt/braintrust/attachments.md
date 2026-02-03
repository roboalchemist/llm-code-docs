# Source: https://braintrust.dev/docs/instrument/attachments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Log attachments

> Upload images, audio, PDFs, and other binary data

Attachments let you log binary data like images, audio, video, PDFs, and large JSON objects alongside your traces. This enables multimodal evaluations, preserves visual context, and handles data structures that exceed standard trace limits.

## Upload files

Create an `Attachment` object with a file path or in-memory buffer. The SDK uploads attachments in the background without affecting logging latency.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Attachment, initLogger } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

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

  logger = init_logger(project="My Project")

  logger.log(
      input={
          "question": "What is this?",
          "context": Attachment(
              data="path/to/input_image.jpg",
              filename="user_input.jpg",
              content_type="image/jpeg",
          ),
      },
      output="Example response.",
  )
  ```
</CodeGroup>

You can place attachments anywhere in log data - nested in objects, in arrays, or at the top level.

## Log large JSON data

For JSON objects exceeding the 6MB trace limit, use `JSONAttachment`. This is ideal for conversation transcripts, document collections, or complex nested structures.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { JSONAttachment, initLogger } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

  // Large conversation transcript
  const transcript = Array.from({ length: 100 }, (_, i) => ({
    role: i % 2 === 0 ? "user" : "assistant",
    content: `Message content ${i}...`,
    timestamp: new Date().toISOString(),
  }));

  logger.log({
    input: {
      transcript: new JSONAttachment(transcript, {
        filename: "conversation_transcript.json",
        pretty: true, // Optional: pretty-print
      }),
    },
    output: "Conversation completed",
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from datetime import datetime
  from braintrust import JSONAttachment, init_logger

  logger = init_logger(project="My Project")

  # Large conversation transcript
  transcript = [
      {
          "role": "user" if i % 2 == 0 else "assistant",
          "content": f"Message content {i}...",
          "timestamp": datetime.now().isoformat(),
      }
      for i in range(100)
  ]

  logger.log(
      input={
          "transcript": JSONAttachment(
              transcript,
              filename="conversation_transcript.json",
              pretty=True,  # Optional: pretty-print
          ),
      },
      output="Conversation completed",
  )
  ```
</CodeGroup>

JSON attachments bypass the 6MB limit and aren't indexed, saving storage and speeding ingestion while remaining fully viewable in the UI.

## Link external files

<Note>
  External attachments are only supported in self-hosted deployments, not in Braintrust cloud.
</Note>

Reference files in external object stores (currently S3 only) without uploading them:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { ExternalAttachment, initLogger } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

  logger.log({
    input: {
      document: new ExternalAttachment({
        url: "s3://my-bucket/path/to/file.pdf",
        filename: "file.pdf",
        contentType: "application/pdf",
      }),
    },
    output: "Document processed",
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import ExternalAttachment, init_logger

  logger = init_logger(project="My Project")

  logger.log(
      input={
          "document": ExternalAttachment(
              url="s3://my-bucket/path/to/file.pdf",
              filename="file.pdf",
              content_type="application/pdf",
          ),
      },
      output="Document processed",
  )
  ```
</CodeGroup>

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

## Read attachments via SDK

You can programmatically read and process attachments using the Braintrust SDK. This allows you to access attachment data in your code for analysis, processing, or integration with other systems.

When accessing a dataset or experiment, the TypeScript and Python SDKs automatically create a `ReadonlyAttachment` object for each attachment.

For attachments in scorers or logs, use the `ReadonlyAttachment` class to access attachment data, check metadata, and process different content types.

<AccordionGroup>
  <Accordion title="Access attachments from a dataset">
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
  </Accordion>

  <Accordion title="Create ReadonlyAttachment from raw logs data">
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
  </Accordion>

  <Accordion title="Handle external attachments">
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
  </Accordion>
</AccordionGroup>

## Next steps

* [Wrap AI providers](/instrument/wrap-providers) for automatic logging with streaming support
* [View your logs](/observe/view-logs) with attachment previews
* [Build evaluations](/evaluate/run-evaluations) using multimodal data
