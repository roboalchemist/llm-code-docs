# Source: https://loops.so/docs/api-reference/create-contact.md

# Create contact

> Create a new contact with an email address and any other contact properties.

<Tip>
  If you want to "update or create" contacts, consider using the [Update a
  contact](/api-reference/update-contact) endpoint instead.
</Tip>

## Request

### Body

<ParamField body="email" type="string" required>
  The contact's email address.
</ParamField>

<ParamField body="firstName" type="string">
  The contact's first name.
</ParamField>

<ParamField body="lastName" type="string">
  The contact's last name.
</ParamField>

<ParamField body="source" type="string">
  A custom source value to replace the default "API". [Read
  more](/contacts/properties#source)
</ParamField>

<ParamField body="subscribed" type="boolean" default={true}>
  Whether the contact will receive campaign and loops emails. [Read
  more](/contacts/properties#subscribed)
</ParamField>

<ParamField body="userGroup" type="string">
  You can use groups to segment users when sending emails. Currently, a contact
  can only be in one user group. [Read more](/contacts/properties#user-group)
</ParamField>

<ParamField body="userId" type="string">
  A unique user ID (for example, from an external application). [Read
  more](/contacts/properties#user-id)
</ParamField>

<ParamField body="mailingLists" type="object">
  Manage mailing list subscriptions.\
  Include key-value pairs of mailing list IDs and a `boolean` denoting if the contact
  should be added (`true`) or removed (`false`) from the list. [Read
  more](/contacts/mailing-lists#add-contacts-to-lists-with-the-api)

  ```json  theme={"dark"}
  "mailingLists": {
    "cm06f5v0e45nf0ml5754o9cix": true,
    "cm16k73gq014h0mmj5b6jdi9r": false
  }
  ```
</ParamField>

### Custom properties

You can also include [custom contact properties](/contacts/properties) in your request body. These should be added as top-level attributes in the request.

Custom properties can be of type `string`, `number`, `boolean` or `date` ([see allowed date formats](/contacts/properties#dates)).

```json  theme={"dark"}
{
  "email": "hello@gmail.com",
  "plan": "pro" /* Custom property */,
  "dateJoined": 1704711066 /* Custom property */
}
```

<Note>
  There are a few [reserved names](/contacts/properties#reserved-names) that you
  cannot use for custom properties.
</Note>

<Tip>
  To empty or reset the value of a contact property, send a `null` value.
</Tip>

## Response

### Success

<ResponseField name="success" type="boolean" required />

<ResponseField name="id" type="string" required>
  The ID of the new contact.
</ResponseField>

### Error

If a matching contact already exists in your audience, a `409 Conflict` error will be returned. All other errors will be `400 Bad Request`.

<ResponseField name="success" type="boolean" required />

<ResponseField name="message" type="string" required>
  An error message describing the problem with the request.
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  {
    "success": true,
    "id": "id_of_contact"
  }
  ```

  ```json Error response theme={"dark"}
  {
    "success": false,
    "message": "An error message"
  }
  ```
</ResponseExample>
