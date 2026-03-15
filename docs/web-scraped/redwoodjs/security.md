# Source: https://docs.redwoodjs.com/docs/security

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Security]

[Version: 8.8]

On this page

<div>

# Security

</div>

RedwoodJS wants you to be able build and deploy secure applications and takes the topic of security seriously.

-   [RedwoodJS Security](https://github.com/redwoodjs/redwood/security) on GitHub
-   [CodeQL code scanning](https://github.com/features/security)
-   [Authentication](/docs/authentication)
-   [Webhook signature verification](/docs/webhooks)
-   [Ways to keep your serverless functions secure](/docs/serverless-functions#security-considerations)
-   [Environment variables for secure keys and tokens](/docs/environment-variables)

> ⚠️ **Security is Your Responsibility** While Redwood offers the tools, practices, and information to keep your application secure, it remains your responsibility to put these in place. Proper password, token, and key protection using disciplined communication, password management systems, and environment management services like [Doppler](https://www.doppler.com) are strongly encouraged.

> **Security Policy and Contact Information** The RedwoodJS Security Policy is located [in the codebase repository on GitHub](https://github.com/redwoodjs/redwood/security/policy).
>
> To report a potential security vulnerability, contact us at [security@redwoodjs.com](mailto:security@redwoodjs.com).

## Authentication[​](#authentication "Direct link to Authentication") 

`@redwoodjs/auth` is a lightweight wrapper around popular SPA authentication libraries. We currently support [the following authentication providers](/docs/authentication) as well as a self-hosted solution ([dbAuth](/docs/auth/dbauth)):

-   Netlify Identity Widget
-   Auth0
-   Azure Active Directory
-   Netlify GoTrue-JS
-   Magic Links - Magic.js
-   Firebase\'s GoogleAuthProvider
-   Ethereum
-   Supabase
-   Nhost

For example implementations, please see [Authentication](https://github.com/redwoodjs/redwood/tree/main/packages/auth) and the use of the `getCurrentUser` and `requireAuth` helpers.

For a demonstration, check out the [Auth Playground](https://redwood-playground-auth.netlify.app).

## GraphQL[​](#graphql "Direct link to GraphQL") 

GraphQL is a fundamental part of Redwood. For details on how Redwood uses GraphQL and handles important security considerations, please see the [GraphQL Security](/docs/graphql#security) section and the [Secure Services](/docs/services#secure-services) section.

### Malicious Document Requests[​](#malicious-document-requests "Direct link to Malicious Document Requests") 

The RedwoodJS GraphQL handler sets [reasonable defaults](/docs/graphql#security) to prevent abusive queries that attackers often use to exploit systems.

### Disable Introspection and Playground[​](#disable-introspection-and-playground "Direct link to Disable Introspection and Playground") 

Because both introspection and the playground share possibly sensitive information about your data model, your data, your queries and mutations, best practices for deploying a GraphQL Server call to [disable these in production](/docs/graphql#introspection-and-playground-disabled-in-production), by default RedwoodJS **only enables introspection and the playground when running in development**.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

For more information on how to enable introspection in production, please see the [GraphQL Docs](/docs/graphql#introspection-and-playground-disabled-in-production).

## Functions[​](#functions "Direct link to Functions") 

When deployed, a [serverless function](/docs/serverless-functions) is an open API endpoint. That means anyone can access it and perform any tasks it\'s asked to do. In many cases, this is completely appropriate and desired behavior. But there are often times you need to restrict access to a function, and Redwood can help you do that using a [variety of methods and approaches](/docs/serverless-functions#security-considerations).

For details on how to keep your functions secure, please see the [Serverless functions & Security considerations](/docs/serverless-functions#security-considerations) section in the RedwoodJS documentation.

## Webhooks[​](#webhooks "Direct link to Webhooks") 

[Webhooks](/docs/webhooks) are a common way that third-party services notify your RedwoodJS application when an event of interest happens.

They are a form of messaging or automation and allows web applications to communicate with each other and send real-time data from one application to another whenever a given event occurs.

Since each of these webhooks will call a function endpoint in your RedwoodJS api, you need to ensure that these run **only when they should**. That means you need to:

-   Verify it comes from the place you expect
-   Trust the party
-   Know the payload sent in the hook hasn\'t been tampered with
-   Ensure that the hook isn\'t reprocessed or replayed

For details on how to keep your incoming webhooks secure and how to sign your outgoing webhooks, please see [Webhooks](/docs/webhooks).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/security.md)