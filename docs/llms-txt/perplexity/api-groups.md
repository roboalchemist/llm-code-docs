# Source: https://docs.perplexity.ai/docs/getting-started/api-groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API Groups & Billing

> Learn how to use the Perplexity API Portal to manage access, usage, billing, and team collaboration.

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
  <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=2f973650a8668a7ca088b6292875361c" alt="API Group Location" width="202" height="180" data-path="docs/assets/images/api_portal/api_group_location.png" />
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
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=13ffb9e9b89d4a491ec2ebce628531cc" alt="API Group Details" width="821" height="842" data-path="docs/assets/images/api_portal/api_group_details.png" />
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

<Card title="Access Billing Dashboard" icon="credit-card" arrow="True" horizontal="True" iconType="solid" cta="Go to Billing" href="https://console.perplexity.ai">
  Navigate directly to your API billing dashboard to manage payment methods, view usage, and configure billing settings.
</Card>

<Steps>
  <Step title="Navigate to Billing">
    Go to the **API Billing** tab in your API Portal.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=1097738622cc99e6118401234d2336e2" alt="API Billing" width="731" height="288" data-path="docs/assets/images/api_portal/api_billing.png" />
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
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=8098883c0cee70e2aad31ec6098c8a23" alt="Auto Reload" width="708" height="227" data-path="docs/assets/images/api_portal/auto_reload.png" />
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
  You'll need to include your API key in the Authorization header of every API request: `Authorization: Bearer $PERPLEXITY_API_KEY`
</Info>

### Creating an API Key

<Steps>
  <Step title="Navigate to API Keys">
    Go to the **API Keys** tab in your API Portal.
  </Step>

  <Step title="Generate New Key">
    Click **+ Create Key** to generate a new API key.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=0897ceb61302037b3630d6fabaa080a9" alt="Generate API Keys" width="737" height="158" data-path="docs/assets/images/api_portal/generate_api_keys.png" />
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
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=b747a3ffd121f74eeb36621bd605449e" alt="Click on Add Member" width="746" height="154" data-path="docs/assets/images/api_portal/click_on_add_member.png" />
    </Frame>
  </Step>

  <Step title="Enter Member Details">
    Enter the user's email address and click **Invite**.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=fa913ab5e5c00e5180a76fa2bc39dfb1" alt="Enter New Member Email" width="549" height="258" data-path="docs/assets/images/api_portal/enter_new_member_email.png" />
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
  <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=b2b794439ae3486730727655433a3517" alt="Filter Members by Role" width="379" height="236" data-path="docs/assets/images/api_portal/filter_members_by_role.png" />
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
    Navigate to the [API Platform console](https://console.perplexity.ai) and open the **Billing** page to view usage metrics

    <Frame>
      <img src="https://mintcdn.com/perplexity/cUI4ejkq6KwLBQXj/docs/assets/images/pricing/view_dashboard.png?fit=max&auto=format&n=cUI4ejkq6KwLBQXj&q=85&s=e6096b7db13381aacfe15983732cc1b5" alt="Navigate to dashboard" width="206" height="191" data-path="docs/assets/images/pricing/view_dashboard.png" />
    </Frame>
  </Step>

  <Step title="Access Invoice History">
    Select **Invoice history** > **Invoices**

    <Frame>
      <img src="https://mintcdn.com/perplexity/cUI4ejkq6KwLBQXj/docs/assets/images/pricing/view_invoice_history.png?fit=max&auto=format&n=cUI4ejkq6KwLBQXj&q=85&s=1d49d5dee2dc0fa6d743723ffb4c97d1" alt="View invoice history" width="1344" height="381" data-path="docs/assets/images/pricing/view_invoice_history.png" />
    </Frame>
  </Step>

  <Step title="View Invoice Details">
    Click on any invoice to view details

    <Frame>
      <img src="https://mintcdn.com/perplexity/cUI4ejkq6KwLBQXj/docs/assets/images/pricing/view_spend_per_api_key.png?fit=max&auto=format&n=cUI4ejkq6KwLBQXj&q=85&s=8c64a3a152d6de8db8c1c7d45b44b4e2" alt="View spend per API key" width="1274" height="575" data-path="docs/assets/images/pricing/view_spend_per_api_key.png" />
    </Frame>
  </Step>

  <Step title="Identify API Key Charges">
    Each item from the total bill will have a code at the end (e.g., pro (743S))

    * The 4 characters in parentheses are the last 4 characters of your API key
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).