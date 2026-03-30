# Marker OCR Documentation

Marker is a tool that converts PDFs, images, and other documents to markdown, JSON, or HTML using deep learning models.

## Quick Links

- **Main Documentation**: See [README.md](README.md) for comprehensive usage guide
- **Examples**: See [examples/README.md](examples/README.md) for usage examples
- **Official Repository**: https://github.com/VikParuchuri/marker
- **Hosted API**: https://www.datalab.to/

## Key Features

- Converts PDF, image, PPTX, DOCX, XLSX, HTML, EPUB files in all languages
- Formats tables, forms, equations, inline math, links, references, and code blocks
- Extracts and saves images
- Removes headers/footers/other artifacts
- Extensible with custom formatting and logic
- Structured extraction with JSON schema (beta)
- Optional LLM-powered accuracy boost
- Works on GPU, CPU, or MPS

## Installation

```bash
pip install marker-pdf
```

For full feature support (PPTX, DOCX, XLSX, etc.):

```bash
pip install marker-pdf[full]
```

## Basic Usage

### Single File Conversion

```bash
marker_single /path/to/file.pdf
```

### Batch Conversion

```bash
marker /path/to/input/folder
```

### With LLM Enhancement

```bash
marker_single file.pdf --use_llm
```

## Output Formats

- **Markdown**: Default output with formatted tables, equations, and code blocks
- **JSON**: Tree-structured output with block types and metadata
- **HTML**: HTML representation with proper formatting
- **Chunks**: Flattened JSON format suitable for RAG applications

## Configuration

Key environment variables and flags:

- `TORCH_DEVICE`: Force a specific torch device (e.g., `cuda`, `cpu`, `mps`)
- `--force_ocr`: Force OCR processing on entire document
- `--use_llm`: Use LLM for improved accuracy
- `--output_format`: Specify output format (markdown, json, html, chunks)
- `--workers`: Number of parallel workers for batch processing

## LLM Services

Marker supports multiple LLM services for enhanced accuracy:

- **Gemini** (default): Google's Gemini API
- **Google Vertex**: Vertex AI for reliability
- **Ollama**: Local models
- **Claude**: Anthropic's Claude API
- **OpenAI**: OpenAI API
- **Azure OpenAI**: Azure's OpenAI service

## API Server

Run a simple FastAPI server:

```bash
pip install uvicorn fastapi python-multipart
marker_server --port 8001
```

Access at `http://localhost:8001/docs` for interactive API documentation.

## Performance

Marker benchmarks favorably against commercial tools like Llamaparse and Mathpix:

- **Speed**: ~2.8 seconds per page (faster than competitors)
- **Accuracy**: 95.67% heuristic score, 4.24/5 LLM score
- **Throughput**: 122 pages/second on H100 GPU

## For More Information

See the complete [README.md](README.md) for:

- Detailed configuration options
- Advanced usage examples
- Custom processor development
- Integration guides
- Troubleshooting tips
- Benchmark methodology and results
