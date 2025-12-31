# Source: https://docs.perplexity.ai/getting-started/api-groups.md

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
  <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=60923b0ed18b3940f05b6c94db67a534" alt="API Group Location" data-og-width="202" width="202" data-og-height="180" height="180" data-path="images/api_portal/api_group_location.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=0d9695c8af0909d534de23367b87c2b1 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=283d9148c742bca11252072ccb3dbc13 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=0c15f6daa67288ab18a2d8044cd051f0 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=37a16253e19753a7d762838ff3f26855 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=1ef2a10965a71634a2fec034906bbe97 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=e06ffdaa832991c18f9908943a9510b5 2500w" />
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
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=1da7640880394837c368c298c345465a" alt="API Group Details" data-og-width="821" width="821" data-og-height="842" height="842" data-path="images/api_portal/api_group_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=7acfb5ff709fcbdcf31ac308c47d0c57 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=32fa8606f546a64d411f1a8dbfec32ea 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=3b08c7f8629bd43364c282b3cd2dfae2 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=72f01191aeca49622d9a09392f12d043 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=4897d712600c5a42837ffa91ed64f6db 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=55a355327c4738a8102fa78db2aabbe9 2500w" />
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

<Card title="Access Billing Dashboard" icon="credit-card" arrow="True" horizontal="True" iconType="solid" cta="Go to Billing" href="https://www.perplexity.ai/account/api/billing">
  Navigate directly to your API billing dashboard to manage payment methods, view usage, and configure billing settings.
</Card>

<Steps>
  <Step title="Navigate to Billing">
    Go to the **API Billing** tab in your API Portal.

    <Frame>
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=c6c2e8f0f4d2b72639fee33c59bcce96" alt="API Billing" data-og-width="731" width="731" data-og-height="288" height="288" data-path="images/api_portal/api_billing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=5d65109817adbce75ffac6991192cc57 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=2bd83e25b683ab3535914325de3798ae 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=027009d05fd6c02e84b6bf9bc4da1b1c 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=b28701dd96ff8ef5e91757e098666add 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=b56a45636e0c33db2b17d1c71b754374 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=2e2bb3598954d408eccb85d7523426e9 2500w" />
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
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ad488d9f227382bda3bbf6119c04d40f" alt="Auto Reload" data-og-width="708" width="708" data-og-height="227" height="227" data-path="images/api_portal/auto_reload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=a28beb091c576c62e24ac716e55f45ab 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=0bad5b10b57c9527a4b0e50701a11402 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=d8bcfe1e32b1b80158a254fcba8bf889 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ac81425af371bfc15bd10b1e1ca126d6 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=07f527d591ebe5622ce4531a4c8f316d 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=3605774e24e8429a675216244126f917 2500w" />
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
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=f8c41558ce9dfd90946bc4680454b73d" alt="Generate API Keys" data-og-width="737" width="737" data-og-height="158" height="158" data-path="images/api_portal/generate_api_keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=e5f35dd228c9f198ab89cfdbc3b7c739 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=e3ec0a151ffac69befdd3dd6f9c3ade5 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=fb67be82e1cc01edd23fbd0d81eed2f2 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=66e9cbd117df41e5118c23251b3f2e1a 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=9e3c6524759c7cd02e8114470b7e5f3a 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=01afce0ba02019235fa4a0c6c21b7624 2500w" />
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
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=deb5bac5862619ceaf32b63371bf70a5" alt="Click on Add Member" data-og-width="746" width="746" data-og-height="154" height="154" data-path="images/api_portal/click_on_add_member.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=04e76cdc3b9ec8cb78b23c45ae581cc2 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ad0a10236e175f55bb1591c7df9402c6 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=141055bf1dfd61d7052a6cf3909d27e8 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=167d0df1c95b647cb067eec01d02e24b 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=251f0aee92b97c931e1b6df1104f80f5 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=fa336b8a62d0602bf18b53fd65b02953 2500w" />
    </Frame>
  </Step>

  <Step title="Enter Member Details">
    Enter the user's email address and click **Invite**.

    <Frame>
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=f401d8effceb10a0c74d1f8637256fd6" alt="Enter New Member Email" data-og-width="549" width="549" data-og-height="258" height="258" data-path="images/api_portal/enter_new_member_email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=30a6b4191cd846c6b30cb4d879f2d3bf 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=de4eaf9f3f43360a39473ae278b93d4f 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=b2d1bcbcf2f559b63f2ea8212e84fea6 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=097789be2ed44686ed690a1a29230ddd 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=dbbe8663c05fbd28eebe36ea125ffbfe 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=4fc27ae417addaa70612961e60fd6389 2500w" />
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
  <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=27f0c659b98920905d55b7b17461080c" alt="Filter Members by Role" data-og-width="379" width="379" data-og-height="236" height="236" data-path="images/api_portal/filter_members_by_role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=74a384913ab947bb5ab9d958aa4831f9 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=b3f4612587303913b122f60815131b73 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=0f103b935268b669a1e08bf4e9111439 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=a0b73af2a29b8a6f40e745e4a1f673a6 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=08c140b29bf4bf5ae47ea53ffd387f86 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ca2cf54efd00a05c1062262ea00f2848 2500w" />
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
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ff1983fb45585f3ae3ee18b4a3f594dd" alt="Navigate to dashboard" data-og-width="206" width="206" data-og-height="191" height="191" data-path="guides/assets/pricing/view_dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=91bf6a71ff8e26e0dbb1bcc39e2584db 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=855a02cc03211b4e1e406439e3465153 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=5750d06c407df3ce17c2ea86a1e46d96 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=d06bcd5f7661de8e5f7130c729ac9365 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=f85bce9d95d9da56aa2785825e3a8379 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=afb598684633b152c5752b5ace7246ee 2500w" />
    </Frame>
  </Step>

  <Step title="Access Invoice History">
    Select **Invoice history** > **Invoices**

    <Frame>
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=e54800b7527b37234b229d08dc980aa5" alt="View invoice history" data-og-width="1344" width="1344" data-og-height="381" height="381" data-path="guides/assets/pricing/view_invoice_history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=3f380c9ea64e00b7651c2155371f82af 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=728aa8f5fdf09ed32b74f5bd73532259 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=e546f4ad52f33b130986d85d64c8fc38 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=9f78bd2444a78fd1b79b350ce62aaea1 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=410cb562cdee4dea19e7d7169fc7836d 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=835023ff6e4e271006d23646890aea47 2500w" />
    </Frame>
  </Step>

  <Step title="View Invoice Details">
    Click on any invoice to view details

    <Frame>
      <img src="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=804d5a1a61d373a6aa27a54254f01f96" alt="View spend per API key" data-og-width="1274" width="1274" data-og-height="575" height="575" data-path="guides/assets/pricing/view_spend_per_api_key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?w=280&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ba5c9b7a13c47ca3bf50b6fd6866430f 280w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?w=560&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=d3ebe858abbdd63907c0aa22e5e4a555 560w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?w=840&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=a9b17b5457b4af60c15e9d66e8a2c359 840w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?w=1100&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=74810af3e32b3a3829ff03f5ac1517d5 1100w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?w=1650&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=eac382d6c4d92b772e23a057def31b56 1650w, https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?w=2500&fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=e9ae27aae538134e04731d3e6cbf5e06 2500w" />
    </Frame>
  </Step>

  <Step title="Identify API Key Charges">
    Each item from the total bill will have a code at the end (e.g., pro (743S))

    * The 4 characters in parentheses are the last 4 characters of your API key
  </Step>
</Steps>
