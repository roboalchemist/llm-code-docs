# Source: https://docs.axonius.com/docs/rules-page.md

# Rules Page

Use the **Rules** page to manage rules in the system. Admins can control rule usage and create, manage, and enforce them.

Rules provide a set of consistent and manageable entitlements to users.

**To access the Rules page in the Identities workspace:**

1. In the **Identity** workspace, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDMWorkspaceRulesNavIcon.png) (Rules) on the left navigation panel. .

**To access the Rules page from the Platform workspace:**

1. In the **Platform** workspace, open the **Assets** page by clicking the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetsPageIcon.png) (Assets) on the left navigation panel.
2. In the **Assets** list on the left, scroll down to the **Identities** section and click **Rules**.

<Image alt="RulesPage.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RulesPage(1).png" />

The **Rules** page shows all rules in the system.

* Click a rule to see the [Asset Profile](/docs/asset-profile-page) page for that rule.

The following information is shown on the Rules page:

* **Adapter Connections** - Displays the icons of the adapter connections used by this rule.
* **Name** - The name of the rule.
* **Display Name** - The name displayed.
* **Rule State** - The current state of the rule: Draft, Active,
* **Draft Asset** -
* **Enforcer** - Indicates whether the enforcer of the rule is Axonius or the 3rd-party application.
* **Criteria Raw Query** -
* **Tags** - A list of tags applied to the rule.

**Rules can originate from one of these sources:**

* **External fulfillment rules** - Rules created in a third-party application, most likely an Identity Provider such as Okta or other IAM products. These rules are imported into Axonius which provides a centralized place where you can review all rules that provide access to users and the ability to manage them. And access management is crucial for IAM teams.

* **Suggested rules** - Using advanced AI and machine learning Axonius suggests rules once a day by Axonius from analyzing the structure and behavior of your organization regarding the various identities, organization associations, and entitlement assignments. The suggested rules are fed by and generate the External fulfillment rules. Suggested rules can be activated as is, duplicated and then edited, or deleted and are automatically added to the Rules list with a status of *Suggested*.

* **Axonius rules** - Axonius rules are different from rules created by identity providers and usually associate users to specific groups or roles where the groups and roles are assigned the permissions. Axonius Rules provide administrators with a way to design fine-grained entitlements including groups and role associations, resources, and permissions. This way the administrators do not have to create and manage groups and roles. The wide range of integration that Axonius has with various applications gives Axonius the ability to assign entitlements directly to the applications. This is done through the Axonius Rules where Axonius is the fulfiller. Also, with this type of rule, Axonius is the authority that assigns the permissions, unlike external fulfillment rules in which the target external system responsible for assigning the permissions.

For more about creating a rule, see [Creating a Rule](/docs/creating-a-rule).
For more about editing rules, see [Editing Rules](https://docs.axonius.com/axonius-help-docs/docs/editing-rules).

## Rule States

Rules can have one of the following states:

* **Draft** - Rules that have never been activated. Rules in draft status are either new rules or a suggested rule when being edited.
* **Active** - A rule that is currently active and being enforced.
* **Inactive** - A rule that was once active and is now deactivated.

### Viewing Rule Versions

All versions of a rule are listed on the **Versions** tab of the rule's [Asset Profile](/docs/asset-profile-page) page. The Versions tab has two sub-tabs:

* **Versions History** - Lists all versions of the rule that are or have been active at any time.
* **Drafted Versions** - Lists all versions of the rule that have never been activated. An edited, never been activated version (a draft) of an active rule is listed here.

See [Rule Versions](/docs/rule-versions) to learn more.