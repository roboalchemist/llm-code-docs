# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/editing.md

# Editing issues

In SonarQube Cloud, you can change the status of an issue in the following cases:

* If you want to fix the issue later, you can accept an issue. The issue status is then marked as **Accepted**.
* If you think the analysis is mistaken, you can mark it as **False positive**, provided you have the corresponding permission.

In addition, you can reassign an issue, tag an issue, and comment on an issue. See [solution-overview](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/solution-overview "mention") for more information.

{% hint style="info" %}

* You can receive an email notification for issue-related events: see [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention").
* You can manage external issues (issues detected by an external tool and imported into SonarQube Cloud) in the same way as internal issues. Be aware that managing an external issue within SonarQube Cloud has no impact on its state in the external tool. For example, when you mark an issue as **False positive** in SonarQube Cloud, it is not reflected in the external tool.
* As you edit issues, the related metrics, for example, number of issues taken into account, will update automatically; as will the quality gate status if it’s relevant. See [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention") for more information.
  {% endhint %}

### Accepting an issue <a href="#accepting" id="accepting"></a>

You may accept an issue if you decide to fix the issue later. Note that SonarQube Cloud ignores accepted issues in the quality reports and ratings of the code.

{% hint style="info" %}
You can add a comment to your issue change action. See **Commenting on an issue** below for more information about issue comments.
{% endhint %}

To accept an issue:

1. Retrieve the issue. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.
2. In the issue card, select the **Open** issue status and select **Accept** in the contextual menu as illustrated below. A **Status change comment** box appears.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-c7dba162e76dd1657d2acc5b172fcb1415377969%2F5355c4ad1ef6a21e8e01eac6bc2ca48f44383d79.png?alt=media" alt="When editing an issue in SonarQube Cloud that you want to accept, select the issue from the Issues page, select Open (showing the current status of that issue), then choose Accept."><figcaption></figcaption></figure></div>

3. Enter your change comment (optional) and select **Change status**. The issue status is changed to **Accepted**.

### Marking an issue as False positive <a href="#false-positive" id="false-positive"></a>

If the analysis is mistaken, you can mark an issue as False positive provided you have the Administer Issues permission on the project. Note that SonarQube Cloud ignores False positive issues in the quality reports and ratings of the code.

{% hint style="info" %}
You can add a comment to your issue change action. See **Commenting on an issue** below for more information about issue comments.
{% endhint %}

To mark an issue as False positive:

1. Retrieve the issue. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.
2. In the issue card, select the **Open** issue status and select **False positive** in the contextual menu. A **Status change comment** box appears.
3. Enter your change comment (optional) and select **Change status**. The issue status is changed to **False positive**.

### Reopening an issue <a href="#reopening" id="reopening"></a>

You can reopen an Accepted issue when it’s time to fix it or reopen a False positive issue if it turns out to be a true positive.

To reopen one or several issues:

1. Retrieve the issue. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.
2. In the issue card, select the **Accepted** or **False positive** issue status and select **Reopen** in the contextual menu. The issue status is reset to **Open**.

### Marking an issue as reviewed <a href="#marking-as-reviewed" id="marking-as-reviewed"></a>

To mark issues as reviewed, you may use the tagging feature: create the Reviewed tag and assign it to reviewed issues: see **Tagging an issue** below. This way, you can filter the reviewed issues by using the Tag filter.

### Assigning an issue <a href="#assigning" id="assigning"></a>

When possible, SonarQube Cloud assigns a default assignee at issue creation time, see [solution-overview](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/solution-overview "mention") for more information. You can assign an unassigned issue to a user, reassign an issue to another user, or unassign an issue.

To assign an issue:

1. Retrieve the issue. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.
2. In the issue card, click the assignee name or the **Not assigned** mention. The list of users to whom you can assign the issue appears.
3. In the list, select the new assignee or select **Not assigned** in the list to unassign the issue.

### Tagging an issue <a href="#tagging" id="tagging"></a>

You can create tags and assign them to issues to retrieve them more easily or to indicate a workflow step. For example, you can use a tag to mark an issue as reviewed.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-346ad41228c907e95994c748db9d4694e4c8a336%2Fee0d4769698ee26de2e4912b672793e0f8cac178.png?alt=media" alt="An issue&#x27;s tags are managed on the right-hand side of the issue&#x27;s description. Select the + sign to manage an issue&#x27;s tags."><figcaption></figcaption></figure></div>

{% hint style="info" %}
Rules can also be tagged (In particular, [built-in-rule-tags](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/built-in-rule-tags "mention") may be assigned to some rules.). An issue inherits the tags assigned to the rule that raised the issue. You can remove the inherited tags.
{% endhint %}

To manage the tags assigned to an issue:

1. Retrieve the issue. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.
2. In the search results list or in the detail view, select in the **Tags** section if the issue. A dialog opens with the list of existing tags.
3. In the dialog, you can use the search field to search for an existing tag. To create a new tag, enter the new tag in the search field: the new tag will appear in the list of tags with a plus sign in front of it .
4. To assign or unassign a tag, select or clear the tag’s checkbox in the list.
5. Click anywhere outside the dialog to close the dialog.

### Commenting on an issue <a href="#commenting" id="commenting"></a>

When accepting an issue or marking an issue as **False positive**, you can add a comment. You can also add a comment to an issue anytime. These comments are visible from the **Activity** tab of the issue: see **Viewing the issue management history and comments** in [reviewing](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/reviewing "mention").

By default, comments are shared between all users. They can be disabled at the global level.

To add a comment to an issue:

1. Retrieve the issue and open its detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.
2. Open the **Activity** tab.
3. Select **Add a comment**. The "Add a comment" dialog box opens.
4. Enter your comment and select **Comment**.
5. Your comment is added to the **Activity** tab.

### Suppressing the issues on a given line <a href="#suppressing" id="suppressing"></a>

In most languages, you can use the `//NOSONAR` comment at the end of a line to suppress all issues on the line. This will suppress all issues - now and in the future - that might be raised on the line.

### Editing several issue in bulk <a href="#editing-issues-in-bulk" id="editing-issues-in-bulk"></a>

To edit several issues at once:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-565bc17bdad671b3b7e1c30c943372441a8eb188%2Fissues-bulk-change.png?alt=media" alt="Bulk change button"><figcaption></figcaption></figure></div>

1. Select issues individually, or select all issues by clicking the bulk change checkbox at the top of the page. You can deselect the issues you do not want to include.
2. Click on the **Bulk change** button to open a modal.
3. In the modal, select the actions to perform:
   * **Assign**: Assign the issues to a user.
   * **Add tags**: Add tags to the issues.
   * **Remove tags**: Remove tags from the issues.
   * **Change status**: To accept, confirm, fix, reopen or mark the issues as a false positive.
   * **Status change comment**: Add a comment about the changes you are applying. Additionally, you can share the comment with Sonar to help improve the analysis.
4. Click **Apply**.

### Creating Jira Cloud work items from SonarQube issues

You can create a Jira Cloud work item from a single or multiple SonarQube issues. See [jira-integration](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/jira-integration "mention") for more information.
