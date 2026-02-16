
# API Groups & Billing

Source: https://docs.perplexity.ai/docs/getting-started/api-groups

Learn how to use the Perplexity API Portal to manage access, usage, billing, and team collaboration.

## What is an API Group?

An **API Group** is your organization's workspace in the Perplexity API Portal. It allows you to:

* **Manage billing** and payment methods for API usage
* **Create and control API keys** for accessing the Perplexity API
* **Invite team members** and control their permissions (optional)
* **Monitor usage and costs** across all your API keys

## Prerequisites

Before getting started, make sure you have:

* A Perplexity account (sign up at [perplexity.ai](https://perplexity.ai))
* **Admin permissions** for billing and API key management
* A **credit card** ready for payment setup (you won't be charged initially)

<Note>
  If you're joining an existing team, you'll need an invitation from an Admin. Contact your team lead to get access.
</Note>

## Accessing the API Portal

Once signed in, navigate to the left-hand sidebar and expand the **API** section to access your API group and related settings.

<Frame>
  <img alt="API Group Location" />
</Frame>

***

## Creating and Managing an API Group

To set up your organization:

<Steps>
  <Step title="Access API Group Settings">
    Click **API Group** in the left sidebar.
  </Step>

  <Step title="Complete Organization Details">
    Fill out your organization's name, address, and tax details.

    <Info>
      Your organization name and address will appear on invoices and help us support you better.
    </Info>

    **Fields include:**

    * Organization name and description
    * Address (Line 1, Line 2, City, State, Zip, Country)
    * Tax ID

    <Frame>
      <img alt="API Group Details" />
    </Frame>
  </Step>
</Steps>

***

## Billing and Payment Methods

### How Billing Works

The Perplexity API uses a **credit-based billing system**:

* **Credits** are purchased in advance and used for API calls
* **Different models** consume different amounts of credits per request
* **Usage is charged** based on tokens processed and search queries made
* **Automatic top-up** can be enabled to avoid service interruptions

<Info>
  See our [Pricing page](./pricing) for detailed cost information per model and usage type.
</Info>

### Setting Up Payment

<Card title="Access Billing Dashboard" icon="credit-card" href="https://www.perplexity.ai/account/api/billing">
  Navigate directly to your API billing dashboard to manage payment methods, view usage, and configure billing settings.
</Card>

<Steps>
  <Step title="Navigate to Billing">
    Go to the **API Billing** tab in your API Portal.

    <Frame>
      <img alt="API Billing" />
    </Frame>
  </Step>

  <Step title="Add Payment Method">
    Click **Add Payment Method** and enter your credit card information.

    <Note>
      This step will not charge your credit card. It just stores payment information for future API usage.
    </Note>
  </Step>

  <Step title="Configure Auto Top-Up (Recommended)">
    Enable automatic credit top-up to avoid service interruptions.

    <Frame>
      <img alt="Auto Reload" />
    </Frame>

    <Warning>
      If you run out of credits, your API keys will be blocked until you add to your credit balance. Auto top-up prevents this by automatically adding credits when your balance drops below a threshold.
    </Warning>
  </Step>
</Steps>

***

## Managing API Keys

### What are API Keys?

API keys are your credentials for accessing the Perplexity API. Each key:

* **Authenticates your requests** to the Perplexity API
* **Tracks usage and billing** for cost attribution
* **Can be revoked or regenerated** for security purposes
* **Should be kept secure** and never shared publicly

<Info>
  You'll need to include your API key in the Authorization header of every API request: `Authorization: Bearer YOUR_API_KEY`
</Info>

### Creating an API Key

<Steps>
  <Step title="Navigate to API Keys">
    Go to the **API Keys** tab in your API Portal.
  </Step>

  <Step title="Generate New Key">
    Click **+ Create Key** to generate a new API key.

    <Frame>
      <img alt="Generate API Keys" />
    </Frame>
  </Step>

  <Step title="Secure Your Key">
    Copy and securely store your API key immediately.

    <Warning>
      API keys are sensitive credentials. Never expose them in client-side code or share them in public repositories.
    </Warning>
  </Step>
</Steps>

***

## Adding and Managing Members

Admins can invite team members to the organization with specific roles: **Admin** or **Member**.

### Adding a Member

<Steps>
  <Step title="Initiate Member Invitation">
    Click **+ Add Member**.

    <Frame>
      <img alt="Click on Add Member" />
    </Frame>
  </Step>

  <Step title="Enter Member Details">
    Enter the user's email address and click **Invite**.

    <Frame>
      <img alt="Enter New Member Email" />
    </Frame>
  </Step>

  <Step title="Member Receives Invitation">
    The invited user will receive an email with a link to join your group.

    <Check>
      Once they accept, they'll appear in your member list with their assigned role.
    </Check>
  </Step>
</Steps>

### Filtering Members by Role

Use the dropdown to filter your list of team members by role.

<Frame>
  <img alt="Filter Members by Role" />
</Frame>

### Roles

* **Admin**: Full access to invite/remove members, manage billing, and view usage data.
* **Member**: Can view usage and account limits but cannot modify settings.

<Warning>
  Only Admins can make changes to billing and member permissions.
</Warning>

***

## Viewing Usage Metrics

All members can view API usage by selecting **Usage Metrics** from the sidebar.

Features include:

* Total API call trends over time
* Breakdown by API model and key
* Optional date range filters

<Check>
  Usage metrics help you monitor API activity and optimize for cost or performance.
</Check>

### Tracking Spend Per API Key

You can track billing for each of your API keys by following these steps:

<Steps>
  <Step title="Navigate to Usage Metrics">
    Navigate to the [API section](https://www.perplexity.ai/account/api) of your **Settings** and click on **Usage Metrics**

    <Frame>
      <img alt="Navigate to dashboard" />
    </Frame>
  </Step>

  <Step title="Access Invoice History">
    Select **Invoice history** > **Invoices**

    <Frame>
      <img alt="View invoice history" />
    </Frame>
  </Step>

  <Step title="View Invoice Details">
    Click on any invoice to view details

    <Frame>
      <img alt="View spend per API key" />
    </Frame>
  </Step>

  <Step title="Identify API Key Charges">
    Each item from the total bill will have a code at the end (e.g., pro (743S))

    * The 4 characters in parentheses are the last 4 characters of your API key
  </Step>
</Steps>
