# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_PARSE_DOCUMENT

> **Note:**
>
> AI_PARSE_DOCUMENT is the updated version of [PARSE_DOCUMENT (SNOWFLAKE.CORTEX)](parse_document-snowflake-cortex.md).
> For the latest functionality, use AI_PARSE_DOCUMENT.

Returns the extracted content from a document on a Snowflake stage as a JSON-formatted string. This
function supports two types of extraction: Optical Character Recognition (OCR) and layout. For more
information, see [Parsing documents with AI_PARSE_DOCUMENT](../../user-guide/snowflake-cortex/parse-document.md).

## Syntax

```sqlsyntax
AI_PARSE_DOCUMENT( <file_object>, [ <options> ] )
```

## Arguments

**Required:**

`file_object`
:   A [FILE](../data-types-unstructured.md) object that specifies the document to parse, stored in a Snowflake stage. For
    information about creating file objects, see [TO_FILE](to_file.md).

**Optional:**

`options`
:   An OBJECT value that contains options for parsing documents. The supported keys are shown below. All are optional.

    * `'extract_images'`: If set to TRUE, the function extracts images embedded in the document. Requires LAYOUT mode.
    * `'mode'`: Specifies the parsing mode. The supported modes are:

      + `'OCR'`: The function extracts text only. This is the default mode.
      + `'LAYOUT'`: The function extracts layout as well as text, including structural content such as tables.
    * `'page_split'`: If set to TRUE, the function splits the document into pages and processes each page
      separately. This feature supports only PDF, PowerPoint (`.pptx`), and Word (`.docx`) documents.
      Documents in other formats return an error. The default is FALSE.

      > **Tip:**
      >
      > To process long documents that exceed the token limit of AI_PARSE_DOCUMENT, set this option to TRUE.
    * `'page_filter'`: An array that specifies ranges of pages of a multi-page document to process. Each
      range is an object with `start` and `end` fields that specify the first (inclusive) and last (exclusive) page in
      the range. Page indexes start at 0. For example, `{'start': 0, 'end': 1}` specifies the first page of the
      document.

      > **Note:**
      >
      > Specifying `page_filter` implies `page_split`. If you specify page ranges, it is not necessary to also set
      > `page_split`.

## Returns

A JSON object (as a string) that contains the extracted data and associated metadata. The `options` argument
determines the structure of the returned object.

> **Tip:**
>
> To use the output in SQL, convert it to an OBJECT value using the [PARSE_JSON](parse_json.md) function.

If the `'page_split'` option is set, the output has the following structure:

> * `"pages"`: An array of JSON objects, each containing text extracted from the document. If the document has only
>   one page, the output still contains a `"pages"` array (which contains a single object). Each page has the following fields:
>
>   > * `"content"`: Plain text (in OCR mode) or Markdown-formatted text (in LAYOUT mode).
>   > * `"index"`: The page index in the file, starting at 0. Page numbers and formats specified in the document are ignored.
>
> > * `"errorInformation"`: Contains error information if document can’t be parsed.
> > * `"metadata"`: Contains metadata about the document, such as page count.
>
> > **Note:**
> >
> > The `"pages"` and `"metadata"` fields are present in the output when parsing succeeds.
> > `"errorInformation"` is present only if parsing fails.

If `'page_split'` is FALSE or is not present, the output has the following structure:

> > * `"content"`: Plain text (in OCR mode) or Markdown-formatted text (in LAYOUT mode).
> > * `"errorInformation"`: Contains error information if the document can’t be parsed.
> > * `"metadata"`: Contains metadata about the document, such as page count.
>
> > **Note:**
> >
> > The `"content"` and `"metadata"` fields are present in the output when parsing succeeds.
> > `"errorInformation"` is present only if parsing fails.

If the `"extract_images"` option is set to TRUE, the output includes an additional field:

> * `"images"`: An array of JSON objects, each representing an extracted image. Each image object has the following fields:
>
>   * `"id"`: A unique identifier for the image.
>   * `"top_left_x"`, `"top_left_y"`, `"bottom_right_x"`, `"bottom_right_y"`: The coordinates of the bounding box of the image on the page.
>   * `"image_base64"`: The extracted image data encoded as a base64 string.

## Examples

For examples, see [AI_PARSE_DOCUMENT examples](../../user-guide/snowflake-cortex/parse-document.md).

### Limitations

Snowflake Cortex functions do not support dynamic tables.
