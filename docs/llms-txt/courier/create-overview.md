# Source: https://www.courier.com/docs/platform/create/create-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Create Overview

> Effortlessly manage and customize multi-tenant email templates in React with Courier Create. Embed a powerful, branded editor, streamline workflows, and deliver personalized messaging at scale.

<Frame caption="Embeddable Designer Built for React Apps">
  <img src="https://mintcdn.com/courier-4f1f25dc/X4imlV9f_sunHT-I/platform/create/assets/create-overview.png?fit=max&auto=format&n=X4imlV9f_sunHT-I&q=85&s=39bddfcbfc663de20c2571ff8cb131ba" alt="Embeddable Designer" width="2060" height="1390" data-path="platform/create/assets/create-overview.png" />
</Frame>

Courier Create is a powerful template editing solution tailored for multi-tenant React applications. With built-in support for tenant-specific configurations and real-time editing capabilities, Courier Create helps streamline the design and deployment of email templates directly within your app's interface.

Embed Courier Create directly into your React application via the `@trycourier/react-designer` package. Courier Create's flexible theming options, and JWT-based authentication allow teams to maintain control over the editing workflow while ensuring security and consistency across multiple tenants. Users can personalize both templates and brand settings using a unified interface that supports advanced features like variable substitution, custom theming, auto-save toggling, and publishing hooks.

Whether you're launching new communications or updating tenant-specific branding, Courier Create offers the tools you need to efficiently manage content across clients without compromising on design flexibility or performance.

## Key Courier-Create Features

* **Embedded React Integration** - Easily embed the template and brand editors directly into your existing React application using the `@trycourier/react-designer` package.
* **Multi-Tenant Support** - Seamlessly manage templates and branding for multiple tenants, with individualized configurations and access controls.
* **Embedded Template Editor** - Create and edit dynamic, personalized templates using a drag-and-drop interface, with support for nested variables and live preview.
* **Brand Editor** - Modify tenant-specific branding elements such as logos, colors, and layout styles directly within your app.
* **[JWT Authentication](/platform/create/authentication)** - Secure access to editing tools via granular JWT scopes, supporting both full and tenant-specific permissions.
* **Email Channel Support** - Fully supports email template editing with future support planned for additional channels like SMS and push.
* **Channel Restriction** - Restrict which channels are visible in the editor using the `routing.channels` prop, perfect for email-only or channel-specific workflows.

## Next Steps

<CardGroup cols={2}>
  <Card title="Installation" href="/platform/create/installation" icon="download">
    Install the Create package
  </Card>

  <Card title="Authentication" href="/platform/create/authentication" icon="lock">
    Generate and scope JWTs
  </Card>

  <Card title="Provider Props" href="/platform/create/provider-props" icon="gear">
    Configure provider properties
  </Card>

  <Card title="Brand Editor" href="/platform/create/brand-designer" icon="palette">
    Customize tenant branding
  </Card>
</CardGroup>
