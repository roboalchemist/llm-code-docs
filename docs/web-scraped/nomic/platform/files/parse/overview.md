# Nomic Documentation

Source: https://docs.nomic.ai/platform/files/parse/overview/

Parse uploaded files to extract structured content and make them ready for analysis, embedding generation, and data visualization.

## What is File Parsing?​

File parsing converts PDF documents into a structured, machine-readable format. This process extracts text, metadata, and structural information.

## Using the Parse API​

Download a test file:

```
import requestsresp = requests.get("https://assets.nomicatlas.com/department-of-labor-data.pdf")with open("department-of-labor-data.pdf", "wb") as f:    f.write(resp.content)
```

Upload and parse it using the Nomic Platform:

```
from nomic import NomicClientclient = NomicClient()# uploadfile = client.upload_file("department-of-labor-data.pdf")# parseresult = client.parse(file)
```

Print the result:

```
import jsonimport sysprint("Parsed document:")json.dump(result["result"], sys.stdout, indent=4)
```

### Example Result​

See the response format here.

```
{    "chunks": [        {            "content": "Department of Labor seal with \"News Release\" text.\nTRANSMISSION OF MATERIALS IN THIS ...",            "embed": "Department of Labor seal with \"News Release\" text.\nTRANSMISSION OF MATERIALS IN THIS ...",            "blocks": [                {                    "type": "Figure",                    "bbox": {                        "left": 0.0791983760260289,                        "top": 0.03243826374863133,                        "width": 0.464428297055313,                        "height": 0.06306505203247072,                        "page": 1                    },                    "content": ""                },                {                    "type": "Text",                    "bbox": {                        "left": 0.20591503267973857,                        "top": 0.13927020202020207,                        "width": 0.5926797385620916,                        "height": 0.026579545454545356,                        "page": 1                    },                    "content": "TRANSMISSION OF MATERIALS IN THIS RELEASE IS EMBARGOED UNTIL 8:30 A.M. (Eastern) Thursday, January 30, 2025"                } ...            ]        },        {            "content": "SEASONALLY ADJUSTED DATA\n## UNADJUSTED DATA\nThe advance number of actual initial claims under ...",            "embed": "SEASONALLY ADJUSTED DATA\n## UNADJUSTED DATA\nThe advance number of actual initial claims under ...",            "blocks": [                {                    "type": "Section Header",                    "bbox": {                        "left": 0.10200000000000001,                        "top": 0.07279166666666662,                        "width": 0.17254248366013072,                        "height": 0.011214646464646538,                        "page": 2                    },                    "content": "## UNADJUSTED DATA"                } ...            ]        } ...    ]}
```

### Direct URL Usage​

You can also pass a public URL directly to parse:

```
result = client.parse("https://assets.nomicatlas.com/department-of-labor-data.pdf")
```

### Parse Options​

You can customize the parsing behavior using ParseOptions:

```
ParseOptions
```

```
from nomic import NomicClientfrom nomic.client_models import ParseOptions, OcrLanguage, ContentExtractionModeclient = NomicClient()# Configure parse optionsoptions = ParseOptions(    ocr_language=OcrLanguage.Chinese_Japanese_English,    content_extraction_mode=ContentExtractionMode.Ocr)result = client.parse(file, options=options)
```

#### OCR Language​

The ocr_language parameter controls which language model is used for optical character recognition:

```
ocr_language
```

- OcrLanguage.English (default): Optimized for English text
```
OcrLanguage.English
```

- OcrLanguage.Latin: For Latin-based languages (Spanish, French, German, etc.)
```
OcrLanguage.Latin
```

- OcrLanguage.Chinese_Japanese_English: For documents containing Chinese, Japanese, or mixed CJK/English text
```
OcrLanguage.Chinese_Japanese_English
```

Example with Chinese/Japanese documents:

```
from nomic import NomicClientfrom nomic.client_models import ParseOptions, OcrLanguageclient = NomicClient()options = ParseOptions(ocr_language=OcrLanguage.Chinese_Japanese_English)result = client.parse("chinese_document.pdf", options=options)
```

#### Content Extraction Mode​

The content_extraction_mode parameter controls the overall extraction strategy:

```
content_extraction_mode
```

- ContentExtractionMode.Hybrid (default): Uses embedded text where available, OCR on images and bitmaps
```
ContentExtractionMode.Hybrid
```

- ContentExtractionMode.Metadata: Only uses embedded document text, no OCR
```
ContentExtractionMode.Metadata
```

- ContentExtractionMode.Ocr: Runs OCR on all pages, even if text is embedded
```
ContentExtractionMode.Ocr
```

#### Other Options​

Additional parsing options include:

- chunking: Configure how documents are split into chunks (chunk size, merge strategy, etc.)
```
chunking
```

- table_summary: Enable table content summarization
```
table_summary
```

- figure_summary: Enable figure/image content summarization
```
figure_summary
```

See the Parse Options documentation for complete details on all available options.

### Non-Blocking Usage​

You can request a non-blocking parse, causing the function to return immediately:

```
task = client.parse(file, block=False)
```

The task object can be polled to get the result. For example:

```
# check without waitingresult = task.get(block=False)# wait for 5 secondsresult = task.get(timeout=5)# wait indefinitelyresult = task.get()
```

### Example of Non-Blocking Usage​

Handle TaskPending in order to continue after a timeout:

```
import timefrom nomic import NomicClientfrom nomic.client import TaskPendingclient = NomicClient()task = client.parse("https://assets.nomicatlas.com/department-of-labor-data.pdf", block=False)start = time.time()while True:    try:        result = task.get(timeout=5)        break    except TaskPending:        print(f"Task still pending after {time.time() - start:.2f} seconds")print(f"Done after {time.time() - start:.2f} seconds")
```

You may see an output like this:

```
Task still pending after 5.02 secondsTask still pending after 10.19 secondsTask still pending after 15.38 seconds...Task still pending after 51.49 secondsDone after 57.25 seconds
```

## Next Steps​

After parsing files, you can:

- Generate embeddings for semantic search
- Create visualizations and maps in Atlas
You may also consider:

- Extracting specific data using a custom schema
- What is File Parsing?
- Using the Parse APIExample ResultDirect URL UsageParse OptionsNon-Blocking UsageExample of Non-Blocking Usage
- Example Result
- Direct URL Usage
- Parse Options
- Non-Blocking Usage
- Example of Non-Blocking Usage
- Next Steps
