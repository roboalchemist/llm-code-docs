Source: https://docs.slack.dev/tools/developer-sandboxes

# Developer sandboxes

A developer sandbox is an Enterprise org environment (a network of two or more Slack workspace instances) that can be used to build against all Slack features safely and securely, without an additional cost. The ability to provision sandboxes is a benefit offered by the [Slack Developer Program](https://api.slack.com/developer-program).

Slack developer sandboxes are enterprise-ready with the controls you need to:

* Secure developer environments
* Maintain compliance and data boundaries
* Empower teams to build without putting production at risk
* Scale access with streamlined management

## Sandbox features {#sandbox-features}

Developer sandboxes are built with the following enterprise-grade features, enabling organizations to innovate safely.

### Security {#security}

#### Email + magic code authentication {#email--magic-code-authentication}

Users log in to sandbox workspaces using a time-limited, single-use code (PIN) sent to their verified work email. This provides a streamlined, yet secure alternative to configuring SSO for each sandbox.

This login experience is passwordless, fast to deploy, and bound to your corporate identity (e.g., @yourcompany.com). It offers strong brute-force protections (e.g., short TTL, single-use, exponential throttling) without a need for setting up SSO or IdP per workspace.

#### Configurable session timeouts {#configurable-session-timeouts}

Admins can define how long users stay logged into sandbox workspaces, enabling shorter, more secure session durations compared to production workspaces.

### User access controls {#user-access-controls}

User access controls include:

* **Email domain restrictions**: Define who can join your sandboxes with domain-based allow lists. For example, only `@yourcompany.com` users can be added, and no external emails are allowed.
* **Fixed identity model**: Users cannot change their email address inside the sandbox. Their identity stays tied to your organization, reducing risk and keeping access aligned with your policies.
* **Guest access control**: Block or limit guest users in developer sandboxes to maintain a secure internal environment.

### Slack Connect on your terms {#slack-connect-on-your-terms}

Restrict Slack Connect to your organization by limiting sandboxes to only connect with other sandbox workspaces within your company, ensuring no production workspace sharing and no external leakage.

Admins can choose to optionally enable org-wide collaboration to allow Slack Connect across all sandboxes under your organization.

### Enterprise policy enforcement {#enterprise-policy-enforcement}

Sandboxes inherit your baseline settings from the parent Enterprise organization, automatically.

Apply restrictions to:

* Admin and audit scopes
* High-sensitivity APIs
* Third-party apps from the Slack Marketplace

These controls cannot be overridden by sandbox owners, ensuring consistent governance.

### Streamlined provisioning {#streamlined-provisioning}

Eliminate manual reviews. Admins can configure default resolution rules (e.g., auto-approve or auto-deny) for incoming sandbox requests, reducing friction and saving time.

Ready to join? Let's get you set up!

* * *

## Signing up for a developer account {#sign-up}

1. Navigate to the [Slack Developer Program](https://api.slack.com/developer-program) page. Click **Join the Program**.
2. Fill out the registration form and click **Submit**.
3. You'll receive an email confirmation to activate your account. Click **Activate Developer Account** from the email; you'll then be directed to the Dashboard page.

Observe the welcome screen — you'll also receive a welcome email. Welcome to the Slack Developer Program! 🎉

Once your account is created and you're logged in, you'll be able to access your developer [Dashboard](https://api.slack.com/developer-program/dashboard). This dashboard features the latest development-related happenings at Slack, and is updated regularly.

* * *

## Provisioning a sandbox {#provision}

To provision a sandbox, navigate to **Sandboxes** and click **Provision Sandbox**.

If you are not a member of a paid plan (the paid plan workspace must have been created at least 30 days ago, unless you're in an Enterprise organization), you'll be prompted to provide a payment method, but note that you will not be charged.

Enter the details for your sandbox. You'll be able to choose whether you want an empty sandbox (1 workspace and 1 demo user) or whether you want to load a Slack template to your sandbox, which contains 1 workspace, 7 system-created fake users, 7 channels, and system-created threads, replies, and reactions to threads/replies.

Click **Provision Sandbox** again, then click **Manage Sandboxes** on the next modal. Once created, your provisioned sandbox will appear on the [Sandboxes](https://api.slack.com/developer-program/sandboxes) page.

To access your new sandbox, click its name and log in with your email address and the password you just created. Once you complete verification, the Sandboxes page will show a workspace with the same name as your sandbox.

Your sandbox has been provisioned successfully. Happy building! 🏖️

### Sandbox statuses {#statuses}

A sandbox can have one of the following statuses:

* **Active**: Active sandboxes have a default lifespan of six months. As long as you are still eligible to provision sandboxes, you can extend the lifespan of the active sandbox to another six months, every six months.
* **Archived**: Once a sandbox reaches the end of its lifespan, it will be automatically archived. Once archived, all users (including you as the admin and owner of the sandbox) will no longer be able to access it.
  * You will receive an email reminding you that your sandbox will be archived 30 days before the sandbox reaches the end of its lifespan.
  * All data will be retained for a three month grace period after the sandbox is archived, except for messages and files based on the [limits](#limits) below. Workflows cannot be executed once the sandbox is archived, including scheduled and webhook workflows.
  * During the grace period, you can choose to unarchive the sandbox; however, the rest of the users in the sandbox must be reactivated via the sandbox Enterprise Management panel.
  * If you lose your eligibility, your sandboxes will be automatically archived within 30 days. If you regain eligibility, you can extend the lifespan of the sandbox.
  * After the grace period, the sandbox will be automatically deleted.
* **Deleted**: Once you delete a sandbox, all data including messages, files, workflows, and users will be irretrievable.

### Sandbox limits {#limits}

Sandboxes have the following limits:

* **Organization creation/count limits**:
  * You can provision up to 10 sandboxes over the course of 30 days.
  * You can have up to two active sandboxes at any given time.
  * A sandbox is active for six months, by default.
* **Workspace creation/count limits**:
  * A sandbox can contain up to three full-featured workspaces. There are no limits on the number of total workspace creations.
* **User limits**:
  * Max eight users per sandbox. This includes owners and admins, but excludes bots and apps.
  * Max two guests per sandbox (single-channel or multi-channel).
  * Max three Slack Connect teams per sandbox. Slack Connect is only allowed between sandboxes.
* **Message and file limits**:
  * The same message and file policies and restrictions are in place as that of a [Free plan](https://app.slack.com/plans).
* **Automations limits**:
  * Each sandbox workspace can have up to 20 integrations (app integrations and published workflows). The maximum is 60 integrations per sandbox.
  * Run-On Slack Infrastructure (ROSI) is available with no additional limits.
  * 10,000 write and 40,000 read limit per sandbox per datastore per day.
  * Cannot be used to distribute third-party apps and workflows.
* **Other limits**:
  * Discovery API enablement is not available on sandboxes unless you are part of our [partner program](https://slack.com/partners).

* * *

## Managing your sandboxes {#manage-sandboxes}

On the [Sandboxes](https://api.slack.com/developer-program/sandboxes) page, click the kebab menu to the right of that sandbox in the Active Sandboxes section and either:

* extend its archive date, or
* delete it.

### Managing events and settings {#events-settings}

On the [Events](https://api.slack.com/developer-program/events) page, you can view, filter, and search for upcoming events.

On the [Settings](https://api.slack.com/developer-program/settings/profile) page, you can:

* update your personal information, or
* update your developer newsletter subscription preferences.

Click **Save profile** to save your changes.

* * *

## FAQs {#faqs}

### What is a developer sandbox? {#sandboxes-what}

As part of the [Slack Developer Program](https://api.slack.com/developer-program), you'll get access to an Enterprise organization sandbox that allows you to explore all features, including automations. You'll also get early access to betas, and can develop and test apps and workflows in a dedicated, fully-featured development environment.

### How are developer sandboxes intended to be used? {#sandboxes-use}

Developer sandboxes are intended to be used for development and application testing purposes.

### Who can sign up for a Slack Developer Program account, and what costs are associated with membership? {#dev-account}

Anyone can sign up for an account, and there are no costs associated with being a member of the Slack Developer Program. [Sign up](https://api.slack.com/developer-program/join) today!

### Who can create a developer sandbox? {#sandboxes-who}

Any developer enrolled in the Slack Developer Program can provision or delete a developer sandbox. However, in order to provision a sandbox, you must either be on a paid plan already, or you must provide a valid payment method for the account.

### Are developer sandboxes available to developers without a paid plan? Why is a payment method required for provisioning? {#payment}

Yes. The payment method is used for identity verification purposes only; you will not be charged.

### How do Enterprise sandboxes work? {#enterprise-sandboxes}

If you belong to an Enterprise organization and your Org Admin has enabled **Allow developer sandboxes > Require approval for sandbox provisioning** within your organization's settings, you'll need to make a request before you can provision a sandbox.

The steps for provisioning a sandbox will remain much the same, except that you can enter an optional reason for your request. After you click **Request Access**, your request will be submitted to your Org Admin.

Your Org Admin will review your request and, if approved, you'll receive a Slackbot notification that you can go ahead and provision your sandbox. If they deny your request or they have disabled sandbox provisioning for your organization, you'll see the relevant message displayed on both your Dashboard and Sandboxes pages.

Your Org Admin also has the ability to manage the sandbox you create.

They can choose to archive it, extend its archive date, or delete it. You'll receive Slackbot notifications when any of these actions are taken.

#### Developer sandboxes for Enterprise admins {#developer-sandboxes-for-enterprise-admins}

If you are an Org Admin, once a developer within your organization submits a request to create a sandbox, you will receive a Slackbot notification to approve or deny the request. You may also configure default actions for incoming sandbox requests rather than having to review and manage requests one by one.

In addition, you can restrict who can join developer sandboxes with an allowlist of email domains (e.g., only users with a `<your-company>.com` email address will be allowed to join a sandbox). You can also restrict Slack Connect channels in a sandbox to sandboxes only owned by your organization, or allow sandboxes to connect to your organization via Slack Connect.

For additional security for sandboxes owned by your organization, you can toggle on the **Enable password-free authentication** setting. However, if the sandboxes already have SSO configured, please contact the Customer Experience team at Slack to remove this configuration first; otherwise password-free authentication will not work properly.

### What features and limitations are applicable to developer sandboxes? {#sandboxes-limits}

Developer sandboxes are Enterprise org environments and offer the same features included with all [Enterprise plans](https://app.slack.com/plans/), but with limitations imposed upon those features. Refer to [sandbox limits](#limits) for more details.

### Do developer sandboxes have access to the information, data, or settings in my parent enterprise or in workspaces under the same domain? {#sandboxes-access}

No. Each developer sandbox is distinct and has no connection to any other workspace that shares a common domain name.

### How many sandboxes can I create and how long do they last? {#sandboxes-status}

You can provision up to 10 sandboxes over the course of 30 days, and you can have up to two active sandboxes at any given time. Sandboxes are active for six months by default. Refer to [sandbox limits](#limits) for more details. As long as you are still eligible to provision sandboxes, you can extend the lifespan of the active sandbox to another six months, every six months. Refer to [sandbox statuses](#statuses) for more details.
