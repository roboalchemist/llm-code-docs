# Source: https://loops.so/docs/api-reference/find-contact.md

# Find contact

> Find a contact by email address or user ID.

## Request

### Query parameters

Search by email or user ID. Only one parameter is allowed.

<ParamField query="email" type="string">
  The contact's email address. Make sure it is
  [URI-encoded](https://en.wikipedia.org/wiki/Percent-encoding).
</ParamField>

<ParamField query="userId" type="string">
  The contact's unique user ID.
</ParamField>

## Response

This endpoint will return a list of contact objects containing all default properties and any [custom properties](/contacts/properties).

If no contact is found, an empty list will be returned.

<ResponseField name="Contacts" type="array">
  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string">
      The contact's Loops-assigned ID.
    </ResponseField>

    <ResponseField name="email" type="string">
      The contact's email address.
    </ResponseField>

    <ResponseField name="firstName" type="string">
      The contact's first name.
    </ResponseField>

    <ResponseField name="lastName" type="string">
      The contact's last name.
    </ResponseField>

    <ResponseField name="source" type="string">
      The source the contact was created from.
    </ResponseField>

    <ResponseField name="subscribed" type="boolean">
      Whether the contact will receive campaign and loops emails.
    </ResponseField>

    <ResponseField name="userGroup" type="string">
      The contact's user group.
    </ResponseField>

    <ResponseField name="userId" type="string">
      The contact's unique user ID.
    </ResponseField>

    <ResponseField name="mailingLists" type="object">
      Mailing lists the contact is subscribed to, represented by key-value pairs of mailing list IDs and `true`.
    </ResponseField>

    <ResponseField name="optInStatus" type="string">
      The contact's [double opt-in](/contacts/double-opt-in) status.\
      One of: `"pending"`, `"accepted"`, `"rejected"` or `null`.

      <Note>
        This will be `null` for contacts unless they are created via a form while double opt-in is enabled.
      </Note>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  [
    {
      "id": "cll6b3i8901a9jx0oyktl2m4u",
      "email": "hello@gmail.com",
      "firstName": "Bob",
      "lastName": null,
      "source": "API",
      "subscribed": true,
      "userGroup": "",
      "userId": null,
      "mailingLists": {
        "cm06f5v0e45nf0ml5754o9cix": true
      },
      "optInStatus": "accepted"
    }
  ]
  ```

  ```json No contact found response theme={"dark"}
  []
  ```
</ResponseExample>
