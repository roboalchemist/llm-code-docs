# Source: https://loops.so/docs/api-reference/examples/transactional-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Transactional email API examples

> Code examples for sending and querying transactional emails with the Loops API and SDKs.

## Send a transactional email

[API reference](/api-reference/send-transactional-email)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/transactional", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      transactionalId: "<transactional-id>",
      dataVariables: {
        loginUrl: "https://example.com/login",
      },
    }),
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.sendTransactionalEmail({
    email: "test@example.com",
    transactionalId: "<transactional-id>",
    dataVariables: {
      loginUrl: "https://example.com/login",
    },
  });
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->transactional->send(
    email: 'test@example.com',
    transactional_id: '<transactional-id>',
    data_variables: [
      'loginUrl' => 'https://example.com/login',
    ],
  );
  ```

  ```ruby Ruby SDK theme={"dark"}
  response = LoopsSdk::Transactional.send(
    email: "test@example.com",
    transactional_id: "<transactional-id>",
    data_variables: {
      loginUrl: "https://example.com/login",
    },
  )
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/transactional",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "transactionalId": "<transactional-id>",
          "dataVariables": {
              "loginUrl": "https://example.com/login",
          },
      }
  )
  ```
</CodeGroup>

## Send a transactional email with attachments

<Note>
  You must request attachments to be enabled in your account before you can send emails with them.
</Note>

[API reference](/api-reference/send-transactional-email#param-attachments)

<CodeGroup>
  ```js JavaScript {13-19} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/transactional", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      transactionalId: "<transactional-id>",
      dataVariables: {
        loginUrl: "https://example.com/login",
      },
      attachments: [
        {
          filename: "example.pdf",
          contentType: "application/pdf",
          data: "<base64-encoded-file-content>",
        },
      ],
    }),
  });
  ```

  ```js JavaScript SDK {11-17} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.sendTransactionalEmail({
    email: "test@example.com",
    transactionalId: "<transactional-id>",
    dataVariables: {
      loginUrl: "https://example.com/login",
    },
    attachments: [
      {
        filename: "example.pdf",
        contentType: "application/pdf",
        data: "<base64-encoded-file-content>",
      },
    ],
  });
  ```

  ```php PHP SDK {11-17} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->transactional->send(
    email: 'test@example.com',
    transactional_id: '<transactional-id>',
    data_variables: [
      'loginUrl' => 'https://example.com/login',
    ],
    attachments: [
      [
        'filename' => 'example.pdf',
        'content_type' => 'application/pdf',
        'data' => base64_encode(file_get_contents('path/to/example.pdf')),
      ],
    ],
  );
  ```

  ```ruby Ruby SDK {7-13} theme={"dark"}
  response = LoopsSdk::Transactional.send(
    email: "test@example.com",
    transactional_id: "<transactional-id>",
    data_variables: {
      loginUrl: "https://example.com/login",
    },
    attachments: [
      {
        filename: 'example.pdf',
        content_type: 'application/pdf',
        data: '<base64-encoded-file-content>',
      },
    ],
  )
  ```

  ```python Python {15-21} theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/transactional",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "transactionalId": "<transactional-id>",
          "dataVariables": {
              "loginUrl": "https://example.com/login",
          },
          "attachments": [
              {
                  "filename": "example.pdf",
                  "contentType": "application/pdf",
                  "data": "<base64-encoded-file-content>",
              },
          ],
      }
  )
  ```
</CodeGroup>

## Send a transactional email with an idempotency key

Add an `Idempotency-Key` header to the request to prevent duplicate requests.

[API reference](/api-reference/send-transactional-email#param-idempotency-key)

<CodeGroup>
  ```js JavaScript {6} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/transactional", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
      "Idempotency-Key": "550e8400-e29b-41d4-a716-446655440000",
    },
    body: JSON.stringify({
      email: "test@example.com",
      transactionalId: "<transactional-id>",
      dataVariables: {
        loginUrl: "https://example.com/login",
      },
    }),
  });
  ```

  ```js JavaScript SDK {11-13} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.sendTransactionalEmail({
    email: "test@example.com",
    transactionalId: "<transactional-id>",
    dataVariables: {
      loginUrl: "https://example.com/login",
    },
    headers: {
      "Idempotency-Key": "550e8400-e29b-41d4-a716-446655440000",
    },
  });
  ```

  ```php PHP SDK {11-13} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->transactional->send(
    email: 'test@example.com',
    transactional_id: '<transactional-id>',
    data_variables: [
      'loginUrl' => 'https://example.com/login',
    ],
    headers: [
      'Idempotency-Key' => '550e8400-e29b-41d4-a716-446655440000',
    ],
  );
  ```

  ```ruby Ruby SDK {7-9} theme={"dark"}
  response = LoopsSdk::Transactional.send(
    email: "test@example.com",
    transactional_id: "<transactional-id>",
    data_variables: {
      loginUrl: "https://example.com/login",
    },
    headers: {
      'Idempotency-Key' => '550e8400-e29b-41d4-a716-446655440000',
    },
  )
  ```

  ```python Python {8} theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/transactional",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json",
          "Idempotency-Key": "550e8400-e29b-41d4-a716-446655440000",
      },
      json={
          "email": "test@example.com",
          "transactionalId": "<transactional-id>",
          "dataVariables": {
              "loginUrl": "https://example.com/login",
          },
      }
  )
  ```
</CodeGroup>

## List published transactional emails

[API reference](/api-reference/list-transactional-emails)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/transactional", {
    method: "GET",
    headers: {
      "Authorization": "Bearer <your-api-key>",
    },
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.getTransactionalEmails();
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->transactional->get();
  ```

  ```ruby Ruby SDK theme={"dark"}

  response = LoopsSdk::Transactional.list(perPage: 50)
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.get(
      "https://app.loops.so/api/v1/transactional",
      headers={
          "Authorization": "Bearer <your-api-key>",
      },
  )
  ```
</CodeGroup>
