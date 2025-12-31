# Source: https://docs.bito.ai/ai-code-reviews-in-git/key-features.md

# Key features

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)

## Features overview

A quick look at powerful features of [**Bito's AI Code Review Agent**](https://bito.ai/product/ai-code-review-agent/)—click to jump to details.

1. [**AI that understands your code**](#ai-that-understands-your-code)
2. [**One-click setup for GitHub, GitLab, and Bitbucket**](#one-click-setup-for-github-gitlab-and-bitbucket)
3. [**Automated and manually-triggered AI code reviews**](#automated-and-manually-triggered-ai-code-reviews)
4. [**Pull request summary**](#pull-request-summary)
5. [**Changelist**](#changelist)
6. [**One-click to accept suggestions**](#one-click-to-accept-suggestions)
7. [**Chat with AI Code Review Agent**](#chat-with-ai-code-review-agent)
8. [**Incremental code reviews**](#incremental-code-reviews)
9. [**Code review analytics**](#code-review-analytics)
10. [**Custom code review rules and guidelines**](#custom-code-review-rules-and-guidelines)
11. [**Multiple specialized engineers for targeted code analysis**](#multiple-specialized-engineers-for-targeted-code-analysis)
12. [**Integrated feedback from dev tools you use**](#integrated-feedback-from-dev-tools-you-use)
13. [**Jira integration**](#jira-integration)
14. [**Supports all major programming languages**](#supports-all-major-programming-languages)
15. [**Enterprise-grade security**](#enterprise-grade-security)

<p align="center"><a href="https://alpha.bito.ai/home/welcome" class="button primary">Start free trial</a><a href="https://bit.ly/bito-code-review-Demo" class="button secondary">Get a demo</a></p>

***

## AI that understands your code

The [AI Code Review Agent](https://bito.ai/product/ai-code-review-agent/) understand code changes in pull requests. It analyzes relevant context from your entire repository, resulting in more accurate and helpful code reviews.

To comprehend your code and its dependencies, it uses Symbol Indexing, Abstract Syntax Trees (AST), and Embeddings.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/">https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/</a></td></tr></tbody></table>

## One-click setup for GitHub, GitLab, and Bitbucket

[Bito Cloud](https://alpha.bito.ai/) offers a one-click solution for using the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud), eliminating the need for any downloads on your machine.

Bito supports integration with the following Git providers:

* [GitHub](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github)
* [GitHub (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github-self-managed)
* [GitLab](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab)
* [GitLab (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab-self-managed)
* [Bitbucket](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket)

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="install-run-using-bito-cloud">install-run-using-bito-cloud</a></td></tr></tbody></table>

## Automated and manually-triggered AI code reviews

By default, the AI Code Review Agent automatically reviews all new pull requests and provides detailed feedback.

To initiate a manual review, simply type **`/review`** in the comment box on the pull request and submit it. This action will start the code review process.

## Pull request summary

Get a concise overview of your pull request (PR) directly in the description section, making it easier to understand the code changes at a glance. This includes a summary of the PR, the type of code changes, whether unit tests were added, and the estimated effort required for review.

The agent evaluates the complexity and quality of the changes to estimate the effort required to review them, providing reviewers the ability to plan their schedule better. For more information, see [What is "Estimated effort to review" in code review output?](https://docs.bito.ai/faqs#what-is-estimated-effort-to-review-in-code-review-output)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOAsIyAImpHDNIOYoVHNM%2Fscrnli_7_12_2024_10-44-40%20PM_2.png?alt=media&#x26;token=fe51ea55-c006-4a23-b3c6-66262ecd7dc5" alt=""><figcaption><p>Summary of Pull Request in the description section.</p></figcaption></figure>

## Changelist

A tabular view that displays key changes in a pull request, making it easy to spot important updates at a glance without reviewing every detail. Changelist categorizes modifications and highlights impacted files, giving you a quick, comprehensive summary of what has changed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKvprpQl5Q6Q5cjQ0JDtI%2Fchangelist_by_bito.png?alt=media&#x26;token=90deeb82-25a6-401a-b26c-43f24dfd7965" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

## One-click to accept suggestions

The AI-generated code review feedback is posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.

You can accept the suggestions with a single click, and the changes will be added as a new commit to the pull request.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXeSZETfSx7uVpMdn6KD4%2Fscrnli_ypuJi4RX3JeL32_1.png?alt=media&#x26;token=83d2a18c-94da-481c-abd0-2bb4e0be341e" alt="One-click to accept AI code review suggestions"><figcaption><p>One-click to accept AI code review suggestions</p></figcaption></figure>

## Chat with AI Code Review Agent

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

Real-time collaboration with the AI Code Review Agent accelerates your development cycle. By delivering immediate, actionable insights, it eliminates the delays typically experienced with human reviews. Developers can engage directly with the Agent to clarify recommendations on the spot, ensuring that any issues are addressed swiftly and accurately.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FDLSrDW0fZeh5flN0awRY%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=88d024d5-e9b9-48b0-a0eb-7b42b355c296" alt="" width="563"><figcaption></figcaption></figure>

## Incremental code reviews

AI Code Review Agent automatically reviews only the recent changes each time you push new commits to a pull request. This saves time and reduces costs by avoiding unnecessary re-reviews of all files.

You can enable or disable incremental reviews using the [Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance).

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="https://bito.ai/blog/how-to-perform-ai-powered-incremental-code-reviews-with-bito/">https://bito.ai/blog/how-to-perform-ai-powered-incremental-code-reviews-with-bito/</a></td></tr></tbody></table>

## Code review analytics

Get in-depth insights into your org’s code reviews with user-friendly [Code Review Analytics](https://alpha.bito.ai/home/dashboard?view=overview) dashboard. Track key metrics such as pull requests reviewed, issues found, lines of code reviewed, and understand individual contributions.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FlInn8tc18zASv8l9iU24%2Fscrnli_7_12_2024_9-49-52%20PM.png?alt=media&#x26;token=ab7c9143-d65e-4fa3-8827-9eb0d634dc13" alt=""><figcaption><p>Code Review Analytics dashboard</p></figcaption></figure>

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="code-review-analytics">code-review-analytics</a></td></tr></tbody></table>

## Custom code review rules and guidelines

The AI Code Review Agent offers a flexible solution for teams looking to enforce custom code review rules, standards, and guidelines tailored to their unique development practices. Whether your team follows specific coding conventions or industry best practices, you can customize the Agent to suite your needs.

We support two ways to customize AI Code Review Agent’s suggestions:

1. [**Provide feedback on Bito-reported issues in pull requests**](https://docs.bito.ai/implementing-custom-code-review-rules#id-1-provide-feedback-on-bito-reported-issues), and the AI Code Review Agent automatically adapts by creating code review rules to prevent similar suggestions in the future.
2. [**Create custom code review guidelines via the dashboard**](https://docs.bito.ai/implementing-custom-code-review-rules#id-2-create-custom-code-review-guidelines). Define rules through the [**Custom Guidelines**](https://alpha.bito.ai/home/ai-agents/custom-guidelines) dashboard in Bito Cloud and apply them to agent instances in your workspace.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="implementing-custom-code-review-rules">implementing-custom-code-review-rules</a></td></tr></tbody></table>

## Multiple specialized engineers for targeted code analysis

The AI Code Review Agent acts as a team of specialized engineers, each analyzing different aspects of your pull request. You'll get specific advice for improving your code, right down to the exact line in each file.

The areas of analysis include:

* Security
* Performance
* Scalability
* Optimization
* Will this change break anything? Based on the diff can we include anything?
* Code structure and formatting (e.g., tab, spaces)
* Basic coding standards including variable names (e.g., ijk)

This multifaceted analysis results in more detailed and accurate code reviews, saving you time and improving code quality.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="../available-commands#review-scope">#review-scope</a></td></tr></tbody></table>

## Integrated feedback from dev tools you use

Elevate your code reviews by harnessing the power of the development tools you already trust. Bito's AI Code Review Agent seamlessly integrates feedback from essential tools including:

* **Static code analysis**
* **Open source security vulnerabilities check**
* **Linter integrations**
* **Secrets scanning** (e.g., passwords, API keys, sensitive information)

**Static code analysis**

Using tools like Facebook’s open-source fbinfer (available out of the box), the Agent dives deep into your code—tailored to each language—and suggests actionable fixes. You can also configure additional tools you use for a more customized analysis experience.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBbscfaNSN1GCmy4PSzkp%2Fscrnli_3_28_2024_5-33-27%20AM_1.png?alt=media&#x26;token=767d2abc-3b4e-4141-b5b0-5f8f5bf4a01e" alt=""><figcaption><p>Static Code Analysis feedback highlighting suggestions and fixes.</p></figcaption></figure>

**Open source security vulnerabilities check**

The AI Code Review Agent checks real-time for the latest high severity security vulnerabilities in your code, using [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) (available out of the box). Additional tools such as [Snyk](https://snyk.io/), or [GitHub Dependabot](https://github.com/dependabot) can also be configured.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FiLlr9WhjlOLIWgk52G9w%2Fscrnli_3_28_2024_5-08-00%20AM_1.png?alt=media&#x26;token=66382333-925d-4d9f-ada3-e14e6dd8c0a1" alt=""><figcaption><p>Showing high-severity security vulnerabilities report.</p></figcaption></figure>

**Linter integrations**

Our integrated linter support reviews your code for consistency and adherence to best practices. By catching common errors early, it ensures your code stays clean, maintainable, and aligned with modern development standards.

**Secrets scanning**

Safeguard your sensitive data effortlessly. With built-in scanning capabilities, the Agent checks your code for exposed passwords, API keys, and other confidential information—helping to secure your codebase throughout the development lifecycle.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="supported-programming-languages-and-tools">supported-programming-languages-and-tools</a></td></tr></tbody></table>

## Jira integration

Seamlessly connect Bito with Jira to automatically validate pull request code changes against linked Jira tickets. This ensures your implementations meet specified requirements through real-time, structured validation feedback directly in your pull requests.

Support for Jira Cloud and Jira Data Center setups enables flexible integrations, while multiple ticket-linking methods ensure accurate requirement tracking.

Boost your team's code quality, collaboration, and traceability with automated Jira ticket validation.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="jira-integration">jira-integration</a></td></tr></tbody></table>

## Supports all major programming languages

No matter if you're coding in Python, JavaScript, Java, C++, or beyond, our AI Code Review Agent has you covered. It understands the unique syntax and best practices of every popular language, delivering tailored insights that help you write cleaner, more efficient code—every time.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="supported-programming-languages-and-tools">supported-programming-languages-and-tools</a></td></tr></tbody></table>

## Enterprise-grade security

Bito and third-party LLM providers never store or use your code, prompts, or any other data for model training or any other purpose.

Bito is SOC 2 Type II compliant. This certification reinforces our commitment to safeguarding user data by adhering to strict security, availability, and confidentiality standards. SOC 2 Type II compliance is an independent, rigorous audit that evaluates how well an organization implements and follows these security practices over time.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="../privacy-and-security">privacy-and-security</a></td></tr></tbody></table>
