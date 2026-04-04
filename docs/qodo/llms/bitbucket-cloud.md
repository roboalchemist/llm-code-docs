# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/enterprise-self-hosted/3.-index-your-codebase/bitbucket-cloud.md

# Bitbucket Cloud

### **Limitations**

| **Capability**                   | **Status**        | **Notes**                                                                                                                                                                               |
| -------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Free/Standard tiers              | **Not supported** | workspace access tokens are only supported in Premium plan.                                                                                                                             |
| Choose individual repos to index | **Not supported** | Qodo Context Engine will index **all** repositories the token can see. If you need to limit scope, create a token tied to a workspace / user that has access only to the desired repos. |
| Webhooks / Marketplace app       | **N/A**           | Bitbucket Cloud integration is **token-only** – no webhooks or Atlassian Connect app is required.                                                                                       |

***

## **Generate an Access Token**

Qodo Context Engine accepts **either** a *Workspace Access Token* **or** a *Personal App Password*.

Both must have **read-only** scopes.

### **Workspace Access Token (Recommended)**

1. **Prerequisite** – you must be a *Workspace Administrator*.
2. In Bitbucket, open **Workspace settings ▸ Access management ▸ Access tokens**.
3. Click **Create access token**.
   * **Name** – something like “qodo-aware”.
   * **Permissions** – tick **Repositories: Read**, **Projects: Read**, **Pull requests: Read**.
4. Press **Create** and **copy the raw token immediately** – Bitbucket shows it only once.

### **Personal App Password (Alternative)**

1. Click your avatar ▸ **Personal settings ▸ App passwords**.
2. Press **Create app password** and give it a meaningful label.
3. Enable the same **read-only** scopes listed above, and add **Workspace: Read** permission (`read:workspace:bitbucket`).
4. Generate and copy the password (it will not be shown again).

## Send relevant information to Qodo

```
[bitbucket_cloud]
[bitbucket_cloud.tokens]
# Option A – workspace token
"my-workspace-name" = "XXXXXXXXXXXXXXXXXXXXXXXX"

# Option B – personal app-password
"user@example.com" = "YYYYYYYYYYYYYYYYYYYYYY"
```

**Placeholders**

| **Token type**  | **Key (left-hand-side)** | **Value (right-hand-side)**   |
| --------------- | ------------------------ | ----------------------------- |
| Workspace token | "\<WORKSPACE\_SLUG>"     | "\<WORKSPACE\_ACCESS\_TOKEN>" |
| App password    | "\<USER\_EMAIL>"         | "\<APP\_PASSWORD>"            |
