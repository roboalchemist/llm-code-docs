# Source: https://flatfile.com/docs/plugins/summarize.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Summarization and Key Phrase Extraction Plugin

> Automatically enriches Flatfile data by performing text summarization and key phrase extraction on specified text fields using natural language processing.

This plugin automatically enriches Flatfile data by performing text summarization and key phrase extraction on a specified text field. It uses the 'compromise' natural language processing library to analyze the content of a source field, generate a concise summary, and identify important phrases. The generated summary and key phrases are then populated into their designated fields.

This is useful for processing large blocks of text, such as product descriptions, user feedback, article content, or support tickets, to quickly get a high-level overview and identify key topics without manual review. The plugin is configured per sheet and can be customized to control the length of the generated summary.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-enrich-summarize
```

## Configuration & Parameters

The `summarize` function accepts a configuration object with the following parameters:

| Parameter           | Type   | Required | Default | Description                                                                                                                                                                                                                                              |
| ------------------- | ------ | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sheetSlug`         | string | Yes      | -       | The slug of the sheet that the plugin should operate on                                                                                                                                                                                                  |
| `contentField`      | string | Yes      | -       | The API key of the field that contains the source text to be summarized                                                                                                                                                                                  |
| `summaryField`      | string | Yes      | -       | The API key of the field where the generated summary should be stored                                                                                                                                                                                    |
| `keyPhrasesField`   | string | Yes      | -       | The API key of the field where the extracted key phrases (as a comma-separated string) should be stored                                                                                                                                                  |
| `summaryLength`     | number | No       | 2       | An optional integer specifying the number of sentences the final summary should contain. This is overridden if `summaryPercentage` is also set                                                                                                           |
| `summaryPercentage` | number | No       | -       | An optional number specifying the desired summary length as a percentage of the total sentences in the content. For example, a value of 30 would create a summary using 30% of the original sentences. This option takes precedence over `summaryLength` |

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { summarize } from "@flatfile/plugin-enrich-summarize";

  const listener = new FlatfileListener();

  listener.use(
    summarize({
      sheetSlug: "articles",
      contentField: "full_text",
      summaryField: "summary",
      keyPhrasesField: "key_phrases",
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { summarize } from "@flatfile/plugin-enrich-summarize";

  const listener = new FlatfileListener();

  listener.use(
    summarize({
      sheetSlug: "articles",
      contentField: "full_text",
      summaryField: "summary",
      keyPhrasesField: "key_phrases",
    })
  );
  ```
</CodeGroup>

### Custom Summary Length

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { summarize } from "@flatfile/plugin-enrich-summarize";

  const listener = new FlatfileListener();

  // Configure the plugin to create a 3-sentence summary
  listener.use(
    summarize({
      sheetSlug: "articles",
      contentField: "full_text",
      summaryField: "summary",
      keyPhrasesField: "key_phrases",
      summaryLength: 3
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { summarize } from "@flatfile/plugin-enrich-summarize";

  const listener = new FlatfileListener();

  // Configure the plugin to create a 3-sentence summary
  listener.use(
    summarize({
      sheetSlug: "articles",
      contentField: "full_text",
      summaryField: "summary",
      keyPhrasesField: "key_phrases",
      summaryLength: 3
    })
  );
  ```
</CodeGroup>

### Percentage-Based Summary

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { summarize } from "@flatfile/plugin-enrich-summarize";

  const listener = new FlatfileListener();

  // Configure the plugin to create a summary using 25% of the original sentences
  listener.use(
    summarize({
      sheetSlug: "product_reviews",
      contentField: "review_text",
      summaryField: "review_summary",
      keyPhrasesField: "review_tags",
      summaryPercentage: 25
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { summarize } from "@flatfile/plugin-enrich-summarize";

  const listener = new FlatfileListener();

  // Configure the plugin to create a summary using 25% of the original sentences
  listener.use(
    summarize({
      sheetSlug: "product_reviews",
      contentField: "review_text",
      summaryField: "review_summary",
      keyPhrasesField: "review_tags",
      summaryPercentage: 25
    })
  );
  ```
</CodeGroup>

## Troubleshooting

* **Plugin not triggering**: Double-check that the `sheetSlug` in your configuration exactly matches the slug of your Sheet in Flatfile
* **Summaries not appearing**: Verify that the `contentField`, `summaryField`, and `keyPhrasesField` names are correct and that the `contentField` actually contains text
* **Data not being processed**: Ensure the `summaryField` is empty for records you expect to be processed, as the plugin will not overwrite existing summaries

## Notes

### Default Behavior

By default, the plugin generates a summary containing 2 sentences. The summarization logic takes sentences from the beginning and end of the source text to form the summary. The plugin will only generate a summary and key phrases if the target `summaryField` is empty; it will not overwrite existing data. If the source `contentField` for a record is empty, the plugin will add an error to that field and skip processing for that record.

### Limitations and Considerations

* The plugin's summarization algorithm is basic: it combines a number of sentences from the beginning and end of the text, separated by "...". It is not an abstractive or AI-based summarization
* The plugin will not overwrite data. If the `summaryField` already contains a value for a given record, that record will be skipped
* Key phrase extraction is based on a fixed grammatical pattern (`#Adjective? #Adjective? #Noun+`), which identifies phrases consisting of up to two optional adjectives followed by one or more nouns
* The plugin depends on the `compromise` NLP library, and the quality of the output is determined by its capabilities
* The plugin is designed to work on `string` field types

### Error Handling

The main error handling pattern is to check for preconditions on a per-record basis. If a precondition fails (e.g., the source text field is empty), the plugin adds a field-level error to the record using `record.addError()`. This provides direct feedback to the user in the Flatfile UI without halting the entire import process.
