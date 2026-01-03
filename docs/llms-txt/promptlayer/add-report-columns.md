# Source: https://docs.promptlayer.com/reference/add-report-columns.md

# Add Column to Evaluation Pipeline

> Adds a new evaluation step (column) to an existing evaluation pipeline. Columns execute sequentially from left to right and can reference data from previous columns.

**Column Types Available:**
- **Primary**: PROMPT_TEMPLATE, ENDPOINT, MCP, HUMAN, CODE_EXECUTION, CODING_AGENT, CONVERSATION_SIMULATOR, WORKFLOW
- **Evaluation**: LLM_ASSERTION, AI_DATA_EXTRACTION, COMPARE, CONTAINS, REGEX, REGEX_EXTRACTION, COSINE_SIMILARITY, ABSOLUTE_NUMERIC_DISTANCE
- **Helper**: JSON_PATH, XML_PATH, PARSE_VALUE, APPLY_DIFF, VARIABLE, ASSERT_VALID, COALESCE, COMBINE_COLUMNS, COUNT, MATH_OPERATOR, MIN_MAX

See the full documentation for detailed configuration requirements for each column type.

This endpoint adds evaluation steps (columns) to an existing evaluation pipeline. Columns execute sequentially from left to right, with each column able to reference outputs from previous columns.

## Important Notes

* **Single Column Per Request**: This endpoint only allows adding one column at a time. To add multiple columns, make separate API calls for each.
* **Column Order Matters**: Columns execute left to right. A column can only reference columns to its left.
* **Unique Names Required**: Each column name must be unique within the pipeline.
* **Dataset Columns Protected**: You cannot overwrite columns that come from the dataset.

## Scoring

By default, only the last column in a pipeline is used for score calculation. To include multiple columns in the final score:

* Set `is_part_of_score: true` on each column you want to include in the score
* Columns must produce boolean or numeric values to be scored
* When multiple columns are marked for scoring, the final score is the average of all included columns

## Column Types and Configuration

For the complete list of supported column types and their detailed configuration options, see the [Node & Column Types](/features/evaluations/column-types) documentation.

## Batch Adding Columns

Since columns must be added one at a time, here's a pattern for adding multiple columns:

```python  theme={null}
import requests

columns = [
    {
        "column_type": "PROMPT_TEMPLATE",
        "name": "Generate",
        "configuration": {...}
    },
    {
        "column_type": "LLM_ASSERTION",
        "name": "Validate",
        "configuration": {...}
    }
]

for column in columns:
    response = requests.post(
        "https://api.promptlayer.com/report-columns",
        headers={"X-API-KEY": "your_key"},
        json={
            "report_id": 456,
            **column
        }
    )
    if response.status_code != 201:
        print(f"Failed: {column['name']}")
        break
```

## Column Reference Syntax

When configuring columns that reference other columns:

* **Dataset columns**: Use exact column name from dataset (e.g., `"question"`)
* **Previous columns**: Use the name you assigned (e.g., `"AI Response"`)
* **Variable columns**: Reference by their name

## Error Handling

The endpoint validates:

1. Column type is valid
2. Column name is unique within the pipeline
3. Configuration matches the column type schema
4. Referenced columns exist (for dependent columns)
5. User has permission to modify the pipeline

Common errors:

* `400`: Invalid configuration or duplicate column name
* `403`: Cannot overwrite dataset columns or lacking permissions
* `404`: Report not found or not accessible


## OpenAPI

````yaml POST /report-columns
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /report-columns:
    post:
      tags:
        - reports
      summary: Add Column to Evaluation Pipeline
      description: >-
        Adds a new evaluation step (column) to an existing evaluation pipeline.
        Columns execute sequentially from left to right and can reference data
        from previous columns.


        **Column Types Available:**

        - **Primary**: PROMPT_TEMPLATE, ENDPOINT, MCP, HUMAN, CODE_EXECUTION,
        CODING_AGENT, CONVERSATION_SIMULATOR, WORKFLOW

        - **Evaluation**: LLM_ASSERTION, AI_DATA_EXTRACTION, COMPARE, CONTAINS,
        REGEX, REGEX_EXTRACTION, COSINE_SIMILARITY, ABSOLUTE_NUMERIC_DISTANCE

        - **Helper**: JSON_PATH, XML_PATH, PARSE_VALUE, APPLY_DIFF, VARIABLE,
        ASSERT_VALID, COALESCE, COMBINE_COLUMNS, COUNT, MATH_OPERATOR, MIN_MAX


        See the full documentation for detailed configuration requirements for
        each column type.
      operationId: addReportColumn
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: API key to authorize the operation. Can also use JWT authentication.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                report_id:
                  type: integer
                  description: The ID of the evaluation pipeline to add this column to.
                  minimum: 1
                column_type:
                  type: string
                  description: >-
                    The type of evaluation or transformation this column
                    performs. Must be one of the supported column types.
                  enum:
                    - ABSOLUTE_NUMERIC_DISTANCE
                    - AI_DATA_EXTRACTION
                    - ASSERT_VALID
                    - CONVERSATION_SIMULATOR
                    - COALESCE
                    - CODE_EXECUTION
                    - COMBINE_COLUMNS
                    - COMPARE
                    - CONTAINS
                    - COSINE_SIMILARITY
                    - COUNT
                    - ENDPOINT
                    - MCP
                    - HUMAN
                    - JSON_PATH
                    - LLM_ASSERTION
                    - MATH_OPERATOR
                    - MIN_MAX
                    - PARSE_VALUE
                    - APPLY_DIFF
                    - PROMPT_TEMPLATE
                    - REGEX
                    - REGEX_EXTRACTION
                    - VARIABLE
                    - XML_PATH
                    - WORKFLOW
                    - CODING_AGENT
                name:
                  type: string
                  description: >-
                    Display name for this column. Must be unique within the
                    pipeline. This name is used to reference the column in
                    subsequent steps.
                  minLength: 1
                  maxLength: 255
                configuration:
                  type: object
                  description: >-
                    Column-specific configuration. The schema varies based on
                    column_type. See documentation for each type's requirements.
                  additionalProperties: true
                position:
                  type: integer
                  description: >-
                    Optional position for the column. If not specified, the
                    column is added at the end. Cannot overwrite dataset
                    columns.
                  minimum: 0
                  nullable: true
              required:
                - report_id
                - column_type
                - name
                - configuration
              example:
                report_id: 456
                column_type: PROMPT_TEMPLATE
                name: Generate Answer
                configuration:
                  template:
                    name: qa_template
                    version_number: null
                  prompt_template_variable_mappings:
                    question: input_question
                  engine:
                    provider: openai
                    model: gpt-4
                    parameters:
                      temperature: 0.7
      responses:
        '201':
          description: Column added successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  report_column:
                    type: object
                    description: >-
                      Details of the created column including its ID and
                      configuration
        '400':
          description: >-
            Bad Request - Invalid column type, configuration validation failed,
            or column name already exists
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  message:
                    type: string
                    example: Report already has a column with that name
        '401':
          description: Unauthorized - Invalid or missing authentication
        '403':
          description: Forbidden - Cannot overwrite dataset columns or missing permissions
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  message:
                    type: string
                    example: You can not overwrite dataset columns
        '404':
          description: Not Found - Report not found or not accessible
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  message:
                    type: string
                    example: Report not found

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt