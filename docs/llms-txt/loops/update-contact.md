# Source: https://loops.so/docs/api-reference/update-contact.md

# Update contact

> Update or create a contact.

Update an existing contact by sending a request containing contact properties.

This endpoint will create a contact if a matching contact does not already exist in your audience.

<Tip>
  If you want to update a contact's email address, the contact will first need a
  `userId` value. You can then make a request containing the `userId` field
  along with an updated email address.
</Tip>

## Request

### Body

<Note>
  Provide either `email` or `userId` to identify the contact you want to update.\
  If both are provided, the system will look for a contact with either a
  matching `email` or `userId` value. If a contact is found for one of the
  values (e.g. `email`), the other value (e.g. `userId`) will be updated. If a
  contact is not found, a new contact will be created using both `email` and
  `userId` values.
</Note>

<ParamField body="email" type="string">
  The contact's email address. If there is no contact with this email, one will
  be created.\
  **Required if `userId` is not provided.**
</ParamField>

<ParamField body="userId" type="string">
  A unique user ID (for example, from an external application). [Read
  more](/contacts/properties#user-id)
  **Required if `email` is not provided.**
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

<ParamField body="subscribed" type="boolean">
  Whether the contact will receive campaign and loops emails. [Read
  more](/contacts/properties#subscribed).

  <Warning>
    If you send `subscribed: true` in your update calls, contacts who have
    previously unsubscribed will be re-subscribed. We recommend leaving this
    field out of your requests unless you specifically want to unsubscribe or
    re-subscribe a contact.
  </Warning>
</ParamField>

<ParamField body="userGroup" type="string">
  You can use groups to segment users when sending emails. Currently, a contact
  can only be in one user group. [Read more](/contacts/properties#user-group)
</ParamField>

<ParamField body="mailingLists" type="object">
  Manage mailing list subscriptions.\
  Include key-value pairs of mailing list IDs and a `boolean` denoting if the contact should be added (`true`) or removed (`false`) from the list. [Read
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
  "favoriteColor": "Blue" /* Custom property */
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
  The ID of the contact.
</ResponseField>

### Error

Errors will be `400 Bad Request`.

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
    "message": "An error message."
  }
  ```
</ResponseExample>
