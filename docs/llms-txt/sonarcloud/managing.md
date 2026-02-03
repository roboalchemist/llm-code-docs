# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/managing.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/managing.md

# Editing issues

In SonarQube Server, you can change the status of an issue in the following cases and provided you have the Administer Issues permission:

* If you want to fix the issue later, you can accept an issue. The issue status is then marked as **Accepted**.
* If you think the analysis is mistaken, you can mark it as **False positive**.

In addition, you can reassign an issue, tag an issue, and comment on an issue.

{% hint style="info" %}

* You can receive an email notification for issue-related events: see the [email](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-your-account/subscribing-to-notifications/email "mention") page.
* You can manage external issues (issues detected by an external tool and imported into SonarQube Server) in the same way as internal issues. Be aware that managing an external issue within SonarQube Server has no impact on its state in the external tool. For example, when you mark an issue as **False positive** in SonarQube Server, it is not reflected in the external tool.
* As you edit issues, the related metrics, for example, number of issues taken into account, will update automatically; as will the quality gate status if it’s relevant.
  {% endhint %}

### Accepting an issue <a href="#accepting" id="accepting"></a>

You may accept an issue if you decide to fix the issue later provided you have the Administer Issues permission on your project. Note that SonarQube Server ignores accepted issues in the quality reports and ratings of the code.

{% hint style="info" %}
You can add a comment to your issue change action. See [#commenting](#commenting "mention") for more information.
{% endhint %}

The procedure below explains how to accept a single issue. To accept several issues at once, see [#bulk-change](#bulk-change "mention").

To accept an issue:

1\. Retrieve the issue, it’s not necessary to open the detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention") for more information.

2\. In the issue card, select the **Open** issue status and select **Accept** in the contextual menu. A **Status change comment** box appears.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/ZeVqSMsOY8BAgYOlkR5v/accept-issue.png" alt="Changing the status of an issue in SonarQube." width="563"><figcaption></figcaption></figure></div>

3\. Enter your change comment (optional) and select **Resolve**. The issue status is changed to **Accepted**.

### Marking an issue as False positive <a href="#false-positive" id="false-positive"></a>

If the analysis is mistaken, you can mark an issue as False positive provided you have the Administer Issues permission on your project. Note that SonarQube Server ignores False positive issues in the quality reports and ratings of the code.

{% hint style="info" %}
You can add a comment to your issue change action. See [#commenting](#commenting "mention") for more information.
{% endhint %}

The procedure below explains how to mark a single issue as False positive. To mark several issues at once, see [#bulk-change](#bulk-change "mention").

To mark an issue as False positive:

1. Retrieve the issue, it’s not necessary to open the detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention") for more information.
2. In the issue card, select the **Open** issue status and select **False positive** in the contextual menu. A **Status change comment** box appears.
3. Enter your change comment (optional) and select **Resolve**. The issue status is changed to **False positive**.

### Reopening an issue <a href="#reopening" id="reopening"></a>

You can reopen an Accepted issue (when it’s time to fix it) or a False positive issue (if it turns out to be a true positive).

The procedure below explains how to reopen a single issue. To reopen several issues at once, see [#bulk-change](#bulk-change "mention").

To reopen one or several issues:

1. Retrieve the issue, it’s not necessary to open the detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention") for more information.
2. In the issue card, select the **Accepted** or **False positive** issue status and select **Open** in the contextual menu. The issue status is reset to **Open**.

### Marking an issue as reviewed <a href="#marking-as-reviewed" id="marking-as-reviewed"></a>

To mark issues as reviewed, you may use the tagging feature: create the Reviewed tag and assign it to reviewed issues: see [#tagging](#tagging "mention"). This way, you can filter the reviewed issues by using the Tag filter.

### Assigning an issue <a href="#assigning" id="assigning"></a>

When possible, SonarQube Server assigns a default assignee at issue creation time (see [solution-overview](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview "mention") for more information). You can assign an unassigned issue to a user, reassign an issue to another user, or unassign an issue.

The procedure below explains how to assign a single issue. To assign several issues at once, see [#bulk-change](#bulk-change "mention").

To assign an issue:

1. Retrieve the issue, it’s not necessary to open the detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention") for more information. To filter the unassigned issues, select **Not assigned** in the **Assignee** filter.
2. In the issue card, click the assignee name or the **Not assigned** mention. The list of users to whom you can assign the issue appears.
3. In the list, select the new assignee (or select **Not assigned** in the list to unassign the issue).

### Customizing a software quality severity level <a href="#issue-severity" id="issue-severity"></a>

Issues inherit software quality severity levels from the rules that raised them. If you decide that a different level is more appropriate for a given issue, you can customize it. Keep in mind that changing the severity level may impact your quality gates.

The following table shows the severity levels of software qualities for [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention") and [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention").

{% tabs %}
{% tab title="MQR SEVERITY TYPES" %}
The table below lists the severity metrics used in Multi-Quality Rule mode.

| **Severity** | **Definition**                                                                                                                                                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Blocker      | An issue that has a significant probability of severe unintended consequences on the application that should be fixed immediately. This includes bugs leading to production crashes and security flaws allowing attackers to extract sensitive data or execute malicious code. |
| High         | An issue with a high impact on the application that should be fixed as soon as possible.                                                                                                                                                                                       |
| Medium       | An issue with a medium impact.                                                                                                                                                                                                                                                 |
| Low          | An issue with a low impact.                                                                                                                                                                                                                                                    |
| Info         | There is no expected impact on the application. For informational purposes only.                                                                                                                                                                                               |

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/6XJBNCIpxcNs14ithgOI/change-issue-severity-mqr.png" alt="Changing the severity level of an issue in SonarQube." width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Users with appropriate permissions are able to set a custom severity on a rule.
{% endhint %}
{% endtab %}

{% tab title="STANDARD EXPERIENCE SEVERITY TYPES" %}
The table below lists the severity metrics used in Standard Experience mode.

| **Severity** | Definition                                                                                                                                                                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Blocker      | An issue that has a significant probability of severe unintended consequences on the application that should be fixed immediately. This includes bugs leading to production crashes and security flaws allowing attackers to extract sensitive data or execute malicious code. |
| Critical     | An issue with a critical impact on the application that should be fixed as soon as possible.                                                                                                                                                                                   |
| Major        | An issue with a major impact on the application.                                                                                                                                                                                                                               |
| Minor        | An issue with a minor impact on the application.                                                                                                                                                                                                                               |
| Info         | There is no expected impact on the application. For informational purposes only.                                                                                                                                                                                               |

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/v2J4zDVuMY3RT5ZNg6sR/6c42cd11a68e42194ce42ada06ade9858780936a.png" alt="Changing the severity level of an issue in SonarQube." width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Users with appropriate permissions are able to set a custom severity on a rule.
{% endhint %}
{% endtab %}
{% endtabs %}

To customize the issue severity level for **Software qualities impacted**:

1. Retrieve the issue you want to manage. See [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention") for more information.
2. Select an issue from the search results list:
   * For Standard Experience, select by issue type: **Bug**, **Vulnerability**, **Code Smells**.
   * For Multi-Quality Rule Mode, select by issue quality: **Security**, **Reliability**, **Maintainability**.
3. Select the severity level you wish to apply from the drop-down list. You can also change the severity level from the issue’s details page.

### Tagging an issue <a href="#tagging" id="tagging"></a>

You can create tags and assign them to issues in order to retrieve issues more easily or to indicate a workflow step. For example, you can use a tag to mark an issue as reviewed. The figure below shows how tags are displayed in the issue item.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/ffyjqUmVLFd1R4IodszV/issue-tags.png" alt="Tagging an issue in SonarQube." width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Rules can also be tagged (In particular, [built-in-rule-tags](https://docs.sonarsource.com/sonarqube-server/user-guide/rules/built-in-rule-tags "mention") may be assigned to some rules and your Quality Standards administrator can assign custom ones). An issue inherits the tags assigned to the rule that raised the issue. You can remove the inherited tags.
{% endhint %}

The procedure below explains how to tag a single issue. To add or remove a tag to/from several issues at once, see [#bulk-change](#bulk-change "mention").

To manage the tags assigned to an issue:

1. Retrieve the issue you want to manage. See [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention") for more information.
2. In the search results list or in the detail view, select in the **Tags** section if the issue. A dialog opens with the list of existing tags.
3. In the dialog, you can use the search field to search for an existing tag. To create a new tag, enter the new tag in the search field: the new tag will appear in the list of tags with a plus sign in front of it .
4. To assign or unassign a tag, select or clear the tag’s checkbox in the list.
5. Click anywhere outside the dialog to close the dialog.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/VMqAUDE6LCCM8UAcRtG5/issue-new-tag.png" alt="Adding a new tag to an issue in SonarQube." width="563"><figcaption></figcaption></figure></div>

### Commenting on an issue <a href="#commenting" id="commenting"></a>

When accepting an issue or marking an issue as **False positive**, you can add a comment. You can also add a comment to an issue anytime. These comments are visible from the **Activity** tab of the issue: see [#history-and-comments](https://docs.sonarsource.com/sonarqube-server/user-guide/reviewing#history-and-comments "mention").

By default, comments are shared between all users (it can be disabled at the global level).

To add a comment to an issue:

1. Retrieve the issue and open its detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention") for more information.
2. Open the **Activity** tab.
3. Select **Add a comment**. The "Add a comment" dialog box opens.
4. Enter your comment and select **Comment**.
5. Your comment is added to the **Activity** tab.

### Suppressing the issues on a given line <a href="#suppressing" id="suppressing"></a>

In most languages, you can use the `//NOSONAR` comment at the end of a line to suppress all issues on the line. This will suppress all issues - now and in the future - that might be raised on the line.

### Managing several issues in bulk <a href="#bulk-change" id="bulk-change"></a>

To manage several issues at once:

1\. In the list of filtered issues, select the issues you want to manage:

* To select one issue, select the issue check box.
* To select all issues, select the **Bulk change** check box. Issues you do not want included in your action can be individually unselected.

2\. Select the **Bulk change** button. The **Change issues** dialog opens.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/TVWuJX95ii192G0EAvVF/issue-bulk-change.png" alt="Applying a bulk change to several issues in SonarQube."><figcaption></figcaption></figure>

3\. In the dialog, select the action you want to perform:

* **Assign**: to assign the issues to the same user.
* **Add tags**: to add the same tag to the issues.
* **Remove tags**: to remove the same tag from the issues.
* **Change status**: to reopen the issues, accept the issues, or mark the issues as **False positive**.

4\. Select **Apply** to complete the bulk changes.

### Related pages

* [fixing](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/fixing "mention")
* [adding-tags-to-rule](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/adding-tags-to-rule "mention")
