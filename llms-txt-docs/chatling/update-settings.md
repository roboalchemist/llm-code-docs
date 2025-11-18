# Source: https://docs.chatling.ai/api-reference/v2/project/update-settings.md

# Update settings

> Update the project settings.

## Request parameters

### Body

<ParamField body="name" type="string" required>
  The project name.
</ParamField>

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
          "name": "My project"
      }
  }
  ```
</ResponseExample>
