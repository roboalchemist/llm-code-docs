# Source: https://docs.bito.ai/ai-code-reviews-in-git/code-review-analytics.md

# Code review analytics

The user-friendly [**Code Review Analytics**](https://alpha.bito.ai/home/dashboard?view=overview) dashboards help you track key metrics such as pull requests reviewed, issues found, lines of code reviewed, and understand individual contributions.

This helps you identify trends and optimize your development workflow.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKxLzGfPTC4vu4aOQKb9O%2Fscrnli_Ir0TnJTHsuycit.png?alt=media&#x26;token=e64bd906-58d6-4fad-a9e7-efb7d1dff7b2" alt=""><figcaption><p>Code Review Analytics dashboard</p></figcaption></figure>

Bito provides four distinct analytical views to help you understand your code review performance from multiple perspectives:

1. [**Overview**](#overview-dashboard): High-level workspace metrics and trends
2. [**Submitter Analytics**](#submitter-analytics-dashboard): Individual contributor performance and patterns
3. [**Repository Analytics**](#repository-analytics-dashboard): Repository and language-specific insights
4. [**PR Analytics**](#pr-analytics-dashboard): Detailed pull request and issue tracking

## "Overview" dashboard

The [**Overview dashboard**](https://alpha.bito.ai/home/dashboard?view=overview) provides a comprehensive high-level view of your workspace's code review performance, showing pull requests reviewed, issues found, and their categorization.

### Key metrics:

* **Code Requests Reviewed - This Month**: Total number of code reviews completed by Bito, including both pull requests from git workflows and IDE-based reviews
* **Lines Reviewed - This Month**: Total lines of code analyzed across all pull request diffs
* **Repositories Reviewed - This Month**: Number of unique repositories that received code review coverage
* **Submitters - This Month**: Count of unique developers (based on Git handles) whose pull requests were reviewed by Bito
* **Issues Found - This Month**: Total number of issues identified across all reviewed code
* **Issues Categories - This Month**: Visual breakdown of issues by primary categories (Security, Performance, Functionality, etc.)
  * *Note: When issues span multiple categories, Bito assigns the most relevant primary category*
* **Merged PRs - This Month**: Number of Bito-reviewed pull requests that were subsequently merged or closed
* **Issues Evaluated for Acceptance Rate - This Month**: Issues in merged pull requests evaluated for potential fixes
* **Acceptance Rate (Merged PRs) - This Month**: Percentage of agent-identified issues that were potentially addressed
  * *Calculated based on code changes detected in related hunks when pull requests were merged*
  * *Available for reviews conducted on or after August 8th, 2024*
  * *Note: This is an approximation based on code change detection*
* **Pull Requests Skipped - This Month**: Pull requests excluded from review due to:
  * Matching exclusion filters in agent configuration
  * Empty diffs
  * Invalid Bito plan status
* **Skip Reason - This Month**: Breakdown of why specific pull requests were skipped

{% hint style="info" %}
Use the **Filters** button (top-right) to customize your view. You can also export the data to PowerPoint or PDF using the **Share menu** button (top-right).
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqJ0D9jAs0glc0H9ROZJR%2Fscrnli_yyMt5LrYSUQ3qJ.png?alt=media&#x26;token=e16114e3-7331-402e-972a-425239827e85" alt=""><figcaption></figcaption></figure>

## "Submitter Analytics" dashboard

The [**Submitter Analytics dashboard**](https://alpha.bito.ai/home/dashboard?view=Submitter_Analytics) helps you gain insights into individual contributor patterns and performance with user-level statistics and visualizations.

### Key metrics:

* **Pull Requests Reviewed - This Month**: Number of pull requests reviewed for each developer. It helps you identify most active team members.
  * Shows top 30 contributors by pull request count
  * Remaining contributors aggregated under 'Other'
* **Lines of Code Reviewed - This Month**: Lines of code reviewed by Bito per developer. It is useful for understanding workload distribution.
  * Displays contributors with minimum 100 lines reviewed
  * Top 30 contributors shown individually
  * Remaining contributors grouped under 'Other'
* **Issues Reported Per 1K Lines - This Month**: Issue density normalized by code volume for developers with at least 1,000 lines of code, enabling fair comparison across different contribution levels. It helps identify patterns in code quality by developer
* **Issue Distribution by Category - This Month**: Breakdown of issues by type for each developer, showing both total count and percentage. Categories with fewer than 5 issues are excluded, with bar height representing total issues and width showing percentage distribution. It helps identify individual strengths and areas for improvement.

{% hint style="info" %}
Use the **Filters** button (top-right) to customize your view. You can also export the data to PowerPoint or PDF using the **Share menu** button (top-right).
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FYwQ2asUTRCbyoOknsNn3%2Fscrnli_Yl7Tdpt26UqS9f.png?alt=media&#x26;token=494a6728-7373-46eb-8676-9c4032c6d700" alt=""><figcaption></figcaption></figure>

## "Repository Analytics" dashboard

The [**Repository Analytics dashboard**](https://alpha.bito.ai/home/dashboard?view=Repository_Analytics) helps you understand repository-level performance and language-specific trends across your codebase.

### Key metrics:

* **Pull Requests Reviewed - This Month**: Review activity across repositories (top 30 shown, remainder grouped as 'Other'). It identifies which codebases receive most attention.
* **Lines of Code Reviewed (Repo) - This Month**: Lines of code reviewed by Bito in each repository (top 30 displayed individually). It helps you understand where development effort is concentrated.
* **Lines of Code Reviewed (Language) - This Month**: Breakdown of reviewed code by programming language. It is useful for resource allocation and expertise planning.
* **Issues Reported Per 1K Lines (Repo) - This Month**: Issue density for repositories with at least 1,000 lines of changes. It identifies repositories that may need additional attention
* **Issues Reported Per 1K Lines (Language) - This Month**: Issue rates across different programming languages (minimum 100 lines required). It helps you identify language-specific training needs.
* **Issue Distribution by Category × Language - This Month**: Issues categorized by both type and programming language, with visualization showing total count (bar height) and percentage distribution (bar width). Categories with fewer than 5 issues excluded. It reveals language-specific issue patterns.
* **Issue Distribution by Category × Repo - This Month**: Issues analyzed across category and repository dimensions, excluding categories with fewer than 5 issues. The visualization shows total issues (bar height) and percentage distribution (bar width). It identifies repository-specific issue trends.

{% hint style="info" %}
Use the **Filters** button (top-right) to customize your view. You can also export the data to PowerPoint or PDF using the **Share menu** button (top-right).
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FooK9QmyVwWBYNrvttO9o%2Fscrnli_4gE0fJ9rkURd5b.png?alt=media&#x26;token=5824e6d1-a2b6-4cd1-9352-54915880adf7" alt=""><figcaption></figcaption></figure>

## "PR Analytics" dashboard

The [**PR Analytics dashboard**](https://alpha.bito.ai/home/dashboard?view=PR_Analytics) helps you dive deep into individual pull request performance with detailed pull request and issue-level analytics.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXudgINW1mbwoPtnazD78%2Fscrnli_II4AGo4vqv2vVE.png?alt=media&#x26;token=e7a12ffb-3f68-4b03-af66-fa6663c1dd01" alt=""><figcaption></figcaption></figure>

The dashboard organizes pull requests into three tabs:

### **1. "Reviewed (Feedback)" tab**

* Shows pull requests where Bito provided actionable feedback
* These pull requests contain issues that require your attention
* Click any pull request to access comprehensive details including every feedback item with its category (Security, Performance, Linter, Functionality, etc.), affected programming language, and direct links to the specific code location within the pull request for quick reference.
* Useful for tracking reviews that generated value

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fkegk2JYQHNFNdJgHpBJq%2Fscrnli_22JO8JVrE9yVoM.png?alt=media&#x26;token=48aa58b4-a94b-4b7c-a350-ff27c21a4748" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FWW4ljirRWUKEBGEHAKoL%2Fscrnli_E38sxBtZlAhnF5.png?alt=media&#x26;token=f1c178a7-eaf5-4aa1-a32e-dc05b9b1b0b7" alt=""><figcaption></figcaption></figure>

### **2. "Reviewed (No Feedback)" tab**

* Shows pull requests that Bito reviewed but found no actionable issues
* Indicates clean code submissions

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FxCfH9nvhHWZrm3LaFHz0%2Fscrnli_90KG4YxvxuK0RP_1.png?alt=media&#x26;token=814f9f19-8ca6-4960-bc88-34b197ce60c3" alt=""><figcaption></figcaption></figure>

### **3. "Skipped" tab**

* Shows pull requests that Bito didn't review due to configuration settings or other constraints
* Includes skip reasons for transparency

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FkveUgvqJzQjAZZ6I9n1R%2Fscrnli_02ms4739jUKR2y_1.png?alt=media&#x26;token=6c8e777c-65b2-4924-bdab-d7b24055d524" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Use the **Filter** button (top-left) to customize views by:

* Specific submitters
* Date ranges
* Pull request status
  {% endhint %}

## **Benefits for technical leadership**

The detailed code review analytics reports enables tech leads and reviewers to:

* **Trace patterns**: Identify recurring issues across pull requests
* **Spot trends**: Recognize systematic problems in code quality
* **Connect insights**: Link high-level analytics to specific code examples
* **Targeted mentoring**: Provide specific guidance based on actual code issues
* **Process improvement**: Adjust development practices based on concrete data

## Best practices for using analytics

#### 1. Regular review cadence

* Check [Overview](#overview-dashboard) metrics for trend monitoring
* Review [Submitter Analytics](#submitter-analytics-dashboard) for team performance discussions
* Analyze [Repository Analytics](#repository-analytics-dashboard) for strategic planning
* Use [PR Analytics](#pr-analytics-dashboard) for issue tracking and mentoring

#### 2. Filtering for insights

* Use date filters to compare time periods
* Filter by specific teams or repositories during retrospectives
* Focus on high-activity contributors or repositories for targeted improvements

#### 3. Export and sharing

* Export monthly reports for stakeholder updates
* Share repository-specific insights with relevant teams
* Use PowerPoint exports for executive presentations
* Archive PDF reports for compliance or historical analysis

#### 4. Action-oriented analysis

* Identify submitters who might benefit from additional code review training
* Focus attention on repositories with high issue density
* Address language-specific patterns through targeted workshops
* Use acceptance rate trends to validate review effectiveness
