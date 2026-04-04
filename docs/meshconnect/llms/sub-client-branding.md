# Source: https://docs.meshconnect.com/advanced/sub-client-branding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Sub-Clients

## **What are Sub-Clients?**

If your product is used directly by end-users, this section is likely not relevant to you. However, if your product is embedded within other platforms (e.g., you are a Payment Service Provider powering payments for multiple retailers), then Sub-Clients are critical.

A **Sub-Client** represents the specific merchant or platform where your product is embedded. Registering them allows you to:

* **Ensure Consistent Branding:** Display the specific retailer's name and logo in the Mesh Link modal, creating a seamless experience for the end-user.
* **Maintain Compliance:** Mesh requires visibility into the legal entity associated with each transaction for compliance purposes.

### **How to Register a Sub-Client**

You can register and manage sub-clients in two ways: via the Mesh Dashboard or programmatically via the Account Management API.

### **Option 1: Via the Mesh Dashboard**

1. Notify your Mesh representative to enable this functionality for your account.
2. Navigate to **Account** > **Link Configuration** > **Clients** tab.
3. Click **"Add a client"**.
4. Enter the Business Legal Name, Display Name, Callback URL(s), and upload the relevant icon.
5. Click **Save**.

### **Option 2: Via the Account Management API**

For high-volume or automated setups, you can use our **Account Management API** to create, update, and delete sub-clients programmatically.

To use this API, you must first generate a dedicated API key and configure security settings.

1. **Generate an API Key:**
   * Go to **Account** > **API Keys**.
   * In the new **Account Management API Keys** section, click to generate a new key.
   * Use this key to authenticate your requests to the `https://admin-api.meshconnect.com` endpoints.
2. **Configure IP Whitelisting (Security Requirement):**
   * To enhance security, access to the Account Management API is restricted to pre-approved IP addresses.
   * Go to the **Account Management API Whitelisted IPs** section in your dashboard.
   * Add the specific IP address ranges from which your servers will make API calls.
   * **Note:** Initially, you can configure these IPs without enforcement. Once your configuration is tested and ready, we will enable the filtering to strictly enforce these rules.

### **Using a Sub-Client in a Transaction**

Once a sub-client is registered (via Dashboard or API), you will receive a unique `subClientId`.

To apply the sub-client's branding and settings to a transaction, simply pass this ID in your `linkToken` request:

JSON

`{
  "subClientId": "your_sub_client_id_here",
  "transferOptions": { ... }
}`

This ensures the Link modal automatically renders with the correct branding for that specific merchant. You can test this flow in our interactive demos by selecting a registered client from the "Sub-client" dropdown.
