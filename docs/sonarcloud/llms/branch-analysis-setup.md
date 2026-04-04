# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis-setup.md

# Branch analysis setup

Setting up branch analysis enables SonarQube Cloud to analyze branches in your project *other than the main branch and pull request branches*. To enable branch analysis, your project must be set up for build-based analysis, not automatic analysis. Branch analysis is not available with automatic analysis.

As with all build-based analyses, the code analysis is performed by the SonarScanner software installed in your build environment and the results are sent to the SonarQube Cloud server for processing and display.

Using a SonarQube Cloud-integrated CI for your builds will make configuration simpler, though setting up branch analysis with a local build environment or a non-integrated CI is also possible. Both options are covered below.

### Setup with a SonarQube Cloud-integrated CI <a href="#setup-with-a-sonarcloud-integrated-ci" id="setup-with-a-sonarcloud-integrated-ci"></a>

Using a SonarQube Cloud-integrated CI simplifies the setup of branch analysis. The integrated CIs are:

* GitHub Actions
* Bitbucket Pipelines
* Azure Pipelines
* GitLab CI
* CircleCI
* Travis CI

Here we use GitHub Actions as an example. Other CIs have different configuration details, so you will need to adapt this example accordingly.

If you followed the in-product tutorial, then you should already have configured your build definition (for example, `.github/workflows/build.yml` in GitHub Actions) for main branch analysis.

For our purposes, the most important section is the part that triggers the workflow on every push to the main branch. In GitHub Actions it looks like this:

```yaml
on:
  push:
    branches:
      - main    # The default branch
```

This is the section that you need to change to enable branch analysis. You simply need to add a directive so that the workflow is triggered not just on each push to the main branch, but also on each push to the other branch (or branches) that you want to analyze.

For example, to enable analysis on all branches with the pattern `branch-*`, you would change this section of `build.yml` to

```yaml
on:
  push:
    branches:
      - main        # The default branch
      - branch-*    # The other branches to be analyzed
```

You should make sure that this newly altered `build.yml` file is checked-in to all the `branch-*` branches. It is good practice to check it into *all* branches, including the main branch, in identical form.

Now, whenever you push a commit to the main branch, the analysis will run and the results will appear on SonarQube Cloud on the main branch page of your project.

Similarly, whenever you push a commit to any branch matching the pattern `branch-*`, the analysis will also run and the result will appear on SonarQube Cloud on the page for that branch.

#### Under the hood <a href="#under-the-hood" id="under-the-hood"></a>

Internally, when the SonarScanner performs a branch analysis in an integrated CI, it automatically sets two *analysis parameters*:

* `sonar.branch.name`: The name of the branch that was analyzed.
* `sonar.branch.target`: The name of the target branch of the branch that was analyzed.

This data is sent up to SonarQube Cloud alongside the analysis results and allows SonarQube Cloud to display the results correctly.

In a non-integrated CI, these parameters must be set manually as part of the configuration of branch analysis. See *Setup with non-integrated CI*, below, for details.

Additionally, in some special cases, even with an integrated CI, you may need to manually set the `sonar.branch.target` parameter. See *Target branch*, below, for details.

### Setup with a non-integrated build environment <a href="#setup-with-a-non-integrated-build-environment" id="setup-with-a-non-integrated-build-environment"></a>

A non-integrated build environment is any build environment (cloud-based CI, local, etc) for which SonarQube Cloud does not provide integration and therefore cannot automatically determine the `sonar.branch.*` analysis parameters. In this case, you need to manually configure these parameters.

Let’s say you want to set up analysis for a branch called `branch-1`. First of all, you would follow the same steps as for the integrated CI:

* Set up your project as described in the in-product tutorial (this sets up main branch analysis)
* Set up your build script so that, in addition to building on each push to the main branch, a build is also triggered on each push to `branch-1`

At this point, you would be done if you were using an integrated CI. For a non-integrated environment you must, additionally, manually set the analysis parameters. For example:

* `sonar.branch.name = branch-1`
* `sonar.branch.target = main`

Where you make this configuration depends on the language you are analyzing and the build tools you are using. The in-product tutorial will indicate where you configure the parameters for your specific case.

### Long-lived and short-lived branches <a href="#long-lived-and-short-lived-branches" id="long-lived-and-short-lived-branches"></a>

In most development processes there are effectively two types of branches, used for two different purposes: long-lived branches and short-lived branches. SonarQube Cloud allows you to indicate the type of a branch using a naming convention (see *Branch name pattern*, below). This lets the system adjust how it analyzes a branch and how it displays the results.

#### Long-lived branches <a href="#longlived-branches" id="longlived-branches"></a>

A *long-lived branch* is a branch that plays a continuous role within the development process of a software project. The main branch of a repository is always considered a long-lived branch, usually representing the next release of the project.

Branches representing previous versions of a project are typically also considered long-lived. In addition, some development workflows use a long-running `develop` or `next` branch (the naming may differ) that runs parallel to the main branch. Such branches are also considered long-lived.

In general, long-lived branches are those that exist side-by-side with the main branch for a relatively long time.

#### Short-lived branches <a href="#shortlived-branches" id="shortlived-branches"></a>

Short-lived branches are those that are intended to exist only temporarily. They are typically a child branch of a long-lived branch and are intended to be merged back into that parent branch within a relatively short period. They include feature branches and bug-fix branches.

#### Pull requests and short-lived branches <a href="#pull-requests-and-shortlived-branches" id="pull-requests-and-shortlived-branches"></a>

Short-lived branch analysis and pull request analysis are two separate features of SonarQube Cloud that can sometimes be confused.

Creating a pull request involves the creation of a branch. This is usually called a "feature" or "bug-fix" branch and it is indeed typically "short-lived". This is the branch that holds the changes that will be merged into the main branch (or another long-lived branch) on approval. SonarQube Cloud pull request analysis is part of that approval process and ensures that only high-quality code is merged.

For more detailed information, see [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention").

*However, short-lived branch analysis in SonarQube Cloud does not refer to the analysis of these pull request branches*.

Instead, short-lived branch analysis is about analyzing feature and bug-fix branches that are *not part of a pull request*. These usually occur in projects that, for whatever reason, do not use pull requests at all, but want to achieve the same objective as pull request analysis, namely, ensuring only high-quality code is merged.

In short, if you already use PRs in your project, then you don’t need short-lived branch analysis. Pull request analysis offers more features (pull request decoration, for example) and requires no configuration. Short-lived branch analysis is only useful in the special case where you want to have (some of) the functionality of pull request analysis, but you do not use PRs in your project workflow.

For more detailed information, see [#short-lived-branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/branch-analysis#short-lived-branch-analysis "mention").

#### Branch name pattern <a href="#branch-name-pattern" id="branch-name-pattern"></a>

You can set a long-lived branches name pattern at the project level and, only with the Enterprise plan, at the organization level. The project-level configuration overrides the organization-level configuration.

### New code with long- and short-lived branches <a href="#new-code-with-long-and-short-lived-branches" id="new-code-with-long-and-short-lived-branches"></a>

The distinction between new code and overall code is a key part of the SonarQube Cloud methodology. See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") fore more details.

The new code definition for all long-lived branches, including the main branch, is the project-level new code definition.

For short-lived branches, the new code consists of all those files which have been modified or added relative to the target branch. Modified files are determined by comparing checksums between the `sonar.branch.target` branch and the short-lived branch to be analyzed.

### Quality gates with long- and short-lived branches <a href="#quality-gates-with-long-and-short-lived-branches" id="quality-gates-with-long-and-short-lived-branches"></a>

For long-lived branches, including the main branch:

* The quality gate defined at the project level is used.
* Both the conditions defined on overall code and conditions defined on new code are applied.
* And, what counts as new code is determined by the prevailing new code definition setting for the branch, as described above.

For short-lived branches:

* The quality gate defined at the project level is used.
* But, only conditions defined on new code are applied.
* And, new code is defined as whatever has changed relative to the parent branch, as described above.

### Target branch <a href="#target-branch" id="target-branch"></a>

The parameter `sonar.branch.target` specifies the target branch of the branch indicated by `sonar.branch.name`.

If `sonar.branch.name` is a *long-lived branch* **B**, then `sonar.branch.target` **T** is the *reference branch* of **B**. This means that issues from **T** will be copied to **B** on the first analysis of **B**. See **Issue synchronization,** below.

If `sonar.branch.name` is a *short-lived branch* **S**, then `sonar.branch.target` **T** is the *intended merge target* of **S**. This means that when analyzing **S**, SonarQube Cloud will only consider code that differs from that in **T**.

### Issue synchronization <a href="#issue-synchronization" id="issue-synchronization"></a>

For any long-lived branch **B** with target branch **T**, during the first analysis only, issues (including their type, severity, status, assignee, changelog, and comments) are copied from **T** to **B**. A comment is added to the changelog of each such issue in **B**:

*This issue has been copied from branch **T** to branch **B**.*

Then, at each subsequent analysis of the long-lived branch, any new issue in **B** that comes from merging a short-lived branch **S** into **B** automatically inherits the attributes (type, severity, etc.) that the issue had in **S**. A comment is added to the changelog of the issue in **B**:

*This issue had been copied from branch **S** to branch **B**.*

For short-lived branches, the issues visible upon analysis are the new issues corresponding to files added or modified in that branch. Modified files are determined by comparing the `sonar.branch.target` branch and the short-lived branch to be analyzed.

Note that the target branch of any branch (short- or long-lived) must itself always be a long-lived branch.

### SonarQube for IDE <a href="#sonarlint" id="sonarlint"></a>

In all SonarQube for IDE products, only issues from a project’s main branch and long-lived branches will be synchronized.

This means that when using Connected Mode with SonarQube for IntelliJ, Visual Studio, VS Code, and Eclipse, issues on short-lived branches are not synchronized. When an issue is marked in SonarQube Cloud as accepted or false positive on a short-lived branch, SonarQube for IDE will still show that issue in the IDE.

### Other settings <a href="#other-settings" id="other-settings"></a>

Other settings, including those for quality profiles, are set at the organization and/or project level. These settings do not differ between long- and short-lived branches and cannot be configured on a per-branch basis.

### Changing the name of a branch <a href="#changing-the-name-of-a-branch" id="changing-the-name-of-a-branch"></a>

The name of a branch, including the main branch, can be changed on the SonarQube Cloud side, on the **Branches** page of the SonarQube Cloud UI.

If you change the name of a branch in the SonarQube Cloud UI you must make sure that the same change is made in the repository itself (in Git, when a branch is renamed, a new branch is created with the same content as the old one, and the old one is deleted). Additionally, in the case of changing the name of a non-main branch, you must also make sure that the same change is made in the analysis parameters (the `sonar.branch.*` properties).

Note that the type of branch (long- vs short-lived) in SonarQube Cloud cannot be changed, even if the name is changed in such a way that it now matches the naming pattern of a different type. For example, if the name of a branch initially matches the long-lived name pattern then it will be a long-lived branch for as long as it exists, even if its name is changed to something that no longer matches the pattern.

### Branch lifetimes <a href="#branch-lifetimes" id="branch-lifetimes"></a>

Long-lived branches are retained until you delete them manually (Administration > Branches). Short-lived branches are deleted automatically after 30 days with no analysis. For more details, see [housekeeping](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/housekeeping "mention").

### Effect of branches on LOC consumption <a href="#effect-of-branches-on-loc-consumption" id="effect-of-branches-on-loc-consumption"></a>

For purposes of paid or Enterprise SonarQube Cloud plans, the number of lines of code that your organization is considered to have is calculated by adding together the LOC of the single largest branch within each project in that organization. All smaller branches within each project are ignored.

{% hint style="info" %}
Code that has already been analyzed does not count toward the LOC limit determined by your license. You cannot use up your LOC limit by analyzing the same code repeatedly.
{% endhint %}
