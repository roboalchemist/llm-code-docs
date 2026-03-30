# Source: https://docs.axonius.com/docs/creating-a-rule.md

# Creating a Rule

You can create new rules to fit the needs of your environment. See [Managing Rules](/docs/managing-rules) for more actions you can perform.

See [Permissions](/docs/permissions-list#identities) for what permissions are necessary to perform actions with rules.

**To create a rule:**

1. At the top right, click **+ Add New Rule**. The **Create a rule** wizard opens. Click **Previous** or **Next** to move through the wizard steps. Click **Close** to close the wizard without creating a rule.

2. In the **Enforcer** section, select the entity responsible for enforcing the rule and click **Next**. There can only be one enforcer for a rule.

<Image align="center" alt="IDM-CreateRuleEnforcerSection.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDM-CreateRuleEnforcerSection.png" />

3. In the **Query & Entitlements** section, there are two sections: **Query** and **Entitlements**.

<Image align="center" alt="Identies - Create Rule" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDM-CreateRule.png" />

4. Under **Query**, select **Automatic access revocation** to automatically revoke access provided by this rule when the identity no longer matches the parameters of the query. See [Using Automatic Revocation and Guardrails](/docs/using-auto-revocation-and-guardrails) for more about how automatic revocation and guardrails work.
5. Next, configure the query to select the user base to which to apply the rule and the entitlements to grant them. You can configure multiple queries. Scroll to the right to reveal the line tools. See [Creating Queries with the Query Wizard](/docs/query-wizard-and-query-filter) for more about using the Query Wizard.

<Image align="center" alt="Identities = Create Rule - Query Section" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDM-CreateRuleQuerySection.png" />

5. Under **Entitlements**, configure the entitlements to grant the users.

   1. Click **Add Account** and select an identity provider account. Each account is associated with a specific adapter connection. Different accounts from the same identity provider may list different entitlements.

   <Image align="center" alt="Identities - Create Rule - Accounts List" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDM-CreateRuleAccountsList.png" />

   2. Click **Add Entitlements** and select entitlements from the list. You can search for entitlements in the Search bar at the top of the list.

   <Image align="center" alt="Identities - Create Rule - Select Entitlements" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDM-CreateRuleEntitlementsList.png" />

   6. Click the expand icon to view the selected entitlements.

<Image align="center" alt="Identities - Entitlements List - Expand" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDM-CreateRuleEntitlementsListExpand.png" />

7. Click **Next**.
8. In the **Rule Details** section, enter a name in **Rule Name** and in **Description**, describe what the rule does.
9. When an already existing rule is being edited, the changes made to the rule are described under **Rule Changes**. The number of users added and/or removed to or from the rule is displayed and the added or removed entitlements are also listed. See [Editing Rules](/docs/editing-rules).

<Image align="center" alt="CreateRule-RuleDetails-new.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateRule-RuleDetails-new.png" />

10. Do one of the following:
    * Click **Save as Active** to save the rule and activate it. The rule is added to the list on the Rules page with a state of *Active* and is added to the Versions sub-tab of the Versions tab on the Asset Profile page. This version's details are shown on the rule's Asset Profile page.
    * Click **Save as Inactive** to save the rule and leave it in the *Inactive* state.
    * Click **Save as Draft** to save the new rule as a draft. The rule is listed on the Rules page with a state of *Draft* and is added to the Draft Versions sub-tab of the Versions tab on the rule's Asset Profile page.
    * Click **Previous** to go back to the previous step to make changes.

**Activating a Draft Rule**
When a draft is activated, it is removed from the Draft list and added to the version's Version History and the rule profile now shows this version's details. It is removed from the Draft Versions sub-tab of the rules Version tab on the Asset Profile page.