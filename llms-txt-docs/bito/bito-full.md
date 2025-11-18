# Bito Documentation

Source: https://docs.bito.ai/llms-full.txt

---

# Welcome to Bito

[Bito](https://bito.ai/) is an **AI-powered code review tool** that helps you catch bugs, security vulnerabilities, code smells, and other issues in your pull requests and code editors. By understanding your entire codebase, Bito provides context-aware, actionable suggestions that improve code quality and security.

It includes real-time recommendations from dev tools you already use such as static code analysis, open source vulnerability scanners, linters, and secrets scanning tools (e.g., passwords, API keys, sensitive information, etc.).

#### Supported platforms

[**AI Code Reviews in Git**](https://docs.bito.ai/ai-code-reviews-in-git/overview)**:** GitHub, GitLab, Bitbucket

[**AI Code Reviews in IDE**](https://docs.bito.ai/ai-code-reviews-in-ide/overview)**:** VS Code, Cursor, Windsurf, JetBrains

<p align="center"><a href="https://alpha.bito.ai/home/welcome" class="button primary">Start free trial</a><a href="getting-started" class="button secondary">Getting started guide</a></p>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FnYACckyUuw2IToyJyF0r%2Fimg-bito-cra.png?alt=media&#x26;token=81b38b43-dc23-495f-8eb8-6f7d54da524f" alt=""><figcaption></figcaption></figure>

## See AI Code Review Agent in action

{% embed url="<https://youtu.be/WukH9rA_5go>" %}

## Quickstart guide

{% stepper %}
{% step %}

### Sign up for Bito

Create your account at [alpha.bito.ai](https://alpha.bito.ai/home/welcome) to get started.
{% endstep %}

{% step %}

### Connect your Git provider

Select your preferred Git platform and follow the guided setup to install the agent:

* [GitHub](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github)
* [GitHub (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github-self-managed)
* [GitLab](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab)
* [GitLab (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab-self-managed)
* [Bitbucket](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket)
* [Bitbucket (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket-self-managed)

Once installed, the agent will be linked to your repositories and ready to assist.
{% endstep %}

{% step %}

### Review pull requests

The AI agent will automatically review **new pull requests** and leave inline comments with suggestions.\
You can also **manually trigger a review** by commenting `/review` on any pull request.

[See full list of available commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands)
{% endstep %}

{% step %}

### Chat with the agent

You can reply to comments posted by the Bito AI agent in a pull request to ask follow-up questions or request clarification. The agent will respond with context-aware answers to help you understand the feedback better.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/chat-with-ai-code-review-agent)
{% endstep %}

{% step %}

### Configure agent settings

To customize your agent, go to [Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) and click the **Settings** button next to the relevant agent. From there, you can choose the review feedback mode, enable or disable automatic reviews, define custom guidelines to align with your team’s standards, and more.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endstep %}
{% endstepper %}

## Helpful resources

<table data-column-title-hidden data-view="cards"><thead><tr><th align="center"></th><th data-hidden></th><th data-hidden data-type="content-ref"></th><th data-hidden data-type="content-ref"></th><th data-hidden data-type="content-ref"></th><th data-hidden data-type="content-ref"></th><th data-hidden data-type="content-ref"></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-type="content-ref"></th></tr></thead><tbody><tr><td align="center"><mark style="color:blue;"><strong>AI Code Review Agent</strong></mark></td><td></td><td></td><td></td><td></td><td></td><td></td><td><a href="ai-code-reviews-in-git/overview">overview</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FUcdZ6vcK9gCjJTUaEDne%2FUntitled%20design%20(4).png?alt=media&#x26;token=20b0eeb0-8004-45cd-9802-7fa0549aa4c4">Untitled design (4).png</a></td><td></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Account and settings</strong></mark></td><td>Manage workspace and personalize Bito</td><td><a href="help/account-and-settings/setting-ai-output-language">setting-ai-output-language</a></td><td><a href="help/account-and-settings/managing-user-access-levels">managing-user-access-levels</a></td><td></td><td></td><td></td><td><a href="help/account-and-settings">account-and-settings</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F645WmCAHgOMYO87FSCRM%2FUntitled%20design%20(5).png?alt=media&#x26;token=115732a3-d63e-4792-bdca-a9c50e4085f4">Untitled design (5).png</a></td><td></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Billing and plans</strong></mark></td><td></td><td></td><td></td><td></td><td></td><td></td><td><a href="help/billing-and-plans">billing-and-plans</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F4pl4GzipZ3Hn1o61AqGm%2FUntitled%20design%20(6).png?alt=media&#x26;token=f81e2f72-ced4-42ce-86bc-0547a1ed138d">Untitled design (6).png</a></td><td></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Privacy and security</strong></mark></td><td></td><td></td><td></td><td></td><td></td><td></td><td><a href="privacy-and-security">privacy-and-security</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFkH7cI5uaBk4mSFTyaaW%2FUntitled%20design%20(7).png?alt=media&#x26;token=b6d74f19-950e-49d2-a79c-c154a668bada">Untitled design (7).png</a></td><td></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Get support</strong></mark></td><td>Get support and learn about our security and privacy policy</td><td><a href="help/support-and-questions/troubleshooting">troubleshooting</a></td><td><a href="privacy-and-security">privacy-and-security</a></td><td></td><td></td><td></td><td><a href="help/support-and-questions">support-and-questions</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F6dVx3gGICbyTYJ2YWxO6%2FUntitled%20design%20(8).png?alt=media&#x26;token=5e5eabea-119e-4007-b2f8-375948110131">Untitled design (8).png</a></td><td></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Changelog</strong></mark></td><td></td><td></td><td></td><td></td><td></td><td></td><td><a href="changelog">changelog</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFsF73C8pvf82gpl6dgBr%2FUntitled%20design%20(9).png?alt=media&#x26;token=487a109b-e66d-4bb0-ad15-7fb45ab702b1">Untitled design (9).png</a></td><td></td></tr></tbody></table>

## Feature guides

<table data-view="cards"><thead><tr><th align="center"></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td align="center"><mark style="color:blue;"><strong>AI that understands your code</strong></mark></td><td><a href="https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/">https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FkPkq5LHtYSalDCHDTP46%2FUntitled%20design%20(10).png?alt=media&#x26;token=97b4b970-e58b-462d-9377-25c37f87b75c">Untitled design (10).png</a></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Chat with AI Code Review Agent</strong></mark></td><td><a href="ai-code-reviews-in-git/chat-with-ai-code-review-agent">chat-with-ai-code-review-agent</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FuG3uzNArjISxQKaIwlD4%2FUntitled%20design%20(11).png?alt=media&#x26;token=7717b4da-d5bd-4832-9be9-57cb317719e9">Untitled design (11).png</a></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Custom code review rules and guidelines</strong></mark></td><td><a href="ai-code-reviews-in-git/implementing-custom-code-review-rules">implementing-custom-code-review-rules</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FmHye90slz6w7KNJPrbMz%2FUntitled%20design%20(12).png?alt=media&#x26;token=935b3f08-9c6f-4dfc-988b-492b12433484">Untitled design (12).png</a></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Code review analytics</strong></mark></td><td><a href="ai-code-reviews-in-git/code-review-analytics">code-review-analytics</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FAr3P1Q8iKedkGw5wc5dT%2FUntitled%20design%20(13).png?alt=media&#x26;token=d3e29396-7b28-4209-bcaa-6d317aa865ed">Untitled design (13).png</a></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Supported programming languages and tools</strong></mark></td><td><a href="ai-code-reviews-in-git/supported-programming-languages-and-tools">supported-programming-languages-and-tools</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FEpQb5PwhjYZFMzJJs24Y%2FUntitled%20design%20(14).png?alt=media&#x26;token=8df8c9f0-fde4-4b1b-9a5c-fadb13579edc">Untitled design (14).png</a></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Available commands</strong></mark></td><td><a href="ai-code-reviews-in-git/available-commands">available-commands</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8tpsZXZa5vaSR5DPd9Z4%2FUntitled%20design%20(17).png?alt=media&#x26;token=cd3cb363-adb7-4e42-a2b9-7c31c6d89cf3">Untitled design (17).png</a></td></tr><tr><td align="center"><mark style="color:blue;"><strong>Agent settings</strong></mark></td><td></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOYL9kSoRur4Z04t2bBcG%2FUntitled%20design%20(18).png?alt=media&#x26;token=af2dac06-ba9a-4fb2-bfbe-622cc1d81a6e">Untitled design (18).png</a></td></tr><tr><td align="center"><mark style="color:blue;"><strong>FAQs</strong></mark></td><td><a href="ai-code-reviews-in-git/faqs">faqs</a></td><td><a href="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F3a9YUrociayAlAcP15ps%2FUntitled%20design%20(16).png?alt=media&#x26;token=eae78693-6120-4390-a695-12bb5de793a6">Untitled design (16).png</a></td></tr></tbody></table>

## Video library

{% embed url="<https://www.youtube.com/@bitoai?sub_confirmation=1>" %}

## Need help?

If you have any questions, feel free to email us at [**support@bito.ai**](mailto:support@bito.ai)


# Getting started

Deploy the AI Code Review Agent in Bito Cloud or opt for self-hosted service.

**The** [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) **supports two deployment options:**

* [**Bito Cloud (fully managed)**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud)
* [**Self-hosted service (run on your own infrastructure)**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service)

Each option comes with its own set of benefits and considerations.

This guide walks you through both options to help you determine which deployment model best fits your team’s needs.

## Bito Cloud

[**Bito Cloud**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud) provides a managed environment for running the AI Code Review Agent, offering a seamless, hassle-free experience. This option is ideal for teams looking for quick deployment and minimal operational overhead.

**Pros:**

* **Simplicity:** Enjoy a straightforward setup with a single-click installation process, making it easy to get started without technical hurdles.
* **Maintenance-Free:** Bito Cloud takes care of all necessary updates and maintenance, ensuring your Agent always operates on the latest software version without any effort on your part.
* **Scalability:** The platform is designed to easily scale, accommodating project growth effortlessly and ensuring reliable performance under varying loads.

**Cons:**

* **Handling of Pull Request Diffs:** For analysis purposes, diffs from pull requests are temporarily stored on our servers.

<p align="center"><a href="ai-code-reviews-in-git/install-run-using-bito-cloud" class="button primary">Install/run using Bito Cloud</a></p>

***

## Self-hosted service

[**Self-hosted**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service) AI Code Review Agent offers a higher degree of control and customization, suited for organizations with specific requirements or those who prefer to manage their own infrastructure.

**Pros:**

* **Full Control:** Self-hosting provides complete control over the deployment environment, allowing for extensive customization and the ability to integrate with existing systems as needed.
* **Privacy and Security:** Keeping the AI Code Review Agent within your own infrastructure can enhance data security and privacy, as all information remains under your direct control.

**Cons:**

* **Setup Complexity:** Establishing a self-hosted environment requires technical know-how and can be more complex than using a managed service, potentially leading to longer setup times.
* **Maintenance Responsibility:** The responsibility of maintaining and updating the software falls entirely on your team, which includes ensuring the system is scaled appropriately to handle demand.

<p align="center"><a href="ai-code-reviews-in-git/install-run-as-a-self-hosted-service" class="button primary">Install/run as a self-hosted service</a></p>


# Privacy and security

Bito doesn't read or store your code. Nor do we use your code for AI model training.

This document explains some of Bito's privacy and security practices.  Our [Trust Center ](https://trust.bito.ai)outlines our various accreditations (SOC 2 Type II) and our various security policies.  You can read our full Privacy Policy at <https://bito.ai/privacy-policy/>. &#x20;

## Bito AI

Security is top of mind at Bito, especially when it comes to your code. A fundamental approach we have taken is we do not store any code, code snippets, indexes or embedding vectors on Bito’s servers unless you expressly allow it.  You decide where you want to store your code, either locally on your machine, in your cloud, or on Bito’s cloud.  Importantly, our AI partners do not store any of this information.

All requests are transmitted over HTTPS and are fully encrypted.

**None** of your code or AI requests are used for AI model training. **None** of your code or AI requests are stored by our AI partners. Our AI model partners are OpenAI, Anthropic, and Google.  Here are their policies where they state that they do not store or train on data related to API access (we access all AI models via APIs):

1. OpenAI: <https://openai.com/enterprise-privacy/>&#x20;
2. Anthropic: <https://www.anthropic.com/uk-government-internal-ai-safety-policy-response/data-input-controls-and-audit>&#x20;
3. Google Cloud: <https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-unveils-ai-and-ml-privacy-commitment> (5th paragraph)

The AI requests including code snippets you send to Bito are sent to Bito servers for processing so that we can respond with an answer.&#x20;

Interactions with Bito AI are auto-moderated and managed for toxicity and harmful inputs and outputs.

Any response generated by the Bito IDE AI Assistant is stored locally on your machine to show the history in Bito UI. You can clear the history anytime you want from the Bito UI.

## SOC 2 Type II Compliance

Bito is SOC 2 Type II compliant. This certification reinforces our commitment to safeguarding user data by adhering to strict security, availability, and confidentiality standards. SOC 2 Type II compliance is an independent, rigorous audit that evaluates how well an organization implements and follows these security practices over time.

Our SOC 2 Type II compliance means:

* **Enhanced Data Security**: We consistently implement robust controls to protect your data from unauthorized access and ensure it remains secure.
* **Operational Excellence**: Our processes are designed to maintain high availability and reliability, ensuring uninterrupted service.
* **Regular Monitoring and Testing**: We conduct continuous monitoring and regular internal reviews to uphold the highest security standards.

This certification is an assurance that Bito operates with a high level of trust and transparency, providing you with a secure environment for your code and data.

For any further questions regarding our SOC 2 Type II compliance or to request a copy of the audit report, please reach out to [**support@bito.ai**](mailto:support@bito.ai)

## Code Flow through Bito’s System

#### AI Code Review Agent

When you use the self-hosted/docker version that you have setup in your VPC, in the docker image Bito checks out the diff and clones the repo for static analysis and also to determine relevant code context for code review.  This context and the diff is passed to Bito's system.  The request is then sent to a third-party LLM (e.g., OpenAI, Google Cloud, etc.). The LLM processes the prompt and return the response to Bito. No code is retained by the LLM. Bito then receives the response, processes it (such as formatting), and returns it to your self-hosted docker instance.  This then posts it to your Git provider.  However, the original query is not retained, nor are the results.  After each code review is completed, the diff and the checked out repo are deleted. &#x20;

If you use the Bito cloud to run the AI Code Review Agent, it runs similarly to the self-hosted version.   Bito ephemerally checks out the diff and clones the repo for static analysis and to determine the relevant code context for code review.  This context and the diff is passed to Bito's system.  The request is then sent by Bito to a third-party LLM (e.g., OpenAI, Google Cloud, etc.). The LLM processes the prompt and return the response to Bito. No code is retained by the LLM.  Bito then receives the response, processes it (such as formatting), and posts it to your Git provider.  However, the original query is not retained, nor are the results.  After each code review is completed, the diff and the checked out repo are deleted. &#x20;

#### AI Chat and Code Completions

When we receive an AI request from a user, it is processed by Bito's system (such as adding relevant context and determining the Large Language Model (LLM) to use). However, the original query is not retained. The request is then sent to a third-party LLM (e.g., OpenAI, Google Cloud, etc.). The LLM processes the prompt and return the response to Bito. Bito then receives the response, processes it (such as formatting), and returns it to the user’s machine.

For enterprises, we have the ability to connect to your own private LLM accounts, including but not limited to OpenAI, Google Cloud, Anthropic, or third-party services such as AWS Bedrock, Azure OpenAI. This way all data goes through your own accounts or Virtual Private Cloud (VPC), ensuring enhanced control and security.

## Data and Business Privacy Policy

In line with Bito's commitment to transparency and adherence to data privacy standards, our comprehensive data and business privacy policy is integrated into our practices. Our complete Terms of Use, including the Privacy Policy, are available at <https://bito.ai/terms-of-use/>, with our principal licensing information detailed at <https://bito.ai/terms-of-service/>.

## Data Retention Policy

Our data retention policy is carefully designed to comply with legal standards and to respect our customers' privacy concerns. The policy is categorized into four levels of data:

1. **Relationship and Usage Meta Data:** This includes all data related to the customer's interaction with Bito, such as address, billing amounts, user account data (name and email), and usage metrics (number of queries made, time of day, length of query, etc.). This category of data is retained indefinitely for ongoing service improvement and customer support.
2. **Bito Business Data:** Includes customer-created templates and settings. This data is terminated 90 days after the end of the business relationship with Bito.
3. **Confidential Customer Business Data:** This includes code, code artifacts, and other organization-owned data such as Jira, Confluence, etc. This data is either stored on-prem/locally on the customer’s machines, or, if in the cloud, is terminated at the end of the business relationship with Bito.
4. **AI Requests:** Data in an AI request to Bito’s AI system. AI requests are neither retained nor viewed by Bito. We ensure the confidentiality of your AI queries; Bito and our LLM partners do not store your code, and none of your data is used for model training. All requests are transmitted via HTTPS and are fully encrypted.

## Sub-processor

Bito uses the following third-party services:  Amazon AWS, Anthropic, Clearbit, Github, Google Analytics, Google Cloud, HelpScout, Hubspot, Microsoft Azure, Mixpanel, OpenAI, SendGrid, SiteGround, and Slack for infrastructure, support, and functional capabilities.&#x20;

## Personal Data

Bito follows industry standard practices for protecting your e-mail and other personal details. Our password-less login process - which requires one-time passcode sent to your e-mail for every login - ensures the complete security of your account.&#x20;

If you have any questions about our security and privacy, please email [**support@bito.ai**](mailto:support@bito.ai)


# Overview

On-demand, context-aware AI code reviews for GitHub, GitLab, and Bitbucket.

{% hint style="info" %}
[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

{% embed url="<https://youtu.be/WukH9rA_5go>" %}

Bito’s [**AI Code Review Agent**](https://bito.ai/product/ai-code-review-agent/) is the first agent built with **Bito’s AI Agent framework and engine**. It is an automated AI assistant (powered by Anthropic’s Claude Sonnet 3.7) that will review your team’s code; it spots bugs, issues, code smells, and security vulnerabilities in Pull/Merge Requests (PR/MR) and provides high-quality suggestions to fix them.

It seamlessly integrates with Git providers such as **GitHub, GitLab, and Bitbucket**, automatically posting recommendations directly as comments within the corresponding Pull Request. It includes real-time recommendations from Static Code Analysis and OSS vulnerability tools such as fbinfer, Dependency-Check, etc. and can include high severity suggestions from other 3rd party tools you use such as Snyk.

{% hint style="info" %}
We also support **GitHub (Self-Managed)** and **GitLab (Self-Managed)**.
{% endhint %}

The AI Code Review Agent acts as a **set of specialized engineers** each analyzing different aspects of your PR. They analyze aspects such as Performance, Code Structure, Security, Optimization, and Scalability. By combining and filtering the results, the Agent can provide you with much more detailed and insightful code reviews, bringing you a better quality code review and helping you save time.

The AI Code Review Agent helps engineering teams merge code faster while also keeping the code clean and up to standard, making sure it runs smoothly and follows best practices.

It ensures a secure and confidential experience without compromising on reliability. Bito neither reads nor stores your code, and none of your code is used for AI model training. Learn more about our [**Privacy & Security practices**](https://docs.bito.ai/privacy-and-security).

By accessing Bito's [**AI that Understands Your Code**](https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/) feature, the AI Code Review Agent can analyze relevant context from your entire repository, providing better context-aware analysis and suggestions. This tailored approach ensures a more personalized and contextually relevant code review experience.

To comprehend your code and its dependencies, we use Symbol Indexing, Abstract Syntax Trees (AST), and Embeddings. Each step feeds into the next, starting from locating specific code snippets with Symbol Indexing, getting their structural context with AST parsing, and then leveraging embedding vectors for broader semantic insights. This approach ensures a detailed understanding of the code's functionality and its dependencies. For more information, see [**How does Bito’s “AI that understands your code” work?**](https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/)

The AI Code Review Agent is built using **Bito Dev Agents**, an open framework and engine to **build custom AI Agents** for software developers that understands code, can connect to your organization’s data and tools, and can be discovered and shared via a global registry.

<p align="center"><a href="https://alpha.bito.ai/home/welcome" class="button primary">Start free trial</a><a href="https://bit.ly/bito-code-review-Demo" class="button secondary">Get a demo</a></p>

## Why use an AI Agent for code review?

In many organizations, senior developers spend approximately half of their time reviewing code changes in PRs to find potential issues. The AI Code Review Agent can help save this valuable time.

AI Code Review Agent **speeds up PR merges by 89%**, **reduces regressions by 34%**, and **delivers 87% human-grade feedback**.

However, it's important to remember that the AI Code Review Agent is designed to assist, not replace, senior software engineers. It takes care of many of the more mundane issues involved in code review, so senior engineers can focus on the business logic and how new development is aligned with your organization’s business goals.

## Pricing details

The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)

## Learn more

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:purple;"><strong>Getting Started</strong></mark></td><td></td><td><a href="../getting-started">getting-started</a></td></tr><tr><td><mark style="color:purple;"><strong>Key Features</strong></mark></td><td></td><td><a href="key-features">key-features</a></td></tr><tr><td><mark style="color:purple;"><strong>Supported Programming Languages and Tools</strong></mark></td><td></td><td><a href="supported-programming-languages-and-tools">supported-programming-languages-and-tools</a></td></tr><tr><td><mark style="color:purple;"><strong>Agent Configuration: bito-cra.properties File</strong></mark></td><td></td><td><a href="install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file">agent-configuration-bito-cra.properties-file</a></td></tr><tr><td><mark style="color:purple;"><strong>FAQs</strong></mark></td><td></td><td><a href="faqs">faqs</a></td></tr></tbody></table>


# Key features

Explore the powerful capabilities of the AI Code Review Agent.

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


# Supported programming languages and tools

Supports key languages & tools, including fbInfer, Dependency Check, and Snyk.

## Supported Programming Languages

### AI Code Review

The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) understands code changes in pull requests by analyzing relevant context from your entire repository, resulting in more accurate and helpful code reviews. The agent provides either **Basic Code Understanding** or **Advanced Code Understanding** based on the programming languages used in the code diff. Learn more about all the supported languages in the table below.

**Basic Code Understanding** is providing the surrounding code for the diff to help AI better understand the context of the diff.

**Advanced Code Understanding** is providing detailed information holistically to the LLM about the changes the diff is making—from things such as global variables, libraries, and frameworks (e.g., Lombok in Java, React for JS/TS, or Angular for TS) being used, the specific functions/methods and classes the diff is part of, to the upstream and downstream impact of a change being made. Using advanced code traversal and understanding techniques, such as symbol indexes, embeddings, and abstract syntax trees, Bito deeply tries to understand what your changes are about and the impact and relevance to the greater codebase, like a senior engineer does when doing code review. [**Read more here about our approach**](https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/).

{% hint style="info" %}
For requests to add support for specific programming languages, please reach out to us at <support@bito.ai>
{% endhint %}

|         Languages        | AI Code Review | Basic Code Understanding | Advanced Code Understanding |
| :----------------------: | :------------: | :----------------------: | :-------------------------: |
|       **Assembly**       |       YES      |            YES           |             YES             |
|      **Bash/Shell**      |       YES      |            YES           |             YES             |
|           **C**          |       YES      |            YES           |             YES             |
|          **C++**         |       YES      |            YES           |             YES             |
|          **C#**          |       YES      |            YES           |             YES             |
|         **Dart**         |       YES      |            YES           |             YES             |
|        **Delphi**        |       YES      |            YES           |             YES             |
|          **Go**          |       YES      |            YES           |             YES             |
|        **Groovy**        |       YES      |            YES           |             YES             |
|       **HTML/CSS**       |       YES      |            YES           |             YES             |
|         **Java**         |       YES      |            YES           |             YES             |
|      **JavaScript**      |       YES      |            YES           |             YES             |
| **JavaScript Framework** |       YES      |            YES           |             YES             |
|        **Kotlin**        |       YES      |            YES           |             YES             |
|          **Lua**         |       YES      |            YES           |             YES             |
|      **Objective-C**     |       YES      |            YES           |             YES             |
|          **PHP**         |       YES      |            YES           |             YES             |
|      **PowerShell**      |       YES      |            YES           |             YES             |
|        **Python**        |       YES      |            YES           |             YES             |
|           **R**          |       YES      |            YES           |             YES             |
|         **Ruby**         |       YES      |            YES           |             YES             |
|         **Rust**         |       YES      |            YES           |             YES             |
|         **Scala**        |       YES      |            YES           |             YES             |
|         **SCSS**         |       YES      |            YES           |             YES             |
|          **SQL**         |       YES      |            YES           |             YES             |
|         **Swift**        |       YES      |            YES           |             YES             |
|       **Terraform**      |       YES      |            YES           |             YES             |
|      **TypeScript**      |       YES      |            YES           |             YES             |
| **TypeScript Framework** |       YES      |            YES           |             YES             |
|        **Vue.js**        |       YES      |            YES           |             YES             |
|   **Visual Basic .NET**  |       YES      |            YES           |             YES             |
|        **Others**        |       YES      |            YES           |             YES             |

***

### Static Code Analysis and Open Source Vulnerabilities Check

For custom SAST tools configuration to support specific languages in the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview), please reach out to us at <support@bito.ai>

|       Languages       |                        Static Code Analysis / Linters                        | Open Source Vulnerabilities Check |
| :-------------------: | :--------------------------------------------------------------------------: | :-------------------------------: |
|      **Assembly**     |                                      NO                                      |                 NO                |
|     **Bash/Shell**    |                                      NO                                      |                 NO                |
|         **C**         |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|        **C++**        |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|         **C#**        |                                      NO                                      |                 NO                |
|        **Dart**       |                                      NO                                      |                 NO                |
|       **Delphi**      |                                      NO                                      |                 NO                |
|         **Go**        |             <p>YES<br>(using <strong>golangci-lint</strong>)</p>             |                YES                |
|       **Groovy**      |                                      NO                                      |                 NO                |
|      **HTML/CSS**     |                                      NO                                      |                 NO                |
|        **Java**       |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|     **JavaScript**    |                 <p>YES<br>(using <strong>ESLint</strong>)</p>                |                YES                |
|       **Kotlin**      |                                      NO                                      |                 NO                |
|        **Lua**        |                                      NO                                      |                 NO                |
|    **Objective-C**    |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|        **PHP**        |                                      NO                                      |                 NO                |
|     **PowerShell**    |                                      NO                                      |                 NO                |
|       **Python**      | <p>YES<br>(using <strong>Astral Ruff</strong> and <strong>Mypy</strong>)</p> |                 NO                |
|         **R**         |                                      NO                                      |                 NO                |
|        **Ruby**       |                                      NO                                      |                 NO                |
|        **Rust**       |                                      NO                                      |                 NO                |
|       **Scala**       |                                      NO                                      |                 NO                |
|        **SCSS**       |                                      NO                                      |                 NO                |
|        **SQL**        |                                      NO                                      |                 NO                |
|       **Swift**       |                                      NO                                      |                 NO                |
|     **Terraform**     |                                      NO                                      |                 NO                |
|     **TypeScript**    |                 <p>YES<br>(using <strong>ESLint</strong>)</p>                |                YES                |
|       **Vue.js**      |                                      NO                                      |                 NO                |
| **Visual Basic .NET** |                                      NO                                      |                 NO                |
|       **Others**      |                                      NO                                      |                 NO                |

***

## Supported Tools and Platforms

|            Tool            |                                Type                                |          Supported/Integrated         |
| :------------------------: | :----------------------------------------------------------------: | :-----------------------------------: |
|       **Astral Ruff**      |                          Linter for Python                         |                  YES                  |
|      **Azure DevOps**      |                           Code Repository                          |              Coming soon              |
|        **Bitbucket**       |                           Code Repository                          |                  YES                  |
|     **detect-secrets**     | Secrets scanner (e.g., passwords, API keys, sensitive information) |                  YES                  |
|         **ESLint**         |                Linter for JavaScript and TypeScript                |                  YES                  |
|     **Facebook Infer**     |       Static Code Analysis for Java, C, C++, and Objective-C       |                  YES                  |
|      **GitHub cloud**      |                           Code Repository                          |                  YES                  |
|  **GitHub (Self-Managed)** |                           Code Repository                          |  YES, supports version 3.0 and above. |
|      **GitLab cloud**      |                           Code Repository                          |                  YES                  |
|  **GitLab (Self-Managed)** |                           Code Repository                          | YES, supports version 15.5 and above. |
|      **golangci-lint**     |                            Linter for Go                           |                  YES                  |
|          **Mypy**          |                   Static Type Checker for Python                   |                  YES                  |
| **OWASP dependency Check** |                              Security                              |                  YES                  |
|          **Snyk**          |                              Security                              |                  YES                  |
|        **Whispers**        | Secrets scanner (e.g., passwords, API keys, sensitive information) |                  YES                  |

***

## Supported output languages for code review feedback

Bito supports posting code review feedback in over 20 languages. You can choose your preferred language in the [agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance). Supported languages include the following:

1. Arabic (عربي)
2. Bulgarian (български)
3. Chinese (Simplified) (简体中文)
4. Chinese (Traditional) (繁體中文)
5. Czech (čeština)
6. Dutch (Nederlands)
7. English (English)
8. French (français)
9. German (Deutsch)
10. Hebrew (עִברִית)
11. Hindi (हिंदी)
12. Hungarian (magyar)
13. Italian (italiano)
14. Japanese (日本語)
15. Korean (한국어)
16. Malay (Melayu)
17. Polish (polski)
18. Portuguese (português)
19. Russian (русский)
20. Spanish (español)
21. Turkish (Türkçe)
22. Vietnamese (Tiếng Việt)


# Install/run using Bito Cloud

Deploy the AI Code Review Agent in Bito Cloud.

[**Bito Cloud**](https://alpha.bito.ai/) offers a single-click solution for using the [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview), eliminating the need for any downloads on your machine. You can create multiple instances of the Agent, allowing each to be used with a different repository on a Git provider such as GitHub, GitLab, or Bitbucket.

We also support **GitHub (Self-Managed)**, **GitLab (Self-Managed)**, and **Bitbucket (Self-Managed)**.

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Connect Bito to your Git provider

Select your Git provider from the options below and follow the step-by-step installation guide to seamlessly set up your AI Code Review Agent.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Guide for GitHub</strong></mark></td><td><a href="install-run-using-bito-cloud/guide-for-github">guide-for-github</a></td></tr><tr><td><mark style="color:blue;"><strong>Guide for GitHub (Self-Managed)</strong></mark></td><td><a href="install-run-using-bito-cloud/guide-for-github-self-managed">guide-for-github-self-managed</a></td></tr><tr><td><mark style="color:blue;"><strong>Guide for GitLab</strong></mark></td><td><a href="install-run-using-bito-cloud/guide-for-gitlab">guide-for-gitlab</a></td></tr><tr><td><mark style="color:blue;"><strong>Guide for GitLab (Self-Managed)</strong></mark></td><td><a href="install-run-using-bito-cloud/guide-for-gitlab-self-managed">guide-for-gitlab-self-managed</a></td></tr><tr><td><mark style="color:blue;"><strong>Guide for Bitbucket</strong></mark></td><td><a href="install-run-using-bito-cloud/guide-for-bitbucket">guide-for-bitbucket</a></td></tr><tr><td><mark style="color:blue;"><strong>Guide for Bitbucket (Self-Managed)</strong></mark></td><td><a href="install-run-using-bito-cloud/guide-for-bitbucket-self-managed">guide-for-bitbucket-self-managed</a></td></tr></tbody></table>


# Guide for GitHub

Integrate the AI Code Review Agent into your GitHub workflow.

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) with your GitHub repositories. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).&#x20;

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

{% embed url="<https://www.youtube.com/watch?v=cmkCwpoQer4>" %}

## Installation and configuration steps

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito**

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup**

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7jB4NvihTZqLpAX1nuaf%2Fscrnli_KuCSLAb2uwZqov.png?alt=media&#x26;token=8c7fdbb7-2358-40ed-9a5f-db23cb11be40" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider**

Bito supports integration with the following Git providers:&#x20;

* GitHub&#x20;
* GitHub (Self-Managed)&#x20;
* GitLab&#x20;
* GitLab (Self-Managed)&#x20;
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for GitHub, select **GitHub** to proceed.

This will redirect you to **GitHub**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjYUnUM1FSNqL4FPlhIeb%2Fscrnli_eJySqPMukXXS5p.png?alt=media&#x26;token=1c3f3d9c-a9a7-42c9-b923-0989aa2fbca6" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Install the Bito app for GitHub** &#x20;

To enable pull request reviews, you need to install and authorize the **Bito’s AI Code Review Agent** app.

On GitHub, select where you want to install the app.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQUYQHV8vf2jbjVPYibBi%2Fscrnli_M43vf65IMb8eev.png?alt=media&#x26;token=7f1c2b04-ee16-45a9-90ce-33f589f9a4d7" alt=""><figcaption></figcaption></figure>

Grant Bito access to your repositories:

* Choose **All repositories** to enable Bito for every repository in your account.&#x20;
* Or, select **Only select repositories** and pick specific repositories using the dropdown menu.&#x20;

{% hint style="info" %}
Bito app uses these permissions:

* **Read** access to metadata
* **Read** and **write** access to code, issues, and pull requests
* **Read** access to organization members
  {% endhint %}

Click **Install & Authorize** to proceed. Once completed, you will be redirected to Bito.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjaaPBoWE8y2AdTHEf1QM%2Fscrnli_T7rYz0M1AVfzWP.png?alt=media&#x26;token=5f5d0b5c-7187-4a96-bd37-2b977e478647" alt="" width="527"><figcaption></figcaption></figure>

### **Step 5: Enable AI Code Review Agent on repositories**

After connecting Bito to your GitHub account, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeMOMn63PXgdez23nneKy%2Fscrnli_bYdbJiIK81y982_1.png?alt=media&#x26;token=752fe5c7-710d-43f6-90fb-0c876d0fc0f3" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual pull request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new pull requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the pull request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FryhzTFegsxvL4eoZewT7%2Fscrnli_2_28_2024_8-57-29%20PM.png?alt=media&#x26;token=af92cdfb-089b-4f95-8200-52adebe366dd" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for pull requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review pull requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a pull request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull request.
{% endhint %}

### **Step 7: Specialized commands for code reviews**

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.&#x20;

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**&#x20;

For more details, refer to [Available Commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

### **Step 8: Chat with AI Code Review Agent**

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your pull request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FivCegqSzdY80hPdZIMGN%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=528ddcda-100d-49a8-b6b5-2b9767a23785" alt="" width="563"><figcaption></figcaption></figure>

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)

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


# Guide for GitHub (Self-Managed)

Integrate the AI Code Review Agent into your self-hosted GitHub Enterprise workflow.

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your self-managed GitHub Enterprise server. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

coming soon...

## Prerequisites

Before proceeding, ensure you've completed all necessary prerequisites.

#### 1. Create a GitHub Personal Access Token (classic):

For GitHub pull request code reviews, ensure you have a **CLASSIC** personal access token with **`repo`** scope. We do not support fine-grained tokens currently.

[**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBZH0vDwrPqYQPMIxIyNW%2Fimage.png?alt=media&#x26;token=a4c42d8d-61a5-4cdb-87a1-622c0ba8f1ae" alt=""><figcaption><p><strong>GitHub Personal Access Token (classic)</strong></p></figcaption></figure>

#### 2. Authorizing a GitHub Personal Access Token for use with SAML single sign-on:

If your GitHub organization enforces [SAML Single Sign-On (SSO)](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enforcing-saml-single-sign-on-for-your-organization), you must authorize your Personal Access Token (classic) through your Identity Provider (IdP); otherwise, Bito's AI Code Review Agent won't function properly.

For detailed instructions, please refer to the [GitHub documentation](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

## Installation and configuration steps

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito**

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup**

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7jB4NvihTZqLpAX1nuaf%2Fscrnli_KuCSLAb2uwZqov.png?alt=media&#x26;token=8c7fdbb7-2358-40ed-9a5f-db23cb11be40" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider**&#x20;

Bito supports integration with the following Git providers:&#x20;

* GitHub&#x20;
* GitHub (Self-Managed)&#x20;
* GitLab&#x20;
* GitLab (Self-Managed)&#x20;
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for self-managed GitHub Enterprise server, select **GitHub (Self-Managed)** to proceed.

{% hint style="info" %}
**Supported versions:**

* **GitHub Enterprise Server:** 3.0 and above
  {% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhJOg0OlVYrzpFw1KP3yw%2Fscrnli_Jk7BcFXL0xXyja.png?alt=media&#x26;token=3bfd22c4-99bc-494c-a426-c6ae7215d466" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Register & install the Bito App for GitHub**&#x20;

To enable pull request reviews, you need to register and install the **Bito’s AI Code Review Agent** app on your self-managed GitHub Enterprise server.

{% hint style="info" %}
If your network blocks external services from interacting with the GitHub server, whitelist all of Bito's gateway IP addresses in your firewall to ensure Bito can access your self-hosted repositories. The Agent response can come from any of these IPs.&#x20;

* **List of IP addresses to whitelist:**&#x20;
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**&#x20;
    {% endhint %}

You need to enter the details for the below mentioned input fields:&#x20;

* **Hosted GitHub URL:** This is the domain portion of the URL where you GitHub Enterprise Server is hosted (e.g., `https://yourcompany.github.com`). Please check with your GitHub administrator for the correct URL.&#x20;
* **Personal Access Token:** Generate a **Personal Access Token (classic)** with **“repo”** scope in your GitHub (Self-Managed) account and enter it into the **Personal Access Token** input field. We do not support fine-grained tokens currently. For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.&#x20;

Click **Validate** to ensure the login credentials are working correctly. If the credentials are successfully validated, click the **Install Bito App for GitHub** button. This will redirect you to your GitHub (Self-Managed) server.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeiSAyQzwhsWkr9bPZrce%2Fscrnli_rCj22uk5HFb2t2_1.png?alt=media&#x26;token=d17d9f8e-c8a3-472e-a13f-8fa4b13e8109" alt=""><figcaption></figcaption></figure>

Before proceeding, you’ll be asked to **enter your GitHub App name** — this is the name that will appear in your GitHub Apps list and during installations. Choose a clear, recognizable name (for example, “Bito Code Reviewer”).

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXWiiC7FFRU0ZXKy9TZcL%2Fscrnli_98w41S7XJ9u6zO.png?alt=media&#x26;token=20db7387-9ddd-4529-bdf8-6c20c358f9fa" alt=""><figcaption></figcaption></figure>

Now select where you want to install the app: &#x20;

* Choose **All repositories** to enable Bito for every repository in your account.&#x20;
* Or, select **Only select repositories** and pick specific repositories using the dropdown menu.&#x20;

{% hint style="info" %}
Bito app uses these permissions:&#x20;

* **Read** access to metadata&#x20;
* **Read** and **write** access to code, issues, and pull requests&#x20;
* **Read** access to organization members
  {% endhint %}

Click **Install & Authorize** to proceed. Once completed, you will be redirected to Bito.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FpkNPb32ypSep8KvCjxhE%2Fscrnli_53aedt4Zg9v0Rm.png?alt=media&#x26;token=210bfd9b-ea7a-449d-8e07-1f080c0ddd82" alt=""><figcaption></figcaption></figure>

### **Step 5: Enable AI Code Review Agent on repositories**&#x20;

After connecting Bito to your self-managed GitHub Enterprise server, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8ou5QfEk0k1I9iskh94k%2Fscrnli_zBhAS7sgD29mGl_1.png?alt=media&#x26;token=0a4afced-697e-4926-a0a9-659a9b4fc3ab" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual pull request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new pull requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the pull request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FryhzTFegsxvL4eoZewT7%2Fscrnli_2_28_2024_8-57-29%20PM.png?alt=media&#x26;token=af92cdfb-089b-4f95-8200-52adebe366dd" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for pull requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review pull requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a pull request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull request.
{% endhint %}

### **Step 7: Specialized commands for code reviews**

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.&#x20;

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**&#x20;

For more details, refer to [Available Commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

### **Step 8: Chat with AI Code Review Agent**

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your pull request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FivCegqSzdY80hPdZIMGN%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=528ddcda-100d-49a8-b6b5-2b9767a23785" alt="" width="563"><figcaption></figcaption></figure>

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)

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


# Guide for GitLab

Integrate the AI Code Review Agent into your GitLab workflow.

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your GitLab repositories. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

{% embed url="<https://youtu.be/wG09qSWFkzQ>" %}

## Prerequisites

Before proceeding, ensure you've completed all necessary prerequisites.

#### 1. Create a GitLab Personal Access Token:

For GitLab merge request code reviews, a token with **`api`** scope is required. Make sure that the token is created by a GitLab user who has the **`Maintainer`** access role.

[**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

{% hint style="info" %}
**Important:** Bito posts comments using the GitLab user account linked to the Personal Access Token used during setup. To display "Bito" instead of your name, create a separate user account (e.g., Bito Agent) and use its token for integration.
{% endhint %}

{% hint style="info" %}
We recommend setting the **token expiration** to at least one year. This prevents the token from expiring early and avoids disruptions in the AI Code Review Agent's functionality.&#x20;

Additionally, we highly recommend updating the token before expiry to maintain seamless integration and code review processes.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FghbsjA3aafRQJBQGnksv%2Fimage%20(1).png?alt=media&#x26;token=6feb55f7-39b3-4d61-8e46-f6b233e64849" alt=""><figcaption><p><strong>GitLab Personal Access Token</strong></p></figcaption></figure>

#### 2. Authorizing a GitLab Personal Access Token for use with SAML single sign-on:

If your GitLab organization enforces SAML Single Sign-On (SSO), you must authorize your Personal Access Token through your Identity Provider (IdP); otherwise, Bito's AI Code Review Agent won't function properly.

For more information, please refer to these GitLab documentation:

* <https://docs.gitlab.com/ee/user/group/saml_sso/>
* <https://docs.gitlab.com/ee/integration/saml.html>
* <https://docs.gitlab.com/ee/integration/saml.html#password-generation-for-users-created-through-saml>

## Installation and configuration steps

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito**

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup**

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7jB4NvihTZqLpAX1nuaf%2Fscrnli_KuCSLAb2uwZqov.png?alt=media&#x26;token=8c7fdbb7-2358-40ed-9a5f-db23cb11be40" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider**

Bito supports integration with the following Git providers:&#x20;

* GitHub&#x20;
* GitHub (Self-Managed)&#x20;
* GitLab&#x20;
* GitLab (Self-Managed)&#x20;
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for GitLab, select **GitLab** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FETj8JmXkQeBAQ5zufjHv%2Fscrnli_7Ci4O6tHHXY58F.png?alt=media&#x26;token=329d6d37-630a-409a-9f2d-b4226d8f8290" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to GitLab**

To enable merge request reviews, you’ll need to connect your Bito workspace to your GitLab account.

You can either connect using **OAuth (recommended)** for a seamless, one-click setup or manually enter your **Personal Access Token**.

To connect via OAuth, simply click the **Connect with OAuth (Recommended)** button. This will redirect you to the GitLab website, where you'll need to log in. Once authenticated, you'll be redirected back to Bito, confirming a successful connection.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrCeLccv5wvxww06Lpqtw%2Fscrnli_5jI39Zex0s92SO.png?alt=media&#x26;token=df661bf6-2cdc-4d01-8225-01e4d6bd0f6a" alt=""><figcaption></figcaption></figure>

If you prefer not to use OAuth, you can connect manually using a **Personal Access Token**.

Start by [generating a Personal Access Token](https://gitlab.com/-/user_settings/personal_access_tokens) with **`api`** scope in your GitLab account. For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.

Once generated, click the **Alternatively, use Personal or Group Access Token** button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FX6IlUtc5Y6XaJoOB9dxv%2Fscrnli_sH76XQeLbsU3aw.png?alt=media&#x26;token=60bdc89d-7345-46b6-ba52-ab34e642b70c" alt=""><figcaption></figcaption></figure>

Now, enter the token into the **Personal Access Token** input field in Bito.

Click **Validate** to ensure the token is functioning properly.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fe2YSKEAzCLXKoy8nhTJE%2Fscrnli_ykor6MMedHkkFM.png?alt=media&#x26;token=a226253e-dc53-4684-8c3d-0a875d93d158" alt=""><figcaption></figcaption></figure>

If you've successfully connected via OAuth or manually validated your token, you can select your **GitLab Group** from the dropdown menu.

Click **Connect Bito to GitLab** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FzxcJdx9oRmZZzLNJTJo8%2Fscrnli_mC61ET3jriAsRg.png?alt=media&#x26;token=a6474328-07a5-470a-aeee-f713dd03b145" alt=""><figcaption></figcaption></figure>

&#x20;

### **Step 5: Enable AI Code Review Agent on repositories**&#x20;

After connecting Bito to your GitLab account, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0TyvAqlOA5QYyh4Kv6JD%2Fscrnli_RtCVLzUlR23QJr_1.png?alt=media&#x26;token=c156d679-7e13-4700-a9ef-4693836d23e8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual merge request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new merge requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the merge request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your merge request, making it seamless to view and address suggestions right where they matter most.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBBOvTOprCCheQBy3MaQ1%2Fscrnli_9_18_2024_8-51-21%20AM.png?alt=media&#x26;token=633cd07e-24c6-4eec-b285-d83754d798cf" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for merge requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review merge requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a merge request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the merge request.
{% endhint %}

### **Step 7: Specialized commands for code reviews**

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.&#x20;

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**&#x20;

For more details, refer to [Available Commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

### **Step 8: Chat with AI Code Review Agent**

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your merge request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FivCegqSzdY80hPdZIMGN%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=528ddcda-100d-49a8-b6b5-2b9767a23785" alt="" width="563"><figcaption></figcaption></figure>

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)

## Screenshots

### Screenshot # 1

{% hint style="info" %}
*AI-generated merge request (MR) summary*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZ08V4Js5ORq7j6n0qR5S%2Fscrnli_9_18_2024_8-20-30%20AM.png?alt=media&#x26;token=80e6b92c-95e2-4d1b-939c-1f976136bac2" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a merge request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the merge request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRGVVrPpKePySgQWiOrd6%2Fscrnli_9_18_2024_8-38-48%20AM_cropped.png?alt=media&#x26;token=20b082f1-dd87-437c-b1dc-268c9564a27a" alt=""><figcaption></figcaption></figure>


# Guide for GitLab (Self-Managed)

Integrate the AI Code Review Agent into your self-hosted GitLab workflow.

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your GitLab (Self-Managed) server. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a merge request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

coming soon...

## Prerequisites

Before proceeding, ensure you've completed all necessary prerequisites.

#### 1. Create a GitLab Personal Access Token:

For GitLab merge request code reviews, a token with **`api`** scope is required. Make sure that the token is created by a GitLab user who has the **`Maintainer`** access role.

[**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

{% hint style="info" %}
**Important:** Bito posts comments using the GitLab user account linked to the Personal Access Token used during setup. To display "Bito" instead of your name, create a separate user account (e.g., Bito Agent) and use its token for integration.
{% endhint %}

{% hint style="info" %}
We recommend setting the **token expiration** to at least one year. This prevents the token from expiring early and avoids disruptions in the AI Code Review Agent's functionality.&#x20;

Additionally, we highly recommend updating the token before expiry to maintain seamless integration and code review processes.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FghbsjA3aafRQJBQGnksv%2Fimage%20(1).png?alt=media&#x26;token=6feb55f7-39b3-4d61-8e46-f6b233e64849" alt=""><figcaption><p><strong>GitLab Personal Access Token</strong></p></figcaption></figure>

#### 2. Authorizing a GitLab Personal Access Token for use with SAML single sign-on:

If your GitLab organization enforces SAML Single Sign-On (SSO), you must authorize your Personal Access Token through your Identity Provider (IdP); otherwise, Bito's AI Code Review Agent won't function properly.

For more information, please refer to the following GitLab documentation:

* [SAML SSO for GitLab.com groups](https://docs.gitlab.com/user/group/saml_sso/)
* [SAML SSO for GitLab Self-Managed](https://docs.gitlab.com/integration/saml/)
* [Password generation for users created through SAML](https://docs.gitlab.com/integration/saml/#password-generation-for-users-created-through-saml)

## Installation and configuration steps

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito**

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup**

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7jB4NvihTZqLpAX1nuaf%2Fscrnli_KuCSLAb2uwZqov.png?alt=media&#x26;token=8c7fdbb7-2358-40ed-9a5f-db23cb11be40" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider**&#x20;

Bito supports integration with the following Git providers:&#x20;

* GitHub&#x20;
* GitHub (Self-Managed)&#x20;
* GitLab&#x20;
* GitLab (Self-Managed)&#x20;
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for GitLab (Self-Managed) server, select **GitLab (Self-Managed)** to proceed.

{% hint style="info" %}
**Supported versions:**

* **GitLab (Self-Managed):** 15.5 and above
  {% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FtgUKG7gdgn9GJgSAASFy%2Fscrnli_QBt6t8kukXYaYE.png?alt=media&#x26;token=b312f994-faf6-49cd-a930-3ee640293f46" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to GitLab** &#x20;

To enable merge request reviews, you’ll need to connect your Bito workspace to your GitLab (Self-Managed) server.

{% hint style="info" %}
If your network blocks external services from interacting with the GitLab server, whitelist all of Bito's gateway IP addresses in your firewall to ensure Bito can access your self-hosted repositories. The Agent response can come from any of these IPs.&#x20;

* **List of IP addresses to whitelist:**&#x20;
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**
    {% endhint %}

You need to enter the details for the below mentioned input fields:&#x20;

* **Hosted GitLab URL:** This is the domain portion of the URL where you GitLab Enterprise Server is hosted (e.g., `https://yourcompany.gitlab.com`). Please check with your GitLab administrator for the correct URL.&#x20;
* **Personal Access Token:** Generate a **GitLab Personal Access Token** with **`api`** scope in your GitLab (Self-Managed) account and enter it into the **Personal Access Token** input field. For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.

Click **Validate** to ensure the token is functioning properly.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fomu0dVL9I0CTQ8yC7MHO%2Fscrnli_27slie02tJkRAf_1.png?alt=media&#x26;token=e2689d19-c041-48aa-90ed-6b678c224dc4" alt=""><figcaption></figcaption></figure>

If the token is successfully validated, you can select your **GitLab Group** from the dropdown menu.

* **Note:** You can select multiple groups after the setup is complete.

Click **Connect Bito to GitLab** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FU4h3BLObcIsIEN0lU95i%2Fscrnli_1L3maXu3pJtiCd.png?alt=media&#x26;token=32be430f-2b99-428b-9f47-c47067966e60" alt=""><figcaption></figcaption></figure>

### **Step 5: Enable AI Code Review Agent on repositories**&#x20;

After connecting Bito to your GitLab self-managed server, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeXTvPIXX2uSyhuWGCLNI%2Fscrnli_BYisAy83ZXjb8j_1.png?alt=media&#x26;token=1b4968fe-9740-498f-aebc-7e854cdf0ccf" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual merge request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new merge requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the merge request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your merge request, making it seamless to view and address suggestions right where they matter most.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBBOvTOprCCheQBy3MaQ1%2Fscrnli_9_18_2024_8-51-21%20AM.png?alt=media&#x26;token=633cd07e-24c6-4eec-b285-d83754d798cf" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for merge requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review merge requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a merge request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the merge request.
{% endhint %}

### **Step 7: Specialized commands for code reviews**

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.&#x20;

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**&#x20;

For more details, refer to [Available Commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

### **Step 8: Chat with AI Code Review Agent**

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your merge request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FivCegqSzdY80hPdZIMGN%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=528ddcda-100d-49a8-b6b5-2b9767a23785" alt="" width="563"><figcaption></figcaption></figure>

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)

## Managing multiple GitLab groups in Bito Cloud

[Bito Cloud](https://alpha.bito.ai/) allows you to connect and manage multiple GitLab groups for **GitLab (Self-Managed)** integrations. Use the instructions below to add or remove GitLab groups for AI code reviews.

### How to add multiple GitLab groups?

You can connect more than one GitLab group to Bito for AI code reviews.

Follow these steps to add additional groups:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F4CZ7NBraXiiD6Iqq7j5a%2Fscrnli_Y8WOHXWq804QA4.png?alt=media&#x26;token=bb9bd6b7-f997-4e59-8cac-344ed3bbc532" alt=""><figcaption></figcaption></figure>

2. At the top-center of the page, click the **“+” (plus) icon** next to the currently selected GitLab group name, then select **Add group** from the dropdown menu.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMslGYbmuoV1rRShmx5Jl%2Fscrnli_W8jQLW06Gxuqt0_1.png?alt=media&#x26;token=f7f30d4e-aae6-46f5-92c9-1e5cb065287c" alt=""><figcaption></figcaption></figure>

3. A popup will appear. Use the **dropdown menu** to select a GitLab group you want to add.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbLf4ueoWPOLRQ3CxwrWI%2Fscrnli_8ZF0yXi7X0hXsw_1.png?alt=media&#x26;token=91597a4e-b462-4400-8a14-65df4307c75c" alt=""><figcaption></figcaption></figure>

4. Click the **Add group** button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0WHxXbmnKKK9RmWfr5pF%2Fscrnli_cz6US78Ei0o7Xj_1.png?alt=media&#x26;token=322cf8e0-0e92-43a0-9d6b-f8486e560f86" alt=""><figcaption></figcaption></figure>

Once added, all repositories from that group will be listed and available for AI code reviews under the default agent.

{% hint style="info" %}
**Note:** This **multiple GitLab groups** feature is currently available **only for GitLab (Self-Managed)** integrations.
{% endhint %}

### How to remove a GitLab group?

To disconnect a GitLab group from Bito Cloud:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FR7Z8pmGAEEi2saOB0MPM%2Fscrnli_Y8WOHXWq804QA4.png?alt=media&#x26;token=f6dbf22d-bfb4-498c-8a87-91508990d724" alt=""><figcaption></figcaption></figure>

2. At the top-center of the page, click the **three dots icon** next to the currently selected GitLab group name, then select **Manage groups** from the dropdown menu.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FdULLEBhV1cLCGuKDWgKm%2Fscrnli_EPno749Af0t5m9_1.png?alt=media&#x26;token=cf282900-50a1-489e-8a03-d19970dcb48e" alt=""><figcaption></figcaption></figure>

3. A popup will appear showing a list of connected groups. Click the **“✕” (cross) icon** next to the group you want to remove.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7RcLErjIG7OHFhhhQUkk%2Fscrnli_ObMG7t14A0Z347_1.png?alt=media&#x26;token=3a242425-7690-46fb-bac0-7a7e448779b5" alt=""><figcaption></figcaption></figure>

3. Confirm the removal in the prompt.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOwjpuYuS6IufShaNMcgZ%2Fscrnli_gARi37sN912InC_1.png?alt=media&#x26;token=65fdba44-9333-4607-9b01-cddfe458c2ad" alt=""><figcaption></figcaption></figure>

Once removed, the repositories from that group will no longer appear in Bito or be included in AI code reviews.

### How to select one or more GitLab Groups?

When you have **multiple GitLab groups connected** in Bito Cloud, the group name at the top-center of the [Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) page becomes a **dropdown menu**.

From this dropdown, you can:

* Select **a single group**
* Select **multiple groups as needed**
* Select **All groups**

The list of repositories displayed below will update automatically based on your selection—showing only the repositories from the selected groups.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FA2eUv2Rf6isNoIbtEovO%2F1_scrnli_XOow3dK4CvFTuP.png?alt=media&#x26;token=a9cfb7fd-fde1-42f6-b93c-8fc594a3cbc9" alt=""><figcaption></figcaption></figure>

## Screenshots

### Screenshot # 1

{% hint style="info" %}
*AI-generated merge request (MR) summary*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZ08V4Js5ORq7j6n0qR5S%2Fscrnli_9_18_2024_8-20-30%20AM.png?alt=media&#x26;token=80e6b92c-95e2-4d1b-939c-1f976136bac2" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a merge request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the merge request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRGVVrPpKePySgQWiOrd6%2Fscrnli_9_18_2024_8-38-48%20AM_cropped.png?alt=media&#x26;token=20b082f1-dd87-437c-b1dc-268c9564a27a" alt=""><figcaption></figcaption></figure>


# Guide for Bitbucket

Integrate the AI Code Review Agent into your Bitbucket workflow.

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your Bitbucket repositories. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

{% embed url="<https://youtu.be/s4iKC4QRAqE>" %}

## Installation and configuration steps

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito**

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup**

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7jB4NvihTZqLpAX1nuaf%2Fscrnli_KuCSLAb2uwZqov.png?alt=media&#x26;token=8c7fdbb7-2358-40ed-9a5f-db23cb11be40" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider**

Bito supports integration with the following Git providers:&#x20;

* GitHub&#x20;
* GitHub (Self-Managed)&#x20;
* GitLab&#x20;
* GitLab (Self-Managed)&#x20;
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for Bitbucket, select **Bitbucket** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ff6khlPh27gsqOuxtn1DX%2Fscrnli_8CcC8oU24XyHAx.png?alt=media&#x26;token=4172d5ad-bdc6-48bc-983e-c147b6e35d0f" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to Bitbucket**

To enable pull request reviews, you’ll need to connect your Bito workspace to your Bitbucket account.

{% hint style="info" %}
If your [Bitbucket access control settings](https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/) block external services from interacting with the Bitbucket server, whitelist all of Bito's gateway IP addresses to ensure Bito can access your repositories. The Agent response can come from any of these IPs.

* **List of IP addresses to whitelist:**
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**

See the [Bitbucket documentation](https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/) for more information.
{% endhint %}

Click **Install Bito App for Bitbucket**. This will redirect you to Bitbucket.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMkEhUlMUfiK26rbEV9lS%2Fscrnli_jBYatEquCn4pVe.png?alt=media&#x26;token=9e3b91d5-1858-4e85-8405-2f1623aaf5a4" alt=""><figcaption></figcaption></figure>

Now, authorize the Bito App to access your Bitbucket repositories.

Select your Bitbucket workspace from the **Authorize for workspace** dropdown menu and then click **Grant access**. Once completed, you will be redirected to Bito.

{% hint style="info" %}
**Note:** You'll only see Bitbucket workspaces where you have **Admin** access. If no workspaces appear in the dropdown, it means your account doesn’t have admin access to any workspace. To connect a workspace, make sure you have admin access for it.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fv0VauXquH5Q6mJg7vTYZ%2Ftinywow_scrnli_24x3kCekLNju4h_84371899.png?alt=media&#x26;token=97b84b58-d5b6-42a7-8e02-571626b5e0bc" alt=""><figcaption></figcaption></figure>

### **Step 5: Enable AI Code Review Agent on repositories**

After connecting Bito to your Bitbucket account, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBopXIGtuWOCxzt8W6gDv%2Fscrnli_Nf0yfPc0l2qOe9_1.png?alt=media&#x26;token=0784b195-5887-4d30-81b6-76a62831c8e5" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual pull request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new pull requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the pull request and click **Add comment now** to submit it. This action will start the code review process.

{% hint style="info" %}
**Note:** After typing **`/review`**, add a space inside the comment box to ensure that **`/review`** is not highlighted as a Bitbucket slash command so that the comment can be posted correctly.
{% endhint %}

The AI-generated code review feedback will be posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfXuf3LO3sIqG6dPwz4fk%2Fscrnli_9_18_2024_8-01-14%20AM.png?alt=media&#x26;token=7b067b12-0e48-4900-89fa-878db4ace071" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for pull requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review pull requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a pull request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull request.
{% endhint %}

### **Step 7: Specialized commands for code reviews**

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.&#x20;

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**&#x20;

For more details, refer to [Available Commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

### **Step 8: Chat with AI Code Review Agent**

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your pull request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FivCegqSzdY80hPdZIMGN%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=528ddcda-100d-49a8-b6b5-2b9767a23785" alt="" width="563"><figcaption></figcaption></figure>

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)

## Screenshots

### Screenshot # 1

{% hint style="info" %}
*AI-generated pull request (PR) summary*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FUBoXJAhcEjR9SPwNbVKz%2Fscrnli_9_18_2024_8-43-54%20AM.png?alt=media&#x26;token=ed39dd98-bc00-4f32-9abb-27a6c0aedef7" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a pull request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the pull request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJmIqJ9p3s7J67rWEMWRk%2Fscrnli_9_18_2024_8-44-53%20AM_b.png?alt=media&#x26;token=66ca75ba-35d1-40c0-961a-d550b1132d9f" alt=""><figcaption></figcaption></figure>


# Guide for Bitbucket (Self-Managed)

Integrate the AI Code Review Agent into your self-hosted Bitbucket workflow.

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git) with your Bitbucket (Self-Managed) server. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial <a href="#video-tutorial" id="video-tutorial"></a>

{% embed url="<https://youtu.be/ZAawiQ22PMc>" %}

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before proceeding, ensure you've completed all necessary prerequisites.

### **1. Create a Bitbucket Personal Access Token:**

For Bitbucket pull request code reviews, a token with **`Project Admin`**  permission is required. Make sure that the token is created by a Bitbucket user who has the **`Admin`**  privileges.

{% hint style="info" %}
**Important:** Bito posts comments using the Bitbucket user account linked to the Personal Access Token used during setup. To display "Bito" instead of your name, create a separate user account (e.g., Bito Agent) and use its token for integration.
{% endhint %}

You can use the **Create Token** button that appears once you provide the **Hosted Bitbucket URL** and your **Bitbucket username**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5YvKDBUEIefxIpKB5GaV%2Fscrnli_g528adnNaTXmWg_1.png?alt=media&#x26;token=cf2dced9-b5ae-4ea9-bd6b-6ce1e7d1ba92" alt="" width="563"><figcaption></figcaption></figure>

Or directly visit the URL of your self-hosted Bitbucket.

To create a token for your user account:

1. Go to **Profile picture** > **Manage account** > **HTTP access tokens**.
2. Select **Create token**.
3. Set the token name, permissions, and expiry.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFgvm4olJ3yhyo0xOiWnf%2Fscrnli_Rr1m0ddO4rSyCR_1%20(2).png?alt=media&#x26;token=07dadb9b-3494-480e-8c35-aeca49af780b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FWaRUeDccyy6D63BTQPyZ%2Fscrnli_um1SDww4ZRtLsi_1%20(1).png?alt=media&#x26;token=10217b14-4a6d-4795-a987-e8f05a7b1aa6" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FlPWS1DtbgwvmwitUYvqt%2Fscrnli_mR0r6q2h3RV3kJ_1%20(1).png?alt=media&#x26;token=4ae08d23-8710-4a7d-babc-1064b3062aea" alt="" width="563"><figcaption></figcaption></figure>

<a href="https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html" class="button primary">View Bitbucket documentation</a>

### **2. Authorizing a Bitbucket Personal Access Token for use with SAML single sign-on:**

If your Bitbucket organization enforces SAML Single Sign-On (SSO), you must authorize your Personal Access Token through your Identity Provider (IdP); otherwise, Bito's AI Code Review Agent won't function properly.

For more information, please refer to [Bitbucket SAML SSO documentation](https://support.atlassian.com/bitbucket-data-center/kb/how-to-configure-saml-sso-for-bitbucket-data-center-with-okta/).

## Installation and configuration steps <a href="#installation-and-configuration-steps" id="installation-and-configuration-steps"></a>

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito** <a href="#step-1-log-in-to-bito" id="step-1-log-in-to-bito"></a>

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup** <a href="#step-2-open-the-code-review-agents-setup" id="step-2-open-the-code-review-agents-setup"></a>

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FaRd44Mm4ssRuJq0JPTDY%2Fscrnli_F8cTXu9Nhus5wi.png?alt=media&#x26;token=1caf8b4c-1f2d-4fee-a4b2-68bfc7cc5925" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider** <a href="#step-3-select-your-git-provider" id="step-3-select-your-git-provider"></a>

Bito supports integration with the following Git providers:

* GitHub
* GitHub (Self-Managed)
* GitLab
* GitLab (Self-Managed)
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for Bitbucket (Self-Managed) server, select **Bitbucket (Self-Managed)** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Frk0l6UdSGntsYtRlPDik%2Fscrnli_v4wqkwtzxUUXo8.png?alt=media&#x26;token=15097f2d-9e3f-45d1-8602-8bda679b0ef0" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to Bitbucket** <a href="#step-4-connect-bito-to-bitbucket" id="step-4-connect-bito-to-bitbucket"></a>

To enable pull request reviews, you’ll need to connect your Bito workspace to your Bitbucket (Self-Managed) server.

{% hint style="info" %}
If your network blocks external services from interacting with the Bitbucket server, whitelist all of Bito's gateway IP addresses in your firewall to ensure Bito can access your self-hosted repositories. The Agent response can come from any of these IPs.

* **List of IP addresses to whitelist:**
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**
    {% endhint %}

You need to enter the details for the below mentioned input fields:

* **Hosted Bitbucket URL:** This is the domain portion of the URL where your Bitbucket Enterprise server is hosted (e.g., `https://bitbucket.mycompany.com`). Please check with your Bitbucket administrator for the correct URL.
* **Bitbucket username:** This is your Bitbucket username used for login. Please check it from your user profile page or ask your Admin.
* **Personal Access Token:** Generate a **Bitbucket Personal Access Token** with **`Project Admin`**  permission in your Bitbucket (Self-Managed) account. Ensure you have Bitbucket **Admin** privileges. Enter the token into the **Personal Access Token** input field. You can use the **Create Token** button that appears once you provide the **Hosted Bitbucket URL** and your **Bitbucket username**.

  For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.

{% hint style="info" %}
**Important:** Bito posts comments using the Bitbucket user account linked to the Personal Access Token used during setup. To display "Bito" instead of your name, create a separate user account (e.g., Bito Agent) and use its token for integration.
{% endhint %}

Click **Validate** to ensure the token is functioning properly.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJfYP00SupO4zpbSiTm5F%2Fscrnli_UJQnm8OmlV2PmM_1.png?alt=media&#x26;token=296c329a-1095-4455-8d5a-7dbdd917b086" alt="" width="563"><figcaption></figcaption></figure>

If the token is successfully validated, click **Connect Bito to Bitbucket** to proceed.

### **Step 5: Enable AI Code Review Agent on repositories** <a href="#step-5-enable-ai-code-review-agent-on-repositories" id="step-5-enable-ai-code-review-agent-on-repositories"></a>

After connecting Bito to your Bitbucket self-managed server, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FU0qx8lO9O8t6dj1lhX1r%2Fscrnli_XExOnuPOb2H8eW_1.png?alt=media&#x26;token=e6075bf3-fc4f-42ec-9ff6-396e2cd5894f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual merge request reviews** <a href="#step-6-automated-and-manual-merge-request-reviews" id="step-6-automated-and-manual-merge-request-reviews"></a>

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new pull requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the pull request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for pull requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review pull requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a pull request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull request.
{% endhint %}

### **Step 7: Specialized commands for code reviews** <a href="#step-7-specialized-commands-for-code-reviews" id="step-7-specialized-commands-for-code-reviews"></a>

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**

For more details, refer to [Available Commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).

### **Step 8: Chat with AI Code Review Agent** <a href="#step-8-chat-with-ai-code-review-agent" id="step-8-chat-with-ai-code-review-agent"></a>

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your pull request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)


# Integrate the AI Code Review Agent into the CI/CD pipeline

Automate code reviews in your Continuous Integration/Continuous Deployment (CI/CD) pipeline—compatible with all CI/CD tools, including Jenkins, Argo CD, GitLab CI/CD, and more.

[**Bito Cloud**](https://alpha.bito.ai/) lets you integrate the [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) into your CI/CD pipeline for automated code reviews. This document provides a step-by-step guide to help you configure and run the script successfully.

## Installation and Configuration Steps

1. [**Select the appropriate Git provider guide from this link**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/..#connect-bito-to-your-git-provider) based on your Git provider, and follow the step-by-step instructions to install the **AI Code Review Agent** using **Bito Cloud**. Be sure to review the prerequisites and the installation/configuration steps provided in the documentation.
2. [**Download the bito-action-script folder from GitHub**](https://github.com/gitbito/CodeReviewAgent/tree/main/bito-action-script), which includes a shell script (`bito-actions.sh`) and a configuration file (`bito_action.properties`).
3. You can integrate the AI Code Review Agent into your CI/CD pipeline in two ways, depending on your preference:

* **Option 1: Using the** `bito_action.properties` **File**
  * Configure the following properties in the `bito_action.properties` file located in the downloaded **bito-action-script** folder.

<table><thead><tr><th width="261" align="center">Property Name</th><th>Description</th></tr></thead><tbody><tr><td align="center"><strong>agent_instance_url</strong></td><td>The URL of the Agent instance provided after configuring the AI Code Review Agent with Bito Cloud.</td></tr><tr><td align="center"><strong>agent_instance_secret</strong></td><td>The secret key for the Agent instance obtained after configuring the AI Code Review Agent with Bito Cloud.</td></tr><tr><td align="center"><strong>pr_url</strong></td><td>URL of your pull request on GitLab, GitHub, or BitBucket.</td></tr></tbody></table>

* Run the following command:
  * `./bito_actions.sh bito_action.properties`
  * **Note:** When using the properties file, make sure to provide all the three parameters in `.properties` file

* #### **Option 2: Using Runtime Values** <a href="#option-2-using-runtime-values" id="option-2-using-runtime-values"></a>
  * Provide all necessary values directly on the command line:
    * `./bito_actions.sh agent_instance_url=<agent_instance_url> agent_instance_secret=<secret> pr_url=<pr_url>`
    * Replace `<agent_instance_url>`, `<secret>`, and `<pr_url>` with your specific values.
  * **Note:** You can also override the values given in the `.properties` file or provide values that are not included in the file. For example, you can configure `agent_instance_url` and `agent_instance_secret` in the `bito_action.properties` file, and only pass `pr_url` on the command line during runtime.
    * `./bito_actions.sh bito_action.properties pr_url=<pr_url>`
    * Replace `<pr_url>` with your specific values.

4. Incorporate the AI Code Review Agent into your CI/CD pipeline by adding the appropriate commands to your build or deployment scripts. This integration will automatically trigger code reviews as part of the pipeline, enhancing your development workflow by enforcing code quality checks with every change.


# Create or customize an Agent instance

Customize the AI Code Review Agent to match your workflow needs.

{% embed url="<https://youtu.be/Oj4A8wd1bio>" %}

[Connecting your Bito workspace to GitHub, GitLab, or Bitbucket](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/..#connect-bito-to-your-git-provider) provides immediate access to the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview). To get you started quickly, Bito offers a **Default Agent** instance—pre-configured and ready to deliver AI-powered code reviews for pull requests and code changes within supported IDEs such as VS Code and JetBrains.

While the **Default Agent** is ready for use right away, Bito also gives you the option to **create new Agent instances** or **customize existing ones** to suit your specific requirements. This flexibility ensures that the Agent can adapt to a range of workflows and project needs.

For example, you might configure one Agent to disable automatic code reviews for certain repositories, another to exclude specific Git branches from review, and yet another to filter out particular files or folders.

This guide will walk you through how to create or customize an Agent instance, unlocking its full potential to streamline your code reviews.

## Creating or customizing AI Code Review Agents&#x20;

Once Bito is connected to your GitHub/GitLab/Bitbucket account, you can easily create a new Agent or customize an existing one to suit your workflow.&#x20;

1. To **create a new Agent**, navigate to the [Code Review > Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard and click the **New Agent** button to open the Agent configuration form.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fe9yWzaBjGDsbCO0TPlE0%2Fscrnli_bfuIbaAP51Klgu.png?alt=media&#x26;token=db8e0ec4-34d8-4684-b4ad-770f36b1d10b" alt=""><figcaption></figcaption></figure>

2. If you’d like to **customize an existing agent**, simply go to the same [Code Review > Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard and click the **Settings** button next to the Agent instance you wish to modify.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNxy8j3UEcxh947QxMj9h%2Fscrnli_4T03Igj7d1r855.png?alt=media&#x26;token=698cb777-e48f-4e1b-bbbf-9e24a317f30f" alt=""><figcaption></figcaption></figure>

Once you have selected an Agent to customize, you can modify its settings in the following areas:&#x20;

&#x20;

## 1. General settings&#x20;

### Agent name&#x20;

Assign a unique alphanumeric name to your Agent. This name acts as an identifier and allows you to invoke the Agent in supported clients using the **`@<agent_name>`** command.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXEjUlDn834h978fCjNH0%2Fscrnli_ZCd0tIRfH725KX_1.png?alt=media&#x26;token=00e30f6d-66df-42f4-a3cb-58ad67f0eb36" alt=""><figcaption></figcaption></figure>

## 2. Customization options&#x20;

Bito provides six tabs for in-depth Agent customization.

These include:

1. Review
2. Custom Guidelines
3. Filters
4. Tools
5. Chat
6. Functional Validation

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F2GeZTPCoolZnQ3jvhFBE%2F10.png?alt=media&#x26;token=886fb830-8c2a-4402-9654-a21ccf8d48f1" alt=""><figcaption></figcaption></figure>

Let's have a look at each tab in detail.

### a. Review

In this tab, you can configure how and when the Agent performs reviews:&#x20;

* **Review language:** Select the output language for code review feedback.
  &#x20;Bito supports over 20 languages, including English, Hindi, Chinese, and Spanish. The AI code review feedback will be posted on the pull requests in the selected language.&#x20;
* **Review feedback mode:** Choose between **Essential** and **Comprehensive** review modes and tailor review request settings to fit your team's unique workflow requirements.
  * In **Essential** mode, only critical issues are posted as inline comments, and other issues appear in the main review summary under "Additional issues".
  * In **Comprehensive** mode, Bito also includes minor suggestion and potential nitpicks as inline comments.
* **Automatic review:** Toggle to enable or disable automatic reviews when a pull request is created and ready for review.&#x20;
* **Automatic incremental review:** Toggle to enable or disable reviews for new commits added to a pull request. Only changes since the last review are assessed.
  * **Batch time:** Specifies how long the AI Code Review Agent waits before running an incremental review after new commits are pushed. The value can range from **`0m` (review immediately)** to **`24h` (review after 24 hours)**. Lower values result in more frequent incremental reviews.

    **Examples:**

    * `10s` → waits **10 seconds** before running the review
    * `12m` → waits **12 minutes** before running the review
    * `1h10m` → waits **1 hour and 10 minutes** before running the review
* **Request changes comments:**  Enable this option to get Bito feedback as **"Request changes"** review comments. Depending on your organization's Git settings, you may need to resolve all comments before merging.
* **Draft pull requests:** By default, the Agent excludes draft pull requests from automated reviews. Disable this toggle to include drafts.&#x20;
* **Automatic summary:** Toggle to enable automatic generation of AI summaries for changes, which are appended to the pull request description.&#x20;
* **Change Walkthrough:** Enable this option to generate a table of changes and associated files, posted as a comment on the pull request.
* **Allow config file settings:** Enabling this setting will allow Agent Settings to be overridden at a repository level by placing a `.bito.yaml` file in the root folder of that repository. [**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/agent-settings/repo-level-settings)
* **Auto-apply agent rules:** Automatically detect and apply best-practice guidelines from agent configuration files like `CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, `.windsurf/rules`, or `GEMINI.md`. When enabled, Bito uses these files to guide its code review. [**Learn more**](https://docs.bito.ai/implementing-custom-code-review-rules#id-3-use-project-specific-guideline-files)
* **Generate interaction diagrams:** When enabled, Bito will generate interaction diagrams during code reviews to visualize the architecture and impacted components in the submitted changes. Currently, it is supported for GitHub and GitLab.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FpxtYSjIHTkO3bijBl9EO%2F1_1.png?alt=media&#x26;token=2bb7e440-4016-4533-b708-4abc4b1555bf" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FVzcTL5nQ0caUVHuKWfyb%2F2.png?alt=media&#x26;token=e47027db-2e68-4334-810f-9965addbf9f3" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKAAly95OdJxOiYDYBuUJ%2F3.png?alt=media&#x26;token=257dffd9-25cd-4add-8216-3128312463f4" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FISyUsZj0LOXlI0aR0CAT%2F4.png?alt=media&#x26;token=01bf1c7f-057e-41df-a33c-3b2829725766" alt=""><figcaption></figcaption></figure>

### b. Custom Guidelines

Create, apply, and manage custom code review guidelines to align the AI agent’s reviews with your team’s specific coding standards.

The agent will follow your guidelines when reviewing pull requests.

[**Learn more**](https://docs.bito.ai/implementing-custom-code-review-rules#id-2-create-custom-code-review-guidelines)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqmcctH3kkEwx9t59Iuny%2F5_1.png?alt=media&#x26;token=484f6982-f678-4667-b317-799ac42f64d9" alt=""><figcaption></figcaption></figure>

### c. Filters

Use filters to customize which files, folders, and Git branches are reviewed when the Agent triggers automatically on pull requests:

* **Exclude Files and Folders:** A list of files/folders that the AI Code Review Agent will not review if they are present in the diff. You can specify the files/folders to exclude from the review by name or glob/regex pattern. The Agent will automatically skip any files or folders that match the exclusion list. This filter applies to both manual reviews initiated through the **`/review`** command and automated reviews.&#x20;
* **Include Source/Target Branches:** This filter defines which pull requests trigger automated reviews based on their source or target branch, allowing you to focus on critical code and avoid unnecessary reviews or AI usage. By default, pull requests merging into the repository’s default branch are subject to review. To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review pull requests when the source or target branch matches the list. This filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
* **Exclude Labels:** Specify pull request (PR) labels to exclude from review by name or glob/regex pattern. The agent will skip any PRs tagged with these labels in GitHub or GitLab.

{% hint style="info" %}
For more information and examples, see [Excluding Files, Folders, or Branches with Filters](https://docs.bito.ai/ai-code-reviews-in-git/excluding-files-folders-or-branches-with-filters).
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FoDyUYEgeEgHaETBSs13m%2F6_1.png?alt=media&#x26;token=1bf3dc7f-f41e-4249-9e24-180b559287b8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRdy2ev0LKHpQikPc8DOb%2Fscrnli_spc1zf61Vl2Olo.png?alt=media&#x26;token=4435cf84-ec24-4eac-b73c-f1cbc404d7d4" alt=""><figcaption></figcaption></figure>

### d. Tools

Enhance the Agent’s reviews by enabling additional tools for static analysis, security checks, and secret detection:&#x20;

* **Secret Scanner:** Enable this tool to detect and report secrets left in code changes.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBxRWhwG67YXEY1YzCS5X%2F7.png?alt=media&#x26;token=80f4d8dd-0afe-441f-9c2c-c76c1027a89c" alt=""><figcaption></figcaption></figure>

### e. Chat

You can chat with the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git) to ask follow-up questions, request alternative solutions, or get clarification on review comments. From this tab, you can manage how the agent responds to these interactions.

* **Auto reply:** Enable Bito to automatically reply to user questions posted as comments on its code review suggestions—no need to tag `@bitoagent` or `@askbito`.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FHlkbzLfeOebXiSPeQVDh%2F8.png?alt=media&#x26;token=0546df4a-2861-4712-82c2-1eaddc8e3a0b" alt=""><figcaption></figcaption></figure>

### f. Functional Validation

Automatically validate pull requests against Jira tickets. Ticket references are detected in the PR description, title, or branch name.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/jira-integration)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqDvk5U9eGFLX3zZXJlBs%2F9.png?alt=media&#x26;token=4c202619-86c9-47d5-964b-54e82a8e3db3" alt=""><figcaption></figcaption></figure>

If you are editing an existing agent, click **Save** to apply the changes.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhFyPs3udWaoGryZNNtIu%2Fscrnli_Dy0cDQUimhLw3F.png?alt=media&#x26;token=a7623f7c-0e0d-47a9-ab88-605ec686ca7e" alt=""><figcaption></figcaption></figure>

## 3. Select repositories for code review

1. If you are creating a new agent instance, click **Select repositories** after configuration to choose the Git repositories the agent will review.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FovkmqjzPOyWwf2grajKm%2F11.png?alt=media&#x26;token=5f66a283-5fd7-4b41-8cdd-991f04284bf3" alt=""><figcaption></figcaption></figure>

2. To enable code review for a specific repository, simply select its corresponding checkbox. You can also enable repositories later, after the Agent has been created. Once done, click **Save and continue** to save the new Agent configuration.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F4l97XCS4fu5KW3aU5H7w%2Fscrnli_D5yUG72YO9dlpi_1.png?alt=media&#x26;token=f9c1c2fd-1a2e-4303-a527-f55e549e0c13" alt=""><figcaption></figcaption></figure>

3. When you save the configuration, your new Agent instance will be added and available on the [**Code Review > Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F9EdG6H9gT3WQKHGTgMbf%2Fscrnli_P0jT2f89e9j4He.png?alt=media&#x26;token=f38b7ff1-6192-4b16-bb5d-2e5e316ae737" alt=""><figcaption></figcaption></figure>


# Clone an Agent instance

Easily duplicate Agent configurations for faster setup.

Save time and effort by quickly creating a new [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) instance using the configuration settings of an existing one. It’s a fast and simple way to set up multiple Agent instances without having to reconfigure each one.

Follow the steps below to get started:

1. [**Log in to Bito Cloud**](https://alpha.bito.ai/) and select a workspace to get started.
2. From the left sidebar, select [**Code Review Agents**](https://alpha.bito.ai/home/ai-agents/code-review-agent).

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FWAlD5Tm3CGt1ZRlSKMpy%2Fscrnli_5pO6ZemgqQagoE.png?alt=media&#x26;token=ede8c747-b4a2-43ca-b825-013a5aedf169" alt=""><figcaption></figcaption></figure>

3. If your Bito workspace is connected to your GitHub/GitLab/Bitbucket account, a list of AI Code Review Agent instances configured in your workspace will appear. Locate the instance you wish to duplicate and click the **Clone** button given in front of it.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FtJeW5xZfsN21VIJTsgub%2Fscrnli_tkWuHJHpsQFmZS.png?alt=media&#x26;token=00b8aa6d-0d21-4753-9ea6-078e88fa0527" alt=""><figcaption></figcaption></figure>

4. An Agent configuration form will open, pre-populated with the input field values. You can edit these values as needed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FdYi4tC2DtqsD17guGho2%2Fscrnli_IfvRZsM0gmzHgj_1.png?alt=media&#x26;token=9cc3dd35-4bb7-4272-bc38-1a64abb4ba15" alt="" width="563"><figcaption></figcaption></figure>

5. Click **Select repositories** to choose Git repositories for the new Agent.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FxcWpSGp6bW3cx1DRTfCM%2Fscrnli_QGxSmiYenNC3Lk.png?alt=media&#x26;token=a7644e4d-a2fa-4136-82f9-29cfee954ca7" alt="" width="563"><figcaption></figcaption></figure>

6. To enable code review for a specific repository, simply select its corresponding checkbox. You can also enable repositories later, after the Agent has been created. Once done, click **Save and continue** to save the new Agent configuration.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fh4PMscB79SgNukvOatA2%2Fscrnli_vg5QAanR0PkKBy_1.png?alt=media&#x26;token=7b86cf8c-b5a8-4a11-a41f-22849adc768c" alt=""><figcaption></figcaption></figure>

7. When you save the configuration, your new Agent instance will be added and available on the [**Code Review Agents**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKVF4JfSXFrj1ImqWrT2q%2Fscrnli_d0bB9ZWwmQ1DQf.png?alt=media&#x26;token=487f6848-d1e7-4cf1-a78d-5aab51161065" alt=""><figcaption></figcaption></figure>


# Delete unused Agent instances

Easily delete Agent instances you no longer need.

If you no longer need an [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) instance, you can delete it to keep your workspace organized. Follow the steps below to quickly remove any unused Agents.

1. [**Log in to Bito Cloud**](https://alpha.bito.ai/) and select a workspace to get started.
2. From the left sidebar, select [**Code Review Agents**](https://alpha.bito.ai/home/ai-agents/code-review-agent).

   If your Bito workspace is connected to your GitHub/GitLab/Bitbucket account, a list of AI Code Review Agent instances configured in your workspace will appear.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXPaSaBzjEl3Oenag60Sc%2Fscrnli_14ld2xgfJQRoXF.png?alt=media&#x26;token=dfcb846f-d813-446a-be41-949603b32aec" alt=""><figcaption></figcaption></figure>

2. Before deleting an Agent, ensure that any repositories currently using it are reassigned to another Agent otherwise a warning popup will appear.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fm3GDTxzzl5x18aN7cx9f%2Fscrnli_643th6cTMQyfME_1.png?alt=media&#x26;token=fab3011c-5c8d-4081-bb33-110d7b32cd8a" alt=""><figcaption></figcaption></figure>

3. Locate the Agent you wish to delete and click the **Delete** button given in front of it.

{% hint style="info" %}
**Note:** The **Default Agent** (provided by Bito) cannot be deleted.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNPnP1XN5rBFd3u75IH1V%2Fscrnli_0DhwMLUbEr6U2q.png?alt=media&#x26;token=f428971f-1cbf-4933-a496-92110c48bb2f" alt=""><figcaption></figcaption></figure>


# Install/run as a self-hosted service

Deploy the AI Code Review Agent on your machine.

The self-hosted AI Code Review Agent offers a more private and customizable option for teams looking to enhance their code review processes within their own infrastructure, while maintaining complete control over their data. This approach is ideal for organizations with specific compliance, security, or customization requirements.

## Understanding CLI vs webhooks service

When setting up the AI Code Review Agent, you have the flexibility to choose between two primary modes of operation: **CLI** and **webhooks service**.

* **CLI** allows developers to manually initiate code reviews directly from terminal. This mode is ideal for quick, on-demand code reviews without the need for continuous monitoring or integration.
* **Webhooks service** transforms the Agent into a persistent service that automatically triggers code reviews based on specific events, such as pull requests or comments on pull requests. This mode is suitable for teams looking to automate their code review processes.

For more details, visit the [**CLI vs webhooks service**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/cli-vs-webhooks-service) page.

## Deployment Options

Based on your needs and the desired integration level with your development workflow, choose one of the following options to install and run the AI Code Review Agent:

{% hint style="info" %}
Before proceeding, ensure you've completed all necessary [**prerequisites for self-hosted**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/prerequisites) AI Code Review Agent.
{% endhint %}

1. [**Install/run via CLI**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-cli): Ideal for developers seeking a simple, interactive way to conduct code reviews from the command line.
2. [**Install/run via webhooks service**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-webhooks-service): Perfect for teams looking to automate code reviews through external events, enhancing their CI/CD workflow.
3. [**Install/run via GitHub Actions**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-github-actions): A great option for GitHub users to seamlessly integrate automated code reviews into their GitHub Actions workflows.


# Prerequisites

Key requirements for self-hosting the AI Code Review Agent.

## Minimum System Requirements

A machine with the following minimum specifications is recommended for Docker image deployment and for obtaining optimal performance of the AI Code Review Agent.

| Requirement     | Minimum Specification |
| --------------- | --------------------- |
| CPU Cores       | 4                     |
| RAM             | 8 GB                  |
| Hard Disk Drive | 80 GB                 |

***

## Supported Operating Systems

* Windows
* Linux
* macOS

***

## OS Prerequisites

<table><thead><tr><th width="192" align="center">Operating System</th><th>Installation Steps</th></tr></thead><tbody><tr><td align="center"><strong>Linux</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>Bash</strong> (minimum version 4.x)</p><ul><li><p>For Debian and Ubuntu systems</p><p><code>sudo apt-get install bash</code></p></li></ul><p></p><ul><li><p>For CentOS and other RPM-based systems</p><p><code>sudo yum install bash</code></p></li></ul></li></ol><p> </p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr><tr><td align="center"><strong>macOS</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>Bash</strong> (minimum version 4.x)</p><p><code>brew install bash</code></p></li></ol><p></p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr><tr><td align="center"><strong>Windows</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>PowerShell</strong> (minimum version 5.x)</p><ul><li><a href="https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4">View Guide</a></li><li>Note: In PowerShell version 7.x, run <code>Set-ExecutionPolicy Unrestricted</code> command. It allows the execution of scripts without any constraints, which is essential for running scripts that are otherwise blocked by default security settings.</li></ul></li></ol><p></p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr></tbody></table>

***

## Required Access Tokens

* **Bito Access Key:** Obtain your Bito Access Key. [**View Guide**](https://docs.bito.ai/help/account-and-settings/access-key)
* **GitHub Personal Access Token (Classic):** For GitHub PR code reviews, ensure you have a CLASSIC personal access token with repo access. We do not support fine-grained tokens currently. [**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)  &#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBZH0vDwrPqYQPMIxIyNW%2Fimage.png?alt=media&#x26;token=a4c42d8d-61a5-4cdb-87a1-622c0ba8f1ae" alt=""><figcaption><p><strong>GitHub Personal Access Token (Classic)</strong></p></figcaption></figure>

* **GitLab Personal Access Token:** For GitLab PR code reviews, a token with API access is required. [**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FghbsjA3aafRQJBQGnksv%2Fimage%20(1).png?alt=media&#x26;token=6feb55f7-39b3-4d61-8e46-f6b233e64849" alt=""><figcaption><p><strong>GitLab Personal Access Token</strong></p></figcaption></figure>

* **Snyk API Token (Auth Token):** For Snyk vulnerability reports, obtain a Snyk API Token. [**View Guide**](https://docs.snyk.io/getting-started/how-to-obtain-and-authenticate-with-your-snyk-api-token)


# CLI vs webhooks service

From one-time reviews to continuous automated reviews.

On your machine or in a Private Cloud, you can run the AI Code Review Agent via either CLI or webhooks service. This guide will teach you about the key differences between CLI and webhooks service and when to use each mode.

## Difference Between CLI and webhooks service

The main difference between CLI and webhooks service lies in their operational approach and purpose. In CLI, the docker container is used for a one-time code review. This mode is ideal for isolated, single-instance analyses where a quick, direct review of the code is needed.

On the other hand, webhooks service is designed for continuous operation. When set in webhooks service mode, the AI Code Review Agent remains online and active at a specified URL. This continuous operation allows it to respond automatically whenever a pull request is opened in a repository. In this scenario, the git provider notifies the server, triggering the AI Code Review Agent to analyze the pull request and post its review as a comment directly on it.

## When to Use CLI and When to Use webhooks service

Selecting the appropriate mode for code review with the AI Code Review Agent depends largely on the nature and frequency of your code review needs.

### CLI: Ideal for Specific, One-Time Reviews

CLI mode is best suited for scenarios requiring immediate, one-time code reviews. It's particularly effective for:

* Conducting quick assessments of specific pull requests.
* Performing periodic, scheduled code analyses.
* Reviewing code in environments with limited or no continuous integration support.
* Integrating with batch processing scripts for ad-hoc analysis.
* Using in educational settings to demonstrate code review practices.
* Experimenting with different code review configurations.
* Reviewing code on local setups or for personal projects.
* Performing a final check before pushing code to a repository.

CLI mode stands out for its simplicity and is perfect for standalone tasks where a single, direct execution of the code review process is all that's needed.

### Webhooks service: For Continuous, Automated Reviews

Webhooks service, on the other hand, is the go-to choice for continuous code review processes. It excels in:

* Continuously monitoring all pull requests in a repository.
* Providing instant feedback in collaborative projects.
* Seamlessly integrating with CI/CD pipelines for automated reviews.
* Performing automated code quality checks in team environments.
* Conducting real-time security scans on new pull requests.
* Ensuring adherence to coding standards in every pull request.
* Streamlining the code review process in large-scale projects.
* Maintaining consistency in code review across multiple projects.
* Enhancing workflows in remote or distributed development teams.
* Offering prompt feedback in agile development settings.

Webhooks service is indispensable in active development environments where consistent monitoring and immediate feedback are critical. It automates the code review process, integrating seamlessly into the workflow and eliminating the need for manual initiation of code reviews.


# Install/run via CLI

CLI mode is best suited for immediate, one-time code reviews.

1. **Prerequisites:** Before proceeding, ensure you've completed all necessary [**prerequisites for self-hosted**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/prerequisites) AI Code Review Agent.
2. **Start Docker:** Ensure Docker is running on your machine.
3. **Repository Download:** [**Download the AI Code Review Agent**](https://github.com/gitbito/codereviewagent) GitHub repository to your machine.
4. **Extract and Navigate:**

* Extract the downloaded .zip file to a preferred location.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBauSkjRmacbzGKV3ESwO%2F1.PNG?alt=media&#x26;token=4faa99de-529c-4b75-bb73-2c5bccf26850" alt=""><figcaption></figcaption></figure>

* Navigate to the extracted folder and then to the “cra-scripts” subfolder.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeupW2typotZUOO8hbmke%2F2.PNG?alt=media&#x26;token=f955c60c-cdd4-480a-8bda-f90ef3c5376c" alt=""><figcaption></figcaption></figure>

* Note the full path to the “cra-scripts” folder for later use.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJB3b2oKe3UEEz0xBIzI1%2Fcra_5.png?alt=media&#x26;token=86d352d7-990b-4392-9e3f-3cf451b22d5c" alt=""><figcaption></figcaption></figure>

5. **Open Command Line:**
   * Use Bash for Linux and macOS.
   * Use PowerShell for Windows.
6. **Set Directory:**
   * Change the current directory in Bash/PowerShell to the “cra-scripts” folder.
   * Example command: `cd [Path to cra-scripts folder]`
   * Adjust the path based on your extraction location.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F1VSZoDtgl9NwqFqu3A44%2F6.PNG?alt=media&#x26;token=3fdefd2a-dad1-436d-911f-51f216d1ef76" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFGkgrLhGlvDiTc5lLePW%2F7.PNG?alt=media&#x26;token=2058e7a7-7819-49cc-ad69-8b4b90af9d12" alt=""><figcaption></figcaption></figure>

7. **Configure Properties:**
   * Open the **bito-cra.properties** file in a text editor from the “cra-scripts” folder. Detailed information for each property is provided on [**Agent Configuration: bito-cra.properties File**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.
   * Set mandatory properties:
     * mode = cli
     * pr\_url
     * bito\_cli.bito.access\_key
     * git.provider
     * git.access\_token

{% hint style="info" %}
**Note:** Valid values for git.provider are GITHUB, GITLAB, or BITBUCKET.
{% endhint %}

* Optional properties (can be skipped or set as needed):
  * git.domain
  * code\_feedback
  * static\_analysis
  * dependency\_check
  * dependency\_check.snyk\_auth\_token
  * review\_scope
  * exclude\_branches
  * exclude\_files
  * exclude\_draft\_pr

{% hint style="info" %}
**Note:** Detailed information for each property is provided on [**Agent Configuration: bito-cra.properties File**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.
{% endhint %}

{% hint style="info" %}
Check the [**Required Access Tokens**](https://docs.bito.ai/ai-code-reviews-in-git/prerequisites#required-access-tokens) guide to learn more about creating the access tokens needed to configure the Agent.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ftwj5rCsz3vdrUfflvjxI%2Fproperties_file.png?alt=media&#x26;token=e39a928d-accf-454a-af03-ffb97dbc68a5" alt=""><figcaption></figcaption></figure>

8. **Run the Agent:**
   * On Linux/macOS in Bash: Run `./bito-cra.sh bito-cra.properties`
   * On Windows in PowerShell: Run `./bito-cra.ps1 bito-cra.properties`

{% hint style="info" %}
This step might take time initially as it pulls the Docker image and performs the code review.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSjDE0OgQ9x2lZfR5mjh6%2F8.PNG?alt=media&#x26;token=f122f4a8-cd4f-46e2-8afd-6fa7efc80234" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FK41KV7WlXAmuZpZCqojj%2Fcra_6.png?alt=media&#x26;token=0c66339b-6cce-4942-b4d5-f1ae85cdae64" alt=""><figcaption></figcaption></figure>

9. **Final Steps:**
   * The script may prompt values of mandatory/optional properties if they are not preconfigured.
   * Upon completion, a code review comment is automatically posted on the Pull Request specified in the **pr\_url** property.

{% hint style="info" %}
**Note:** To improve efficiency, the AI Code Review Agent is disabled by default for pull requests involving the **"main"** branch. This prevents unnecessary processing and token usage, as changes to the **"main"** branch are typically already reviewed in release or feature branches. To change this default behavior and include the **"main"** branch, please [**contact support**](mailto:support@bito.ai).
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


# Install/run via webhooks service

The webhooks service is best suited for continuous, automated reviews.

## Prerequisites

### Minimum System Requirements

A machine with the following minimum specifications is recommended for Docker image deployment and for obtaining optimal performance of the AI Code Review Agent.

| Requirement     | Minimum Specification |
| --------------- | --------------------- |
| CPU Cores       | 4                     |
| RAM             | 8 GB                  |
| Hard Disk Drive | 80 GB                 |

***

### Supported Operating Systems

* Windows
* Linux
* macOS

***

### OS Prerequisites

<table><thead><tr><th width="192" align="center">Operating System</th><th>Installation Steps</th></tr></thead><tbody><tr><td align="center"><strong>Linux</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>Bash</strong> (minimum version 4.x)</p><ul><li><p>For Debian and Ubuntu systems</p><p><code>sudo apt-get install bash</code></p></li></ul><p></p><ul><li><p>For CentOS and other RPM-based systems</p><p><code>sudo yum install bash</code></p></li></ul></li></ol><p> </p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr><tr><td align="center"><strong>macOS</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>Bash</strong> (minimum version 4.x)</p><p><code>brew install bash</code></p></li></ol><p></p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr><tr><td align="center"><strong>Windows</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>PowerShell</strong> (minimum version 5.x)</p><ul><li><a href="https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4">View Guide</a></li><li>Note: In PowerShell version 7.x, run <code>Set-ExecutionPolicy Unrestricted</code> command. It allows the execution of scripts without any constraints, which is essential for running scripts that are otherwise blocked by default security settings.</li></ul></li></ol><p></p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr></tbody></table>

***

### Required Access Tokens

* **Bito Access Key:** Obtain your Bito Access Key. [**View Guide**](https://docs.bito.ai/help/account-and-settings/access-key)
* **GitHub Personal Access Token (Classic):** For GitHub PR code reviews, ensure you have a CLASSIC personal access token with repo access. We do not support fine-grained tokens currently. [**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)  &#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBZH0vDwrPqYQPMIxIyNW%2Fimage.png?alt=media&#x26;token=a4c42d8d-61a5-4cdb-87a1-622c0ba8f1ae" alt=""><figcaption><p><strong>GitHub Personal Access Token (Classic)</strong></p></figcaption></figure>

* **GitLab Personal Access Token:** For GitLab PR code reviews, a token with API access is required. [**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FghbsjA3aafRQJBQGnksv%2Fimage%20(1).png?alt=media&#x26;token=6feb55f7-39b3-4d61-8e46-f6b233e64849" alt=""><figcaption><p><strong>GitLab Personal Access Token</strong></p></figcaption></figure>

* **Snyk API Token (Auth Token):** For Snyk vulnerability reports, obtain a Snyk API Token. [**View Guide**](https://docs.snyk.io/getting-started/how-to-obtain-and-authenticate-with-your-snyk-api-token)

***

## Installation and Configuration Steps

1. **Prerequisites:** Before proceeding, ensure you've completed all necessary [**prerequisites for self-hosted**](#prerequisites) AI Code Review Agent.
2. **Server Requirement:** Ensure you have a server with a domain name or IP address.
3. **Start Docker:** Initialize Docker on your server.
4. **Clone the repository:** [**Clone the AI Code Review Agent**](https://github.com/gitbito/codereviewagent) GitHub repository to your server using the following command:
   * `git clone https://github.com/gitbito/CodeReviewAgent.git`
   * **Note:** It is recommended to clone the repository instead of downloading the .zip file. This approach allows you to easily [**update the Agent**](#how-to-update-the-self-hosted-ai-code-review-agent) later using the `git pull` command.
5. **Open the repository folder:**
   * Navigate to the repository folder and then to the “cra-scripts” subfolder.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FYaZdU057J1qY8mpafUQP%2F2.PNG?alt=media&#x26;token=4ad6af3d-47be-442b-9c5d-2bdc0400c944" alt=""><figcaption></figcaption></figure>

* Note the full path to the “cra-scripts” folder for later use.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FmuagwhDXqUteSbOTJNPp%2Fcra_5.png?alt=media&#x26;token=7f776742-cd2f-4db2-8a00-b2165ee44752" alt=""><figcaption></figcaption></figure>

6. **Open Command Line:**
   * Use Bash for Linux and macOS.
   * Use PowerShell for Windows.
7. **Set Directory:**
   * Change the current directory in Bash/PowerShell to the “cra-scripts” folder.
   * Example command: `cd [Path to cra-scripts folder]`
   * **Note:** Adjust the path based on where you cloned the repository on your system.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FGnsxyvCury17bK6ojK9V%2F6.PNG?alt=media&#x26;token=fca033ea-6f05-4bf8-a033-75ee11be7e4a" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8A09WmtAoKU9Cln7b3uf%2F7.PNG?alt=media&#x26;token=da370a92-d4e5-4710-a097-4fa789fe54a3" alt=""><figcaption></figcaption></figure>

8. **Configure Properties:**
   * Open the **bito-cra.properties** file in a text editor from the “cra-scripts” folder. Detailed information for each property is provided on [**Agent Configuration: bito-cra.properties File**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.
   * Set mandatory properties:
     * mode = server
     * bito\_cli.bito.access\_key
     * git.access\_token
   * Optional properties (can be skipped or set as needed):
     * git.provider
     * git.domain
     * code\_feedback
     * static\_analysis
     * dependency\_check
     * dependency\_check.snyk\_auth\_token
     * server\_port
     * review\_scope
     * exclude\_branches
     * exclude\_files
     * exclude\_draft\_pr

{% hint style="info" %}
**Note:** Valid values for git.provider are GITHUB or GITLAB.
{% endhint %}

{% hint style="info" %}
**Note:** Detailed information for each property is provided on [**Agent Configuration: bito-cra.properties File**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.
{% endhint %}

{% hint style="info" %}
Check the [**Required Access Tokens**](https://docs.bito.ai/ai-code-reviews-in-git/prerequisites#required-access-tokens) guide to learn more about creating the access tokens needed to configure the Agent.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRlugvd7UX2qXOoAwhnsL%2Fcra_9.png?alt=media&#x26;token=0522b55c-a95a-4264-9853-980d09cfcfa9" alt=""><figcaption></figcaption></figure>

9. **Run the Agent:**
   * **On Linux/macOS in Bash:**
     * Run `./bito-cra.sh service start bito-cra.properties`
     * **Note:** It will provide the Git Webhook secret in encrypted format.
   * **On Windows in PowerShell:**
     * Install OpenSSL
       * Reference-1: <https://wiki.openssl.org/index.php/Binaries>
       * Reference-2: <https://slproweb.com/products/Win32OpenSSL.html>
     * Run `./bito-cra.ps1 service start bito-cra.properties`
     * **Note:** It will provide the Git Webhook secret in encrypted format.

{% hint style="info" %}
This step might take time initially as it pulls the Docker image and performs the code review.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FzalttOI7Osr6BzwS94fW%2F8.PNG?alt=media&#x26;token=8615d023-cd00-4fc1-9616-9b6df3abd6c0" alt=""><figcaption></figcaption></figure>

10. **Provide Missing Property Values:** The script may prompt for values of mandatory/optional properties if they are not preconfigured.
11. **Copy Webhook Secret:** During the script execution, a webhook secret is generated and displayed in the shell. Copy the secret displayed under **"Use below as Gitlab and Github Webhook secret:"** for use in GitHub or GitLab when setting up the webhook.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F2eGxT6LoIlvMmHmC3avR%2Fscrnli_1_22_2024_7-34-26%20AM.png?alt=media&#x26;token=dc037dff-e5aa-43b4-809c-e1d01f838a27" alt=""><figcaption></figcaption></figure>

## Webhook Setup Guide

[**GitHub Webhook Setup Guide**](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks)**:**

* Login to your [GitHub](https://github.com/) account.
* Navigate to the main page of the repository. Under your repository name, click **Settings**.
* In the left sidebar, click **Webhooks**.
* Click **Add webhook**.
* Under **Payload URL**, enter the URL of the webhook endpoint. This is the server's URL to receive webhook payloads.
  * **Note:** The GitHub Payload URL should follow this format: `https://<domain name/ip-address>/api/v1/github_webhooks`, where `https://<domain name/ip-address>` should be mapped to Bito's AI Code Review Agent container, which runs as a service on a configured TCP port such as 10051. Essentially, you need to append the string **"/api/v1/github\_webhooks"** (without quotes) to the URL where the AI Code Review Agent is running.
  * For example, a typical webhook URL would be `https://cra.example.com/api/v1/github_webhooks`
* Select the **Content type** “application/json” for JSON payloads.
* In **Secret token**, enter the webhook secret token that you copied above. It is used to validate payloads.
* Click on **Let me select individual events** to select the events that you want to trigger the webhook. For code review select these:
  * **Issue comments** - To enable Code Review on-demand by issuing a command in the PR comment.
  * **Pull requests** - To auto-trigger Code Review when a pull request is created.
  * **Pull request review comments** - So, you can share feedback on the review quality by answering the feedback question in the code review comment.
* To make the webhook active immediately after adding the configuration, select **Active**.
* Click **Add webhook**.

[**GitLab Webhook Setup Guide**](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html#configure-a-webhook-in-gitlab)**:**

* Login to your [GitLab](https://gitlab.com/users/sign_in) account.
* Select the repository where the webhook needs to be configured.
* On the left sidebar, select **Settings > Webhooks**.
* Select **Add new webhook**.
* In **URL**, enter the URL of the webhook endpoint. This is the server's URL to receive webhook payloads.
  * **Note:** The GitLab webhook URL should follow this format: `https://<domain name/ip-address>/api/v1/gitlab_webhooks`, where `https://<domain name/ip-address>` should be mapped to Bito's AI Code Review Agent container, which runs as a service on a configured TCP port such as 10051. Essentially, you need to append the string **"/api/v1/gitlab\_webhooks"** (without quotes) to the URL where the AI Code Review Agent is running.
  * For example, a typical webhook URL would be `https://cra.example.com/api/v1/gitlab_webhooks`
* In **Secret token**, enter the webhook secret token that you copied above. It is used to validate payloads.
* In the **Trigger** section, select the events to trigger the webhook. For code review select these:
  * **Comments** - for on-demand code review.
  * **Merge request events** - for automatic code review when a merge request is created.
  * **Emoji events** - So, you can share feedback on the review quality using emoji reactions.
* Select **Add webhook**.

[**BitBucket Webhook Setup Guide**](https://support.atlassian.com/bitbucket-cloud/docs/create-and-trigger-a-webhook-tutorial/)**:**

* Login to your [BitBucket](https://bitbucket.org/) account.
* Navigate to the main page of the repository. Under your repository name, click **Repository Settings**.
* In the left sidebar, click **Webhooks**.
* Click **Add webhook**.
* Under **URL**, enter the URL of the webhook endpoint. This is the server's URL to receive webhook payloads.
  * **Note:** The BitBucket Payload URL should follow this format: `https://<domain name/ip-address>/api/v1/bitbucket_webhooks`, where `https://<domain name/ip-address>` should be mapped to Bito's AI Code Review Agent container, which runs as a service on a configured TCP port such as 10051. Essentially, you need to append the string **"/api/v1/bitbucket\_webhooks"** (without quotes) to the URL where the AI Code Review Agent is running.
  * For example, a typical webhook URL would be `https://cra.example.com/api/v1/bitbucket_webhooks`
* In **Secret token**, enter the webhook secret token that you copied above. It is used to validate payloads.
* In the **Triggers** section, select the events to trigger the webhook. For code review select these:
  * **Pull Request > Comment created** - for on-demand code review.
  * **Pull Request > Created** - for automatic code review when a merge request is created.
* Select **Save**.

***

## Using the AI Code Review Agent

After configuring the webhook, you can invoke the AI Code Review Agent in the following ways:

{% hint style="info" %}
**Note:** To improve efficiency, the AI Code Review Agent is disabled by default for pull requests involving the **"main"** branch. This prevents unnecessary processing and token usage, as changes to the **"main"** branch are typically already reviewed in release or feature branches. To change this default behavior and include the **"main"** branch, please [**contact support**](mailto:support@bito.ai).
{% endhint %}

1. **Automated Code Review**: If the webhook is configured to be triggered on the **Pull requests** event (for GitHub) or **Merge request** event (for GitLab), the agent will automatically review new pull requests as soon as they are created and post the review feedback as a comment within your PR.
2. **Manually Trigger Code Review:** To start the process, simply type **`/review`** in the comment box on the pull request and submit it. If the webhook is configured to be triggered on the **Issue comments** event (for GitHub) or **Comments** event (for GitLab), this action will initiate the code review process. The **`/review`** command prompts the agent to review the pull request and post its feedback directly in the PR as a comment.

   Bito also offers specialized commands that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.

   * **`/review security`:** Analyzes code to identify security vulnerabilities and ensure secure coding practices.
   * **`/review performance`:** Evaluates code for performance issues, identifying slow or resource-heavy areas.
   * **`/review scalability`:** Assesses the code's ability to handle increased usage and scale effectively.
   * **`/review codeorg`:** Scans for readability and maintainability, promoting clear and efficient code organization.
   * **`/review codeoptimize`:** Identifies optimization opportunities to enhance code efficiency and reduce resource usage.

   By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**

   For more details, refer to [Available Commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrcIGhiEeBRVPV69BaaiW%2Fscrnli_2_28_2024_8-57-29%20PM.png?alt=media&#x26;token=845b4c88-5b7a-4e7a-a9fb-13648095a15e" alt=""><figcaption></figcaption></figure>

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

***

## How to update the self-hosted AI Code Review Agent

Please follow these steps:

1. **Update the Agent's repository:**
   * Pull the latest changes from the <https://github.com/gitbito/CodeReviewAgent> repository by running the following command in your terminal, ensuring you are inside the repository folder:
   * `git pull origin main`
2. **Restart the Docker container:**
   * To restart the Docker container running as a service, use the below command.
   * **On Linux/macOS in Bash:** Run `./bito-cra.sh service restart bito-cra.properties`
   * **On Windows in PowerShell:** Run `./bito-cra.ps1 service restart bito-cra.properties`

***

## Stop Docker Container

To stop the Docker container running as a service, use the below command.

* On Linux/macOS in Bash: Run `./bito-cra.sh service stop`
* On Windows in PowerShell: Run `./bito-cra.ps1 service stop`

***

## Check Status

To check the status of Docker container running as a service, use the below command.

* On Linux/macOS in Bash: Run `./bito-cra.sh service status`
* On Windows in PowerShell: Run `./bito-cra.ps1 service status`


# Install/run via GitHub Actions

Seamlessly integrate automated code reviews into your GitHub Actions workflows.

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


# Agent Configuration: bito-cra.properties File

Setting up your agent: understanding the bito-cra.properties file

{% hint style="info" %}
**Note:** This file is only available for people who are using the [**self-hosted**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service) version of AI Code Review Agent.
{% endhint %}

The **bito-cra.properties** file offers a comprehensive range of options for configuring the [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview), enhancing its flexibility and adaptability to various workflow requirements.

## bito-cra.properties Available Options

<table><thead><tr><th width="232" align="center">Property Name</th><th>Supported Values</th><th width="141">Is Mandatory?</th><th>Description</th></tr></thead><tbody><tr><td align="center"><strong>mode</strong></td><td><ul><li>cli</li><li>server</li></ul></td><td>Yes</td><td>Whether to run the Docker container in CLI mode for a one-time code review or as a webhooks service to continuously monitor for code review requests.</td></tr><tr><td align="center"><strong>pr_url</strong></td><td>Pull request URL in GitLab, GitHub and Bitbucket</td><td>Yes, if the mode is CLI.</td><td><p>The pull request provides files with changes and the actual code modifications.<br><br>When the <code>mode</code> is set to <code>server</code>, the <code>pr_url</code> is received either through a webhook call or via a REST API call.</p><p> </p><p>This release only supports webhook calls; other REST API calls are not yet supported.</p></td></tr><tr><td align="center"><strong>code_feedback</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>Setting it to <code>True</code> activates general code review comments to identify functional issues. If set to <code>False</code>, general code review will not be conducted.</td></tr><tr><td align="center"><strong>bito_cli.bito.access_key</strong></td><td><p>A valid Bito Access Key generated through Bito's web UI.</p><p> </p><p><a href="https://docs.bito.ai/account-and-settings/access-key">Learn More</a></p></td><td>Yes</td><td>Bito Access Key is an alternative to standard email and OTP authentication.</td></tr><tr><td align="center"><strong>git.provider</strong></td><td><ul><li>GITLAB</li><li>GITHUB</li><li>BITBUCKET</li></ul></td><td>Yes, if the mode is CLI.</td><td>The name of git repository provider.</td></tr><tr><td align="center"><strong>git.access_token</strong></td><td>A valid Git access token provided by GITLAB or GITHUB or BITBUCKET</td><td>Yes</td><td>You can use a personal access token in place of a password when authenticating to GitHub/GitLab/BitBucket in the command line or with the API.</td></tr><tr><td align="center"><strong>git.domain</strong></td><td>A URL where Git is hosted.</td><td>No</td><td>It is used to enter the custom URL of self-hosted GitHub/GitLab Enterprise.</td></tr><tr><td align="center"><strong>static_analysis</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>Enable or disable static code analysis, which is used to uncover functional issues in the code.</td></tr><tr><td align="center"><strong>static_analysis_tool</strong></td><td><ul><li>fb_infer</li><li>astral_ruff</li><li>mypy</li></ul></td><td>No</td><td>Comma-separated list of static analysis tools to run (e.g., <code>fb_infer,astral_ruff,mypy</code>).</td></tr><tr><td align="center"><strong>linters_feedback</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>Enables feedback from linters like ESLint, golangci-lint, and Astral Ruff.</td></tr><tr><td align="center"><strong>secret_scanner_feedback</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>Enables detection of secrets in code. For example, passwords, API keys, sensitive information, etc.</td></tr><tr><td align="center"><strong>dependency_check</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>This feature is designed to identify security vulnerabilities in open-source dependency packages, specifically for JS/TS/Node.JS and GoLang. Without this input, reviews for security vulnerabilities will not be conducted.</td></tr><tr><td align="center"><strong>dependency_check.snyk_auth_token</strong></td><td>A valid authentication token for accessing Snyk's cloud-based security database.</td><td>No</td><td>If not provided, access to Snyk's cloud-based security database for checking security vulnerabilities in open-source dependency packages will not be available.</td></tr><tr><td align="center"><strong>code_context</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>Enables enhanced code context awareness.</td></tr><tr><td align="center"><strong>server_port</strong></td><td>A valid and available TCP port number.</td><td>No</td><td>This is applicable when the <code>mode</code> is set to <code>server</code>. If not specified, the default value is <code>10051</code>.</td></tr><tr><td align="center"><strong>review_comments</strong></td><td><ul><li>1</li><li>2</li></ul></td><td>No</td><td><p>Set the value to <code>1</code> to display the code review in a single post, or <code>2</code> to show code review as inline comments, placing suggestions directly beneath the corresponding lines in each file for clearer guidance on improvements.</p><p><br>The default value is <code>2</code>.</p></td></tr><tr><td align="center"><strong>review_scope</strong></td><td><ul><li>security</li><li>performance</li><li>scalability</li><li>codeorg</li><li>codeoptimize</li></ul></td><td>No</td><td>Specialized commands to perform detailed analyses on specific aspects of your code.<br><br>You can provide comma-separated values to perform multiple types of code analysis simultaneously.<br><br><a href="../../available-commands#review-scope"><strong>Learn more</strong></a></td></tr><tr><td align="center"><strong>include_source_branches</strong></td><td>Glob/regex pattern.</td><td>No</td><td>Comma-separated list of branch patterns (glob/regex) to allow as pull request sources.</td></tr><tr><td align="center"><strong>include_target_branches</strong></td><td>Glob/regex pattern.</td><td>No</td><td>Comma-separated list of branch patterns (glob/regex) to allow as pull request targets.</td></tr><tr><td align="center"><strong>exclude_files</strong></td><td>Glob/regex pattern.</td><td>No</td><td><p>A list of files/folders that the AI Code Review Agent will not review if they are present in the diff.</p><p></p><p>By default, these files are excluded: <code>*.xml</code>, <code>*.json</code>, <code>*.properties</code>, <code>.gitignore</code>, <code>*.yml</code>, <code>*.md</code><br><br><a href="../excluding-files-folders-or-branches-with-filters"><strong>Learn more</strong></a></p></td></tr><tr><td align="center"><strong>exclude_draft_pr</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>A binary setting that enables/disables automated review of pull requests (PR) based on the draft status.<br><br>The default value is <code>True</code> which skips automated review of draft PR.<br><br><a href="../excluding-files-folders-or-branches-with-filters"><strong>Learn more</strong></a></td></tr><tr><td align="center"><strong>cra_version</strong></td><td><ul><li>latest</li><li>Any specific version tag</li></ul></td><td>No</td><td>Sets the agent version to run (<code>latest</code> or a specific version tag).</td></tr><tr><td align="center"><strong>post_as_request_changes</strong></td><td><ul><li>True</li><li>False</li></ul></td><td>No</td><td>Posts feedback as 'Request changes' review comments. Depending on your organization's Git settings, you may need to resolve all comments before merging.</td></tr><tr><td align="center"><strong>support_email</strong></td><td>Email address</td><td>No</td><td>Contact email shown in error messages.</td></tr><tr><td align="center"><strong>suggestion_mode</strong></td><td><ul><li>essential</li><li>comprehensive</li></ul></td><td>No</td><td><p>Controls AI suggestion verbosity. Available options are <code>essential</code> and <code>comprehensive</code>.<br></p><p>In <strong>Essential</strong> mode, only critical issues are posted as inline comments, and other issues appear in the main review summary under "Additional issues".</p><p><br>In <strong>Comprehensive</strong> mode, Bito also includes minor suggestion and potential nitpicks as inline comments.</p></td></tr></tbody></table>

&#x20;

&#x20;


# Available commands

Invoke the AI Code Review Agent manually or within a workflow.

The [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) offers a suite of commands tailored to developers' needs. You can manually trigger a code review by entering any of these commands in the comment box below a pull/merge request on GitHub, GitLab, or Bitbucket and submitting the comment. Alternatively, if you are using the self-hosted version, you can configure these commands in the [**bito-cra.properties file**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) for automated code reviews.

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull/merge request.
{% endhint %}

## /review

This command provides a broad overview of your code changes, offering suggestions for improvement across various aspects but without diving deep for secure coding or performance optimizations or scalability improvements etc. This makes it ideal for catching general code quality issues that might not necessarily be critical blockers but can enhance readability, maintainability, and overall code health.

Think of it as a first-pass review to identify potential areas for improvement before delving into more specialized analyses.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FxlP180wDIuX69YbFO92n%2Fimage%20(9).png?alt=media&#x26;token=567f8c72-51aa-4682-8946-b540dc3258ec" alt=""><figcaption></figcaption></figure>

## Review Scope

Five specialized commands are available to perform detailed analyses on specific aspects of your code. Details for each command are given below.

1. `/review security`
2. `/review performance`
3. `/review scalability`
4. `/review codeorg`
5. `/review codeoptimize`

{% hint style="info" %}
You can provide comma-separated values to perform multiple types of code analysis simultaneously.

**Example:** `/review performance,security,codeoptimize`
{% endhint %}

### Combining general feedback with specialized review scopes

If you'd like to receive general code quality feedback alongside specialized analyses, include the `general` keyword in your review command.

For example, to receive feedback on general code quality, performance, and security, use:

* **Example:** `/review general,performance,security`

This ensures a holistic review encompassing both general code quality and specific areas of concern.

## /review security

This command performs an in-depth analysis of your code to identify vulnerabilities that could allow attackers to steal data, gain unauthorized access, or disrupt your application. This includes checking for weaknesses in input validation, output encoding, authentication, authorization, and session management. It also looks for proper encryption of sensitive data, secure coding practices, and potential misconfigurations that could expose your system.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fp7zoap8rRgTdWt8kqGxN%2Fscrnli_3_28_2024_2-59-52%20AM_1.png?alt=media&#x26;token=a4e78f8a-f0e6-4dcc-ba64-1e40a1cbea9b" alt=""><figcaption><p>Highlighting the security vulnerability detected and the proposed solution.</p></figcaption></figure>

## /review performance

This command evaluates the current performance of the code by pinpointing slow or resource-intensive areas and identifying potential bottlenecks. It helps developers understand where the code may be underperforming against expected benchmarks or standards. It is particularly useful for identifying slow processes that could benefit from further investigation and refinement.

This includes checking how well your code accesses data and manages tasks like database interactions and memory usage.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FoUbz3zRLYdIafoSro9AH%2Fscrnli_3_28_2024_3-05-21%20AM_2_1.png?alt=media&#x26;token=27535222-fdb7-4ce8-9d58-8ec4c2eede7d" alt=""><figcaption><p>Highlighting the performance issue detected and the proposed solution.</p></figcaption></figure>

## /review scalability

This command analyzes your code to identify potential roadblocks to handling increased usage or data. It checks how well the codebase supports horizontal scaling and whether it is compatible with load balancing strategies. It also ensures the code can handle concurrent requests efficiently and avoids bottlenecks from single points of failure. The command further examines error handling and retry mechanisms to promote system resilience under pressure.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvDYzSi6S0qB9IymAJtji%2Fscrnli_3_28_2024_3-05-21%20AM_1_1.png?alt=media&#x26;token=d0668429-845b-44a8-868d-8addaff3da15" alt=""><figcaption><p>Highlighting the scalability issue detected and the proposed solution.</p></figcaption></figure>

## /review codeorg

This command scans your code for readability, maintainability, and overall clarity. This includes checking for consistent formatting, clear comments, well-defined functions, and efficient use of data structures. It also looks for opportunities to reduce code duplication, improve error handling, and ensure the code is written for future growth and maintainability.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZXYio6wPTj0DsUxW8Uz0%2Fscrnli_3_28_2024_2-53-13%20AM_1.png?alt=media&#x26;token=ea6cdeb2-8b20-4c11-b48b-c049e7d9fd26" alt=""><figcaption><p>Highlighting the code structure issue detected and the proposed solution.</p></figcaption></figure>

## /review codeoptimize

This command helps identify specific parts of the code that can be made more efficient through optimization techniques. It suggests refactoring opportunities, algorithmic improvements, and areas where resource usage can be minimized. This command is essential for enhancing the overall efficiency of the code, making it faster and less resource-heavy.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FTKHJZ5xZ5ueLqlAVi7u8%2Fscrnli_3_28_2024_2-01-01%20AM_1.png?alt=media&#x26;token=27a7e6c0-77d7-4611-aabf-8eae284e635f" alt=""><figcaption><p>Precise code optimization advice pinpointing exact lines in a file.</p></figcaption></figure>

## Control code review workflow

These commands allow you to manage the AI Code Review Agent's behavior directly within your pull requests across GitHub, GitLab, and Bitbucket.

### /pause

Pauses automatic AI reviews on the current pull request.

**Use case:** Useful when significant changes are underway, and you want to prevent the AI from reviewing incomplete code.

**Example:** Add a comment with `/pause` to the pull request.

### /resume

Resumes the automatic AI reviews that were previously paused on the pull request.

**Use case:** Once your code changes are ready for review, use this command to re-enable the AI's automatic analysis.

**Example:** Add a comment with `/resume` to the pull request.

### /resolve

Marks all Bito-posted review comments as resolved.

**Use case:** After addressing the issues highlighted by the AI, use this command to clean up the comment threads.

**Example:** Add a comment with `/resolve` to the pull request.

{% hint style="info" %}
**Note:** The `/resolve` command is currently supported in GitLab and Bitbucket.
{% endhint %}

### /abort

Cancels all in-progress AI code reviews on the current pull request.

**Use case:** If an AI review is no longer needed or was initiated by mistake, this command stops the process.

**Example:** Add a comment with `/abort` to the pull request.

## Display Code Review in a Single Post

By default, the `/review` command generates inline comments, placing code suggestions directly beneath the corresponding lines in each file for clearer guidance on improvements. If you prefer a single consolidated code review instead of separate inline comments, use the `#inline_comment` parameter and set its value to `False`.

**Example:** `/review #inline_comment=False`

**Example:** `/review scalability #inline_comment=False`

{% hint style="info" %}
**Note:** The `/review` command defaults to `#inline_comment=True`, so you can omit this parameter when its value is `True`.
{% endhint %}


# Chat with AI Code Review Agent

Ask questions about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

Real-time collaboration with the AI Code Review Agent accelerates your development cycle. By delivering immediate, actionable insights, it eliminates the delays typically experienced with human reviews. Developers can engage directly with the Agent to clarify recommendations on the spot, ensuring that any issues are addressed swiftly and accurately.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

## How to chat?

To start a conversation, type your question directly as a reply to the Agent’s code review comment.&#x20;

The AI Code Review Agent will **analyze your comment and determine** if it’s a valid and relevant question.&#x20;

* If the agent decides it’s a valid question, it will respond with helpful insights.
* If the agent determines it’s unclear, off-topic, or not related to its feedback, it will **not respond**.

To help the agent recognize your question faster, you can also **tag your comment** with **@bitoagent** or **@askbito**. Tagging informs the Agent that your message is intended as a question. However, **tagging does not guarantee a reply**. The agent will still **analyze your comment and decide** whether it is a valid question worth responding to.

Bito usually responds within about 10 seconds.

* On **GitHub** and **Bitbucket**, you may need to manually refresh the page to see the response.
* On **GitLab**, updates happen automatically.

{% hint style="info" %}
**Note:** The AI Code Review Agent will only respond to questions posted as a reply to its own comments.\
It will not reply to questions added on threads that it didn’t start.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhvDrQ1DMSqIECpvjdstX%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=89b64664-0bea-4835-afba-5e85372338d2" alt="" width="563"><figcaption></figcaption></figure>

### What you can ask about

When chatting with the AI Code Review Agent, you can ask questions to better understand or improve the code feedback it provided. Here are examples of what you can ask:

* **Clarifications about a highlighted issue**\
  Ask the AI to explain why it flagged a certain line of code or why something might cause a problem.
* **Request for alternative solutions**\
  Request different ways to fix or improve the code beyond what was originally suggested.
* **Deeper explanations**\
  If you want to understand the technical reasoning behind a suggestion (e.g., security concerns, performance impacts, best practices), you can ask for more detailed explanations.
* **Request for examples**\
  Ask the AI to provide an example snippet showing the corrected or improved code.
* **Trade-off discussions**\
  Ask the AI about pros and cons of different approaches it may have suggested (e.g., performance vs. readability).
* **Best practices guidance**\
  Request advice on best practices related to the specific code snippet — such as naming conventions, error handling, optimization tips, or design patterns.
* **Language-specific advice**\
  If you’re working in a particular language (e.g., JavaScript, Python, Java), you can ask for language-specific guidance related to the comment.
* **Request for more context**\
  If the suggestion feels too "short" or "surface level," you can ask the AI to explain more about the broader coding or architectural concept behind its feedback.
* **Security and safety questions**\
  If a suggestion touches on security (like input validation, authentication, or encryption), you can ask for further security-related advice.
* **Testing and validation**\
  Ask the AI if it recommends writing any tests based on its code suggestions and what those tests might look like.

{% hint style="info" %}
**Tip:** Feel free to ask your question in your preferred language! Bito supports over 20 languages, including English, Hindi, Chinese, and Spanish.
{% endhint %}

### What you cannot ask about

The AI can only answer questions related to its **own code review comments**.

* **You cannot** ask general questions about the repository or unrelated topics.
* **You cannot** start a new thread independently — your question must be a reply to a comment made by Bito’s AI Code Review Agent.

If your comment is not linked to a Bito review comment, the AI will **not respond**.


# Implementing custom code review rules

Customize Bito’s AI Code Review Agent to enforce your coding practices.

Bito’s [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) offers a flexible solution for teams looking to enforce custom code review rules, standards, and guidelines tailored to their unique development practices. Whether your team follows specific coding conventions or industry best practices, you can customize the Agent to suite your needs.

We support three ways to customize AI Code Review Agent’s suggestions:&#x20;

1. [**Provide feedback on Bito-reported issues in pull requests**](#id-1-provide-feedback-on-bito-reported-issues), and the AI Code Review Agent automatically adapts by creating code review rules to prevent similar suggestions in the future.
2. [**Create custom code review guidelines via the dashboard**](#id-2-create-custom-code-review-guidelines). Define rules through the [**Custom Guidelines**](https://alpha.bito.ai/home/ai-agents/custom-guidelines) dashboard in Bito Cloud and apply them to agent instances in your workspace.
3. [**Use project-specific guideline files**](#id-3-use-project-specific-guideline-files). Add guideline files (like `.cursor/rules/*.mdc`, `.windsurf/rules/*.md`, `CLAUDE.md`, `GEMINI.md`, or `AGENTS.md`) to your repository, and the AI Code Review Agent automatically uses them during pull request reviews to provide feedback aligned with your project's standards.

## 1- Provide feedback on Bito-reported issues

AI Code Review Agent refines its suggestions based on your feedback. When you **provide negative feedback on Bito-reported issues in pull requests**, the Agent automatically adapts by creating **custom code review rules** to prevent similar suggestions in the future.

Depending on your Git platform, you can provide negative feedback in the following ways:

* **GitHub:** Select the checkbox given in feedback question at the end of each Bito suggestion or leave a negative comment explaining the issue with the suggestion.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FREsLjCbSETT4ng9V2urf%2Fscrnli_uijoVDl73Faal3.png?alt=media&#x26;token=b3f6ab0e-d06f-435c-9411-2784fe3b4eb8" alt=""><figcaption></figcaption></figure>

* **GitLab:** React with negative emojis (e.g., thumbs down) or leave a negative comment explaining the issue with the suggestion.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FIwUQHSeKUQoOMG2Hkuc5%2Fscrnli_T3dqxb73IGQCQX.png?alt=media&#x26;token=55faaf4d-8257-45c5-9a9e-a58598d438a4" alt=""><figcaption></figcaption></figure>

* **Bitbucket:** Provide manual review feedback by leaving a negative comment explaining the issue with the suggestion.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRagYwO9GOvrNWOkcvAAY%2Fscrnli_1JWWOjCcvIVHRc.png?alt=media&#x26;token=83cd24a6-32eb-4b83-8b6e-3fcc704f0c86" alt="" width="563"><figcaption></figcaption></figure>

The **custom code review rules** are displayed on the [**Learned Rules**](https://alpha.bito.ai/home/ai-agents/review-rules) dashboard in Bito Cloud.

These rules are applied at the repository level for the specific programming language.

By default, newly generated custom code review rules are disabled. Once negative feedback for a specific rule reaches a threshold of 3, the rule is automatically enabled. You can also manually enable or disable these rules at any time using the toggle button in the **Status** column.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5nhsxVcDUiGQB7BG2ubh%2Fscrnli_RSAeHezIwIR9Ja.png?alt=media&#x26;token=c026270e-d340-4feb-b648-7fed0e090aa8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Providing a positive reaction emoji or comment has no effect and will not generate a new code review rule.
{% endhint %}

After you provide negative feedback, Bito generates a new code review rule in your workspace. The next time the AI Code Review Agent reviews your pull requests, it will automatically filter out the unwanted suggestions.

## 2- **Create custom code review guidelines**

We understand that different development teams have unique needs. To accommodate these needs, we offer the ability to implement **custom code review guidelines** in Bito’s [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git).

Once you add guidelines, the agent will follow them when reviewing pull requests. You can manage guidelines (create, apply, and edit) entirely in the dashboard.

By enabling custom code review guidelines, Bito helps your team maintain consistency and improve code quality.

{% hint style="info" %}
**Note:** Custom review guidelines are available only on the [**Enterprise Plan**](https://bito.ai/pricing/). Enabling them also upgrades your workspace to the **Enterprise Plan**.
\
[**Visit pricing page**](https://bito.ai/pricing/)
{% endhint %}

### How to add a guideline

#### Step 1: Open the **Custom Guidelines** tab

* Sign in to [Bito Cloud](https://alpha.bito.ai/).
* Click [Custom Guidelines](https://alpha.bito.ai/home/ai-agents/custom-guidelines) in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FWyaHHs2jeqqtciaNwnlf%2Fscrnli_89a02mkxIZwF1j.png?alt=media&#x26;token=2b3ecd82-91b4-44ac-874a-be700e4c5a61" alt=""><figcaption></figcaption></figure>

#### Step 2: Fill the form

**A. Manual setup**

1. Click **Add guidelines** button from the top right.
2. Fill out:
   * **Guideline name**
   * **Language** (select a specific programming language or select **General** if the guideline applies to all languages)
   * **Custom Guidelines and Rules** (enter your guidelines here)
3. Click **Create guideline**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fkf8i8x3CAOFr0DDxkoLY%2Fscrnli_pL9L6X0q4ZzoQu.png?alt=media&#x26;token=e6542c5b-c121-422e-b9a5-6c2fd1ecbb35" alt="" width="563"><figcaption></figcaption></figure>

**B. Use a Template**

1. Click **Add guidelines** button from the top right.
2. Choose a template from the **Use template** dropdown menu.
3. Review/edit fields as needed.
4. Click **Create guideline**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FuXpSbSVzVbvHpME4HQJT%2Fscrnli_VbfcVt9RI01jRh.png?alt=media&#x26;token=a2997a4e-22d7-4c16-9c37-54548aff0416" alt="" width="563"><figcaption></figcaption></figure>

#### Step 3: Apply to an Agent

* After creating a guideline, you’ll see an **Apply review guideline** dropdown.
* Select the **Agent instance**, then click **Manage review guidelines** to open its settings.

{% hint style="info" %}
**To apply the guideline later:** go to [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent), find the Agent instance, click **Settings**, and manage guidelines there.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FikJjSQFsqVVgbk1X4lrF%2Fscrnli_Hrlv93i7v03AvS.png?alt=media&#x26;token=48612ba8-2db3-485e-ba91-7b52182746fb" alt="" width="563"><figcaption></figcaption></figure>

#### Step 4: Save configuration

On the Agent settings page, hit **Save** (top-right) to apply guideline changes.

{% hint style="info" %}
**Note:** Visit the [**Custom Guidelines**](https://alpha.bito.ai/home/ai-agents/custom-guidelines) tab to edit or delete any guideline.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fnn3bFOYEfxzxUJxoDwRA%2Fscrnli_K7jwJZpHs15W6R.png?alt=media&#x26;token=ec0ade53-1f64-4128-8008-263a7e765479" alt=""><figcaption></figcaption></figure>

### Managing review guidelines from agent settings

Efficiently control which custom guidelines apply to your AI Code Review Agent through the Agent settings interface.

1. Go to [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard from the Bito Cloud sidebar.
2. Click **Settings** next to the target agent instance.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNpRzcdMJCARZJGr6zsfu%2Fscrnli_7EzY56dyc0u017.png?alt=media&#x26;token=3a96a9b3-695f-4662-8e2e-dce3731020c9" alt=""><figcaption></figcaption></figure>

3. Navigate to the **Custom Guidelines** section. Here you can either create a new guideline or select from existing guidelines.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjMyWG2I1k48LEV9gjqjr%2Fscrnli_oktJf4u3e0VkU0.png?alt=media&#x26;token=ccb1a18f-1d77-463c-8996-a6e1bb611f9d" alt=""><figcaption></figcaption></figure>

3. **Create a new guideline**
   * If you click **Create a new guideline** button, you will see the same form as mentioned earlier where you can enter the details to create a review guideline.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvTHf5T3XDheW0tEU8iM4%2Fscrnli_IOT11izz4107ka.png?alt=media&#x26;token=19f2da6f-f7e5-4fd9-a274-bf7ee6d1671d" alt=""><figcaption></figcaption></figure>

4. **Or select an existing guideline**
   * If you click **Select from existing guidelines** button, you will get a popup screen from where you can select from a list review guidelines you already created. Use checkboxes to enable or disable each guideline for the selected agent and then click **Add selected**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FpSCt7YJ81pd4W7n4H5Od%2Fscrnli_3JcRnxBHQ135wD.png?alt=media&#x26;token=aa2a8893-4e2f-44ff-9a66-5f960e8ec202" alt=""><figcaption></figcaption></figure>

5. Once you’ve applied or adjusted guidelines, click the **Save** button in the top-right corner to confirm changes.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ftm0jWnSPBLc49zA8FhGL%2Fscrnli_K7jwJZpHs15W6R.png?alt=media&#x26;token=4c5a3503-71a0-48ab-9bad-f805f39bd43a" alt=""><figcaption></figcaption></figure>

### FAQs

#### What types of custom code review guidelines can be implemented?

You can implement a wide range of custom code review guidelines, including:&#x20;

* Style and formatting guidelines&#x20;
* Security best practices&#x20;
* Performance optimization checks&#x20;
* Code complexity and maintainability standards
* etc.

#### Is "custom code review guidelines" feature available in Team Plan?

No, this feature is available exclusively on the [**Enterprise Plan**](https://bito.ai/pricing/). Enabling the **"custom code review guidelines"** feature also upgrades your workspace to the **Enterprise Plan**.

For more details on **Enterprise Plan**, visit our [**Pricing Page**](https://bito.ai/pricing/).

## 3- Use project-specific guideline files

The AI Code Review Agent can read guideline files directly from your repository and use them during code reviews. These are the same guideline files that AI coding assistants (like Cursor, Windsurf, and Claude Code) use to help developers write code.

By adding these files to your repository, the agent automatically follows your project's specific coding standards, architecture patterns, and best practices when reviewing pull requests.

### Supported guideline files

The AI Code Review Agent currently supports analyzing the following guideline files that are commonly used by different AI coding agents:

CRA currently supports analyzing the following guideline files that are commonly used by different AI coding agents:

| `.cursor/rules/*.mdc`  | Cursor IDE               |
| ---------------------- | ------------------------ |
| `.windsurf/rules/*.md` | Windsurf IDE             |
| `CLAUDE.md`            | Claude Code              |
| `GEMINI.md`            | Gemini CLI               |
| `AGENTS.md`            | OpenAI CodeX, Cursor IDE |

### How to organize your guideline files

**Multiple files in one directory**

You can split your guidelines across multiple files:

```
.cursor/rules/project-overview.mdc
.cursor/rules/architecture-principles.mdc
.cursor/rules/security-standards.mdc
```

For Windsurf, use the `.md` extension:

```
.windsurf/rules/coding-standards.md
.windsurf/rules/api-patterns.md
```

**Module-specific guidelines:**

Place guideline files in subdirectories to create rules for specific parts of your codebase:

```
.cursor/rules/global-standards.mdc
providers/.cursor/rules/provider-implementation.mdc
auth/.cursor/rules/authentication-rules.mdc
```

The agent finds all relevant guideline files based on which files changed in your pull request.

{% hint style="info" %}
**Note:** Rule precedence (where subdirectory rules override parent-level rules) will be added in a future release. Currently, the agent considers all applicable guideline files equally.
{% endhint %}

### How citations work

Every relevant Bito comment includes a **Citations** section that links to the specific guideline that triggered the comment. The link takes you directly to the relevant line in your guideline file, making it easy to verify the feedback and understand why it was given.

### Example scenario

Let's say you're building an application that integrates multiple LLM providers. Your guideline file specifies:

* All providers must extend the `BaseLLMProvider` class
* All providers must implement standard methods like `generateResponse()` and `streamResponse()`
* New providers must be registered in the `config/providers.json` file

When someone submits a pull request to add a new provider, the agent can catch issues like:

* The new provider doesn't extend the base class
* Required methods are missing
* The provider wasn't added to the configuration file

Each comment links back to the specific guideline, so the developer knows exactly what needs to be fixed.

### Sample guideline file

Here's an example `AGENT.md` file to help you get started:

{% code expandable="true" %}

````markdown
# LLM Proxy Architecture & Design Document

## Document Overview

### Purpose
This document serves as a coding guideline and technical reference for AI agents working with this codebase. It provides comprehensive information about the current architecture, design patterns, implementation details, and the rationale behind design decisions. AI agents should use this document to understand the existing code structure, maintain consistency when making modifications, and follow established patterns when extending functionality.

### What This Document Covers
- **System Architecture**: High-level overview of components and their interactions
- **Design Patterns**: Detailed explanation of the Factory Pattern implementation
- **Component Design**: In-depth analysis of each system component
- **Data Flow**: Request/response lifecycle through the system
- **Design Decisions**: Rationale behind current architectural choices
- **Implementation Details**: Code structure, conventions, and patterns in use

---

## Table of Contents
1. [System Architecture](#system-architecture)
2. [Design Patterns](#design-patterns)
3. [Component Design](#component-design)
4. [Data Flow](#data-flow)
5. [Design Decisions](#design-decisions)
6. [Error Handling Strategy](#error-handling-strategy)
7. [Security Considerations](#security-considerations)
8. [Coding Conventions](#coding-conventions)

---

## System Architecture

### High-Level Overview

The LLM Proxy application follows a layered architecture with clear separation between the presentation layer (FastAPI), business logic layer (Provider implementations), and integration layer (external LLM APIs).

```
┌─────────────────────────────────────────────┐
│           FastAPI Application               │
│         (Presentation Layer)                │
│   - Request validation (Pydantic)           │
│   - Route handling (/chat endpoint)         │
│   - Response formatting                     │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│          Provider Factory                   │
│        (Abstraction Layer)                  │
│   - Provider selection logic                │
│   - Instance creation                       │
└────────────────┬────────────────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
┌──────────────┐   ┌──────────────┐
│   OpenAI     │   │  Anthropic   │
│   Provider   │   │   Provider   │
│              │   │              │
│ (Concrete    │   │ (Concrete    │
│  Impl.)      │   │  Impl.)      │
└──────┬───────┘   └──────┬───────┘
       │                  │
       ▼                  ▼
┌──────────────┐   ┌──────────────┐
│  OpenAI API  │   │ Anthropic API│
└──────────────┘   └──────────────┘
```

### Component Layers

1. **Presentation Layer** (`main.py`)
   - Handles HTTP requests/responses
   - Validates input using Pydantic models
   - Manages API endpoints

2. **Abstraction Layer** (`providers/factory.py`)
   - Implements Factory Pattern
   - Routes requests to appropriate providers
   - Decouples client code from concrete implementations

3. **Business Logic Layer** (`providers/*.py`)
   - Abstract base class defines contract
   - Concrete providers implement LLM-specific logic
   - Handles API communication and response parsing

4. **Integration Layer**
   - External API calls via httpx
   - Authentication management
   - Network error handling

---

## Design Patterns

### Factory Design Pattern

The application implements the **Factory Design Pattern** to create provider instances without exposing creation logic to the client.

#### Pattern Components

1. **Abstract Product** (`LLMProvider`)
```python
class LLMProvider(ABC):
    def __init__(self, model: str):
        self.model = model
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass
```

**Purpose**: Defines the contract that all concrete providers must implement.

2. **Concrete Products** (`OpenAIProvider`, `AnthropicProvider`)
```python
class OpenAIProvider(LLMProvider):
    def generate_response(self, prompt: str) -> str:
        # OpenAI-specific implementation
        pass
```

**Purpose**: Implement provider-specific logic while adhering to the base contract.

3. **Factory** (`ProviderFactory`)
```python
class ProviderFactory:
    @staticmethod
    def get_provider(provider_name: str, model: str) -> LLMProvider:
        providers = {
            "openai": OpenAIProvider,
            "anthropic": AnthropicProvider
        }
        return providers[provider_name.lower()](model)
```

**Purpose**: Encapsulates provider instantiation logic.

#### Benefits of This Pattern

- **Loose Coupling**: Client code depends on abstractions, not concrete classes
- **Open/Closed Principle**: Open for extension (new providers), closed for modification
- **Single Responsibility**: Each provider handles only its specific implementation
- **Testability**: Easy to mock providers for testing
- **Scalability**: Adding new providers requires minimal changes

---

## Component Design

### 1. Base Provider (`providers/base.py`)

**Responsibility**: Define the contract for all LLM providers

**Key Design Decisions**:
- Uses ABC (Abstract Base Class) to enforce implementation
- Stores model name as instance variable for reuse
- Single abstract method keeps interface simple

**Design Rationale**:
- Python's ABC ensures compile-time checking of implementations
- Simple interface reduces cognitive load for implementers
- Storing model allows for provider-specific model validation in future

### 2. OpenAI Provider (`providers/openai_provider.py`)

**Responsibility**: Implement OpenAI Chat Completions API integration

**Key Features**:
- Environment-based API key management
- Message format conversion (user prompt → OpenAI format)
- Response parsing (extract content from choices)
- Timeout handling (30 seconds)

**API Contract**:
```
POST https://api.openai.com/v1/chat/completions
Headers: Authorization: Bearer <key>
Body: {
  "model": "gpt-4",
  "messages": [{"role": "user", "content": "prompt"}]
}
```

**Error Handling**:
- Validates API key presence on initialization
- Catches HTTP errors and wraps with descriptive messages
- Re-raises exceptions for upstream handling

### 3. Anthropic Provider (`providers/anthropic_provider.py`)

**Responsibility**: Implement Anthropic Messages API integration

**Key Features**:
- Custom header format (x-api-key, anthropic-version)
- Max tokens configuration (1024)
- Content array response parsing

**API Contract**:
```
POST https://api.anthropic.com/v1/messages
Headers: 
  x-api-key: <key>
  anthropic-version: 2023-06-01
Body: {
  "model": "claude-3-sonnet",
  "max_tokens": 1024,
  "messages": [{"role": "user", "content": "prompt"}]
}
```

**Design Choices**:
- Hard-coded max_tokens provides consistent behavior
- Version header ensures API stability
- Array access for content assumes single response

### 4. Provider Factory (`providers/factory.py`)

**Responsibility**: Create provider instances based on string identifiers

**Implementation Strategy**:
- Dictionary-based mapping for O(1) lookup
- Case-insensitive provider names
- Descriptive error messages for invalid providers

**Extensibility**:
```python
# Adding new provider:
providers = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "deepseek": DeepseekProvider,  # Just add here
}
```

### 5. FastAPI Application (`main.py`)

**Responsibility**: HTTP interface and request orchestration

**Key Components**:

1. **Request Model**:
```python
class ChatRequest(BaseModel):
    provider: str
    model: str
    prompt: str
```
- Leverages Pydantic for automatic validation
- Clear field names match user expectations

2. **Response Model**:
```python
class ChatResponse(BaseModel):
    provider: str
    model: str
    response: str
```
- Echoes input parameters for traceability
- Returns plain text response

3. **Endpoint Handler**:
```python
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    provider = ProviderFactory.get_provider(request.provider, request.model)
    response_text = provider.generate_response(request.prompt)
    return ChatResponse(...)
```

**Error Mapping**:
- `ValueError` (invalid provider) → HTTP 400
- Generic `Exception` (API errors) → HTTP 500

---

## Data Flow

### Request Lifecycle

```
1. Client sends POST /chat
   ↓
2. FastAPI receives request
   ↓
3. Pydantic validates request body
   ↓
4. ProviderFactory.get_provider() called
   ↓
5. Factory returns concrete provider instance
   ↓
6. provider.generate_response() called
   ↓
7. Provider makes HTTP call to LLM API
   ↓
8. Provider parses response
   ↓
9. Response wrapped in ChatResponse model
   ↓
10. JSON response sent to client
```

### Detailed Flow Example (OpenAI)

```python
# Client Request
POST /chat
{
  "provider": "openai",
  "model": "gpt-4",
  "prompt": "Tell me a joke"
}

# Internal Processing
1. Pydantic validates: ChatRequest object created
2. Factory called: ProviderFactory.get_provider("openai", "gpt-4")
3. OpenAIProvider instantiated with model="gpt-4"
4. generate_response("Tell me a joke") called
5. HTTP POST to OpenAI API:
   {
     "model": "gpt-4",
     "messages": [{"role": "user", "content": "Tell me a joke"}]
   }
6. OpenAI responds with completion
7. Extract: data["choices"][0]["message"]["content"]
8. Return text to endpoint
9. Wrap in ChatResponse

# Client Response
{
  "provider": "openai",
  "model": "gpt-4",
  "response": "Why did the chicken cross the road?..."
}
```

---

## Design Decisions

### 1. Why Factory Pattern?

**Decision**: Use Factory Pattern instead of simple if/else logic

**Rationale**:
- **Scalability**: Adding providers doesn't require modifying existing code
- **Testability**: Easy to mock factory for unit tests
- **Maintainability**: Provider logic isolated in separate classes
- **Professional Standard**: Industry-recognized pattern for this use case

**Alternative Considered**: Direct instantiation with if/else
```python
# Rejected approach
if provider == "openai":
    result = OpenAIProvider(model).generate_response(prompt)
elif provider == "anthropic":
    result = AnthropicProvider(model).generate_response(prompt)
```
**Why Rejected**: Violates Open/Closed Principle, harder to extend

### 2. Why httpx Over Official SDKs?

**Decision**: Use httpx for HTTP calls instead of official provider SDKs

**Rationale**:
- **Minimal Dependencies**: Keeps requirements.txt small
- **Unified Interface**: Single HTTP client for all providers
- **Transparency**: Direct API calls are easier to debug
- **Control**: Full control over request/response handling

**Trade-offs**:
- Less abstraction (must handle response parsing)
- No built-in retry logic
- Manual API version management

### 3. Synchronous vs Asynchronous

**Decision**: Use synchronous HTTP calls with httpx.Client

**Rationale**:
- **Simplicity**: Easier to understand and debug
- **Current Scale**: Single request doesn't benefit from async
- **API Constraints**: LLM APIs are inherently blocking

**Future Consideration**: Switch to async if supporting streaming responses

### 4. Error Handling Strategy

**Decision**: Simple try/except with HTTP status code mapping

**Rationale**:
- **Simplicity**: Requirements specified basic error handling
- **Client Clarity**: HTTP status codes are standard
- **Debugging**: Error messages preserved in exceptions

**Not Included** (but recommended for production):
- Structured logging
- Retry logic
- Rate limiting
- Circuit breakers

### 5. Environment Variables for API Keys

**Decision**: Use environment variables instead of configuration files

**Rationale**:
- **Security**: Prevents accidental commit of credentials
- **12-Factor App**: Follows best practices for configuration
- **Flexibility**: Easy to change without code modification
- **Cloud-Ready**: Works seamlessly with container orchestration


---

## Error Handling Strategy

### Current Implementation

```python
try:
    provider = ProviderFactory.get_provider(request.provider, request.model)
    response_text = provider.generate_response(request.prompt)
    return ChatResponse(...)
except ValueError as e:
    # Invalid provider name
    raise HTTPException(status_code=400, detail=str(e))
except Exception as e:
    # API errors, network issues, etc.
    raise HTTPException(status_code=500, detail=str(e))
```

### Error Categories

1. **Client Errors (400)**:
   - Invalid provider name
   - Unsupported model
   - Malformed request

2. **Server Errors (500)**:
   - Missing API keys
   - Network timeouts
   - API errors (rate limits, service unavailable)
   - Response parsing failures


---

## Security Considerations

### Current Implementation

1. **API Key Management**:
   - Stored in environment variables
   - Never logged or returned in responses
   - Validated on provider initialization

2. **Request Validation**:
   - Pydantic models enforce type safety
   - No SQL injection risk (no database)
   - No command injection (no shell execution)

### Current Limitations

1. **No Rate Limiting**: The application does not implement rate limiting
2. **No Authentication**: Endpoints are publicly accessible
3. **No Input Sanitization**: Prompt length and content are not validated beyond Pydantic type checking
4. **No Retry Logic**: Failed API calls are not automatically retried

---

## Coding Conventions

### File Organization

**Current Structure**:
```
llm-proxy/
├── main.py                      # FastAPI application entry point
├── providers/                   # Provider package
│   ├── __init__.py             # Package exports
│   ├── base.py                 # Abstract base class
│   ├── openai_provider.py      # OpenAI implementation
│   ├── anthropic_provider.py   # Anthropic implementation
│   └── factory.py              # Factory implementation
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variable template
└── README.md                   # User documentation
```

### Naming Conventions

1. **Classes**: PascalCase (e.g., `LLMProvider`, `OpenAIProvider`)
2. **Functions/Methods**: snake_case (e.g., `generate_response`, `get_provider`)
3. **Constants**: UPPER_SNAKE_CASE (e.g., `OPENAI_API_KEY`)
4. **Files**: snake_case (e.g., `openai_provider.py`)

### Code Patterns

1. **Provider Implementation**:
   - Inherit from `LLMProvider`
   - Validate API key in `__init__`
   - Implement `generate_response(prompt: str) -> str`
   - Use httpx.Client with 30-second timeout
   - Wrap errors with descriptive messages

2. **Error Handling**:
   - Use `try/except` blocks in provider implementations
   - Raise `ValueError` for missing API keys
   - Raise generic `Exception` with descriptive messages for API errors
   - Let FastAPI endpoint handle HTTP status code mapping

3. **Environment Variables**:
   - Load with `os.getenv()`
   - Validate presence in provider `__init__`
   - Use pattern: `{PROVIDER}_API_KEY`

4. **Type Hints**:
   - All methods should include type hints
   - Use Pydantic models for request/response validation
   - Return type explicitly stated

### Documentation Standards

1. **Docstrings**: All classes and methods include docstrings
2. **Comments**: Inline comments explain non-obvious logic
3. **README**: User-facing documentation with examples

### Dependencies

**Current Dependencies**:
- `fastapi==0.109.0`: Web framework
- `uvicorn[standard]==0.27.0`: ASGI server
- `pydantic==2.5.3`: Data validation
- `httpx==0.26.0`: HTTP client
- `python-dotenv==1.0.0`: Environment variable management

**Rationale**: Minimal, well-maintained dependencies that serve specific purposes.

---

## Summary

This document captures the current state of the LLM Proxy application. When working with this codebase, AI agents should:

1. **Follow the Factory Pattern**: All new providers must inherit from `LLMProvider` and be registered in `ProviderFactory`
2. **Maintain Consistency**: Use the same error handling, timeout values, and code structure as existing providers
3. **Respect Abstractions**: Keep provider-specific logic within provider classes
4. **Update Documentation**: Any changes to architecture should be reflected in this document
5. **Preserve Simplicity**: The design prioritizes simplicity and clarity over advanced features

The architecture demonstrates clean separation of concerns through the Factory Design Pattern, making the codebase maintainable and understandable for both human developers and AI agents.

````

{% endcode %}


# Excluding files, folders, or branches with filters

Customize which files, folders, and Git branches are reviewed when the Agent triggers automatically on pull requests.

The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) offers powerful filters to exclude specific files and folders from code reviews and gives you precise control over which Git branches are included in automated reviews.

These filters can be configured at the Agent instance level, overriding the default behavior.

## Exclude Files and Folders filter

A list of files/folders that the AI Code Review Agent will not review if they are present in the diff. You can specify the files/folders to exclude from the review by name or glob/regex pattern. The Agent will automatically skip any files or folders that match the exclusion list.

This filter applies to both manual reviews initiated through the `/review` command and automated reviews triggered via webhook.

By default, these files are excluded: `*.xml`, `*.json`, `*.properties`, `.gitignore`, `*.yml`, `*.md`

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8qrlYfC2AhUXtfITPKks%2Fscrnli_67LP18Ctwr8Zli.png?alt=media&#x26;token=91709f9b-b295-412e-8595-af17eac6cf53" alt=""><figcaption></figcaption></figure>

### Examples

{% hint style="info" %}
**Note:**

* Patterns are case sensitive.
* Don’t use double quotes, single quotes or comma in the pattern.
* Users can pass both types of patterns - Unix files system based glob pattern or regex.
  {% endhint %}

| Exclusion Rule for Files & Folders                                                                      | Applicable Pattern                       | Matched Examples                                                                                                                                 | Not Matched Examples                                                          |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Exclude all properties files in all folders and subfolders                                              | `*.properties`                           | `resource/config.properties`, `resource/server/server.properties`                                                                                | `resource/config.yaml`, `resource/config.json`                                |
| Exclude all files, folders and subfolders in folder starting with `resources`                           | `resources/`                             | `resources/application.properties`, `resources/config/config.yaml`                                                                               | `app/resources/file.txt`, `config/resources/service.properties`               |
| Exclude all files, folders and subfolders in folder `src/com/resources`                                 | `src/com/resources/`                     | `resources/application.properties`, `resources/config/config.yaml`                                                                               | `app/resources/file.txt`, `config/resources/service.properties`               |
| Exclude all files, folders and subfolders in subfolder `resource` and in parent folder `src`            | `src/*/resource/*`                       | <p><code>src/com/resource/main.html</code>,</p><p><code>src/com/resource/script/file.css</code>, <code>src/com/resource/app/script.js</code></p> | `src/resource/file.txt`, `src/com/config/file.txt`, `app/com/config/file.txt` |
| Exclude non-css files from folder `src/com/resource/` and subfolders                                    | `^src\/com\/resource\\/(?!.*\\.css$).*$` | <p><code>src/com/resource/main.html, src/com/resource/app/script.js</code>, </p><p><code>src/com/config/file.txt</code></p>                      | `src/com/resource/script/file.css`                                            |
| Exclude specific file `controller/webhook_controller.go`                                                | `controller/webhook_controller.go`       | `controller/webhook_controller.go`                                                                                                               | `controller/controller.go`, `controller/webhook_service.go`                   |
| Exclude non-css files from folder starting with `config` and its subfolders                             | `^config\\/(?!.*\\.css$).*$`             | `config/server.yml`, `config/util/conf.properties`                                                                                               | `config/profile.css`, `config/styles/main.css`                                |
| Exclude all files & folders                                                                             | `*`                                      | `resource/file.txt`, `config/file.properties`, `app/folder/`                                                                                     | `-`                                                                           |
| Exclude all files & folders starting with name `bito` in `module` folder                                | `module/bito*`                           | `module/bito123`, `module/bitofile.js`, `module/bito/file.js`                                                                                    | `module/filebito.js`, `module/file2.txt`, `module/util/file.txt`              |
| Exclude single-character folder names                                                                   | `*/?/*`                                  | `src/a/file.txt`, `app/b/folder/file.yaml`                                                                                                       | `folder/file.txt`, `ab/folder/file.txt`                                       |
| Exclude all folders, subfolders and files in those folders except folder starting with `service` folder | `^(?!service\\/).*$`                     | `config/file.txt`, `resources/file.yaml`                                                                                                         | `service/file.txt`, `service/config/file.yaml`                                |
| Exclude all files in all folders except `.py`, `.go`, and `.java` files                                 | `^(?!.*\\.(py\|go\|java)$).*$`           | `config/file.txt`, `app/main.js`                                                                                                                 | `main.py`, `module/service.go`, `test/Example.java`                           |
| Exclude non-css files from folder `src/com/config` and its subfolders                                   | `^config\\/(?!.*\\.css$).*$`             | `config/server.yml`, `config/util/conf.properties`                                                                                               | `config/profile.css`, `config/styles/main.css`                                |

## Include Source/Target Branches filter

This filter defines which pull requests trigger automated reviews based on their source or target branch, allowing you to focus on critical code and avoid unnecessary reviews or AI usage.

By default, pull requests merging into the repository’s default branch are subject to review. To extend review coverage, additional branches may be specified using explicit branch names or valid glob/regex patterns. When the source or target branch of a pull request matches one of the patterns on your inclusion list, Bito’s AI Code Review Agent will trigger an automated review.

This filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F00UMeHuAITRMKGaBoZjO%2Fscrnli_P386e3Jr001VDd.png?alt=media&#x26;token=826ced85-028e-4317-852e-05ac8185a80b" alt=""><figcaption></figcaption></figure>

**Watch video tutorial:**

{% embed url="<https://youtu.be/31h8V-ip0J8>" %}

### Examples

{% hint style="info" %}
**Note:**

* Patterns are case sensitive.
* Don’t use double quotes, single quotes or comma in the pattern.
* Users can pass both types of patterns - Unix files system based glob pattern or regex.
  {% endhint %}

| Inclusion Rules for Branch                                                                                         | Pattern                                               | Matched Examples                                | Not Matched Examples                                |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------- |
| Include any branch that starts with name `BITO-`                                                                   | `BITO-*`                                              | `BITO-feature`, `BITO-123`                      | `feature-BITO`, `development`                       |
| Include any branch that does not start with `BITO-`                                                                | `^(?!BITO-).*`                                        | `feature-123`, `release-v1.0`                   | `BITO-feature`, `BITO-123`                          |
| Include any branch which is not `BITO`                                                                             | `^(?!BITO$).*`                                        | `feature-BITO`, `development`                   | `BITO`                                              |
| Include branches like `release/v1.0` and `release/v1.0.1`                                                          | `release/v\\d+\\.\\d+(\\.\\d+)?`                      | `release/v1.0`, `release/v1.0.1`                | `release/v1`, `release/v1.0.x`                      |
| Include any branch ending with `-test`                                                                             | `*-test`                                              | `feature-test`, `release-test`                  | `test-feature`, `release-testing`                   |
| Include the branch that has keyword `main`                                                                         | `main`                                                | `main`, `main-feature`, `mainline`              | `master`, `development`                             |
| Include the branch named `main`                                                                                    | `^main$`                                              | `main`                                          | `main-feature`, `mainline`, `master`, `development` |
| Include any branch name that does not start with `feature-` or `release-`                                          | `^(?!release-\|feature-).*$`                          | `hotfix-123`, `development`                     | `feature-123`, `release-v1.0`                       |
| Include branches with names containing digits                                                                      | `.*\\d+.*`                                            | `feature-123`, `release-v1.0`                   | `feature-abc`, `main`                               |
| Include branches with names ending with `test` or `testing`                                                        | `.*(test\|testing)$`                                  | `feature-test`, `bugfix-testing`                | `testing-feature`, `test-branch`                    |
| Include branches with names containing a specific substring `test`                                                 | `*test*`                                              | `feature-test`, `test-branch`, `testing`        | `feature`, `release`                                |
| Include branches with names containing exactly three characters                                                    | `^.{3}$`                                              | `abc`, `123`                                    | `abcd`, `ab`                                        |
| Include branch names starting with `release`, `hotfix`, or `development` but not starting with `Bito` or `feature` | `^(?!Bito\|feature)(release\|hotfix\|development).*$` | `release-v1.0`, `hotfix-123`, `development-xyz` | `Bito-release`, `feature-hotfix`, `main-release`    |
| Include all branches where name do not contains version like `1.0`, `1.0.1`, etc.                                  | `^(?!.\\b\\d+\\.\\d+(\\.\\d+)?\\b).*`                 | `feature-xyz`, `main`                           | `release-v1.0`, `hotfix-1.0.1`                      |
| Include all branches which are not alphanumeric                                                                    | `^.[^a-zA-Z0-9].$`                                    | `feature-!abc`, `release-@123`                  | `feature-123`, `release-v1.0`                       |
| Include all branches which contains space                                                                          | `.*\\s.*`                                             | `feature 123`, `release v1.0`                   | `feature-123`, `release-v1.0`                       |

## Draft pull requests filter

A binary setting that enables/disables automated review of pull requests (PR) based on the draft status. Enter `True` to disable automated review for draft pull requests, or `False` to enable it.

The default value is `True` which skips automated review of draft PR.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Feq4VAtW5pzAXmMb56Tkh%2Fscrnli_6lY6vx73F6U1U6.png?alt=media&#x26;token=34238de9-542e-490f-a9df-4d2daf762e21" alt=""><figcaption></figcaption></figure>

## How to configure the filters?

### Bito Cloud (Bito-hosted Agent)

You can configure filters using the Agent configuration page. For detailed instructions, please refer to the [**Install/run Using Bito Cloud**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud) documentation page.

### CLI or webhooks service (self-hosted Agent)

You can configure filters using the [**bito-cra.properties file**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file). Check the options `exclude_branches`, `exclude_files`, and `exclude_draft_pr` for more details.

### GitHub Actions (self-hosted Agent)

You can configure filters using the GitHub Actions repository variables: `EXCLUDE_BRANCHES`, `EXCLUDE_FILES`, and `EXCLUDE_DRAFT_PR`. For detailed instructions, please refer to the [**Install/Run via GitHub Actions**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-github-actions) documentation page.


# Code review analytics

Get in-depth insights into your code review process.

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


# Request changes comments

Block merges until code issues are fixed.

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


# Jira integration

Bring Jira issue requirements into every pull request and get validation results back automatically.

{% hint style="info" %}
**Note:** The Jira integration is available only on the [**Enterprise Plan**](https://bito.ai/pricing/).
{% endhint %}

Bito integrates with Jira to automatically validate pull request code changes against linked Jira ticket requirements, helping ensure your implementations align with the specified requirements in those tickets.

## How it works

When you create a pull request, Bito automatically:

1. **Detects Jira ticket references** in your pull request description, title, or branch name
2. **Crawls the linked Jira tickets** to extract requirements from issue descriptions and related Stories/Epics
3. **Analyzes your code changes** against these requirements
4. **Provides structured validation results** directly in your pull request comments

## **Jira integration options in Bito**

Bito supports two ways to connect with Jira, depending on where your Jira instance is hosted:

1. [**Jira Cloud**](#connect-bito-with-jira-cloud-hosted-by-atlassian)**:** for Jira sites hosted by Atlassian (e.g., `https://mycompany.atlassian.net`).
2. [**Jira Data Center**](#connect-bito-with-jira-data-center-hosted-on-your-own-server)**:** for Jira instances hosted on your own company domain or servers (e.g., `https://jira.mycompany.com`).

## Connect Bito with Jira Cloud (hosted by Atlassian)

{% stepper %}
{% step %}

### Connect Bito to Jira

1. Navigate to the [**Manage integrations**](https://alpha.bito.ai/home/cra-integrations) page in your Bito dashboard
2. In the **Available integrations** section, you will see **Jira**. Click **Connect** to proceed.
3. Select the option **Jira Cloud**. You will be redirected to the official Jira website, where you need to grant Bito access to your Atlassian account.
4. Click **Accept** to continue. If the integration is successful, you will be redirected back to Bito.
   {% endstep %}

{% step %}

### Agent-specific settings

After completing the initial setup, you can control Jira integration on a per-agent basis:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page in your Bito dashboard.
2. Find the Agent instance you want to connect with Jira and open its settings.
3. Within the Agent settings screen, click on the **Integrations** tab.
4. Locate the **Functional validation** option and **enable** this setting to activate automatic pull request validation against Jira tickets.
   {% endstep %}
   {% endstepper %}

{% hint style="info" %}
**Note:** The **Functional validation** feature must be enabled in your Bito agent settings for the integration to work.
{% endhint %}

## Connect Bito with Jira Data Center (hosted on your own server)

{% stepper %}
{% step %}

### Connect Bito to Jira

1. Navigate to the [**Manage integrations**](https://alpha.bito.ai/home/cra-integrations) page in your Bito dashboard
2. In the **Available integrations** section, you will see **Jira**. Click **Connect** to proceed.
3. Select the option **Jira Data Center (self-managed)**.
4. Provide connection details:
   * **Domain URL**: Enter the base URL for your Jira instance (e.g. `https://jira.mycompany.com`).
   * **Personal Access Token**: Enter a valid Personal Access Token with admin permissions. Read the [official Jira documentation](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) to learn how to create a Personal Access Token.
5. Click **Connect to Jira**. You will be redirected to your self-hosted Jira website, where you need to grant Bito access to your Jira account.
6. Click **Allow** to continue. If the integration is successful, you will be redirected back to Bito.
   {% endstep %}

{% step %}

### Agent-specific settings

After completing the initial setup, you can control Jira integration on a per-agent basis:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page in your Bito dashboard.
2. Find the Agent instance you want to connect with Jira and open its settings.
3. Within the Agent settings screen, click on the **Integrations** tab.
4. Locate the **Functional validation** option and **enable** this setting to activate automatic pull request validation against Jira tickets.
   {% endstep %}
   {% endstepper %}

## Linking Jira tickets to pull requests

Bito offers multiple ways to link your Jira tickets with pull requests. You can use any of these methods:

#### Method 1: Branch name

Name your source branch using the Jira issue key:

```
feature/QP-123-implement-user-authentication
bugfix/QP-456-fix-login-error
```

#### Method 2: Pull request description

Include the Jira ticket reference in your PR description:

```
This PR implements user authentication as specified in QP-123.

Related tickets: QP-123, QP-124
```

OR

```
This PR implements shopping cart functionality as specified in:
https://your-company.atlassian.net/browse/QP-3
https://your-company.atlassian.net/browse/QP-7
```

#### Method 3: Pull request title

Include the Jira issue key in your PR title:

```
QP-123: Implement user authentication feature
[QP-456] Fix login validation error
```

## Understanding the validation results

When Bito completes its analysis, it adds a **"Functional Validation by Bito"** table to your pull request comments. This table contains four columns:

#### Source

Displays the **Jira issue key** (e.g., "QP-11", "QP-123") that references the specific Jira ticket being validated.

#### Requirement / Code Area

Shows a brief description of the requirement or task that needs to be completed, summarizing what needs to be done according to the Jira ticket.

#### Status

Indicates the completion status of each requirement:

* **Met**: The requirement has been fully implemented in the pull request
* **Missed**: The requirement has not been addressed in the pull request
* **Partial**: The requirement has been partially implemented but still needs additional work

#### Notes

Provides detailed information about the validation status:

* **For "Met" items**: Explains what has been successfully implemented
* **For "Missed" items**: Describes what is missing and needs to be addressed
* **For "Partial" items**: Details what has been completed and what still remains to be done

## Example validation output

Here's what a typical validation table looks like:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZLqYnwgMQ0bSmzdAUbmv%2Fscrnli_KjIe1WJ48Jm3Cf.png?alt=media&#x26;token=932928cb-447a-4cb9-956a-fc246a96c30f" alt=""><figcaption></figcaption></figure>

## Benefits

* **Automated quality assurance**: Ensure code changes meet specified requirements
* **Improved collaboration**: Bridge the gap between project management and development
* **Reduced manual reviews**: Bito AI automatically catches missing implementations during code review
* **Better traceability**: Maintain clear links between requirements and code changes

By leveraging Bito's Jira integration, your development team can maintain higher code quality while ensuring that all requirements are properly addressed in every pull request.

## Best practices

#### For developers

* Always reference Jira tickets in your pull requests using one of the supported methods
* Review the validation table and address any "Missed" or "Partial" items before merging

#### For teams

* Ensure Jira tickets contain clear, detailed requirements
* Use consistent naming conventions for branches and pull request titles
* Enable functional validation for all relevant agents

## Troubleshooting

**Validation table not appearing:**

* Check that your Jira integration is properly configured in the [**Manage integrations**](https://alpha.bito.ai/home/cra-integrations) page
* Verify that **Functional validation** is enabled in your agent settings
* Ensure your pull request contains valid Jira issue key references

**Incorrect validation results:**

* Review your Jira ticket descriptions for clarity and completeness
* Verify that linked Stories/Epics contain relevant requirements
* Check that your code changes are in the expected areas


# Agent settings

Learn how to customize the AI Code Review Agent.

Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) supports different configuration methods depending on the deployment environment:

1. **Bito-hosted** – The agent runs on Bito's infrastructure and is configured through the [Bito web UI](https://alpha.bito.ai/).
2. **Self-hosted** – The agent runs on user-managed infrastructure and is configured by editing the [`bito-cra.properties` file](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file).

The sections below provide configuration guidance for each setup.

## Bito-hosted agent configuration

In Bito-hosted AI Code Review Agent, you can configure the agent through the [Bito web UI](https://alpha.bito.ai/).

To customize an existing agent, open the [**Code Review > Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page and click the **Settings** button next to the Agent instance to be modified.

The agent settings page allows configuration of options such as:

* **Agent name** – Define a unique name for easy identification.
* **Review options** – Choose the review mode (Essential or Comprehensive), set feedback language, and enable features like auto-review, incremental review, summaries, and change walkthroughs.
* **Custom guidelines** – Create and apply custom code review rules tailored to your team’s standards directly from the dashboard.
* **Filters** – Exclude specific files, folders, or branches from review to focus on relevant code.
* **Tools** – Enable additional checks, such as secret scanning and static analysis.
* **Chat** – Configure how the agent responds to follow-up questions in pull request comments and manage automatic replies.

These settings tailor the agent’s behavior to match team workflows and project needs. For detailed guidance, see [Create or customize an Agent instance](https://docs.bito.ai/ai-code-review-agent/install-run-using-bito-cloud/create-or-customize-an-agent-instance).

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="install-run-using-bito-cloud/create-or-customize-an-agent-instance">create-or-customize-an-agent-instance</a></td></tr></tbody></table>

{% embed url="<https://youtu.be/Oj4A8wd1bio>" %}

## Self-hosted agent configuration

In self-hosted deployments, configuration is managed by editing the [`bito-cra.properties` file](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file). This file defines how the agent operates and connects to required services.

Key configuration options include:

* **Mode**
  * `mode = cli`: Processes a single pull request using a manual URL input.
  * `mode = server`: Runs as a webhook service and listens for incoming events from Git platforms.
* **Authentication**
  * `bito_cli.bito.access_key`: Required for authenticating the agent with the Bito platform.
  * `git.provider`, `git.access_token`, etc.: Required for connecting to the appropriate Git provider (e.g., GitHub, GitLab, Bitbucket).
* **General feedback settings**
  * `code_feedback`: Enables or disables general feedback comments in reviews.
* **Analysis tools**
  * `static_analysis`: Enables static code analysis.
  * `dependency_check`: Enables open-source dependency scanning.
  * `dependency_check.snyk_auth_token`: Required when using Snyk for vulnerability detection.
* **Review format and scope**
  * `review_comments`: Defines output style (e.g., single post or inline comments).
  * `review_scope`: Limits the review focus to specific concerns such as security, performance, or style.
* **Filters**
  * `include_source_branches` and `include_target_branches`: Restrict reviews to pull requests that match specified source and target branch patterns.
  * `exclude_files`: Skips selected files based on glob patterns.
  * `exclude_draft_pr`: Skips draft pull requests when enabled (default: `True`).

Each property is documented in detail on the [bito-cra.properties file documentation](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file">agent-configuration-bito-cra.properties-file</a></td></tr></tbody></table>


# Repo level settings

Configure repository-specific Code Review Agent settings using the .bito.yaml file.

Repo-level Agent settings let you control how the [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) behaves for each repository.&#x20;

By placing a **`.bito.yaml`** file in the root of your repository, you can define custom review preferences that apply only to that repository.&#x20;

Bito automatically detects the presence of a `.bito.yaml` file in a repository and applies its configuration to override the global Agent settings defined by admins in the Bito Cloud UI.

This gives developers fine-grained control while admins maintain global oversight and billing management.

## Why use repo-level settings&#x20;

Large organizations often have different review needs across projects.&#x20;

Centralized (agent-level) settings don’t scale well — especially when each repo has its own coding standards, branch structure, or tooling.&#x20;

**Repo-level configuration helps by:**&#x20;

* Enabling custom review behavior per repository.
* Allowing custom guidelines flexibility at the repo level.&#x20;
* Keeping settings version-controlled and transparent.

## How it works&#x20;

1. Add a `.bito.yaml` file to the root of your repository. To get started, [download a sample `.bito.yaml` file](https://github.com/gitbito/repo-level-settings-file).
2. Add the [supported configuration fields](#supported-settings-in-.bito.yaml-file) (key-value pairs) to specify how the Code Review Agent should behave for that repository.
3. When the Code Review Agent runs, Bito automatically detects the file and applies those settings for that repository.

{% hint style="info" %}
**Note:** Repo-level overrides are applied only if your workspace admin has enabled **“Allow config file settings”** in [Agent Settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance). This option is **required** for repo-level overrides to take effect and is **turned on by default**.
{% endhint %}

## Enabling repo-level overrides&#x20;

Admins can manage this from the [Agent Settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) panel.&#x20;

* **Setting name:** Allow config file settings&#x20;
* **Description:** Enabling this allows repositories to override Agent Settings by placing a `.bito.yaml` file in the repo root.

{% hint style="info" %}
**Note:** Only workspace admins can toggle this setting from the Bito dashboard (cannot be changed via `.bito.yaml` file).
{% endhint %}

## Supported settings in `.bito.yaml` file

You can override the following Code Review Agent settings:&#x20;

<table data-header-hidden><thead><tr><th width="257.99993896484375">Setting</th><th>Description</th></tr></thead><tbody><tr><td><strong>suggestion_mode</strong> </td><td><p>Controls how detailed the review comments are.<br><br>Choose between <strong>Essential</strong> and <strong>Comprehensive</strong> review modes:</p><ul><li>In <strong>Essential</strong> mode, only critical issues are posted as inline comments, and other issues appear in the main review summary under "Additional issues".</li><li>In <strong>Comprehensive</strong> mode, Bito also includes minor suggestion and potential nitpicks as inline comments.</li></ul><p><br><strong>Valid values:</strong> <code>essential</code> or <code>comprehensive</code></p></td></tr><tr><td><strong>post_description</strong> </td><td>Automatically create summary of changes and append to your existing pull request summary.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>post_changelist</strong></td><td>Adds a walkthrough section to pull request comments.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>include_source_branches</strong></td><td>Source branches defined using comma-separated GLOB or regex patterns for which Bito automatically reviews pull requests.<br><br><strong>Example:</strong> <code>"feature/*, release/*, main"</code>    </td></tr><tr><td><strong>include_target_branches</strong></td><td>Target branches defined using comma-separated GLOB or regex patterns for which Bito automatically reviews pull requests.<br><br><strong>Example:</strong> <code>"feature/*, release/*, main"</code></td></tr><tr><td><strong>exclude_files</strong></td><td>Comma-separated file path GLOB patterns to exclude from code reviews.<br><br><strong>Example:</strong> <code>"*.md, *.yaml, config/*"</code></td></tr><tr><td><strong>exclude_draft_pr</strong></td><td>Excludes draft pull requests from automatic reviews.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>secret_scanner_feedback</strong></td><td>Enables or disables secret scanning feedback. Bito detects and reports secrets left in code changes.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>linters_feedback</strong></td><td>Run Linting tools during code reviews.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>custom_guidelines</strong></td><td><p>Adds repo-defined coding guidelines, supporting both general and language-specific configurations.<br><br>Provide the <strong>name</strong> and <strong>path</strong> to review guidelines that you want bito to follow. These files must exist in your <strong>source branch</strong> at review time.<br><br>We accept up to 3 general guidelines and 1 language specific guideline per language.<br><br><strong>Example:</strong></p><pre class="language-yaml"><code class="lang-yaml">custom_guidelines:
  general:
    - name: "Global Checks"
      path: "./guidelines/global_checks.txt"
    - name: "Security Rules"
      path: "./guidelines/security.txt"
    - name: "Legacy Style Guide"
      path: "./guidelines/legacy.txt"
    - name: "Performance Checks"
      path: "./guidelines/perf.txt"
    - name: "Code Style"
      path: "./guidelines/style.txt"
  per_language:
    python:
      name: "Python Best Practices"
      path: "./guidelines/py.txt"
    javascript:
      name: "JS Style Guide"
      path: "./guidelines/js.txt"
    typescript:
      name: "TS Checks"
      path: "./guidelines/ts.txt"
    java:
      name: "Java Coding Standards"  
      Path: "./guidelines/java.txt"
</code></pre></td></tr><tr><td><strong>dependency_check.enabled</strong></td><td><p>Run Dependency Check analysis during code reviews.<br></p><p><strong>Valid values:</strong> <code>true</code> or <code>false</code></p></td></tr><tr><td><strong>repo_level_guidelines_enabled</strong></td><td>When enabled, Bito will automatically detect and use best-practice guidelines from agent configuration files such as <code>CLAUDE.md</code>, <code>AGENTS.md</code>, <code>GEMINI.md</code>, <code>.cursor/rules</code>, or <code>.windsurf/rules</code> during code reviews.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>sequence_diagram_enabled</strong></td><td>When enabled, Bito will generate interaction diagrams during code reviews to visualize the architecture and impacted components in the submitted changes.<br>Currently, it is supported for GitHub and GitLab.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>static_analysis.fb_infer.enabled</strong></td><td>Run Static Analysis tools during code reviews for providing better feedback.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>labels_excluded</strong></td><td>Comma-separated list of labels that, if present on a pull request or merge request, skip automatic review.<br><br>This is case-sensitive by default. For example, if we mention "Bug" in the repo-level <code>.bito.yaml</code> file and the tagged label is "bug", we won't match it. Users can use regex to make it case-insensitive, e.g., <code>(?i)^bug$</code> or <code>(?i)bug</code>.<br><br><strong>Example:</strong> <code>"wip, do-not-review, chore, size/*"</code> or <code>&#x3C;nil></code></td></tr></tbody></table>

&#x20;

## Sample `.bito.yaml` file

```yaml
suggestion_mode: comprehensive       # 'essential' = only major issues, 'comprehensive' = everything
post_description: true                # Include summary description in PR comment
post_changelist: true                 # Include walkthrough of changes

include_source_branches: feature/**,bugfix/**
include_target_branches: main,develop
exclude_files: docs/**,README.md

exclude_draft_pr: true            # Don't review draft PRs
secret_scanner_feedback: true      # Enable secret scanning feedback
linters_feedback: true             # Enable linting / static analysis

custom_guidelines:
  general:
    - name: "Global Checks"
      path: "./guidelines/global_checks.txt"
    - name: "Security Rules"
      path: "./guidelines/security.txt"
    - name: "Legacy Style Guide"
      path: "./guidelines/legacy.txt"
    - name: "Performance Checks"
      path: "./guidelines/perf.txt"
    - name: "Code Style"
      path: "./guidelines/style.txt"
  per_language:
    python:
      name: "Python Best Practices"
      path: "./guidelines/py.txt"
    javascript:
      name: "JS Style Guide"
      path: "./guidelines/js.txt"
    typescript:
      name: "TS Checks"
      path: "./guidelines/ts.txt"
    java:
      name: "Java Coding Standards"  
      Path: "./guidelines/java.txt"  

```

## Download `.bito.yaml` file&#x20;

### From GitHub:

You can download a sample `.bito.yaml` configuration file directly from Bito’s official GitHub repository.&#x20;

This file includes all supported configuration fields with example values to help you get started quickly.&#x20;

1. Go to the [Bito GitHub repository](https://github.com/gitbito/repo-level-settings-file).&#x20;
2. Open the `.bito.yaml` file.&#x20;
3. Click the **Download raw file** button to download it.

### From Bito Cloud UI:

You can also download the sample `.bito.yaml` configuration file from the Bito Cloud UI.&#x20;

* Go to [Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard.&#x20;
* Click the **Download settings file** button given in the Agent panel.&#x20;

{% hint style="info" %}
**Note:** Web browsers such as Google Chrome do not allow downloading files that begin with a dot `.`. As a result, when you download the sample settings file, it will be saved with a different name (for example, `agent.yaml` or `bito.yaml`). To use it correctly, rename the file to `.bito.yaml` before adding it to your repository.
{% endhint %}

{% hint style="info" %}
**Note:** By default, files that start with a dot `.` are hidden in most file explorers.

To view hidden files:&#x20;

* **Windows:** In File Explorer, go to the top menu bar, click **View**, then enable **Hidden items**.&#x20;
* **macOS:** Press `Command + Shift + .` in Finder.
* **Linux:** Run `ls -a` in your terminal.
  {% endhint %}

{% hint style="info" %}
**Note:** On macOS, the Finder app may not allow naming a file starting with a dot (e.g., `.bito.yaml`). In that case, open Terminal and use the following command to rename the file (replace `filename.yaml` with your actual file name):

`mv filename.yaml .bito.yaml`&#x20;
{% endhint %}

## Rules and limits

* The `.bito.yaml` file is read from the **source branch** of the pull request.&#x20;
* If a repo defines custom guidelines, agent-level guidelines are ignored for that repository.&#x20;
* If any property in the `.bito.yaml` file contains an invalid value, the entire configuration file will be rejected and default Agent Settings will be used instead.&#x20;
* If a property is missing in the `.bito.yaml` file, the corresponding value from the global Agent Settings will be used instead.


# FAQs

Answers to popular questions about the AI Code Review Agent.

## How do I whitelist Bito's gateway IP address for my on-premise Git platform?

To ensure the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) operates smoothly with your **GitHub (Self-Managed)** or **GitLab (Self-Managed)**, please whitelist all of Bito's gateway IP addresses in your firewall to allow incoming traffic from Bito. This will enable Bito to access your self-hosted repository.

**List of IP addresses to whitelist:**

* **`18.188.201.104`**
* **`3.23.173.30`**
* **`18.216.64.170`**

The agent response can come from any of these IPs.

## How can I prevent the AI Code Review Agent from stopping due to token expiry?

You should set a longer expiration period for your **GitHub Personal Access Token (Classic)** or **GitLab Personal Access Token**. We recommend setting the expiration to at least one year. This prevents the token from expiring early and avoids disruptions in the AI Code Review Agent's functionality.

Additionally, we highly recommend updating the token before expiry to maintain seamless integration and code review processes.

For more details on how to create tokens, follow these guides:

* **GitHub Personal Access Token (Classic):** [**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
* **GitLab Personal Access Token:** [**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

## What is "Estimated effort to review" in code review output?

This is an estimate, on a scale of 1-5 (inclusive), of the time and effort required to review this Pull Request (PR) by an experienced and knowledgeable developer. A score of 1 means a short and easy review, while a score of 5 means a long and hard review. It takes into account the size, complexity, quality, and the needed changes of the PR code diff. The score is produced by AI.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrRiW74jFIfoO1sB43Ipg%2Fscrnli_3_28_2024_6-13-26%20AM.png?alt=media&#x26;token=54a484a5-3be7-48b3-8d51-712779b7f7ac" alt=""><figcaption></figcaption></figure>

## Why does Bito need access to my Git account?&#x20;

Bito requires certain permissions to analyze pull requests and provide AI-powered code reviews. It never stores your code and only accesses the necessary data to deliver review insights.

## What permissions does Bito need?&#x20;

Bito requires: &#x20;

1. Read access to code and metadata: To analyze PRs and suggest improvements&#x20;
2. Read and write access to issues and pull requests: To post AI-generated review comments &#x20;
3. Read access to organization members: To provide better review context&#x20;

## I don’t have admin permissions. Can I still use Bito?&#x20;

If you don’t have admin access, you’ll need your administrator to install Bito on your organization’s Git account. Once installed, you can use it for PR reviews on allowed repositories. GitHub also sends a notification to the organization owner to request the organization owner to install the app.

## Does Bito store my code?&#x20;

No, Bito does not store or train models on your code. It only analyzes pull request data in real-time and provides suggestions directly within the PR.

## Can I choose which repositories Bito has access to?&#x20;

Yes, after installation, you can select specific repositories instead of granting access to all. You can also manage repository access later through our web dashboard.

## What happens after I install the Bito App?&#x20;

Once installed, you’ll be redirected to Bito, where you can:&#x20;

1. Select repositories for AI-powered reviews&#x20;
2. Customize review settings to fit your workflow&#x20;
3. Open a pull request to start receiving AI-driven suggestions

## Where can I get help if I have issues installing Bito?&#x20;

Contact <support@bito.ai> for any assistance.&#x20;


# Overview

Get instant feedback on your code changes directly within your code editor.

Unlock the power of AI-driven code reviews in VS Code, Cursor, Windsurf, and all JetBrains IDEs (including IntelliJ IDEA, PyCharm, WebStorm, and more) with Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview). This tool provides real-time, human-like feedback on your code changes, catching common issues before you submit a pull request.

The AI Code Review Agent helps you improve your code as you develop, so you don't have to wait for days to get feedback. This accelerates development cycles, boosts team productivity, and ensures higher code quality.

You can start using the Agent immediately—no setup is required!

<p align="center"><a href="https://marketplace.visualstudio.com/items?itemName=Bito.Bito" class="button primary">Install on VS Code</a><a href="https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant" class="button primary">Install on JetBrains</a><a href="https://open-vsx.org/extension/Bito/Bito" class="button primary">Install on Cursor</a><a href="https://open-vsx.org/extension/Bito/Bito" class="button primary">Install on Windsurf</a></p>

{% embed url="<https://youtu.be/RhgtIVuQTTw>" %}

## Prerequisites

1. Install the latest Bito IDE extension for [VS Code](https://marketplace.visualstudio.com/items?itemName=Bito.Bito), [JetBrains](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant), [Cursor](https://open-vsx.org/extension/Bito/Bito), or [Windsurf](https://open-vsx.org/extension/Bito/Bito).
2. A workspace subscribed to the Bito **Team Plan**. [Read documentation](https://docs.bito.ai/help/billing-and-plans/managing-workspace-plan) on how to upgrade.

{% hint style="info" %}
[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

3. The root of your project must use a supported Version Control System such as Git, Perforce, or SVN, and be opened in the supported IDE.

## How to use the Agent in IDE?

1. Open the Bito IDE extension.
2. Login to your workspace subscribed to the Bito **Team Plan**.
3. Type **`@codereview`** in the chat box to open a menu and select from the following actions:
   * **localchanges:** Review only the changes you’ve made in your local workspace that haven’t been staged yet. This is useful for quickly checking your current edits before moving them forward.
   * **stagedchanges:** Review the changes you’ve staged in Git but haven’t committed yet. This helps ensure only clean, well-reviewed updates get committed.
   * **uncommittedchanges:** Review all modifications that exist locally but aren’t yet committed—both staged and unstaged. Ideal for a full review of your current working directory.
   * **path:** Review a specific file or multiple files by providing their paths. This allows you to target critical files without running a review across your entire project.
   * **commitId:** Review one commit or a range of commits by referencing their commit IDs. Perfect for validating code history, checking incremental updates, or reviewing PR-related commits.

{% hint style="info" %}
**Supported review options based on your Version Control System (VCS):**

* If your project uses **Git**, all five review options are available.
* If your project uses a **non-Git VCS** (e.g., Perforce, SVN), only two review options are available:

  * **uncommittedchanges**
  * **path**

  Unsupported options will be hidden automatically.
  {% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FGn2V5FTwYtxPuCNchVkI%2Fscrnli_9HHvA5zvpYGTZW.png?alt=media&#x26;token=ced5c22f-1be9-4f59-8189-4d2bdcdbb8ec" alt=""><figcaption></figcaption></figure>

4. After that, choose between **Essential** and **Comprehensive** review modes:
   * In **Essential** mode, only critical issues are posted.
   * In **Comprehensive** mode, Bito also includes minor suggestion and potential nitpicks.
5. Submit to get the code review feedback.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0j3ANS8kCL2k701K2Fnb%2Fscrnli_In07VqlCg1h2JX.png?alt=media&#x26;token=3681155f-56cb-4ee2-98db-d23c1ca3b904" alt=""><figcaption></figcaption></figure>

## Start code review from context menu

You can also invoke the AI Code Review Agent directly from the **context menu** by right-clicking in the code editor and selecting commands under the **"Bito Code Review Agent"** menu.

This provides faster, on-the-go access to code reviews right where you work.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FmTmQV5vdOwcH1F9nTQKq%2FScreenshot%202025-10-03%20195645.png?alt=media&#x26;token=ee08a39a-a8bb-4c07-8038-0d7e00291448" alt=""><figcaption></figcaption></figure>

## Reviewing the feedback

Once the AI code review is complete, you'll receive a notification in the IDE. You can view the feedback in the Bito Panel, which includes a list of issues and their fixes.

Each item will contain the following details:

* **Issue description:** Description of the identified issue.
* **Fix description:** Recommended approach or steps to resolve the issue.
* **File path:** The file containing the issue.
* **Code suggestion:** The AI-generated code fix for the issue.

{% hint style="info" %}
Each code suggestion includes an **Apply** button. Click it to open the diff view, where you can review the changes and choose to accept or undo them.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F1cJ05HHTKAujAMuDvx4o%2FScreenshot%202025-08-08%20215021.png?alt=media&#x26;token=e489d83d-7cda-4fef-baf9-2525e6a5c60b" alt=""><figcaption></figcaption></figure>

## Code review session history

To view past code reviews, click the **Session history** icon in the top-right corner of the Bito Panel. This opens the **Session history** tab, which lists all your previous code review sessions.

From the list, click any session to open it and view the complete code review details along with the AI suggestions.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FDcBc1t3l7tHN9O1HNSzj%2Fscrnli_y9PGf09WQU5cq7.png?alt=media&#x26;token=79debcfd-5c60-4bf3-b38e-4e49667125dd" alt=""><figcaption></figcaption></figure>


# Installation guide


# Installing on Visual Studio Code

It takes less than 2 minutes

Get up and running with Bito in just a few steps! Bito seamlessly integrates with Visual Studio Code, providing powerful AI-driven code reviews directly within your editor. Click the button below to quickly install the Bito extension and start optimizing your development workflow with context-aware [AI Chat](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito), and more.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Install on VS Code</strong></mark></td><td><a href="https://marketplace.visualstudio.com/items?itemName=Bito.bito">https://marketplace.visualstudio.com/items?itemName=Bito.bito</a></td></tr></tbody></table>

## Video guide

Watch the video below to learn how to download the Bito extension on VS Code.

{% embed url="<https://www.loom.com/share/28bb3b7d1000422fb2459c4aee16463d>" %}
How to install Bito extension on VS Code
{% endembed %}

## Step-by-step instructions

1. In Visual Studio Code, go to the extension tab and search for Bito.

<div align="left"><figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOG7YiSRkjlDEBdbe9KNq%2Fimage.png?alt=media&#x26;token=5d8f0ae4-a82a-4d10-a768-112a1d626310" alt=""><figcaption></figcaption></figure></div>

2. Install the extension. We recommend you restart the IDE after the installation is complete.

{% hint style="info" %}
Starting with Bito version 1.3.4, the extension is only supported on VS Code versions 1.72 and higher. Bito does not support VS Code versions below 1.72, and earlier versions of Bito do not function properly on these older versions.
{% endhint %}

3. After a successful install, the Bito logo appears in the Visual Studio Code pane.

<img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhKqWVGtnM77IwKTs7GBM%2Fimage.png?alt=media&#x26;token=551802db-1ab3-4060-a8fd-314c97ab57d0" alt="" data-size="original">

4. Click the Bito logo to launch the extension and complete the setup process. You will either need to create a new workspace if you are the first in your company to install Bito or join an existing workspace created by a co-worker. See [managing-workspace-members](https://docs.bito.ai/help/account-and-settings/managing-workspace-members "mention")

{% hint style="info" %}
Visual Studio Code Marketplace Link <https://marketplace.visualstudio.com/items?itemName=Bito.bito>
{% endhint %}

## Setup Bito extension in VS Code running through SSH

SSH (Secure Shell) is a network protocol that securely enables remote access, system management, and file transfer between computers over unsecured networks.

Visual Studio Code IDE allows developers to access and collaborate on projects from any connected machine remotely. The corresponding extension \[Remote -SSH] must be installed on the host machine's Visual Studio Code IDE to utilize this feature.

The Bito VS Code extension seamlessly integrates with Remote development via SSH, allowing developers to utilize Bito features and capabilities on their remote machines.

### Remote SSH connection and setup

Please follow the instructions given in the links below:

* <https://code.visualstudio.com/docs/remote/ssh>
* <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse>

**Video Guide:**

{% embed url="<https://www.loom.com/share/29af0fa7133b4173a1c51b1ee1a71095>" %}

## Setup Bito extension in VS Code running through WSL

Running VS Code on WSL allows developers to work in a Linux-like environment directly from Windows. This kind of setup is to take advantage of development experience on both operating systems.

WSL provides access to Linux command-line tools, utilities, and applications, to enhance productivity and streamline the development process.

This setup ensures a consistent development environment across different systems, making it easier to develop, test, and deploy applications that will run on Linux servers.

### WSL connection and setup

Please follow the instructions given in the links below:

* <https://code.visualstudio.com/docs/remote/wsl-tutorial>
* <https://learn.microsoft.com/en-us/windows/wsl/install>

**Video Guide:**

{% embed url="<https://www.loom.com/share/ac1b89c9c04a4c4e9de3067deb319d2b>" %}


# Installing on JetBrain IDEs

It takes less than 2 minutes

Get up and running with Bito in just a few steps! Bito seamlessly integrates with popular JetBrains IDEs such as IntelliJ IDEA, PyCharm, and WebStorm, providing powerful AI-driven code reviews directly within your editor. Click the button below to quickly install the Bito extension and start optimizing your development workflow with context-aware [AI Chat](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito), and more.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Install on JetBrains</strong></mark></td><td><a href="https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4--bito-ai-code-assistant">https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4--bito-ai-code-assistant</a></td></tr></tbody></table>

## Video guide

Watch the video below to learn how to download the Bito extension on JetBrains IDEs.

{% embed url="<https://www.loom.com/share/0dbbbdb278114cb88f2cbb9806849ff7>" %}
How to install Bito extension on JetBrains IDEs
{% endembed %}

## Step-by-step instructions

1. In JetBrains IDEs such as IntelliJ, go to **File -> Settings** to open the **Settings** dialog, and click **Plugins -> Marketplace** tab in the settings dialog. Search for Bito.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F6Nlx25tskAb3rLzvaR58%2Fimage.png?alt=media&#x26;token=14bafff5-49af-4251-83ec-15b059cace17" alt=""><figcaption><p>Settings in IntelliJ IDE</p></figcaption></figure>

2\. Click "Install" to install the Bito extension. We recommend you restart the IDE after the installation is complete.

{% hint style="info" %}
Starting with Bito version 1.3.4, the extension is only supported on JetBrains versions 2021.2.4 and higher. JetBrains version 2021.1.3 is no longer supported from Bito version 1.3.4 onward.
{% endhint %}

3\. Bito panel will appear on the right-hand sidebar. Click it to complete the setup process. You will either need to create a new workspace if you are the first in your company to install Bito or join an existing workspace created by a co-worker. See [managing-workspace-members](https://docs.bito.ai/help/account-and-settings/managing-workspace-members "mention")

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrW565i0d8YPg8jc2eymy%2Fimage.png?alt=media&#x26;token=bd30680d-ea29-436c-afa2-a242075bc8b7" alt=""><figcaption><p>Bito in IntelliJ right-hand side bar</p></figcaption></figure>

{% hint style="info" %}
The menu to invoke the settings dialog may differ for different IDEs of the JetBrains family. The screenshots highlighted above are for the IntelliJ IDEA. You can access the Bito extension directly from the JetBrains marketplace at <https://plugins.jetbrains.com/plugin/18289-bito>.
{% endhint %}


# Vim/Neovim Plugin

Vim/ Neovim Plugin for Bito Using Bito CLI

We are excited to announce that one of our users has developed a dedicated Vim and Neovim plugin for Bito, integrating it seamlessly with your favorite code editor. This plugin enhances your coding experience by leveraging the power of Bito's AI capabilities directly within Vim and Neovim.

**Installation**

To get started with "vim-bitoai," follow these steps:

**Step 1: Install Bito CLI**

Make sure you have Bito CLI installed on your system. If you haven't installed it, you can find detailed instructions in the Bito CLI repository at[ https://github.com/gitbito/CLI](https://github.com/gitbito/CLI).

**Step 2: Install the Plugin**

Open your terminal and navigate to your Vim or Neovim plugin directory. Then, clone the "vim-bitoai" repository using the following command:

```sh
git clone https://github.com/zhenyangze/vim-bitoai.git

```

**Step 3: Configure the Plugin**

Open your Vim or Neovim configuration file and add the following lines:

```sh
" Vim Plug
Plug 'zhenyangze/vim-bitoai'

" NeoBundle
NewBundle 'zhenyangze/vim-bitoai'

" Vundle
Plugin 'zhenyangze/vim-bitoai'
```

Save the configuration file and restart your editor or run :source \~/.vimrc (for Vim) or  :source \~/.config/nvim/init.vim (for Neovim) to load the changes.

**Step 4: Verify the Installation**

Open Vim or Neovim, and you should now have the "vim-bitoai" plugin installed and ready to use.

**Usage**

You can use its powerful features once you have installed the "vim-bitoai" plugin. Here are some of the available commands:

* BitoAiGenerate: Generates code based on a given prompt.
* BitoAiGenerateUnit: Generates unit test code for the selected code block.
* BitoAiGenerateComment: Generates comments for methods, explaining parameters and output.
* BitoAiCheck: Performs a check for potential issues in the code and suggests improvements.
* BitoAiCheckSecurity: Checks the code for security issues and provides recommendations.
* BitoAiCheckStyle: Checks the code for style issues and suggests style improvements.
* BitoAiCheckPerformance: Analyzes the code for performance issues and suggests optimizations.
* BitoAiReadable: Organizes the code to enhance readability and maintainability.
* BitoAiExplain: Generates an explanation for the selected code.

To execute a command, follow these steps:

1. Open a file in Vim or Neovim that you want to work on.
2. Select the code block you want to act on. You can use visual mode or manually specify the range using line numbers.
3. Execute the desired command by running the corresponding command in command mode. For example, to generate code based on a prompt, use the : BitoAiGenerate command.\
   Note: Some commands may prompt you for additional information or options.
4. The plugin will communicate with the Bito CLI and execute the command, providing the output directly within your editor.

By leveraging the "vim-bitoai" plugin, you can directly harness the power of Bito's AI capabilities within your favorite Vim or Neovim editor. This integration lets you streamline your software development process, saving time and effort in repetitive tasks and promoting efficient coding practices.

**Customization**

The "vim-bitoai" plugin also offers customization options tailored to your specific needs. Here are a few variables you can configure in your Vim or Neovim configuration file:

* **g:bito\_buffer\_name\_prefix:** Sets the prefix for the buffer name in the Bito history. By default, it is set to 'bito\_history\_'.
* **g:vim\_bito\_path:** Specifies the path to the Bito CLI executable. If the Bito CLI is not in your system's command path, you can provide the full path to the executable.
* **g:vim\_bito\_prompt\_{command}:** Allows you to customize the prompt for a specific command. Replace {command} with the desired command.

To define a custom prompt, add the following line to your Vim or Neovim configuration file and replace your prompt with the desired prompt text:

```javascript
if !exists("g:vim_bito_prompt_{command}")
    let g:vim_bito_prompt_{command}="your prompt"
endif
```

Remember to restart your editor or run the appropriate command to load the changes.

We encourage you to explore the "vim-bitoai" plugin and experience the benefits of seamless integration between Bito and your Vim or Neovim editor. Feel free to contribute to the repository or provide feedback to help us further improve this plugin and enhance your coding experience.


# Upgrading Bito plugin

How to Update Bito Plugin on VS Code and JetBrains IDEs

Keeping your Bito plugin up to date ensures you have access to the latest features and improvements. In this article, we will guide you through the steps to update the Bito plugin on both VS Code and JetBrains IDEs. Let's dive in!&#x20;

**Updating Bito Plugin on VS Code**&#x20;

1. Open your VS Code IDE&#x20;
2. Navigate to the Extensions view by clicking on the square icon in the left sidebar&#x20;
3. In the search bar, type "Bito" to locate the Bito plugin&#x20;
4. Once you locate the Bito plugin, click on the update button to initiate the update &#x20;

Pro Tip 💡: Enable Auto-update for Bito Plugin on VS Code (as shown in the video)&#x20;

{% embed url="<https://www.loom.com/share/0b3fd776e789455da540ed6c4147a064>" %}
Updating Bito plugin on VS Code&#x20;
{% endembed %}

**Updating Bito Plugin on JetBrains IDEs**&#x20;

1. Open your JetBrains IDE (e.g., IntelliJ IDEA, PyCharm, etc.)&#x20;
2. Go to Settings by clicking on "File" in the menu bar (Windows/Linux) or by clicking on "IntelliJ IDEA" in the menu bar (macOS).&#x20;
3. In the Settings window, navigate to the "Plugins" section&#x20;
4. Switch to the "Installed" tab to view the list of installed plugins&#x20;
5. Locate the Bito plugin in the list and click on the update button to initiate the update&#x20;

{% embed url="<https://www.loom.com/share/4a9242f55f8a4873a36325d91d106394>" %}
Updating Bito Plugin on JetBrains IDEs
{% endembed %}


# Start free trial

Unlock premium Bito features with our 14-day free trial.

The Bito free trial gives you access to premium features for 14 days, allowing you to experience the full capabilities of Bito's AI-powered coding assistant.&#x20;

You can start your free trial directly from the Bito IDE extension using any of the three methods below.

## How to start your free trial

### Method 1: Using Bito AI chat

The easiest way to start your trial is through natural interaction:

1. Type a message in the Bito chat box and send it.
2. Look for the popup that appears after sending your message.
3. Click **Try for free** in the popup notification.
4. Complete signup in the browser window that opens.
5. Select **Start Trial** to activate your free trial.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFrW8360Kx2nycQq3uxO1%2FScreenshot%202025-09-15%20at%203.31.58%E2%80%AFPM.png?alt=media&#x26;token=3e83afdd-aa94-4163-a5cd-cda446e62173" alt=""><figcaption></figcaption></figure>

### Method 2: Click upgrade button

For a direct approach to upgrading:

1. Click the **UPGRADE** button given at the top of the chat window
2. Complete signup in the browser window that opens.
3. Select **Start Trial** to activate your free trial.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvgADIfnAQs5Xg8SZ5J8N%2Fscrnli_pha8fHYI2mEU62.png?alt=media&#x26;token=2f04a7a4-4a11-444f-8ef1-77f9dfdc0a39" alt="" width="407"><figcaption></figcaption></figure>

### Method 3: Quick trial activation

The fastest way to start your free trial:

1. Hover over **Include my code** (located above the Bito chat box).
2. In the popup, select **Click for 14 day free trial** to immediately activate your trial.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FdJPf3JQlM3uIHZcaGaDi%2FScreenshot%202025-09-15%20at%203.31.35%E2%80%AFPM_1.png?alt=media&#x26;token=a60b529c-d9de-4f79-8b76-aeea1a36fd75" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**💡 Pro tip:** Method 3 is the quickest option as it starts your trial instantly without opening any external windows.
{% endhint %}

## Available features in free trial

During your free trial, you'll have access to all the features of Bito Team Plan as mentioned on our [**Pricing**](https://bito.ai/pricing/) page. It includes:

* [**AI Code Reviews in Git**](https://docs.bito.ai/ai-code-reviews-in-git/overview)
* [**AI Code Reviews in IDE**](https://docs.bito.ai/ai-code-reviews-in-ide/overview)
* [**AI Chat**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito)
* [**AI that understands your code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code)
* and more.

<a href="https://bito.ai/pricing/" class="button primary">Visit our Pricing page</a>

## Need Help?

If you encounter any issues while starting your free trial:

* Check your internet connection.
* Ensure your Bito extension is up to date.
* Contact [**support@bito.ai**](mailto:support@bito.ai) if the trial doesn't activate properly.

## Next steps

Once your free trial is active, explore all the premium features available to you. Consider upgrading to a paid plan before your trial expires to continue enjoying advanced functionality.


# AI Chat in Bito

Bito AI chat is the most versatile and **flexible** way to use AI assistance. You can **type any technical question** to generate the best possible response. Check out these [use-cases-and-examples](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito/use-cases-and-examples "mention") to understand all you can do with Bito.

To use AI Chat, type the question in the chat box, and press '**Enter**' to send. You can add a new line in the question with '**SHIFT+ ENTER**'.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FisiEWE5VIqkIX7AGtjS6%2Fimage.png?alt=media&#x26;token=8a6da8a2-164f-4ed7-91c1-3f721a59adb5" alt=""><figcaption></figcaption></figure>

Bito starts streaming answers within a few seconds, depending on the size and complexity of the prompt.

{% hint style="info" %}
**Note:** **Team Plan** users receive **50 AI Chat requests per user per day** in the Bito IDE extension, while **Free Trial** users are limited to **20 AI Chat requests per day**.
{% endhint %}

Bito makes it super easy to use the answer generated by AI, and take a number of actions.&#x20;

#### Copy Answer

Copy the answer to the clipboard.

![](https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQmoc9EEI7xAfSOHOsOQj%2Fimage.png?alt=media\&token=b472bbcf-d611-4502-9cbd-fdad293f5126)

#### Regenerate Answer

AI may not give the best answer on the first attempt every time. You can ask Bito AI to regenerate the answer by clicking "Regenerate" button next to the answer.&#x20;

![](https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FEpH6CTrWSryVcBiLtpNT%2Fimage.png?alt=media\&token=7aa59479-21de-4643-85eb-26d7ac30744b)

#### Rate Response

Vote response "Up" or "Down". This feedback Bito improve the prompt handling.&#x20;

![](https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8Ku7DLryyOWFItdGx2RU%2Fimage.png?alt=media\&token=0e91552b-a390-4a1f-9ed1-6644cbc49815)

#### Modify Last Prompt

![](https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FcowfeVyCNol80r1EJtub%2Fimage.png?alt=media\&token=78299c6e-469e-42ef-ba95-730eb2a39128)

Many of these commands can be executed with keyboard shortcuts documented here: [keyboard-shortcuts](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito/keyboard-shortcuts "mention")


# Keyboard shortcuts

Bito UI in Visual Studio Code and JetBrains IDEs is entirely keyboard accessible. You can navigate Bito UI with standard keyboard actions such as TAB, SHIFT+TAB, ENTER, and ESC keys. Additionally, you can use the following shortcuts for quick operations.

The following video demonstrates important keyboard shortcuts.

{% embed url="<https://www.loom.com/share/a578f79e82414afb9c4fc7997cbc44f2>" %}

### General

| Command                                                                                                                                                     | Shortcuts                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Open Bito Panel:** Toggle Bito Panel on and off in the JetBrains IDE. In the Visual Studio Code, the shortcut opens the Bito panel if not already opened. | SHIFT + CTRL + O                                                                                                                                                                                                                                                                                                                                      |
| Puts cursor in the chatbox when Bito panel is in focus.                                                                                                     | SPACEBAR (Or start typing your question directly)                                                                                                                                                                                                                                                                                                     |
| **Execute** the chat command                                                                                                                                | ENTER                                                                                                                                                                                                                                                                                                                                                 |
| Add a **new line** in the chatbox                                                                                                                           | CTRL + ENTER or SHIFT + ENTER                                                                                                                                                                                                                                                                                                                         |
| **Modify** the **most recently executed** prompt. This copies the last prompt in the chatbox for any edits.                                                 | CTRL + M                                                                                                                                                                                                                                                                                                                                              |
| Expands and Collapse the "Shortcut" panel                                                                                                                   | <p>WINDOWS: CTRL + <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span>  <br>MAC: CTRL + SHIFT+  <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span>  </p> |

### Question & Answers

The following keyboard shortcuts work after the Q/A block is selected.&#x20;

| Command                                                                                                                 | Keyboard Shortcut                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Navigate between the Questions/Answers block. </p><p>Note: You must select the Q/A container with TAB/SHIFT+TAB.</p> | :arrow\_up: / :arrow\_down:                                                                                                                                                                                                                                                                                                                          |
| Copy the answer to the clipboard.                                                                                       | CTRL + C                                                                                                                                                                                                                                                                                                                                             |
| Insert the answer in the code editor                                                                                    | CTRL + I                                                                                                                                                                                                                                                                                                                                             |
| Toggle the diff view (when Diff View is applicable)                                                                     | CTRL + D                                                                                                                                                                                                                                                                                                                                             |
| Expand/Collapse the code block in the question.                                                                         | <p>WINDOWS: CTRL + <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span>  <br>MAC: CTRL + SHIFT+  <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span> </p> |
| Regenerate the answer                                                                                                   | CTRL + L                                                                                                                                                                                                                                                                                                                                             |
| Modify the prompt for the selected Q\&A. Bito copies the prompt in the chatbox that you can modify as needed.           | CTRL + U                                                                                                                                                                                                                                                                                                                                             |

### Change Default Keyboard Shortcuts

Bito has carefully selected the keyboard shortcuts after thorough testing. However, it's possible that Bito selected key combination may conflict with IDE or other extensions shortcut. You can change the Bito default shortcut keys to avoid such conflicts.&#x20;

#### Visual Studio Code Editor

1. To Open the Keyboards Shortcuts editor in VS Code, navigate to the menu under **File** > **Preferences** > **Keyboard Shortcuts**. (**Code** > **Preferences** > **Keyboard Shortcuts** **on macOS**)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FaMvFa1brpPpOtGrizNN9%2Fimage.png?alt=media&#x26;token=37f47323-0c58-4285-8930-ff74fcc259c1" alt=""><figcaption></figcaption></figure>

2. Search for default available commands, keybindings, or Bito extension-specific commands in VSCode keyboard shortcut editor.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbEpQlRxPM7Zfe8undFaD%2Fimage.png?alt=media&#x26;token=cf8fd721-6da2-4075-b741-7044b01ec691" alt=""><figcaption></figcaption></figure>

3. Finding a conflict in Key binding → Search for the key and take necessary action, e.g., **Remove** or **Reset.**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FssX3ehsh7Eyr7GDKhAMx%2Fimage.png?alt=media&#x26;token=d9267a20-0456-47af-800a-69fd3cb1b762" alt=""><figcaption></figcaption></figure>

4. **Add** a new key binding or map the existing Bito extension command.\
   Provide the necessary information (**Command ID**) to add the new key binding.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeuPp23D6Qnwe36vXIXzg%2Fimage.png?alt=media&#x26;token=ee3a223e-8a71-4734-b935-1f6893655bd5" alt=""><figcaption></figcaption></figure>

#### JetBrains&#x20;

JetBrains Document: <https://www.jetbrains.com/help/idea/configuring-keyboard-and-mouse-shortcuts.html>

1. **File > settings > keymaps > configure keymaps**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSghgMvL6zl2sZThE825G%2Fimage.png?alt=media&#x26;token=9168b5ac-20be-49e0-8cdb-13e31db2232a" alt=""><figcaption></figcaption></figure>

2. Bito extension shortcuts can be **overwritten** by going into the\
   File > Settings > Keymaps > configure keymaps > to the action you want to assign.  It will also overwrite the Bito shortcut if there are conflicts.
3. Bito extension keyboard shortcuts can be **changed** from the IntelliJ settings.\
   File > Settings > Keymaps > configure keymaps > plugins > Bito > action you want to change by right click.
4. Bito extension Keyboard shortcuts can be **deleted** from the IntelliJ settings.\
   File > Settings > Keymaps > configure keymaps > plugins > Bito > action you want to delete by right click.


# Chat session history

Bito automatically saves the chat session History. The session history is stored locally on your computer. You can return to any chat session and continue the AI conversation from where you left off. Bito will automatically maintain and restore the memory of the loaded chat session.

You can "Delete" any saved chat session or share a permalink to the session with your coworkers.

Here is the video overview of accessing and managing the session history.

{% embed url="<https://youtu.be/Qf4CGDUvOhI>" %}
Chat Session History
{% endembed %}

&#x20;

&#x20;


# Share chat session

Let your friends see what you and Bito are creating together.

Easily share insights from any [AI Chat](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito) session by creating a unique shareable link directly from the Bito extension in VS Code or JetBrains IDEs.

Whether you need to share AI-generated code suggestions, explanations, or any other chat insights, this feature allows you to create a public link that others can access. The link will remain active for 15 days and can be viewed by anyone with access to the URL, making collaboration and knowledge sharing seamless.

Additionally, you can quickly share your AI Chat session through a pre-written Tweet or an Email.&#x20;

{% hint style="info" %}
**Note:**

* The link will expire in 15 days.
* The session link will be publicly accessible by anyone with the link.
* Recipients can access the chat session in any web browser by using the unique URL.&#x20;
  {% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FB4p3LnzMqtgJsCLPJHKh%2Fscrnli_9_29_2023_3-39-04%20PM.png?alt=media&#x26;token=8f6da297-9724-4fcf-9b88-7b88e5a6424e" alt="" width="521"><figcaption></figcaption></figure>

Let's see how it is done:

1. Open Bito in Visual Studio Code or any JetBrains IDE.
2. Start a conversation in Bito’s AI Chat user interface.
3. Locate the share button on the top right of the Bito extension side-panel.
4. Click the share button to open a menu with options, including X (Twitter), Email, and Link.
5. **Share on X (Twitter):**
   1. Click on **X (Twitter)** from the menu, and a dialogue window will appear, asking whether you want to open the external site.
   2. Simply click "Open" to proceed.
   3. You will be redirected to the X (Twitter) website, with a pre-written tweet containing a link to your Chat Session ready to be published.
   4. Click the "Post" button to send the tweet.
6. **Share Through Email:**
   1. Click on **Email** from the menu, and you will be redirected to your email application.
   2. Select your email account if needed.
   3. The email will be pre-filled with all the necessary information, including the link to your Chat Session.
   4. Add the receiver(s) of this email using the "To" input field.
   5. Click the "Send" button to send the email.
7. **Share the Link:**
   1. Click on **Link** from the menu.
   2. A confirmation popup will appear. Click **Share session** to generate a unique URL for your chat session, which will automatically be copied to your clipboard for easy sharing.
   3. Feel free to share this link with anyone you'd like to.


# Appearance settings

The IDE customization settings are accessible through the new toolbar dropdown menu titled **"Extension Settings"**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0UHixHJuikUv2nUwjnps%2Fscrnli_3_17_2024_4-57-38%20PM.png?alt=media&#x26;token=01f3ed45-ab19-44d8-b315-62f8d72b9ad9" alt=""><figcaption></figcaption></figure>

## Light and Dark Themes

In Visual Studio Code and JetBrains IDEs, you can choose between a light or dark theme for the Bito panel to match your coding environment preference. For VS Code users, Bito also offers an adaptive theme mode in which the Bito panel and font colors automatically adjust based on your selected VS Code theme, creating a seamless visual experience.

You can set the desired theme through the **Theme** dropdown.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FlRXvpZ7emEWstkU9swru%2Fimage-20240314-053256_1.png?alt=media&#x26;token=2f7a2102-5825-464d-8582-3e822c2401f4" alt=""><figcaption></figcaption></figure>

## Theme Screenshots <a href="#theme-screenshots" id="theme-screenshots"></a>

### **“Always Light” Theme**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrJkeUFEIBJROh8kyqkFI%2Fimage-20240314-054325.png?alt=media&#x26;token=a7a3f5b4-355d-4c2f-8995-b698e5d3c23e" alt=""><figcaption></figcaption></figure>

### “Always Dark” Theme

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNa5470kJL5SvFd34hYCD%2Fimage-20240314-055349.png?alt=media&#x26;token=8aca281b-8a59-4c9e-a141-f5bbebbdf389" alt=""><figcaption></figcaption></figure>

### “Light” or “Dark” Theme - Matching IDE

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fg22q5U24ydE7xZNFmqXV%2Fimage-20240314-055544.png?alt=media&#x26;token=89f5e442-f1df-4a13-b4a9-f62758bce224" alt=""><figcaption></figcaption></figure>

### “Adaptive” Theme

Theme adapted from “Noctis Lux”:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FetW5a893BDxuAX8ZgEx1%2Fimage-20240314-055626.png?alt=media&#x26;token=c1f2be05-e0c1-4de4-b07f-3014223fd47e" alt=""><figcaption><p>Theme adapted from “Noctis Lux”</p></figcaption></figure>

Theme adapted from “Solarized Light”:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfoWGLG8RatwT0V8BOU89%2Fimage-20240314-060049.png?alt=media&#x26;token=7f0a5b7c-2241-406d-b216-050e95ec8318" alt=""><figcaption><p>Theme adapted from “Solarized Light”</p></figcaption></figure>

Theme adapted from “Tomorrow Night Blue”:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FCuwAYjFtdY2GIQh1KUfg%2Fimage-20240314-060227.png?alt=media&#x26;token=416314ee-badc-4245-a52f-a4b2f2360c95" alt=""><figcaption><p>Theme adapted from “Tomorrow Night Blue”</p></figcaption></figure>

Theme adapted from “barn-cat”:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FGvGPnHqjOsrEMZpUWCw2%2Fimage-20240314-060450.png?alt=media&#x26;token=b55363bf-2ec6-4919-901c-8e2253435a14" alt=""><figcaption><p>Theme adapted from “barn-cat”</p></figcaption></figure>

***

## Font Size Control

Take control of your code readability! Within the Bito extension settings, you can now adjust the font size for a comfortable viewing experience.

You can set the desired font size through the **Font Size** text field. However, if you check the **Font Size (Match with IDE Font)** checkbox, it will override the set font size with the ***Editor*** font size.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F78r9YzvAg3BXodRT8ORM%2Fimage-20240314-053234_1.png?alt=media&#x26;token=4be34fa8-ab75-4bff-bb72-11f958bada58" alt=""><figcaption></figcaption></figure>


# Open Bito in a new tab or window

Learn how to customize Bito’s view by switching from a side panel to a new tab or a separate window.

{% embed url="<https://youtu.be/e1Vrcqp2mj4>" %}


# Use cases and examples

Supercharging development with AI

Bito AI Assistance can help with generating new content or help with your existing code.&#x20;

Click on each use case for an example instruction and response.

* [Generate Code](#generate-code)
* [Command Syntax](#command-syntax)
* [Learn technical concepts](#learn-technical-concepts)
* [Generate test cases](#test-case)
* [Explain code](#explain-this-code)
* [Comment method](#comment-method)
* [Improve code performance](#improve-performance)
* [Check security](#check-for-security)
* [Find style issues](#find-style-issues)

## Generate Code

**Instruction**

{% hint style="info" %}
Implement a simple rest API in Go.
{% endhint %}

**Response**

{% hint style="success" %}

```go
package main
import ( 
"encoding/json" "fmt" "net/http" )
type user struct { Name string json:"name" Age int json:"age" }
func main() 
{http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) { 
	// Create user 
	u := user{ Name: "John Doe", Age: 25, }
	// Encode user
	uj, err := json.Marshal(u)
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	// Return user
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s\n", uj)
})
http.ListenAndServe(":3000", nil)
}
```

{% endhint %}

## **Command Syntax**

**Instruction**

{% hint style="info" %}
How to rebase a branch in git?
{% endhint %}

**Response**

{% hint style="success" %}

1. Checkout the branch you want to rebase:

$ git checkout

1. Rebase your branch against the upstream branch:

$ git rebase upstream/

1. Resolve any conflicts that arise.
2. Once all conflicts are resolved, do a git status to verify that all files have been updated correctly.
3. Finally, push the rebased branch to the remote repository:

$ git push origin --force
{% endhint %}

## **Learn Technical Concepts**

**Instruction**

{% hint style="info" %}
Can you explain the B+ tree with a code example?
{% endhint %}

**Response**

{% hint style="success" %}
A B+ tree is a self-balancing tree data structure used in databases to store and retrieve data efficiently. It is a variation of the B-tree and is designed to minimize the number of disk accesses required for insertion, deletion, and retrieval operations. B+ trees are characterized by the number of keys stored per node, the order of the nodes, and the number of children per node.

For example, a B+ tree of order 5 would have 5 keys per node and 5 children per node. When a node becomes full, it will split into two nodes, each containing half of the keys and half of the children. This means that all the nodes at the same level will have the same number of keys, making retrieval operations more efficient.

Here is an example in Python

```python
class Node:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.children = [None] * (order + 1)

class BPlusTree:
    def __init__(self, order):
        self.root = Node(order)
 
    def insert(self, key):
        if not self.root.keys:
            self.root.keys.append(key)
        else:
            pass # traverse the tree and insert the key
 
    def delete(self, key):
        pass # traverse the tree and delete the key
 
    def search(self, key):
        pass # traverse the tree and search for the key
 
# Create a B+ tree of order 5
bplus_tree = BPlusTree(5)
 
# Insert a key
bplus_tree.insert(10)
 
# Delete a key
bplus_tree.delete(10)

# Search for a key
bplus_tree.search(10)
```

{% endhint %}

## **Test Case**

**Instruction**

{% hint style="info" %}
Generate test cases for the following method.

```typescript
genrateLabelDiffArray(newLabelArray,oldLabelArray=[])
  {
    let new_ =[],old_=[],merged_=[];
    newLabelArray.forEach((lbl)=>{
      if(new_[lbl] === undefined){ new_[lbl] =0;merged_[lbl]=0; }
      ++new_[lbl];
      ++merged_[lbl];
    });
    
    oldLabelArray.forEach((lbl)=>{
      if(old_[lbl] === undefined){ old_[lbl] =0; }
      if(merged_[lbl] === undefined){ merged_[lbl] =0; }

      ++old_[lbl];
      --merged_[lbl]
    });
    let final = [];

    merged_.forEach((value,key)=>{
      if(value!=0){ 
      //  final[key.toString()] = value;
      final.push(key+":"+value);
       }
    })
    
      return final;
  }
```

{% endhint %}

**Response**

{% hint style="success" %}
Test Case 1: Input: newLabelArray = \[ 'Apple', 'Banana', 'Mango', 'Apple' ] oldLabelArray = \[ 'Banana', 'Mango', 'Orange' ] Expected Output: \['Apple:2', 'Orange:-1']

Test Case 2: Input: newLabelArray = \[ 'Apple', 'Banana', 'Apple', 'Orange' ] oldLabelArray = \[ 'Banana', 'Mango', 'Orange' ] Expected Output: \['Apple:2', 'Mango:-1']
{% endhint %}

## **Explain this Code**

**Instruction**

{% hint style="info" %}
What does this code do?

```typescript
genrateLabelDiffArray(newLabelArray,oldLabelArray=[])
  {
    let new_ =[],old_=[],merged_=[];
    newLabelArray.forEach((lbl)=>{
      if(new_[lbl] === undefined){ new_[lbl] =0;merged_[lbl]=0; }
      ++new_[lbl];
      ++merged_[lbl];
    });
    
    oldLabelArray.forEach((lbl)=>{
      if(old_[lbl] === undefined){ old_[lbl] =0; }
      if(merged_[lbl] === undefined){ merged_[lbl] =0; }

      ++old_[lbl];
      --merged_[lbl]
    });
    let final = [];

    merged_.forEach((value,key)=>{
      if(value!=0){ 
      //  final[key.toString()] = value;
      final.push(key+":"+value);
       }
    })
    
      return final;
  }
```

{% endhint %}

**Response**

{% hint style="success" %}
This code takes two arrays, newLabelArray and oldLabelArray, and generates a new array that contains the difference between the two arrays. It does this by first creating three empty arrays, new\_, old\_, and merged\_. It then iterates through the newLabelArray and adds each label to the new\_ array, as well as the merged\_ array. It then iterates through the oldLabelArray and does the same for the old\_ array, but also subtracts it from the merged\_ array. Finally, it iterates through the merged\_ array and checks for any values that are not equal to 0 and adds them to the final array. It then returns this final array.
{% endhint %}

## **Comment Method**

**Instruction**

{% hint style="info" %}
Generate a comment for this method, explaining the parameters and output

```typescript
genrateLabelDiffArray(newLabelArray,oldLabelArray=[])
  {
    let new_ =[],old_=[],merged_=[];
    newLabelArray.forEach((lbl)=>{
      if(new_[lbl] === undefined){ new_[lbl] =0;merged_[lbl]=0; }
      ++new_[lbl];
      ++merged_[lbl];
    });
    
    oldLabelArray.forEach((lbl)=>{
      if(old_[lbl] === undefined){ old_[lbl] =0; }
      if(merged_[lbl] === undefined){ merged_[lbl] =0; }

      ++old_[lbl];
      --merged_[lbl]
    });
    let final = [];

    merged_.forEach((value,key)=>{
      if(value!=0){ 
      //  final[key.toString()] = value;
      final.push(key+":"+value);
       }
    })
    
      return final;
  }
```

{% endhint %}

**Response**

{% hint style="success" %}
/\* This method takes two arrays, newLabelArray and oldLabelArray. It uses the elements of both arrays to generate a merged array, merged\_, where it counts the occurrences of each element in both arrays. It then creates a third array, final, containing the elements of merged\_ where the difference is not 0. The output is the final array. \*/
{% endhint %}

## **Improve Performance**

**Instruction**

{% hint style="info" %}
How can I improve the performance of this code?

```typescript
genrateLabelDiffArray(newLabelArray,oldLabelArray=[])
  {
    let new_ =[],old_=[],merged_=[];
    newLabelArray.forEach((lbl)=>{
      if(new_[lbl] === undefined){ new_[lbl] =0;merged_[lbl]=0; }
      ++new_[lbl];
      ++merged_[lbl];
    });
    
    oldLabelArray.forEach((lbl)=>{
      if(old_[lbl] === undefined){ old_[lbl] =0; }
      if(merged_[lbl] === undefined){ merged_[lbl] =0; }

      ++old_[lbl];
      --merged_[lbl]
    });
    let final = [];

    merged_.forEach((value,key)=>{
      if(value!=0){ 
      //  final[key.toString()] = value;
      final.push(key+":"+value);
       }
    })
    
      return final;
  }
```

{% endhint %}

**Response**

{% hint style="success" %}

1. Use ES6 syntax to simplify the code.&#x20;
2. Use a hashmap instead of looping through the arrays.&#x20;
3. Use a single loop to build the final array instead of two loops.&#x20;
4. Use array methods instead of for-each loops.&#x20;
5. Use optimized data structures like Set and Map.
   {% endhint %}

**Instruction**

{% hint style="info" %}
Rewrite this code with performance improvements?&#x20;

```typescript
genrateLabelDiffArray(newLabelArray,oldLabelArray=[])
  {
    let new_ =[],old_=[],merged_=[];
    newLabelArray.forEach((lbl)=>{
      if(new_[lbl] === undefined){ new_[lbl] =0;merged_[lbl]=0; }
      ++new_[lbl];
      ++merged_[lbl];
    });
    
    oldLabelArray.forEach((lbl)=>{
      if(old_[lbl] === undefined){ old_[lbl] =0; }
      if(merged_[lbl] === undefined){ merged_[lbl] =0; }

      ++old_[lbl];
      --merged_[lbl]
    });
    let final = [];

    merged_.forEach((value,key)=>{
      if(value!=0){ 
      //  final[key.toString()] = value;
      final.push(key+":"+value);
       }
    })
    
      return final;
  }
```

{% endhint %}

**Response**

{% hint style="success" %}

```typescript
// Rewritten Code
function genrateLabelDiffArray(newLabelArray, oldLabelArray = []) {
  let new_ = {},
    old_ = {},
    merged_ = {},
    final = [];

  newLabelArray.forEach((lbl) => {
    new_[lbl] = new_[lbl] ? new_[lbl] + 1 : 1;
    merged_[lbl] = merged_[lbl] ? merged_[lbl] + 1 : 1;
  });

  oldLabelArray.forEach((lbl) => {
    old_[lbl] = old_[lbl] ? old_[lbl] + 1 : 1;
    merged_[lbl] = merged_[lbl] ? merged_[lbl] - 1 : -1;
  });

  Object.entries(merged_).forEach(([key, value]) => {
    if (value !== 0) {
      final.push(key + ":" + value);
    }
  });
  
  return final;
}
```

{% endhint %}

## **Check for Security**

**Instruction**

{% hint style="info" %}
Find potential security issues in this code

```typescript
import database
search_term = input("Enter a search term: ")
query = "SELECT * FROM users WHERE name = '" + search_term + "'"
results = database.query(query)
print(results)
```

{% endhint %}

**Response**

{% hint style="success" %}

1. A lack of input validation: the user-supplied search term is not being validated to ensure it is safe to use in a database query. This could leave the system open to SQL injection attacks.
2. A lack of output encoding: the results from the database are not being encoded before they are printed. This could leave the system open to cross-site scripting attacks.
   {% endhint %}

**Instruction**

{% hint style="info" %}
Rewrite this code with fix to potential security issues

```typescript
import database
search_term = input("Enter a search term: ")
query = "SELECT * FROM users WHERE name = '" + search_term + "'"
results = database.query(query)
print(results)
```

{% endhint %}

**Response**

{% hint style="success" %}

```python
import database

# Get the user-supplied search term
search_term = input("Enter a search term: ")

# Use the user-supplied search term to query the database
query = "SELECT * FROM users WHERE name = %s"
results = database.query(query, (search_term,))

# Print the results
print(results)
```

{% endhint %}

## **Find Style Issues**

**Instruction**

{% hint style="info" %}
Identify potential issues that EsLint would find in this code

```typescript
genrateLabelDiffArray(newLabelArray,oldLabelArray=[])
  {
    let new_ =[],old_=[],merged_=[];
    newLabelArray.forEach((lbl)=>{
      if(new_[lbl] === undefined){ new_[lbl] =0;merged_[lbl]=0; }
      ++new_[lbl];
      ++merged_[lbl];
    });
    
    oldLabelArray.forEach((lbl)=>{
      if(old_[lbl] === undefined){ old_[lbl] =0; }
      if(merged_[lbl] === undefined){ merged_[lbl] =0; }

      ++old_[lbl];
      --merged_[lbl]
    });
    let final = [];

    merged_.forEach((value,key)=>{
      if(value!=0){ 
      //  final[key.toString()] = value;
      final.push(key+":"+value);
       }
    })
    
      return final;
  }
```

{% endhint %}

**Response**

{% hint style="success" %}
//ESLint would find the following issues:

* Missing semicolons (potential syntax errors)
* Missing spacing after 'forEach' statements
* Unused variables (e.g. 'old\_')
* Missing spacing between operators (e.g. '++new\_\[lbl]')
  {% endhint %}


# Templates

Instantly improve code performance, security, and readability with AI suggestions.

Templates help you improve your code quality instantly with AI-powered analysis. Get automated suggestions for performance optimization, security fixes, style improvements, and code cleanup without leaving your editor. Each template provides actionable feedback and ready-to-use code improvements that you can review and apply with a single click.

## Available templates

1. **Performance Check:** Optimize code performance and efficiency
2. **Security Check:** Identify and fix security vulnerabilities
3. **Style Check:** Apply coding style and formatting standards
4. **Improve Readability:** Enhance code clarity and organization
5. **Clean Code:** Remove debugging and logging statements

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSUfmpzVe0yq0ea7e9lj4%2Fscrnli_Q8Y7M7221K22CC.png?alt=media&#x26;token=a7bbc8bb-2a88-49f0-8a79-84b562537e09" alt=""><figcaption><p>Templates menu in Bito Panel</p></figcaption></figure>

## How to use templates

### Prerequisites

Select the code you want to analyze in your editor before using any template.

### Method 1: Click Templates button

1. Select code in your editor
2. Click the **Templates** button at the bottom of the Bito extension panel

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FIlm54ABFlep53SbO7Msl%2Fscrnli_LBZSDOD5kJEFCP.png?alt=media&#x26;token=152de194-82c8-438c-bad4-324a3dbfd330" alt=""><figcaption></figcaption></figure>

3. Choose the desired template from the dropdown menu

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FTmv57b2zTSu8ICeeNCm3%2FScreenshot%202025-09-24%20102702.png?alt=media&#x26;token=09ada6e2-347c-4acf-828d-29b42d66c6b0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Quick navigation:** Use arrow keys, Tab, or Shift+Tab to navigate the template menu
{% endhint %}

### Method 2: Open context menu

1. Select code in your editor
2. Right-click in the editor window
3. Hover over "Bito AI" in the context menu
4. Select the desired template from the submenu

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ffyd1ApBur9JzmIeIXXhN%2Fscrnli_yY9qlUNuqjsgEE.png?alt=media&#x26;token=a2a29dae-a4b3-4690-bbfc-87d912e74343" alt=""><figcaption></figcaption></figure>

### Method 3: Using slash `/` command in Bito chat box

1. Select code in your editor
2. Type `/` at the start of the Bito chat box
3. Choose the desired template from the dropdown menu

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fy6oQkPh1vEw2JhTJ6MnW%2Fscrnli_JtdylGOpPjV88Q.png?alt=media&#x26;token=5f92dbcd-0d01-48f3-bf3d-85beb34b2c50" alt=""><figcaption></figcaption></figure>

4. Type some text after the slash `/` to filter templates by name

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FkEoCYacM81CVY5qJdJdv%2Fscrnli_2L9qhV0bMjXexI.png?alt=media&#x26;token=447a8882-685e-4b98-a6e6-f574f57ec032" alt=""><figcaption></figcaption></figure>

### Method 4: Command Palette (VS Code)

1. Select code in your editor
2. Go to View → Command Palette (or press Ctrl+Shift+P / Cmd+Shift+P)
3. Type "bito" to see available templates
4. Select the desired template from the list

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FCVbZKpLylmEiUkPkVzFG%2Fscrnli_N85cjZ9T9Km35L.png?alt=media&#x26;token=5929d7f7-811f-4277-bc82-b5996fab2dbb" alt=""><figcaption></figcaption></figure>

## Applying code suggestions

When templates provide code improvements, you'll see an **Apply** button above the suggested code snippet.

1. Click the **Apply** button to open the diff view

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrCdkW4vw2G9iBry12rvj%2Fscrnli_1kuwzDuJ2KtDkM.png?alt=media&#x26;token=ba3f30a3-86b8-4d57-8a58-6f9e20d10bcf" alt="" width="402"><figcaption></figcaption></figure>

2. Review the changes highlighted in the diff:
   * Red lines show code to be removed
   * Green lines show code to be added
3. Choose your action:
   * **Accept** - Apply the suggested changes to your code
   * **Undo** - Reject the changes and keep your original code

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8HNiIQgoLELP1LQ1uSrT%2Fscrnli_JoOQ87pEpkZgyu.png?alt=media&#x26;token=f9ffdfad-6762-428b-95eb-5a73c6607d4f" alt=""><figcaption></figcaption></figure>

## Tips

* Select meaningful code blocks for better analysis results
* Templates work best with complete functions or logical code segments
* Review suggested changes before applying them to your codebase
* Verify that the changes don't break existing functionality
* Use multiple templates on the same code for comprehensive analysis
* Use the diff view to understand exactly what changes will be made


# AI that Understands Your Code

Work on your code with AI that knows your code!

<table data-view="cards"><thead><tr><th data-type="content-ref"></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="ai-that-understands-your-code/overview">overview</a></td><td>AI that Understands Your Code</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/how-it-works">how-it-works</a></td><td>Bito indexes your code locally using AI</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/available-keywords">available-keywords</a></td><td>Keywords to invoke AI that understands your code</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/example-questions">example-questions</a></td><td>What type of questions can be asked?</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/how-does-bito-understand-my-code">how-does-bito-understand-my-code</a></td><td>Sneak peek into the inner workings of Bito</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/using-in-visual-studio-code">using-in-visual-studio-code</a></td><td>AI that understands your code in VS Code</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/using-in-jetbrains-ides">using-in-jetbrains-ides</a></td><td>AI that understands your code in JetBrains IDEs (e.g., PyCharm)</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/managing-index-size">managing-index-size</a></td><td>Exclude unnecessary files and folders from repo to index faster!</td><td></td></tr><tr><td><a href="ai-that-understands-your-code/faqs">faqs</a></td><td>Answers to popular questions</td><td></td></tr></tbody></table>

&#x20;

&#x20;


# Overview

AI that Understands Your Code

{% embed url="<https://youtu.be/WTji_Kvs_4U>" %}
AI that understands your code
{% endembed %}

Bito has created the ability for our AI to understand your codebase, which produces dramatically better results that are personalized to you. This can help you write code, refactor code, explain code, debug, and generate test cases – all with the benefits of AI knowing your entire code base.

Bito AI automatically figures out if you're asking about something in your code. If it's confident, it grabs the relevant parts of your code from our [**index**](https://docs.bito.ai/help/bitos-ai-stack/indexing) and feeds them to the [**Large Language Models (LLMs)**](https://docs.bito.ai/help/bitos-ai-stack/large-language-models-llm) for accurate answers. But if it's unsure, Bito will ask you to confirm before proceeding.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FExHigCl44d1V8X11z1so%2Fscrnli_3_28_2024_7-05-52%20AM.png?alt=media&#x26;token=11ebed21-24ca-42ee-a8c8-238aa2949126" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To specifically ask questions related to your codebase, add the keyword **"my code"** in English, Cantonese, Japanese, Mandarin, Spanish, or Portuguese (more languages coming soon) to your questions in the Bito chatbox.

Example: **in my code explain the file apiUser.js**

Additional keywords for various languages are listed on the [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page.
{% endhint %}

For now, this feature is only available for our **Team Plan** which costs $15 per user per month. We have plans to release it for our **Free Plan** soon. But it will be limited to repos of 10MB indexable size.

Recent breakthroughs in [**Generative AI**](https://docs.bito.ai/help/bitos-ai-stack/generative-ai) and [**Large Language Models (LLMs)**](https://docs.bito.ai/help/bitos-ai-stack/large-language-models-llm) have helped make many AI Coding Assistant tools available, including Bito, to help you develop software faster.&#x20;

The major issue with these AI assistants, though, is that they have no idea about your entire codebase. Some tools take context from currently opened files in your IDE, while others enable you to manually enter code snippets in a chat-like interface and then ask questions about them.&#x20;

But with Bito’s AI that understands your entire repository, this is a whole new capability. For example, what if you could ask questions like:&#x20;

* how can I add a button to mute and unmute the song to **my code** in my music player? By default, set this button to unmute. Also, use the same design as existing buttons in UI.&#x20;
* In **my code** list all the files and code changes needed to add column desc in table raw\_data in dailyReport DB.&#x20;
* In **my code** suggest code refactoring for api.py and mention all other files that needs to be updated accordingly&#x20;
* Please write the frontend and backend code to take a user’s credentials, and authenticate the user. Use the authentication service in **my code**&#x20;

This will definitely improve the way you build software.


# How it Works?

Bito indexes your code locally using AI

{% embed url="<https://www.youtube.com/watch?v=RXMIkgozmwc>" %}

When you open a project in Visual Studio Code or JetBrains IDEs, Bito lets you enable the [**indexing**](https://docs.bito.ai/help/bitos-ai-stack/indexing) of code files from that project’s folder. Basically, this indexing mechanism leverages our new [**AI Stack**](https://docs.bito.ai/help/bitos-ai-stack) that enables Bito to understand your entire codebase and answer any questions regarding it.&#x20;

The index is stored locally on your system to provide better performance while maintaining the security/privacy of your private code.

{% hint style="info" %}
It takes 12 minutes per each 10MB of code to understand your repo, as the index is being built locally.
{% endhint %}

## How to Ask Questions?

Once indexing is complete, you can ask any question in the Bito chatbox. Bito uses AI to determine if you are asking about something in your codebase. If Bito is confident, it grabs the relevant parts of your code from our [**index**](https://docs.bito.ai/help/bitos-ai-stack/indexing) and feeds them to the [**Large Language Models (LLMs)**](https://docs.bito.ai/help/bitos-ai-stack/large-language-models-llm) for accurate answers. But if it's unsure, Bito will ask you to confirm before proceeding.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fum9m2Les997qz8ivTDLg%2Fscrnli_3_28_2024_7-05-52%20AM.png?alt=media&#x26;token=415c22f8-e92a-4fdf-bd79-b1affca7cdc5" alt=""><figcaption></figcaption></figure>

In case you ask a general question (not related to your codebase), then Bito will directly send your request to our LLM without first looking for the appropriate local context.

However, if you want to ask a question about your code no matter what, then you can use specific keywords such as **"my code", "my repo", "my project", "my workspace"**, etc., in your question.

The complete list of these keywords is given on our [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page.

Once Bito sees any input containing these keywords, it will use the index to identify relevant portions of code or content in your folder and use it for processing your question, query, or task.

## Security of your code&#x20;

As usual, security is top of mind at Bito, especially when it comes to your code.  A fundamental approach we have taken is to keep all code on your machine, and not store any code, code snippets, indexes, or [**embedding vectors**](https://docs.bito.ai/help/bitos-ai-stack/embeddings) on Bito’s servers or our API partners. All code remains on your machine, Bito does not store it. In addition, none of your code is used for AI model training.&#x20;

Learn more about [**Bito’s Privacy and Security Practices**](https://docs.bito.ai/privacy-and-security).&#x20;


# Available Keywords

Keywords to invoke AI that understands your code

Here is the list of keywords in different languages to ask questions regarding your entire codebase. Use any of these keywords in your prompts inside Bito chatbox.

### English:&#x20;

* my code&#x20;
* my repo&#x20;
* my project&#x20;
* my workspace&#x20;

### Chinese:&#x20;

* 我的代码&#x20;
* 我的仓库&#x20;
* 我的代码库&#x20;
* 我的项目&#x20;
* 我的文件夹&#x20;

### Chinese Traditional:&#x20;

* 我的程式碼&#x20;
* 我的倉庫&#x20;
* 我的項目&#x20;
* 我的工作區&#x20;

### Spanish:&#x20;

* Mi código&#x20;
* Mi repo&#x20;
* Mi proyecto&#x20;
* Mi espacio de trabajo&#x20;

### Japanese:&#x20;

* 私のコード&#x20;
* 私のリポ&#x20;
* 私のプロジェクト&#x20;
* 私のワークスペース&#x20;

### Portuguese:&#x20;

* Meu código&#x20;
* Meu repo&#x20;
* Meu projeto&#x20;
* Meu espaço de trabalho

## Polish

* Mój obszar roboczy
* moje miejsce pracy
* mój obszar roboczy
* moj kod
* mój kod
* moim kodzie
* moje repo
* moje repozytorium
* moim repo
* moj projekt
* mój projekt
* moim projekcie


# Example Questions

What Types of Questions Can be Asked?

You can try asking any question you may have in mind regarding your codebase. In most cases, Bito will give you an accurate answer. Bito uses AI to determine if you are asking about something in your codebase.

However, if you want to ask a question about your code no matter what, then you can use our pre-defined keywords such as **"my code", "my repo", "my project", "my workspace"**, etc., in your question.

The complete list of these keywords is given on our [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page.&#x20;

## **Here are some popular use cases (with example questions):**&#x20;

### Code Explanation&#x20;

* What a particular code file does&#x20;
  * In **my code** what does code in sendgrid/sendemail.sh do?&#x20;
* What a particular function in my code does&#x20;
  * In **my repo** explain what function message\_tokens do&#x20;

### Code Translation&#x20;

* In **my project** rewrite the code of signup.php file in nodejs&#x20;

### Code Refactoring&#x20;

* In **my workspace** suggest code refactoring for api.py and mention all other files that need to be updated accordingly&#x20;

### Fix Bugs&#x20;

* In **my code** find runtime error possibilities in script.js&#x20;
* Find logical errors in scraper.py in **my code**&#x20;

### Detect Code Smells&#x20;

* In **my code** detect code smells in /app/cart.php and give solution&#x20;

### Generate Documentation&#x20;

* Generate documentation for search.ts in **my workspace** in markdown format&#x20;

### Generate Unit tests&#x20;

* In **my code** write unit tests for index.php&#x20;
* In **my code** generate test code for code coverage of cache.c&#x20;

### Summarize Recent Code Changes&#x20;

* summarize recent code changes in **my code**&#x20;

### Code Search using natural language&#x20;

* Any function to compute tokens in **my project**?&#x20;
* Any code or script to send emails in **my workspace**?&#x20;
* In **my repo** list all the line numbers where $alexa array is used in index.php.

### Give details of making modifications&#x20;

* In **my code** list all the files and code changes needed to add column desc in table raw\_data in dailyReport DB.


# How does Bito Understand My Code?

Sneak Peek into the Inner Workings of Bito

Bito deploys a [**Vector Database**](https://docs.bito.ai/help/bitos-ai-stack/vector-databases) locally on the user’s machine, bundled as part of the Bito IDE plug-in. This database uses [**Embeddings**](https://docs.bito.ai/help/bitos-ai-stack/embeddings) (a vector with over 1,000 dimensions) to retrieve text, function names, objects, etc. from the codebase and then transform them into multi-dimensional vector space.&#x20;

Then when you give it a function name or ask it a question, that query is converted into a vector and is compared to other vectors nearby. This returns the relevant search results. So, it's a way to perform search not on keywords, but on meaning. Vector Databases are able to do this kind of search very quickly.

{% hint style="info" %}
Learn more about [**how Bito indexes your code**](https://docs.bito.ai/help/bitos-ai-stack/indexing) so that it can understand it.
{% endhint %}

Bito also uses an **Agent Selection Framework** that acts like an autonomous entity capable of perceiving its environment, making decisions, and taking actions to achieve certain goals. It figures out if it’s necessary to do an embeddings comparison on your codebase, do we need to perform an action against Jira, or do we do something else.&#x20;

Finally, Bito utilizes [**Large Language Models (LLMs)**](https://docs.bito.ai/help/bitos-ai-stack/large-language-models-llm) from Open AI, Anthropic, and others that actually provide the answer to the question by leveraging the context provided by the Agent Selection Framework and the embeddings.&#x20;

This is what makes us stand out from other AI tools like ChatGPT, GitHub Copilot, etc. that do not understand your entire codebase.&#x20;

We’re making significant innovations in our [**AI Stack**](https://docs.bito.ai/help/bitos-ai-stack) to simplify coding for everyone. To learn more about this head over to [**Bito’s AI Stack documentation**](https://docs.bito.ai/help/bitos-ai-stack).


# Using in Visual Studio Code

AI that understands your codebase in VS Code

{% embed url="<https://www.youtube.com/watch?v=RXMIkgozmwc>" %}

{% hint style="info" %}
This feature is only available for our **Team Plan**. Visit the [pricing page](https://bito.ai/pricing/) or [billing documentation](https://docs.bito.ai/help/billing-and-plans) to learn more about our paid plans.
{% endhint %}

1. Open your project’s folder using Visual Studio Code.&#x20;
2. Bito uses AI to create an [**index**](https://docs.bito.ai/help/bitos-ai-stack/indexing) of your project’s codebase. It enables Bito to understand the code and provide relevant answers. There are three ways to start the indexing process:&#x20;

   * When you open a new project, a popup box will appear through which Bito asks you whether you want to enable indexing of this project or not. Click on the “Enable” button to start the indexing process. You can also skip this step by clicking the “Maybe later” button. You can always index the project later if you want.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F3ftxNdlBeDRY6xqmhejw%2Fscrnli_8_29_2023_8-18-34%20AM.png?alt=media&#x26;token=d33f6f5b-1c69-4239-902e-0f6eacb9ec8c" alt="" width="563"><figcaption></figcaption></figure>

* In the bottom-left of Bito plug-in pane, hover your mouse cursor over this icon. You can also enable indexing from here by clicking on the “Click to enable it” text.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FltGHnZG7Y3tn50FP6Ra7%2Fscrnli_8_29_2023_8-47-21%20AM.png?alt=media&#x26;token=3ad4ae10-517f-4670-bdbc-350c0db5cc9e" alt="" width="563"><figcaption></figcaption></figure>
* Another option is to open the "Manage Repos" tab by clicking the laptop icon in the top-right corner of the Bito plugin pane.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fg0XkBWFOQEVv9GHwOKzM%2Fscrnli_8_29_2023_8-22-36%20AM.png?alt=media&#x26;token=7f868a77-67b6-4c2e-84a3-d3f584220e6a" alt="" width="563"><figcaption></figcaption></figure>
* From here you can start the [**indexing process**](https://docs.bito.ai/help/bitos-ai-stack/indexing) by clicking on the “Start Indexing” button. Here, you will also see the total indexable size of the repository. Read more about [**What is Indexable Size?**](https://docs.bito.ai/feature-guides/ai-that-understands-your-code/managing-index-size#what-is-indexable-size)

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8dC14JxM7PqVLnCOjPtD%2Fscrnli_8_29_2023_8-24-50%20AM.png?alt=media&#x26;token=70f208d7-7ea6-4d7e-b6d7-f9354516a4c8" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Bito usually takes around 12 minutes per each 10MB of code to understand your repo.
{% endhint %}

{% hint style="info" %}
Bito will still work correctly if you don’t enable indexing of your project. However, in that case, Bito will only be able to provide general answers.&#x20;
{% endhint %}

{% hint style="info" %}
If you have previously indexed some projects using Bito then they will show in the “Other projects” section.&#x20;
{% endhint %}

{% hint style="info" %}
Index building is aborted if the user logs out or if the user's subscription is canceled (downgraded from a paid plan to a free plan).
{% endhint %}

3. Let’s start the indexing process by using any of the above-mentioned methods.&#x20;
4. The status will now be updated to “Indexing in progress...” instead of “Not Indexed”. You will also see the real-time indexing progress for the current folder, based on the number of files indexed.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7gam7HQsLQpZbezxiN1w%2Fscrnli_8_29_2023_8-26-22%20AM.png?alt=media&#x26;token=edbe2d56-7454-4f55-bf55-79b09e169b7c" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
In case you close the VS Code while the indexing is in progress then don’t worry. The indexing will be paused and will automatically continue from where it left off when you reopen VS Code. Currently, the indexing will resume 5-10 minutes after reopening the IDE.
{% endhint %}

{% hint style="info" %}
The progress indicator for the other folders is updated every 5 minutes.
{% endhint %}

5. Once the indexing is complete, the status will be updated from “Indexing in progress...” to “Indexed”, and will look like this.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fg4WeAttB0V8dgR67vtF0%2Fscrnli_8_29_2023_8-27-30%20AM.png?alt=media&#x26;token=82dfe9c4-2a9b-44b3-a25a-b6cc1a35a079" alt="" width="563"><figcaption></figcaption></figure>
6. Now you can ask any question regarding your codebase by adding the keyword **"my code"** to your AI requests in the Bito chatbox. Bito is ready to answer them!

{% hint style="info" %}
Example: **in my code explain the file apiUser.js**

Additional keywords for various languages are listed on the [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page. Also, here are some [**Example Questions**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/example-questions).
{% endhint %}

7. In case you ever want to delete an index then you can do that by clicking on this three dots button and then clicking the “Delete” button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfeTslygIhN3kuY5f8zSv%2Fscrnli_8_29_2023_8-28-59%20AM.png?alt=media&#x26;token=a5e62723-b423-4a16-bb48-46674e8a442d" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Index deletion is allowed even if the index is in progress or in a paused state.
{% endhint %}

8. A warning popup box will open in the bottom of Bito’s plugin pane. You can either click on the “Delete” button to delete the project’s index from your system or click on the “Cancel” button to go back.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FV94JPEw8OV9wrLOhmyb1%2Fscrnli_8_29_2023_8-30-25%20AM.png?alt=media&#x26;token=5db7c77f-033d-43ad-8e73-30a42783d8e4" alt="" width="563"><figcaption></figcaption></figure>

## A Quick Example from a Real Project&#x20;

For the sake of this tutorial, we’ve created a simple **“Music Player using JavaScript”**.&#x20;

Here’s how it looks:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FPB7eGZdEzgd5jFpT3Vcf%2Fb40.png?alt=media&#x26;token=a2f08375-1b09-4969-a031-15b49751e631" alt=""><figcaption></figcaption></figure>

We have added a bunch of songs to this project. The song details like name, artist, image, and the music file name are stored in a file called **music-list.js**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJIiaFQosvis14KXWdTTL%2Fb44.png?alt=media&#x26;token=8738366a-c749-40d5-bdb0-e4a2457c4fb6" alt="" width="375"><figcaption></figcaption></figure>

### Question # 1&#x20;

Let’s ask Bito to **list names of all song artists used in my code**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhXSVLnx1pjP12JpiaSNw%2Fb43.png?alt=media&#x26;token=ef967b55-d328-4821-8c34-a0c8905df65c" alt="" width="558"><figcaption></figcaption></figure>

As you can see, Bito gave the correct answer by utilizing its understanding of our repository.&#x20;

Similarly, we can ask any coding-related question like find bugs, improve code, add new features, etc.&#x20;

### Question # 2&#x20;

Our music player is working fine, but we don’t have any option to mute/unmute the song.&#x20;

Let’s ask Bito to add this feature.&#x20;

**Here’s the question I used:**&#x20;

In my code how can i add a button to mute and unmute the song? By default, set this button to unmute. Also, use the same design as existing buttons in UI.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQArzJvfKL6Vguip5gwPD%2Fb45.png?alt=media&#x26;token=c5aa365c-1adc-4ee9-bdec-f2314b064c99" alt="" width="550"><figcaption></figcaption></figure>

After adding the code suggested by Bito, here’s how the music player looks when it starts (unmuted).

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FC0Ojp9aaKqpKljABdlp5%2Fscrnli_8_18_2023_12-03-42%20PM.png?alt=media&#x26;token=1883350d-3cde-437c-a448-43eccfeb8477" alt=""><figcaption></figcaption></figure>

And when muted:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKiC6qO4SjSjl0mEL8EkX%2Fscrnli_8_18_2023_12-04-27%20PM.png?alt=media&#x26;token=1d57af8b-d8f4-4bcd-b037-a00afd65706a" alt=""><figcaption></figcaption></figure>


# Using in JetBrains IDEs

AI that understands your codebase in JetBrains IDEs (e.g., PyCharm)

{% hint style="info" %}
This feature is only available for our **Team Plan**. Visit the [pricing page](https://bito.ai/pricing/) or [billing documentation](https://docs.bito.ai/help/billing-and-plans) to learn more about our paid plans.
{% endhint %}

1. Open your project’s folder using a JetBrains IDE. For this guide, we are using PyCharm.&#x20;
2. Bito uses AI to create an [**index**](https://docs.bito.ai/help/bitos-ai-stack/indexing) of your project’s codebase. It enables Bito to understand the code and provide relevant answers. There are three ways to start the indexing process:&#x20;

   * When you open a new project, a popup box will appear through which Bito asks you whether you want to enable indexing of this project or not. Click on the “Enable” button to start the indexing process. You can also skip this step by clicking the “Maybe later” button. You can always index the project later if you want.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fy4ohwQiz0sw1OSyBBIMV%2Fscrnli_8_29_2023_8-45-58%20AM.png?alt=media&#x26;token=22b663b4-57cc-46e5-ade2-580917864a53" alt="" width="563"><figcaption></figcaption></figure>

* In the bottom-left of Bito plug-in pane, hover your mouse cursor over this icon. You can also enable indexing from here by clicking on the “Click to enable it” text.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FprqcLERo0qda71JHfUE5%2Fscrnli_8_29_2023_8-48-59%20AM.png?alt=media&#x26;token=5f890235-5513-4393-868a-7d40a535345c" alt="" width="563"><figcaption></figcaption></figure>
* Another option is to open the "Manage Repos" tab by clicking the laptop icon in the top-right corner of the Bito plugin pane.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSEWw2YdRKyTgLzHqaYEh%2Fscrnli_8_29_2023_11-18-57%20AM.png?alt=media&#x26;token=1239730f-dca8-4c7c-bad6-23b536d64b1a" alt="" width="563"><figcaption></figcaption></figure>
* From here you can start the [**indexing process**](https://docs.bito.ai/help/bitos-ai-stack/indexing) by clicking on the “Start Indexing” button given in front of your current project. Here, you will also see the total indexable size of the repository. Read more about [**What is Indexable Size?**](https://docs.bito.ai/feature-guides/ai-that-understands-your-code/managing-index-size#what-is-indexable-size)

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOKUGPMR97iPKglm0lA4e%2Fscrnli_8_29_2023_11-24-10%20AM.png?alt=media&#x26;token=744020d6-fbfc-4f34-b605-eb0d251cb923" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Bito usually takes around 12 minutes per each 10MB of code to understand your repo.
{% endhint %}

{% hint style="info" %}
Bito will still work correctly if you don’t enable indexing of your project. However, in that case, Bito will only be able to provide general answers.
{% endhint %}

{% hint style="info" %}
If you have previously indexed some projects using Bito then they will show in the “Other projects” section.
{% endhint %}

{% hint style="info" %}
Index building is aborted if the user logs out or if the user's subscription is canceled (downgraded from a paid plan to a free plan).
{% endhint %}

3. Let’s start the indexing process by using any of the above-mentioned methods.&#x20;
4. The status will now be updated to “Indexing in progress...” instead of “Not Indexed”. You will also see the real-time indexing progress for the current folder, based on the number of files indexed.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fsgi0Dr5uyQjWu1aGi5kh%2Fscrnli_8_29_2023_8-53-07%20AM.png?alt=media&#x26;token=9753b843-b5be-4547-adaf-6ec7799ccb54" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
In case you close the JetBrains IDE (e.g., PyCharm) while the indexing is in progress then don’t worry. The indexing will be paused and will automatically continue from where it left off when you reopen the IDE. Currently, the indexing will resume 5-10 minutes after reopening the IDE.
{% endhint %}

{% hint style="info" %}
The progress indicator for the other folders is updated every 5 minutes.
{% endhint %}

5. Once the indexing is complete, the status will be updated from “Indexing in progress...” to “Indexed”, and will look like this.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMk4ALxEg2KLaCnaY01dY%2Fscrnli_8_29_2023_8-57-52%20AM.png?alt=media&#x26;token=37e7c22d-d03e-4225-a355-6f02c60308d2" alt="" width="563"><figcaption></figcaption></figure>
6. Now you can ask any question regarding your codebase by adding the keyword **"my code"** to your AI requests in the Bito chatbox. Bito is ready to answer them!

{% hint style="info" %}
Example: **in my code explain the file apiUser.js**

Additional keywords for various languages are listed on the [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page. Also, here are some [**Example Questions**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/example-questions).
{% endhint %}

7. In case you ever want to delete an index then you can do that by clicking on this three dots button and then clicking the “Delete” button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FY5fdRWYIXVti75AYv1mB%2Fscrnli_8_29_2023_8-59-06%20AM.png?alt=media&#x26;token=d39c4ff1-fd47-4563-a464-e7e45f48b5a1" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Index deletion is allowed even if the index is in progress or in a paused state.
{% endhint %}

8. A warning popup box will open in the bottom of Bito’s plugin pane. You can either click on the “Delete” button to delete the project’s index from your system or click on the “Cancel” button to go back.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQmcRxNbxYroopCn1epWo%2Fscrnli_8_29_2023_8-59-51%20AM.png?alt=media&#x26;token=5a2e7dbe-11c7-4d48-88b7-50310052238e" alt="" width="563"><figcaption></figcaption></figure>

## A Quick Example from a Real Project&#x20;

For the sake of this tutorial, we’ve created a clone of popular game **“Wordle”** using Python.&#x20;

Here’s how it looks:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJmOfDBFx3uAxIYb7z0S0%2Fb53.png?alt=media&#x26;token=c1e6ce20-bfeb-44df-ac87-670c2eae0d2f" alt=""><figcaption></figcaption></figure>

We have stored the list of words in files that are inside the “word\_files” folder. A word is selected from these files randomly at the start of the game that the player has to guess.&#x20;

### Question # 1&#x20;

Let’s ask Bito to **understand my code and briefly write about what this game is all about and how to play it**&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBbvesJzw19rEQUeK0hDs%2Fb54.png?alt=media&#x26;token=44f3c3f5-33bf-45b4-b23f-97c41a7b3e55" alt="" width="536"><figcaption></figcaption></figure>

Bito correctly described the game by just looking at its source code.

### Question # 2&#x20;

Our game (PyWordle) is working fine, but there is no count down timer to make it a bit more challenging.&#x20;

So, let’s ask Bito to add this feature.&#x20;

**Here’s the question I used:**&#x20;

> suggest code for main.py "class PyWordle" to add a count down timer for this game in my code. I'm using "self" in functions and variable names, so suggest the code accordingly. The player will lose the game if the time runs out. Set the time limit to 2 minutes (format like 02:00). The timer will start when the game starts. Also reset the timer when the game restarts, such as when player closes the "you won / you lost" popup. Display this real-time count down timer on the right-side of where the player score is displayed. Use the similar design as the player score UI. Also tell me exactly where to add your code. Make sure all of this functionality is working.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FPCW1jspVRlq7GJ7gyF4H%2Fb55.png?alt=media&#x26;token=b2f539b3-126e-47c8-b450-63d755902047" alt="" width="537"><figcaption></figcaption></figure>

Bito suggested the code which looks good. But, it was a bit incomplete and needs some improvements. So, I further asked a series of questions to Bito (one-by-one) to fix the remaining issues.&#x20;

After adding the code suggested by Bito, here's how the PyWordle game looks now. As you can see the countdown timer is accurately added where we want it to be added.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqawYeeYn6KAlKA9OGMYm%2Fb56.jpg?alt=media&#x26;token=5096f8d2-4b15-4615-bdaf-645b16bc0ae3" alt=""><figcaption></figcaption></figure>


# Managing Index Size

Exclude unnecessary files and folders from repo to index faster!

## What is Indexable Size?&#x20;

Indexable size is size of all code files, excluding following from the folder:&#x20;

* **Directory/File based filtering**
  * logs, node\_modules, dist, target, bin, package-lock.json, data.json, build, .gradle, .idea, gradle, extension.js, vendor.js, ngsw\.json, polyfills.js, ngsw-worker.js, runtime.js, runtime-main.js, service-worker.js, bundle.js, bundle.css
* **Extension based filtering**
  * bin, exe, dll, log, aac, avif, bmp, cda, gif ,mp3, mp4, mpeg, weba, webm, webp, oga, ogv, png, jpeg, jpg, bmp, wpa, tif, tiff, svg, ico, wav, mov, avi, doc, docx, ppt, pptx, xls, xlsx, ods, odp, odt, pdf, epub, rar, tar, zip, vsix, 7z, bz, bz2, gzip, jar, war, gz, tgz, woff, woff2, eot, ttf, map, apk, app, ipa, lock, tmp, logs, gmo, pt
* **Hidden files are filtered** i.e., files starting with "."&#x20;
* **All Empty files are filtered.**&#x20;
* **All Binary files are also filtered.**

## Is there any limit on repository size?&#x20;

For workspaces that have upgraded to Bito's **Team Plan**, we have set the indexable size limit to 120MB per repo. However, once we launch the "AI that Understands Your Code" feature for our **Free Plan** users, they will be restricted to repositories with an indexable size limit of 10MB.

Learn more about [**indexable size**](#what-is-indexable-size) above and see which files and folders are excluded by default.

You can reduce your repo's indexable size by excluding certain files and folders from indexing using [**.bitoignore**](#what-is-.bitoignore-and-how-to-use-it) file and remain within the limit.

## What if a repo hits 120MB limit?

If a repo hits 120MB limit, then the below error message will be displayed in the "Manage repos" tab and the repo's index status will be changed to "Not Indexed".

{% hint style="danger" %}
Sorry, we don’t currently support repos of this size. Please use .bitoignore to reduce the size of the repo you want Bito to index.
{% endhint %}

To fix this issue, follow our instructions regarding [**how to use .bitoignore file**](#what-is-.bitoignore-and-how-to-use-it) and reduce your repo's size and bring it under the max limit of 120MB.

After that, you must [**delete the index**](https://docs.bito.ai/ai-code-reviews-in-ide/faqs#how-to-delete-project-index-from-ide) and then restart the indexing by clicking on the "Start Indexing" button shown for the repo folder. You can also follow our step-by-step guides to [**Start Indexing in Visual Studio Code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-visual-studio-code) and [**Start Indexing in JetBrains**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-jetbrains-ides) IDEs.

## What is .bitoignore and how to use it?

A `.bitoignore` file is a plain text file where each line contains a pattern or rules that tells Bito which files or directories to ignore and not index. In other words, it's a way to reduce your repo's indexable size. You can also see [**which files/folders are excluded by default**](#what-is-indexable-size).

**There are two ways to use `.bitoignore` file:**

1. Create a `.bitoignore` file inside the folder where indexes created by Bito are stored. e.g. `<user-home-directory>/.bito/localcodesearch/.bitoignore`
   * On Windows, this path will be something like: `C:\Users\<your username>\.bito\localcodesearch\.bitoignore`
   * **Note:** The custom ignore rules you set in this `.bitoignore` file will be applied to all the repositories where you have **enabled indexing**.
2. Create a `.bitoignore` file inside your repository's root folder.

{% hint style="info" %}
If a **.gitignore** file is available in your repo then Bito will also use that to ignore files & folders from indexing process. Both **.bitoignore** and **.gitignore** files can work together without any issues.
{% endhint %}

{% hint style="info" %}
At present, Bito considers only those **.gitignore** files that are placed in the project root directory and **.bitoignore** files that are placed either in `<user-home-directory\.bito\localcodesearch>` or `<project-root-directory>`
{% endhint %}

Changes to the `.bitoignore` file are taken into account at the beginning of the indexing process, not during or after the indexing itself.

Therefore, to implement changes made to the `.bitoignore` file, you'll need to [**delete the index**](https://docs.bito.ai/ai-code-reviews-in-ide/faqs#how-to-delete-project-index-from-ide) and then restart the indexing by clicking on the "Start Indexing" button shown for the repo folder. You can also follow our step-by-step guides to [**Start Indexing in Visual Studio Code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-visual-studio-code) and [**Start Indexing in JetBrains**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-jetbrains-ides) IDEs.

{% hint style="info" %}
Please note that any changes to the **.bitoignore** or **.gitignore** file will take a minimum of 3 to 5 minutes to trigger new indexing.
{% endhint %}

## Common .bitoignore Patterns <a href="#common-.bitoignore-patterns" id="common-.bitoignore-patterns"></a>

Understanding these patterns/rules is crucial for effectively managing the files and directories that Bito indexes and excludes in your projects.

<table><thead><tr><th width="330">Sample Rule</th><th>Description</th></tr></thead><tbody><tr><td><code># this is a comment.</code></td><td>Any line that starts with a <code>#</code> symbol is considered as a comment and will not be processed.</td></tr><tr><td><code>*</code></td><td>(Wildcard character) Ignores all files</td></tr><tr><td><code>**</code></td><td>(Wildcard character) Match any number of directories.</td></tr><tr><td><code>todo.txt</code></td><td>Ignores a specific file named <code>todo.txt</code></td></tr><tr><td><code>*.txt</code></td><td>Ignores all files ending with <code>.txt</code></td></tr><tr><td><code>*.*</code></td><td>Ignores all files with any extension.</td></tr><tr><td><code>Engine/</code> or <code>Engine/**</code></td><td>Ignores all files in the <code>Engine</code> directory and their subdirectories (contents).</td></tr><tr><td><code>subdirectory1/example.html</code></td><td>Ignore the file named <code>example.html</code>, specifically located in the directory named <code>subdirectory1</code>.</td></tr><tr><td><code>!contacts.txt</code></td><td>(Negation Rule) Explicitly tracks <code>contacts.txt</code>, even if all <code>.txt</code> files are ignored.</td></tr><tr><td><code>!Engine/Batch/Builds</code></td><td>(Negation Rule) Tracks the <code>Builds</code> directory inside <code>Engine/Batch</code>, overriding a broader exclusion.</td></tr><tr><td><code>!Engine/Batch/Builds/**</code></td><td>(Negation Rule) Tracks the <code>Builds</code> directory and all of its subdirectories inside <code>Engine/Batch</code>, overriding a broader exclusion.</td></tr><tr><td><code>!.java</code></td><td>(Negation Rule) Ensures that all <code>.java</code> files are included, overriding any previous ignore rules that might apply to them.</td></tr><tr><td><code>!subdirectory1/*.txt</code></td><td>(Negation Rule) Track files with the <code>.txt</code> extension located specifically in the <code>subdirectory1</code> directory, even if other rules might otherwise ignore <code>.txt</code> files.</td></tr><tr><td><code>BitoUtil?.java</code></td><td>The <code>?</code> (question mark) matches any single character in a filename or directory name.</td></tr></tbody></table>

## Negation `!` (exclamation mark)

When a pattern starts with `!` it negates the pattern, meaning it explicitly includes files or directories that would otherwise be ignored. For example, have a look at this sample **.bitoignore** file:

{% tabs %}
{% tab title=".bitoignore" %}

```
Engine/**
!Engine/Build/BatchFiles/**
```

{% endtab %}
{% endtabs %}

&#x20;Here `!Engine/Build/BatchFiles/**` pattern includes all files in the `Engine/Build/BatchFiles` directory and its subdirectories, even though `Engine/**` pattern would ignore them.

{% hint style="info" %}
**Avoid Ambiguous Patterns:** Negation patterns can become confusing when they potentially match multiple files. Target specific files or folders rather than using wildcards in negation patterns.

For example, it is better to use patterns like **`!Engine/Build/BatchFiles/script.bat`** instead of **`!Engine/Build/BatchFiles/**`**
{% endhint %}

## .bitoignore Examples

### Exclude Files/Folders

```
# Ignore specific file named "config.ini"
config.ini

# Ignore all files with a '.bak' extension
*.bak

# Ignore all files with a '.kunal' extension
*.kunal

# Exclude directories
backup
temp/
dist/vendor
```

### Exclude Everything Except Specific Files

To exempt a file, ensure that the negation pattern `!` appears afterward, thereby overriding any broader exclusions.

```
# Ignore all files except C++, header and python files
*
!*.cpp
!*.h
!*.py
```


# FAQs

Answers to Popular Questions

## How many repositories can Bito index?&#x20;

Bito can index unlimited repositories for workspaces that have subscribed to our **Team Plan**. This feature is also coming soon for our **Free Plan**. But it will be limited to 10MB maximum indexable size of repository.&#x20;

## Why is the index creation taking a long time?&#x20;

Bito takes time to thoroughly read your entire repository and understand it. This is completely normal. If your repository is a bit large, then it can take several hours to get [**indexed**](https://docs.bito.ai/help/bitos-ai-stack/indexing).&#x20;

Bito usually takes around 12 minutes per each 10MB of code to understand your repo.&#x20;

## Why is the answer not complete?&#x20;

There is a limit on the amount of memory/context that can be used at a time to answer the question, so the answers sometimes may not cover all the code. To solve for this, restrict the questions by providing additional criteria like:&#x20;

* In my code explain message\_tokens in ai/request.js

## Where can I see the status of my Index?&#x20;

Open your project in VS Code or JetBrains IDEs. From the Bito plugin pane, click the laptop icon located in the top-right corner.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXZVEbTI8H6qOP6PHDwyw%2Fscrnli_8_29_2023_8-23-36%20AM.png?alt=media&#x26;token=53079c1d-0572-417a-b38f-f0f24538be5b" alt="" width="563"><figcaption></figcaption></figure>

On this tab, you will see the status of your current project as well as the status of any other project that you indexed previously.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FalKaS0IhqxjsiKmhwIMk%2Fscrnli_8_29_2023_8-27-30%20AM.png?alt=media&#x26;token=6a5c75cd-4046-402a-aeb3-55f26bb111e2" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
List of Indexing Statuses:

* **Not Indexed:** A new project that you have not started indexing yet.
* **Indexing in progress:** A project that is currently being indexed.
* **Indexing is paused:** A project that was previously being indexed but is now paused for some reason. Generally, if you close the IDE while the project is being indexed, its status will change from "Indexing in progress" to "Indexing is paused".
* **Indexed:** A project that has already been indexed, and Bito is ready to answer any questions about it.
  {% endhint %}

## What happens if my IDE got closed while indexing is in progress?&#x20;

In case you close the Visual Studio Code or JetBrains IDE (e.g., PyCharm) while the [**indexing**](https://docs.bito.ai/help/bitos-ai-stack/indexing) is in progress then don’t worry. The indexing will be paused and will automatically continue from where it left off when you reopen the IDE. Currently, the indexing will resume 5-10 minutes after reopening the IDE.

## How to delete project index from IDE?

1. To delete an index, navigate to the "Manage repos" tab.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOUr4D9YvtbF8gfdwH0H8%2Fscrnli_8_29_2023_8-23-36%20AM.png?alt=media&#x26;token=ae3a91ed-ff2a-4a39-b073-1057c7c8d353" alt="" width="563"><figcaption></figcaption></figure>
2. Next, click on the three dots button located in front of your project’s name, and then select the "Delete" option.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8crcrMhH4YlYv1ZgOtim%2Fscrnli_8_29_2023_8-28-59%20AM.png?alt=media&#x26;token=53baef28-8960-4d0d-a2fe-c5aa88123430" alt="" width="563"><figcaption></figcaption></figure>
3. A warning popup box will appear at the bottom of Bito's plugin pane. You can choose to click the "Delete" button to remove the project's index from your system, or click the "Cancel" button to go back.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjQfH6PVPC9NqWTt06mR9%2Fscrnli_8_29_2023_8-30-25%20AM.png?alt=media&#x26;token=7beaecb3-3190-47cc-97b6-8e6a2aa5fee4" alt="" width="563"><figcaption></figcaption></figure>

## How to fix indexing issues in Visual Studio Code and JetBrains IDEs (e.g., IntelliJ IDEA, PyCharm, etc.)?

{% hint style="info" %}
Before getting started, please ensure that you have allowed your project sufficient time to be indexed. Bito typically requires approximately 12 minutes for every 10MB of code to understand your repository.
{% endhint %}

{% embed url="<https://www.youtube.com/watch?ab_channel=Bito&v=-nw6K5jTHQc>" %}

If for some reason you are struggling to index your project’s folder while using Visual Studio Code or JetBrains IDEs, then follow the below steps to delete the folder that contains all the indexes and try to re-index your project.&#x20;

1. Close all JetBrains IDEs and VS Code instances where Bito is installed.&#x20;
2. Go to your users directory. For example, on Windows it will be something like **C:\Users\\\<your username>**
3. Now, find **.bito** folder and delete it. (**Note:** All configuration settings and project indexes created by Bito will be deleted. You will also be logged out from Bito IDE plugin)

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FitV2BiLj7eoNelJz5iIW%2FScreenshot%202023-09-19%20113841.png?alt=media&#x26;token=bca5f6b1-25d1-4ac4-a652-d6b1078e75e8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If Windows is installed on a drive other than “C”, you will need to locate the **.bito** folder on that drive instead.
{% endhint %}

4. Once you have deleted the **.bito** folder, open your project in the IDE again.&#x20;
5. After restarting the IDE, you will need to enter your email ID and a 6-digit code to log in. Once you're logged in, select the workspace that has an active paid subscription.
6. After that, when Bito asks if you wish to index the folder, you can select "Maybe later".&#x20;
7. Then, navigate to the "Manage repos" tab in the Bito plugin pane, where you should see the folder name listed under the "Current project" along with its size, indicating that it is not indexed. Since you have deleted the **.bito** folder, the "Other projects" section will no longer display any entries.&#x20;
8. Finally, click on "Start Indexing" and it should begin indexing the folder.&#x20;

{% hint style="info" %}
For testing purposes, we suggest using a folder with a small size and avoid changing the folder in IDE until indexing is completed and the folder icon turns green.&#x20;

By the way, you can continue using Bito while indexing is in progress in the background.
{% endhint %}


# AI Architect

AI that understands your codebase inside out — and codes like your team.

Bito’s **AI Architect** builds a knowledge graph of your entire codebase.&#x20;

It analyzes all your repositories (whether you have 50 or 5000 repos) to learn about your codebase architecture, microservices, modules, API endpoints, design patterns, and more.&#x20;

AI Architect can then provide accurate and well-written code.&#x20;

This fundamentally changes the game for enterprises with many microservices or large, complex codebases.&#x20;

We believe AI Architect provides an ability to perform a code review similar to how a principal engineer or an architect would be able to help connect the dots on the impact of your changes across your codebase.&#x20;

## How you can use AI Architect

AI Architect is designed to be flexible and can power multiple use cases across different AI coding tools and workflows.

* [**Integrate via MCP server**](#getting-started) – Use AI Architect as an **MCP (Model Context Protocol) server** to connect with tools like [Claude Code](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-claude-code), [Cursor](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-cursor), [Windsurf](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-windsurf), and [GitHub Copilot (VS Code)](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-github-copilot-vs-code). It helps connected tools understand your codebase and workflows better, resulting in accurate and more reliable suggestions.
* [**Example: Bito’s AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) – One example of AI Architect in action is **Bito’s AI Code Review Agent**, which uses AI Architect to deliver smarter, context-aware code reviews directly in your pull requests and IDEs.

## Why use AI Architect?

Most AI coding tools struggle with accuracy in real-world codebases because they don’t know your internal APIs, endpoints, or library usage.&#x20;

AI Architect eliminates this problem by learning from your actual repositories.&#x20;

* How your team structures code&#x20;
* How different services interact&#x20;
* How external dependencies are used&#x20;
* Etc.&#x20;

**Key benefits include:**&#x20;

* **Accurate, production-ready code** — because it knows your codebase inside out.&#x20;
* **Consistent design adherence** — aligns with your architecture patterns and coding conventions.&#x20;
* **Faster onboarding** — new engineers or AI agents can quickly understand the system structure.&#x20;
* **Enhanced documentation and diagramming** — through its internal understanding of interconnections between modules and APIs.&#x20;
* **Smarter code reviews** — reviews with system-wide awareness of dependencies and impacts.&#x20;

&#x20;

## How AI Architect differs from Embeddings?

Traditional embeddings work like a search engine — they retrieve code snippets or documents similar to a given query.&#x20;

They can find related content but can’t understand how different parts of your system work together.&#x20;

AI Architect, on the other hand:&#x20;

* Builds a knowledge graph that captures relationships between repositories, modules, APIs, and libraries.
* Provides precise answers and implementations, not just search results.
* Understands context and intent — how and why something is implemented in your codebase.
* Enables system-aware reasoning, allowing AI agents to generate or review code with full architectural understanding.

## Getting started

1. Contact Bito support team at <support@bito.ai>  to have your repositories indexed. You will get an **MCP server URL** and **Auth token** from Bito.
2. Configure MCP server in supported AI coding tools such as Claude Code, Cursor, Windsurf, and GitHub Copilot (VS Code).

   Select your AI coding tool from the options below and follow the step-by-step installation guide to seamlessly set up AI Architect.

   * [**Guide for Claude Code**](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-claude-code)
   * [**Guide for Cursor**](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-cursor)
   * [**Guide for Windsurf**](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-windsurf)
   * [**Guide for GitHub Copilot (VS Code)**](https://docs.bito.ai/other-bito-ai-tools/ai-architect/guide-for-github-copilot-vs-code)


# Guide for Claude Code

Integrate Claude Code with AI Architect for more accurate, codebase-aware AI assistance.

Use Bito's [**AI Architect**](https://docs.bito.ai/other-bito-ai-tools/ai-architect) with **Claude Code** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Claude Code can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Contact Bito support team at <support@bito.ai> to have your repositories indexed. You will get an **MCP server URL** and **Auth token** from Bito.
2. Download **BitoAIArchitectGuidelines.md** file. You will need to copy/paste the content from this file later when configuring AI Architect.

## Set up AI Architect

Follow the setup instructions for your operating system:

* [**Windows**](#windows)
* [**macOS**](#macos)
* [**Linux**](#linux)

## Windows

{% stepper %}
{% step %}

### Create configuration directory

1. Press **Win + R**
2. Type: `%USERPROFILE%`
3. Press **Enter** to open your home directory
   {% endstep %}

{% step %}

### Create `.claude` folder

1. In File Explorer, create new folder
2. Name it: `.claude`
3. You should now see the folder in `%USERPROFILE%\.claude`
   {% endstep %}

{% step %}

### Create MCP configuration file

1. Navigate into the `.claude` folder
2. Right-click in empty space → **New > Text Document**
3. Name it: `mcp.json`
4. Open with Notepad or VS Code
5. Paste the following:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

6. Save the file (Ctrl + S)
   {% endstep %}

{% step %}

### Create guidelines file

1. In the `.claude` folder, create new text document
2. Name it: `mcp-usage.md`
3. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
4. Save (Ctrl + S)
   {% endstep %}

{% step %}

### Restart Claude Code

Close and reopen Claude Code completely.

**File locations:**

* MCP config: `C:\Users\[YourUsername]\.claude\mcp.json`
* Guidelines: `C:\Users\[YourUsername]\.claude\mcp-usage.md`
  {% endstep %}
  {% endstepper %}

## macOS

{% stepper %}
{% step %}

### Create configuration directory

1. Open Terminal (**Cmd + Space**, type Terminal)
2. Run:

```sh
mkdir -p ~/.claude
```

{% endstep %}

{% step %}

### Create MCP configuration file

1. In Terminal, run:

```sh
nano ~/.claude/mcp.json
```

2. Paste the following:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

3. Save: Press `Ctrl + O`, then press Enter, then `Ctrl + X`
   {% endstep %}

{% step %}

### Create guidelines file

1. In Terminal, run:

```sh
nano ~/.claude/mcp-usage.md
```

2. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Verify files

```sh
ls -la ~/.claude/
```

You should see both `mcp.json` and `mcp-usage.md`
{% endstep %}

{% step %}

### Restart Claude Code

Close and reopen Claude Code.

**File locations:**

* MCP Config: `~/.claude/mcp.json`
* Guidelines: `~/.claude/mcp-usage.md`&#x20;
  {% endstep %}
  {% endstepper %}

## Linux

{% stepper %}
{% step %}

### Create configuration directory

1. Open Terminal
2. Run:

```sh
mkdir -p ~/.claude
```

{% endstep %}

{% step %}

### Create MCP configuration file

1. In Terminal, run:

```sh
nano ~/.claude/mcp.json
```

2. Paste:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Create guidelines file

1. In Terminal, run:

```sh
nano ~/.claude/mcp-usage.md
```

2. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Verify files

```sh
ls -la ~/.claude/
```

You should see both `mcp.json` and `mcp-usage.md`
{% endstep %}

{% step %}

### Restart Claude Code

Close and reopen Claude Code.

**File locations:**

* MCP Config: `~/.claude/mcp.json`
* Guidelines: `~/.claude/mcp-usage.md`
  {% endstep %}
  {% endstepper %}


# Guide for Cursor

Integrate Cursor with AI Architect for more accurate, codebase-aware AI assistance.

Use Bito's [**AI Architect**](https://docs.bito.ai/other-bito-ai-tools/ai-architect) with **Cursor** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Cursor can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Contact Bito support team at <support@bito.ai> to have your repositories indexed. You will get an **MCP server URL** and **Auth token** from Bito.
2. Download **BitoAIArchitectGuidelines.md** file. You will need to copy/paste the content from this file later when configuring AI Architect.

## Set up AI Architect

Follow the setup instructions for your operating system:

* [**Windows**](#windows)
* [**macOS**](#macos)
* [**Linux**](#linux)

## Windows

{% stepper %}
{% step %}

### Locate Cursor config directory

1. Press **Win + R**
2. Type: `%APPDATA%\Cursor`
3. Press Enter

If folder doesn't exist, run Cursor once to create it.
{% endstep %}

{% step %}

### Create/update MCP configuration

1. In `%APPDATA%\Cursor`, find or create: `cursor_desktop_config.json`
2. Open with Notepad or VS Code
3. Add or update the `mcpServers` section:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

4. Save
   {% endstep %}

{% step %}

### Create workspace guidelines file

1. In your project root, create: `.cursorrules`
2. Open with text editor
3. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
4. Save
   {% endstep %}

{% step %}

### Activate in Cursor

1. Open Cursor
2. Press `Ctrl + ,` (comma) to open Settings
3. Navigate to **Features > MCP** or **Developer > MCP**
4. Click **Refresh** button
5. You should see "BitoAIArchitect" listed
   {% endstep %}

{% step %}

### Restart Cursor

Close and reopen Cursor.

**File paths:**

* Global config: `C:\Users\[YourUsername]\AppData\Roaming\Cursor\cursor_desktop_config.json`
* Workspace guidelines: `[ProjectRoot]\.cursorrules`
  {% endstep %}
  {% endstepper %}

## macOS

{% stepper %}
{% step %}

### Create Cursor config directory

1. Open Terminal
2. Run:

```sh
mkdir -p ~/.cursor
```

{% endstep %}

{% step %}

### Create/update MCP configuration

1. Run:

```sh
nano ~/.cursor/cursor_desktop_config.json
```

2. Paste:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Create workspace guidelines file

1. In your project root, run:

```sh
nano .cursorrules
```

2. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Activate in Cursor

1. Open Cursor
2. Press `Cmd + ,` to open Settings
3. Navigate to **Features > MCP**
4. Click **Refresh** button
5. "BitoAIArchitect" should appear
   {% endstep %}

{% step %}

### Restart Cursor

Close and reopen Cursor.

**File paths:**

* Config: `~/.cursor/cursor_desktop_config.json`
* Workspace guidelines: `[ProjectRoot]/.cursorrules`
  {% endstep %}
  {% endstepper %}

## Linux

{% stepper %}
{% step %}

### Create Cursor config directory

1. Open Terminal
2. Run:

```sh
mkdir -p ~/.cursor
```

{% endstep %}

{% step %}

### Create/update MCP configuration

1. Run:

```sh
nano ~/.cursor/cursor_desktop_config.json
```

2. Paste:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Create workspace guidelines file

1. In your project root, run:

```sh
nano .cursorrules
```

2. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Activate in Cursor

1. Open Cursor
2. Press `Ctrl + ,` to open Settings
3. Navigate to **Features > MCP**
4. Click **Refresh** button
5. "BitoAIArchitect" should appear
   {% endstep %}

{% step %}

### Restart Cursor

Close and reopen Cursor.

**File paths:**

* Config: `~/.cursor/cursor_desktop_config.json`
* Workspace guidelines: `[ProjectRoot]/.cursorrules`
  {% endstep %}
  {% endstepper %}


# Guide for Windsurf

Integrate Windsurf with AI Architect for more accurate, codebase-aware AI assistance.

Use Bito's [**AI Architect**](https://docs.bito.ai/other-bito-ai-tools/ai-architect) with **Windsurf** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Windsurf can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Contact Bito support team at <support@bito.ai> to have your repositories indexed. You will get an **MCP server URL** and **Auth token** from Bito.
2. Download **BitoAIArchitectGuidelines.md** file. You will need to copy/paste the content from this file later when configuring AI Architect.

## Set up AI Architect

Follow the setup instructions for your operating system:

* [**Windows**](#windows)
* [**macOS**](#macos)
* [**Linux**](#linux)

## Windows

{% stepper %}
{% step %}

### Create Windsurf config directory

1. Press **Win + R**
2. Type: `%USERPROFILE%\.codeium\windsurf`
3. Press **Enter**

If the folder doesn't exist:

1. Navigate to: `%USERPROFILE%\.codeium`
2. Create new folder: `windsurf`
   {% endstep %}

{% step %}

### Create MCP configuration file

1. In the `windsurf` folder, create: `mcp_config.json`
2. Open with Notepad or VS Code
3. Paste:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

4. Save
   {% endstep %}

{% step %}

### Create workspace instructions file

1. In your project root, create folder: `.windsurf`
2. Inside `.windsurf`, create: `instructions.md`
3. Open with text editor
4. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
5. Save
   {% endstep %}

{% step %}

### Activate in Windsurf

1. Open Windsurf
2. Click **Settings** (gear icon)
3. Navigate to **Cascade > Model Context Protocol (MCP) Servers**
4. You should see "BitoAIArchitect" listed
5. Click **Refresh** if needed
   {% endstep %}

{% step %}

### Restart Windsurf

Close and reopen Windsurf.

**File paths:**

* Global config: `C:\Users\[YourUsername]\.codeium\windsurf\mcp_config.json`
* Workspace instructions: `[ProjectRoot]\.windsurf\instructions.md`
  {% endstep %}
  {% endstepper %}

## macOS

{% stepper %}
{% step %}

### Create Windsurf config directory

1. Open Terminal
2. Run:

```sh
mkdir -p ~/.codeium/windsurf
```

{% endstep %}

{% step %}

### Create MCP configuration file

1. Run:

```sh
nano ~/.codeium/windsurf/mcp_config.json
```

2. Paste:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Create workspace instructions file

1. In your project root, run:

```sh
mkdir -p .windsurf
```

```sh
nano .windsurf/instructions.md
```

2. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Activate in Windsurf

1. Open Windsurf
2. Click **Settings**
3. Navigate to **Cascade > Model Context Protocol (MCP) Servers**
4. Click **Refresh** to load changes
5. "BitoAIArchitect" should appear
   {% endstep %}

{% step %}

### Restart Windsurf

Close and reopen Windsurf.

**File paths:**

* Config: `~/.codeium/windsurf/mcp_config.json`
* Workspace instructions: `[ProjectRoot]/.windsurf/instructions.md`
  {% endstep %}
  {% endstepper %}

## Linux

{% stepper %}
{% step %}

### Create Windsurf config directory

1. Open Terminal
2. Run:

```sh
mkdir -p ~/.codeium/windsurf
```

{% endstep %}

{% step %}

### Create MCP configuration file

1. Run:

```sh
nano ~/.codeium/windsurf/mcp_config.json
```

2. Paste:

```json
{
  "mcpServers": {
    "Bito": {
      "transport": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Create workspace instructions file

1. In your project root, run:

```sh
mkdir -p .windsurf
```

```sh
nano .windsurf/instructions.md
```

2. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
3. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### Activate in Windsurf

1. Open Windsurf
2. Click **Settings**
3. Navigate to **Cascade > Model Context Protocol (MCP) Servers**
4. Click **Refresh**
5. "BitoAIArchitect" should appear
   {% endstep %}

{% step %}

### Restart Windsurf

Close and reopen Windsurf.

**File paths:**

* Config: `~/.codeium/windsurf/mcp_config.json`
* Workspace instructions: `[ProjectRoot]/.windsurf/instructions.md`
  {% endstep %}
  {% endstepper %}


# Guide for GitHub Copilot (VS Code)

Integrate GitHub Copilot in VS Code with AI Architect for more accurate, codebase-aware AI assistance.

Use Bito's [**AI Architect**](https://docs.bito.ai/other-bito-ai-tools/ai-architect) with **GitHub Copilot in VS Code** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), GitHub Copilot can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Contact Bito support team at <support@bito.ai> to have your repositories indexed. You will get an **MCP server URL** and **Auth token** from Bito.
2. Download **BitoAIArchitectGuidelines.md** file. You will need to copy/paste the content from this file later when configuring AI Architect.
3. Requires Visual Studio Code version 1.99 or later (check with `code --version`)
4. GitHub Copilot extension installed and enabled
5. GitHub account with Copilot access

## Set up AI Architect

Follow the setup instructions for your operating system:

* [**Windows**](#windows)
* [**macOS**](#macos)
* [**Linux**](#linux)

## Windows

{% stepper %}
{% step %}

### Ensure VS Code is up to date

1. Open VS Code
2. Go to **Help > Check for Updates**
3. Install any available updates
4. Verify version: Open terminal and run `code --version`
   {% endstep %}

{% step %}

### Enable Agent mode

1. Press `Ctrl + ,` to open Settings
2. In the search bar, type: `chat.agent.enabled`
3. Check the box to enable **Chat: Agent Enabled**
   {% endstep %}

{% step %}

### Choose configuration method

You have two options:

**Option A: Workspace configuration (recommended for team projects)**

* Location: `[ProjectRoot]\.vscode\mcp.json`
* Shared with team via version control
* Project-specific

**Option B: User configuration (personal, all workspaces)**

* Location: `%APPDATA%\Code\User\settings.json`
* Only available to you across all projects
* Global configuration
  {% endstep %}

{% step %}

### Workspace configuration (Option A)

1. In your project root, create folder: `.vscode`
2. Inside `.vscode`, create file: `mcp.json`
3. Open with VS Code or Notepad
4. Paste:

```sh
{
  "servers": {
    "Bito": {
      "type": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

5. Save the file (Ctrl + S)
   {% endstep %}

{% step %}

### User configuration (Option B) (Alternative)

1. Press `Ctrl + Shift + P` to open Command Palette
2. Type: `Preferences: Open User Settings (JSON)`
3. Press Enter
4. Add this configuration to your settings.json:

```json
{
  "mcp": {
    "servers": {
      "Bito": {
        "type": "http",
        "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
        "headers": {
          "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "timeout": 60000,
        "disabled": false
      }
    }
  }
}
```

{% hint style="info" %}
**Note:** If settings.json already has content, make sure to add the `"mcp"` section properly within the existing JSON structure.
{% endhint %}

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

5. Save (Ctrl + S)
   {% endstep %}

{% step %}

### Start the MCP server

1. If using workspace config, open `.vscode/mcp.json` in VS Code
2. A **Start** button will appear above the configuration in the editor
3. Click **Start** to activate the server
4. Wait for confirmation that the server has started
   {% endstep %}

{% step %}

### Verify setup

1. Open GitHub Copilot Chat (Ctrl + Alt + I)
2. Click the dropdown at the bottom and select **Agent** mode
3. Click the **Tools** icon (wrench symbol) in the chat interface
4. Verify "BitoAIArchitect" appears in the list of available tools
5. You should see the available tools from the BitoAIArchitect MCP server
   {% endstep %}

{% step %}

### Optional - Add project guidelines

1. In your project root, create folder: `.github`
2. Inside `.github`, create file: `copilot-instructions.md`
3. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
4. Save the file

**File paths:**

* Workspace config: `[ProjectRoot]\.vscode\mcp.json`
* User config: `C:\Users\[YourUsername]\AppData\Roaming\Code\User\settings.json`
* Guidelines (optional): `[ProjectRoot]\.github\copilot-instructions.md`&#x20;
  {% endstep %}
  {% endstepper %}

## macOS

{% stepper %}
{% step %}

### Ensure VS Code is up to date

1. Open VS Code
2. Go to **Code > Check for Updates** (or **Help > Check for Updates**)
3. Install any available updates
4. Verify version in Terminal: `code --version`
   {% endstep %}

{% step %}

### Enable Agent mode

1. Press `Cmd + ,` to open Settings
2. In the search bar, type: `chat.agent.enabled`
3. Check the box to enable **Chat: Agent Enabled**
   {% endstep %}

{% step %}

### Choose configuration method

**Option A: Workspace configuration (recommended for team projects)**

* Location: `[ProjectRoot]/.vscode/mcp.json`
* Shared with team, project-specific

**Option B: User configuration (personal, all workspaces)**

* Location: `~/Library/Application Support/Code/User/settings.json`
* Global across all projects
  {% endstep %}

{% step %}

### Workspace configuration (Option A)

1. In Terminal, navigate to your project root
2. Run:

```sh
mkdir -p .vscode
```

```sh
nano .vscode/mcp.json
```

3. Paste:

```json
{
  "servers": {
    "Bito": {
      "type": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

4. Save: `Ctrl + O`, Enter, `Ctrl + X`
   {% endstep %}

{% step %}

### User configuration (Option B) (Alternative)

1. Press `Cmd + Shift + P` to open Command Palette
2. Type: `Preferences: Open User Settings (JSON)`
3. Press Enter
4. Add this configuration to your settings.json:

```json
{
  "mcp": {
    "servers": {
      "Bito": {
        "type": "http",
        "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
        "headers": {
          "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "timeout": 60000,
        "disabled": false
      }
    }
  }
}
```

{% hint style="info" %}
**Note:** If settings.json already has content, make sure to add the `"mcp"` section properly within the existing JSON structure.
{% endhint %}

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

5. Save: `Cmd + S`
   {% endstep %}

{% step %}

### Start the MCP server

1. Open the mcp.json file in VS Code
2. Click **Start** button that appears above the configuration
3. Wait for server to activate
   {% endstep %}

{% step %}

### Verify setup

1. Open Copilot Chat (`Cmd + Alt + I` or `Cmd + Shift + I`)
2. Select **Agent** mode from the dropdown
3. Click **Tools** icon to view available tools
4. Verify "BitoAIArchitect" is listed
   {% endstep %}

{% step %}

### Optional - Add project guidelines

```sh
mkdir -p .github
```

```sh
nano .github/copilot-instructions.md
```

Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file

**File paths:**

* Workspace: `[ProjectRoot]/.vscode/mcp.json`
* User: `~/Library/Application Support/Code/User/settings.json`
* Guidelines: `[ProjectRoot]/.github/copilot-instructions.md`&#x20;
  {% endstep %}
  {% endstepper %}

## Linux

{% stepper %}
{% step %}

### Ensure VS Code is up to date

1. Open VS Code
2. Go to **Help > Check for Updates**
3. Install updates if available
4. Verify: `code --version` in terminal
   {% endstep %}

{% step %}

### Enable Agent mode

1. Press `Ctrl + ,` to open Settings
2. Search: `chat.agent.enabled`
3. Enable **Chat: Agent Enabled**
   {% endstep %}

{% step %}

### Choose configuration method

**Option A: Workspace** - `[ProjectRoot]/.vscode/mcp.json` (recommended)

**Option B: User** - `~/.config/Code/User/settings.json` (global)
{% endstep %}

{% step %}

### Workspace configuration (Option A)

```sh
mkdir -p .vscode
```

```sh
nano .vscode/mcp.json
```

Paste:

```json
{
  "servers": {
    "Bito": {
      "type": "http",
      "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
      "headers": {
        "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "timeout": 60000,
      "disabled": false
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

Save: `Ctrl + O`, Enter, `Ctrl + X`
{% endstep %}

{% step %}

### User configuration (Option B) (Alternative)

1. Press `Ctrl + Shift + P`
2. Type: `Preferences: Open User Settings (JSON)`
3. Add to settings.json:

```json
{
  "mcp": {
    "servers": {
      "Bito": {
        "type": "http",
        "url": "Enter_MCP_Server_URL_Here", // e.g. "https://mcp.bito.ai/123456/mcp"
        "headers": {
          "Authorization": "Enter_Auth_Token_Here" // e.g. "Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "timeout": 60000,
        "disabled": false
      }
    }
  }
}
```

{% hint style="info" %}
**Note:** If settings.json already has content, make sure to add the `"mcp"` section properly within the existing JSON structure.
{% endhint %}

{% hint style="info" %}
**Note:**

* Replace the text **`Enter_MCP_Server_URL_Here`** with the actual MCP server URL.
* Replace the text **`Enter_Auth_Token_Here`** with the actual auth token.
  {% endhint %}

5. Save: `Ctrl + S`
   {% endstep %}

{% step %}

### Start server & verify

1. Open mcp.json in VS Code, click **Start** button
2. Open Copilot Chat (`Ctrl + Alt + I`)
3. Select **Agent** mode
4. Click **Tools** icon to verify "BitoAIArchitect" is listed
   {% endstep %}

{% step %}

### Optional - Add guidelines

1. In Terminal, run:

```sh
mkdir -p .github
```

```sh
nano .github/copilot-instructions.md
```

2. Copy and paste ALL contents of `BitoAIArchitectGuidelines.md` into this file
3. Save: `Ctrl + O`, Enter, `Ctrl + X`

**File paths:**

* Workspace: `[ProjectRoot]/.vscode/mcp.json`
* User: `~/.config/Code/User/settings.json`
* Guidelines: `[ProjectRoot]/.github/copilot-instructions.md`
  {% endstep %}
  {% endstepper %}


# AI Code Review Agent (with AI Architect vs without AI Architect)

From single-repo reviews to system-wide insights

The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) becomes significantly more powerful when paired with [**AI Architect**](https://docs.bito.ai/other-bito-ai-tools/ai-architect).

Below is a clear explanation of how the agent behaves in each setup and why AI Architect unlocks much deeper, system-level insights.

## AI Code Review Agent without AI Architect

The standard AI Code Review Agent analyzes code at the **repository level**.

It creates a ***within-repo knowledge graph*** by building:

* Abstract Syntax Trees (ASTs)
* Symbol indexes
* Local dependency relationships

This allows it to perform strong, context-aware code reviews **within a single repository**, including:

* Identifying issues in the diff
* Understanding dependencies inside the repo
* Checking for consistency and correctness within that project
* Suggesting improvements based on local patterns

However, the agent’s visibility stops at the repository boundary. It cannot detect effects on other services or codebases.

## AI Code Review Agent powered by AI Architect

When **AI Architect** is enabled, the **AI Code Review Agent** gains a **complete view of your entire engineering ecosystem**.

AI Architect builds a **cross-repository knowledge graph** that maps:

* All services
* Shared libraries
* Modules and components
* Inter-service dependencies
* Upstream and downstream call chains

With this system-level understanding, the agent can perform much deeper analysis.

#### **Key capabilities unlocked by AI Architect**

**1. Cross-repository awareness**

The agent understands how code in one repo interacts with code in others — crucial for microservices and distributed systems.

**2. Cross-repo impact analysis**

During a pull request review, the agent can identify:

* What breaks downstream if you change an interface
* Which services call the function you updated
* Which teams or repos depend on your changes
* Whether the update introduces architecture-wide risks

**3. Architecture-level checks**

The agent evaluates your changes not just for correctness, but for their alignment with the overall system design.

**4. Early problem detection across the entire codebase**

Ripple effects, breaking changes, or dependency violations that traditionally appear only in staging or after deployment can now be flagged directly during review.

***

### **Side-by-side comparison**

| Capability                  | Without AI Architect | With AI Architect                 |
| --------------------------- | -------------------- | --------------------------------- |
| Scope                       | Single repository    | Entire system (multi-repo)        |
| Knowledge graph             | Repo-only            | Cross-repository, system-wide     |
| AST + symbol analysis       | ✅                    | ✅ (plus cross-repo linking)       |
| Dependency visibility       | Local to repo        | Full call chains across repos     |
| Impact analysis             | Local only           | Upstream + downstream, multi-repo |
| Architecture checks         | Limited              | System-level validation           |
| Ripple-effect detection     | ❌                    | ✅                                 |
| Multi-service understanding | ❌                    | ✅                                 |


# Bito CLI

Command Line Interface (Powered by Bito AI Chat) to Automate Your Tasks

{% embed url="<https://www.youtube.com/watch?v=3dkg7oOSELQ>" %}

<table data-view="cards"><thead><tr><th data-type="content-ref"></th><th></th></tr></thead><tbody><tr><td><a href="bito-cli/overview">overview</a></td><td>Bito CLI (Command Line Interface)</td></tr><tr><td><a href="bito-cli/install-or-uninstall">install-or-uninstall</a></td><td>Learn how to setup Bito CLI on your device (Mac, Linux, and Windows)</td></tr><tr><td><a href="bito-cli/configuration">configuration</a></td><td>Manage Bito CLI settings</td></tr><tr><td><a href="bito-cli/how-to-use">how-to-use</a></td><td>Learn how to work with Bito CLI (including examples)</td></tr><tr><td><a href="bito-cli/available-commands">available-commands</a></td><td>Learn about all the powerful commands to use Bito CLI</td></tr><tr><td><a href="bito-cli/faqs">faqs</a></td><td>Answers to popular questions</td></tr></tbody></table>


# Overview

Bito CLI (Command Line Interface)

{% embed url="<https://www.youtube.com/watch?v=3dkg7oOSELQ>" %}

[Bito CLI (Command Line Interface)](https://github.com/gitbito/CLI) is an innovative tool that harnesses the power of [Bito AI chat](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito) functionality to automate software development workflows. It can automate repetitive tasks like software documentation, test case generation, pull request review, release notes generation, writing commit message or pull request description, and much more.

For example, you can run a command like `bito –p writedocprompt.txt -f mycode.js` for non-interactive mode in Bito CLI (where `writedocprompt.txt` will contain your prompt text such as `Explain the code below in brief` and `mycode.js` will contain the actual code on which the action is to be performed).

{% hint style="info" %}
Here is the complete list of [**available commands for Bito CLI**](https://docs.bito.ai/other-bito-ai-tools/bito-cli/available-commands).
{% endhint %}

**Download Bito CLI from GitHub:**

{% embed url="<https://github.com/gitbito/CLI>" %}

With support for 50+ programming languages (Python, JavaScript, SQL, etc.) and 50+ spoken languages (English, German, Chinese, etc.), Bito CLI is versatile and adaptable to different project needs. Furthermore, it's designed to be compatible across multiple operating systems, including Windows, Mac, and Linux, ensuring a wide range of usability.&#x20;

You can either use "ADVANCED" AI models like GPT-4o, Claude Sonnet 3.5, and best in class AI models, or "BASIC" AI models like GPT-4o mini and similar models inside Bito CLI.&#x20;

When using Basic AI models, your prompts and the chat's memory are limited to 40,000 characters (about 18 single-spaced pages). However, with Advanced AI models, your prompts and the chat memory can go up to 240,000 characters (about 110 single-spaced pages). This means that Advanced models can process your entire code files, leading to more accurate answers.&#x20;

If you are seeking the best results for complex tasks, then choose Advanced AI models.

{% hint style="info" %}
Access to Advanced AI models is only available in Bito's [**Team Plan**](https://bito.ai/pricing/). However, Basic AI models can be used by both free and paid users.
{% endhint %}

Bito CLI is an invaluable asset for developers looking to increase efficiency and productivity in their workflows. It allows developers to save time and focus on more complex and creative aspects of their work. Additionally, Bito CLI plays a crucial role in supporting continuous integration and deployment (CI/CD) processes. Explore some [intelligent AI automations](https://github.com/gitbito/AI-Automation) we've created using Bito CLI, which you can implement in your projects right now. These automations showcase the powerful capabilities of Bito CLI.&#x20;

To get started, check out our guide on [how to use Bito CLI](https://docs.bito.ai/other-bito-ai-tools/bito-cli/how-to-use), ensuring you make the most out of it.&#x20;


# Install or uninstall

Learn how to setup Bito CLI on your device (Mac, Linux, and Windows)

## Installing Bito CLI (Recommended)&#x20;

We recommend you use the following methods to install Bito CLI.&#x20;

### Mac and Linux&#x20;

`sudo curl https://alpha.bito.ai/downloads/cli/install.sh -fsSL | bash`

**Note:** curl will always download the latest version.

#### Archlinux&#x20;

Arch and Arch based distro users can install it from [AUR](https://aur.archlinux.org/packages/bito-cli)&#x20;

`yay -S bito-cli`

or

`paru -S bito-cli`

**Note for the Mac Users:** You might face issues related to verification for which you will have to manually do the steps from [here](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) (we are working on fixing it as soon as possible).&#x20;

### Windows&#x20;

* In the [Bito CLI GitHub repo](https://github.com/gitbito/CLI), open the folder that has the latest version number.&#x20;
* From here, download the MSI file called `Bito CLI.exe` and then install Bito CLI using this installer.
* On Windows 11, you might get notification related to publisher verification. Click on "Show more" or "More info" and click on "Run anyway" (we are working on fixing this as soon as possible).&#x20;

{% hint style="info" %}
Once the installation is complete, start a new command prompt and run `bito` command to get started.&#x20;
{% endhint %}

## Installing with Manual Binary Download (Not Recommended)&#x20;

While it's not recommended, you can download the Bito CLI binary from our repository, and install it manually. The binary is available for Windows, Linux, and Mac OS (x86 and ARM architecture).&#x20;

### Mac and Linux&#x20;

1. In the [Bito CLI GitHub repo](https://github.com/gitbito/CLI), open the folder that has the latest version number.&#x20;
2. From here, download the Bito CLI binary specific to your OS platform.
3. Start the terminal, go to the location where you downloaded the binary, move the downloaded file (in the command below use bito-\* filename you have downloaded) to filename bito.

   `mv bito-<os>-<arch> bito`
4. Make the file executable using following command `chmod +x ./bito`
5. Copy the binary to `/usr/local/bin` using following command `sudo cp ./bito /usr/local/bin`&#x20;
6. Set PATH variable so that Bito CLI is always accessible. `PATH=$PATH:/usr/local/bin`&#x20;
7. Run Bito CLI with `bito` command. If PATH variable is not set, you will need to run command with the complete or relative path to the Bito executable binary.

### Windows&#x20;

1. In the [Bito CLI GitHub repo](https://github.com/gitbito/CLI), open the folder that has the latest version number.&#x20;
2. From here, download the Bito CLI binary for Windows called `bito.exe`.&#x20;
3. For using Bito CLI, always move to the directory containing Bito CLI prior to running it.
4. Set PATH variable so that Bito CLI is always accessible.&#x20;
   1. Follow the instructions as per this [link](https://share.bito.co/static/share?aid=02f4506f-1208-4d97-bb1d-96f3b4a1a017)&#x20;
   2. Edit the "Path" variable and add a new path of the location where Bito CLI is installed on your machine. &#x20;

## Uninstalling Bito CLI&#x20;

### Mac and Linux&#x20;

`sudo curl https://alpha.bito.ai/downloads/cli/uninstall.sh -fsSL | bash`

**Note:** This will completely uninstall Bito CLI and all of its components.

### Windows&#x20;

For Windows, you can uninstall Bito CLI just like you uninstall any other software from the control panel. You can follow these steps:&#x20;

1. Click on the Windows Start button and type "control panel" in the search box, and then open the Control Panel app.&#x20;
2. Under the "Programs" option, click on "Uninstall a program".&#x20;
3. Find "Bito CLI" in the list of installed programs and click on it.&#x20;
4. Click on the "Uninstall" button (given at the top) to start the uninstallation process.&#x20;
5. Follow the instructions provided by the uninstall wizard to complete the uninstallation process.

After completing these steps, Bito CLI should be completely removed from your Windows machine.&#x20;


# Configuration

Manage Bito CLI settings

## bito config \[flags]&#x20;

* run `bito config -l` or `bito config --list` to list all config variables and values.&#x20;
* run `bito config -e` or `bito config --edit` to open the config file in default editor.&#x20;

## Sample Configuration&#x20;

```
bito:
 access_key: ""
 email: first.last@mycompany.com
 
 preferred_ai_model: ADVANCED
settings:
 auto_update: true
 max_context_entries: 20
```

## What is an Access Key and How to Get it?&#x20;

[**Access Key**](https://docs.bito.ai/help/account-and-settings/access-key) is an alternate authentication mechanism to Email & OTP based authentication. You can use an Access Key in Bito CLI to access various functionalities such as **Bito AI Chat**. Here’s a guide on [how to create an Access Key](https://docs.bito.ai/help/account-and-settings/access-key). Basically, after creating the Access Key, you have to use it in the config file mentioned above. For example, `access_key: “YOUR_ACCESS_KEY_HERE”`&#x20;

Access Key can be persisted in Bito CLI by adding it in the config file using `bito config -e`. Such persisted Access Key can be over-ridden by running `bito -k <access-key>` or `bito --key <access-key>` for the transient session (sessions that last only for a short time).&#x20;

## Preferred AI Model Type&#x20;

By default AI Model Type is set to `ADVANCED` and it can be overridden by running `bito -m <BASIC/ADVANCED>`. Model type is used for AI query in the current session. Model type can be set to `BASIC` or `ADVANCED`, which is case insensitive.&#x20;

"ADVANCED" refers to AI models like GPT-4o, Claude Sonnet 3.5, and best in class AI models, while "BASIC" refers to AI models like GPT-4o mini and similar models.&#x20;

When using Basic AI models, your prompts and the chat's memory are limited to 40,000 characters (about 18 single-spaced pages). However, with Advanced AI models, your prompts and the chat memory can go up to 240,000 characters (about 110 single-spaced pages). This means that Advanced models can process your entire code files, leading to more accurate answers.&#x20;

If you are seeking the best results for complex tasks, then choose Advanced AI models.&#x20;

{% hint style="info" %}
Access to Advanced AI models is only available in Bito's [**Team Plan**](https://bito.ai/pricing/). However, Basic AI models can be used by both free and paid users.
{% endhint %}

To see how many Advanced AI requests you have left, please visit the [Requests Usage](https://alpha.bito.ai/home/settings/bito-premium/request-usage) page. On this page, you can also set [hard and soft limits](https://docs.bito.ai/billing-and-plans/advanced-ai-requests-usage#hard-and-soft-limits) to control usage of Advanced AI model requests for your workspace and avoid unexpected expenses.&#x20;

Also note that even if you have set `preferred_ai_model: ADVANCED` in Bito CLI config but your Advanced AI model requests quota is finished (or your self-imposed [hard limit](https://docs.bito.ai/billing-and-plans/advanced-ai-requests-usage#what-is-the-hard-limit) is reached) then Bito CLI will start using Basic AI models instead of Advanced AI models.&#x20;


# How to use?

Learn how to work with Bito CLI (including examples)

## Prerequisites&#x20;

Terminal&#x20;

* Bash (for Mac and Linux)&#x20;
* CMD (for Windows)&#x20;

## Using Bito CLI&#x20;

Before you can use Bito CLI, you need to [install](https://docs.bito.ai/other-bito-ai-tools/bito-cli/install-or-uninstall) and [configure](https://docs.bito.ai/other-bito-ai-tools/bito-cli/configuration) it. Once the setup is done, follow the steps below:&#x20;

* **Execute Chat:** Run `bito` command on command prompt to get started. Ask anything you want help with such as `awk command to print first and last column`.&#x20;
* **Note:** Bito CLI supports long prompts through multiline input. To complete and submit the prompt, press `Ctrl+D`. `Enter/Return` key adds a new line to the input.&#x20;
* Exit Bito CLI: To quit/exit from Bito CLI, type `quit` and press `Ctrl+D` .&#x20;
* Terminate: Press `Ctrl+C` to terminate Bito CLI.&#x20;

{% hint style="info" %}
Here is the complete list of [**available commands for Bito CLI**](https://docs.bito.ai/other-bito-ai-tools/bito-cli/available-commands).
{% endhint %}

## Getting Started&#x20;

Check out the video below to get started with Bito CLI.

{% embed url="<https://youtu.be/3dkg7oOSELQ>" %}

## Examples&#x20;

Here are two examples for you to see My Prompt in action:&#x20;

1. How to Create Git Commit Messages and Markdown Documentation with Ease using Bito CLI My Prompt:&#x20;

{% embed url="<https://www.youtube.com/watch?v=q42hqwT-jsg>" %}

2. How to generate test data using Bito CLI My Prompt:&#x20;

{% embed url="<https://www.youtube.com/watch?v=GYa0p511NUQ>" %}


# Available commands

Learn about all the powerful commands to use Bito CLI

## Help&#x20;

Run any one of the below commands.

`bito --help`

or

`bito config –help`

## Check Bito CLI Version&#x20;

Run any one of the below commands to print the version number of Bito CLI installed currently.

`bito -v`

or

`bito --version`

## Bito CLI MyPrompt (Automation using Bito CLI)&#x20;

The below commands can help you automate repetitive tasks like software documentation, test case generation, writing pull request description, pull request review, release notes generation, writing commit message, and much more.

{% hint style="info" %}
Explore some [**intelligent AI automations**](https://github.com/gitbito/AI-Automation) we've created using [**Bito CLI**](https://docs.bito.ai/other-bito-ai-tools/bito-cli), which you can implement in your projects right now. These automations showcase the powerful capabilities of Bito CLI.
{% endhint %}

### 1- Non-Interactive Mode with File Input&#x20;

Run the below command for non-interactive mode in Bito (where `writedocprompt.txt` will contain your prompt text such as `Explain the code below in brief` and `mycode.js` will contain the actual code on which the action is to be performed).&#x20;

```
bito –p writedocprompt.txt -f mycode.js
```

### 2- Standard Input Mode&#x20;

Run the below command to read the content at standard input in Bito (where `writedocprompt.txt` will contain your prompt text such as `Explain the code below in brief` and input provided will have the actual content on which the action is to be performed).&#x20;

```
bito –p writedocprompt.txt
```

### 3- Direct File Input&#x20;

Run the below command to directly concatenate a file and pipe it to `bito` and get instant result for your query.&#x20;

#### On Mac/Linux&#x20;

```
cat file.txt | bito
```

#### On Windows&#x20;

```
type file.txt | bito
```

### 4- Redirect Output to a File&#x20;

#### On Mac/Linux&#x20;

Run the below command to redirect your output directly to a file (where `-p` can be used along with `cat` to perform prompt related action on the given content).&#x20;

```
cat inventory.sql | bito -p testdataprompt.txt > testdata.sql
```

#### On Windows&#x20;

Run the below command to redirect your output directly to a file (where `-p` can be used along with `type` to perform prompt related action on the given content).&#x20;

```
type inventory.sql | bito -p testdataprompt.txt > testdata.sql
```

### 5- Store Context/Conversation History&#x20;

Run the below command to store context/conversation history in non-interactive mode in file `runcontext.txt` to use for next set of commands in case prior context is needed. If `runcontext.txt` is not present it will be created. Please provide a new file or an existing context file created by `bito` using `-c` option. With `-c` option now context is supported in non-interactive mode

#### On Mac/Linux&#x20;

```
cat inventory.sql | bito -c runcontext.txt -p testdataprompt.txt > testdata.sql
```

#### On Windows&#x20;

```
type inventory.sql | bito -c runcontext.txt -p testdataprompt.txt > testdata.sql
```

### 6- Instant Response for Queries&#x20;

Run the below command to instantly get response for your queries using Bito CLI.&#x20;

```
echo "give me code for bubble sort in python" | bito
```

## Using Comments&#x20;

Anything after `#` symbol in your prompt file will be considered as a comment by Bito CLI and won't be part of your prompt.&#x20;

You can use `\#` as an escape sequence to make `#` as a part of your prompt and to not use it for commenting anymore.&#x20;

### Few examples for above:&#x20;

* Give me an example of bubble sort in python # everything written here will be considered as a comment now.&#x20;
* Explain what this part of the code do: \\#include\<stdio.h>
  * In the example above `\#` can be used as an escape sequence to include # as a part of your prompt.&#x20;
* \#This will be considered as a comment as it contains # at the start of the line itself.&#x20;

## Using Macro&#x20;

Use `{{%input%}}` macro in the prompt file to refer to the contents of the file provided via `-f` option.

**Example:** To check if a file contains JS code or not, you can create a prompt file `checkifjscode.txt` with following prompt:&#x20;

```
Context is provided below within contextstart and contextend
contextstart
{{%input%}}
contextend
Check if content provided in context is JS code.
```


# FAQs

Answers to popular questions

## Enabling unicode For Windows 10 and below&#x20;

Unicode characters (using other languages) might not be readily supported on command prompt if you are on Windows 10 or below. You can run command `chcp 936` in cmd prior to using `bito` to support unicode characters in Windows 10 or below.

{% hint style="info" %}
If you are on Windows 11 then you shouldn't encounter any such issues.
{% endhint %}

## Using Homebrew for Bito CLI

1. Before using homebrew, please make sure that you uninstall any previously installed versions of Bito CLI using the [uninstall guide provided here](https://docs.bito.ai/other-bito-ai-tools/bito-cli/install-or-uninstall).&#x20;
2. Once above is done then you can use following commands to install Bito CLI using homebrew:
   1. First tap the CLI repo using `brew tap gitbito/bitocli` command, this should be a one time action and not required every time.
   2. Now you can install Bito CLI using following command:
      * `brew install bito-cli` - this should install Bito CLI based upon your machine architecture.
   3. To update Bito CLI to the latest version, use following commands:
      1. Please make sure you always do `brew update` before upgrading to avoid any errors.
      2. `brew update` - this will update all the required packages before upgrading.
      3. `brew upgrade bito-cli` - once above is done, this will update Bito CLI to the latest version.
   4. To uninstall Bito CLI you can either use the [uninstall guide from here](https://docs.bito.ai/other-bito-ai-tools/bito-cli/install-or-uninstall) or use following commands:
      * `brew uninstall bito-cli` - this should uninstall Bito CLI completely from your system.&#x20;


# Bito's AI stack

Learn About AI Technologies & Concepts Powering Bito

<table data-view="cards"><thead><tr><th data-type="content-ref"></th><th></th></tr></thead><tbody><tr><td><a href="bitos-ai-stack/embeddings">embeddings</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/vector-databases">vector-databases</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/indexing">indexing</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/generative-ai">generative-ai</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/large-language-models-llm">large-language-models-llm</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/llm-tokens">llm-tokens</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/llm-parameters">llm-parameters</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/retrieval-augmented-generation-rag">retrieval-augmented-generation-rag</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/prompts">prompts</a></td><td></td></tr><tr><td><a href="bitos-ai-stack/prompt-engineering">prompt-engineering</a></td><td></td></tr></tbody></table>


# Embeddings

Bito leverages the power of embeddings to [understand your entire codebase](https://docs.bito.ai/feature-guides/ai-that-understands-your-code). But WTF are these embeddings, and how do they help Bito understand your code?&#x20;

If you are curious to know, this guide is for you!&#x20;

## What is Embedding?

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FsFApPUNBNyvz2x8EtZnM%2Fembeddings.gif?alt=media&#x26;token=a336faca-fa2a-429e-9e0b-8b64a86f681f" alt=""><figcaption></figcaption></figure>

Embeddings, at their essence, are like magic translators. They convert data—whether words, images, or, in Bito's case, code—into vectors in a dense numerical space. These vectors encapsulate meaning or semantics. Basically, these vectors help computers understand and work with data more efficiently.&#x20;

Imagine an embedding as a vector (list) of floating-point numbers. If two vectors are close, they're similar. If they're far apart, they're different. Simple as that!&#x20;

{% hint style="info" %}
**A vector embedding looks something like this:** \[0.02362240, -0.01716885, 0.00493248, ..., 0.01665339]
{% endhint %}

## Why Embeddings?&#x20;

In this section, we'll explore the most common and impactful ways embeddings are used in everyday tech and applications.&#x20;

**Word Similarity & Semantics:** Word embeddings, like Word2Vec, map words to vectors such that semantically similar words are closer in the vector space. This allows algorithms to discern synonyms, antonyms, and more based on their vector representations.&#x20;

**Sentiment Analysis:** By converting text into embeddings, machine learning models can be trained to detect and classify the sentiment of a text, such as determining if a product review is positive or negative.&#x20;

**Recommendation Systems:** Embeddings can represent items (like movies, books, or products) and users. By comparing these embeddings, recommendation systems can suggest items similar to a user's preferences. For example, by converting audio or video data into embeddings, systems can recommend content based on similarity in the embedded space, leading to personalized user recommendations.&#x20;

**Document Clustering & Categorization:** Text documents can be turned into embeddings using models like Doc2Vec. These embeddings can then be used to cluster or categorize documents based on their content.&#x20;

**Translation & Language Models:** Models like BERT and GPT use embeddings to understand the context within sentences. This contextual understanding aids in tasks like translation and text generation.&#x20;

**Image Recognition:** Images can be converted into embeddings using convolutional neural networks (CNNs). These embeddings can then be used to recognize and classify objects within the images.&#x20;

**Anomaly Detection:** By converting data points into embeddings, algorithms can identify outliers or anomalies by measuring the distance between data points in the embedded space.&#x20;

**Chatbots & Virtual Assistants:** Conversational models turn user inputs into embeddings to understand intent and context, enabling more natural and relevant responses.&#x20;

**Search Engines:** Text queries can be converted into embeddings, which are then used to find relevant documents or information in a database by comparing embeddings.

## Let’s look at an example&#x20;

Suppose you have two functions in your codebase:&#x20;

**Function # 1:**&#x20;

```python
def add(x, y):
    return x + y
```

**Function # 2:**&#x20;

```python
def subtract(x, y):
    return x - y
```

Using embeddings, Bito might convert these functions into two vectors. Because these functions perform different operations, their embeddings would be at a certain distance apart. Now, if you had another function that also performed addition but with a slight variation, its embedding would be closer to the `add` function than the `subtract` function.&#x20;

Let's oversimplify and imagine these embeddings visually:&#x20;

**Embedding for Function # 1 (add):**&#x20;

\[0.9, 0.2, 0.1]

**Embedding for Function # 2 (subtract):**&#x20;

\[0.2, 0.9, 0.1]

Notice the numbers? The first positions in these lists are quite different: **0.9** for addition and **0.2** for subtraction. This difference signifies the varied operations these functions perform.&#x20;

Now, let's add a twist. Suppose you wrote another addition function, but with an extra print statement:

**Function # 3:**&#x20;

```python
def add_and_print(x, y):
    result = x + y
    print(result)
    return result
```

**Bito might give an embedding like:**&#x20;

\[0.85, 0.3, 0.15]

If you compare, this new list is more similar to the `add` function's list than the `subtract` one, especially in the first position. But it's not exactly the same as the pure `add` function because of the added print operation.&#x20;

This distance or difference between lists is what Bito uses to determine how similar functions or chunks of code are to one another. So, when you ask Bito about a piece of code, it quickly checks these number lists, finds the closest match, and guides you accordingly!&#x20;

## How Bito Uses Embeddings&#x20;

When you ask Bito a question or seek assistance with a certain piece of code, Bito doesn't read the code the way we do. Instead, it refers to these vector representations (embeddings). By doing so, it can quickly find related pieces of code in your repository or understand the essence of your query.&#x20;

For example, if you ask Bito, "Where did I implement addition logic?", Bito will convert your question into an embedding and then look for the most related (or closest) embeddings in its index. Since it already knows the `add` function's embedding represents addition, it can swiftly point you to that function.

## Models for Generating Embeddings&#x20;

When we talk about turning data into these nifty lists of numbers (embeddings), several models and techniques come into play. These models have been designed to extract meaningful patterns from vast amounts of data and represent them as compact vectors. Here are some of the standout models:&#x20;

**Word2Vec:** One of the pioneers in the world of embeddings, this model, developed by researchers at Google, primarily focuses on words. Given a large amount of text, Word2Vec can produce a vector for each word, capturing its context and meaning.&#x20;

**Doc2Vec:** An extension of Word2Vec, this model is designed to represent entire documents or paragraphs as vectors, making it suitable for larger chunks of text.&#x20;

**GloVe (Global Vectors for Word Representation):** Developed by Stanford, GloVe is another method to generate word embeddings. It stands out because it combines both global statistical information and local semantic details from a text.&#x20;

**BERT (Bidirectional Encoder Representations from Transformers):** A more recent and advanced model from Google, BERT captures context from both left and right (hence, bidirectional) of a word in all layers. This deep understanding allows for more accurate embeddings, especially in complex linguistic scenarios.&#x20;

**FastText:** Developed by Facebook’s AI Research lab, FastText enhances Word2Vec by considering sub-words. This means it can generate embeddings even for misspelled words or words not seen during training by breaking them into smaller chunks.&#x20;

**ELMo (Embeddings from Language Models):** This model dynamically generates embeddings based on the context in which words appear, allowing for richer representations.&#x20;

**Universal Sentence Encoder:** This model, developed by Google, is designed to embed entire sentences, making it especially useful for tasks that deal with larger text chunks or require understanding the nuances of entire sentences.&#x20;

**GPT (Generative Pre-trained Transformer):** Developed by OpenAI, GPT is a series of models (from GPT-1 to GPT-4o) that use the Transformer architecture to generate text. While GPT models are famous for generating text, they can also produce vector embeddings. Their latest embeddings model is **text-embedding-ada-002** which can generate embeddings for text search, code search, sentence similarity, and text classification tasks.&#x20;

{% hint style="info" %}
Bito uses **text-embedding-ada-002** from **OpenAI** and we’re also trying out some open-source embedding models for our [AI that Understands Your Code](https://docs.bito.ai/feature-guides/ai-that-understands-your-code) feature.
{% endhint %}

These models, among many others, power a wide range of applications, from natural language processing tasks like sentiment analysis and machine translation to aiding assistants like Bito in understanding and processing code or any other form of data.

## Embeddings: More Than Just Numbers&#x20;

While embeddings might seem like just another technical term or a mere list of numbers, they are crucial bridges that connect human logic and machine understanding. The ability to convert complex data, be it code, images, or even human language, into such vectors, and then use the 'distance' between these vectors to find relatedness, is nothing short of magic.&#x20;

In the context of Bito, embeddings aren't just a feature—it's the core that powers its deep understanding of your code, making it an indispensable tool for developers. So, the next time you think of Bito's answers as magical, remember, it's the power of embeddings at work!&#x20;


# Vector databases

Think of a huge, never-ending stream of information like photos, tweets, and songs pouring in every second. We need special storage boxes to keep all this info organized and find what we need quickly. One of the new, cool storage boxes people are talking about is called a **“Vector Database”**. So, what's this Vector Database thing, and why is it something you might want to know about? Let's unwrap this mystery and make it super easy to understand.&#x20;

## What is a Vector Database?&#x20;

A vector database is designed to handle vectorized data - that is, data represented as vectors. A vector, in this context, is a mathematical construct that embeds information into a high-dimensional space, with each dimension representing a different feature of the data.&#x20;

Traditionally, databases have been adept at handling structured data (like rows and columns in a spreadsheet) or even semi-structured data (like JSON documents). However, with the rise of machine learning and artificial intelligence, there is an increasing need to efficiently store and query data that isn't just numbers or text but is represented in multi-dimensional space.&#x20;

Vector database fills this gap by excelling at managing and querying data in the form of vectors. This is particularly useful for tasks that involve similarity search, like finding the most similar images, text, or even audio clips, in a process known as **"nearest neighbor search"**.&#x20;

## Why are Vector Databases Important?&#x20;

Imagine trying to search for a song that sounds like another song or finding images that are visually similar to a given image. These tasks are non-trivial because they involve understanding the content at a deeper, more abstract level. Vector databases allow us to convert these abstract, complex features into a mathematical space where 'similarity' can be computed and searched efficiently.&#x20;

For instance, in the world of machine learning, models like neural networks can convert images or text into vectors during their processing stages. These vectors, known as [**embeddings**](https://docs.bito.ai/help/bitos-ai-stack/embeddings), capture the essence of the data. When you query a vector database with another vector, it retrieves the most similar items based on the vector's position and distance in that high-dimensional space.&#x20;

## Key Features of Vector Databases&#x20;

**Efficient Similarity Search:** They use specialized indexing and search algorithms to perform fast and efficient **nearest neighbor searches**.&#x20;

**Scalability:** They are designed to handle large volumes of data and high-dimensional vectors without sacrificing performance.&#x20;

**Machine Learning Integration:** They are often integrated with machine learning models and pipelines to enable real-time embedding and querying.&#x20;

**Language Agnosticism:** Vector databases can handle any data that can be vectorized, whether it's images, text, audio, or any other form of media.&#x20;

## Real-World Applications&#x20;

**Recommendation Systems:** Vector databases can power recommendation engines that suggest products, movies, or songs by finding items that are similar to a user’s past behavior.&#x20;

**Image Retrieval:** They are used in image search engines to find images that are visually similar to a query image.&#x20;

**Natural Language Processing:** In the field of NLP, vector databases enable searching through large corpora of text for documents or entries that are contextually similar to a given piece of text.&#x20;

**Fraud Detection:** They can be used to detect anomalies or patterns in transaction data that signify fraudulent activity by comparing against typical transaction vectors.&#x20;

## Best Free, Paid, and Open-Source Vector Databases&#x20;

Let's look at some top players:&#x20;

[**Pinecone:**](https://www.pinecone.io/) A cloud-native, managed vector database that doesn't require infrastructure management. Pinecone offers fast data processing and quality relevance features like metadata filters and supports both sparse and dense vectors. Key offerings include duplicate detection, rank tracking, and deduplication.&#x20;

[**Milvus:**](https://milvus.io/) An open-source vector database tailored for AI applications and similarity search, it provides fast search capabilities across trillions of vector datasets and boasts high scalability and reliability. Its use cases span across image and chatbot applications to chemical structure search.&#x20;

[**Chroma:**](https://www.trychroma.com/) Aimed at building LLM applications, Chroma is an open-source, AI-native embedding database offering features like filtering and intelligent grouping. It positions itself as a database that combines document retrieval capabilities with AI to enhance data querying processes.&#x20;

[**Weaviate:**](https://weaviate.io/) This is a cloud-native, open-source vector database that stands out with its AI modules and ability to handle text, images, and other data conversions into searchable vectors. It offers quick neighbor search and is designed with scalability and security in mind.&#x20;

[**Deep Lake:**](https://github.com/activeloopai/deeplake) Designed for deep learning and LLM-based applications, Deep Lake supports a wide array of data types and integrates with various tools to facilitate model training and versioning. It emphasizes ease in deploying enterprise-grade products.&#x20;

[**Qdrant:**](https://github.com/qdrant/qdrant) A versatile open-source vector search engine and database that supports payload-based storage and extensive filtering. It is well-suited for semantic matching and faceted search, with a focus on efficiency and configuration simplicity.&#x20;

[**Elasticsearch:**](https://www.elastic.co/elasticsearch/vector-database) A highly scalable open-source analytics engine capable of handling diverse data types, Elasticsearch is part of the Elastic Stack, offering fast search, fine-tuned relevance, and sophisticated analytics.&#x20;

[**Vespa:**](https://vespa.ai/) Vespa is an open-source data serving engine that enables machine-learned decisions on massive datasets at serving time. It's built for high-performance and high-availability use cases, facilitating a variety of complex query operations.&#x20;

[**Vald:**](https://github.com/vdaas/vald) Focused on dense vector search, Vald is a distributed, cloud-native search engine that uses the ANN Algorithm NGT for neighbor searches. It features automatic indexing, index backup, and horizontal scaling.&#x20;

[**ScaNN:**](https://github.com/google-research/google-research/tree/master/scann) A Google-developed method that improves search accuracy and performance for vector similarity, ScaNN is known for its effective compression techniques and support for different distance functions.&#x20;

[**Pgvector:**](https://github.com/pgvector/pgvector) As a PostgreSQL extension, pgvector brings vector similarity search to the robust, feature-rich environment of PostgreSQL, enabling embeddings to be stored and searched alongside other application data.&#x20;

[**Faiss:**](https://github.com/facebookresearch/faiss) Developed by Facebook AI Research, Faiss is a library for efficient similarity search and clustering of dense vectors. It's versatile, supporting various distances and batch processing, and it can operate on datasets larger than available RAM.&#x20;

## How to Choose the Right Vector Database for Your Project&#x20;

When you're picking out the perfect vector database, think about these things:&#x20;

* Do you need someone else to handle the techy database stuff, or do you have wizards in-house?&#x20;
* Got your vectors ready, or do you need the database to make them for you?&#x20;
* How fast do you need the data – right now, or can it wait?&#x20;
* How much experience does your team have with this kind of tech?&#x20;
* Is the database easy to learn, or is it going to be lots of late nights?&#x20;
* Can you trust the database to be up and running when you need it?&#x20;
* What's the price tag for setting it up and keeping it going?&#x20;
* How secure is it, and does it check all the legal boxes?&#x20;

## Challenges and Considerations&#x20;

While vector databases are powerful, they come with challenges. The management and querying of high-dimensional data can be resource-intensive. The efficiency of a vector database often depends on the underlying infrastructure and the effectiveness of its indexing and compression algorithms.&#x20;

Furthermore, security and privacy are crucial, especially when handling sensitive data. Vector databases must ensure that they incorporate robust security measures to protect against unauthorized access and data breaches.&#x20;

## The Future of Vector Databases&#x20;

As data continues to grow in volume and complexity, the importance of vector databases will only increase. Their integration with AI and machine learning is a match set for the future where almost every digital interaction may involve some form of similarity search or content-based retrieval.&#x20;

## Conclusion&#x20;

Vector Databases are a cutting-edge solution designed to handle the complexity of modern data needs, particularly in the realm of similarity search and AI applications. Understanding and leveraging vector databases can unlock a plethora of opportunities across industries, making them an exciting area of development in the database technology landscape.&#x20;

As companies and developers keep using AI more and more, the use of vector databases is expected to increase a lot. This signals the start of a new period in how we handle data, where the way we sort and keep information is as complex and varied as the data itself.&#x20;


# Indexing

Indexing involves breaking down a source code file into smaller chunks and converting these chunks into [**embeddings**](https://docs.bito.ai/help/bitos-ai-stack/embeddings) that can be stored in a [**vector database**](https://docs.bito.ai/help/bitos-ai-stack/vector-databases). Bito indexes your entire codebase locally (on your machine) to understand it and provide answers tailored to your code.&#x20;

{% hint style="info" %}
Learn more about Bito's [**AI that Understands Your Code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code) feature.
{% endhint %}

## How Bito Indexes Your Code&#x20;

In the steps below, we'll show you how Bito indexes your code, ensuring that each query you have is met with precise and contextually relevant information. From breaking down code into digestible chunks to leveraging advanced AI models for nuanced understanding, Bito transforms the daunting task of code analysis into a seamless and efficient experience.&#x20;

Here's how the magic happens:&#x20;

### Step 1: Chunk Breakdown&#x20;

*Dividing Code into Pieces*&#x20;

Bito starts by breaking down your source code files into smaller sections, known as 'chunks'. It’s like cutting up a long text into paragraphs to make it more manageable. Each chunk represents a piece of your code that can be individually indexed and analyzed.&#x20;

### Step 2: Indexing Each Chunk&#x20;

*Creating a Searchable Reference*&#x20;

After breaking down the file, each chunk is indexed, similar to creating a catalog entry. This step is crucial as it allows for the efficient location of the code segment later on.&#x20;

### Step 3: Generating Embeddings&#x20;

*Translating Code into Numeric Vectors*&#x20;

For every chunk, Bito generates a numeric vector or [**“embedding”**](https://docs.bito.ai/help/bitos-ai-stack/embeddings). This process, which can be done using OpenAI or alternative open-source embedding models, translates the code into a mathematical representation. The idea is to create a form that can be easily compared and matched with other code chunks.&#x20;

### Step 4: Storing the Vectors&#x20;

*Saving the Essential Data*&#x20;

These embeddings are then stored in an index file on your machine. This index file is like a detailed directory, listing the file name, the location of the chunk within the file (start and end), and the embedding vector for each piece of code.&#x20;

### Step 5: Query Embedding&#x20;

*Understanding Your Questions*&#x20;

When you ask a question in Bito's chatbox, the AI checks whether it has some specific keywords like "my code", "my project", etc. If so, Bito generates a numeric vector for your query, mirroring the process used for code chunks.&#x20;

{% hint style="info" %}
The complete list of these keywords is given on our [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page.&#x20;
{% endhint %}

### Step 6: Finding the Nearest Neighbor&#x20;

*Matching Your Query with Code*&#x20;

Using the query's vector, Bito searches the index to find the code chunk with the closest matching embedding. This step identifies the relevant sections of your codebase that can answer your question.&#x20;

### Step 7: Contextualization&#x20;

*Building a Bigger Picture*&#x20;

Identifying chunks is just part of the process. Bito ensures that these chunks make sense in the broader context of your code. If necessary, it expands the search to include complete functions or related code segments, creating a fuller, more accurate context.&#x20;

### Step 8: Leveraging Language Models&#x20;

*Consulting the AI Experts*&#x20;

With the context in hand, Bito consults with language models – either basic (GPT-4o mini and similar models) or advanced (GPT-4o, Claude Sonnet 3.5, and best in class AI models) – to interpret the code within the context and provide an accurate response to your query.&#x20;

### Step 9: Session Privacy&#x20;

*Keeping Your Data Local*&#x20;

All the indexing and querying happens on your local machine. The index files are stored in the user’s home folder, for example on Windows the path will be something like **C:\Users\Furqan\\.bito\localcodesearch** folder. It ensures that your code and session history remain private and secure.&#x20;

### Step 10: Safeguarding Data&#x20;

*Ensuring Confidentiality*&#x20;

Bito is committed to privacy. All LLM accounts it uses are under strict agreements to prevent your data from being used for training, recorded, or logged.&#x20;

### Step 11: Handling Hallucination&#x20;

*Reducing AI Fabrication*&#x20;

Bito is designed to minimize AI 'hallucinations' or fabrications, ensuring the answers you receive are based on your actual code. Although complete elimination of hallucination isn't feasible, as it sometimes aids in constructing beyond seen data, Bito strives to keep it in check, especially when dealing with your local code.&#x20;

With these steps, Bito provides a robust and privacy-conscious method for indexing and understanding your code, simplifying navigation and enhancing productivity in your development projects.&#x20;


# Generative AI

Generative AI has been making waves across various sectors, from art to technology, leaving many people scratching their heads and wondering: WTF is Generative AI? In this guide, we'll unpack the buzzword and provide you with a clear understanding of what Generative AI is, how it works, and why it's becoming increasingly important in our digital world.&#x20;

## What is Generative AI?&#x20;

At its core, Generative AI refers to the subset of artificial intelligence where the systems are designed to generate new content. It’s like giving an artist a canvas, but the artist is an algorithm that can create images, compose music, write text, generate programming source code, and much more.&#x20;

Generative AI systems are typically powered by machine learning models that have been trained on vast datasets. They learn patterns, structures, and features from this data and use this understanding to generate new, original creations that are often indistinguishable from content created by humans.&#x20;

## How Does Generative AI Work?&#x20;

Generative AI works using advanced machine learning models such as Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs).&#x20;

These models involve two key components:&#x20;

1. **Generative Models:** These are the AI algorithms that create the new data. For example, a generative model might create new images of animals it has never seen before by learning from a dataset of animal pictures.
2. **Discriminative Models:** In the case of GANs, the discriminative model evaluates the data generated by the generative model. This is like an art critic who tells the artist if their work is believable or not.&#x20;

The two models work together in a sort of AI tug-of-war, with the generative model trying to produce better and better outputs and the discriminative model trying to get better at telling the difference between generated and real data.&#x20;

## Applications of Generative AI&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FGSnb4hsCKMQjBa91gb9Q%2FUntitled-2023-11-02-0453.png?alt=media&#x26;token=93696a69-c35f-4403-95fe-584287c87d79" alt=""><figcaption></figcaption></figure>

Generative AI has a plethora of applications, here are a few:&#x20;

* **Art:** Apps like DeepArt and platforms like DALL-E generate original visuals and art based on user prompts.
* **Music:** AI like OpenAI's Jukebox can generate music, complete with lyrics and melody, in various styles and genres.
* **Text:** Tools like ChatGPT can write articles, poetry, and even code based on text prompts. Bito also falls in this category as an AI Coding Assistant.
* **Design:** Generative AI can suggest design layouts for everything from websites to interior decorating.
* **Deepfakes:** This controversial use involves generating realistic video and audio recordings that can mimic real people.&#x20;

## Benefits and Challenges&#x20;

### Benefits&#x20;

* **Efficiency:** Generative AI can produce content much faster than humans.
* **Creativity:** It has the potential to create novel combinations that might not occur to human creators.
* **Personalization:** AI can tailor content to individual tastes and preferences.&#x20;

### Challenges&#x20;

* **Ethics:** Generative AI raises questions about authenticity and the ownership of AI-generated content.
* **Quality Control:** Ensuring consistent quality of AI-generated content can be challenging.
* **Misuse:** There’s a risk of its use in creating misleading information or deepfakes.&#x20;

## Future Prospects&#x20;

The future of Generative AI is both exciting and uncertain. It could revolutionize how we create and consume content. For instance, imagine personalized movies generated in real-time to match your mood, or educational content adapted perfectly to each student's learning style.&#x20;

As technology advances, so too will the capabilities of Generative AI. It's not just about the ‘WTF’ factor; it's about recognizing the potential and preparing for the transformation it will bring about.&#x20;

## Conclusion&#x20;

Generative AI is at the frontier of innovation, standing at the crossroads of creativity and computation. It is transforming the conventional processes of creation across various fields and presenting us with a future where the line between human and machine-made is increasingly blurred. While it brings with it a host of benefits, we must tread carefully to navigate the ethical considerations and harness its power for the greater good.&#x20;

As with any transformative technology, the question isn’t just 'WTF is Generative AI?' but also 'How do we responsibly integrate it into our society?' That is the real challenge and opportunity ahead.


# Large Language Models (LLM)

Large Language Models (LLMs) are advanced AI algorithms trained to understand, generate, and sometimes translate human language. They are called “large” for a good reason: they consist of millions or even billions of parameters, which are the fundamental data points the model uses to make predictions and decisions.&#x20;

## How Do LLM Work?&#x20;

Imagine teaching a child language by reading every book you can find. That’s essentially what LLMs go through. They are fed vast amounts of text data and use statistical methods to find patterns and learn from context. Through a process known as machine learning, these models become adept at predicting the next word in a sentence, answering questions, summarizing texts, and more.&#x20;

## The Training Regime&#x20;

**Data, Data, and More Data:** LLMs are the heavyweight champions of the data world. They are trained on diverse datasets comprising encyclopedias, books, articles, and websites to learn a wide range of language patterns and concepts.&#x20;

**Supervised and Unsupervised Learning:** Some LLMs learn through supervised learning, meaning they learn from datasets that have been labeled or corrected by humans. Others use unsupervised learning, meaning they infer patterns and rules from raw data without human annotation.&#x20;

**Fine-Tuning:** After the initial training, LLMs can be fine-tuned for specific tasks, like legal document analysis or medical diagnosis, by training them further on specialized data.&#x20;

## Applications of LLMs&#x20;

**Writing Assistance:** Grammarly or the autocomplete in your email are powered by LLMs. They predict what you’re trying to say and help you say it better.&#x20;

**Chatbots:** If you've ever chatted with [Bito](https://bito.ai/) and noticed that it sounds almost like a real person, that's because it is powered by several state-of-the-art Large Language Models.&#x20;

**Translation Services:** Services like Google Translate use LLMs to convert text from one language to another, learning from vast amounts of bilingual text to improve their accuracy.&#x20;

## The Magic Behind the Scenes&#x20;

**Neural Networks:** The core technology behind LLMs is artificial neural networks, particularly a type called Transformer models. These mimic some aspects of human brain function and are particularly good at handling sequential data like text.&#x20;

**Training Hardware:** Training LLMs requires significant computational power, often involving hundreds of GPUs or specialized TPUs that work in tandem for weeks or months.&#x20;

**Continuous Learning:** LLMs don’t stop learning after their initial training. They can continue to learn from new data, improving their performance over time.&#x20;

## Examples of Large Language Models&#x20;

### GPT Series by OpenAI&#x20;

The GPT series by OpenAI has been a trailblazer in the field of LLMs. Each version of the Generative Pre-trained Transformer has been more powerful than the last, with GPT-4o as a staggering leap forward. Boasting over 200 billion parameters, this model is not just about size; it’s about the nuanced understanding and generation of human-like text. GPT-4o can craft essays that are indistinguishable from those written by humans, compose complex poetry, and even generate functional computer code across several languages, which is a testament to its versatility.&#x20;

GPT-4o's influence extends across industries. For instance, it can simulate conversations, create educational content, and even assist programmers by converting natural language descriptions into code snippets. Its advanced capabilities are being integrated into various software applications and tools, enhancing productivity and sparking creative new approaches to problem-solving.&#x20;

### BERT by Google&#x20;

**BERT** stands for **Bidirectional Encoder Representations from Transformers**. It's a complicated name, but really, it's just Google's method for making search engines smarter. Unlike earlier models, BERT examines the context of a word in both directions (left and right of the word) within a sentence, leading to a far more nuanced interpretation of the query. This ability means that BERT can grasp the full intent behind your searches, so the results you get are closer to what you actually need. &#x20;

Since its integration into Google's search engine, BERT has significantly improved the relevance of results for millions of queries every day. For users, this often translates to finding answers more quickly and accurately, sometimes in subtle ways that may go unnoticed but are nonetheless powerful. Beyond search, BERT is also revolutionizing natural language processing tasks such as language translation, question answering, and text summarization.&#x20;

In summary, both the GPT series and BERT are not just steps but giant leaps forward in our ability to interface with machines in a more natural, intuitive way. They are redefining what's possible in the realm of AI and continuing to pave the way for smarter, more responsive technology.&#x20;

## Ethical Considerations and Challenges&#x20;

**Bias in AI:** Since LLMs learn from existing data, they can perpetuate and amplify biases present in that data. It’s an ongoing challenge to ensure that LLMs are fair and unbiased.&#x20;

**Privacy:** Training LLMs on personal data raises privacy concerns. Ensuring data used is anonymized and secure is paramount.&#x20;

**Environmental Impact:** The energy consumption of training and running LLMs is significant. Researchers are working on more efficient models to mitigate this.&#x20;

## The Future of LLMs&#x20;

**Evolving Intelligence:** LLMs are getting more sophisticated, with future models expected to handle more complex tasks and exhibit greater understanding of human language.&#x20;

**Interdisciplinary Integration:** LLMs are beginning to intersect with other fields, such as bioinformatics and climatology, providing unique insights and accelerating research.&#x20;

**Democratization of AI:** As LLMs become more user-friendly, their use is expanding beyond tech companies to schools, small businesses, and individual creators.&#x20;

## Conclusion&#x20;

Large Language Models are transforming how we interact with machines, making them more human-like than ever. They're a blend of colossal data, computing power, and intelligent algorithms, pushing the boundaries of what machines can understand and accomplish. As they evolve, LLMs will continue to shape our digital landscape in unpredictable and exciting ways. Just remember, the next time you type out a sentence and your phone suggests the end of it, there’s a little bit of LLM magic at work.&#x20;


# LLM tokens

At the heart of every LLM, from GPT-3.5 Turbo to the latest GPT-4o, are tokens. These are not your arcade game coins but the fundamental units of language that these models understand and process. Imagine tokens as the DNA of digital language—their sequence dictates how an LLM interprets and responds to text.&#x20;

A token is created when we break down a massive text corpus into digestible bits. Think of it like slicing a cake into pieces; each slice, or token, can vary from a single word to a punctuation mark or even a part of a word. The process of creating tokens, known as **tokenization**, simplifies complex input text, making it manageable for LLMs to analyze.&#x20;

**Here’s a quick reference to understand token equivalents:**&#x20;

* 1 token ≈ 4 characters in English&#x20;
* 1 token ≈ ¾ of a word&#x20;
* 100 tokens ≈ 75 words or about 1–2 sentences&#x20;

## Tokenization Methods&#x20;

Imagine you have a sentence: **"The quick brown fox jumps over the lazy dog."** An LLM would use tokenization to chop this sentence into manageable pieces. Depending on the chosen method (we’ve discussed it in the next section below), this could result in a variety of tokens, such as:&#x20;

* **Word-level:** \["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]&#x20;
* **Subword-level:** \["The", "quick", "brown", "fox", "jumps", "over", "the", "la", "zy", "dog"]&#x20;
* **Character-level:** \["T", "h", "e", " ", "q", "u", "i", "c", "k", " ", ...]&#x20;

Each method has its own advantages and disadvantages.&#x20;

**Word-level tokenization** is straightforward and aligns with the way humans naturally read and write text. It is effective for languages with clear word boundaries and for tasks where the meaning is heavily dependent on the use of specific words. However, this method can lead to very large vocabularies, especially in languages with rich morphology or in cases where the text contains a lot of different proper nouns or technical terms. This large vocabulary can become a problem when trying to manage memory and computational efficiency.&#x20;

**Subword-level tokenization**, often implemented through methods like Byte Pair Encoding (BPE) or SentencePiece, addresses some of the issues of word-level tokenization. By breaking down words into more frequently occurring subunits, this method allows the model to handle rare or out-of-vocabulary (OOV) words more gracefully. It balances the vocabulary size and the ability to represent the full range of text seen during training. It can also be more effective for agglutinative languages (like Turkish or Finnish), where you can combine many suffixes with a base word, leading to an explosion of possible word forms if using word-level tokenization.&#x20;

**Character-level tokenization** has the advantage of the smallest possible vocabulary. Since it deals with characters, it is very robust to misspellings and OOV words. However, because it operates at such a fine-grained level, it may require more complex models to understand higher-level abstractions in the text. Models may need to be larger or more complex to learn the same concepts that could be learned with fewer parameters at higher levels of tokenization.&#x20;

Beyond these, there are other tokenization methods such as:&#x20;

* **Byte-level:** Similar to character-level, but treats the text as a sequence of bytes, which can be useful for handling multilingual text uniformly.&#x20;
* **Morpheme-level:** Breaks words down into morphemes, which are the smallest meaningful units of language. This can be useful for capturing linguistic nuances but requires sophisticated algorithms to implement effectively.&#x20;
* **Hybrid approaches:** Some models use a combination of the above methods, often starting with a larger unit and then falling back to smaller units when the first approach does not work.&#x20;

The choice of tokenization can affect not just the performance of an LLM but also its understanding of the text. For example, using a subword tokenizer that never breaks down "dog" into smaller pieces ensures that the model always considers "dog" as a semantic unit. In contrast, if "dog" could be broken down into "d" and "og", the model might lose the understanding that "dog" represents an animal.&#x20;

## Tokens and Model Costs&#x20;

The complexity and number of tokens directly impact the computational horsepower needed to run AI models. More tokens generally mean more memory and processing power, which translates to higher costs.&#x20;

When you use services like OpenAI's GPT models, you're charged based on the number of tokens processed. With different rates for different models (like Davinci or Ada), budgeting for AI usage can get tricky. This makes the choice of tokenization method not just a technical decision but also a financial one.&#x20;

## Overcoming the Token Limit Challenge&#x20;

A crucial point about LLMs is that they can only handle a limited number of tokens at once—this is their **token limit**. The more tokens they can process, the more complex the tasks they can handle.&#x20;

Imagine asking an AI to write a novel in one go. If the token limit is low, it might only manage a chapter. If it's high, you could get a full book, but it might take ages to write. It's all about finding the balance between performance and practicality.&#x20;

**Here’s the token limits chart of popular LLMs.**&#x20;

| Model Name             | Context Window | Max Output Tokens |
| ---------------------- | -------------- | ----------------- |
| GPT-3.5 Turbo          | 16,385 tokens  | 4,096 tokens      |
| GPT-3.5 Turbo Instruct | 4,096 tokens   | 4,096 tokens      |
| GPT-4                  | 8,192 tokens   | 8,192 tokens      |
| GPT-4o                 | 128,000 tokens | 4,096 tokens      |
| GPT-4o mini            | 128,000 tokens | 16,384 tokens     |
| Claude Sonnet 3.5      | 200,000 tokens | 8192 tokens       |

&#x20;But what happens when you have more to say than the token limit allows?&#x20;

## 5 Strategies to Beat Token Limits&#x20;

1. **Truncation:** The most straightforward approach is to cut the text down until it fits the token budget. However, this is like trimming a picture; you lose some of the scenes.
2. **Chunk Processing:** Break your text into smaller pieces, process each chunk separately, and stitch the results together. It's like watching a series of short clips instead of a full movie.
3. **Summarization:** Distill your text to its essence. For example, "It's sunny today. What will the weather be like tomorrow?" can be shortened to "Tell me tomorrow's weather."
4. **Remove Redundant Terms:** Cut out the fluff—words that don't add significant meaning (like "the" or "and"). This streamlines the text but beware, over-pruning can alter the message.
5. **Fine-Tuning Language Models:** Custom-train your model on specific data to get better results with fewer tokens. It’s like prepping a chef to make a dish they can cook blindfolded.&#x20;

## Conclusion&#x20;

Tokens are much more than jargon—they're central to how language models process and understand our queries and commands. &#x20;

Understanding tokens and their role in AI language processing is fundamental for anyone looking to leverage the power of LLMs in their work or business. By grasping the basics of tokenization and its impact on computational requirements and costs, users can make informed decisions to balance performance with budget.&#x20;


# LLM parameters

Parameters are the individual elements of a Large Language Model that are learned from the training data. Think of them as the synapses in a human brain—tiny connections that store learned information.&#x20;

## How Parameters Work in LLMs&#x20;

Each parameter in an LLM holds a tiny piece of information about the language patterns the model has seen during training. They are the fundamental elements that determine the behavior of the model when it generates text.&#x20;

For example, imagine teaching a child what a cat is by showing them pictures of different cats. Each picture tweaks the child's understanding and definition of a cat. In LLMs, each training example tweaks the parameters to better understand and generate language.&#x20;

## The Role of Parameters in Understanding and Generating Language&#x20;

Parameters are crucial because they allow the model to perform tasks such as translation, write articles, and even generate source code. When you ask an AI a question, the parameters work together to sift through the learned patterns and generate a response that makes sense based on the training it received.&#x20;

For instance, if you ask an AI to write a poem, the parameters will determine how to structure the poem, what words to use, and how to create rhyme or rhythm, all based on the data it was trained on.&#x20;

## The Scale of LLM Parameters: Just How Large Are We Talking?&#x20;

When we say "Large" in LLM, we're not kidding. The size of a language model is directly related to the number of parameters it has.&#x20;

Take GPT-4, for example, with its 1.76 trillion parameters. That's like 1.76 trillion different dials the model can tweak to get language just right. Each parameter holds a piece of information that can contribute to understanding a sentence's structure, the meaning of a word, or even the tone of a text.&#x20;

Earlier models had significantly fewer parameters. GPT-1, for instance, had only 117 million parameters. With each new generation, the number of parameters has grown exponentially, leading to more sophisticated and nuanced language generation.&#x20;

## Training LLMs: How Parameters Learn&#x20;

Training an LLM involves a process called **"backpropagation"** where the model makes predictions, checks how far off it is, and adjusts the parameters accordingly.&#x20;

Let's say we're training an LLM to recognize the sentiment of a sentence. We show it the sentence "I love sunny days!" tagged as positive sentiment. The LLM predicts positive but isn't very confident. During backpropagation, it adjusts the parameters to increase the confidence for future similar sentences.&#x20;

This process is repeated millions of times with millions of examples, gradually fine-tuning the parameters so that the model's predictions become more accurate over time.&#x20;

## Parameter’s Impact on AI Performance and Limitations&#x20;

The number of parameters is one of the key factors influencing an AI model's performance. However, more parameters can mean a model requires more computational power and data to train effectively, which can lead to increased costs and longer training times.&#x20;

With great power comes great responsibility—and greater chances of making mistakes. More parameters can sometimes mean that the model starts seeing patterns where there aren't any, a phenomenon known as "overfitting" where the model performs well on training data but poorly on new, unseen data.&#x20;

## The Future of Parameters in LLMs&#x20;

The future of LLMs might not just be about adding more parameters, but also about making better use of them. Innovations in how parameters are structured and how they learn are ongoing.&#x20;

AI researchers are exploring ways to make LLMs more parameter-efficient, meaning they can achieve the same or better performance with fewer parameters. Techniques like "parameter sharing" and "sparse activation" are part of this cutting-edge research.&#x20;

## Conclusion&#x20;

Parameters in LLMs are the core elements that allow these models to understand and generate human-like text. While the sheer number of parameters can be overwhelming, it's their intricate training and fine-tuning that empower AI to interact with us in increasingly complex ways.&#x20;

As AI continues to evolve, the focus is shifting from simply ramping up parameters to refining how they're used, ensuring that the future of AI is not just smarter but also more efficient and accessible.&#x20;


# Retrieval Augmented Generation (RAG)

**Retrieval Augmented Generation (RAG)** is a paradigm-shifting methodology within natural language processing that bridges the divide between information retrieval and language synthesis. By enabling AI systems to draw from an external corpus of data in real-time, RAG models promise a leap towards a more informed and contextually aware generation of text.&#x20;

RAG fuses in-depth data retrieval with creative language synthesis in AI. It's like having an incredibly knowledgeable friend who can not only recall factual information but also weave it into a story seamlessly, in real-time.&#x20;

## The Mechanics of RAG&#x20;

To understand RAG, let's break it down:&#x20;

* **Retrieval:** Before generating any new text, the RAG model retrieves information from a large dataset or database. This could be anything from a simple database of facts to an extensive library of books and articles.&#x20;
* **Augmented:** The retrieved information is then fed into a generative model to "augment" its knowledge. This means the generative model doesn't have to rely solely on what it has been trained on; it can access external data for a more informative output.&#x20;
* **Generation:** Finally, the model generates text using both its pre-trained knowledge and the newly retrieved information, leading to more accurate, detailed, and relevant responses.&#x20;

## The Components of a RAG Model&#x20;

A RAG model typically involves two major components:&#x20;

1. **Document Retriever:** This is a neural network or an algorithm designed to sift through the database and retrieve the most relevant documents based on the query it receives.&#x20;
2. **Sequence-to-Sequence Model:** After retrieval, a Seq2Seq model, often a transformer-based model like BERT or GPT, takes the retrieved documents and the initial query to generate a coherent and relevant piece of text.&#x20;

## How to Build a RAG&#x20;

Let's imagine we want to build a RAG model that, when given a prompt about a historical figure or event, can generate a detailed and accurate paragraph.&#x20;

### Step 1: Choose Your Data Source&#x20;

First, you need a database from which the model can retrieve information. For historical facts, this could be a curated dataset like Wikipedia articles, historical texts, or a database of historical records.&#x20;

### Step 2: Index Your Data Source&#x20;

Before you can retrieve information, you need to index your data source to make it searchable. You can use software like Elasticsearch for efficient indexing and searching of text documents.&#x20;

### Step 3: Set Up the Retriever&#x20;

You then need a retrieval model that can take a query and find the most relevant documents in your database. This could be a simple TF-IDF (Term Frequency-Inverse Document Frequency) retriever or a more sophisticated neural network-based approach like a Dense Retriever that maps text to embeddings.&#x20;

### Step 4: Integrate with a Generative AI Model&#x20;

The retrieved documents are then fed into a generative AI model, like GPT-4o or BERT. This model is responsible for synthesizing the information from the documents with the original query to generate coherent text.&#x20;

### Step 5: Training Your RAG Model&#x20;

If you're training a RAG model from scratch, you'd need to fine-tune your generative AI model on a task-specific dataset. You’d need to:&#x20;

* Provide pairs of queries and the correct responses.&#x20;
* Allow the model to retrieve documents during training and learn which documents help it generate the best responses.&#x20;

### Step 6: Iterative Refinement&#x20;

After initial training, you can refine your model through further iterations, improving the retriever or the generator based on the quality of outputs and user feedback.&#x20;

Building such a RAG system would be a significant engineering effort, requiring expertise in machine learning, NLP, and software engineering.&#x20;

## Why RAG is a Game-Changer&#x20;

RAG significantly enhances the relevance and factual accuracy of text generated by AI systems. This is due to its ability to access current databases, allowing the AI to provide information that is not only accurate but also reflects the latest updates.&#x20;

Moreover, RAG reduces the amount of training data needed for language models. By leveraging external databases for knowledge, these models do not need to be fed as much initial data to become functional.&#x20;

RAG also offers the capability to tailor responses more specifically, as the source of the retrieved data can be customized to suit the particular information requirement. This functionality signifies a leap forward in making AI interactions more precise and valuable for users seeking information.&#x20;

## Practical Applications of RAG&#x20;

The applications of RAG are vast and varied. Here are a few examples:&#x20;

* **Customer Support:** RAG can pull up customer data or FAQs to provide personalized and accurate support.&#x20;
* **Content Creation:** Journalists and writers can use RAG to automatically gather information on a topic and generate a draft article.&#x20;
* **Educational Tools:** RAG can be used to create tutoring systems that provide students with detailed explanations and up-to-date knowledge.&#x20;

## Challenges and Considerations&#x20;

Despite its advantages, RAG also comes with its set of challenges:&#x20;

* **Quality of Data:** The retrieved information is only as good as the database it comes from. Inaccurate or biased data sources can lead to flawed outputs.&#x20;
* **Latency:** Retrieval from large databases can be time-consuming, leading to slower response times.&#x20;
* **Complexity:** Combining retrieval and generation systems requires sophisticated machinery and expertise, making it complex to implement.&#x20;

## Conclusion&#x20;

Retrieval Augmented Generation is a significant step forward in the NLP field. By allowing machines to access a vast array of information and create something meaningful from it, RAG opens up a world of possibilities for AI applications. &#x20;

Whether you're a developer looking to build smarter AI systems, a business aiming to improve customer experience, or just an AI enthusiast, understanding RAG is crucial for advancing in the dynamic field of artificial intelligence.&#x20;


# Prompts

A prompt, in the simplest terms, is the initial input or instruction given to an AI model to elicit a response or generate content. It's the human touchpoint for machine intelligence, a cue that sets the AI's gears in motion.&#x20;

Prompts are more than mere commands; they are the seeds from which vast trees of potential conversations and content grow. Think of them as the opening line of a story, the question in a quiz, or the problem statement in a mathematical conundrum – the prompt is the genesis of the AI's creative or analytical output.&#x20;

For example, when you ask GPT-4o "What's the best way to learn a new language?" you've given it a prompt. The AI then processes this and generates advice based on its training data.&#x20;

## The Art of Prompt Engineering&#x20;

Prompt engineering is a discipline in itself, evolving as an art and science within AI communities. Crafting effective prompts is akin to programming without code; it's about phrasing and framing your request to the AI in a way that maximizes the quality and precision of its output.&#x20;

Good prompt engineering can involve:&#x20;

* **Being specific:** Clearly defining what you want the AI to do.&#x20;
* **Setting the tone:** Informing the AI of the style or mood of the content you expect.&#x20;
* **Contextualizing:** Providing background information to guide the AI's responses.&#x20;

**Example:** Instead of saying, "Tell me about France," a well-engineered prompt would be, "Write a short travel guide for first-time visitors to France, highlighting top attractions, cultural etiquette, and local cuisine."&#x20;

## The Role of Prompts in Generative AI&#x20;

Generative AI, which includes everything from text to image generation models, relies heavily on prompts to determine the direction of content creation. Prompts for generative AI act as a blueprint from which the model can conjure up entirely new pieces of content – whether that's an article, a poem, a piece of art, or a musical composition.&#x20;

Prompts tell the AI not just what to create, but can also suggest how to create it, influencing creativity, tone, structure, and detail. As generative AI grows more sophisticated, the potential for complex and nuanced prompts increases, allowing for more customized and high-fidelity outputs.&#x20;

**Example:** Prompting an AI with "Create a poem in the style of Edgar Allan Poe about the sea" instructs the model to adopt a specific literary voice and thematic focus.&#x20;

## Challenges and Considerations&#x20;

Crafting the perfect prompt isn't always straightforward. One of the challenges lies in the AI's interpretation of the prompt. Ambiguity can lead to unexpected or unwanted results, while overly restrictive prompts may stifle the AI's creative capabilities.&#x20;

Moreover, ethical considerations arise when prompts are designed to elicit biased or harmful content. The AI's response is contingent upon its training data, and if that data includes prejudiced or false information, the output may reflect those biases. Responsible prompt engineering thus also involves an awareness of potential harm and the implementation of safeguards against it.&#x20;

**Example:** To avoid bias in AI-generated news summaries, prompts should be engineered to require neutrality and fact-checking.&#x20;

## Conclusion&#x20;

Prompts are the simple commands or questions we use to kickstart a conversation with AI, guiding it to understand and generate the responses or content we seek. They're like the steering wheel for the AI's capabilities, crucial for navigating the vast landscape of information and creativity the AI models offer.&#x20;

As we continue to interact with and shape AI technology, mastering the use of prompts becomes our way of ensuring that the conversation flows in the right direction. Simply put, the better we become at asking, the better AI gets at answering.&#x20;

So, the next time you interact with a language model, remember that the quality of the output is often a direct reflection of your input - your prompt is the key.&#x20;


# Prompt engineering

Prompt Engineering is the art and science of crafting inputs (prompts) that guide AI to produce the desired outputs. It's about understanding how to communicate with an AI in a way that leverages its capabilities to the fullest. Think of it as giving directions to a supremely intelligent genie without any misunderstandings.&#x20;

{% hint style="info" %}
In Bito’s backend, we do a lot of prompt engineering to ensure that you always receive accurate outputs.
{% endhint %}

## Why is it Important?&#x20;

Generative AI, like OpenAI’s GPT models, are revolutionizing industries from content creation to coding. But their utility hinges on the quality of the prompts they receive. A well-engineered prompt can yield rich, accurate, and nuanced responses, while a poor one can lead to irrelevant or even nonsensical answers.&#x20;

## The Anatomy of a Good Prompt&#x20;

### Clarity and Specificity&#x20;

AI models are literal. If you ask for an article, you'll get an article. If you ask for a poem about dogs in space, you’ll get exactly that. The specificity of your request can significantly alter the output.&#x20;

**Example:**&#x20;

* **Vague Prompt:** Write about health.&#x20;
* **Engineered Prompt:** Write a comprehensive guide on adopting a Mediterranean diet for improving heart health, tailored for beginners.&#x20;

### Contextual Information&#x20;

Providing context helps the AI understand the nuance of the request. This could include tone, purpose, or background information.&#x20;

**Example:**&#x20;

* **Without Context:** Explain quantum computing.&#x20;
* **With Context:** Explain quantum computing in simple terms for a blog aimed at high school students interested in physics.&#x20;

### Closed vs. Open Prompts&#x20;

Closed prompts lead to specific answers, while open prompts allow for more creativity. Depending on your goal, you may need one over the other.&#x20;

**Example:**&#x20;

* **Closed Prompt:** What is the capital of France?&#x20;
* **Open Prompt:** Describe a day in the life of a Parisian.&#x20;

## The Practice of Prompt Engineering&#x20;

Prompt engineering is not a "get it right the first time" kind of task. It involves iterating prompts based on the responses received. Tweaking, refining, and even overhauling prompts based on output can lead to more accurate and relevant results.&#x20;

A significant part of prompt engineering is experimentation. By testing different prompts and studying the outputs, engineers learn the nuances of the AI's language understanding and generation capabilities.&#x20;

Keywords are the bread and butter of prompt engineering. Identifying the right keywords can steer the AI in the desired direction.&#x20;

**Example:**&#x20;

* **Without Keyword Emphasis:** Write about the internet.&#x20;
* **With Keyword Emphasis:** Write an article focused on the evolution of internet privacy policies.&#x20;

## Advanced Techniques&#x20;

### Chain of Thought Prompts&#x20;

These prompts mimic a human thought process, providing a step-by-step explanation that leads to an answer or conclusion. This can be especially useful for complex problem-solving.&#x20;

**Example:**&#x20;

* **Chain of Thought Prompt:** To calculate the gravitational force on an apple on Earth, first, we determine the mass of the apple and the distance from the center of the Earth...&#x20;

### Zero-Shot and Few-Shot Learning&#x20;

In zero-shot learning, the AI is given a task without previous examples. In few-shot learning, it’s provided with a few examples to guide the response. Both techniques can be leveraged in prompt engineering for better results.&#x20;

**Example:**&#x20;

* **Zero-Shot Prompt:** What are five innovative ways to use drones in agriculture?&#x20;
* **Few-Shot Prompt:** Here are two ways to use drones in agriculture: 1) Crop monitoring, 2) Automated planting. List three more innovative ways.&#x20;

## Ethical Considerations and Limitations&#x20;

* **Bias and Sensitivity:** Prompt engineers must be mindful of inherent biases and ethical considerations. This includes avoiding prompts that could lead to harmful outputs or perpetuate stereotypes.&#x20;
* **Realistic Expectations:** LLMs and Generative AI are powerful but not omnipotent. Understanding their limitations is crucial in setting realistic expectations for what prompt engineering can achieve.&#x20;
* **Data Privacy and Security:** As prompts often contain information that may be sensitive, engineers must consider data privacy and security in their designs.&#x20;

## Conclusion&#x20;

Prompt engineering is more than a technical skill—it’s a new form of linguistic artistry. As we continue to integrate AI into our daily lives, becoming adept at communicating with these systems will become as essential as coding is today.&#x20;

Whether you’re a writer, a developer, or just an AI enthusiast, mastering the craft of prompt engineering will place you at the forefront of this exciting conversational frontier. So go ahead, start crafting those prompts, and unlock the full potential of your AI companions.&#x20;


# Account and settings

Manage your Bito workspace, members and the personal settings

<table data-view="cards"><thead><tr><th data-type="content-ref"></th><th></th></tr></thead><tbody><tr><td><a href="account-and-settings/creating-a-bito-account">creating-a-bito-account</a></td><td>Learn how to sign up or log in to Bito</td></tr><tr><td><a href="account-and-settings/workspace">workspace</a></td><td>Learn how to create, join, or change workspace</td></tr><tr><td><a href="account-and-settings/managing-workspace-members">managing-workspace-members</a></td><td>Invite coworkers and manage their workspace membership</td></tr><tr><td><a href="account-and-settings/setting-ai-output-language">setting-ai-output-language</a></td><td>Personalize Bito to speak your language</td></tr><tr><td><a href="account-and-settings/managing-user-access-levels">managing-user-access-levels</a></td><td>Learn about different access levels and permissions</td></tr><tr><td><a href="account-and-settings/access-key">access-key</a></td><td>An alternative to standard email and OTP authentication</td></tr></tbody></table>


# Creating a Bito account

Try Advanced AI Coding Assistant for Free

You would need to create an account with your email to use Bito. You can sign up for Bito directly from the IDE extension or the Bito web interface at <https://alpha.bito.ai/>.&#x20;

1. After you install the Bito extension, click the "Sign up or Sign-in" button on the Bito sign-up flow screen.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrKXn8cHKNAL5GnpscTIz%2Fscrnli_10_11_2023_2-20-15%20PM.png?alt=media&#x26;token=0b44a956-ca5d-449d-98c2-c48231d50b02" alt=""><figcaption></figcaption></figure>

2. In the next screen, enter your work email address, and verify through a six-digit code sent to your email address.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfBan4b3U8lc5mjiMlqFU%2Fimage.png?alt=media&#x26;token=5c517cd8-7450-4857-a9e1-bfb16bd5e970" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFdYZqY99H9Uc5edpKF81%2Fimage.png?alt=media&#x26;token=d6f1cc20-880e-44e3-b48b-dffb5bf7fb5e" alt=""><figcaption></figcaption></figure>

3. Once your email is verified, you will get an option to create your profile. Enter your full name and set the language for the AI setup. Bito uses this setting to generate the output regardless of prompt language. &#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FpPJRCUaojm4vLIHlz1ts%2Fimage.png?alt=media&#x26;token=000cf658-5583-429f-a43f-a0902d7afcb4" alt=""><figcaption></figcaption></figure>

Now, let's learn[ **how to create a new workspace or join an existing one**](https://docs.bito.ai/help/account-and-settings/workspace) to start using Bito.


# Workspace

Learn How to Create, Join, or Change Workspace

A workspace is a dedicated environment or space where teams can collaborate and use Bito services. After logging into your Bito account, you can either create a new workspace or join an existing one you've been invited to.

{% hint style="info" %}
You can use Bito in a single-player mode for all the use cases. However, it works best when your coworkers join the Workspace for collaboration.
{% endhint %}

## Create a New Workspace

The link to create a new workspace will appear at the bottom of the sign-up flow screen. Click on "Create Workspace" to get started.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FHWxQUAPaH5sVDqga1dzu%2Fscrnli_10_11_2023_2-22-59%20PM.png?alt=media&#x26;token=d19d8cb2-9d6f-4914-bed7-5a895597a73f" alt="" width="548"><figcaption></figcaption></figure>

Now, enter the name of the workspace. You can also choose to make this workspace discoverable by the users with the same domain email as your email. Finally, click on the "Next" button to proceed creating a new workspace.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fb6VbR8KXhaS0Y3BjpkEm%2FScreenshot%202023-10-11%20020015.png?alt=media&#x26;token=c74aa767-af5d-4c7b-bd2e-a2c15e146709" alt="" width="548"><figcaption></figcaption></figure>

{% hint style="info" %}
For example, if your email is <smith@mywebsite.com> and you enable the "Workspace discovery" feature, then any other person with an email that ends in @mywebsite.com (like <john@mywebsite.com>, <furqan@mywebsite.com>, and so on) can join your workspace after they sign in.

You can always switch this feature off later by visiting the [**Workspace Settings**](https://alpha.bito.ai/home/settings/advance-settings) page.
{% endhint %}

{% hint style="info" %}
Workspace discovery feature is not available for public email addresses like @gmail.com, @outlook.com, @yahoo.com, etc.
{% endhint %}

Once you complete the Workspace setup, Bito will be ready to use.

## Join an Existing Workspace

If your email domain is allowed for the Workspace, or your coworker invited you, you will see the Workspace listed during the sign-up flow under the "Workspaces Available to Join" list.

Simply click on the "Join" button given in front of the workspace you want to join. Joining your company or team Workspace takes less than a minute.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fqel6Daae7iDdBCscKnar%2FScreenshot%202023-10-11%20015945.png?alt=media&#x26;token=9a76b5af-6697-4dd7-ab30-2eb6af7e273e" alt="" width="548"><figcaption></figcaption></figure>

Alternatively, you can join the Workspace through the Workspace link shared by your coworker.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FCgFvEd6zWzp7YVGwLXcz%2Fscrnli_10_11_2023_2-41-20%20PM.png?alt=media&#x26;token=447f8451-865a-43da-858c-48fc11f085b5" alt=""><figcaption></figcaption></figure>

## Change Workspace

Follow the below steps to switch to a different workspace:

1. First log out of your Bito account.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FELpLDBOMVjAQ8nkPd3J1%2Fscrnli_10_11_2023_3-33-22%20PM.png?alt=media&#x26;token=523b51ae-945f-42cc-a3db-3c34248b288a" alt=""><figcaption></figcaption></figure>

2. Then, log back in and choose the workspace you want from the available list.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FzlQEezrD2Fnu8hwfw5YV%2FScreenshot%202023-10-11%20015929.png?alt=media&#x26;token=3e4ee15f-5903-4eea-aa13-6e0885b2d97a" alt="" width="548"><figcaption></figcaption></figure>

### How to See Which Workspace You Are In?

In the IDE extension, place your mouse cursor over the workspace icon. The workspace name will show up as a tooltip.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5J2vqqbLURf4qs7NmmXo%2Fscrnli_10_11_2023_2-50-44%20PM.png?alt=media&#x26;token=1e20fd29-5ad1-4148-a317-5f2be27814bc" alt="" width="521"><figcaption></figcaption></figure>


# Managing  workspace members

Bring your team together

In Bito, collaboration happens within a **Workspace**, where team members are assigned roles and access based on their responsibilities. In most cases, every organization would create one Workspace. Anyone can [**sign up on Bito**](https://alpha.bito.ai/), create a workspace for their team, and invite their coworkers to join the Workspace.&#x20;

The [**Manage Users → Members**](https://alpha.bito.ai/home/members) dashboard introduces a clear, flexible interface for managing user access and feature seats across your team.

## Seat management overview

At the top of the **Members** dashboard, you’ll see a summary of your seat usage and assignment status:

* **Seats purchased**: Displays the total number of seats your workspace has purchased and the total billing amount.
* **Seats assigned**: Shows how many of those seats are assigned for:
  * **IDE Code Reviews**
  * **Git Code Reviews**
* **Seat assignment mode**:
  * **Auto (Assign & Buy):** In this mode, available seats will be automatically assigned to developers (marked as [Eligible](https://docs.bito.ai/billing-and-plans/overview#assigning-code-review-agent-seats)) when they join the workspace or when they submit their first pull request reviewed by Bito. If all seats are assigned, new seat is purchased and assigned automatically.
    * ***Note:** This mode is useful for dynamic teams where new contributors are added frequently.*
    * ***Note:** This is the default mode for all new workspaces.*
  * **Auto (Assign only):** In this mode, available seats will be automatically assigned to developers (marked as [Eligible](https://docs.bito.ai/billing-and-plans/overview#assigning-code-review-agent-seats)) when they join the workspace or when they submit their first pull request reviewed by Bito. If no seats are available, Bito will not purchase additional seats, and the developer will not gain access to Bito features.
  * **Manual:** In this mode, workspace admins need to manually purchase seats and [assign them to developers](https://docs.bito.ai/billing-and-plans/overview#assigning-code-review-agent-seats) as needed. Bito will review pull requests only for submitters who have an assigned seat.
    * ***Note:** This mode is ideal for teams that want tighter control over who gets access and when billing occurs.*

You can switch between these modes based on your team's seat allocation preferences.

<a href="../../billing-and-plans/overview#seat-management" class="button primary">Learn more</a>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fk892sPlZPXvsMUJJQD8O%2Fscrnli_jE3Uiba03IjHl3.png?alt=media&#x26;token=0357c01b-3100-48d6-acb9-6222200ce6ef" alt=""><figcaption></figcaption></figure>

## Managing members by feature

Below the seat overview, you'll find three tabs to manage different types of access:

#### 1. **Git Code Review tab**

Assign or unassign seats to members specifically for the Git based Code Review Agent feature. Each member listed here can be toggled on or off depending on whether you want to allocate a seat for this feature.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FtyTtpwy7rcDF5gS0eiCo%2Fscrnli_4XpAlWqsuim28d.png?alt=media&#x26;token=fb85bf93-c45c-453c-bed1-92ea4dad2251" alt=""><figcaption></figcaption></figure>

#### 2. **IDE Code Review tab**

Similar to the Git Code Review tab, this tab lets you assign or remove access to Bito's AI Chat and code review feature in supported IDEs. You can also [invite new members](#inviting-coworkers-to-the-workspace) to join the workspace.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FkCCdW3bit3FaCDFXdZUa%2Fscrnli_0JzrS8S3Gip93M_1.png?alt=media&#x26;token=d96f858a-ed59-48c2-aebb-8ca7f66a9917" alt=""><figcaption></figcaption></figure>

#### 3. **Admin tab**

This tab is dedicated to managing administrative roles within the workspace. Only members with elevated permissions are shown here.

This tab displays a table with the following information:

* **Name**: Displays the full name and email address of the member.
* **Role**: A dropdown that allows you to set or update the user’s administrative role:
  * **Owner**: Full control over the workspace.
  * **Admin**: Access to most workspace management functions.
  * **+ Billing contact**: (Checkbox) Receives billing-related communications.
  * **Billing only**: (Button) Limits the member to billing management tasks.

**Additional options:**

Each admin row has a three-dot menu offering:

* **Remove from Admin members**: Revoke administrative privileges.
* **Remove from workspace**: Completely remove the user from the workspace.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjvjwFLEt9xotsiKVcX3j%2Fscrnli_hRg3q01U3ivPsa.png?alt=media&#x26;token=62ef6fce-4d55-4ee1-a8b1-00d7c1997e96" alt=""><figcaption></figcaption></figure>

## Inviting coworkers to the Workspace

You can use Bito in a single-player mode for all the use cases. However, it works best when your coworkers join the Workspace to collaborate with Bito. There are three ways you can invite your coworkers.&#x20;

**Option 1** - Allow your work e-mail domain for the Workspace. This setting is turned on by default, and all users with the same e-mail domain as yours will automatically see the Workspace under "Pending Invitations" when signing up in Bito. You can manage this setting after you create the Workspace through the "Settings" page in your Bito account.&#x20;

{% hint style="info" %}
You may still need to notify your coworkers about Bito and share Bito workspace URL. We don't send e-mails to your coworkers unless you invite them to the Workspace.&#x20;
{% endhint %}

**Option 2** - Invite your coworkers via e-mail when you create your Workspace or later from your workspace setting.&#x20;

**Option 3**- Share a web link specific to your Workspace via the channel of your choice: e-mail, Slack, or Teams. The link is automatically created and shown when creating a workspace or on the workspace settings page.

## Adding Admin members

To add a new admin:

1. Click the **“Add members”** button at the top of the Admin tab.
2. In the popup:
   * Select an existing user from your workspace, **or**
   * Invite a new member by entering their email address.
3. Assign the appropriate role and permissions as needed.


# Setting AI output language

Communicate in Your Preferred Language

Bito users come from all over the world, and it makes it super easy to set the AI output language. Bito will automatically generate the text output in the language in your user profile setting, regardless of the prompt input language.&#x20;

Bito allows setting this language when creating an account, as described in [creating-a-bito-account](https://docs.bito.ai/help/account-and-settings/creating-a-bito-account "mention").&#x20;

You can also set or change this setting anytime by going to [**Settings > Profile settings**](https://alpha.bito.ai/home/profile) in Bito Cloud. Here is a quick video walkthrough.&#x20;

{% embed url="<https://www.loom.com/share/2b8100233f2145a5ad792cd6e1d9e8b0>" %}
Setting AI output language in Bito
{% endembed %}

**Supported Languages:**

Bito offers 20+ languages for you to choose from. Here is the list of currently supported languages:

1. English **(Default Language)**
2. Bulgarian (български)
3. Chinese (Simplified) (简体中文)
4. Chinese (Traditional) (繁體中文)
5. Czech (čeština)
6. French (français)
7. German (Deutsch)
8. Hungarian (magyar)
9. Italian (italiano)
10. Japanese (日本語)
11. Korean (한국어)
12. Polish (polski)
13. Portuguese (português)
14. Russian (русский)
15. Spanish (español)
16. Turkish (Türkçe)
17. Vietnamese (Tiếng Việt)
18. Dutch (Nederlands)
19. Hebrew (עִברִית)
20. Arabic (عربي)
21. Malay (Melayu)
22. Hindi (हिंदी)

**Using the Language Support Feature**

Once you have selected your preferred language, Bito will communicate with you in your selected language. Take full advantage of this feature by:

* Asking questions or giving commands to Bito in your selected language
* Receiving responses and outputs from Bito in the language you've selected

Note: All responses from Bito will appear in the selected language, regardless of the input language

Enjoy the convenience of conversing with Bito in your native language and take your coding experience to a new level!&#x20;


# Managing user access levels

Understanding User Roles in Bito Workspaces

A Bito Workspace represents your organization. It is the highest level of organization in Bito.  &#x20;

In a Bito Workspace, different user types play distinct roles in managing and collaborating within the workspace. Here is an overview of the three user types: **Owner, Admin, and User**. Understanding these roles will help you effectively manage your workspace and optimize team collaboration.&#x20;

**Owner:** The Owner holds the highest level of authority within the workspace&#x20;

**Admin:** Admins have a significant role in managing the workspace alongside the Owner&#x20;

**User:** Users have access to the workspace with limited administrative privileges&#x20;

Here's a table summarizing the roles of the different user types in a Bito Workspace:

<table><thead><tr><th width="292"></th><th>Owner</th><th>Admin</th><th>Member</th></tr></thead><tbody><tr><td>Make or Remove Other Owner</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Promote another user to admin or remove admin</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Manage Subs and Billing</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Manage Overage Limits</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Add Member by E-mail</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Access and Share Join workspace link</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Deactivate Member</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Edit WS Settings - Name, Discovery</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Approve Member [When joining from the "Invite Workspace" web link]</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Force Reauthentication</td><td>Yes</td><td>Yes</td><td>No</td></tr></tbody></table>


# Access key

An alternative to standard email and OTP authentication

**Bito Access Key** allows for an alternate authentication mechanism in contrast to the standard Email & OTP based authentication. Access Keys can be created via the [Bito Web UI](https://alpha.bito.ai/) and utilized within the [Bito CLI](https://docs.bito.ai/other-bito-ai-tools/bito-cli). This guide outlines the process of creating or deleting an Access Key.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ft16iiwHjspLM4hlT1BrD%2Fscrnli_kddkiyfRuZeUdC.png?alt=media&#x26;token=422dec4b-a477-48c2-8efb-fe587842260c" alt=""><figcaption></figcaption></figure>

## Creating an Access Key&#x20;

Follow these steps to create a Bito Access Key:&#x20;

1. Log in to your account at: <https://alpha.bito.ai/>&#x20;
2. Navigate to **Settings > Advanced settings** by [visiting this link](https://alpha.bito.ai/home/advanced).
3. Click the **Create new key** button.
4. Enter a name for your Bito Access Key to make it easily identifiable.
5. Click **Create Bito Access Key** to generate your key.
6. Copy the key immediately, as it will not be displayed again after you close the popup.

{% hint style="info" %}
It's crucial to protect your Bito Access Key. Avoid checking it into your code repositories to prevent accidental exposure. If you suspect that your Bito Access Key has been compromised, promptly delete it and create a new one. You can do this anytime.
{% endhint %}

{% hint style="info" %}
You can create multiple Bito Access Keys to use in different projects.
{% endhint %}

## Deleting an Access Key&#x20;

To delete an existing Bito Access Key, follow these steps:&#x20;

1. Log in to your account at: <https://alpha.bito.ai/>&#x20;
2. Navigate to **Settings > Advanced settings** by [visiting this link](https://alpha.bito.ai/home/advanced).
3. Click the **trash icon** next to the Bito Access Key you want to delete.
4. A confirmation popup will appear asking if you are sure you want to delete the key. Click **Yes** to proceed.

{% hint style="info" %}
Once a Bito Access Key is deleted, it cannot be recovered. So, before deleting a key, ensure it is not in use.
{% endhint %}


# Billing and plans

Learn About Subscription Plans, Payment Methods, and Refunds.

<table data-view="cards"><thead><tr><th data-type="content-ref"></th><th></th></tr></thead><tbody><tr><td><a href="billing-and-plans/overview">overview</a></td><td>Guide to billing and paid plans</td></tr><tr><td><a href="billing-and-plans/payment-methods">payment-methods</a></td><td>Learn how to pay and manage your payment methods</td></tr><tr><td><a href="billing-and-plans/managing-workspace-plan">managing-workspace-plan</a></td><td>Upgrade or downgrade your subscription anytime!</td></tr><tr><td><a href="billing-and-plans/pay-for-additional-workspace-members">pay-for-additional-workspace-members</a></td><td>Learn how payments work when you invite a coworker to the workspace</td></tr><tr><td><a href="billing-and-plans/advanced-ai-requests-usage">advanced-ai-requests-usage</a></td><td>Manage your spending to avoid unexpected expenses</td></tr><tr><td><a href="billing-and-plans/billing-history">billing-history</a></td><td>Access your payment records</td></tr><tr><td><a href="billing-and-plans/billing-details">billing-details</a></td><td>Manage your billing address and other details</td></tr><tr><td><a href="billing-and-plans/security">security</a></td><td>How stripe protects your sensitive information</td></tr><tr><td><a href="billing-and-plans/refund-policy">refund-policy</a></td><td>We currently do not give refunds</td></tr><tr><td><a href="billing-and-plans/discounts">discounts</a></td><td>We currently do not offer discounts</td></tr></tbody></table>


# Overview

Guide to Billing and Paid Plans

Bito offers four pricing plans designed to support developers and teams of all sizes:&#x20;

1. Free Plan
2. Team Plan
3. Professional Plan
4. Enterprise Plan

Read more details on [**Bito's Pricing**](https://bito.ai/pricing/) page or watch the video below to learn how billing and paid plans work in Bito.

{% embed url="<https://www.youtube.com/watch?v=Xx8vSb5HhXk>" %}

## Free Plan

Bito's **Free Plan** is available at no cost and provides a powerful set of capabilities for individual and hobbyist developers.

**The Free Plan includes:**

* [**Free AI-powered pull request summaries**](https://docs.bito.ai/ai-code-reviews-in-git/key-features#pull-request-summary) for GitHub, GitLab, and Bitbucket
* [**30+ programming languages**](https://docs.bito.ai/ai-code-reviews-in-git/supported-programming-languages-and-tools) supported (including Python, JavaScript, TypeScript, Go, Rust, and more)
* [**20+ output languages**](https://docs.bito.ai/ai-code-reviews-in-git/supported-programming-languages-and-tools#supported-output-languages-for-code-review-feedback) available (including English, Chinese, Spanish, and more)

<a href="https://bito.ai/pricing/" class="button primary">Learn more</a>

## Team Plan

The **Team Plan** is designed for small to medium teams (up to 25 seats) who need advanced code review capabilities. It includes all the features of the **Free Plan**, and also provides access to premium features.

The **Team Plan** uses best-in-class AI models such as Claude Sonnet 4, OpenAI's GPT-4o, and Anthropic's Claude Sonnet 3.5.

**Pricing:**

* **Annual:** $12 per seat per month (billed annually)
* **Monthly:** $15 per seat per month (billed monthly starting on the 1st of the month)

**The Team Plan includes:**

* Everything in Free Plan, plus
* Unlimited, [**codebase-aware AI code reviews**](https://docs.bito.ai/ai-code-reviews-in-git/key-features#ai-that-understands-your-code) in Git
* Supports multiple Git platforms, such as:
  * [GitHub](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github)
  * [GitHub (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github-self-managed)
  * [GitLab](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab)
  * [GitLab (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab-self-managed)
  * [Bitbucket](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket)
  * [Bitbucket (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket-self-managed)
* [**Chat with Bito Agent in pull requests**](https://docs.bito.ai/ai-code-reviews-in-git/chat-with-ai-code-review-agent)
* [**Changelist**](https://docs.bito.ai/ai-code-reviews-in-git/key-features#changelist) (A table that shows what changed in a pull request)
* [**Line-by-line reviews**](https://docs.bito.ai/ai-code-reviews-in-git/key-features#one-click-to-accept-suggestions) with actionable code suggestions
* [**Analytics**](https://docs.bito.ai/ai-code-reviews-in-git/code-review-analytics) (Get in-depth insights into your code review process)
* [**AI code reviews in supported code editors**](https://docs.bito.ai/ai-code-reviews-in-ide/overview) (VS Code, Cursor, Windsurf, and all JetBrains IDEs)
* [**50 AI Chat requests per user per day**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito) in Bito IDE extension
  * ***Note:** Free trial users are limited to 20 AI Chat requests per day.*
* [**Templates**](https://docs.bito.ai/ai-code-reviews-in-ide/templates) provide ready-made checks to help you quickly analyze and refine your code in the editor.

<a href="https://bito.ai/pricing/" class="button primary">Learn more</a>

## Professional Plan

The **Professional Plan** is designed for growing teams and organizations that need advanced capabilities beyond the **Team Plan**.

**Pricing:**

* **Annual:** $20 per seat per month (billed annually)
* **Monthly:** $25 per seat per month (billed monthly starting on the 1st of the month)

**The Professional Plan includes:**

* Everything in Team Plan, plus:
* Unlimited seats
* [**Custom code review guidelines**](https://docs.bito.ai/ai-code-reviews-in-git/implementing-custom-code-review-rules)
* [**Jira integration**](https://docs.bito.ai/ai-code-reviews-in-git/jira-integration)
* Code reviews in CI/CD pipelines
* Self-hosted for $5 per seat a month
* Learning system that adapts to your team's preferences
* Dedicated Slack with Bito team
* Increased code review limits in your IDE

<a href="https://alpha.bito.ai/home/welcome" class="button primary">Start your 14-day free trial</a>

## Enterprise Plan

The **Enterprise Plan** is aimed at large organizations. It includes all **Professional Plan** features and also provides access to premium features.

**The Enterprise Plan includes:**

* Everything in Professional Plan, plus
* Bito's AI Architect ([learn more](https://bito.ai/product/ai-architect))
* Impact analysis across your codebase, services, modules
* Code reviews in CI/CD pipelines
* On-prem or self-hosted
* Multi-org support
* Customer support
  * Dedicated CSM
  * SLA support
  * Agreement redlines
  * Custom invoicing and payment terms
* Security and compliance
  * SSO, SCIM, and SAML (Coming soon)
  * Audit Logs (Coming soon)

<a href="https://bit.ly/contact-bito-sales" class="button primary">Contact us to upgrade to Enterprise Plan</a>

## Seat management

Bito uses seat-based billing to give workspace admins precise control over usage and costs.

From the [**Members**](https://alpha.bito.ai/home/members) dashboard, workspace admins can choose how seats are purchased and assigned to users.

### Bito provides three modes for seat management:

{% stepper %}
{% step %}

### Auto (Assign & Buy)

In this mode, available seats will be automatically assigned to developers (marked as [Eligible](#assigning-code-review-agent-seats)) when they join the workspace or when they submit their first pull request reviewed by Bito. If all seats are assigned, new seat is purchased and assigned automatically.

* ***Note:** This mode is useful for dynamic teams where new contributors are added frequently.*
* ***Note:** This is the default mode for all new workspaces.*
  {% endstep %}

{% step %}

### Auto (Assign only)

In this mode, available seats will be automatically assigned to developers (marked as [Eligible](#assigning-code-review-agent-seats)) when they join the workspace or when they submit their first pull request reviewed by Bito. If no seats are available, Bito will not purchase additional seats, and the developer will not gain access to Bito features.
{% endstep %}

{% step %}

### Manual

In this mode, workspace admins need to manually purchase seats and [assign them to developers](#assigning-code-review-agent-seats) as needed. Bito will review pull requests only for submitters who have an assigned seat.

* ***Note:** This mode is ideal for teams that want tighter control over who gets access and when billing occurs.*
  {% endstep %}
  {% endstepper %}

{% hint style="info" %}
The **Team Plan** supports up to 25 seats, whereas the **Professional Plan** and **Enterprise Plan** allows for unlimited seats.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FoBDDPHO2bhUpFw3iulTP%2Fscrnli_QJ3jsjfiDcfrSt.png?alt=media&#x26;token=fa7b5c66-b351-4b33-829f-99160e219311" alt=""><figcaption></figcaption></figure>

## Add or remove seats manually

Workspace admins can manually purchase additional seats or remove unused ones.

1. Go to the [**Members**](https://alpha.bito.ai/home/members) dashboard and click the **settings** icon at the top-right corner of the table.
2. In the popup, use the **`+`** and **`−`** icons to adjust the seat count.
3. Click **Confirm** to apply the changes.

{% hint style="info" %}
Seat adjustments take effect immediately. If seats are added mid-month, the charges are prorated for the remaining days of the billing cycle.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FGG8a1b2kqUDvV6VMvG8I%2Fscrnli_y0t19cms654sc8_1.png?alt=media&#x26;token=cb131a06-0992-4e74-9e9b-3f9a18b75a1e" alt=""><figcaption></figcaption></figure>

## Seat assignment across Bito products

Seats apply separately to each Bito product:

* **IDE Code Review**\
  Seats for AI code review in code editors can be assigned to any user in a workspace. These users appear under the **IDE Code Review** tab on the [**Members**](https://alpha.bito.ai/home/members) dashboard.
* **Git Code Review**\
  Seats for the AI code review in GitHub, GitLab, and Bitbucket are tied to Git handles that submit pull requests. These handles appear under the **Git Code Review** tab.
  * In **Auto (Assign & Buy) mode**, seats are assigned (and purchased if necessary) as soon as a Git handle submits its first pull request.
  * In **Auto (Assign only) mode**, available seats are assigned as soon as a Git handle submits its first pull request. If no seats are available, Bito will not purchase additional seats, and the developer will not gain access to the AI Code Review Agent.
  * In **Manual mode**, admins must assign seats manually to these Git handles before they can use the AI Code Review Agent.

### Assigning Code Review Agent seats

To manage seat access for your team:

1. Go to the **Git Code Review** tab on the [**Members**](https://alpha.bito.ai/home/members) dashboard.
2. Find the developer’s **Git handle** (imported automatically after GitHub, GitLab, or Bitbucket integration).
3. Use the drop-down menu in front of the Git handle and choose one of the following seat statuses:
   * **Assigned** – Immediately gives the user access to Bito features (such as the AI Code Review Agent).
   * **Eligible** – Marks the user to automatically receive a seat when one becomes available.
     * **Note:** This option only applies when your Bito workspace is using **Auto (Assign & Buy)** or **Auto (Assign only)** mode.
   * **Ineligible** – The user will not receive a seat or access to Bito features.

{% hint style="info" %}
**Note:**

* In **Auto (Assign & Buy)** or **Auto (Assign only)** mode, available seats are automatically assigned to developers marked as **Eligible**.
* In **Manual** mode, seats must be explicitly assigned to developers by selecting **Assigned** from the drop-down menu.
  {% endhint %}

***

All billing and plans functionality is available at [Bito’s website](https://alpha.bito.ai/) by logging in with your email. Additionally, from Bito's IDE plug-in, click on the hamburger menu icon in the top-right corner (denoted by three horizontal lines) and select **Account Settings** to redirect to Bito's website.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FcHvilqSXXduIm3igyV89%2Fscrnli_7_26_2024_9-49-18%20AM.png?alt=media&#x26;token=87f0ff33-b19f-45c5-8582-a93dd6d6317d" alt="" width="473"><figcaption></figcaption></figure>

From there you can go to the [**Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page to access the billing functionality.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5R1bjWqVQLKkHkWMkwJd%2Fbilling_ss_2.jpg?alt=media&#x26;token=7b95aac3-8060-442a-a286-d9a6f563a344" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** You cannot make billing changes directly from the Bito IDE extension.
{% endhint %}

Bito uses Stripe to handle all payment processing and securely store your credit card/payment information. Bito itself does not store your credit card/payment information.&#x20;

Bito bills at the Workspace level. All users within a given Workspace will be billed on the same plan. You cannot have some users on the **Team Plan** and some users on the **Free Plan**, within the same workspace.

When you [signed up for Bito](https://docs.bito.ai/help/account-and-settings/creating-a-bito-account), you [created or joined a workspace](https://docs.bito.ai/help/account-and-settings/workspace). Primary Owners, Owners, and Admins can change the billing plan for a workspace. You can see your workspace by going to [Home page](https://alpha.bito.ai/) or [Workspace Settings](https://alpha.bito.ai/home/settings/advance-settings) page. You can see your Role by going to [Members](https://alpha.bito.ai/home/settings/members) page. You can change your workspace by logging out, and when you log-in, you will choose which workspace you want to be a part of. It’s similar to Slack, where you can access different workspaces.&#x20;

Within each Workspace, Bito bills at the seat (sometimes referred to as “user”) level from the first of the month to the last day of the month. So, if you have 12 users in your Workspace (let’s call it the “MyCompany” workspace), when an Admin signs up for the **Team Plan**, the “MyCompany” workspace will be billed for all 12 users. Bito’s **Team Plan** costs $15 per user per month. So, you will pay $180 per month for 12 users, and that will be charged on the 1st of the month for the next month. To give an example, on September 1, you would be charged $180 for the month of September.  Any overages you had in terms of accessing Advanced AI models for the month of August, would also be charged on September 1.

{% hint style="info" %}
To repeat, each month’s bill will include your base $15 per month fee per user for the current month, and the overage charges for the previous month.
{% endhint %}

Your first month when you sign up, you will be billed for the current month in a prorated fashion.  For example, if you signed up in the middle of March, you would be billed $7.50 per seat (half of the $15 full month fee). &#x20;

For any additional questions, please review the documentation we have. In addition, please feel free to contact Bito at [**support@bito.ai**](mailto:support@bito.ai) with any questions.


# Payment methods

Learn How to Pay and Manage Your Payment Methods

## Supported Payment Methods

We use [Stripe](https://stripe.com/) as our trusted payment handler to ensure seamless and secure transactions. We offer a variety of convenient payment methods to cater to your preferences.&#x20;

### Below is a list of accepted payment methods:

* Credit and Debit Cards (Visa, Mastercard, American Express, Diners, Discover, JCB, and China Union Pay)&#x20;
* Google Pay, Apple Pay, Alipay, Cash App Pay&#x20;
* Bank Accounts in the US and many other countries

## Manage (Add or Delete) Payment Methods&#x20;

Payment methods for Bito are managed securely by Stripe. You can add or delete payment methods if you want.

{% hint style="info" %}
Managing payment methods functionality is not available for workspaces on the **Free Plan**.
{% endhint %}

### To add a new payment method, follow these steps:&#x20;

1. Go to the [**Manage Subscription > Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page.
2. Click on the "Edit payment methods" button.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fb8doLKuEnZshKK326xJl%2Fb4_1.png?alt=media&#x26;token=ea6fdf59-16fa-4f0b-8110-9a67c4b18a11" alt=""><figcaption></figcaption></figure>
3. On this page, you will see your currently active plan as well as your existing payments method attached to your account.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FajJR8EBRTyQRmlod4uFw%2Fb5.jpg?alt=media&#x26;token=9ece712e-a032-471f-9706-c7b539b5ea34" alt=""><figcaption></figcaption></figure>
4. Click on the "Add payment method" button.&#x20;
5. A form will open through which you can add any of our supported payment methods mentioned above.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrZls12xmOtVfekWx494k%2Fb6.jpg?alt=media&#x26;token=e7156a52-5993-4256-830b-ef2e9b81d419" alt="" width="375"><figcaption></figcaption></figure>
6. Fill in the form and press the "Add" button to add a new payment method.

### To delete a payment method, follow these steps:&#x20;

1. Go to the [**Manage Subscription > Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page.
2. Click on the "Edit payment methods" button.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fb8doLKuEnZshKK326xJl%2Fb4_1.png?alt=media&#x26;token=ea6fdf59-16fa-4f0b-8110-9a67c4b18a11" alt=""><figcaption></figcaption></figure>
3. On this page, you will see your currently active plan as well as your existing payments method attached to your account.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FaTEvGKSjQeRE2AFcThMj%2Fb7.jpg?alt=media&#x26;token=7c32c832-8ce7-4536-abbf-e86a27bdc971" alt=""><figcaption></figcaption></figure>
4. Click on the three dots button in front of the payment method you want to delete.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FzdiAnWjFWFDMmbMzvDoO%2Fb8_1.png?alt=media&#x26;token=aafb818d-51e3-49b4-8317-71c2abca8c80" alt=""><figcaption></figcaption></figure>
5. Now click "Delete" from the popup menu.&#x20;
6. A warning popup box will open, asking you to confirm whether you really want to delete the payment method.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjWLoKkOWPg55cfWUBEgj%2Fb9_1.png?alt=media&#x26;token=2b3ab6fc-1c5a-4d88-af8b-7eb3df6044bd" alt=""><figcaption></figcaption></figure>
7. Simply click the "Delete payment method" button on this warning popup to remove this payment method from your account.
8. As you can see in the below screenshot, the "Visa" payment method is removed successfully.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FR4l4WYAUOQFGdgMWULmU%2Fb10.jpg?alt=media&#x26;token=ac182b01-e283-49ca-89f7-bd5182e3dea4" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you currently have an active paid plan and only one payment method is attached to your account, then you won't be able to delete it. You can only delete secondary payment methods.
{% endhint %}


# Managing workspace plan

Upgrade or Downgrade Your Subscription Anytime!

## How to Upgrade Workspace Plan?&#x20;

Follow the below steps to upgrade from **Free Plan** to **Team Plan**:&#x20;

1. Go to the [**Manage Subscription > Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page.&#x20;
2. In the **Current plan** section, click the "Change plan" button.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FgSam5K2vi8ClVGDOhM7H%2Fb3_1.png?alt=media&#x26;token=a4c0306d-6ac0-460c-bb0b-286b77dc527a" alt=""><figcaption></figcaption></figure>
3. On this page, you will see your **current plan (i.e., Free Plan)** as well as the **Team Plan**.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZcn4r8iBbqKohgNeIoXZ%2Fscrnli_8_30_2024_10-35-56%20AM.png?alt=media&#x26;token=eada7860-a589-4dbc-8455-b03e4cca1903" alt=""><figcaption></figcaption></figure>
4. Click the "Upgrade" button provided in the **Team Plan**. This action will redirect you to the secure Stripe Checkout page.
5. On the Stripe Checkout page, you can see the price you have to pay, as well as the form where you can enter your payment details. The price you will see for the **Team Plan** will depend on the number of days and time left in the current month as well as the total number of members in your workspace. Here's a list of [**Payment Methods**](https://docs.bito.ai/help/billing-and-plans/payment-methods) we accept.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FwB9Gvcy8BhIUh2uWBXtc%2Fb12.jpg?alt=media&#x26;token=0ebf50d9-be03-4dbd-a022-3596e37d804c" alt=""><figcaption></figcaption></figure>
6. Select your preferred payment method, fill in the form, and click on the “Subscribe” button.
7. After completing the transaction, you will be redirected to Bito where a confirmation message will be shown.
8. As you can see in the below screenshot, your workspace plan has successfully upgraded from **Free Plan** to **Team Plan**.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOnSiDVjdYSjeKFfEQd8X%2Fb13.jpg?alt=media&#x26;token=70783eb5-6197-408f-b361-8c6c87f275e8" alt=""><figcaption></figcaption></figure>

That's it! You can now start using the features of **Team Plan**.&#x20;

## How to Downgrade/Cancel Workspace Plan?&#x20;

You can cancel your paid plan at any time and move back to the **Free Plan**. When you do cancel, you will retain the use of your paid plan until the end of the billing cycle as you have already paid for that. At this time, we are unable to offer refunds. Also, any additional usage beyond the allocated limit of your paid plan will be charged in the next billing cycle.&#x20;

Follow the below steps to downgrade from **Team Plan** to **Free Plan**:

1. Go to the [**Manage Subscription > Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page.&#x20;
2. In the **Current plan** section, click the "Cancel plan" button.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKLXQaFmei34bOoAgUyig%2Fb14_1.png?alt=media&#x26;token=beecf109-d874-46a5-8865-7d92fa6b5863" alt=""><figcaption></figcaption></figure>
3. A popup will appear. It has two steps.&#x20;

   * In the first step, you have to select a reason for canceling your plan. It will help us improve Bito. After selecting a reason, click “Continue to cancel”.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOxwaKee18rXpDwQUdcaw%2Fb15_1.png?alt=media&#x26;token=c03cc8f9-2068-48ee-a839-8cc820abf7d9" alt=""><figcaption></figcaption></figure>

   * The second step provides you with some information about what to expect after your plan is canceled. If all looks good press the “I want to cancel” button to cancel your subscription.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbyCmP1HPnW4V0jr9qHq5%2Fscrnli_10_13_2023_12-37-24%20PM_cropped.png?alt=media&#x26;token=3ae1fc30-163f-4177-8ee3-3cf8145dd4ff" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Once you cancel your subscription, you can easily renew it before the next billing cycle.
{% endhint %}

## How to Renew Workspace Plan?&#x20;

To renew your Workspace plan, follow these steps:&#x20;

1. Go to the [**Manage Subscription > Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page.&#x20;
2. In the “Current plan” section, click the "Renew plan" button. You will be redirected to a secure page powered by Stripe.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fjvidc3f3dSeAeMLO5V6x%2Fb19_1.png?alt=media&#x26;token=6ef83e42-9dd3-4aa1-aef9-79d93a7cc530" alt=""><figcaption></figcaption></figure>
3. If you had previously cancelled your subscription plan, you will see the details of your cancelled plan on this page, along with a “Renew plan” button.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fym0ZO1c599iOytek2EeX%2Fb20_1.png?alt=media&#x26;token=aabcf42a-8674-4022-bafc-50fd53986cea" alt=""><figcaption></figcaption></figure>
4. Click on the “Renew plan” button to proceed with the renewal process.&#x20;
5. On this page, you will find all the details of your previously cancelled plan before you renew it.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fy8CqxqPHpa6tl5zNKtoR%2Fb21_1.png?alt=media&#x26;token=cdd32ea1-2523-4ecd-be10-c099d76e3156" alt=""><figcaption></figcaption></figure>
6. Click on the “Renew plan” button to complete the renewal of your subscription or press the “Go back” button to return to the previous screen.


# Pay for additional workspace members

Learn How Payments Work When You Invite a Coworker to the Workspace

If your workspace is using the **Free Plan**, your account will not be charged when you invite new members. However, if your workspace has subscribed to the **Team Plan**, each member you invite will be charged based on the price of the **Team Plan** and the number of days and time left in the current month. Additionally, the **600 Advanced AI Model requests** will be added to the total quota of the workspace for each member invited.

Read more at [**Bito's pricing page**](https://bito.ai/pricing/).

## Inviting coworkers to the Workspace

1. Go to the [**Manage Users > Members**](https://alpha.bito.ai/home/settings/members) page.
2. Click on the “Invite members” button.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FxWDeKxAoMsvDnoJXTr1J%2Fb22_1.png?alt=media&#x26;token=95ddda39-eb68-4a6f-86b2-f05557404f48" alt=""><figcaption></figcaption></figure>
3. A form will open in a popup box.&#x20;
4. Enter emails of your coworkers that you want to add in the workspace.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FwKHtUMFjRNebKIsLZcGh%2Fb23_1.png?alt=media&#x26;token=12b5e987-867f-4aca-84b3-7e9768d9c725" alt=""><figcaption></figcaption></figure>
5. Press the “Send” button to proceed.&#x20;
6. A warning message will appear informing you that inviting new members to the workspace will result in additional charges.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fq2JecMKEnI2YtiS8Vv1Z%2Fb24_1.png?alt=media&#x26;token=e94806bf-8329-43bf-b135-2dc5a154ed03" alt=""><figcaption></figcaption></figure>
7. If you are ok with that, press the “Invite members” button to send the invitation.

{% hint style="info" %}
When the invited person joins the workspace, the billing account attached to the workspace will be charged automatically.
{% endhint %}


# Advanced AI requests usage

View and manage your workspace usage to avoid unexpected expenses.

If you are on a paid plan, such as the **Team Plan**, and are the owner or admin of a workspace, you can easily view the **Advanced AI Model requests** (GPT-4o or similar) included for the current month and the number of requests used by your workspace members and AI Agents.

{% hint style="info" %}
If you are on the **Free Plan**, this plan does not include Advanced AI Model requests, so this feature is not relevant to your plan.
{% endhint %}

To view your usage, simply visit the [**Settings > Requests Usage**](https://alpha.bito.ai/home/bito-premium/ai-request-usage) dashboard.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FLvhkrI1qRsPMv3sZgAah%2Fscrnli_BhFvQLrCPOhJD5.png?alt=media&#x26;token=dd474bb4-436e-43d1-b279-0e4173406b33" alt=""><figcaption></figcaption></figure>

## What is an Advanced AI Model Request?&#x20;

Bito uses best-in-class AI models (such as GPT-4o, Claude Sonnet 3.7, and similar models) to offer its services. These are known as **Advanced AI models** and are only accessible through our [paid plans](https://bito.ai/pricing/).

When your **Advanced AI Model Request** quota is used up, [AI Chat](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito) requests will be blocked for the rest of the day and will become available again the next day.


# Billing history

Access Your Payment Records

Bito maintains your billing history through [Stripe](https://stripe.com/).&#x20;

To view your past payments, follow these steps:&#x20;

1. Open the [**Manage Subscription > Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page.
2. Click on the "View billing history" button. You will be redirected to a secure page powered by Stripe.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRb33gTAF6OgFdiXVFpRK%2Fb4_2.png?alt=media&#x26;token=88e3d3f5-3365-4c8f-8825-b4aaf2bb9133" alt=""><figcaption></figcaption></figure>
3. On this page, you will see your complete billing history.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQHX1PeSDNM8hVAz8N0fu%2Fb29.jpg?alt=media&#x26;token=6639753e-fb62-4634-b429-064add048209" alt=""><figcaption></figcaption></figure>
4. Open a specific invoice to view its complete details.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F6qJIfI9mVamzu3aHyEM0%2Fb29_1.png?alt=media&#x26;token=4ecf17fa-034a-4dfa-9952-66823a2347b2" alt=""><figcaption></figcaption></figure>
5. From the invoice page, you can view more details by clicking “View invoice and payment details”.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FS4UIXR3FcXygpHsZHZgu%2Fb30_1.png?alt=media&#x26;token=6c659668-c857-4a36-9dd0-da6ec8e0a4e6" alt=""><figcaption></figcaption></figure>

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FTHNG3xeGg1qE7Tj6B6by%2Fb31.png?alt=media&#x26;token=c0093158-0f20-4196-930b-ffcee9cb74c0" alt=""><figcaption></figcaption></figure>
6. &#x20;You can also download the invoice and the receipt from this page by clicking the “Download invoice” and “Download receipt” buttons respectively.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNx8WhbD71HFZFPb1gjsx%2Fb30_2.png?alt=media&#x26;token=1ddd7cd3-723e-4f34-8946-30b07803c28f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Billing History functionality is not available for workspaces on the **Free Plan**.
{% endhint %}


# Billing details

Manage your billing address and tax (VAT, GST, etc) details.

## Add or Update Billing Address

1. Open the [**Manage Subscription > Billing and Plans**](https://alpha.bito.ai/home/settings/bito-premium/billing) page.
2. Click on the "Edit billing details" button. You will be redirected to a secure page powered by Stripe.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvXmD9GsC6iMGnhY5KfDs%2Fscrnli_10_13_2023_3-20-38%20PM_cropped.png?alt=media&#x26;token=743391c3-2ed4-47d9-8008-5dce602eede9" alt=""><figcaption></figcaption></figure>
3. On this page, you will see your current plan details as well as billing information such as address. Click on "Update information" button to add/edit your billing details.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqkOFaeSsEvCiidfMDovc%2Fscrnli_10_13_2023_3-21-16%20PM_cropped.png?alt=media&#x26;token=1a0af9ca-13eb-463b-9da4-75ec6b42697e" alt=""><figcaption></figcaption></figure>

4. Now, you will see a form through which you can add your billing information such as the billing address and tax (VAT, GST, etc) details. Click on the "Save" button to save your changes or click on the "Cancel" button to return to the previous screen.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FiL84s7NmUEnAfxPHy8CI%2Fscrnli_ZCA7fAh2h28iGG.png?alt=media&#x26;token=13225208-e8ba-4c05-8631-c456e6a4fa05" alt="" width="384"><figcaption></figcaption></figure>


# Security

How Stripe Protects Your Sensitive Information

We understand that the security of your payment information is of utmost importance. That's why we have partnered with Stripe, a globally recognized and trusted payment platform, to ensure that your sensitive data remains safe and secure throughout the payment process.&#x20;

If you have any questions, please contact us at [**support@bito.ai**](mailto:support@bito.ai)&#x20;

## Why Stripe?&#x20;

When you subscribe to our paid plans, we rely on Stripe's robust infrastructure to handle your payment details securely.&#x20;

**Here's why we chose Stripe as our trusted payment handler:**&#x20;

### 1. PCI Compliance&#x20;

Stripe is certified as a Level 1 Service Provider under the Payment Card Industry Data Security Standard (PCI DSS). It is the most stringent level of certification available in the payment industry. This means that Stripe adheres to strict security standards and undergoes regular audits to ensure compliance.&#x20;

It ensures that all cardholder data is handled securely throughout the payment journey.&#x20;

&#x20;Rest assured that your sensitive card information is securely handled at all times. Neither Bito nor Stripe stores your sensitive data on their servers. Even our staff cannot access it. Your payment details are safe with us.&#x20;

### 2. GDPR Compliance&#x20;

Stripe also complies with the General Data Protection Regulation (GDPR) and regularly undergoes audits to maintain its certifications.&#x20;

### 3. Secure API Communication&#x20;

All communication between Bito and Stripe occurs through secure APIs (Application Programming Interfaces). These APIs are designed to transmit data in an encrypted format, adding an extra layer of security to the payment process.&#x20;

### 4. Data Encryption&#x20;

All data transmitted to Stripe is encrypted using industry-standard encryption protocols, such as TLS (Transport Layer Security). This ensures that sensitive information, including credit card details and personal data, is protected during transit.&#x20;

### 5. Secure Card Information Handling&#x20;

Stripe follows the principle of "security by design" and does not store cardholder data on its servers. Instead, it utilizes tokenization, a process that replaces sensitive card information with unique tokens. These tokens are used for subsequent transactions, reducing the risk of unauthorized access to card data.&#x20;

This means that even if Stripe's systems were compromised, your original card information would remain safe as the token holds no value to potential attackers.&#x20;

### 6. Intrusion Detection and Prevention&#x20;

Stripe maintains a comprehensive intrusion detection and prevention system to monitor and block any unauthorized attempts to access its systems. Suspicious activities are flagged in real-time, and appropriate action is taken to mitigate potential threats.&#x20;

### 7. Radar Fraud Detection&#x20;

Stripe's Radar uses machine learning algorithms to detect and prevent fraudulent transactions in real-time. This intelligent system constantly evolves and adapts to new fraud patterns, providing enhanced protection for Bito's customers.&#x20;

### 8. Continuous Monitoring&#x20;

Stripe conducts regular security assessments and audits to identify vulnerabilities and address potential weaknesses in its systems. This continuous monitoring approach allows them to stay proactive in the face of emerging security risks.


# Refund policy

We Currently Do Not Give Refunds

To ensure that you are not billed for the upcoming month, kindly cancel your subscription before the 1st day of the upcoming month.




---

[Next Page](/llms-full.txt/1)

