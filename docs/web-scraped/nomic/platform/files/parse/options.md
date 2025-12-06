# Nomic Documentation

Source: https://docs.nomic.ai/platform/files/parse/options/

Customize document parsing behavior using the ParseOptions class and its related configuration objects.

```
ParseOptions
```

## ParseOptions​

The main options object for configuring document parsing.

### Parameters​

#### content_extraction_mode​

```
content_extraction_mode
```

Type: ContentExtractionMode (default: ContentExtractionMode.Hybrid)

```
ContentExtractionMode
```

```
ContentExtractionMode.Hybrid
```

The overall strategy for extracting content from the document.

- ContentExtractionMode.Hybrid (default): Uses embedded document text where available, and runs OCR on images and bitmaps found in the document. Best balance of speed and accuracy for most documents.
```
ContentExtractionMode.Hybrid
```

- ContentExtractionMode.Metadata: Only uses embedded document text. Disables all OCR. Fastest option, but may miss content in scanned documents or images.
```
ContentExtractionMode.Metadata
```

- ContentExtractionMode.Ocr: Runs OCR on all pages, even if text is embedded. Slowest option, but provides the most consistent results across different document types.
```
ContentExtractionMode.Ocr
```

Example:

```
from nomic.client_models import ParseOptions, ContentExtractionModeoptions = ParseOptions(    content_extraction_mode=ContentExtractionMode.Ocr)
```

#### ocr_language​

```
ocr_language
```

Type: OcrLanguage (default: OcrLanguage.English)

```
OcrLanguage
```

```
OcrLanguage.English
```

Language selection for OCR. Choosing the correct language model significantly improves accuracy for non-English documents.

- OcrLanguage.English (default): Optimized for English text
```
OcrLanguage.English
```

- OcrLanguage.Latin: For Latin-based languages including Spanish, French, German, Italian, Portuguese, and other Romance and Germanic languages
```
OcrLanguage.Latin
```

- OcrLanguage.Chinese_Japanese_English: For documents containing Chinese, Japanese, or mixed CJK/English text
```
OcrLanguage.Chinese_Japanese_English
```

Example:

```
from nomic.client_models import ParseOptions, OcrLanguage# For a Spanish documentoptions = ParseOptions(ocr_language=OcrLanguage.Latin)# For a mixed Chinese/English documentoptions = ParseOptions(ocr_language=OcrLanguage.Chinese_Japanese_English)
```

#### table_summary​

```
table_summary
```

Type: TableSummaryOptions | None (default: None)

```
TableSummaryOptions | None
```

```
None
```

Options for generating table summaries. When None, default behavior is used.

```
None
```

See TableSummaryOptions below for details.

#### figure_summary​

```
figure_summary
```

Type: FigureSummaryOptions | None (default: None)

```
FigureSummaryOptions | None
```

```
None
```

Options for generating figure summaries. When None, default behavior is used.

```
None
```

See FigureSummaryOptions below for details.

## TableSummaryOptions​

Options for generating summaries of table content.

### Parameters​

#### enabled​

```
enabled
```

Type: bool (default: False)

```
bool
```

```
False
```

Whether to generate a natural language summary of table content. When enabled, tables will have an additional text description that can improve retrieval and understanding.

Example:

```
from nomic.client_models import ParseOptions, TableSummaryOptionsoptions = ParseOptions(    table_summary=TableSummaryOptions(enabled=True))
```

## FigureSummaryOptions​

Options for generating summaries of figures and images.

### Parameters​

#### enabled​

```
enabled
```

Type: bool (default: True)

```
bool
```

```
True
```

Whether to generate a natural language description of figure content. When enabled, figures and images will have text descriptions that describe their visual content.

Example:

```
from nomic.client_models import ParseOptions, FigureSummaryOptions# Disable figure summarization for faster processingoptions = ParseOptions(    figure_summary=FigureSummaryOptions(enabled=False))
```

## Complete Example​

Here's a comprehensive example showing how to use all the options together:

```
from nomic import NomicClientfrom nomic.client_models import (    ParseOptions,    ContentExtractionMode,    OcrLanguage,    TableSummaryOptions,    FigureSummaryOptions,)client = NomicClient()# Configure comprehensive parse optionsoptions = ParseOptions(    # Use OCR on all pages for maximum consistency    content_extraction_mode=ContentExtractionMode.Ocr,    # Use Latin language model for Spanish document    ocr_language=OcrLanguage.Latin,    # Enable table summaries for better retrieval    table_summary=TableSummaryOptions(enabled=True),    # Keep figure summaries enabled (default)    figure_summary=FigureSummaryOptions(enabled=True))# Parse with custom optionsfile = client.upload_file("document.pdf")result = client.parse(file, options=options)
```

## Best Practices​

### Choosing Content Extraction Mode​

- Use Hybrid (default) for most documents - it provides the best balance
- Use Metadata when you know the document has good embedded text and you need maximum speed
- Use Ocr for scanned documents, documents with poor embedded text, or when you need consistent results
### Selecting OCR Language​

Always set ocr_language to match your document's primary language:

```
ocr_language
```

- Documents in English → OcrLanguage.English
```
OcrLanguage.English
```

- Documents in Spanish, French, German, etc. → OcrLanguage.Latin
```
OcrLanguage.Latin
```

- Documents in Chinese, Japanese, or mixed CJK/English → OcrLanguage.Chinese_Japanese_English
```
OcrLanguage.Chinese_Japanese_English
```

### Using Summaries​

- Table summaries: Enable when tables contain important information that should be retrievable through semantic search
- Figure summaries: Usually beneficial to keep enabled unless you're processing documents with many irrelevant images
- ParseOptionsParameters
- Parameters
- TableSummaryOptionsParameters
- Parameters
- FigureSummaryOptionsParameters
- Parameters
- Complete Example
- Best PracticesChoosing Content Extraction ModeSelecting OCR LanguageUsing Summaries
- Choosing Content Extraction Mode
- Selecting OCR Language
- Using Summaries
