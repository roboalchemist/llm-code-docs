# Source: https://docs.promptlayer.com/reference/create-reports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Evaluation Pipeline

> Creates a new evaluation pipeline (report) with optional evaluation columns and custom scoring.

This endpoint creates an Evaluation Pipeline associated with a dataset.

## Request Parameters

| Parameter                | Type      | Required | Description                                            |
| ------------------------ | --------- | -------- | ------------------------------------------------------ |
| `dataset_group_id`       | `integer` | Yes      | ID of the dataset group to use                         |
| `name`                   | `string`  | No       | Name for the pipeline (auto-generated if not provided) |
| `folder_id`              | `integer` | No       | Folder ID for organization                             |
| `dataset_version_number` | `integer` | No       | Specific dataset version (uses latest if not provided) |
| `columns`                | `array`   | No       | List of evaluation columns to add                      |
| `score_configuration`    | `object`  | No       | Custom scoring logic configuration                     |

## Column Definition

Each column in the `columns` array accepts:

| Field              | Type      | Required | Description                                                        |
| ------------------ | --------- | -------- | ------------------------------------------------------------------ |
| `column_type`      | `string`  | Yes      | Type of column (see supported types below)                         |
| `name`             | `string`  | Yes      | Display name for the column                                        |
| `configuration`    | `object`  | Yes      | Column-type-specific configuration                                 |
| `position`         | `integer` | No       | Position in the pipeline (auto-assigned if not provided)           |
| `is_part_of_score` | `boolean` | No       | Whether this column contributes to the score (defaults to `false`) |

### Supported Column Types

<Info>
  For detailed configuration options for each column type, see the [Node & Column Types](/features/evaluations/column-types) documentation.
</Info>

| Type                        | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| `PROMPT_TEMPLATE`           | Runs a prompt template from the registry                     |
| `CODE_EXECUTION`            | Executes custom Python or JavaScript code                    |
| `ENDPOINT`                  | Calls an external HTTP endpoint                              |
| `WORKFLOW`                  | Runs a PromptLayer workflow                                  |
| `MCP`                       | Executes an MCP action                                       |
| `HUMAN`                     | Manual human evaluation                                      |
| `CONVERSATION_SIMULATOR`    | Simulates multi-turn conversations for testing chatbots      |
| `LLM_ASSERTION`             | AI-powered assertion that evaluates content against a prompt |
| `AI_DATA_EXTRACTION`        | AI-powered data extraction from content                      |
| `COMPARE`                   | Compares two values for equality                             |
| `CONTAINS`                  | Checks if a value contains a substring                       |
| `REGEX`                     | Matches content against a regular expression                 |
| `COSINE_SIMILARITY`         | Calculates semantic similarity between texts                 |
| `ABSOLUTE_NUMERIC_DISTANCE` | Calculates absolute difference between numbers               |
| `JSON_PATH`                 | Extracts data using JSONPath expressions                     |
| `XML_PATH`                  | Extracts data using XPath expressions                        |
| `REGEX_EXTRACTION`          | Extracts content using a regular expression                  |
| `PARSE_VALUE`               | Parses and converts values to a specific type                |
| `VARIABLE`                  | Static value or constant                                     |
| `ASSERT_VALID`              | Validates data format (JSON, number, SQL)                    |
| `COALESCE`                  | Returns first non-null value from multiple sources           |
| `COMBINE_COLUMNS`           | Combines multiple column values into a dict                  |
| `COUNT`                     | Counts chars, words, sentences, or paragraphs                |
| `MATH_OPERATOR`             | Numeric comparison operations                                |
| `MIN_MAX`                   | Finds minimum or maximum values                              |

## Scoring

There are two independent ways to calculate scores:

### Built-in Scoring (`is_part_of_score`)

Set `is_part_of_score: true` on columns to have PromptLayer automatically average their values into a score.

### Custom Scoring (`score_configuration`)

Write custom code that receives all report data and calculates the score however you want.

| Field           | Type     | Required | Description                                     |
| --------------- | -------- | -------- | ----------------------------------------------- |
| `code`          | `string` | Yes      | Python or JavaScript code for score calculation |
| `code_language` | `string` | No       | `"PYTHON"` (default) or `"JAVASCRIPT"`          |

Your custom code receives a `data` variable (list of row dictionaries with all column values) and must return a dictionary with at least a `score` key (0-100).

## Examples

### Built-in Scoring

Use `is_part_of_score: true` to have PromptLayer automatically average the column values:

```python  theme={null}
import requests

response = requests.post(
    "https://api.promptlayer.com/reports",
    headers={"X-API-Key": "your_api_key"},
    json={
        "dataset_group_id": 123,
        "name": "Pipeline with Built-in Scoring",
        "columns": [
            {
                "column_type": "LLM_ASSERTION",
                "name": "Accuracy Check",
                "configuration": {
                    "source": "response",
                    "prompt": "Is this response accurate?"
                },
                "is_part_of_score": True
            },
            {
                "column_type": "LLM_ASSERTION",
                "name": "Safety Check",
                "configuration": {
                    "source": "response",
                    "prompt": "Is this response safe?"
                },
                "is_part_of_score": True
            }
        ]
    }
)
```

### Custom Scoring

Use `score_configuration` to write custom scoring logic:

```python  theme={null}
import requests

response = requests.post(
    "https://api.promptlayer.com/reports",
    headers={"X-API-Key": "your_api_key"},
    json={
        "dataset_group_id": 123,
        "name": "Pipeline with Custom Scoring",
        "columns": [
            {
                "column_type": "LLM_ASSERTION",
                "name": "Accuracy Check",
                "configuration": {
                    "source": "response",
                    "prompt": "Is this response accurate?"
                }
            },
            {
                "column_type": "LLM_ASSERTION",
                "name": "Safety Check",
                "configuration": {
                    "source": "response",
                    "prompt": "Is this response safe?"
                }
            }
        ],
        "score_configuration": {
            "code": """
# Weighted scoring: accuracy matters more
weights = {"Accuracy Check": 0.7, "Safety Check": 0.3}
total_weight = weighted_sum = 0

for row in data:
    for col, weight in weights.items():
        if col in row:
            total_weight += weight
            if row[col] == True:
                weighted_sum += weight

score = (weighted_sum / total_weight * 100) if total_weight > 0 else 0
return {"score": round(score, 2)}
""",
            "code_language": "PYTHON"
        }
    }
)
```


## OpenAPI

````yaml POST /reports
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /reports:
    post:
      tags:
        - reports
      summary: Create Evaluation Pipeline
      description: >-
        Creates a new evaluation pipeline (report) with optional evaluation
        columns and custom scoring.
      operationId: createEvaluationPipeline
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
                dataset_group_id:
                  type: integer
                  description: >-
                    The ID of the dataset group containing the dataset versions
                    to evaluate. The dataset group must be within a workspace
                    accessible to the authenticated user.
                  minimum: 1
                name:
                  type: string
                  description: >-
                    Optional name for the evaluation pipeline. If not provided,
                    a unique name will be auto-generated. Must be between 1 and
                    255 characters if specified.
                  minLength: 1
                  maxLength: 255
                folder_id:
                  type: integer
                  description: >-
                    Optional folder ID to organize the pipeline within your
                    workspace. If not specified, the pipeline will be created at
                    the root level.
                  minimum: 1
                  nullable: true
                dataset_version_number:
                  type: integer
                  description: >-
                    Optional specific dataset version number to use. If not
                    specified, the latest non-draft version will be used. Cannot
                    be -1 (draft version).
                  nullable: true
                columns:
                  type: array
                  description: >-
                    Optional list of evaluation columns to create with the
                    pipeline.
                  items:
                    type: object
                    properties:
                      column_type:
                        type: string
                        description: >-
                          Type of column (e.g., LLM_ASSERTION, VARIABLE,
                          CODE_EXECUTION, PROMPT_TEMPLATE)
                      name:
                        type: string
                        description: Display name for the column
                      configuration:
                        type: object
                        description: Column-type-specific configuration
                      position:
                        type: integer
                        description: >-
                          Position in the pipeline (auto-assigned if not
                          provided)
                      is_part_of_score:
                        type: boolean
                        description: >-
                          Whether this column contributes to built-in score
                          averaging (defaults to false)
                    required:
                      - column_type
                      - name
                      - configuration
                score_configuration:
                  type: object
                  description: Optional custom scoring logic configuration.
                  properties:
                    code:
                      type: string
                      description: >-
                        Python or JavaScript code for score calculation.
                        Receives 'data' variable (list of row dictionaries) and
                        must return {'score': number}.
                    code_language:
                      type: string
                      enum:
                        - PYTHON
                        - JAVASCRIPT
                      description: Language of the code (defaults to PYTHON)
                  required:
                    - code
              required:
                - dataset_group_id
              example:
                dataset_group_id: 123
                name: QA Evaluation Pipeline
                columns:
                  - column_type: LLM_ASSERTION
                    name: Language Check
                    configuration:
                      source: response
                      prompt: Is the response written in {language}?
                      variable_mappings:
                        language: target_language
                    is_part_of_score: true
      responses:
        '201':
          description: Evaluation pipeline created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: Indicates if the operation was successful
                    example: true
                  report_id:
                    type: integer
                    description: >-
                      The unique ID of the created evaluation pipeline. Use this
                      ID to run evaluations.
                    example: 456
                  report_columns:
                    type: array
                    description: >-
                      List of created columns (only present if columns were
                      provided in the request)
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        report_id:
                          type: integer
                        column_type:
                          type: string
                        name:
                          type: string
                        position:
                          type: integer
                        is_part_of_score:
                          type: boolean
                        configuration:
                          type: object
                required:
                  - success
                  - report_id
                example:
                  success: true
                  report_id: 456
                  report_columns:
                    - id: 789
                      report_id: 456
                      column_type: LLM_ASSERTION
                      name: Language Check
                      position: 2
                      is_part_of_score: true
                      configuration:
                        source: response
                        prompt: Is the response written in {language}?
                        variable_mappings:
                          language: target_language
        '400':
          description: >-
            Bad Request - Invalid parameters, draft dataset version, or no
            datasets in group
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Dataset must have at least one non-draft version
        '401':
          description: Unauthorized - Invalid or missing authentication
        '403':
          description: >-
            Forbidden - Access to dataset group not allowed or missing
            permissions
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Access to this dataset group is not allowed
        '404':
          description: Not Found - Dataset group or version not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Dataset group not found

````