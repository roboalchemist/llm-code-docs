# Source: https://docs.roboflow.com/developer/rest-api/model-monitoring/attach-metadata-to-an-inference.md

# Attach Metadata to an Inference

You can attach a custom metadata value to each inference result and view it in the Model Monitoring dashboard.

## Applications

Custom metadata has a number of applications, from tagging data to make it easier to find and organize, to adding additional context to an inference result. For example, let's suppose you're an automotive manufacturer with three factories across the United States. A few things you might consider adding to your inference results include location, which production-line an image was taken on, whether a certain operation passed or failed, and the expected result of the inference (like `color=blue`).

## Create Custom Metadata

<mark style="color:green;">`POST`</mark> `/:workspace/inference-stats/metadata`

Attaches additional data to an inference result that will be displayed in the Model Monitoring dashboard.

When you make an inference request with Roboflow's Inference Container or Hosted Inference API, you will receive an `inference_id` in the response. Using this ID, you can add it to the `inference_ids` array as shown below to attach your metadata to it. The `field_name` is a name for the property, and the `value` is the value.

For example, if I want to attach a geographic location to my inference results, I would set the `field_name` to "location" and the `value` would be a location like "united\_states".

**Note:** The values for `field_name` and `field_value` are completely user-defined. Be sure to keep the formatting consistent, including the letter case. For example `field_name: "my_location"` and `field_name: "My_location"` will be treated as two separate metadata values.

### **Example Request:**

```
curl --location --request POST 'https://api.roboflow.com/${WORKSPACE}/inference-stats/metadata' \
--header 'Content-Type: application/json' \
--data-raw '{
    "api_key": "<your_api_key>",
    "data": [
        {
            "inference_ids": ["a12a19a9-a933-44c9-970c-a55ea03bb453"],
            "field_name": "camera_location",
            "field_value": "canada"
        },
        {
            "inference_ids": ["accf0af9-bdf0-4b22-8106-6988d4cada5a"],
            "field_name": "camera_location",
            "field_value": "emea"
        }
    ]
}'
```

**Headers:**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Body:**

| Name   | Type             | Description                                                                                                         |
| ------ | ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| `data` | Array\<Metadata> | <p>{</p><p>"inference\_ids": Array\<string>;</p><p>"field\_name": string;</p><p>"field\_value": string;</p><p>}</p> |

**Response:**

{% tabs %}
{% tab title="200" %}

```json
{
  "status": "ok"
}
```

{% endtab %}

{% tab title="400" %}

```json
{
  "error": "Invalid request"
}
```

{% endtab %}
{% endtabs %}

### **Example Using Python:**

<pre><code><strong>import requests
</strong>from inference_sdk import InferenceHTTPClient

# Change these
api_key = "YOUR_API_KEY"
workspace = "YOUR_WORKSPACE_ID"

# Default values
field_name = "test_field"
field_value = "test_value"
model_id = "coco/24"
image_path = "https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg"
api_url = "https://detect.roboflow.com"

# Initialize the client
print("Initializing the InferenceHTTPClient...")
client = InferenceHTTPClient(api_url=api_url, api_key=api_key)

# Run the inference
result = client.infer(image_path, model_id=model_id)
print("Result:", result)

# Extract the inference ID from the result
inference_id = result.get('inference_id')
if inference_id:
    print("Inference ID:", inference_id)
else:
    raise ValueError("Inference ID not found in the response.")

url = f"https://api.roboflow.com/{workspace}/inference-stats/metadata"

# Set the headers and data for the POST request
headers = {
    "Content-Type": "application/json"
}
data = {
    "api_key": api_key,
    "data": [
        {
            "inference_ids": [inference_id],
            "field_name": field_name,
            "field_value": field_value
        }
    ]
}

# Make the POST request to attach the custom metadata
response = requests.post(url, headers=headers, json=data)

# Check the response status
if response.status_code == 200:
    print("Custom metadata attached successfully:", response.json())
else:
    print("Failed to attach custom metadata:", response.text)
</code></pre>
