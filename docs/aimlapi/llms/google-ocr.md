# Source: https://docs.aimlapi.com/api-references/vision-models/ocr-optical-character-recognition/google/google-ocr.md

# Google OCR

{% hint style="info" %}
When calling the API described on this page, the ID of a specific model is not provided. The request is made solely by specifying the correct method URL and valid parameters.
{% endhint %}

## Model Overview

This API provides a feature to extract characters from images.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## Extract text from images using OCR.

> Performs optical character recognition (OCR) to extract text from images, enabling text-based analysis, data extraction, and automation workflows from visual data.

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Vision.v1.OCRResponseDTO":{"type":"object","properties":{"pages":{"type":"array","items":{"type":"object","properties":{"index":{"type":"integer","description":"The page index in a PDF document starting from 0"},"markdown":{"type":"string","description":"The markdown string response of the page"},"images":{"type":"array","items":{"type":"object","properties":{"id":{"type":"string","description":"Image ID for extracted image in a page"},"top_left_x":{"type":"integer","nullable":true,"description":"X coordinate of top-left corner of the extracted image"},"top_left_y":{"type":"integer","nullable":true,"description":"Y coordinate of top-left corner of the extracted image"},"bottom_right_x":{"type":"integer","nullable":true,"description":"X coordinate of bottom-right corner of the extracted image"},"bottom_right_y":{"type":"integer","nullable":true,"description":"Y coordinate of bottom-right corner of the extracted image"},"image_base64":{"type":"string","nullable":true,"format":"uri","description":"Base64 string of the extracted image"}},"required":["id","top_left_x","top_left_y","bottom_right_x","bottom_right_y"]},"description":"List of all extracted images in the page"},"dimensions":{"type":"object","nullable":true,"properties":{"dpi":{"type":"integer"},"height":{"type":"integer"},"width":{"type":"integer"}},"required":["dpi","height","width"],"description":"The dimensions of the PDF page's screenshot image"}},"required":["index","markdown","images","dimensions"]},"description":"List of OCR info for pages"},"model":{"type":"string","enum":["mistral-ocr-latest"],"description":"The model used to generate the OCR."},"usage_info":{"type":"object","properties":{"pages_processed":{"type":"integer","description":"Number of pages processed"},"doc_size_bytes":{"type":"integer","nullable":true,"description":"Document size in bytes"}},"required":["pages_processed","doc_size_bytes"],"description":"Usage info for the OCR request."}},"required":["pages","model","usage_info"]}}},"paths":{"/v1/ocr":{"post":{"operationId":"DocumentModelsController_processOCRRequest_v1","summary":"Extract text from images using OCR.","description":"Performs optical character recognition (OCR) to extract text from images, enabling text-based analysis, data extraction, and automation workflows from visual data.","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["google/gc-document-ai"]},"document":{"anyOf":[{"type":"string","format":"uri"},{"type":"string"}],"description":"The document file to be processed by the OCR model."},"mimeType":{"type":"string","enum":["application/pdf","image/gif","image/tiff","image/jpeg","image/png","image/bmp","image/webp","text/html"],"description":"The MIME type of the document."},"pages":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","enum":["start"]},"start":{"type":"integer","minimum":1}},"required":["type","start"]},{"type":"object","properties":{"type":{"type":"string","enum":["end"]},"end":{"type":"integer","minimum":1}},"required":["type","end"]},{"type":"object","properties":{"type":{"type":"string","enum":["range"]},"start":{"type":"integer","minimum":1},"end":{"type":"integer","minimum":2}},"required":["type","start","end"]},{"type":"object","properties":{"type":{"type":"string","enum":["indices"]},"indices":{"type":"array","items":{"type":"integer","minimum":1},"maxItems":15}},"required":["type","indices"]}],"description":"Specific pages you wants to process"}},"required":["document"],"additionalProperties":false}}}},"responses":{"201":{"description":"Successfully processed document with OCR","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Vision.v1.OCRResponseDTO"}}}}},"tags":["Vision Models"]}}}}
```
