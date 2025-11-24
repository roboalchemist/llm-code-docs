# Source: https://docs.chatling.ai/api-reference/v2/project/list-settings.md

# List settings

> Retrieve the settings of the project.

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="project_id" type="string">
      The unique identifier of the project.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the project.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "project_id": "8917794239",
          "name": "My first project"
      }
  }
  ```
</ResponseExample>
