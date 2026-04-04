# Source: https://documentation.onesignal.com/docs/en/keys-and-ids.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keys & IDs

> Find and manage your OneSignal App ID, Organization ID, and API keys. Learn how to create, rotate, secure, and migrate keys safely.

Your OneSignal account includes **public IDs** and **private API keys**.

* Use **IDs** (like App ID) to configure SDKs and reference apps.
* Use **API keys** to authenticate secure REST API requests.

This guide explains what each key does, where to find it, and how to manage it securely.

***

## App ID

The **App ID** is a public UUID (v4) that identifies your OneSignal app.

You use it for:

* Initializing the SDK (Mobile SDK setup, Web SDK setup)
* Making API requests such as Create message and Create user

Find your App ID in the dashboard under **Settings > Keys & IDs** or via the [View apps](/reference/view-apps) API.

<Frame caption="OneSignal dashboard: Navigate to your Settings > Keys & IDs">
  <img src="https://mintcdn.com/onesignal/W0DIQbUDatcgdZf6/images/dashboard/dashboard-keys-and-ids-app-id.jpg?fit=max&auto=format&n=W0DIQbUDatcgdZf6&q=85&s=6a39364c8ca631b3a0623e704fedc8af" alt="OneSignal dashboard Keys & IDs page showing App ID location." width="2722" height="1330" data-path="images/dashboard/dashboard-keys-and-ids-app-id.jpg" />
</Frame>

<br />

<Frame caption="App ID location in the OneSignal dashboard.">
  <img src="https://mintcdn.com/onesignal/W0DIQbUDatcgdZf6/images/dashboard/dashboard-keys-and-ids-app-id-number.jpg?fit=max&auto=format&n=W0DIQbUDatcgdZf6&q=85&s=07fa6040dbc41ffa7dff116a0b1ad575" width="1375" height="528" data-path="images/dashboard/dashboard-keys-and-ids-app-id-number.jpg" />
</Frame>

<Check>
  Your App ID is safe to use in client-side SDK initialization. It is not a secret.
</Check>

***

## Organization ID

The **Organization ID (Org ID)** is a UUID (v4) that groups all apps under your billing plan.

You need it for Organization-level APIs such as:

* [Create an app](/reference/create-an-app)
* [Update an app](/reference/update-an-app)

Find it in **Organizations > Your Organization > Keys & IDs** or via the [View an app](/reference/view-an-app) API.

<Frame caption="Organization ID location in the OneSignal dashboard.">
  <img src="https://mintcdn.com/onesignal/MWGmj5X1CnFliD-c/images/dashboard/dashboard-keys-and-ids-organization-id.png?fit=max&auto=format&n=MWGmj5X1CnFliD-c&q=85&s=b28d6312569975a67ca3eb1be9f568e4" alt="OneSignal dashboard showing Organization ID under Keys & IDs." width="2560" height="1228" data-path="images/dashboard/dashboard-keys-and-ids-organization-id.png" />
</Frame>

***

## API keys overview

OneSignal supports two types of API keys:

| Key Type                 | Scope               | Used For                                                  |
| ------------------------ | ------------------- | --------------------------------------------------------- |
| **App API Key**          | Single app          | Sending messages, creating users, app-level operations    |
| **Organization API Key** | Entire organization | Creating apps, managing API keys, org-level configuration |

You can create up to 16 API keys and configure IP allowlisting.

<Warning>
  Both are **private secrets** and must be stored securely.
</Warning>

### App API key

Use an **App API Key** for most REST API requests related to a specific app.

**Authentication format:**

Include the key in the `Authorization` header with the `key` authentication scheme:

```http  theme={null}
Authorization: key YOUR_REST_API_KEY
```

You can create App API Keys in **App Settings > Keys & IDs** or via the [Create API key](/reference/create-api-key) API.

<Warning>
  Treat App API Keys like passwords.

* Never expose them in mobile or web client code.
* Never commit them to public repositories (like GitHub).
* Store them in a secure backend or secret manager.
</Warning>

### Organization API key

Use an **Organization API Key** for:

* **App management**: [Creating apps](/reference/create-an-app), [Viewing apps](/reference/view-apps)
* **App API key management**: [Create API key](/reference/create-api-key), [Delete API key](/reference/delete-api-key), [Rotate API key](/reference/rotate-api-key)

Create within OneSignal dashboard in **Organizations > Your Organization > Keys & IDs**

<Frame caption="The Organization API key replaces the legacy User Auth key.">
  <img src="https://mintcdn.com/onesignal/W0DIQbUDatcgdZf6/images/dashboard/default-org-api-keys-and-ids.jpg?fit=max&auto=format&n=W0DIQbUDatcgdZf6&q=85&s=d014d99705d175a153d43444b42adca3" width="1846" height="840" data-path="images/dashboard/default-org-api-keys-and-ids.jpg" />
</Frame>

As with app API keys, you can configure up to 16 org keys and include IP allowlisting configuration.

***

## Create API keys

You can create both App and Organization API keys from the dashboard.

* App API keys can also be created via the [Create API key](/reference/create-api-key) API.
* Organization API keys can only be created via dashboard.

**Create a key:**

1. Go to Keys & IDs (App or Organization level).
2. Click **Add Key**.

<Frame caption="API keys are displayed only once after creation.">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9f590d021be57131df946faf1aafe9179706717305dc8b8e6cd28657f2ce73e1-Screenshot_2024-12-02_at_2.41.45_PM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=30c7f657c663c040a916958357d46922" alt="Modal for creating a new API key in OneSignal dashboard." width="1464" height="630" data-path="images/docs/9f590d021be57131df946faf1aafe9179706717305dc8b8e6cd28657f2ce73e1-Screenshot_2024-12-02_at_2.41.45_PM.png" />
</Frame>

1. Enter a descriptive name (example: CRM Sync Service).
2. (Optional) Configure IP allowlisting.
3. Click **Create**.
4. Copy and securely store the key immediately.

<Frame caption="Generated API key (displayed only once).">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/beea445a650b5e0c671e04a8f6b6325e3ac5b07a57c740eb48a0a93fa67317f9-Screenshot_2024-12-02_at_2.48.30_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=bad020bd251f37bdd05c77ac061c7ea1" width="764" height="768" data-path="images/docs/beea445a650b5e0c671e04a8f6b6325e3ac5b07a57c740eb48a0a93fa67317f9-Screenshot_2024-12-02_at_2.48.30_PM.png" />
</Frame>

<Warning> API keys are shown only once. If you lose the key, you must rotate it. </Warning>

### IP allowlist (optional but recommended)

You can restrict API key usage to specific IP addresses.

* Enter space-separated CIDR blocks
  * Example: `192.0.2.0/24 192.0.2.123/32`
* Requests from non-allowed IPs will be denied.

Use IP allowlisting for:

* Backend services with static IPs
* High-security production environments

<Frame caption="Creating an API key with IP allowlisting enabled.">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1ef65bb43edf88887e66e3d4b3656041f2657a8147b5088406f932ba027996bc-Screenshot_2024-12-02_at_2.43.20_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=d2687921db6608a2a2e8c4ff52ce89c3" alt="IP allowlist configuration field in API key creation modal." width="764" height="542" data-path="images/docs/1ef65bb43edf88887e66e3d4b3656041f2657a8147b5088406f932ba027996bc-Screenshot_2024-12-02_at_2.43.20_PM.png" />
</Frame>

***

## Key management

After creating a key, you can manage it via the key list interface:

<Frame caption="Key list showing key name and Key ID (not the secret).">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d2d9589a34c75894ace59a5796d7b4d118147916ddc409726af35c18d3b7fd9e-Screenshot_2024-12-09_at_3.04.53_PM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=f3464df2b7d063bb81eca2d5a7f21040" alt="API key list in OneSignal dashboard showing key names and IDs." width="1992" height="902" data-path="images/docs/d2d9589a34c75894ace59a5796d7b4d118147916ddc409726af35c18d3b7fd9e-Screenshot_2024-12-09_at_3.04.53_PM.png" />
</Frame>

<Info> The **Key ID** is a label for reference. It is not the secret API key. </Info>

### Edit API keys

You can:

* Update the key name
* Modify IP allowlist settings

Editing does not change the secret value. No integration changes are required.

* App API keys can be updated via dashboard or the [Update API key](/reference/update-api-key) API.
* Organization API keys can only be updated via dashboard.

### Rotate API keys

Rotating a key:

* Generates a new secret
* Keeps the same name and configuration
* Immediately invalidates the old secret

**When to rotate:**

* The key was exposed
* A team member with access leaves
* Routine security rotation

<Warning> After rotating a key, update all services using it. Requests with the old key will fail. </Warning>

* App API keys can be rotated via dashboard or the [Rotate API key](/reference/rotate-api-key) API.
* Organization API keys can only be rotated via dashboard.

### Delete API keys

Deleting a key:

* Permanently removes it
* Immediately blocks API access using that key

Use deletion when a key is no longer needed.

* App API keys can be deleted via dashboard or the [Delete API key](/reference/delete-api-key) API.
* Organization API keys can only be deleted via dashboard.

***

## Migrating from legacy API keys

We introduced rich API key management on November 14, 2024.

**Migration Steps**

1. Create a new App or Organization API key.
2. Replace the legacy key in your code.
3. Update your API base URL to:

```http  theme={null}
https://api.onesignal.com
```

Instead of:

```http  theme={null}
https://onesignal.com/api/v1/
```

1. Disable or delete the legacy key in Keys & IDs.

<Check> Test API requests in a staging environment before disabling your legacy key in production. </Check>

***

## Disabling your app

**Block API access:**

* Delete or rotate API keys to immediately block REST API usage.

**Disable message sending:**

* Go to **Settings > Manage App > Disable App**.

See [Disabled Apps & Organizations](./disabled-apps) for details.

<Warning>
  Disabling an app does not stop billing. Monthly Active Users (MAU) for disabled apps still count toward billing.

  To stop billing, delete the app or move it to a Free Organization.

  Contact `support@onesignal.com` for assistance.
</Warning>

***

## Security best practices

* Store API keys in a secure backend (never client-side).
* Use environment variables or a secrets manager.
* Enable IP allowlisting when possible.
* Rotate keys periodically.
* Use separate keys for staging and production.

***

## Frequently asked questions

### How do I find my API key?

Go to **Dashboard > App > Settings > Keys & IDs**.

Copy the **REST API Key** (app-level) or **Organization API Key** (account-level).

***

### Can I retrieve a legacy REST API key?

No. OneSignal does not display previously generated legacy REST API keys.

If you cannot find it in your codebase, generate a new **Rich API key** and update your integration.

***

### What is the difference between an App ID, REST API key, and Organization API key?

* **App ID**: A public identifier for your app. Used in SDK setup and API requests to specify the app.
* **REST API Key**: A secret key used to send messages and manage users for one app.
* **Organization API Key**: A secret key used to manage apps and organization-level settings across your entire account.

***

Built with [Mintlify](https://mintlify.com).
