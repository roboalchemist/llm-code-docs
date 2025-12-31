# Source: https://docs.ultravox.ai/api-reference/corpora/corpora-sources-delete.md

# Delete Corpus Source

> Deletes the specified source



## OpenAPI

````yaml delete /api/corpora/{corpus_id}/sources/{source_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/corpora/{corpus_id}/sources/{source_id}:
    delete:
      tags:
        - corpora
      operationId: corpora_sources_destroy
      parameters:
        - in: path
          name: corpus_id
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
        '204':
          description: No response body
      security:
        - apiKeyAuth: []
components:
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt