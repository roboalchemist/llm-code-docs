# Source: https://docs.bito.ai/changelog/previous-releases.md

# Previous releases

{% hint style="info" %}
[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

{% hint style="info" %}
Want to see what’s new? Check out the latest updates on our [**Changelog**](https://docs.bito.ai/changelog) page.
{% endhint %}

## IDE V1.5.9 - 8th Aug 2025

### Transitioning Bito's IDE extension to AI Code Reviews

Over the coming weeks, Bito is focusing its IDE extension's core functionality from AI Chat and Code Completions into a powerful utility experience for software engineers: an agentic, codebase-aware AI Code Review Agent in your VS Code and JetBrains IDE.

<mark style="color:blue;">**What’s being added**</mark>

**Bito AI Code Reviews in IDE:** Available in limited beta for VS Code and JetBrains IDEs. Offers real-time feedback on code changes, directly in your editor.

<p align="center"><a href="https://marketplace.visualstudio.com/items?itemName=Bito.Bito" class="button primary">Install for VS Code</a><a href="https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant" class="button primary">Install for JetBrains</a></p>

The upcoming **`@codereview`** command in the chat box will let you run the following code reviews:

* **localchanges** – Review local changes&#x20;
* **stagedchanges** – Review staged changes&#x20;
* **path** – Review a single file or multiple files&#x20;
* **commitId** – Review a single commit or a range of commits&#x20;

If you’d like access to the beta, [email us at support@bito.ai](mailto:support@bito.ai?subject=Beta%20access%20to%20AI%20Code%20Reviews%20in%20IDE\&body=Hello!%20My%20name%20is%20______%20and%20I%20work%20for%20______.%20I%27d%20like%20to%20preview%20Bito%27s%20AI%20Code%20Reviews%20for%20my%20IDE.%20Today%2C%20I%20use%20______%20\(VS%20Code%20or%20JetBrains\).).

<p align="center"><a href="../ai-code-reviews-in-ide/overview" class="button primary">Learn more</a></p>

<mark style="color:blue;">**What’s being removed**</mark>

By end of August (and your next monthly billing cycle), the following features will be removed from the IDE extension:&#x20;

* AI Code Completions&#x20;
* Prompt Templates&#x20;
* Parts of AI Chat in your IDE not associated with AI Code Reviews&#x20;

These features are deprecated from the IDE extension to reduce surface area and double down on quality, context-aware reviews. Fortunately, there are many tools available that focus on these engineering features. \
&#x20;

<mark style="color:blue;">**Who gets access**</mark>

Today, the beta of Bito AI Code Reviews in your IDE is limited to select engineering team. If you’d like access, email us at <support@bito.ai>.&#x20;

<mark style="color:blue;">**How will billing change**</mark>

For paying **Team Plan** (formerly known as 10X Developer Plan) customers that use Bito's IDE extension for AI Chat and Code Completion, this will be your last month with access to those features.

You may [update your subscription here](https://alpha.bito.ai/home/bito-premium/change-plan) or remain a customer for access to premium features of Bito's AI Code Reviews in Git and your IDE. [Learn more about AI Code Reviews](https://bito.ai/).

<mark style="color:blue;">**What’s next for Bito**</mark>

Our comprehensive focus on AI Code Reviews across Git and IDEs enables Bito to invest all of its resources in developing and maintaining the highest quality AI powered code reviewing tools on the market. We proudly believe our suite of developer tools are the industry’s best and we intend to keep building the best, for you.

Stay tuned for:&#x20;

* Agentic code reviews with dynamic codebase insight&#x20;
* Native integrations with project management tools
* More programming language support

Have questions or feedback? Email us at <support@bito.ai>.

## AI Code Review Agent - 1st Aug 2025

<mark style="color:blue;">**New feature**</mark>

**Multi-group support for GitLab (Self-Managed):** [Bito Cloud](https://alpha.bito.ai/) now supports selecting **multiple GitLab groups** for [GitLab (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab-self-managed) integrations. Repositories from all selected groups will be available for AI code reviews—making it easier to manage code across teams and projects.

This feature is currently available **only** for **GitLab (Self-Managed)** integrations.

<a href="../../ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab-self-managed#managing-multiple-gitlab-groups-in-bito-cloud" class="button primary">Learn more</a>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FWb7qgTu5Kt8xENYImJar%2Fscrnli_XOow3dK4CvFTuP.png?alt=media&#x26;token=83e7bcd4-957f-4fe5-95c6-f2a1c257daa9" alt=""><figcaption></figcaption></figure>

## AI Code Review Agent - 25th Jul 2025

<mark style="color:blue;">**New feature**</mark>

**Support for Bitbucket (Self‑Managed):** You can now connect Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) to your self-hosted Bitbucket server—bringing intelligent, context-aware code reviews right into your internal environment. Bito automatically reviews pull requests, offering in‑line suggestions, clear PR summaries, and changelist overviews that help your team catch issues faster and merge with greater confidence—all while operating securely within your network perimeter.

<a href="../ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket-self-managed" class="button primary">Learn more</a>

## Bito Cloud - 27th Jun 2025

<mark style="color:blue;">**New feature**</mark>

**Create custom code review guidelines in Bito Cloud:** Workspaces on the [**Enterprise Plan**](https://bito.ai/pricing/) can now create, manage, and apply [**custom code review guidelines**](https://docs.bito.ai/ai-code-reviews-in-git/implementing-custom-code-review-rules#id-2-create-custom-code-review-guidelines) directly from the Bito dashboard—no need to submit them manually anymore.

Previously, Enterprise teams had to send their guidelines to Bito for setup.

With this release, you have full control to define and enforce your team’s coding standards instantly using the [**Custom Guidelines**](https://alpha.bito.ai/home/ai-agents/custom-guidelines) tab.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="../../ai-code-reviews-in-git/implementing-custom-code-review-rules#id-2-create-custom-code-review-guidelines">#id-2-create-custom-code-review-guidelines</a></td></tr></tbody></table>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQvz3VHiBUseFxkQ7VPXJ%2Fscrnli_Vn4xC4eh0BqgU2.png?alt=media&#x26;token=1593f3bc-64a2-4a6f-9263-1030f80fa8ce" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0oCiQLsyfPAq7VnnkVpg%2Fscrnli_SG7HCmG3tbPE6O.png?alt=media&#x26;token=cfa30ebb-a6a0-4534-87af-7ff53ca51e1d" alt=""><figcaption></figcaption></figure>

## Bito Cloud - 17th Jun 2025

<mark style="color:blue;">**New feature**</mark>

**Seat based billing and member management:** We’ve introduced a new seat management system that gives you more visibility and control over how seats are assigned and billed for Bito products — **AI Chat/Wingman** and **AI Code Review Agent**.

From the updated [**Members**](https://alpha.bito.ai/home/members) dashboard, workspace admins can now:

* View and manage seats separately for **AI Chat/Wingman** and **AI Code Review Agent**.
* Choose between **Auto** or **Manual** modes for purchasing and assigning seats.
* Manually purchase, assign, or remove seats directly from the dashboard.
* Track Git handles associated with pull request activity and manage billing accordingly.

This update helps teams better align usage with billing and ensures clarity on who is consuming which product within a workspace.

[**Learn more**](https://docs.bito.ai/help/billing-and-plans/overview#seat-management)

{% embed url="<https://www.youtube.com/watch?v=Xx8vSb5HhXk>" %}

## AI Code Review Agent - 10th Jun 2025

<mark style="color:blue;">**New feature**</mark>

**Agentic code reviews are here:** Bito’s [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git) is now fully Agentic. This update replaces the previous chain-of-thought pipeline with an Agentic approach that dynamically identifies context, generates and validates reviews autonomously, and explores code more freely. The result: deeper issue detection, better code understanding, and higher-quality suggestions with less noise.

## AI Code Review Agent - 9th May 2025

<mark style="color:blue;">**New feature**</mark>

**Request changes in GitLab:** Now, Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git) fully supports GitLab's "Request Changes" feature. Quickly post suggestions and clearly mark merge requests that need further attention—just like you already do in GitHub and Bitbucket. Stay consistent, save time, and streamline your code review workflow across all your favorite Git platforms.

**Improved readability in Bitbucket:** To enhance readability and reduce clutter, we now show a maximum of 10 additional suggestions for Bitbucket code reviews. Focus on the most critical improvements first and make faster decisions with clearer, more concise feedback.

## AI Code Review Agent - 2nd May 2025

<mark style="color:blue;">**New feature**</mark>

**Request changes now works for Bitbucket too:** You can now post AI-generated suggestions as **“Request Changes”** in Bitbucket pull requests—just like on GitHub. This helps you enforce quality standards consistently across both platforms.

**Cleaner, more organized comments on GitHub:** All AI comments now stay in a single thread, making reviews easier to follow. You’ll see the **Changelist** (summary of key changes) at the top, so you can understand what’s changed before diving into the suggestions.

**Smarter AI learning for better reviews:** AI Code Review Agent now processes learned rules in batches—reducing cost and improving performance when applying custom rules across reviews.

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Fixed one-click to accept suggestions:** We’ve fixed issues where some suggestions couldn’t be applied directly. Now, most fixes are just one click away.

## AI Code Review Agent - 25th Apr 2025

<mark style="color:blue;">**New feature**</mark>

**More control with new slash commands:** You now have better control over your code reviews with new commands. Easily `/pause`, `/resume`, or `/abort` reviews across GitHub, GitLab, and Bitbucket. Additionally, you can `/resolve` comments directly within GitLab and Bitbucket, streamlining your review workflow.

* `/pause` - Pauses automatic reviews on this pull request.
* `/resume` - Resumes automatic reviews.
* `/resolve` - Marks all Bito-posted review comments as resolved.
* `/abort` - Cancels all in-progress.

**Improved accuracy in suggestions:** The AI Code Review Agent now accurately identifies which lines have changed, preventing irrelevant suggestions on unchanged lines that appeared due to context lines. This ensures more precise and useful feedback during code reviews.

**Faster code reviews:** AI Code Review Agent now processes trivial code parts in parallel to significantly speeds up overall review times and boosts productivity.

**Streamlined GitHub commenting:** You can now submit comments as "Request Changes" directly within GitHub, improving your feedback process. Additionally, inline comments are processed faster through batching, making your GitHub review workflow smoother.

**Flexible agent configuration:** Customize your review processes more effectively with new agent configuration settings. You can choose between Essential and Comprehensive review modes and tailor review request settings to fit your team's unique workflow requirements.

In Essential mode, only critical issues are posted as inline comments, and other issues appear in the main review summary under "Additional issues". In Comprehensive mode, Bito also includes minor suggestion and potential nitpicks as inline comments.

## AI Code Review Agent - 11th Apr 2025

<mark style="color:blue;">**New feature**</mark>

**Multilingual code reviews:** You can now receive AI-generated review comments in your preferred language! Bito supports over 20 languages, including English, Hindi, Chinese, and Spanish.

Simply click **Edit** next to your agent's instance name.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fxtf6JAAKkc1g97ciox8e%2Fscrnli_c3L7VuSh42i38A.png?alt=media&#x26;token=1d9f23b6-3c31-4d0e-96bb-512079c1fb69" alt=""><figcaption></figcaption></figure>

Then, choose your desired language from the **Review language** dropdown.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXQYjcrXg5epcsOfgd89w%2Fscrnli_CHgSk51WY2J3tu.png?alt=media&#x26;token=3f1c0656-1ad2-434e-9573-97c5b9d51c66" alt=""><figcaption></figcaption></figure>

**Enhanced chat interactions:** Interact effortlessly with AI Code Review Agent directly from your comments. Just tag your questions with `@bitoagent` or `@askbito`, and the AI Code Review Agent will promptly answer your queries, streamlining your review discussions.

**Improved Git branch configuration:** Gain more precise control over your review process with separate input fields for Source and Target branches. Previously combined into one, these fields are now clearly distinguished, enabling accurate and flexible Git branch inclusion for reviews.

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Fixed code review rules generation:** Bito now avoids generating unnecessary rules if review feedback is positive, and prevents incorrect rule creation, ensuring relevant and accurate code review rules.&#x20;

**Fixed incremental reviews:** Incremental reviews now accurately reflect only unmerged changes, eliminating confusion and improving the clarity of your review process.

## AI Code Review Agent - 4th Apr 2025

<mark style="color:blue;">**New feature**</mark>

**Chat with AI Code Review Agent:** We are excited to introduce our new chat feature that helps you ask questions directly to our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview). Use it to inquire about highlighted issues, request alternative solutions, or get clarifications on suggested fixes to support your coding decisions.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

{% hint style="info" %}
**Note:** On GitHub and Bitbucket, you need to manually refresh the page to see Bito AI responses, while GitLab updates automatically. Typically, responses are delivered in around 10 seconds.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F3y4hnagju3r9Q1hX1iAn%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=9517cf3b-1e19-4046-b956-60e1709adac0" alt="" width="563"><figcaption></figcaption></figure>

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Improved code review quality:** We fixed Python indentation issues and refined context formatting so the AI accurately understands member variables, ensuring you get clear and reliable feedback on your code.&#x20;

## AI Code Review Agent - 28th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Include Branches filter replaces Exclude Branches filter:** We’ve updated Bito’s [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) to use an “Include Source/Target Branches” filter instead of the previous “Exclude Source/Target Branches” filter. This change gives you more precise control over which branches get reviewed, allowing you to focus on critical code and avoid unnecessary reviews or AI usage. Your existing settings have been automatically migrated, and the web UI now clearly displays your selected branches.

**Improved context for JavaScript/TypeScript projects:** We’ve integrated SCIP as a symbol search tool (with zoekt as a backup) for JavaScript and TypeScript. This enhancement builds a more accurate code context for smarter reviews.&#x20;

**More efficient AI code reviews:** We’ve reduced Advanced AI request usage and made reviews faster by improving our AI prompts.

**More actionable code reviews:** Enhanced review guidelines and suggestion criteria deliver more accurate feedback, cut down on false positives, and present concise suggestions—making your reviews clearer and more actionable.

## Bito Cloud - 21st Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Improved visibility on AI requests usage:** We’ve updated the [Requests Usage](https://alpha.bito.ai/home/bito-premium/ai-request-usage) dashboard to give you a more detailed view of how your team is using AI requests. Now, you can easily see the number of queries made alongside the Advanced AI requests used, as Bito Wingman queries can utilize multiple Advanced AI requests per query. This enhanced breakdown helps you monitor usage more effectively and optimize your workflow.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXG7GXTjzzsj6v3pYHtBQ%2Fexported_image-7.png?alt=media&#x26;token=c3878c1b-f3e5-4760-9d9b-2e169a52f431" alt=""><figcaption></figcaption></figure>

## AI Code Review Agent - 18th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Automated reviews only for default branch:** By default, the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now excludes `main`, `master` and `*` all non-default branches from automated code reviews. This means you won’t get reviews on branches that aren’t the main focus of your development. Pull requests merging into your repository’s default branch are always reviewed, even if the branch is added in exclusion list. And if you need a review on another branch, simply use the `/review` command to override the defaults.

## AI Code Review Agent - 13th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Focused feedback:** Our improved [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now filter out trivial suggestions so you get only the feedback that truly matters.

**Manual reviews on disabled repos:** You can now trigger manual code reviews for GitLab and Bitbucket repositories even if they're disabled. This gives you more control over when you receive valuable feedback. ***Note:** Automatic reviews still run only on enabled repositories.*

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Reliable code reviews:** We fixed an issue that caused Additional Feedback (performance and code structure) reviews to fail, ensuring a smoother review process.

**Uninterrupted code reviews:** Automatic retry logic now manages Bitbucket rate-limit errors, keeping your reviews running without interruption.

**Complete TypeScript context:** We've fixed an issue where TypeScript export global variables weren't included in the review context. Now your reviews capture all the important code elements to provide context-aware and accurate AI code reviews.

## IDE V1.5.6 - 13th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Amazon Nova Lite 1.0 is now in Bito AI Chat:** We're excited to announce that **Amazon Nova Lite 1.0** is now available in Bito AI Chat for both [VS Code](https://marketplace.visualstudio.com/items?itemName=Bito.Bito) and [JetBrains](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant) extensions. This lightning-fast, low-cost AI model provides real-time coding suggestions and accurately troubleshoots issues. It’s perfect for basic tasks that don’t require complex reasoning.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FaaXMROTCj3ROCh1x5J2B%2Fscrnli_4Rn243VMdGTo5p.png?alt=media&#x26;token=8a29cd5c-c5e0-4fb9-a7c7-813911cde73f" alt="" width="496"><figcaption></figcaption></figure>

## Bito Wingman - 13th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Optimized context
:** [Bito Wingman](https://docs.bito.ai/changelog/broken-reference) now focuses on the most relevant parts of your conversation by using the last 30 Q\&A messages as context. This update enhances context understanding, leading to more accurate and timely responses.

**Faster parallel tool calls
:** Bito Wingman can now execute up to 10 tool calls at the same time, enabling smoother multitasking and a more efficient workflow. Say goodbye to long wait times—tasks now complete quicker, allowing you to focus on what matters most. Get more done, with less friction!

**Extended tool timeout
:** We've increased the tool execution timeout to 2 minutes. This update gives tools the extra time they need to process longer tasks, resulting in fewer errors and a more reliable performance during your work.

## AI Code Review Agent - 11th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Add GitHub repositories with ease:** We’ve added an **"Add Repositories"** button in [Bito Cloud](https://alpha.bito.ai/home/ai-agents/code-review-agent) that takes you directly to GitHub, allowing you to seamlessly add new repositories for AI code review. This update saves you time and simplifies your workflow.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBC2q1cS2287ghMlNTOeW%2Fscrnli_mKXF4hJU3gtV6q.png?alt=media&#x26;token=0ef79b96-fd9d-496d-b046-3157931bf893" alt=""><figcaption></figcaption></figure>

**Automatic enabling for selected GitHub repositories:** When you install Bito's GitHub AI code review app with selective repo access, your chosen repositories are now auto-enabled. This means less manual configuration and a faster start to your code review process.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fux4BpZVyhS5bO2HnNy53%2Fscrnli_8eUiPjgC0GU3yr.png?alt=media&#x26;token=e6664249-abe3-4f54-9ed6-cd407716aa4b" alt=""><figcaption></figcaption></figure>

## Bito Wingman - 7th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Updated the "Change applier" tool:** The **Change applier** tool in [Bito Wingman](https://docs.bito.ai/changelog/broken-reference) can now apply up to four changes at once. This reduces backup clutter and speeds up your workflow.

**Safer code updates:** Our **Change applier** tool now uses strict validation to ensure only the intended updates are made, keeping your code secure and error-free.

**Improved symbol search:** Find what you need faster—the updated **Code symbol search** tool now works with both files and directories, making project navigation simpler.

**Smarter handling for large files:** For large files, we automatically use the **Change applier** tool. If it can’t complete the update, we provide clear manual instructions so you stay in control without extra hassle.&#x20;

**Precise change planning:** Our updated prompts for **Change planner** tool now target only the areas that need changes, leaving your existing code untouched for maximum reliability.

## IDE V1.5.4 - 7th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Apply code feature now available in Bito's JetBrains extension:** Previously exclusive to our [VS Code extension](https://marketplace.visualstudio.com/items?itemName=Bito.Bito), this update now includes an **"Apply"** button with every AI code suggestion in [Bito's JetBrains extension](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant). Click the **"Apply"** button to instantly open a diff view of the changes, then choose to accept or undo them. This integrated workflow saves time by eliminating the need for manual copy-pasting.

[**Try in JetBrains**](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant)

[**Try in VS Code**](https://marketplace.visualstudio.com/items?itemName=Bito.Bito)

## AI Code Review Agent - 7th Mar 2025

<mark style="color:blue;">**New feature**</mark>

**Smarter code review suggestions:** Our enhanced AI code review suggestions now capture a fuller picture of your code by including complete function contexts and filtering out less relevant checks. This means you get more targeted, actionable insights that help maintain code quality, reducing noise and focusing on the changes that truly matter.

## AI Code Review Agent - 28th Feb 2025

<mark style="color:blue;">**New feature**</mark>

**Supported Claude Sonnet 3.7:** We've upgraded our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) with Claude Sonnet 3.7—a new AI model that brings deep thinking capabilities to your pull requests, making code reviews more accurate and context aware. With advanced reasoning and powerful coding skills, it delivers insightful and detailed feedback, helping you quickly identify issues and improve your code quality with greater confidence.

## AI Code Review Agent - 24th Feb 2025

<mark style="color:blue;">**New feature**</mark>

**Connect Bito to GitLab effortlessly:** Setting up your GitLab repositories with [Bito's AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) has never been easier. Our improved OAuth authentication flow lets you connect with GitLab with a single click—no need to manually enter your Personal/Group Access Token.

Automatic token validation and refresh further streamline the process, ensuring a fast and secure setup.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FajlQGjfzHjaovgdmZND8%2Fscrnli_O1o6wkf9t9A8zs.png?alt=media&#x26;token=8af62ed9-b725-4553-8d72-8f601bb2eca3" alt=""><figcaption></figcaption></figure>

## IDE V1.5.3 - 24th Feb 2025

<mark style="color:blue;">**New feature**</mark>

**Apply AI code suggestions directly in your files:** Bito now features an **"Apply"** button with every AI code suggestion. Click the button to instantly open a diff view of the changes, then choose to accept or undo them. This integrated workflow saves time by eliminating the need for manual copy-pasting.

Available exclusively in our VS Code extension.

[**Try it now!**](https://marketplace.visualstudio.com/items?itemName=Bito.Bito)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FlPuR5uwotMnzgi3wYTwB%2Fscrnli_3PsoFviiB7AiZn.png?alt=media&#x26;token=4e032a66-8277-4be2-987e-d98866735767" alt="" width="484"><figcaption><p>Click the "Apply" button.</p></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FzxR7jBjCmRc2KKZVBeRe%2Fscrnli_ShRScg19x7g17K.png?alt=media&#x26;token=6a892427-c7bb-4da9-bb84-435e61d74124" alt=""><figcaption><p>View AI code suggestions in a Diff View.</p></figcaption></figure>

## AI Code Review Agent - 18th Feb 2025

<mark style="color:blue;">**New feature**</mark>

**Introducing custom code review rules:** Our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now refines its suggestions based on your feedback. When you react with negative emojis or comments on Bito-reported issues, the Agent automatically adapts by creating rules to prevent similar suggestions in future.&#x20;

For teams seeking deeper customization, you can provide us with your specific code review guidelines. Our team will implement these guidelines into your Bito workspace, ensuring it enforces your unique coding practices. To get started, email your guidelines to <support@bito.ai>.&#x20;

Enjoy a more tailored code review process that aligns perfectly with your project's needs, saving you time and reducing unwanted feedback.&#x20;

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/implementing-custom-code-review-rules)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FidQucoWSpLGvJq6NHU9U%2Fscrnli_l6Ry6idr6hN3dg.png?alt=media&#x26;token=6d68ea4f-59b2-4c04-ba54-1c791cf2767b" alt=""><figcaption><p>Custom code review rules for AI</p></figcaption></figure>

## AI Code Review Agent - 14th Feb 2025

<mark style="color:blue;">**Announcement**</mark>

**AI Code Review Agent removed from Bito IDE extensions:** We have temporarily removed the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) from our [VS Code](https://marketplace.visualstudio.com/items?itemName=Bito.bito) and [JetBrains](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4--bito-ai-code-assistant) extensions while we work on resolving some issues. However, AI Code Reviews remain a key focus for Bito and will continue to be fully available for pull request reviews on GitHub, GitLab, and Bitbucket.

We appreciate your understanding and encourage you to share any feedback at <support@bito.ai>.

## IDE V1.5.1 - 7th Feb 2025

<mark style="color:blue;">**New feature**</mark>

**DeepSeek-V3 (served from the US and Europe) is now in Bito AI Chat:** We're excited to announce that DeepSeek-V3 is now available in Bito AI Chat for both [VS Code](https://marketplace.visualstudio.com/items?itemName=Bito.bito) and [JetBrains](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4--bito-ai-code-assistant) extensions. It features an innovative Mixture-of-Experts design and multi-token prediction that enables extended context processing, delivering enhanced performance on complex coding tasks.

Bito’s use of DeepSeek is securely served from the United States and Europe.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfE7yLUWhxbcVulRggZmB%2Fscrnli_XzXkrwjAQo7nVz.png?alt=media&#x26;token=f7561df2-6781-41c7-b9ed-ff88cd951632" alt="" width="484"><figcaption></figcaption></figure>

## IDE V1.5.1 - 6th Feb 2025

<mark style="color:blue;">**New feature**</mark>

**o3-mini is now in Bito AI Chat:** We've upgraded Bito AI Chat with OpenAI's latest o3-mini models, now available in both [VS Code](https://marketplace.visualstudio.com/items?itemName=Bito.bito) and [JetBrains](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4--bito-ai-code-assistant) extensions. These new models bring faster responses, improved reasoning, and more accurate coding assistance—all designed to fit the way you code.

With o3-mini, you get three options tailored to your needs:

* **o3-mini Low:** Fastest response time for quick coding help and simple queries.
* **o3-mini Medium:** Balanced speed and depth, perfect for everyday development.
* **o3-mini High:** More advanced reasoning for complex technical discussions.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FmXqOHG0CYASmcPGT17yV%2Fscrnli_7vd45OEJNOPBQP.png?alt=media&#x26;token=e653f418-2846-48b7-8cce-c7ff8df45aee" alt="" width="485"><figcaption></figcaption></figure>

## AI Code Review Agent - 27th Jan 2025

<mark style="color:blue;">**New feature**</mark>

**Free AI-generated pull request summaries:** Bito's [AI Code Review Agent](https://bito.ai/product/ai-code-review-agent/) now provides concise summaries of pull requests on the [Free Plan](https://bito.ai/pricing/). With these summaries, you can quickly understand key changes, reduce manual review effort, and make faster, informed decisions—all while saving time for your team.

[**Try it for free**](https://alpha.bito.ai/home/welcome)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FD8vDDSZHUqplOwbHkzRj%2Ftuxpi.com.1738128020.jpg?alt=media&#x26;token=b59f5e8c-b45b-420d-9374-7e9f4f9e102f" alt=""><figcaption><p>Free AI-generated pull request summary by Bito</p></figcaption></figure>

**Increased AI usage limits:** [Free Plan](https://bito.ai/pricing/) users now have access to:

* **6X AI Code Completions** - increased from 50 to 300 per month
* **Nearly 4X AI Chat requests** - increased from 20 to 75 per day

The increased limits mean developers won't hit daily AI request caps, ensuring uninterrupted coding sessions.

## AI Code Review Agent - 17th Jan 2025

<mark style="color:blue;">**New feature**</mark>

**Simplified setup for the AI Code Review Agent:** Getting started is now faster and easier than ever. No more manual webhooks! With just a few clicks, you can seamlessly connect your Bito workspace to GitHub, GitLab, or Bitbucket for AI-powered code reviews. &#x20;

Manually configured agents will continue to work without any interruptions. However, manual webhook setups are no longer supported for new configurations.&#x20;

Upgrade to the new setup for a smoother experience and better control.&#x20;

[**Get started**](https://alpha.bito.ai/home/ai-agents/code-review-agent)

## IDE V1.4.7 - 19th Dec 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing Bito Wingman:** Your AI coding partner that takes action, handling tasks like coding, documentation, and project management from start to finish. Wingman has incredible reasoning and planning capabilities, can access and understand your files, and can also access apps like Jira, Linear, Confluence, and the web.

Currently available only in [**VS Code**](https://docs.bito.ai/getting-started/installing-on-visual-studio-code) and in private beta. Want early access? Contact us at [**support@bito.ai**](mailto:support@bito.ai)

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Install on VS Code</strong></mark></td><td><a href="https://marketplace.visualstudio.com/items?itemName=Bito.Bito">https://marketplace.visualstudio.com/items?itemName=Bito.Bito</a></td></tr><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="broken-reference">Broken link</a></td></tr></tbody></table>

## Billing and plan updates - 26th Nov 2024

**Start your free trial — no credit card required:** Unlock Bito's premium features like the [AI Code Review Agent](https://bito.ai/product/ai-code-review-agent/) and intelligent [AI that understands your code](https://bito.ai/product/ai-for-coding/), all designed to help you ship high-quality code faster.

Cancel anytime, no commitments needed.

[Start free trial](https://alpha.bito.ai/home/bito-premium/change-plan)

## AI Code Review Agent - 22nd Nov 2024

<mark style="color:blue;">**New feature**</mark>

**Supported Linter for Go language:** Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now supports golangci-lint, enabling faster, more thorough Go code reviews with automatic issue detection and enforcement of best practices. Enhance code quality and streamline your workflow effortlessly!

## IDE V1.4.3 - 20th Nov 2024

<mark style="color:blue;">**New feature**</mark>

**Choose your preferred AI model:** Take control of your AI chats! Now, you can choose your preferred AI model in the Bito extension for [VS Code](https://marketplace.visualstudio.com/items?itemName=Bito.Bito) and [JetBrains](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant)—choose between free Basic models or premium Advanced ones for a tailored coding experience.

[Learn more](https://docs.bito.ai/changelog/broken-reference)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FM5XHN9YVH9EPNW8jY2b3%2FScreenshot%202024-11-21%20142823.png?alt=media&#x26;token=032870ef-b735-4fca-b7fa-15e72b145d5b" alt=""><figcaption></figcaption></figure>

**Open Bito in a new tab or window:** Keep your coding environment clutter-free by opening Bito separately while still navigating your editor effortlessly. A larger view of Bito is ideal for diving into detailed code reviews or accessing AI-driven insights with ease.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito/open-bito-in-a-new-tab-or-window)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FCAP3rfv1copNT4XyW89d%2Fscrnli_w63tgPPhV46dyD.png?alt=media&#x26;token=41a7651d-e11b-4cf0-9d3e-a0013d677b00" alt="" width="456"><figcaption></figcaption></figure>

## IDE V1.4.2 - 8th Nov 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing the new `/createpr` command:** Create pull requests directly from your IDE with AI-generated titles, summaries, and Changelists. Save time, stay focused, and streamline your workflow effortlessly!

[Learn more](https://docs.bito.ai/changelog/broken-reference)

**Code + chat context:** We’ve improved Bito’s [AI that understands your code](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/overview) feature by enabling it to use prior chat context when answering queries. Now you can seamlessly continue conversations, request changes to existing code, and get smarter, more relevant responses tailored to your workflow—all without losing valuable context.

## AI Code Review Agent - 7th Nov 2024

<mark style="color:blue;">**New feature**</mark>

**Integrated linter feedback:** The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now includes linter support, starting with ESLint for JavaScript and TypeScript. Integrated linting enhances code quality feedback, helping you catch errors early, keep projects aligned with best practices, and save time in the review process.

## AI Code Review Agent - 29th Oct 2024

<mark style="color:blue;">**New feature**</mark>

**Improved usability and formatting:** We’ve redesigned the [AI Code Review Agent’s](https://docs.bito.ai/ai-code-reviews-in-git/overview) comments in pull requests to make them more user-friendly and easier to read. With clearer formatting, you can now quickly spot key feedback and take action faster.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FPwa1N37gtIjImktuyFOs%2Fcra_ui_collapsed.png?alt=media&#x26;token=16421a58-9897-4371-9c64-e049ce220f5f" alt=""><figcaption><p>Example of collapsed comment</p></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fe3S3NxSELHd0AZYx4WMX%2Fcra_ui_expanded.png?alt=media&#x26;token=37b4014b-493c-4f8d-abc7-f27f99839111" alt="" width="464"><figcaption><p>Example of expanded comment</p></figcaption></figure>

**Skip redundant automated reviews:** The Agent now skips automated full reviews if one is already running, saving valuable resources and cutting unnecessary costs. Manual reviews remain unaffected, giving you full control over the review process.

## AI Code Review Agent - 22nd Oct 2024

<mark style="color:blue;">**New feature**</mark>

**Enhanced code analysis for quality suggestions:** We've made significant updates to the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview)'s prompts for deeper code analysis, delivering relevant and actionable suggestions to help you improve your code quality.

**Incremental review control at workspace level:** You can now enable or disable incremental reviews at the workspace level, giving you greater flexibility to manage review settings across different projects. Please contact <support@bito.ai> to configure this feature.

## AI Code Review Agent - 18th Oct 2024

<mark style="color:blue;">**New feature**</mark>

**Auto-review draft PR when marked as ready:** The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now automatically performs a full or incremental review when a pull request moves from draft to ready status. This feature offers immediate insights to help you spot issues early, saving you time and streamlining your workflow.&#x20;

**Enable or disable incremental reviews:** Incremental review can now be enabled or disabled at the Agent instance level, giving your team more control over the review process. Please contact <support@bito.ai> to customize this feature according to your team's needs.

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Improved code review quality:** We've optimized the AI Code Review Agent's prompts to provide more accurate, high-quality feedback, helping you identify and resolve issues faster.&#x20;

## IDE V1.4.1 - 15th Oct 2024

<mark style="color:blue;">**New feature**</mark>

**Review committed code in your IDE:** [AI Code Review Agent](https://docs.bito.ai/changelog/broken-reference) can now review the latest commit, specific commits, or a range of commits, giving you better control over your code review process. This allows you to spot issues faster and ensure higher code quality before pushing to production.&#x20;

Try the new commands in Bito extensions for [VS Code](https://marketplace.visualstudio.com/items?itemName=Bito.bito) and [JetBrains](https://plugins.jetbrains.com/plugin/18289-chatgpt-gpt-4o--bito-ai-code-assistant):&#x20;

* **`/review #lastcommit`**: Review the latest commit in the branch.&#x20;
* **`/review #commit=<commithash>`**: Review a specific commit by its hash.&#x20;
* **`/review #commit=<commithash-1>..<commithash-2>`**: Review a range of commits between two commit hashes.

[**Learn more**](https://docs.bito.ai/changelog/broken-reference)

**Easier access to AI code reviews:** You can now effortlessly invoke the AI Code Review Agent directly from the context menu by right-clicking in the code editor and selecting commands under the **"Bito Code Review Agent"** menu. This provides faster, on-the-go access to code reviews right where you work.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFQIO7ONJ3nWwKmK1se83%2FScreenshot%202024-10-21%20075920.png?alt=media&#x26;token=5ec29024-5339-46ca-9929-9786e47234ce" alt=""><figcaption></figcaption></figure>

**Quickly switch between Code Review and AI Chat:** With the new **"Back to AI Chat"** button above the chatbox, you can easily jump back to AI Chat for conversations without interrupting your code review flow. Stay productive and manage both tasks seamlessly.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0mKKxUue9Xi01aPy3Ou9%2FScreenshot%202024-10-21%20064516.png?alt=media&#x26;token=4eaf71ea-3702-4d55-81e7-e67c6adafe30" alt=""><figcaption></figcaption></figure>

## AI Code Review Agent - 10th Oct 2024

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**15% faster AI code reviews:** We've optimized our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview), cutting execution time by 15%. This improvement boosts your team's productivity, enabling quicker code reviews and helping you deliver high-quality features faster. Stay agile and keep your development process running smoothly!

## AI Code Review Agent - 26th Sep 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing incremental code reviews:** Our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now automatically reviews only the recent changes each time you push new commits to a pull request. This saves time and reduces costs by avoiding unnecessary re-reviews of all files.

## AI Code Review Agent - 19th Sep 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing Changelist:** a new tabular view in the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent)'s feedback that displays key changes in a pull request, making it easy to spot important updates at a glance without reviewing every detail. Changelist categorizes modifications and highlights impacted files, giving you a quick, comprehensive summary of what has changed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FU5eSjP7gQ6JolLWUySuI%2Fchangelist_by_bito.png?alt=media&#x26;token=291ac3d3-cf5c-45ef-974d-a145d41c81a7" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

## AI Code Review Agent - 12th Sep 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing the Chain of Thought (CoT) approach:** Our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now leverages the Chain of Thought (CoT) approach, which involves step-by-step reasoning to analyze your code more effectively. You will now receive more precise feedback, detailed explanations, and better solutions to enhance your code quality.

## AI Code Review Agent - 30th Aug 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing Claude Sonnet 3.5:** Our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now exclusively uses the Anthropic Claude Sonnet 3.5 model, delivering more accurate and reliable code reviews. This new AI model offers superior performance in understanding complex code patterns and providing actionable recommendations.

## IDE V1.3.9 - 30th Aug 2024

<mark style="color:blue;">**New feature**</mark>

**AI code reviews with advanced code understanding:** [AI Code Review Agent within Bito’s extension for VS Code and JetBrains](https://docs.bito.ai/changelog/broken-reference) now offers deeper insights by fully understanding the entire repository context. This upgrade enhances code reviews, making them more relevant to your project’s needs and delivering actionable, precise suggestions directly within your coding environment.

To get started, [configure the default @codereview agent instance](https://docs.bito.ai/changelog/broken-reference) with your Git information or use an already configured Agent instance from your Bito Cloud workspace.

## Billing and plan updates - 28th Aug 2024

We’ve made major upgrades to the 10X Developer Plan, including:

1. **50% more GPT-4o requests** - from 400 to 600 per month.&#x20;
2. **70% lower cost for additional GPT-4o requests** - Reduced from $0.10 to $0.03 per request.&#x20;

All at the same affordable cost of $15.

[View pricing](https://bito.ai/pricing/)

## AI Code Review Agent - 14th Aug 2024

<mark style="color:blue;">**New feature**</mark>

**Support for Bitbucket:** Now seamlessly integrate Bito’s AI Code Review Agent into your Bitbucket workflow. No downloads required—just a single-click install. Get AI-powered reviews posted as comments directly within your pull requests. Currently available on Bito cloud or through a self-hosted service via CLI.&#x20;

[Learn how to install](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/getting-started/install-run-using-bito-cloud)&#x20;

## IDE V1.3.8 - 12th Aug 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing GPT-4o mini:** GPT-4o mini is now the default AI model for all basic AI requests. Available for both the Free Plan and the 10X Developer Plan, this upgrade brings improved performance and efficiency to your everyday coding tasks.&#x20;

**Introducing AI Chat Analytics:** Explore our new analytics dashboard to gain insights into the AI Chat usage across your team. Track metrics such as total chats, chats per user, model usage, and more. Available under both the Free Plan and the 10X Developer Plan, this dashboard will help you make data-driven decisions for better collaboration and productivity.&#x20;

[View dashboard](https://alpha.bito.ai/home/dashboard?view=Chat_Analytics)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FuCmQpmloUMEk70wejUGh%2FAI%20chat%20analytics_1.jpg?alt=media&#x26;token=64147049-f465-4e01-aa79-604930ad633c" alt=""><figcaption><p>AI Chat Analytics</p></figcaption></figure>

## IDE V1.3.6 - 17th Jul 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing the AI Code Review Agent for IDEs:** Get human-like feedback on your code changes as you develop. Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now supports VS Code and all JetBrains IDEs, including IntelliJ IDEA, PyCharm, WebStorm, and more. Developers can now address code issues early, accelerating development cycles and boosting team productivity.

The Agent is ready to use immediately without any setup required. Upgrade to the Bito [10X Developer Plan](https://bito.ai/pricing/) today and experience the future of code review firsthand.

[Read documentation](https://docs.bito.ai/changelog/broken-reference)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqOaWWMwCCcHJFbUSRN4t%2FScreenshot%202024-07-16%20045836.png?alt=media&#x26;token=c823aa96-ab54-4e08-9c4f-bfa30c62d72b" alt="" width="444"><figcaption><p><strong>AI Code Review Agent for VS Code and JetBrains IDEs</strong></p></figcaption></figure>

## AI Code Review Agent - 12th Jul 2024

<mark style="color:blue;">**New feature**</mark>

**Introducing code review analytics:** Explore our new [analytics dashboards](https://alpha.bito.ai/home/dashboard?view=overview) for in-depth insights into your code review process. These user-friendly reports help you track key metrics such as pull requests reviewed, issues found, lines of code reviewed, and understand individual contributions.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrlVw2PbnuDqIYYUijesc%2Fscrnli_7_12_2024_9-49-52%20PM.png?alt=media&#x26;token=29ae6b79-6a78-41ae-b7e1-39857c58921e" alt=""><figcaption><p>Code Review Analytics dashboard</p></figcaption></figure>

**Provide feedback on code review quality:** For GitLab, we've added support for emoji-based reactions, while for GitHub, you can respond to feedback question(s) given at the end of code review comments.&#x20;

This will help your team track the quality of suggestions provided by the AI Code Review Agent through the "Acceptance Rate" statistics available on the [code review analytics dashboard](https://alpha.bito.ai/home/dashboard?view=overview).

<div><figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FHPrtHcbw4yh03XFxaSPU%2Fscrnli_7_12_2024_9-59-45%20PM.png?alt=media&#x26;token=8bed01c2-68e4-45c5-875a-e6ea2eca860a" alt=""><figcaption><p>GitLab emoji-based reactions</p></figcaption></figure> <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FwEHZYumAJ1sbjZipcja2%2Fscrnli_7_12_2024_10-00-12%20PM.png?alt=media&#x26;token=9468e9a8-1c5a-4701-9720-690a017cbc34" alt=""><figcaption><p>GitHub feedback questions</p></figcaption></figure></div>

<mark style="color:blue;">**Improvement and bug fixes**</mark>

**Track your Bito AI usage:** Stay on top of how your team is using Bito AI. With the [Requests Usage dashboard](https://alpha.bito.ai/home/bito-premium/ai-request-usage), you can easily see how many AI requests your team members and AI Agents are making. The [Usage Management dashboard](https://alpha.bito.ai/home/bito-premium/usage-management) allows you to manage resources and control costs efficiently. This way, you can ensure that you're getting the most out of Bito AI without overspending.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FB79JiI9DjCzRXmeGZfJd%2Fscrnli_7_12_2024_10-27-17%20PM.png?alt=media&#x26;token=971cbd1c-1c1c-43f6-b7ef-a3ddc78bc34d" alt=""><figcaption><p>Requests Usage dashboard</p></figcaption></figure>

**Enhanced context understanding with prompt engineering:** Our improved AI prompts now offer superior comprehension of your code context, significantly increasing the accuracy in identifying and addressing code issues. With Bito AI, critical problems are less likely to be overlooked, ensuring you receive a thorough and reliable code analysis.&#x20;

**Enhanced understanding of CSS, SCSS, and Terraform:** Bito AI now analyzes both immediate context and broader structure of code in CSS, SCSS, and Terraform files, including nested configurations and dependencies. This enables Bito to provide more accurate suggestions, optimizations, and error detections.&#x20;

For CSS and SCSS, Bito AI identifies patterns and offers improvements in style management and consistency. For Terraform, it understands and optimizes infrastructure as code, ensuring more efficient and scalable deployments.&#x20;

**Enhanced presentation of code review comments:** We've made changes to how the AI Code Review Agent presents its feedback to enhance clarity and usability.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FoegucS9h10LyL6F6klF9%2Fscrnli_7_12_2024_10-44-40%20PM_1.png?alt=media&#x26;token=ec1c5a8a-23ea-490a-b434-ae3d16c6008e" alt="" width="563"><figcaption><p>New look of code review comments</p></figcaption></figure>

## IDE V1.3.5 - 27th Jun 2024

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Prioritized Results from Open Files in IDE:** When you ask a question about your code in [Bito AI Chat](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito), the AI now prioritizes answers from the files you have open in your IDE. By analyzing the relevant code first, Bito ensures more accurate and context-specific responses. This means you will now see relevant code snippets from what you are currently working on, saving you time and effort in finding the information you need.

Bito filters active files to exclude binary files, files with invalid extensions, files outside the project directory, and files in Diff view. The filtered list is then used to retrieve answers from the index.

{% embed url="<https://www.loom.com/share/4489546fbbc347709c2a0a34eacaa17e>" %}

## AI Code Review Agent - 7th Jun 2024

<mark style="color:blue;">**New Feature**</mark>

**Filter Your Code Reviews, Exclude What You Don't Need:** Introducing filters that give you control over what the AI Code Review Agent analyzes. They let you exclude specific files, folders, Git branches, or even draft pull requests from AI code reviews using glob/regex patterns.

For more information, see [Excluding Files, Folders, or Branches with Filters](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/excluding-files-folders-or-branches-with-filters).

**AI Code Reviews with GPT-4o:** GPT-4o integration brings a major upgrade to the AI Code Review Agent, enhancing code review quality, accelerating processing, and reducing costs.

**Redesigned Comment Layout:** We've redesigned the Agent's output comments to enhance readability and usability. The new layout is more organized and user-friendly, making it easier to navigate and understand the feedback. Important details are prioritized, saving you time and streamlining the review process.

<div><figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FtL6RSqKI0T9vBj1iT1XT%2FRedesigned%20comment%20layout_1.png?alt=media&#x26;token=01f0cae2-10a5-41e7-95b4-50907c8a1673" alt=""><figcaption></figcaption></figure> <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0gfTOE9AzOU525hy06AC%2FRedesigned%20comment%20layout_2.png?alt=media&#x26;token=ee9ecb0b-4dd2-4286-983b-1b84e820a27d" alt=""><figcaption></figcaption></figure></div>

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Improved Code Review Quality with Less Noise:** The Agent now analyzes each issue individually. This allows it to provide more focused and insightful suggestions tailored to the specific problem at hand. The cleanup process is also improved to reduce noise and unnecessary information. This means you'll get clearer, more actionable feedback that's easier to understand and implement.

## AI Code Review Agent - 22nd May 2024

<mark style="color:blue;">**New Feature**</mark>

**No Duplicate Comments:** Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) now avoids posting duplicate comments. It achieves this by reviewing all its previous suggestions on a pull request before adding new ones. If it finds an existing suggestion that matches a new one, it skips the new one to avoid duplicates. This ensures the Agent provides only unique and relevant feedback on each pull request. However, if a user deletes a suggestion, the Agent will recommend it again in the next review.

**More Relevant Suggestions:** We've improved the accuracy and relevance of code suggestions by better understanding the context of your code.&#x20;

**Targeted Code Analysis via GitHub Actions:** The AI Code Review Agent running via GitHub Actions now offers targeted code analysis with specialized commands! You can perform code reviews on specific areas of your codebase, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`:** Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`:** Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`:** Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`:** Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`:** Identifies optimization opportunities to enhance code efficiency and reduce resource usage.

For more details, refer to [Available Commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).

**GPT-4o for Advanced AI Model Requests:** We're thrilled to announce that Bito now leverages the power of GPT-4o for advanced AI model requests. This upgrade significantly enhances Bito's capabilities, providing you with faster responses. No need to update your IDE, CLI, or agents! This update works seamlessly behind the scenes, so you can experience the benefits of GPT-4o right away.

## AI Code Review Agent - 7th May 2024

<mark style="color:blue;">**New Feature**</mark>

**5 New Commands for Targeted Code Analysis:** The [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) now offers specialized commands designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`:** Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`:** Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`:** Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`:** Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`:** Identifies optimization opportunities to enhance code efficiency and reduce resource usage.&#x20;

For more details, refer to [Available Commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).&#x20;

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Limiting Advanced AI Requests for Agent Execution:** Each execution of the AI Code Review Agent consumes advanced AI requests, which are now capped at a maximum of 20. This ensures a consistent experience and prevents users from unintentionally exceeding their advanced AI request quotas.&#x20;

**Combining Multiple Suggestions for Same Line and Range:** We've improved how the AI Code Review Agent handles multiple suggestions for the same line or line range. Previously, each suggestion appeared as a separate comment, making it cumbersome for users to navigate through multiple entries. Now, all suggestions for the same line or line range are consolidated into a single comment, enhancing user convenience.

## AI Code Review Agent - 24th Apr 2024

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Handle Larger Pull Requests of Nearly Unlimited Size:** No more limitations on pull request size! The AI Code Review Agent can now analyze more code at once, enabling smoother code reviews for pull requests of nearly unlimited size (subject to our [Fair Use Policy](https://bito.ai/fair-use/)).&#x20;

**More Focused and Relevant Recommendations:** We've significantly enhanced the attention span of our AI Code Review Agent by optimizing its context window. The agent also filters out unnecessary suggestions (such as document notes, non-impacting changes etc.), delivering high-quality and precise code reviews that save you valuable time.&#x20;

**Static Code Analysis for Python via GitHub Actions:** The AI Code Review Agent, running through GitHub Actions, can now analyze Python code using Astral Ruff and Mypy, in addition to its existing support for Java, Objective C, and C/C++. This enhances code quality and speeds up development cycles by proactively identifying errors and vulnerabilities in your Python codebase.

## AI Code Review Agent - 12th Apr 2024

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Improved Code Review Quality with Less Noise:** We've enhanced the [AI Code Review Agent](https://bito.ai/product/ai-code-review-agent/) to ensure you only see relevant suggestions. This means you'll no longer see suggestions that are already implemented in the code or those that primarily recommend documentation updates. Plus, each suggestion now displays the most relevant code changes (diff), making it easier to understand the context of the suggestion.

**Better Code Review Process:** The Agent now triggers automatic code reviews only for essential events, such as opening a pull/merge request. This reduces unnecessary reviews triggered by actions like closing and reopening. You can still request a manual code review by simply posting `/review` in a comment on the pull/merge request.

## AI Code Review Agent - 22nd Mar 2024

<mark style="color:blue;">**New Feature**</mark>

**AI that Understands Your Code:** The [AI Code Review Agent](https://bito.ai/product/ai-code-review-agent/) can now better understand code changes in pull requests. It achieves this by analyzing relevant context from your entire repository, resulting in more accurate and helpful code reviews.&#x20;

To comprehend your code and its dependencies, we use Symbol Indexing, Abstract Syntax Trees (AST), and Embeddings. For more information, see [How does Bito’s “AI that understands your code” work?](https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/)&#x20;

Supported languages include JavaScript, TypeScript, Java, Go, Python, C, C++, PHP, and C#.&#x20;

**Static Code Analysis for Python:** The AI Code Review Agent now actively supports static code analysis for Python code using Astral Ruff and Mypy, in addition to its existing support for Java, Objective C, and C/C++. It proactively identifies potential errors and vulnerabilities within your Python codebase, thereby improving code quality and accelerating development cycles.&#x20;

**Inline Comments:** We've added support for inline comments in both GitHub and GitLab. This means code suggestions are now provided directly within each file, under the code diff. This offers a clearer view of the specific lines that need fixing.&#x20;

Inline commenting is by default enabled for all new and existing AI Code Review Agent instances. The “Overview” section now shows the number of files changed and suggestions made in a pull request, along with a link that directs you to the specific file changes.&#x20;

To manually trigger inline code reviews with comments directly on the code diffs, post the `/review` command as comment on the pull request. You can also add a new optional parameter like `/review #inline_comment=False`. This lets you receive a full-post code review instead of separate inline comments under the diffs.&#x20;

## AI Code Review Agent - 15th Mar 2024

<mark style="color:blue;">**New Feature**</mark>

**Added Support for GitHub/GitLab Enterprise (self-hosted):** You can now integrate Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) with your on-premises GitHub or GitLab environment to enhance security. This is crucial for organizations in regulated industries with strict data compliance requirements.

[**Get started using Bito Cloud**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud)

**Multiple Specialized Engineers:** We've made significant improvements to the way the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) analyzes your code. It now acts as a set of specialized engineers each analyzing different aspects of your PR.  They analyze aspects such as Performance, Code Structure, Security, Optimization, and Scalability. By combining and filtering the results, the Agent can provide you with much more detailed and insightful code reviews, bringing you a better quality code review and helping you save time.

## IDE V1.3.0 - 15th Mar 2024

<mark style="color:blue;">**New Feature**</mark>

**Light and Dark Themes:** In Visual Studio Code and JetBrains IDEs, you can choose between a light or dark theme for the Bito panel to match your coding environment preference. For VS Code users, Bito also offers an adaptive theme mode in which the Bito panel and font colors automatically adjust based on your selected VS Code theme, creating a seamless visual experience.

{% hint style="info" %}
The IDE customization settings are accessible through the new toolbar dropdown menu titled **"Extension Settings"**.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOzrvVqbA0A20gkRK9BNL%2Fscrnli_3_17_2024_4-57-38%20PM.png?alt=media&#x26;token=a80764cc-717c-4a4d-b43e-65ebd394d141" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqvA1VWRBblX4zZJBkgLD%2Fimage-20240314-053256.png?alt=media&#x26;token=72b56560-ca80-4316-93b5-8780c755b3cf" alt=""><figcaption></figcaption></figure>

**Font Size Control:** Take control of your code readability! Within the Bito extension settings, you can now adjust the font size for a comfortable viewing experience.

**AI Smartly Identifies Your Question's Intent:** Bito automatically figures out if you're asking about something in [your code](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/overview). If it's confident, it grabs the relevant parts of your code from our [index](https://docs.bito.ai/help/bitos-ai-stack/indexing) and feeds them to the Large Language Models (LLMs) for accurate answers. But if it's unsure, Bito will ask you to confirm before proceeding.&#x20;

Don't worry, existing [cue words](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) such as "my code" and "my repo" still work perfectly!

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvfmmnWqiElOcm2mEWTzc%2Fscrnli_3_28_2024_7-05-52%20AM.png?alt=media&#x26;token=12b9e003-5d27-4f16-a5fd-d2f72d5123cd" alt=""><figcaption></figcaption></figure>

## IDE V1.2.9 - 12th Mar 2024

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Fixed Multi-Level Paths in .bitoignore:** The `.bitoignore` file now correctly handles paths with multiple subdirectories. Previously, using patterns to ignore deeply nested directories wasn't working as expected in VS Code. For instance, if you add a pattern like `project/data/subfolder` to your `.bitoignore` file, it will now correctly ignore all files and subdirectories within the `project/data/subfolder` directory.

**Fixed Slash Command Usability Issue:** Bito chatbox no longer blocks users from typing content that starts with a slash `/`, such as `/bin/bash`. The Template panel now disappears entirely if no matching templates are found after entering additional characters following the slash.

## IDE V1.2.8 - 16th Feb 2024

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**400 Advanced AI Requests Monthly:** Exciting news from Bito's **10X Developer Plan**! We've raised your Advanced AI Models' quota from 100 to 400 requests per month. This significant increase allows for uninterrupted usage, giving you the freedom to explore more without worrying about limits. For more information, please visit our [**Pricing Page**](https://bito.ai/pricing/).

**Advanced AI Default in Bito Chat:** 10X Developer Plan now starts with Advanced AI Models as default for Bito AI Chat in the IDE extension, ensuring immediate access to top-tier coding assistance for enhanced efficiency and creativity.&#x20;

**Suggest Code Inside Brackets:** We've resolved the issue that prevented AI Code Completions within inline brackets, including arrays, function headers, and more. Now, when you input code within brackets—like creating an array in PHP, such as `$numbers = [89, 7, 22,<Bito_DISPLAYS_CODE_COMPLETION_HERE>];`—right after you add a space or comma following the last array element, Bito immediately provides suggestions to help you fill in the code faster. It's not just for arrays; this works for all kinds of brackets in your code.

## AI Code Review Agent - 14th Feb 2024

<mark style="color:blue;">**New Feature**</mark>

**Bito's AI Code Review Agent:** Your team's new automated code reviewer! Leveraging the best Large Language Models such as GPT-4 and Claude 2.1, this tool is here to transform how senior developers review code.

{% embed url="<https://youtu.be/QzMFfl2KRJI>" %}

**Here’s what it offers:**

* **Automated Code Reviews:** Instantly spots bugs, code smells, and security vulnerabilities in your Pull/Merge Requests.
* **Integration with Git Providers:** Works with GitHub, GitLab, and Bitbucket (coming soon), posting recommendations as comments right within the Pull Request.
* **Comprehensive Analysis:** Utilizes static analysis and OSS vulnerability tools for thorough insights.
* **Tailored Suggestions:** Offers specific, actionable advice to improve your code, ensuring it’s up to standard.
* **Privacy First:** Prioritizes your security and confidentiality; no code is read or stored.

This AI Agent not only speeds up code merging but also elevates code quality, letting you focus on what matters. Ready to code smarter, not harder? Welcome to the future with Bito.

Experience this cutting-edge tool on [**Bito Cloud**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud) or opt for a [**self-hosted service**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service) via CLI, webhooks, or GitHub Actions.

{% hint style="info" %}
It's included at no extra cost with Bito's **10X Developer** plan. For more information, please visit our [**Pricing Page**](https://bito.ai/pricing/).
{% endhint %}

## IDE V1.2.5 - 24th Nov 2023

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**DLL Files Excluded From Index:** To improve the [indexing](https://docs.bito.ai/help/bitos-ai-stack/indexing) speed of your projects, we will now be excluding DLL files by default.

**Fixed localStorage is Full Error:** Some of you might have bumped into a bit of trouble with a JavaScript error saying your localStorage is full. We have resolved that issue. So, no more storage woes!&#x20;

**Fixed AI Code Completions Setting:** We have fixed the Java exception that occurs when you try to switch the [AI Code Completions](https://docs.bito.ai/changelog/broken-reference) feature on or off without an internet connection.&#x20;

**Fixed "Enable/Disable This" Link:** In Bito panel, we've fixed the "Enable/Disable This" link that wasn't working properly before. Now, you can use it to access the [AI Code Completions settings](https://docs.bito.ai/changelog/broken-reference) without any trouble.&#x20;

## IDE V1.2.4 - 16th Nov 2023

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Fixed Backward Compatibility Issue:** Bito now works seamlessly with JetBrains version 2021.x and onwards. Thanks to your valuable feedback, we have identified and fixed the issue that was breaking backward compatibility of the Bito extension in JetBrains IDEs, such as IntelliJ IDEA.&#x20;

If you encountered annoying error messages like **`Cannot load class co.bito.intellij.webview.BitoWindowFactory`**, they're a thing of the past now! Simply update your Bito extension to the new version 1.2.4, and you'll be all set.&#x20;

## IDE V1.2.3 - 7th Nov 2023

<mark style="color:blue;">**New Feature**</mark>

**AI Code Completions Now in JetBrains IDEs!** Say goodbye to long hours of staring at your screen trying to figure out the next line of code. With Bito, as soon as you start typing a few characters or jot down a comment, it will start offering real-time, tailored suggestions that fit your coding style.&#x20;

Powered by the latest and best-in-class LLMs, Bito offers autocomplete capabilities for SQL queries, regex patterns, functions, loops, if-else blocks, and more—right within your IDE as you code&#x20;

Curious to know more? Dive into our [documentation](https://docs.bito.ai/changelog/broken-reference) to see how this feature can make your coding life a breeze.

{% hint style="info" %}
AI Code Completions are disabled by default. Learn how to [**Enable/Disable AI Code Completions**](https://docs.bito.ai/changelog/broken-reference) in settings.
{% endhint %}

{% embed url="<https://youtu.be/tyGsPOva4Zg>" %}

**Slash `/` command support for Templates:** Using templates in Bito just got a whole lot easier and cooler! All you have to do is type a forward slash **`/`** right at the start in the Bito chat box. Once you do, the template menu will open from where you can quickly select and use the template you want.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5ujTusk2cR9lLbHUOu4s%2Fscrnli_11_8_2023_9-41-56%20AM.png?alt=media&#x26;token=20a1e7d1-58b4-4baf-883d-75ec4ff039b0" alt="" width="454"><figcaption></figcaption></figure>

Want to narrow down your choices? Simply start typing after the **`/`** slash, and it'll only show you templates that match your words. And hey, you can also use the arrow keys, or Tab and Shift + Tab, to navigate the templates menu.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbBXPc23uvJ2LKKXxGDOK%2Fscrnli_11_8_2023_9-48-51%20AM.png?alt=media&#x26;token=567f8993-7b40-4110-a60c-1db3b18b77d1" alt=""><figcaption></figcaption></figure>

Give it a try and make your coding experience super smooth and fun!&#x20;

## IDE V1.2.0 - 23rd Oct 2023

{% hint style="info" %}
Currently, the **AI Code Completions** feature is only available in [Bito's VS Code extension](https://marketplace.visualstudio.com/items?itemName=Bito.Bito). It will be coming soon for JetBrains IDEs.
{% endhint %}

<mark style="color:blue;">**New Feature**</mark>

**AI Code Completions:** Get real-time and personalized code completions from AI that understands your code. Just type some initial code in your file or provide explicit instructions as comments, and watch Bito suggest the code you're most likely to write next.&#x20;

Powered by the latest and best-in-class LLMs, Bito offers autocomplete capabilities for SQL queries, regex patterns, functions, loops, if-else blocks, and more—right within your IDE as you code&#x20;

Curious to know more? Dive into our [documentation](https://docs.bito.ai/changelog/broken-reference) to see how this feature can make your coding life a breeze.

{% hint style="info" %}
In release 1.2.0, AI Code Completions are disabled by default. Learn how to [**Enable/Disable AI Code Completions**](https://docs.bito.ai/changelog/broken-reference) in VS Code settings.
{% endhint %}

{% embed url="<https://youtu.be/TaaxGAG34Aw>" %}

## IDE V1.1.9 - 18th Oct 2023

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Fresh Look:** The Bito Panel UI is now more intuitive and pleasing to work with. We've put most buttons closer to where you type, and guess what? You've got 30% more screen space to see the AI's answers!

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyO1HMpmpmJPU8I4wc4ef%2F1.png?alt=media&#x26;token=befe3774-f690-4016-9417-c38ef3a1fd05" alt="" width="340"><figcaption></figcaption></figure>

**Custom Prompt Templates Output:** Select where the results from your [Custom Prompt Templates](https://docs.bito.ai/changelog/broken-reference) should be displayed. Your options are:&#x20;

* Display in Bito panel (Default)&#x20;
* Output in diff view

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbMOVQRtpvoH2pfkUPbU6%2F2.png?alt=media&#x26;token=66fd1815-0a74-4c66-83ab-b6218f22cbb1" alt="" width="366"><figcaption></figcaption></figure>

**Clickable File Links:** Source code file names that are mentioned in [AI Chat](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito) answers are now clickable. A single click will open the respective file directly in your IDE. No more hunting for files!&#x20;

**Speed Boost:** We've supercharged [indexing in VS Code](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-visual-studio-code) to match pace with JetBrains IDEs (e.g., IntelliJ IDEA, PyCharm, etc.) and optimized how we calculate [index sizes](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/managing-index-size) for both.&#x20;

**Bug Fixes:** No more hiccups with the [Generate Comment](https://docs.bito.ai/ai-code-reviews-in-ide/templates) feature in Bito menu; it will now correctly show outputs in [Diff View](https://docs.bito.ai/changelog/broken-reference). Also, we have resolved some customer reported issues where Diff View wasn't working.&#x20;

## IDE V1.1.8 - 26th Sep 2023

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Performance Upgrades:** Bito can now process multiple chunks at once, slashing network calls and giving a considerable boost to indexing speed for both JetBrains & VS Code users. Plus, VS Code users can expect an even swifter performance with our newly integrated batched writes.&#x20;

**Bug Fixes:** Our team has diligently tackled issues from V1.1.7:&#x20;

1. We've resolved the race conditions that occurred when switching between multiple IDE windows.&#x20;
2. In Bito's ["AI that Understands Your Code"](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code) feature, we've corrected problems with the "my code" keyword in Spanish and Portuguese. Additionally, Polish language keywords are now supported.
3. The keyboard shortcut for code insertion in the IDE extension has been fixed.

## IDE V1.1.7 - 8th Sep 2023

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

<mark style="color:blue;">**Improvements in AI that Understands Your Code**</mark>

After introducing code-understanding capabilities in our previous versions, we've now made it even better in this release. Learn more about Bito's [**AI that Understands Your Code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code) feature.&#x20;

**Introducing .bitoignore:** You can now tell Bito to skip certain files and folders during indexing. Perfect for indexing those big repositories without the unimportant stuff.&#x20;

**30% to 40% Faster Indexing:** We have improved the way your repo is indexed. Now, Bito can understand every 10MB of code in just 16 to 18 minutes, a big leap from the old 30-minute mark. Enjoy the speed!&#x20;

**Up to 120MB Max Repo Size:** You can now index larger repositories. We've bumped up the indexing limit to 120MB per repo. Need to trim a bit? Use the .bitoignore feature to exclude specific files and folders and remain within the limit. Happy indexing!&#x20;

**Over-100% Indexing Bug Fixed:** Good news! We've fixed that quirky bug where the indexing went beyond 100% during repo reindexing. No more overachieving percentages!&#x20;

<mark style="color:blue;">**Billing Related Bug Fixes**</mark>

**Billing Invite Glitch: All Sorted!** Had trouble inviting users via the Bito Web UI for billing? Good news! We've fixed that hiccup. Invite away!

## IDE V1.1.6 - 28th Aug 2023

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**File/Folder Filtering Improved for Indexing:** We've added more files and folders to the exclusion list, speeding up the indexing process by preventing Bito from indexing unnecessary files and folders.

**Progress Indicator for Indexing:** Index building now has a progress indicator based on the number of files indexed. The progress indicator for the current folder is updated in real-time. However, for projects in the "Other projects" section, the progress indicator is updated every 5 minutes.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbBH06CkjI2BtYteaRGnj%2Fwn_1.png?alt=media&#x26;token=9ba467b1-2f80-4272-892f-9e1768d2c32e" alt=""><figcaption></figcaption></figure>

**Added "Indexing is paused" status:** This status will be displayed for a project that was previously being indexed but is now paused for some reason. Generally, if you close the IDE while the project is being indexed, its status will change from "Indexing in progress" to "Indexing is paused."

## IDE V1.1.4 - 14th Aug 2023

<mark style="color:blue;">**New Feature**</mark>

**AI that Understands Your Code:** Bito's most requested feature is here. Bito AI now comprehends your codebase inside out using AI indexing, ensuring privacy as the index stays on your system. &#x20;

Simply add "**my code**" or “**我的仓库**” in Chinese to your AI requests and watch Bito efficiently navigate your repository, providing precise solutions.&#x20;

&#x20;Try it out with queries like:&#x20;

1. Find errors in scraper.py in my code.&#x20;
2. Write frontend and backend code for user authentication, using the authentication service in my code.&#x20;
3. List files and changes needed to add a "desc" column in the "raw\_data" table in the "dailyReport" DB in my code.&#x20;

Have an even better experience with Bito’s AI assistant, seamlessly attuned to your codebase. Explore more in the documentation [here](https://docs.bito.ai/feature-guides/ai-that-understands-your-codebase).

This feature is currently available to our [paid plan](https://bito.ai/pricing/) subscribers and will be launched for free plan subscribers soon.&#x20;

## IDE V1.1.3 - 4th Aug 2023

<mark style="color:blue;">**Improvement**</mark>

**Expanded Contextual Memory:** Bito now has a larger contextual memory and output capability, that can process up to 40,000 characters (around 18 single-spaced pages). This expanded memory encompasses the provided prompt, existing context from previous chats, and the generated output.&#x20;

Our latest version of Bito offers 3X longer conversation memory, ensuring contextually accurate responses. Chat like never before!

## IDE V1.0.138 & CLI V3.1 - 23rd May 2023

<mark style="color:blue;">**New Features**</mark>

**Language support for AI Output:** We're excited to announce that Bito now supports multiple languages in IDEs, allowing you to converse in your preferred language. With this update, you can easily switch to your desired language within the chat interface.&#x20;

Supported languages: English, Bulgarian, Chinese (Simplified), Chinese (Traditional), Czech, French, German, Hungarian, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Turkish, and Vietnamese.&#x20;

How to Access:&#x20;

1. Click on the settings icon in the plugin interface's top right corner.&#x20;
2. Select your preferred language from the list of supported languages.&#x20;
3. Save your choice; Bito will now communicate with you in the selected language.&#x20;

<div><figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FI5muFv1cBXSbLLtCnD4Y%2F1_1.jpg?alt=media&#x26;token=2626b3bc-9dc7-47f1-a531-00498a87cc9c" alt=""><figcaption><p>Language Settings</p></figcaption></figure> <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FELWS5ic00BEypXVu1wyU%2F2.jpg?alt=media&#x26;token=8374fd2f-05cb-4a18-a27c-40812faf32cf" alt=""><figcaption><p>Language Options</p></figcaption></figure></div>

Note: All responses from Bito will appear in the selected language, regardless of the input language.  &#x20;

Enjoy the convenience of conversing with Bito in your native language and take your coding experience to a new level!&#x20;

**Custom Templates in IDE Context Menu:** Your requests are our priority! We are pleased to introduce running "Custom Prompt Templates" to the IDE context menu. Building on the success of our previous release, where we introduced [custom templates](https://docs.bito.ai/custom-prompt-templates) in the Bito plugin, we've taken it a step further. Now, you can access your personalized templates directly from the context menu in your IDE from "Run Custom Prompt Template"

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F2gyImeKm5jiyw92yU0O5%2Fimage.png?alt=media&#x26;token=9a9a4218-dfe8-4664-bd80-8fa693d27c72" alt=""><figcaption><p>Execute Custom Prompt Template with Context Menu</p></figcaption></figure>

Clicking "Run Custom Prompt Template" opens up a list of your templates in the Command Pallet or other secondary menu, depending on your IDE.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FL15IkzjHNWCslcwKaarQ%2Fimage.png?alt=media&#x26;token=cb6bf0ee-0e6a-43b4-9bc1-073dba0e92cf" alt=""><figcaption></figcaption></figure>

**Introducing Context in Bito CLI:** Bito CLI can now remember previous conversations, allowing for a more seamless and contextual experience. With the addition of context file support, you can now pass a context file using the -c command to preserve the context and history of your conversation. Watch our helpful tutorial to learn more about utilizing context files in Bito CLI.&#x20;

Say goodbye to repetitive context-setting and dive straight into productive and context-aware discussions with Bito CLI! 💬💡

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

**Bito Version 1.0.135 and IntelliJ IDEA 2021.1.x Compatibility:** We recently discovered an issue where Bito version 1.0.135 was not compatible with specific older versions of IntelliJ IDEA. We want to assure you that we have addressed this compatibility concern, and Bito is now fully compatible with IntelliJ IDEA.&#x20;

**Automatic CLI updates:** Say goodbye to manual updates! We're thrilled to introduce the CLI Auto-update feature. With this, Bito CLI will automatically check for updates whenever you open it. If a new version is available, the CLI will seamlessly update itself, ensuring you're always equipped with the latest enhancements, bug fixes, and features. Stay ahead of the curve without the hassle of manual updates!&#x20;

## IDE V1.0.135 - 1st May 2023

<mark style="color:blue;">**New Features**</mark>

**Introducing  Custom Prompt Template:** Bito allows you to create and save custom prompt templates for IDEs. Define a template name and prompt, and Bito will execute it on the selected code. You can add up to 4 custom templates and edit or remove them as needed. Learn more about [Custom Prompt Template](https://docs.bito.ai/changelog/broken-reference).&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FohBtaYzf0MEZrWmm7dyB%2FMy%20template.PNG?alt=media&#x26;token=0cfe10b9-b51d-44b6-b59a-5390a71abd3f" alt=""><figcaption><p>My custom template</p></figcaption></figure>

<mark style="color:blue;">**Improvement and Bug fixes**</mark>

1. **Resolved OTP verification issue:** Unfortunately, some customers experienced an issue last week where they could not complete OTP verification during login to the Bito Plugin. We are happy to report that this issue has been resolved in the latest release.
2. **Fix for Context Menu and Shortcuts on Ubuntu 2023.1 JetBrains:** Fixed an issue where the context menu and shortcuts were not functioning correctly on Ubuntu 2023.1 JetBrains, causing the selection of code and options like explain code not to work as intended. This has now been resolved.

## IDE V1.0.134 & CLI 3.0 - 14th April 2023

#### <mark style="color:blue;">New Features</mark>

1. **CLI "My Prompt":** We're excited to announce the launch of Bito CLI My Prompt, our first step in empowering developers to automate tasks with AI.   My Prompt makes creating accurate and concise prompts for your development tasks easy, reusing them with simple Bito commands. It allows you to automate various coding tasks, such as generating commit messages, test data, or code documentation. The possibilities are limitless. Two new command line options support My Prompt feature:

*-p option: To specify a file containing the prompt or instructions for the AI models to operate.*

-f option: To specify the file to perform the operation/instructions described in the prompt file.

Here are two examples for you to see My Prompt in action:

***Create Git Commit Messages and Markdown Documentation with Ease using Bito CLI My Prompt***

{% embed url="<https://youtu.be/q42hqwT-jsg>" %}

**Generate test data using Bito CLI My Prompt:**

{% embed url="<https://youtu.be/GYa0p511NUQ>" %}

2. **Generate Unit Test Shortcut (Waitlist):** With this new shortcut button, developers can now easily generate unit tests for their code with just a click. This new feature is designed to streamline the testing process and improve code quality, making it easier for developers to deliver high-quality work.

   &#x20;

   Be the first to try our exciting new feature! You can now add yourself to the waitlist by clicking on the icon.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ffmy70fMFHLQeinQeRMbe%2Fimage.png?alt=media&#x26;token=bcbe5296-ad6a-4ea4-80cc-50e22b363e39" alt=""><figcaption></figcaption></figure>

<mark style="color:blue;">**Improvement and Bug fixes:**</mark>

1. Improved Explain Code Shortcut: Previously, the Explain Code shortcut button provided a summary of the code logic, but with our latest update, it now also provides a detailed, step-by-step explanation of the code. We have merged two previous shortcuts into one. Now, developers can easily understand the code logic and its components.&#x20;
2. We've fixed an issue where the CTRL+C command was not working on Mac OS. Now, you can easily copy and paste text without any problems.
3. We've resolved an issue with context menus and shortcuts not working on Ubuntu 2023.1 JetBrains. This fix ensures that all shortcuts and context menus work as expected, making it easier for developers to navigate the IDE.
4. We've fixed an issue on Linux version 2023.1 IntelliJ where users could not type anything in the text area of our chat interface. This fix ensures that users can input text as expected.

## IDE V1.0.133 - 30th March 2023

#### <mark style="color:blue;">New Features</mark>

1. **Chat Session History:** In the last release, we added [Context-Aware chat](#new-features-1).  This release lets you view past chat sessions on the chat interface. The history feature is located at the top right corner of the chat interface. With this, users can easily revisit their past conversations, making it easier to pick up where they left off. Additionally, users can share their past chat sessions with colleagues, making it easier to collaborate and share knowledge. The new chat session History adds another layer of convenience and functionality to the AI assistant.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFyTzkRHjrWowUsy2DrDn%2Fimage.png?alt=media&#x26;token=e2c79921-1117-489e-baca-81983aaadf83" alt=""><figcaption><p>Access Chat Session History</p></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FPgfwhRVPY4DDm8b6x3GX%2Fimage.png?alt=media&#x26;token=b054e65d-8ea9-4c57-aeb1-122265ddfff7" alt=""><figcaption><p>History of Chat Sessions</p></figcaption></figure>

1. **GPT-4:** We are thrilled to announce that we have integrated GPT-4, the industry's latest and most powerful generation model. With GPT-4 integration, Bito's AI assistant is now even more powerful and capable of providing detailed and accurate responses to various programming-related queries. Developers can ask complex questions and receive natural language responses that are both helpful and informative.
2. **Long Code Input:** Bito fully leverages GPT-4's increased token limit. With this, users could input and receive feedback on larger blocks of code, making it easier to troubleshoot and optimize code for performance. The exact size of the code depends on many factors, including how long the current chat session is. **Bito can take 2-3x longer code input than the input length supported by the previous version of Bito.**&#x20;

{% hint style="info" %}
Note that we use a combination of GPT-4 and GPT Turbo 3.5 models. We route long, complex prompts to GPT-4 and short prompts to Turbo 3.5 models. This helps us balance the quality of output that Bito generates and the cost of servicing users. If you ask Bito about the model in use, most likely, it will say GPT-3, as this simple prompt is routed to Turbo 3.5.&#x20;

We may offer a paid version of Bito in the future that always uses GPT-4 or other advanced models. However, our internal testing has shown that the output quality for simple and short prompts is not very different between 3.5 and 4. The full benefit of GPT-4 is realized in complex, long prompts or when prompts are related to niche facts that models are likely to hallucinate. We have not seen "hallucination" as a major issue for the development-related use cases that Bito is targeting.&#x20;
{% endhint %}

<mark style="color:blue;">**Improvement and Bug fixes:**</mark>

1. **Stop Generation in Chat Interface:** We have added a Stop Generation button to our chat interface, allowing users to stop the response generation process anytime. This feature will be especially helpful in cases where users have asked a question incorrectly or want to modify their question before receiving a response.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fim46UjPYspL0gpRjrW5C%2Fimage.png?alt=media&#x26;token=528a0a02-cd39-47e5-86ba-06be83fa15ca" alt=""><figcaption></figcaption></figure>

2. **Diff View Bug Fix** – We have resolved a bug in our VS Code Extension v1.0.132. The bug affected one of our key features, Diff view, which provides a side-by-side view of changes proposed by Bito AI in the IDE. The bug was causing multiple diff views to open simultaneously, which could be confusing. This has been fixed now.&#x20;

## IDE V1.0.132 & CLI V2.0 - 16th March 2023

#### <mark style="color:blue;">**New Features**</mark>

1. **Context-Aware Chat:** Our latest update is the most critical one since our launch. Many of our users had requested an interactive chat experience similar to ChatGPT, which was unavailable in earlier versions. With this new update, you can now ask follow-up questions to refine the output, which considers the chat history for context. You can initiate a chat session with a custom request, use Bito Shortcuts like Performance Check, and follow up with additional prompts.  To give you an idea of how it works, here is an example of an interactive chat session.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fca12fq7crzUMWpMNACig%2Fimage.png?alt=media&#x26;token=49da75e2-cad2-4882-8efd-aa8f447765cb" alt=""><figcaption></figcaption></figure>

2. **Instant Results:** With the latest release of Bito, you can now experience instant results that appear within seconds. In previous versions, users had to wait patiently while being entertained by amusing messages, but we understand that this could become frustrating over time. This new update implements streaming output, allowing you to access the information you need with minimal delay immediately.

Note: Context-Aware Chat and Instant Results are available in the latest version of [Bito CLI](https://github.com/gitbito/cli) and [Chrome Extension](https://chrome.google.com/webstore/detail/bito-ai-use-chatgpt-to-10/afchmofckbnlkpnjkdikdkgnjelhlbkg?hl=en).

<mark style="color:blue;">**Improvements & Bug Fixes**</mark>

1. **Dynamic Font Size & Family:** This feature in Bito adjusts the interface's font size and family dynamically based on the font size you have set up in your Integrated Development Environment (IDE) settings. The goal of this feature is to make the chat interface more accessible and comfortable to use for all users, regardless of their font preferences, visual acuity, or screen size.
2. **Configure Keyboard Shortcuts**: This feature allows users to customize the default keyboard shortcuts in Bito to avoid conflicts with other IDE-specific shortcuts they may be using. By configuring keyboard shortcuts, users can streamline their workflow and increase their productivity by accessing Bito functions more quickly and efficiently. The instructions for configuring keyboard shortcuts in Bito are in this [link](https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito/keyboard-shortcuts#change-default-keyboard-shortcuts).

## IDE V1.0.130 - 24nd Feb 2023

#### <mark style="color:blue;">**New Features**</mark>

1. **Diff View:** Bito Shortcuts added many quick operations on your existing code, such as checking performance, improving code readability, or security check. The Diff View in IDE now gives a side-by-side view of the changes proposed by Bito AI. Bito automatically creates a temp file with the proposed code changes and displays diff view with your current code file. IDE's built-in "diff review feature" lets you review and accept/reject the changes. We love that Bito AI can improve your code in many ways, but we want you to be in control while incorporating changes to your code repository. Diff view is built just for that.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FAvKmLxli6s6jS9OIhcS2%2Fimage.png?alt=media&#x26;token=f0942238-8c45-4d42-831f-b1f4246faf2b" alt=""><figcaption><p>Diff view for the code changes proposed by Bito</p></figcaption></figure>

2. **Keyboard Accessibility:** We have added keyboard accessibility to all UI elements in Bito. You can navigate with Tab and Shift + Tab. Standard keys such as Enter, ESC, and Up/Down arrows work. You can also move between Q\&A with the Up and Down arrow keys once the Q/A container is focused.
3. **Keyboard Shortcuts:** Keyboard shortcuts for the most commonly used commands.&#x20;
   * &#x20;SHIFT+ CTRL + O: Brings Bito panel in focus. With this shortcut, you can toggle Bito Panel on/off in the JetBrains extensions. In VS Code, the shortcut will open the Bito panel (if not already opened). You can use shortcuts of other tabs (e.g. CTRL + SHIFT + E for Explorer) to close Bito. &#x20;
   * SPACEBAR: Puts cursor in the chatbox when Bito panel is in focus.
   * ENTER: Execute the chat command.
   * CTRL+ ENTER or SHIFT + ENTER: Adds a new line in the chatbox.
   * The following shortcuts work on the Q\&A when a Q\&A is selected.&#x20;
     1. CTRL + C: Copy the answer to the clipboard.
     2. CTRL + I: Insert the answer in the code editor.&#x20;
     3. CTRL + D: Toggle the diff view (when Diff View is applicable)
     4. CTRL + UP/DOWN (Mac: CTRL + SHIFT + UP/DOWN): Expand and collapse the code block where applicable.&#x20;
     5. CTRL + L : Regnerate the answer.
     6. CTRL + U: Modify the prompt for the selected Q\&A. Bito copies the prompt in the chatbox that you can modify as needed.&#x20;
   * CTRL + M: Modify the most recently executed prompt.&#x20;
   * CTRL + UP/DOWN (CTRL + SHIFT + UP/DOWN on Mac): Expands and collapses the "Shortcut" panel in Bito.&#x20;
4. **Sharing:** You can easily share a single question and answer to any channel. Every question and answer has a web permalink that you can share on Twitter and E-mail directly. Copy and paste the link into Slack, Teams, Jira, or Confluence.
5. **Regenerate** the results of any prompt with a single click.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FE6lTSPl9UjFGFZc9RJ5l%2Fimage.png?alt=media&#x26;token=57d09d57-bf7a-424d-b5d6-603aeeafb34e" alt=""><figcaption></figcaption></figure>

6. **Edit prompt** lets you modify a previously executed prompt. You can edit any prompt with the "Edit Prompt" action next to the question.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FDy5abQH18ErwRlzJX9ZE%2Fimage.png?alt=media&#x26;token=4a390664-b42d-48b1-84bd-196506d77bfc" alt=""><figcaption><p>Edit any prompt. </p></figcaption></figure>

To modify the most recent prompt, click the "Redo" icon in the chatbox.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FIesRBsIQ5X6nojFSzv0t%2Fimage.png?alt=media&#x26;token=f5ec06e6-2525-4a1c-8ace-f5e93bd389ac" alt=""><figcaption><p>Edit the last prompt</p></figcaption></figure>

<mark style="color:blue;">**Improvements & Bug Fixes**</mark>

1. The Bito icon in the JetBrains IDE is optimized, so the extension panel doesn't take up space when not in use.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FkOXfbAhYo8UtCYlQN2xH%2Fimage.png?alt=media&#x26;token=79dcbb58-3352-4df9-92f4-8b2085f5af72" alt=""><figcaption></figcaption></figure>

## V1.0.129 - 31st Jan 2023

#### <mark style="color:blue;">**Improvements & Bug Fixes**</mark>

1. **Code Block** formatting and syntax highlighting make it easy to distinguish code from the text content in the chat output. When you use Shortcuts to transform any existing code, the original code is collapsed by default in the question box, thus giving more space for the answer, and the output code is formatted and syntax highlighted.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FovocCUypfkiuXEcjetPV%2Fimage.png?alt=media&#x26;token=bb41cf8e-dd19-4417-b178-611526230fee" alt=""><figcaption></figcaption></figure>

2. Several UI improvements to make Bito look and work great in your IDE. We have reduced padding around the questions and answers blocks so you see more content. The scrollbars are optimized to take up less space and reduce visual clutter.&#x20;

## V1.0.128 - 18th Jan 2023

#### <mark style="color:blue;">**New Features**</mark>

1. **Shortcuts** give your existing code power of Bito AI. Select any code snippet in your code editor, and use Bito Shortcuts to run security, performance, or style check. Know how the code works, what it does, or generate comments. You can clean code, improve readability or automatically add exception handling. Behind the scene, we automatically generate the best possible prompt for the best AI output, so you don't have to spend time with prompts.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKCpTz8rwPkECiEWpxXUE%2Fimage.png?alt=media&#x26;token=ad1404ff-f9f4-421b-97fe-50fe5c1437ad" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">**Improvements & Bug Fixes**</mark>

1. Fixed crash when using Bito JetBrain extension with PyCharm.
2. Fixed Git dependency issue in the Visual Studio Code extension.&#x20;

## V1.0.127 - 13th Jan 2023

#### <mark style="color:blue;">**New Features**</mark>

1. **Additional pre-defined** prompts to improve the quality and readability of the code.
   * **Improve Readability** - Makes code more readable by organizing the better
   * **Clean Code** - Remove debugging, commented code, and log-related code.
   * **Make Robust** - Add exception/error handling to the code.
   * **Add Steps** - Add explanation steps to the block of codes.&#x20;

#### <mark style="color:blue;">**Improvement and Bug Fixes**</mark>

1. Improved UX for smaller screen resolution.&#x20;

## V1.0.125 - 26th Dec 2022

#### <mark style="color:blue;">**New Features**</mark>

1. **Pre-defined prompts** for various checks on your existing code. Select your code and choose one of the below options:
   * **Explain Steps:** Explain "How the code works?".
   * **Explain Code:** Explain "What does this code do?"
   * **Generate Comment:** Generate a comment for the selected code.
   * **Performance Check:** Check the selected code for performance and gives pointers to fix the performance. It also rewrites the code with the suggested performance fixes,
   * **Security Check:** Check the selected code for security issues and gives pointers to fix them. It also rewrites the code with the suggested security fixes,
   * **Style Check:** Check the selected code for the style issues and gives suggestions to fix them. It also rewrites the code with the suggested style fixes.
2. **Command Pallet** support in Visual Studio Code. All Bito commands are accessible in the Visual Studio Command Pallet.
3. **Insert output from Bito AI** into your code file with a single click. This is great for inserting any generated code in your code editor. It inserts the code wherever your cursor is, or if you want to replace the existing code, select the code and insert the new code.&#x20;

#### <mark style="color:blue;">Improvements & Bug Fixes</mark>

1. **Keyboard** support for the AI Chatbox. Send the request with 'Enter' and add a new line to the chat with 'CTRL+Enter.'
