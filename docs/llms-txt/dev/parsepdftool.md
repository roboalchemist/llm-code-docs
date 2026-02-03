# Source: https://dev.writer.com/blueprints/parsepdftool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Parse PDF tool

Uses Writer API to extract the text content of a PDF file stored in Writer cloud.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=48f50e8bf109f7831fdbfa4e9408f45e" alt="" data-og-width="2192" width="2192" data-og-height="1440" height="1440" data-path="images/agent-builder/blueprints/parse-pdf-tool-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5ad2d84b29e01744a462462a730da1a9 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=bcf9524a6b1c14839b769532822734c4 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=599a7746ee59866eccb25faa305f2b64 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=920b04be5d8375eedd7317e5eb950b14 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=be4f87b12814eb0b33f40e981e08187e 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=287bb224737172f052ab63cd18ff1277 2500w" />

## Overview

The **Parse PDF tool** block extracts text content from PDF files stored in the Writer cloud. Use it to convert PDF documents into searchable, analyzable text that can be used in AI workflows, content analysis, or data extraction processes.

## Common use cases

* Extracting text from PDF documents for analysis
* Converting PDF reports into searchable content
* Processing PDF forms and documents
* Building document processing workflows

## How it works

1. **PDF input**: Provide a PDF file UUID from the Writer cloud. The file must be uploaded to Writer first; you can upload a file first using the "Add files to Writer Cloud" block. You can also use files uploaded via the API, no-code agents, or the Writer cloud UI.
2. **Content extraction**: The block extracts text content from the PDF using the Writer API.
3. **Format selection**: Choose to enable markdown formatting for the extracted content.
4. **Text processing**: Converts PDF content into the selected format and returns it as a string.

The block handles PDF parsing, text extraction, and formatting. The extracted text maintains the document's structure.

### When to enable markdown formatting

You can choose to parse the PDF content as plain text or markdown. The default is plain text.

**When to use markdown:**

* Preserving document structure and hierarchy
* Maintaining formatting for readability
* Working with documents that have headings, lists, or emphasis
* Creating summaries that maintain document organization

**When to use plain text:**

* Simple text analysis and processing
* When formatting isn't relevant to your workflow
* Extracting raw text for AI processing
* Reducing complexity in downstream processing

## Examples

### Document analysis workflow

This example shows how to extract and analyze text from PDF documents in a complete workflow.

**Blueprint Flow:**

1. **UI Trigger** → User uploads PDF document
2. **Add files to Writer Cloud** → Uploads PDF document to Writer cloud
3. **Parse PDF tool** → Extracts text from PDF document
4. **Text generation** → Creates analysis and summary
5. **Set state** → Stores analysis for user review

**Block Configuration:**

* **File:** `@{result.0.id}`. This variable is the UUID of the file in Writer cloud. The `Add files to Writer Cloud` block returns a list of file objects that were uploaded to Writer cloud. To process multiple files, you can use the [**For each loop** block](/blueprints/for-eachloop) to iterate over the list of files.
* **Enable markdown:** `disabled`. Extracts content as plain text, because the formatting isn't relevant to the text generation task.

<Warning>The Parse PDF tool only accepts file UUID from the Writer cloud. Files must be uploaded first using the "Add files to Writer Cloud" block or File input component.</Warning>

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4098391a24854a61c3131003ca41ee87" alt="" data-og-width="2408" width="2408" data-og-height="1572" height="1572" data-path="images/agent-builder/blueprints/parse-pdf-tool-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=50a40f135ae328c57771ca5b4fad5b46 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2dca62d57b10b9a34de4eb0db35555c1 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ff7b404897f28d8040ccc84cc3d853d6 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e5b5bf0c6cdc8948200c65794f5ecdb0 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ad3e6403448667ac98a81c916368f6e8 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-pdf-tool-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c0c3d2788d43d373ed3a007368da4639 2500w" />

This workflow enables automated document analysis and text extraction for research and content processing.

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>File</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <code>""</code>
      </td>

      <td>UUID of a file object in Files API.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Format: uuid
      </td>
    </tr>

    <tr>
      <td>Enable markdown</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <code>yes</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The PDF was parsed successfully.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error parsing the PDF.</td>
    </tr>
  </tbody>
</table>

The **Parse PDF tool** block returns the extracted text content as a string. Access the output using the `@{result}` variable in the block that follows it in a blueprint.
