# Source: https://docs.roboflow.com/developer/rest-api/manage-images/list-add-and-remove-image-tags.md

# List, Add, and Remove Image Tags

You can assign tags to specific images on Roboflow using the REST API

{% tabs %}
{% tab title="REST API" %}
To add, remove, and set tags to images hosted on Roboflow, make POST request to the following API endpoint. Use the Search API to retrieve the image ID associated with the image name:

```url
https://api.roboflow.com/:workspace/:project/images/:image_id/tags
```

Here is an example request to the API (can "add", "remove", or "set" a tag):

```bash
curl -X POST "https://api.roboflow.com/my-workspace/my-project-name/images/image-id/tags?api_key=$ROBOFLOW_API_KEY" \
-H 'Content-Type: application/json' \
--data \
'{
    "operation": "add",
    "tags": "image_tag_test"
}'
```

This endpoint accepts the following values in the POST body:

```json
{
     // // options are ["add", "remove", "set"]
     "operation": string,
     
     // array of strings of the tags
     "tags": string[],
     
}
```

The API will add the tag to the specified image in Roboflow (remember to pass in the image ID to the post request and not the image name).
{% endtab %}
{% endtabs %}
