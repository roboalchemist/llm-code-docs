# Source: https://docs.unstructured.io/open-source/how-to/set-ocr-agent.md

# Set the OCR agent

## Task

You want to specify the type of agent that you use when performing optical character recognition (OCR) on files, such as images and PDFs.

<Note>This task works only with the Unstructured open source library.</Note>

## Approach

Set the environment variable named `OCR_AGENT` to one of the following supported values:

* `unstructured.partition.utils.ocr_models.tesseract_ocr.OCRAgentTesseract` to use Tesseract OCR. This is the default if not otherwise specified.
* `unstructured.partition.utils.ocr_models.paddle_ocr.OCRAgentPaddle` to use Paddle OCR.
* `unstructured.partition.utils.ocr_models.google_vision_ocr.OCRAgentGoogleVision` to use Google Cloud Vision OCR.

Also, be sure to install the corresponding OCR agent and its dependencies, if you have not already done so:

* For Tesseract OCR, [see the dependency list](https://github.com/Unstructured-IO/unstructured/blob/main/requirements/extra-pdf-image.in).
* For Paddle OCR, [see the dependency list](https://github.com/Unstructured-IO/unstructured/blob/main/requirements/extra-paddleocr.in).
* For Google Cloud Vision OCR, [see the dependency list](https://github.com/Unstructured-IO/unstructured/blob/main/requirements/extra-pdf-image.in).

## Example code

This example uses a PNG file with an embedded combination of English and Korean text. This example uses Tesseract OCR.

Language codes will differ depending on the OCR agent you use:

* For Tesseract OCR, [see the language codes list](https://github.com/Unstructured-IO/unstructured/blob/main/unstructured/partition/common/lang.py).
* For Paddle OCR, [see the language codes list](https://github.com/Unstructured-IO/unstructured/blob/main/unstructured/partition/lang.py) and [language names list](https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/multi_languages_en.md#language_abbreviations).
* For Google Cloud Vision OCR, [see the language codes list](https://cloud.google.com/vision/docs/languages).

```python Python theme={null}
import json

from unstructured.partition.image import partition_image

# Source: https://github.com/Unstructured-IO/unstructured-ingest/blob/main/example-docs/img/english-and-korean.png
# Path to the local file to process, relative to this .py file.
filename = "local-ingest-png/english-and-korean.png"

elements = partition_image(
  filename=filename,
  strategy="ocr_only",
  languages=["eng", "kor"] # Language codes differ by the OCR agent used.
)

# Convert the list of returned elements into a list of dictionaries for printing or saving.
element_dicts = [element.to_dict() for element in elements]

# Print the list.
print(json.dumps(element_dicts, indent=2))

# Or, save the list locally:
#
# file = "local-ingest-output/english-and-korean.json"
#
# with open(file, "w") as file:
#     json.dump(element_dicts, file, indent=2)
```
