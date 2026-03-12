# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/enterprise-self-hosted/3.-index-your-codebase/gerrit.md

# Gerrit

### Limitations

<table data-header-hidden><thead><tr><th>Capability</th><th width="206.15625">Status</th><th>Notes</th></tr></thead><tbody><tr><td>Choose individual repos to index</td><td><strong>Not supported</strong></td><td><p>Qodo Context Engine indexes <strong>all</strong> repositories visible to the token.</p><p>If you need to limit the scope, use a service account with restricted access.</p></td></tr><tr><td>Webhooks / Plugins</td><td><strong>N/A</strong></td><td>Integration is token‑only; no additional plugins are required.</td></tr></tbody></table>

***

## 1. Generate an Access Token

Gerrit uses an HTTPS username and password for API and Git access.

#### **Prerequisites**

User must have `Read` access to the relevant repositories, on top of the ability to just view them.

To make sure you have `Read` access:

1. Go to **Repositories** ▸ **All-Projects** ▸ **Access** (**All-Projects** is an example, can be a specific project or a parent project that others inherit)
2. Search for `Reference: refs/heads/*`
3. Make sure the correct user's group has `Read`: `ALLOWED`.

### **Generate HTTP Access Token**

1. Sign in to Gerrit and open **Settings ▸ HTTP Credentials**.
2. Click **Generate New Password**.
3. **Copy the generated password** – Gerrit shows it only once.
4. **Note your Gerrit username**. It will be required alongside the password.

***

## 2. Send relevant information to Qodo

```toml
[gerrit]
base_url = "<https://gerrit.example.com>"
username = "<GERRIT_USERNAME>"
token = "<HTTP_PASSWORD>"

```

**Placeholders**

| Field               | Description                                            |
| ------------------- | ------------------------------------------------------ |
| `<GERRIT_USERNAME>` | Gerrit account name used to generate the HTTP password |
| `<HTTP_PASSWORD>`   | The generated password/token from **HTTP Credentials** |
| `base_url`          | Base URL of your Gerrit server                         |

> Notes
>
> * Currently, only one Gerrit token is supported per deployment.
> * Ensure the account has read‑only access to the repositories you want indexed.

***

## 3. (Optional) Set a custom certificate bundle

> If your self-hosted Git server uses a custom CA SSL certificate, share your ca-certificate.pem file with the Qodo team.
