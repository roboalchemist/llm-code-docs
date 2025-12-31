# Source: https://graphite-58cc94ce.mintlify.dev/docs/graphite-admin.md

# User permissions

> Learn how to manage users and billing information for your organization as a Graphite admin.

Team admins can manage billing, add or remove seats, and view or download invoices from *Settings* > [*Billing*](https://app.graphite.com/settings/billing). Team admins can also promote other members of the team to the admin role or restrict their access to read-only mode.

## Becoming a Graphite admin

* If you have admin or owner privileges in GitHub, you are automatically an admin for that organization in Graphite.

* If you create a team in Graphite, you become a Graphite admin for that team.

* If you enter payment details in Graphite, you become a Graphite admin for that team.

* If another Graphite admin promotes you to admin, you become an admin for the team.

<Note>
  Being a Graphite admin does not grant you additional privileges in GitHub.
</Note>

## Manage users

Graphite admins can manage Graphite users in their plan from *Settings* > [*Billing*](https://app.graphite.com/settings/billing) in the Graphite app.

* To add a member to your team, click `Invite your teammates`; once they accept the invitation, they will appear in your team membership list.

* Edit a team member's role by selecting either "Admin" or "Member" next to their name.

  * Graphite admins can make anyone in their organization a Graphite admin (even if they're not an owner in GitHub).

  * Graphite admins can change Graphite admins (who aren't GitHub owners) to "Member" status. This means GitHub owners are always Graphite admins (and this is immutable).

* To remove a member from your team, click the `...` icon next to their name and select `Remove from team`.

* To restrict a team member's access to read-only mode, click the `...` icon next to their name and select `Restrict access`. Admins can be in read-only mode and retain their admin privileges (e.g., manage billing info).

## Manage billing

Graphite subscriptions are managed through the Stripe billing portal, found at *Settings* > [*Billing*](https://app.graphite.com/settings/billing) > *Manage plan*. Anyone in your org can pay through the billing portal, and the person who manages Graphite payments for your org can update the previous payment method.
