# Source: https://flatfile.com/docs/plugins/sentiment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sentiment Analysis Plugin

> Automatically analyze sentiment in text fields and add sentiment scores and categories to your Flatfile records

This plugin analyzes the sentiment of text within specified fields of records in a Flatfile Sheet. It operates during the data processing phase by hooking into the record commit lifecycle. For each designated text field, the plugin calculates a sentiment score, categorizes it as 'positive', 'negative', or 'neutral', and adds this information back to the record in two new fields: `<field_name>_sentiment_score` and `<field_name>_sentiment_category`. It also adds informational messages to the record detailing the outcome of the analysis. This is useful for automatically classifying customer feedback, product reviews, support tickets, or any other free-text data to quickly gauge user sentiment.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-enrich-sentiment
```

## Configuration & Parameters

The plugin accepts a configuration object with the following parameters:

### `sheetSlug` (required)

* **Type:** `string`
* **Description:** The slug of the sheet that this plugin should run on.

### `textFields`

* **Type:** `string[]`
* **Description:** An array of field keys (column names) that contain the text to be analyzed.
* **Default:** `['description']`

### `automaticValidation`

* **Type:** `boolean`
* **Description:** A flag to enable or disable the sentiment analysis. If set to `false`, the plugin will add an info message to each record indicating that analysis is disabled but will not perform any analysis.
* **Default:** `false` - The analysis only runs if this is explicitly set to `true`.

### `errorMessages`

* **Type:** `object`
* **Description:** A configuration object for custom error messages. Note: This option is defined in the type interface but is not used in the current plugin implementation.

## Usage Examples

### Basic Usage

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { enrichSentiment } from '@flatfile/plugin-enrich-sentiment';

    export default function(listener) {
      // Analyzes the 'description' field in the 'contacts' sheet.
      listener.use(enrichSentiment({
        sheetSlug: 'contacts',
        textFields: ['description'],
        automaticValidation: true
      }));
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { enrichSentiment } from '@flatfile/plugin-enrich-sentiment';

    export default function(listener: FlatfileListener) {
      // Analyzes the 'description' field in the 'contacts' sheet.
      listener.use(enrichSentiment({
        sheetSlug: 'contacts',
        textFields: ['description'],
        automaticValidation: true
      }));
    }
    ```
  </Tab>
</Tabs>

### Multiple Text Fields

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { enrichSentiment } from '@flatfile/plugin-enrich-sentiment';

    export default function(listener) {
      // A more detailed configuration for a customer feedback sheet.
      // Analyzes both 'comment' and 'feedback' fields.
      listener.use(enrichSentiment({
        sheetSlug: 'customer-feedback',
        textFields: ['comment', 'feedback'],
        automaticValidation: true
      }));
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { enrichSentiment } from '@flatfile/plugin-enrich-sentiment';

    export default function(listener: FlatfileListener) {
      // A more detailed configuration for a customer feedback sheet.
      // Analyzes both 'comment' and 'feedback' fields.
      listener.use(enrichSentiment({
        sheetSlug: 'customer-feedback',
        textFields: ['comment', 'feedback'],
        automaticValidation: true
      }));
    }
    ```
  </Tab>
</Tabs>

### Advanced Custom Usage

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    // This example shows how to use the exported helper functions
    // inside a custom recordHook for more fine-grained control.
    import { FlatfileListener } from '@flatfile/listener';
    import { recordHook } from '@flatfile/plugin-record-hook';
    import { performEnrichSentiment } from '@flatfile/plugin-enrich-sentiment';

    export default function(listener) {
      listener.use(recordHook('reviews', async (record) => {
        const reviewText = String(record.get('review_text'));

        // Use the exported helper function directly
        const { error, result } = performEnrichSentiment(reviewText, 'review_text');

        if (error) {
          record.addWarning('review_text', error);
        } else if (result) {
          // Custom logic: only add a 'positive_review' flag
          if (result.category === 'positive' && result.score > 3) {
            record.set('positive_review', true);
            record.addInfo('review_text', 'This is a highly positive review!');
          }
        }
        return record;
      }));
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    // This example shows how to use the exported helper functions
    // inside a custom recordHook for more fine-grained control.
    import { FlatfileListener } from '@flatfile/listener';
    import { recordHook } from '@flatfile/plugin-record-hook';
    import { performEnrichSentiment } from '@flatfile/plugin-enrich-sentiment';

    export default function(listener: FlatfileListener) {
      listener.use(recordHook('reviews', async (record) => {
        const reviewText = String(record.get('review_text'));

        // Use the exported helper function directly
        const { error, result } = performEnrichSentiment(reviewText, 'review_text');

        if (error) {
          record.addWarning('review_text', error);
        } else if (result) {
          // Custom logic: only add a 'positive_review' flag
          if (result.category === 'positive' && result.score > 3) {
            record.set('positive_review', true);
            record.addInfo('review_text', 'This is a highly positive review!');
          }
        }
        return record;
      }));
    }
    ```
  </Tab>
</Tabs>

### Using Utility Functions

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { analyzeSentiment } from '@flatfile/plugin-enrich-sentiment';

    const analysis = analyzeSentiment("Flatfile is an amazing tool!");
    // analysis -> { score: 6, category: 'positive' }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { analyzeSentiment } from '@flatfile/plugin-enrich-sentiment';

    const analysis = analyzeSentiment("Flatfile is an amazing tool!");
    // analysis -> { score: 6, category: 'positive' }
    ```
  </Tab>
</Tabs>

## API Reference

### `enrichSentiment(config: EnrichSentimentConfig)`

The main entry point for the plugin. It creates and registers a `recordHook` with Flatfile that performs sentiment analysis on incoming records based on the provided configuration.

**Parameters:**

* `config` (EnrichSentimentConfig): An object containing configuration options
  * `sheetSlug` (string): The slug of the sheet to target
  * `textFields` (string\[]): An array of field keys to analyze. Defaults to `['description']`
  * `automaticValidation` (boolean): Must be `true` to enable analysis

**Returns:** A function of type `(listener: FlatfileListener) => void` which is used to install the plugin into a Flatfile listener.

### `analyzeSentiment(text: string)`

A pure function that takes a string of text and returns its sentiment analysis.

**Parameters:**

* `text` (string): The input text to analyze

**Returns:** An object with the following properties:

* `score` (number): A numerical score representing the sentiment. Positive values are positive, negative values are negative
* `category` ('positive' | 'negative' | 'neutral'): A string category for the sentiment

### `performEnrichSentiment(value: string, field: string)`

A wrapper around `analyzeSentiment` that includes basic validation and formats the output for use within a record hook. It checks for empty input and structures the return value with either an error or a result object.

**Parameters:**

* `value` (string): The text value from the record field
* `field` (string): The name of the field being analyzed, used for creating informative messages

**Returns:** An object with one of two shapes:

* On success: `{ error: null, result: { score: number, category: string, message: string } }`
* On error (empty input): `{ error: string, result: null }`

## Troubleshooting

### Empty Text Fields

If a text field specified in the `textFields` configuration is empty or null, the plugin will not throw an error. Instead, it will add a warning to the record using `record.addWarning()` with a message like "No text found for sentiment analysis in field: \[field\_name]".

### Analysis Not Running

If `automaticValidation` is set to `false` or is omitted, the plugin will not perform any analysis or add any warnings. It will only add an informational message to the record stating that automatic analysis is disabled.

## Notes

### Default Behavior

* The plugin is **disabled by default**. You must explicitly set `automaticValidation: true` to enable sentiment analysis.
* If no `textFields` are specified, the plugin will default to analyzing the `description` field.

### Generated Fields

The plugin adds two new fields to each processed record for each analyzed text field:

* `<field_name>_sentiment_score`: Contains the numerical sentiment score
* `<field_name>_sentiment_category`: Contains the sentiment category ('positive', 'negative', or 'neutral')

Ensure your Sheet configuration or downstream systems can handle these new fields.

### Configuration Considerations

* The configuration property to enable the plugin is `automaticValidation` (boolean), not `autoAnalysis`.
* The `errorMessages` property in the `EnrichSentimentConfig` type is defined but not currently implemented in the plugin's logic.
* The plugin relies on the `sentiment` npm package for its analysis logic.
