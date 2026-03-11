# Source: https://docs.axonius.com/docs/editing-rules.md

# Editing Rules

See [Permissions](/docs/permissions-list#identities) for what permissions are necessary to perform actions with rules.

### Editing Active Rules

When the Active version of a rule is edited, the current version remains active and a new draft version is created.

**To edit a Rule with a state of *Active*:**

1. From the **Rules** table, select the rule you want to edit.
2. In the Rule profile page, click **Update Rule**. A new version of the active rule is created and a new draft is added to the **Draft Versions** tab.
3. In the Rule wizard, make the changes you want.
4. Click **Simulate** to display a graph of the results of the rule's current configuration.
5. Click **Save** to save and activate it.
6. The edited rule becomes the active version of this rule and is displayed in the rule's Profile page. The previously active version is assigned a state of *Inactive*.

### Editing Draft Version Rules

**To edit a Rule with a state of *Draft*:**

1. From the **Versions** tab, hover on the rule you want to edit and click **Edit**.
2. In the Rule wizard, make the changes you want.
3. Click **Simulate** to display a graph of the results of the rule's current configuration.
4. Click **Save** to save and activate it.
5. The edited rule becomes the active version of this rule and is displayed in the rule's Profile page. The previously active version is assigned a state of *Inactive*.

### Editing Rules and Working with Draft Rules

A rule must be in **Draft** mode to edit it.

* Click **Update Draft** to save changes to the rule and save them in the draft version.

* Click **Delete Set** to remove a complete connection and all the configured entitlements. Click **X** (visible on hover) next to a specific entitlement to remove just that specific entitlement.

**Impact**- number of users fit the rule / number of users in the permission account
**Marginal impact**- number of users fit only that specific rule (and no other rule that gives that same permission) / number of users in the permission account
**Precision**- Number of users that fit the rule and has the permission / Number of users who fit the rule