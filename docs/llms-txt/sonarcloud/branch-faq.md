# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/branches/branch-faq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/branches/branch-faq.md

# Branch FAQ

*Branch analysis is available starting in* [*Developer Edition*](https://www.sonarsource.com/plans-and-pricing/developer/)*.*

### How long are branches retained? <a href="#branches-retained" id="branches-retained"></a>

Branches will be deleted automatically when they are inactive according to your settings at **Administration** > **Configuration** > **General Settings** > **Housekeeping** > **Number of days** before deleting inactive branches except for branches you have set to be kept when inactive. These branches are kept until you delete them manually at the project level at **Project Settings > Branches and Pull Requests**. See [branch-analysis](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/branches/branch-analysis "mention") for more information on keeping inactive branches.

### Does my project need to be stored in an SCM like Git or SVN? <a href="#scm" id="scm"></a>

No, you don’t need to be connected to an SCM. However, SCM data still enhances the SonarQube experience (including issue auto-assignment and issue backdating), and you will be well prepared to take advantage of [pull-request-analysis](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/pull-request-analysis "mention")!

### What if I mark an issue "Accept" or "False-Positive" in a branch? <a href="#false-positive" id="false-positive"></a>

If you have configured the **Reference Branch** [defining-new-code](https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/clean-as-you-code-settings/defining-new-code "mention") for a branch, issues in the reference branch automatically inherit their attributes from this original branch (including the **Accept** and **False Positive** resolutions) after the merge.

### Can I manually delete a branch? <a href="#delete-branch" id="delete-branch"></a>

You can delete a branch in the **Branches** tab at **Project Settings** > **Branches and Pull Requests**.

### Does the payload of the Webhook include branch information? <a href="#webhook-branch" id="webhook-branch"></a>

Yes, an extra node called `branch` is added to the payload.

### When are Webhooks called? <a href="#webhooks" id="webhooks"></a>

When the computation of the background task is done for a given branch.

### What is the impact on my LOCs consumption vs my license? <a href="#loc" id="loc"></a>

The [license-administration](https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/license-administration "mention") of your largest branch is counted toward your license limit. All other branches are ignored.
