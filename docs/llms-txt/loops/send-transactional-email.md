# Source: https://loops.so/docs/api-reference/send-transactional-email.md

# Send transactional email

> Send a transactional email to a contact.

## Request

### Body

<ParamField body="email" type="string" required>
  The email address of the recipient.
</ParamField>

<ParamField body="transactionalId" type="string" required>
  The ID of the transactional email to send.
</ParamField>

<ParamField body="addToAudience" type="boolean" default={false}>
  If `true`, a contact will be created in your audience using the `email` value
  (if a matching contact doesn't already exist).
</ParamField>

<ParamField body="dataVariables" type="object">
  An object containing data as defined by the data variables added to the
  transactional email template. Values can be of type `string` or `number`. If
  you have added [optional data
  variables](/transactional#optional-data-variables) to your email, you can
  exclude them from the `dataVariables` object or set the value to `""`.
</ParamField>

<ParamField body="attachments" type="object[]">
  <Note>
    Please [email us](mailto:help@loops.so) to enable attachments on your
    account before using them with the API.
  </Note>

  An array containing file objects sent along with an email message.

  <Expandable>
    <ParamField body="filename" type="string">
      The name of the file, shown in email clients.
    </ParamField>

    <ParamField body="contentType" type="string">
      The MIME type of the file.
    </ParamField>

    <ParamField body="data" type="string">
      The base64-encoded content of the file.
    </ParamField>
  </Expandable>
</ParamField>

<Info>
  To set dynamic Subject, From, Reply to, CC, BCC email header fields, add data
  variables to those fields in the editor, then include data for each variable
  in the API request. Read our [transactional email
  guide](/transactional#data-variables-in-email-headers) for more details.
</Info>

### Headers

<ParamField header="Idempotency-Key" type="string">
  Optionally send an idempotency key to avoid duplicate requests. The value
  should be a string of up to 100 characters and should be unique for each
  request. We recommend using V4 UUIDs or some other method with enough
  guaranteed entropy to avoid collisions during a 24 hour window. The endpoint
  will return a `409 Conflict` response if the idempotency key has been used in
  the previous 24 hours.
</ParamField>

## Response

### Success

<ResponseField name="success" type="boolean" required />

### Error

If the transactional email is not found, a `404 Not Found` will be returned.

If you send an idempotency key which has already been used in the previous 24 hours, a `409 Conflict` response will be returned.

All other errors will be `400 Bad Request`.

<Info>
  Deprecated fields will be removed in the future so avoid using them in your
  code.
</Info>

<ResponseField name="success" type="boolean" required />

<ResponseField name="message" type="string" required />

<ResponseField name="path" type="string" deprecated />

<ResponseField name="error" type="object" deprecated />

<ResponseField name="transactionalId" type="string" deprecated />

<ResponseExample>
  ```json Response theme={"dark"}
  {
    "success": true
  }
  ```

  ```json Typical error response theme={"dark"}
  {
    "success": false,
    "message": "An error message."
  }
  ```

  ```json Error response 2 theme={"dark"}
  {
    "success": false,
    "message": "An error message.",
    "path": "<path>"
  }
  ```

  ```json Error response 3 theme={"dark"}
  {
    "success": false,
    "message": "An error message.",
    "error": {
      "path": "<path>",
      "message": "An error message."
    },
  }
  ```

  ```json Error response 4 theme={"dark"}
  {
    "success": false,
    "message": "An error message.",
    "error": {
      "path": "<path>",
      "reason": "An error message."
    },
  }
  ```

  ```json Error response 5 theme={"dark"}
  {
    "success": false,
    "message": "An error message.",
    "error": {
      "path": "<path>",
      "message": "An error message."
    },
    "transactionalId": "<transactional-id>"
  }
  ```
</ResponseExample>
