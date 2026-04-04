# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/reviewing.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/reviewing.md

# Reviewing issues

### Viewing issue details <a href="#viewing-issue-details" id="viewing-issue-details"></a>

To view the issue’s details, retrieve an issue and click on its title. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.

The main components of the issue detail page are as follows:

1. A list of filtered issues.
2. A path to the code file where the issue is located.
3. Current issue.
4. Other issues that were raised in the same code file.
5. A detailed view of the issue.
6. The coding rule that raised the issue. Click on the link to read more about the rule that raised the issue.
7. Tabs with detailed information about the issue:
   * **Where is the issue?** See the issue’s location and message in the code.
   * **Why is this an issue?** Read the issue’s description.
   * **How can I fix it?** See how to fix the issue and view a noncompliant code example and a compliant solution.
   * **Activity**: Read comments and management history of the issue.
   * **More info**: View additional resources and information that can help you to understand and fix the issue.
8. Issue message displayed in the code.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-3e11eba9b0d8dc80136e7c94afaeba80866bddc0%2Fdefc9eb3fc2f8d06bc3e4295a2725ee5d286e37a.png?alt=media" alt="There are eight key places in the SonarQube Cloud user interface to review an issue’s details."><figcaption></figcaption></figure>

### Navigating through the issue’s secondary locations <a href="#secondary-locations" id="secondary-locations"></a>

All SonarQube Cloud issues specify a location in the code showing where the issue occurs. However, some of the more complex rules produce issues for which a single location is not enough to adequately explain why the issue has occurred. These more complex rules often identify additional locations in the code to help understand the problem. These additional locations are referred to as secondary locations. Secondary locations may just indicate other locations that are related to the issue or may identify a flow through the code that leads to the issue.

#### Other locations <a href="#other-locations" id="other-locations"></a>

Retrieve the issue and navigate to the issue's detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.

1. Additional locations are shown in the left sidebar. Click on the locations to highlight them in the code on the right. You can also use the keyboard combination indicated under the list to navigate to the previous or next location.
2. The highlighted location of the issue in the code with the issue’s message.
3. List of additional locations in the code on the right side.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-27ac046647101f5d0f60144774250e8568290d89%2F835f4f1e851076e197a3198d433ac28ffbd4e1f5.png?alt=media" alt="When reviewing your issue&#x27;s details, additional locations will be listed in the left sidebar. The location of your selected instance is highlighted in the code, and additional locations are called out with red numbers in the code."><figcaption></figcaption></figure></div>

#### Execution flow <a href="#execution-flow" id="execution-flow"></a>

When the issue originates upstream, paths through the code (execution flows) are shown from the source to the sink (destination). In particular, for issues breaking a security-injection rule, there is a vulnerability when the inputs handled by your application are controlled by a user (potentially an attacker) and not validated or sanitized. In that case, SonarQube Cloud displays the execution flow from the sources (user-controlled inputs) to sinks (sensitive functions).

{% hint style="info" %}
Check out this [video](https://www.youtube.com/watch?v=17G-aZcuMKw) for an example of a security issue with an execution flow.
{% endhint %}

To navigate through the execution flow of an issue:

1. Retrieve the issue and open its detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information. The execution flows are listed in the left sidebar.
2. To navigate to a location in the execution flow, select it in the list. You can also use the key combination indicated under the flow to navigate to the previous or next location in the flow.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-8bc2ff5d36a0794bf045f34d222d629d72b0904c%2Fb1bcb7318da4543c6f981b4da2b7a97034268f7e.png?alt=media" alt="SonarQUbe Cloud calls out the execution flow for issues that break security-injection rules. The flow of information through the issue is shown in the left sidebar."><figcaption></figcaption></figure></div>

### Management history and comments <a href="#history-and-comments" id="history-and-comments"></a>

1. Retrieve the issue and open its detail view. See [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") for more information.
2. Open the **Activity** tab. The tab shows the number of comments added to the issue.
3. View the activities and comments or click **Add a comment** to leave a comment about the issue.
