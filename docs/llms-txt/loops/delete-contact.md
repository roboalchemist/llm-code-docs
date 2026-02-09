# Source: https://loops.so/docs/api-reference/delete-contact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete contact

> Delete a contact by email address or user ID.

## Request

### Body

You can delete a contact by using either their `email` or `userId` value.

<ParamField body="email" type="string">
  The contact's email address.
</ParamField>

<ParamField body="userId" type="string">
  The contact's `userId` value.
</ParamField>

## Response

### Success

<ResponseField name="success" type="boolean" required />

<ResponseField name="message" type="string" required>
  "Contact deleted."
</ResponseField>

### Error

If a matching contact is not found, a `404 Not Found` will be returned. All other errors will be `400 Bad Request`.

<ResponseField name="success" type="boolean" required />

<ResponseField name="message" type="string" required>
  An error message describing the problem with the request.
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  {
    "success": true,
    "message": "Contact deleted."
  }
  ```

  ```json Error response theme={"dark"}
  {
    "success": false,
    "message": "An error message."
  }
  ```
</ResponseExample>
