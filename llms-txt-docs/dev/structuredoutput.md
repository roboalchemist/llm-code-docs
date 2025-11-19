# Source: https://dev.writer.com/blueprints/structuredoutput.md

# Structured output

Allows to define a JSON response format, which the agent will use to structure its output.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c076d45dd7890a11f83ccb8080ff8c27" alt="" data-og-width="2188" width="2188" data-og-height="1456" height="1456" data-path="images/agent-builder/blueprints/structured-output-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=870c0941bdc69bd910a40869fadde28b 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=693cb70fc92838c821d42a51c8add4e0 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3f39c493f83a20e42567cf8460f75dc6 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=cc0df85f56d8bd645ac9b90a32d9e2f5 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=23d2d5f5ee532c7aa14c998da2521d9b 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c855a4318b04d32bb6350549b53c4102 2500w" />

## Overview

The **Structured Output** block allows you to define a JSON response format that the AI model uses to structure its output. This is useful when you need the model to return data in a specific schema, such as for downstream processing, API responses, reliable data extraction, or integrations. The block returns the JSON object that matches the schema.

You can specify a prompt describing the data you want, and provide a [JSON Schema](https://json-schema.org/) to enforce the structure of the output. The model attempts to generate a response that matches the schema.

## Common use cases

* Extracting structured data from unstructured text; for example, extracting entities, tables, or key-value pairs
* Generating API responses in a specific format
* Creating objects for further automation or integration
* Enforcing data validation on AI-generated output

## How it works

1. **Prompt**: Describe the data you want the model to generate.
2. **JSON Schema**: Define the required structure for the output. See [JSON Schema](https://json-schema.org/) for more information about how to write a JSON Schema.
3. **Model**: Select the model to use for generation.
4. **Max output tokens**: Set the maximum length of the output.

The block sends the prompt and schema to the model, which returns a JSON object matching the schema. If the output isn't parsable as JSON or doesn't match the schema, the block raises an error.

## Examples

### Data extraction from documents

This example shows how to extract structured data from unstructured documents using AI.

**Blueprint Flow:**

1. **UI Trigger** → User selects a document from the interface
2. **Parse PDF tool** → Extracts text from document. Note: the document must already be uploaded to the Writer cloud.
3. **Structured output** → Extracts specific data fields
4. **HTTP Request** → Sends structured data to external API

**Block Configuration:**

* **Prompt:** "Extract the following information from the document. Document content: @{result}. Return the data in the following format: company name, contact person, email, phone number, and address."

* **JSON Schema:**

  ```json  theme={null}
  {
    "type": "object",
    "properties": {
      "company_name": {"type": "string"},
      "contact_person": {"type": "string"},
      "title": {"type": "string"},
      "email": {"type": "string", "format": "email"},
      "phone": {"type": "string"},
      "address": {"type": "string"}
    },
    "required": ["company_name", "contact_person", "email"],
    "additionalProperties": false
  }
  ```

* **Model:** `palmyra-x5`

This workflow enables automated extraction of structured data from unstructured documents.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=28b740cca2a244b2001580a4b1446dc5" alt="" data-og-width="2104" width="2104" data-og-height="1446" height="1446" data-path="images/agent-builder/blueprints/structured-output-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b4279b1d5ff05201faae3624a50612cb 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5dfb494596ffde326b48960c3b8cebcd 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=82c63586a3a5244d043b46aac87322bc 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=71f1cbc1b5606e58ae7ceceb24a93c74 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=eec0384750a4c4bfd87006c015154c1c 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/structured-output-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f73a952d15924b89dae2cb0ef656536e 2500w" />

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Prompt</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>Description of a JSON object to be created.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Model</td>
      <td>Model Id</td>
      <td>-</td>

      <td>
        <code>palmyra-x5</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>JSON Schema</td>
      <td>JSON</td>
      <td>-</td>

      <td>
        <code>
          {"{}"}
        </code>
      </td>

      <td>JSON schema that defines the structure of the response. For example, `{"type": "object", "properties": {...}, "required": [...]}`.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Max output tokens</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <code>1024</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Range:
        1    to  16384
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>If the function doesn't raise an Exception.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>If the function raises an Exception.</td>
    </tr>
  </tbody>
</table>

The **Structured Output** block returns the JSON object that matches the schema. You can access this value in the following block as `@{result}`.
