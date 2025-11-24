# Source: https://docs.apify.com/platform/collaboration/organization-account/how-to-use.md

# Using the organization account

**Learn to use and manage your organization account using the Apify Console or API. View the organizations you are in and manage your memberships.**

***

Once an account becomes an organization, you can no longer log into it. Instead, you can switch into the organization from one of its member accounts to manage account information, memberships, and Actor runs.

While you can't manage an organization account via https://docs.apify.com/api/v2.md, you can still manage its runs and resources via API like you would with any other account.

**https://www.youtube.com/watch?v=BIL6HqtnvKk on organization accounts.**

## In the Apify Console

You can switch into **Organization account** view using the account button in the top-left corner.

![Switch to organization account](/assets/images/switch-to-organization-bc78bf615e803f6a5521c31f86bb66f0.png)

In the menu, the account you are currently using is displayed at the top, with all the accounts you can switch to displayed below. When you need to get back to your personal account, you can just switch right back to it—no need to log in and out.

The resources you can access and account details you can edit will depend on your https://docs.apify.com/platform/collaboration/list-of-permissions.md in the organization.

> When switching between accounts, beware which account you start an Actor run in. If you accidentally start an organization's Actor run in your personal account, the run will be billed to your account (and vice versa).

### Manage your organizations

You can view and manage the organizations you are a member of from the **Organizations** tab on your https://console.apify.com/account#/myorganization.

If you want to leave an organization you own, you must first transfer ownership to someone else.

![My organizations](/assets/images/my-organizations-0b632703aa9f336c2de4beb03e228888.png)

### Transfer ownership

The organization, its Actors, and its integrations will keep running as they are. The original owner will either leave the organization or become a member with permissions defined by the new owner. Only the new owner will have complete access to the organization.

## Via API

While you cannot manage an organization account's settings and members via API, you can access its Actor and task runs, webhooks, schedules, and storages just as you would with any other account.

As a member of an organization, you are assigned an https://docs.apify.com/platform/integrations.md (under the **Integrations** tab) and proxy password (click the **Proxy** button in the left menu) for accessing the Apify platform via REST API.

![Integration tokens](/assets/images/integrations-4dfa366351c8338af2f1f909b138a5a3.png)

The API tokens' functionality reflects your account's permissions in the organization, so if you only have the **read** and **run** permissions for Actors, you will only be able to view and run Actors via API. Only you can view your API token and password.

> Do not share your API token or password with untrusted parties.

If you have the **manage organization access keys** permission, you are able to view and use organization-wide API tokens. These are shared across the organization, so everyone with the **manage organization access keys** permission can use them for organization-wide integrations.

For a https://docs.apify.com/api/v2.md and help on using them, visit the API.
