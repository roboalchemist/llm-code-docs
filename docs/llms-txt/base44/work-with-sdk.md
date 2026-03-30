# Source: https://docs.base44.com/developers/references/sdk/getting-started/work-with-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Common SDK uses

> Work with authentication, integrations, functions, and error handling

Beyond data management, the Base44 SDK provides modules for authentication, integrations, custom backend functions, and more. This guide covers common patterns for working with these features.

## Authentication

The `auth` module provides methods for working with user authentication. The most common use case is getting information about the currently authenticated user.

<CodeGroup>
  ```typescript Get current user theme={null}
  const user = await base44.auth.me();
  console.log(user.email, user.name, user.role);
  ```

  ```typescript Check authentication status theme={null}
  const isAuthenticated = await base44.auth.isAuthenticated();

  if (!isAuthenticated) {
    // Redirect to login or show auth prompt
  }
  ```

  ```typescript Log out theme={null}
  base44.auth.logout();
  ```
</CodeGroup>

## Core integrations

Base44 provides built-in integrations for common tasks like working with AI, sending emails, and handling files. Access these through the `integrations.Core` module.

<CodeGroup>
  ```typescript Generate AI responses theme={null}
  const response = await base44.integrations.Core.InvokeLLM({
    prompt: "Write a welcome email for a new user",
    responseFormat: "text",
  });
  ```

  ```typescript Send an email theme={null}
  await base44.integrations.Core.SendEmail({
    to: "user@example.com",
    subject: "Welcome to our app",
    html: "<h1>Welcome!</h1><p>Thanks for joining.</p>",
  });
  ```

  ```typescript Upload a file theme={null}
  const result = await base44.integrations.Core.UploadFile({
    file: fileObject,
    fileName: "document.pdf",
  });
  console.log(result.url);
  ```

  ```typescript Generate an image theme={null}
  const image = await base44.integrations.Core.GenerateImage({
    prompt: "A sunset over mountains",
    size: "1024x1024",
  });
  console.log(image.url);
  ```
</CodeGroup>

## Backend functions

The `functions` module lets you invoke custom backend functions defined in your app. Pass any data your function needs as parameters.

<CodeGroup>
  ```typescript Invoke a function theme={null}
  const result = await base44.functions.invoke("processOrder", {
    orderId: "123",
    action: "fulfill",
  });
  ```
</CodeGroup>

## Error handling

All SDK errors are instances of `Base44Error`, which includes the HTTP status code and error details. Use this to handle different error scenarios gracefully.

<CodeGroup>
  ```typescript Handle errors theme={null}
  import { Base44Error } from "@base44/sdk";

  try {
    const result = await base44.entities.Task.list();
  } catch (error) {
    if (error instanceof Base44Error) {
      console.error(`Status: ${error.status}`);
      console.error(`Message: ${error.message}`);
      console.error(`Code: ${error.code}`);
    } else {
      console.error("Unexpected error:", error);
    }
  }
  ```
</CodeGroup>

## See more

<CardGroup cols={2}>
  <Card title="Base44 client" icon="code" href="/developers/references/sdk/getting-started/client">
    Work with the client in different contexts
  </Card>

  <Card title="auth module" icon="lock" href="/developers/references/sdk/docs/interfaces/auth">
    Complete authentication API reference
  </Card>

  <Card title="integrations module" icon="plug" href="/developers/references/sdk/docs/type-aliases/integrations">
    Complete integrations API reference
  </Card>

  <Card title="functions module" icon="code" href="/developers/references/sdk/docs/interfaces/functions">
    Complete functions API reference
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).