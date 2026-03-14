# Source: https://plivo.com/docs/faq/account/account-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Account Management

> Common questions about managing your Plivo account, subaccounts, and settings

Frequently asked questions about Plivo account setup, credentials, security, team management, and subaccounts.

***

## How do I create a Plivo account?

1. Go to [Plivo signup](https://cx.plivo.com/signup)
2. Enter your name, work email, and set a password
3. Verify your email via activation link
4. Verify your phone number

**Requirements:**

* Work email address — personal (e.g., @gmail.com, @yahoo.com) and disposable email domains are not accepted
* Valid phone number for verification
* No VPN during onboarding

<Note>
  Plivo validates email domains during signup. If validation fails, signup will not proceed.
</Note>

To send voice or messaging traffic to countries beyond the US and India, a minimum spend agreement is required. See [Plivo Pricing](https://www.plivo.com/pricing/) for details.

***

## What is Data Region?

During signup, you select a **Data Region** that determines which phone numbers and services you can access.

| Data Region       | Can Access                                                                                                           | Payment Method                   |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **United States** | Phone numbers in [supported countries](https://www.plivo.com/virtual-phone-numbers/coverage/), international calling | International credit/debit cards |
| **India**         | Indian phone numbers only, calling within India                                                                      | Indian credit/debit cards only   |

<Warning>
  **Data region cannot be changed after account creation.** If you need both Indian numbers and international calling, you'll need separate accounts for each region.
</Warning>

### When to choose India

* Your business is registered in India
* You only need Indian phone numbers
* You're making calls within India

### When to choose United States

* You need phone numbers outside India
* You need to make international calls
* You're operating globally

***

## What happens if my signup is delayed?

Plivo verifies all signups to ensure compliance with telecommunications regulations. Accounts may be placed on hold if risk assessment indicates concerns. Contact [Plivo Support](https://support.plivo.com) if delayed.

***

## Why can't I create an account with my email?

Plivo requires a **business domain email address** for account registration.

| Email Type      | Accepted? | Example                                                                          |
| --------------- | --------- | -------------------------------------------------------------------------------- |
| Business domain | ✅ Yes     | [john@yourcompany.com](mailto:john@yourcompany.com)                              |
| Personal email  | ❌ No      | [john@gmail.com](mailto:john@gmail.com), [john@yahoo.com](mailto:john@yahoo.com) |
| Temporary email | ❌ No      | [john@tempmail.com](mailto:john@tempmail.com)                                    |

***

## I can't log in to my account. What should I do?

### Troubleshooting steps

| Issue                           | Solution                                                                     |
| ------------------------------- | ---------------------------------------------------------------------------- |
| **Forgot password**             | Click "Forgot password" on login page, check email (including spam)          |
| **Password reset link expired** | Request a new reset link (links expire after 24 hours)                       |
| **2FA code not working**        | Ensure device time is synced; try recovery codes                             |
| **Locked out of 2FA**           | Contact [Plivo Support](https://support.plivo.com) with account verification |
| **Account suspended**           | Check email for suspension notice; contact support                           |
| **Browser issues**              | Clear cache/cookies, try incognito mode, or different browser                |

### If password reset emails aren't arriving

1. Check spam/junk folder
2. Verify you're using the correct email address
3. Add `noreply@plivo.com` to your contacts
4. Wait 5-10 minutes (email delivery can be delayed)
5. Try requesting another reset

### If you've lost access to 2FA

1. Try using **recovery codes** (saved during 2FA setup)
2. If no recovery codes, contact [Plivo Support](https://support.plivo.com) with:
   * Account email address
   * Auth ID (if known)
   * Business verification documents

<Warning>
  **Security verification required:** For security, Plivo requires identity verification before disabling 2FA on an account. This process may take 1-2 business days.
</Warning>

***

## Why is my account disabled or suspended?

Your account may be disabled for several reasons:

| Reason                        | Solution                                          |
| ----------------------------- | ------------------------------------------------- |
| **Policy violation**          | Check email for violation notice, contact support |
| **Suspicious activity**       | Verify identity with support                      |
| **Fraudulent usage detected** | Contact support with business verification        |
| **AUP violation**             | Review Acceptable Use Policy, contact support     |
| **Inactivity**                | Contact support to reactivate                     |

### To reactivate a disabled account

1. Check your email for any notices from Plivo
2. Log in to Console (if possible) and review any alerts
3. Contact [Plivo Support](https://support.plivo.com) with:
   * Your account email
   * Auth ID (if known)
   * Business verification documents (if requested)

<Note>
  Reactivation may require identity verification and can take 1-3 business days depending on the reason for suspension.
</Note>

***

## How do I close my account?

Navigate to **Account > Service Address** and click **Close Account**.

**After closure:**

* All applications, phone numbers, endpoints, and logs are permanently deleted
* Remaining credits are refunded within 20 business days (only recharges from the last 90 days)
* Trial credits are not refunded
* Team members lose access immediately

***

## What are Auth ID and Auth Token?

| Credential     | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| **Auth ID**    | Your unique account identifier (username) — cannot be changed |
| **Auth Token** | Your API password — can be changed                            |

Find them at the top of the [Plivo Console](https://cx.plivo.com/home) home page.

***

## How do I regenerate my Auth Token?

1. Go to [Auth Settings](https://cx.plivo.com/profile/auth) in the Plivo console
2. Click **Generate Auth Token**
3. Select when to expire the old token:
   * **Delete immediately** — old token stops working right away
   * **Delete in 48 hours** — gives you time to update your applications
4. Type `delete auth token` to confirm

<Warning>
  Only one Auth Token can be active at a time. After the old token expires, any application still using it will fail to authenticate. Update all integrations with the new token and test before the old token expires.
</Warning>

***

## Is Two-Factor Authentication mandatory?

Yes. 2FA is mandatory for all Plivo accounts.

**Available methods:**

* Phone OTP (SMS/Voice)
* Authenticator apps (Google Authenticator, 1Password, Microsoft Authenticator, Authy)
* Recovery codes

***

## How do I set up an authenticator app for 2FA?

1. Go to **Account > Settings > Security > Two-Factor Authentication**
2. Click **Add** next to Authenticator App
3. Verify with OTP sent to your phone
4. Scan the QR code with your authenticator app
5. Enter the generated code to confirm

***

## How do I change my phone number for 2FA?

1. Navigate to **Account > Settings > Security > Two-Factor Authentication**
2. Click the 3-dot menu next to Phone Verification
3. Select **Change Number**
4. Authenticate with your current method
5. Enter and verify the new number

***

## How do I set up Single Sign-On (SSO)?

1. Navigate to **Account > Settings > Security**
2. Click **Configure** in the Configure SSO widget
3. Select your identity provider
4. Follow the configuration guide

Contact [Plivo Support](https://support.plivo.com) to access SSO.

***

## What is IP Whitelisting?

IP Whitelisting restricts API access to specific IP addresses.

**To configure:**

1. Go to **Account > Settings > IP Whitelisting**
2. Click **+ Add CIDR Address**
3. Enter IP addresses in CIDR format (e.g., `192.0.2.0/24`, `1.1.1.1/32`)
4. Toggle the switch to enable

***

## What are the security best practices?

* Use a strong password (12+ characters with mixed case, numbers, symbols)
* Enable 2FA
* Use role-based access for team members
* Use individual email addresses
* Monitor account alerts
* Keep Auth Token private like a password
* Regularly rotate Auth Tokens
* Set up IP whitelisting

***

## What should I do if my account is compromised?

1. Check login notification emails from Plivo
2. Review payment receipts for unfamiliar charges
3. Check usage logs in the console
4. Immediately regenerate your Auth Token
5. Change your password
6. Review and remove unauthorized team members
7. Contact [Plivo Support](https://support.plivo.com)

***

## What are the team roles?

| Role                  | Access                                                            |
| --------------------- | ----------------------------------------------------------------- |
| **Owner**             | Full access (auto-assigned to account creator, cannot be changed) |
| **Admin**             | Same as owner — billing, credentials, configuration, logs         |
| **Developer**         | Application configuration, logs, API access (no billing)          |
| **Support**           | View logs and usage (read-only)                                   |
| **Financial Analyst** | Billing and payment access only                                   |

***

## How do I transfer account ownership?

Account ownership cannot be reassigned to a different team member. However, you can transfer access by updating the owner's email address:

1. Go to [Profile Details](https://cx.plivo.com/profile/details) in the Plivo console
2. Update the email address to the new owner's email
3. Complete the 2FA verification to confirm the change

The new email address holder will then have owner access to the account.

***

## How do I invite team members?

1. Go to **Settings > Account > Team**
2. Click **Add New User**
3. Enter the user's email address
4. Select the appropriate role
5. Click **Invite User**

***

## What are the benefits of subaccounts?

* Individual phone numbers and applications per subaccount
* Unique Auth ID and Auth Token for each
* Credits deducted from main account (no separate recharges)
* Single consolidated invoice
* Ability to whitelist unique sender IDs per subaccount

Billing is at the account level — subaccounts provide a usage breakdown split by main account and each subaccount, but there is no separate invoice per subaccount.

***

## How do I create a subaccount?

**Via Console:**

1. Navigate to subaccount management
2. Click **Create Subaccount**
3. Configure settings

**Via API:** Use the [Subaccount API](https://www.plivo.com/docs/account/api/subaccount/).

***

## What balance notifications does Plivo send?

Plivo automatically sends email alerts when your balance drops below $250, $100, and \$10.

**Configure custom alerts:**

1. Go to Payment Settings
2. Set up to 3 custom threshold amounts
3. Add additional notification email addresses

**Recommendation:** Set one alert equal to your average daily usage.

***

## Where do I find pricing information?

Access pricing by country through:

* **Voice:** Console > Voice > Pricing
* **SMS:** Console > Messaging > Pricing

***

## What is the inactive account policy?

Accounts with stored payment methods are vulnerable to takeover. Inactive accounts may be sold or misused. Accounts are reviewed for activity periodically.

To keep your account active, maintain regular usage or contact support.

***

## How do I create a support ticket?

1. Go to [Plivo Support](https://support.plivo.com)
2. Click **Create New Ticket**
3. Enter email, subject, and description
4. Select category and priority
5. Attach files if needed
6. Click **Create New Ticket**

Check ticket status anytime at **Check Ticket Status** on the support homepage.

***

## Related Resources

* [Payments](/docs/billing/payments)
* [Invoices](/docs/billing/invoices)
* [Subaccount API](https://www.plivo.com/docs/account/api/subaccount/)
* [Contact Support](https://support.plivo.com)
