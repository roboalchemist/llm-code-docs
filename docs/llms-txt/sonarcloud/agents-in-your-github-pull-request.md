# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/with-ai-features/agents-in-your-github-pull-request.md

# Agents in your GitHub pull request

### The SonarQube Remediation Agent

{% hint style="success" %}
The SonarQube Remediation Agent is a [Beta](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#beta) feature available with Enterprise plan accounts. It is free during the beta phase and will be a paid feature when it moves to [General Availability](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#general-availability). To learn more about the terms & conditions, please see our legal page about features in [Early Access](https://www.sonarsource.com/legal/early-access/).

If your SonarQube Cloud organization is not on an Enterprise plan, please see the [getting-started-with-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise "mention") pages to get the process started.
{% endhint %}

Once the SonarQube Remediation Agent is activated as described on the [sonarqube-remediation-agent](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/sonarqube-remediation-agent "mention") page, it's activity can be reviewed in SonarQube Cloud and the agent can be engaged in GitHub on your open PR.

The agent is triggered when your quality gate fails during the pull request (PR) analysis. If you have additional commits on the PR that cause your quality gate to fail, you will trigger a new agent and only engage with the most recent agent called.

Once active, the SonarQube Remediation Agent automatically generates commit suggestions for new issues introduced in the PR. It only offers fix suggestions for issues in the PR within which the agent is was triggered.

### Agent behavior

After your SonarQube Cloud administrator has completed the steps laid out in the [#enable-your-agent](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/sonarqube-remediation-agent#enable-your-agent "mention") article, navigate to *Your SonarQube Cloud Project* > **Agent activity** to view your remediation agent’s activity. The **Agent activity** page provides basic information and hyperlinks to:

1. The GitHub PR where the agent exists.
2. The PR summary for the relevant pull request. See the *Pull request analysis* page for information about [#understanding-your-pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis#understanding-your-pull-request-analysis "mention").
3. A timestamp for the recorded activity.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-7a642f1331c4cd99b243cee05179b93ceb4c55ed%2Fsonarqube-cloud-agent-activity-page.png?alt=media" alt="The SonarQube Cloud Agent activity page lists each of the agent&#x27;s event moments on your pull request analyses."><figcaption></figcaption></figure>

### Engage with the agent

A single **Remediation Agent Summary** will be created on your pull request explaining the agent’s suggestions, and a unique **Agent Fix (Issue X of Y)** commit suggestion for each issue will be created for review by a developer. The summary provides an explanation about each fix suggestion, including links to the issue description, type, severity, and estimated effort required to fix (where applicable). See the diagram below for a more detailed explaination:

1. The status of your quality gate will be shown on the activity history of our PR. The next action item in your history should be the Remediation Agent summary; if it doesn't show up or isn't updating its status, try refreshing your page.
2. Select the **Suggested fixes** collapsible to reveal the list of fixes provided by the agent. The summary page provides information about:
   * **Quality:** each issue's [software-qualities](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/software-qualities "mention")
   * **Issue:** the issues's rule description and a link to the issue as found in the SonarQube Cloud Pull request analysis
   * **Status**: the state of each issue's resolution in relation to the agent's activity
3. Each fix suggestion provides the issue's rule description and the accompanying information as found with every SonarQube rule. The generation of fix suggestions takes place in the background and the new code does not introduce new issues.
4. Select **View fix** to jump to a unique comment in your PR history. There, you can review the fix in more detail and if approved, commit the fix as a change. See [#review-agent-fix-suggestions](#review-agent-fix-suggestions "mention") for more information.
5. If the agent can't provide a fix suggestion, the issue will be listed here. Depending on the number of issues and the parameters of your quality gate, you may need to fix these issues in the IDE before being able to merge your PR. See the page about using [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention") and connected mode, if needed.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-6fa5ebf35a58ef3edc942e7bf3ac0ce30f04a998%2Fsonarqube-cloud-remediation-agent-summary.png?alt=media" alt="The current state of SonarQube Remediation Agent&#x27;s activity will be summarized as a comment in your pull request on GitHub." width="375"><figcaption></figcaption></figure></div>

### Review agent fix suggestions

If in point 4 above, you selected **View fix**, you'll arrive at a unique comment designed for reviewing your specific issue.

Each issue has its own comment that includes a dif view of the suggested change along with an explanation about the fix suggestion. Additional information includes links to the issue description, type, severity, and an estimated effort required to fix the issue (where applicable).

1. Use this information to find your issue's location in your code.
2. A dif view is provided so you can see what will be changed if you choose to **Select fix** (see number 4 below).
3. The suggestion details include an AI-generated explanation of what the code change is accomplishing.
4. Choosing **Select fix** means that you have reviewed the content and have marked the agent's fix suggestion to be commited to your PR. The fix suggestion will be added to a list that must be confirmed in the next step.
5. *IMPORTANT*: Select **Commit changes** only when you are ready to accept *all of your selected fixes*. Selecting the **Commit changes** checkbox applies all of the reviewed changes you accepted in point 4. Once selected, all of the changes will be applied to your code in a new commit. The new code does not introduce new issues.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-b6544bf71f447b6a28c907f9377731e1506a4112%2Fsonarqube-cloud-remediation-agent-comment-diagram.png?alt=media" alt="Each fix suggestion reported by the SonarQube Remediation Agent will have information that helps you understand what will be changed, if you accept the fix." width="375"><figcaption></figcaption></figure></div>

### The agent's commit

The SonarQube Remediation Agent will contain important information that you may want to reference later. Here's a list of the information that it includes:

* The fixes you reviewed and approved (when selecting **Select fix**) will be kept as hidden items in your PR history. The fix comment, as described in [#review-agent-fix-suggestions](#review-agent-fix-suggestions "mention"), will be updated to confirm that the fix suggestion was commited to your PR.
* All of the fixes that you select will be in the single commit with a unique reference number, and marked as co-authored by *you* and the *sonarqube-agent \[bot]*.
* The new commit will trigger another pull request analysis on SonarQube Cloud. The results of the analysis will determine what happens next in your PR:
  * If your quality gate passes, you can proceed with merging in accordance with your Branch protection rules.
  * If your quality gate fails, the SonarQube Remediation Agent will be retriggered, and you can restart the review process of its fix suggestion. The agent may take a few minutes to run depending on the complexity of your project. Refreshing the page in GitHub can help show the agent's most recent activity.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-16694dd7f8117c3c6ef1a2c25a9ac031eec97955%2Fsonarqube-cloud-accept-agent-fixes.png?alt=media" alt="The SonarQube Remediation Agent&#x27;s comment history and commit will retain all of the information needed to understand the proposed changes to your code." width="563"><figcaption></figcaption></figure></div>
