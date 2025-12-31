# Source: https://loops.so/docs/api-reference/list-contact-properties.md

# List contact properties

> Retrieve a list of your account's contact properties.

## Request

### Query parameters

<ParamField query="list" type="string">
  Use `?list=custom` to only list your team's custom properties.
</ParamField>

## Response

This endpoint will return a list of contact property objects.

<ResponseField name="Contact properties" type="array">
  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="key" type="string">
      The property's name key.
    </ResponseField>

    <ResponseField name="label" type="string">
      The human-friendly label for this property.
    </ResponseField>

    <ResponseField name="type" type="string">
      The type of property (one of `string`, `number`, `boolean` or `date`).
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  [ 
    {
      "key": "firstName",
      "label": "First Name",
      "type": "string"
    },
    {
      "key": "lastName",
      "label": "Last Name",
      "type": "string"
    },
    {
      "key": "email",
      "label": "Email",
      "type": "string"
    },
    {
      "key": "notes",
      "label": "Notes",
      "type": "string"
    },
    {
      "key": "source",
      "label": "Source",
      "type": "string"
    },
    {
      "key": "userGroup",
      "label": "User Group",
      "type": "string"
    },
    {
      "key": "userId",
      "label": "User Id",
      "type": "string"
    },
    {
      "key": "subscribed",
      "label": "Subscribed",
      "type": "boolean"
    },
    {
      "key": "createdAt",
      "label": "Created At",
      "type": "date"
    },
    {
      "key": "favoriteColor",
      "label": "Favorite Color",
      "type": "string"
    },
    {
      "key": "plan",
      "label": "Plan",
      "type": "string"
    }
  ]
  ```

  ```json Custom-only Response theme={"dark"}
  [
    {
      "key": "favoriteColor",
      "label": "Favorite Color",
      "type": "string"
    },
    {
      "key": "plan",
      "label": "Plan",
      "type": "string"
    }
  ]
  ```
</ResponseExample>
