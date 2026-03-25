# Source: https://docs.roboflow.com/developer/python-sdk/search-for-an-image.md

# Source: https://docs.roboflow.com/developer/rest-api/manage-images/search-for-an-image.md

# Search for an Image

You can search for images hosted on Roboflow using the Python SDK and REST API.

To search for images hosted on Roboflow, make POST request to the following API endpoint:

```url
https://api.roboflow.com/:workspace/:project/search
```

Here is an example request to the API:

```bash
curl -X POST "https://api.roboflow.com/my-workspace/my-project-name/search?api_key=$ROBOFLOW_API_KEY" \
-H 'Content-Type: application/json' \
--data \
'{
    "like_image": "image_id",
    "in_dataset": true,
    "limit": 125,
}'
```

This endpoint accepts the following values in the POST body:

```json
{
     // when provided, provides results sorted by semantic similarity
     "like_image": string,
     
     // when provided, provides results sorted by semantic similarity
     "prompt": string,
     
     // defaults to 0
     "offset": int,
     
     // default to 50 (max: 250)
     "limit": int,
     
     // when present, filters images that have the provided tag
     "tag": string,
     
     // when present, filters images that have the provided class name
     "class_name": string,
     
     // when present, filters images that are in the provided project
     "in_dataset": string,
     
     // when present, returns only images that are in any batch
     "batch": boolean,
     
     // when present, returns only images present in the provided batch
     "batch_id": string,

     // when present, returns only images that are in any annotation job
     "annotation_job": boolean,

     // when present, returns only images present in the provided annotation job
     "annotation_job_id": string,
     
     // specify the fields to return, defaults to ["id", "created"]
     // options are ["id", "name", "annotations", "labels", "split", "tags", "owner", "embedding", "created"]
     "fields": string[]
}
```

The search API will return a response with the following structure. The values available will vary depending on the additional `fields` you have specified:

```json
{
    "offset": 0,
    "total": 292,
    "results": [
        {
            "id": "image123",
            "name": "humpbackwhale.jpg",
            "owner": "owner123",
            "annotations": {
                "count": 5,
                "classes": {
                    "whale": 1,
                    "fish": 4
                }
            },
            "labels": [],
            "tags": [
                "cam_x13"
            ]
        }
        // ... etc.
    ]
}
```

{% tabs %}
{% tab title="Python SDK" %}
To search for images using the Python SDK, use the `search_all()` method. The method accepts a `prompt` value, which is the search query you want to send to Roboflow.

See the search filter documentation for more information on advanced filters supported in searches.

```python
import roboflow

roboflow.login()

rf = roboflow.Roboflow()

project = rf.project("PROJECT_ID")

records = []

for page in project.search_all(
    prompt="mug",
    like_image = image_id,
    offset = 0,
    limit = 100,
    tag = "tag",
    class_name = "class_name",
    in_dataset = True,
    batch = False,
    batch_id = "batch_id",
    annotation_job = False,
    annotation_job_id = "annotation_job_id",
    fields = ["id", "created", "name", "labels"],
):
    records.extend(page)

print(len(records))
```

{% endtab %}

{% tab title="REST API" %}

{% endtab %}
{% endtabs %}
