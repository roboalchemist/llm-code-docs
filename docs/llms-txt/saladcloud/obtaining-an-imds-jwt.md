# Source: https://docs.salad.com/container-engine/how-to-guides/imds/obtaining-an-imds-jwt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Obtaining an IMDS JWT

*Last Updated: May 10, 2025*

You can obtain a signed JWT (JSON Web Token) from the SaladCloud IMDS (Instance Metadata Service) that can be verified
with public keys provided by Salad. This offers a secure way to
[authenticate to external services](/container-engine/tutorials/security/jwt-authentication), such as your own API or a
third-party service.

You can find code samples and the full API reference in the [API Reference Docs](/reference/imds/get-token).

This JWT can also be used to authenticate with [S4](/storage/explanation/overview) for temporary file storage.
