# Source: https://docs.roboflow.com/developer/rest-api/manage-images/delete-an-image-from-a-dataset.md

# Delete an Image from a Dataset

You can remove images from a Dataset using the REST API.

{% tabs %}
{% tab title="REST API" %}
To remove images from a Dataset, make a DELETE request to the following API endpoint, passing the image IDs in the endpoint.

```url
https://api.roboflow.com/:workspace/:project/images
```

Here is an example request to the API to remove images

```bash
curl "https://api.roboflow.com/my-workspace/my-project/images?api_key=$ROBOFLOW_API_KEY" \
  -X DELETE \
  -H "Content-Type: application/json" \
  -d '{"images": ["1", "2"]}'
```

This endpoint returns a 204 status if the operation was successful.
{% endtab %}
{% endtabs %}
