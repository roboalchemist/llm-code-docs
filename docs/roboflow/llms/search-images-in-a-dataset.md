# Source: https://docs.roboflow.com/developer/rest-api/search-images-in-a-dataset.md

# Search Images in a Dataset

The Workspace Image Search API lets you ilst and search images within your workspace.

With this API, you can filter, sort, and perform semantic searches using a query string that is similar to [the image search feature in the Roboflow web application](https://docs.roboflow.com/developer/rest-api/manage-images/search-for-an-image).&#x20;

### Endpoint

To make a request to the API, send a `POST` request to the following endpoint:

```
https://api.roboflow.com/{WORKSPACE}/search/v1?api_key=API_KEY
```

Where `WORKSPACE` is your Workspace ID, and `API_KEY` is your API key.

[Learn how to find your Workspace ID](https://docs.roboflow.com/developer/authentication/workspace-and-project-ids).

[Learn how to find your API key.](https://docs.roboflow.com/developer/rest-api/authenticate-with-the-rest-api)

### Authentication

To access the API, you need to include your API key in the request. The API key should be passed as a query parameter.

Example: `?api_key={YOUR_API_KEY}`

### Request Format

#### Headers

* `Content-Type: application/json`

#### Body Parameters

* `query`: A string to filter, sort, or perform a semantic search. For Example: "nightime project:{my-project-url}" will filter for images in the `my-project-url` project and apply a semantic sort for images that match `nighttime`.
* `pageSize`: Number of results to return per page (default: 50).
* `fields`: List of fields to include in the response. Possible values are "tags", "width", "height", "filename", "aspectRatio", "split".

#### Example Request

```bash
curl --location 'https://api.roboflow.com/{WORKSPACE}/search/v1?api_key={API_KEY}' \
--header 'Content-Type: application/json' \
--data '{
    "query": "project:foo nightime",
    "pageSize": 10,
    "fields": ["tags", "width", "height", "filename", "aspectRatio", "split"]
}'

```

### Response Format

The response is a JSON object containing the following fields:

* `results`: An array of image objects.
* `total`: Total number of images found.
* `continuationToken`: A token for pagination.

#### Image Object Fields

depending on fields requested in the `fields` parameter:

* `id`: Unique identifier of the image.
* `projectData`: Object containing project-specific data.
  * `split`: Indicates the dataset split (e.g., "test").
  * `inDataset`: Boolean indicating if the image is in the dataset.
* `tags`: Array of tags associated with the image.
* `width`: Width of the image in pixels.
* `height`: Height of the image in pixels.
* `filename`: Name of the image file.
* `aspectRatio`: Aspect ratio of the image.

#### Pagination and `continuationToken`

The `continuationToken` returned in the response lets you scroll between pages that match a search result. When the `continuationToken` is included in a subsequent request, it fetches the next set of results.

To use the `continuationToken`, include it in the request body of your next API call. This will retrieve the next page of results based on your original query.

#### Project and Dataset Filters

In addition to all the filters available in [the in app dataset search](https://docs.roboflow.com/developer/rest-api/manage-images/search-for-an-image), the workspace wide search also support filters for `project` and `dataset` .  For example you can use a query like `project:foo project:bar` to find all images that are in both projects `foo` and `bar`.  \
\
A query like `dataset:foo`will return images in project `foo` that have been labeled and are added to the dataset in the project.
