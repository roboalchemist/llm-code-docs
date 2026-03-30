# Source: https://docs.debricked.com/product/vulnerability-management/pull-requests/solve-vulnerabilities-using-pull-requests-pr.md

# Solve vulnerabilities using Pull Requests (PR)

Assume there is repository with huge number of vulnerabilities. It will take time to go through each one of them and potentially fix them. OpenText Core SCA offers the ability to open a pull request to solve many vulnerabilities at once.

### **Support for Pull Requests** <a href="#supportforpullrequests" id="supportforpullrequests"></a>

Currently, OpenText Core SCA only supports pull requests for certain package managers and integrations using the GitHub app, GitLab or Azure DevOps. For information regarding the support of your package manager, see the [language support page](https://docs.debricked.com/overview/language-support).

### **Solve multiple vulnerabilities using a Pull Request** <a href="#solvingavulnerabilityusingapullrequest" id="solvingavulnerabilityusingapullrequest"></a>

Following are the steps for to solve multiple vulnerabilities:

1. In a repository, click **Generate pull request** to let the tool update your dependencies, solve vulnerabilities, and create a pull request.
2. Click **View generated fix** to view the pull request.
3. When the pull request is merged, you will notice a decrease in the number of vulnerabilities.

#### **Set a commit message**

Once you click the **Pull Request** button, a new modal is displayed where it is possible to set your own commit message. If you choose not to provide a message, by default the message will be "Fix CVE-XXX" or "Bulk fix vulnerabilities", depending on the type of Pull Request that is created.&#x20;

### **Solve a single vulnerability using a Pull Request** <a href="#solveasinglevulnerabilityusingapullrequest" id="solveasinglevulnerabilityusingapullrequest"></a>

It is possible to solve a specific vulnerability in a repository using pull requests, instead of multiple CVEs at once as in the example above.

Following are the steps to solve a specific vulnerability:

1. In a repository, click the specific vulnerability you wish to remediate.
2. In the CVE view, click the **Open pull request** button. You can see the vulnerable version(s) and the proposed change.
3. Click **Confirm** to execute the changes.

{% hint style="warning" %}
If a pull-request is made, creating a new branch, this branch can be viewed in the web tool. If the pull-request is rejected and the branch is deleted, the branch can still be viewed in the UX. This is the case even after a re-scan of the repo, since the branch is still in the database. This data will be pruned only after 30 days.
{% endhint %}
