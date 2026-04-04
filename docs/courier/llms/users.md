# Source: https://www.courier.com/docs/platform/users/users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Management

> Learn how to define notification recipients using profiles, lists, audiences, tenants, and tokens for targeted, multi-channel delivery.

## Overview

Courier gives you flexible ways to define who receives notifications, from simple email addresses to audience-based segmentation. You may see "recipient" used interchangeably with "user"; they mean the same thing.

## Key Features

* **User Profiles** - Store contact details, preferences, and custom attributes through UI and API
* **Multi-Tenant Architecture** - Organize users into tenants for B2B SaaS platforms
* **Push Token Management** - Automatic device token handling for mobile notifications
* **Profile Customization** - Add custom attributes for personalized messaging

## Creating Users

<Frame caption="User Creation Interface">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/users/user-creation-form.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=b9f64c5db0ecde4df0d12eb553216d78" alt="User Creation Interface" width="2210" height="1364" data-path="assets/platform/users/user-creation-form.png" />
</Frame>

Create users in the Courier dashboard or through the API. The dashboard lets you:

* Add contact information (email, phone, etc.)
* Set custom attributes
* Configure initial preferences
* Assign to tenants

**Create a user via API** (`PUT /profiles/{user_id}`):

```json  theme={null}
{
  "profile": {
    "email": "user@example.com",
    "phone_number": "+1234567890",
    "custom": {
      "name": "John Doe",
      "subscription_tier": "premium",
      "company": "Acme Corp",
      "role": "admin"
    }
  }
}
```

## Importing Users via CSV

You can bulk import users through the Courier dashboard using a CSV file.

### How to Import

1. Navigate to **Users** in the left sidebar
2. Click the **Import** button
3. Download the CSV template using the link in the import dialog
4. Add your user data to the downloaded template
5. Upload the populated CSV file
6. Click **Add Users** to create the profiles

### CSV Format Requirements

* **Delimiter**: Commas (`,`). The file must be comma-separated.
* **Encoding**: UTF-8 without BOM. Do not use UTF-16 or UTF-8 with BOM.
* **Header row**: Must match the template exactly. Do not rename, reorder, or add columns.
* **Quoting**: Values containing commas should be wrapped in double quotes. Empty fields should use `""`.
* **Trailing newline**: The file must **not** end with a blank line after the last row of data. A trailing newline causes the parser to interpret the empty final line as a data row with one field, triggering a "Too few fields" error.

<Warning>
  If you open the CSV template in Excel or Google Sheets, save it as **CSV (Comma delimited)**, not as `.xlsx` or tab-separated. Some spreadsheet applications change the delimiter based on your locale (e.g. semicolons in European locales), add trailing empty columns, or re-encode the file as UTF-16. Any of these will cause import errors. See [Known Spreadsheet Pitfalls](#known-spreadsheet-pitfalls) below.
</Warning>

### Template Fields

The CSV template includes the following fields. Only `id` is required; all others are optional.

The fields below are listed in the same order as the CSV template columns.

| Field                   | Description                                |
| ----------------------- | ------------------------------------------ |
| `id`                    | Unique user identifier (required)          |
| `name`                  | Full display name                          |
| `first_name`            | First name                                 |
| `last_name`             | Last name                                  |
| `email`                 | Email address                              |
| `phone_number`          | Phone number (E.164 format recommended)    |
| `gender`                | Gender                                     |
| `birthdate`             | Date of birth                              |
| `zoneinfo`              | Timezone (e.g. `America/New_York`)         |
| `locale`                | Locale code (e.g. `en_US`)                 |
| `given_name`            | Given name (OIDC standard)                 |
| `family_name`           | Family name (OIDC standard)                |
| `middle_name`           | Middle name                                |
| `nickname`              | Casual name                                |
| `preferred_username`    | Preferred display name                     |
| `profile`               | URL to profile page                        |
| `picture`               | URL to profile image                       |
| `website`               | URL to personal website                    |
| `email_verified`        | Whether email is verified (`true`/`false`) |
| `phone_number_verified` | Whether phone is verified (`true`/`false`) |
| `sub`                   | Subject identifier (OIDC standard)         |
| `courier.channel`       | Default channel preference                 |

### Creating a CSV File from a Text Editor

If you run into persistent import errors, the most reliable approach is to create the CSV directly in a plain text editor (VS Code, Notepad, or TextEdit in plain text mode) rather than through a spreadsheet application. This avoids encoding and delimiter issues entirely.

1. Open a new file in your text editor
2. Paste the header row from the template (or copy it from below)
3. Add one data row per user, matching the 22 fields exactly
4. Save the file as UTF-8 with a `.csv` extension
5. Make sure there is **no blank line** after your last row of data

Here's a working example with one test user:

```csv  theme={null}
"id","name","first_name","last_name","email","phone_number","gender","birthdate","zoneinfo","locale","given_name","family_name","middle_name","nickname","preferred_username","profile","picture","website","email_verified","phone_number_verified","sub","courier.channel"
"user_001","Jane Doe","Jane","Doe","jane@example.com","","","","","","","","","","","","","","","","",""
```

Each row must have exactly 22 comma-separated values. Use `""` for any field you want to leave empty.

### Known Spreadsheet Pitfalls

If you use Excel or Google Sheets to edit the CSV template, be aware of these common issues:

* **Encoding changes**: Excel's "Export" function can produce UTF-16 files instead of UTF-8. Always use **Save As > CSV (Comma delimited)** rather than Export. If you're unsure, open the saved file in a text editor and verify it looks like readable plain text.
* **Delimiter substitution**: In European and some other locales, Excel uses semicolons (`;`) instead of commas as the CSV delimiter. Check your file in a text editor after saving. If you see semicolons between fields, switch Excel's list separator in your system settings or create the file in a text editor instead.
* **Extra columns**: Excel sometimes adds trailing empty columns when re-saving. The template has 22 fields; if your header has more, the importer will expect that many fields in every row. Open the file in a text editor and remove any extra commas at the end of the header row.
* **Re-saving overwrites fixes**: If you fix a CSV in a text editor and then re-open and save it in Excel, Excel may reintroduce the same encoding or delimiter issues. After fixing a file in a text editor, upload it directly without opening it in a spreadsheet application again.

### Troubleshooting CSV Import

<Info>
  When you see a "Too few fields" error, open your CSV file in a plain text editor first. This lets you see exactly what the parser sees: the raw characters, delimiters, and encoding.
</Info>

**"Too few fields: expected N fields but parsed 1"**: The entire data row is being read as a single field. This means the parser cannot split the row on commas. Common causes:

* **Wrong delimiter**: Open in a text editor and check whether fields are separated by commas. If you see semicolons or tabs, re-save as CSV (Comma delimited).
* **Wrong encoding**: If the file contents look garbled in a text editor (unusual characters, `ÿþ` at the start, or double-spaced letters like `"i","d"`), the file is likely UTF-16. Re-create the file in UTF-8, or copy and paste the contents into a new text file and save as UTF-8.
* **BOM marker**: A UTF-8 BOM (`EF BB BF`) at the start of the file can occasionally interfere with header parsing. If you see `ï»¿` before the first field in a text editor, remove those characters.

**"Too few fields" error on the last row only**: This usually means your file has a trailing blank line. Open the file in a text editor, go to the very end, and delete any empty lines after the last data row.

**Expected field count doesn't match template (e.g. "expected 25" when template has 22)**: Your header row has extra columns. Open the file in a text editor and count the commas in the header. You should have exactly 21 commas (for 22 fields). Remove any extra trailing commas or columns that were added by your spreadsheet application.

**File looks correct but still fails**: Try creating the file from scratch in a text editor using the [example above](#creating-a-csv-file-from-a-text-editor). This eliminates invisible characters, encoding issues, and other artifacts that spreadsheet applications can introduce.

## User Profile Management

### Direct Address Targeting

<Info>The code samples below illustrate a subset of the message object used to make a call to the send API.</Info>

For simple use cases, specify email addresses or phone numbers directly in API calls:

```json  theme={null}
{
  "to": {
    "email": "user@example.com"
  }
}
```

### Profile-Based Targeting

Store contact details, preferences, and custom attributes in a user profile, then reference the profile by ID when sending. This separates user data from sending logic, giving you flexible routing and personalization.

```json  theme={null}
{
  "to": {
    "user_id": "user_123"
  }
}
```

**Benefits:**

* **Flexible routing** - Channel selection based on user preferences and routing rules
* **Personalization** - Access user attributes for dynamic content
* **Preference management** - Users control their notification channels and frequency
* **Data persistence** - User information persists across notifications

<Frame caption="Custom Attributes on the User">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/users/user-custom-attributes.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=ca486ed1b7b61f550ffce0f41a5076f7" alt="User Custom Attributes" width="2030" height="802" data-path="assets/platform/users/user-custom-attributes.png" />
</Frame>

<Info>For more on programmatic profile management, see the [Profiles API Documentation](/api-reference/user-profiles/get-a-profile).</Info>

## Multi-Tenant Support

For B2B SaaS platforms, you can organize users into tenants. A user can belong to multiple tenants, each with its own preferences and branding.

```json  theme={null}
{
  "to": {
    "user_id": "user_123",
    "context": {
      "tenant_id": "company_abc"
    }
  }
}
```

Tenants give you scoped preferences, custom branding, and hierarchical structures. For more on tenant hierarchies, inheritance, and advanced features, see the [Tenants documentation](/platform/tenants/tenants-overview).

## Push Notification Setup

Push notifications require device tokens that link users to their mobile devices. You can manage tokens automatically through Courier SDKs or manually through the API.

### Device Token Management

Device tokens are unique identifiers that push notification providers (FCM, APNS) use to deliver messages to specific devices. Courier manages these tokens and associates them with user profiles.

**Token lifecycle:**

* **Registration**: When a user installs your app
* **Updates**: When tokens change or refresh
* **Cleanup**: When users uninstall or switch devices

### Push Message Targeting

Once tokens are configured, target users for push notifications:

```json  theme={null}
{
  "message": {
    "to": {
      "user_id": "user_123"
    },
    "content": {
      "title": "Your order is ready!",
      "body": "Pick up your order at the nearest location."
    },
    "routing": {
      "method": "single",
      "channels": ["push"]
    }
  }
}
```

Courier automatically selects the right device tokens based on the user's registered devices and your configured push providers. There are two ways to configure tokens.

### SDK-Based Token Management (Recommended)

Use [Courier SDKs](/sdk-libraries/sdks-overview) for automatic token handling:

```javascript  theme={null}
// React Native example
import { Courier } from '@courier/react-native';

// SDK automatically handles token generation and refresh
await Courier.setUserId('user_123');
```

**SDK benefits:**

* **Automatic token generation and refresh**
* **Device registration handling**
* **Cross-platform support** (iOS, Android, React Native)
* **Error handling and retries**
* **Background sync**

### Manual Token Management

<Info>
  **Not Recommended**: Manual token management requires handling token refresh, rotation, and validity yourself. Use [Courier SDKs](/sdk-libraries/sdks-overview) for automatic token management instead.
</Info>

For edge cases requiring direct token control, use the [Token Management API](/api-reference/device-tokens/get-all-tokens).

**Add a token** (`PUT /users/{user_id}/tokens/{token}`):

```json  theme={null}
{
  "token": "device_token_from_firebase",
  "provider_key": "firebase-fcm"
}
```

Required fields are `token` and `provider_key` (one of `firebase-fcm`, `apn`, `expo`, `onesignal`). You can optionally include `device`, `properties`, `expiry_date`, and `tracking`.

**When you might need manual management:**

* Custom token handling logic
* Legacy app integration without SDK support
* Specific provider requirements not covered by SDKs

## Related Resources

<CardGroup cols={2}>
  <Card title="Lists & Audiences" href="/platform/users/audiences" icon="users">
    Group targeting and segmentation
  </Card>

  <Card title="Profiles API" href="/api-reference/user-profiles/get-a-profile" icon="code">
    User profile management reference
  </Card>

  <Card title="User Profiles Tutorial" href="/tutorials/sending/how-to-manage-user-profiles" icon="graduation-cap">
    Create, update, and manage user profiles step by step
  </Card>

  <Card title="Tenants" href="/platform/tenants/tenants-overview" icon="building">
    Multi-tenant user management for B2B platforms
  </Card>
</CardGroup>
