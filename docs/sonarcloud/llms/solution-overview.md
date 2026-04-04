# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/solution-overview.md

# Issue management solution

This page explains how SonarQube Cloud identifies, assigns, and synchronizes issues. Information is included about issue lifecycles and also explains issue-related features and concepts.

### Issue identification and assignment by SonarQube Cloud <a href="#identification-and-assignment" id="identification-and-assignment"></a>

For each code file:

1. SonarQube Cloud checks if the file has been renamed.
2. SonarQube Cloud determines:
   * Whether an issue found during the current analysis is new or existed previously.
   * If an issue found during the previous analysis has been fixed.
3. For each new issue:
   * SonarQube Cloud determines and sets the issue date. The issue date is the analysis date except in some cases where issue backdating to the line commit date is necessary.
   * SonarQube Cloud tries to automatically assign the issue to an appropriate SonarQube Cloud user.

#### Method used to identify if an issue is new <a href="#method-used-to-identify-if-an-issue-is-new" id="method-used-to-identify-if-an-issue-is-new"></a>

SonarQube (Server, Cloud) use the same algorithm to determine whether an issue is new or existed previously:

* For each issue found in the file from the previous analysis, it compares it to each issue found in this file during the current analysis:
  * If there is no match then it considers the issue as Fixed.
  * If there is a match and the issue status is Fixed in the previous analysis then it reopens the issue.
* For each issue found in the file during the current analysis, if there is no matching issue in the file from the previous analysis then it is considered new.

This algorithm relies on the issue’s line hash. The line hash is calculated based on the content of the first line the issue is reported on, excluding the white spaces.

The figure below shows the comparison process between two issues.

<figure><img src="broken-reference" alt="Questions used by SonarQube to identify whether an issue is new or not"><figcaption></figcaption></figure>

* If the issue is on the same rule, with the same line hash (but not necessarily with the same message) : MATCH
* If the issue is on the same rule, on the same line number with the same message (but not necessarily with the same line hash): MATCH
* If the issue is on the same rule but the detected block moved inside the file, then if the issue is on the same line within the moved block, and has the same message: MATCH

#### Issue backdating (new issues raised on old code) <a href="#issue-backdating-new-issues-raised-on-old-code" id="issue-backdating-new-issues-raised-on-old-code"></a>

In some corner cases, new issues or issues that didn’t exist in the previous analysis, may be detected on old code or code outside of the new code definition period. See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for more details. This may be the case, for instance, if the issue has existed in code for a long time but was only found in the most recent analysis because new rules were added to the quality profile. In such cases, SonarQube Cloud doesn’t apply the analysis date as the issue date but uses backdating so that it can correctly identify whether the new issue is to be reported on new code or old code (overall code).

If the date of the last change to the line is available then SonarQube Cloud will backdate to this date an issue identified as new in the following cases:

* On the first analysis of a project or branch.
* When the rule is new in the quality profile (a brand new rule activated or a rule that was deactivated and is now activated) or when a rule parameter was changed.
* When SonarQube Cloud has just been upgraded because rule implementations could be smarter now.
* When the rule is external, rule managed and applied by an external, third-party analyzer.
* Previously excluded files are now analyzed.

{% hint style="warning" %}
During a pull request analysis, new issues on old code are not reported since only new code issues are reported. It means that the first analysis on the target branch after the merge may report new issues on old code that were not reported by the pull request analysis.
{% endhint %}

#### Automatic issue assignment <a href="#automatic-issue-assignment" id="automatic-issue-assignment"></a>

SonarQube Cloud automatically assigns an issue during analysis to the last committer on the issue line - called issue author - if the author can be correlated to a SonarQube Cloud user.

Login and email correlations between SCM account and SonarQube Cloud user are made automatically. For example, if the user commits with their email address and that email address is part of their SonarQube Cloud user profile, then new issues raised on lines where the user was the last committer will be automatically assigned to the user.

{% hint style="info" %}

* Currently, issues on any level above a file, for example, issues reported at a directory or project level, cannot be automatically assigned.
* If the SCM login associated with an issue is longer than 255 characters including the characters for an issue author, the author will be left blank.
  {% endhint %}

### Issue life cycle <a href="#life-cycle" id="life-cycle"></a>

An issue can have one of the following statuses:

* **Open**: initial value after the first analysis. A user can reopen an **Accepted** or **False positive** issue. 
* **Accepted**: set by an authorized user if they decide to fix the issue later or not fix the issue. \
  SonarQube Cloud ignores **Accepted** issues in the ratings of the code but displays the number of **Accepted** issues in the various analysis snapshots.
* **False positive:** set by an authorized user if the analysis is mistaken. \
  SonarQube Cloud ignores **False positive** issues in the quality reports and the ratings of the code.
* **Fixed**: set by SonarQube Cloud after a subsequent analysis if the previously open issue has been fixed in the code (is no longer being detected). \
  SonarQube Cloud purges **Fixed** issues after 30 days.

{% hint style="info" %}
If users tend to mark a lot of issues as **False positive**, it means that some coding rules are not appropriate for the project. In that case, rules can be deactivated in quality profiles or the analysis scope of the project can be adjusted to exclude files. See [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention") and the [setting-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope "mention") pages for more information.
{% endhint %}

The figure below shows the issue life cycle.

<figure><img src="broken-reference" alt="The different statuses an issue can have during its lifecycle in SonarQube"><figcaption></figcaption></figure>
