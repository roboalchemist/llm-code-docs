# Source: https://docs.roboflow.com/developer/rest-api/annotation-insights/annotation-insights-legacy-endpoint.md

# Annotation Insights (Legacy Endpoint)

{% hint style="danger" %}
This endpoint will soon be deprecated. Please upgrade to the new endpoint: Annotation Stats v2
{% endhint %}

Roboflow provides statistics on annotations associated with your workspace and projects. You can view annotation insights in the Roboflow dashboard and through the REST API.

{% tabs %}
{% tab title="REST API" %}
To retrieve annotation insights for a workspace, make a GET request to the following endpoint:

```url
https://api.roboflow.com/workspace-stats
```

This endpoint accepts the following URL parameters:

* `api_key`: API key for the workspace from which to retrieve statistics.
* `start`: Retrieve statistics starting from this date (accepts a number in milliseconds).
* `end`: Retrieve statistics ending from this date (accepts a number in milliseconds).
* `includeTicks`: When true, include graphing ticks.
* `projectId`: Retrieve data only for the specified project.
* `rawData`: When true, returns raw (un-aggregated) data for unique images labeled.
* `limit`: The number of records to return. `rawData` must be `true`.
* `offset`: Offset of records to be returned. `rawData` must be `true`.

This endpoint returns a payload with the following structure:

```json
{
    "data": {
        "last_updated": "2023-01-01T20:07:21.057Z",
        "data": [
            {
                "projectId": "project123",
                "projectName": "My CV Project",
                "total_time_spent_annotating_minutes": 24.09,
                "total_images_labeled": 10,
                "total_boxes_created": 0,
                "seconds_per_image": 31,
                "num_images_marked_null": 0,
                "acceptance_rate": 0
            }
        ],
        "labelers": [
            {
                "id": "labelerId123",
                "displayName": "Lenny Raccoon",
                "email": "lenny@roboflow.foo"
            }
        ],
        // if includeTicks=true
        "ticks": [
            {
                start_ms": 1656929228959,
                "end_ms": 1660867628959,
                "values": {
                    "labelerId123": {
                        "total_time_spent_annotating_minutes": 133.38,
                        "total_images_labeled": 983,
                        "total_boxes_created": 1432,
                        "seconds_per_image": 0
                    }
                }
            }
        ]
    }
}
```

{% endtab %}
{% endtabs %}
