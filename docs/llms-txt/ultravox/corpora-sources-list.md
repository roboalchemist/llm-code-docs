# Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-list.md

# List Corpus Sources

> Lists all sources that are part of the specified corpus



## OpenAPI

````yaml get /api/corpora/{corpus_id}/sources
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/corpora/{corpus_id}/sources:
    get:
      tags:
        - corpora
      operationId: corpora_sources_list
      parameters:
        - in: path
          name: corpus_id
          schema:
            type: string
            format: uuid
          required: true
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Paginatedultravox.v1.CorpusSourceList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    Paginatedultravox.v1.CorpusSourceList:
      type: object
      required:
        - results
      properties:
        next:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cD00ODY%3D"
        previous:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3
        results:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.CorpusSource'
        total:
          type: integer
          example: 123
    ultravox.v1.CorpusSource:
      type: object
      properties:
        corpusId:
          type: string
          description: The id of this source's corpus.
        sourceId:
          type: string
          description: The unique ID of this source.
        created:
          type: string
          description: When this source was created.
          format: date-time
        name:
          type: string
          description: The name of this source.
        description:
          type: string
          description: A description of this source.
        stats:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.SourceStats'
          description: The current stats for this source.
        loadSpec:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CrawlSpec'
          description: >-
            DEPRECATED. Prefer setting crawl instead. If either crawl or upload
            is set, this field will be ignored.
        crawl:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CrawlSpec'
          description: Allows loading documents by crawling the web.
        upload:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.UploadSpec'
          description: Allows loading from a uploaded document.
      description: >-
        A source of documents for building a corpus. A source defines where
        documents
         are pulled from.
    ultravox.v1.SourceStats:
      type: object
      properties:
        status:
          enum:
            - SOURCE_STATUS_UNSPECIFIED
            - SOURCE_STATUS_INITIALIZING
            - SOURCE_STATUS_READY
            - SOURCE_STATUS_UPDATING
          type: string
          description: >-
            The current status of this source, indicating whether it affects
            queries.
          format: enum
        lastUpdated:
          type: string
          description: When this source last finished contributing contents to its corpus.
          format: date-time
        numDocs:
          type: integer
          description: >-
            The number of documents in this source. This includes both loaded
            documents
             and derived documents.
          format: int32
      description: The current stats for a source.
    ultravox.v1.CrawlSpec:
      type: object
      properties:
        maxDocuments:
          type: integer
          description: The maximum number of documents to ingest.
          format: int32
        maxDocumentBytes:
          type: integer
          description: The maximum size of an individual document in bytes.
          format: int32
        relevantDocumentTypes:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.MimeTypeFilter'
          description: >-
            The types of documents to keep. Any documents surfaced during
            loading
             that don't match this filter will be discarded. If not set, Ultravox will
             choose a default that includes types known to provide real value.
        startUrls:
          type: array
          items:
            type: string
          description: >-
            The list of start URLs for crawling. If max_depth is 1, only these
            URLs will
             be fetched. Otherwise, links from these urls will be followed up to the
             max_depth.
        maxDepth:
          type: integer
          description: >-
            The maximum depth of links to traverse. Use 1 to only fetch the
            startUrls,
             2 to fetch the startUrls and documents directly linked from them, 3 to
             additionally fetch documents linked from those (excluding anything already
             seen), etc.
          format: int32
      description: The specification of how to acquire documents for this source.
    ultravox.v1.UploadSpec:
      type: object
      properties:
        documentIds:
          type: array
          items:
            type: string
          description: |-
            The IDs of uploaded documents. These documents must
             have been previously uploaded using the document upload API.
      description: >-
        The specification of how to acquire documents for uploaded documents
        source.
    ultravox.v1.MimeTypeFilter:
      type: object
      properties:
        include:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.MimeTypeSet'
          description: Mime types must be in this set to be kept.
        exclude:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.MimeTypeSet'
          description: Mime types must not be in this set to be kept.
      description: A Filter to apply to mime types.
    ultravox.v1.MimeTypeSet:
      type: object
      properties:
        mimeTypes:
          type: array
          items:
            type: string
          description: The mime types in this set.
      description: >-
        A set of mime types. Entries may be a full mime type (e.g. "text/html")
        or a
         type without a subtype (e.g. "text"). Entries without a subtype will match
         all subtypes (e.g. "text" will match "text/html", "text/plain", etc.).
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt