# Source: https://docs.debricked.com/product/vulnerability-management/pull-requests.md

# Pull Requests (PR)

The goal of a Pull Request is to completely remove the CVE from the repository. Note that some dependency versions do not allow a safe version of the currently vulnerable dependency. Therefore, the pull request will only be generated if at least one of the affected direct dependencies has been updated to a safe version.

OpenText Core SCA currently supports two types of pull requests:

### **CVE-specific Pull Request** <a href="#cve-specificpullrequest" id="cve-specificpullrequest"></a>

The pull request creation depends on the nature of the dependency relations. If updating the lock file suffices to fix the vulnerable dependency, the pull request will contain the updated lock file. If an update to the direct dependency is required, OpenText Core SCA will apply the fix to the main dependency file containing the direct dependency versions. Afterwards, OpenText Core SCA will update the lock file with the new version of the direct dependency and its dependencies.

When you generate a CVE-specific pull request, the following actions are performed to your repository and dependency files:

* Generate the dependency updates in the dependency file to fix the CVE.
* Make required changes to your dependency files as stated above.
* Create a branch in the repository.
* Push the remediated dependency files.
* Create pull request to original branch.

### **Repository-specific Pull Request** <a href="#repository-specificpullrequest" id="repository-specificpullrequest"></a>

Repository-specific pull requests are a way of remediating vulnerabilities in bulk, with a single click of a button. Instead of focusing on remediating a specific CVE, OpenText Core SCA widens the scope to all CVEs that affect a specific repository. Currently, OpenText Core SCA only supports lockfile-only repository-specific pull requests. They are a quick way of making sure that your dependency files are up-to-date. These pull requests generate your lock file(s) from scratch in an attempt to update indirect dependency versions within given constraints. This will fix the majority of the CVEs in many cases. When generating a repository-specific pull request from the repository view, it will be based on the branch selected in the dropdown provided after clicking the **Generate pull request** button.

When you generate a repository-specific pull request, the following actions are performed to your repository and dependency files:

* Apply required changes to your dependency files as stated above.
* Create a branch in the repository.
* Push the remediated dependency files.
* Create pull request to original branch.

### **Lockfile-only fix**

The lockfile-only fix means that you can regenerate the lockfile in your repository and the vulnerability will be solved. You don't need to update the root dependency - rather you should reinstall the same version (for example: run yarn upgrade and get a new lock.file). This is used when the version constraints set by the root dependency allow for the safe version of the indirect dependency, but it has been a while since you did the install. Then, re-installing it will solve the problem.

### **Branch selection**

The type of pull request being generated determines what the new generated branch will be based on. If you’re generating a bulk fix from the repository view, the branch will be based on the branch selected in the drop-down provided after pressing the **Generate pull request** button. If you're instead generating a pull request from the page of a specific CVE, the chosen branch will depend on a few factors:

* If a default branch containing the CVE is detected in your repository, the pull request branch will be based on it.
* If OpenText Core SCA is unable to detect a default branch, or the CVE exists in a branch other than the default one for that repository, OpenText Core SCA will first check if the CVE exists in the main or dev branch. If not, the branch which contains the latest commit in the repository is selected.

For more information on how to solve a vulnerability using a PR in the web tool, click the below link:

{% content-ref url="pull-requests/solve-vulnerabilities-using-pull-requests-pr" %}
[solve-vulnerabilities-using-pull-requests-pr](https://docs.debricked.com/product/vulnerability-management/pull-requests/solve-vulnerabilities-using-pull-requests-pr)
{% endcontent-ref %}
