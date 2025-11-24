# Source: https://loops.so/docs/api-reference/examples/contacts.md

# Contacts API examples

> Code examples for managing contacts with the Loops API and SDKs.

## Create a contact

[API reference](/api-reference/create-contact)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/create", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: "test@example.com",
      firstName: "John",
      lastName: "Doe",
    }),
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.createContact(
    "test@example.com",
    {
      firstName: "John",
      lastName: "Doe"
    },
  );
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->create(
    email: 'test@example.com',
    properties: [
      'firstName' => 'John',
      'lastName' => 'Doe',
    ],
  );
  ```

  ```ruby Ruby SDK theme={"dark"}
  response = LoopsSdk::Contacts.create(
    email: "test@example.com",
    properties: {
      firstName: "John",
      lastName: "Doe",
    },
  )
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/contacts/create",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "firstName": "John",
          "lastName": "Doe"
      }
  )
  ```
</CodeGroup>

## Create a contact and add them to a mailing list

[API reference](/api-reference/create-contact)

<CodeGroup>
  ```js JavaScript {11-13} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/create", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: "test@example.com",
      firstName: "John",
      lastName: "Doe",
      mailingLists: {
        "<mailing-list-id>" => true
      },
    }),
  });
  ```

  ```js JavaScript SDK {10-12,17} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const properties = {
    firstName: "John",
    lastName: "Doe",
  };

  const mailingLists = {
    "<mailing-list-id>" => true,
  };

  const response = await loops.createContact(
    "test@example.com",
    properties,
    mailingLists,
  );
  ```

  ```php PHP SDK {11-13} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->create(
    email: 'test@example.com',
    properties: [
      'firstName' => 'John',
      'lastName' => 'Doe',
    ],
    mailing_lists: [
      '<mailing-list-id>' => TRUE,
    ],
  );
  ```

  ```ruby Ruby SDK {7-9} theme={"dark"}
  response = LoopsSdk::Contacts.create(
    email: "test@example.com",
    properties: {
      firstName: "John",
      lastName: "Doe",
    },
    mailing_lists: {
      "<mailing-list-id>" => true,
    },
  )
  ```

  ```python Python {13-15} theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/contacts/create",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "firstName": "John",
          "lastName": "Doe",
          "mailingLists": {
              "<mailing-list-id>": True
          }
      }
  )
  ```
</CodeGroup>

## Update a contact

When updating a contact you must provide an `email` or `userId` value to identify the contact.

<Tip>
  You can use the "update" endpoint to update or create contacts. If the provided email or user ID does not exist, a new contact will be created.
</Tip>

[API reference](/api-reference/update-contact)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/update", {
    method: "PUT",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      planName: "Pro",
    }),
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";  

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.updateContact(
    "test@example.com",
    {
      planName: "Pro",
    },
  );
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->update(
    email: 'test@example.com',
    properties: [
      'planName' => 'Pro',
    ],
  );
  ```

  ```ruby Ruby SDK theme={"dark"}
  response = LoopsSdk::Contacts.update(
    email: "test@example.com",
    properties: {
      planName: "Pro",
    },
  )
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.put(
      "https://app.loops.so/api/v1/contacts/update",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "planName": "Pro"
      }
  )
  ```
</CodeGroup>

## Update a contact's email address

For this the contact will need to already have a `userId` value set.

[API reference](/api-reference/update-contact)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/update", {
    method: "PUT",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      userId: "12345",
      email: "new-email@example.com",
    }),
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.updateContact(
    "new-email@example.com",
    {
      userId: "12345",
    },
  );
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->update(
    email: 'new-email@example.com',
    properties: [
      'userId' => '12345',
    ],
  );
  ```

  ```ruby Ruby SDK theme={"dark"}
  response = LoopsSdk::Contacts.update(
    email: "new-email@example.com",
    properties: {
      userId: "12345",
    },
  )
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.put(
      "https://app.loops.so/api/v1/contacts/update",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "new-email@example.com",
          "userId": "12345"
      }
  )
  ```
</CodeGroup>

## Subscribe a contact to a mailing list

[API reference](/api-reference/update-contact)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/update", {
    method: "PUT",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      mailingLists: {
        "<mailing-list-id>" => true
      },
    }),
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.updateContact(
    "test@example.com",
    {},
    {
      "<mailing-list-id>": true,
    },
  );
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->update(
    email: 'test@example.com',
    mailing_lists: [
      '<mailing-list-id>' => TRUE,
    ],
  );
  ```

  ```ruby Ruby SDK theme={"dark"}
  response = LoopsSdk::Contacts.update(
    email: "test@example.com",
    mailing_lists: {
      "<mailing-list-id>" => true,
    },
  )
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.put(
      "https://app.loops.so/api/v1/contacts/update",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "mailingLists": {
              "<mailing-list-id>": True
          }
      }
  )
  ```
</CodeGroup>

## Unsubscribe a contact from a mailing list

This removes a contact from a specific mailing list. [See below](#unsubscribe-a-contact) to see how to fully unsubscribe a contact.

Use `false` to unsubscribe a contact from a mailing list.

[API reference](/api-reference/update-contact)

<CodeGroup>
  ```js JavaScript {9-11} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/update", {
    method: "PUT",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      mailingLists: {
        "<mailing-list-id>" => false
      },
    }),
  });
  ```

  ```js JavaScript SDK {8-10} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.updateContact(
    "test@example.com",
    {},
    {
      "<mailing-list-id>" => false,
    },
  );
  ```

  ```php PHP SDK {7-9} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->update(
    email: 'test@example.com',
    mailing_lists: [
      '<mailing-list-id>' => FALSE,
    ],
  );
  ```

  ```ruby Ruby SDK {3-5} theme={"dark"}
  response = LoopsSdk::Contacts.update(
    email: "test@example.com",
    mailing_lists: {
      "<mailing-list-id>" => false,
    },
  )
  ```

  ```python Python {11-13} theme={"dark"}
  import requests

  response = requests.put(
      "https://app.loops.so/api/v1/contacts/update",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "mailingLists": {
              "<mailing-list-id>": False
          }
      }
  )
  ```
</CodeGroup>

## Unsubscribe a contact

Set `subscribed` to `false` to unsubscribe a contact. The contact will no longer receive campaign or loop emails, but will remain listed in your audience.

[API reference](/api-reference/update-contact)

<CodeGroup>
  ```js JavaScript {9} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/update", {
    method: "PUT",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      subscribed: false,
    }),
  });
  ```

  ```js JavaScript SDK {7-9} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.updateContact(
    "test@example.com",
    {
      subscribed: false,
    },
  );
  ```

  ```php PHP SDK {7} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->update(
    email: 'test@example.com',
    subscribed: false,
  );
  ```

  ```ruby Ruby SDK {3} theme={"dark"}
  response = LoopsSdk::Contacts.update(
    email: "test@example.com",
    subscribed: false,
  )
  ```

  ```python Python {11} theme={"dark"}
  import requests

  response = requests.put(
      "https://app.loops.so/api/v1/contacts/update",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "subscribed": False
      }
  )
  ```
</CodeGroup>

## Delete a contact

You can delete contacts by email or user ID.

[API reference](/api-reference/delete-contact)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/contacts/delete", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
    }),
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.deleteContact({
    email: "test@example.com",
  });
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->contacts->delete(
    email: 'test@example.com',
  );
  ```

  ```ruby Ruby SDK theme={"dark"}
  response = LoopsSdk::Contacts.delete(
    email: "test@example.com",
  )
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/contacts/delete",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
      }
  )
  ```
</CodeGroup>
