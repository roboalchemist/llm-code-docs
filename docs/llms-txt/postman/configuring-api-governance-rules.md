# Configure API Governance rules in Postman

> Configurable governance rules are available with [Postman Enterprise plans](https://www.postman.com/pricing/). If you don’t have an Enterprise account, you’ll be able to see the API Governance page, but you won’t be able to add new rules.

You can configure the API Governance rules that Postman applies to your [API specifications](/docs/api-governance/api-definition/api-definition-warnings/) in the Postman API Builder and Spec Hub. Follow API Governance rules at the beginning of the [API lifecycle](https://www.postman.com/api-platform/api-lifecycle/) to keep your APIs consistent without requiring more work later.

Super Admins and API Governance Managers can configure rules and turn them on and off for public workspaces and internal workspaces everyone in your team can access. See [Define roles and permissions within a Postman team](/docs/administration/roles-and-permissions/#team-roles) for more information.

You can [create](#add-custom-rules) and [edit](#edit-custom-rules) your own custom rules to evaluate your team’s APIs. You can also [import existing rules](#add-rules-to-your-api-governance-configuration) into your team’s rule library. Then [create a workspace group](#turn-configured-rules-on-and-off) with the workspaces and rules you’d like Postman to apply to your APIs.

![Image 1: API governance dashboard](https://assets.postman.com/postman-docs/v11/api-governance-dashboard-v11.jpg)

To access the configurable API Governance rules, do the following:

1. Go to the [Postman home screen](https://go.postman.co/).
2. Click **API Governance** in the team information pane.

## Add custom rules

You can create new custom rules that Postman can use to evaluate your API specifications in the API Builder or Spec Hub. Postman provides you with a boilerplate rule to help you start writing your custom rules. You can also use snippets of commonly used property-value pairs to help you write your custom rules.

To add a custom rule, do the following:

1. Go to the [Postman home screen](https://go.postman.co/), and then click **API Governance** in the team information pane.
1. Click **Create Rule**.
1. Define the rule in the editor. It must adhere to [custom Spectral rule guidelines](/docs/api-governance/configurable-rules/spectral/).

    You can use a curated list of commonly used property-value pair snippets to write your rules. Snippets are available in the right pane of the editor. Selecting a snippet adds the property-value pair automatically to your rule, helping you get started with writing rules. Once added to your rule, you can edit the snippets to meet your specific requirements.

    > Postman will prompt you with suggestions as you enter text. Select one to autocomplete your rule.

1. The rule must be valid YAML or JSON. Use the dropdown list to choose the correct syntax.
1. Click **Create**.

    ![Image 2: Create a custom API Security rule](https://assets.postman.com/postman-docs/v11/api-governance-create-new-custom-rule-v11-40.jpg)

1. Find your new rule under **Custom Rules** and [turn it on](#turn-configured-rules-on-and-off).

You can also click **Upload file(s)** to upload a new rule in valid YAML or JSON format.

> You can't create a custom rule that duplicates an existing rule.

> You can write and add custom functions to your custom governance rules that Postman applies to your API specifications. For more information, see [Create custom governance functions in Postman](/docs/api-governance/configurable-rules/configuring-custom-governance-functions/).

## Edit custom rules

You can edit custom governance rules you created earlier.

To edit a custom rule, do the following:

1. Select the **Rule Library** tab, and then select the **Rules** tab.
1. Under **Created by your team**, select the name of the custom rule you’d like to edit.

    ![Image 3: Create a custom API Governance rule](https://assets.postman.com/postman-docs/v10/edit-custom-governance-rule-v10.jpg)

1. Edit the custom rule, and then click **Save**.

You can also click **Delete** to delete the custom rule. Then click **Delete** to confirm.

If you delete a custom rule, and you want to add it back into Postman, you must click **Create Rule** to create the rule again.

## Add rules to your API Governance configuration

In addition to the rules turned on by default in Postman, you can add other rules to your team's rule library from the rule library. You can also create your own custom rules.

### Import rules from the rule library

The rule library has Postman's API governance guidelines, Zalando's RESTful API and event guidelines, and Postman's OWASP API guidelines.

1. Select the **Rule Library** tab, and then select the **Rules** tab.
1. Click **Import** to open the rule library.
1. Click **Import** next to a rule to import it. Details and API format requirements are available under the rule name.

    > You can click **View all** below a set of guidelines to view all of its rules. To import all rules for a particular set of guidelines, click **Import All**.

    ![Image 4: Import API Governance rule from Postman library](https://assets.postman.com/postman-docs/import-postman-rule-from-rule-library-10.12.0.jpg)

1. Once you import new rules from the library, add the rules to a workspace group to [turn them on](#turn-configured-rules-on-and-off) for the workspaces in the group.

## Turn configured rules on and off

To meet your team's development needs, you can turn individual governance rules on or off for public workspaces and internal workspaces everyone in your team can access. To do so, select the **Workspace Groups** tab. You can create a new group of workspaces to apply individual governance rules to by clicking **Create Group**, or you can select an existing group to update its governance configuration. To apply individual governance rules to all workspaces, select the default **All workspaces** group.

To turn a governance rule on or off for a workspace group, select an existing group, and then click **Edit**. To turn a governance rule on, select the checkbox next to the rule name. To turn a governance rule off, clear the checkbox next to the rule name.

![Image 5: Turn individual rules on and off](https://assets.postman.com/postman-docs/api-governance-turn-rules-on-off-10.12.0.jpg)

Once you've made the desired changes, click **Review Changes**, then **Apply Changes** to save them. Your team will only see violations for the governance rules that have been explicitly applied to the workspace the API resides in.

You can view detailed metrics on API Governance rule compliance in your specifications. Learn how to view metrics for specifications in [Spec Hub](/docs/reports/api-governance-specifications-reports/) and [the Postman API Builder](/docs/reports/api-builder-reports/).

## Remove rules from your API Governance configuration

To remove an API Governance rule, locate the rule in your team's rule library and click ![Image 6: Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke-small.svg#icon) **Remove** next to its name. You can later choose to [re-import it from the rule library](#import-rules-from-the-rule-library).

If you remove a custom rule, you'll need to add it back into Postman using [**Create Rule**](#add-custom-rules) if you want to use it again.