# Source: https://docs.axonius.com/docs/rules-simulator.md

# Using the Rule Simulator

A rule defines the level of access each identity gets within the organization based on various identifiers and the employee's position, such as department, team, and role.

Use the **Rules Simulator** to build a Query Intersection Venn diagram to compare between rules that grant access and permissions. This  helps you learn about the rules in your organization and determine when multiple rules can be condensed, making your rules easier to manage.

To open the **Rule Simulator**, on the Rules page, click **Rule Simulator**.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IDMRuleSimulator.png)

## Common Use Cases

Here are some common use cases for the Rules Simulator.

### Overlap Analysis

You can use the Rules Simulator to compare between rules. You can compare up to six rules at once. Click on the overlapping sections to analyze the comparison to determine which users overlap between the various rules. Based on your analysis, you may determine that it would be best to condense some or all of the overlapping rules into one rule.

Alternatively, you may want to modify the queries that the rules are based on to lower the overlap between who is covered by each rule.

If one rule's query shows a complete overlap with another rule, then you may determine that the rule is redundant and can be deleted.

In the example below, the overlap in the center of all the triangles indicates that the Marketing Assignments rule entirely overlaps with the Sales and Marketing Assignments rules. This indicates that the Marketing rule is redundant and can be deleted.

<Image alt="RulesSimulator" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RulesSimulator.png" />

### Coverage Analysis

Additionally, you can use the Rules Simulator to perform a coverage analysis to reveal if the rules in place are granting certain permissions to too many or too few users and may need to be revised to be more effective. Alternatively, the analysis may help you confirm that the rules are working as expected, or that a new rule is needed.

To perform a coverage analysis, compare a Query used by an existing or not-yet-created rule to the entitlements, or the access, that the rule grants.

For example, if the overlap between the query and the entitlements is small:

* For a not-yet-created rule, that would indicate that the rule is probably not needed as most of the users represented by the query don't require those entitlements.
* Alternatively, it could indicate that the rule is needed but that the query needs to be altered to cover a more accurate user base.
* If there is a large overlap, it would indicate that the query and entitlements are a strong basis for the rule as it reflects a high demand for those entitlements among that subset of users.

The example below shows that the "All Sales Engineering" rule covers 100% of the users in the "Assigned with Sales" group. This demonstrates that the rule is effective and that the users of the group were granted access by the rule.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RulesSimulator_Coverage.png)

## Configuring a Rules Simulation

You can configure a rules simulation for up to six rules in your system.

**To configure a Rules Simulation:**

1. Select an enforcer. This is the party that executes the commands determined by the rule.
2. In the Intersecting Query area select the rules that you want to compare.
   1. (Optional) Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FilterIcon-BlackOutline.png) to filter the data returned by the selected rule. When a filter is applied, a red dot appears on the filter icon. To clear the filter, click the icon, and then **Clear** and **Save**.
   2. (Optional) Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PencilEditIcon.png) to assign a custom name to the rule. This is useful when you want a more representative name than the rule name itself. When a custom name is applied, a red dot appears on the pencil icon. To clear the custom name, click the icon, and then **Clear** and **Save**.
   3. (Optional) Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Plus-button-sm.png) to add another rule.
3. (Optional) Click to enable the Show results for previous date toggle. For more information see [Viewing Query Results from a Historical Date](/docs/historical-query-results).
4. Click **Save**.

<Image alt="RulesSimulator_Overlap2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RulesSimulator_Overlap2.png" />

## Viewing Simulation Results

The Venn diagram is displayed in the preview panel. Each triangle represents one of the selected rules.

You can use the check boxes to focus in on specific rules and/or intersections between the rules. Alternatively, you can click one of the triangles or one of the overlapping areas on the chart.

* In the right panel, you can view all the managed identities that are impacted by the rule or the selected area of chart.
* For a more detailed view of this Managed Identities list, click **Asset Page** to open the list in the User asset page.
* To use the list as the basis for a new rule, click **Save As**.

<br />