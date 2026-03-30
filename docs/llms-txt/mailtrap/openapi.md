# Source: https://docs.mailtrap.io/guides/integrations/retool/openapi.md

# Retool OpenAPI

Retool allows you to create an OpenAPI resource to connect to REST APIs using OpenAPI specifications. OpenAPI resources are integrations that allow you to securely connect to external services (e.g., Mailtrap) and automatically populate fields, such as, for example, query. This removes the need for manual configuration and improves accuracy.

In this guide, you'll learn how to connect Mailtrap's email delivery services to Retool using this approach, which allows you to:

* **Send transactional emails**: Automate internal processes like approval workflows, or trigger observability alerts when metrics drop below thresholds.
* **Send bulk emails**: Distribute newsletters or send legal/compliance notifications to your entire user base.
* **Sync and manage contacts**: Add users to onboarding lists or update contact fields to trigger automated email sequences.
* **Manage suppressions**: Review bounced/unsubscribed addresses and remove resolved emails to resume communication.

{% hint style="info" %}
For the integration to work, you need to add and [verify your email sending domain](https://help.mailtrap.io/article/69-sending-domain-setup) since Mailtrap allows you to send emails only from a verified domain.
{% endhint %}

### How to configure a resource

In this section, we’ll show you how to configure [Retool resources](https://docs.retool.com/data-sources/quickstarts/resources), which can be re-used in [queries](https://docs.retool.com/queries/quickstart).

#### Step 1. Locate Mailtrap OpenAPI specifications

Mailtrap maintains its API definitions in a structured format. To implement this in Retool, you must use the YML specifications, which you can find under **specs** in [mailtrap/mailtrap-openapi](https://github.com/mailtrap/mailtrap-openapi/tree/main/specs).

Once you choose your desired implementation, to ensure Retool can parse the schema correctly, be sure to click on **Raw**, so you can use the **Raw** URL of the YAML file.&#x20;

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FjkoC247UuKtElY1OcG4j%2Fopenapi%201.png?alt=media&#x26;token=f9298e4d-1dfb-4d29-b6d2-9379c0d2a0f7" alt=""><figcaption></figcaption></figure>

Then, simply copy the URL:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FS3qYtQ4CAJ8fRbTn55IK%2Fopenapi%202.png?alt=media&#x26;token=c589c88f-b14b-463f-b5bf-977184522626" alt=""><figcaption></figcaption></figure>

### Step 2. Configure a Resource in Retool

Navigate to the **Resources** tab in Retool and create a new **OpenAPI** resource.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FIbGV3cINV0yd13PR25o2%2Fopenapi%203.png?alt=media&#x26;token=8db080e6-2c19-4f5d-84de-af0f71469fb0" alt=""><figcaption></figcaption></figure>

There, you will need to configure the following settings:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FdtPY6D357nJdLsM1oO8M%2Fopenapi%204.png?alt=media&#x26;token=cc933765-41f9-449e-8e83-59aa202f8a61" alt=""><figcaption></figcaption></figure>

Once you insert the required details, make sure to click **Create resource**. Also note that you will also be able to re-use this Resource across your projects.

**Hint**: To make sure you’ve entered everything correctly before using the Resource in your Queries, click on **Test connection**. If the connection works, you should get the following message:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fv2fVtXNpyAi2kjg2zwmo%2Fopenapi%205.png?alt=media&#x26;token=76c3dead-0154-43ff-87e9-f026c84e9589" alt=""><figcaption></figcaption></figure>

### How to configure queries&#x20;

In the following section, we will show you some queries you can run with the OpenAPI resources connected to Mailtrap and possible use cases.

#### Transactional email sending

To send transactional emails, use the [email-sending-transactional.openapi.yml](https://github.com/mailtrap/mailtrap-openapi/blob/main/specs/email-sending-transactional.openapi.yml). Transactional emails are executed via the `POST /send` endpoint.

**Use cases**:

{% tabs %}
{% tab title="Internal process automation" %}
Trigger approval emails for vacation requests, hardware purchase requests, internal discount approvals, etc.
{% endtab %}

{% tab title="Observability alerts" %}
Automated notifications triggered by Retool workflows when specific metrics (MRR, revenue, or site traffic) drop below a defined threshold.
{% endtab %}
{% endtabs %}

**Query implementation example**: Select the `POST /send` endpoint, use the following structure of the request body, and add dynamic variables into the payload using `{{ }}` syntax where necessary:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FRwuoVycaCVycyhwzKUjI%2Fopenapi%206.png?alt=media&#x26;token=de6cad80-0aca-4cc1-b1a1-68c05245da33" alt=""><figcaption></figcaption></figure>

**Response**:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FYVMiAY0BzfFClndrxLSf%2Fopenapi%207.png?alt=media&#x26;token=c0a6c3d0-8223-433a-97ba-0dd8b92aaa66" alt=""><figcaption></figcaption></figure>

Example code you can copy for the request body:

```json
{
  "from": {"email": "sender@example.com"},
  "to": [{"email": "{{ user_email }}"}],
  "subject": "Vacation Request Approved",
  "text": "The request for ID {{ request_id }} has been finalized."
}
```

#### Bulk email sending

To send bulk emails, use the [email-sending-bulk.openapi.yml](https://github.com/mailtrap/mailtrap-openapi/blob/main/specs/email-sending-bulk.openapi.yml). `POST /bulk/send` endpoint is optimized for delivery of promotional or marketing emails to multiple recipients simultaneously through the [Bulk stream](https://docs.mailtrap.io/email-api-smtp/setup/bulk-stream).

**Use cases**:

{% tabs %}
{% tab title="Legal and compliance notifications" %}
Send mandatory updates regarding Terms of Service (ToS) changes, Privacy Policy updates to the entire user database, etc.
{% endtab %}

{% tab title="Newsletter distribution" %}
Trigger monthly or weekly updates to a broad list of subscribers.
{% endtab %}
{% endtabs %}

**Query implementation example**: Choose the `POST /bulk/send` endpoint and use a request body.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FGwrIuDRE7CU9jf9ddROJ%2Fopenapi%208.png?alt=media&#x26;token=5001edb3-6851-4e49-aa36-413db933bccb" alt=""><figcaption></figcaption></figure>

**Response**:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FhxMJJI41TLVPFYlN54nI%2Fopenapi%209.png?alt=media&#x26;token=c1c664f3-e55b-4a08-8de4-c90f152b057a" alt=""><figcaption></figcaption></figure>

Example code you can use for the request body:

```json
{
  "from": {"email": "sender@example.com"},
  "to": [{"email": "recipient@example.com"}, {"email": "recipient+1@example.com"}],
  "bcc": [{"email": "recipient+2@example.com"}],
  "subject": "Monthly Newsletter",
  "html": "<h1>Privacy Policy Update</h1>",
  "category": "newsletter"
}
```

#### Contact synchronization and updates

To sync contacts from external databases or CRMs with Mailtrap or create, update, and manage contact lists, use the [contacts.openapi.yml](https://github.com/mailtrap/mailtrap-openapi/blob/main/specs/contacts.openapi.yml).&#x20;

If used in combination with [Mailtrap Automation](https://docs.mailtrap.io/email-marketing/automations) feature, you can set up the query for:

{% tabs %}
{% tab title="User onboarding" %}
Once a new customer is added to a specific "Onboarding" contact list, the onboarding email sequence will be sent automatically.
{% endtab %}

{% tab title="Lifecycle triggers" %}
Update a contact field (e.g., `subscription_status: "trial_ended"`) to trigger automated Mailtrap sequences, such as a "Welcome" or "Nurture" email series.
{% endtab %}
{% endtabs %}

**Query implementation example**: Use the `PATCH` method with path parameters for `account_id` and `contact_identifier` to update specific metadata fields without overwriting the entire contact object.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FSXxR7UAekeeCpypLuu0Q%2Fopenapi%2010.png?alt=media&#x26;token=732f12ba-dde5-4a8d-9be9-e42285533f03" alt=""><figcaption></figcaption></figure>

**Response**:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FH3ZBYUBrmpTPy29PByOd%2Fopenapi%2011.png?alt=media&#x26;token=9e0d23d0-8749-40a3-bfa2-7cf6492260ab" alt=""><figcaption></figcaption></figure>

#### Suppression list management

To get a list of your suppressions or delete certain emails from your suppression list use the [account-management.openapi.yml](https://github.com/mailtrap/mailtrap-openapi/blob/main/specs/account-management.openapi.yml). It uses the `GET /suppressions` and `DELETE /suppressions/{id}` endpoints with which you can maintain email deliverability standards.&#x20;

**Primary use cases**:

{% tabs %}
{% tab title="Contacts review" %}
Review the list of bounced or unsubscribed addresses to protect IP reputation.
{% endtab %}

{% tab title="List cleanup" %}
Remove a specific email from the suppression list once the underlying issue (e.g., a full inbox or temporary server error) has been resolved, allowing future communication to resume.
{% endtab %}
{% endtabs %}

**Query implementation example**: If you were to use the query to get a list of emails in your suppressions list, use `GET /accounts/{account_id}/account_accesses`, and specify your Mailtrap account ID.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FVOUFi8lcN0Gp2kgjrJ2Z%2Fopenapi%2012.png?alt=media&#x26;token=8284c32e-f37b-43a2-aad0-eae94c2ce92e" alt=""><figcaption></figcaption></figure>

**Response**:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fzmg9KezLfJWtn7NiHmrY%2Fopenapi%2013.png?alt=media&#x26;token=7b82b0a9-368e-4832-acb2-be5c3d191703" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Keep in mind that we take into account the suppressions for both transactional and bulk email sending.
{% endhint %}
