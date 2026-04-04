# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/api-parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Partition Endpoint parameters

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

The Unstructured Partition Endpoint provides parameters to customize the processing of documents. These parameters include:

The only required parameter is `files` -  the file you wish to process.

[//]: # "TODO: In the future we should automatically generate this table to make sure it's up to date"

| POST, Python                               | JavaScript/TypeScript                    | Description                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `files` (*shared.Files*)                   | `files` (*File*, *Blob*, *shared.Files*) | The file to process.                                                                                                                                                                                                                                                                                                                                   |
| `chunking_strategy` (*str*)                | `chunkingStrategy` (*string*)            | Use one of the supported strategies to chunk the returned elements after partitioning. When no chunking strategy is specified, no chunking is performed and any other chunking parameters provided are ignored. Supported strategies: `basic`, `by_title`, `by_page`, and `by_similarity`. [Learn more](/api-reference/legacy-api/partition/chunking). |
| `content_type` (*str*)                     | `contentType` (*string*)                 | A hint to Unstructured about the content type to use (such as `text/markdown`), when there are problems processing a specific file. This value is a MIME type in the format `type/subtype`. For available MIME types, see [model.py](https://github.com/Unstructured-IO/unstructured/blob/main/unstructured/file_utils/model.py).                      |
| `coordinates` (*bool*)                     | `coordinates` (*boolean*)                | True to return bounding box coordinates for each element extracted with OCR. Default: false. [Learn more](/api-reference/legacy-api/partition/examples#saving-bounding-box-coordinates).                                                                                                                                                               |
| `encoding` (*str*)                         | `encoding` (*string*)                    | The encoding method used to decode the text input. Default: `utf-8`.                                                                                                                                                                                                                                                                                   |
| `extract_image_block_types` (*List\[str]*) | `extractImageBlockTypes` (*string\[]*)   | The types of elements to extract, for use in extracting image blocks as Base64 encoded data stored in element metadata fields, for example: `["Image","Table"]`. Supported filetypes are image and PDF. [Learn more](/api-reference/legacy-api/partition/extract-image-block-types).                                                                   |
| `gz_uncompressed_content_type` (*str*)     | `gzUncompressedContentType` (*string*)   | If file is gzipped, use this content type after unzipping. Example: `application/pdf`                                                                                                                                                                                                                                                                  |
| `hi_res_model_name` (*str*)                | `hiResModelName`  (*string*)             | The name of the inference model used when strategy is `hi_res`. Options are `layout_v1.1.0` and `yolox`. Default: `layout_v1.1.0`. [Learn more](/api-reference/legacy-api/partition/examples#changing-partition-strategy-for-a-pdf).                                                                                                                   |
| `include_page_breaks` (*bool*)             | `includePageBreaks` (*boolean*)          | True for the output to include page breaks if the filetype supports it. Default: false.                                                                                                                                                                                                                                                                |
| `languages` (*List\[str]*)                 | `languages` (*string\[]*)                | The languages present in the document, for use in partitioning and OCR. [View the list of available languages](https://github.com/tesseract-ocr/tessdata). [Learn more](/api-reference/legacy-api/partition/examples#specifying-the-language-of-a-document-for-better-ocr-results).                                                                    |
| `output_format` (*str*)                    | `outputFormat` (*string*)                | The format of the response. Supported formats are `application/json` and `text/csv`. Default: `application/json`.                                                                                                                                                                                                                                      |
| `pdf_infer_table_structure` (*bool*)       | `pdfInferTableStructure` (*boolean*)     | **Deprecated!** Use `skip_infer_table_types` instead. If true and `strategy` is `hi_res`, any `Table` elements extracted from a PDF will include an additional metadata field, `text_as_html`, where the value (string) is a just a transformation of the data into an HTML table.                                                                     |
| `skip_infer_table_types` (*List\[str]*)    | `skipInferTableTypes` (*string\[]*)      | The document types that you want to skip table extraction for. Default: `[]`.                                                                                                                                                                                                                                                                          |
| `starting_page_number` (*int*)             | `startingPageNumber` (*number*)          | The page number to be be assigned to the first page in the document. This information will be included in elements' metadata and can be be especially useful when partitioning a document that is part of a larger document.                                                                                                                           |
| `strategy` (*str*)                         | `strategy` (*string*)                    | The strategy to use for partitioning PDF and image files. Options are `auto`, `vlm`, `hi_res`, `fast`, and `ocr_only`. Default: `auto`. [Learn more](/api-reference/legacy-api/partition/partitioning).                                                                                                                                                |
| `unique_element_ids` (*bool*)              | `uniqueElementIds` (*boolean*)           | True to assign UUIDs to element IDs, which guarantees their uniqueness (useful when using them as primary keys in database). Otherwise a SHA-256 of the element's text is used. Default: false.                                                                                                                                                        |
| `vlm_model` (*str*)                        | (Not yet available)                      | Applies only when `strategy` is `vlm`. The name of the vision language model (VLM) provider to use for partitioning. `vlm_model_provider` must also be specified. For a list of allowed values, see the end of this article.                                                                                                                           |
| `vlm_model_provider` (*str*)               | (Not yet available)                      | Applies only when `strategy` is `vlm`. The name of the vision language model (VLM) to use for partitioning. `vlm_model` must also be specified. For a list of allowed values, see the end of this article.                                                                                                                                             |
| `xml_keep_tags` (*bool*)                   | `xmlKeepTags` (*boolean*)                | True to retain the XML tags in the output. Otherwise it will just extract the text from within the tags. Only applies to XML documents.                                                                                                                                                                                                                |

The following parameters only apply when a chunking strategy is specified. Otherwise, they are ignored. [Learn more](/api-reference/legacy-api/partition/chunking).

| POST, Python                     | JavaScript/TypeScript             | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `combine_under_n_chars` (*int*)  | `combineUnderNChars` (*number*)   | Applies only when the chunking strategy is set to `by_title`. Use this parameter to combines small chunks until the combined chunk reaches a length of `n` characters. This can mitigate the appearance of small chunks created by short paragraphs, not intended as section headings, being identified as `Title` elements in certain documents. Default: the same value as `max_characters`. |
| `include_orig_elements` (*bool*) | `includeOrigElements` (*boolean*) | True (the default) to have the elements that are used to form a chunk appear in `.metadata.orig_elements` for that chunk.                                                                                                                                                                                                                                                                      |
| `max_characters` (*int*)         | `maxCharacters` (*number*)        | Cut off new sections after reaching a length of `n` characters. (This is a hard maximum.) Default: 500.                                                                                                                                                                                                                                                                                        |
| `multipage_sections` (*bool*)    | `multipageSections` (*boolean*)   | Applies only when the chunking strategy is set to `by_title`. Determines if a chunk can include elements from more than one page. Default: true.                                                                                                                                                                                                                                               |
| `new_after_n_chars` (*int*)      | `newAfterNChars` (*number*)       | Applies only when the chunking strategy is specified. Cuts off new sections after reaching a length of `n` characters. (This is a soft maximum.) Default: 1500.                                                                                                                                                                                                                                |
| `overlap` (*int*)                | `overlap` (*number*)              | A prefix of this many trailing characters from the prior text-split chunk is applied to second and later chunks formed from oversized elements by text-splitting. Default: none.                                                                                                                                                                                                               |
| `overlap_all` (*bool*)           | `overlapAll` (*boolean*)          | True to have an overlap also applied to "normal" chunks formed by combining whole elements. Use with caution, as this can introduce noise into otherwise clean semantic units. Default: none.                                                                                                                                                                                                  |
| `similarity_threshold` (*float*) | `similarityThreshold` (*number*)  | Applies only when the chunking strategy is set to `by_similarity`. The minimum similarity text in consecutive elements must have to be included in the same chunk. Must be between 0.0 and 1.0, exclusive (0.01 to 0.99, inclusive). Default: 0.5.                                                                                                                                             |

The following parameters are specific to the Python and JavaScript/TypeScript clients and are not sent to the server. [Learn more](/api-reference/legacy-api/partition/sdk-python#page-splitting).

| POST, Python                          | JavaScript/TypeScript                 | Description                                                                                                                                                                                                                                          |
| ------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `split_pdf_page` (*bool*)             | `splitPdfPage` (*boolean*)            | True to split the PDF file client-side. [Learn more](/api-reference/legacy-api/partition/sdk-python#page-splitting).                                                                                                                                 |
| `split_pdf_allow_failed` (*bool*)     | `splitPdfAllowFailed` (*boolean*)     | When `true`, a failed split request will not stop the processing of the rest of the document. The affected page range will be ignored in the results. When `false`, a failed split request will cause the entire document to fail. Default: `false`. |
| `split_pdf_concurrency_level` (*int*) | `splitPdfConcurrencyLevel` (*number*) | The number of split files to be sent concurrently. Default: 5. Maximum: 15.                                                                                                                                                                          |
| `split_pdf_page_range` (*List\[int]*) | `splitPdfPageRange` (*number\[]*)     | A list of 2 integers within the range `[1, length_of_pdf]`. When pdf splitting is enabled, this will send only the specified page range to the API.                                                                                                  |

Need help getting started? Check out the [Examples page](/api-reference/legacy-api/partition/examples) for some inspiration.

Allowed values for `vlm_model_provider` and `vlm_model` pairs include the following:

<Warning>
  The following models are no longer available as of the following dates:

  * For `anthropic`, `claude-3-5-sonnet-20241022`: October 22, 2025
  * For `bedrock`, `us.anthropic.claude-3-5-sonnet-20241022-v2:0`: October 22, 2025

  Unstructured recommends the following actions:

  * For new workflows, do not use any of these models.
  * For any workflow that uses any of these models, update that workflow as soon as possible to use a different model.

  Workflows that attempt to use any of these models on or after its associated date will return errors.
</Warning>

| `vlm_model_provider` | `vlm_model`                                  |
| -------------------- | -------------------------------------------- |
| `anthropic`          | `claude-sonnet-4-20250514`                   |
| `bedrock`            | `us.amazon.nova-lite-v1:0`                   |
| `bedrock`            | `us.amazon.nova-pro-v1:0`                    |
| `bedrock`            | `us.anthropic.claude-3-haiku-20240307-v1:0`  |
| `bedrock`            | `us.anthropic.claude-3-opus-20240229-v1:0`   |
| `bedrock`            | `us.anthropic.claude-3-sonnet-20240229-v1:0` |
| `bedrock`            | `us.anthropic.claude-sonnet-4-20250514-v1:0` |
| `bedrock`            | `us.meta.llama3-2-11b-instruct-v1:0`         |
| `bedrock`            | `us.meta.llama3-2-90b-instruct-v1:0`         |
| `openai`             | `gpt-4o`                                     |
| `openai`             | `gpt-5-mini-2025-08-07`                      |
| `vertexai`           | `gemini-2.0-flash-001`                       |
