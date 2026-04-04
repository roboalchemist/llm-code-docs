# Annotations

In addition to the basic OCR functionality, Mistral Document AI API adds the `annotations` functionality, which allows you to extract information in a structured json-format that you provide. Specifically, it offers two types of annotations: 
- `bbox_annotation`: gives you the annotation of the bboxes extracted by the OCR model (charts/ figures etc) based on user requirement and provided bbox/image annotation format. The user may ask to describe/caption the figure for instance.
- `document_annotation`: returns the annotation of the entire document based on the provided document annotation format.


<div style={{ textAlign: 'center' }}>
  <img
    src="/img/ocr_annotations_explanation.png"
    alt="annotations_explanation_graph"
    width="600"
    style={{ borderRadius: '15px' }}
  />
</div>


**Key capabilities**:
* Labeling and annotating data
* Extraction and structuring of specific information from documents into a predefined JSON format
* Automation of data extraction to reduce manual entry and errors
* Efficient handling of large document volumes for enterprise-level applications

**Common use cases**:
* Parsing of forms, classification of documents, and processing of images, including text, charts, and signatures
* Conversion of charts to tables, extraction of fine print from figures, or definition of custom image types
* Capture of receipt data, including merchant names and transaction amounts, for expense management.
* Extraction of key information like vendor details and amounts from invoices for automated accounting.
* Extraction of key clauses and terms from contracts for easier review and management

## How it works

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/ocr_annotations_workflow.png"
    alt="annotations_workflow_graph"
    width="800"
    style={{ borderRadius: '15px' }}
  />
</div>

**BBOX Annotations**
- All document types: 
  - After regular OCR is finished; we call a Vision capable LLM for all bboxes individually with the provided annotation format.

**Document Annotation**
- pdf/image: 
  - Independent of OCR; we convert all pages into images and send all images to a Vision capable LLM along with the provided annotation format.
- pptx/docx/...:
  - We run OCR first and send the output text markdown to a Vision capable LLM along with the provided annotation format.


You can use our API with the following document formats:
- [OCR with  pdf](basic_ocr.md#ocr-with-pdf)
- [OCR with uploaded pdf](basic_ocr.md#ocr-with-uploaded-pdf)
- [OCR with image](basic_ocr.md#ocr-with-image): even from low-quality or handwritten sources.
- scans, DOCX, PPTX.

In these examples, we will only consider the `OCR with pdf` format.

## BBox Annotation

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

Here is an example of how to use our Annotation functionalities using the Mistral AI client and Pydantic:

**Define the Data Model**

First, define the response formats for `BBox Annotation` using Pydantic models:

```python
from pydantic import BaseModel