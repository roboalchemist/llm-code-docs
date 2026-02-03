# Source: https://loops.so/docs/api-reference/create-contact-property.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create contact property

> Create a new contact property.

## Request

### Body

<ParamField body="name" type="string" required>
  The name of the property.\
  This should be in `camelCase`, like `planName` or `favoriteColor`.
</ParamField>

<ParamField body="type" type="string" required>
  The property's value type.

  Allowed values:

  * `string`
  * `number`
  * `boolean`
  * `date`
</ParamField>

<Note>
  There are a few [reserved names](/contacts/properties#reserved-names) that you
  cannot use for contact properties.
</Note>

## Response

### Success

<ResponseField name="success" type="boolean" required />

### Error

Errors will be `400 Bad Request`.

<ResponseField name="success" type="boolean" required />

<ResponseField name="message" type="string" required>
  An error message describing the problem with the request.
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  {
    "success": true
  }
  ```

  ```json Error response theme={"dark"}
  {
    "success": false,
    "message": "An error message."
  }
  ```
</ResponseExample>
