# Source: https://docs.roboflow.com/developer/rest-api/list-image-batches.md

# List Image Batches

You can get a list of the batches that your uploaded images are grouped into by making the following GET request:

```bash
curl --location --request GET 'https://api.roboflow.com/${WORKSPACE}/${PROJECT}/batches?api_key=${ROBOFLOW_API_KEY}'
```

This request will return a response in the following format:

```json
{
    "batches": [
        {
            "name": "Uploaded on 11/22/22 at 1:39 pm",
            "numJobs": 2,
            "images": 115,
            "uploaded": {
                "_seconds": 1669146024,
                "_nanoseconds": 818000000
            },
            "id": "<BATCH_ID 1>"
        },
        {
            "numJobs": 0,
            "images": 11,
            "uploaded": {
                "_seconds": 1669236873,
                "_nanoseconds": 47000000
            },
            "name": "Upload via API",
            "id": "<BATCH_ID 2>"
        }
    ]
}
```

To get info for a specific Batch only, you can add the batch Id to the path of the request:

```bash
curl --location --request GET 'https://api.roboflow.com/${WORKSPACE}/${PROJECT}/batches/${BATCH_ID}?api_key=${ROBOFLOW_API_KEY}'
```

This request will return data in the following format:

```json
{
    "name": "Uploaded on 11/22/22 at 1:39 pm",
    "uploaded": {
        "_seconds": 1669146024,
        "_nanoseconds": 818000000
    },
    "images": 115,
    "numJobs": 2,
    "id": "<BATCH_ID>"
}
```
