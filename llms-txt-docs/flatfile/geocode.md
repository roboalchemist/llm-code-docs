# Source: https://flatfile.com/docs/plugins/geocode.md

# Geocode Address Data

> Automatically enrich location data using the Google Maps Geocoding API to convert addresses into geographic coordinates and vice-versa.

The Geocode plugin for Flatfile automatically enriches location data using the Google Maps Geocoding API. Its primary purpose is to convert addresses into geographic coordinates (latitude and longitude) and vice-versa.

Use cases include:

* **Forward Geocoding**: Automatically populating latitude and longitude fields from a given address field
* **Reverse Geocoding**: Automatically populating a formatted address from given latitude and longitude fields
* **Data Enrichment**: Extract and add supplementary location data to records, such as country and postal code

The plugin operates during the data commit phase (`commit:created`), processing records in bulk before they are finalized.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-enrich-geocode
```

## Configuration & Parameters

The plugin is configured by passing a configuration object to the `enrichGeocode` function.

| Parameter        | Type    | Default       | Description                                                               |
| ---------------- | ------- | ------------- | ------------------------------------------------------------------------- |
| `sheetSlug`      | string  | `"addresses"` | The slug of the sheet you want the plugin to process                      |
| `addressField`   | string  | `"address"`   | The field key/name in your sheet that contains the address to be geocoded |
| `latitudeField`  | string  | `"latitude"`  | The field key/name in your sheet for the latitude value                   |
| `longitudeField` | string  | `"longitude"` | The field key/name in your sheet for the longitude value                  |
| `autoGeocode`    | boolean | `true`        | A flag to enable or disable the automatic geocoding process               |

### Default Behavior

If no configuration is provided, the plugin will attempt to run on a sheet with the slug "addresses", looking for an "address" field to geocode and populating "latitude" and "longitude" fields.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import enrichGeocode from "@flatfile/plugin-enrich-geocode";

  export default function (listener) {
    // Assumes a sheet with slug 'addresses' and fields 'address', 'latitude', 'longitude'
    listener.use(enrichGeocode({}));
  }
  ```

  ```typescript TypeScript
  import type { FlatfileListener } from "@flatfile/listener";
  import enrichGeocode from "@flatfile/plugin-enrich-geocode";

  export default function (listener: FlatfileListener) {
    // Assumes a sheet with slug 'addresses' and fields 'address', 'latitude', 'longitude'
    listener.use(enrichGeocode({}));
  }
  ```
</CodeGroup>

### Custom Configuration

<CodeGroup>
  ```javascript JavaScript
  import enrichGeocode from "@flatfile/plugin-enrich-geocode";

  export default function (listener) {
    listener.use(
      enrichGeocode({
        sheetSlug: 'contacts',
        addressField: 'full_address',
        latitudeField: 'lat',
        longitudeField: 'lon'
      })
    );
  }
  ```

  ```typescript TypeScript
  import type { FlatfileListener } from "@flatfile/listener";
  import enrichGeocode from "@flatfile/plugin-enrich-geocode";

  export default function (listener: FlatfileListener) {
    listener.use(
      enrichGeocode({
        sheetSlug: 'contacts',
        addressField: 'full_address',
        latitudeField: 'lat',
        longitudeField: 'lon'
      })
    );
  }
  ```
</CodeGroup>

### Advanced Usage - Direct API Function

<CodeGroup>
  ```javascript JavaScript
  import { performGeocoding } from "@flatfile/plugin-enrich-geocode";

  async function geocodeSingleAddress(address, apiKey) {
    console.log(`Geocoding address: ${address}`);
    const result = await performGeocoding({ address }, apiKey);

    if ('message' in result) {
      console.error(`Error: ${result.message}`);
    } else {
      console.log(`Coordinates: ${result.latitude}, ${result.longitude}`);
      console.log(`Formatted Address: ${result.formatted_address}`);
    }
  }
  ```

  ```typescript TypeScript
  import { performGeocoding } from "@flatfile/plugin-enrich-geocode";

  async function geocodeSingleAddress(address: string, apiKey: string) {
    console.log(`Geocoding address: ${address}`);
    const result = await performGeocoding({ address }, apiKey);

    if ('message' in result) {
      console.error(`Error: ${result.message}`);
    } else {
      console.log(`Coordinates: ${result.latitude}, ${result.longitude}`);
      console.log(`Formatted Address: ${result.formatted_address}`);
    }
  }
  ```
</CodeGroup>

## API Reference

### enrichGeocode(config)

The main entry point for the plugin. Returns a `bulkRecordHook` compatible with the Flatfile listener's `use()` method.

**Parameters:**

* `config` (object): Configuration object with the parameters described above

**Returns:**
A function that can be passed to `listener.use()` and will be executed on the `commit:created` event.

### performGeocoding(input, apiKey)

An async function that makes a direct call to the Google Maps Geocoding API for both forward and reverse geocoding.

**Parameters:**

* `input` (object): Must contain either:
  * `address` (string): The address to geocode
  * `latitude` (number) and `longitude` (number): The coordinates to reverse geocode
* `apiKey` (string): Your Google Maps Geocoding API key

**Returns:**
A Promise that resolves to either:

**Success (GeocodingResult):**

```javascript
{
  latitude: number,
  longitude: number,
  formatted_address: string,
  country?: string,
  postal_code?: string
}
```

**Failure (GeocodingError):**

```javascript
{
  message: string,
  field: string // 'address', 'coordinates', or 'input'
}
```

**Example with Error Handling:**

<CodeGroup>
  ```javascript JavaScript
  import { performGeocoding } from "@flatfile/plugin-enrich-geocode";

  async function findCoordinates(apiKey) {
    const result = await performGeocoding({ address: "Eiffel Tower" }, apiKey);
    
    if ('message' in result) {
      console.error(`Geocoding failed on field '${result.field}': ${result.message}`);
    } else {
      console.log(`Coordinates: ${result.latitude}, ${result.longitude}`);
    }
  }
  ```

  ```typescript TypeScript
  import { performGeocoding } from "@flatfile/plugin-enrich-geocode";

  async function findCoordinates(apiKey: string) {
    const result = await performGeocoding({ address: "Eiffel Tower" }, apiKey);
    
    if ('message' in result) {
      console.error(`Geocoding failed on field '${result.field}': ${result.message}`);
    } else {
      console.log(`Coordinates: ${result.latitude}, ${result.longitude}`);
    }
  }
  ```
</CodeGroup>

## Notes

### API Key Requirement

A valid Google Maps Geocoding API key is required for this plugin to function. The plugin will look for the key in the environment variables as `GOOGLE_MAPS_API_KEY` or in Flatfile secrets with the name `GOOGLE_MAPS_API_KEY`.

### Data Enrichment and Sheet Configuration

Upon successful geocoding, the plugin will attempt to set values for the following fields on the record: `latitude`, `longitude`, `formatted_address`, `country`, and `postal_code`. Your Flatfile Sheet must be configured with these fields to store the enriched data. The latitude and longitude fields are configurable; the others are hardcoded.

### Error Handling Pattern

If the Google Maps API returns an error (e.g., `ZERO_RESULTS`, `REQUEST_DENIED`) or if the network request fails, the plugin will not halt the import process. Instead, it will add an error message to the specific record and field that caused the issue using `record.addError()`. This allows users to see which records failed to geocode and why directly in the Flatfile UI.

### Event Trigger

The plugin is designed to run on the `listener.on('commit:created')` event. This means it processes data after a user has reviewed their data and clicked the final submit button, but before the data is sent to its final destination.
