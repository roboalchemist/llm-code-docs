# Document AI QnA

The Document QnA capability combines OCR with large language model capabilities to enable natural language interaction with document content. This allows you to extract information and insights from documents by asking questions in natural language.

**The workflow consists of two main steps:**

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/document_qna.png"
    alt="Document QnA Graph"
    width="800"
    style={{ borderRadius: '15px' }}
  />
</div>

1. Document Processing: OCR extracts text, structure, and formatting, creating a machine-readable version of the document.

2. Language Model Understanding: The extracted document content is analyzed by a large language model. You can ask questions or request information in natural language. The model understands context and relationships within the document and can provide relevant answers based on the document content.


**Key capabilities:**
- Question answering about specific document content
- Information extraction and summarization
- Document analysis and insights
- Multi-document queries and comparisons
- Context-aware responses that consider the full document

**Common use cases:**
- Analyzing research papers and technical documents
- Extracting information from business documents
- Processing legal documents and contracts
- Building document Q&A applications
- Automating document-based workflows

The examples below show how to interact with a PDF document using natural language:

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral