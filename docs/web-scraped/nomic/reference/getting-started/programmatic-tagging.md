# Nomic Documentation

Source: https://docs.nomic.ai/reference/getting-started/programmatic-tagging

Atlas allows you to add custom tags to your data, both directly within the map interface as well as programmatically via the Atlas API. This enables you to add or remove tags from specific data points based on their IDs.

See the API reference for more details.

## Add Tags​

You can apply or remove a tag for a specific set of data points using their unique identifiers. This is useful for integrating tagging into automated workflows or external systems.

The endpoint requires the projection_id of your map, the desired tag_name, and an array of ids corresponding to the data points you want to modify.

```
projection_id
```

```
tag_name
```

```
ids
```

The examples below use a projection_id (52fcac24-9ab0-4545-8065-0d2fe8350d09) for a data map of research paper excerpts. We demonstrate how to add the tag "New Tag" to data points with the provided IDs.

```
projection_id
```

```
52fcac24-9ab0-4545-8065-0d2fe8350d09
```

```
curl -L "https://api-atlas.nomic.ai/v1/query/update/tag/ids" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "52fcac24-9ab0-4545-8065-0d2fe8350d09",    "tag_name": "New Tag",    "ids": ["0", "89", "295"],    "operation": "add"}'
```

You can find the projection_id on your dataset preview page, located at atlas.nomic.ai/data/<YOUR_ORG_NAME>/<YOUR_DATASET_NAME>.

```
projection_id
```

```
atlas.nomic.ai/data/<YOUR_ORG_NAME>/<YOUR_DATASET_NAME>
```

Upon successful execution, the API will return a JSON object confirming the operation:

```
{'success': True, 'tag_id': 'af1fb708-f538-45bf-9de8-ffc0983af10f', 'points_tagged': 3}
```

- success: A boolean indicating if the operation was successful.
```
success
```

- tag_id: The UUID of the tag that was applied or removed.
```
tag_id
```

- points_tagged: The number of data points that were successfully processed. Note that this might be less than the number of IDs provided if some IDs were not found in the dataset.
```
points_tagged
```

Note: you need to specify the id_field parameter if you are trying to add tags to a dataset with a unique_id_field that you have configured, for example:

```
id_field
```

```
unique_id_field
```

```
curl -L "https://api-atlas.nomic.ai/v1/query/update/tag/ids" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "52fcac24-9ab0-4545-8065-0d2fe8350d09",    "tag_name": "New Tag",    "id_field": "my_unique_id_field",    "ids": ["0", "89", "295"],    "operation": "add"}'
```

## Remove Tags​

This example shows how to remove the tag "New Tag Review" from the data point with ID 295, using the default unique ID field configured for the dataset.

```
295
```

```
curl -L "https://api-atlas.nomic.ai/v1/query/update/tag/ids" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "52fcac24-9ab0-4545-8065-0d2fe8350d09",    "tag_name": "New Tag",    "ids": ["295"],    "operation": "remove"}'
```

- Add Tags
- Remove Tags
