# Source: https://loops.so/docs/api-reference/send-event.md

# Send event

> Send events to trigger emails in Loops.

## Request

### Body

<Note>
  Provide either an `email` or `userId` value or both to identify the contact.\
  If both are provided, the system will look for a contact with either a
  matching `email` or `userId` value. If a contact is found for one of the
  values (e.g. `email`), the other value (e.g. `userId`) will be updated. If a
  contact is not found, a new contact will be created using both `email` and
  `userId` values.
</Note>

<ParamField body="email" type="string">
  The contact's email address.\
  **Required if `userId` is not provided.**
</ParamField>

<ParamField body="userId" type="string">
  The contact's unique user ID. This must already have been added to your
  contact in Loops.\
  **Required if `email` is not provided.**
</ParamField>

<ParamField body="eventName" type="string" required>
  The name of the event.
</ParamField>

<ParamField body="eventProperties" type="object">
  An object containing event property data for the event. Values can be of type
  `string`, `number`, `boolean` or `date`. [Read more](/events/properties)
</ParamField>

<ParamField body="mailingLists" type="object">
  Manage the contact's mailing list subscriptions.\
  Include key-value pairs of mailing list IDs and a `boolean` denoting if the contact
  should be added (`true`) or removed (`false`) from the list. [Read
  more](/contacts/mailing-lists#add-contacts-to-lists-with-the-api)

  ```json  theme={"dark"}
  {
    "mailingLists": {
      "cm06f5v0e45nf0ml5754o9cix": true,
      "cm16k73gq014h0mmj5b6jdi9r": false
    }
  }
  ```
</ParamField>

### Contact properties

You can also include default and custom [contact properties](/contacts/properties) in your request body, which will update the contact in Loops. These should be added as top-level attributes in the request.

Contact properties can be of type `string`, `number`, `boolean` or `date` ([see allowed date formats](/contacts/properties#dates)).

```json  theme={"dark"}
{
  "email": "hello@gmail.com",
  "eventName": "signup",
  "firstName": "Bob", /* Contact property */
  "plan": "pro" /* Custom contact property */
}
```

<Note>
  There are a few [reserved names](/contacts/properties#reserved-names) that you cannot use for custom properties.
</Note>

<Tip>
  To empty or reset the value of a contact property, send a `null` value.
</Tip>

### Headers

<ParamField header="Idempotency-Key" type="string">
  Optionally send an idempotency key to avoid duplicate requests.\
  The value should be a string of up to 100 characters and should be unique for each request. We recommend using V4 UUIDs or some other method with enough guaranteed entropy to avoid collisions during a 24 hour window.\
  The endpoint will return a `409 Conflict` response if the idempotency key has been used in the previous 24 hours.
</ParamField>

## Response

### Success

<ResponseField name="success" type="boolean" required />

### Error

If you send an idempotency key which has already been used in the previous 24 hours, a `409 Conflict` response will be returned.

All other errors will be `400 Bad Request`.

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
