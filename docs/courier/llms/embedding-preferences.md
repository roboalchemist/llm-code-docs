# Source: https://www.courier.com/docs/platform/preferences/embedding-preferences.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedding Preferences

> Integrate Courier's preference management components directly into your React or web application for seamless user notification control.

## Overview

Embed Courier's preference management directly into your application using React components, custom hooks, or web components. This approach provides seamless user experience where notification preferences feel native to your application, with complete control over styling, layout, and user workflow integration.

Embedded preferences maintain the full functionality of hosted preference centers while allowing deep customization to match your design system and user experience patterns.

<Tip>
  **Example Implementation**: View the complete [Newsletter Preferences example](https://github.com/trycourier/courier-guides/tree/main/preferences-center) to see embedded preferences in action.
</Tip>

## Key Features

Embedded preference components provide comprehensive preference management with complete customization control:

* **Seamless Integration** - Preferences feel native to your application without external redirects
* **Complete Customization** - Full control over styling, layout, and user experience design
* **Multi-Framework Support** - React components, custom hooks, and framework-agnostic web components
* **Real-Time Updates** - Immediate preference synchronization with Courier's preference system

## Core Components

### React Components

#### PreferencesV4 Component

Pre-built React component that renders a complete preference interface with subscription topics, channel selection, and real-time updates.

```tsx  theme={null}
import React from "react";
import { Footer, Header, PreferencesV4 } from "@trycourier/react-preferences";
import { CourierProvider } from "@trycourier/react-provider";

const PreferencePage: React.FunctionComponent<{
  tenantId?: string,
  draft?: boolean,
}> = ({ tenantId, draft = false }) => {
  return (
    <CourierProvider
      clientKey="your_client_key_here"
      userId="current_user_id"
    >
      <Header />
      <PreferencesV4 tenantId={tenantId} draft={draft} />
      <Footer />
    </CourierProvider>
  );
};
```

**Props:**

* `tenantId` (optional): Specify tenant for multi-tenant applications
* `draft` (optional): Show draft preferences before publishing

#### Custom React Hooks

Build completely custom preference interfaces using Courier's preference hooks for maximum flexibility:

```jsx  theme={null}
import React, { useEffect } from 'react';
import { usePreferences } from '@trycourier/react-hooks';

function CustomPreferenceInterface({ tenantId }) {
  const {
    recipientPreferences,
    preferencePage,
    fetchRecipientPreferences,
    fetchPreferencePage,
    updateRecipientPreferences,
    isLoading,
  } = usePreferences();

  useEffect(() => {
    fetchRecipientPreferences(tenantId);
    fetchPreferencePage(tenantId);
  }, [tenantId]);

  const handleToggle = (templateId, currentStatus) => {
    updateRecipientPreferences({
      templateId,
      status: currentStatus === "OPTED_IN" ? "OPTED_OUT" : "OPTED_IN",
      hasCustomRouting: false,
      digestSchedule: "",
      routingPreferences: [],
      tenantId,
    });
  };

  if (isLoading || !preferencePage) {
    return <div>Loading preferences...</div>;
  }

  return (
    <div>
      {recipientPreferences?.map((pref) => (
        <div key={pref.templateId}>
          <label>
            <input
              type="checkbox"
              checked={pref.status === "OPTED_IN"}
              onChange={() => handleToggle(pref.templateId, pref.status)}
            />
            {/* Get friendly name from preferencePage.sections */}
          </label>
        </div>
      ))}
    </div>
  );
}
```

**Hook Returns:**

* `recipientPreferences` - Array of user preference objects with templateId and status
* `preferencePage` - Preference page configuration with sections and topics
* `fetchRecipientPreferences(tenantId)` - Function to load user preferences
* `fetchPreferencePage(tenantId)` - Function to load preference page structure
* `updateRecipientPreferences(config)` - Function to update user preferences
* `isLoading` - Boolean indicating if any requests are in progress

<Note>
  The `usePreferences` hook uses Courier's **GraphQL** preference API (`recipientPreferences`, `preferencePage`, `updatePreferences`) under the hood, providing a React-friendly interface for preference management. For topic-based integrations or server-side workflows, use the [User Preferences API](/api-reference/user-preferences/get-users-preferences) (REST) instead.
</Note>

<Tip>
  **Explore Components**: Use this [interactive demo](https://bwebs.github.io/courier-test/window-preferences.html) to explore Courier's preference components and their capabilities.
</Tip>

### Web Components

For non-React applications, use Courier's web components that work with any JavaScript framework or vanilla HTML:

```html  theme={null}
<div id="preference-container">
  <courier-preference-page></courier-preference-page>
  
  <script type="text/javascript">
    window.courierConfig = {
      clientKey: 'your_client_key_here',
      userId: 'current_user_id'
    };
  </script>
  <script src="https://courier-components-xvdza5.s3.amazonaws.com/v3.6.4.js"></script>
</div>
```

### Implementation Comparison

| Approach           | Best For                           | Customization    | Development Effort |
| ------------------ | ---------------------------------- | ---------------- | ------------------ |
| **PreferencesV4**  | Quick integration, standard UI     | Styling only     | Minimal            |
| **Custom Hooks**   | Complex workflows, custom UX       | Complete control | High               |
| **Web Components** | Non-React apps, simple integration | CSS variables    | Low                |

## Getting Started

### Installation

```bash  theme={null}
yarn add @trycourier/react-hooks @trycourier/react-provider @trycourier/react-preferences styled-components
```

**Package Usage:**

* `@trycourier/react-preferences` - Pre-built PreferencesV4 component
* `@trycourier/react-hooks` - Custom hooks like usePreferences for building custom UIs
* `@trycourier/react-provider` - CourierProvider for authentication and context

<Warning>
  All @trycourier packages must use the same version for compatibility.
</Warning>

### Authentication Setup

Get your Client Key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in your Courier dashboard (it's in its own "Client Key" section, separate from the API Keys). Store it securely:

```bash  theme={null}
REACT_APP_COURIER_CLIENT_KEY=your_client_key_here
```

### Custom API URL

`CourierProvider` accepts an optional `apiUrl` prop. When set, the SDK uses this value as the **complete** GraphQL endpoint URL; it does **not** append `/client/q` automatically. This is primarily useful for proxying requests during local development to avoid CORS issues.

```tsx  theme={null}
// Local dev: proxy through Vite/Next.js/etc.
<CourierProvider clientKey="..." userId="..." apiUrl="/api/client/q" />

// Production: omit apiUrl to use the default (https://api.courier.com/client/q)
<CourierProvider clientKey="..." userId="..." />
```

See [How To Embed Preferences in React](/tutorials/preferences/how-to-embed-preferences-in-react#local-development-and-cors) for a full local development proxy example.

## User ID Requirements

<Note>
  **Critical**: The `userId` in your preference components must match the `to.user_id` used in send requests for preference enforcement to work correctly.
</Note>

Ensure consistent user identification across:

* Preference component initialization
* Send API requests
* User profile management
* Authentication systems

## Next Steps

<CardGroup cols={2}>
  <Card title="Preferences Editor" href="/platform/preferences/preferences-editor" icon="gear">
    Configure subscription topics and sections for your embedded components
  </Card>

  <Card title="Hosted Preference Center" href="/platform/preferences/hosted-page" icon="globe">
    Compare with turnkey hosted preference center solution
  </Card>

  <Card title="User Preferences API" href="/api-reference/user-preferences/get-users-preferences" icon="code">
    Programmatically manage user preferences and access custom routing data
  </Card>

  <Card title="React SDK v7 Documentation" href="/sdk-libraries/client-sdks/react-sdk" icon="react">
    Explore React v7 components for preferences (v8 React SDK does not include preferences components)
  </Card>
</CardGroup>
