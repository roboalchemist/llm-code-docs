# Source: https://flatfile.com/docs/embedding/react.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# React Embedding

> Embed Flatfile in React applications

Embed Flatfile in your React application using our React SDK. This provides React components and hooks for seamless integration.

## Installation

```bash  theme={null}
npm install @flatfile/react
```

## Basic Implementation

### 1. Wrap Your App

Wrap your application with the `FlatfileProvider`:

```jsx  theme={null}
import { FlatfileProvider } from "@flatfile/react";

function App() {
  return (
    <FlatfileProvider publishableKey="pk_your_publishable_key">
      <YourApp />
    </FlatfileProvider>
  );
}
```

### 2. Add Import Trigger

Use the `useFlatfile` hook to open Flatfile:

```jsx  theme={null}
import { useFlatfile } from "@flatfile/react";

function YourComponent() {
  const { openPortal } = useFlatfile();

  const handleImport = () => {
    openPortal({});
  };

  return (
    <div>
      <h1>Welcome to our app</h1>
      <button onClick={handleImport}>Import Data</button>
    </div>
  );
}
```

### 3. Get Your Credentials

**publishableKey**: Get from [Platform Dashboard](https://platform.flatfile.com) → Developer Settings

For authentication guidance including JWT tokens and user management, see [Advanced Configuration](./advanced-configuration).

## Complete Example

<Note>
  The example below will open an empty space. To create the sheet your users
  should land on, you'll want to create a workbook as shown further down this
  page.
</Note>

```jsx  theme={null}
import React from "react";
import { FlatfileProvider, useFlatfile } from "@flatfile/react";

function ImportButton() {
  const { openPortal } = useFlatfile();

  const handleImport = () => {
    openPortal({});
  };

  return <button onClick={handleImport}>Import Data</button>;
}

function App() {
  return (
    <FlatfileProvider publishableKey="pk_your_publishable_key">
      <div>
        <h1>My Application</h1>
        <ImportButton />
      </div>
    </FlatfileProvider>
  );
}

export default App;
```

## Making API Requests

<Info>
  The `publishableKey` is designed exclusively for initializing `FlatfileProvider`. To make API requests, use the `accessToken` from the `useFlatfileInternal` hook.
</Info>

Use `useFlatfileInternal` to access the `accessToken` for making authenticated API calls:

```jsx  theme={null}
import { useEffect, useState } from "react";
import { useFlatfileInternal } from "@flatfile/react";
import { FlatfileClient } from "@flatfile/api";

function MyComponent() {
  const { accessToken, sessionSpace } = useFlatfileInternal();
  const [data, setData] = useState([]);

  useEffect(() => {
    // Wait for the space to be created and token to be available
    if (!accessToken || !sessionSpace?.id) return;

    // Initialize the API client with the accessToken
    const api = new FlatfileClient({ token: accessToken });

    const fetchData = async () => {
      try {
        const workbooks = await api.workbooks.list({ 
          spaceId: sessionSpace.id 
        });
        setData(workbooks.data);
      } catch (error) {
        console.error("API Error:", error);
      }
    };

    fetchData();
  }, [accessToken, sessionSpace?.id]);

  return <div>{data.length} workbooks found</div>;
}
```

For a complete guide on authentication and making API requests, see the [React Authentication Guide](/sdks/react/authentication).

## Configuration Options

For all configuration options including authentication, theming, and advanced settings, see [Advanced Configuration](./advanced-configuration).

## Using Space Component

For more control, you can use the `Space` component directly:

```jsx  theme={null}
import { FlatfileProvider, Space } from "@flatfile/react";

function App() {
  return (
    <FlatfileProvider
      publishableKey="pk_your_publishable_key"
      config={{ displayAsModal: true }}
    >
      <Space config={{ name: "Embedded Space" }} />
    </FlatfileProvider>
  );
}
```

## Creating New Spaces

To create a new Space each time:

1. Add a `workbook` configuration object. Read more about workbooks [here](../core-concepts/workbooks).
2. Optionally [deploy](../core-concepts/listeners) a `listener` for custom data processing. Your listener will contain your validations and transformations

```jsx  theme={null}
import { FlatfileProvider, Workbook } from "@flatfile/react";

const workbookConfig = {
  name: "My Import",
  sheets: [
    {
      name: "Contacts",
      slug: "contacts",
      fields: [
        { key: "name", type: "string", label: "Name" },
        { key: "email", type: "string", label: "Email" },
      ],
    },
  ],
};

function App() {
  return (
    <FlatfileProvider publishableKey="pk_your_publishable_key">
      <Workbook config={workbookConfig} />
    </FlatfileProvider>
  );
}
```

For detailed workbook configuration, see the [Workbook API Reference](https://reference.flatfile.com/api-reference/workbooks).

## Reusing Existing Spaces

For production applications, you should create Spaces on your server and pass the Space ID to your React application:

### Server-side (Node.js/Express)

```javascript  theme={null}
// Create Space on your server
const space = await api.spaces.create({
  name: "User Import",
  workbooks: [workbookConfig],
});

// Pass spaceId to your React app
res.json({ spaceId: space.data.id, token: space.data.accessToken });
```

### Client-side (React)

```jsx  theme={null}
import { FlatfileProvider, useFlatfile } from "@flatfile/react";

function ImportComponent() {
  const { openPortal } = useFlatfile();
  const [spaceId, setSpaceId] = useState(null);

  useEffect(() => {
    // Get Space ID from your server
    fetch("/api/create-space")
      .then((res) => res.json())
      .then((data) => setSpaceId(data.spaceId))
      .then((data) => setToken(data.token));
  }, []);

  <FlatfileProvider accessToken="token">
    <Space id="spaceId">
  </FlatfileProvider>

  const handleImport = () => {
    if (spaceId) {
      openPortal({});
    }
  };

  return <button onClick={handleImport}>Import Data</button>;
}
```

This approach allows you to:

* Create Spaces with server-side authentication
* Add custom event listeners and data processing
* Control Space lifecycle and cleanup

For complete server setup examples, see [Server Setup](/embedding/server-setup).

## TypeScript Support

The React SDK includes full TypeScript support:

```tsx  theme={null}
import { FlatfileProvider, useFlatfile } from "@flatfile/react";

interface Props {
  onDataImported?: (data: any) => void;
}

function ImportComponent({ onDataImported }: Props) {
  const { openPortal } = useFlatfile();

  const handleImport = (): void => {
    openPortal({});
  };

  return <button onClick={handleImport}>Import Data</button>;
}
```

## Next Steps

* **React Authentication**: [Complete guide to using accessToken for API requests](/sdks/react/authentication)
* **Advanced Configuration**: [Authentication, theming, and advanced options](./advanced-configuration)
* **Server Setup**: [Backend integration and event handling](./server-setup)
* **API Integration**: Use [Flatfile API](https://reference.flatfile.com) to retrieve processed data
* **Package Documentation**: See [@flatfile/react documentation](https://www.npmjs.com/package/@flatfile/react)

## Quick Links

<CardGroup cols={2}>
  <Card title="React Authentication" icon="key" href="/sdks/react/authentication">
    Using accessToken for secure API requests
  </Card>

  <Card title="Advanced Configuration" icon="gear" href="/embedding/advanced-configuration">
    Authentication, theming, and advanced options
  </Card>

  <Card title="Server Setup" icon="server" href="/embedding/server-setup">
    Backend integration and event handling
  </Card>
</CardGroup>

## Example Projects

<CardGroup cols={2}>
  <Card title="React Example" icon="react" href="https://github.com/FlatFilers/create-flatfile-react">
    Complete React application with Flatfile embedding
  </Card>
</CardGroup>
