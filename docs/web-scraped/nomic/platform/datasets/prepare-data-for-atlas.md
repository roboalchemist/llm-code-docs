# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/prepare-data-for-atlas

You get get started with Datasets by uploading your data. Dataset will automatically generate embeddings and index your data for retrieval and visualization.

The Atlas unstructured data visualization activates on any dataset store in the platform.

For programmatic dataset uploads, our Python SDK allows you to upload datasets directly from Python code.

## File and Format Requirements​

- Supported formats: CSV, TSV, JSON, or JSONL
- Column names:

For CSV/TSV: Files must include a header row specifying column names
For JSON/JSONL: Each object must use consistent field names
- For CSV/TSV: Files must include a header row specifying column names
- For JSON/JSONL: Each object must use consistent field names
- Content: At least one column/field to embed, containing either natural language text or a path to an image.
- Size limits: at least 20 rows (and for free users, at most 250,000 rows), with a total file size under 1GB
## Best Practices​

### Null Data​

When uploading numeric data that contains missing values, the proper formatting is:

- JSON/JSONL: Use the null keyword (without quotes) for missing values
```
null
```

- CSV/TSV: Leave cells empty to represent NULL values
Important: If a column contains mixed data types (such as numbers and text like "n/a"), we will interpret the entire column as string data. For optimal analysis in Atlas, ensure your numeric columns contain only numbers and properly formatted NULL values.

### Date and Time Formatting​

For consistent handling of temporal information, we recommend using ISO 8601 format: YYYY-MM-DD for dates (e.g., 2024-03-14) and YYYY-MM-DDThh:mm:ssZ for timestamps (e.g., 2024-03-14T15:30:00Z).

```
YYYY-MM-DD
```

```
2024-03-14
```

```
YYYY-MM-DDThh:mm:ssZ
```

```
2024-03-14T15:30:00Z
```

Our CSV parser will attempt to detect other date formats, but using the ISO standard ensures the most reliable parsing.

### Include All Available Metadata​

When preparing your dataset, include all relevant metadata fields since we can efficiently handle datasets with many columns. These additional columns provide valuable context and enable richer analysis through the data map controls. Consider including metadata like timestamps, categories, authors, status fields, IDs, ratings, and any other fields that could provide useful context or filtering capabilities.

### Date and Time Formatting​

For consistent handling of temporal information, convert all datetime fields to ISO 8601 format. Instead of using formats like 3/14/24 3:30 PM, use the standardized format 2024-03-14T15:30:00Z. This ensures that the data map can properly process and display temporal data across your dataset.

```
3/14/24 3:30 PM
```

```
2024-03-14T15:30:00Z
```

### Unnest Data​

If your data contains nested structures or objects (like JSON objects), unnest them into separate columns before uploading to Atlas. For example, instead of having a single column containing {"status": "open", "priority": 3}, split it into two separate columns: status with value "open" and priority with value 3. This flat structure allows for better filtering and analysis in Atlas.

```
{"status": "open", "priority": 3}
```

```
status
```

```
priority
```

## Adding Custom Positioning Coordinates​

Dataset visualizations can display your rows using custom coordinate systems provided in your dataset, instead of relying solely on the default projection based on embeddings. This is useful for visualizing data with inherent spatial properties or pre-defined layouts.

### Custom X-Y Coordinates​

To use custom X-Y coordinates, include paired columns in your dataset containing the numerical X and Y values for each data point. Atlas recognizes the following naming patterns for these columns:

- Position_X and Position_Y
```
Position_X
```

```
Position_Y
```

- Position-X and Position-Y
```
Position-X
```

```
Position-Y
```

- Position.X and Position.Y
```
Position.X
```

```
Position.Y
```

- Position X and Position Y
```
Position X
```

```
Position Y
```

Example:

```
id,text,Position_X,Position_Y1,"Point A",10.5,20.12,"Point B",15.2,25.83,"Point C",12.0,22.5
```

If valid paired columns are detected, they will appear as selectable options (e.g., "Position XY") in the Position Mode dropdown within the map's View Settings. Multiple distinct X-Y pairs (e.g., Layout1_X, Layout1_Y, Layout2_X, Layout2_Y) are supported.

```
Position Mode
```

```
Layout1_X
```

```
Layout1_Y
```

```
Layout2_X
```

```
Layout2_Y
```

### Geospatial Coordinates​

For datasets containing geographical information, include columns with latitude and longitude values. Atlas recognizes the following naming patterns:

- lat and lon
```
lat
```

```
lon
```

- latitude and longitude
```
latitude
```

```
longitude
```

Example:

```
id,location_name,latitude,longitude1,"City Hall",40.7128,-74.00602,"Central Park",40.7850,-73.96823,"Statue of Liberty",40.6892,-74.0445
```

Atlas will automatically detect these columns and offer a geospatial projection mode in the Position Mode dropdown.

```
Position Mode
```

Currently, only one pair of latitude/longitude columns (one latitude column and one longitude column) is supported per dataset.

## Upload​

### Visit Platform Dashboard​

Once you are signed up for Atlas and logged in, visit https://atlas.nomic.ai/data to open your Atlas Dashboard.

Alteratively, on the Nomic Atlas homepage click the Dashboard button.

```
Dashboard
```

Your organization's data maps live here. For new organizations with no datasets yet, you will be prompted to get started uploading your first dataset.

### Create New Dataset​

If you have no datasets yet, visiting your dashboard will prompt you to create one.

If you have existing datasets,
click  to create a new dataset.

You can upload text to Atlas with dataset connectors, by dragging your file in directly, or by using the Atlas Python SDK.

If you are using a connector or dragging in your own file, make sure to inspect the auto-inferred Name,
Embedding Field,
and dataset settings (e.g., whether to use a multilingual model when embedding, which we deactivate in the above video) before clicking . Your map will take a few minutes to load, requiring more time the more data you upload.

### Upload Options​

These options are available when uploading data in the Atlas UI. More options are available when you upload data with the Atlas Python SDK.

#### Dataset Name​

The name which will be used for your data map's display in the Dashboard, as well as its URL.

#### Dataset Description​

The description for your dataset visible within the dataset information menu and your dataset settings.

#### Field to Embed​

The attribute of your dataset used to arrange the points in the Atlas map.

Atlas automatically selects the best field for embedding from the dataset you choose, but you can choose a different field.

The embedding field determines how the datapoints will get arranged as a map in Atlas: data that show up as neighboring points in the data map will have similar semnatic content in this field/column from your dataset (and thus similar embeddings via the embedding model). Typically, you will want this to be the text column from your data, as opposed to non-semantic content like IDs or numerical metadata.

#### Embedding Model​

Which embedding model to use, which will group data points together based on semantic meaning:

• English (nomic-embed-text-v1.5): If you use this model and your data contains multiple languages, this model will create distinct clusters of text depending on the language used.

• Multilingual (gte-multilingual-base): If you use this model and your data contains multiple languages, this model will cluster text regardless of language used.

#### Dataset Visibility​

For Business & Enterprise accounts, you can make a map private so that they are not publicly accessible, and only members of your organization will be able to find/access the map.

• Public: anyone can view

• Private: only your fellow organization members can view

• Restricted: manually grant access

## Data Preparation Guides & Examples​

View our data export guides to see walkthroughs of getting data from common sources and platforms into the right format for Atlas.

## CSV Parsing with DuckDB​

Atlas uses DuckDB for parsing and processing CSV files, which provides robust automatic type detection capabilities. When you upload a CSV file, DuckDB automatically:

- Detects the dialect of your CSV file (delimiter, quoting rules, escape characters)
- Infers the data types of each column
- Detects whether the file has a header row
### Type Detection​

Atlas uses DuckDB to convert values in each column to candidate types, following this priority order:

- BIGINT (integer)
- DOUBLE (floating point)
- TIMESTAMP
- VARCHAR (string)
A column is assigned the highest-priority type that successfully converts all sampled values. If values cannot be converted to a particular type, that candidate type is eliminated. VARCHAR is always the fallback type.

For more details on DuckDB's CSV parsing and type inference, visit the DuckDB CSV auto detection documentation.

- File and Format Requirements
- Best PracticesNull DataDate and Time FormattingInclude All Available MetadataDate and Time FormattingUnnest Data
- Null Data
- Date and Time Formatting
- Include All Available Metadata
- Date and Time Formatting
- Unnest Data
- Adding Custom Positioning CoordinatesCustom X-Y CoordinatesGeospatial Coordinates
- Custom X-Y Coordinates
- Geospatial Coordinates
- UploadVisit Platform DashboardCreate New DatasetUpload Options
- Visit Platform Dashboard
- Create New Dataset
- Upload Options
- Data Preparation Guides & Examples
- CSV Parsing with DuckDBType Detection
- Type Detection
