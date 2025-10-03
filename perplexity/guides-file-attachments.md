# Source: https://docs.perplexity.ai/guides/file-attachments

## 
[​](https://docs.perplexity.ai/guides/file-attachments#overview)
Overview
Sonar models support document analysis through file uploads. You can provide files either as URLs to publicly accessible documents or as base64 encoded bytes. Ask questions about document content, get summaries, extract information, and perform detailed analysis of uploaded files in multiple formats including PDF, DOC, DOCX, TXT, and RTF.
**SDK Installation Required** : Install the official SDK first - `pip install perplexityai` for Python or `npm install @perplexity-ai/perplexity_ai` for TypeScript/JavaScript.
Document files can be provided as:
  * A public URL pointing to the file
  * Base64 encoded bytes (without any prefix)

Supported formats: PDF, DOC, DOCX, TXT, RTF.
The maximum file size is 50MB. Files larger than this limit will not be processed.
## 
[​](https://docs.perplexity.ai/guides/file-attachments#supported-features)
Supported Features
  * **Document Summarization** : Get concise summaries of document content
  * **Question Answering** : Ask specific questions about the document
  * **Content Extraction** : Extract key information, data, and insights
  * **Multi-language Support** : Analyze documents in various languages
  * **Large Document Handling** : Process lengthy documents efficiently
  * **Multiple Formats** : Support for PDF, DOC, DOCX, TXT, and RTF files


## 
[​](https://docs.perplexity.ai/guides/file-attachments#basic-usage)
Basic Usage
### 
[​](https://docs.perplexity.ai/guides/file-attachments#simple-document-analysis)
Simple Document Analysis
#### 
[​](https://docs.perplexity.ai/guides/file-attachments#using-a-public-url)
Using a Public URL
cURL
Python
JavaScript
Go
Copy
Ask AI
```
curl -X POST "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "content": [
          {
            "type": "text",
            "text": "Summarize this document"
          },
          {
            "type": "file_url",
            "file_url": {
              "url": "https://example.com/document.pdf"
            },
            "file_name": "document.pdf"
          }
        ],
        "role": "user"
      }
    ],
    "model": "sonar-pro"
  }'

```

#### 
[​](https://docs.perplexity.ai/guides/file-attachments#using-base64-encoded-bytes)
Using Base64 Encoded Bytes
cURL
Python
JavaScript
Copy
Ask AI
```
curl -X POST "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "content": [
          {
            "type": "text",
            "text": "Summarize this document"
          },
          {
            "type": "file_url",
            "file_url": {
              "url": "JVBERi0xLjQKJeLjz9MKNCAwIG9iago..."
            },
            "file_name": "report.pdf"
          }
        ],
        "role": "user"
      }
    ],
    "model": "sonar-pro"
  }'

```

### 
[​](https://docs.perplexity.ai/guides/file-attachments#advanced-analysis-with-web-search)
Advanced Analysis with Web Search
cURL
Python
JavaScript
Copy
Ask AI
```
curl -X POST "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "content": [
          {
            "type": "text",
            "text": "What are the key findings in this research paper? Provide additional context from recent studies."
          },
          {
            "type": "file_url",
            "file_url": {
              "url": "https://example.com/research-paper.pdf"
            },
            "file_name": "research-paper.pdf"
          }
        ],
        "role": "user"
      }
    ],
    "model": "sonar-pro",
    "web_search_options": {"search_type": "pro"}
  }'

```

## 
[​](https://docs.perplexity.ai/guides/file-attachments#file-requirements)
File Requirements
## Format Support
  * PDF files (.pdf extension)
  * Word documents (.doc, .docx extensions)
  * Text files (.txt extension)
  * Rich Text Format (.rtf extension)
  * Text-based documents (not scanned images)
  * Base64 encoded file bytes
  * Password-protected files (if publicly accessible)


## Size Limits
  * Maximum file size: 50MB
  * Recommended: Under 50MB for optimal performance
  * Maximum processing time: 60 seconds
  * Large files may take longer to analyze


## 
[​](https://docs.perplexity.ai/guides/file-attachments#common-use-cases)
Common Use Cases
### 
[​](https://docs.perplexity.ai/guides/file-attachments#academic-research)
Academic Research
Copy
Ask AI
```
question = "What methodology was used in this study and what were the main conclusions?"

```

### 
[​](https://docs.perplexity.ai/guides/file-attachments#legal-documents)
Legal Documents
Copy
Ask AI
```
question = "Extract the key terms and conditions from this contract"

```

### 
[​](https://docs.perplexity.ai/guides/file-attachments#financial-reports)
Financial Reports
Copy
Ask AI
```
question = "What are the revenue trends and key financial metrics mentioned?"

```

### 
[​](https://docs.perplexity.ai/guides/file-attachments#technical-documentation)
Technical Documentation
Copy
Ask AI
```
question = "Explain the implementation details and provide a step-by-step guide"

```

## 
[​](https://docs.perplexity.ai/guides/file-attachments#best-practices)
Best Practices
Optimize Your Questions
  * Be specific about what information you need
  * Ask one focused question per request for best results
  * Use follow-up questions to dive deeper into specific sections


Prepare Your Documents
  * Ensure documents are text-based, not scanned images
  * For URLs: Use publicly accessible URLs (Google Drive, Dropbox, etc.)
  * For URLs: Verify the URL returns the document directly, not a preview page
  * For base64: Encode the entire file content properly
  * For base64: Provide only the base64 string without any prefix (no `data:` URI scheme)


Handle Large Documents
  * Break down complex questions into smaller parts
  * Consider processing large documents in sections
  * Use streaming for real-time responses on lengthy analyses


## 
[​](https://docs.perplexity.ai/guides/file-attachments#error-handling)
Error Handling
### 
[​](https://docs.perplexity.ai/guides/file-attachments#common-issues)
Common Issues
Error | Cause | Solution  
---|---|---  
`Invalid URL` | URL not accessible or invalid base64 | Verify URL returns file directly or check base64 encoding  
`File too large` | File exceeds 50MB limit | Compress or split the document  
`Processing timeout` | Document too complex | Simplify question or use smaller sections  
`Invalid base64` | Malformed base64 string | Ensure proper base64 encoding without prefix  
## 
[​](https://docs.perplexity.ai/guides/file-attachments#pricing)
Pricing
PDF analysis follows standard Sonar pricing based on:
  * Input tokens (document content + question)
  * Output tokens (AI response)
  * Web search usage (if enabled)


Large documents consume more input tokens. Consider the document size when estimating costs.
