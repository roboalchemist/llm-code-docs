# Source: https://docs.bito.ai/changelog.md

# Changelog

{% hint style="info" %}
[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

{% hint style="info" %}
Looking for older updates? You can find them on our [**Previous releases**](https://docs.bito.ai/changelog/previous-releases) page.
{% endhint %}

## AI Code Review Agent - 19th Jan 2026

<mark style="color:blue;">**New feature**</mark>

**Introducing AI Code Reviews in CLI:** Get AI-powered code reviews directly in your terminal. Catch security vulnerabilities, bugs, and performance issues early – before they reach production.

Integrate seamlessly into your CI/CD pipeline!

Ship code with confidence knowing critical issues are caught early when they're cheapest to fix.

<a href="ai-code-reviews-in-cli/overview" class="button primary">Learn more</a>

## AI Architect - 12th Jan 2026

<mark style="color:blue;">**New feature**</mark>

**Kubernetes deployment support:** [AI Architect](https://docs.bito.ai/ai-architect/overview) now supports Kubernetes deployment alongside Docker Compose. Deploy to your existing K8s cluster to leverage enterprise orchestration, advanced scaling capabilities, and seamless integration with your containerized infrastructure.

<a href="ai-architect/install-ai-architect-self-hosted" class="button primary">Learn more</a>

## AI Architect - 11th Dec 2025

<mark style="color:blue;">**New feature**</mark>

**Introducing Bito's AI Architect:** [AI Architect](https://docs.bito.ai/ai-architect/overview) builds a knowledge graph of your codebase — from repos to modules to APIs — delivering deep codebase intelligence to the coding agents you already use (e.g. Claude Code, Cursor, Windsurf, GitHub Copilot, and more).

Get production-ready code in one shot, faster issue triaging, consistent design adherence, and smarter code reviews powered by deep understanding of your architecture, services, and patterns.

**Getting started:**

1. [**Download and install Bito's AI Architect**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted) — Get AI Architect from GitHub, run the setup script to connect your Git provider and LLMs, then index your repositories to build the knowledge graph
2. **Connect your coding agent** — Configure the MCP server in your preferred AI coding agent:
   * [Claude Code](https://docs.bito.ai/ai-architect/guide-for-claude-code)
   * [Cursor](https://docs.bito.ai/ai-architect/guide-for-cursor)
   * [Windsurf](https://docs.bito.ai/ai-architect/guide-for-windsurf)
   * [GitHub Copilot (VS Code)](https://docs.bito.ai/ai-architect/guide-for-github-copilot-vs-code)
   * [Junie (JetBrains)](https://docs.bito.ai/ai-architect/guide-for-junie-jetbrains)
   * [JetBrains AI Assistant](https://docs.bito.ai/ai-architect/guide-for-jetbrains-ai-assistant)

<a href="https://alpha.bito.ai/home/welcome/ai-architect" class="button primary">Try Bito's AI Architect</a><a href="ai-architect/overview" class="button secondary">Read documentation</a><a href="https://www.youtube.com/watch?v=qAMtZ41-xJY" class="button secondary">Watch demo</a>

## AI Code Review Agent - 10th Nov 2025

<mark style="color:blue;">**New feature**</mark>

**Repository-level Agent settings with `.bito.yaml`:** You can now customize [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) behavior for individual repositories using a `.bito.yaml` configuration file. This gives teams the flexibility to define repository-specific review settings, coding guidelines, and preferences while admins maintain centralized oversight and visibility from the Bito dashboard.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/agent-settings/repo-level-settings)

## Billing and plan updates - 5th Nov 2025 &#x20;

**New Professional plan and annual billing options:** We've introduced a new **Professional Plan** ($20/month per seat, billed annually) designed for growing teams that need advanced capabilities beyond our **Team Plan**.&#x20;

Additionally, **annual billing is now available** across all paid plans at a discounted rate.&#x20;

Our updated plan structure:&#x20;

* **Team:** $12/month per seat (billed annually) or $15/month per seat (billed monthly)
  * *Up to 25 seats per team*&#x20;
* **Professional:** $20/month per seat (billed annually) or $25/month per seat (billed monthly)
  * *Unlimited seats*&#x20;
* **Enterprise:** [Contact us for custom pricing](https://bit.ly/contact-bito-sales)

[Learn more](https://bito.ai/pricing/)

## AI Code Review Agent - 3rd Nov 2025

<mark style="color:blue;">**New feature**</mark>

**Project-aware code reviews:** The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now reads and uses guideline files that are commonly used by AI coding agents like Cursor, Windsurf, and Claude Code.

Simply add guideline files (`.cursor/rules/*.mdc`, `.windsurf/rules/*.md`, `CLAUDE.md`, `GEMINI.md`, or `AGENTS.md`) to your repository, and the agent automatically applies your project's standards when reviewing pull requests.

Bito comments based on these guidelines include a citation linking to the specific guideline, so you can see exactly which rule triggered the feedback.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/implementing-custom-code-review-rules#id-3-use-project-specific-guideline-files)

## AI Code Review Agent - 3rd Oct 2025

<mark style="color:blue;">**New feature**</mark>

**Support for Perforce and SVN:** The [Bito IDE extension](https://docs.bito.ai/ai-code-reviews-in-ide/overview) now supports AI code reviews for projects using Perforce and SVN, in addition to Git. This means developers working in enterprise or legacy environments can get the same automated code insights and faster feedback without needing to switch tools or workflows.

**New review option `uncommittedchanges`:** You can now review all uncommitted changes in one go, including both local (unstaged) changes and staged changes. This makes it easier to spot issues across your entire workspace, helping you fix problems earlier and keep your commits clean.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-ide/overview)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FoM9dEdizfJogjBRlYAJC%2Fscrnli_pX9BP8cQO3cX50.png?alt=media&#x26;token=0ac47f46-d975-4a5c-90cf-f649c65ccb9b" alt=""><figcaption></figcaption></figure>

## AI Code Review Agent - 19th Sep 2025

<mark style="color:blue;">**New feature**</mark>

**Simplified Bitbucket integration:** Say goodbye to API tokens! We've completely streamlined your Bitbucket integration experience. Instead of manually creating API tokens and filling out forms, you can now connect Bito to Bitbucket with just a few clicks by installing the Bito app directly.&#x20;

It's faster, more secure, and eliminates all the tedious setup steps.&#x20;

[**Check out our updated setup guide**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket) to get started.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMkEhUlMUfiK26rbEV9lS%2Fscrnli_jBYatEquCn4pVe.png?alt=media&#x26;token=9e3b91d5-1858-4e85-8405-2f1623aaf5a4" alt=""><figcaption></figcaption></figure>

## AI Code Review Agent - 11th Sep 2025

<mark style="color:blue;">**New feature**</mark>

**Introducing Jira integration:** Bito now automatically validates your pull requests against Jira ticket requirements, ensuring your code changes align perfectly with project specs.

Reviewers no longer need to manually cross-check tickets and code — they can see requirement coverage at a glance.

To get started, simply [connect Bito with Jira](https://alpha.bito.ai/home/cra-integrations) and reference your Jira tickets in pull request titles, descriptions, or branch names.

[**Learn more about Jira Integration**](https://docs.bito.ai/ai-code-reviews-in-git/jira-integration)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FlmxE3AL5TJZeCzb3FDOL%2Fscrnli_VbFg1QB3vlCSKD.png?alt=media&#x26;token=8c0ceccc-c46e-4bc2-a931-337015781516" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZLqYnwgMQ0bSmzdAUbmv%2Fscrnli_KjIe1WJ48Jm3Cf.png?alt=media&#x26;token=932928cb-447a-4cb9-956a-fc246a96c30f" alt=""><figcaption></figcaption></figure>

## AI Code Review Agent - 9th Sep 2025

<mark style="color:blue;">**Important update**</mark>

**Bitbucket integration now uses API tokens:** Bitbucket has announced the [deprecation of app passwords](https://www.atlassian.com/blog/bitbucket/bitbucket-cloud-transitions-to-api-tokens-enhancing-security-with-app-password-deprecation) to enhance security across their platform. Starting September 9th, 2025, no new app passwords can be created, and existing app passwords will stop working entirely on June 9, 2026.&#x20;

**What's changing:** We've updated Bito to support Bitbucket's new API token authentication method. This transition ensures your Bitbucket integration remains secure and functional beyond the deprecation timeline.&#x20;

**What you need to do:** If you're currently using app passwords for your Bitbucket integration, you'll need to switch to API tokens.&#x20;

[Check out our updated setup guide](https://docs.bito.ai/ai-code-review-agent/install-run-using-bito-cloud/guide-for-bitbucket) to get started.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FDFzFbm0rKwuGHxNifPDQ%2Fscrnli_N7GAQ8TRE57s0p_1.png?alt=media&#x26;token=fd2c8fa2-eb2f-4768-a608-905980c7f0b9" alt="" width="563"><figcaption></figcaption></figure>

## AI Code Review Agent - 8th Sep 2025

<mark style="color:blue;">**New feature**</mark>

**Pull request and issue-level analytics:** We're excited to introduce the [**PR Analytics dashboard**](https://alpha.bito.ai/home/dashboard?view=PR_Analytics) – a powerful new addition to [Bito's Code Review Analytics](https://docs.bito.ai/ai-code-reviews-in-git/code-review-analytics) that gives you granular visibility into individual pull request performance and issue-level insights.

See exactly how many issues were found in each pull request.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/code-review-analytics#pr-analytics-dashboard)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FtC5YIbDbY3pObSzqEwod%2Fscrnli_22JO8JVrE9yVoM.png?alt=media&#x26;token=19ecd438-7e95-4f0e-919c-d7f4dc3bafd8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjHPD0ckFu7JvYtrYA8jQ%2Fscrnli_E38sxBtZlAhnF5.png?alt=media&#x26;token=5568d23b-6088-4dcd-84ad-5cae0040fda7" alt=""><figcaption></figcaption></figure>
