# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-github-actions.md

# Install/run via GitHub Actions

## Prerequisites

* **Bito Access Key:** Obtain your Bito Access Key. [**View Guide**](https://docs.bito.ai/help/account-and-settings/access-key)
* **GitHub Personal Access Token (Classic):** For GitHub PR code reviews, ensure you have a CLASSIC personal access token with repo access. We do not support fine-grained tokens currently. [**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBZH0vDwrPqYQPMIxIyNW%2Fimage.png?alt=media&#x26;token=a4c42d8d-61a5-4cdb-87a1-622c0ba8f1ae" alt=""><figcaption><p><strong>GitHub Personal Access Token (Classic)</strong></p></figcaption></figure>

***

## Installation and Configuration Steps:

1. **Enable GitHub Actions:**
   * Login to your [GitHub](https://github.com/) account.

   * Open your repository and click on the "Settings" tab.

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvHdaHm4Z56JwiwmEFP6s%2Fscrnli_2_21_2024_3-01-34%20AM.png?alt=media&#x26;token=032babc3-47ef-46bc-b077-387717ad37fb" alt=""><figcaption></figcaption></figure>

   * Select "Actions" from the left sidebar, then click on "General".

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FA0Zjef3Jhzo4JYTtCxqc%2Fscrnli_2_21_2024_3-06-05%20AM.png?alt=media&#x26;token=f4231134-afed-4978-888f-1c250f0bf12e" alt=""><figcaption></figcaption></figure>

   * Under "Actions permissions", choose "Allow all actions and reusable workflows" and click "Save".

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNjcCGFCnyxfBVTjJPT5Q%2Fscrnli_2_21_2024_3-08-42%20AM.png?alt=media&#x26;token=70f465bf-8623-479a-a437-aed85c6b1605" alt=""><figcaption></figcaption></figure>

2. **Set Up Environment Variables:**
   * Still in the "Settings" tab, navigate to "Secrets and variables" > "Actions" from the left sidebar.

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKLj5Wg3Ip6u58RHA3s1E%2Fscrnli_2_21_2024_3-11-29%20AM.png?alt=media&#x26;token=8700dac2-cd6e-484a-a22a-25245d6a664a" alt=""><figcaption></figcaption></figure>

   * **Configure the following under the "Secrets" tab:**

     For each secret, click the **New repository secret** button, then enter the exact name and value of the secret in the form. Finally, click **Add secret** to save it.

     * **Name:** `BITO_ACCESS_KEY`
       * **Secret:** Enter your Bito Access Key here. Refer to the [guide for obtaining your Bito Access Key](https://docs.bito.ai/help/account-and-settings/access-key#creating-an-access-key).
     * **Name:** `GIT_ACCESS_TOKEN`
       * **Secret:** Enter your GitHub Personal Access Token (Classic) with repo access. We do not support fine-grained tokens currently. For more information, see the [Prerequisites](#prerequisites) section.

{% hint style="info" %}
Check the above ["Prerequisites"](#prerequisites) section to learn more about creating the access tokens needed to configure the Agent.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FI6QvP52ueBYA9tsFQ7l5%2Fscrnli_5_8_2024_9-16-14%20PM.png?alt=media&#x26;token=2fe9491d-175f-4576-831f-8b7385ada5cb" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FIDpWabR1EZLLGXzxCyHC%2Fscrnli_2_21_2024_3-16-52%20AM.png?alt=media&#x26;token=424856b3-49c8-432a-be7c-60549bf876da" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FGuEDWm1KqYCrNTZOqM6p%2Fscrnli_5_8_2024_9-00-51%20PM.png?alt=media&#x26;token=4f92c5a3-42a0-4b4a-aeef-b2c8df065b41" alt=""><figcaption></figcaption></figure>

* **Configure the following under the "Variables" tab:**

  For each variable, click the **New repository variable** button, then enter the exact name and value of the variable in the form. Finally, click **Add variable** to save it.

  * **Name:** `STATIC_ANALYSIS_TOOL`
    * **Value:** Enter the following text string as value: `fb_infer,astral_ruff,mypy`
  * **Name:** `GIT_DOMAIN`
    * **Value:** Enter the domain name of your Enterprise or self-hosted GitHub deployment or skip this if you are not using Enterprise or self-hosted GitHub deployment.
    * **Example of domain name:** `https://your.company.git.com`
  * **Name:** `EXCLUDE_BRANCHES`
    * **Value:** Specify branches to exclude from the review by name or valid glob/regex patterns. The agent will skip the pull request review if the source or target branch matches the exclusion list.
    * **Note:** For more information, see [**Source or Target branch filter**](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#source-or-target-branch-filter).
  * **Name:** `EXCLUDE_FILES`
    * **Value:** Specify files/folders to exclude from the review by name or glob/regex pattern. The agent will skip files/folders that match the exclusion list.
    * **Note:** For more information, see [**Files and folders filter**](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#files-and-folders-filter).
  * **Name:** `EXCLUDE_DRAFT_PR`
    * **Value:** Enter `True` to disable automated review for draft pull requests, or `False` to enable it.
    * **Note:** For more information, see [**Draft pull requests filter**](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#draft-pull-requests-filter).

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMQ6h8wLoIqq1xVMtEtpr%2Fscrnli_5_8_2024_9-06-44%20PM.png?alt=media&#x26;token=13b7916d-157f-444c-9a1e-b36da99a4d6f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FcyXbRNa1JYxzj2a1c5Kq%2Fscrnli_5_8_2024_9-05-52%20PM.png?alt=media&#x26;token=249cdd7a-3af4-4e4a-84e0-e8b3131e5cbb" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FiZGNOMmwNgetznzOpd3g%2Fscrnli_6_8_2024_2-42-08%20PM.png?alt=media&#x26;token=d337d0a1-d55d-4cb3-876c-806337847de8" alt=""><figcaption></figcaption></figure>

3. **Create the Workflow Directory:**
   * In your repository, create a new directory path: `.github/workflows`.

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5DqiIeX3txynw6vpvCiM%2Fscrnli_2_21_2024_3-26-03%20AM.png?alt=media&#x26;token=152acdbf-7c37-4362-b31b-497fbe0c38d8" alt=""><figcaption></figcaption></figure>

4. **Add the Workflow File:**
   * [**Download this `test_cra.yml` file**](https://github.com/gitbito/codereviewagent/blob/main/.github/workflows/test_cra.yml) from AI Code Review Agent's GitHub repo.

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fh4LN96R8F82Y1GYnfsd9%2Fscrnli_4_25_2024_11-33-39%20AM.png?alt=media&#x26;token=e6a5a35c-30d2-4420-8f68-7a978d82cb1f" alt=""><figcaption></figcaption></figure>

   * In your repository, upload this `test_cra.yml` file inside the `.github/workflows` directory either in your source branch of each PR or in a branch (e.g. main) from which all the source branches for PRs will be created.

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FgpBbMpIdcmNoAzRPQOfz%2Fscrnli_2_21_2024_3-30-18%20AM.png?alt=media&#x26;token=1b48e29b-973e-4c4e-a56f-89a01823798b" alt=""><figcaption></figcaption></figure>

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfeuTY2qVrnDM9KECS7Nw%2Fscrnli_2_21_2024_3-35-03%20AM.png?alt=media&#x26;token=14793b09-2082-4a7e-985f-b5bb03bdfaa6" alt=""><figcaption></figcaption></figure>

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBHt1t7XeGt0NfW5S8SyF%2Fscrnli_2_21_2024_3-36-52%20AM.png?alt=media&#x26;token=70184475-2a52-468d-8f3d-82aad598acd4" alt=""><figcaption></figcaption></figure>

   * Commit your changes.

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F9y1cx93l2yEq6uMyn5mj%2Fscrnli_2_21_2024_3-39-40%20AM.png?alt=media&#x26;token=9a58194c-4d80-408f-b01a-f24de236c6ba" alt=""><figcaption></figcaption></figure>

     <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvHx8lu7qa5sgb3FJWUvY%2Fscrnli_2_21_2024_3-42-14%20AM.png?alt=media&#x26;token=9a788f5a-4d6e-4caf-a113-9b392e5efb02" alt=""><figcaption></figcaption></figure>

## Customizations for self-hosted GitHub

1. Create a self-hosted Runner using Linux image and x64 architecture as described in the [**GitHub documentation**](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners).
2. Create a copy of Bito's repository [**gitbito/codereviewagent**](https://github.com/gitbito/CodeReviewAgent) main branch into your self-hosted GitHub organization e.g. "myorg" under the required name e.g. "gitbito-bitocodereview". In this example, now this repository will be accessible as "myorg/gitbito-bitocodereview".
3. Update `test_cra.yml`as below:
   * **Change line from:**
     * runs-on: ubuntu-latest
   * **to:**
     * runs-on: \<label of the self-hosted GitHub Runner> e.g. self-hosted, linux etc.
4. Update `test_cra.yml`as below:
   * **Replace all lines having below text:**
     * uses: gitbito/codereviewagent\@main
   * **with:**
     * uses: myorg/gitbito-bitocodereview\@main
5. Commit and push your changes in `test_cra.yml` .

## Using the AI Code Review Agent

After configuring the GitHub Actions, you can invoke the AI Code Review Agent in the following ways:

{% hint style="info" %}
**Note:** To improve efficiency, the AI Code Review Agent is disabled by default for pull requests involving the **"main"** branch. This prevents unnecessary processing and token usage, as changes to the **"main"** branch are typically already reviewed in release or feature branches. To change this default behavior and include the **"main"** branch, please [**contact support**](mailto:support@bito.ai).
{% endhint %}

1. **Automated Code Review**: The agent will automatically review new pull requests as soon as they are created and post the review feedback as a comment within your PR.
2. **Manually Trigger Code Review:** To start the process, simply type **`/review`** in the comment box on the pull request and submit it. This command prompts the agent to review the pull request and post its feedback directly in the PR as a comment.

   Bito also offers specialized commands that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.

   * **`/review security`:** Analyzes code to identify security vulnerabilities and ensure secure coding practices.
   * **`/review performance`:** Evaluates code for performance issues, identifying slow or resource-heavy areas.
   * **`/review scalability`:** Assesses the code's ability to handle increased usage and scale effectively.
   * **`/review codeorg`:** Scans for readability and maintainability, promoting clear and efficient code organization.
   * **`/review codeoptimize`:** Identifies optimization opportunities to enhance code efficiency and reduce resource usage.

   By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**

   For more details, refer to [Available Commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FryhzTFegsxvL4eoZewT7%2Fscrnli_2_28_2024_8-57-29%20PM.png?alt=media&#x26;token=af92cdfb-089b-4f95-8200-52adebe366dd" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull request.
{% endhint %}

## Screenshots

### Screenshot # 1

{% hint style="info" %}
*AI-generated pull request (PR) summary*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fk5wsTj4siolCcaZqHRIX%2Fscrnli_9_13_2024_12-33-56%20PM.png?alt=media&#x26;token=63cb7da9-21ca-41a1-83ba-9b107d07a6cf" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a pull request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the pull request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FP0sUIAZ3Lq0FqL9ytfPF%2Fscrnli_9_13_2024_12-49-29%20PM_cropped_3.png?alt=media&#x26;token=d74d3b27-4831-4735-9559-6f9da191e910" alt=""><figcaption></figcaption></figure>
