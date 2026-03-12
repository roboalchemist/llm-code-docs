# Source: https://documentation.onesignal.com/docs/en/apps-organizations.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Apps, Organizations, & Accounts

> Learn how to add, rename, move, and delete OneSignal Apps and Organizations, and understand the relationship between accounts, apps, and organizations.

When you sign up at [OneSignal.com](https://onesignal.com), a user account is created and tied to your email address. With your account, you can create, manage, or be invited to multiple **Apps** and **Organizations**.

<Note>
  If your company already has a OneSignal App or Organization, email the account admin to request an invite. Share the [Manage Team Members](./manage-team-members) guide to help them give you access faster 😉.
</Note>

***

## OneSignal account structure

Your email address is used to log in to your OneSignal account. From there, you can access the **Apps** and **Organizations** in which you are a [Team Member](./manage-team-members).

### Apps vs. Organizations

* A **OneSignal App** holds user and messaging data for a single project, across all platforms (web, iOS, Android, email, etc.). Each app exists within a single Organization.
* A **OneSignal Organization** is a container for managing multiple apps, billing, and team permissions.

You can have:

* Unlimited apps (free to create)
* Multiple organizations (free or paid)
* Apps for separate environments (e.g., dev, staging, production)
* Different access levels per app or organization

***

## Access levels and roles

OneSignal supports two levels of access:

### App-level access

* Access to only the specific app(s) a user is invited to.
* Cannot view billing or upgrade plan settings.

### Organization-level access

* Access to all apps within the organization.
* Only **Admin** roles can manage billing and upgrades.

### User roles

Access can be further scoped by roles:

| Role   | Description                                                         |
| ------ | ------------------------------------------------------------------- |
| Admin  | Full access, including settings, billing, and user management.      |
| Editor | Can create and send messages but cannot manage settings or billing. |
| Viewer | Read-only access for analyzing performance and message stats.       |

For more details, see [Manage Team Members](./manage-team-members).

***

## Managing your user account

We highly recommend enabling [two-factor authentication](./2-step-authentication). This adds an extra layer of security to your account. See [Data collection & security FAQ](./data-questions) for additional details.

### Reset password or email

1. Navigate to [Account Management](https://dashboard.onesignal.com/profile) or click **your email drop-down > Manage Account**.
2. Add your Email, New Password, and Confirm Password.
3. Click **Submit**.

<Frame caption="Reset account password">
  <img src="https://mintcdn.com/onesignal/W0DIQbUDatcgdZf6/images/dashboard/dashboard-managing-your-user-account.jpg?fit=max&auto=format&n=W0DIQbUDatcgdZf6&q=85&s=0a0c699abf3af0f6fc36f3fab0f4b1a9" width="2722" height="1223" data-path="images/dashboard/dashboard-managing-your-user-account.jpg" />
</Frame>

### Delete your account

<Warning>
  Deleting your user account only removes your email from OneSignal. It does not delete apps or downgrade paid plans. Be sure to [Downgrade your plan](./billing-faq) if needed.
</Warning>

To delete:

1. Navigate to [Account Management](https://dashboard.onesignal.com/profile) or click **your email drop-down > Manage Account**.
2. Scroll down to **Delete Account**
3. If you don't have the option to delete your account, contact `ar@onesignal.com`.

***

## Manage apps

* **Create an app**:
  * Log in at onesignal.com and click **New App/Website**.
  * Or use the [Create an App API](/reference/create-an-app)

* **Rename an app**:
  * From the dashboard **All Apps** page, click **Options > Rename** next to the app.
  * Or use the [Update an App API](/reference/update-an-app)

* **Find App ID**:
  * See [Keys & IDs](./keys-and-ids).

* **Delete an app**:
  * You can delete apps within Free organizations and under 5,000 total subscriptions from the **All Apps** page via **Options > Delete**.
  * For larger apps, contact `support@onesignal.com`.

***

## Manage organizations

We highly recommend enabling [two-factor authentication](./2-step-authentication) at the Organization level to force all team members to use 2FA. This adds an extra layer of security to your Organization. See [Data collection & security FAQ](./data-questions) for additional details.

* **Create an organization**:
  * Visit the **Organizations** page or click **New Organization** in the dashboard (no paid plan required to create).
  * Or use the [Create an App API](/reference/create-an-app)

* **Rename an organization**:
  * In **Organizations**, click **Options > Rename** next to the org.

* **Find Org ID**:
  * It's the UUID in the URL when selecting your organization. Example: `https://dashboard.onesignal.com/organizations/THE_ORG_ID/apps`

* **Delete an organization**:
  * Go to **Organizations**, click **Options > Remove**.
  * You must move the apps out of the organization before deleting it.
  * If you need assistance, contact `support@onesignal.com` with the Org ID you want to delete.

### Add or move apps between organizations

* **Add app to organization**:
  * Go to **Organizations > select your Organization > Move Apps Into Organization**.
  * Select your apps and click **Move Apps**.
  * You need:
    * Admin access to the Organization
    * Admin access to the App
    * The apps to be in a Free Organization.

<Note>
  If you need assistance, email `support@onesignal.com` with:

* The App ID(s) you want to move
* The Org ID to move them to.
* You must contact Support from an email with Admin access to the Apps and Organization.
</Note>

***

## FAQ

### Where can I see when my app was created?

Use the [View App](/reference/view-an-app) or [View Apps](/reference/view-apps) API to get the `created_at` timestamp.

### Why do I see limitations on a paid plan?

Your app might not be assigned to the correct paid Organization. Follow [Add or move apps between organizations](#add-or-move-apps-between-organizations) to add your app to the paid org.

If you need assistance, email `support@onesignal.com` with:

* The App ID(s) you want to move
* The Org ID to move them to.
* You must contact Support from an email with Admin access to the Apps and Organization.

### What are the best practices for agencies?

Agencies can manage client apps using one of two approaches:

1. **Centralized billing**
   Use a single Organization to manage and pay for all client apps.
2. **Client-managed billing**
   Each client sets up their own Organization and handles their own billing.

You can mix paid and free apps by assigning them to the appropriate Organization.

Need help? [Contact our Sales Team](https://onesignal.com/contact).

### How can we access analytics, messages, and users across multiple Apps?

OneSignal does not have a single cross-app dashboard view. Each app's data is accessed separately. Here are the recommended approaches for working across apps:

* **Analytics** — Use [Event Streams](./event-streams) to route message delivery and engagement data from each app to a centralized analytics platform like Snowflake, BigQuery, or Amplitude.
* **Messaging** — Use the [Create message API](/reference/create-message) to send messages to multiple apps in parallel from your backend. You can also create [Templates](./templates) once and copy them across apps using the [Copy template API](/reference/copy-template-to-another-app).
* **Users** — Use the [REST API](/reference/view-user) to query user data per app. If you need a unified view of users across apps, export user data via [CSV export](/reference/csv-export) or stream it via Event Streams to an external data warehouse.

### How do we change our dashboard timezone?

The OneSignal dashboard graphs are in UTC. This cannot be changed at this time. All other dates and times are in the timezone of your browser. To change the timezone, you need to change the timezone of the browser you are using to access the dashboard.

***

Built with [Mintlify](https://mintlify.com).
