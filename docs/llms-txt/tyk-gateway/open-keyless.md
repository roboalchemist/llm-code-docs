# Source: https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/open-keyless.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Open (No Authentication)

> How to configure open or keyless authentication in Tyk.

Open or keyless authentication allows access to APIs without any authentication. This method is suitable for public APIs where access control is not required.

Tyk OAS APIs are inherently "open" unless authentication is configured, however the older Tyk Classic API applies [Auth Token](/api-management/authentication/bearer-token) protection by default.

You can disable authentication for a Tyk Classic API by setting the `use_keyless` flag in the API definition.

Built with [Mintlify](https://mintlify.com).
