# Source: https://docs.bito.ai/ai-code-reviews-in-git/request-changes-comments.md

# Request changes comments

Bito’s **Request changes comments** feature helps enforce code quality by blocking merges until all AI-generated review comments are resolved—fully supported in GitHub, GitLab, and Bitbucket.

When enabled, Bito identifies actionable issues in pull requests and posts them as **formal “Request changes” review comments**. If your repository uses **branch protection rules** that require all review conversations to be resolved before merging, Bito’s flagged comments will automatically block the pull request until addressed.

This ensures developers don’t accidentally merge incomplete or unreviewed code.

{% embed url="<https://youtu.be/E_2awjmFBfo>" %}

## How it works

### 1. Enable comment resolution rules in your Git provider

#### **GitHub:**

* Go to your repository → **Settings** → **Branches**
* Create or edit a branch protection rule (e.g., for `main`)
* Enable:
  * ✅ Require a pull request before merging
  * ✅ Require conversation resolution before merging

#### **GitLab:**

* Go to your project → **Settings** → **Merge requests**
* Under **Merge checks**, enable:
  * ✅ All threads must be resolved
* Click **Save changes** button.

#### **Bitbucket:**

* Go to your repository → **Repository settings** → **Branch restrictions**
* Click **Add a branch restriction** button.
* Under **Select branches**, define the target branches where this restriction should apply. Pull requests merging into these branches will be blocked until all "Request changes" comments are resolved. You can choose one of two options:
  * **By branch name or pattern**: Enter a specific branch name (e.g., `main`) or use a wildcard pattern to cover multiple branches. For example, using an asterisk `*` applies the restriction across all branches, while `release/*` applies it to every release branch.
  * **By branch type**: Select a branch type (e.g., `development`, `release`) from the dropdown menu.
* Switch to **Merge settings** tab.
* Under **Merge checks**, enable:
  * ✅ No changes are requested
* Under **Merge conditions**, enable:
  * ✅ Prevent a merge with unresolved merge checks
  * ***Note:** This setting is only available if your organization uses **Bitbucket Cloud Premium**. It will block anyone from merging the PR if there are unresolved "request change" comments.*\
    *On **Standard Bitbucket Cloud**, this option is unavailable; users will see a warning if they attempt to merge with unresolved "request change" comments, but the merge will still be allowed.*
* Click **Save** button.

{% hint style="info" %}
**Note:** Request change comments usually have to be resolved by the person who posted them. Since here these comments are posted by Bito, the user must comment **`/resolve`** in the pull request to resolve them.
{% endhint %}

### 2. Turn on “Request changes comments” in Bito

* Go to **Repositories** in the Bito dashboard.
* Click on **Settings** for your desired AI Code Review Agent instance.
* Enable the toggle: **“Request changes comments”**
* Save changes

When this is on, Bito will flag **actionable AI feedback** as formal review comments requiring resolution. Informational or minor suggestions will remain as regular comments.

### 3. What happens in a pull request

* Bito runs an AI code review on your pull request or merge request.
* Actionable issues are posted as **change requests**.
* Your Git provider treats these comments according to your configured merge rules.
* If comment resolution is required, the merge is blocked until the flagged issues are resolved.

## Example workflow

1. Developer opens a pull request or merge request.
2. Bito reviews the code and posts a “request change” comment on a problematic line.
3. The Git provider blocks the merge due to unresolved comments or threads.
4. Developer fixes the issue and marks the thread as resolved.
5. Merge becomes possible once all conditions are met.

## Why use this feature?

* Enforces follow-up on critical AI-detected issues.
* Works natively with GitHub, GitLab, and Bitbucket workflows.
* Ensures only reviewed and clean code gets merged.
* Helps maintain consistent code quality at scale.
