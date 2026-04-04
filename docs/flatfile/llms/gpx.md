# Source: https://flatfile.com/docs/plugins/gpx.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GPX File Parser and Analyzer

> Automatically processes GPX (GPS Exchange Format) files to extract waypoints, tracks, routes, and calculate geographic statistics like distance and elevation gain.

This plugin automatically processes GPX (GPS Exchange Format) files attached to records in a Flatfile Sheet. When a commit is created, the plugin triggers on a specified Sheet. It reads GPX data from a designated field in a record, parses the XML content, and extracts waypoints, tracks, and routes.

The primary purpose is to enrich records with structured data derived from GPX files. It can convert the geographic data into a tabular format, calculate aggregate statistics like total distance and elevation gain, and extract metadata like the name and description of the activity.

Use cases include analyzing fitness activities, processing geographic survey data, or managing collections of GPS routes, where users provide GPX files and the system needs to automatically extract and display key information and statistics.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-enrich-gpx
```

## Configuration & Parameters

The plugin is configured with an object containing the following properties, which map to field slugs in your Sheet:

### Required Parameters

* **sheetSlug** (`string`): The slug of the sheet the plugin should operate on.
* **gpxFileField** (`string`): The field slug in the source record that contains the GPX file content as a string.

### Optional Parameters

* **removeDuplicatesField** (`string`): The field slug that acts as a boolean flag. If the value in this field for a given record is the string "true", duplicate points will be removed from the parsed data.
* **filterDatesField** (`string`): The field slug that acts as a boolean flag. If the value in this field for a given record is the string "true", the parsed data will be filtered by a date range.
* **startDateField** (`string`): The field slug containing the start date for filtering. This is only used if `filterDatesField` is set to "true". The value should be a valid date string.
* **endDateField** (`string`): The field slug containing the end date for filtering. This is only used if `filterDatesField` is set to "true". The value should be a valid date string.

### Default Behavior

By default, the plugin will parse the GPX file without removing duplicates or filtering by date. These processing steps are only activated if the corresponding fields (`removeDuplicatesField`, `filterDatesField`) in the record are explicitly set to the string "true". If filtering is enabled but the start or end date fields are empty or invalid, the date filter will not be applied.

## Usage Examples

### Basic Setup

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { enrichGpx } from "@flatfile/plugin-enrich-gpx";

  export default function (listener) {
    listener.use(enrichGpx(listener, {
      sheetSlug: 'gpx-data',
      gpxFileField: 'gpx_file',
      removeDuplicatesField: 'remove_duplicates',
      filterDatesField: 'filter_dates',
      startDateField: 'start_date',
      endDateField: 'end_date'
    }));
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { enrichGpx } from "@flatfile/plugin-enrich-gpx";

  export default function (listener: FlatfileListener) {
    listener.use(enrichGpx(listener, {
      sheetSlug: 'gpx-data',
      gpxFileField: 'gpx_file',
      removeDuplicatesField: 'remove_duplicates',
      filterDatesField: 'filter_dates',
      startDateField: 'start_date',
      endDateField: 'end_date'
    }));
  }
  ```
</CodeGroup>

### Complete Configuration Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { enrichGpx } from "@flatfile/plugin-enrich-gpx";

  export default function (listener) {
    const config = {
      sheetSlug: 'gpx-data', // The sheet to target
      gpxFileField: 'gpx_file', // Field with GPX string content
      removeDuplicatesField: 'remove_duplicates', // Field to enable/disable deduplication
      filterDatesField: 'filter_dates', // Field to enable/disable date filtering
      startDateField: 'start_date', // Field with the filter start date
      endDateField: 'end_date' // Field with the filter end date
    };

    listener.use(enrichGpx(listener, config));
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { enrichGpx, GpxParserConfig } from "@flatfile/plugin-enrich-gpx";

  export default function (listener: FlatfileListener) {
    const config: GpxParserConfig = {
      sheetSlug: 'gpx-data', // The sheet to target
      gpxFileField: 'gpx_file', // Field with GPX string content
      removeDuplicatesField: 'remove_duplicates', // Field to enable/disable deduplication
      filterDatesField: 'filter_dates', // Field to enable/disable date filtering
      startDateField: 'start_date', // Field with the filter start date
      endDateField: 'end_date' // Field with the filter end date
    };

    listener.use(enrichGpx(listener, config));
  }
  ```
</CodeGroup>

### Using Utility Functions

The plugin exports several utility functions that can be used independently for custom data processing tasks:

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { calculateDistance } from "@flatfile/plugin-enrich-gpx";

  // Define two waypoints
  const point1 = { latitude: 40.7128, longitude: -74.0060 }; // New York City
  const point2 = { latitude: 34.0522, longitude: -118.2437 }; // Los Angeles

  // Calculate the distance between them
  const distanceInKm = calculateDistance(point1, point2);

  console.log(`The distance is approximately ${distanceInKm.toFixed(2)} km.`);
  // Expected output: The distance is approximately 3944.42 km.
  ```

  ```typescript TypeScript theme={null}
  import { calculateDistance, Waypoint } from "@flatfile/plugin-enrich-gpx";

  // Define two waypoints
  const point1: Waypoint = { latitude: 40.7128, longitude: -74.0060 }; // New York City
  const point2: Waypoint = { latitude: 34.0522, longitude: -118.2437 }; // Los Angeles

  // Calculate the distance between them
  const distanceInKm: number = calculateDistance(point1, point2);

  console.log(`The distance is approximately ${distanceInKm.toFixed(2)} km.`);
  // Expected output: The distance is approximately 3944.42 km.
  ```
</CodeGroup>

## API Reference

### enrichGpx(listener, config)

The main plugin entry point that configures and attaches a record hook to a Flatfile listener.

**Parameters:**

* `listener`: FlatfileListener - The Flatfile listener instance to attach the hook to
* `config`: GpxParserConfig - Configuration object containing field mappings

**Returns:** void

### calculateDistance(point1, point2)

Calculates the great-circle distance between two geographical points using the Haversine formula.

**Parameters:**

* `point1`: Waypoint - Object with `latitude` and `longitude` properties
* `point2`: Waypoint - Object with `latitude` and `longitude` properties

**Returns:** number - The distance between the two points in kilometers

### removeDuplicatePoints(points)

Removes duplicate waypoints from an array based on latitude, longitude, elevation, and time.

**Parameters:**

* `points`: Waypoint\[] - Array of waypoint objects

**Returns:** Waypoint\[] - New array with duplicate waypoints removed

### filterByDateRange(points, startDate, endDate)

Filters waypoints to include only those within a specified date range.

**Parameters:**

* `points`: Waypoint\[] - Array of waypoint objects with optional `time` property
* `startDate`: Date - Start of the date range
* `endDate`: Date - End of the date range

**Returns:** Waypoint\[] - Filtered array of waypoints

### calculateStatistics(tabularData)

Calculates total distance and cumulative positive elevation gain for a path of waypoints.

**Parameters:**

* `tabularData`: Waypoint\[] - Sorted array of waypoint objects

**Returns:** object - Object with `totalDistance` (km) and `elevationGain` (meters) properties

### convertToTabularFormat(waypoints, tracks, routes)

Merges separate arrays of waypoints, tracks, and routes into a single, flat array sorted by time.

**Parameters:**

* `waypoints`: Waypoint\[] - Array of waypoint objects
* `tracks`: Track\[] - Array of track objects
* `routes`: Route\[] - Array of route objects

**Returns:** Waypoint\[] - Single, sorted array containing all points

## Troubleshooting

### Common Issues

* **Data not processing**: Ensure the `sheetSlug` in the configuration exactly matches the slug of your target Sheet
* **Field mapping errors**: Verify that all field slugs in the configuration match the field keys in your Sheet template
* **Invalid GPX content**: Check that the `gpxFileField` contains valid GPX XML content
* **Date filtering not working**: Ensure the `filterDatesField` contains the string "true" and that date fields contain valid date strings

### Error Handling

The plugin includes comprehensive error handling:

* **Missing GPX content**: Adds error message 'GPX file content is required' to the `gpxFileField`
* **Invalid XML**: Adds generic error message 'Failed to parse GPX content' to the `gpxFileField`
* **Processing continues**: Records are always returned to ensure other records can be processed

## Notes

### Important Considerations

* The plugin operates on the `commit:created` event using a `recordHook`
* GPX data must be provided as a complete XML string within the specified field
* Boolean-like options are controlled by the string value "true", not native boolean types
* The plugin will overwrite values in target fields with extracted GPX data
* Processing steps (deduplication, date filtering) are only activated when explicitly enabled

### Limitations

* Does not handle file uploads directly, only processes string content from uploads
* Requires valid GPX XML format for successful parsing
* Date filtering requires valid date strings in the specified format
