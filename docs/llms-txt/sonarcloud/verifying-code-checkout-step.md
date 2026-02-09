# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/various-setups/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/scanner-environment/verifying-code-checkout-step.md

# Checked-out code

The SonarScanners run on code that is checked out from the repository. During the checkout of a working copy (clone) of the code from the project repository, we recommend using the full depth. Indeed, the so-retrieved SCM metadata enables various features such as:

* New Code detection:
  * On pull requests, not just the last commit but all the commits that are not on the target branch are considered. This requires a history long enough to find the common commit.
  * On long-living branches, the New Code definition can be set in different ways but a longer history is always better.
* Blame information display and automatic issue assignment based on the blame information.
* [#issue-backdating-new-issues-raised-on-old-code](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/solution-overview#issue-backdating-new-issues-raised-on-old-code "mention")

In addition, we recommend cloning all the branches of the repository to avoid reference errors during the checkout.

With Git, this means using `fetch-depth: 0`. This disables shallow clones and fetches all branches.

{% hint style="warning" %}

* Avoid any attempt at performing actions on the cloned repository to make sure the repository contains valid repository metadata (e.g. the .git folders have not been removed).
* The code in the cloned repository matches the code in the original repository (e.g no code is added to the branch on the cloned repository before analysis).
  {% endhint %}
