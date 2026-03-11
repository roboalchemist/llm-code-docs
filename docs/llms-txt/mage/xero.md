# Source: https://docs.mage.ai/data-integrations/sources/xero.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Xero

> Sync accounting data from Xero including invoices, contacts, payments, and more. Supports incremental syncing with automatic OAuth token refresh.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="data-integration" />

## Configuration

To set up the Xero source, provide the following configuration parameters:

| Key                         | Description                                                                        | Sample Value           | Required |
| --------------------------- | ---------------------------------------------------------------------------------- | ---------------------- | -------- |
| `client_id`                 | Client ID issued when you create your Xero app.                                    | `abcdefg`              | ✅        |
| `client_secret`             | Client secret generated when you create your Xero app.                             | `abcdefg`              | ✅        |
| `tenant_id`                 | Tenant ID associated with your Xero organization.                                  | `abcdefg`              | ✅        |
| `start_date`                | The start date for syncing data. Format: `YYYY-MM-DDTHH:MM:SSZ`.                   | `2021-01-01T00:00:00Z` | ✅        |
| `refresh_token`             | OAuth refresh token (required if `refresh_token_secret_name` is not provided).     | `abcdefg`              | ⚠️       |
| `refresh_token_secret_name` | Name of the Mage secret containing the refresh token (recommended for production). | `XERO_REFRESH_TOKEN`   | ⚠️       |

<Note>
  You must provide either `refresh_token` or `refresh_token_secret_name`. Using `refresh_token_secret_name` is recommended because Xero uses rotating refresh tokens (each token can only be used once), and this option automatically persists the new token after each refresh.
</Note>

### Option 1: Direct Refresh Token

```yaml  theme={"system"}
client_id: YOUR_CLIENT_ID
client_secret: YOUR_CLIENT_SECRET
tenant_id: YOUR_TENANT_ID
start_date: "2021-01-01T00:00:00Z"
refresh_token: YOUR_REFRESH_TOKEN
```

<Warning>
  Xero refresh tokens are single-use. Each time the token is refreshed, a new one is issued and the old one is invalidated. With this option, the new token is only stored in memory during the sync, so subsequent pipeline runs may fail if the token has been rotated.
</Warning>

### Option 2: Mage Secret (Recommended)

```yaml  theme={"system"}
client_id: YOUR_CLIENT_ID
client_secret: YOUR_CLIENT_SECRET
tenant_id: YOUR_TENANT_ID
start_date: "2021-01-01T00:00:00Z"
refresh_token_secret_name: XERO_REFRESH_TOKEN
```

First, create a secret in Mage. You can choose any name for your secret:

1. Open a pipeline edit page
2. Expand the right side panel
3. Click the **"Secrets"** tab
4. Click **"Add new secret"**
5. Enter your chosen secret name (e.g., `XERO_REFRESH_TOKEN`) and your initial refresh token as the value
6. Copy the secret name to your Xero config's `refresh_token_secret_name` field

<Check>
  The tap will automatically update the secret with the new refresh token after each sync, ensuring reliable long-term operation.
</Check>

## Supported Streams

The Xero source supports the following streams:

### Incremental Streams

These streams support incremental syncing based on the `start_date` configuration and bookmark state:

| Stream                | Primary Key         | Replication Key |
| --------------------- | ------------------- | --------------- |
| `accounts`            | AccountID           | UpdatedDateUTC  |
| `bank_transactions`   | BankTransactionID   | UpdatedDateUTC  |
| `bank_transfers`      | BankTransferID      | CreatedDateUTC  |
| `contacts`            | ContactID           | UpdatedDateUTC  |
| `credit_notes`        | CreditNoteID        | UpdatedDateUTC  |
| `employees`           | EmployeeID          | UpdatedDateUTC  |
| `expense_claims`      | ExpenseClaimID      | UpdatedDateUTC  |
| `invoices`            | InvoiceID           | UpdatedDateUTC  |
| `items`               | ItemID              | UpdatedDateUTC  |
| `journals`            | JournalID           | JournalNumber   |
| `linked_transactions` | LinkedTransactionID | UpdatedDateUTC  |
| `manual_journals`     | ManualJournalID     | UpdatedDateUTC  |
| `overpayments`        | OverpaymentID       | UpdatedDateUTC  |
| `payments`            | PaymentID           | UpdatedDateUTC  |
| `prepayments`         | PrepaymentID        | UpdatedDateUTC  |
| `purchase_orders`     | PurchaseOrderID     | UpdatedDateUTC  |
| `quotes`              | QuoteID             | UpdatedDateUTC  |
| `receipts`            | ReceiptID           | UpdatedDateUTC  |
| `users`               | UserID              | UpdatedDateUTC  |

### Full Table Streams

These streams are fully synced on each run (no incremental support):

| Stream                | Primary Key        |
| --------------------- | ------------------ |
| `branding_themes`     | BrandingThemeID    |
| `contact_groups`      | ContactGroupID     |
| `currencies`          | Code               |
| `organisations`       | OrganisationID     |
| `repeating_invoices`  | RepeatingInvoiceID |
| `tax_rates`           | TaxType            |
| `tracking_categories` | TrackingCategoryID |

## How to Generate Credentials

To use this source, you need to create a Xero OAuth app and complete the OAuth flow.

### 1. Create a Xero App

Go to the [Xero Developer Portal](https://developer.xero.com/app/manage) and create a new app. Note down your **Client ID** and **Client Secret**.

### 2. Configure OAuth2 Scopes

When setting up your Xero app, grant the following OAuth2 scopes:

| Scope                          | Required For                            |
| ------------------------------ | --------------------------------------- |
| `accounting.settings.read`     | Organisation settings, currencies, etc. |
| `accounting.transactions.read` | Invoices, bank transactions, payments   |
| `accounting.contacts.read`     | Contacts                                |
| `accounting.reports.read`      | Reports                                 |
| `accounting.journals.read`     | Journals                                |
| `accounting.attachments.read`  | Attachments                             |
| `offline_access`               | Long-lived access via refresh tokens    |

<Note>
  * The minimum scope required for discovery is `accounting.settings.read`.
  * You only need scopes for the streams you plan to sync.
  * Missing scopes for a selected stream will result in `401` or `403` errors.
</Note>

**Example Scope String:**

```
accounting.settings.read accounting.transactions.read accounting.contacts.read accounting.reports.read accounting.journals.read accounting.attachments.read offline_access
```

### 3. Complete the OAuth2 Authorization Flow

Follow [Xero's OAuth2 Auth Flow Guide](https://developer.xero.com/documentation/guides/oauth2/auth-flow/) to obtain your initial `access_token` and `refresh_token`.

<Tip>
  Make sure to request the `offline_access` scope to receive a refresh token.
</Tip>

### 4. Get Your Tenant ID

The `tenant_id` uniquely identifies your Xero organization. After completing OAuth authentication:

1. Call the connections endpoint:

```bash  theme={"system"}
curl -X GET "https://api.xero.com/connections" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

2. Extract the `tenantId` from the response:

```json  theme={"system"}
[
  {
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "tenantId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "tenantType": "ORGANISATION",
    "tenantName": "Your Company Name"
  }
]
```

<Note>
  If your app is connected to multiple Xero organizations, the response will contain multiple entries. Choose the `tenantId` for the organization you want to sync data from.
</Note>


Built with [Mintlify](https://mintlify.com).