# Source: https://docs.promptlayer.com/reference/get-snippet-usage.md

# Get Snippet Usage

> Get all prompts that use a given snippet (prompt template). Returns a list of prompts and their version numbers that reference this snippet.

Get all prompts that use a given snippet (prompt template). Returns a list of prompts and their version numbers that reference this snippet, as well as any release labels that reference it. The identifier can be either the prompt name or the prompt id.


## OpenAPI

````yaml GET /prompt-templates/{identifier}/snippet-usage
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompt-templates/{identifier}/snippet-usage:
    get:
      tags:
        - prompt-templates
        - snippets
      summary: Get Snippet Usage
      description: >-
        Get all prompts that use a given snippet (prompt template). Returns a
        list of prompts and their version numbers that reference this snippet.
      operationId: get_snippet_usage
      parameters:
        - required: true
          schema:
            type: string
            title: X-Api-Key
          name: X-API-KEY
          in: header
        - name: identifier
          in: path
          required: true
          schema:
            type: string
            title: identifier
            description: The identifier can be either the prompt name or the prompt id.
        - name: prompt_version_number
          in: query
          required: false
          schema:
            type: integer
            title: prompt_version_number
            description: Optional specific version number to check usage for
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetSnippetUsageResponse'
        '403':
          description: Access denied - Invalid workspace_id
        '404':
          description: Prompt template not found
components:
  schemas:
    GetSnippetUsageResponse:
      type: object
      properties:
        success:
          type: boolean
        message:
          type: string
        snippet_name:
          type: string
          description: The name of the snippet prompt template
        snippet_usage:
          type: array
          items:
            type: object
            properties:
              prompt_registry_id:
                type: integer
                description: The ID of the prompt that uses this snippet
              prompt_name:
                type: string
                description: The name of the prompt that uses this snippet
              version_numbers:
                type: array
                items:
                  type: integer
                description: List of version numbers that use this snippet
          description: List of prompts using this snippet
        total_prompts_using_snippet:
          type: integer
          description: Total number of prompts using this snippet
        label_usage:
          type: array
          items:
            type: object
            properties:
              prompt_registry_id:
                type: integer
                description: The ID of the prompt with a label using this snippet
              prompt_name:
                type: string
                description: The name of the prompt with a label using this snippet
              label_name:
                type: string
                description: The name of the label using this snippet
          description: List of labels using this snippet
        total_labels_using_snippet:
          type: integer
          description: Total number of labels using this snippet
      title: GetSnippetUsageResponse

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt