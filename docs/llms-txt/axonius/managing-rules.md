# Source: https://docs.axonius.com/docs/managing-rules.md

# Managing Rules

Use the following procedures to manage rules in your system.

See [Permissions](/docs/permissions-list#identities) for what permissions are necessary to perform actions with rules.

## Creating a New Draft Version of a Rule

Create a new draft version of an existing rule when you want to modify the rule without affecting the currently active version.

**To create a new draft version of a rule:**

1. On the **Rules** page, find the rule you want.
2. Click **New Draft Version**. The **Create a New Rule** wizard is opened and populated with the parameters of the rule.
3. Make the parameter changes you want and do one of the following:
   * Click **Save as Active** to save the rule and activate it. The rule is added to the list on the Rules page with a state of 'Active' and is added to the Versions sub-tab of the Versions tab on the Asset Profile page. This version's details are shown on the rule's Asset Profile page. The previous version is set to 'Inactive'.
   * Click **Save as Inactive** to save the rule and leave it in the 'Inactive' state. This version becomes the current version of the rule but 'Inactive'. The previous version is set to 'Inactive'.
   * Click **Save as Draft** to save the new rule as a draft. The rule is listed on the Rules page with a state of 'Draft' and is added to the Draft Versions sub-tab of the Versions tab on the rule's Asset Profile page.
   * Click **Previous** to go back to the previous step to make changes.

## Duplicating a Rule

Duplicate a rule to create a new rule that is similar to an existing rule. Any rule in any state can be duplicated.

<Callout icon="📘" theme="info">
  Notes

  * When duplicating a rule from the **Version History** or **Draft Versions** lists, the new copy is added to that rule's Draft Versions list.
  * When a rule is duplicated from the **Rules** page, a *new* rule is created and added to the **Rules** list with a state of *Draft*. It is not a new version of the duplicated rule. It is a new rule with it's own versions and drafts.
</Callout>

**To duplicate a rule:**

1. From the **Rules** page, hover over the rule you want to duplicate.
2. Click the more menu and then **Duplicate**. The new copy is added to the rule's Draft Versions tab and it's details drawer is opened.
3. Edit the new rule.
4. Click **Save** and select whether to save the rule as a draft or as the *Active* version or as *Inactive*.

## Deactivating a Rule

You can deactivate a rule from the Rules page. When a rule is deactivated, any permissions granted by the rule when it was active are revoked. Only an active version of a rule can be deactivated. The deactivated rule is still listed on the Version History tab.

**To deactivate a rule:**

1. From the **Rules** page, hover over the rule you want to deactivate.
2. Click the more menu and then **Deactivate**. The rule is deactivated.

## Activating a Rule

You can activate a rule from the Rules page. When a rule is activated, all permissions granted by the rule are granted. If the rule was previously deactivated, all permissions are regranted. If the rule was a draft, it is added to the Version History tab and removed from the Drafts tab.

**To activate a rule:**

1. From the **Rules** page, hover over the rule you want to activate.
2. Click the more menu and then **Activate**. The rule is activated.

## Archiving a Rule

For the purposes of compliance, a rule that has been activated at any time is not deleted from the system. It is inactivated and moved into the archive to retain their full history. Archived rules can also be duplicated and those duplicates become a draft of a new rule and are listed on the Rules page. These are new rules and follow the work flow of all new rules.
Archived rules can be reactivated/restored later.

**To archive a rule:**

* In the **Rules** page, hover over the rule you want to archive, click the 3-dot menu and select **Archive**.

The rule is deactivated and moved to the **Archive** page.

## Deleting a Rule

Only draft rules that were never activated can be deleted. Rules that had a state of *Active* or *Inactive* at any time are archived, along with all their versions.

**To delete a rule:**

* Hover over the rule in the **Rules** list, click the 3-dot menu and select **Delete**.