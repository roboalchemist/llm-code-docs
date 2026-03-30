# Source: https://www.courier.com/docs/platform/create/installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating the Embeddable Designer

> Courier Create is designed to be simple to embed and customize within your React application. This guide walks you through the basic setup and advanced usage patterns for integrating the Template Editor.

## Basic Setup

To start, install the [package](https://www.npmjs.com/package/@trycourier/react-designer/v/0.0.2):

<Note>Minimal supported React version is 18.2.0.</Note>

```bash  theme={null}
npm install @trycourier/react-designer
# or
yarn add @trycourier/react-designer
```

Import the required components and styles:

```jsx  theme={null}
import "@trycourier/react-designer/styles.css";
import { TemplateEditor, TemplateProvider } from "@trycourier/react-designer";
```

Use the components in your app:

```jsx  theme={null}
function App() {
  return (
    <TemplateProvider templateId="template-123" tenantId="tenant-123" token="your-jwt-token">
      <TemplateEditor />
    </TemplateProvider>
  );
}
```

<Note>The `TemplateProvider` creates the template automatically if it does not already exist. </Note>

### Authentication

The `token` prop on `TemplateProvider` accepts a JWT issued by the Courier API. Generate this token server-side and pass it to your frontend; never expose your API key in the browser.

```bash  theme={null}
curl --request POST \
  --url https://api.courier.com/auth/issue-token \
  --header 'Authorization: Bearer $YOUR_AUTH_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "scope": "user_id:$YOUR_USER_ID tenants:read tenants:notifications:read tenants:notifications:write",
    "expires_in": "30 days"
  }'
```

The example above grants access to all tenants. To restrict the token to a single tenant, use tenant-scoped scopes like `tenant:tenant-123:read` instead. See the [Authentication page](/platform/create/authentication) for the full list of available scopes.

### Publishing Hook

Users can override the default publish button with custom logic:

```jsx  theme={null}
import { TemplateEditor, TemplateProvider, useTemplateActions } from "@trycourier/react-designer";

function SaveButtonComponent() {
  const { publishTemplate } = useTemplateActions();

  const handlePublishTemplate = async () => {
    // Your custom logic here
    await publishTemplate();
  };

  return (
    <TemplateProvider templateId="template-123" tenantId="tenant-123" token="your-jwt-token">
      <TemplateEditor hidePublish />
      <button onClick={handlePublishTemplate}>Save Template</button>
    </TemplateProvider>
  );
}
```

### Theming Support

You can customize the editor's appearance using the theme prop:

```jsx  theme={null}
<TemplateEditor
  theme={{
    background: "#ffffff",
    foreground: "#292929",
    border: "#DCDEE4",
    primary: "#ffffff",
    primaryForeground: "#696F8C",
    radius: "6px",
    // Add more theme variables as needed
  }}
/>
```

### Disabling Auto-Save

By default, the Courier Create editor auto-saves content. To disable this feature, configure the provider as follows:

```jsx  theme={null}
const { saveTemplate, publishTemplate } = useTemplateActions();

const handleSaveTemplate = async () => {
  await saveTemplate(); // Save first
  await publishTemplate(); // Then publish
};

<TemplateProvider templateId="template-123" tenantId="tenant-123" token="your-jwt-token">
  <TemplateEditor autoSave={false} hidePublish />
  <button onClick={handleSaveTemplate}>Save Template</button>
</TemplateProvider>
```

### Restricting Visible Channels

You can restrict which channels appear in the template editor by using the `routing.channels` prop. This is useful when your application only uses specific channels (e.g., email-only workflows).

To show only email (hiding Slack, SMS, push, etc.):

```jsx  theme={null}
<TemplateEditor
  routing={{
    method: "single",
    channels: ["email"]
  }}
/>
```

The `channels` array controls which channels appear in the editor - any channels not in that array will be hidden. You can include multiple channels if needed:

```jsx  theme={null}
<TemplateEditor
  routing={{
    method: "single",
    channels: ["email", "sms"]
  }}
/>
```

The `method` property controls delivery strategy:

* `"single"` - delivers via first available channel (fallback routing)
* `"all"` - delivers via all configured channels simultaneously

Available channel values: `"email"`, `"sms"`, `"push"`, `"inbox"`, `"slack"`, `"msteams"`

## Using Variables

Variables are placeholders in your template that get replaced with actual data when the email is sent. For example, instead of writing `Hello customer` you can write Hello `{{user.firstName}}`, which will display the recipient's actual name.

The Courier Embeddable editor supports nested variable structures:

```jsx  theme={null}
<TemplateEditor
  variables={{
    user: {
      firstName: "John",
      lastName: "Doe",
      email: "john@example.com",
    },
    company: {
      name: "Acme Inc",
      address: {
        street: "123 Main St",
        city: "San Francisco",
      },
    },
  }}
/>
```

### How to Insert Variables

1. When editing text, type `{{` to open the variable suggestions dropdown. Select the variable you want to insert from the list.
2. Via curly braces `{}` icon in top toolbar (if the variables are available for selected element).

## Sending a Message

<Note>Ensure you include the `tenant_id` in the message `context` and `template` identifier.</Note>

```jsx  theme={null}
import { CourierClient } from "@trycourier/courier";

const courier = new CourierClient({ authorizationToken: "your-auth-token" });

const { requestId } = await courier.send({
  message: {
    context: {
      tenant_id: "tenant-123",
    },
    to: {
      email: "user@example.com",
      data: {
        name: "Spike Spiegel",
      },
    },
    template: "tenant/template-123", //`tenant/` must be prefixed with the template_id
  },
});

```

## Overview

Your sample implementation will look something like this:

```jsx  theme={null}
import React from "react";
import "@trycourier/react-designer/styles.css";
import {
  TemplateEditor,
  TemplateProvider,
  BrandEditor,
  BrandProvider
} from "@trycourier/react-designer";

// Replace with your own values
const token = process.env.REACT_APP_COURIER_TOKEN;
const tenantId = "test-tenant";
const templateId = "template-123";

function App() {
  return (
    <div>
      <TemplateProvider templateId={templateId} tenantId={tenantId} token={token}>
        <TemplateEditor 
         variables={{
				  "user": {
				    "firstName": "John",
				    "lastName": "Doe",
				    "email": "john@example.com"
				  },
				  "company": {
				    "name": "Acme Inc",
				    "address": {
				      "street": "123 Main St",
				      "city": "San Francisco"
				    }
				  }
				}}
        />
      </TemplateProvider>
    </div>
  );
}

export default App;

```

<Frame caption="Embeddable Designer Preview">
  <img src="https://mintcdn.com/courier-4f1f25dc/X4imlV9f_sunHT-I/platform/create/assets/create-overview.png?fit=max&auto=format&n=X4imlV9f_sunHT-I&q=85&s=39bddfcbfc663de20c2571ff8cb131ba" alt="Embeddable Designer" width="2060" height="1390" data-path="platform/create/assets/create-overview.png" />
</Frame>
