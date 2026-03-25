# Source: https://docs.axonius.com/docs/rule-versions.md

# Rule Versions

Rule versions ensure that all changes made to a rule are stored. Versioning allows the system to track changes made to each specific rule. Each time a rule is modified, a new version is created and the one who made the changes logged. This is essential for understanding how rules evolve over time and who made those changes. Versions also allow for the rollback of a rule that was activated, as well as for change management and compliance audits.

Versioning for internal rules are managed within Axonius. Versioning for external rules are managed by the respective application.

**To access a rule's versions:**

1. From the **Rules** page, select a rule.
2. Click the **Versions** tab.  There are two sub-tabs, "Version History" and "Draft Versions".
   ![RuleVersionsTab.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RuleVersionsTab.png)

## Version History Tab

The Version History tab lists all versions of a rule that have had a state of "active" or "inactive" at any time. Version numbers start at 0 (zero). All rule versions are preserved and cannot be deleted. When a draft version of a rule is saved with a state of active or inactive, it is removed from the Draft Versions tab and added to the Version History tab with the properly incremented version number.

![RuleVersionHistoryTab.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RuleVersionHistoryTab.png)

The Version History tab provides the following information about each version:

* **Version** - The version number. Version numbers start at 0 (zero).
* **Rule** - The name of the rule.
* **Description** - A short description of the rule.
* **Adapter connections** - Icons for all the adapter connections related to the rule.
* **Criteria raw query** - The AQL query that defines the assets to which the rule applies.
* **Fetch time** - The time stamp of the last fetch for the related query.

## Draft Versions Tab

The Draft Versions tab lists all rule drafts. A draft is a version of a rule that has never been set to an active or inactive state. When you create a new draft of an active rule from the Rules page, a new draft appears on the Draft Versions tab.

![DraftVersionTab.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DraftVersionTab.png)

The Draft version tab provides the following information about each version:

* **Name** - The name of the draft rule.
* **Description** - A short description of the rule.
* **Fetch time** - The time stamp of the last fetch for the related query.

To edit a draft rule, select one from the list.
When a new rule is created, an internal rule within Axonius, if it is saved as a Draft version,