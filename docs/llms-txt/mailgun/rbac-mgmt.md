# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/api-key-mgmt/rbac-mgmt.md

# API Management and Security

Email API keys provide secure access to email services and data. They enable access to our APIs and allow integrating email functionalities into applications. At Mailgun, we prioritize security through granular access controls and role based authentication, ensuring that each API key has precisely the permissions it needs and nothing more. Proper management of these keys ensures smooth operation, protects against unauthorized access, and maintains the security of sensitive information.

Mailgun provides two types of API keys for authenticating against the API:

## Account API Keys

When you sign up for Mailgun, you can generate one or more API keys depending on your plan which allow you to perform all CRUD operations via our various API endpoints and for any of your sending domains. These keys have complete access to your account, so they should be stored securely and never shared publicly.
With most plans, you can add additional API keys with a specific role via [Role Based Access Control (RBAC)](https://help.mailgun.com/hc/en-us/articles/4406099964059-Changing-an-account-user-s-role-and-permissions#h_01HWR65G3PE12TF4T1RJDT73YP).

**To view and create your account API key(s):**

1. Navigate to the **Mailgun Dashboard**
2. Select **Account Settings** on the right side
3. On the **API keys** page click the "Create key" button and fill in the form fields in the modal as needed.
4. When ready, click the modal's "Create Key" button and record the generated key secret for safekeeping.


Security Notice
Your API key(s) provides full access to your Mailgun account. Store it securely using environment variables or a secrets management system. Never commit this key to version control or share it in public forums.

## Domain Sending Keys

Domain Sending Keys are API keys that only allow sending messages via a POST call on /messages and /messages.mime endpoints for the specific domain in which they are created. These keys provide a secure way to enable sending functionality without exposing your full account access. This is ideal for production applications that only need to send email.

**To create a sending API key:**

1. Navigate to the **Mailgun Dashboard**
2. Select the **Sending** tab on the left side of the Mailgun dashboard
3. Select the **Domains** tab and choose the domain for which you want to add a sending key
4. Navigate to the **Sending keys** tab
5. Click **Add Sending Key**


Domain Sending Keys are recommended for production applications as they limit potential security exposure by restricting access to only the sending functionality.

# Managing Role Based Access Control (RBAC) API Keys

Role Based Access Control (RBAC) API Keys empower admin users to generate API keys using predefined roles that dictate the access level of each key. This feature allows you to implement the principle of least privilege, ensuring team members and applications have only the permissions they need.

Availability
Role Based Access Control is available on Enterprise and certain Business plans. See our [Pricing page](https://www.mailgun.com/pricing/) for more details about plan features.

Important Limitations
Assigned roles cannot be updated after creation. If you need to change a key's permissions, you must create a new key with the desired role and revoke the old one. Be sure to save the key in a secure location immediately upon creation, as you will only be able to view it once.

## Understanding Roles

Each role is designed to align with common organizational functions and access requirements:

- **Admin:** Full administrative access across all endpoints. Ideal for account owners and senior technical leadership who need complete control over the Mailgun account.
- **Analyst:** Read only access to data and metrics. Perfect for data analysts, business intelligence teams, and stakeholders who need to review email performance without making changes.
- **Developer:** Full access to technical endpoints needed for building and maintaining email integrations. Designed for engineering teams who implement and manage email functionality in applications.
- **Support:** Read access to most endpoints with write access to specific management endpoints. Tailored for customer support teams who need to investigate issues and manage email deliverability without broader administrative privileges.


## API Permissions Framework

During the API key creation process, you select a predefined role that assigns specific access levels to various public API endpoints. Understanding these permission types helps you choose the appropriate role for each use case.

| Permission Type | Description |
|  --- | --- |
| **No Access** | The API key cannot access these endpoints. Any attempt to call these endpoints will return an authentication error. |
| **Read** | Allows the API key to access `GET` endpoints within the selected permission category. Ideal for monitoring, reporting, and auditing purposes. |
| **Read/Write** | Allows the API key to access `GET`, `PATCH`, `PUT`, `DELETE`, and `POST` endpoints within the selected permission category. Provides full operational control within that category. |


## RBAC API Key Permissions by Role

The table below details each role's specific permissions across all public API endpoints. Use this reference when determining which role best fits your security and operational requirements.

| Endpoints | Admin | Analyst | Developer | Support |
|  --- | --- | --- | --- | --- |
| Domains | Read/Write | Read | Read/Write | Read |
| Messages | Read/Write | Read | Read/Write | Read |
| Webhooks | Read/Write | Read | Read/Write | Read |
| Logs | Read/Write | Read | Read/Write | Read |
| Tags | Read/Write | Read | Read/Write | Read |
| Metrics | Read/Write | Read | Read/Write | Read |
| Unsubscribes (suppressions) | Read/Write | No Access | Read/Write | Read/Write |
| Complaints (suppressions) | Read/Write | No Access | Read/Write | Read/Write |
| Bounces (suppressions) | Read/Write | No Access | Read/Write | Read/Write |
| Whitelist (suppressions) | Read/Write | Read | Read/Write | Read/Write |
| Routes | Read/Write | Read | Read/Write | Read |
| Mailing Lists | Read/Write | Read | Read/Write | Read/Write |
| Templates | Read/Write | Read | Read/Write | Read/Write |
| IPs | Read/Write | Read | Read/Write | Read |
| IP Pools | Read/Write | Read | Read/Write | Read |
| Sub-Accounts | Read/Write | Read | Read/Write | Read |
| Validations | Read/Write | Read | Read/Write | Read |
| Secure Tracking | Read/Write | Read | Read/Write | Read |
| Custom Message Limit | Read/Write | Read | Read | Read |
| Credentials | Read/Write | No Access | Read | No Access |
| Keys | Read/Write | No Access | Read | No Access |
| IP Allowlist | Read/Write | Read | Read/Write | Read |
| Account Management | Read/Write | Read | Read/Write | Read |
| Users on an account | Read | No Access | No Access | No Access |
| Another user's details on an account | Read | No Access | No Access | No Access |
| Own user details | Read | Read | Read | Read |


## Custom Message Limits

The Custom Message Limit feature imposes a hard limit on how many messages your account can send during a calendar month. This is a protective measure that helps prevent unexpected overages and provides budget control for high volume senders.

When message limits are enabled:

- The primary account holder receives an email notification at 50% of the limit
- A second notification is sent at 75% of the limit
- After reaching 100% of the limit, the account will be temporarily disabled until the beginning of the following month


You can re-enable your account before the next month begins by either adjusting the message limit via the dashboard or through the API, or by upgrading your plan.

## Sending Limits for Subaccounts

Primary account admins, developers, and billing users can set individual message sending limits for each subaccount. This provides granular control over resource allocation across your organization or client base.
To configure subaccount sending limits use the [Set a custom sending limit API endpoint](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/put-v5-accounts-subaccounts-subaccount_id-limit-custom-monthly)

Subaccount limits are particularly useful for:

- Agencies managing multiple client accounts
- Organizations with multiple departments or business units
- Platforms providing email services to end users


# Best Practices for API Key Management

## Key Storage and Security

**Never expose API keys in client side code.** API keys should only be used in server side applications where they cannot be accessed by end users. Store keys using:

- Environment variables in production environments
- Secrets management systems like AWS Secrets Manager, HashiCorp Vault, or Azure Key Vault
- Encrypted configuration files with restricted access permissions


**Implement key rotation policies.** Regularly rotate your API keys to minimize the risk of compromised credentials. We recommend rotating keys at least quarterly, or immediately if you suspect a key has been exposed.

**Use the most restrictive role possible.** Always assign the minimum permissions required for each use case. If an application only needs to send email, use a Domain Sending Key rather than a primary account key.

## Monitoring and Auditing

Monitor your API key usage regularly through the Mailgun dashboard. Watch for:

- Unexpected spikes in API calls that might indicate compromised credentials
- Failed authentication attempts
- API calls from unfamiliar IP addresses or geographic regions


## Responding to Compromised Keys

If you suspect an API key has been compromised:

1. Immediately revoke the compromised key in your Mailgun dashboard
2. Generate a new key with the appropriate role
3. Update all applications and services using the old key
4. Review your account activity logs for unauthorized usage
5. Consider implementing IP allowlisting for additional security


## IP Allowlisting

For enhanced security, configure IP allowlisting to restrict API access to specific IP addresses or ranges. This adds an additional layer of protection by ensuring that even if a key is compromised, it cannot be used from unauthorized locations.

# Related Resources

- [Mailgun API Reference Documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Email Best Practices Guide](https://www.mailgun.com/resources/)
- [Mailgun Security Features](https://www.mailgun.com/security/)
- [Contact Mailgun Support](https://www.mailgun.com/support/)