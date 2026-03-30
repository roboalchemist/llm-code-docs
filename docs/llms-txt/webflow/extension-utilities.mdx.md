# Source: https://developers.webflow.com/designer/reference/extension-utilities.mdx

***

title: Extension utilities
slug: designer/reference/extension-utilities
description: >-
Essential utilities for managing your Designer Extension's interaction with
Webflow
hidden: false
'og:title': 'Webflow Designer API: Extension Utilities'
'og:description': >-
Configure your extension, access site information, respond to user events, and
more with the Designer API's utility functions.
-----------------------------------------------

The Designer API offers essential utilities to manage your extension's behavior and interaction with the Designer.

<CardGroup>
  <Card
    title="Site information"
    href="/designer/reference/get-site-info"
    icon={
        <>
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/LayoutDashboard.svg" alt="" className="hidden dark:block" />
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/LayoutDashboard.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Access site details and configure how your extension appears in the Designer
  </Card>

  <Card
    title="User events"
    href="/designer/reference/events"
    icon={
        <>
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Interactions.svg" alt="" className="hidden dark:block" />
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Interactions.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Subscribe to Designer events to create responsive extensions
  </Card>

  <Card
    title="App discovery"
    href="/designer/reference/app-intents-and-connections"
    icon={
        <>
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Export.svg" alt="" className="hidden dark:block" />
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Export.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Make your extension discoverable in element settings
  </Card>

  <Card
    title="User authentication"
    href="/designer/reference/get-user-id-token"
    icon={
        <>
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Encryption.svg" alt="" className="hidden dark:block" />
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Encryption.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Authenticate users with the Data API, and access Data API resources
  </Card>
</CardGroup>

## Best practices

<CardGroup cols={1}>
  <Card title="Dynamic updates">
    [Subscribe to relevant events](/designer/reference/events) like when a user selects a new element to keep your extension in sync with the Designer state.
  </Card>

  <Card title="Appropriate sizing">
    [Size your extension appropriately](/designer/reference/resize-extension) with `resizeExtension()`. Too large and it dominates the UI; too small and it's hard to use.
  </Card>
</CardGroup>

<Callout type="success">
  For a comprehensive guide to building effective extensions, check out our [Quick Start Guide](/designer/docs/getting-started-designer-extensions) and [App Setup](/designer/reference/app-structure) documentation.
</Callout>
