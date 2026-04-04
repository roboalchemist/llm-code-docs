# Source: https://flatfile.com/docs/plugins/what3words.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What3Words Converter Plugin

> Automatically convert What3Words addresses into standard geographic data including country codes, nearest places, and latitude/longitude coordinates using the official What3Words API.

The What3Words plugin for Flatfile automatically converts What3Words (W3W) addresses into standard geographic data. It listens for data commits, takes a W3W address from a specified field in a sheet, and uses the official What3Words API to fetch the corresponding country, nearest place, and latitude/longitude coordinates. The plugin then populates this information into other specified fields within the same record.

This is useful for any data import workflow where users provide locations using the What3Words system, and the application requires standard address components or geographic coordinates for mapping, logistics, or data normalization.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-convert-what3words
```

## Configuration & Parameters

The plugin is configured through the `convertWhat3words` function, which accepts a configuration object with the following parameters:

### Required Parameters

<ParamField path="what3wordsField" type="string" required>
  The key of the field in your sheet that contains the What3Words address to be converted.
</ParamField>

<ParamField path="countryField" type="string" required>
  The key of the field where the resulting country code (e.g., "GB") will be stored.
</ParamField>

<ParamField path="nearestPlaceField" type="string" required>
  The key of the field where the name of the nearest place (e.g., "London") will be stored.
</ParamField>

<ParamField path="latField" type="string" required>
  The key of the field where the resulting latitude coordinate will be stored.
</ParamField>

<ParamField path="longField" type="string" required>
  The key of the field where the resulting longitude coordinate will be stored.
</ParamField>

### Optional Parameters

<ParamField path="sheetSlug" type="string" default="**">
  The slug of the specific sheet you want this plugin to apply to. If not provided, the plugin will apply to all sheets in the workbook that have a field matching the `what3wordsField` configuration.
</ParamField>

## Usage Examples

### Basic Usage

Apply the What3Words converter to a specific sheet:

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { convertWhat3words } from '@flatfile/plugin-convert-what3words';

  export default function (listener) {
    listener.use(
      convertWhat3words({
        sheetSlug: 'locations',
        what3wordsField: 'w3w_address',
        countryField: 'country_code',
        nearestPlaceField: 'city',
        latField: 'latitude',
        longField: 'longitude'
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { convertWhat3words } from '@flatfile/plugin-convert-what3words';

  export default function (listener: FlatfileListener) {
    listener.use(
      convertWhat3words({
        sheetSlug: 'locations',
        what3wordsField: 'w3w_address',
        countryField: 'country_code',
        nearestPlaceField: 'city',
        latField: 'latitude',
        longField: 'longitude'
      })
    );
  }
  ```
</CodeGroup>

### Apply to All Sheets

Configure the plugin to run on all sheets by omitting the `sheetSlug` option:

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { convertWhat3words } from '@flatfile/plugin-convert-what3words';

  export default function (listener) {
    // Applies to all sheets with a 'what3words' field
    listener.use(
      convertWhat3words({
        what3wordsField: 'what3words',
        countryField: 'country',
        nearestPlaceField: 'nearestPlace',
        latField: 'latitude',
        longField: 'longitude'
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { convertWhat3words } from '@flatfile/plugin-convert-what3words';

  export default function (listener: FlatfileListener) {
    // Applies to all sheets with a 'what3words' field
    listener.use(
      convertWhat3words({
        what3wordsField: 'what3words',
        countryField: 'country',
        nearestPlaceField: 'nearestPlace',
        latField: 'latitude',
        longField: 'longitude'
      })
    );
  }
  ```
</CodeGroup>

## Troubleshooting

### Conversions Not Working

* **API Key**: Verify that the `W3W_API_KEY` secret is correctly set in your Flatfile Space
* **Configuration**: Double-check that the `sheetSlug` and all field keys (`what3wordsField`, `countryField`, etc.) in your configuration exactly match the schema of your sheet
* **Data Format**: Ensure the field specified in `what3wordsField` contains valid, correctly formatted What3Words addresses

### Error Messages

If the What3Words API call fails for any reason (e.g., invalid W3W address, network error, invalid API key), the plugin will add a record-level error to the `what3wordsField` with the message "Invalid What3Words address". This error will be visible to the user in the Flatfile UI.

## Notes

### Environment Setup

You must add your What3Words API key as an environment secret named `W3W_API_KEY` in your Flatfile Space before using this plugin.

### Default Behavior

* **Sheet Targeting**: When `sheetSlug` is not provided, the plugin applies to all sheets in the workbook that contain a field matching the `what3wordsField` configuration
* **Event Trigger**: The plugin operates using `bulkRecordHook`, which runs when the user clicks "Continue" or "Submit" on a sheet (during the `commit:created` event)
* **Processing**: The conversion is not real-time as the user types; it occurs during the commit process

### Error Handling

* The plugin processes records individually within a batch
* A failure on one record will not stop the processing of other records
* Errors are logged to the console for debugging purposes
* User-facing errors are attached directly to the record and field that caused the issue

### Idempotency

The plugin processes records on each commit. If data is re-committed, the conversion will run again, potentially overwriting previously converted data.
