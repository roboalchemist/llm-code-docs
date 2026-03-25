# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/supported-models/sam3.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/supported-models/sam3.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/supported-models/sam3.md

# Source: https://docs.roboflow.com/deploy/supported-models/sam3.md

# SAM3

We support Meta's [Segment Anything Model 3](https://github.com/facebookresearch/sam3) inferencing via our [Serverless Hosted API](https://docs.roboflow.com/deploy/serverless-hosted-api-v2). We offer two different SAM3 endpoints:

* [Promptable concept segmentation](#post-sam3-concept_segment) (**PCS**), segmentation using **text prompts**
* [Promptable visual segmentation](#post-sam3-visual_segment) (**PVS**), interactive segmentation using **points/boxes**

## Code samples

#### PCS Code Sample

Below is a code sample that uses PCS endpoint for SAM3 inferencing. User needs to pass [Roboflow's API Key](https://app.roboflow.com/settings/api) via  `API_KEY` env variable.

```python
import os
import requests
import base64
import cv2
import numpy as np

# From "https://media.roboflow.com/notebooks/examples/dog.jpeg"
image = cv2.imread("./dog.jpeg")

# Encode image as base64
_, buffer = cv2.imencode('.jpg', image)
image_base64 = base64.b64encode(buffer).decode('utf-8')

payload = {
    "image": { "type": "base64", "value": image_base64 },
    "prompts": [
        { "type": "text", "text": "person" },
        { "type": "text", "text": "dog" },
    ],
    "output_prob_thresh": 0.5,
    "format": "polygon",
}

url = "https://serverless.roboflow.com/sam3/concept_segment?api_key=" + os.getenv("API_KEY")
response = requests.post(url, json=payload)
data = response.json()

for key in dat
    print(key) # Should be prompt_results and time
```

#### PVS Code Sample

See [Github Gist](https://gist.github.com/Erol444/4cbc33c6ac52d83c63f6f9d86ca8a7a4) for an interactive demo using OpenCV, which was used in this video:

{% embed url="<https://www.youtube.com/watch?v=01xrBzqHZ6c>" %}

## Endpoints

## SAM3 PCS (promptable concept segmentation)

> \*\*Concept Segmentation (Text Prompts)\*\*\
> \
> Allows you to segment objects using text prompts.\
> \
> \*\*Image Input\*\*: The \`image\` field accepts either:\
> \- \`{"type": "url", "value": "\<IMAGE\_URL>"}\` - A publicly accessible image URL\
> \- \`{"type": "base64", "value": "\<BASE64\_DATA>"}\` - Base64 encoded image data\
> \
> &#x20;\*\*Prompts\*\*: Each prompt in the \`prompts\` array should have \`type: "text"\` and a \`text\` field with the object description.

```json
{"openapi":"3.1.0","info":{"title":"Roboflow SAM3 API","version":"0.64.4"},"servers":[{"url":"https://serverless.roboflow.com"}],"paths":{"/sam3/concept_segment":{"post":{"summary":"SAM3 PCS (promptable concept segmentation)","description":"**Concept Segmentation (Text Prompts)**\n\nAllows you to segment objects using text prompts.\n\n**Image Input**: The `image` field accepts either:\n- `{\"type\": \"url\", \"value\": \"<IMAGE_URL>\"}` - A publicly accessible image URL\n- `{\"type\": \"base64\", \"value\": \"<BASE64_DATA>\"}` - Base64 encoded image data\n\n **Prompts**: Each prompt in the `prompts` array should have `type: \"text\"` and a `text` field with the object description.","operationId":"sam3_segment_image_sam3_concept_segment_post","parameters":[{"name":"api_key","in":"query","required":true,"schema":{"type":"string","title":"API Key"},"description":"Your Roboflow API Key. Get one at https://app.roboflow.com/settings/api"}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/Sam3SegmentationRequest"}}}},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Sam3SegmentationResponse"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"Sam3SegmentationRequest":{"properties":{"image":{"$ref":"#/components/schemas/InferenceRequestImage","description":"The image to be segmented."},"prompts":{"items":{"$ref":"#/components/schemas/Sam3Prompt"},"type":"array","minItems":1,"title":"Prompts","description":"List of prompts (text and/or visual)"},"format":{"type":"string","title":"Format","description":"One of 'polygon', 'rle'","default":"polygon"},"image_id":{"type":"string","title":"Image Id","description":"Optional ID for caching embeddings."},"output_prob_thresh":{"type":"number","title":"Output Prob Thresh","description":"Score threshold for outputs.","default":0.5},"model_id":{"type":"string","title":"Model Id","description":"The model ID of SAM3. Use 'sam3/sam3_final' to target the generic base model.","default":"sam3/sam3_final"},"nms_iou_threshold":{"type":"number","title":"Nms Iou Threshold","description":"IoU threshold for cross-prompt NMS. If not set, NMS is disabled. Must be in [0.0, 1.0] when set."}},"type":"object","required":["image","prompts"],"title":"Sam3SegmentationRequest"},"InferenceRequestImage":{"properties":{"type":{"type":"string","title":"Type","description":"The type of image data provided, one of `url`, `base64`"},"value":{"type":"string","title":"Value","description":"Image data corresponding to the image type, if type = 'url' then value is a string containing the url of an image, else if type = 'base64' then value is a string containing base64 encoded image data."}},"type":"object","required":["type"],"title":"InferenceRequestImage","description":"Image data for inference request.\n\nAttributes:\n    type (str): The type of image data provided, one of 'url', 'base64', or 'numpy'.\n    value (Optional[Any]): Image data corresponding to the image type."},"Sam3Prompt":{"properties":{"type":{"type":"string","title":"Type","description":"Hint: `text` or `visual`"},"text":{"type":"string","title":"Text","description":"Text prompt describing the object to segment"},"output_prob_thresh":{"type":"number","title":"Output Prob Thresh","description":"Score threshold for this prompt's outputs. Overrides request-level threshold if set."},"boxes":{"items":{"anyOf":[{"$ref":"#/components/schemas/Box"},{"$ref":"#/components/schemas/BoxXYXY"}]},"type":"array","title":"Boxes","description":"Absolute pixel boxes as either XYWH or XYXY entries"},"box_labels":{"items":{"anyOf":[{"type":"integer"},{"type":"boolean"}]},"type":"array","title":"Box Labels","description":"List of 0/1 or booleans for boxes"}},"type":"object","required":["type"],"title":"Sam3Prompt","description":"Unified prompt that can contain text and/or geometry. Absolute pixel coordinates are used for boxes."},"Sam3SegmentationResponse":{"properties":{"prompt_results":{"items":{"$ref":"#/components/schemas/Sam3PromptResult"},"type":"array","title":"Prompt Results","description":"Results for each prompt in the request"},"time":{"type":"number","title":"Time","description":"The time in seconds it took to produce the segmentation including preprocessing"}},"type":"object","required":["prompt_results","time"],"title":"Sam3SegmentationResponse"},"Sam3PromptResult":{"properties":{"prompt_index":{"type":"integer","title":"Prompt Index","description":"Index of the prompt this result corresponds to"},"echo":{"$ref":"#/components/schemas/Sam3PromptEcho","description":"Echo of the original prompt for reference"},"predictions":{"items":{"$ref":"#/components/schemas/Sam3SegmentationPrediction"},"type":"array","title":"Predictions","description":"Segmentation predictions for this prompt"}},"type":"object","required":["prompt_index","predictions"],"title":"Sam3PromptResult"},"Sam3PromptEcho":{"properties":{"prompt_index":{"type":"integer","title":"Prompt Index"},"type":{"type":"string","title":"Type","description":"The prompt type (`text` or `visual`)"},"text":{"type":"string","title":"Text","description":"The text prompt if type is `text`"},"num_boxes":{"type":"integer","title":"Num Boxes","description":"Number of bounding boxes in the prompt"}},"type":"object","title":"Sam3PromptEcho"},"Sam3SegmentationPrediction":{"properties":{"format":{"type":"string","title":"Format","description":"The format of the mask data, either `polygon` or `rle`"},"confidence":{"type":"number","title":"Confidence","description":"Confidence score for this prediction"},"masks":{"items":{"items":{"items":{"type":"number"},"type":"array","minItems":2,"maxItems":2},"type":"array"},"type":"array","title":"Masks","description":"Array of polygons, each polygon is an array of [x, y] coordinate points"}},"type":"object","required":["format","confidence","masks"],"title":"Sam3SegmentationPrediction"},"HTTPValidationError":{"properties":{"detail":{"items":{"$ref":"#/components/schemas/ValidationError"},"type":"array","title":"Detail"}},"type":"object","title":"HTTPValidationError"},"ValidationError":{"properties":{"loc":{"items":{"anyOf":[{"type":"string"},{"type":"integer"}]},"type":"array","title":"Location"},"msg":{"type":"string","title":"Message"},"type":{"type":"string","title":"Error Type"}},"type":"object","required":["loc","msg","type"],"title":"ValidationError"}}}}
```

## SAM3 PVS (promptable visual segmentation)

> \*\*Interactive Segmentation (SAM 2 Style)\*\*\
> \
> SAM 3 also supports interactive segmentation using points and boxes.\
> \
> \*\*Image Input\*\*: The \`image\` field accepts either:\
> \- \`{"type": "url", "value": "\<IMAGE\_URL>"}\` - A publicly accessible image URL\
> \- \`{"type": "base64", "value": "\<BASE64\_DATA>"}\` - Base64 encoded image data\
> \
> \> \*\*Note\*\*: NumPy arrays are NOT supported on the serverless API. Use URL or base64 encoding only.\
> \
> \*\*Prompts\*\*: Support point-based prompts with positive/negative clicks for interactive segmentation.

```json
{"openapi":"3.1.0","info":{"title":"Roboflow SAM3 API","version":"0.64.4"},"servers":[{"url":"https://serverless.roboflow.com"}],"paths":{"/sam3/visual_segment":{"post":{"summary":"SAM3 PVS (promptable visual segmentation)","description":"**Interactive Segmentation (SAM 2 Style)**\n\nSAM 3 also supports interactive segmentation using points and boxes.\n\n**Image Input**: The `image` field accepts either:\n- `{\"type\": \"url\", \"value\": \"<IMAGE_URL>\"}` - A publicly accessible image URL\n- `{\"type\": \"base64\", \"value\": \"<BASE64_DATA>\"}` - Base64 encoded image data\n\n> **Note**: NumPy arrays are NOT supported on the serverless API. Use URL or base64 encoding only.\n\n**Prompts**: Support point-based prompts with positive/negative clicks for interactive segmentation.","operationId":"sam3_visual_segment_sam3_visual_segment_post","parameters":[{"name":"api_key","in":"query","required":true,"schema":{"type":"string","title":"API Key"},"description":"Your Roboflow API Key. Get one at https://app.roboflow.com/settings/api"}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/Sam2SegmentationRequest"}}}},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Sam2SegmentationResponse"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"Sam2SegmentationRequest":{"properties":{"image":{"$ref":"#/components/schemas/InferenceRequestImage","description":"The image to be segmented."},"image_id":{"type":"string","title":"Image Id","description":"The ID of the image to be segmented used to retrieve cached embeddings. If an embedding is cached, it will be used instead of generating a new embedding. If no embedding is cached, a new embedding will be generated and cached."},"prompts":{"$ref":"#/components/schemas/Sam2PromptSet","description":"A list of prompts for masks to predict. Each prompt can include a bounding box and / or a set of postive or negative points."},"format":{"type":"string","title":"Format","description":"The format of the response. Must be one of 'json', 'rle', or 'binary'. If binary, masks are returned as binary numpy arrays. If json, masks are converted to polygons. If rle, masks are converted to RLE format.","default":"json"},"sam2_version_id":{"type":"string","title":"Sam2 Version Id","description":"The version ID of SAM to be used for this request. Must be one of hiera_tiny, hiera_small, hiera_large, hiera_b_plus","default":"hiera_large"},"multimask_output":{"type":"boolean","title":"Multimask Output","description":"If true, the model will return three masks. For ambiguous input prompts (such as a single click), this will often produce better masks than a single prediction.","default":true},"save_logits_to_cache":{"type":"boolean","title":"Save Logits To Cache","description":"If True, saves the low-resolution logits to the cache for potential future use.","default":false},"load_logits_from_cache":{"type":"boolean","title":"Load Logits From Cache","description":"If True, attempts to load previously cached low-resolution logits for the given image and prompt set.","default":false}},"type":"object","required":["image"],"title":"Sam2SegmentationRequest","description":"SAM2 visual segmentation request."},"InferenceRequestImage":{"properties":{"type":{"type":"string","title":"Type","description":"The type of image data provided, one of `url`, `base64`"},"value":{"type":"string","title":"Value","description":"Image data corresponding to the image type, if type = 'url' then value is a string containing the url of an image, else if type = 'base64' then value is a string containing base64 encoded image data."}},"type":"object","required":["type"],"title":"InferenceRequestImage","description":"Image data for inference request.\n\nAttributes:\n    type (str): The type of image data provided, one of 'url', 'base64', or 'numpy'.\n    value (Optional[Any]): Image data corresponding to the image type."},"Sam2SegmentationResponse":{"properties":{"prompt_results":{"items":{"$ref":"#/components/schemas/Sam2PromptResult"},"type":"array","title":"Prompt Results","description":"Results for each prompt in the request"},"time":{"type":"number","title":"Time","description":"The time in seconds it took to produce the segmentation including preprocessing"}},"type":"object","required":["prompt_results","time"],"title":"Sam2SegmentationResponse"},"Sam2PromptResult":{"properties":{"prompt_index":{"type":"integer","title":"Prompt Index","description":"Index of the prompt this result corresponds to"},"predictions":{"items":{"$ref":"#/components/schemas/Sam2SegmentationPrediction"},"type":"array","title":"Predictions","description":"Segmentation predictions for this prompt"}},"type":"object","required":["prompt_index","predictions"],"title":"Sam2PromptResult"},"HTTPValidationError":{"properties":{"detail":{"items":{"$ref":"#/components/schemas/ValidationError"},"type":"array","title":"Detail"}},"type":"object","title":"HTTPValidationError"},"ValidationError":{"properties":{"loc":{"items":{"anyOf":[{"type":"string"},{"type":"integer"}]},"type":"array","title":"Location"},"msg":{"type":"string","title":"Message"},"type":{"type":"string","title":"Error Type"}},"type":"object","required":["loc","msg","type"],"title":"ValidationError"}}}}
```
