# Source: https://docs.axonius.com/docs/editing-enforcement-actions-in-a-risk-score.md

# Editing Enforcement Actions in a Risk Score

All Risk Scores are **Enforcement Sets**. After creating them, you can edit them and add more actions and advanced configurations as in any Enforcement Set. All Risk Scores created on the Risk Score page are available in the Action Center as well, and vice versa.

To learn more about Enforcement Sets, see [Enforcement Sets Page](/docs/using-the-ec-page),[Creating Enforcement Sets](/docs/creating-new-enforcement-sets), and [Managing Enforcement Sets](/docs/manage-ec-sets).

To learn more about defining Risk Score using an Enforcement Action, see [Axonius - Calculate Risk Score](/docs/risk-score).

To navigate to a specific Risk Score's page in the Action Center, click the  ![LaunchIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-1FWYINZW.png) icon next to the Risk Score's name. From this page, you can do the following:

* Edit the Enforcement Set name (Risk Score name) or add a description to it. The new name will be displayed in the Axonius Risk Score page once you refresh it.
* Change the query (the assets this Risk Score applies to) under **Run this Enforcement Set on assets matching the following query**.

<Callout icon="❗️" theme="error">
  Note

  You cannot change the query when it is associated with more than one Enforcement Action, meaning, if there is more than one action in the Enforcement Set - see example below. In this case, the query selection menu is disabled.
</Callout>

* [Schedule the Enforcement Set runs](/docs/scheduling-ec-set-runs).
* [Configure Success, Failure, and Post Enforcement Actions](/docs/create-ec-set#configuring-success-failure-and-post-enforcement-actions). An Enforcement Set can include one or more Success, Failure, or Post Actions.
  * **Success Actions** run on each asset for which the main action completes successfully.
  * **Failure Actions** run on each asset for which the main action does not complete successfully.
  * **Post Actions** run on ALL assets matching the query after the main action has completed.

In the following example, an **Add Custom Data to Assets** success action is set to run on each asset for which the main action has calculated the Risk Score successfully. To learn more about this action, see [Axonius - Add Custom Data to Assets](/docs/add-custom-data).

![AddSuccessAction](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-Q2AVIZTA.png)

You can add to each asset a custom field named **Risk Score Exists**. The field type is Single Value, the value type is Boolean, and the field value is Yes - indicating that all these assets have a Risk Score.

![AddCustomData](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-J9S3DQB6.png)

After any change you make to the Enforcement Set, make sure to click **Save** or **Save and Run**.