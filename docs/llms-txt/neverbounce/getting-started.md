# Source: https://developers.neverbounce.com/reference/getting-started.md

# Getting Started

The NeverBounce API is a RESTful service that communicates over HTTPS and returns responses in JSON format. This widely adopted structure ensures seamless compatibility with most programming languages and frameworks, making it easy to integrate into your application stack.

To simplify integration, we provide official SDKs for Node.js, Java, .NET, and Python. Our latest Node.js SDK (v5.0.0) has been fully rewritten in TypeScript and offers convenient, modern methods for interacting with the API. Key improvements in this version include:

* Requires Node.js 18 or higher
* Rewritten in TypeScript with full type definitions
* Migrated to ES Modules
* Utilizes the modern Fetch API
* Improved error handling with strict TypeScript types

Installation

Use the following command to install the SDK:

```c bash
npm install neverbounce --save
```

[npm](https://www.npmjs.com/package/neverbounce)

⚠️ Note: The Node.js SDK is designed for server-side use only and is not suitable for use in browser environments.

> 📘 Use in the browser
>
> The standard API is not suitable for use in client-side scripts (e.g. jQuery, Javascript). Using it on the client-side would require exposing sensitive API credentials; giving anyone access to your account. Instead please use our [Javascript Widget](/v4.0/docs/widget-getting-started).