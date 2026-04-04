# API Tokens

API tokens allow users to authenticate REST and GraphQL API queries (see [APIs introduction](/cms/api/content-api)).

:::caution Security
Prefer read‑only tokens for public access, scope server tokens to only what you need, rotate long‑lived tokens, and store them in a secrets manager. Never expose admin tokens in client‑side code.
:::

</IdentityCard>

</Tabs>

This key is used to encrypt and decrypt token values. Without this key, tokens remain usable, but will not be viewable after initial display. New Strapi projects will have this key automatically generated.

## Usage

Using API tokens allows executing a request on [REST API](/cms/api/rest) or [GraphQL API](/cms/api/graphql) endpoints as an authenticated user.

API tokens can be helpful to give access to people or applications without managing a user account or changing anything in the Users & Permissions plugin.

When performing a request to Strapi's REST API, the API token should be added to the request's `Authorization` header with the following syntax: `bearer your-api-token`.

:::note
Read-only API tokens can only access the `find` and `findOne` functions.
:::