# Source: https://docs.roboflow.com/developer/rest-api/manage-images/get-details-about-an-image.md

# Get Details About an Image

You can fetch details of a specific image using the REST API.

To fetch details of a specific image, make a GET request to the following API endpoint.

```url
https://api.roboflow.com/:workspace/:project/images/:image_id
```

Here is an example request to the API to fetch the details of an image

```bash
curl -X GET "https://api.roboflow.com/my-workspace/my-project-name/images/image-id?api_key=$ROBOFLOW_API_KEY" \
-H 'Content-Type: application/json'
```

This endpoint returns a JSON object containing the following information about the image:

```typescript
{
    "image":
        "id": string,
        "name": string,
        "annotation": {
            "key": string,
            "width": number,
            "height": number,
            "boxes": Array<{
                "label": string,
                "x": number,
                "y": number,
                "width": number,
                "height": number
            }>
        },
        "labels": string[],
        "split": string,
        "tags": string[],
        "created": number,
        "urls": {
            "original": string,
            "thumb": string,
            "annotation": string
        },
        "embedding": number[]
    }
}
```
