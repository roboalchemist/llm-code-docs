# Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-documents-get.md

# Get Corpus Source Document

> Retrieves details for the specified source document



## OpenAPI

````yaml get /api/corpora/{corpus_id}/sources/{source_id}/documents/{document_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/corpora/{corpus_id}/sources/{source_id}/documents/{document_id}:
    get:
      tags:
        - corpora
      operationId: corpora_sources_documents_retrieve
      parameters:
        - in: path
          name: corpus_id
          schema:
            type: string
            format: uuid
          required: true
        - in: path
          name: document_id
          schema:
            type: string
            format: uuid
          required: true
        - in: path
          name: source_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ultravox.v1.CorpusDocument'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    ultravox.v1.CorpusDocument:
      type: object
      properties:
        corpusId:
          type: string
          description: The id of the corpus in which this document is included.
        sourceId:
          type: string
          description: The id of the source that provides this document.
        documentId:
          type: string
          description: The unique ID of this document.
        created:
          type: string
          description: When this document was created.
          format: date-time
        mimeType:
          type: string
          description: |-
            The MIME type of the document.
             https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types
        metadata:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CorpusDocumentMetadata'
          description: Metadata about the document.
        sizeBytes:
          type: string
          description: The size of the document contents, in bytes.
      description: >-
        A single complete source of information included in a corpus. In the
        most
         straight-forward case, this could be an uploaded PDF or a single webpage.
         However, documents can also be created from other documents during processing,
         for example turning an HTML page into a markdown document.
    ultravox.v1.CorpusDocumentMetadata:
      type: object
      properties:
        publicUrl:
          type: string
          description: The public URL of the document, if any.
        language:
          type: string
          description: The BCP47 language code of the document, if known.
        title:
          type: string
          description: The title of the document, if known.
        description:
          type: string
          description: A description of the document, if known.
        published:
          type: string
          description: The timestamp that the document was published, if known.
          format: date-time
      description: >-
        Metadata about a document. This is typically not included in the
        document's
         chunks, but can be used for filtering or citations.
         Derived documents inherit metadata from their source documents in general.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt