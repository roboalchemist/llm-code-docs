# Source: https://docs.chatling.ai/api-reference/v2/members/list-members.md

# List members

> Get a list of all the members in the project.

## Request parameters

### Query

<ParamField query="page" type="integer" default="1">
  The page number for pagination.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="pages" type="object">
      <Expandable title="properties">
        <ResponseField name="current_page" type="integer">
          The current page number.
        </ResponseField>

        <ResponseField name="last_page" type="integer">
          The last page number.
        </ResponseField>

        <ResponseField name="per_page" type="integer">
          The number of items per page.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="members" type="array">
      <Expandable title="properties">
        <ResponseField name="email" type="string">
          The email address of the member.
        </ResponseField>

        <ResponseField name="status" type="string">
          The status of the member (`Active` or `Pending`).
        </ResponseField>

        <ResponseField name="roles" type="array">
          The roles of the member in the project.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "pages": {
              "current_page": 1,
              "last_page": 1,
              "per_page": 15
          },
          "members": [
              {
                  "email": "elon@tesla.com",
                  "status": "Active",
                  "roles": [
                      "Owner"
                  ]
              },
              {
                  "email": "mark@meta.com",
                  "status": "Active",
                  "roles": [
                      "Admin"
                  ]
              },
              {
                  "email": "sundar@google.com",
                  "status": "Pending",
                  "roles": [
                      "Editor",
                      "Billing"
                  ]
              }
          ]
      }
  }
  ```
</ResponseExample>
