# Source: https://docs.roboflow.com/developer/rest-api/model-monitoring/retrieve-statistics-about-deployed-models-in-a-workspace.md

# Retrieve Statistics About Deployed Models in a Workspace

You can retrieve Model Monitoring statistics using the Model Monitoring API. This endpoint currently accepts 3 query params (in addition to the api\_key):

* **startTime**: DateTime string in the format "YYYY-MM-DD HH:mm:ss". If empty, will default to 24 hours from the time of the request
* **endTime**: DateTime string in the format "YYYY-MM-DD HH:mm:ss". If empty, will default to the current time of the request
* **modelNames**: A string of comma separate model names, i.e. "?modelNames=license-plate-detector,truck-detector"

### Stats

`GET /:workspace/inference-stats`

### **Example Request:**

```
curl --location --request GET 'https://api.roboflow.com/${WORKSPACE}/inference-stats?api_key=<your_api_key>&startTime=&endTime=' \
```

**Example Response:**

{% tabs %}
{% tab title="200" %}

```json
{
    "num_inferences": 120,
    "prev_num_inferences": 290,
    "num_errors": 0,
    "prev_num_errors": 0,
    "avg_confidence": 0.92541713388321,
    "prev_avg_confidence": 0.8610920182589827,
    "avg_response_time": 0.16464362986438943,
    "prev_avg_response_time": 0.043521592255159045,
    "inference_stats": [
        {
            "model_name": "cards-3z9gn",
            "predicted_class": "Playingcards",
            "num_inferences": 106,
            "prev_num_inferences": 190,
            "num_errors": null,
            "prev_num_errors": null,
            "avg_confidence": 0.931105958703923,
            "prev_avg_confidence": 0.935741652940449,
            "avg_response_time": 0.176652773857811,
            "prev_avg_response_time": 0.05487422056841488,
            "median_confidence": 0.9268901944160461,
            "class_count": 211,
            "deployment_types": "hosted",
            "inference_server_versions": "0.15.3,0.16.0",
            "model_num_inferences": 107,
            "prev_model_num_inferences": 190
        },
        {
            "model_name": "cards-3z9gn",
            "predicted_class": "",
            "num_inferences": 1,
            "prev_num_inferences": null,
            "num_errors": null,
            "prev_num_errors": null,
            "avg_confidence": 0,
            "prev_avg_confidence": null,
            "avg_response_time": 0,
            "prev_avg_response_time": null,
            "median_confidence": 0,
            "class_count": 1,
            "deployment_types": "hosted",
            "inference_server_versions": "0.16.0",
            "model_num_inferences": 107,
            "prev_model_num_inferences": null
        },
        {
            "model_name": "hard-hat-sample-8j2w3",
            "predicted_class": "head",
            "num_inferences": null,
            "prev_num_inferences": 100,
            "num_errors": null,
            "prev_num_errors": null,
            "avg_confidence": null,
            "prev_avg_confidence": 0.6933842897415161,
            "avg_response_time": null,
            "prev_avg_response_time": 0.021951598459972955,
            "median_confidence": null,
            "class_count": null,
            "deployment_types": "hosted",
            "inference_server_versions": "0.15.1",
            "model_num_inferences": null,
            "prev_model_num_inferences": 100
        },
        {
            "model_name": "hard-hat-sample-8j2w3",
            "predicted_class": "helmet",
            "num_inferences": null,
            "prev_num_inferences": 100,
            "num_errors": null,
            "prev_num_errors": null,
            "avg_confidence": null,
            "prev_avg_confidence": 0.7451311349868774,
            "avg_response_time": null,
            "prev_avg_response_time": 0.021951598459972955,
            "median_confidence": null,
            "class_count": null,
            "deployment_types": "hosted",
            "inference_server_versions": "0.15.1",
            "model_num_inferences": null,
            "prev_model_num_inferences": 100
        },
        {
            "model_name": "coco",
            "predicted_class": "car",
            "num_inferences": 11,
            "prev_num_inferences": null,
            "num_errors": null,
            "prev_num_errors": null,
            "avg_confidence": 0.91790372133255,
            "prev_avg_confidence": null,
            "avg_response_time": 0.0647244118180817,
            "prev_avg_response_time": null,
            "median_confidence": 0.91790372133255,
            "class_count": 22,
            "deployment_types": "hosted",
            "inference_server_versions": "0.15.3",
            "model_num_inferences": 11,
            "prev_model_num_inferences": null
        },
        {
            "model_name": "license-plate-recognition-rxg4e",
            "predicted_class": "License_Plate",
            "num_inferences": 2,
            "prev_num_inferences": null,
            "num_errors": null,
            "prev_num_errors": null,
            "avg_confidence": 0.8706022202968597,
            "prev_avg_confidence": null,
            "avg_response_time": 0.07911215199999333,
            "prev_avg_response_time": null,
            "median_confidence": 0.8706022202968597,
            "class_count": 2,
            "deployment_types": "hosted",
            "inference_server_versions": "0.15.3",
            "model_num_inferences": 2,
            "prev_model_num_inferences": null
        }
    ]
}
```

{% endtab %}
{% endtabs %}
