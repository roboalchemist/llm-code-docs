# Source: https://console.groq.com/docs/model-permissions

---
description: Control which models are available at the organization and project level. Restrict API access to specific models using allow or block strategies.
title: Model Permissions - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Model Permissions

Limit which models can be used at the organization and project level. When a request attempts to use a restricted model, the API returns a 403 error.

## [How It Works](#how-it-works)

Configure model permissions using either **"Only Allow"** or **"Only Block"** strategies:

### [Only Allow](#only-allow)

When you only allow specific models, all other models are blocked.

**Example:** Only allow `llama-3.3-70b-versatile` and `llama-3.1-8b-instant` → all other models are blocked.

### [Only Block](#only-block)

When you only block specific models, all other models remain available.

**Example:** Only block `openai/gpt-oss-120b` → all other models remain available.

## [Organization and Project Level Permissions](#organization-and-project-level-permissions)

You can configure model permissions on either your organization, project, or both. These permissions cascade from the organization to the project, meaning that the project can only configure model permissions within the models which are allowed by the organization-level permissions.

### [Organization Level Permissions](#organization-level-permissions)

Members of the organization with the **Owner** role can configure model permissions at the organization level.

### [Project Level Permissions](#project-level-permissions)

Members of the organization with either the **Developer** or **Owner** role can configure model permissions at the project level.

### [Cascading Permissions](#cascading-permissions)

Permissions cascade from organization to project level. Organization settings always take precedence.

**How it works:**

1. **Organization Check First:** The system checks if the model is allowed at the org level  
   * If blocked at org level → request rejected  
   * If allowed at org level → proceed to project check
2. **Project Check Second:** The system checks if the model is allowed at the project level  
   * If blocked at project level → request rejected  
   * If allowed at project level → request proceeds

**Key point:** Projects can only work with models that are available after org-level filtering. They can only allow a subset of what the org allows, or block a subset of what the org allows. A model blocked at the org level cannot be enabled at the project level.

See the examples below for more details.

## [Configuring Model Permissions](#configuring-model-permissions)

### [At the Organization Level](#at-the-organization-level)

1. Go to [**Settings** → **Organization** → **Limits**](https://console.groq.com/settings/limits)
2. Choose **Only Allow** or **Only Block**
3. Select which models to allow or block
4. Click **Save**

### [At the Project Level](#at-the-project-level)

1. Select your project from the project selector
2. Go to [**Settings** → **Projects** → **Limits**](https://console.groq.com/settings/project/limits)
3. Choose **Only Allow** or **Only Block**
4. Select which models to allow or block  
   * **Only Allow:** Choose from models available after org-level filtering  
   * **Only Block:** Choose from models available after org-level filtering
5. Click **Save**

## [Error Responses](#error-responses)

Requests to restricted models return a 403 error with specific error codes depending on where the block occurred.

### [Organization-Level Block](#organizationlevel-block)

When a model is blocked at the organization level:

JSON

```
{
  "error": {
    "message": "The model `openai/gpt-oss-120b` is blocked at the organization level. Please have the org admin enable this model in the org settings at https://console.groq.com/settings/limits",
    "type": "permissions_error",
    "code": "model_permission_blocked_org"
  }
}
```

### [Project-Level Block](#projectlevel-block)

When a model is blocked at the project level:

JSON

```
{
  "error": {
    "message": "The model `openai/gpt-oss-120b` is blocked at the project level. Please have a project admin enable this model in the project settings at https://console.groq.com/settings/project/limits",
    "type": "permissions_error",
    "code": "model_permission_blocked_project"
  }
}
```

## [Common Use Cases](#common-use-cases)

* **Compliance:** Restrict models that don't meet your data handling requirements
* **Cost Control:** Limit access to higher-cost models for specific teams
* **Environment Isolation:** Different model access for dev, staging, and production
* **Team Access:** Give teams access to specific models based on their needs

## [Examples](#examples)

**Scenario 1: Org permissions only**

* **Org:** Only Allow `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `openai/gpt-oss-120b`
* **Project:** No restrictions

**Result:** Project can use `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `openai/gpt-oss-120b`; all other models are blocked by the organization.

  
**Scenario 2: Project permissions only**

* **Org:** No restrictions (all models available)
* **Project:** Only Block `openai/gpt-oss-120b`

**Result:** Project can use all models except `openai/gpt-oss-120b`.

  
**Scenario 3: Only Allow org → Only Allow subset on project**

* **Org:** Only Allow `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `openai/gpt-oss-120b`
* **Project:** Only Allow `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`

**Result:** Project can use `llama-3.3-70b-versatile` and `llama-3.1-8b-instant`, as the project permissions narrow it down. The organization allowed `openai/gpt-oss-120b` is blocked by the project. All other models are blocked by the organization.

  
**Scenario 4: Only Allow org → Block subset on project**

* **Org:** Only Allow `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `openai/gpt-oss-120b`
* **Project:** Only Block `openai/gpt-oss-120b`

**Result:** Project can use `llama-3.3-70b-versatile` and `llama-3.1-8b-instant`, as the project blocks `openai/gpt-oss-120b` from the organization's allowed set. All other models are blocked by the organization.

  
**Scenario 5: Only Block org → Only Allow subset on project**

* **Org:** Only Block `openai/gpt-oss-120b`, `openai/gpt-oss-20b`
* **Project:** Only Allow `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`

**Result:** Project can only use `llama-3.3-70b-versatile` and `llama-3.1-8b-instant`, as the project only allows a subset from the organization's allowed set. All other models are blocked by the project.

  
**Scenario 6: Only Block org → Block more on project**

* **Org:** Only Block `openai/gpt-oss-120b`
* **Project:** Only Block `llama-3.3-70b-versatile`

**Result:** Project blocked from using both `openai/gpt-oss-120b` and `llama-3.3-70b-versatile`. The project level permissions combine with the organization-level permissions to block both models. All other models are available.

## [FAQ](#faq)

### [Can I configure different permission strategies for different projects?](#can-i-configure-different-permission-strategies-for-different-projects)

Yes, each project can have its own "only allow" or "only block" strategy. However, all project permissions are limited by organization-level settings.

### [What happens if I block all models?](#what-happens-if-i-block-all-models)

All API requests will be rejected with a 403 `permissions_error`.

### [Can I temporarily disable model permissions?](#can-i-temporarily-disable-model-permissions)

Yes, you can modify or remove permission settings at any time. Changes take effect immediately.

### [Do model permissions affect existing API keys?](#do-model-permissions-affect-existing-api-keys)

Yes, permissions apply to all API requests regardless of which API key is used. Restrictions are based on the organization and project, not the API key.

### [Can a project enable a model that's blocked at the org level?](#can-a-project-enable-a-model-thats-blocked-at-the-org-level)

No, organization-level blocks always take precedence. Projects can only further restrict access, not expand it.

  
---

  
Need help? Contact our support team at **[\[email protected\]](/cdn-cgi/l/email-protection#22515752524d50566245504d530c414d4f)** or visit our [developer community](https://community.groq.com).