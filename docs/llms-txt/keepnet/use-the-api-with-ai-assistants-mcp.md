# Source: https://doc.keepnetlabs.com/api-reference/use-the-api-with-ai-assistants-mcp.md

# Use the API with AI assistants (MCP)

Keepnet’s API documentation is available via **MCP (Model Context Protocol)** so you can use it inside AI-powered tools (Cursor, Codex, Claude, ChatGPT, or any client that supports MCP). Once connected, you can ask in plain language for things like *“List all companies I have”* or *“List training enrollments for customer Acme LLC”* and the assistant will use the API docs and endpoints to guide you or perform the calls (if the tool supports it).

This page describes the MCP URL, how to get started, example prompts, and best practices for security and clarity.

***

## MCP documentation URL

**URL:** `https://doc.keepnetlabs.com/~gitbook/mcp`

Use this URL as the **MCP server / documentation source** in your AI tool. The exact way to add it depends on the product:

* **Cursor** — MCP or Docs: add the URL as a remote/docs source so the assistant can read the API reference.
* **Claude / ChatGPT / Codex** — If the product supports “add documentation URL” or “connect knowledge base”, paste this URL. Otherwise, you may need to use a browser or plugin that loads the doc site and passes context to the model.

The MCP endpoint serves the same content as the rest of the Keepnet API docs (Quickstart, Reseller use-cases, endpoints, auth). The assistant uses it to answer questions about endpoints, request shapes, and step-by-step flows.

***

## Getting started: “I want to connect Keepnet’s APIs, lead me!”

A good first prompt is: **“Hey, I want to connect Keepnet’s APIs, lead me!”**

The assistant should then guide you through:

1. **Credentials** — You need a **Client ID** and **Client Secret** from the Keepnet platform (**Company → Company Settings → REST API**). Generate a new credential set and copy both values once (the secret is shown only once).
2. **Where to store them** — Prefer **environment variables** or the tool’s **secure storage** (e.g. Cursor’s env, Claude’s secure credentials). Do **not** paste the Client Secret into chat or into code that you commit.
3. **Getting a token** — The API uses **OAuth 2.0 Client Credentials**. The assistant should point you to `POST https://api.keepnetlabs.com/connect/token` with `grant_type=client_credentials`, `client_id`, `client_secret`, and `scope=api1`. You can do this once manually (e.g. with curl or Postman) or use a small script; the assistant can generate the script from the docs.
4. **Using the token** — Use the returned `access_token` as `Authorization: Bearer <token>` in all API requests. The assistant can then help you call the right endpoints for your next requests.

If the AI tool can execute requests (e.g. via MCP tools or a code runner), it may offer to run the token request for you **only if** credentials are provided via env vars or secure input — never ask the user to paste the secret into the chat.

***

## Example prompts after you have a token

Once credentials are set and you have (or can obtain) an access token, you can ask in natural language. The assistant will map your question to the API and, if the tool allows, to the right use-case or endpoint.

### List all companies I have on the platform

**Example prompt:** *“List all companies I have on the platform please.”*

**Maps to:** Reseller use-case **List companies with license details**.\
**Endpoint:** `POST /api/companies/search` with body e.g. `pageNumber: 1`, `pageSize: 10`, `orderBy: "CreateTime"`.\
**Note:** For **Reseller** credentials this returns all companies you manage. For **Company Admin** you typically use `GET /api/companies/my` for your single company.

***

### List training enrollments for a customer (e.g. Acme LLC)

**Example prompt:** *“Please list training enrollment for customer Acme LLC.”*

**Maps to:** Reseller use-case **View customer's enrollment list and report**.\
**Flow:**

1. Get the customer’s Company ID: `POST /api/companies/search` → find the company by name (e.g. “Acme LLC”) and take its `resourceId`.
2. List enrollments for that customer: `POST /api/enrollments/search` with header `X-KEEPNET-Company-Id: <companyResourceId>` and body e.g. `{ "filter": {}, "pageNumber": 1, "pageSize": 20 }`.

The assistant can describe this flow and, if the tool supports it, show or run the requests.

***

### Create a system user on my customer profile

**Example prompt:** *“Help me to create a system user on my customer profile.”*\
Or: *“Create a system user for customer Acme LLC.”*

**Maps to:** Reseller use-case **Add system user for a customer**.\
**Flow:**

1. Get the customer’s Company ID: `POST /api/companies/search` → pick the company and note `resourceId`.
2. Create the system user: `POST /api/system-users` with header `X-KEEPNET-Company-Id: <companyResourceId>` and body with `email`, `firstName`, `lastName`, `phoneNumber` (required), and optional `roleResourceIdList`, `statusId`.

The assistant should remind you to use **dummy or test data** (e.g. `user@example.com`) in examples and to never paste real secrets in chat.

***

### Set up SCIM for my customers

**Example prompt:** *“I want to setup SCIM for my customers.”*\
Or: *“Create a SCIM integration for customer Acme LLC.”*

**Maps to:** Reseller use-case **Set up SCIM for a customer**.\
**Flow:**

1. Get the customer’s Company ID: `POST /api/companies/search` → pick the company and note `resourceId`.
2. Create the SCIM integration: `POST /api/scim` with header `X-KEEPNET-Company-Id: <companyResourceId>` and body at least `name` (e.g. `"Entra ID Sync"`), and optionally `groupResourceId`, `groupBySCIMFieldResourceId`, `fieldMappings`, `syncPlatformGroup`.
3. Share the returned **SCIM token** and endpoint URL with the customer so they can configure their IdP (Entra ID, Okta, etc.). The assistant can point to the platform’s SCIM setup guides for the IdP side.

***

### More examples

| You say                                          | Use-case / intent                                                                                                                  |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| “Export my company list for billing.”            | **Export customer list for billing** — `POST /api/companies/search/export`                                                         |
| “List target users for customer X.”              | **List or export target users for a customer** — `POST /api/target-users/search` with `X-KEEPNET-Company-Id`                       |
| “Add target users to customer Acme.”             | **Add target users for a customer** — `POST /api/target-users` with header + body                                                  |
| “Show me phishing campaign list for customer Y.” | **View customer's campaign list and report** — `POST /api/phishing-simulator/phishing-campaign/search` with `X-KEEPNET-Company-Id` |
| “Create a new company.”                          | **Create a company** — `POST /api/companies` (multipart/form-data)                                                                 |

The assistant uses the MCP documentation to resolve the correct endpoint, method, headers, and body shape.

***

## Best practices

* **Never paste Client Secret (or access token) into chat.** Use environment variables or the tool’s secure credential storage. The assistant should remind users of this when guiding “connect Keepnet’s APIs”.
* **Reseller vs Company Admin** — If you are a **Reseller**, many list/report actions require **Company ID** (`X-KEEPNET-Company-Id`) to scope to one customer. The assistant should ask which customer (by name or ID) when the request is customer-specific, then resolve Company ID from `POST /api/companies/search` if needed.
* **Token expiry** — Tokens expire (e.g. after 1 hour). If the tool gets `401 Unauthorized`, the assistant should suggest requesting a new token via `POST /connect/token`.
* **Use dummy data in examples** — When the assistant generates sample bodies (emails, names, company names), it should use placeholders (e.g. `user@example.com`, “Acme LLC”, `xC5kfGz7w2Nz`) so users don’t accidentally use production data or PII in chat or in code they share.
* **Link back to the docs** — For complex flows (e.g. SCIM, company groups), the assistant can point to the full use-case page in the API reference (e.g. **Set up SCIM for a customer**, **List and manage company groups**) so users can read the full steps and error handling.

***

## Where this fits in the docs

* **Placement:** Under **API REFERENCE**, e.g. right after **Quickstart** or as a separate top-level entry like **Use the API with AI assistants (MCP)**.
* **Audience:** Developers and admins who use Cursor, Codex, Claude, ChatGPT, or other MCP-capable tools and want to use natural language to discover and call Keepnet’s API.
* **Cross-links:** Link from this page to **Quickstart** (auth, token) and to the Reseller use-cases (list companies, enrollment list, system user, SCIM, etc.). From Quickstart, add a short line: “Use the API from AI assistants (MCP): [Use the API with AI assistants (MCP) →](https://doc.keepnetlabs.com/api-reference/use-the-api-with-ai-assistants-mcp).”

***
