# Source: https://docs.perplexity.ai/getting-started/api-groups

## 
[​](https://docs.perplexity.ai/getting-started/api-groups#what-is-an-api-group%3F)
What is an API Group?
An **API Group** is your organization’s workspace in the Perplexity API Portal. It allows you to:
  * **Manage billing** and payment methods for API usage
  * **Create and control API keys** for accessing the Perplexity API
  * **Invite team members** and control their permissions (optional)
  * **Monitor usage and costs** across all your API keys


## 
[​](https://docs.perplexity.ai/getting-started/api-groups#prerequisites)
Prerequisites
Before getting started, make sure you have:
  * A Perplexity account (sign up at [perplexity.ai](https://perplexity.ai))
  * **Admin permissions** for billing and API key management
  * A **credit card** ready for payment setup (you won’t be charged initially)


If you’re joining an existing team, you’ll need an invitation from an Admin. Contact your team lead to get access.
## 
[​](https://docs.perplexity.ai/getting-started/api-groups#accessing-the-api-portal)
Accessing the API Portal
Once signed in, navigate to the left-hand sidebar and expand the **API** section to access your API group and related settings.
![API Group Location](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_location.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=60923b0ed18b3940f05b6c94db67a534)
* * *
## 
[​](https://docs.perplexity.ai/getting-started/api-groups#creating-and-managing-an-api-group)
Creating and Managing an API Group
To set up your organization:
1
Access API Group Settings
Click **API Group** in the left sidebar.
2
Complete Organization Details
Fill out your organization’s name, address, and tax details.
Your organization name and address will appear on invoices and help us support you better.
**Fields include:**
  * Organization name and description
  * Address (Line 1, Line 2, City, State, Zip, Country)
  * Tax ID


![API Group Details](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_group_details.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=1da7640880394837c368c298c345465a)
* * *
## 
[​](https://docs.perplexity.ai/getting-started/api-groups#billing-and-payment-methods)
Billing and Payment Methods
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#how-billing-works)
How Billing Works
The Perplexity API uses a **credit-based billing system** :
  * **Credits** are purchased in advance and used for API calls
  * **Different models** consume different amounts of credits per request
  * **Usage is charged** based on tokens processed and search queries made
  * **Automatic top-up** can be enabled to avoid service interruptions


See our [Pricing page](https://docs.perplexity.ai/getting-started/pricing) for detailed cost information per model and usage type.
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#setting-up-payment)
Setting Up Payment
## [Access Billing Dashboard Navigate directly to your API billing dashboard to manage payment methods, view usage, and configure billing settings. Go to Billing ](https://www.perplexity.ai/account/api/billing)
1
Navigate to Billing
Go to the **API Billing** tab in your API Portal.
![API Billing](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/api_billing.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=c6c2e8f0f4d2b72639fee33c59bcce96)
2
Add Payment Method
Click **Add Payment Method** and enter your credit card information.
This step will not charge your credit card. It just stores payment information for future API usage.
3
Configure Auto Top-Up (Recommended)
Enable automatic credit top-up to avoid service interruptions.
![Auto Reload](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/auto_reload.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ad488d9f227382bda3bbf6119c04d40f)
If you run out of credits, your API keys will be blocked until you add to your credit balance. Auto top-up prevents this by automatically adding credits when your balance drops below a threshold.
* * *
## 
[​](https://docs.perplexity.ai/getting-started/api-groups#managing-api-keys)
Managing API Keys
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#what-are-api-keys%3F)
What are API Keys?
API keys are your credentials for accessing the Perplexity API. Each key:
  * **Authenticates your requests** to the Perplexity API
  * **Tracks usage and billing** for cost attribution
  * **Can be revoked or regenerated** for security purposes
  * **Should be kept secure** and never shared publicly


You’ll need to include your API key in the Authorization header of every API request: `Authorization: Bearer YOUR_API_KEY`
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#creating-an-api-key)
Creating an API Key
1
Navigate to API Keys
Go to the **API Keys** tab in your API Portal.
2
Generate New Key
Click **+ Create Key** to generate a new API key.
![Generate API Keys](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/generate_api_keys.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=f8c41558ce9dfd90946bc4680454b73d)
3
Secure Your Key
Copy and securely store your API key immediately.
API keys are sensitive credentials. Never expose them in client-side code or share them in public repositories.
* * *
## 
[​](https://docs.perplexity.ai/getting-started/api-groups#adding-and-managing-members)
Adding and Managing Members
Admins can invite team members to the organization with specific roles: **Admin** or **Member**.
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#adding-a-member)
Adding a Member
1
Initiate Member Invitation
Click **+ Add Member**.
![Click on Add Member](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/click_on_add_member.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=deb5bac5862619ceaf32b63371bf70a5)
2
Enter Member Details
Enter the user’s email address and click **Invite**.
![Enter New Member Email](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/enter_new_member_email.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=f401d8effceb10a0c74d1f8637256fd6)
3
Member Receives Invitation
The invited user will receive an email with a link to join your group.
Once they accept, they’ll appear in your member list with their assigned role.
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#filtering-members-by-role)
Filtering Members by Role
Use the dropdown to filter your list of team members by role.
![Filter Members by Role](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/images/api_portal/filter_members_by_role.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=27f0c659b98920905d55b7b17461080c)
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#roles)
Roles
  * **Admin** : Full access to invite/remove members, manage billing, and view usage data.
  * **Member** : Can view usage and account limits but cannot modify settings.


Only Admins can make changes to billing and member permissions.
* * *
## 
[​](https://docs.perplexity.ai/getting-started/api-groups#viewing-usage-metrics)
Viewing Usage Metrics
All members can view API usage by selecting **Usage Metrics** from the sidebar. Features include:
  * Total API call trends over time
  * Breakdown by API model and key
  * Optional date range filters


Usage metrics help you monitor API activity and optimize for cost or performance.
### 
[​](https://docs.perplexity.ai/getting-started/api-groups#tracking-spend-per-api-key)
Tracking Spend Per API Key
You can track billing for each of your API keys by following these steps:
1
Navigate to Usage Metrics
Navigate to the [API section](https://www.perplexity.ai/account/api) of your **Settings** and click on **Usage Metrics**
![Navigate to dashboard](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_dashboard.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=ff1983fb45585f3ae3ee18b4a3f594dd)
2
Access Invoice History
Select **Invoice history** > **Invoices**
![View invoice history](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_invoice_history.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=e54800b7527b37234b229d08dc980aa5)
3
View Invoice Details
Click on any invoice to view details
![View spend per API key](https://mintcdn.com/perplexity/l9g7Fas5bu7d8tY5/guides/assets/pricing/view_spend_per_api_key.png?fit=max&auto=format&n=l9g7Fas5bu7d8tY5&q=85&s=804d5a1a61d373a6aa27a54254f01f96)
4
Identify API Key Charges
Each item from the total bill will have a code at the end (e.g., pro (743S))
  * The 4 characters in parentheses are the last 4 characters of your API key


