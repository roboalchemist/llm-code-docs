# Graphite Documentation

Source: https://graphite.com/docs/llms-full.txt

---

# Advanced Tutorials
Source: https://graphite-58cc94ce.mintlify.dev/docs/advanced-tutorials

Take it to the next level with advanced CLI commands.

<CardGroup cols={3}>
  <Card href="/edit-branch-order#gt-reorder-to-modify-branch-ordering" icon="git-branch" title="Edit the branch order in a stack">
    Use the CLI to easily rearrange branches in your stack.
  </Card>

  <Card href="/collaborate-on-a-stack" icon="git-branch-plus" title="Collaborate on a stack">
    Collaborate with your teammates on a stack of pull requests.
  </Card>

  <Card href="/multiple-trunks" icon="split" title="Multitrunk support">
    Create and sync pull requests against multiple trunks.
  </Card>
</CardGroup>

## Watch a video tutorial

Follow along with our video tutorials! In two-minute pieces, we break down each command that you'll need to know to get started with the Graphite CLI.

<Frame>
  <iframe width="750" height="360" src="https://www.youtube.com/embed/pYKuimOYWaA?si=lfPQ3iocq2z9UU8Z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>


# LLM-Friendly Documentation
Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-ingestion

Optimized formats of Graphite Documentation for ingestion as context for LLMs and AI tools.

[llms-txt](https://llmstxt.org/) files are specialized documentation resources designed specifically for AI and Large Language Model (LLM) consumption. These files provide structured, machine-readable documentation.

### /llms.txt

The `/llms.txt` file is an industry standard that helps general-purpose LLMs index more efficiently, similar to how a sitemap helps search engines. AI tools can use this file to understand documentation structure.

Download Graphite Documentation's `/llms.txt` file at: [https://graphite.com/docs/llms.txt](https://graphite.com/docs/llms.txt)

### /llms-full.txt

The `/llms-full.txt` file combines the entire documentation site into a single file as full context for AI tools.

Download Graphite Documentation's `/llms-full.txt` file at: [https://graphite.com/docs/llms-full.txt](https://graphite.com/docs/llms-full.txt)


# AI Privacy and Security
Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-privacy-and-security

Graphite offers a handful of AI features to automate parts of the developer workflow. These features are opt-in and do not store or train on your data.

Graphite offers a handful of generative AI features to automate parts of the developer workflow.

Examples of our AI features include:

* Generating pull request titles and descriptions

* Generating review comments

* Generating suggested edits in response to review comments

* And others coming soon

We know that AI can be a sensitive topic for many organizations, which is why:

* By default, Graphite does not include your data in any requests we make to either of our AI subprocessors (currently Anthropic and OpenAI;see below for more details)

* Graphite will always ask for user approval before triggering or enabling features that include your data in requests to either of these subprocessors

* Neither Graphite nor any of its subprocessors use your data to train their models

* Graphite holds a high bar when protecting your data, as outlined in our [Terms of Service](https://graphite.com/terms-of-service) and [Privacy Policy](https://graphite.com/privacy)

Many of our AI features are powered through partnerships with Anthropic and OpenAI, who currently act as our AI subprocessors. We have strict agreements in place with both companies that explicitly prohibit the use of your data to train models, and your data remains protected and confidential at all times. Our agreements are available here:

* Anthropic:

  * Agreement: [https://www.anthropic.com/legal/commercial-terms](https://www.anthropic.com/legal/commercial-terms)

  * Your data is not used for training: [https://support.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training#h\_1a7d240480](https://support.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training#h_1a7d240480)

* OpenAI:

  * Agreement: [https://openai.com/policies/business-terms/](https://openai.com/policies/business-terms/)

  * Your data is not used for training: [https://openai.com/enterprise-privacy/](https://openai.com/enterprise-privacy/)

These subprocessors receive the minimum data necessary to generate the best possible response; examples of data we may send them include:

* Any metadata around the pull request (author, timestamp, etc.)

* The code the pull request changes

* Related or similar pull requests

* Related or similar parts of your codebase

We are committed to protecting your data and privacy at all times, and we understand that some organizations would rather not use these features at all. To disable AI features across your entire organization, please email [support@graphite.dev](mailto:support@graphite.dev) and request a complete block of all AI features for your organization. You can always email us again if you change your mind, and we will unblock these features for your organization upon request.

Lastly, depending on your plan, enabling some of these features may have additional costs. For more details on our features and pricing, please see our [pricing page](https://graphite.com/pricing).


# Review comments
Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-review-comments

Understanding Graphite Agent's feedback and how to get the most value from it

## How Graphite Agent provides feedback

When Graphite Agent identifies an issue in a pull request, it adds a comment directly on the relevant lines of code. Each comment includes:

1. A clear description of the problem
2. An explanation of why it matters
3. A concrete suggestion for how to fix it

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=edfecd70e73ffcf614d47e7d71789575" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=aa256609b96cba52119fc2f20cec1d2c 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=52759b1714791cfeb828219ad97e06f6 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1854017b46299e9aa933352d13523e7b 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=07b9e9ea347f0c02d110fde87130dc1b 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=0a7d597db2c9ac0e936f8d72a713035a 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8a0393b0-1742254644-diamond-product-images_0007_08-commit-suggestion.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e6493f91e72786c285672740f7ac0ef8 2500w" />
</Frame>

You can see Graphite Agent's comments, suggestions, and choose to commit suggestions — just like your teammates'.

## Types of issues Graphite Agent identifies

Graphite Agent catches a wide range of issues that often slip through manual code review and testing:

### Logic bugs

Graphite Agent identifies when your implementation doesn't match the intended behavior, detecting issues like:

* Functions that don't accomplish what they're named to do
* Inconsistencies between code behavior and documentation
* Mismatches between API usage and implementation
* Off-by-one errors and incorrect loop boundaries

### Edge cases

Graphite Agent finds potential failure modes that aren't handled in your code:

* Missing null checks or error handling
* Race conditions in asynchronous code
* Memory leaks and resource management issues
* Unexpected side effects

### Security vulnerabilities

Graphite Agent spots security issues before they reach production:

* SQL injection vulnerabilities
* Cross-site scripting (XSS) opportunities
* Authorization bypass possibilities
* Insecure cryptographic practices

### Performance issues

Graphite Agent detects code that might cause performance problems:

* Inefficient algorithms or data structures
* Unnecessary API calls or database queries
* Memory-intensive operations that could be optimized
* N+1 query patterns

### Accidentally committed code

Graphite Agent catches code that was likely not meant to be committed:

* Debug statements and console logs
* Test data and development configurations
* Commented-out code blocks
* Temporary workarounds

## Tracking AI review impact

You can monitor AI review activity and impact from the AI code review dashboard, accessible via the [AI code review settings page](https://app.graphite.com/ai-reviews).

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-2.png?fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=8b24fe51f217281a66dccc2cecbcffe0" data-og-width="2560" width="2560" data-og-height="1504" height="1504" data-path="images/ai-reviews-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-2.png?w=280&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=fdaea466614b5f8979544b1cfdecdc44 280w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-2.png?w=560&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=da540df77217edcf786b345cdc6fc7a6 560w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-2.png?w=840&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=053ab7c64c0e6cac435d5dab5cf0eff3 840w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-2.png?w=1100&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=cf42512a9576d9177999fd82bf1f8c5d 1100w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-2.png?w=1650&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=9e6ead0d2af3154f06dad4edf70010bc 1650w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-2.png?w=2500&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=b82207e768430427d18670ae16366309 2500w" />
</Frame>

The **Insights and metrics** section provides:

* Total issues found across all reviewed PRs, broken down by category (logic bugs, security issues, edge cases, etc.)
* Statistics on PRs reviewed and issues that led to fixes
* Comment feedback metrics showing upvote/downvote rates
* Visual breakdown of issue types discovered

<Frame caption="The Highlights feed shows impactful issues caught by Graphite Agent">
  <img src="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=b52980162334664fa01c861fc69c4d50" data-og-width="2560" width="2560" data-og-height="1504" height="1504" data-path="images/ai-reviews-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=280&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=66330e5654e545542cbe0c38ee00695d 280w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=560&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=b34880a3deca52d91236d17ec7a39741 560w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=840&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e047aeec7bdf05c291da84a7ffc2d19f 840w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=1100&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=8fb1ca6e3268cd075b9634b2752315c3 1100w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=1650&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=a89d4a3aa760b8a76fa462b2ece5923f 1650w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=2500&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=98c38cccfde9b04dbb1b92b4d3042825 2500w" />
</Frame>

The **Highlights** and **Feed** tabs let you:

* View all comments Graphite Agent has left across your repositories
* Filter by category to focus on specific types of issues
* See prevented bugs and their potential impact
* Review code snippets with inline explanations

## How to check AI review status

For any pull request, you can see the AI review status in the right-hand panel of the PR page:

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=40fe4eb00134716cb9666290cfb120b6" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2cca6aa3c14dfdb324ad6e655b663815 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c588c4b8c65b45fd9bec924802a0014b 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c9b4f5410d587529b8e44d4ed51c32eb 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b10de1dec9bd2428554c09457154548c 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=35d0a62c2ccfbd6084d4e9233fc6abc7 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0a7546b2-1742254644-diamond-product-images_0006_07-pr-page.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=722f1dc9c3fe40f8d76ed706bc5fd7bf 2500w" />
</Frame>

The status will show as:

* **Running**: Graphite Agent is currently analyzing the PR
* **Completed**: Graphite Agent has finished reviewing and left any relevant comments
* **Not running**: The PR won't be analyzed (e.g., if the PR exceeds 100,000 characters)


# Customization
Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-review-customization

Tailor AI reviews to your team's specific needs and coding standards

## Making AI reviews work for your team

While Graphite Agent will catch bugs out of the box, you can customize its behavior to better match your team's specific needs and coding standards. AI reviews offer two primary customization options: **Exclusions** and **Custom rules**.

<Frame caption="AI reviews customization interface">
  <img src="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=4ecc00cdba3cb276a28cf7f02348d6ba" data-og-width="2336" width="2336" data-og-height="1584" height="1584" data-path="images/ai-reviewer-customizations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=280&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=801b12656fd7f31e18412c9dc5b41525 280w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=560&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=cbd77ac882797e04572734fff53a077e 560w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=840&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=f42ac19ca3a0b722c40cc72dc20162e8 840w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=1100&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=2ea41cddd6dabc78c98826e82e2cf481 1100w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=1650&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=24c4692118a0bee9f6824f717560a0ac 1650w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-customizations.png?w=2500&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=8c238155ecd08f82f0d274e228c43d40 2500w" />
</Frame>

## Exclusions: Specifying what to ignore

Comment exclusions allow you to specify situations where Graphite Agent should **not** leave comments. This reduces noise and focuses AI reviews on what matters most to your team.

Common exclusion use cases:

* **Ignore generated code**: Prevent extraneous comments on generated code from build artifacts, schemas, and other generated files.
* **Skip specific types of comments**: Turn off categories of feedback that aren't relevant to your team
* **Ignore certain repositories or directories**: Focus AI reviews where they matter most
* **Exclude specific patterns**: Define patterns that shouldn't be flagged (e.g., team-specific style conventions)

### Best practices for writing exclusions

Make the language as targeted as possible by specifying the exact scope where the exclusion should apply. If an exclusion is written too broadly, then Graphite Agent may not leave valid comments.

Bad example:

```
### Bad example: Overly broad exclusion

Don't suggest performance improvements.
```

Why is this bad?

* This is too broad and would miss legitimate performance issues. The rule could be rewritten instead as:

```
Do not suggest performance optimizations for code in the /scripts directory - these are one-time utility scripts.
```

Good example:

```
### Good example: Language-specific syntax exclusion

Do not comment on missing "return" keywords in Kotlin single-expression functions. This is valid Kotlin syntax.
```

To set up exclusions:

1. Go to the [AI reviews settings page](https://app.graphite.com/ai-reviews)
2. Click on Workspace Settings
3. Create and save your exclusions

## Custom rules: Teaching Graphite Agent your standards

Custom rules allow you to define explicit guidelines for Graphite Agent to follow when reviewing your code. This is especially powerful for enforcing team-specific best practices.

With custom rules, you can:

* Define coding standards specific to your codebase
* Implement architectural guidelines for your team
* Enforce security or performance best practices
* Ensure consistent patterns across your repositories

<Frame caption="Custom rule interface">
  <img src="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=486fb3d8b71cb571c13843ee506a2cda" data-og-width="2346" width="2346" data-og-height="1584" height="1584" data-path="images/ai-reviewer-add-custom-rule-with-templates.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=280&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=d075d556af1aaf5f8c9106bc8ac854ca 280w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=560&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=91b9cfdceb5c39b6cf1ced7de0f17158 560w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=840&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=0a06f64d47bb0d71a1d70f55af3149c7 840w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=1100&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=582be71ba4a7bb46ed9e0c7ddaa20f42 1100w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=1650&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=afd8e66e884d0e0cba09f40e1c743cbd 1650w, https://mintcdn.com/graphite-58cc94ce/AlNXHu6AEKyFvgRD/images/ai-reviewer-add-custom-rule-with-templates.png?w=2500&fit=max&auto=format&n=AlNXHu6AEKyFvgRD&q=85&s=7e7057c9ce2e38a414455d96d1e1a8bf 2500w" />
</Frame>

There are two ways to configure custom rules: custom prompts and file-based rules. Below is our recommendation for when each option is most appropriate.

### Custom prompts (Recommended)

Custom prompts are rules written directly in the Graphite UI. They're the recommended approach for most teams.

**Why custom prompts work best:**

* **Focused**: Each rule addresses one specific concern
* **Fast to iterate**: Test and refine rules based on their effectiveness
* **Better performance**: No file processing overhead
* **Easy to manage**: All rules across all repos visible in a single interface

**Getting started:**

1. Use built-in templates for common scenarios:

   * Language-specific style guides (JavaScript, Python, Go, etc.)
   * Security best practices
   * Accessibility standards

2. **Start small**: Create focused rules that address specific concerns

   * Example: "JavaScript error handling patterns"
   * Example: "API response formatting standards"

3. **Quick start**: Copy relevant sections from your existing coding guidelines and refine them into focused rules

### File-based rules

File-based rules reference existing documentation in your repository using glob patterns. Use these sparingly when you have living documentation that changes frequently.

**When to use file-based rules:**

* Documentation maintained by other teams that changes regularly
* Shared architectural decision records across repositories
* Style guides that are actively updated

**How they work:**

1. Specify a glob pattern (e.g., `docs/coding-style.md`)
2. Graphite Agent reads the file content from your repository
3. Uses that content as context during code review

**Example patterns:**

```
docs/coding-standards.md    # Specific documentation file
CONTRIBUTING.md             # Contributing guidelines
docs/architecture/*.md      # Architecture documentation
```

**Limitations:**

* Large files are truncated for performance
* Too many files can reduce review quality
* Glob patterns are case-sensitive

### Best practices for writing custom rules

**Structure your rules clearly:**

* **Format**: Rule → Bad example → Good example → Reasoning
* **Focus**: One specific concern per rule
* **Examples**: Provide 2-3 clear, contrasting examples
* **Test**: Try your rule on recent PRs to verify it adds value

**What works best:**

* Language-specific conventions (naming, imports, error handling)
* Security guidelines (authentication, data validation)
* Framework-specific patterns (React hooks, API design)

**What to avoid:**

* Overly broad rules ("write good code")
* Subjective preferences without clear reasoning
* Complex architectural patterns that only sometimes apply

Bad examples:

```
### Bad example 1: Vague database rule

Rule: Don't make breaking changes to database fields. When dropping or adding fields could cause issues, flag them in review.
```

Why is this bad?

* Too vague. The rule needs to specify what types of field drops or additions would be considered breaking.
* Not actionable. The rule should be specific, like: "Never drop a required field directly. Always make it nullable first and stop writing to it so that it is no longer used by the entity."
* No examples provided.

```
### Bad example 2: Unclear CSS class naming rule

Always comment on color values like #FF0000 being used in stylesheets. Don't comment on utility classes like bg-red-500 or text-primary.
```

Why is this bad?

* More context is needed. The rule should specify which files or frameworks this applies to (CSS files, styled-components, etc.).
* This isn't phrased as a rule. The rule should be stated clearly as "Never use hex color values directly, always use design system tokens instead."
* This prompt mixes custom rules and exclusions. The latter sentence is not necessary.

Good examples:

````
### Good example 1: Security rule with clear structure

## Security Rules

### Rule: Never expose detailed error messages

**Rule:**
Never expose detailed error messages that reveal stack traces or internal system details. In production environments, always return generic error messages to protect the system while logging full details internally for debugging.

**Bad example:**
```js
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.stack });
});
```

**Good example:**
```js
app.use((err, req, res, next) => {
  res.status(500).json({ error: "Internal Server Error" });
});
```

**Reasoning:**
Revealing stack traces or internal error details can leak sensitive implementation information, making it easier for attackers to exploit vulnerabilities.
````

````
### Good example 2: Database rule with specific context

## Database Rules

### Rule: Use `text` instead of `varchar(n)` for new PostgreSQL columns

**Rule:**
When adding new string columns to TypeORM entities, always use `text` type instead of `varchar(n)` unless there's a specific business requirement for length constraints.

**Good example:**
```ts
@Column({ type: 'text' })
description: string;
```

**Bad example:**
```ts
@Column({ type: 'varchar', length: 255 })
description: string;
```

**Reasoning:**
PostgreSQL handles `text` and `varchar` identically in terms of performance, but `text` avoids arbitrary length limits that can cause issues as data grows.
````

For additional recommendations, see [Anthropic's suggestions for prompt engineering best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#be-explicit-with-your-instructions).

To set up custom rules:

1. Go to the [AI reviews settings page](https://app.graphite.com/ai-reviews?view=settings)
2. Scroll to the "Custom rules" section and click on "Create custom rule"
3. Choose a template or add a custom prompt for your new rule
4. Save your configuration

## Excluding files from AI review

For large repositories, you may want to exclude certain files from AI review analysis. This is useful for:

* Data files that don't need to be reviewed
* Generated code that is automatically created by tools
* Any files that would make a PR too big for Graphite Agent to analyze

You can exclude files by marking them as generated files in your repository's `.gitattributes` file:

```
# Exclude specific files
docs/data.txt linguist-generated=true

# Exclude file types
*.csv linguist-generated=true
*.pb.go linguist-generated=true

# Exclude entire directories
data/** linguist-generated=true
generated/** linguist-generated=true
```

Files marked as `linguist-generated` will be:

* Automatically collapsed in GitHub pull request views
* Excluded from AI review when determining if a PR is too large
* Skipped during the AI review process

For more information, see GitHub's documentation on [customizing how changed files appear on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/customizing-how-changed-files-appear-on-github).

## PR-level filtering

Advanced PR-level filtering provides granular control over where AI reviews run. You can configure AI reviews to run on specific pull requests based on defined criteria.

With PR-level filtering, you can control AI reviews based on:

* **PR author**: Run reviews only for specific team members or external contributors
* **File paths**: Analyze PRs only when certain files or directories are modified
* **PR labels**: Trigger reviews based on GitHub labels applied to pull requests
* **PR title and description**: Filter based on text content in PR titles or descriptions
* **Parent branch**: Run analysis based on target branch naming conventions

PR-level filtering provides flexibility to:

* **Control usage and costs**: Optimize AI review usage by focusing on the most important PRs
* **Focus analysis on critical PRs**: Ensure reviews target high-impact changes while skipping routine updates
* **Implement organization-specific review policies**: Align AI review behavior with your team's development workflows and governance requirements

Once saved, AI reviews will only run on new and updated pull requests that match the configured settings in enabled repositories. You can configure these settings through the AI reviews settings page, and organization admin permissions are required to modify them.


# Experimental comments
Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-review-experimental-comments

Learn about experimental AI review comments and how to provide feedback

## About experimental comments

### Why am I seeing this?

As a part of improving Graphite Agent, some comments that users receive are created by **experimental pipelines** that the team is testing.
By testing these experimental pipelines, we can learn what works well and what doesn't, which helps us build features that truly improve your development experience.

### We'd appreciate your feedback

Your input is incredibly valuable and helps us make Graphite Agent better for everyone. We want to know:

* What did you find helpful about this comment?
* What could be improved?
* Would you want to see more comments like this in the future?

Our team reviews each comment that receives feedback to improve Graphite Agent and deliver a better experience.

### How to leave feedback

Use the 👍 or 👎 reaction on the comment itself in your PR, in Graphite or in GitHub.

**If you downvote on Graphite**, a popup will appear asking for more details. Your specific feedback helps us understand what went wrong and how to improve future reviews.

Our team may reach out to you to ask for more information.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/hol-2nDiwKaLTxXr/images/ai-reviewer-feedback.png?fit=max&auto=format&n=hol-2nDiwKaLTxXr&q=85&s=a8d95b2541282b3f6feee01a05bba335" alt="Feedback popup for experimental comments" data-og-width="445" width="445" data-og-height="462" height="462" data-path="images/ai-reviewer-feedback.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/hol-2nDiwKaLTxXr/images/ai-reviewer-feedback.png?w=280&fit=max&auto=format&n=hol-2nDiwKaLTxXr&q=85&s=30d45140b16b5f7cbeb1593f059777d7 280w, https://mintcdn.com/graphite-58cc94ce/hol-2nDiwKaLTxXr/images/ai-reviewer-feedback.png?w=560&fit=max&auto=format&n=hol-2nDiwKaLTxXr&q=85&s=1a2146a0b01a510c8dc26c373a6acf69 560w, https://mintcdn.com/graphite-58cc94ce/hol-2nDiwKaLTxXr/images/ai-reviewer-feedback.png?w=840&fit=max&auto=format&n=hol-2nDiwKaLTxXr&q=85&s=6f3d90862c32febfa241c990edef2e1a 840w, https://mintcdn.com/graphite-58cc94ce/hol-2nDiwKaLTxXr/images/ai-reviewer-feedback.png?w=1100&fit=max&auto=format&n=hol-2nDiwKaLTxXr&q=85&s=88880d8929e3f02d14bb92256f6c6e9a 1100w, https://mintcdn.com/graphite-58cc94ce/hol-2nDiwKaLTxXr/images/ai-reviewer-feedback.png?w=1650&fit=max&auto=format&n=hol-2nDiwKaLTxXr&q=85&s=a3070cbd2fb87752c63ec4fb63033fb5 1650w, https://mintcdn.com/graphite-58cc94ce/hol-2nDiwKaLTxXr/images/ai-reviewer-feedback.png?w=2500&fit=max&auto=format&n=hol-2nDiwKaLTxXr&q=85&s=9c1462976e91c02af9c14a1f3e515976 2500w" />
</Frame>


# AI Reviews
Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-reviews

Catch bugs before they ship to production with AI code review

AI reviews powered by Graphite Agent help your team build better software by automatically reviewing pull requests and catching bugs before they ship.

## How AI reviews help your team

AI reviews analyze every pull request in your repositories, identifying potential issues and suggesting fixes instantly - no manual configuration required. AI reviews help your team:

* **Ship faster**: Reduce review cycles and speed up the merge process
* **Fix bugs early**: Catch logic issues, edge cases, and performance problems before they reach production
* **Improve code quality**: Get actionable feedback that makes your codebase more robust
* **Reduce incidents**: Prevent bugs that cause outages or customer-facing issues

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=b52980162334664fa01c861fc69c4d50" data-og-width="2560" width="2560" data-og-height="1504" height="1504" data-path="images/ai-reviews-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=280&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=66330e5654e545542cbe0c38ee00695d 280w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=560&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=b34880a3deca52d91236d17ec7a39741 560w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=840&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e047aeec7bdf05c291da84a7ffc2d19f 840w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=1100&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=8fb1ca6e3268cd075b9634b2752315c3 1100w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=1650&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=a89d4a3aa760b8a76fa462b2ece5923f 1650w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-3.png?w=2500&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=98c38cccfde9b04dbb1b92b4d3042825 2500w" />
</Frame>

## What makes AI reviews different

Unlike other code review tools, AI reviews:

* **Focuses on real bugs** - not just style issues or best practices
* **Understands context** - analyzes your entire codebase to provide relevant feedback
* **Provides actionable suggestions** - shows exactly how to fix issues, not just what's wrong
* **Learns from feedback** - improves based on how your team interacts with comments

Ready to see AI reviews in action? Get started in minutes:

<CardGroup cols={3}>
  <Card title="Setup & configuration" icon="settings" href="/ai-reviews-setup">
    Enable AI reviews and get immediate feedback on your PRs.
  </Card>

  <Card title="Review comments" icon="message-square-diff" href="/ai-review-comments">
    See the types of bugs Graphite Agent catches and how it communicates them.
  </Card>

  <Card title="Customization" icon="sliders-horizontal" href="/ai-review-customization">
    Tailor AI reviews to your team's specific needs and coding standards.
  </Card>
</CardGroup>

*AI reviews are designed with the security of your data in mind. You can find more details in our [AI security and privacy](/ai-privacy-and-security) page.*


# Setup & configuration
Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-reviews-setup

Get started with AI reviews in under 5 minutes

## Getting started with AI reviews

AI reviews can be enabled in just a few clicks, with no configuration required to start catching bugs in your pull requests.

### Enabling AI reviews

1. Navigate to the [AI code review settings page](https://app.graphite.com/ai-reviews)

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=c93f873df83987fa690cbd5cb1596185" data-og-width="2560" width="2560" data-og-height="1504" height="1504" data-path="images/ai-reviews-0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=280&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=32e47daee026863bc223dd7af8ebb2a8 280w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=560&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=c6f02f81ca7811bb671c817884125ff6 560w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=840&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=7296f326b5a8f789acdf27d92acd287e 840w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=1100&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e6ae203e53994de04ea9c9b5ed2fe659 1100w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=1650&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=3156ff930c22f48b3a12b57df07ff689 1650w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=2500&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=2e465d8e8d70d084028d9b344e24a65a 2500w" />
</Frame>

2. Click "Enable automatic reviews" to set up Graphite Agent to review PRs automatically

3. Select the repositories where you want AI reviews enabled
   * You can choose specific repositories or enable AI reviews across your entire organization
   * If you don't see the repositories you're looking for, make sure they're [synced with Graphite](https://app.graphite.com/settings/synced-repos)

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=621edc4550a8583f0270d3c7c1299403" data-og-width="2560" width="2560" data-og-height="1504" height="1504" data-path="images/ai-reviews-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=280&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e27e6ac0b5c379c4d32e72c76fc8616f 280w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=560&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e11f69fec61b6041b35789f35d6d8c0f 560w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=840&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=6ba302f98069c99128407f944da1b1be 840w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=1100&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=62266dd6b1aa3f42633cdad8748fe2db 1100w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=1650&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=4d564c8635511e3366ecfccef0681527 1650w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=2500&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=1de9e1d19efb3f35212f51dd75e4b30e 2500w" />
</Frame>

4. Click "Done" to save your settings. Graphite Agent will now automatically review all new pull requests in the selected repositories

### What happens next

Once enabled, Graphite Agent:

* Automatically analyzes new pull requests in the selected repositories
* Comments directly on pull requests when it finds potential issues
* Suggests fixes for the problems it identifies

Graphite Agent works behind the scenes, with no changes required to your existing PR workflow. Your team can continue using GitHub just as they do today, with Graphite Agent providing additional feedback alongside human reviewers.

For teams using continuous integration, Graphite Agent works alongside your test suite to catch issues that tests often miss, like logic bugs, edge cases, and security vulnerabilities.

## Enabling AI reviews on personal repositories

In order to enable AI reviews on your personal repositories, you must first install the Graphite GitHub App on your personal account.

1. Navigate to your [GitHub authentication settings page](https://app.graphite.com/settings)

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b4789c7b73c1c0ab577b728a1c79ab57" data-og-width="2840" width="2840" data-og-height="2160" height="2160" data-path="images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3d94cfef51da895fecc12274c147fbb9 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b01150fee43820fa027e45b8fe1e629e 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=317bf76986e066a284540b72c6ce6db1 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ada9f41ad3961dde58ea8393172a8e80 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=54f679ac0bd2c0848682bb9a1bd59e9d 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7949f9ad67e04aa2ff2eb734441917c8 2500w" />
</Frame>

2. If this is your first time authenticating Graphite using the GitHub App, select the "Install GitHub App" button; otherwise, select the "Add organization" button.

3. Install the Graphite GitHub App using the pop-up window that appears, selecting your personal account's login.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b3e957118043903a50ad26ffe51e0dfb" data-og-width="780" width="780" data-og-height="910" height="910" data-path="images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=6e16b8923bbebb2bd15ba61a0fb15c2a 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=25a39d4b4ffd042177b331e43e79b11e 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f3c28c80f8d673e28d4659319006c617 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1c3a8197b707cd63c8cc5ad283e4b33e 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b1c44e10dc81dfb913ced16048565d57 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=36340374f27e21e8bffad5064428493b 2500w" />
</Frame>

4. After returning to the GitHub authentication settings page, click the "Join team" button next to your personal account's login.

After completing these steps, you can enable AI reviews on your personal account following the instructions for [Getting started with AI reviews](/ai-reviews-setup#getting-started-with-ai-reviews).

<Info>
  You can only enable AI reviews on personal repositories that you own.
</Info>

## Advanced configuration

While AI reviews work great out of the box, you can customize them to better fit your team's workflow and standards. See our [Customization](/ai-review-customization) page for details on:

* Setting up exclusions to prevent Graphite Agent from commenting on certain types of issues
* Creating custom rules that match your team's coding guidelines
* Excluding files from AI review analysis


# Authenticate With GitHub
Source: https://graphite-58cc94ce.mintlify.dev/docs/authenticate-with-github-app

Graphite is built on top of GitHub's APIs, so you need to provide Graphite access to your GitHub resources to create, review, and merge PRs.

## GitHub authentication methods

Currently, GitHub is the only git provider that Graphite integrates with. When setting up an account with Graphite, you'll have two options to authenticate with GitHub:

* Option 1: Install [the Graphite App](https://github.com/apps/graphite-app) (a GitHub App) on your organization ***(recommended)***

* Option 2: Provide Graphite with a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

<Note>
  We no longer support OAuth as an authentication method. Users who previously authenticated with OAuth remain supported, but new signups must use GitHub App or PAT.
</Note>

## Option 1 - Install the Graphite GitHub App

When creating an account on Graphite, it's strongly recommended that you install or request installation of Graphite's GitHub App on your organization.

GitHub Apps are the officially [recommended way](https://docs.github.com/en/apps/publishing-apps-to-github-marketplace/github-marketplace-overview/about-github-marketplace-for-apps) to integrate with GitHub. Some benefits for installing [Graphite’s GitHub App](https://github.com/marketplace/graphite-dev) on your organization:

* Access to GitHub webhooks, which provides Graphite with push-based updates for information like CI status, mergeability, and real-time push events within seconds.

* Access to the Graphite Merge Queue. The Merge Queue is only available if our GitHub App is installed on the organization.

* Avoid hitting secondary rate limits with the GitHub API. This means fewer API requests to keep your data up-to-date, leading to fewer API errors and lower latency.

* Provides the most security for your organization, giving users more control over which repositories the app can access through fine-grained permissions and short-lived tokens.

### Install the Graphite App on an organization

<Note>
  You can only install a Graphite App on an organization if you're an organization owner. If you're not an owner, you should [request to install the Graphite App](/authenticate-with-github-app#request-to-install-the-graphite-app-on-an-organization) instead.
</Note>

If you're an organization owner, you can install the Graphite App on your chosen organization by following the Graphite onboarding flow, or directly from the [GitHub marketplace.](https://github.com/apps/graphite-app)

See GitHub's instructions to [install an App from the GitHub marketplace](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations).

### Request to install the Graphite App on an organization

If you're not an organization owner, you can [request approval for the app to be installed](https://docs.github.com/en/apps/using-github-apps/requesting-a-github-app-from-your-organization-owner). Once you've done so, you should reach out to an organization owner to have your request approved. You can find a list of organization roles and members using this link: `https://github.com/orgs/{org-name}/people`.

### Authorize the GitHub App with your personal account

After the Graphite App has been installed on your organization or if you're signing up for Graphite with an organization that has the app installed, you'll also need to [give the Graphite App approval](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps) to retrieve information about your GitHub account and make changes on your behalf.

The screen to do so will look like this:

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4e22e8aea1a15e73c7e4457b1920a343" data-og-width="1350" width="1350" data-og-height="1246" height="1246" data-path="images/d7298895-1700536958-frame-10123321.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a9f5dcbde123335bb996ed1d77b9ba62 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4b44bbfe98e2b2ef957bd487368d6527 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=041c0dddd9e0ecb4ef2ddc42a0d34ef1 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=db7b50dfc2aa71ee049580a701a9a6db 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ebee02ca922b1fcee9eaaeafba17c4ae 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a5ff45cf54003ebd1dd5dc623349c4bd 2500w" />
</Frame>

<Note>If your GitHub Organization uses [SAML SSO authentication](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/about-authentication-with-single-sign-on), ensure that your GitHub user account also has an active SAML session with the organization on GitHub while authorizing the GitHub app.</Note>

## Option 2 - Provide Graphite with a Personal Access Token

If you're unable to authenticate/install the Graphite App for any reason, you can always use Graphite with a Personal Access Token. At any point in the Graphite onboarding flow, you can click **"Authenticate with a personal access token"**, and the screen will look like this:

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=9df32a82a78c5b6005f599ffc9796ef0" data-og-width="1364" width="1364" data-og-height="954" height="954" data-path="images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=38e15fe6036be2c25096a86dc5bb1ddb 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=84f76751d0e1208c32e0c836d74a0192 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=9e872e0a875f66e958c5738e1c49ad41 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=6d775ff26d771405d276614878ab8559 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8b706aa87f42088d7fb307a9967b4bb7 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/804e52b5-1700444982-screenshot-2023-11-19-at-7-49-31-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c5aa3379e3bb13c16082587d484d6f69 2500w" />
</Frame>

From here, generate a token on GitHub with the requires scopes pre-selected and paste it into the field to continue account creation. Learn more about the scopes Graphite requires in our [privacy and security docs](/privacy-and-security).

<Warning>
  **Warning**

  GitHub Personal Access Tokens are designed to give command line tools limited access to work with your account. While they provide the minimum clearance to use the Graphite CLI and app, they give the user the added responsibility of granting the token the correct permissions and have a limited lifespan before they expire. You may have a slower/limited experience with Graphite if you proceed with a PAT.
</Warning>

## Manage GitHub authentication

To make adjustments to your GitHub authentication and the resources which Graphite has access to, go to your [GitHub authentication settings](https://app.graphite.com/settings?org=withgraphite) in Graphite:

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f306b329-1700537052-frame-10123322.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1ca4cad1d9a342e410403f892b30267f" data-og-width="728" width="728" data-og-height="696" height="696" data-path="images/f306b329-1700537052-frame-10123322.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f306b329-1700537052-frame-10123322.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=de47f2f7a66909a8e53f7a5b5dbcd65f 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f306b329-1700537052-frame-10123322.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=db3ec5e8c55a2af808b137a3518e547c 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f306b329-1700537052-frame-10123322.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=aeadc400cb5b3c2ddef5f6334ef12d7e 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f306b329-1700537052-frame-10123322.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=947f8d678f2f1cfc9f300439fa28c37d 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f306b329-1700537052-frame-10123322.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a790822c159c2bfb23f92475181fc1f1 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f306b329-1700537052-frame-10123322.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=39d08a847692d2e901e38b4aef33ef4c 2500w" />
</Frame>


# Automations
Source: https://graphite-58cc94ce.mintlify.dev/docs/automations

Learn how to automate tedious code review tasks like assigning reviewers, adding labels, and more with automations.

Graphite supports automating common actions when PR attributes meet your specified criteria by creating automation rules.

With these rules, automatically take actions such as adding reviewers, labels, or comments when a PR is opened by a specific author, containing files in specific directories, or a variety of other powerful filters.

<Frame>
  <video controls width="100%" poster="/images/1705419433-automations_cover.jpg">
    <source src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1705419433-automations_cover.mp4?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=de39f14c584fe9f1c454de0a32e0e7a5" type="video/mp4" data-path="images/1705419433-automations_cover.mp4" />

    Your browser does not support the video tag.
  </video>
</Frame>

## Automation rules

Automation rules have two aspects: a filter trigger and an action.

### Filter trigger

To specify the filtering trigger for PRs:

* You can use any of the filters powering Graphite's PR inbox today

* Additionally, you can specify a glob pattern for filenames. With this, you can create rules for PRs containing common suffixes (e.g. `**/*.ts` files), or that are contained in specified sub-directories (e.g. `**/myteam/**`), among other patterns.

### Actions

When a PR matches your condition, you can configure one or more of the following actions:

* Add reviewers to the PR. This supports both individuals and GitHub teams.

* Add assignees to the PR. This supports making the PR author the assignee.

* Add labels to the PR.

* Leave a comment on the PR. For example, you can leave a reminder for PRs opened containing changes to a particularly sensitive area of the code.

* Notify someone through Slack. For example, set a notification for all frontend changes for instances when you want to know about a change, but don’t necessarily want to be added as the reviewer.

* Post a GIF on the PR. For example, post a random "approved!" GIF from GIPHY each time a PR is fully approved.

## Manage rules

Navigate to *Automations* from the sidebar in the Graphite web app.

### **Create rules**

* Click **Create rule**.

* Specify the repository for the rule. Note that this must be one of your synced repositories (see [configuring default repositories](/use-pr-inbox#default-repositories)).

* Configure the conditions you want to match PRs on, and the actions to automatically take on those matched PRs.

To confirm your conditions are configured correctly, you can preview past PRs that match your rules before activating the rule.

When you're done, click **Activate rule**. This automatically applies the rule to open PRs that match your triggers, as well as all matching PRs going forward, until the rule is deactivated.

<Info>
  Rules match once per PR. If a PR doesn't initially match, it's re-evaluated on each update until there is a match. After it's matched once, it won't trigger again on that PR, avoiding surprises like leaving the same comment repeatedly. Automations evaluate on published PRs only, and do not evaluate on PRs that are closed or in draft mode.
</Info>

### View rules

To view a rule, navigate to *Automations* in the Graphite web app. There you'll see a list of all active rules in your GitHub org for repositories that you have access to. If you don't have access to a given repository, you won't see rules configured for it.

### Edit rules

To edit a rule, navigate to \*Automations \*in the Graphite web app.

Click the pencil icon to edit the rule. You can edit any rule for repositories you have access to, making it easy for teammates to update shared team rules.

<Info>
  Because PR actions trigger at most once, if a given PR has previously already matched a rule that you're editing, note that it won't re-evaluate again after you edit your rule. This means that if you change your actions, those new actions won't apply to previously matched PRs.
</Info>

## Rule triggering

When a rule triggers on a PR, Graphite automatically applies the triggers. Graphite will also leave a comment on the PR on GitHub to let the author know the rule matched, including a link to the rule in Graphite so it's easy to see why that rule matched the PR.


# Basic Tutorials
Source: https://graphite-58cc94ce.mintlify.dev/docs/basic-tutorials

Understand the core CLI commands.

<CardGroup cols={3}>
  <Card href="/create-a-pull-request" icon="git-pull-request" title="Create a pull request">
    Start the transition from git to gt.
  </Card>

  <Card href="/create-stack" icon="layers" title="Create a stack">
    Build new branches on top of existing ones.
  </Card>

  <Card href="/sync-with-a-remote-repo" icon="refresh-ccw" title="Sync your changes">
    Keep your work up-to-date with the latest changes on remote.
  </Card>
</CardGroup>

## Watch a video tutorial

Follow along with our video tutorials! In two-minute pieces, we break down each command that you'll need to know to get started with the Graphite CLI.

<Frame>
  <iframe width="750" height="360" src="https://www.youtube.com/embed/WgTe0B19slY?si=JhftN6K_coXzHwwy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>


# Best Practices For Reviewing Stacked PRs
Source: https://graphite-58cc94ce.mintlify.dev/docs/best-practices-for-reviewing-stacks

Learn best practices to keep in mind when reviewing PRs in a stack.

Introducing [stacked pull requests](https://www.stacking.dev/) to your engineering org can seem like a big change to your code review workflow, but it doesn’t need to be painful. While many code changes will still be small enough for a single, un-stacked PR, sharing a few best practices with your team around reviewing PRs in a stack can help you seamlessly introduce stacking into your engineering workflow and get the full benefits of doing so. With these simple guidelines, you’ll provide relevant, timely feedback to the stack’s author and keep changes flowing smoothly.

### Best practices for reviewing stacked PRs

Here’s how we recommend you & your team to review stacked pull requests with Graphite:

1. **Review a PR in a stack as though it was an independent change:** If the PR doesn’t make sense without a lot of additional context from the stack, request that the author split up the stack differently to make each change more atomic.

2. **Review stacked PRs as soon as you’re tagged as a reviewer:** Don’t wait for downstack changes to be approved and merged, as this serializes reviews and greatly reduces the time savings of stacking.

3. **Start from the bottom:** If you’re tagged as a reviewer on multiple PRs in the stack, review from the bottom of the stack (closest to main) upwards.

4. **Check for upstack changes as you review:** If code in the stacked PR you’re reviewing changes again upstack (indicated by an orange bar on the right in Graphite), click to view the upstack change. You can then navigate back to the PR you were reviewing using the stack visualization (or navigate down the stack with the keyboard shortcut `⌘` + `Shift` + `↓`) and finish your review with the context of the upstack change.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=43a5882098f40fee83d55257c149dd67" data-og-width="1082" width="1082" data-og-height="502" height="502" data-path="images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1c9a85dee6ad26270f6fc3f51d62bfca 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5622de896f1acbe9c56f6973dc210530 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3dc76523a67099f41601ec2ccb626f91 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=228316a0369e6e739d95376d0a0177d6 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=6ce455ff4f9452c14915cd5fc9241be5 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e31d13cd-1715821959-screenshot-2024-05-15-at-5-47-05-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8a577de21f8b1be6b5e54edd0e1e2575 2500w" />
</Frame>

### Make your stacked PRs easy to review

Reviewing is only part of the stacking workflow - you should also make sure to follow best practices when creating stacks to make them as easy as possible to understand and review:

1. **Separate stacked PRs logically:** Each PR should be easy to understand and review independently - see [best practices frameworks for splitting up large changes into stacks](https://graphite.com/blog/five-methods-for-stacking) for ideas on how to do this.

2. **Submit PRs as soon as they’re ready to review:** Even if you plan to stack additional changes on top, you should submit your changes for review to ensure you get feedback as quickly as possible.

3. **If you’re actively working on a PR, mark it as a draft:** Open PRs in a stack should be considered ready to review, so if you’re still working on the PR or need to go back and make changes to address review feedback you should mark the PR as a draft until it’s ready to be reviewed again.

4. **Choose the best reviewers for each PR in the stack:** Choose who is most relevant for each individual change (or set up automations to do this for you) - you most likely don’t want the same set of reviewers to every PR.

5. **Use “merge when ready” to put stack merges on autopilot:** Unless a change needs manual assistance to land, default to turning on “merge when ready” to ensure your stacked PRs merge quickly once approved.

### Set up your org for successful stacking

Lastly, make sure your engineering organization is set up to start stacking successfully with the following best practices:

1. **Update your branch protection rules in GitHub:** Turn off “dismiss stale approvals” & “require approval of the most recent reviewable push” [settings in GitHub](/github-configuration-guidelines#required-settings) to ensure stacks merge smoothly.

2. **Assign reviewers automatically with automations:** [Set up automations](https://app.graphite.com/automations) in Graphite to automatically assign the most relevant reviewers for each PR based on file types & paths. Automations is a more powerful and granular system than `CODEOWNERS` for assigning reviewers, built for teams building in large monorepos.

3. **Warn authors about large PRs:** [Set up an automation](https://app.graphite.com/automations) to comment on PRs larger than 250 lines of code or 25 files changed to encourage authors to break up larger changes into stacks.

By following these simple best practices for reviewers, authors, and your organization, you’ll be set up for success when introducing stacking to your workflow, and ensure that you’re maximizing the time savings stacked PRs can provide in the review cycle.


# Use Beta CLI Releases
Source: https://graphite-58cc94ce.mintlify.dev/docs/beta-cli

Join the Graphite CLI beta test group for early access to the newest features.

Get early access to the newest CLI features!

## homebrew

(As with the stable CLI, we recommend `brew`).

```bash Terminal theme={null}
brew install withgraphite/tap/graphite-beta
```

## npm

```bash Terminal theme={null}
npm install -g @withgraphite/graphite-cli@beta
```

## Slack Channel

New versions will be announced in the #cli-beta channel in our [community Slack.](https://graphite.com/join-slack)

<Warning>
  The beta CLI may be unstable.
  If you encounter any issues please report them in the `#cli-beta` Slack channel.
  See the [instructions](/install-the-cli) for how to install the latest stable version.
</Warning>

<Note>
  You do not need to uninstall your current CLI version to use the beta version.
</Note>


# Billing & plans
Source: https://graphite-58cc94ce.mintlify.dev/docs/billing-plans

Learn about the Graphite plans for teams.

Graphite offers three paid plans — **Starter**, **Team**, and **Enterprise** — as well as a free **Hobby** plan for personal projects.

<table
  style={{
  width: '100%',
  borderCollapse: 'collapse',
  fontFamily: 'system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif'
}}
>
  <tbody>
    <tr style={{ background: 'color-mix(in srgb, currentColor 10%, transparent)' }}>
      <td style={{ padding: '16px 12px', verticalAlign: 'top' }} />

      <td style={{ padding: '16px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>
        <div style={{ fontWeight: 700 }}>Starter</div>
        <div style={{ fontStyle: 'italic' }}>\$20/seat/month</div>
        <div style={{ opacity: 0.85 }}>(billed annually)</div>
      </td>

      <td style={{ padding: '16px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>
        <div style={{ fontWeight: 600 }}>Team</div>
        <div style={{ fontStyle: 'italic' }}>\$40/seat/month</div>
        <div style={{ opacity: 0.85 }}>(billed annually)</div>
      </td>

      <td style={{ padding: '16px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>
        <div style={{ fontWeight: 700 }}>Enterprise</div>
        <div style={{ fontStyle: 'italic' }}>Custom, talk to Sales</div>
      </td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}><strong>Best for</strong></td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>
        For small teams looking to ship higher quality code, faster.
      </td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>
        For growing teams looking to streamline their reviews and improve code quality with unlimited AI.
      </td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>
        For orgs operating at scale with advanced control and security needs.
      </td>
    </tr>

    <tr style={{ background: 'color-mix(in srgb, currentColor 6%, transparent)' }}>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}><strong>Pull requests</strong></td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>GitHub sync</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>All repos</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>All repos</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>All repos</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Inbox / Notifications</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Integrations</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Basic (Slack)</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Advanced</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Advanced</td>
    </tr>

    <tr style={{ background: 'color-mix(in srgb, currentColor 6%, transparent)' }}>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}><strong>Stacking</strong></td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>CLI / VSCode / MCP</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Stack merge</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr style={{ background: 'color-mix(in srgb, currentColor 6%, transparent)' }}>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}><strong>Graphite Agent</strong></td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>AI-generated PR titles + descriptions</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Chat</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Limited</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Unlimited</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Unlimited</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>PR reviews</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Limited</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Unlimited</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Unlimited</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Review customization (automation, filters, rules)</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Suggested fixes + CI summaries</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr style={{ background: 'color-mix(in srgb, currentColor 6%, transparent)' }}>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}><strong>Team features</strong></td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Insights</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>CI optimizer</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Automations</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Merge queue</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Basic</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>Advanced</td>
    </tr>

    <tr style={{ background: 'color-mix(in srgb, currentColor 6%, transparent)' }}>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}><strong>Admin</strong></td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Code indexing controls</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>AI privacy controls</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Custom analytics</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>ACLs</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>SAML/SSO</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Audit log (SIEM)</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>GHES</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Premium support / SLAs</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Custom MSA</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Custom payment</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>

    <tr>
      <td style={{ padding: '10px 12px', verticalAlign: 'top' }}>Private uploads</td>

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }} />

      <td style={{ padding: '10px 12px', verticalAlign: 'top', borderLeft: '1px solid color-mix(in srgb, currentColor 18%, transparent)' }}>✓</td>
    </tr>
  </tbody>
</table>

### **Team plan trial**

During your 30-day trial period, you can invite as many contributors as you'd like to your Graphite workspace with the **Team** plan features. For best practices on trialing Graphite with your team, [see here](https://graphite.com/docs/onboarding-your-team).

You can choose a plan by visiting `Select a plan` in [billing](https://app.graphite.com/settings/billing) settings.

### **How billing works**

Workspaces on a monthly subscription are invoiced once a month.

Workspaces on an annual subscription are invoiced once a year, with the potential for additional invoices on a monthly basis if users join the Graphite team.

Changes to the number of seats on a team are reflected on the following month's invoice. If a new user joins your team, their seat will be added to your next invoice, with the charge prorated to reflect the remaining days in the billing cycle.


# Command Cheatsheet
Source: https://graphite-58cc94ce.mintlify.dev/docs/cheatsheet



While you can find a full list of `gt` commands in the [command reference](/command-reference), there are a handful of common commands and combinations to remember.

This list is grouped by primary function.

## Basic workflow commands

These commands are constantly in use when creating and pushing changes to a repository with Graphite.

| Command                                               | Alias                        | Description                                                                                                                            |
| ----------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `gt log short`                                        | `gt ls`                      | List Graphite-tracked stacks and branches in your repository in a minimized format                                                     |
| `gt create --all --message <COMMIT_MESSAGE>`          | `gt c -am <COMMIT_MESSAGE>`  | Create changes, stage the changes, create a new branch and commit the changes to the new branch all at once                            |
| `gt submit --stack`                                   | `gt ss`                      | Submit your changes across all PRs on a stack                                                                                          |
| `gt submit --stack --update-only`                     | `gt ss -u`                   | Update all PRs for branches in your stack that already have PRs, but do not create new ones                                            |
| `gt modify`                                           | `gt m -a`                    | Update an existing branch with all new changes by amending the existing commit on that branch                                          |
| `gt modify --all --commit --message <COMMIT_MESSAGE>` | `gt m -cam <COMMIT_MESSAGE>` | Update an existing branch with all new changes by creating an entirely new commit on that branch                                       |
| `gt undo`                                             | `gt undo`                    | Undo the most recent Graphite mutations                                                                                                |
| `gt sync --force`                                     | `gt sync -f`                 | Pull your trunk branch, automatically clean up any branches corresponding to merged PRs, and restack any branches that do not conflict |

## Collaborate on a stack

Commands to view teammates' code and communicate changes.

| Command                | Alias   | Description                                                                                                                                        |
| ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gt get <BRANCH_NAME>` |         | Get a stack locally that's been created or manipulated by someone else. Often followed up with \`gt delete\` to delete irrelevant branches locally |
| `gt checkout`          | `gt co` | Often used when to check out a singular branch for collaboration OR personal use                                                                   |

## Stack navigation/manipulation commands

Commands to move up and down the stack, and to restack branches (if necessary).

| Command             | Alias        | Description                                                                                                                                                                        |
| ------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gt up, gt down`    | `gt u, gt d` | Quickly move up and down a stack of branches. By default, it takes a step argument of 1, but can add a step value (for example, \`gt up 2\`) to skip a certain number of branches. |
| `gt top, gt bottom` | `gt t, gt b` | Quickly move all the way down (b) or all the way up (t) a stack                                                                                                                    |


# Use CLI Binaries
Source: https://graphite-58cc94ce.mintlify.dev/docs/cli-binaries



We publish binaries of our CLI [here](https://github.com/withgraphite/homebrew-tap/releases). Here's an example a script you might use to download the binaries on a VM. Note that we are using `gt-linux` here — there are other OS/arch combinations available on that page.

```bash Terminal theme={null}
version="$(curl https://registry.npmjs.org/@withgraphite/graphite-cli/stable | jq -r .version)"
url="https://github.com/withgraphite/homebrew-tap/releases/download/v$version/gt-linux"
curl -L "$url" -o /path/to/gt
chmod +x /path/to/gt
```

You can replace `/path/to/gt` with your preferred install location (e.g., `/usr/local/bin/gt`).


# CLI Changelog
Source: https://graphite-58cc94ce.mintlify.dev/docs/cli-changelog

See the history of changes for the Graphite CLI.

### Current versions:

**Stable: 1.7.8**      **Beta: 1.7.8**      **Alpha: 1.7.9**

<Update label="1.7.9" description="2025-11-14" tags={["feature","bug-fix"]}>
  * Added ability to set and manage a default profile through the interactive config menu.
  * Show unstaged changes during `gt create`.
  * Added a tip explaining the difference between `gt checkout` (unfrozen) and `gt get` (frozen) when fetching new branches.
  * Fixed error with missing refs on remote.
  * Made `--edit-title` and `--edit-description` imply `--cli` automatically.
  * Ensured `--cli` is auto-enabled only when PR title/description editing is actually enabled.
  * Added clarification to `gt delete` explaining that deleting branches for open PRs is a local-only operation; PRs must be manually closed in GitHub.
</Update>

<Update label="1.7.8" description="2025-11-12" tags={["feature", "performance"]}>
  * Added a feature to automatically check out branches authored by the current user as unfrozen when using `gt get`.
  * Optimized performance when gathering rebase metadata.
</Update>

<Update label="1.7.7" description="2025-10-25" tags={["bug-fix", "feature"]}>
  * Added `--to <target_branch>` flag to `gt up` for targeted branch navigation within large stacks.
  * Updated CLI, menu bar app, and VS Code extensions to request `app.graphite.com` instead of `app.graphite.dev`.
  * Trim whitespace from branch names in `gt rename` to prevent command failures.
  * Changed debug log file extension from `.log` to `.log.jsonl` for to match updated format.
</Update>

<Update label="1.7.6" description="2025-10-31" tags={["feature", "bug-fix"]}>
  * Added a feature to display warnings from PR submissions directly in the CLI to provide additional guidance to users.
  * Added retries on intermittent server errors.
  * Updated `--edit` to imply `--cli` in `gt submit` to ensure users can edit PR titles and descriptions directly in the CLI.
  * Fixed an issue where checking out the current branch after a rebase would create incorrect previous-branch entries in the reflog.
  * Fixed inconsistencies in upgrade behavior due to different packaging systems.
  * Fixed messaging to show "Updating PRs..." instead of "Creating/updating PRs..." when the update-only flag is used.
  * Fixed an issue where editing a PR description wouldn't show the existing content by fetching the PR body from the server.
  * Fixed an issue where `gt-fetch-head` refs could cause conflicts when creating new refs by deleting them when deleting a branch.
  * Fixed terminal alignment issues by replacing the pencil emoji (✏️) with a memo emoji (📝).
  * Improved error messages when a branch is updated outside of Graphite and `gt submit` fails.
  * Improved error reporting for Graphite API failures.
</Update>

<Update label="1.7.5" description="2025-10-25" tags={["bug-fix", "performance"]}>
  * Fixed an issue where `gt submit` would incorrectly warn about out-of-date trunk when trunk was up-to-date.
  * Fixed a bug where `gt submit` would fail with a force-with-lease error with custom fetch refspecs (or shallow clones).
  * Added automatic re-tries in some cases to improve `gt submit` reliability.
</Update>

<Update label="1.7.4" description="2025-10-06" tags={["feature", "bug-fix", "performance"]}>
  * Added gt upgrade command to update the CLI.
  * Introduced automatic background updates (configurable via user settings).
  * Added a feature to automatically fast-forward the trunk to the upstream merge base when it's out of sync, improving UX during sync operations.
  * Added a feature that prevents submitting changes after a branch has been merged or added to a merge queue.
  * Merged branches are now shown as merged in status and are uneditable to prevent accidental edits.
  * Performance improvements to gt log --short and gt checkout
  * Improved messaging to help users resolve "BlockedWhileMerging" errors by suggesting next steps in the CLI.
  * Fixed messaging in gt demo stack output to use "upstack" instead of "downstack" for descendant branches.
  * Fixed a critical logging regression that caused loss of debug logs.
  * Fixed an issue where the CLI wouldn't update the trunk when fetching if a branch hadn't yet been submitted.
</Update>

<Update label="1.7.2" description="2025-10-06" tags={["feature", "bug-fix", "performance"]}>
  * Added a feature to block submits and modifications to merging branches.
  * Added various performance optimizations on sync/get commands.
  * Fixed issue where syncing or fetching a frozen branch would unfreeze it.
</Update>

<Update label="1.7.1" description="2025-09-26" tags={["feature", "bug-fix"]}>
  * Added controls to show/hide inline tips.
  * Added `--reset-author` flag to `gt modify` for resetting commit authorship.
  * Added the ability to `gt get` PRs opened outside of Graphite.
  * Added `--upstack` and `--downstack` options to `gt delete`
  * Fixed bug where progress indicators would sometimes interfere with prompts for ssh key passphrases.
  * Fixed autocomplete output formatting for better terminal compatibility.
</Update>

<Update label="1.7.0" description="2025-09-01" tags={["feature", "bug-fix", "improvement", "performance"]}>
  * Added new `gt freeze` and `gt unfreeze` commands. Freezing a branch prevents modifications to that branch.
  * New branches from `gt get` will be frozen by default.
  * Added warnings for newly empty branches after restack operations.
  * Added a cap to debug log size.
  * Improved `gt feedback` experience and reliability.
  * Fixed issue where `gt undo` could remove unstaged or untracked changes.
  * Fixed bug where `gt undo` sometimes failed after `gt continue`.
  * Fixed issue where org prefixes were duplicated for team reviewers in PRs.
  * Fixed branch sync to correctly detect trunk status when upstream is missing.
  * Fixed issue where `gt sync` would hang when branches were too far behind trunk.
  * Automatically set `--no-interactive` mode when stdin/stdout are not TTYs.
</Update>

<Update label="1.6.8" description="2025-08-05" tags={["bug-fix"]}>
  * Added warnings when trunk is out of date during `gt submit`.
  * Fixed an issue where `gt sync` and `gt get` could result in slow operations.
  * Fixed an issue where `gt feedback` incorrectly reported a failure.
  * Fixed an issue where `gt submit` incorrectly required the `--force` flag.
  * Fixed an issue where `gt log` with `-n 0` would report the incorrect branch.
  * Fixed an issue where `gt revert` would fail to perform any action.
  * Fixed an issue where git hooks configured absolute paths would not be found.
</Update>

<Update label="1.6.7" description="2025-07-09" tags={["bug-fix"]}>
  * Fixed an issue where `gt submit` would incorrectly report a branch as having a "New parent".
  * `gt submit --branch` now validates that a branch name is provided when the flag is used.
  * Fixed an issue where `gt absorb` would fail with an error message "Shas does not match current stack".
  * Fixed an issue where rebasing empty branch could cause incorrect metadata.
  * Fixed an issue where `gt track` would not recover a diverged branch if the branch was already tracked.
  * [GT MCP](/gt-mcp) beta released.
</Update>

<Update label="1.6.6" description="2025-06-11" tags={["bug-fix"]}>
  * Add an option to cancel the operation when `gt get` or `gt sync` encounter merge conflicts.
  * Fixed an issue where `gt submit` would incorrectly warn about missing remote changes.
</Update>

<Update label="1.6.5" description="2025-06-04" tags={["bug-fix"]}>
  * Added logging of processes holding index.lock when Git commands fail due to lock contention.
  * Extended debug log expiry from 1 to 7 days for better access to historical logs.
  * Added validation for unexpected arguments in the `gt checkout` command to avoid accidental invocations.
  * Fixed an issue where some vscode extension activity could cause excessive log file usage.
</Update>

<Update label="1.6.4" description="2025-05-19" tags={["bug-fix", "performance"]}>
  * Fixed a bug where `gt submit` and `gt sync` could incorrectly report a new remote version.
  * Fixed a bug where `gt submit` may try to push the same branch twice.
  * Fixed a bug where help text would be displayed in a single column when piped to another command.
  * Fixed an issue where polling in the vscode extension could cause large amounts of log file usage.
</Update>

<Update label="1.6.3" description="2025-05-09" tags={["bug-fix", "performance"]}>
  * Fixed a bug in `gt submit` and `gt sync` that caused performance degradation and crashes when pull requests were modified outside of Graphite.
</Update>

<Update label="1.6.2" description="2025-05-02" tags={["bug-fix", "performance"]}>
  * `gt track` shows the exact number of commits that will go into the new branch, making it easier to spot oversized stacks.
  * Updated git fetch commands to no longer fetch tags, reducing network usage and speeding up operations.
  * Fixed a bug in `gt pr` where branch names were interpreted as a PR number if they started with a digit.
  * Fixed a bug in `gt submit` where PR descriptions were being generated larger than the GitHub PR description limit.
  * Fixed a bug in `gt submit` where PR titles were being generated larger than the GitHub PR title limit.
  * Fixed a bug in `gt submit` where pushing all the branches in a stack could partially fail leading to inconsistent diffs in some PRs.
  * Fixed a bug in `gt submit` where temporary branches were not being cleaned up correctly.
  * Fixed a bug in `gt create` where the branch name was incorrectly added to the commit message.
  * Fixed a bug where in certain cases, trunk commits could be included in a tracked branch, resulting in many Graphite operations hanging or failing.
  * Fixed a bug where certain cases of syncing a branch submitted outside of Graphite would crash the CLI.
  * Added better protections against running too many `git` subprocesses.
</Update>

<Update label="1.6.1" description="2025-03-21" tags={["bug-fix", "performance"]}>
  * Fixed a bug where in certain cases, trunk commits could be included in a tracked branch, resulting in many Graphite operations hanging or failing.
  * Fixed a bug where certain cases of syncing a branch submitted outside of Graphite would crash the CLI.
  * Added better protections against running too many `git` subprocesses.
</Update>

<Update label="1.6.0" description="2025-03-07" tags={["feature", "bug-fix", "improvement"]}>
  * Added support for multiple `-m` flags in `gt create`, `gt modify`, and `gt squash`.
  * Provided additional context when commands fail due to Graphite maintenance and incidents.
  * Use commit message for branch name if there are no staged changes.
  * Updated output colors to avoid difficult to read output.
  * Fixed a bug where `gt feedback` could fail due to large log files.
  * Fixed a bug where the remote repository could be marked as ''.
  * Fixed a bug where a large number of commits can cause "Invalid string length" exceptions.
  * Fixed a bug where whitespace in the repository path is not handled correctly when worktrees are used.
  * Dropped official support for Node 18 in anticipation of its end-of-life date on 2024-04-30.
  * Removed `gt interactive`
</Update>

<Update label="1.5.3" description="2025-01-21" tags={["improvement", "bug-fix"]}>
  * Introduced a progress bar for `git fetch` and `git push` operations.
  * Fixed an issue where feature flags could be inadvertently disabled.
  * Adjusted some command output formatting for consistency.
</Update>

<Update label="1.5.2" description="2024-12-23" tags={["bug-fix", "improvement"]}>
  * Cleanup `graphite-base` branches if a submit fails to push to remote
  * Fixed a bug where `graphite-base` branches were incorrectly introduced in trailing trunk multi-trunk configurations
  * Fixed a bug where `gt submit` could lead to incorrect diffs upstack if submit was not run on the full stack
  * Fixed a bug where `gt rename` did not use configured branch prefixes
  * Fixed a bug where `gt` commands could fail with `EAGAIN` errors
  * Fixed a bug where `gt delete` could fail when run on untracked branches
</Update>

<Update label="1.5.1" description="2024-12-12" tags={["bug-fix", "improvement"]}>
  * Fixed a bug where `gt submit` on a stack would lead to temporary incorrect diffs on the upstack remote PRs
  * Fixed a bug where `gt sync` failed with `"RangeError: Invalid string length"`
  * Updated `gt rename` to fail if the user aborts the command
  * Updated `gt squash` to fail if the squash command does nothing
  * Updated all output to properly respect the `--no-interactive` flag (e.g. `gt log`, `gt info`…)
</Update>

<Update label="1.5.0" description="2024-12-04" tags={["feature", "bug-fix"]}>
  * Introduced `gt abort`, which aborts the current rebase operation and restores the repository state to before the original command that introduced the conflict
  * Introduced `gt undo`, which undoes the most recent Graphite mutation, restoring the repository to its state before the mutation was applied
  * Fixed a bug where submitting a moved branch could temporarily result in incorrect diffs on remote
  * Updated `gt create` to prompt for a branch name for empty branches if one was not provided
</Update>

<Update label="1.4.11" description="2024-11-22" tags={["improvement"]}>
  * Internal improvements to config files
  * Add linux arm64 build to releases
</Update>

<Update label="1.4.8" description="2024-09-26" tags={["improvement"]}>
  * Added additional debugging information for pr info updates
</Update>

<Update label="1.4.7" description="2024-09-26" tags={["bug-fix", "improvement"]}>
  * Fixed a bug in `gt demo` that would corrupt the repo's name and owner
  * Updated sending non-info cli output to stderr instead of sending everything to stdout
</Update>

<Update label="1.4.6" description="2024-09-26" tags={["bug-fix", "improvement"]}>
  * Fixed a bug where `gt sync` would not update trunk if there were no previously submitted branches
  * Updated `gt submit --branch` to work while checked out untracked branches
  * Updated support for git pre-push hooks on Windows machines
</Update>

<Update label="1.4.5" description="2024-09-13" tags={["feature", "bug-fix", "improvement"]}>
  * Added support for working with and updating branches checked out across worktrees
  * Added support for working with branches automatically rebased by graphite
  * Fixed a bug where adding an undefined trunk would corrupt cli metadata
  * Fixed a bug where `gt sync --all` would only clean up branches on the current trunk
  * Improved `gt submit` performance by skipping unnecessary fetches
  * Improved performance of deleting branches by only deleting required metadata
  * Updated `gt checkout` to work while on a detached head
  * Updated `gt submit` to submit branches that have never been submitted with Graphite
  * Updated `gt sync` to better handle cases where the branch was updated outside of Graphite
  * Updated `gt init --trunk` to warn against setting a trunk that does not exist locally
  * Updated `gt sync` and `gt get` to work on untracked branches
</Update>

<Update label="1.4.4" description="2024-08-09" tags={["feature", "bug-fix", "improvement"]}>
  * Added new `gt unlink` command to unlink a branch from the currently associated PR
  * Added better support for re-using branch names
  * Added support for passing a branch name to `gt info`
  * Added installation information to CLI releases
  * Fixed a bug where rebases would not handle commits without a parent commit (e.g. original or orphaned commits)
  * Fixed a bug where rebases with merge commits would cause conflicts with already merged commits
  * Fixed a bug where request error logs could cause circular structure errors
  * Updated `gt rename` to use the correct name when asking for a rename confirmation
  * Updated `gt create --insert` to leave descendants in an un-restacked state when there are conflicts
  * Updated `gt delete` to also prune branches
  * Updated pre-push git hooks to better handle running in repo root
</Update>

<Update label="1.4.3" description="2024-08-09" tags={["feature", "bug-fix", "improvement"]}>
  * Added a `--stack` flag to `gt checkout` to only show current stack
  * Fixed a bug where `gt log` and `gt checkout` don't work on untracked branches
  * Fixed a bug where unsetting a trunk would not fully unset it
  * Fixed a bug where `gt` throws a cannot read undefined error while reading "validationResult"
  * Fixed a bug where `gt track` might get into an infinite loop while recovering diverged branches
  * Improved merge conflict status to handle unstaged changes during rebasing
  * Updated instructions for committing untracked files to be more clear
  * Updated networking error diagnostics
  * Updated `gt pr`, `gt docs`, and `gt dash` to print out the URL being opened
</Update>

<Update label="1.4.2" description="2024-07-30" tags={["feature", "bug-fix", "improvement"]}>
  * Added support for `--verbose/-v` in `gt create` and `gt modify` to include the diff in the commit message template
  * Added a `--add` flag to `gt trunk` to configure an additional trunk branch
  * Updated list of unmerged conflict files to print paths relative to the current working directory
  * Updated `gt create` to suppress the detached HEAD message on every create
  * Update pre-push hook error messages to include more details
  * Updated `gt demo` to work in repos the user cannot submit to yet
  * Fixed a bug where the branch name date prefix was incorrect in `gt config`
  * Fixed a bug where `gt submit` would not fetch the branch before submitting to determine if it needs submitting
  * Fixed a bug where `gt continue` would swallow the post-rewrite git hook output
  * Fixed a bug where `gt track` would incorrectly tell you to track the branch
  * Fixed a bug where the `--force` flag was not respected in `gt submit` when the remote was updated
  * Fixed a bug in the interactive selector with `--all` where trunks could not be correctly selected
</Update>

<Update label="1.4.1" description="2024-07-10" tags={["feature", "bug-fix", "improvement"]}>
  * Added a `--trunk/-t` to `gt checkout` to switch to the current trunk
  * Fixed bug where `gt sync` would try to update a trunk you don't have configured
  * Fixed bug in `gt demo` that incorrectly created a "-p" directory to run the demo in
  * Updated `gt init --reset` to also reset PR metadata
  * Reduced the maximum number of parallel git calls in order to reduce spawn errors
</Update>

<Update label="1.4.0" description="2024-07-03" tags={["feature"]}>
  * This version of the Graphite CLI adds support for working on multiple trunks that will be rolled out over the coming weeks via a server-side feature flag.
</Update>

<Update label="1.3.10" description="2024-06-26" tags={["improvement"]}>
  * Updated `gt squash` to no-op when there are no commits to squash or only a single commit
  * Updated all prompt suggestions to support fuzzy searching branches
</Update>

<Update label="1.3.9" description="2024-06-18" tags={["improvement"]}>
  * Updated `gt demo` to initialize Graphite automatically if the current repo has not yet been initialized
</Update>

<Update label="1.3.8" description="2024-06-12" tags={["improvement", "bug-fix"]}>
  * Updated `gt absorb` to print the number of hunks that were not absorbed
  * Updated `gt log` to not show `updated remotely` since it does not respect the new sync changes
  * Fixed bug where `gt sync` would always ask to reconcile when there were local changes
</Update>

<Update label="1.3.7" description="2024-06-05" tags={["improvement", "bug-fix"]}>
  * Updated `gt modify` to print out conflicts when it cannot restack cleanly
  * Added better error handling in `gt sync/get` for server-side errors
  * Fixed more cases of the bug where local version was being overwritten by remote even when user selected `no` from prompt
  * Fixed bug where remote tracking errors would cause commands to fail completely
  * Fixed bug where staged changes were incorrectly detected because of a stale index cache
</Update>

<Update label="1.3.6" description="2024-05-29" tags={["improvement", "bug-fix"]}>
  * Updated `gt feedback` to not require to be run in a repo
  * Fixed bug where a command could trigger thousands of parallel git commands at once causing spawn issues
  * Fixed bug where `gt get` would try to checkout a branch that was just deleted
</Update>

<Update label="1.3.5" description="2024-05-22" tags={["improvement", "bug-fix"]}>
  * Updated `gt modify` to leave descendants in an unrestacked state when there are conflicts.

  * Updated `gt split` behavior to skip git hooks.

  * Fixed bug where local version was being overwritten by remote even when user selected `no` from prompt.

  * Fixed bug where remote rebase-only changes were not reconciled during `gt sync`.

  * Fixed bug where staged changes were incorrectly detected as unstaged.

  * Fixed bug where files changed in parent directories were not detected.

  * Fixed bug where children of split branches were not being tracked.

  * Fixed bug where pre-push hooks were not being run from the repo root.

  * Removed references to deprecated command names.
</Update>

<Update label="1.3.4" description="2024-04-29" tags={["bug-fix"]}>
  * Fixed multiple issues with the new versions of `gt get`, `gt sync`, and `gt submit`. The new versions will be rolled back out with this release.

  * Fixed an issue where `post-checkout` hooks were swallowed, resulting in issues when interactive scripts are used.

  * Fixed some typos in command output.

  * `gt demo` now skips all Git hooks (with an implicit global `--no-verify`).

  * `gt sync` no longer prints out `Restacking branches` if there are no branches to restack.

  * Added details about troubleshooting to `gt --help`.
</Update>

<Update label="1.3.3" description="2024-04-05" tags={["bug-fix"]}>
  * Fixed an issue where `gt submit` could fail in certain cases due to the format of a Git remote URL.

  * Fixed an issue where the wrong branch name was referenced by `gt move`'s prompt.

  * Fixed an issue where `gt absorb` could fail in certain environments.

  * Fixed an issue where `gt log short` could incorrectly show a branch as "updated remotely" when it was not.

  * Added interactivity to `gt feedback`.
</Update>

<Update label="1.3.2" description="2024-03-26" tags={["bug-fix"]}>
  * Fixed a bug where `gt submit` would hang in certain cases.
</Update>

<Update label="1.3.1" description="2024-03-23" tags={["improvement", "bug-fix"]}>
  * Updated `gt submit` to match the new behavior of `gt sync` and `gt get`.

  * `gt submit` now skips branches with no commits between head and base and their descendants, instead of failing outright (GitHub does not allow PRs with no commits).

  * `gt submit` now prompts to restack if the `--restack` flag is not passed and it would fail without restacking.

  * Fixed a bug where `gt submit` would restack in certain cases when the `--restack` flag was not passed.

  * Fixed a bug where `gt submit` was not prompting to choose between pasting template/commit messages and editing them.

  * Fixed a bug where legacy scoped submit commands were not enforcing that branches be restacked before submitting.

  - Deleting branches in `gt sync`, `gt get`, `gt submit`, or with `gt delete` now prints the SHA the branch was at before deletion like Git, as there is no reflog for deleted branches.

  * Added better error messaging for the new version of `gt sync` when unauthed.

  * Fixed a bug where commands that open a URL would fail if `xdg-open` was not installed, instead of printing the URL to the terminal.

  * Fixed a bug where `gt get` would not set up the remote-tracking branch properly.

  * Fixed a bug in the new version of `gt get` and `gt sync` where branches would not get newly associated with PRs.

  * Fixed a typo in `gt absorb`.
</Update>

<Update label="1.3.0" description="2024-03-20" tags={["feature"]}>
  * This version of the Graphite CLI includes a significant update to `gt sync` and `gt get` that will be rolled out over the coming weeks via a server-side feature flag.

  - The primary goal of these changes is to improve the experience of syncing remote changes to your local branches, ensuring that flows like collaborating on a stack or applying suggested edits to a PR are seamless and reliable.

  - Notably, `gt sync` now syncs all branches, where previously it just synced trunk. This brings it closer to the behavior of `gt get`.

  - Conversely, `gt get` with no argument passed is essentially "`gt sync` for the currently checked out stack."

  - The full behavior is:

  1. Update the trunk branch to match remote

  2. Clean up branches associated with merged or closed PRs

  3. Sync any remote changes to local branches

  4. Restack branches as needed

  * If you'd like to be included in the initial rollout of these changes, please let us know in the #cli-beta channel on our Community Slack. Since we are using a server-side feature flag, updating to 1.3.0 alone will not enable the new behavior.

  * The changes are largely based on your feedback, and we're excited to see how they improve your experience with Graphite. THANK YOU!

  - `gt create` now applies the branch prefix to branch names passed in directly (e.g. `gt create branch-name` with a prefix of `prefix/` will yield a branch called `prefix/branch-name`). This behavior can be disabled in `gt config`. If the branch name already begins with the prefix, it will not be added again.

  - Graphite now sets the environment variable `GT` to `1`, which can be checked by subprocesses like an editor or Git hook to determine if they are being run from Graphite.

  * Fixed a bug where `gt absorb` would fail if the git config to detect copies in diffs was enabled.

  * Fixed a bug where `gt split --by-hunk` would leave the user in a detached state if interrupted.

  * If no changes are staged in a step of `gt split --by-hunk`, it will now prompt to stage changes again instead of exiting with an error.

  - Slightly updated help text and error messages for `gt fold`.
</Update>

<Update label="1.2.8" description="2024-03-12" tags={["bug-fix"]}>
  * Fixed a segfault issue caused by a dependency.
</Update>

<Update label="1.2.7" description="2024-03-07" tags={["improvement", "bug-fix"]}>
  * Added support for \`gt demo\` to use a temporary repository if run from outside of a repository.

  * Added support for \`gt demo\` to be run without authenticating the CLI.

  * Fixed an issue where tab autocompletion did not work inside of \`gt demo\`.

  - Added support for \`gt create\` to use AI to populate commit message and branch name. This will be rolled out via a server-side feature flag over the coming weeks.
</Update>

<Update label="1.2.6" description="2024-03-05" tags={["improvement", "bug-fix"]}>
  * By default, `gt create` will now replace slashes in commit messages when inferring branch names, and will convert uppercase letters to lowercase. Both of these new behaviors can be disabled in \`gt config\`.

  * Added individual `--edit-title` and `--edit-description` flags to `gt submit` to allow for editing the PR title and body, respectively. `--no-edit-title` and `--no-edit-description` can be used to skip the prompts for each. Note that `--edit `and `--no-edit` will still work as before.

  * Added support for `gt submit` to use AI to populate PR titles and description. This will be rolled out via a server-side feature flag over the coming weeks.

  * When creating new PRs, `gt submit` will continue to a web browser to edit PR metadata. `--cli` can be passed to use the CLI flow.

  * Added a setting to `gt config` to toggle the above behavior: i.e., use the CLI instead of web by default. In that case, \`--web\` can be passed to use the web flow.

  - Fixed an issue resulting in certain commands failing when using a YubiKey-protected SSH key.

  - Fixed an issue where `gt demo` would not work on Windows.

  * Debug logs are now always written, even when the `--debug` flag is not passed.

  * The `--debug` flag now logs to the terminal as well as to a file.

  * `gt feedback <message> --with-debug-context` now sends our engineers all debug logs from the past 24 hours.
</Update>

<Update label="1.2.5" description="2024-02-27" tags={["improvement", "bug-fix"]}>
  * Adjusted the set of branches that might be included in the new prompt to update upstack branches.

  * Fixed an issue where staged changes could be discarded inadvertently during a `gt sync`.

  * Fixed an issue where `gt demo` would fail on Windows.

  * Added an NPM `postinstall` script to ensure NodeJS version compatibility.
</Update>

<Update label="1.2.4" description="2024-02-22" tags={["improvement", "bug-fix"]}>
  * `gt submit` now prompts to update upstack branches with open PRs when run from a mid-stack branch.

  * `gt submit` is now able to detect when GitHub/Graphite sync is not enabled for a repository. We'll be rolling out the check for this over the coming weeks.

  * A warning is now displayed when branches diverge from Graphite's tracking, and a new flow has been added to `gt track` to remediate diverged branches.

  * `gt log` is now sorted stably.

  - Fixed the `gt sq` alias for `gt squash`.

  - Fixed an issue where `gt submit` would fail (before submitting upstack branches) if run from a merged branch.

  - Fixed an issue where `gt submit` would fail if a pre-push hook had spaces in its path.

  - Ensured better error messaging for various commands when a rebase is in progress.

  - Removed the `--show-delete-progress` flag of `gt submit`.
</Update>

<Update label="1.2.3" description="2024-02-14" tags={["bug-fix"]}>
  Fixed an issue where `gt submit` would fail in repositories using `git-lfs`.
</Update>

<Update label="1.2.2" description="2024-02-13" tags={["improvement", "bug-fix"]}>
  * Adjusted some copy in `gt absorb`
  * Fixed an issue where `gt absorb` only worked when run from the root of a repository
  * Fixed an issue where aborting a `gt create` could leave you in a detached state
  * Added protections against creating server-side PR dependency cycles
</Update>

<Update label="1.2.1" description="2024-02-11" tags={["bug-fix"]}>
  * Fixed an issue where the `gt ab` alias for absorb wasn't recognized
  * Fixed an issue where `gt absorb --patch` hung instead of opening the patch selector
  * Fixed an issue where invalid Graphite metadata would prevent any command from being run
</Update>

<Update label="1.2.0" description="2024-02-09" tags={["feature", "improvement", "bug-fix"]}>
  * Introduced `gt absorb`, which automatically amends staged changes to commits in your stack
  * You can now select which PR template will be used by default in `gt config`
  * `gt checkout -` now selects the last branch that was checked out, just like Git
  * `gt sync` now denotes the currently checked out branch when it was unable to restack it cleanly
  * Added clearer messaging for the action needed to avoid detected merge conflicts on `submit`
  * Fixed an issue where pressing Escape in an interactive prompt selected the current option
  * Fixed an issue where GitHub pull request templates with extensions other than .txt and .md were not detected
  * Fixed an issue where invalid/expired auth on `gt get` resulted in an unclear error message
  * Fixed an issue where `gt get` would not work for stacked branches if using a YubiKey-protected SSH key
  * Fixed an issue where `gt track` would display remote-tracking branches as potential parents
</Update>

<Update label="1.1.5" description="2024-02-02" tags={["improvement", "bug-fix", "feature"]}>
  * Fixed bug in `create` and `modify` where we showed `--update` as an option when there were only unstaged changes (now we only show `--all` and `--patch`)
  * We now show `--patch` as an option for `create` and `modify` even when there are only untracked changes
  * Added interface to let users pick untracked files to track in `--patch` mode (in `create` and `modify`)
  * Improved error messaging for `gt get` for when we can't find a PR for the requested branch
  * Updated `gt get <trunk>` functionality to checkout the trunk branch
  * Improved error messaging for when a user tries to fold a branch into main
  * Added an example to `gt fold --help`
  * Fixed bug where `gt rename` could cause branches to become untracked
  * Added support for `pre-push` git hook
</Update>

<Update label="1.1.4" description="2024-01-31" tags={["improvement"]}>
  * Added an alias `gt --help --all`, which is equivalent to `gt --help --all-commands`
</Update>

<Update label="1.1.3" description="2024-01-22" tags={["feature", "improvement"]}>
  * Added an option to change the trunk branch name in `gt config`
  * Removed prompt to submit on web when the `--no-edit` flag is passed to `gt submit`
  * Updated `gt --help --all-commands`
  * Added `gt completion` to `gt --help --all`
</Update>

<Update label="1.1.2" description="2024-01-16" tags={["bug-fix"]}>
  * Fixed a bug where `gt demo` would error out once the user attempts to run `gt create`
</Update>

<Update label="1.1.1" description="2024-01-12" tags={["bug-fix"]}>
  * Fixed a bug where `gt submit` would unnecessarily prompt that the branch would conflict with remote.

  * Fixed a bug where `gt sync` failed with `"RangeError: Invalid string length"`

  * Updated `gt rename` to fail if the user aborts the command

  * Updated `gt squash` to fail if the squash command does nothing

  * Updated all output to properly respect the `--no-interactive` flag (e.g. `gt log`, `gt info`…)

  * Updated `gt init --reset` to also reset PR metadata

  * Reduced the maximum number of parallel git calls in order to reduce spawn errors
</Update>

<Update label="1.1.0" description="2024-01-09" tags={["feature"]}>
  * Added new `gt demo` feature which interactively teaches you how to use `gt` to create pull requests and stacks.

    * Run `gt demo pull-request` from any repo to create a sample PR.

    * Run `gt demo stack` from any repo to create a sample stack of PRs.

  * Made improvements to `gt help --all-commands`

    * Organized the commands into sections, for better scanning & readability

    * Updated each command description to be shorter on this help page, for better readability

    * Added docs links to the bottom of the help output

    * Configured wrap width of the output to be more responsive to your terminal size

    * Colorized anything in `backticks` in the help output

  - Fixed error messaging in `gt pr` to show the branch name when we couldn't find an open PR for the current branch

  - Fixed the copy in `gt guide workflow` based on community feedback.

  - Fixed `gt merge` to correctly handle the case when a branch is locked.

  - Fixed a bug with `gt get` where it was not correctly checking out the branch after syncing it
</Update>

<Update label="1.0.14" description="2023-12-20" tags={["improvement", "bug-fix"]}>
  * Improved error messaging when config file is invalid.

  * Updated `gt submit` behavior when upstack branches have merged.

  * Added `gt interactive` command to open the Graphite Interactive extension.

  * Updated `gt auth` to print more information about the user's auth status.

  - Fixed an issue where `gt track` would hang if no parent was explicitly passed to the command.
</Update>

<Update label="1.0.13" description="2023-12-13" tags={["bug-fix"]}>
  * Fixed bug where "needs restack" was not printing out in `gt log short`.
</Update>

<Update label="1.0.12" description="2023-12-11" tags={["improvement", "bug-fix"]}>
  * Updated `gt --help` to be an overview of `gt` and the Graphite workflow.

  * Moved the previous command help reference to `gt --help --all-commands`.

  * Added an inline CLI guide to the Graphite workflow, available underneath \`gt guide workflow\`.
</Update>

<Update label="1.0.11" description="2023-11-27" tags={["bug-fix"]}>
  * Fixed bug where aliases were not respected.

  * Added retry when fetching branch from remote fails.
</Update>

<Update label="1.0.10" description="2023-11-13" tags={["improvement", "bug-fix"]}>
  * Updated the `gt submit --draft` flag to only no longer convert already published PRs back to drafts.

  * Added support for team reviewers. Team reviewers can either be specified using `gt submit --team-reviewers slug` or through `gt submit --reviewers org/slug`.

  - Added output to `log short` when a branch needs to be fetched from remote (using `gt get`).

  - Added output after `gt checkout` specifying whether a branch needs to be submitted, fetched, or restacked.

  * Removed a reference to legacy command names.
</Update>

<Update label="1.0.9" description="2023-10-23" tags={["improvement", "bug-fix"]}>
  * Improved how PR descriptions are persisted across aborted `submit` runs.

  * Modified version prompting so users are only asked to upgrade their CLIs once per day.

  - Fixed a bug in remote changes detection.
</Update>

<Update label="1.0.8" description="2023-10-16" tags={["improvement", "bug-fix"]}>
  * Added an `--update` option for `create` and `modify` that stages changes to all already-tracked files.

  * Added support for `gt get <pr-number>.`

  * Added a `--comment` flag to `submit` which will add a comment with the provided text to the submitted PR.

  * Added additional debugging information to the output file of the `--debug` flag.

  - Fixed a bug where the incorrect version number was displayed after running `gt get` for a remote branch
</Update>

<Update label="1.0.7" description="2023-10-04" tags={["improvement", "bug-fix"]}>
  * Added `gt aliases --legacy` command to automatically add all of the old shortcuts to your aliases configuration.

  * Added ability to navigate through prompts using ctrl+n and ctrl+p.

  * Updated `submit` description behavior to include commit messages if no default template exists.

  * Updated how we detect if there are remote changes to a PR that need to be resolved.

  - Fixed a bug where local state could become corrupt after switching trunk branch.

  - Fixed a bug where we were syncing information for untracked branches.

  - Fixed incorrect `restack` deprecation warning.
</Update>

<Update label="1.0.6" description="2023-09-29" tags={["improvement", "bug-fix"]}>
  * Updated the default behavior on `gt submit` to not restack branches.

  * Added an optional `--restack` flag to `gt submit`.

  * Always prompt on `gt submit` if the branch will have conflicts with main.
</Update>

<Update label="1.0.5" description="2023-09-18" tags={["bug-fix"]}>
  * Fixed a stray line of output in `gt create`.

  * Fixed an issue where syncing PR data from remote could set the wrong parent.
</Update>

<Update label="1.0.4" description="2023-09-18" tags={["improvement", "bug-fix"]}>
  * Updated `--help` output to be more consistent and more helpful.

  * Added a new command `gt aliases` to open up the alias file in your editor.

  * Now removes `~/.graphite_user_config` once your configuration has been moved to the new location to reduce confusion.

  - `gt submit` now opens the PR in your browser if you pass the `--view` flag.

  - `gt rename` now prompts instead of immediately failing if you don't pass `--force` when required.

  - `gt up `interactive selection now prompts you a single time instead of at each level (similar to the `top` change from v1.0.2).

  * Fixed the `gt pr` command.

  * Fixed a bug where no error message was printed when you try to create a branch with an invalid or existing name.

  * Updated branch naming validation to more closely match the Git specification. Please let us know if you see any inconsistencies.
</Update>

<Update label="1.0.3" description="2023-09-15" tags={["bug-fix"]}>
  * Fixed an issue where restacking did not respect the `commit.gpgSign` configuration value.

  * Fixed an issue where `create` with just a branch name incorrectly failed to execute.

  * Fixed an issue where the `git --version` check failed on Windows (and likely certain other git distributions).
</Update>

<Update label="1.0.2" description="2023-09-15" tags={["improvement", "bug-fix"]}>
  * `gt top` interactive selection now offers which tip to travel to instead of prompting at each intermediate step. We'll be porting the same behavior to `gt up` soon.- The `--debug` flag now logs to a file instead of stdout.- Clearer error messaging for outdated Git version.

  * Fixed a bug where `gt sync` could reset the index and working tree, and improved error handling in similar cases with uncommitted changes.- Fixed the error messge when running a deprecated command to print the correct alias file location.
</Update>

<Update label="1.0.1" description="2023-09-14" tags={["bug-fix"]}>
  * Fixed a bug where `gt submit --stack` did not work from the trunk branch.
</Update>

<Update label="1.0.0" description="2023-09-13" tags={["feature"]}>
  ### Renaming and configuration

  * All commands that fell under `branch`, `stack`, `upstack`, `downstack`, `repo`, and `user` have been renamed to drop the noun. Old command names still work, but will be removed in an upcoming version.

  * The full list of commands is available in `gt --help` or at [https://graphite.com/graphite-cli-v1-command-names](https://graphite.com/graphite-cli-v1-command-names).

  * Graphite now supports custom aliasing for any command via `~/.config/graphite/aliases` (or `$XDG_CONFIG_HOME/graphite/aliases`).

  * A preset to copy into this file to keep the old short command names is found at [https://graphite.com/docs/legacy-alias-preset](https://graphite.com/docs/legacy-alias-preset).

  * All Graphite configuration now lives in the interactive `gt config` command.

  * Graphite's user-level configuration files are now XDG Base Directory Specification compliant, or stored in `~/.config/graphite` by default.

  `gt create`

  * `gt create` is the new command to create a Graphite branch (formerly `branch create`)

  * `gt create` now supports inferring a branch name from the commit editor, which means it is now possible to run it with no arguments.

  * If you have unstaged changes and no staged changes when running `gt create`, you are now asked whether you'd like to stage and commit them as part of the new branch.

  `gt modify`

  * `gt modify` is the new command to modify a Graphite branch (formerly `gt commit amend`/`gt commit create`).

  * The default behavior is to amend the current commit on the branch, unless the branch has no commits or `--commit` is passed.

  * When amending a commit, the editor is not opened by default unless `-e`/`--edit` is passed.

  * If you have unstaged changes and no staged changes when running `gt amend`, you are now asked whether you'd like to stage them before running the amend or commit operation.

  * `gt branch edit` has been moved to `gt modify --interactive-rebase`

  **`gt sync`**

  * `gt sync` is the new command to update your trunk branch, clean up merged branches, and restack most branches in your repo.

  * `gt sync` now restacks all branches by default (no longer need `-r`).

  * If any branch has conflicts with its parent branch, instead of launching you into a conflict resolution, `sync` will print out the list of conflicting branches so that you can run `gt restack` on them.

  `gt submit`

  * `gt submit` is the new command to push branches to GitHub and create stacked PRs for them.

  * `gt submit` submits the currently checked out branch and its ancestors (dependent branches) by default.

  * `gt ss` is included in the alias file by default as an alias for `gt submit --stack`, which replicates the behavior of the old `gt stack submit`

  * `gt submit` now handles cases where branches in your stack have merged or been updated remotely, as long as there are no rebase conflicts to resolve. This includes both incorporating remote changes and removing merged branches from the stack.

  * `gt submit` now ensures that your branches are restacked instead of failing when they aren't.

  ### Entirely new commands

  * `gt pop` to delete the current branch and check out its parent without modifying the working tree. Can't be run if the current branch has children.

  * `gt trunk` to navigate directly to your trunk branch.

  * `gt parent` to print out the raw parent of the branch (for scripting).

  * `gt children` to print out the raw children of the branch, line by line (for scripting).

  * `gt revert` (experimental) to create a branch that reverts a commit in your trunk branch.

  ### Other changes

  * Added a new `--stat` flag to `gt info` that prints out a diffstat instead of a full diff. Compatible with either `--diff` or `--patch`.

  * `gt create --insert` now asks which siblings should be moved onto the new branch if there are more than one of them.

  * Performance improvements.

  ### Bug fixes

  * Fixed a bug where stray output was printed while completing command names.

  * Fixed an issue where a single optional PR template was interpreted as required PR template.

  * Fixed a bug where branch prefixes could not end with a slash.

  * Fixed a bug where `split --hunk` would not work for branches that added new files.

  * Fixed a bug where the branches created by `split` were all based on the parent of the split branch instead of being stacked correctly.

  * Fixed a bug where the `--patch` flag to `create` and `modify` did not include new files.

  ### Notes

  * The `test` command has been temporarily removed due to persistent bugginess, but will be added back when we have time to dedicate to making it work well. For now, one option is to script using the new `gt children` and `gt parent` commands, which should handle most use cases.

  * We are still working on further improvements to `sync` and would love your feedback in this area!

  * We'd also love to hear about how we can make `revert` work best for you!

  * As of the release of this version, certain parts of the web app and docs may still reference the old command names. We're updating those places as you read this!
</Update>

<Update label="0.22.16" description="2023-09-08" tags={["improvement", "bug-fix"]}>
  * Added autocomplete support for the renamed commands.
  * Fixed a bug in `get` when the PR does not exist locally.
  * Fixed a bug where an `git range-diff` failure could block submit.
</Update>

<Update label="0.22.15" description="2023-09-07" tags={["improvement", "bug-fix"]}>
  * Introduced an environment variable to preview the command rename and custom aliasing system that will be released next week as Graphite CLI v1. For more details, see [https://graphite.com/graphite-cli-v1-command-names](https://graphite.com/graphite-cli-v1-command-names).
  * Introduced a new interactive command `gt config` which covers all user- and repo-level configurations. The `gt user` and `gt repo` top-level commands will be deprecated in an upcoming release.
  * `checkout` now prompts to `sync` when the branch's PR has been merged.
  * `get` no longer fetches branches for merged PRs.
  * Fixed a bug where having the VSCode extension open while restacking could corrupt cached stack data.
  * Fixed a bug where restacks would get stuck in a confusing/corrupt state due to concurrent git processes (i.e. VSCode extesnion).
  * Fixed a bug where an `git range-diff` failure could block submit.
</Update>

<Update label="0.22.14" description="2023-09-06" tags={["bug-fix"]}>
  * Fixed a bug where users with a Yubikey-protected SSH key were unable to `sync`.
  * Fixed a bug where an uncaught IPC exception would appear after running a command.
  * The cool part is that turning this configuration on allows you to set custom aliases via the `~/.graphite_aliases` file, which we know some of you have been asking us about for quite a while!
</Update>

<Update label="0.22.9" description="2023-08-31" tags={["bug-fix"]}>
  * Fixed a bug where the wrong version could be shown in `gt log`.
  * Fixed a bug where `get` didn't work to fetch new branches.
  * Cleaned up a suggestion to run `submit --force`
  * Removed the interactive portion at the end of `init` for branch tracking (hint about `track` is still shown).
  * `GT_RENAME` flag now displays the correct command names in suggestions.
</Update>

<Update label="0.22.8" description="2023-08-31" tags={["improvement", "bug-fix"]}>
  * You guessed it -- more performance improvements!

  * `submit` commands now automatically pull in changes from remote and rebase on top of them when your local changes don't conflict with them.

  * `downstack get` now shows which version of the PR has been fetched.

  * `gt log` now shows the last submitted version of each PR, as well as whether you need to \`submit\` or \`get\`.

  * `branch checkout` now informs you if you need to `get`.

  * Fixed an issue where `branch checkout --patch` failed with an incorrect error message.

  * Fixed an issue where `downstack get` failed with an incorrect error message.

  * Fixed some issues with inconsistent failures in `get`

  * Added an experimental `graphite_aliases` file (see below)

  We are currently in the process of renaming all Graphite commands. This version is the first one with the full set of renamed commands implemented. If you'd like to try out this new command surface, you can add "export GT\_RENAME=1" to your shell configuration file (e.g. \~/.zshrc) to be warned when you run a renamed command and what the new name is. It may be unstable and is primarily meant for employee testing purposes until further notice. There is no overlap between the old set of commands and the new set.
  For more information, see this [Notion doc](https://www.notion.so/withgraphite/Proposal-for-Graphite-CLI-changes-400d068c7c8546fcbc90b5573e6f27e9?pvs=4).
  The cool part is that turning this configuration on allows you to set custom aliases via the `~/.graphite_aliases` file, which we know some of you have been asking us about for quite a while!
</Update>

<Update label="0.22.6" description="2023-08-25" tags={["improvement", "bug-fix"]}>
  * More performance improvements!

  * Fixed an issue where mangled output was displayed in `gt user editor`.

  * Fixed an issue where `downstack merge` didn't exit if the PR was already merging/merged.

  * Fixed an issue where `downstack get` did not work.
</Update>

<Update label="0.22.4" description="2023-08-21" tags={["improvement", "bug-fix"]}>
  * More performance improvements!

  * Added a clearer warning about Node.js version compatibility for `npm` installs.

  * Fixed an issue where `--force` in `submit` was not respected.

  * Building on a change from 0.22.1, `downstack get` now automatically pulls in changes from GitHub if the local state of the branch matches a submitted version of the branch's open pull request, \*\*even if rebased\*\*.

  * `submit` now prompts for a `downstack get` in cases where there are remote changes that need to be synced.
</Update>

<Update label="0.22.3" description="2023-08-16" tags={["improvement", "bug-fix"]}>
  * Many small performance improvements!

  * Added a `--rerequest-review` flag to `submit` commands that rerequests review from anyone who has reviewed the PR.

  * `submit` is now blocked by an ongoing rebase.

  * `--quiet` is now respected by underlying `git commit` calls.
</Update>

<Update label="0.22.1" description="2023-08-10" tags={["bug-fix"]}>
  * Fixed a bug where `prNumber` was incorrectly displayed in the `gt log` output instead of the actual PR number.

  * `downstack get` now automatically pulls in changes from GitHub if the local state of the branch matches a submitted version of the branch's open pull request.

  * `submit` commands now suggest running `downstack get` when the above situation is detected.

  * YubiKey prompting for SSH is now moved behind a config, in order to address some bugs that passing through the YubiKey prompt introduced. If you are using a YubiKey to authenticate with GitHub, you can enable this config with `gt user yubikey --enable`.

  * Added a global `--cwd` flag to run any Graphite command in a directory other than the one it is initiated from.
</Update>

<Update label="0.22.0" description="2023-08-04" tags={["feature"]}>
  * Added a new `gt downstack merge` command to merge stacks and PRs directly from the CLI.

  * `submit` commands now display code updates and metadata updates as two different statuses in the list of updates.
</Update>

<Update label="0.21.5" description="2023-07-27" tags={["improvement", "bug-fix"]}>
  * We had a few versions' worth of iterating on internal issues and the new release process from our monorepo, thanks for bearing with us!
</Update>

<Update label="0.21.0" description="2023-07-21" tags={["feature"]}>
  * We pushed a few patch versions to npm and brew between 0.20.24 and now, but there were no major changes in any of them, so they are not listed in the changelog.

  * `gt log` now shows the PR's overall status (consistent with Graphite app; takes stacks into account).

  * Added a new `-m` flag to `submit` commands that enables "merge when ready" on the Graphite app, merging the PR if it is already ready to be merged.

  * Added a new option `--exclude-templates` to `gt user submit-body` which specifies that the PR template should not be included in the default PR description when `--include-commit-messages` is enabled.

  * Fixed a few long-standing performance issues that affected all commands, most noticeably shorter-running ones.

  * Fixed an issue where the Yubikey prompt shown by git commands was not being diplayed.

  * Fixed an issue where the \`branch track\` command was missing.
</Update>

<Update label="0.20.22" description="2023-06-22" tags={["improvement", "bug-fix"]}>
  * Added the request ID to HTTP error message output for better user issue debugging
</Update>

<Update label="0.20.21" description="2023-06-22" tags={["improvement", "bug-fix"]}>
  * No changes, had to bump a new version to get around accidentally pushing v0.20.19 to `npm` as v0.20.20
</Update>

<Update label="0.20.20" description="2023-06-21" tags={["improvement", "bug-fix"]}>
  * `gt dash` commands now use the app URL from the user's profile when passing links to `open`.
</Update>

<Update label="0.20.19" description="2023-05-11" tags={["improvement", "bug-fix"]}>
  * When editing a PR description, the temporary file is now named `GRAPHITE_PR_DESCRIPTION.md`. This allows for Markdown syntax highlighting, and also adding additional editor config by specifically targeting this file name.
</Update>

<Update label="0.20.18" description="2023-4-28" tags={["bug-fix"]}>
  * Fixed a bug where `gt changelog` was broken for the binary version of the CLI (e.g. installed via `brew`).

  * Fixed a bug where `gt branch edit` was accidentally removed from the CLI. Thank you @vampire!

  * Added `fish` completion support via `gt fish >> ~/.config/fish/completions/gt.fish`! Thank you @szamanr!
</Update>

<Update label="0.20.17" description="2023-4-24" tags={["improvement", "bug-fix"]}>
  * This should fix the npm install issues!
</Update>

<Update label="0.20.16" description="2023-4-21" tags={["bug-fix"]}>
  * Fixed a bug where `repo sync` attempts to delete branches that were never associated with a PR.
</Update>

<Update label="0.20.15" description="2023-3-22" tags={["improvement", "bug-fix"]}>
  * Add setting trunk to remote version if it cannot be fast-forwarded.
</Update>

<Update label="0.20.14" description="2023-2-10" tags={["improvement", "bug-fix"]}>
  * Add `--always` flag to submit to always push updates, even if the branch has not changed.
</Update>

<Update label="0.20.13" description="2022-1-20" tags={["improvement", "bug-fix"]}>
  * Tweaked git passthrough copy to make it clear that a command was run.

  * Fixed a bug where `test` commands didn't support multiple separators in a branch name.

  * Replaced individual `gt ls-remote` calls on `submit` with a single one, which should speed up submission significantly!

  * Fixed a bug where PR data was not being synced in the background.
</Update>

<Update label="0.20.12" description="2022-11-25" tags={["improvement", "bug-fix"]}>
  * `gt stack submit` now prompts for submission info inline after each individual branch, instead of after all branches.

  * The `--edit/-e` flag on `submit` commands now allows updating the PR title and body.

  * The `--reviewers/-r` flag on `submit` commands can now update existing PRs.

  * The `--reviewers/-r` flag on `submit` commands now accepts a string of comma separated reviewers (e.g. `user1, user2`).

  * `gt commit amend` no longer requires staged changes.

  * `gt commit amend` no longer allowed on empty branches.

  * `gt commit create/amend` no longer allowed during a rebase.

  * Improved suggested messages when encountering errors during a rebase.

  * Improved error messaging by showing error code and number when available.

  * Improved error reporting when running `test` commands.
</Update>

<Update label="0.20.11" description="2022-09-26" tags={["improvement", "bug-fix"]}>
  * Changed many error messages to be more actionable, and changed some tips to always-visible messages.

  * Improved accuracy of checking whether a branch is up to date on `submit`.

  * The `--edit/-e` flag on `submit` now opens an editor for each PR without prompting first. Passing no flag still prompts the user whether they'd like to open an editor, and `--no-edit` still skips the prompt,

  * The `--select/-s` flag of `submit` now prompts about which branches to include in the submit as the first step so that it can validate that the correct dependencies are included in the submit scope.

  * Fixed a bug preventing creation of a debug context within a large repository.

  * Fixed a bug logging output for `gt branch test` on branches with a slash in the name.

  * Running git commands no longer opens another terminal on Windows.
</Update>

<Update label="0.20.10" description="2022-08-02" tags={["improvement", "bug-fix"]}>
  * Addressed one remaining gap in pager parity with git: set the environment variables `LESS=FRX` and `LV=-c` if unset.
</Update>

<Update label="0.20.9" description="2022-08-02" tags={["improvement", "bug-fix"]}>
  * Fixed remaining issues with pager by switching from a temp file to a pipe.

  * Fixed a bug where `gt log short` wouldn't show the filled-in circle for branches needing a restack.

  * Fixed a bug where `gt branch split` untracked children of the branch being split if the last branch in the split kept its name.
</Update>

<Update label="0.20.8" description="2022-07-29" tags={["improvement", "bug-fix"]}>
  * Improved error mesaging around failed pager execution.
</Update>

<Update label="0.20.7" description="2022-07-29" tags={["improvement", "bug-fix"]}>
  * `gt log`, `gt changelog`, and `gt branch info` now display in a pager. The pager defaults to your git pager, but can be overridden with (for example) `gt user pager --set 'less -FRX'`.

  * Fixed a bug where `--no-edit` on `submit` would automatically open new PRs in draft mode (it now prompts unless `--draft`, `--publish`, or `--no-interactive` is set).

  * Fixed a bug where killing the CLI during submit could result in being unable to submit again (due to a temporary filename clash).

  * Fixed colors for `gt branch info --patch`.

  * Fixed a bug related to buffer size for certain git commands.

  * Fixed the error displayed when attempting to install Graphite on old Node.js versions.
</Update>

<Update label="0.20.6" description="2022-07-25" tags={["improvement", "bug-fix"]}>
  * `submit` after an aborted submit now asks the user whether they'd like to use their cached PR body instead of always using it.

  * `gt branch split` now tracks untracked branches automatically before splitting.

  * `gt branch untrack` now untracks the current branch if no branch name is provided.

  * Fixed an issue where `gt branch create` would fail instead of creating a branch with no commit in certain cases.

  * Fixed `gt branch edit`.
</Update>

<Update label="0.20.5" description="2022-07-22" tags={["improvement", "bug-fix"]}>
  * Fixed `gt changelog`.

  * Fixed `submit`, `downstack edit` for editor commands containing spaces.

  * Fixed `git push` errors being swallowed on submit.
</Update>

<Update label="0.20.4" description="2022-07-21" tags={["improvement", "bug-fix"]}>
  * Added `gt changelog` and `gt docs`. You probably want to pipe the changelog to a pager or file :).

  * Fixed a bug where a `git rebase --abort` after a restack conflict would result in Graphite being wrong about the current branch.

  * Improved `test` command output.

  * Internal improvements.
</Update>

<Update label="0.20.3" description="2022-07-21" tags={["improvement", "bug-fix"]}>
  * Minor internal fix.
</Update>

<Update label="0.20.2" description="2022-07-19" tags={["improvement", "bug-fix"]}>
  * Fixed an issue preventing installation.
</Update>

<Update label="0.20.1" description="2022-07-19" tags={["improvement", "bug-fix"]}>
  * Fixed an issue preventing installation.
</Update>

<Update label="0.20.0" description="2022-07-19" tags={["feature"]}>
  * Added a new command `gt branch split` that allows the user to interactive split a branch into multiple dependent branches. There are two styles of operation:

    * `--by-commit` mode (aliases `--commit`, `-c`) prompts the user to select the commits within the branch that they'd like to have branches at.

    * `--by-hunk` mode (aliases `--hunk`, `-h`) prompts the user to create a series of single-commit branches from the changes of the branch using the `git add --patch` interface.

  * Greatly improved `gt log short` readability. Give it a try!

  * `gt branch create`, `gt commit create`, and `gt commit amend` now support the `-p/--patch` option (like `git commit --patch`). Please note that this won't be the most useful option until autostashing is implemented, planned soon.

  * Branch navigation commands now notify the user if the branch being checked out is either

    * behind its parent (needs restacking)

    * upstack of a branch that is behind its parent

    * untracked

  * `gt log` and `gt log short` now show untracked branches when `--show-untracked/-u` is passed in.

  * `gt branch checkout` now includes untracked branches in the selector when `--show-untracked/-u` is passed in.

  * Added `-n` as an alias for `--no-edit` for `submit`. Try out `gt ss -np` to quickly publish your changes!

  * Added `--select`/`-s` option for `submit` to select which branches to push.

  * Added `--force`/`-f` option `submit` to do a force-push, i.e. `git push -f`, instead of the default `git push --force-with-lease`.

  * Added a non-blocking note if the user submits a branch that is not restacked on trunk.

  * On trying to submit branches with PRs already closed/merged, instead of failing immediately users will be prompted to choose either to abort or create new PRs.

  * `submit` now correctly sets the upstream of the pushed branch.

  * You can now configure whether you'd like commit messages in PR bodies by default behind the configuration `gt user submit-body --include-commit-messages`. Disabled by default. Use `gt user submit-body --no-include-commit-messages` to disable.

  * Added `--force`/`-f` for `gt downstack get` to always overwrite local branches.

  * `gt downstack track` can now take a positional branch name argument (like `gt branch track`).

  * Added `--diff`/`-d` for `gt branch info` to show the diff of the whole branch (unlike `--patch`/`-p` which shows the diff of each commit).

  * Interactive prompts autocomplete is now case-insensitive.

  * `gt --help` now includes a link to the CLI documention.

  * Improved `gt repo init` copy.

  * Improved error messaging for when an internal `git` command fails.

  * Improved error messaging for when a `submit` command fails due to a GitHub API error.

  * Improved `test` command output.

  * Improved clarity of positional arguments for all commands with them in `--help`

  * Improved performance of internal cache.

  * Improved telemetry.

  * Fixed a bug where `test` commands were completely broken.

  * Fixed a bug where `upstack onto` autocomplete did not work if `uso` shortcut was used.

  * Fixed a bug where `--no-interactive` and `--no-edit` were not handled properly for `submit`

  * Fixed a bug where `gt log` would break on the initial commit of a repository.

  * Fixed a bug where trunk would be in the list of branches to track in `gt repo init`

  * Fixed a bug where the error message for old versions of Node.js wouldn't show up.

  * Added cycle detection for parent pointers.
</Update>

<Update label="0.19.6" description="2022-07-07" tags={["improvement", "bug-fix"]}>
  * Fixed a bug where continue state could be corrupted by running a `gt` command before running `gt continue`.

  * Fixed a bug where `upstack onto` could target untracked branches, resulting in corrupted state.

  * Fixed a bug where renaming a branch to its current name resulted in corrupted state.

  * Added `dstr` as an alias for `downstack track`.

  * Slightly improved rebase conflict printout.
</Update>

<Update label="0.19.5" description="2022-07-06" tags={["improvement", "bug-fix"]}>
  * Added a new command `gt downstack track` that, from an untracked branch, allows you to track recursively by choosing the parent until you reach a tracked branch. Use `--force/-f` to automatically select the nearest ancestor of each branch, which should give behavior similar to `gt stack fix --regen` of old.

  * Added a new command `gt branch fold` that folds the changes of the current branch into the parent branch. Uses the parent branch's name for the new branch with default; pass in `--keep/-k` to use the current branch's name instead.

  * Added a new command `gt branch squash` that turns a branch of multiple commits into a single-commit branch. Takes `--message/-m` and `--no-edit/-n` arguments just like `gt commit amend`, and defaults to using the message of the first commit on the branch.

  * Fixed a bug where if neither `--draft` nor `--submit` was passed, updated PRs would always be published if previously drafts, and new PRs would be published instead of being created as draft.

  * Fixed a bug where `gt branch track --force` wouldn't always select the nearest ancestor.

  * Fixed a bug where `gt` with no command would throw an uncaught exception instead of displaying the help message.

  * Fixed a bug where cancelling certain interactive prompts would result in undefined behavior.
</Update>

<Update label="0.19.4" description="2022-07-05" tags={["improvement", "bug-fix"]}>
  * Based on a user survey, we've slightly changed the defaults for PR title and description on `submit` commands.

    * PR Title defaults to the title of the first (or only) commit on the branch.

    * PR Description defaults to a list of commit messages followed by a PR template, if one exists.

  * `branch info` and `log` now show the commit hash of trunk.

  * Added a `repo init --reset` which clears all Graphite metadata.

  * Added a new user-scoped configuration enabled by `gt user restack-date --use-author-date` which when enabled passes `--committer-date-is-author-date` to the internal `git rebase` of restack operations. To return to the default, use `gt user restack-date --no-use-author-date`.

  * Added autocompletion for the `branch up` disambiguation prompt.

  * Added `gt dpr` as a shortcut for `gt dash pr`

  * Renamed the `--no-draft` option for \`submit\` commands to `--publish/-p`. There are three modes of operation for the command:

    * By default, leave existing PRs in the same state and create new PRs in draft mode.

    * When `--draft/-d` is passed, all PRs in the submit scope will be marked as draft.

    * When `--publish/-p` is passed, all PRs in the submit scope will be marked ready for review.

  * Added an interactive prompt for `gt branch rename` when no new name is passed in.

  * Added a `--force/-f` option for `gt branch track `that skips the interactive prompt by picking the nearest tracked ancestor.

  * Fixed a bug where `branch submit` and `downstack submit` base validation would fail incorrectly on certain operating systems.

  * Fixed a bug where leftover cached metadata across CLI versions could result in inconsistent state.
</Update>

<Update label="0.19.3" description="2022-06-28" tags={["improvement", "bug-fix"]}>
  * Changed the flow of `gt branch track`. Now, it tracks the current branch by default, unless another branch is specified. By default, prompts the user to select a branch to be its parent if there are multiple possibilities, or you can pass in a `--parent`.

  * Updated the new `log short` view to be more comprehensible (uses diagram symbols from `log`).

  * Fixed a bug where `--restack` wouldn't restack all branches as expected if `gt repo sync` was run from trunk.

  * Fixed a bug where `gt ss` would fail if run from trunk.

  * Fixed a bug where `gt downstack get` would fail to get branches that existed locally but were untracked by `gt`.

  * Fixed a bug where after a `git rebase`, Graphite metadata could end up in a broken state.

  * Fixed a bug that prevented `gt feedback --with-debug-context` from working as expected.

  * Fixed a bug where `gt upstack onto` interactive selection could appear wonky.

  * Fixed some copy in v0.19 newly added features.
</Update>

<Update label="0.19.2" description="2022-06-15" tags={["improvement", "bug-fix"]}>
  * Fixed an issue where `downstack get `was completely broken.

  * Replaced the emoji for `Pushing to remote and creating/updating PRs...` step of `submit`

  * Fixed an issue where `gt branch edit` would only work if the branch was not in need of restacking.

  * Added support to rebase local changes on top of remote for `downstack get`

  * Fixed a bug where choosing to cancel `submit` because of an empty branch did not abort correctly.
</Update>

<Update label="0.19.1" description="2022-06-14" tags={["improvement", "bug-fix"]}>
  * Removed some development tooling as a workaround to unblock Homebrew release. Sorry for the delay!

  * Fixed a shebang issue that resulted from trying to clean up Node.js v18 warnings. Added a different fix to prevent Node.js warnings from showing up in CLI output.

  * Fixed a bug with Node.js v14 support.

  * Changed the Homebrew Node.js dependency to v16, which is the same as we use for development.
</Update>

<Update label="0.19.0" description="2022-06-13" tags={["feature"]}>
  * Ensured every commonly used command has an alias and changed a few names. A current list of commands will be included in the Community Slack with this release.

    * `gt branch show` is now `gt branch info`. As this command is relatively new, we are not leaving `show` as an alias.

    * `gt branch create --restack` is now `gt branch create --insert`. This was the originally intended name, and it does something different than `gt repo sync --restack`

    * `gt downstack sync` is now `gt downstack get`. It was confusing to have two `sync` commands do entirely different things!

    * The old names `gt branch prev` and `gt branch next` for `down` and `up` are now fully deprecated.

  * Updated a significant portion of the info and error messages spanning almost every command.

  * Ensured every command has up-to-date and helpful `--help`.

  * Added a number of tips to various commands.

  * Greatly improved autcompletion —now every command has autocomplete for nouns, verbs, flags, and branch names when applicable.

  * `gt branch checkout`, `gt upstack onto`, and `gt branch track` now all have substring autocompletion for interactive branch selection. Enjoy! :D

  * `gt auth` and `gt user` commands can now be run outside of a Git repository.

  * Removed the concept of "ignored branches" from `gt repo init`, and the user config.Removed the `gt repo ignored-branches` command.

  * Removed `gt <scope> fix`. `fix` is now an alias for `restack`.

  * Removed `gt <scope> validate`

  * Removed `gt branch parent`, `gt branch children`, and `gt branch pr-info`. All of this information is now found in `gt branch info`. `gt branch rename` is now the only way to reset PR info for a branch, as PR info is now synced by branch name for the open PR with that name.

  * Removed `gt repo fix`.

  * Removed `gt repo trunk`. You can change the trunk branch by running `gt repo init --trunk <trunkName>` .

  * Removed `exec` functionality of `gt downstack edit`—we recommend using `gt stack test` for running a command on each branch in your stack.

  * Added a new command `gt branch track`. In order to track an existing git branch `<branchName>`, ensure that it is based on a Graphite branch `<parentBranchName>`, and then with `<parentBranchName>` checked out, run `gt branch track <branchName>` to start tracking it as a Graphite branch.

    * You can also specify a `--parent` in `gt branch track` instead of checking out the desired parent before running the command.

    * If run without a branch to track `gt branch track` suggests branches that have the current branch/specified parent in their history.

  * Added `gt branch untrack` to remove Graphite metadata for a branch.

  * Added a new flow to `gt repo init` for letting users new to Graphite convert an existing "stack" of branches into a Graphite stack. Essentially calls `gt branch track` in a loop.

  * Added a new verb `gt <scope> restack` for the `branch`, `upstack`, `downstack`, and `stack` nouns. For each branch in the scope, this command checks if the branch is based on its parent, and rebases it if necessary. `gt upstack fix` and `gt stack fix` will alias to `restack` for a couple versions.

  * Improved `gt log short` - the view now essentially a single-line-per-branch version of `gt log`. The old style can still be accessed with `gt log short --classic`.

  Added a `--reverse` option to `gt log` and `gt log short/.` Helpful for big stacks!

  * Added `--stack` option for `gt log` and `gt log short`. Only displays the current stack (i.e. what \`gt stack submit\` would submit).

  * Added `--steps <n>` option for `gt log` and `gt log short`. Implies `--stack` and only shows \`n\` levels above and below the current branch.

  * Rebase conflict message now shows a `gt log short --steps 3` centered at the branch being resolved.

  * Interactive selection for `gt branch checkout`and `gt upstack onto` now uses the new `gt log short` view. Much easier to see what you're doing with long branch names!

  * `gt dash` can now open the PR page for the current branch or a specified one: `gt dash pr [numberOrBranchName]`

  * `gt branch info` can now show the current PR description with `--description`.

  * Added `upstack` and `downstack` counterparts of `gt branch test`.

  * `gt branch delete` now restacks the deleted branch's children onto its parent.

  * Removed the `--resubmit` flow from `repo sync` —we may add it back in the future.

  * Added a `--restack` option to `repo sync`, which restacks the current branch and any branches in stacks with cleaned up branches. We imagine a common flow if you know that you don't have conflicts with trunk will be `gt rs -rf`. Or even `gt rs -rf && gt ss`.

  * Fixed a bug where `--draft` and `--no-draft` on `submit` commands would unnecessarily submit unchanged PRs.

  * Fixed bugs related to rebases not being performed properly that often resulted in confusing state and messaging.

  * Now fails gracefully if running on an unsupported Node.js version (requires Node.js version 14 or higher)

  * The Graphite CLI experience survey is no longer shown when commands are run in non-interactive mode.

  **Note from the maintainers:**

  Thanks for trying out the new version of the Graphite CLI! Please let us know if you see any issues with this new version, or have any suggestions for improvements related to functionality, flow, or transparency/simplicity.

  New documentation for the CLI is coming soon! We love hearing your feedback about what documentation would be helpful —keep it coming!

  Rebasing on `gt downstack get` has been outscoped for this release in order to get it to you sooner! We're still excited to put it out soon.
</Update>

<Update label="0.18.7" description="2022-05-31" tags={["improvement", "bug-fix"]}>
  * Fixed a pervasive bug that prevented using `gt` on Windows at all — there are likely still remaining issues to work out before we have full support, and we still recommend using WSL for the most stable Graphite experience. Thanks to our community for helping out here!

  * Fixed a bug where `git push` error messages would not be displayed on `submit`, resulting in confusion around whether pushes were failing because of e.g. `pre-push` hooks or`--force-with-lease` errors.

  * Added better support for multiple checkouts (i.e. `git worktre`\`). We consider our support experimental, see the new section of the docs for details.
</Update>

<Update label="0.18.6" description="2022-05-20" tags={["improvement", "bug-fix"]}>
  * Fixed a bug where running `gt branch rename` on submitted branches would result in `gt` becoming largely unusable.

  * Added a new `--force/-f` option to `gt branch rename` that is required for already-submitted branches.

  * `gt branch rename` now respects character replacement settings.
</Update>

<Update label="0.18.5" description="2022-05-19" tags={["improvement", "bug-fix"]}>
  * `.` and `/` are no longer replaced in branch names.

  * Fixed a regression where the current branch wouldn't be selected by default in `gt branch checkout` interactive mode.

  * Upgraded `node` and `yarn` dependencies, please let us know if you see any weirdness!
</Update>

<Update label="0.18.4" description="2022-05-16" tags={["improvement", "bug-fix"]}>
  * `gt downstack sync` no longer requires turning on a configuration option to use (for real this time)
</Update>

<Update label="0.18.3" description="2022-05-13" tags={["improvement", "bug-fix"]}>
  * Rewritten `gt downstack sync` using a different mechanism for fetching remote stack dependencies.

  * `gt downstack sync` no longer requires turning on a configuration option to use.

  * Fixed an issue in `submit` where in-progress PR title wouldn't be saved if the user cancelled while writing the body.
</Update>

<Update label="0.18.2" description="2022-05-12" tags={["improvement", "bug-fix"]}>
  * Fixed certain cases of an issue where restacking after `stack edit` and `commit create` would use an incorrect upstream. A broader fix is coming in v0.19.0.

  * Fixed an issue where after certain `downstack edit` or `upstack onto` flows, branches would be pushed to GitHub in an order that caused them to be closed prematurely.

  * Added `gt branch-prefix --reset` to turn off the user prefix for automatically generated branch names.

  * Cleaned up copy in `submit` commands.
</Update>

<Update label="0.18.1" description="2022-05-10" tags={["improvement", "bug-fix"]}>
  * `gt repo sync` and `gt repo fix` now prompt to delete closed branches in addition to merged ones.

  * Added more customization for auto-generated branch name prefixes. Check out `gt user branch-date` and `gt user branch-replacement`.

  * Config files are now written with 600 permissions instead of 644.

  * Fixed an issue where `downstack sync` would overwrite the local copy of a branch even if the user chose not to.

  * Fixed an issue where a misconfigured trunk wouldn't be brought to the user's attention.

  * Fixed an issue where Graphite would fail to parse repository owner/name.

  * Removed deprecation warning for `gt stacks` - it's been long enough.

  * Cleaned up interactive mode copy for `submit`.
</Update>

<Update label="0.18.0" description="2022-05-04" tags={["feature"]}>
  ### New functionality

  * Added an experimental command `gt downstack sync` to pull down the remote copy of a branch and its downstack dependencies from remote. This feature is gated behind a configuration by default, and we are still working on the documentation. If you would like to try it out and help us iterate on the feature, please join the #experimental channel in the Graphite community Slack server!

  * Added additional functionality to `submit` to support the experimental collaboration features. Gated by default.

  * Added additional functionality to `gt repo sync` to support the experimental collaboration features. Gated by default.

  ### New commands

  * Added a new command `gt branch edit` that runs a native `git rebase --interactive` over the commits on the current branch. This command is intended for advanced Git users who want to make use of the commit structure within a branch while working with Graphite.

  * Added a new command `gt branch show` that runs a native `git log` over the commits on the current branch. Includes a `--patch/-p` option to view the diffs.

  ### New ways to use existing commands

  * Added an `--insert` option to `gt branch create` which restacks all children of the parent of the new branch onto the new branch itself.

  * Added interactive branch selection for `gt upstack onto` (similar to `gt branch checkout`). No longer requires a positional argument.

  * `gt repo sync` now handles `--no-interactive` correctly.

  * `gt commit amend --no-edit` now fails and warns the user when there are no staged changes, just like `gt commmit create`.

  * `--no-edit` is now aliased to `-n` for `gt continue` and `gt commit amend`.

  * `gt continue` now supports `--all/-a` to stage all changes.

  * `submit --no-interactive` no longer un-publishes submitted PRs (unless `--draft` is specified).

  * `gt downstack edit` now supports an `exec/x` option to execute arbitrary shell commands in between branch restacks (based on `git rebase --interactive`).

  * `gt branch delete` now supports deleting the current branch. It checks out the parent (or trunk if Graphite cannot find a parent).

  ### Fixes

  * Fixed a bug where `submit --no-interactive` could prompt the user for reviewers.

  * Fixed a bug where `gt repo owner` would set the remote as well, breaking `sync` and resulting in having to manually edit the configuration file to get Graphite working again.

  * Fixed a bug where `submit` would fail for certain classes of branch name.

  * Fixed a bug where comments in the `gt downstack edit` file were not respected.

  * Fixed a bug where `p` as an alias for `pick` in `gt downstack edit` did not work properly.

  * Fixed a bug where `fix` could swallow a rebase exception and leave the repository in a bad state.

  * Fixed a bug where `gt branch checkout` interactive selection would fail if executed from an untracked branch.

  * Fixed a bug where `gt branch delete` could fail to delete the branch but leave it in a corrupt state.

  ### Improvements

  * Improved the speed of `gt downstack edit` and `gt upstack onto` by being smarter about when a rebase is actually necessary.

  * Improved the speed of stack validation for some commands.

  ### Under the hood

  * Added infra to backfill the SHA of branch parent in metadata globally wherever it is safe to do so to prepare for an upcoming update to the stack validation algorithm that we expect to improve performance and reduce hangs.

  * Added plenty of tests and refactored code core to many commands for stability and future extensibility.
</Update>

<Update label="0.17.11" description="2022-04-23" tags={["improvement", "bug-fix"]}>
  * Fix an issue introduced in the previous version where the async calls to fill in PR info on `submit` would not be awaited serially, resulting in a poor user experience.
</Update>

<Update label="0.17.10" description="2022-04-22" tags={["improvement", "bug-fix"]}>
  * `sync` commands no longer allow pushing to branches associated with closed/merged PRs.

  * Rename `gt branch sync` to `gt branch pr-info` as its behavior is not aligned with the other \`sync\` commands.

  * Fix some output formatting for `sync` and `submit` commands.

  * Fix an issue where pr data could be overwritten on `submit`.

  * Decreased max branch name length slightly to support an upcoming feature.

  * Start tracking SHA of branch parent in metadata, a requirement for some upcoming features.

  * This version includes some initial changes to sync branch metadata with remote, gated by a hidden flag.
</Update>

<Update label="0.17.9" description="2022-04-14" tags={["improvement", "bug-fix"]}>
  * Flipped `gt log short` view to match other log commands and `up`/`down` naming convention. `↳` `→` `↱`!

  * Graphite now asks for confirmation if the user tries to submit an empty branch.

  * Graphite now displays an info message when it creates an empty commit on a new branch.

  * The empty commit copy in the commit editor now only appears when Graphite has created an empty commit.

  * Added support for remotes not named `origin` - use the new `gt repo remote` command to set the name of your remote.

  * Added support for branch names up to GitHub's max supported length (256 bytes including `/refs/heads` gives us room for 245 bytes).

  * Allowlisted many git commands for passthrough.

  * Added autocomplete support for `gt branch delete`.

  * Changed force option on `gt branch delete` from `-D` to `-f`.

  * Cleaned up output on `gt branch delete` failure.

  * Fixed an issue where a branch could not be submitted if its name matched a file in the repository.

  * Fixed an issue where `gt repo max-branch-length` wouldn't print the configured value.

  * Added more debug information for the `--debug` option.
</Update>

<Update label="0.17.8" description="2022-04-08" tags={["improvement", "bug-fix"]}>
  * Happy Friday! This should fix many hangs that users are experiencing.
</Update>

<Update label="0.17.7" description="2022-04-08" tags={["improvement", "bug-fix"]}>
  * Graphite no longer cleans up local branches that share a name with merged branches on remote unless they have been associated with the merged PR (via a `submit` command).

  * Fix bug where PR info wasn't being synced periodically.

  * Added a new command `upstack fix`, similar to `stack fix` that only runs upstack of the current branch.

  * `commit create` and `commit amend` now internally run an `upstack fix` instead of a `` stack fix` ``

  * Fix a hang related to `git config diff.external` being set.

  * Fix autocompletions for `gt branch checkout`.
</Update>

<Update label="0.17.6" description="2022-03-29" tags={["improvement", "bug-fix"]}>
  * Support handling corrupted `.graphite_merge_conflict` files.
</Update>

<Update label="0.17.5" description="2022-03-23" tags={["improvement", "bug-fix"]}>
  * Add deprecation warnings for `gt branch next` and `gt branch prev` in favor of `gt branch up` and `gt branch down`, respectively.

  * Add `gt bu` and `gt bd` shortcuts for `gt branch up` and `gt branch down`, respectively.

  * Change `gt branch delete` shortcut to `gt bdl`.

  * Support passing through `gt stash` as `git stash`.

  * Fix bug where `fish` users couldn't add backticks to commit message using the `-m` option.

  * Silence retype errors.

  * Minor copy updates.
</Update>

<Update label="0.17.4" description="2022-02-25" tags={["improvement", "bug-fix"]}>
  * Refactored config loading to reduce race conditions.

  * Add quotes around commit message in ammend command.

  * Minor copy updates.
</Update>

<Update label="0.17.3" description="2022-02-25" tags={["improvement", "bug-fix"]}>
  * Fix bug regarding repository config file reading from repository subdirs.
</Update>

<Update label="0.17.2" description="2022-02-16" tags={["improvement", "bug-fix"]}>
  * Support numbers when generating a branch name from a commit message through `gt bc -m <message>`

  * Prompt for a commit message when autogenerating an empty commit when running `branch create` with no staged changes.
</Update>

<Update label="0.17.1" description="2022-02-15" tags={["improvement", "bug-fix"]}>
  * Support creating new branches with no staged changes, by automatically creating an empty commit.
</Update>

<Update label="0.17.0" description="2022-02-15" tags={["improvement", "bug-fix"]}>
  * Enable changing existing PRs' draft status using the `--draft` flag on submit.

  * Add a new command, `gt downstack edit` which enables interactive reordering of stack branches.

  * Update implementation of `gt stack submit` to avoid GitHub rate limitted when submitting large stacks.
</Update>

<Update label="0.16.8" description="2022-02-02" tags={["improvement", "bug-fix"]}>
  * Enable manually setting reviewers on submit with the `-r` flag.
</Update>

<Update label="0.16.7" description="2022-02-01" tags={["improvement", "bug-fix"]}>
  * Allow Graphite to run when there are untracked files.
</Update>

<Update label="0.16.6" description="2022-01-27" tags={["improvement", "bug-fix"]}>
  * Fix issue with detecting downstack/upstack branches on submit
</Update>

<Update label="0.16.5" description="2022-01-07" tags={["improvement", "bug-fix"]}>
  * Fix issue with detecting some PR templates
</Update>

<Update label="0.16.4" description="2021-12-13" tags={["improvement", "bug-fix"]}>
  * Wildcard matching for ignored branches (`gt repo ignored-branches --set`) now accepts glob-patterns

  * Option to remove a branch from ignored list (`gt repo ignored-branches --unset`)

  * Submit now supports --update-only option which will only update-existing PRs and not create new ones.

  * Bugfix: Submit to honor the --no-verify flag

  * Better logging and documentation to clarify behavior
</Update>

<Update label="0.16.3" description="2021-12-3" tags={["improvement", "bug-fix"]}>
  * Support up and down aliases for `gt branch` next/prev respectively.

  * Fix issue where `gt tips` could not be disabled.

  * Inherit shell editor preference for user from env (\$GIT\_EDITOR/\$EDITOR) and prompt user to set shell editor preference on submit if env not set.

  * Allow user to change editor preference using `gt user editor`
</Update>

<Update label="0.16.2" description="2021-10-25" tags={["improvement", "bug-fix"]}>
  * Support for `gt continue` to continue the previous Graphite command when interrupted by a rebase.
</Update>

<Update label="0.16.1" description="2021-10-14" tags={["improvement", "bug-fix"]}>
  * Fix issue with `gt repo sync` deleting metadata for existing branches.

  * Reduce merge conflicts caused by `gt commit amend`.
</Update>

<Update label="0.16.0" description="2021-10-12" tags={["improvement", "bug-fix"]}>
  * Support for branch autocomplete functionality on gt branch-related commands. Enable this functionality by running \`gt completion\` and adding the ouputted bash script to your relevant bash profile (e.g. \~/.bashrc, \~/.zshrc).

  * Added functionality to query users for feedback on the Graphite CLI.

  * Refactor the suite of gt submit commands to make them more easily cancellable; re-ordered submit to edit all PRs locally before doing any writes and cancelling mid-submit will save any previously entered data (e.g. title and body).

  * Submit also now includes a `--dry-run` flag to show the user what will be submitted in the invocation.

  * Submit queries GitHub for PRs before submitting, resolving an issue where submit would sometimes try to create a new PR though one already existed for that head branch/base branch combo on GitHub (Graphite just didn't know about it).
</Update>

<Update label="0.15.1" description="2021-10-4" tags={["improvement", "bug-fix"]}>
  * Fix `gt commit create -m` multi-word commit messages.
</Update>

<Update label="0.15.0" description="2021-10-4" tags={["improvement", "bug-fix"]}>
  * Support for `gt stack top` and `gt stack bottom`.

  * Adjusted logic for cleaning metadata in `gt repo sync`.
</Update>

<Update label="0.14.4" description="2021-10-1" tags={["improvement", "bug-fix"]}>
  * Improve performance of stack logic on repos with a high number of local branches.

  * Allow `gt commit create` to be used without `-m`, launching the system editor.

  * Infer the body of a PR from the commit message body (if it exists).

  * Add `gt repo trunk --set`.
</Update>

<Update label="0.14.3" description="2021-09-30" tags={["improvement", "bug-fix"]}>
  * Improved `gt repo sync` performance when repos have a high number of stale branches. `gt repo sync` now deletes branches more eagerly and has an optional flag to show progress (`--show-delete-progress`).

  * New command `gt repo fix` searches for common problems that cause degraded Graphite performance and suggests common remediations.
</Update>

<Update label="0.14.2" description="2021-09-29" tags={["improvement", "bug-fix"]}>
  * Tacit support for merge-based workflows; merges no longer cause exponential branching in `gt log` and hang `gt upstack onto`.

  * Fixes to recreation of debug state in `gt feedback debug-context --recreate`.
</Update>

<Update label="0.14.1" description="2021-09-27" tags={["improvement", "bug-fix"]}>
  * Assorted improvements to the `gt repo sync` merged branch deletion logic and options to fix dangling branches.

  * `gt branch parent --reset` resets Graphite's recorded parent for a branch (to undefined).

  * `gt branch sync --reset` resets Graphite's recorded PR info a branch (to undefined).
</Update>

<Update label="0.14.0" description="2021-09-16" tags={["improvement", "bug-fix"]}>
  * `gt debug-context` captures debug metadata from your repository and can send that to Screenplay to help troubleshoot issues.

  * `gt repo sync` now pulls in PR information for all local branches from GitHub to link any PRs Graphite doesn't know about/better remove already-merged branches.

  * Re-enable metadata deletion from `repo sync`.

  * Re-enable pull request base pushing from `repo sync`.

  * `gt branch create -m` now has `-a` flag to include staged changes in the commit.
</Update>

<Update label="0.13.1" description="2021-09-01" tags={["improvement", "bug-fix"]}>
  * Disable metadata deletion from `repo sync`

  * Disable pull request base pushing from `repo sync`
</Update>

<Update label="0.13.0" description="2021-08-31" tags={["improvement", "bug-fix"]}>
  * `stack submit` now checks if update is needed for each branch.

  * Support `upstack submit` and `branch submit`

  * Fixed bug which was preventing `upstack` from having the alias `us`

  * Added a command `branch rename` to rename branches and correctly update metadata.

  * Better support cancelling out of prompts.

  * Rename `stack clean` to `repo sync` and update to be able to be run from any branch.

  * Update `repo sync` to delete old branch metadata refs.

  * Update `repo sync` to update PR merge bases if necessary.

  * Support passing through commands to git which aren't supported by Graphite.

  * Add experimental command `stack test`.

  * Fix bug causing branches to show up twice in log commands.

  * Show PR and commit info in `log` command

  * Add tip advising against creating branches without commits.
</Update>

<Update label="0.12.3" description="2021-08-23" tags={["improvement", "bug-fix"]}>
  * Fix outdated copy reference to gp.

  * Print error stack trace when --debug flag is used.

  * Flag midstack untracked branches in `gt ls` output.

  * Improve submit to correctly support `gt stack submit` and `gt downstack submit`

  * Reduce unnecessary git ref calls to improve performance in large repos.

  * Support graceful handling of sigint.
</Update>

<Update label="0.12.2" description="2021-08-23" tags={["improvement", "bug-fix"]}>
  * Fix bug in `gt ls` stack traversal.
</Update>

<Update label="0.12.1" description="2021-08-23" tags={["improvement", "bug-fix"]}>
  * Fix bug resulting in always showing tips for `gt ls`.
</Update>

<Update label="0.12.0" description="2021-08-23" tags={["improvement", "bug-fix"]}>
  * Disallow branching off an ignored branch.

  * Disallow sibling branches on top of trunk branch.

  * Establish pattern of toggleable CLI tips.

  * Rewrite `gt ls` to improve speed and output formatting.

  * Optimize git ref traversal and memoization.
</Update>

<Update label="0.11.0" description="2021-08-18" tags={["improvement", "bug-fix"]}>
  * Support PR templates in `stack submit` command.

  * Update `stack submit` to support interactive title and description setting.

  * Update `stack submit` to support creating draft PRs.

  * Allow max branch length to be configured (from the default of 50).

  * Fix a crash in logging that happened in a edge case involving trailing trunk branches.

  * Hide remote branches in `log long` output.
</Update>

<Update label="0.10.0" description="2021-08-17" tags={["improvement", "bug-fix"]}>
  * Fix case where commands fail if a branch's stack parent had been deleted.

  * Fix copy across CLI to use `gt` rather than the old `gp`.

  * Add more shortcut aliases for commands such as `s` for `submit`

  * Fix copy around `repo-config` to `repo`

  * Add command `branch checkout`

  * Refactor \`stacks\` command into \`log short\`

  * Update `log` command to support `log`, `log short` and `log long`

  * Support dropping the space on double-alias shortcuts. Eg \`branch next\` = \`b n\` = \`bn\`, \`stack submit\` = \`ss\` etc

  * Throw actionable errors if two branches point at the same commit.

  * Add top level `graphite` alias such that the CLI can be called using both \`gt\` and \`graphite\`.
</Update>

<Update label="0.9.1" description="2021-08-15" tags={["improvement", "bug-fix"]}>
  * Fix `gp` alias deprecation warning for homebrew installations.
</Update>

<Update label="0.9.0" description="2021-08-15" tags={["improvement", "bug-fix"]}>
  * Rename graphite CLI alias to `gt` from `gp` per feedback.
</Update>

<Update label="0.8.2" description="2021-08-13" tags={["improvement", "bug-fix"]}>
  * Improved performance of `gp stacks` command, particularly in repositories with a large number of stale branches.

  * Changed search-space limiting settings to live at the top level and apply to both stacks and log. (`gp repo max-stacks-behind-trunk`, `gp repo max-days-behind-trunk`).
</Update>

<Update label="0.8.1" description="2021-08-10" tags={["improvement", "bug-fix"]}>
  * Improved performance of `gp log` command, particularly in repositories with a large number of stale branches.

  * Users can now set the maximum number of stacks to show behind trunk in `gp log` (`gp repo log max-stacks-behind-trunk`) as well as the maximum age of stacks to show (`gp repo log max-days-behind-trunk`).

  * `gp log` also now has `--on-trunk` and `--behind-trunk` options.

  * Improved CLI documentation and copy.
</Update>

<Update label="0.8.0" description="2021-08-07" tags={["improvement", "bug-fix"]}>
  * Autogenerated branch name date format change.

  * stack fix command now has `stack f` alias.

  * branch create command now has `branch c` alias.

  * branch create command now has `branch c` alias.

  * `stack regen` is deprecated, and is now a flag for `stack fix --regen`.

  * `stack fix` now shows an interactive prompt by default.
</Update>

<Update label="0.7.1" description="2021-08-06" tags={["improvement", "bug-fix"]}>
  * Dont zero count months when generating branch names.

  * Improve help text for amend.

  * Improve help auth print out.
</Update>

<Update label="0.7.0" description="2021-08-05" tags={["improvement", "bug-fix"]}>
  * Refactor `gp log` command, while supporting old behavior with `gp log --commits/-c`

  * Check for updates in orphaned child process, making all commands faster.

  * More helpful validation error messaging.

  * `gp branch next/prev` now support interactive choices and stepping multiple branches.

  * `gp branch create [-m]` now doesn't commit by default. It can also autogenerate branch names from commit messages.

  * Added `gp commit create -m` for creating commits and fixing upstack.

  * Added `gp commit amend -m` for amending commits and fixing upstack.

  * Added `gp user branch-prefix [--set]` reading and setting your branch prefix.

  * Added `gp branch parent [--set]` plumbing command for reading and setting a branch parent.

  * Added `gp branch children` plumbing command for reading the children of a branch.
</Update>

<Update label="0.6.3" description="2021-08-02" tags={["improvement", "bug-fix"]}>
  * Better telemetry for measuring cli performance.

  * `gp l` alias for log command.
</Update>

<Update label="0.6.2" description="2021-08-02" tags={["improvement", "bug-fix"]}>
  * `stack fix` now works for a individual stack. (Upstack inclusive for now)
</Update>

<Update label="0.6.1" description="2021-08-02" tags={["improvement", "bug-fix"]}>
  * Fix homebrew release to not include a dev dependency on `chai`.
</Update>

<Update label="0.6.0" description="2021-08-02" tags={["improvement", "bug-fix"]}>
  * Support `--no-verify` flag when running `branch create` to skip precommit hooks.

  * Validation passes when a branch points to the same commit as trunk HEAD.

  * Add `repo init` command.

  * Self heal `.graphite_repo_config` file.

  * Always track trunk branch and ignored branches.

  * Update `stack regen` to always set stack foundations to trunk.

  * Update `stack regen` such that, when from from trunk, regenerates all stacks.

  * `branch next/prev` now traverses based on Graphite's stack metadata.

  * Refactor `gp stacks` print output.
</Update>

<Update label="0.5.4" description="2021-07-30" tags={["improvement", "bug-fix"]}>
  * Update `stack regen` to operate across entire stack rather than just upstack.

  * `stack submit` infers PR title from single-commit branches.

  * Using trunk branch inference, ignore trunk parents such as trailing `prod` branches.
</Update>

<Update label="0.5.3" description="2021-07-29" tags={["improvement", "bug-fix"]}>
  * Begin infering trunk branch from `.git` config.

  * Ignore trunk parent branches during validation and other operations.
</Update>

<Update label="0.5.2" description="2021-07-28" tags={["improvement", "bug-fix"]}>
  * \`upstack onto\` can now move branches with no parent branches.

  * `validate` now passes cases where branches point to the same commit.

  * `stack fix` now prints better messaging during rebase conflicts.

  * Removed unused args from `stack submit` and `stack fix`.

  * Updated copy
</Update>

<Update label="0.5.1" description="2021-07-28" tags={["improvement", "bug-fix"]}>
  * Dont automatically create repository config file.
</Update>

<Update label="0.5.0" description="2021-07-27" tags={["improvement", "bug-fix"]}>
  * Improved `stack submit` command and promoted command out of expermental status.
</Update>

<Update label="0.4.3" description="2021-07-27" tags={["improvement", "bug-fix"]}>
  * Update all copy to match new termonology from the 4.0.0 refactor.
</Update>

<Update label="0.4.2" description="2021-07-27" tags={["improvement", "bug-fix"]}>
  * Update `branch create` command to accept optional positional argument for branch name.
</Update>

<Update label="0.4.1" description="2021-07-27" tags={["improvement", "bug-fix"]}>
  * Fix demo command and downstack string.
</Update>

<Update label="0.4.0" description="2021-07-27" tags={["improvement", "bug-fix"]}>
  * Refactor all command names into a noun-verb subcommand pattern.

  * Introduce concept of `upstack` and `downstack`.

  * Simplify documentation.

  * Minor bugfixes.
</Update>

<Update label="0.3.4" description="2021-07-25" tags={["improvement", "bug-fix"]}>
  * Fix bug in checking for uncommitted changes.
</Update>

<Update label="0.3.3" description="2021-07-25" tags={["improvement", "bug-fix"]}>
  * Self heal if branch metadata parent somehow becomes self.

  * Diff rolls back changes if commit hook fails.

  * Fix bug in metadata stack traversal used by `fix` command.

  * Restack fails fast if there are uncommitted changes.
</Update>

<Update label="0.3.2" description="2021-07-24" tags={["improvement", "bug-fix"]}>
  * Slim down size of homebrew artifact.
</Update>

<Update label="0.3.1" description="2021-07-24" tags={["improvement", "bug-fix"]}>
  * Diff now only commits staged changes.
</Update>

<Update label="0.3.0" description="2021-07-24" tags={["improvement", "bug-fix"]}>
  * Support resolving merge conflicts during a recursive restack.

  * Update `sync` command to be visable in `--help`.
</Update>

<Update label="0.2.0" description="2021-07-22" tags={["improvement", "bug-fix"]}>
  * Update unlisted `gp sync` command to support trunk argument.

  * Update unlisted `gp sync` command to prompt before deleting branches.
</Update>


# CLI Overview
Source: https://graphite-58cc94ce.mintlify.dev/docs/cli-overview

Create, stack, and submit pull requests directly from the command line.

The Graphite CLI is a tool to help you break up large engineering tasks into a series of small, incremental code changes directly from the command line. The Graphite CLI makes it easy to stay unblocked as an author, develop faster, and provide more helpful comments as a reviewer.

## Start with a guide

<CardGroup cols={2}>
  <Card href="/install-the-cli" icon="chevron-right" title="Set up the CLI">
    Install and authenticate the Graphite CLI to create and submit PRs.
  </Card>

  <Card href="/configure-cli" icon="square-terminal" title="Configure the CLI">
    Set up shell completion, custom branch naming, PR messages, and more.
  </Card>

  <Card href="/initialize-in-a-repo" icon="zap" title="Initialize Graphite in a repository">
    Learn how to initialize Graphite inside of an existing repository.
  </Card>

  <Card href="/cli-quick-start" icon="circle-play" title="Quick start">
    Learn how to author stacked pull requests with the CLI, from your first edit to merging.
  </Card>
</CardGroup>

## Tutorials

<CardGroup cols={2}>
  <Card href="/create-a-pull-request" icon="git-pull-request" title="Create a pull request">
    Learn to create a single pull request with CLI.
  </Card>

  <Card href="/create-stack" icon="layers-2" title="Create a stack">
    Stacks are what Graphite is all about - learn how to create one with the CLI.
  </Card>

  <Card href="/visualize-stack" icon="layers" title="Visualize a stack">
    If you've already created a stack with the CLI, see what it looks like locally.
  </Card>

  <Card href="/navigate-stack" icon="square-stack" title="Navigate a stack">
    Learn how to quickly move between PRs in a stack using the CLI.
  </Card>
</CardGroup>


# Quick Start
Source: https://graphite-58cc94ce.mintlify.dev/docs/cli-quick-start

Learn to create stacked pull requests with the Graphite CLI.

## Introduction

The `gt` CLI tool has 2 key purposes:

1. Simplifying git commands, especially some of the sharper edges like rebasing.

2. Enabling PR stacking, which can help you move faster and stay unblocked.

We think simplifying `git` and pull request creation is compelling on its own! However, adding pull request stacking to your workflow levels it up even further.

<Tip>
  To read about the benefits of pull request stacking, visit [stacking.dev](https://stacking.dev).
</Tip>

## The workflow

This guide will walk you through the lifecycle of stacking: creating stacks, responding to reviewer feedback up and down the stack, pulling in new changes from the main branch to open stacks, and finally merging.

Not all changes require stacks, but the same commands & concepts apply to a single PR as to a stack of 25 PRs.

The Graphite workflow can be broken down to the following steps:

<Steps>
  <Step title="Create a stack" />

  <Step title="Submit the stack" />

  <Step title="Address feedback" />

  <Step title="Merge the stack" />

  <Step title="Sync from trunk & clean up your merged branches locally" />
</Steps>

### Creating a first pull request

Creating a pull request with `gt` should feel similar to workflows you already do with GitHub:

```bash Terminal theme={null}
# Checkout the main branch using gt checkout
gt checkout main


# Make changes with your editor
echo "new code changes" >> file.js


# Create a branch with a single commit
#   - the --all flag will stage any modified files
#   - a branch will be created from the given `--message`
#   - the commit will have the given `--message`
#   - the branch will be checked out for you
gt create --all \
	--message "feat(api): Add new API method for fetching users"


# Push changes to your remote and create a new pull request
gt submit


# If you need to make any follow up changes to the PR, you can
# amend the existing commit with gt modify
echo "some more changes" >> file.js
gt modify --all


# Submit new changes
gt submit
```

### Stacking a second pull request

While you're waiting for a review on your first pull request, you can continue to build out changes by stacking a second pull request on top of the first.

A stack is **a sequence of pull requests**, each building off of its parent. Stacks enable users to break up a large engineering task into a series of small, incremental code changes, **each of which can be tested, reviewed, and merged independently**. If you aren't sure how to start breaking up your changes into stacks of PRs, check out our more detailed guide with [5 helpful frameworks for structuring a stack](/how-to-structure-your-stacks).

`gt` treats stacking as a first-class concept. Stacking new PRs, addressing reviewer feedback in any part of your stack, and making sure upstack branches stay in sync with changes downstack are all seamlessly handled for you by the core `gt` commands.

To stack more changes on top of an existing pull request:

```bash Terminal theme={null}
# Open an interactive branch picker:
#
#   - select the pull request you want to stack on top of
#   - press Enter
#
# to check the branch out.
gt checkout


# Make changes with your editor
echo "update frontend to use the API from PR 1" > \
  frontend/admin/UsersPage.tsx


# Create a second PR on top of the first one
gt create --all \
  --message "feat(frontend): Load and show a list of users"


# Push the stack, which will also create a 2nd pull request
# on top of the first one
gt submit --stack
```

Visualize your new stack locally:

```bash Terminal theme={null}
gt log short  # or run `gt ls`
```

Now that it's pushed, open the PR in Graphite:

```bash Terminal theme={null}
gt pr
```

and assign reviewers using the UI.

If you prefer assigning a reviewer at the same time as submitting, run:

```bash Terminal theme={null}
gt submit --stack --reviewers alice
```

to assign **@alice** as the reviewer on each PR in the stack.

<Tip>
  **Tip**

  You can repeat the process of checking out the top branch, making changes, and creating a new branch with `gt create` to create larger and larger PR stacks.
</Tip>

### Addressing reviewer feedback

It's likely that you'll be asked to make some changes to your stack as a result of code review. The `gt modify` command will let you edit any branch in a stack, and automatically restack all the branches above it.

Example: You have a stack of 2 PRs, and your coworker asks you to make changes on the bottom-most PR.

First, checkout the bottom PR and address the changes in your editor:

```bash Terminal theme={null}
gt checkout first_pr_in_the_stack
echo "making some edits" > a_file_my_coworker_wants_changed.js
```

Next, run `gt modify` to **amend** the last commit in this branch and **restack** all the branches above it:

```bash Terminal theme={null}
gt modify -a
```

An equivalent (but more manual) way to do this would be:

```bash Terminal theme={null}
git add a_file_my_coworker_wants_changed.js
git commit --amend --no-edit
gt restack  # restack all the branches above
```

Now the first branch has the **new changes** from your PR feedback, and the second branch stacked on top is fully **up to date** with those changes as well.

If you prefer to make a 2nd explicit commit for your PR feedback changes, you can do that with `gt modify` as well. Replace the `gt modify -a` command with:

```bash Terminal theme={null}
gt modify --commit \
	--all \
	--message "Responded to reviewer feedback"


# OR shorthand
gt modify -cam "Responded to reviewer feedback"
```

and a new commit will be created for you. All branches above the current branch will be restacked on top of this new commit.

### Pulling the latest changes from main into your stack

As you're developing new features, the `main` trunk branch will eventually get ahead of your open branches.

To update all of your open stacks with the latest changes from `main`, run:

```bash Terminal theme={null}
gt sync
```

This command will:

* Pull the latest changes into main

* Restack (rebase) all your open PRs on top of the new changes in main

* Prompt you to delete any local merged/closed branches

If any of your stacks happen to have merge conflicts as a result of restacking on the new main, gt sync will prompt you to checkout those branches, and manually run `gt restack` to fix any conflicts.

### Merging your stack

Once your stack has been reviewed and is passing CI, open the top of the stack in the Graphite UI:

```bash Terminal theme={null}
# Checkout the top PR in the stack
gt top


# Open the PR in Graphite
gt pr
```

On the PR page, merge the stack by clicking the **Merge** button.

To only merge the first part of a stack and leave the rest unmerged, navigate downstack on the PR page to the top-most PR you want to merge from, and press the **Merge** button from there.

### Sync from trunk & clean up your merged branches locally

Once you've merged your stack into `main` (or whatever your trunk branch is), run `gt sync` to get the latest changes in `main`. In addition to fetching updates, `gt sync` will:

* Automatically detect any merged/closed branches and prompt you to delete them locally.

* Rebases any branches/stacks you have locally onto the newest changes.

<Tip>
  **Tip**

  To make sure you're always working on the most up-to-date version of your base branch, make sure you're frequently running `gt sync` throughout your workflow.
</Tip>


# Graphite CLI V1 Command Names
Source: https://graphite-58cc94ce.mintlify.dev/docs/cli-v1-command-names

Discover Graphite CLI v1's revamped command names.

The Graphite CLI v1 release included a shift in the naming scheme for Graphite CLI commands. We removed the noun-verb model and shifted to a flat command naming scheme. For those of you who have been with us for a while and gotten used to the beta commands, we also introduced a **custom aliasing system** that allows you to use any command names you want. You can configure it by editing the `.graphite_aliases` file in your home directory.

**See the [Legacy alias preset](/legacy-alias-preset) subpage for a list of aliases that replicates the old command names.**

| Command name                     | Default alias | Old command name                    |
| -------------------------------- | ------------- | ----------------------------------- |
| `gt create`                      | `gt c`        | `gt branch create`                  |
| `gt modify`                      | `gt m`        | `gt commit amend`                   |
| `gt modify --commit`             | `gt m -c`     | `gt commit create`                  |
| `gt submit`                      | `gt s`        | `gt downstack submit`               |
| `gt submit --stack`              | `gt ss`       | `gt stack submit`                   |
| `gt sync`                        |               | `gt repo sync`                      |
| `gt checkout`                    | `gt co`       | `gt branch checkout`                |
| `gt log`                         | `gt l`        | `gt log`                            |
| `gt log short`                   | `gt ls`       | `gt log short`                      |
| `gt log long`                    | `gt ll`       | `gt log long`                       |
| `gt info`                        |               | `gt branch info`                    |
| `gt up`                          | `gt u`        | `gt branch up`                      |
| `gt down`                        | `gt d`        | `gt branch down`                    |
| `gt top`                         | `gt t`        | `gt branch top`                     |
| `gt bottom`                      | `gt b`        | `gt branch bottom`                  |
| `gt auth`                        |               | `gt auth`                           |
| `gt init`                        |               | `gt repo init`                      |
| `gt config`                      |               | `gt user <config>/gt repo <config>` |
| `gt move`                        |               | `gt upstack onto`                   |
| `gt reorder`                     |               | `gt downstack edit`                 |
| `gt rename`                      | `gt rn`       | `gt branch rename`                  |
| `gt delete`                      | `gt dl`       | `gt branch delete`                  |
| `gt pop`                         |               | `gt branch unbranch`                |
| `gt get`                         |               | `gt downstack get`                  |
| `gt fold`                        |               | `gt branch fold`                    |
| `gt split`                       | `gt sp`       | `gt branch split`                   |
| `gt squash`                      | `gt sq`       | `gt branch squash`                  |
| `gt restack`                     | `gt r`        | `gt <scope> restack`                |
| `gt modify --interactive-rebase` |               | `gt branch edit`                    |
| `gt track`                       | `gt tr`       | `gt stack/downstack track`          |
| `gt untrack`                     | `gt utr`      | `gt branch untrack`                 |
| `gt feedback`                    |               | `gt feedback`                       |
| `gt dash`                        |               | `gt dash`                           |
| `gt docs`                        |               | `gt docs`                           |
| `gt changelog`                   |               | `gt changelog`                      |
| `gt continue`                    | `gt cont`     | `gt continue`                       |
| `gt merge`                       | `gt mg`       | `gt downstack merge`                |
| `gt completion`                  |               | `gt completion`                     |
| `gt fish`                        |               | `gt fish`                           |


# Code Indexing
Source: https://graphite-58cc94ce.mintlify.dev/docs/code-indexing

Graphite can index your code for short periods of time to improve performance of various features.

By default, Graphite doesn't store your code. Any time that you see your code on the Graphite web app, that code is coming from **GitHub**.

This approach comes with tradeoffs: our customers often see inconsistent performance or run into rate limits. In order to provide you with a faster and more reliable experience, Graphite offers an optional (but recommended) feature called "code indexing". When enabled, Graphite maintains an index of the files in each of your synced repositories, delivering dramatically faster response times, higher availability, and eliminating rate limits versus falling back to GitHub.

## Improvements

When enabled, the code index is used to improve the following:

* [Graphite Chat](/graphite-chat): Tool call results are returned faster, more consistently, and without rate limits.
* [AI Reviews](/ai-reviews): Reviews can reference related files in the codebase to improve review quality. *(coming soon)*
* [Merge Queue](/graphite-merge-queue): Substantial improvement in the speed of merge operations. *(coming soon)*
* [PR Review Page](/review-proposed-changes): File diff views load faster and are resilient to third-party networking issues. *(coming soon)*

We intend to leverage the index to improve more parts of the Graphite platform as well!

## Enabling and Disabling

[Graphite admins](/graphite-admin) can toggle code indexing at any time from the [settings](https://app.graphite.com/settings/code-indexing).

When you **enable** the Graphite code index:

* Graphite begins to index your repositories and PRs as they are updated.

When you **disable** the Graphite code index:

* Graphite stops indexing your repositories and PRs.
* All Graphite features stop using the index.
* All code stored in the index is deleted within 30 days.

## Privacy Considerations

To understand more about the security and privacy implications of using the Graphite code index, please see [our dedicated page](/code-indexing-security).


# Code Indexing Security
Source: https://graphite-58cc94ce.mintlify.dev/docs/code-indexing-security

Graphite offers a secure code-indexing service which improves the performance of platform features. This feature is opt-in and no AI is trained on your data.

Code Indexing connects to your code repositories to dramatically improve the speed and completeness of Graphite features. You can read more about the feature [here](/code-indexing). This feature is strictly **opt-in** and **is not used to train on your data**.

We know that your source code is one of your most valuable assets, which is why we handle it with the highest level of care:

* By default, this feature is **disabled**. It must be explicitly enabled by an organization administrator.
* Neither we nor our subprocessors use your code to train any AI models.
* Your data is kept in a dedicated environment, logically isolated from all other customers.
* All data is encrypted in transit and at rest, as outlined in our commitment to data protection.

We are committed to protecting your data and privacy. Upon an administrator disabling Code Indexing through the [settings page](https://app.graphite.com/settings/code-indexing) or deleting your organization, all indexed data will be deleted within 30 days.


# Collaborate On A Stack
Source: https://graphite-58cc94ce.mintlify.dev/docs/collaborate-on-a-stack

Learn how to work on shared collaborative stacks with other Graphite users.

Learn how to work on shared collaborative stacks with other Graphite users. Stacking doesn’t have to be single-player, and it’s a great way to collaborate with teammates on a project or feature! This page talks about how to fetch remote stacks, stack on top of your co-worker’s PRs, and submit your own changes when working with others.

## Getting remote branches with gt get

`gt get` allows you to pull your coworker's stacks from remote into your local repository to see their changes on your own machine or as a starting point for collaboration.

For example, coworker A creates and submits their branch:

```bash Terminal theme={null}
gt create my_branch -m "My changes"
gt submit
```

Then, coworker B pulls the branch to their machine:

```bash Terminal theme={null}
gt get my_branch
```

This syncs all branches that `my_branch` depends on (starting from the bottom of the stack). If any of the branches already exist locally and differ from the remote version, Graphite will ask to either overwrite your local changes or rebase them on top of the remote version.

<Tip>
  `gt get` is also the recommended workflow for developers who work on more than one machine:submit draft PRs for your stack on one machine with `gt submit` and then use `gt get` from the other device.
</Tip>

## Building together

To build on top of your coworker's changes run `gt get` on the branch you want to build on top of, make your changes, and run `gt create` , exactly the same way you would to create a stack on-top of your own branch. For example, to stack some analytics changes on-top of your coworker's frontend changes:

```bash Terminal theme={null}
gt get "my-coworkers-frontend-changes"
touch analytics.js
gt create -m "add-analytics"
```

Lastly, when you're ready to, just run `gt submit` to submit your new branches to Graphite.

## Staying in sync

As you and your teammates push to your shared stack, you should both periodically run:

* `gt sync` to pull down any new changes the other has made to existing branches
* `gt get` for each net new branch the other has made
* `gt submit` to push up changes

If you encounter any conflicts during restacking, Graphite will drop you into the same conflict resolution flow that you are already familiar with from both Graphite and git.

<Note>
  `gt sync` restacks by default to keep your branches up-to-date with the latest remote. If your trunk branch has been updated, you may be prompted to resubmit changes (including rebase-only changes). If you'd like to sync without restacking, run `gt sync --no-restack`.
</Note>

## Getting a partial stack

By default, `gt get` will sync the full stack. If you'd like to pull down just part of a stack, you can run `gt get --downstack` to sync just downstack branches.

## Safely building on a coworkers stack

In `gt` version 1.7.0, the concept of "frozen" branches was introduced. A "frozen" branch will still be kept up to date with remote changes when it is synced, but will block local changes being made to it. This allows you to pull down a coworker's branch and stack on top of it without worrying about accidentally making edits to their changes.

* If `gt get` is pulling down a new branch, it will mark that branch as "frozen" by default (you can use the `--unfrozen` flag if you want to get the branch in an editable state).
* You can also use `gt freeze` and `gt unfreeze` to update the "frozen" status of a branch.
* You can see if a branch is frozen or not with the `gt info` or `gt log` command.

## Advanced: collaborating on non-Graphite branches

We strongly recommend that coworkers who wish to collaborate on a branch both use `gt` to ensure that the dependencies are managed and synced correctly as you work together.

Only branches that your coworkers have submitted with `gt` can be synced down to your local environment, as we rely on the Graphite submission to keep track of the dependency tree.

If you want to stack on top of your non-Graphite-using coworkers’ branches, the best way to do this is `git pull` and `gt track`. However, Graphite will rebase these branches on a `gt sync`, just like branches you created.


# Command Reference
Source: https://graphite-58cc94ce.mintlify.dev/docs/command-reference

This reference documents every command and flag available in Graphite’s command-line interface.

Follow the [installation guide](/install-the-cli) to set up the Graphite CLI.

## Global flags

`--help`Show help for a command.

`--allCommands`This is not printed with the global help, but if passed to `gt --help --all`, will print out the full list of command help.

`--cwd`Working directory in which to perform operations.

`--debug`Write debug output to the terminal.

`--interactive`Enable interactive features like prompts, pagers, and editors. Enabled by default. Disable with `--no-interactive`.

`--verify`Enable git hooks. Enabled by default. Disable with `--no-verify`.

`--quiet`Minimize output to the terminal. Implies `--no-interactive`.

## Available commands

### `gt abort`

Aborts the current Graphite command halted by a rebase conflict.

#### flags

`-f, --force`Do not prompt for confirmation; abort immediately.

### `gt absorb`

Amend staged changes to the relevant commits in the current stack. Relevance is calculated by checking the changes in each commit downstack from the current commit, and finding the first commit that each staged hunk (consecutive lines of changes) can be applied to deterministically. If there is no clear commit to absorb a hunk into, it will not be absorbed. Prompts for confirmation before amending the commits, and restacks the branches upstack of the current branch.

#### flags

`-a, --all`Stage all unstaged changes before absorbing. Unlike create and modify, this will not include untracked files, as file creations would never be absorbed.

`-d, --dry-run`Print which commits the hunks would be absorbed into, but do not actually absorb them.

`-f, --force`Do not prompt for confirmation; apply the hunks to the commits immediately.

`-p, --patch`Pick hunks to stage before absorbing.

### `gt add [args..]`

git add passthrough

#### arguments

`[args] (optional)`git add arguments

### `gt aliases`

Edit your command aliases.

#### flags

`--legacy`Append legacy aliases to your configuration. See [https://graphite.com/docs/legacy-alias-preset](https://graphite.com/docs/legacy-alias-preset) for more details.

`--reset`Reset your alias configuration.

### `gt auth`

Add your auth token to enable Graphite CLI to create and update your PRs on GitHub.

#### flags

`-t, --token`Auth token. Get it from: [https://app.graphite.com/activate](https://app.graphite.com/activate)

### `gt bottom`

Switch to the branch closest to trunk in the current stack.

### `gt changelog`

Show the Graphite CLI changelog.

### `gt checkout [branch]`

Switch to a branch. If no branch is provided, opens an interactive selector.

#### arguments

`[branch] (optional)`The branch to checkout.

#### flags

`-a, --all`Show branches across all configured trunks in interactive selection.

`-u, --show-untracked`Include untracked branches in interactive selection.

`-s, --stack`Only show ancestors and descendants of the current branch in interactive selection.

`-t, --trunk`Checkout the current trunk.

### `gt cherry-pick [args..]`

git cherry-pick passthrough

#### arguments

`[args] (optional)`git cherry-pick arguments

### `gt children`

Show the children of the current branch.

### `gt completion`

Set up `bash` or `zsh` tab completion.

### `gt config`

Configure the Graphite CLI.

### `gt continue`

Continues the most recent Graphite command halted by a rebase conflict.

#### flags

`-a, --all`Stage all changes before continuing.

### `gt create [name]`

Create a new branch stacked on top of the current branch and commit staged changes. If no branch name is specified, generate a branch name from the commit message. If your working directory contains no changes, an empty branch will be created. If you have any unstaged changes, you will be asked whether you'd like to stage them.

#### arguments

`[name] (optional)`The name of the new branch.

#### flags

`--ai`Automatically AI-generate the branch name and the commit message (if unset)

`-a, --all`Stage all unstaged changes before creating the branch, including to untracked files.

`-i, --insert`Insert this branch between the current branch and its child. If there are multiple children, prompts you to select which should be moved onto the new branch.

`-m, --message`Specify a commit message.

`--no-ai`Do not automatically AI-generate the branch name and the commit message. Takes precedence over --ai.

`-p, --patch`Pick hunks to stage before committing.

`-u, --update`Stage all updates to tracked files before creating the branch.

`-v, --verbose`Show unified diff between the HEAD commit and what would be committed at the bottom of the commit message template. If specified twice, show in addition the unified diff between what would be committed and the worktree files, i.e. the unstaged changes to tracked files.

### `gt dash`

Opens your Graphite dashboard.

### `gt delete [name]`

Delete a branch and its Graphite metadata (local-only). Children will be restacked onto the parent branch. If the branch is not merged or closed, prompts for confirmation. This command does not perform any action on GitHub or the remote repository. If you delete a branch with an open pull request, you will need to manually close the pull request.

#### arguments

`[name] (optional)`The name of the branch to delete. If no branch is provided, opens an interactive selector.

#### flags

`--downstack`Also delete any ancestors of the specified branch.

`-f, --force`Delete the branch even if it is not merged or closed.

`--upstack`Also delete any children of the specified branch.

### `gt demo [demoName]`

Run interactive demos in any repo to learn how to use the Graphite CLI. This will teach you how to create pull requests & stacks with Graphite.

Usage:

1. gt demo pull-request: Learn how to create a PR
2. gt demo stack: Learn how to create a stack of PRs

#### arguments

`[demoName] (optional)`Demo to run

### `gt docs`

Show the Graphite CLI docs.

### `gt down [steps]`

Switch to the parent of the current branch.

#### flags

`-n, --steps`The number of levels to traverse downstack.

### `gt feedback [message]`

Post a string directly to the maintainers' Slack so they can drown in praise, factor in your feedback, laugh at your jokes, cry at your insults, or fall victim to Slack injection attacks.

#### arguments

`[message] (optional)`Positive or constructive feedback for the Graphite team! Jokes are chill too.

#### flags

`-d, --with-debug-context`Include logs from the past 24 hours in your feedback. This can help us understand what's going on in your repo.

### `gt fish`

Set up `fish` tab completion.

### `gt fold`

Fold a branch's changes into its parent, update dependencies of descendants of the new combined branch, and restack. This is useful when you have a branch that is no longer needed and you want to combine its changes with its parent branch. This command does not perform any action on GitHub or the remote repository. If you fold a branch with an open pull request, you will need to manually close the pull request.

#### flags

`-k, --keep`Keeps the name of the current branch instead of using the name of its parent.

### `gt freeze [branch]`

Freezing a branch prevents local modifications to the branch including any restacks. You can still sync remote changes to the branch with `gt sync` or `gt get`. You can also build PRs on top of a frozen branch. Freezing can be useful when you want to stack on top of someone else's PRs without making any changes to them. This operation can be undone with `gt unfreeze`.

#### arguments

`[branch] (optional)`The branch to freeze. Defaults to the current branch.

### `gt get [branch]`

For a given branch or PR number, sync branches from trunk to the given branch from remote, prompting the user to resolve any conflicts. If the branch passed to get already exists locally, any local branches upstack of the branch are also synced; to opt out of this behavior, use the --downstack flag. Note that remote-only branches upstack of the branch are not currently synced. If no branch is provided, sync the current stack.

#### arguments

`[branch] (optional)`Branch or PR number to get from remote.

#### flags

`-d, --downstack`When syncing a branch that already exists locally, don't sync upstack branches.

`-f, --force`Overwrite all fetched branches with remote source of truth

`--restack`Restack any branches in the stack that can be restacked without conflicts (true by default; skip with --no-restack).

`-U, --unfrozen`Checkout new branches as unfrozen (allow local edits)

### `gt guide [title]`

Read extended guides on how to use the gt program.

### `gt info [branch]`

Display information about the current branch.

#### arguments

`[branch] (optional)`The branch to show info for. Defaults to the current branch.

#### flags

`-b, --body`Show the PR body, if it exists.

`-d, --diff`Show the diff between this branch and its parent. Takes precedence over patch.

`-p, --patch`Show the changes made by each commit.

`-s, --stat`Show a diffstat instead of a full diff. Modifies either --patch or --diff. If neither is passed, implies --diff.

### `gt init`

Initialize Graphite in this repository by selecting a trunk branch. Can also be used to change the trunk branch of the repository.

#### flags

`--reset`Untrack all branches.

`--trunk`The name of your trunk branch. If no name is passed, you will be prompted to select one interactively.

### `gt log [command]`

Commands that log your stacks.

Has three forms, `gt log`, `gt log short`, and `gt log long`.

* `gt log long` ignores all options and displays a graph of the commit ancestry of all branches.
* `gt log` and `gt log short` display all tracked branches and their dependency relationships.

The difference between the latter two is that `gt log` displays more information about each branch.

`gt ls` and `gt ll` are default aliases for `gt log short` and `gt log long` respectively.

#### arguments

`[command] (optional)`The format to use. If not provided, `gt log` is assumed.

#### flags

`-a, --all`Show branches across all configured trunks.

`--classic`Use the old short logging style, which runs out of screen real estate more quickly. Other options will not work in classic mode.

`-r, --reverse`Print the log upside down. Handy when you have a lot of branches!

`-u, --show-untracked`Include untracked branched in the log.

`-s, --stack`Only show ancestors and descendants of the current branch.

`-n, --steps`Only show this many levels upstack and downstack. Implies --stack.

### `gt merge`

Merge the pull requests associated with all branches from trunk to the current branch via Graphite.

#### flags

`-c, --confirm`Asks for confirmation before merging branches. Prompts for confirmation if the local branches differ from remote, regardless of the value of this flag.

`--dry-run`Reports the PRs that would be merged and terminates. No branches are merged.

### `gt modify`

Modify the current branch by amending its commit or creating a new commit. Automatically restacks descendants. If you have any unstaged changes, you will be asked whether you'd like to stage them.

#### flags

`-a, --all`Stage all changes before committing.

`-c, --commit`Create a new commit instead of amending the current commit. If this branch has no commits, this command always creates a new commit.

`-e, --edit`If passed, open an editor to edit the commit message. When creating a new commit, this flag is ignored.

`--interactive-rebase`Ignore all other flags and start a git interactive rebase on the commits in this branch.

`-m, --message`The message for the new or amended commit. If passed, no editor is opened.

`-p, --patch`Pick hunks to stage before committing.

`--reset-author`Set the author of the commit to the current user if amending.

`-u, --update`Stage all updates to tracked files before committing.

`-v, --verbose`Show unified diff between the HEAD commit and what would be committed at the bottom of the commit message template. If specified twice, show in addition the unified diff between what would be committed and the worktree files, i.e. the unstaged changes to tracked files.

### `gt move`

Rebase the current branch onto the target branch and restack all of its descendants. If no branch is passed in, opens an interactive selector.

#### flags

`-a, --all`Show branches across all configured trunks in interactive selection.

`-o, --onto`Branch to move the current branch onto.

`--source`Branch to move (defaults to current branch).

### `gt parent`

Show the parent of the current branch.

### `gt pop`

Delete the current branch but retain the state of files in the working tree.

### `gt pr [branch]`

Opens the pull request page for a branch or PR number. If no branch is passed, the current branch's PR is opened.

#### arguments

`[branch] (optional)`A branch name or PR number to open.

#### flags

`--stack`Open the stack page.

### `gt rebase [args..]`

git rebase passthrough

#### arguments

`[args] (optional)`git rebase arguments

### `gt rename [name]`

Rename a branch and update metadata referencing it. If no branch name is supplied, you will be prompted for a new branch name. Note that this removes any association to a pull request, as GitHub pull request branch names are immutable.

#### arguments

`[name] (optional)`The new name for the current branch.

#### flags

`-f, --force`Allow renaming a branch that is already associated with an open GitHub pull request.

### `gt reorder`

Reorder branches between trunk and the current branch, restacking all of their descendants. Opens an editor where you can reorder branches by moving around a line corresponding to each branch.

### `gt reset [args..]`

git reset passthrough

#### arguments

`[args] (optional)`git reset arguments

### `gt restack`

Ensure each branch in the current stack has its parent in its Git commit history, rebasing if necessary. If conflicts are encountered, you will be prompted to resolve them via an interactive Git rebase.

#### flags

`--branch`Which branch to run this command from. Defaults to the current branch.

`--downstack`Only restack this branch and its ancestors.

`--only`Only restack this branch.

`--upstack`Only restack this branch and its descendants.

### `gt restore [args..]`

git restore passthrough

#### arguments

`[args] (optional)`git restore arguments

### `gt revert [sha]`

Create a branch that reverts a commit on the trunk branch. Currently experimental.

#### arguments

`[sha]`The commit to revert.

#### flags

`-e, --edit`Edit the commit message.

### `gt split`

Split the current branch into multiple branches.

Has three forms: `gt split --by-commit`, `gt split --by-hunk`, and `gt split --by-file <pathspecs>`.

* `gt split --by-commit` slices up the commit history, allowing you to select split points between existing commits.
* `gt split --by-hunk` interactively stages changes to create new single-commit branches.
* `gt split --by-file <pathspecs>` extracts files matching the pathspecs and splits them into a new parent branch.

All forms must be run interactively except for `--by-file` which can run non-interactively.
`gt split` without options will prompt for a splitting strategy.

`gt sp` is an alias for `gt split`.

#### flags

`-c, --commit, --by-commit`Split by commit - slice up the history of this branch.

`-f, --file, --by-file`Split by file - takes a number of pathspecs and splits any matching files into a new parent branch.

`-h, --hunk, --by-hunk`Split by hunk - split into new single-commit branches.

### `gt squash`

Squash all commits in the current branch into a single commit and restack upstack branches.

#### flags

`--edit`Modify the existing commit message.

`-m, --message`The updated message for the commit.

`-n, --no-edit`Don't modify the existing commit message. Takes precedence over --edit

### `gt submit`

Idempotently force push all branches in the current stack from trunk to the current branch to GitHub, creating or updating distinct pull requests for each. Validates that branches are properly restacked before submitting, and fails if there are conflicts. Blocks force pushes to branches that overwrite branches that have changed since you last submitted or got them. Opens an interactive prompt that allows you to input pull request metadata. To change this default behavior, run `gt config` and select the `Submit settings` menu. `gt ss` is a default alias for `gt submit --stack` to also submit descendants of the current branch.

#### flags

`--ai`Automatically AI-generate title and description for all PRs. Only works when creating new PRs. If --edit, use the generated metadata as starting points.

`--always`Always push updates, even if the branch has not changed. Can be helpful for fixing an inconsistent Graphite stack view on Web/GitHub resulting from downtime/a bug.

`--branch`Which branch to run this command from. Defaults to the current branch.

`--cli`Edit PR metadata via the CLI instead of on web.

`--comment`Add a comment on the PR with the given message.

`-c, --confirm`Reports the PRs that would be submitted and asks for confirmation before pushing branches and opening/updating PRs. If either of --no-interactive or --dry-run is passed, this flag is ignored.

`-d, --draft`If set, all new PRs will be created in draft mode.

`--dry-run`Reports the PRs that would be submitted and terminates. No branches are restacked or pushed and no PRs are opened or updated.

`-e, --edit`Input metadata for all PRs interactively. If neither --edit nor --no-edit is passed, only prompts for new PRs.

`--edit-description`Input the PR description interactively. Default only prompts for new PRs. Takes precedence over --no-edit.

`--edit-title`Input the PR title interactively. Default only prompts for new PRs. Takes precedence over --no-edit.

`-f, --force`Force push: overwrites the remote branch with your local branch. Otherwise defaults to --force-with-lease.

`--ignore-out-of-sync-trunk`Perform the submit operation even if the trunk branch is out of sync with its upstream branch. This can lead to incorrect metadata being used during the submit.

`-m, --merge-when-ready`If set, marks all PRs being submitted as merge when ready, which will let them automatically merge as soon as all merge requirements are met.

`--no-ai`Don't use AI to generate any PR fields. Takes precedence over --ai.

`-n, --no-edit`Don't edit any PR fields inline. Takes precedence over --edit.

`--no-edit-description`Don't prompt for the PR description. Takes precedence over --edit-description and --edit.

`--no-edit-title`Don't prompt for the PR title. Takes precedence over --edit-title and --edit.

`-p, --publish`If set, publishes all PRs being submitted.

`--rerequest-review`Rerequest review from current reviewers.

`--restack`Restack branches before submitting. If there are conflicts, output the branch names that could not be restacked

`-r, --reviewers`If set without an argument, prompt to manually set reviewers. Alternatively, accepts a comma separated string of reviewers

`-s, --stack`Submit descendants of the current branch in addition to its ancestors.

`--target-trunk`Which trunk to open PRs against on remote. Defaults to the target trunk for the current local trunk (defined in `gt config`), or the current local trunk if no target trunk is configured.

`-t, --team-reviewers`Comma separated list of team slugs. You can either pass "slug" to this flag or "org/slug" to the reviewers flag. Will enable the --reviewers prompt if set without arguments.

`-u, --update-only`Only push branches and update PRs for branches that already have PRs open.

`-v, --view`Open the PR in your browser after submitting.

`-w, --web`Open a web browser to edit PR metadata, even if no new PRs are being created or if configured to edit PR metadata via the CLI.

### `gt sync`

Sync all branches with remote, prompting to delete any branches for PRs that have been merged or closed. Restacks all branches in your repository that can be restacked without conflicts. If trunk cannot be fast-forwarded to match remote, overwrites trunk with the remote version.

#### flags

`-a, --all`Sync branches across all configured trunks.

`-f, --force`Don't prompt for confirmation before overwriting or deleting a branch in any place where confirmation is requested.

`--restack`Restack any branches that can be restacked without conflicts (true by default; skip with --no-restack).

### `gt top`

Switch to the tip branch of the current stack. Prompts if ambiguous.

### `gt track [branch]`

Start tracking the current (or provided) branch with Graphite by selecting its parent. Can recursively track a stack of branches by specifying each branch's parent interactively. This command can also be used to fix corrupted Graphite metadata.

#### arguments

`[branch] (optional)`Branch to begin tracking. Defaults to the current branch.

#### flags

`-f, --force`Sets the parent to the most recent tracked ancestor of the branch being tracked to skip prompts. Takes precedence over --parent

`-p, --parent`The tracked branch's parent. Must be set to a tracked branch. If provided, only one branch can be tracked at a time.

### `gt trunk`

Show the trunk of the current branch.

#### flags

`--add`Add an additional trunk.

`-a, --all`Show all configured trunks.

### `gt undo`

Undo the most recent Graphite mutations.

#### flags

`-f, --force`Do not prompt for confirmation; undo the most recent command immediately.

### `gt unfreeze [branch]`

Freezing a branch prevents local modifications to the branch including any restacks. Unfreezing will enable local modifications to the branch. See `gt freeze` for more information.

#### arguments

`[branch] (optional)`The branch to unfreeze. Defaults to the current branch.

### `gt unlink [branch]`

Unlink the PR currently associated with the branch.

#### arguments

`[branch] (optional)`The branch to unlink.

### `gt untrack [branch]`

Stop tracking a branch with Graphite. If the branch has children, they will also be untracked. Default to the current branch if none is passed in.

#### arguments

`[branch] (optional)`Branch to stop tracking.

#### flags

`-f, --force`Will not prompt for confirmation before untracking a branch with children.

### `gt up [steps]`

Switch to the child of the current branch. Prompts if ambiguous.

#### flags

`-n, --steps`The number of levels to traverse upstack.

`--to`Target branch to navigate towards. When multiple children exist, selects the path leading to this branch.

### `gt upgrade`

Update your CLI to the latest stable version.


# Comparing Git And Gt
Source: https://graphite-58cc94ce.mintlify.dev/docs/comparing-git-and-gt

Learn the key differences between working with the Graphite CLI vs. vanilla git.

In this guide, you’ll learn some of the main differences between using `gt` and `git`, like fixup commits, working asynchronously, check pointing, syncing from remote, and restacking.

Once you learn more about `gt` and how it interacts with `git`, you can then re-integrate your previous `git` workflow into `gt`.

## Example of gt vs. git

Imagine you’re an engineer at a company that builds task management software (for example, Asana, Linear, or JIRA) and you want to build the ability to search across all task titles.

Let’s say this project has four parts:

1. Add an index to the task table on `title` so you can search through this field quickly

2. Add a helper function to query this table given a search query and returning tasks that match: `searchTasks(string searchQuery) -> Task[]`

3. Expose an endpoint on your webserver that allows the frontend to search for tasks

4. Query this endpoint and display results on the frontend

Here’s how this would look in `git`**:**

```sh terminal theme={null}
// Create new branch & check it out
$ git branch task_search && git checkout task_search
// Make index changes (~10 lines of code)
$ git add --all && git commit --message 'add index for searching tasks'
// Make helper function (~50 lines of code)
$ git add --all && git commit --message 'add helper function to search tasks'
// Make endpoint (~100 lines of code)
$ git add --all && git commit --message 'add endpoint to search tasks'
// Make UI (~200 lines of code)
$ git add --all && git commit --message 'addtUI to display searched tasks'
// Push changes to remote
$ git push origin task_search
```

Now you have a **branch** that implements search end to end. Next you want to get this reviewed by your teammates before it gets merged. There are a couple important issues here:

* This is a large PR! It has many lines of code changes for someone to review.

* The folks who own the UI are different from the folks who own the task table. You need multiple people on different teams to review your PR.

Here’s how this would look in `gt`:

```sh terminal theme={null}
// Make index changes (~10 lines of code)
$ gt create --all --message 'add index for searching tasks'
// Make helper function (~50 lines of code)
$ gt create --all --message 'add helper function to search tasks'
// Make endpoint (~100 lines of code)
$ gt create --all --message 'add endpoint to search tasks'
// Make UI (~200 lines of code) using aliases
$ gt create -a -m 'add UI to display searched tasks'
// Submit changes to remote
$ gt submit --stack
```

Now you have a **stack** that implements search end to end. A stack is made up of multiple branches stacked on top of each other.

Instead of creating a single PR to merge all these changes, Graphite creates four PRs for this stack (one per `gt create` command above). You can get each PR reviewed by a person who is familiar with that particular change.

This solves the two issues when using `git`: each PR with `gt` is small (and easier to review), and you can get reviews from different people for different parts of your change depending on their expertise.

## Fixup commits in gt

Continuing with the example above, let’s say you receive some comments about performance, related to the second part of your change “add helper function to search tasks”. You want to only search tasks within the last year—tasks older than that are out of scope for your search prototype.

How this looks with `git`:

```sh TERMINAL theme={null}
// Make changes to limit the helper function's search scope to ~1 year
$ git add --all // stage changes
$ git commit --fixup=<commit hash of add helper function to search tasks> // Make the fixup commit
$ git rebase --interactive --autosquash=<commit hash of add helper function to search tasks>~1 // Merge fixup commit into previous commit
```

How this looks with `gt`:

```sh TERMINAL theme={null}
$ gt checkout 'add helper function to search tasks'
// Make changes to limit the helper function's search scope to ~1 year
$ gt modify --all // Stage & amend these changes into "add helper function to search tasks"
// Push stack to remote
$ gt submit --stack
```

<Note>
  If you make changes lower down the stack, it is important to run `gt submit --stack` versus just `gt submit` because changes up the stack will not receive the new updates otherwise. This will result in the PR diff on the UI to not match what you see locally through `git show` or `gt info --diff` for any upstack PRs.
</Note>

## Working asynchronously

The reason `gt` is so powerful is because it enables working asynchronously. Because each branch in the **stack** is independent, you can keep building on top of the existing changes without worrying about growing the size of your PR and making things a worse experience for reviewers.

Let’s say you’re waiting on your above PR(s) to be reviewed, when a colleague has a great idea that rather than just allowing people to search for tasks, you should also allow them to search for user profiles in the same UI.

In `git`, you now have three options:

* Wait until `task_search` is merged into `main`, pull `main`, then create a new branch `profile_search` and repeat the earlier steps

  * This isn’t great because you now need to wait for reviews and merging before you can work on `profile_search`

* Update `task_search` with all changes required to implement `profile_search`

  * This isn’t great because now you have to further pollute the `task_search` PR which was already large, and wait for reviews from new reviewers, and so on.

* Create a new branch `profile_search` on top of `task_search`, and make changes to that.

  * This works well, until you need to change `task_search`, and run a rebase. The `gt` workflow handles this for you automatically.

In `gt`, you can simply run:

```sh terminal theme={null}
$ gt checkout 'add UI to display searched tasks'
// Make changes to implement profile search
$ gt create --all --message 'implement profile search'
$ gt submit --stack
```

Now, implementing profile search is built on top of “add UI to display searched tasks”, but it creates a new PR that is independent of all the changes below it. You can keep building on top of this stack, while all PRs lower down the stack (”downstack”) are independent of these changes up the stack (”upstack”).

## Check pointing in gt

A common use case for `git commit` is to check point yourself in the process of development. An example commit history would look something like:

1. Initialize boilerplate

2. Fix copy paste bug in boilerplate

3. Fill out functions in boilerplate

4. …

If you want to do something similar in `gt`, just use `gt create` every time you would `git commit`. However, it is important to not `gt submit` the entire stack until some organization is done, otherwise each of your intermediate check points will create PRs, making for a really poor review experience for your reviewers. Instead, once you have your changes in a good place, use `gt fold` to fold a child branch into its parent. This will allow you to create checkpoints without submitting PRs for each checkpoint.

<Tip>
  Run into any issues with `gt fold`? You can always split it back into separate branches with `gt split`.
</Tip>

## Syncing from remote, restacking, and resubmitting

While you're working on a piece of code, there is a chance that someone else touches the same code on `main`, or someone makes changes that you want to use. In `git`, to handle this you could do:

```sh terminal theme={null}
$ git checkout main
$ git pull
$ git checkout <my new branch>
$ git merge main
```

In `gt`, you would do the following instead:

```sh terminal theme={null}
$ gt sync
$ gt checkout <my new branch>
$ gt restack // This will rebase your stack onto main
```

Let’s assume you have a stack of PR#1 → PR#2 → PR#3.

`gt restack` tells Graphite to check if any rebases need to happen in order to correct your dependency list. For example, let's say you make a change lower down in the stack, in PR #1. PR #3 doesn't know about this until you do`gt restack`. So`gt restack`is telling Graphite that you have made changes on a PR that could affect its children—to check the children for any conflicts, and perform a rebase if it finds them.


# Configure The CLI
Source: https://graphite-58cc94ce.mintlify.dev/docs/configure-cli

Learn how to configure the Graphite CLI to customize and speed up your workflow.

## Set up shell completion

Graphite supports `zsh`, `bash`, and `fish` tab completion. You can run one of the following commands:

### For zsh

```bash Terminal theme={null}
gt completion >> ~/.zshrc
```

### For bash

```bash Terminal theme={null}
gt completion >> ~/.bashrc
```

or

```bash Terminal theme={null}
gt completion >> ~/.bash_profile
```

### For fish

```bash Terminal theme={null}
gt fish >> ~/.config/fish/completions/gt.fish
```

## Configuration options

Run `gt config` to open an interactive menu which lets you configure your Graphite CLI. The options are described in more detail below.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=3139dd5351544c2b66fe054e09e06e9d" data-og-width="572" width="572" data-og-height="187" height="187" data-path="images/gt-config-1-7-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=280&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=11fc09ca35b4c615ee30cdfa6fe955c2 280w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=560&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=6ab4bf8af5fbcca4334a621322658552 560w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=840&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=53fae0a8870efb26f0b224b88ec01d1f 840w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=1100&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=6999220fc1dd6ec8381d0de244a4ceb5 1100w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=1650&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=ee7a2b62ce7abe79b35277ef72409b0c 1650w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=2500&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=387242e43ef6a65fbd75566c03f0c5a0 2500w" />
</Frame>

## User-level configuration

<Note>
  User configuration is stored in `~/.config/graphite/`, [unless you have `$XDG_CONFIG_HOME` set.](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
</Note>

### Branch naming settings

If you don't specify a name for your branch when using [`gt create`](/command-reference#create-name), then Graphite will generate one for you based on the commit message.

There are several options to configure:

1. A custom prefix (for example, initials).

2. Whether or not the date is prepended to the branch.

3. Whether to allow certain characters like slashes and uppercase letters

4. The character to replace unsupported symbols (for example, whitespace and anything other than alphanumeric characters, periods, dashes, underscores, and slashes.)

### Submit settings

**Set PR metadata in CLI**

Graphite lets you prepare your PR for review in the web UI by default. This allows you to preview markdown, pull options like reviewers and labels from downstack PR's, and update all PR's in a stack at once.

Enable this setting to instead default to writing PR description in the CLI.

**PR description**

Graphite includes your GitHub PR template in the commit message by default.

Graphite can include the commit messages of your branch in the body of your PR automatically on submit. If you enable this, you can choose whether or not to also include your PR template.

If you only have a single commit on your branch, the first line of the message (its title) will not be included as this is already the default for the name of the PR.

### Rebase behavior

The `git rebase` flag `--committer-date-is-author-date` is useful if you don't want your Graphite restack operations to update the committer date of the commits in your branches. In order to have Graphite's internal rebases use this flag, you can enable this configuration.

### Empty branch settings

Specify how Graphite should handle empty branches after an operation (keep or delete).

### Default utilities

By default, Graphite uses the `git` editor for drafting PR descriptions and other flows that require editing text. You can configure a different editor.

By default, Graphite opens PR descriptions and other flows that require editing text in the `git` pager. You can configure a different pager, or disable paging entirely.

Note that just like git, Graphite sets the environment variables `LESS=FRX` and `LV=-c` if they are not already set. If something else is setting your `LESS` env var, you can use `gt user pager --set "less -FRX"` to get the recommended pager settings.

<Tip>
  You can also set the editor or pager on a per-command basis with the `GT_EDITOR` and `GT_PAGER` environment variables, respectively.
</Tip>

### Tips

Toggle on and off inline tips in the Graphite CLI.

### Yubikey

If you use a Yubikey to protect your GitHub SSH key, you may be used to Git commands reminding you to touch it. Graphite is not able to print this output directly to the CLI due to how Git calls SSH, so you can enable this configuration to be reminded when Graphite is about to run a command that requires you to touch your Yubikey.

### Update settings

You can individually enable or disable automatic updates and update prompts.

As of [version 1.7.4](/cli-changelog#1-7-4), `gt` is able to automatically update in the background. These automatic updates are disabled by default for existing `gt` installs that get updated to `1.7.4` or higher. They are enabled by default for new `gt` installs.

The configuration for automatic updates and update prompts gets set in the `~/.config/graphite/user_config` file:

```json  theme={null}
"updateAutomatically": true,
"promptForUpdates": true,
```

## Repository-level configuration

<Note>
  Repository-level configuration is stored in the `.git` folder of your repository.
</Note>

### Git remote name

Graphite defaults to pushing to and pulling from `origin`.If you have configured a different name for your remote, you can set it manually.

### GitHub repository information

Once the remote URL is set, Graphite infers the GitHub repository name and owner from the remote URL, but in cases where they are not inferred correctly, you can override them.

## Using Graphite CLI with multiple GitHub user accounts/auth tokens

<Note> Multiple profiles are supported from `gt` version `1.7.2` onwards </Note>

In your `~/.config/graphite/user_config` file you can set alternative named profiles so that each can make use of separate auth tokens:

```shell  theme={null}
{
  "alternativeProfiles": [
    {
      "name": "work_github_account",
      "authToken": "xxxx"
    },
    {
      "name": "personal_github_account",
      "authToken": "xxxx"
    }
  ]
}
```

Then set the `GRAPHITE_PROFILE` environment variable with the name of the profile you want to run `gt` commands with:

```shell  theme={null}
GRAPHITE_PROFILE=work_github_account gt sync
```

You can also name one of the profiles as "default" for it to always be used when not specifying the `GRAPHITE_PROFILE` environment variable:

```shell  theme={null}
{
  "alternativeProfiles": [
    {
      "name": "default",
      "authToken": "xxxx"
    },
    {
      "name": "personal_github_account",
      "authToken": "xxxx"
    }
  ]
}
```


# Enable Signed Commits
Source: https://graphite-58cc94ce.mintlify.dev/docs/configure-signed-commits

Learn how to enable commit signing in Graphite.

Setting up a GPG key enables Graphite to sign commits when performing remote operations on your behalf to simplify your workflow, like rebasing, and allows GitHub to mark commits as verified.

If your repo is configured in GitHub to require [commit signing](https://docs.github.com/en/authentication/managing-commit-signature-verification), you need to configure GitHub to recognize Graphite’s signed commits as well. In these cases, Graphite needs to sign the commit or GitHub will not allow the commits to be merged.

## Set up signed commits

To set up a key for signing commits, visit [https://app.graphite.com/settings/preferences](https://app.graphite.com/settings/preferences). The “Commit signing” section walks you through:

* Generating a personal private/public key pair in Graphite for signing

* Adding the public key to GitHub


# Create A Pull Request
Source: https://graphite-58cc94ce.mintlify.dev/docs/create-a-pull-request

Learn to use the Graphite CLI to create a single pull request.

This tutorial will teach you how to create a single pull request with the `gt` CLI. Your goal is to learn how your existing Git/GitHub workflow for creating pull requests maps to `gt` commands.

This tutorial intentionally avoids discussing stacked pull requests, so you can stay focused on building confidence with the basic single PR workflow.

<Note>
  Before working through this tutorial, make sure to [install & authenticate the CLI](/install-the-cli).
</Note>

## Choose a repo to work in

Pick a Git repository that already exists on your computer, and change to that directory:

```bash Terminal theme={null}
cd ~/path/to/your/repo
```

If you don’t have a repository or prefer a blank one for demo purposes, you can [create a new repository](https://github.com/new) on GitHub, git clone it locally, and cd to the folder.

If this is the first time working with `gt` in this repo, run `gt init` and select your trunk branch when prompted (usually `main` or `master`):

```bash Terminal theme={null}
gt init
```

Your repo is now configured to work with `gt` and you’re ready to start making your first pull request.

## Build your feature

For this tutorial, pretend that your team is building a new activity feed feature, and you’ve been assigned a task to build a server API endpoint that returns the current user’s activity feed items:

```bash Terminal theme={null}
GET /activity-feed


[
  { id: 1, title: "Photo uploaded", body: "Alice uploaded a photo" },
  { id: 2, title: "Comment on post", body: "Charlie commented on Bob's post" },
]
```

Your goal is to get something up with dummy data quickly, so the frontend engineers on your team can start building UI components that consume this API.

This tutorial isn’t focused on coding, so paste this command into your terminal to quickly create a file with the new API changes:

```bash Terminal theme={null}
cat << EOF > activity_feed.js
const express = require('express');
const app = express();
const port = 3000;


// Fake data for the activity feed
const activityFeed = [
  {
    id: 1000,
    title: 'New Photo Uploaded',
    body: 'Alice uploaded a new photo to her album.'
  },
  {
    id: 2000,
    title: 'Comment on Post',
    body: "Bob commented on Charlie's post."
  },
  {
    id: 13,
    title: 'Status Update',
    body: 'Charlie updated their status: "Excited about the new project!"'
  }
];


app.get('/feed', (req, res) => {
  res.json(activityFeed);
});


app.listen(port, () => {
  console.log(\`Server running on port \${port}\`);
});
EOF
```

Run `git status` and confirm that `activity_feed.js` shows up as an untracked file. At this point, you’re ready to commit your work to a new branch.

## Commit and create a branch

If you’re coming from Git/GitHub, you’re probably used to this workflow:

```bash Terminal theme={null}
# Create a new branch
git checkout -b your-feature-branch-name


# Do some coding
echo "some changes" >> a_file.js


# Stage your changes
git add a_file.js


# Commit your changes
git commit -m "feat: Add a new feature to a_file.js"
```

Because this is such a common workflow, we’ve wrapped it up in a single `gt create` command, which:

* Takes a commit message

* Creates a branch with a name based on that commit message

* Commits your changes under that same message

* Checks out the new branch

From the previous section, your repo should have an uncommitted file called `activity_feed.js`.

To commit this new file & create a new branch for it:

```bash Terminal theme={null}
gt add activity_feed.js
gt create --message "feat: Add basic activity feed API"
```

If you run `gt log short`, you should see your new branch, with an indicator that you’ve also checked the branch out:

```plain Terminal theme={null}
◉  12-26-feat_Add_basic_activity_feed_API
◯  main
```

Now that your branch is created, you’re ready to submit it for review.

<Tip>
  `gt create` takes an `--all` flag that will stage your unstaged changes for you, similar to `git commit --all`.

  Both `--all` and `--message` have short versions: `gt create -am "commit message"` works the same as `git commit --all --message "commit message"`.
</Tip>

## Submit the branch

Once your work is finished locally, the next step in the authoring workflow is to submit it for code review.

Since `gt create` already checked out your new feature branch for you, run the following command to create a new pull request:

```bash Terminal theme={null}
gt submit
```

It will prompt you with a few questions:

* Whether you want to edit the PR description now

  * If you select **yes**, it will open the PR description in your `$EDITOR` for editing.

* Whether you want a draft PR, or to publish it immediately

  * Since this is a tutorial, it’s probably best to create a **draft** PR

When `gt submit` completes, it will print out the URL of the newly created pull request. You can either directly click the URL, or run `gt pr` to quickly open the new PR in your default browser.

<Tip>
  Graphite has a streamlined, stack-aware code review interface that `gt pr` will take you to by default. However, your coworkers can still decide whether to review with Graphite or GitHub, as we 2-way sync every pull request.

  Comments & feedback from the GitHub PR interface will show up on Graphite, and vice versa!
</Tip>

## Responding to review feedback

Once your coworker reviews your new pull request, it’s possible they might have some blocking changes they’d like you to make.

A typical Git workflow might look like this:

```bash Terminal theme={null}
# Check out the branch and address the feedback
git checkout your-feature-branch
echo "respond to feedback" > file.js


# Stage + commit the changes
git add file.js
git commit -m "responded to feedback"


# Push the new changes to GitHub & update your PR
git push origin your-feature-branch
```

With `gt`, you can make this a little easier.

If you need to check out your branch, you can do it with autocomplete and/or arrow key selection by running:

```bash Terminal theme={null}
gt checkout
```

You’ll be prompted for which branch to pick, saving you the effort of copying the branch name from your pull request on GitHub.

Once you’ve made your changes and are ready to `git add && git commit`, you can run:

```bash Terminal theme={null}
gt modify
```

and your changes will be amended to the existing commit.

If you prefer to create a new commit for your changes, you can pass the `--commit` flag to `gt modify`:

```bash Terminal theme={null}
gt modify --commit --message "Responded to Alice's feedback"


# or, with short arguments:
gt modify -cm "Responded to Alice's feedback"


# or, with short command AND short arguments :)
gt m -cm "Responded to Alice's feedback"
```

Now that you’ve committed your changes, you can push them up using the same command as before:

```bash Terminal theme={null}
gt submit
```

The full workflow for updating an existing branch is:

```bash Terminal theme={null}
# Check out your branch interactively
gt checkout  # or gt co


# Make changes and amend the branch
echo "some changes" > file.js
gt modify    # or gt m


# Push the changes up
gt submit    # or gt s
```


# Create A Stack
Source: https://graphite-58cc94ce.mintlify.dev/docs/create-stack

Learn how to create stacked branches with the Graphite CLI.

## Prerequisites

To create a stack of branches with the Graphite CLI, make sure you've:

* [Installed and configured the CLI](/install-the-cli)

* [Authenticated with GitHub](/install-the-cli#install-the-cli)

* [Initialized `gt`](/initialize-in-a-repo) in a repo of your choice

## Create your first branch with the CLI

If you're familiar with the `git` workflow, creating a branch and staging/committing changes shouldn't be new to you. While using a `git`-style workflow to create branches in Graphite still works, we strongly recommend that you follow the Graphite workflow when creating and editing branches:

1. Add your changes directly on top of an existing branch. \*\*DON'T \*\*create an empty branch before doing so (we'll explain further down).

2. Stage these changes using `gt add -a` to stage all of your files, or `gt add <FILENAME>` to stage individual files

3. Create a new branch with these changes using `gt create ...`

This follows the traditional *stacked changes* workflow, treating each branch as an atomic changeset that contains (at least to start with) a single commit.

Graphite generally treats branches as if they were commits. This means that something you would break up into multiple commits in a typical `git` workflow, you would instead break up into multiple branches in Graphite (typically with one commit on each branch).

### Different ways to create a branch

Here are a few ways to create a branch containing a single commit using `gt create`:

```bash Terminal theme={null}
# navigate to the trunk branch of your repository
gt trunk


# * build part 1 of your feature *


# the following two commands create a new branch off of main with your changes and add a commit


# add all unstaged changes (same syntax as git add)
gt add -A
# create a commit on a new branch with its name inferred from your commit message
gt create
# OR specify your commit message via an option, just like git
gt create -m "part 1"
# OR you can also specify a branch name yourself
gt create making_part_1
# This works too!
gt create -m "part 1" making_part_1




# If you don't run `add`, you'll be prompted to add your changes interactively.
# You can also run `add` as part of the create command with the `-a` flag
gt create -am "part 1"


# You can make the previous command even shorter by using an alias (most common gt commands have an alias, and you can even configure your own!)
gt c -am "part 1"
```

### Configure a branch prefix

When using `gt create`, you can decide whether to pass in a branch name. A branch name is auto-generated from your commit message if a branch name isn't provided.

You can configure a prefix for `gt create` to add to all of your auto-generated branch names. See [Configure the CLI](/configure-cli) for more details.

## Stack more branches on top

Once you've created a branch with your first set of changes, you can continue to build your stack by issuing more `gt create` commands as you work.

```bash Terminal theme={null}
# * build part 2 of your feature *


# create a new branch on your stack
gt create -am "part 2"


# * build part 3 of your feature *


# create another new branch on your stack
gt create -am "part 3"
```

## Create a stack from an existing branch

If you have a large branch that you want to split up into a stack of smaller branches, you can use the `gt split` command. Learn more about [splitting a branch](/squash-fold-split).


# Edit The Branch Order In A Stack
Source: https://graphite-58cc94ce.mintlify.dev/docs/edit-branch-order

Learn how to edit the branch order in a stack using Graphite CLI commands.

## Prerequisites

You should be familiar with how to:

* [Create branches in a stack](/create-stack)

* [Visualize a stack](/visualize-stack)

* [Create and submit pull requests](/create-submit-prs)

* [Update mid-stack branches](/update-mid-stack-branches)

* [Sync changes from a remote repository](/sync-with-a-remote-repo)

## Edit the order of branches in your stack

The Graphite CLI allows you to modify the dependencies of any of your branches often with just a single command.

### gt move to modify branch ordering

`gt move` rebases the current branch and all of its recursive children (anything upstack of the current branch) onto a branch of your choice.

```bash Terminal theme={null}
# check out the branch you wish to uproot (no pun intended)
gt checkout second_branch
# run gt move with no arguments to open an interactive picker
gt move
```

Output of the previous commands:

```bash Terminal theme={null}
? Choose a new base for second_branch (autocomplete or arrow keys) ›
    ◯    another_first_branch
❯   │ ◯  first_branch
    ◯─┘  main
```

You can also run `gt move --onto <BRANCH_NAME>` if you already know the branch name of your current branch's new parent. After successfully running `gt move --onto` with `main`, you should see the following output (given that there are no merge conflicts)

```bash Terminal theme={null}
Restacked some_branch_mid_stack on main.
Restacked next_branch on some_branch_mid_stack.
```

### gt reorder to modify branch ordering

If you've created a stack of several branches and want to open an editor to do an interactive re-ordering of branches, you can use `gt reorder`. `gt reorder` opens an editor that allows you to manually copy and paste branch names into different orders. The editor will only show the branch you currently have checked out, as well as anything downstack (ancestors) of it.

```bash Terminal theme={null}
# check out the branch
gt branch checkout some_branch_mid_stack
# reorder downstack branches
gt reorder
```

Output of the previous commands (in a vim editor):

```bash Terminal theme={null}
third_branch
second_branch
first_branch
# main (trunk, shown for orientation)
#
# Stack will be rearranged on trunk to match the above order.
~
~
~
~
```

You can shuffle, add, and delete branches as necessary to produce a stack that has the dependencies you desire. For example, deleting `second_branch` in the above example yields the following output:

```bash Terminal theme={null}
first_branch does not need to be restacked on main.
Restacked third_branch on first_branch.
```

### --insert flag on create to modify branch ordering

To create an entirely new branch in the middle of a stack and automatically rebase any dependent branches, use the optional `--insert` branch when invoking the `gt create` command. See the following example:

```bash Terminal theme={null}
# check out the branch on top of which you want to create some changes
gt checkout first_branch


# * create some changes *


# stage, commit, and insert your changes with gt branch create
gt create --all --insert --message "inserted_branch"


# aliases for the previous two commands
gt co first_branch_in_the_stack
gt c -aim "creating_a_branch_in_between"
```

Output of the previous commands:

```bash Terminal theme={null}
[inserted_branch bad2ec6] inserted_branch
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 inserted_branch
Restacked second_branch on inserted_branch.
```

### Resolve merge conflicts when editing branch ordering

Under the hood, `gt move` , `gt reorder`, and `gt create --insert` perform restacks just like `gt modify` —and there is a chance you can run into merge conflicts when invoking them. If you do, you can follow the same flow as [encountering merge conflicts after creating/amending commits](/update-mid-stack-branches) to branches mid-stack.


# Evaluating Graphite
Source: https://graphite-58cc94ce.mintlify.dev/docs/evaluating-graphite

Learn more about how to evaluate if Graphite is right for your team.

Teams that use stacked pull requests deliver high quality software faster. Graphite is the integrated developer platform that helps teams on GitHub stack.

<CardGroup cols={2}>
  <Card title="Privacy & security" href="/privacy-and-security" icon="lock">
    [Learn how Graphite is committed to maintaining the highest security standards for customer data, including SOC 2 Type II compliance.](/privacy-and-security)
  </Card>

  <Card title="Pricing & plans" href="/billing-plans" icon="banknote">
    [Explore our pricing tiers, how billing is calculated, and what's included in each package.](/billing-plans)
  </Card>

  <Card title="Setting up a proof-of-concept" href="/onboarding-your-team" icon="shield">
    [Learn how teams set up Graphite trials and choose metrics to evaluate success.](/onboarding-your-team)
  </Card>

  <Card title="Evaluating tools" href="/evaluating-tools" icon="hammer">
    [See how Graphite compares to other stacking tools and learn about the tradeoffs to best suit your needs.](/evaluating-tools)
  </Card>
</CardGroup>


# Evaluating Tools For Stacking
Source: https://graphite-58cc94ce.mintlify.dev/docs/evaluating-tools

Learn about the differences between Graphite and other tools for stacking pull requests.

Graphite aims to enable a stacked-PR workflow with an industry-standard version control system (GitHub). Besides Graphite, there are other tools aiming to solve this problem as well.

## Comparing Phabricator and Graphite

You can think of a Graphite design goal as bringing the Phabricator code review and authoring experience to GitHub, such as a robust review queue and first-class support for stacking—along with some enhancements, such as bidirectional syncing with GitHub and Team Insights.

As a result of being built on GitHub, there are some differences. For example, Phabricator PRs (“diffs”) have a single state tied to the PR, while Graphite (and GitHub) PRs convey state on a per reviewer level.

Both Graphite and Phabricator encourage stacking atomic changes that are reviewed one at a time, but the tools and steps differ in some ways (the `gt` flow vs. the `arc` flow). And it’s not always straightforward to compare the Mercurial vs. `gt` workflows one-to-one. For example, in Mercurial you would commit as usual, then submit with `arc diff` / `jf submit`. In Graphite, you commit using `gt create` and `gt submit`.

Overall however Graphite offers the best features of Phabricator, along with a greatly improved, polished user experience.

## Comparing Sapling and Graphite

[Sapling](https://sapling-scm.com/) is a source control system with a CLI and review interface that sits on top of GitHub. It’s inspired by the versions of Mercurial and Phabricator used internally at Meta, and is maintained by [Meta Open Source](https://opensource.fb.com/). Graphite and Sapling provide similar CLI tools (with some differences), and a review interface optimized for diff stacking. There are some key differences between the products to consider when choosing one.

### CLI comparison

The Sapling CLI requires that you clone a new repository using `sl`, meaning you can't use familiar `git` commands. Each `sl` command is used completely in place of its equivalent `git` command.

The Graphite CLI works on any repository as long as you’ve initialized `gt` inside of it (using `gt repo init`, or invoking any other `gt` command). The `gt` CLI also utilizes Git passthrough: `gt` will pass any commands it doesn’t know through to `git` so that your regular `git` workflow remains uninterrupted.

#### Branching and commits

Sapling doesn’t have a staging area (like there is in `git`), and each branch has exactly one commit —this may look familiar and feel comfortable to those coming from a Mercurial background, but might feel restrictive to those coming from Git.

Graphite is flexible across multiple workflows in order to account for developers of all backgrounds and experiences. Depending on what you’re comfortable with, you can stage your changes, create multiple commits on a branch, continuously amend one commit and so on, all while maintaining the ability to stack and submit PRs with `gt`.

#### Commands

Sapling commands are straightforward and generally do one task each.

Graphite commands range from simple to more complex and can execute several subsequent `git` commands under the hood to try to automate some of the more repetitive parts of the workflow.

Sapling has support for commands like `undo` which Graphite doesn’t yet support.

Both Sapling and Graphite CLI tools optimize development for stacked changes, and both automatically rebase your modifications as you build your stack. In general, Sapling reflects a workflow very close and true to Mercurial’s, while Graphite is a bit more flexible and might be more accommodating for users who are starting with an established Git workflow.

### Review interface comparison

Sapling’s ReviewStack is a minimal interface that allows you to see a list of PRs on a repository along with their approval state. Graphite’s app features a “pull request inbox” that functions like an email client.

#### App features

Graphite shows the overall approval state of the PRs as well as merge conflict status, check statuses, individual reviewer statuses, and the last updated date. It includes five pre-made sections with PRs that need your review, have been approved, returned to you for changes, and so on. You can also modify and create custom sections with filters on properties like author, date published, and status.

#### Design systems

Sapling’s ReviewStack uses the GitHub design system, which may be more visually familiar for GitHub users but lacks some of the features from GitHub.

Graphite uses a unique design system and components and supports more features for writing comments and reviews.

#### Comment and review

Sapling’s comment and review experience supports GitHub's markdown rendering but does not have a way to preview your comment before submission nor does it include buttons to insert markdown tags. Sapling also doesn't support typeahead search when tagging people and teams and linking to pull requests in comments. The PR description is not editable through ReviewStack.

Graphite’s interface fully supports GitHub markdown and previews when writing and editing PR descriptions, comments and reviews. Graphite supports typeahead search when tagging teams, teammates, and pull requests in comments. You can also use the `/` shortcut to invoke your own macros, and include emojis and memes from a shared customizable meme library.

#### File uploads

Sapling's ReviewStack doesn't have support for file uploads through their interface.

Graphite supports multi-file uploads for images, videos, and other GitHub supported file formats.

#### Visualization and navigation

The UIs provided for both Sapling and Graphite make viewing stacked PRs a lot easier, with visualizations that allow you to quickly navigate between PRs in a stack, and a dropdown to view each independently submitted version of a PR.

Both seamlessly integrate with GitHub; each PR in GitHub has an equivalent page in Graphite or Sapling.

#### Additional features

Graphite’s app has a few additional features like live check status and ability to re-run checks, AI summarization, and a customizable diff view (like whitespace settings, unified vs. split views, and font settings), and keyboard shortcuts to help you create and review PRs even faster.

Graphite supports webhooks from GitHub for faster event detection without hitting rate limits/API errors. Read more about [GitHub authentication methods supported by Graphite](/authenticate-with-github-app).

### Features for fast-moving teams

Sapling does a great job of building a platform that supports the use of stacked PRs. Graphite has additional features oriented around team productivity, including team insights, a stack-aware merge queue, a Slack integration for real-time actionable notifications (including the ability to review small PRs directly from Slack), static analysis (coming soon), and reviewer assignment (coming soon). We encourage you to try out both to see what works best for you and your team.

## Get in touch

Want to know how Graphite compares to a software you're considering or currently using? Reach out to us at [support@graphite.dev](mailto:support@graphite.dev)


# External Merge Queue Integration (Beta)
Source: https://graphite-58cc94ce.mintlify.dev/docs/external-merge-queue-integration

Learn how to use Graphite with your existing external merge queue.

If you already use a separate, external merge queue offering, Graphite can integrate with that merge queue, reducing the manual work required to merge stacks of PRs.

Graphite's integration will:

* Merge PRs one-by-one by enqueueing them in your merge queue

* Automatically rebase PRs before adding them to the merge queue, as necessary

This offers a quick and seamless way to onboard your team to Graphite when you're already using an external merge queue.

## Limitations

Unlike Graphite's merge queue, external merge queues don't use stack context to optimize merges, so you won't benefit from the same performance boosts and guarantees available with the [Graphite merge queue](/graphite-merge-queue).

In particular, with external merge queues Graphite can only merge PRs one at a time: for a stack of PRs `A` ← `B` ← `C`, where `A` is the base PR

* `A` will be added to the queue

* Only when `A` is successfully merged will Graphite rebase `B` and then add `B` to the queue

* Repeat for `C`

## GitHub merge queue

### Enable the external merge queue integration

Go to *Merge queue* in the Graphite app settings page ([https://app.graphite.com/settings/merge-queue)](https://app.graphite.com/settings/merge-queue), and:

<Steps>
  <Step title="Click Add merge queue" />

  <Step title="Select the repository you want to enable it for by using the dropdown selector" />

  <Step title="Select External merge queue integration as the merge queue type" />

  <Step title="Click Next" />

  <Step title="Select Enable adding to GitHub merge queue and save your merge queue settings" />
</Steps>

To merge, click the **Merge when ready** toggle in the top right of the PR page.

When a PR is the first open PR in the stack and has **Merge when ready** active, Graphite will then add the PR to your GitHub merge queue.

## Other merge queues

**If you use a merge queue outside of the Graphite or GitHub merge queues, Graphite can be configured to add PR to your queue by applying a custom label to the PR.**

Note: if you merge PRs with your merge queue another way, such as running CLI commands or calling an API, Graphite won't be able to merge your PRs for you.

### Prerequisites

1. Ensure that a PR can be enqueued via label
2. (Recommended) Prevent the merge queue from merging into branches named `graphite-base/*`. See [Automatic rebasing](https://graphite.com/docs/merge-pull-requests#automatic-rebasing) for more information.

### Enable the external merge queue integration

Go to *Merge queue* in the Graphite app settings page ([https://app.graphite.com/settings/merge-queue)](https://app.graphite.com/settings/merge-queue), and:

<Steps>
  <Step title="Click Add merge queue" />

  <Step title="Select the repository you want to enable it for by using the dropdown selector" />

  <Step title="Select External merge queue integration as the merge queue type" />

  <Step title="Click Next to specify your merge label and save your merge queue settings" />
</Steps>

### Merging via your merge queue

Once you've completed the configuration steps above, PRs created in that repo can now be merged via your merge queue.

* **For single PRs, and base PRs in a stack:** the merge button is replaced with an "Apply merge label" button that immediately applies the merge label

* **For upstack PRs:** the merge button is replaced with an "Apply merge label when ready" button that acts as follows: for a stack of PRs `A` ← `B` ← `C`, where `A` is the base PR:

  * `A` immediately receives your repo's merge label, handing off merging to your merge queue

  * When `A` is successfully merged, Graphite rebases `B`, and upon succeeding applies your repo's merge label. If the rebase fails, Graphite informs the author as usual.

  * It repeats the process for `B`, and so forth for larger stacks.

During the merge process, the PR status for each PR will communicate if the PR is actively waiting on downstack merges, or if the merge has been handed off to your merge queue.

### (Optional) Updating your PR inbox

#### Enqueued PRs

To track enqueued PRs in your PR inbox, you can create a section with the following settings:

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2503211e-1707176385-3p-mq-pr-inbox.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=632d8b378bdbe71fae96d27b1a2badde" data-og-width="1380" width="1380" data-og-height="1215" height="1215" data-path="images/2503211e-1707176385-3p-mq-pr-inbox.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2503211e-1707176385-3p-mq-pr-inbox.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d1fa3ae92fb06db998bfe10c5aadef15 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2503211e-1707176385-3p-mq-pr-inbox.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=87d5f5770616364e28909a5c76c71b78 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2503211e-1707176385-3p-mq-pr-inbox.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=6de20b6247ef93cc1549f2ac629891f9 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2503211e-1707176385-3p-mq-pr-inbox.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c9cd0eeac07ddc0ab1734065e357d49a 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2503211e-1707176385-3p-mq-pr-inbox.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c5df21313b5c3513c3f006de0ad64968 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2503211e-1707176385-3p-mq-pr-inbox.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=66a21651a7aae087a465bf02b1e0bc08 2500w" />
</Frame>

#### Blocked PRs

Many merge queues represent merge failures by adding a label denoting that the PR is blocked. You can create a section to track these with the following settings:

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4cd0801a1964035e68f32229958df150" data-og-width="1380" width="1380" data-og-height="1298" height="1298" data-path="images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c052aaf63928a8c7de0ac65821f219e5 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=bd60429964e692123cf75c8cbf8743f5 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=402fe893d416a39265f05d2124057342 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=58375cc8efc769bd404acaadf785609d 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=dcf556378bb9646bf904c3545bbbbe83 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a3bfa94b-1707176539-3p-mq-blocked-pr-inbox.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=31cbeb80f80534323ba1d15a4f88f28f 2500w" />
</Frame>

### Troubleshooting

* **PRs getting evicted while enqueued:** once you mark a stack as ready to merge, re-stacking those PRs when they're already in your merge queue may result in your merge queue evicting them due to making changes. You may want to avoid re-stacking a PR while your merge queue is processing it.

* **Handling failed merges:** your merge queue may take actions like adding a "blocked" label on PRs that failed to merge. To re-enqueue after fixing the issues, manually remove the custom label.


# FAQs
Source: https://graphite-58cc94ce.mintlify.dev/docs/faqs

Questions? We've got answers.

Unblock yourself with our troubleshooting references. If you're ever stuck, you can reach out to us over [community Slack](https://community.graphite.com) or email [support@graphite.dev](mailto:support@graphite.dev).

<CardGroup cols={2}>
  <Card title="Onboarding FAQs" href="/onboarding-troubleshooting" icon="user-round-plus">
    [Answers to common questions when getting started with Graphite as a
    first-time user or stacker.](/onboarding-troubleshooting)
  </Card>

  <Card title="CLI troubleshooting FAQs" href="/pricing-faq" icon="terminal">
    [Tips and best practices for resolving common Graphite CLI
    issues.](/pricing-faq)
  </Card>
</CardGroup>


# Feature Requests & Bugs
Source: https://graphite-58cc94ce.mintlify.dev/docs/feature-requests-bugs

Learn how to easily share feature requests and bug reports with the Graphite team.

As a Graphite user, your feature requests and bug reports play a huge part in helping us improve the product experience. Here's how to give us your feedback:

* From the CLI, run `gt feedback {your message}`

* Share feedback from the Graphite dashboard command bar by typing `⌘` + `K` and then "feedback", or by typing `G` then `F`.

* Post in the `#ideas` or `#bug-reports` channels in the Graphite [Slack community](https://community.graphite.com)

* [Contact us via our feedback form](https://graphite.com/contact-us)

* Reach out to [support@graphite.dev](mailto:support@graphite.dev)


# Overview
Source: https://graphite-58cc94ce.mintlify.dev/docs/get-started

Learn how to create, review, and merge stacked pull requests with Graphite.

<CardGroup cols={2}>
  <Card href="/cli-quick-start" icon="rocket" title="CLI quick start">
    Get acquainted with the Graphite workflow in 5 steps.
  </Card>

  <Card href="/install-the-cli" icon="download" title="Install the CLI">
    Split large tasks into small, incremental code changes.
  </Card>

  <Card href="/ai-reviews" icon="sparkles" title="AI Reviews">
    Get immediate, actionable feedback with Graphite's codebase-aware AI code review agent.
  </Card>

  <Card href="/authenticate-with-github-app" icon="github" title="Authenticate with GitHub">
    Grant Graphite access to your GitHub organization(s).
  </Card>
</CardGroup>

***

## Key features

<CardGroup cols={2}>
  <Card href="/cli-overview" icon="terminal" title="CLI">
    Simple commands that help you spend less time wrangling with git.
  </Card>

  <Card href="/vs-code-extension" icon="code" title="VS Code extension">
    A GUI designed to make stacking visual and simple, right from your IDE.
  </Card>

  <Card href="/use-pr-inbox" icon="inbox" title="PR inbox">
    Stay up-to-date with PRs across many repos using custom filters and rules.
  </Card>

  <Card href="/insights" icon="chart-column-big" title="Insights">
    Insights

    Measure and optimize your team's developer productivity.
  </Card>
</CardGroup>

## Take a tour of Graphite

See a demo of creating, reviewing, and merging a stack of pull requests using the Graphite CLI and dashboard, as well as Graphite's interoperability with GitHub.

<Frame>
  <iframe width="750" height="360" src="https://www.youtube.com/embed/sBcd9uopLOY?si=uOngw8W4RGjl_E9p" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

<Info>
  This video references the old names for the Graphite CLI's commands. The naming scheme has changed as of V1.0.0, which was released on 2023-09-13. The legacy commands will still be functional, but the CLI will prompt you to use the new command names. We will eventually deprecate the legacy names in future versions.

  The rest of our documentation has been updated accordingly—we'll update the product tour soon!
</Info>


# Use The Graphite Merge Queue
Source: https://graphite-58cc94ce.mintlify.dev/docs/get-started-merge-queue

Learn how to use the Graphite merge queue in your repo.

Before starting, make sure the merge queue is [set up and configured](/set-up-merge-queue).

## Add a pull request to the merge queue

You can add a pull request to the Graphite merge queue from the Graphite app or by adding a label to a PR on Graphite or GitHub.

### Enqueue through the Graphite app

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/14128d4e-1683650434-queue-pull-request.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8bfb9e3ad8376a1db1b2f22a171d87f7" data-og-width="5326" width="5326" data-og-height="2094" height="2094" data-path="images/14128d4e-1683650434-queue-pull-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/14128d4e-1683650434-queue-pull-request.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=0278f6861e19bce6ba4b6f54ca9f7f28 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/14128d4e-1683650434-queue-pull-request.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=441fc43cc79b7c4a210523ef8a1f27a1 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/14128d4e-1683650434-queue-pull-request.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=be8a33e757ce5703dd1b423d0bd610e9 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/14128d4e-1683650434-queue-pull-request.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a2796c8c3503bbaa52cbe9fe2b940a08 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/14128d4e-1683650434-queue-pull-request.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a0df6bd7af655d405f5ddce9f5e9daae 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/14128d4e-1683650434-queue-pull-request.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=281256003569749a36efeea565805304 2500w" />
</Frame>

Once the Graphite merge queue is enabled on a repository, you'll still see the option to merge a pull request, but the confirmation modal will show an option to queue the PR rather than to merge it immediately. There are a few minor differences between the merge modal and the queue modal:

* You **cannot** override the merge strategy from the queue modal as you can from the merge modal. Merge strategy for the queue is set at the repository-level through your [repository settings](https://app.graphite.com/settings/repo)

* We don't support commit message/title edits from the queue modal as we do in the merge modal. For PRs merged using the squash and merge strategy, the PR title and PR description will be used for the commit message/title.

* When queuing individual PRs (not a stack), you have the option to queue the PR as a **hot-fix**. When you queue a PR as a hot-fix, your PR will automatically jump to the front of the queue. Note that it will still wait to rebase and rerun CI, but will merge next in line. Hot-fixes will be marked in the merge activity page with a small flame icon.

### Enqueue via label

Make sure you've [configured your repository](/set-up-merge-queue#enable-adding-to-the-queue-via-a-label) to enqueue PRs with a GitHub label.\
After you've created/configured a label which you want to use to indicate that a PR should be added to the queue, simply adding the label to any PR will enqueue the PR. There are a few things to note:

* If the label is added to a PR that isn't mergeable, it will toggle the PR's **merge when ready** property on and will be enqueued once mergeable

* If the label is removed from a PR, it will be removed from the queue (or merge when ready will be toggled off)

* If a PR is removed from the queue for any reason (failing checks, merge conflicts), the label will be removed

* If the label is added to a PR that is part of a stack, the label will be automatically added to all downstack PRs as well.

* If the label is removed from a PR that is part of a stack, the label will be automatically removed from all upstack PRs as well.

<Info>
  A Graphite account is required for using merge labels. If we detect a user without a Graphite account applies a merge label, it will be removed and a note will be added to the PR about this requirement.

  If a user successfully merges with a label on GitHub into the Graphite merge queue, they become a billable active user per our [pricing plans](/pricing-faq).
</Info>

## Merge activity page

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d883af35a85f3ec3d691988e80a6da5f" data-og-width="6668" width="6668" data-og-height="3388" height="3388" data-path="images/24270600-1688786414-mq-updated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e1840141197fd0dccd1719c188d9bf80 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=dc6148b96a04951903d605c6f713a0e9 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c1c78ca1688150f4ad158c36003edea6 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d6d613413ca470a5223f4f03479f013e 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e4b1490650fc4c75db680d76110e934c 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e69c8e4528c6df50a8135206b140f307 2500w" />
</Frame>

The merge activity page shows merge history for a given repository. You can select which repository you're viewing with the repository selector in the top right of the page.

#### PR details

Queued PRs display directly above the `trunk`'s merge history where you can see the PR's position in the queue, size, and estimated time to merge. Under the `...` menu, you also have the option to remove PRs (including the currently merging PR) from the queue.

#### Timeline

The timeline on the right side of the page shows the queue activity, which includes merges, hot-fixes, removals, and failures.

#### Pause the queue

In case you need to do so, you can pause the queue by clicking the `...` on the PR header and selecting `pause queue`. When the queue is paused, PRs can still be added to the queue but they **will not** be merged.


# GitHub Autolinks
Source: https://graphite-58cc94ce.mintlify.dev/docs/github-autolinks

Learn how to configure GitHub autolinks to automatically reference external resources like issue trackers in your pull requests on Graphite.

## What are GitHub Autolinks?

GitHub autolinks allow you to automatically convert text references in pull requests, issues, commit messages, and release descriptions into clickable links to external resources. This feature is particularly useful for connecting your code changes to external project management tools, issue trackers, or documentation.

When properly configured, typing a reference like `JIRA-123` or `TICKET-456` in your pull request description or comments will automatically create a hyperlink to the corresponding resource in your external system.

## How Autolinks Work on Graphite

Graphite fully supports GitHub's autolinks feature. Any autolinks you configure in your GitHub repository settings will automatically work in:

* Pull request titles and descriptions
* Pull request comments and reviews
* Commit messages
* Stack descriptions

Since Graphite maintains 2-way sync with GitHub, autolinks configured through GitHub will be rendered correctly in the Graphite interface, making it easy to navigate to related tickets, issues, or documentation while reviewing code.

## Configuration

Autolinks must be configured through your GitHub repository settings. Once configured, they will work automatically in both GitHub and Graphite.

### Prerequisites

* Repository admin permissions
* GitHub Pro, GitHub Team, GitHub Enterprise Cloud, or GitHub Enterprise Server

### Configuring Autolinks on GitHub

To set up autolinks for your repository:

1. Navigate to your repository on GitHub
2. Click **Settings** in the repository menu
3. In the left sidebar, click **Autolinks** under the "Integrations" section
4. Click **Add autolink reference**
5. Configure your autolink:
   * **Reference prefix**: A short identifier that will trigger the autolink (e.g., `JIRA-`, `TICKET-`, `DOC-`)
   * **Target URL**: The URL template with `<num>` as a placeholder for the identifier (e.g., `https://your-jira.atlassian.net/browse/JIRA-<num>`)
   * **Format**: Choose between alphanumeric or numeric identifiers
6. Click **Add autolink reference** to save

For detailed instructions, see [GitHub's official documentation on configuring autolinks](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-autolinks-to-reference-external-resources).

## Common Use Cases

### Issue Tracking Systems

Link to your project management and issue tracking tools:

**Jira**

* Prefix: `JIRA-`
* URL: `https://your-company.atlassian.net/browse/JIRA-<num>`
* Example: `JIRA-123` → Links to Jira ticket JIRA-123

**Linear**

* Prefix: `LIN-`
* URL: `https://linear.app/your-team/issue/LIN-<num>`
* Example: `LIN-456` → Links to Linear issue LIN-456

**Zendesk**

* Prefix: `TICKET-`
* URL: `https://your-company.zendesk.com/agent/tickets/<num>`
* Example: `TICKET-789` → Links to Zendesk ticket #789

### Documentation Systems

Connect to internal documentation:

**Confluence**

* Prefix: `CONF-`
* URL: `https://your-company.atlassian.net/wiki/pages/viewpage.action?pageId=<num>`
* Example: `CONF-100` → Links to Confluence page

**Notion**

* Prefix: `NOTION-`
* URL: `https://notion.so/your-workspace/<num>`
* Example: `NOTION-abc123` → Links to Notion page

### Design Systems

Link to design mockups and specifications:

**Figma**

* Prefix: `FIG-`
* URL: `https://www.figma.com/file/your-file-id/?node-id=<num>`
* Example: `FIG-250` → Links to Figma design

## Best Practices

### Choose Clear Prefixes

Use prefixes that clearly indicate the external system:

* Make them short but descriptive (2-5 characters + hyphen)
* Use uppercase for consistency
* Include a hyphen at the end (e.g., `JIRA-` not `JIRA`)

### Avoid Prefix Conflicts

GitHub doesn't allow overlapping prefixes. For example, you cannot configure both `TICK` and `TICKET` as prefixes, as `TICK` would match first.

### Document Your Autolinks

Consider documenting your team's autolink conventions in:

* Your repository's README
* Pull request templates
* Team onboarding documentation

This helps team members know which references are available and how to use them effectively.

### Use in PR Descriptions

Include relevant autolink references in your PR descriptions to provide context:

```markdown  theme={null}
## Summary
This PR implements the new authentication flow requested in JIRA-1234.

## Related Issues
- JIRA-1234: Add OAuth2 support
- DOC-567: Authentication architecture guide
- FIG-890: Login flow mockups
```

When viewing this PR in Graphite, all these references will be clickable links to the external resources.

## Limitations

* **Admin permissions required**: Only repository administrators can configure autolinks
* **No overlapping prefixes**: Reference prefixes cannot overlap with each other
* **Case sensitivity**: Autolinks are case-sensitive by default
* **Configuration location**: Autolinks must be configured through GitHub settings (not configurable directly in Graphite)
* **Alphanumeric support**: While GitHub supports both numeric and alphanumeric identifiers, some older systems may only support numeric references

## Troubleshooting

### Autolinks Not Working

If your autolinks aren't rendering correctly:

1. **Verify configuration**: Check that the autolink is properly configured in your GitHub repository settings
2. **Check permissions**: Ensure you have admin access to configure autolinks
3. **Verify prefix**: Confirm you're using the exact prefix including any hyphens or special characters
4. **Check plan**: Autolinks require GitHub Pro or higher
5. **Clear cache**: Try refreshing the page or clearing your browser cache

### Links Not Opening Correctly

If autolinks are rendering but pointing to the wrong location:

1. **Verify URL template**: Double-check that your target URL includes `<num>` as the placeholder
2. **Test the URL**: Manually construct a URL with a test identifier to verify it works
3. **Check identifier format**: Ensure you've selected the correct format (numeric vs. alphanumeric)


# Configure GitHub Repository Settings
Source: https://graphite-58cc94ce.mintlify.dev/docs/github-configuration-guidelines

Learn how to configure your repository settings on GitHub for the best experience stacking with Graphite.

## GitHub repository settings

**Limit how many branches and tags can be updated in a single push**: `Disabled` **(Required)**

* This is a new GitHub setting that limits the number of branches that can be pushed atomically

* The Graphite CLI pushes all branches in your stack (and potentially a temporary base branch for each) atomically to ensure accurate behavior for PR history and code owner protections. A limit on the number of branches that can be pushed will prevent `gt submit` for stacks above a certain size.

* Alternatively, you can set the number to a very high value, but stack sizes will be limited for Graphite users in your repository (i.e. setting the limit to 30 will limit stack sizes to 15).

**Automatically delete head branches**: `Enabled` **(Highly recommended)**

* This helps prevent mistakes when merging PRs in a stack.

* For example, if you have a stack of PRs (A ← B, where A is the base PR), when you merge A with this setting on, GitHub automatically changes the target branch of B from A to `main`. However, when this setting is off, then merging A does not change the target branch of B: you must first manually restack—otherwise merging B won't work as intended.

## Branch protection rules

Branch protection rules allow you to set requirements for changes being made to specified branches on GitHub.

These rules can be useful to ensure that code changes are passing tests, and get the right approval from the right people. The recommendations are meant internally (that is, not for open source repositories with external contributors) for fast-moving companies to balance security and efficiency.

<Note>
  Graphite projects branch protection rules from the base of the stack (the branch that everything is merging into).
</Note>

### Required settings

The following branch protection rule settings are required for Graphite. Without these, Graphite's automatic management of stacked PRs may result in unexpected behavior.

**Dismiss stale pull request approvals when new commits are pushed:** `Disabled`

* As part of the merge process, Graphite may rebase a PR causing new commits to be pushed. If those changes cause approvals to be dismissed, it can lead to merge failures.

* If you need non-rebase changes to be dismissed, we created an open-source GitHub Action that is a drop-in replacement for this rule. You can find it on the GitHub Actions marketplace here: [https://github.com/marketplace/actions/dismiss-stale-approvals](https://github.com/marketplace/actions/dismiss-stale-approvals)

**Require approval of the most recent reviewable push**: `Disabled`

* As part of the merge process for a stack of PRs, Graphite changes the target branch of PRs before merging. Since this counts as a reviewable push, it can lead to merge failures.

**Require signed commits**: action needed if `Enabled`

* If you have this enabled, each engineer should set up their [signing key in Graphite](/configure-signed-commits).

**Require merge queue**: `Disabled`

* The GitHub merge queue does not understand stacks and can end up merging PRs out of order. We recommend using the [Graphite Merge Queue](/graphite-merge-queue), which is optimized for merging stacks.

**Require deployments to succeed before merging**: `Disabled`

* Graphite does not currently support deployment checks.

### Recommended settings

The following are branch protection rules that we've found to work best for teams balancing velocity with safety. While Graphite does not require these settings, you may find these useful alongside Graphite's recommended workflow of small, frequent PRs.

**Restrict who can dismiss pull request reviews**: `Disabled`

* There are many cases where a pull request author can become blocked by a previous review. For example, if a reviewer requests changes to a pull request and then goes on vacation, the author is now blocked on merging that pull request even after making the appropriate changes because the “Changes requested” review is blocking the merge. An author might also want to dismiss a previous approval if they’ve made significant changes to the code since the original review.

**Require a pull request before merging**: `Enabled`

* It's standard practice to require changes to have pull requests for any changes you plan to merge. This ensures some visibility for changes that are being made.

**Require approvals**: `Enabled`

* Requiring approvals ensures that there is always someone else to sign off on the changes before they are merged.

**Recommended number of approvals needed**: `1`

* It's easier to stay unblocked by only requiring one approval. This helps make it clear to any reviewer that their approval will completely unblock the pull request for merge. It also removes the undue burden for engineers to review. If the author decides they want additional reviews they can always tag specific reviewers.

**Require status checks to pass before merging**: `Enabled`

* We recommend that you turn this on and set important CI tests as “required” to ensure that they are passing before a pull request is merged. If you have this branch protection rule turned on you can still have a mix of required and not required status checks—only failed required status checks will block a pull request merge. If you have a flaky test that is incorrectly returning a failed status, you can also leave it as not-required and it won’t block merges. For required status checks, you can select an app as the expected source of status state changes.

**Require conversation resolution before merging**: `Enabled`

* This branch protection rule is meant to ensure that all conversation threads have been read and acknowledged by the author. Sometimes, the pull request gets updated in a way in which GitHub can no longer tie an older conversation thread with the latest changes. In these cases GitHub will not display the conversation thread in-line in the code. This makes it difficult for authors to find and resolve old conversation threads that may no longer apply to the latest version of the pull request.

**Require linear history**: `Enabled`

* This setting prevents people from pushing merge commits to the protected branch. This will require them to merge pull requests using the “squash and merge” or “rebase and merge” options. Therefore, in order to enable this branch protection rule you must first enable at least one of these merge strategy options. Ensuring linear history will make it easier to diagnose issues introduced by changes and also make it easier to reverse those changes.

**Include administrators**: `Disabled`

* There might be unforeseen circumstances where an admin needs to bypass one or more branch protection rules above. In order to merge pull requests that are missing requirements, admins need to check a box acknowledging that they are bypassing requirements. Our recommendation is that anyone that you designate as an administrator should be trusted to use this only when appropriate.

## Rulesets

If you use GitHub rulesets instead of branch protection rules, we recommend the equivalent configurations as above. Make sure to update any rulesets that may apply to your Graphite-enabled repo.

Please note that admin merge is not currently supported on repositories using rulesets.

## GitHub Actions

We recommend the following triggers for Github Actions:

```yaml  theme={null}
on:
  pull_request:
    types: [opened, synchronize, reopened]
  push:
    branches: [main]
```

We do not recommend triggering CI on the pull\_request type `edited`. This action is triggered when metadata about the PR is changed, not the PR itself (that would be `synchronize`). The `edited` event triggers a CI run when the PR below a given PR is merged—as the change of the base branch from the downstack PR to trunk is considered an “edit”.

We also recommend [updating "concurrency" to prevent multiple concurrent CI runs](/troubleshooting#why-are-my-actions-running-twice) on the same pull request.


# GitHub Enterprise Server
Source: https://graphite-58cc94ce.mintlify.dev/docs/github-enterprise-server

Learn how Graphite Enterprise customers can use Graphite with a GitHub Enterpise Server instance.

By default, Graphite connects to GitHub Cloud seamlessly - including [GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-server@3.12/admin/overview/setting-up-a-trial-of-github-enterprise-cloud). Some companies chose to self-host their GitHub servers however, in an offering formally known as [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@3.12/admin/overview/about-github-enterprise-server).

## Does Graphite support connecting to a self-hosted GitHub server?

Graphite Enterprise customers can use Graphite with a self-hosted GitHub Enterprise Server instance. We are able to connect through a combination of stable IP addresses and an IP allow list in the user's VPC. There is currently no way to self-serve connecting Graphite to one's self-hosted GitHub server. If you are interested in adopting Graphite at your company and do not use GitHub Cloud, [please reach out to our support team](https://graphite.com/contact-us) for help integrating. Note: we only support this pattern of integration for Enterprise customers.

## How can I tell if my company is self-hosting GitHub?

If you are uncertain whether your team uses a self-hosted GitHub server, try browsing to a company pull request and inspecting your URL. If the URL matches the pattern `https://github.com/<org>/<repo>/pull/<number>`, then you are using a standard cloud-hosted version of GitHub. However, if the URL matches a custom domain that does not include the host `github.com`, then it's likely your company is self-hosting GitHub Enterprise Server.

<Note>
  Most modern companies choose to run on GitHub Cloud. If your company does not have specific important reasons to self-host such as extreme security concerns, we strongly recommend folks chose to host on GitHub Cloud, regardless of their use of Graphite.
</Note>

## Does Graphite offer a self-hosted form of Graphite itself?

No. There is no self-hosted deployment of Graphite's service available for a user to run in their own cloud. It's possible that we may consider such an offering in the future, but there are no plans in the works at the moment.


# User permissions
Source: https://graphite-58cc94ce.mintlify.dev/docs/graphite-admin

Learn how to manage users and billing information for your organization as a Graphite admin.

Team admins can manage billing, add or remove seats, and view or download invoices from *Settings* > [*Billing*](https://app.graphite.com/settings/billing). Team admins can also promote other members of the team to the admin role or restrict their access to read-only mode.

## Becoming a Graphite admin

* If you have admin or owner privileges in GitHub, you are automatically an admin for that organization in Graphite.

* If you create a team in Graphite, you become a Graphite admin for that team.

* If you enter payment details in Graphite, you become a Graphite admin for that team.

* If another Graphite admin promotes you to admin, you become an admin for the team.

<Note>
  Being a Graphite admin does not grant you additional privileges in GitHub.
</Note>

## Manage users

Graphite admins can manage Graphite users in their plan from *Settings* > [*Billing*](https://app.graphite.com/settings/billing) in the Graphite app.

* To add a member to your team, click `Invite your teammates`; once they accept the invitation, they will appear in your team membership list.

* Edit a team member's role by selecting either "Admin" or "Member" next to their name.

  * Graphite admins can make anyone in their organization a Graphite admin (even if they're not an owner in GitHub).

  * Graphite admins can change Graphite admins (who aren't GitHub owners) to "Member" status. This means GitHub owners are always Graphite admins (and this is immutable).

* To remove a member from your team, click the `...` icon next to their name and select `Remove from team`.

* To restrict a team member's access to read-only mode, click the `...` icon next to their name and select `Restrict access`. Admins can be in read-only mode and retain their admin privileges (e.g., manage billing info).

## Manage billing

Graphite subscriptions are managed through the Stripe billing portal, found at *Settings* > [*Billing*](https://app.graphite.com/settings/billing) > *Manage plan*. Anyone in your org can pay through the billing portal, and the person who manages Graphite payments for your org can update the previous payment method.


# Graphite Chat
Source: https://graphite-58cc94ce.mintlify.dev/docs/graphite-chat

Chat with an AI-powered conversational assistant for pull request review and collaboration

Chat lets you interact with Graphite Agent directly on the pull request review page. Graphite Agent is an AI assistant that helps you understand code changes, get instant feedback, and make edits directly from the chat interface without leaving your review workflow.

<Note>
  The Graphite Chat panel is found on the right side of your PR review page.
  Simply type your question or request to get started.
</Note>

## What you can do with Graphite Chat

### Get PR summaries and context

Ask Graphite Agent to explain what changed in a pull request, highlight potential issues, or provide context about specific code sections. Highlight specific lines in your PR diff to ask targeted questions about that code.

* *"Summarize the changes in this PR"*
* *"What are the main issues I should focus on?"*
* *"Explain what this function does"*
* *"What should I pay attention to while reviewing this?"*

### Make direct code edits

Graphite Agent proposes specific fixes that you can apply with one click without leaving the review page.

* *"Fix the type error on line 42"*
* *"Add error handling to this function"*
* *"Optimize this database query"*
* *"Does this code have tests? If not, write them"*

### Search across your codebase

Find related files, understand dependencies, and get context from other PRs without switching tabs. Graphite has full awareness of your entire codebase and PR history.

* *"Where else is this API endpoint used?"*
* *"Show me similar implementations in the codebase"*
* *"How does this relate to PR #123?"*
* *"Does this follow our existing patterns?"*

### Address reviewer feedback

Get help understanding and implementing feedback from your teammates and reviewers.

* *"How should I address this comment?"*
* *"What are the tradeoffs of the approach my teammate suggested?"*
* *"Help me implement the changes requested in this review"*

### Debug CI failures

Diagnose and resolve failing checks directly from your PR page with full context from your CI results.

* *"Fix failing checks"*
* *"Why are the tests failing?"*
* *"How can I run this locally?"*

## How it works

Graphite Agent uses AI to analyze your code changes and provide contextual assistance. Unlike generic AI tools, Graphite has full awareness of your codebase, PR stack, CI failures, reviewer comments, and team coding patterns.

**What makes it different:**

* **Fully embedded**: Ask questions, get suggestions, apply edits, and commit without leaving your PR
* **Codebase-aware**: Understands your full codebase history, entire PR stack, and team conventions
* **Interactive editing**: Preview and apply changes directly to your PR with the built-in editor
* **Works for everyone**: Designed for both reviewers seeking context and authors making updates

<Tip>
  All edits made with Graphite Chat are tracked in version control and can be
  reviewed like any other change.
</Tip>

## Editor

When Graphite suggests code changes, you can preview them in context before applying:

1. Click to open the **Editor**
2. Review suggested changes alongside your existing code
3. Make additional tweaks if needed
4. Apply changes directly to your PR
5. Commit and merge without switching to your IDE

## Privacy and security

Graphite Chat processes only the necessary code and metadata from your pull requests to provide contextual assistance. Your data is:

* **Not used for training**: Strict agreements prevent AI providers from training on your code
* **Minimally exposed**: Only relevant PR content is sent for analysis
* **Securely handled**: Protected by Graphite's enterprise security standards

*Graphite Chat is designed with the security of your data in mind. You can find more details in our [AI security and privacy](/ai-privacy-and-security) page.*


# Graphite for Startups
Source: https://graphite-58cc94ce.mintlify.dev/docs/graphite-for-startups

For companies looking to grow with Graphite.

The Startup program is for early stage startups. If it sounds like you may be eligible, you can apply by reaching out to [billing@graphite.com](mailto:billing@graphite.com) with the following information:

* Company name
* Domain name
* Total GitHub collaborators (inclusive of all roles)
* Fundraising rounds (pre-seed, seed, series A, Series B, etc.)

### What is offered in the startup program?

If you’re approved for the startup program, you’ll receive a \$1,500 credit and be put on the **Team** plan. **The credits are valid for 12 months, or until the credits are used.** These credits are only applicable for the **Team** plan, and cannot be used for the **Starter** plan.

After your credits expire (or are used up), you’ll remain on the Team plan at full price. You can read more about the features offered under the team plan in our pricing docs [here](/billing-plans) or on our pricing page [here](https://graphite.com/pricing).

### **Will I have to pay for Graphite if I use the Startup program?**

Yes. The Startup program is a one-time credit of \$1,500 that’s valid for 12 months, or until the credit is used. Once the credits are depleted, you’ll need to use Graphite through one of our paid plan options.

## **Graphite for open source**

If you are working on a free open source community-led project, you may qualify for a free Team plan. Reach out to [billing@graphite.com](mailto:billing@graphite.com) to find out if you’re eligible. Please include:

* A link to the GitHub org
* A link to the website
* A brief description of the project


# Merge Queue
Source: https://graphite-58cc94ce.mintlify.dev/docs/graphite-merge-queue

Learn how Graphite's merge queue can help your team merge stacks faster and reduce merge conflicts.

A merge queue prevents semantic merge conflicts by automating the rebase process during merge and ensures that the `trunk` branch stays “green"—helping development teams move faster while preventing breakages.

The Graphite Merge Queue is the only merge queue that is stack-aware.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d883af35a85f3ec3d691988e80a6da5f" data-og-width="6668" width="6668" data-og-height="3388" height="3388" data-path="images/24270600-1688786414-mq-updated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e1840141197fd0dccd1719c188d9bf80 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=dc6148b96a04951903d605c6f713a0e9 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c1c78ca1688150f4ad158c36003edea6 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d6d613413ca470a5223f4f03479f013e 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e4b1490650fc4c75db680d76110e934c 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/24270600-1688786414-mq-updated.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e69c8e4528c6df50a8135206b140f307 2500w" />
</Frame>

<Note>
  Ready to start using the Graphite Merge Queue? See [Set up the Graphite merge queue](/set-up-merge-queue).
</Note>

## Why Graphite's merge queue?

You would likely benefit from a merge queue if:

* Your `trunk` branch is frequently broken

* You're consistently slowed down from rebasing changes

* You have the combined issue of long-running checks with a high PR merge rate

Traditional merge queues provide many benefits, but they can also slow teams down by enforcing the ordering of commits and validating those commits in sequence—likely reducing the speed at which merges land.

The Graphite Merge Queue is **stack-aware**, providing opportunities for faster concurrent/batched merges and optimizing the order in which PRs are merged. So if the stack is added to the queue together, the merge queue can process and validate the entire stack in parallel. No need for CI to run again since we have already validated the CI against that exact change (this is also known as fast-forward merge, as described below).

Beyond stack awareness, the Graphite Merge Queue can be configured with further [optimizations](/merge-queue-optimizations) to both increase speed and reduce CI cost.

See our [blog post](https://graphite.com/blog/what-is-a-merge-queue) to learn more about the benefits of merge queues.

### Supported merge strategies

**Rebase:** rebase your changes on top of your trunk with commits unchanged (equivalent to GitHub's rebase and merge)

**Squash:** rebase your changes on top of your trunk with each PR squashed to a single commit (equivalent to GitHub's squash and merge)

**Fast-forward merge:** you can opt to enable "fast-forward merge" on either of the above strategies in order to process stacked PRs in parallel (a Graphite-only setting).

### How the Graphite merge queue interacts with GitHub

In your repository settings, you have the option to enforce the Graphite merge queue. If it isn't enforced, users will be able to merge PRs through GitHub directly (bypassing the merge queue entirely). Enforcing the Graphite merge queue requires some configuration on GitHub's side, namely setting up the correct branch protection rules and authorizing with Graphite's GitHub App. Read more about advanced Graphite merge queue [settings](/set-up-merge-queue).

<Warning>
  The Graphite merge queue is not compatible with GitHub's merge queue. If you want to use the Graphite merge queue and you're currently using GitHub's, you must disable it for your repository before continuing. Instructions on using Graphite with the GitHub merge queue can be found [here](/external-merge-queue-integration).
</Warning>

When a PR is added to the Graphite merge queue, we leave comments on your GitHub PR in three instances: when the PR is added to the queue, when it is merged through the queue, and when it fails/is removed from the queue.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=fd1ecd1ef2fd92495ad06989b33b0c44" data-og-width="1856" width="1856" data-og-height="330" height="330" data-path="images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=035685f4f860f2eb889dd1db12dc3bdd 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b50e9e80ebbc42744f5e6becf91c8187 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=596525218f2481241777e8e78de7fa72 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5e7e2ee2868c3a1c6136ae75f0783d9e 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4f52db20aad0b9b72dc5e74e793489fa 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b4832b39-1683658248-screenshot-2023-05-09-at-2-50-43-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8fa25dfc85cc25380691819d0069b28d 2500w" />
</Frame>

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=6e835051adb137559e660b48f6f6b419" data-og-width="1852" width="1852" data-og-height="326" height="326" data-path="images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ae22bb8566f8d4120a56b6bc3de498bd 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a182f6cac684a47192d1cd8ce0548aa5 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=fe287c3de44c2af48c5cbafd735d14f1 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=3318acba90ffc2e36f8fe95fafaa581e 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=fd3a8c41f3156170cdf6da014d5672f5 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/41c7ae08-1683658272-screenshot-2023-05-09-at-2-51-08-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b2379e7f92647ca0bad5f76a5879c6e9 2500w" />
</Frame>

## External merge queue integration

If you already use a separate external merge queue offering, Graphite's external merge queue integration simplifies the merging experience. While it doesn't experience the same stack-aware optimizations as Graphite's merge queue, it can be a quick way to ramp-up your team. See [external merge queue integration](/external-merge-queue-integration) for more info.


# GT MCP
Source: https://graphite-58cc94ce.mintlify.dev/docs/gt-mcp

Use the Graphite CLI with AI agents through Model Context Protocol

<Note>
  GT MCP is currently in beta and some workflows may not be fully supported.
</Note>

## Overview

GT MCP allows AI agents to automatically create stacked PRs, breaking down large AI-generated changes into smaller, reviewable stacked pull requests.

* With large AI-generated diffs, stacking is more essential than ever. Just like reviewing large human PRs, reviewing massive AI-generated diffs can be overwhelming, and makes it hard to understand what changes your agent has made.
* Stacking breaks AI output into clear, sequential chunks, so you can understand what's changing and why—earlier, faster, and in order. It helps your agent reason through changes chronologically, validating each step as it goes.

## Installation

GT MCP is built into the Graphite CLI. Update your CLI version to 1.6.7 to get access:

**Homebrew**

```bash  theme={null}
brew update && brew upgrade withgraphite/tap/graphite
```

**npm**

```bash  theme={null}
npm install -g @withgraphite/graphite-cli@stable
```

## Setup

### Claude Code

```bash Terminal theme={null}
claude mcp add graphite gt mcp
```

### Cursor IDE

Open Cursor Settings > Tools & Integrations > Add Custom MCP

```json  theme={null}
{
  "mcpServers": {
    "graphite": {
      "command": "gt",
      "args": ["mcp"]
    }
  }
}
```


# How To Structure A Stack
Source: https://graphite-58cc94ce.mintlify.dev/docs/how-to-structure-your-stacks

Five helpful frameworks for breaking up large changes into stacked PRs.

[Stacking](https://www.stacking.dev/) helps you break up large changes into small, independent PRs that can be easily reviewed and merged, but how do you actually split up a feature and start "thinking in stacks" as you build? Learning how to architect your stacks effectively will both help you derive the largest efficiency gains from the workflow and perhaps even give you a better way of thinking about building large features. This doc outlines 5 classic frameworks for structuring stacks of PRs - we use nearly all of them here at Graphite and we encourage you to add them all to your toolbox as you get comfortable with stacking!

## Before you start stacking

Before you start doing any stacking, consider your repository’s architecture. How is your code structured? What are the different functional components of your codebase?

For example, a common layout for simple web apps might be to split the code into a[layered architecture](https://en.wikipedia.org/wiki/Multitier_architecture), i.e. a database layer, a backend service, and a frontend service.

Once you note the different functional components your codebase is comprised of, think about how those components interact - there will typically be some sort of dependency graph. In the simple layered architecture, you'd need to first add support for a new feature to the database and backend layers before adding it to the frontend.

Remember that each PR in a stack should be easy to understand and review independently - having a good understanding of the architecture of your codebase will help you follow this principle in your stacks.

With that in mind, here are five helpful frameworks for splitting large code changes up into stacks.

## Functional component stacks

The most straightforward way to structure a stack is to have each branch/PR in the stack contain one major component of the feature you're building.

For example, if you're building a full-stack feature, you could create the following stack:

1. PR for database/model changes

2. PR for changes to the backend

3. PR for front-end changes using the backend changes

4. PR for integration tests for the change as a whole

By splitting the change up into functional components like this, your reviewers can focus their attention on just one part of the change at a time. Additionally, this framework lets you tag different reviewers for each part of the change, so reviewers with expertise in a certain subsystem can just focus on that part of the review.

## Iterative improvement stacks

Another framework we use frequently here at Graphite is a stack where each PR improves on the preceding changes iteratively. In this model, as soon as you have a change large enough to be reviewable, you create a PR and put it up for review. While waiting for that change to be reviewed, you can continue to make improvements on top of your first PR, forming the next PR in the stack. Continue this process until the feature you're building is ready to ship.

A common pattern in this model is to address non-blocking review feedback by adding a new PR with the changes to the top of the stack. These feedback-driven PRs make it easy for your reviewer to confirm that their feedback was addressed appropriately.

Here's what this kind of stack might look like:

1. PR for the initial feature

2. PR for an iterative improvement

3. PR for an iterative improvement

4. PR addressing review feedback on the initial feature PR

One failure mode to watch out for with this structure of stack is waiting too long before merging any of the PRs. Until a PR is merged, there is a risk that a colleague could introduce conflicting changes that require your PR to be reworked. Additionally you don’t need the full stack to be complete to start merging it - you can merge a set of PRs at the base of the stack as soon as they're ready, and then continue to work on the top of the stack.

## Refactor/change stacks

When fixing bugs, you'll often need to refactor the code around where the bug lives. Instead of fixing and refactoring at the same time, stacking lets you first refactor the code and then stack the actual bug fix on top of the refactor as a separate PR.

Here's what a refactor/change stack looks like:

1. PR for the refactor

2. PR for the bug fix

By making this separation, it makes it very explicit to reviewers what part of the changes are refactoring and what part of the changes are the actual bug fix.

## Version bumps/generated code stacks

Another common software development task is updating library versions or generating code. These types of updates are usually not particularly interesting or risky, but they create noise in code review that can distract reviewers and make it more difficult to determine the more meaningful parts of the change.

In practice, version bump/code gen stacks look very similar to refactor/change stacks:

1. PR for the version bump or code generation

2. PR for anything that uses the updates

By separating out these types of changes into their own PR and then stacking the changes that use the updates in another PR on the stack, reviewers will have a much easier time understanding what part of the code is just boilerplate and what part of the code has the more meaningful changes.

## Riskiness stacks

Finally, you can use stacks to isolate risky parts of a change. Ideally, if you need to revert a change, you want to revert the smallest amount of code possible to minimize the revert's impact on unrelated code or features. If you worry that some of the changes you are making are riskier than others, you can pull the risky parts of the change into their own PRs, but still keep them part of the stack they belong to.

Here's what this might look like:

1. PR for low-risk changes

2. PR for a high-risk change

3. PR for another high-risk change

This way, if either of the high-risk PRs cause issues, you can easily them while still keeping the code that landed in the low-risk PR in production.

## When to split up your changes

These five frameworks are helpful ways of thinking about splitting up larger changes into a stack. One last practical question is *when* you should perform these splits: as you write your code or at the end once you've finished your change? The short answer is that you can do either - it's largely a matter of personal preference. Both the Graphite [CLI](/cli-overview) and [VS Code extension](/vs-code-extension) support stacking new PRs on top of existing changes as the default workflow. If you prefer to write all of your code changes and then split them into stacks, you can do this easily with [gt split](/squash-fold-split#split-a-branch-into-multiple-branches).

By incorporating these five frameworks into your development practice, you can make the most of stacked PRs and streamline your development cycle.


# Initialize Graphite In A Repository
Source: https://graphite-58cc94ce.mintlify.dev/docs/initialize-in-a-repo

Learn how to initialize the Graphite CLI in your git repository.

To use the Graphite CLI in a Git repository, we need to know your trunk branch (typically `main` or `master`). This helps us know where to merge pull requests, and how to synchronize changes from your upstream `origin`.

To initialize your repository, run `gt init`:

```bash Terminal theme={null}
cd ~/my-project
gt init
```

The CLI will prompt you to select a trunk branch for your development flow. Follow the prompt to choose a trunk branch, and press **Enter** to confirm.

This configuration is stored at `.git/.graphite_repo_config` inside each repository you initialize.

<Note>
  If you forget to run `gt init` in your repository, don't worry! All `gt` commands check for initialization first, and will auto-prompt you to choose a trunk branch at the time of running any command.
</Note>


# Insights
Source: https://graphite-58cc94ce.mintlify.dev/docs/insights

Learn how to track your team's engineering velocity with Graphite Insights.

<Note>
  Insights is currently in beta.
</Note>

Graphite's goal is to improve engineering efficiency. Graphite Insights helps measure and improve that efficiency through transparent, customizable stats.

Insights allows you to create, save, and share custom views with your queries. You can look at activity for yourself and your team members. This transparency aims to give all team members the benefit of data—regardless of their role on the team.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9006508a-1688787621-insights.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=99f47df5abdb25604a94e2d267125fe3" data-og-width="6668" width="6668" data-og-height="3388" height="3388" data-path="images/9006508a-1688787621-insights.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9006508a-1688787621-insights.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5bc8556c217e21fac402ac004c9f88d5 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9006508a-1688787621-insights.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2fbf73644d4be9b43f3e2e9fc09104b0 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9006508a-1688787621-insights.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f729d9b88569640dc851a83f8a2ce49e 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9006508a-1688787621-insights.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=aaeb6382a4cd3346e39ce48bbdd92a43 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9006508a-1688787621-insights.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4a0130ddbfcc787ca48ffd1b783d8864 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9006508a-1688787621-insights.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=34d1316fee0323b90d5ee3eb7a6e0f0d 2500w" />
</Frame>

### What kind of data will I see?

<Note>
  For a deep dive into Insights stats and how they're computed, see [Insights stats definitions](/insights-stats-definitions).
</Note>

For selected users (aggregated):

* Total PRs merged

* Average number of PRs merged per person

* Average number of PRs reviewed per person

* Median publish to merge time

* Median review response time

* Median wait time to first review

* Average number of review cycles until merge

* (Graph) Number of PRs reviewed per person over a time period

* (Graph) Number of PRs reviewed by Graphite users vs. non-Graphite users over a time period

* (Graph) Number of PRs merged per person over a time period

* (Graph) Number of PRs merged by Graphite users vs. non-Graphite users over a time period

For each individual user:

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/92368f05-1688789123-insights-table.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=38ddd1e4915f88582c1a924433ffa369" data-og-width="6668" width="6668" data-og-height="3388" height="3388" data-path="images/92368f05-1688789123-insights-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/92368f05-1688789123-insights-table.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7d493068a8c07ad1ff4c3b72d3cf5f89 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/92368f05-1688789123-insights-table.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=732ba3cf3ece91ff393ece4300ceba0e 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/92368f05-1688789123-insights-table.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f2050542bed77617bd30a4c9199c3435 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/92368f05-1688789123-insights-table.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=30612858fff614e4dfef3c02b2611f20 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/92368f05-1688789123-insights-table.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5d53933f13a4430b90f8a345aa330c5d 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/92368f05-1688789123-insights-table.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2822c804ac13d9046275d05b14f637f4 2500w" />
</Frame>

<Note>
  Is there a stat you want to see that isn't captured by Graphite Insights? Reach out to us at **[support@graphite.dev](mailto:support@graphite.dev)** or message us in our [Slack community](https://graphite-community.slack.com/).
</Note>

### Adjust the Insights time period

The statistics that are shown on the Insights page are aggregated over a specific time period. Graphite provides four fixed time periods for your convenience: the past week, month, quarter, or year. You also have the option to input a custom time period.

Each Graphite plan includes a defined sync period for historical GitHub data. The Starter plan includes insights going back up to 2 months. The Standard and Enterprise plans include up to 2 years.

### Select users

You also have the ability to filter and view insights for specific people or groups of people, as well as the aggregate across your entire organization.


# Insights Data in Graphite
Source: https://graphite-58cc94ce.mintlify.dev/docs/insights-data-missing

Learn how to ensure Graphite can compute insights for your repositories

Insights data in Graphite is computed based on a few factors. If you’re not seeing data for your repositories, it may be due to one of the following:

* **Repositories not yet selected in Graphite**
  Graphite computes insights only for repositories explicitly selected by you or your organization in the [Graphite app](https://app.graphite.com/). Be sure to select the repositories you'd like insights to be computed for.

* **Insights are pending computation in Graphite**
  Once you've selected repositories, Graphite will need some time to compute insights. In most cases, this happens within a day or two.

* **Your selected date range exceeds your current plan’s sync window.**
  Each Graphite plan includes a defined sync period for historical GitHub data. The Starter plan includes insights going back up to 2 months. The Standard and Enterprise plans include up to 2 years.


# Insights Stats Definitions
Source: https://graphite-58cc94ce.mintlify.dev/docs/insights-stats-definitions

Learn how the stats on Graphite insights are computed.

Graphite computes stats for each user as an author and as a reviewer. **Stats are computed on merged PRs only**.

## Methodology

**Active users:** For a user to be active in the selected time frame and repos they must have:

1. created a PR on GitHub to be considered active on GitHub **or**

2. created a stack of 2+ PRs on Graphite to be considered active on Graphite

**Rollups**: The graphed metrics are weekly rollups, where weeks start on Monday and end on Sunday. Rollups are medians-of-medians, where we first take each individual active user’s median value for the week, then take the median of those values.

**Calculating pre-Graphite median:** For each active Graphite user in the selected time frame, we look at the median of each user’s 28 days of usage on GitHub before they ever created a stack with Graphite (in the selected repos). Then take the median again across all users. The goal is to create a fair benchmark of performance before these users starting using Graphite

**Minimum 5+ active Graphite users:** We won’t attempt to draw comparisons between developers using Graphite or GitHub if there are fewer than 5 active Graphite users in the selected timeframe.

## Author stats

* **PRs merged:** Total number of PRs where the user was an author

* **Time waiting on reviews:** Median time of PRs authored by the user (that have open requests for reviews) were sitting without any reviews

* **Wait time to first review:** Median time of a PR being marked as *ready for review* for the first time, and someone reviewing it

* **Publish to merge time:** Median time between a PR being marked as *ready for review* for the first time, and it being merged

* **Review cycles until merge:**

  * Computes the max number of review cycles any reviewer had until the PR was merged

  * Then across all PRs, computes the median of this number

## Reviewer side stats

* **PRs reviewed:** Total number of PRs that the user left a review on

**Response time to review requests:** Median of the difference in time between the user being requested (or re-requested) for a review, (referred to as review request/review *pairs*) for the given user

## Insights example

Here's an example of a sequence of events and how that activity will impact Insights stats:

1. User X authors a PR in draft state that adds 10 lines of code, and deletes 5 lines of code

2. User X publishes the PR, making it ready for review

3. User X requests reviews from User A, User B, and User C

4. User A requests changes on the PR

5. User B leaves a review comment on the PR

6. User X makes updates, and re-requests reviews from User A and User B

7. User A leaves a review comment on the PR

8. User B leaves a review comment on the PR

9. User X makes updates, and re-requests review from User A

10. User A approves the PR

11. User X merges the PR

These events will affect each stats in the following ways:

* PRs merged will go up by 1 for User X

* PRs reviewed will go up by 1 for User A and User B (User C did not review, so no change there)

* Response time to review requests will be computed for each reviewer on each review request/review pair as (\*review time \*- *review request time*). This will then feed into the reviewer’s aggregated median statistic.

  * User A response time for first review request = *time at event #4* - *time at event #3*

  * User B response time for first review request = *time at event #5* - *time at event #3*

  * User A response time for second review request = *time at event #7* - *time at event #6*

  * User B response time for second review request = *time at event #8* - *time at event #6*

  * User A response time for third review request = *time at event #10* - *time at event #9*

* Time waiting on reviews will be computed based on how long the author was waiting on reviews for that PR. This then feeds into the author’s aggregated median statistic.

  * Time waiting on reviews on the PR above for User X as author = (*time at event #4* - *time at event #3*) + (*time at event #7* - *time at event #6*)

  * Note that we didn’t count the time between event #10 and event #9 here because there was a review from User B on the PR—so the author wasn’t waiting on reviews during this time period. In case User X re-requested review from both User A and User B in event #9, we would also add (*time at event #10* - *time at event #9*) into the computation above.

* Wait time to first review will be computed based on how long the author waited until anyone reviewed their PR after it was published/ready for review. This will then feed into the author’s aggregated median statistic.

  * Wait time until first review on above PR for User X as author = *time at event #4* - *time at event #2*

* Publish to merge time will be computed based on how long it took for the PR to be merged after it was published/ready for review. This will then feed into the author’s aggregated median statistic.

  * Publish to merge time on above PR for User X as author = *time at event #11* - *time at event #2*

* Review cycles until merge for a PR will be computed as the max number of review request/review pairs that a reviewer had until the PR was merged. This will then feed into the author’s aggregated median statistic.

  * Review cycles for User A as reviewer = \[(event #10, event #9), (event #7, event #6), (event #4, event #3)] (count = 3)

  * Review cycles for User B as reviewer = \[(event #8, event #6), (event #5, event #3)] (count = 2)

  * Max review cycles on above PR for User X as author = max(3, 2) ⇒ 3

* Lines of code added will go up by 10 for User X

* Lines of code deleted will go up by 5 for User X


# Install & Authenticate The CLI
Source: https://graphite-58cc94ce.mintlify.dev/docs/install-the-cli

Learn how to install & authenticate Graphite's CLI to start creating stacked pull requests.

The Graphite CLI is a tool to help you break up large engineering tasks into a series of small, incremental code changes directly from the command line. The Graphite CLI makes it easy to stay unblocked as an author, develop faster, and provide more helpful comments as a reviewer.\
\
The Graphite CLI is fully compatible with `git`—just install it on an existing repository and begin using our suite of `gt` commands.

## Install the CLI

Install the Graphite CLI using either [Homebrew](https://brew.sh/) or [npm](https://www.npmjs.com/):

### brew installation

We recommend installing via Homebrew for smoothest sailing, [even on Linux!](https://docs.brew.sh/Homebrew-on-Linux)

```bash Terminal theme={null}
brew install withgraphite/tap/graphite
gt --version
```

### npm installation

```bash Terminal theme={null}
npm install -g @withgraphite/graphite-cli@stable
gt --version
```

### node.js versioning (for npm installation only)

We develop Graphite with Node.js v18, but Graphite should run with no major issues on any current version of Node. If you run into any issues that seem Node-related, try using v18 as a first workaround! If that doesn't work, we recommend the `brew` installation, which ships standalone binaries for both MacOS and Linux.

### git versioning

As of v1.0.0, Graphite requires a minimum `git --version` of 2.38.0.

#### Ubuntu

Ubuntu LTS currently provides a relatively old version of Git by default. You can source the latest version from the \`git-core\` PPA repository.

```bash Terminal theme={null}
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
```

[Read more on the Git website](https://git-scm.com/download/linux)

#### MacOS

Upgrading to the latest version of XCode tooling, provides a recent version of git that's suitable for Graphite. You can also use Homebrew to install the latest version of Git.

#### Unsafe: overriding

If you believe this is an error, and your git version is higher than 2.38.0 but something about it's packaging is making Graphite incorrectly infer it's not the right version, you can unsafely suppress this message via `GRAPHITE_IGNORE_GIT_VERSION=1`. This is discouraged, so be careful; most Graphite commands will not work on older versions.

### Windows

Currently, the best way to install Graphite on Windows is via `npm`. If you do not use Node in your day-to-day work, there are a variety of ways to get it set up on your system, listed in the NPM documentation.

[Click here for instructions.](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm#os-x-or-windows-node-installers)

Alternatively, you can use either `brew` or `npm` on WSL (Windows Subsystem for Linux).

We are always working towards better native Windows support, although occasionally it falls behind \*nix systems in priority. If you run into any issues, especially if they are blocking your workflow, please reach out in our [community Slack](https://community.graphite.com).

## Authenticate the CLI

<Note>
  To use Graphite to create or update pull requests in GitHub for the branches in your stack using `gt submit`, you must authenticate the CLI with your GitHub account. See [Privacy and Security](/privacy-and-security) to understand which GitHub permissions Graphite requires.
</Note>

1. Sign into [https://app.graphite.com/activate](https://app.graphite.com/activate) with your GitHub account.

2. Copy the `gt auth --token <your_cli_auth_token>` command shown (your CLI auth token will be pre-filled for you).

3. Paste and run it in your terminal.

```bash Terminal theme={null}
> gt auth --token <YOUR_AUTH_TOKEN>
🔐 Saved auth token to "/Users/pranathiperi/.graphite_user_config"
```

Once you've authenticated the CLI, you can run `gt submit` to create or update pull requests in GitHub for every branch in your stack.

Your privacy and security are our top priorities. Graphite is architected to ask for the minimum set of permissions necessary within the constraints of GitHub's API. Learn more about our [GitHub integration](/privacy-and-security).


# Integrations
Source: https://graphite-58cc94ce.mintlify.dev/docs/integrations

Personalize your workflow by connecting Graphite to your favorite apps.

## Supported integrations

You can choose to customize your Graphite workflow by integrating with a number of supported applications. Reach out and let us know if you have ideas for Graphite extensions!

<CardGroup cols={3}>
  <Card icon="puzzle" href="/vs-code-extension" title="VS Code extension">
    Not a CLI person? Use Graphite right from your IDE.
  </Card>

  <Card icon="square-menu" href="/menu-bar-app" title="Menu bar app">
    Keep track of your PRs in your Mac menu bar.
  </Card>

  <Card icon="slack" href="/slack-notifications" title="Slack notifications">
    Real-time notifications — review and merge PRs from Slack.
  </Card>

  <Card icon="loader-circle" href="/linear" title="Linear">
    View, link, and create Linear issues from pull requests.
  </Card>

  <Card icon="square-kanban" href="/jira" title="Jira">
    View, link, and create Jira issues from pull requests.
  </Card>
</CardGroup>


# Jira
Source: https://graphite-58cc94ce.mintlify.dev/docs/jira

Learn how to integrate Graphite with Jira to view, link, and create issues associated with pull requests.

<img src="https://mintcdn.com/graphite-58cc94ce/4eK3kidU7PG-WjjO/images/jira-access-request.png?fit=max&auto=format&n=4eK3kidU7PG-WjjO&q=85&s=95dc0543454ecb8c56399207dc9e765f" data-og-width="1161" width="1161" data-og-height="822" height="822" data-path="images/jira-access-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/4eK3kidU7PG-WjjO/images/jira-access-request.png?w=280&fit=max&auto=format&n=4eK3kidU7PG-WjjO&q=85&s=9fb4f5cbbd55fd450c189a6583445b04 280w, https://mintcdn.com/graphite-58cc94ce/4eK3kidU7PG-WjjO/images/jira-access-request.png?w=560&fit=max&auto=format&n=4eK3kidU7PG-WjjO&q=85&s=ba1cbd277995ecd86b7131ff7fe14802 560w, https://mintcdn.com/graphite-58cc94ce/4eK3kidU7PG-WjjO/images/jira-access-request.png?w=840&fit=max&auto=format&n=4eK3kidU7PG-WjjO&q=85&s=81159de02e9d202c7136bdec4b6eb637 840w, https://mintcdn.com/graphite-58cc94ce/4eK3kidU7PG-WjjO/images/jira-access-request.png?w=1100&fit=max&auto=format&n=4eK3kidU7PG-WjjO&q=85&s=e025257ae7583586503586991f3d6559 1100w, https://mintcdn.com/graphite-58cc94ce/4eK3kidU7PG-WjjO/images/jira-access-request.png?w=1650&fit=max&auto=format&n=4eK3kidU7PG-WjjO&q=85&s=89b367daff3aa6c4e2078ca67a714de7 1650w, https://mintcdn.com/graphite-58cc94ce/4eK3kidU7PG-WjjO/images/jira-access-request.png?w=2500&fit=max&auto=format&n=4eK3kidU7PG-WjjO&q=85&s=618110d386ce7b34d75a923796e13140 2500w" />

With Graphite's Jira integration you can view, link, and create issues associated with pull requests right from the Graphite web app.

### Prerequisites

* A Jira account

## Connect Jira

Connect your Jira account directly from the [*Connected accounts* settings page](https://app.graphite.com/settings/connected-accounts) on the Graphite app.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-connect-jira-button.png?fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=bddd924f6eacb14710e4c7311440fc6c" data-og-width="1435" width="1435" data-og-height="635" height="635" data-path="images/show-connect-jira-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-connect-jira-button.png?w=280&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=420c7aa12a82d5b65ff049e77f54e883 280w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-connect-jira-button.png?w=560&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=20d460c97a644272f29b10e19f262d60 560w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-connect-jira-button.png?w=840&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=c4e9e18206d7874b4e03c1ff86082381 840w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-connect-jira-button.png?w=1100&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=6f3cae48e205e31fed727f5665ead521 1100w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-connect-jira-button.png?w=1650&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=70417278453097800bee3b1c5173954e 1650w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-connect-jira-button.png?w=2500&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=5dc451349c3ca6e7c6e7b86ac05f87e8 2500w" />
</Frame>

After clicking the `Connect` button you will be directed to Jira to finish the integration setup process.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/graphite-connected-accts-w-jira.png?fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=78527e40723016333175f3d741fedaa6" data-og-width="1163" width="1163" data-og-height="511" height="511" data-path="images/graphite-connected-accts-w-jira.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/graphite-connected-accts-w-jira.png?w=280&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=0be40f403e374768f066cd1f6a547834 280w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/graphite-connected-accts-w-jira.png?w=560&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=c7a2afa999a9ffc03bc03efe7a6dd0f9 560w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/graphite-connected-accts-w-jira.png?w=840&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=df2a1b5d250c445fb9629a9a50e49df4 840w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/graphite-connected-accts-w-jira.png?w=1100&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=4dbc13de2ca675f0e346fb4224ba3a2b 1100w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/graphite-connected-accts-w-jira.png?w=1650&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=89d871fbb73ea57de949be33e2eaab91 1650w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/graphite-connected-accts-w-jira.png?w=2500&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=fcdff7289cda62a629dd77246e6996b1 2500w" />
</Frame>

Once the integration is successfully configured, you should see confirmation on the **Connected accounts** settings page.

## Using the Jira integration on the PR page

After you've installed the integration, you can will then be able to view any associated Jira issues in the sidebar of the **Pull Request** page.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/jira-in-graphite.png?fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=e935d18fed6744760e93006b917fd9ac" data-og-width="1446" width="1446" data-og-height="847" height="847" data-path="images/jira-in-graphite.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/jira-in-graphite.png?w=280&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=d98cd1797af9d38666d9a8ff1927a119 280w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/jira-in-graphite.png?w=560&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=ca94581d4d75dcc043035ee3d1c9a2e0 560w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/jira-in-graphite.png?w=840&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=a4c775011aaa91eb6e40855210d2327f 840w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/jira-in-graphite.png?w=1100&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=00feec51acc7a0aa85feabe65ff4530d 1100w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/jira-in-graphite.png?w=1650&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=c5a1d3fc113dde986b4261ed040b6a27 1650w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/jira-in-graphite.png?w=2500&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=3988f097b1b695ede7a9d3d6d739a572 2500w" />
</Frame>

### Linking an existing issue

To link a Jira issue to a pull request, click the **+** symbol located in the issue tracker sidebar component.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-link-issue-jira.png?fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=442f61bf53d8ce140bcc4a030b8401a3" data-og-width="1452" width="1452" data-og-height="879" height="879" data-path="images/show-link-issue-jira.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-link-issue-jira.png?w=280&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=019796c8947a84226208fb4fefd64191 280w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-link-issue-jira.png?w=560&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=3173c7a56647643ad3fb44318d07954f 560w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-link-issue-jira.png?w=840&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=aa6039d277a0c9593a9075243dd74fde 840w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-link-issue-jira.png?w=1100&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=52e6c20452bf1480e89b4974510f230b 1100w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-link-issue-jira.png?w=1650&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=42c9a040b50cabac306faa0cf0d75f30 1650w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/show-link-issue-jira.png?w=2500&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=703621cdc0cdfcc29f35f509a98275e2 2500w" />
</Frame>

From here you can:

* Search for a Jira Issue by name

* \[OR] Paste a Jira Issue URL

### Creating a new Jira Issue from PR page

To create and link a new Jira Issue from the Pull Request page, you can click `Create new issue` in the issue tracker sidebar component.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/new-jira-modal.png?fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=35a608e0caaf4deb5262afc65307dd62" data-og-width="1582" width="1582" data-og-height="1521" height="1521" data-path="images/new-jira-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/new-jira-modal.png?w=280&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=9be3f16478f040d9775717d621936fa9 280w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/new-jira-modal.png?w=560&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=837771f6eb40f13f1b236ac697665ca9 560w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/new-jira-modal.png?w=840&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=ced7c78833ef40a4bf86a51b472b754c 840w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/new-jira-modal.png?w=1100&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=b31afa77a5956a75241bf7851b549cbc 1100w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/new-jira-modal.png?w=1650&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=6935422c483b357d7f6351e870463704 1650w, https://mintcdn.com/graphite-58cc94ce/5-r_sd14jPfxQ4c9/images/new-jira-modal.png?w=2500&fit=max&auto=format&n=5-r_sd14jPfxQ4c9&q=85&s=b44811a9ecdb4e56abbd6850fa8f0587 2500w" />
</Frame>

From here you can assign a *Project, Issue Type, Summary, Description, Status, and Priority*. Once you click `Create issue`. The issue will be created in Jira, and will be linked to the current pull request.


# Learn to Stack
Source: https://graphite-58cc94ce.mintlify.dev/docs/learn-to-stack

A practical starter guide for trunk-based development and stacking.

<CardGroup cols={2}>
  <Card title="Trunk-based development" href="/trunk-based-development" icon="pen">
    [Learn about the benefits of trunk-based development and how teams work from a single shared branch.](/trunk-based-development)
  </Card>

  <Card title="Structuring a stack" href="/how-to-structure-your-stacks" icon="waves-ladder">
    [Five helpful frameworks for deciding how to build your stacks from the ground up.](/how-to-structure-your-stacks)
  </Card>

  <Card title="Best practices for reviewing stacks" href="/best-practices-for-reviewing-stacks" icon="scan-search">
    [How to think about reviewing stacked changes for timely and high-quality feedback.](/best-practices-for-reviewing-stacks)
  </Card>

  <Card title="Comparing Git and Graphite" href="/comparing-git-and-gt" icon="git-compare">
    [See how the Git commands you're used to translate to simple Graphite CLI commands.](/comparing-git-and-gt)
  </Card>
</CardGroup>


# Legacy CLI Command Alias Preset
Source: https://graphite-58cc94ce.mintlify.dev/docs/legacy-alias-preset

Copy legacy aliases to retain old command names & avoid deprecation warnings in Graphite CLI.

Copy the following into your `gt aliases` configuration to replicate the legacy command names. This will remove deprecation warnings when the old names are used.

```md .md theme={null}
# Edit this file to configure aliases for Graphite commands.
# If you delete this file, it will be recreated with the default aliases.
# The first word of each line is the alias, and the rest is the command.
# Lines starting with # are ignored.


# The aliases for ss, ls, and ll are defined by default and must be overridden to be disabled.
# They are shown below to demonstrate the formatting.


ls log short
ll log long
ss submit --stack


# GRAPHITE LEGACY PRESET
# SOURCE: https://graphite.com/docs/legacy-alias-preset


bc create
ca modify
cc modify --commit
dss submit
bs submit
uss submit --stack
rs repo sync
bco checkout
bi info
bu up
bd down
bt top
bb bottom
ri init
uso move --onto
dse reorder
brn rename
bdl delete
dsg get
bf fold
bsp split
bsq squash
br restack --only
usr restack --upstack
dsr restack --downstack
sr restack
be modify --interactive-rebase
btr track
but untrack
dsm merge
```


# Linear
Source: https://graphite-58cc94ce.mintlify.dev/docs/linear

Learn how to integrate Graphite with Linear to view, link, and create issues associated with pull requests.

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d9e64d62-1741191316-browser-window.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5bce2bc3ccb2652d0f15a46d13ae4b03" data-og-width="832" width="832" data-og-height="665" height="665" data-path="images/d9e64d62-1741191316-browser-window.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d9e64d62-1741191316-browser-window.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b1c578ed6a49db59b4fd971c92b64eb9 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d9e64d62-1741191316-browser-window.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d1b26dbc9afe29b301edf9339c8e4274 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d9e64d62-1741191316-browser-window.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=87be022624c3363d9727fdd519bde8ca 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d9e64d62-1741191316-browser-window.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=6b2a5b2ef4953ae4676602a0249a49f1 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d9e64d62-1741191316-browser-window.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=91c30efa18346888569deb2a3be6d5fe 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d9e64d62-1741191316-browser-window.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=da5f650e75356df75d516a786a9cb7b9 2500w" />

With Graphite's Linear integration you can view, link, and create issues associated with pull requests right from the Graphite web app.

### Prerequisites

* A Linear account

## Connect Linear

Connect your Linear account directly from the [*Connected accounts* settings page](https://app.graphite.com/settings/connected-accounts) on the Graphite app.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4c705623-1741213051-frame-10124206-1.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=87d7ee43435dd335a6cd61c6ec13c386" data-og-width="760" width="760" data-og-height="270" height="270" data-path="images/4c705623-1741213051-frame-10124206-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4c705623-1741213051-frame-10124206-1.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7b0326f5656d6ec0088302f9b8ee4b11 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4c705623-1741213051-frame-10124206-1.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=24e60e87ff31a4a66e352d137811b010 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4c705623-1741213051-frame-10124206-1.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=feb3a575012f1a0c182a920b48bc5456 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4c705623-1741213051-frame-10124206-1.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=588752b28a8c90859f21bcfcdadb2a6c 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4c705623-1741213051-frame-10124206-1.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4d406d84584e659cf62a35f9a92d1321 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4c705623-1741213051-frame-10124206-1.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=9ff2560efe49f7c4e030ac01dccf4c40 2500w" />
</Frame>

After clicking the `Connect` button you will be directed to Linear to finish the integration setup process.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b081be25-1741213061-frame-10124207-1.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=9b7855bdff4813d6009eecb74ed16835" data-og-width="760" width="760" data-og-height="270" height="270" data-path="images/b081be25-1741213061-frame-10124207-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b081be25-1741213061-frame-10124207-1.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=44e5054a186bcffe10b0ffb857e50fe8 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b081be25-1741213061-frame-10124207-1.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=0578b805298fcdf09ffd2017bfc74684 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b081be25-1741213061-frame-10124207-1.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=92b2c67a360726166f5cd0c2b2001665 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b081be25-1741213061-frame-10124207-1.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c87d65efd8c1fed53da6cfe192f1f93c 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b081be25-1741213061-frame-10124207-1.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=788950d014eaf494dfb6450749a5c8ee 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b081be25-1741213061-frame-10124207-1.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7385b968b6a392a6fe8e59fd7f780df9 2500w" />
</Frame>

Once the integration is successfully configured, you should see confirmation on the **Connected accounts** settings page.

## Using the Linear integration on the PR page

After you've installed the integration, you can will then be able to view any associated Linear issues in the sidebar of the **Pull Request** page.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/eb0e2cd1-1741211170-frame-10123871.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ff754f55294cbf587c0fa89adcf71967" data-og-width="1304" width="1304" data-og-height="822" height="822" data-path="images/eb0e2cd1-1741211170-frame-10123871.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/eb0e2cd1-1741211170-frame-10123871.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8f61f8e1a9c00b03ff5864e4889cbc0a 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/eb0e2cd1-1741211170-frame-10123871.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b584c182efc3e709c6d9d224d50d2ed1 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/eb0e2cd1-1741211170-frame-10123871.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=018ca7a8474597916b01ebf4ed12278a 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/eb0e2cd1-1741211170-frame-10123871.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=af8d31f69aa36d0e935c7f88773a3d42 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/eb0e2cd1-1741211170-frame-10123871.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2d4e14607f9e3f7c9ddfbea11ac8c04b 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/eb0e2cd1-1741211170-frame-10123871.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a7705282b71a96d4e30192a481d20d88 2500w" />
</Frame>

### Linking an existing issue

To link a Linear issue to a pull request, click the **+** symbol located in the issue tracker sidebar component.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/83650d6a-1741211386-link-issue-popout.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8ba352d18dd62252c905a9fecdd7c660" data-og-width="1406" width="1406" data-og-height="1000" height="1000" data-path="images/83650d6a-1741211386-link-issue-popout.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/83650d6a-1741211386-link-issue-popout.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ca1603c1f1e3a9aa18ece10f85945881 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/83650d6a-1741211386-link-issue-popout.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=24257ec19f0c9423c90605cb382db90b 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/83650d6a-1741211386-link-issue-popout.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=eb53cf3384ece231253205c8f7716f21 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/83650d6a-1741211386-link-issue-popout.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e1072aeb03ca726bf18cc07835786e17 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/83650d6a-1741211386-link-issue-popout.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=514633621aa6c0ca38db849c310267f3 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/83650d6a-1741211386-link-issue-popout.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3ca2a07a2d19ae53e1e65af921e16bbd 2500w" />
</Frame>

From here you can:

* Search for a Linear Issue by name

* \[OR] Paste a Linear Issue URL

### Creating a new Linear Issue from PR page

To create and link a new Linear Issue from the Pull Request page, you can click `Create new issue` in the issue tracker sidebar component.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c3fa9d75-1741211806-create-modal-1.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3a1e55684fe6c1f02aedf5518aa89cf7" data-og-width="1648" width="1648" data-og-height="1000" height="1000" data-path="images/c3fa9d75-1741211806-create-modal-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c3fa9d75-1741211806-create-modal-1.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ebcf165c697f8551a918785a0c25c4da 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c3fa9d75-1741211806-create-modal-1.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=fe86d9d1334cbeeda2b2828f5f81638b 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c3fa9d75-1741211806-create-modal-1.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=df6427da0d41d1a5a80729e41bb1f3b9 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c3fa9d75-1741211806-create-modal-1.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d833e6c2dd9d56bce73255681535bd64 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c3fa9d75-1741211806-create-modal-1.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1f9212b2b6bf300858a2e690df47928a 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c3fa9d75-1741211806-create-modal-1.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=24e2d436ef19126e600dcd2761ad0787 2500w" />
</Frame>

From here you can assign a *Team, Title, Description, Status, and Priority*. Once you click `Create issue`. The issue will be created in Linear, and will be linked to the current pull request.


# Memes And Macros
Source: https://graphite-58cc94ce.mintlify.dev/docs/memes-and-macros

Add some fun to your code reviews.

## Memes and macros

One of the best parts about reviewing PRs in the Graphite app is the ability to use custom memes and macros in your comments, descriptions, and reviews.

### Upload new memes

Each organization on Graphite has their own custom meme library, which you can access on the `Meme Library` tab of the PR inbox, or by using the `G` + `/` keyboard shortcut. To upload a gif or image, click the `upload` button and set a name for the meme:

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=705ed36654faacdbf383e8bdbcba8e5c" data-og-width="2854" width="2854" data-og-height="1456" height="1456" data-path="images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e3906cdd997158205c7e10bf663068c8 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=18678723fb27cd27524f2460054ce946 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2226e6d58297ec785cf5798f3573cebb 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1a675e251d8e0d6adcf8d149677a2db9 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=17e54b68fe72eb1951f577c039d17004 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=bb578c33540fb446b070de465d6d7882 2500w" />
</Frame>

### Use custom memes in comments and reviews

To add a meme to your comment or review, you can click the "meme" icon in the footer of the comment box markdown editor to browse your meme library, or use the `/` character to search for a meme by name.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=705ed36654faacdbf383e8bdbcba8e5c" data-og-width="2854" width="2854" data-og-height="1456" height="1456" data-path="images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e3906cdd997158205c7e10bf663068c8 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=18678723fb27cd27524f2460054ce946 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2226e6d58297ec785cf5798f3573cebb 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1a675e251d8e0d6adcf8d149677a2db9 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=17e54b68fe72eb1951f577c039d17004 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/bcdf927c-1695008256-screenshot-2023-09-17-at-11-36-28-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=bb578c33540fb446b070de465d6d7882 2500w" />
</Frame>


# Menu Bar App (Mac)
Source: https://graphite-58cc94ce.mintlify.dev/docs/menu-bar-app

Keep track of all of your PRs from your Mac menu bar.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f4b3612f4ace25ecf2c51714f7bb21f6" data-og-width="1378" width="1378" data-og-height="962" height="962" data-path="images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=92cb32fd106e74a27f5d0301e37269cc 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ca82a1bfc1e84eda20aaaca22b51d251 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=6a9a5ceddbbd8c8d3cc52284f7bcfb9b 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=9325dea27aee4d9b230d2fd2978c98b3 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c8ac80ee0c7e31896eeaf37bd6f5f80c 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/37b1c073-1698955015-screenshot-2023-11-01-at-10-43-13-am.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=9365421cb0ac02043b83a2482066a4dc 2500w" />
</Frame>

## Setup instructions

1. The Graphite CLI is a prerequisite for the menu bar app. Follow [these instructions](/install-the-cli) to set it up on your machine.

2. Download the [menu bar app](https://system-tray-app-releases-prod.s3.us-west-2.amazonaws.com/latest/Graphite-menu-bar.dmg).


# Merge Pull Requests
Source: https://graphite-58cc94ce.mintlify.dev/docs/merge-pull-requests

Learn how to seamlessly merge a single PR or stack of PRs with Graphite and handle merge conflicts efficiently.

Merging a stack of PRs manually through GitHub can be time-consuming and involve a lot of context switching. You merge, rebase, wait for CI to pass, and merge again all the way up the stack—or you're forced to ditch the clean PRs you've carefully created, squashing your changes back into a single mega-PR for the sake of merge speed.

Graphite offers an automated solution that gives you the best of both worlds.

Once your PR is approved and passes CI (and any other checks or merge protections you've enabled in GitHub), you can merge it from Graphite. Just click the purple "Merge" button on the right side of the PR title bar.

## Merge a stack of PRs

Depending on which PR you are viewing in the stack, this button will behave differently:

* If you're on the first PR in the stack or are merging a stack of one, the `Merge` button will just merge that single PR.

* If you're in the middle of a stack, `Merge N` where `N` is your position in the stack and will merge all PRs up until the `N`th.

* If you're at the top of the stack, all PRs in the stack will be merged.

`Merge (N) PRs` lets you fire-and-forget merging your stack. When you click the button, Graphite automatically merges each of your PRs one-by-one.

This feature rebases PRs on an as-needed basis (to avoid merge conflicts generated by GitHub's lack of stack support). And it waits for GitHub checks to pass at each step of the way before merging.

<Tip>
  Not all PRs in the stack need to be accepted and passing checks to merge.

  For example, if only PRs 1, 2, and 3 in a stack of 5 have been accepted and are passing checks, you can still utilize `Merge all (n)` on PR 3 to merge those into trunk—just make sure you `gt sync` and `gt submit` the rest of your stack before merging again.
</Tip>

### Configure merge options

Clicking `merge` will first present you with a modal to configure your merge options before starting the merge job. In this merge modal, you have the option to:

* Select your preferred merge strategy. Graphite pre-fills with your default merge strategy from GitHub.

* Edit a custom commit title and message for your PR. Graphite will use your PR title and message as the commit title and message by default.

* Use your GitHub admin merge privileges to merge past blockers, if applicable. (Please note that admin merge is available only in repositories that do not use rulesets.)

A confirmation appears in the bottom left corner of the screen once your PR is merged.

<Tip>
  Make sure to run `gt sync` on the Graphite CLI immediately after merging a change to your remote trunk branch—this will zip through and delete your merged branches, ensuring that your local environment is up-to-date and ready for you to keep developing.
</Tip>

### Track the status of your merge on GitHub

Graphite will update a single comment on GitHub with the status of your PR's merge.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e257530741e7bbfc9249512a339c2275" data-og-width="1864" width="1864" data-og-height="394" height="394" data-path="images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b3563d4144a7842239c8c593c880cc15 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=98eb8a861de981805ac987d5a9930abb 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=94a5a290d902c6bd50364eb7da1f2f5b 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8dacda550fc9304b60104cf202c790d6 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2787444d65e69a63f2b414df07aaac04 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1647e499-1695087134-screenshot-2023-09-18-at-9-31-59-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=3ebc9e99e4d335384dfdf7368b4df7b8 2500w" />
</Frame>

### Compatibility with GitHub branch protection rules

If you have the *dismiss stale pull request approvals when new commits are pushed* branch protection rule enabled for your repository on GitHub, you will **not** be able to successfully merge a stack with the Graphite UI. [See our documentation for configuring GitHub repository settings](https://graphite.com/docs/github-configuration-guidelines#required-settings) for more information and a workaround.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=3fcb65eccff1e3dd906653929fa73568" data-og-width="1256" width="1256" data-og-height="118" height="118" data-path="images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=afaab0a8a6e90d94e697090fc3d5a667 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d509670719f7eccc35b89b1a5f729130 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=75d0d20432ccef1eba479a1e8302822e 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7de864881e79bc284b38634698235382 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=52c568970cbc5eadf20ea421745a8cf0 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/28097070-1697120500-screenshot-2023-10-12-at-10-20-44-am.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=978f7f93c779183a1f4c11fe077732e5 2500w" />
</Frame>

## Resolve merge conflicts

If `Merge (N)` fails due to a rebase conflict, go to your terminal and run `gt sync` && `gt restack` && `gt submit --stack` (resolving any conflicts along the way and running `gt continue`). Once you've done this, go back to the affected PR in Graphite (or to the same place in the stack where you initially kicked off the `Merge (N)` job), and click `Merge (N)` one more time to re-queue the PR for merging.

### Types of merge conflicts stack merge can resolve

When PRs are merged on GitHub using a squash and merge or a rebase and merge, GitHub [creates a commit/set of commits](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#squashing-and-merging-a-long-running-branch) for those merged changes.

This means that if you have a stack with `PR A` at the base, followed by `PR B` and `PR C`, when `PR A` is merged into trunk:

* GitHub creates a commit or set of commits on trunk for the changes in `PR A`.

* Critically, because this is a new commit, the common ancestor of `PR B` and trunk does not change.

* As a result, GitHub thinks `PR B` now includes the commits of both `PR B` and the already-merged commits of `PR A`.

This behavior becomes problematic when you have a `PR A` and `PR B` that modify the same lines and you merge both PRs using one of the aforementioned merge strategies. For any `PR C` that is stacked atop `PR A` and `B`, the following transpires:

* The latest version of the change lines on trunk are those in `PR B`.

* GitHub believes that `PR C` contains the commits in `PR A` and `PR B`.

* When GitHub tests mergeability of `PR C`, it first tries to apply `PR A`—and now gets a merge conflict—even though in reality you're simply replaying history and there's no new change.

If you use the Graphite CLI, you'll notice that the CLI handles this scenario for you intelligently. When GitHub reports these sorts of merge conflicts, a `gt sync` will pull down the latest changes and rebase PR C for you, cutting out the problematic commits—and a subsequent re-submit will then eliminate the detected merge conflict for PR C.

`Merge (N)` is designed to similarly automatically resolve this type of merge conflict without the need for manual intervention or monitoring. When a merge conflict is found, the merge cron performs a shallow clone of the repository, containing just the stack commits and the trunk commit and utilizes Graphite's knowledge of the stack to perform the same set of operations.

<Warning>
  Graphite can't resolve any legitimate merge conflicts as a result of racing PRs on trunk that require human intervention. If a Graphite rebase fails, Graphite will cancel the merge job. You must restart the job by fixing the issue locally, re-submitting the PR, and enqueueing a new merge job.
</Warning>

## How a stack merge works

Each time the cron job processes a merge job it runs through the following decision tree:

* If the base PR in the stack has pending GitHub checks, do nothing.

* If the base PR in the stack is passing all GitHub checks and can be merged, merge. The next PR in the stack is now the new base PR.

* If the base PR in the stack has merge conflicts, rebase the PR and re-submit it (re-entering the waiting-for-CI phase).

During the merge process, Graphite prioritizes:

1. Speed of overall stack merge.

2. Minimizing the number of total CI runs.

To achieve these principles, it's important to note that:

* Graphite merges rather than rebasing each individual PR before merging.

* Graphite only rebases PRs lazily. When Graphite detects a merge conflict on a PR, Graphite only rebases that PR, and not the additional PRs further up the stack. This means that if a stack has `m` merge conflicts, there will only be `m` total rebases (and additional CI runs) kicked off by the merge process.

### Merge job duration

Graphite's cron job to process outstanding merge jobs runs at a cadence of once per minute.

As a result, the length of a merge job depends on how many PRs need to be rebased. If there are no merge conflicts, `Merge (N)` will take `n` minutes, but if there are merge conflicts, job time is a byproduct of the time it takes to run GitHub checks on a PR and how many PRs encounter merge conflicts.

## Compatibility with third-party merge queues

Today, merge stack supports label-based merge queues, with future plans to support GitHub's merge queue (currently not compatible).

If you're not sure whether `Merge (N)` will work with your team's merge process, feel free to reach out to **[support@graphite.dev](mailto:support@graphite.dev)**—we'd love to help you with this.

## Automatic rebasing

<Tip>
  Graphite will automatically rebase your stacked PRs after you begin merging them — so you don’t have to. This results in temporary `graphite-base/*` branches that you can ignore
</Tip>

### Requirements

Graphite will automatically rebase your partially-merged stacks so long as you click `merge` from the Graphite app. **This feature does not work when merging from GitHub.**

### How it works

When you partially merge a stack of pull requests, Graphite runs a job that automatically rebases the remote branches corresponding to the PRs “upstack” of the one(s) you merged. This means there is never a moment where the new base of the stack points to a branch or pull request that no longer exists, so there’s no possibility of seeing an incorrect code diff.

This operation results in temporary `graphite-base/*` branches that lets Graphite retarget the rebased branches atomically -- ensuring your CODEOWNERS rules and GitHub Actions workflows don't misfire.

### Ignoring Graphite's temporary branches in your CI

You should configure your CI to ignore branches named `graphite-base/*` . Not doing so can result in unnecessary builds for these temporary branches and cancelled jobs when Graphite deletes these branches.

Here's how to disable running CI for these branches in GitHub Actions:

```yaml  theme={null}
on:
  pull_request:
    types: [opened, reopened, synchronize]
    branches-ignore:
      - "**/graphite-base/**"
```

### Troubleshooting

If your CI hasn't been configured to ignore Graphite's temporary branches yet, your CI job may fail due to an error looking like:

```
Fetching base branch: refs/heads/graphite-base/*
fatal: couldn't find remote ref refs/heads/graphite-base/*
```

The workaround is to trigger a fresh CI run on the PR. You can do this by:

* Running `gt sync && gt submit` (this will only work if `gt sync` fetches new commits from trunk and restacks the PR -- otherwise `gt submit` will be a no-op since there were no changes)
* Submitting a dummy change to the PR

The long-term fix to prevent this issue from appearing is [ignoring Graphite's temporary branches in your CI](https://graphite.com/docs/merge-pull-requests#ignoring-graphite%E2%80%99s-temporary-branches-in-your-ci).


# Merge Queue Optimizations
Source: https://graphite-58cc94ce.mintlify.dev/docs/merge-queue-optimizations

Learn how to speed up your Graphite merge queue

The Graphite merge queue offers three optimizations that both speed up the merging process and reduce CI costs.

You can use all merge queue optimizations at the same time. The optimizations are:

1. Fast-forward merge (run CI on all PRs in a stack in parallel)

2. Parallel CI (run CI in parallel on multiple stacks simultaneously, and merge them as CI passes)

3. Batching (run CI and merge batches of stacks at a time, instead of one-by-one)

CI Optimization is available regardless of if you use the Graphite merge queue. It lets you skip running CI on mid-stack PRs when updates to other PRs in the stack trigger rebases.

Note that a "stack" can be a single PR.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a567c9f-1732219799-pika-1732219769508-1x.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a1a97b33d8380c59ad3b4875a7b51f91" data-og-width="1196" width="1196" data-og-height="1128" height="1128" data-path="images/2a567c9f-1732219799-pika-1732219769508-1x.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a567c9f-1732219799-pika-1732219769508-1x.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e910cef5c48a36b53e11916790ca593a 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a567c9f-1732219799-pika-1732219769508-1x.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7ec9d8c07ed2d9f36f98fde4e9d0b688 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a567c9f-1732219799-pika-1732219769508-1x.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4b664b1bec783e6ecd0ad4cbce55b072 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a567c9f-1732219799-pika-1732219769508-1x.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a5ddd761bc5c7915e2c633d8e4d2d8c6 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a567c9f-1732219799-pika-1732219769508-1x.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b835be7e01e06473889a5b2cd808202b 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a567c9f-1732219799-pika-1732219769508-1x.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2a81fe45290ccbad55f308dbe85defdb 2500w" />
</Frame>

## Running CI on multiple *PRs* in a stack in parallel (fast-forward merge)

Process CI on all PRs in a stack in parallel. We highly recommend keeping this setting enabled.

## Running CI on multiple *stacks* in parallel

For even faster merges, you can run CI on multiple stacks at the same time. Paired with fast-forward merging, this means you're processing PRs in each stack in parallel *and* processing the larger unit of stacks

Parallel CI speeds up your merge queue by running your CI checks in parallel for multiple stacks (including individual PRs not part of a stack) at once, without compromising on correctness. This is especially helpful if your repo sees a high volume of PRs, long CI times, or both.

<Tip>
  Companies who have enabled Parallel CI on their Graphite Merge Queues have seen **1.5x faster merges**, which includes time spent running CI (33% decrease for p95, 26% for p75).

  Orgs heavily using stacked PRs can expect to see even greater speed gains. Customers have seen up to **2.5x faster merges** (60% decrease for p95, 34% decrease for p75).
</Tip>

### How running CI in parallel works

Parallel CI uses speculative execution, similar to branch prediction, to run CI for multiple enqueued stacks at the same time. This significantly speeds up time-to-merge: instead of waiting for CI to run one-by-one, it can run (for example) 3 at a time. For repos with long queues, this can shorten your time-to-merge to a fraction of the time. In many cases, this brings the expected wait time down to just 1 CI cycle.

### Trading off speed vs. correctness

Graphite’s merge queue operates on stacks as the primary unit rather than a PR (where single PR’s are equivalent to a stack of size 1), and this applies to parallel CI as well. If any PR in the stack encounters a failure, the whole stack will fail to merge, allowing you to treat stack merges as atomic operations.

When setting up parallel CI mode, you can choose whether to:

* **Run CI on each PR in the stack individually**. This is the highest level of correctness guarantees: it ensures no PR in your stack would independently break trunk.

* **Run CI on the topmost PR in the stack.** This relaxes CI guarantees, while further reducing CI runs. If you require each merged stack to keep trunk green, but don’t have that same strictness for each PR within a stack, then we recommend this mode for a combination of higher speed and lower CI costs.

### Example of running CI in parallel

Suppose you’ve configured Graphite to run up to 3 parallel CI runs, and you have 5 unrelated stacks enqueued at a similar time: `A`, `B`, `C`, `D`, and `E`.

1\. CI starts for `A`. In parallel, Graphite creates these temporary groupings and starts CI at the same time:

* `A` ← `B` (i.e. `B` rebased on `A`), thereby testing this group of 2 PR’s at once

* `A` ← `B` ← `C`, thereby testing this group of 3 PR’s at once

2\. Once `A` succeeds, it’s merged.

* Graphite then starts CI for the grouping: `B` ← `C` ← `D`, thereby testing this group of 3 PR’s at once.

3\. Once `B` succeeds, the same process repeats: a group for `C` ← `D` ← `E` is created and CI runs.

4\. If at this point `C` fails, then:

* `C` is evicted from the queue.

* The runs for groups `C` ← `D` and `C` ← `D` ← `E` are both canceled.

5\. `D` then becomes the first PR in the queue:

* CI starts for `D`.

* Graphite starts CI for the grouping: `D` ← `E`.

If your CI tests aren’t flaky, the cost is low and the benefits are high: parallel execution only runs more CI when CI fails in the merge queue.

However, because parallel CI assumes that your CI tests in the merge queue will pass, be careful with flaky tests. If CI tests fail, you not only need to evict the failing PR, but restart CI runs on any subsequently enqueued PR’s with speculatively running CI. While this doesn’t make your time-to-merge any slower than when parallel CI is disabled, it does generate more CI runs.

### Enabling parallel CI

**Prerequisites**:

* You must allow the `graphite-app` bot in GitHub to bypass merge restrictions, via your existing branch protection rules or rulesets. See how to set up this up [here](/set-up-merge-queue#bypass-pr-permissions)

* Your repo must support [draft PR's](https://github.blog/2019-02-14-introducing-draft-pull-requests/)

**To enable:** go to *Merge queue* in [your Graphite app settings page](https://app.graphite.com/settings/merge-queue), and:

1. If you haven't already, [enable the Graphite merge queue](/set-up-merge-queue#enable-the-graphite-merge-queue-for-your-repository) in your repo

2. If you already have the merge queue enabled in the repo, find it in the list and click the **Edit** icon

3. In the merge queue configuration panel, enable **Parallel CI**

4. Select an option for **How should CI run?** - see the section above for more details.

5. Specify a **Concurrency** value, which determines the number of stacks to run CI for in parallel

<Tip>
  Not sure which concurrency value to use? You'll get the most benefit by from having enough concurrent runs to handle your PR volume given your typical CI runtimes. For example, if your CI takes 30min, and your peak hour PR volume is 3 PR's per 30min, 3 concurrent runs will give you the most benefit.

  If your tests are flaky, you may want to start lower and then gradually increase it as you see how your CI performs.
</Tip>

### End-user experience when using parallel CI

In order to implement this strategy, Graphite groups stacks into a temporary draft PR. This draft PR is used to execute CI runs. The Graphite PR page will point you to this draft PR. These PRs’ titles are always prefixed with `[Graphite MQ] Draft PR` to make them easy to identify.

When Graphite groups stacks in the merge queue for running CI, it creates a branch with a predictable prefix: `gtmq_`. You can use this for customizing CI runs or other behavior for enqueued PR’s.

When an enqueued PR merges, it’ll be marked as *closed* in GitHub instead of *merged*. Graphite will render and treat it as *merged* across the product, including the PR inbox, PR page, and statistics shared by Insights. This allows you to keep the GitHub branch protection rule on to require a linear history.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a27d50cbbfe83bf2a376d3ce38ad0146" data-og-width="2520" width="2520" data-og-height="1032" height="1032" data-path="images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=70b8fcc72dac0b4b971f356871424e1d 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=49fdcbde848fbd3280bd09fe307f3fff 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4422d4435116fbf4317483f004af4ecd 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=58cf4a766cdf840cba354908b890047c 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=50ceb5401326fa9ff023aebec880f746 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/8278df1d-1709237882-screenshot-2024-02-29-at-3-17-49-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=5a8e25888b58b98050f06919540c0107 2500w" />
</Frame>

### Further reading about parallel CI

* Read more about [speculative execution](https://www.uber.com/blog/bypassing-large-diffs-in-submitqueue/) in Uber's paper

* If you use tools that monitor whether the PR is merged, your integration may stop working. Many tools have options to monitor merged commits rather than PR status: for example, see [Linear's guide on linking commits](https://linear.app/docs/github#link-using-commits).

## Running CI on multiple *groups* of stacks in parallel (batching)

<Note>
  This feature is available in private beta. Please [contact support](https://graphite.com/contact-us) for access.
</Note>

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a679334-1732229774-pika-1732225950829-1x.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2f00e34fbf5cda622c2f0b77fd07bde4" data-og-width="1142" width="1142" data-og-height="960" height="960" data-path="images/2a679334-1732229774-pika-1732225950829-1x.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a679334-1732229774-pika-1732225950829-1x.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=5e96d9981bf8ec0c6d1bc3287b401da8 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a679334-1732229774-pika-1732225950829-1x.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2d0c5b7f9cc6b9ede961553834aa00a3 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a679334-1732229774-pika-1732225950829-1x.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c0a539d1b0b8293a6ca2d99ef0dc6662 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a679334-1732229774-pika-1732225950829-1x.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e505eeb052cc2fab1058da41c6eeb793 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a679334-1732229774-pika-1732225950829-1x.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d8ba5ec6f6d738545680ff2bb90d6d78 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/2a679334-1732229774-pika-1732225950829-1x.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=3f9be967f31f0904966de986c3265db4 2500w" />
</Frame>

To increase merge queue throughput and speed up merges, the Graphite merge queue also supports processing groups of stacks simultaneously.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b98850c1-1738093764-image.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=11769854ace1d16bf954b90e2b3acf69" data-og-width="1560" width="1560" data-og-height="880" height="880" data-path="images/b98850c1-1738093764-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b98850c1-1738093764-image.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=38391682b5aeda63eb5de664ebebe2ec 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b98850c1-1738093764-image.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=6123e216a6beaaaf06212ac1705a938b 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b98850c1-1738093764-image.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=de983f175ef33d84d5b4514c989d5b29 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b98850c1-1738093764-image.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1e2558adf61cdda55ecb139236b5c40d 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b98850c1-1738093764-image.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f1bf367e877da66829bb92e1f4a77861 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b98850c1-1738093764-image.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=84dedaa38fbd0e413d8314edad899ae9 2500w" />
</Frame>

When a batch merge fails, Graphite can automatically handle the failure by identifying the offending change:

<Steps>
  <Step title="The system identifies which stacks in the batch caused the failure by running CI on smaller subsets of the batch" />

  <Step title="Stacks that pass CI are automatically added back to the merge queue to continue processing" />

  <Step title="Stacks that fail CI are identified and removed from the queue" />
</Steps>

This process ensures that even if only one stack in a batch causes issues, the other stacks can still merge without manual intervention.
Two strategies are supported:

1. Full parallel isolation (default): By checking every stack in the batch in parallel, the problematic stacks are identified quickly.

2. Bisection: By using a bisection approach, problematic stacks are identified efficiently with fewer CI runs, as each iteration verifies half of the remaining stacks as safe.


# Merge A Stack Of PRs Manually
Source: https://graphite-58cc94ce.mintlify.dev/docs/merge-stack-prs-github

Learn how to merge a stack of PRs outside of Graphite.

## Merge a stack manually

<Note>
  For the best experience, we recommend merging a stack of pull requests [through Graphite stack merge](/merge-pull-requests).
</Note>

Merging with stack merge in the Graphite app saves a substantial amount of time. However, if you'd like to manually merge your PRs, merge the PRs in the stack one at a time:

<Steps>
  <Step title="Merge">
    Merge the bottom PR of your stack into your trunk on the [Graphite app](https://app.graphite.com/) (or through GitHub).
  </Step>

  <Step title="Sync">
    Run `gt sync` from any branch of your stack to pull `trunk` to local, delete the merged branch, and restack the rest of your stack on `trunk`.
  </Step>

  <Step title="Submit">
    From any branch in your stack, run `gt submit` to force push the restacked branches so the new bottom of your stack can be merged into `trunk`.
  </Step>

  <Step title="Repeat until you've landed all of the branches in your stack." />
</Steps>

<Note>
  We recommend always merging from the bottom of the stack. While there are other techniques, we've found that this is the most intuitive and safest model for our users.

  Merging in reverse order from the middle or top of the stack and collapsing all of the PRs into one is the **fastest** way to merge an entire stack, but there are a number of pitfalls for users—namely around syncing this merged state locally (to continue developing on any upstack PRs) or undoing these changes if a user decides not to merge a PR. This may lead to perilous situations where users have felt like they've lost code or can't re-create their previous state.

  While certainly not impossible, it's also harder to re-derive the original stack of PRs when looking at the `git` history.
</Note>


# Merge When Ready
Source: https://graphite-58cc94ce.mintlify.dev/docs/merge-when-ready

Learn how to automatically merge PRs with Graphite once all branch protection rules have been met.

*Merge when ready* is Graphite's equivalent to GitHub's [automerge](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request). By enabling merge when ready on a single PR or a stack of PRs, you're granting Graphite permission to merge the PR(s) after all branch protection rules have been met.

<Info>
  Merge when ready is only supported for merges into the default branch of your repo. If you use a multitrunk setup, make sure you are enabling merge when ready for PRs that you intend to merge into the default branch.
</Info>

## Enable merge when ready for a single PR

To enable merge when ready for a PR, activate the toggle next to the merge button.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8ca58d43-1695090211-frame-10123063.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=678752980eda997d0e281ce0d3869482" data-og-width="1294" width="1294" data-og-height="206" height="206" data-path="images/8ca58d43-1695090211-frame-10123063.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8ca58d43-1695090211-frame-10123063.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1e6f82bfa862ce64f1dc8f8fb1482da0 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8ca58d43-1695090211-frame-10123063.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=dc04af285e7350fc7bdc56b3bef7bfca 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8ca58d43-1695090211-frame-10123063.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=be4918c36d27557073b969816b1b6232 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8ca58d43-1695090211-frame-10123063.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=26345d51d669005b1750d7d4f3fd3cbd 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8ca58d43-1695090211-frame-10123063.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=bd0ca586f169793ac78f72261d131f3c 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8ca58d43-1695090211-frame-10123063.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4f1e94ec049ca2fb1f07b5ddb11d78f1 2500w" />
</Frame>

<Info>
  Merge when ready is only available if the PR is in a non-mergeable state. If the PR is mergeable, the merge when ready toggle will be disabled.
</Info>

## Enable merge when ready for a stack

You can quickly enable merge when ready for a stack by navigating to the top-most PR in the stack and toggling on merge when ready for that PR. Graphite will show you a confirmation modal asking whether or not you want to enable merge when ready on all downstack PRs.

<Note>
  Downstack PRs that have "merge when ready" enabled will merge whenever they individually become ready to, such as once they are approved and required CI checks have passed. They will not wait for or require any upstack PR to also be ready before merging.
</Note>

Graphite will show the same confirmation modal when disabling merge when ready for any PR in the middle or top of a stack.


# Mergeability Status Check
Source: https://graphite-58cc94ce.mintlify.dev/docs/mergeability-status-check

Prevent accidental mid-stack merges.

### Mergeability status check on GitHub

To help prevent accidental mid-stack merges, Graphite creates an optional status check on GitHub for upstack PRs. This status check appears as "in progress" for all upstack PRs, and passes for all base PRs.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=27642ae19c6d5c965d23e134ceb7f8de" data-og-width="1640" width="1640" data-og-height="70" height="70" data-path="images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=003a082a1871d7d5846b429b18e69fc1 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=122b703080d5dc0b4880da30e95cec86 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=9608298d4e114ea2c41fa001e86f96e7 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=37b7d175cac513abe4f721db73956e9c 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f137fe58a8cf6646db8c432834aed052 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8d80d3f4-1738275171-screenshot-2025-01-30-at-17-02-27.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=138dfc57dad42157ef3083c5f29ac994 2500w" />
</Frame>

Since it's an optional check, you can still merge mid-stack if needed.

To configure this status check for your GitHub org:

* Open the Graphite web app's settings page

* Select the "Mergeability checks" page

* Edit the `Mergeability check on GitHub` setting


# Develop On Multiple Trunk Branches
Source: https://graphite-58cc94ce.mintlify.dev/docs/multiple-trunks

Learn how to develop against multiple trunk branches with the Graphite CLI.

Some codebases don't have a single trunk branch (e.g. all commits go to `main`), but rather multiple longer-lived trunk branches. Some reasons for this workflow may be release/deploy branches, long-lived feature branches, or staging branches. In these setups, creating branches and PRs off the correct trunk branch is critical for many reasons:

* **Developing:** The output of `gt ls` will be clearer, e.g. running `gt ls` on `main` will show stacks based on `main`.

* **Reviewing:** Requirements like CI status will be evaluated against the trunk branch's branch protection rules on Graphite's PR page. This is especially useful for upstack PR's, where Graphite evaluates requirements like CI against trunk.

* **Merging:** Graphite's [Merge feature for stacks](/merge-pull-requests) will merge down to the correct trunk branch.
  <Note>[Merge When Ready](/merge-when-ready) is only supported for merges into the default branch of your repo. Make sure you are enabling Merge When Ready only for PRs that you intend to merge into the default branch.</Note>

The guide below shows you how to use Graphite for such projects.

## Prerequisites

Your CLI version should be >= `1.4.0`. If you are on a lower version, [update your CLI version](/update-cli) to get the latest first-class support for multitrunk workflows.

You should be familiar with how to:

* [Create branches in a stack](/create-stack)

* [Create and submit pull requests](https://graphite.com/create-submit-prs)

<Info>Graphite treats each configured trunk independently and can only merge stacked PRs into their trunk. Performing trunk-to-trunk merges, such as updating a long-lived feature trunk with changes from a main trunk or vice-versa, is outside Graphite's scope and users can continue using their own `git` or CI workflow to handle this without conflicting with Graphite.</Info>

## Creating PRs off different trunks

The trunk branch is the root of your stack that you open PRs against and eventually merge into. When you first initialize the CLI in a repo, Graphite will ask you to select a trunk branch. In the following tree, `main` is the trunk and all the stacks are based off it. Each branch has a single dependency so each stack can only have a single trunk.

```bash Terminal theme={null}
◯    bug-fix
│ ◯  feature1-frontend
│ ◯  feature1-backend
◉─┘  main
```

In order to create a PR off a different trunk branch, you need to configure the branch you want to base off of as another trunk. Then you can check out that other trunk branch and create new branches off it. When you submit PRs for the branches based off other trunks, they will be based off these other trunks. The Graphite workflow is the same across trunks and Graphite now makes working with multiple trunks easy.

For example, say you had a release branch `release-v10` that you needed to merge a bug fix into. You would first need to add `release-v10` as a trunk branch. Then you can checkout the new trunk with `gt checkout release-v10`. Once you've implemented your fix, you can use `gt create` to create a branch for it in the same way as any other branch. You can then submit a PR for the bug fix which will open a PR against the trunk `release-v10`. Your state will now look like the following:

```bash Terminal theme={null}
◯    bug-fix-1
│ ◯  feature1-frontend
│ ◯  feature1-backend
◯─┘  main


◉  bug-fix-2
◯  release-v10
```

To switch back to working off of `main`, simply checkout `main` again with `gt checkout main`. Graphite supports easily switching between branches, even across trunks.

The next sections go into detail about how to add additional trunks and work with multiple trunks.

## Configuring trunks with the CLI

When you first initialize the CLI in a repo, Graphite will ask you to select a trunk branch.

```bash Terminal theme={null}
Welcome to Graphite!


? Select a trunk branch, which you base branches on - inferred trunk main (autocomplete or arrow keys) ›
❯   main
    release-v10
    green
```

After initial set up, you can then interactively configure what trunk branches you have configured via `gt config`:

Run `gt config`:

```shell  theme={null}
gt config
```

Select `Repository-level settings` then `Trunk branches`:

```bash Terminal theme={null}
? What would you like to configure? › - Use arrow-keys. Return to submit.
❯   Repository-level settings
    Branch naming settings
    Submit settings
    Restack settings
    Default utilities
    Tips
    Yubikey reminders
    Exit
```

```bash Terminal theme={null}
? Repo-level configuration › - Use arrow-keys. Return to submit.
❯   Trunk branches
    PR Templates
    Remote repository
    Back
    Exit
```

See your currently configured trunk branches, and the different options for configuring trunk branches:

```bash Terminal theme={null}
? Configured trunks:
        main
        release-v10
 › - Use arrow-keys. Return to submit.
❯   Add additional trunk branch
    Remove configured trunk
    Configure a target trunk to open PRs against
    Back
    Exit
```

### Adding an additional trunk branch

From the interactive menu, select `Add additional trunk branch`:

```bash Terminal theme={null}
? Configured trunks:
        main
        release-v10
 › - Use arrow-keys. Return to submit.
❯   Add additional trunk branch
    Remove configured trunk
    Configure a target trunk to open PRs against
    Back
    Exit
```

Select the branch you want to configure as a trunk:

```bash Terminal theme={null}
? Select a trunk branch, which you base branches on (autocomplete or arrow keys) ›
     main
     develop
❯    release-v10
```

You can also add an additional trunk branch non-interactively by using the `--add` flag with the [gt trunk](/command-reference#gt-trunk) command:

```bash Terminal theme={null}
gt trunk --add <trunk-name>
```

### Removing a configured trunk branch

**Note that removing a configured trunk may un-track all branches based locally on this trunk.**

From the interactive menu, select `Remove configured trunk`:

```bash Terminal theme={null}
? Configured trunks:
        main
        release-v10
 › - Use arrow-keys. Return to submit.
    Add additional trunk branch
❯   Remove configured trunk
    Configure a target trunk to open PRs against
    Back
    Exit
```

Select the configured trunk you would like to remove:

```bash Terminal theme={null}
? Which configured trunk would you like to remove? ›
❯   main
    deploys
```

### \[Optional] Configuring a target trunk to open PRs against

**This is a not a common workflow and usually only used in workflows where you work off a branch locally (i.e. \*\***`green`\***\*) that is strictly a descendant of the branch they merge into (i.e. \*\***`main`\***\*)**. Targeting a different branch on remote than the one you have locally can otherwise have unknown consequences in the Graphite CLI.

By using this setup, you are choosing to open PRs against a different trunk than the one you work on locally. This means that you can base your branches off `green` locally and have all PRs submitted through Graphite open PRs against another branch, `main`.

From the interactive menu, select `Configure a target trunk to open PRs against`:

```bash Terminal theme={null}
? Configured trunks:
        main
        release-v10
 › - Use arrow-keys. Return to submit.
    Add additional trunk branch
    Remove configured trunk
❯   Configure a target trunk to open PRs against
    Back
    Exit
```

Select the local trunk you would like to set a target trunk for:

```bash Terminal theme={null}
WARNING: You are about to configure Graphite to open PRs against a different remote branch than the one you are based on locally.
WARNING: This is an uncommon workflow since most users develop locally based off the same branch they are merging PRs into.
WARNING: This workflow is only recommended if your local branch is a descendant of the remote target.
? Which configured trunk would you like to set a target trunk for? ›
❯   green
    release-v10
```

Select the remote branch you would like to open PRs against on remote (by default, Graphite opens PRs against the same trunk you have set locally):

```bash Terminal theme={null}
? For branches based on main, which remote branch should Graphite open PRs against?
By default, PRs will be opened against main on remote. ›
    green (default)
❯   main
    release-v10
```

## Working with multiple trunks

By default, all Graphite commands assume you are working off a single trunk. For times when you want to do things across multiple trunks, some commands have a `--all` flag to see/perform actions across all configured trunks. Everything else should work normally.

### Seeing your configured trunks

`gt trunk` will print out the trunk your current branch is based off of:

```bash Terminal theme={null}
> gt trunk
main
```

`gt trunk --all` will print out all your configured trunks:

```bash Terminal theme={null}
> gt trunk --all
main
deploys
```

### Seeing your stacks across trunks

`gt log [short]` will show you your stacks on your current trunk:

```bash Terminal theme={null}
> gt log short
◉    bug-fix
│ ◯  feature1-frontend
│ ◯  feature1-backend
◯─┘  main
```

`gt log [short] --all` will show you all your stacks across all your configured trunks:

```bash Terminal theme={null}
> gt log short --all
◉    bug-fix-1
│ ◯  feature1-frontend
│ ◯  feature1-backend
◯─┘  main


◯    bug-fix-2
│ ◯  bug-fix-3
◯─┘  release-v10
```

### Checking out branches across trunks

`gt checkout {branch_name}` will work with any Graphite tracked branch, regardless of the trunk it is based off of.

In the interactive selector, `gt checkout` will by-default only show you options based off your current trunk.

```bash Terminal theme={null}
> gt checkout
? Checkout a branch (autocomplete or arrow keys) ›
❯   ◯    bug-fix-1
    │ ◯  feature1-frontend
    │ ◯  feature1-backend
    ◯─┘  main
```

Add the `--all` flag to see all branches across all configured trunks.

`gt checkout --all`:

```bash Terminal theme={null}
> gt checkout --all
? Checkout a branch (autocomplete or arrow keys) ›
❯   ◯    bug-fix-1
    │ ◯  feature1-frontend
    │ ◯  feature1-backend
    ◯─┘  main (trunk)
    ◯    bug-fix-2
    │ ◯  bug-fix-3
    ◯─┘  release-v10 (trunk)
```

### Moving branches across trunks

Similar to `checkout`, `gt move --onto {branch_name}` will work with any Graphite tracked branch, regardless of the trunk it is based off of. Add the `--all` flag to see all branches across all configured trunks.

### Syncing branches across trunks

By default, `gt sync` will only update the trunk you are currently based off of and sync branches based off this current trunk. To update all your trunks and sync branches based off all your trunks at once, pass the `--all` flag.

## Troubleshooting

**PR is targeting the wrong trunk.** You can fix this by simply moving the branch onto the correct trunk: `gt move --onto {trunk}`. After that, you can submit your stack to reflect the changes remotely. Learn more about [tracking branches with gt track](/track-branches).

## Versions before 1.4.0

Before `1.4.0`, Graphite only supported working off a single trunk at a time. So to switch trunk branches, you had to re-initialize the CLI with a different trunk every time you needed to switch which trunk you were working off of:

```bash Terminal theme={null}
gt init --trunk <trunk-name>
```

There was no real support for working on multiple trunks simultaneously.


# Navigate A Stack
Source: https://graphite-58cc94ce.mintlify.dev/docs/navigate-stack

Learn how to navigate stacked branches with the Graphite CLI.

## Prerequisites

To navigate a stack of branches with the Graphite CLI, make sure you've:

* [Installed and configured the CLI](/install-the-cli)

* [Authenticated with GitHub](/install-the-cli#authenticating-the-cli)

* [Initialized `gt`](/initialize-in-a-repo) in a repo of your choice

* [Created](/create-stack) or tracked a branch/stack of branches

## `gt log`

You can use `gt log` to view the current state of your repository:

```bash Terminal theme={null}
> gt log


◉ pp--06-14-part_3 (current)
│ 8 seconds ago
│
│ 95338df - part 3
│
◯ pp--06-14-part_2
│ 8 seconds ago
│
│ 95610c6 - part 2
│
◯ pp--06-14-part_1
│ 27 seconds ago
│
│ 48cd85e - part 1
│
◯ main
│ 5 weeks ago
│
```

### Check out a branch

Branches in Graphite are just `git` branches under the hood—you can check them out with native `git`, but the easiest way is to use `gt checkout`:

```bash Terminal theme={null}
# checkout pp--06-14-part_1
gt checkout pp--06-14-part_1


# even easier, use the alias!
gt co pp--06-14-part_1
```

If you aren't sure which branch you want to checkout, you can also use `gt checkout` (or `gt co`) in interactive mode:

```bash Terminal theme={null}
> gt co


? Checkout a branch (autocomplete or arrow keys) ›
    pp--06-14-part_3
    pp--06-14-part_2
❯   pp--06-14-part_1
    main
```

Now, you can see in `gt log short` you're on `part_1` as intended:

```bash Terminal theme={null}
> gt ls


◯  pp--06-14-part_3
◯  pp--06-14-part_2
◉  pp--06-14-part_1
◯  main
```

### Move up and down a stack

Sometimes you want to move to the branch directly above or below the current branch in a stack. The `gt up`, `gt down`, `gt top`, and `gt bottom` commands help make this possible.

Since `gt bottom` takes you to the bottom-most branch in your stack not including your trunk branch, you can use `gt checkout --trunk/-t`, which always takes you to your `trunk` branch (e.g. `main`):

```bash Terminal theme={null}
# check out the branch directly upstack (in this case part_2)
gt up
#alias for branch up
gt u


# check out the branch directly downstack (in this case back to part_1)
gt down
#alias for branch down
gt d


# move multiple branches at a time (up to part_3)
gt up 2
# alias for branch up 2
gt u 2


# move multiple branches at a time (back to main)
gt down 3
# alias for branch down 3
gt d 3


# move to the tip of the stack (back to part_3)
gt top
# alias for branch top
gt t


# move to the base of the stack, not including trunk (to part_1)
gt bottom
# alias for branch bottom
gt b
```

<Note>
  If you find yourself navigating a complex stack where there are multiple children of a particular branch, `gt up` and `gt top` will ask which child branch you'd like to checkout if there's ever ambiguity.
</Note>


# Onboarding FAQs
Source: https://graphite-58cc94ce.mintlify.dev/docs/onboarding-troubleshooting

Answers to common questions when getting started with Graphite.

## Having issues selecting a repository owner?

If you don’t see your desired owner in the list of owners in the Graphite onboarding flow and know that the Graphite GitHub App isn’t installed on the owning account, you should follow the instructions underneath the list of owners starting with `Don't see what you're looking for above?`. If you know that the Graphite GitHub App is installed on your organization, you should click the `Authenticate Graphite App` button.

If you're [a collaborator on a personal repository](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository) that you'd like to use with Graphite, you must install the Graphite GitHub App on your personal account.

If you're still unable to select your desired repository owner, contact us at **[support@graphite.dev](mailto:support@graphite.dev)**.

## Don't see the repository you're looking for?

You can choose which repositories within your organization you want the Graphite GitHub App to have access to. If you don't see a certain repo in the repository selector in the Graphite Web App, it's likely that you haven't granted the Graphite GitHub App access to those repositories. You can do so in the GitHub App settings within your organization. (The URL will look like this: `https://github.com/{orgname}/settings/installations`)

If you're using a Personal Access Token to onboard with Graphite and you don't see repositories for that organization, there are two possibilities:

1. Your organization may use SAML SSO, so you must authorize the token after it's been created for it to have access to that organization's resources. See [GitHub's instructions](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

2. The organization has restricted access to resources for classic PATs. See more about this on [GitHub's documentation](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#restricting-access-by-personal-access-tokens-classic), and you can reach out to an organization owner to find out if they can lift this restriction.

If you're a collaborator on a private personal repository, then the owner of the repository must also install the Graphite GitHub application on their personal account in order to select the repository in Graphite. You can also authenticate with a Personal Access Token to see private repositories, but installing the Graphite GitHub App is recommended.

## Why is Graphite asking to act on my behalf?

You have arrived at this step because:

1. The Graphite App is installed on your organization but you don’t see it in the organizations list

2. You clicked `Add organization from GitHub` and the organization had the word `Configure` next to it in this list (indicating that the app is already installed on the organization)

This primarily treats the case where a new user is onboarding with Graphite and wants to join an organization that **already has the Graphite App installed.** Once you click this button, you will see a confirmation modal saying that we will redirect you to GitHub to authorize the Graphite App along with a special note that if you do so, **the Graphite App will only have access to the organizations on which it's installed**.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4e22e8aea1a15e73c7e4457b1920a343" data-og-width="1350" width="1350" data-og-height="1246" height="1246" data-path="images/d7298895-1700536958-frame-10123321.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a9f5dcbde123335bb996ed1d77b9ba62 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4b44bbfe98e2b2ef957bd487368d6527 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=041c0dddd9e0ecb4ef2ddc42a0d34ef1 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=db7b50dfc2aa71ee049580a701a9a6db 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ebee02ca922b1fcee9eaaeafba17c4ae 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/d7298895-1700536958-frame-10123321.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a5ff45cf54003ebd1dd5dc623349c4bd 2500w" />
</Frame>

This button only appears if you haven’t already authenticated the Graphite App. Once you do so, you will return to the organization selection screen and see your desired organization.

## Why are all my GitHub organization's repositories saying `Missing permissions` in Graphite UI, or `gt` CLI saying I need to join a team?

You may have been removed from the GitHub organization. Check this with the organization's GitHub administrators.

If you have not been removed and the organization uses [SAML SSO authentication](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/about-authentication-with-single-sign-on), ensure that your GitHub user account also has an active SAML session with your organization.


# Setting Up A Proof Of Concept
Source: https://graphite-58cc94ce.mintlify.dev/docs/onboarding-your-team

Best practices for teams new to stacking with Graphite.

Stacking is a team sport - here are some proven ways to help your team start stacking with Graphite successfully.

### Try Graphite as a team

It can be difficult to get all of your engineers to adopt a new workflow at once. A good way to ease your company into Graphite is to start with a group of 5–10 engineers who commit to using it together, preferably on the same team. This way there are enough engineers to experience the collaborative benefits of Graphite, and you can take the lessons learned from that group and apply them to the rest of the engineering organization.

### Evaluate for at least 4 weeks

Commit to using Graphite for at least one month as a team - this gives everyone enough time to acclimate to the tool and adapt their workflows.

### Define success criteria

Pick some heuristics to help identify how your team is trending. [Graphite Insights](/insights) provides plenty of data to gauge and improve developer productivity. When starting out, it’s useful to monitor:

* *Median PR size*: When your team starts stacking, their PRs should get smaller.

* *Median wait time to first review*. PRs should be reviewed quickly, which is typically indicative of right-sized PRs and good team patterns. You want this number to stay stable or decrease over time.

* *Average number of review cycles until merge*: PRs that are merged quickly are indicative of quick PR review cycles, which is representative of good collaboration practices. PRs that are self-contained are easier to review and limit the duration of iteration cycles and issues with merging. The longer it takes a PR to merge, the likelier it is to create more merge conflicts. You want this number to stay stable or decrease over time.

* *Total PRs merged*: Small PRs get merged faster. You should see this number increasing as your team gets more familiar with stacking and using Graphite.

### Emphasize high-leverage features

Graphite is designed to make engineers more efficient at every turn. Here are a handful of Graphite features that tend to show the most immediate impact:

* [Stacking in the CLI](/create-stack): Quickly create stacks with the CLI.

* [Merge a stack](/merge-pull-requests): Use Graphite’s automated solution to merge a stack of PRs.

* [PR review capabilities](/review-proposed-changes): Comment on unchanged lines of code, unresolved threads, and suggested edits.

* [PR versions](/pull-request-versions): See and compare versions of a pull request to keep track of the history of a PR.

* [VS Code extension](/vs-code-extension): This is especially useful for engineers who are less comfortable using a CLI.

* [PR inbox](/use-pr-inbox): Even dedicated CLI users can find value in using the PR inbox to quickly see the state of their PRs, which ones need their attention, and have the ability to customize their inbox filters and layout.

* [Notifications](/slack-notifications): Get PRs reviewed quickly by integrating with Slack. Receive real-time notifications and approve, comment, or request changes on a PR directly from Slack.


# Pricing FAQ
Source: https://graphite-58cc94ce.mintlify.dev/docs/pricing-faq

Your pricing questions, answered.

### **I need help convincing my team to pay. What should I do?**

We have plenty of resources for Graphite champions. Here are a few:

* Documentation on **[why your team should use Graphite](https://graphite.com/docs/why-you-should-use-graphite)**
* Case studies that show [**how Graphite improved developer productivity**](https://graphite.com/customers) at Asana, Ramp, and Shopify.
* [**Schedule a Graphite demo**](https://graphite.com/contact-us) for your team!

### **Do you have an individual tier?**

We have a Hobby tier on personal repositories with these features:

* GitHub sync with personal repos
* Inbox/Notifications
* CLI/VSCode/MCP
* AI PR titles and descriptions
* Limited AI Chat
* Limited AI reviews

### **When does my trial end?**

Your trial ends either 30 days after it began or when you upgrade, whichever comes first.

### **What happens if my trial ends, and I haven’t upgraded?**

If one of your trials ends and you haven’t upgraded to the **Starter** or **Team** plans, your workspace will lose access to Graphite features. If you're using Graphite with your personal repositories, your workspace will be placed into the free **Hobby** tier which gives you limited access to Graphite.

### **What Graphite features are available for each tier?**

You can find a breakdown of features in the **Starter**, **Team**, or **Enterprise** plans in the pricing and plans doc or our pricing page.

### Does Graphite offer plans for startups?

Early stage startups can apply to our Startup plan. If you’re eligible, you’ll receive a \$1500 credit (6 months of Team for ≤ 5 seats). After your credit expires (or is used), you’ll be automatically upgraded to the **Team** plan.

You can read more about the Startup plan [here](https://graphite.com/docs/graphite-for-startups).

### **My project is open source and doesn’t have significant funding. Can I use Graphite for free?**

Reach out to our team at [support@graphite.dev](mailto:support@graphite.dev) to check your eligibility. Please include the link to the GitHub org, link to the website, and a brief description of the project.

### **What payment methods do you accept?**

We accept payment for the Starter and Team plans via credit card. Billing is managed via Stripe.

### Can someone who doesn’t use Graphite pay for my subscription?

Yes. Click `Select a plan` in organization billing settings for the product you wish to purchase. Then, copy the URL of the Stripe portal (starts with `https://billing.graphite.com`), and send it to whoever is making the purchase.

### **How do I purchase a specific number of seats?**

As you add members to your team, Graphite will automatically calculate the number of seats to bill. We do not currently support adding “empty” seats to a team or setting a seat cap. Admins can manage seats by manually adding and removing users.

### **Who is on my Graphite team?**

Anyone who joins your workspace on Graphite or is reviewed by Graphite's reviewer is considered part of your team.

### **What is “advanced” Merge Queue?**

If you have sophisticated merge queue needs that aren’t met by the Team plan, reach out to our sales team to learn more.


# Privacy & Security
Source: https://graphite-58cc94ce.mintlify.dev/docs/privacy-and-security

Learn how Graphite prioritizes security to safeguard your source code.

To achieve our mission to build state-of-the-art developer tools, Graphite values security above all else. We are SOC 2 Type II compliant, passing a rigorous auditing procedure established by the American Institute of Certified Public Accountants (AICPA). SOC 2 Type II assesses non-financial reporting controls across five areas: security, availability, processing integrity, confidentiality, and privacy. We also continuously pen test. [Learn more](https://graphite.com/privacy) about our security practices.

<Note>
  Unlike SOC 2 Type I certification, which focuses on a company’s controls at a specific point in time, Type II goes further. It evaluates how effectively these controls operate over an extended period of typically six months or more. For our enterprise users, this certification streamlines the vendor due diligence process. If you have questions about our security policies or want to request a copy of our SOC 2 Type II report, reach out to our security team at [support@graphite.dev](mailto:support@graphite.dev).
</Note>

## Permissions requested by the Graphite GitHub App

We recommend authenticating via the Graphite GitHub App when you first create your Graphite account, which allows your organization to grant Graphite access on a repo-by-repo basis.

The Graphite GitHub App asks for the following permissions:

* `Read & write: actions, checks, contents, pull requests, workflows`

  * Used to create, display, update, and merge PRs with Graphite

* `Read: administration, commit statuses, deployments, issues, metadata`

  * Used to display PRs and their relevant statuses and metadata on Graphite

* `Read: organization properties, roles, and members`

  * Used to display organization info on Graphite

* `Read: user emails`

  * Used to send transactional emails about Graphite

* `Webhook event subscriptions`

  * Used to keep Graphite's view of GitHub data up-to-date in real time, allowing for best performance of many features (only available with GitHub App authentication)

<Note>
  Depending on your GitHub organization's settings, you may have to "request to add" the Graphite GitHub App—one of your GitHub organization owner will then have to approve the app for use, at which point you'll be able to sign into Graphite.
</Note>

## CLI

When you call `gt submit`, the Graphite CLI pushes the branches in your stack to the remote repository in GitHub directly from the client. Metadata about which branches were pushed to GitHub are sent to Graphite servers so we can open those PRs on your behalf.

## Web app

When you open the app in your browser, it calls GitHub's API directly from the client to retrieve and display pull requests in repositories you have access to according to the filter views you've defined. The only data stored on Graphite servers are basic profile metadata (GitHub ID, username, profile picture) and the auth token generated when you sign in with GitHub, which we use to save your PR filter views and maintain your session.

### User-uploaded media assets

We use a secure domain for hosting all user-uploaded media assets, such as images and videos. If you are using a VPN, or other form of network security that could block network requests, then you may need to allowlist this domain: `https://user-attachments.graphiteusercontent.dev/`.

## AI Summarize

Graphite's AI Summarize feature on the app utilizes Anthropic's API to create summaries of PR changes with the help of artificial intelligence. In order to protect the source code and privacy of our customers and in accordance with [Anthropic's terms of use,](https://support.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training) your source code and PR metadata are not used in training sets.

We've also crafted the feature to be PR-by-PR opt-in; if you don't press the button, your code will not be processed by Anthropic. If you have more questions about this feature, don't hesitate to shoot us a message [on Slack](https://join.slack.com/t/graphite-community/shared_invite/zt-1oiaympp2-R3Oz2DZzycWc1vudtDDvLw) or email [security@graphite.com](mailto:security@graphite.com).

## Logging

During normal usage of the CLI and the website, Graphite will generate and store logs to help us better debug in the event of an error and better understand the profile of our users. Examples of that data include:

* Metadata about your repository: for example, number of branches or counts of Graphite commands being run. We use this to debug failing commands in the CLI (for example, in the past we found that a repository with a very high number of branches would cause the CLI to hang).

* Metadata about your usage: for example, commands being run, command run time, or any CLI errors. We use this to understand where to further our engineering investment and understand how widespread issues are.

* Metadata about your GitHub account: for example, organizations which you're a member of on GitHub. We use this to track the usage of our product and understand what types of organizations we work best for.

## How Graphite keeps your source code safe

We understand how important it is to keep your source code safe. That's why we built Graphite with security and privacy best practices from day one, using encryption in motion and at rest.

### Encryption

Graphite stores GitHub access tokens returned from App authentication logins. These tokens are revokable by both Graphite and the user’s GitHub settings.

We store these tokens in a Postgres database, encrypted in motion and at rest. We also manually encrypt the access tokens using`aes-256-cbc`and decrypt when we read them into server memory. To encrypt/decrypt, we use a secret stored in AWS secret manager.

We additionally encrypt data in our database with a key stored in a different service. So even if the database was compromised, access would not be gained to the Github API tokens.

### Learn more

We're more than happy to provide you with copies of our security-related company policies to give you a better sense of how we approach security at Graphite.

Please email [security@graphite.com](mailto:security@graphite.com) to request copies, or feel free to share your team's security questionnaire if you have a standard format.


# Pull Request Versions
Source: https://graphite-58cc94ce.mintlify.dev/docs/pull-request-versions

Learn how to view history of PR in Graphite using versions.

Graphite uses "versions" of a pull request to keep track of the history of a PR. On first submit, a PR is `v1 `and is incremented each time a PR is updated and submitted through `gt submit`.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c90ccb87-1695079770-frame-10123058.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f37c77b1dfbcf96f9286e309e385c204" data-og-width="1294" width="1294" data-og-height="206" height="206" data-path="images/c90ccb87-1695079770-frame-10123058.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c90ccb87-1695079770-frame-10123058.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=42f4bbae47ef847a04e9d1fc2ac681f0 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c90ccb87-1695079770-frame-10123058.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=30172b57f5e615efce026732036a075e 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c90ccb87-1695079770-frame-10123058.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1d03055211f9eb57efb90e4cd314d451 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c90ccb87-1695079770-frame-10123058.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=feb09d559efeeee3010197e830202604 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c90ccb87-1695079770-frame-10123058.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=aca4f5fffa257a5882fc4b5b909d1848 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/c90ccb87-1695079770-frame-10123058.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=eaf47d01edd3e1617f658f1707f79ae1 2500w" />
</Frame>

## Switch between PR versions

By default, the pull request page shows you a "diff" between `v1` (the initial submitted state of the PR) and `vN`, where `N` is the latest version of the PR. You can toggle between the version you're currently viewing by clicking the versions dropdown and choosing a version for the "right" and "left" sides of the diff.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=51a26eb2367a88cb685d14f2e1981992" data-og-width="2232" width="2232" data-og-height="1114" height="1114" data-path="images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=61e83f2c1d7beed0115885f0a7b1edcd 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=202c5f6e9084bdb49d74ca002c5dae23 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5e241f55dcaee52ab7b450a7a1591618 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a81bc0ddd4caec3417932195e68b6e23 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=bd856def91edaad9b76cd66a0c12f79f 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/918e78a2-1695053397-screenshot-2023-09-18-at-12-09-31-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5dfce70265db9b9c3d22ac3dcda6f27f 2500w" />
</Frame>

### "Hide reviewed changes"

In the event that a pull request is updated *after* you've already reviewed it, you'll see a banner prompting you to `hide reviewed changes`.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7bb373a5-1695053666-changes-since-last-reviewed.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=37832377625c2149c7fd3f0ffc817054" data-og-width="1294" width="1294" data-og-height="206" height="206" data-path="images/7bb373a5-1695053666-changes-since-last-reviewed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7bb373a5-1695053666-changes-since-last-reviewed.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d9439a11b2ebe764afab9592a3b5850a 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7bb373a5-1695053666-changes-since-last-reviewed.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=0b0fc9e8bf7c7a2be6920ae3d8cd67a9 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7bb373a5-1695053666-changes-since-last-reviewed.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d46cc50795efc11569702a90bcc3d21b 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7bb373a5-1695053666-changes-since-last-reviewed.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=981d8bc0a093b3ba38edeb980c04871f 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7bb373a5-1695053666-changes-since-last-reviewed.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=32aa5eb932ce96878bd04bcb7c060771 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7bb373a5-1695053666-changes-since-last-reviewed.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e908a5037a810b0eee9333d54ba6edd8 2500w" />
</Frame>

Clicking `hide reviewed changes` automatically changes your view so you see a comparison between the last reviewed version and the latest version of the pull request.


# Restack Branches
Source: https://graphite-58cc94ce.mintlify.dev/docs/restack-branches

Learn to restack Git branches efficiently with Graphite's CLI.

## Prerequisites

You should be familiar with how to:

* [Create branches in a stack](/create-stack)

* [Visualize a stack](/visualize-stack)

* [Create and submit pull requests](/create-submit-prs)

* [Update mid-stack branches](/update-mid-stack-branches)

* [Sync changes from a remote repository](/sync-with-a-remote-repo)

A key benefit of using Graphite as opposed to vanilla `git` when working with stacks is dependency management for your branches—keeping track of the "parent" of a given branch. When a parent branch changes in some way or is deleted, vanilla `git`, because it does not have this concept of branch dependencies, leaves the parent as-is.

`gt modify` [automatically restacks any dependent branches](/update-mid-stack-branches#automatic-restacking-of-branches) and prompts you to resolve merge conflicts when needed. Another instance that requires branch restacking is after you've [synced changes from a remote repository](/sync-with-a-remote-repo).

Here's the output of `gt log long` to get an idea of what's happening on the `git` level when `gt sync` is unable to automatically restack:

```bash Terminal theme={null}
> gt log long


* ff393d3 - (40 minutes ago) part 1 (#100) - Pranathi Peri (origin/main, origin/HEAD, main)
| * 7ebfd3f - (14 hours ago) part 3 - Pranathi Peri (origin/pp--06-14-part_3, pp--06-14-part_3)
| * 6fe5a7c - (14 hours ago) part 2 - Pranathi Peri (HEAD -> pp--06-14-part_2, origin/pp--06-14-part_2)
| * 4f3f756 - (14 hours ago) part 1 - Pranathi Peri
|/
```

`main` has advanced to the squash-and-merge commit for `part_1`, but `part_2`—even though it is supposed to be based on `main` now—is actually still sitting on the old version of `part_1`.

`gt restack` fixes that. This command, for the current stack, ensures that all branches are based on the current version of their parents.

```bash Terminal theme={null}
Hit conflict restacking pp--06-14-part_2 on main.


You are here (resolving pp--06-14-part_2):
◯ pp--06-14-part_3
◉ pp--06-14-part_2
◯ main


To fix and continue your previous Graphite command:
(1) resolve the listed merge conflicts
(2) mark them as resolved with gt add .
(3) run gt continue to continue executing your previous Graphite command
It's safe to cancel the ongoing rebase with `gt abort`
```

Resolving merge conflicts during a restack is performed the same way as amending or creating a new commit on a branch in the middle of a stack:

```bash Terminal theme={null}
> gt continue -a


Resolved rebase conflict for pp--06-14-part_2.
Restacked pp--06-14-part_3 on pp--06-14-part_2.


> gt log short


◯ pp--06-14-part_3
◉ pp--06-14-part_2
◯ main


> gt log long


* 543c8b3 - (14 hours ago) part 3 - Pranathi Peri (pp--06-14-part_3)
* 778006d - (14 hours ago) part 2 - Pranathi Peri (HEAD -> pp--06-14-part_2)
* ff393d3 - (44 minutes ago) part 1 (#100) - Pranathi Peri (origin/main, origin/HEAD, main)
```

After running the `restack` command, you can see that `git` and `gt` are in agreement about the history. Next, you may want to resubmit the restacked versions of these branches (`gt submit`), or make some changes to a branch mid-stack to address any review comments.


# Review Pull Requests
Source: https://graphite-58cc94ce.mintlify.dev/docs/review-proposed-changes

Learn how to review pull requests on the Graphite dashboard.

You can be notified that a PR needs your review in Graphite in one of two ways:

* Pull requests appear in the *Needs Review* section of your pull request inbox

* Through the Graphite integration for Slack

## Start a review

You can start a review by hovering over a line number to leave a comment. Clicking the line number will allow you to leave a comment on a single line, and clicking and dragging across multiple lines will allow you to leave a comment that spans multiple lines of code. Graphite allows you to comment on both changed and unchanged lines of code.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a3cddb8a1be44bfd9be0ccb748350fbb" data-og-width="1350" width="1350" data-og-height="756" height="756" data-path="images/8e7821f8-1700537924-frame-10123324.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c354b2cfe20252b990a94c1f99c76976 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=695e76c722d87e0ba3f415ef0aa029c1 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f5870826f8d76933986ca1e65ab10aad 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=50ff5662a6a0d807c613aff35b5b3543 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7116104bae1b14be334211a2a2037fc3 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f54915f21ff24162f360b31746ccd4d2 2500w" />
</Frame>

In the comment field, leave your comment. The commenting box provides a number of markdown formatting options to select from in the footer. You can switch between markdown and preview format for each comment by clicking the "eye" icon near the right corner of each comment box.

### One-off or batched comments

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=16d0d73b5cdf67cc8ec0d66d32972827" data-og-width="1350" width="1350" data-og-height="756" height="756" data-path="images/fe71f73c-1700538055-frame-10123325.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ed4e365009a99a30243ef3f4ad616549 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a5d42ded91c75ab5fb2e675444adebc9 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=08a4149e2e7a71159ce7ff8e97eb88b1 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2226e2ddfa5643d27fad2ace7d92c7aa 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c54a0a8ddcef6ddff287d75d06e6c2e1 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1bd214d0a5c49d550fdeddf2ad867872 2500w" />
</Frame>

When you finish entering your comment, you can click the dropdown on the `post thread` button to either:

* Post thread: this posts the comment immediately. Great for one-off, non-opinionated comments.

* Add to review: this will add the comment to a "batch." Once you batch the comment, it will be pending and only visible to you until you've submitted your final review, at which point all of your batched comments will also be submitted.

If you chose to add your comment to your review, the review bar that's pinned to the bottom of the PR will light up to show how many comments you have pending.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=5e6bb7a4c2e760ea3a4c3c61be51fa7d" data-og-width="1350" width="1350" data-og-height="626" height="626" data-path="images/7a69657b-1700538163-frame-10123326.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=10f607834807ddef1f22484f64825307 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=dcda6110ab217771aa06d5f96d83d471 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=80e22dfb7bfb818ebbbdea1ad3a627ff 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f1c792a7c6b5e8ff19094746b4a9117d 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e72dfb2d4440d1fabbcadfbbff197ce5 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f2e86bd52d358b46e76fa0cd021dc992 2500w" />
</Frame>

### Suggested edits

While reviewing, you can directly leave a suggested code edit to streamline the review process. You can either add these manually yourself, or leverage Graphite AI to turn your plain English suggestion into a code edit - saving both reviewer and author time.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ff59645669a4317ae7d30e125e29c84c" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/ddb190d4-1705423210-ai-suggested-edit_static.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8dedbd942c0c22496c1a487f9d1256ff 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2a4b6817b1fd1ea0a84a8501ee4add90 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=191e39ed1800008341bfef7eee6cf508 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=92f5cdff3eb33a1f6b88bdcac53fd9e2 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c1d2f52b10f52493fecc74e93ad05310 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2419bdb1b3504fb0e7c20fb14b54c3ea 2500w" />
</Frame>

## Leave a final review

Once you finish reading through and commenting on the contents of the pull request, you can leave a final review by hovering over the review bar that's pinned to the bottom of the PR page.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=16480ab9ab1f58f715ff40dee2ba26d6" data-og-width="1350" width="1350" data-og-height="626" height="626" data-path="images/465cf66a-1700538277-frame-10123327.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=bfb1f3a5b4eb5ffb1556c2c1d5cfb1d9 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ad1b6386cdfa8b531b7afb39c5f4bfe5 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=46474eb9561e04bd31ff05e85cef686f 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=02a36d193698ee5052d2dd8d919b26f1 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=aec111e5f5b513170f3071d30f9cce71 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7cfb7b6754c7045b556407d2c52c3e52 2500w" />
</Frame>

After you've added a summary of your review, you have three options:

* Request changes

* Just add comments

* Approve

<Note>
  If you have any pending comments at the time you're leaving your final review, they will all be posted with your final review at once.
</Note>


# Set Up The Graphite Merge Queue
Source: https://graphite-58cc94ce.mintlify.dev/docs/set-up-merge-queue



With the Graphite merge queue, rather than being merged straight into main, the PR will enter a "queue" and wait its turn to be merged.

The merge queue is **repository-specific**. When you enable it for a repository, it will operate on its `main`/`trunk` branch. We currently don't have support for multiple queues on a single repository (that is, two merge queues for the `trunk` branch and `deploy` branch of a repository).

## Prerequisites

* [Graphite Team or Enterprise plan](/pricing-faq)

* [Graphite App installed](/authenticate-with-github-app) on your org

## Enable the Graphite merge queue for your repository

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/21877fe2-1683648016-repo_settings.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c97b69ed7e99d99b4455d57618dceb99" data-og-width="5326" width="5326" data-og-height="2094" height="2094" data-path="images/21877fe2-1683648016-repo_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/21877fe2-1683648016-repo_settings.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8cadbe0bb875a57e264f18c8b35a3791 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/21877fe2-1683648016-repo_settings.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=af0a2c6d38da6f7055b057ba949eac27 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/21877fe2-1683648016-repo_settings.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=baeaced0bcc43d94c98b9d95a66f68e8 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/21877fe2-1683648016-repo_settings.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7bd14fc4f789421b81166e9acb377a3f 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/21877fe2-1683648016-repo_settings.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2341ca256c38fcd1e20f1de3c116bcd1 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/21877fe2-1683648016-repo_settings.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=04e0cef3fadae9348a6b6be4993cb187 2500w" />
</Frame>

Enable the Graphite merge queue for a given repository:

Go to *Merge queue* in the Graphite app settings page ([https://app.graphite.com/settings/merge-queue)](https://app.graphite.com/settings/merge-queue)

1. Click **Add merge queue**

2. Select the repository you want to enable it for by using the dropdown selector

3. Click **Next** to adjust and save your merge queue settings

## Configure the merge queue for your repository

In GitHub, most repos use either **branch protection rules** or **rulesets** to restrict certain actions. Follow the corresponding instructions for what your repo uses.

Some orgs may use both if transitioning from branch protection rules to rulesets: in that case, follow both instructions.

### Branch protection rules

#### Push permissions

Some repositories restrict which accounts can merge to the trunk branch with the **Restrict who can push to matching branches** branch protection rule.

* **Required:** if this setting is already enabled for your repo's trunk branch, add `graphite-app` to the list of actors with push access. Otherwise, this rule will prevent the merge queue from merging PRs.

* **Strongly recommended:** enable this setting, and make `graphite-app` the *only* actor with push access. This helps your teammates remember to use the merge queue for merging.

<Info>
  Graphite is not "required" to be the controller of history on `main`—and combining Graphite merge queue merges and non-merge queue merges will function—but the experience is much worse. If there are merges made to `main` outside the merge queue, they will be detected and the merge queue will restart the merge (rebase on top of those changes and restart CI) that is currently active. This could lead to failures if a timeout is configured for the merge queue, and results in users constantly being pushed behind non-merge queue users.
</Info>

To view this setting, go to **Settings** in GitHub for the repository you have the Graphite merge queue enabled for.

Next, go to the **Branches** settings under **Code and automation**.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c847fb7aaefe3265a732da82071cf996" width="750" data-og-width="664" data-og-height="548" data-path="images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=61409b1a6361d3758a5780693c3e3be9 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ab19c8d2f5274f44a868095b14bbbe81 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7059cb51323a6f5a0c0a032eb073bca6 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=640b18b74e79370a8df014b21695a148 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=0b4de21e3efc2179242c23fd4f453898 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ca7ef7f2-1688787122-screenshot-2023-06-30-at-4-29-16-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e505869be1c48d60a3be16356d8312a8 2500w" />
</Frame>

Click the **edit** button on the branch the Graphite merge queue targets (the branch which all PRs are merged into).

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5582a02ea1112e42fe70838cd0c94306" data-og-width="1574" width="1574" data-og-height="312" height="312" data-path="images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7e5ae1f167cc5a2528c411a2ece0a093 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=0001df93df3b28acf990f8d9e90ec2b9 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ac01f120fbe6de437f193d72e7a54b30 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5391e2a360bc2016059359a777eb1526 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ed36fbaa1f29f08784910b08ee0d8214 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b31c570b-1688787204-screenshot-2023-06-30-at-4-30-32-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=138ad4c44983d727b3bed0e410418ecb 2500w" />
</Frame>

Here you'll find the **Restrict who can push to matching branches** setting.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=cc50652613dad04f334ed4b17424b2c0" data-og-width="2292" width="2292" data-og-height="1186" height="1186" data-path="images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b7b48bb6ea77e9b46c5b139bc6b3b77f 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=678a624cb26bb79bb2485eff2735da13 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=395302172e8554931ff660c6842f2d5f 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=dbab06fa567e6e056ff39b428d458c65 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3d722f7bf09c7f2b31449e0bee235a80 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ed4583f6-1689791434-screenshot-2023-07-19-at-2-30-22-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5562ff5843e31832c4925f29d757ddbd 2500w" />
</Frame>

<Warning>
  GitHub automatically includes admins and maintainers as users who can bypass these rules and there currently isn't a setting to disable this.

  As it stands, admins and maintainers will still have the ability to bypass the merge queue despite having these settings enabled.
</Warning>

#### Bypass PR permissions

In order to implement speed improvements, the Graphite merge queue requires the **Allow specified actors to bypass required pull requests** permission. While you can use the merge queue with this setting disabled, enabling it will help our merge queue merge faster with [merge queue optimizations](/merge-queue-optimizations).

Under *Protect matching branches* → *Require a pull request before merging*

* Ensure that you have **Allow specified actors to bypass required pull requests** selected

* Add the Graphite App (graphite-app) to the list of who can bypass required requests

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=9730b5932584f86f1a16e0e95d2d01c9" data-og-width="1580" width="1580" data-og-height="1434" height="1434" data-path="images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2c22549b10c37027e908e6dc48f6f932 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a257256852f72d2275e1e3b9b4a26625 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f25a1a302044dfe08cfdd4dce15afe4d 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=faece2215f2537b08f77b05727baba98 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=326610f48dc05c7f73943cc39f35cfa0 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/96bfc5b0-1688787289-screenshot-2023-06-30-at-4-31-44-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=cd84a050b271353ede972b06a07be675 2500w" />
</Frame>

### Rulesets

Simply add the `Graphite App` to the **Bypass list** with **Always allow**.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4fe8c8bcfd1a75bcda5417286e868def" data-og-width="1588" width="1588" data-og-height="302" height="302" data-path="images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a428c5feeb315d44f356f30149c33767 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ff9e2701212120f7a3cd3534a34fb2cf 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4b5b99803abea2f553e9ece06b0d9d0d 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2262ce10c3a04d0994c8f45f5b7bb362 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f673577f498c4761e82f9a6f3179a762 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/18d8ecf7-1709912717-screenshot-2024-03-08-at-10-41-38-am.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f0d01d965a99eb80eeeae6a53088082e 2500w" />
</Frame>

Note that multiple rulesets can apply to a single repo or branch. Make sure to update this for all rulesets impacting your merge queue enabled repo and branch.

## Optional: Adjust merge queue settings

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/40d96e88-1683648678-merge_queue_settingw.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=1806afc2ff0ec8fa2006b40b97c15388" data-og-width="5326" width="5326" data-og-height="2094" height="2094" data-path="images/40d96e88-1683648678-merge_queue_settingw.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/40d96e88-1683648678-merge_queue_settingw.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=3a20590a92e1c575f84a8837169075b8 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/40d96e88-1683648678-merge_queue_settingw.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=40969aa7a3ebc4bc463517fec51d5eef 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/40d96e88-1683648678-merge_queue_settingw.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7995a6e8ca2afaec39efb23ec33b213f 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/40d96e88-1683648678-merge_queue_settingw.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=df1973e39ed8fcd005198808bcde3134 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/40d96e88-1683648678-merge_queue_settingw.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e90f10e84c0932a2329c63621b1e4a2a 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/40d96e88-1683648678-merge_queue_settingw.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c93536a00547a082c51462acacdc2f01 2500w" />
</Frame>

When you enable the Graphite merge queue for your repository, there are a few settings and configurations that are available to customize. Before you enable these settings, make sure you have [GitHub App authentication enabled](/authenticate-with-github-app), and have configured your repository's branch protection rules accordingly as explained above.

### Default merge strategy

* **Rebase**: rebase your changes on top of your trunk with commits unchanged (equivalent to GitHub's rebase and merge)

* **Squash**: rebase your changes on top of your trunk with each PR squashed to a single commit (equivalent to GitHub's squash and merge)

If you haven't enabled the queue, you can change the merge strategy for your PR directly from the merge modal. When the queue is enabled, you can set the merge strategy at the queue level so that all the PRs that are queued to that merge queue abide by the same rule.

### Timeout

Configuring the merge queue timeout allows you to place an upper-limit on the amount of time a PR can stay at the head of the queue, ensuring that the queue never hangs in the event that a regression is introduced.

### Adding to the queue via label

Specifying a merge label lets users add that label to a PR to let the merge queue know to merge it when it's ready. Removing a label will remove it from the queue. This allows seamlessly merging PR's from GitHub by just adding a label.

Adding a label to a PR that isn't yet mergeable will toggle a PR's *Merge when ready* property—as long as the label is applied, a PR will be merged when all branch protection rules are met.

You can automatically create this label in Graphite while adding a merge queue to your repo, or when modifying its settings.

<Note>
  You can only enqueue via label if you have a Graphite account set up.

  If a user tries to add the merge queue label to their PR and doesn't have a Graphite account, the label will be removed and the user will be prompted to create an account on Graphite in the PR's comments on GitHub.
</Note>


# Set up merge queue integration
Source: https://graphite-58cc94ce.mintlify.dev/docs/setup-merge-queue-integration

To allow users to merge stacks via the Graphite UI, Graphite needs to know who to hand off PRs to for merging

| Merge mechanism          | Integration                                                                                                                                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No merge queue           | You can skip this step. Users will be able to merge stacks directly through the Graphite UI without any additional setup.                                                                                                    |
| Non-Graphite merge queue | You need to set up the merge queue integration for each repo so that users can enqueue stacks from the Graphite UI. For instructions, refer to [External Merge Queue Integration (Beta)](/external-merge-queue-integration). |
| Graphite merge queue     | To learn about Graphite's stack-optimized merge queue, refer to [Merge queue](/graphite-merge-queue).                                                                                                                        |


# Configure recommended CI settings
Source: https://graphite-58cc94ce.mintlify.dev/docs/setup-recommended-ci-settings

Set up your GitHub repository's CI to work well with Graphite

### Ignore Graphite's temporary branches in your CI

You should configure your CI to ignore PRs whose base branch is named `graphite-base/*`. Not doing so may result in failed CI jobs, specifically when they reference Graphite's temporary branches which have been deleted.

Here’s how to disable running CI for these branches in GitHub Actions:

```
on:
  pull_request:
    types: [opened, reopened, synchronize]
    branches-ignore:
      - "**/graphite-base/**"
```

For more information about when and why these temporary branches get created, refer to [Automatic rebasing](/merge-pull-requests#automatic-rebasing).

### Ensure that CI is running on upstack branches

Graphite calculates and enforces mergeability for pull requests that are dependent on other pull requests in a stack, based on the checks that are required to merge into the trunk (target) branch of the stack, e.g. `main`.

If your repository is only running checks for PRs based on your trunk branch, then checks for upstack PRs will not run until downstack PRs are merged. Thus, we recommend configuring your CI to run on any branch (aside from `graphite-base` branches as mentioned above).

We provide [CI Optimizations](/stacking-and-ci) that allow you to conditionally skip certain checks depending on stack position. This can be useful to help control CI costs.


# Slack Notifications
Source: https://graphite-58cc94ce.mintlify.dev/docs/slack-notifications

Learn how to integrate Graphite with Slack to receive real-time, actionable notifications about your PRs.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/61b6128c-1688839902-notifs.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=dcc683d0d35f0600590a69f0ffd868a0" data-og-width="5392" width="5392" data-og-height="4210" height="4210" data-path="images/61b6128c-1688839902-notifs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/61b6128c-1688839902-notifs.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=30fa00b35bffbbf7ba0f01ef0ce94552 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/61b6128c-1688839902-notifs.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e059cf916d9f2c6eac1189781e474e30 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/61b6128c-1688839902-notifs.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=dd449123dbc5a39337f06cc472ef2b5d 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/61b6128c-1688839902-notifs.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b15337382712631ff72a3b4bc2431d84 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/61b6128c-1688839902-notifs.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=54e3dd2a3a285823890fea24be3c5dc0 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/61b6128c-1688839902-notifs.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8d55575cbf331decc380392edadca222 2500w" />
</Frame>

You have the ability to configure Slack notifications for PR activities like review requests, comments, mentions, and status changes. For some PRs, you can also approve, comment, request changes, or merge directly from Slack.

### Prerequisites

* A Slack workspace (free or paid)

## Install Graphite for Slack

Install the Graphite integration for Slack directly from the [notifications settings page](https://app.graphite.com/settings/notifications) on the Graphite app.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b7bc33ac38e0b2d7abe9de6f6cf773ef" data-og-width="2328" width="2328" data-og-height="588" height="588" data-path="images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=141e5e4aabc88765d620940a48d31956 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4d6b715b8a22e0358d5e010142b7d941 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=87269879e71fabaddb57ac9041d6c420 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=86c720131451374ad1d2f12472a2af9d 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d6fff7fd3093838bbb6d87973d387e56 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/9e707430-1688840382-screenshot-2023-07-08-at-2-19-27-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2a47437dae218a7d71aec61cda75999b 2500w" />
</Frame>

After adding your Slack workspace, you will be prompted to give the Graphite app permissions to proceed.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=1acbb3cd2603bcb96d6e7d94f091f074" data-og-width="1218" width="1218" data-og-height="1162" height="1162" data-path="images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c98464dde82e205348dcebe85c743eb6 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b082c80a3257f40d645ccff66992121f 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=25d9c9638d293fc2c7d80ff78995c60e 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=cb97e27fb5f8583ca0686292737d2a07 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=0cf69208dd0dfea92a27483db2239b31 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/1e2a70e0-1675699556-screenshot-2023-02-06-at-11-05-49-am.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=604d583e1c1774f1e7e236d4f7a2f28b 2500w" />
</Frame>

In the future, you can modify the Graphite App's access to select workspaces and channels through this settings page.

<Note>
  **Note**

  When there are major updates to our integration for Slack, we will sometimes prompt users to "re-install" the integration for their workspace. To do so, you can follow the exact same installation flow in this guide. No need to remove the existing integration—adding the integration again will override your previous one.
</Note>

## Set up real-time notifications

After you've installed the integration, you can enable real-time notifications in the [notifications settings page](https://app.graphite.com/settings/notifications) on the Graphite app. You can configure which types of events you want to receive notifications for.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/10bb323e-1688840928-notifs-settings.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d73642bf9a30b1b70c9b17f68ae373dc" data-og-width="3340" width="3340" data-og-height="4210" height="4210" data-path="images/10bb323e-1688840928-notifs-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/10bb323e-1688840928-notifs-settings.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e6167eca342aa558bef664bf5997a2f6 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/10bb323e-1688840928-notifs-settings.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8759e3ff35e595c54b50b375e46792cd 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/10bb323e-1688840928-notifs-settings.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8f67eee4e7c22689d4b518f88000d02c 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/10bb323e-1688840928-notifs-settings.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=1e8967a90d539512b716666422463013 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/10bb323e-1688840928-notifs-settings.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=1c6ef03b9455f148dba28042e3174a0b 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/10bb323e-1688840928-notifs-settings.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=5649727919626063735e4982066d0370 2500w" />
</Frame>

### Reviewing and merging PRs from Slack

The Slack integration gives you the option to directly review and merge PRs from Slack. No extra setup is needed: simply enable Slack notifications for **Review requests** and **Activity on your PRs**. Reviewing from Slack is available for PRs of up to 25 lines.

### Privacy and authorization

For the purpose of providing personalized and configurable updates and information about code contributions, the Graphite app can:

* Send messages as **@graphite** in selected channels

* Start direct messages with people

* Upload, edit, and delete files as **Graphite**

* View files shared in channels and conversations that Graphite has been added to

* Add, edit, and delete remote files on a user’s behalf

* View remote files added by the app in a workspace

* Show previews of app.graphite.com URLs in messages

* View people in a workspace

* View URLs from app.graphite.com


# Squash, Fold, And Split Changes
Source: https://graphite-58cc94ce.mintlify.dev/docs/squash-fold-split

Learn how to squash, fold, and split changes with the Graphite CLI.

## Prerequisites

You should be familiar with how to:

* [Create branches in a stack](/create-stack)

* [Visualize a stack](/visualize-stack)

* [Update mid-stack branches](/update-mid-stack-branches)

## Squash commits in a branch

`gt squash` allows you to squash multi-commit branches into a single commit branch, restacking upstack branches if necessary. This command is useful if you meant to run `gt modify` instead of `gt modify -c`, or to maintain single-commit branches after invoking `gt fold`. For example:

```bash Terminal theme={null}
> gt log
◉ 06-28-second_branch (current)
│ 10 minutes ago
│
| 6s7a8d7 - last committed change
│ d7d41b6 - committing another change
│ 8c6d8de - committing some changes
│
◯ 06-28-first_branch
│ 5 minutes ago
│
│ 232e8cf - initial commit
│
◯ main
│ 10 minutes ago
│
│ 1e0b290 - Merging a pull request


# we want to squash the three commits on 06-28-second_branch into one
> gt squash


# /* opens an interactive editor to rename the single commit */


> gt log
◉ 06-28-second_branch (current)
│ just now
|
│ 9e13a52 - a single commit
│
◯ 06-28-first_branch
│ 5 minutes ago
│
│ 232e8cf - initial commit
│
◯ main
│ 10 minutes ago
│
│ 1e0b290 - Merging a pull request
```

## Fold branches together

`gt fold` folds (combines) the current branch into its parent, and makes all children of the current branch children of the parent branch accordingly. It preserves the commit history of both the branches and their descendants. By default, it will use the name of the parent for the resulting combined branch, but you can use the name of the branch being folded (current branch) instead with the `--keep` flag. For example:

```bash Terminal theme={null}
> gt log
◉ 06-28-second_branch (current)
│ 10 minutes ago
│
│ d7d41b6 - committing another change
│ 8c6d8de - committing some changes
│
◯ 06-28-first_branch
│ 5 minutes ago
│
│ 232e8cf - initial commit
│
◯ main
│ 10 minutes ago
│
│ 1e0b290 - Merging a pull request


# we want to fold 06-28-second_branch into 06-28-first_branch
> gt fold
# or
> gt f
Folded 06-28-second_branch into 06-28-first_branch.


> gt log
◉ 06-28-first_branch (current)
│ just now
│
│ d7d41b6 - committing another change
│ 8c6d8de - committing some changes
│ 232e8cf - initial commit
│
◯ main
│ 10 minutes ago
│
│ 1e0b290 - Merging a pull request
```

## Split a branch into multiple branches

`gt split` splits the current branch into two or more branches. You can use one of two methods to split a branch:

* `--by-commit/--commit/-c`

* `--by-hunk/--hunk/-h`

If there is only one commit on the branch, you will enter `hunk` mode automatically. If there's more than one commit on the branch and you don't pass in an option, you'll be prompted to choose one.

### By commit using the `--by-commit` flag

In this mode, you split your branch along already-defined commit boundaries. For example, if you have a branch with five commits on it, you could put the first three into one branch and the others into another. This preserves commit history of the original branch and its descendants.

<Frame>
  <video autoPlay muted loop playsInline className="w-full aspect-video" src="https://www.datocms-assets.com/85246/1687975920-rpreplay_final1687975546.mov" />
</Frame>

### By hunk using the `--by-hunk` flag

This mode allows you to split your branch by selecting hunks that you'd like to apply to each new branch. The interface is made up of iterative calls to `git add --patch`, which prompts you to stage your changes. You can split your branch by first staging only those you'd like to include in the first branch, then giving it a name, then moving on to the second, giving that one a name, and so on.

<Frame>
  <video autoPlay muted loop playsInline className="w-full aspect-video" src="https://www.datocms-assets.com/85246/1687975922-rpreplay_final1687975370.mov" />
</Frame>

<Note>
  The branch name on a GitHub PR is **immutable**, so if you already have a PR open for a branch you're splitting and would like one of the new branches to stay attached to the PR, **make sure to give the original branch's name to that new branch**!

  For example, if I have a PR open for my branch `new_feature` and I get asked to split out a necessary refactor that I included in the same branch, I can split my branch into `necessary_refactor` and (a now smaller) `new_feature`. When I resubmit, my feature changes will stay attached to any ongoing discussion on the original PR.
</Note>


# CI Optimizations
Source: https://graphite-58cc94ce.mintlify.dev/docs/stacking-and-ci

Learn CI optimizations & best practices for stacked pull requests.

Stacking leads to developers creating smaller easier-to-review pull requests, which can lead to more CI runs unless you optimize your CI for stacking. Organizations with fewer than 10 stackers are unlikely to see any difference in CI wait times or runs.

Additional CI runs occur when stacking PRs in part due to the additional PRs created, and due to behind-the-scenes rebasing to keep stacked branches up to date.

To solve this, Graphite offers an API endpoint for your CI workflows to query, allowing you to customize which PRs in stacks you want to run CI on.

## How CI Optimizations work

CI Optimizations is set up per-repository, and requires a very small amount of configuration, namely:

* How many PRs at the bottom of each stack should run CI?

* Should CI be run at the top of the stack?

In addition to this configuration, you'll add a step to your CI that calls the Graphite Buildkite/GitHub actions step. These CI steps are open-source, so you know exactly what is running in your CI pipeline. The details on adding these steps can be found below.

Each step is a wrapper script for a very simple API call that responds with a boolean: whether CI should be skipped. You don't need to worry about handling the API response manually or querying any additional data about the PR/stack from GitHub to decide whether to run CI – just add the step to the beginning of your configuration.

* If the request to our API is malformed or errors for any reason, we will not skip CI

* If CI Optimizations have been disabled, we will not skip CI

* If the PR is in a merge queue or merging as a stack with Graphite, we will not skip CI

## How to set up CI Optimizations

To begin setting up CI Optimizations, click the "Add new" button on its settings page on the Graphite dashboard.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d03f4defc7b959bfdd0287a63693adc1" data-og-width="1358" width="1358" data-og-height="633" height="633" data-path="images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=0ed8d5e62d654b3f17f33b88f3a9e412 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=1a3b3ba6858c4ddc97793d207da8ad8a 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=3624cf6d0c0f93c9dae4e5e10bd59219 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=61e27cd39f91ac0a50d7d52b76fad1e5 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=48584ed9ed05ed6aea019ce412e0f821 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/4e66e804-1740619633-screenshot-2025-02-26-at-15-24-07.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ccd3e45445df0d4c5f9af3c4f440cd4e 2500w" />
</Frame>

You'll see a panel as in the below screenshot, which will guide you through adding the step for your CI provider, and configuring when CI should run.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=00200f97c4e42bac75c550f0e89d8e8a" data-og-width="730" width="730" data-og-height="706" height="706" data-path="images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7477bde32e193ed4e4e1246e58cb1fbc 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d91f93a128b5909e0d6cbddde7bbe170 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4e32b27dafdb0036ea5debdf6da7da8c 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e27b0c0a621d90e9d4c3f3801b239b54 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c8075c51a63de3c0e2b96ad3cb2a5d3a 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f197da27-1740624151-screenshot-2025-02-26-at-15-24-49.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f2b462e2a9f0275150d5bbb7a1b9e0ac 2500w" />
</Frame>

Once you're done, a card for your repository will appear on the settings page. You can edit the settings at any time.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4939608a8967bd4a2cb58a4fb7a7ee01" data-og-width="771" width="771" data-og-height="247" height="247" data-path="images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=cd7c7006c9c215a50db961def491a63e 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ce5d40a3a7ab62f343c9a7f04907d0ec 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8589a84753a91a30cfc4fcd241d90c6f 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d0a06379df3aed29b7673bf242338e39 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2bbce26253ccca3d6d7e1b1794eae562 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/efdb8a56-1740624315-screenshot-2025-02-26-at-15-25-11.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7085558b8bd27e9d45f98988be88cc83 2500w" />
</Frame>

## Setting up the Buildkite step

There are two ways to configure Graphite to optimize your Buildkite pipelines:

### Option 1: Graphite *pipeline* runs first (recommended)

<Info>
  In this Buildkite configuration, you create a new **Graphite CI optimizer** pipeline that runs before your repo's other pipeline(s). It has the advantage of explicitly showing PR authors that some of their CI did not run when the optimizer skips CI.
</Info>

In Buildkite, create a new “Stack CI Optimizer” pipeline that runs before all other CI pipelines. This new pipeline determines if CI should run for this PR, and triggers the other pipeline(s) if so.

**Getting started**

1. [Create a new CI optimization in Graphite settings](https://app.graphite.com/settings/ci-optimizations) and copy the pipeline YAML

2. [In Buildkite](https://buildkite.com), create a new pipeline for the same repo you configured in the previous step

3. Paste the YAML copied from Graphite into the Buildkite pipeline configuration UI or into your repo's `.buildkite/` directory as a **new pipeline**. Remember to update the `trigger` step in the pasted YAML so the CI optimizer pipeline can call your own pipeline after it decides whether to optimize CI for your PR.

4. In **your own** pipeline settings under GitHub > GitHub Settings, check the box **Skip builds with existing commits**. This ensures the Graphite optimizer pipeline runs first and conditionally triggers your existing pipelines.

Note: you can test Buildkite pipeline changes in branches/PRs before merging them into your main trunk branch, so you can verify the optimizer is configured correctly before enabling it for your repo.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=be10531afe0bc618ab11a5b5abda6d96" data-og-width="1722" width="1722" data-og-height="478" height="478" data-path="images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=856fec656bf53eafb0d6f2f28520909c 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=93dc5149bdc5ae856eb6c5803aa6c434 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=da8f7a29c511e25772f9e209bb172607 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3f42292daca4943014266f5b22fba984 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4a899e798432296b3a64a067728e3894 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/b995bc95-1715363378-screenshot-2024-04-03-at-18-28-11.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5af5817e8803502e5d3476c050e47fc4 2500w" />
</Frame>

### Option 2: Graphite *job* runs first

<Info>
  In this Buildkite configuration, you add a job to the start of your pipeline that your others wait for. It has the disadvantage of showing the overall pipeline status as green on GitHub, even when the CI optimizer decides to skip tests. The Buildkite and Graphite UIs show the accurate skip statuses.
</Info>

**Getting started**

1. [Create a new CI optimization in Graphite settings](https://app.graphite.com/settings/ci-optimizations) and copy the pipeline YAML

2. Add the following YAML to the beginning of your repo's pipeline(s), **including the `wait` step** (pipelines are typically stored in `.buildkite/`). Replace `graphite_token` with the token from the first step.

```yaml YAML theme={null}
steps:
  - name: ":graphite: Graphite CI optimizer"
    soft_fail: true
    plugins:
      withgraphite/graphite-ci#main:
        graphite_token: "xxxxxxxxxxxxxxxxxxxxxxx"


  - wait

  # the rest of your jobs in the pipeline
  - label: "Your first job to run after the optimizer"
    command: echo "hello"
```

*Note: You should *[*securely pass your token*](https://buildkite.com/pipelines/security/managing-secrets)* to the Graphite plugin instead of storing it in your pipeline configuration.*

## Setting up the GitHub Actions step

1. [Create a new CI optimization in Graphite settings](https://app.graphite.com/settings/ci-optimizations) and copy the pipeline YAML

2. Add the following to your GitHub Actions workflows (typically stored in `.github/workflows/)`. Replace `graphite_token` with the token from the first step.

```yaml YAML theme={null}
jobs:
  optimize_ci:
    runs-on: ubuntu-latest # or whichever runner you use for your CI
    outputs:
      skip: ${{ steps.check_skip.outputs.skip }}
    steps:
      - name: Optimize CI
        id: check_skip
        uses: withgraphite/graphite-ci-action@main
        with:
          graphite_token: ${{ secrets.GRAPHITE_CI_OPTIMIZER_TOKEN }}

  your_first_job:
    ...

  your_second_job:
    ...
```

Then **for each job** in the workflow you want to optimize, add the following YAML:

```yaml YAML theme={null}
job_name:
  needs: optimize_ci
  if: needs.optimize_ci.outputs.skip == 'false'
  ...
```

This ensures the optimized jobs only run when the CI optimizer gives them the signal.

## Error handling

Graphite's Buildkite and GitHub Actions integrations are configured to "fail open" so that outages and errors still result in your CI running.

## Other ways to optimize CI

### Breaking up CI

Google recommends breaking up your tests from one CI job into many which run at different points. One recommended split is:

* CI that runs on all PRs

* CI that runs on PRs, excluding upstack

* CI that runs after PRs merge to main

In GitHub actions, and other providers, you can do this by creating multiple workflows and setting different triggers for them.

### Dependencies and test caching

If your organization doesn’t already have one set up, a dependency management tool (such as [Bazel](https://bazel.build/) or [Buck](https://buck.build/)) can be really helpful. These tools look at what code changed, and determine which tests need to run as a result. This prevents unnecessary CI runs with stacking by skipping any tests that were unaffected.

In a similar vein, workflow orchestration tools with caching can create a similar effect. For example, [Turborepo](https://vercel.com/solutions/turborepo) caches CI results based on the hash of the project’s files. Unlike Bazel and Buck, all tests will still run, but if the input files were unchanged across a stack, the test will hit the cache and make the cost negligible.

### Required CI

If your organization has branch protection rules turned on for all base branches (instead of only trunk, for example), and you are not running CI on upstack PRs, you may see upstack PR as “missing required CI”. This is because the CI job that is required has not yet run on that PR (because it’s waiting for dependencies to be merged).

## Reducing CI runs with the Graphite Merge Queue

Lastly, the Graphite Merge Queue can help you save on CI cost when merging. The merge queue allows various configurations that help reduce the number of CI runs:

1. Batching: CI will run just once per `batch size` stacks, where `batch size` can be configured in our UI. This results in a saving of `batch size` \* `stack height` CI runs.

2. Parallel CI: Users can configure CI to run just once per stack, allowing users to save `stack height` CI runs.

This can be very useful for organizations that merge a lot of stacks.


# Sync Changes From A Remote Repository
Source: https://graphite-58cc94ce.mintlify.dev/docs/sync-with-a-remote-repo

Learn how to sync changes from a remote repository with Graphite's CLI, managing branch updates and conflicts.

## Prerequisites

You should be familiar with how to:

* [Create branches in a stack](/create-stack)

* [Visualize a stack](/visualize-stack)

* [Create and submit pull requests](/create-submit-prs)

* [Update mid-stack branches](/update-mid-stack-branches)

## Sync changes from your remote repository

If your remote `trunk` branch (also known as `origin/main`) gets ahead of your local repository while you're developing, you can use `gt sync` to bring your stack up-to-date. Using a [trunk-based-development workflow](/trunk-based-development) allows you to frequently sync changes from your `main` branch without running into unmanageable merge conflicts.

`gt sync` does a few things:

* Pulls in the latest changes from `main`

* Prompts you to delete any stale local branches which have been merged into trunk

* [Restacks](https://graphite.com/docs/restack-branches) your upstack branches which have not been merged and your current stack onto `main`. If you encounter any merge conflicts, you'll be prompted to resolve them.

Let's say that you've squash-and-merged in the first branch in your stack, `pp--06-14-part_1`, of a three-branch stack. Since you know that your `main` branch has been updated with the changes of `pp--06-14-part_1,` you can sync that change from remote using the `gt sync` command:

```bash Terminal theme={null}
> gt sync


🌲 Pulling main from remote...
main fast-forwarded to 4604ea03f728126332fa23bbfa74643c18d2fca3.
🧹 Checking if any branches have been merged/closed and can be deleted...
✔ pp--06-14-part_1 is merged into main. Delete it? … yes
Deleted branch pp--06-14-part_1
Restacked pp--06-14-part_2 on main.
Restacked pp--06-14-part_3 on pp--06-14-part_2.
```

If you run `gt log`, you see that `part_2` is now based on `main`:

```bash Terminal theme={null}
◉ pp--06-14-part_3 (current)
│ 39 minutes ago
│
│ PR #101 part 3
│ pp--06-14-part_3: https://app.graphite.com/github/pr/withgraphie/pranathi-test-repo/102
│
│ 95338df - part 3
│
◯ pp--06-14-part_2
│ 39 minutes ago
│
│ PR #101 part 2
│ pp--06-14-part_2: https://app.graphite.com/github/pr/withgraphite/pranathi-test-repo/101
│
│ 95610c6 - part 2
│
◯ main (current)
│ 30 minutes ago
│
```

### Dealing with conflicts

Syncing from a remote repository is almost always followed by restacking any of the dependent branches. `gt sync` tries to restack as much as it can without needing your input to resolve conflicts.

You can think of restacking branches as distributing the new changes from your `main` branch across all of the branches that are dependent on trunk and haven't yet been merged.

If these changes conflict with changes you've made, `gt sync` might output something like:

```bash Terminal theme={null}
All branches restacked cleanly, except for:
▸ 09-14-part_4
You can fix these conflicts with gt restack.
```

This means you need to check out `09-14-part_4` and run `gt restack`, which will take into standard `git` conflict resolution (just like if you had hit conflicts during `gt modify`).


# Track Branches
Source: https://graphite-58cc94ce.mintlify.dev/docs/track-branches

Learn how to track git branches with the Graphite CLI.

## Prerequisites

You should be familiar with how to:

* [Create branches in a stack](/create-stack)

* [Visualize a stack](/visualize-stack)

* [Create and submit pull requests](/create-submit-prs)

* [Edit the order of branches in a stack](/edit-branch-order)

* [Sync changes from a remote repository](/sync-with-a-remote-repo)

## Track branches with the CLI

If you're just getting started with Graphite, it's likely you have some branches floating around that you created with `git`, but you want to pull them into your `gt` workflow. Alternatively, there are situations in which tracking branches can help fix your `gt` state if your metadata ever gets messed up.

### Git passthrough

`git` passthrough enables users to switch between native `git` commands and `gt` without interrupting their workflow. There are a number of `git` commands that aren't implemented in `gt` because there's no need to recreate them. Here are several you may find useful throughout your workflow:

* `git add`: Stage files to commit; `-p` is helpful for precise cases

* `git stash:` Save changes for later (retrieve with `git stash pop`). Since restacking requires the working tree to be clean, stashing changes you don't intend to commit is often necessary while using `gt`. The `-p` option is just like `git add`'s.

* `git diff`: See what has changed between two branches.

* `git status`: Keep track of your worktree and staging area, just like `git`.

* `git rebase`: Useful for preparing branches created outside of Graphite to be tracked (see below). Also potentially dangerous (see below).

Knowing the effects/benefits of `git` passthrough is useful when working with externally created branches, since you may need to use a combination of `git` and `gt` commands to update your working state. If you ever need to do something that isn't natively supported in `gt`, you can *always* jump back to `git` and sync your changes to `gt` if needed.

### Track branches created outside of `gt`

Because of the "restacking" model, it is always safe to update your branches with simple `git` commands—a `gt restack` will rebase descendants so that they have the new version in their history.

If you use `git` instead of `gt` to create a branch, you must let `gt` know what its parent is with `gt track`. It prompts you to select a parent for the current branch from the branch's `git` history:

```bash Terminal theme={null}
# Ensure the branch you want to track has the desired parent in its history
# In this case, we want to stack our branch `first_branch` on `main`
git checkout first_branch
git rebase main first_branch


# Now, we'll track our branch
gt track
# alias
gt tr
```

If there is more than one potential parent for the `first_branch`, you'll be prompted to select one:

```bash Terminal theme={null}
? Select a parent for first_branch (autocomplete or arrow keys) ›
❯   last_branch
    some_other_branch
    main
```

If you want to track a specific branch that already exists, you can pass the branch name as an argument to `branch track`:

```bash Terminal theme={null}
gt track <DESIRED_BRANCH>
```

### Track a whole stack at once

Imagine you've created a stack of multiple branches outside of Graphite, or on a different machine, for example. If you run `gt track` from the tip, Graphite will automatically track multiple branches in a row iterating by parent commits from your current branch until you reach a branch that is already tracked. The `--force` flag chooses the nearest ancestor of each branch as its parent.

### Track branches to repair `gt` metadata

`gt track` can also be used to fix Graphite metadata if it ever becomes corrupted or invalid.

## Dangers of using a vanilla Git rebase

The CLI's engine keeps track of the base of each branch—meaning, the commit in its history that corresponds to its parent branch. This means that if you use a vanilla `git rebase` that removes that commit from the branch's history, **your branch and its children may suddenly become untracked**. In order to bring the branch back into Graphite, you must ensure the branch is correctly based on its parent, and then use `gt track` to fix its metadata.

Rebases that don't remove that base of the branch from its history are safe. For example, running a `git rebase -i` on the commits of a branch is safe, although there is a command for this called `gt modify --interactive rebase` that runs an interactive rebase and then restacks upstack branches when you `gt continue`.


# CLI Troubleshooting FAQs
Source: https://graphite-58cc94ce.mintlify.dev/docs/troubleshooting

Tips for resolving common Graphite CLI issues.

### Submit a bug report

If you find yourself in a bad state and are unsure how to proceed, please submit a bug report with debug information by running `gt feedback` and sending debug logs. This allows us to fix most issues.

### Unblock yourself

If the CLI gets stuck in a broken state and you are not able to wait for a member of our team to help, there are a few options.

* `gt dev cache --clear` is a safe command that sometimes fixes inadvertent issues that we haven't caught before release. It doesn't change any `git` or Graphite state.

* `gt untrack` specific branches that are behaving weirdly. You will then need to re-track branches with `gt track` – note that in certain cases you may need to `git rebase` manually in order to track a branch with the correct parent. [Read more about `gt track`](/track-branches#track-branches-created-outside-of-gt) .

* `gt init --reset` is the nuclear option which deletes all Graphite metadata from your repository. All branches will need to be re-tracked.

* The debug logs that `gt feedback` sends us are stored at `~/.local/share/graphite/debug` (or `$XDG_DATA_HOME/graphite/debug`). Each file contains the logs for a single CLI invocation, and includes information about underlying git commands and network requests. Logs are stored for 24 hours —`gt feedback` sends the whole directory. If you encounter any issues with the `gt feedback` command, feel free to zip the directory and include it in a support ticket to [support@graphite.dev](mailto:support@graphite.dev). You can also go spelunking in the logs yourself if you are curious!

If none of these work, and you would like specific help for your issue, reach out in our [community Slack channel](https://community.graphite.com).

## CLI FAQ

### Why did my "submit" overwrite a coworker's changes to my branch?

We use `git push --force-with-lease` under the hood for our push, which should ensure this doesn't happen. You should only be able to overwrite changes that you have already pushed from your machine or synced to your machine with `gt get`.

Using this option is just like using `--force` (push to a branch on remote even if remote's SHA cannot be fast-forwarded to the new SHA), with the caveat that if the remote's SHA for the branch doesn't match the "remote-tracking branch" on your machine (for example, `refs/remotes/origin/feature`), it will fail, as this means that someone else has updated the branch since you last pushed to it or pulled it. Graphite respects the "remote-tracking branch", only updating it on a `gt submit` or `gt get` operation.

The issue can arise if you have some other tooling (for example, some VS Code extension) that is `git fetch`ing your branches in the background. This could update the "remote-tracking branch" and result in the `--force-with-lease` check passing—even if someone has updated the branch to a commit that you haven't synced to your repository (or pushed yourself).

### Why are my actions running twice?

Because `gt stack submit` both performs a `git push` and a GitHub API call, occasionally GitHub will pick up both as a [`synchronize`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request) event on the PR.

We recommend using GitHub's [concurrency](https://docs.github.com/en/actions/using-jobs/using-concurrency) configuration to ensure that you do not have duplicated CI.

For example, the following configuration will cancel previous CI runs on the same pull request:

```yaml YAML theme={null}
concurrency:
  group: ${{ github.repository }}-${{ github.workflow }}-${{ github.ref }}-${{ github.ref == 'refs/heads/main' && github.sha || ''}}
  cancel-in-progress: true
```

### Why am I getting a 500 error when submitting PRs after renaming repository?

When trying to submit pull requests using `gt submit` after a GitHub repository has been renamed, you may encounter a 500 error from the pre-submit-pull-requests endpoint, even though repository syncing works correctly within Graphite.

Even though GitHub redirects old repository URLs to new ones for Git operations, this redirection may cause issues with `gt`'s PR submission process. Ensure both your Git and Graphite configurations are updated to use the new repository name directly:

* Run `gt config` to access `Repository-level settings` > `Remote repository` > `Configure repo name` and update the repository name to match the new repository name
* Run `git remote set-url origin https://github.com/owner/new-repo-name.git` to update your Git remote origin to point to the new repository name

### Single-commit workflow

The Graphite CLI use branches instead of commits to represent atomic changes in a stack. But it's possible to replicate the single-commit workflow.

Just don't use `gt modify --commit`, and if you end up with multiple commits on a branch by accident, you can always use `gt squash` to get your branch back to a single commit. This way, you can essentially only use `gt`, and your workflow will look something like (making use of lots of shortcuts and short-form flags):

Terminal

```python  theme={null}
# make changes to the codebase

gt c -am "my first commit"

# make some more changes

gt c -am "my second commit"

# now we're ready to submit!

gt s -np

# address requested changes

gt co my_first_commit
gt m -a
gt ss

# or you can use

gt absorb -a
gt ss

# ... etc
```


# Introduction To Trunk Based Development
Source: https://graphite-58cc94ce.mintlify.dev/docs/trunk-based-development

Learn more about trunk-based development's benefits, best practices, and comparison with Gitflow.

## What is trunk-based development?

Trunk-based development is a practice in which all developers work on a shared branch, called the `trunk` or `mainline` using a version control system of their choice. Instead of creating long-lived feature branches, developers make changes directly to the `main` branch, which is continuously integrated and tested.

## Continuous integration

Trunk-based development is a prerequisite for continuous integration (CI). Each time changes are pushed to the `trunk` branch (which often happens several times a day), a suite of automated tests run before and after the merge to determine whether or not the change introduces regressions.

**Every change to `trunk` triggers a build and a series of automated tests**. A change that breaks your `trunk` branch must be fixed immediately before making any other changes—this may sound time-consuming at first, but since tests are run at each step of the development process, bugs and regressions are encountered far less frequently in a team that practices CI.

## Gitflow vs. trunk-based development

Gitflow is a branching model that creates multiple long-lived branches for different stages of the development process (for example, feature branch, develop branch, release branch, and master branch). Different developers use different techniques to merge/commit between these branches, adding increased complexity to the system.

Additionally, Gitflow developers work on large, long-lived feature branches for collaboration. These feature branches are often maintained for days or even months, making the merge into the `main` branch a tedious and risky task. These feature branches are usually so large that "code freeze" periods are required to ensure that the `main` branch is still in a working state, since these merge events are more prone to introducing regressions and bugs.

In contrast, trunk-based development uses a single shared branch (`trunk`) where all developers work and continuously integrate their changes. The model is relatively simple and agile, operating under the assumption that the `trunk` branch is always stable to work off of and commit to. Small batches or "stacks" of branches are extremely short-lived, and changes are merged into `trunk` every couple of hours.

Here's a visual distinction between trunk-based development, and a Gitflow-style of development:

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e623efdf786fc7e8409556c281aa207e" data-og-width="2094" width="2094" data-og-height="888" height="888" data-path="images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e9aee35b5cd5eb25ddb5c69e0fd67661 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=6e49b8566435d328dfc3d4ca66c3afc9 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=445afdb8a310040e3f2b3c3d433bb631 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=05138021d0e55ede0a28b32d9fbe02c1 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e66d64782d48ab78e5b15abb06996476 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/019eb4b3-1678122396-screenshot-2023-03-06-at-12-06-07-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=14b0d3475aa7934fc3077362eaa361c4 2500w" />
</Frame>

*Image from [Google Cloud](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development)*

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8a30c0422d60dcc66364f32405c1ad2c" data-og-width="2096" width="2096" data-og-height="1296" height="1296" data-path="images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3ac5dc3d882886b02b2c5d5eadb653c2 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f903c3ec11d5551a8050a0b70fc9905c 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=9719d0a3d21848faddfca78036075ed1 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ca93b51f756e5e0305412cbf1e3d8ca4 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2f13b3f8fae4da83744562e00ca3cbc8 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/f97b5ea1-1678122402-screenshot-2023-03-06-at-12-06-22-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b015360e5bb10f9d6a1b82485f967e4d 2500w" />
</Frame>

*Image from [Google Cloud](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development)*

## Benefits of trunk-based development

There are many benefits of trunk-based development, but these are the most notable ones:

* **Fast feature delivery**: In trunk-based development, changes are continuously integrated and tested (the `trunk` must always be green), so new features can be delivered faster than in a feature-branching model where features are developed in isolation and then integrated later.

* **"Green" collaboration:** Team members frequently update and sync their work with the `main` branch in trunk-based development. With this approach, peers integrate each other's changes on an hourly or minute-by-minute basis, ensuring the base they're working off of is never stale.

* **Granular code reviews:** Trunk-based development encourages smaller, "stacked" changes off of `trunk`, making code reviews more manageable and easier to complete. Additionally, since changes are continuously merged and tested, review feedback cycles tend to be much shorter.

## Getting started with trunk-based development

### Small, batched, or stacked changes

First and foremost, developers must understand how to break their changes up into small, dependent branches—those coming from a feature-branch oriented workflow may find this difficult at first.

### Speedy, frequent code review

The goal of trunk-based development is to merge changes as quickly as possible, while still keeping `trunk` error-free. For this to happen, batched/stacked changes should be reviewed as quickly as possible, so branches exist for less than a day. The longer a branch exists, the higher the chance of introducing bugs and merge conflicts when merging the changes into `trunk`. Breaking up changes into smaller, dependent branches allows developers to have their code reviewed and merged while simultaneously working on new changes.

### Limit the number of active branches and feature flags

Many teams have three or more active branches on a given repository—such as a develop branch, a release branch, several feature branches, and a `main` branch. In trunk-based development, it's **strongly recommended** to keep the number of active branches to a minimum.

Since a team's agility depends on the working status of the `trunk` branch, having multiple open branches makes repairing or reverting bad changes to `trunk` unnecessarily complicated. In situations where developers are inclined to create a feature or release branch as a gate or to develop risky features separately from the `main` branch, using **feature flags** is suggested. Feature flags wrap specific changes in an "inactive" code path and can be conditionally enabled/disabled—eliminating the need for creating another branch and instead introducing the changes directly into `trunk` in a non-destructive way.

### Fast automated test suite and build process

To achieve CI, each commit to a repository must undergo testing before, during, and after it merges into `trunk`, and subsequently trigger an automated build process. As a result, this automated test suite should consist of only short-running integration or unit or acceptance tests, and the automated build process should be quick and repeatable. Automated tests should be reliable (not flaky), and should assess the high-level functionality of the code system—and more comprehensive end-to-end tests can be run later on in development.

## See also

* [Trunk-based development overview](https://trunkbaseddevelopment.com/#)

* [Short-lived feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/)

* [Trunk-based development: deciding factors](https://trunkbaseddevelopment.com/deciding-factors/)

* [Google Cloud Architecture DevOps tech: Trunk-based development](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development)

* [Google Cloud Architecture DevOps tech: Continuous integration](https://cloud.google.com/architecture/devops/devops-tech-continuous-integration)

* [Atlassian: Trunk Based Development](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)


# Update The CLI
Source: https://graphite-58cc94ce.mintlify.dev/docs/update-cli

Learn how to update the Graphite CLI.

## Versions 1.7.4 and greater

```bash Terminal theme={null}
gt upgrade
```

## homebrew

```bash Terminal theme={null}
brew update && brew upgrade withgraphite/tap/graphite
```

## npm

```bash Terminal theme={null}
npm install -g @withgraphite/graphite-cli@stable
```

<Tip>
  If you are having trouble updating through homebrew, fully resetting your tap may fix the issue:
  `brew uninstall graphite && brew untap withgraphite/tap && brew install withgraphite/tap/graphite`
</Tip>


# Update Mid Stack Branches
Source: https://graphite-58cc94ce.mintlify.dev/docs/update-mid-stack-branches

Learn how to make changes to mid-stack branches and auto-restack seamlessly with Graphite CLI.

You can iterate on your stack before it's merged by using the following three concepts:

* Using `gt checkout` to hop between branches in your stack

* Adding changes to a branch using `gt modify`

* Pushing the new changes to remote using `gt submit`

## Prerequisites

You should be familiar with how to:

* [Create branches in a stack](/create-stack)

* [Visualize a stack](/visualize-stack)

* [Navigate a stack](/navigate-stack)

* [Create and submit pull requests](/create-submit-prs)

## Working with commits

Any branch you create with Graphite (using the [recommended workflow](/create-stack#create-your-first-branch-with-the-cli)) will already contain a commit with your initial changes. There are two main ways to update your branch with new changes:

* Maintain the 1:1 relationship between commits and branches, meaning you'll use `gt modify` to continuously amend the commit on the branch (recommended)

* Create multiple commits on each branch using `gt modify --commit` each time you make changes

### Amend commits

By default, the `gt modify` command amends the commit on the branch. Here's how you would address feedback on a branch in the middle of your stack by amending a commit:

```bash Terminal theme={null}
# address review comments by amending a commit


# navigte to the appropriate branch in the stack
gt checkout some_branch_mid_stack


# make some changes to your files


# amend the latest commit on that branch (this automatically restacks any branches upstack)
gt modify -a
# OR don't pass the -a flag to be prompted to stage changes interactively
gt modify


# you can also use aliases for both of these commands
gt co some_branch_mid_stack
gt m -a
```

### Create commits

If you prefer to create an entirely new commit for each of the changes you make to a branch, you can use `gt modify` with the `--commit` flag:

```bash Terminal theme={null}
# navigte to the appropriate branch in the stack
gt checkout some_branch_mid_stack


# make some changes to your files


# create a new commit (this automatically restacks any branches upstack)
gt modify --commit -am "my fourth commit"
# OR don't pass -a or -m to be prompted to enter a commit message and stage changes interactively
gt modify --commit


# you can also use aliases for both of these commands
gt co some_branch_mid_stack
gt m -c
```

### Automatically restack branches

Given that there are no merge conflicts (see next section), `gt modify` will automatically restack any upstack branches on top of your new changes and provide the following output:

```bash Terminal theme={null}
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 my amended commit
Restacked next_branch on some_branch_mid_stack.
Restacked last_branch on next_branch.
```

### Resolve upstack conflicts when modifying branches

If `gt modify` encounters any conflicts as they recursively restack your branches, you'll be prompted to resolve your conflicts before continuing:

```bash Terminal theme={null}
Hit conflict restacking next_branch on some_branch_mid_stack.


You are here (resolving next_branch):
◯ top_branch
◉ next_branch
◯ some_branch_mid_stack
◯ first_branch
◯ main


To fix and continue your previous Graphite command:
(1) resolve the listed merge conflicts
(2) mark them as resolved with gt add .
(3) run gt continue to continue executing your previous Graphite command
It's safe to cancel the ongoing rebase with `gt abort`
```

You can always exit out of the rebase using `gt abort`.

Read more about [restacking branches](/restack-branches).

## Absorbing changes into your stack

While `gt modify` allows you to make changes to a single branch in your stack, Graphite also provides `gt absorb`, which automatically applies your changes to the relevant branches throughout your stack, without needing to check each one out individually.

Each change will be amended into the correct commit in a branch downstack from the currently checked out branch, inclusive.

Before applying the changes, `gt absorb` will show which lines will be absorbed into each commit, and prompt for confirmation (unless the `--force` flag is passed).

```bash Terminal theme={null}
# Receive review comments on your stack


# Make changes


# absorb all changes into the branches downstack of the current branch, inclusive (this automatically restacks any branches upstack)
gt absorb -a
# OR don't pass the -a flag to be prompted to stage changes interactively
gt absorb
```

### How does `gt absorb` work?

For each "hunk" of changed lines, `gt absorb` attempts to "commute" the change with each commit in your stack to find the most recent commit that they do not commute with, which tends to be the correct commit to amend them to. It is possible that a hunk commutes all the way down to your trunk branch, in which case it will not be absorbed into any commit. In this case, you can then apply those changes to the correct branch manually with `gt checkout` and `gt modify`.


# Pull Request Inbox
Source: https://graphite-58cc94ce.mintlify.dev/docs/use-pr-inbox

Think of the pull request inbox as an "email client" for your PRs—it helps you stay organized and view which PRs need your attention.

## Default repositories

Your default repositories are the repositories which your pull request inbox will display PRs for. You can select up to three default repositories on the Graphite free tier, and up to 30 on the Graphite Team and Enterprise tiers.

<Note>
  You can still view pull requests on Graphite in repositories that are not selected in your default repositories. However, they will not show up in your pull request inbox.
</Note>

## Inbox sections

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/014dfd82-1700537534-frame-10123323.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4344ddd17d0369efb3e31b46356cde27" data-og-width="1350" width="1350" data-og-height="1246" height="1246" data-path="images/014dfd82-1700537534-frame-10123323.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/014dfd82-1700537534-frame-10123323.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f5a7a61e5ff28fd83dc19af60da437b0 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/014dfd82-1700537534-frame-10123323.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f54c74486c87c56219757019763c4672 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/014dfd82-1700537534-frame-10123323.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=9729d076fca627dd34e56f33de3a723c 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/014dfd82-1700537534-frame-10123323.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=1707a7cbc903ab7d4c03926dfb5f1c09 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/014dfd82-1700537534-frame-10123323.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ebd6b09ad3d11935b46e2e808aee98c3 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/014dfd82-1700537534-frame-10123323.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4be79843c5de0b6c3394adde7c125ca8 2500w" />
</Frame>

Graphite creates six default sections for you:

* Needs your review

* Approved

* Returned to you

* Merging and recently merged

* Drafts

* Waiting for review

### Add a new section

You can create an entirely new section with custom filters and preferences by clicking the `add new section` button under your existing sections.

### Edit an existing section

You can edit an existing section by clicking the ⚙️ icon on the right side of the section header.

### Rearrange sections

The order of your inbox sections is customizable. Drag the section to rearrange it from the left menu, or the section itself.

### Share sections

You can share your section configs with your teammates by clicking the ⚙️ icon, and scrolling to the bottom to find `Share filters`. This generates a shareable link that your teammates can navigate to in their browser to create a new section with your filters pre-configured.

You can choose to share the filter as-is, or have Graphite dynamically replace your GitHub username with your teammate's usernames as they add in your section config.

Note that this is a one-way export: if you update your section's filter configs, and want your teammates to see the new configurations, generate a new link and share it with them again.

## Search PRs

Search for PRs within the app across your synced repositories. Fuzzy search is supported across PR title, description, author, and more.

Access the search bar in the sidebar menu, or with the `cmd + k` shortcut.


# VS Code Extension
Source: https://graphite-58cc94ce.mintlify.dev/docs/vs-code-extension

Not a CLI person? Graphite's VS Code extension lets you create and manage stacked pull requests visually, right from your IDE.

The Graphite VS Code extension builds directly off of the Graphite CLI - it allows you to break up large engineering tasks into a series of small, incremental code changes directly from your IDE.

## Installation

In order to install the Graphite VS Code extension, make sure that you have the [Graphite CLI installed](/install-the-cli).

After that, you can install the extension from the [Visual Studio marketplace](https://marketplace.visualstudio.com/items?itemName=Graphite.gti-vscode) and the [Open VSX Registry](https://open-vsx.org/extension/Graphite/gti-vscode), or by searching for "Graphite" in the extensions tab of your IDE.

## Launch the extension

You have a few options to start the VS Code extension:

* Click the Graphite icon in your VS Code sidebar (try dragging it to your sidebar!)

* Run the **Graphite: Open Graphite interactive** command from the [command palette](https://code.visualstudio.com/getstarted/userinterface#_command-palette)

* [Define your own keyboard shortcut](https://code.visualstudio.com/getstarted/keybindings) to run the `graphite.open-gti` command

<Tip>
  You can modify the "Show in Sidebar" option in your VS Code settings to display the extension in an editor tab instead of a sidebar tab.
</Tip>

## Current features

* Visualize and manage your stacks within your IDE

* Create new branches

* Modify existing branches

* Submit pull requests

* Sync your trunk branch

* First-class support for [stacking](https://www.stacking.dev/)

### Upcoming features

We're currently working on adding more functionality to the VS Code extension, including detail view for branches and their PRs, the ability to edit PRs via the extension, and more!

### Don't use VS Code?

We're bringing the GUI to other IDEs soon!


# Configuration
Source: https://graphite-58cc94ce.mintlify.dev/docs/vs-code-extension-configuration

Customize the Graphite VS Code extension.

Everyone's IDE is personalized to their own workflow, so we've introduced some customizations to make using the VS Code extension as personalized as possible.

## Branch name vs. PR title

In the "settings" on the top right corner of the extension, you can select whether you'd like to show the branch name or the PR title in the stack visualization by default. When PR title is selected as the default and a branch doesn't have a PR title or a PR yet, we'll show you the branch name.

## Amend vs. commit

In the "settings" on the top right corner of the extension, you can select whether you'd like the default modification of a branch to amend the most recent commit on that branch, or to create an entirely new one on the branch. This corresponds to `gt modify` or `gt modify -c`.

## Draft vs. publish

Choose whether you want to default to creating draft or published PRs upon submitting from the extension. Draft will be selected by default.

## Open stack edit on submit (beta)

Upon submitting from the extension, open Graphite's "stack edit" feature to add reviewers, edit description, tags, etc.

## Filetree display

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=6021d1bcc9f8bd7761a916ada4f76f4a" data-og-width="1384" width="1384" data-og-height="626" height="626" data-path="images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f2ea42b94201e8eb8f9a63b2eb039874 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=76635e87dc10d19f48e56f510303d603 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2bed6f5f02a89f43e565329bf86d36a5 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=3e2c815b73741e75383e951b34bf698c 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b934b28826abd14fae727fd0bcefc3bb 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/570a2f26-1705600451-screenshot-2024-01-18-at-12-51-50-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=29f7c46841a1880b4cfc49e1df181fcb 2500w" />
</Frame>

When focusing the contents of a branch of viewing uncommitted changes, you can click the "..." in the branch pane to adjust the filetree view to:

* Short file names

* Full file paths

* Tree

* One-letter directories

In the same menu, you can opt to show changes by:

* Commit

* [Version](/pull-request-versions)


# Create A Pull Request
Source: https://graphite-58cc94ce.mintlify.dev/docs/vs-code-extension-first-pr

Learn to use the Graphite VS Code extension to create a single pull request.

## Prerequisites

Open VS Code in a repository where you're comfortable making changes. Once you've [installed the Graphite VS Code extension](https://marketplace.visualstudio.com/items?itemName=Graphite.gti-vscode), there will be a Graphite icon on the far left of VS Code.

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=fcc0976d25759fda14bdb7a9e774a6d4" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7f13445eaf593978fe87527b7a7d94ee 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ebe1349b48252bc7a0212f6d1b736c55 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=556601dd422799947dc9c1189fe0c99b 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=cdd6e8a1e05ac57228f740f4cd2950a1 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1b657715463c804468fc25c3271c6cd8 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/95bfb7b8-1708221593-screenshot-2024-02-17-at-8-53-28-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=74a321d510c06fe682c171a7849e78a4 2500w" />

When you click the Graphite icon in the left rail, you'll be asked to configure Graphite if you never have before. Follow the prompts in the extension to set it up.

Once you configure Graphite, you'll see all of the branches in your repository as a tree: for example, in the below example, main has two directly descendent child branches ("Feature A" and "Feature B").

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=be8e037de313853696abd0a2763a46e2" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f07bf0aed1da72181c0d6bf1e99198f9 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=34a3ad1ac4bca3c8ea4ff394de6e98e8 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=89c132ff083e2ded6137b4d86c688e17 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=98dae1f89bd32bab0bb4c6f075760f32 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2cb86a22edc2fd628b8b6113210c63ef 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/da577c6d-1708221624-screenshot-2024-02-17-at-8-57-21-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5227efb213168ae320a0764b22cb7505 2500w" />

Make sure you do not have uncommitted changes in your repository (these will show up as a yellow "uncommitted changes" branch in the Graphite extension). If you do have uncommitted changes, either commit them to a branch or delete them using whatever tools you usually use to work with Git repos before continuing.

## Checkout main

The VS Code extension will show the branch you currently have checked out with a triangle next to the branch name. If you have a branch other than your trunk branch (usually named `main` or `master`) checked out, click on trunk and press checkout to change the branch you have.

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=665106ca489738bf9b75e83e700d1d52" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8e06b68fabaf2f5bc8d9e69249567a78 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=00182332d04e85721617dad7e626276f 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=117038b5f6d22a9878aacdbb5c4cf043 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3389c3d0d70a5903de8699d2671820ed 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1bd00c48f69c3e9d4010340449b1d43b 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/a5851193-1708221770-screenshot-2024-02-17-at-8-57-25-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=161ee4e303622257e2c83c9f111c4b1b 2500w" />

## Make changes

Make changes to your repository, either by adding a file or editing an existing file. That file should now show up under "uncommitted changes" in the extension.

<img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=47c8c149e842df35f2910b9206aa7261" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f7a03d2082c7fdbcf7e9fc45d9cb5d22 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7bd47a06914638f356fbffb3b665178f 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b5b4a76897fad20a24547b8077079279 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=6e57e23c5844ed13281660b5e362ce85 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=760e03facd3cfb39a6270dd53f0c1d5e 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/30a7fe74-1708221908-screenshot-2024-02-17-at-8-57-39-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4e17288fbf24058b48bee90459e509e6 2500w" />

## Stage your changes

Select uncommitted changes, and you'll see all the changed files in your repository (files added, files modified, and files deleted). Clicking the checkbox next to a file allows you to stage it in git (the equivalent of running `git add`).

<img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7f254218a0c8fd29cf66e06f9c11de8d" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=00caa0351aa4dab98a031e07b58003ea 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2b0b58d4e06ec54d4281d8816e969a47 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=56a50fc7a328e12a2b93595b86817c3f 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8915232fda9db8f61b4a874ab1ad1286 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=83b5d4dd63908c05b24969cb858a06eb 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/050fa24a-1708221987-screenshot-2024-02-17-at-8-57-42-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=71792646b1527002f15873603a186fd0 2500w" />

## Create a branch

Once you've staged changes, you can create a new branch by entering a commit title and pressing create branch.

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=914c893cbd14dbfcdb9cd18c480d2dc5" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8622afe9daecee143e028f3455be5fb8 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c556ea74b347afb3b7bd98461bb7c3b0 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=0a1826e0324fe889ac20f7bd76b8c5c3 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=73ac64a9ee5b49ac959bc47f1adef361 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e5390604e006f30e49db7453fd862f8a 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ec8e0860-1708222058-screenshot-2024-02-17-at-8-57-47-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=be6e5dade00f6b64a8bea77851bccca3 2500w" />

Your new branch should now show up in the tree as checked out:

<img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f157359092b649bbd404dd4cde6fde57" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4ed810c8d08e7869a70ceb783e913b49 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=86f7f04a4a7e0399cf2181d7fff350d6 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=da9163eed5ea166f27f980dda6283f4e 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=8417e1f2000f9b9d0966ca942a68d720 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=fa081580866c07f4695b317070c7ce64 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/376cd6fb-1708222250-screenshot-2024-02-17-at-8-57-50-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=74bd152a9004e5af3e37902960572d26 2500w" />

## Submit your branch

Assuming your repository is connected to a remote, you should see a "Sync" button in the top left of the extension pane and an upload button next to any branches that don't yet have a PR opened for them.

Click the upload button next to your first PR to open a draft PR. After opening the PR, there will be a circle next to the branch showing the PR's status (in this case it's open).

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1cea038e7874fdc25f8714a83d3256a2" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=df703809bef367ac725f870dd420692d 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8f7062e816c569c4a0a8d9a01d929745 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=9e9a66a86492d6bb1fb4a2751bd8ffd4 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3ee8a8493e39757e897d6b635832f849 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=03a3edeff940b53c266d66d001a38662 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e0b8685fa9ad905dcca4f68a7342698c 2500w" />

That's it - you just created your first pull request using the Graphite VS Code extension!


# Create PRs For A Stack
Source: https://graphite-58cc94ce.mintlify.dev/docs/vs-code-extension-first-stack

Learn to use the Graphite VS Code extension to create pull requests for a stack.

## Prerequisites

Complete the [Create a pull request](/vs-code-extension-first-pr) guide, and make sure you've:

* Checked out your first PR

* Don't have any uncommitted changes

  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1cea038e7874fdc25f8714a83d3256a2" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=df703809bef367ac725f870dd420692d 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8f7062e816c569c4a0a8d9a01d929745 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=9e9a66a86492d6bb1fb4a2751bd8ffd4 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3ee8a8493e39757e897d6b635832f849 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=03a3edeff940b53c266d66d001a38662 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e0b8685fa9ad905dcca4f68a7342698c 2500w" />

## Stacking

The goal of this guide is to teach you how to [stack](https://stacking.dev/) with the Graphite VS Code extension.

Stacking is a technique to continue developing while you wait for review on PRs. A stacked branch is a branch that is created on top of another branch that is still waiting for review. As that previous branch is updated and ultimately merged into main, Graphite will incorporate those changes into any dependent branches.

If this is confusing now, don't worry - it becomes clearer as you do it.

## Make and stage changes

Like in the earlier guide, make changes to your repository, either by adding a file or editing an existing file. That file should now show up under "uncommitted changes" in the extension.

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1cea038e7874fdc25f8714a83d3256a2" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=df703809bef367ac725f870dd420692d 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8f7062e816c569c4a0a8d9a01d929745 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=9e9a66a86492d6bb1fb4a2751bd8ffd4 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3ee8a8493e39757e897d6b635832f849 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=03a3edeff940b53c266d66d001a38662 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/86d2617d-1708222363-screenshot-2024-02-17-at-8-58-37-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e0b8685fa9ad905dcca4f68a7342698c 2500w" />

Select uncommitted changes, and you'll see all the changed files in your repository (files added, files modified, and files deleted). Clicking the checkbox next to a file allows you to stage it in git (the equivalent of running `git add`).

<img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=22fd3e20ce6fa230d80484a895739239" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ff330f3f23763e56f827111d5b759cc7 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=07b8e216dc5555ed3e626dcd491ef5c4 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=439b9d4c0f0d449660dff132d0fc3160 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a701de5869f8fb3a7836455e22faafad 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f284555f1451da8ee0d5e75ae29fed8c 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/0252bb51-1708223343-screenshot-2024-02-17-at-8-59-01-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a8eeca2d64d0b175e0b1221ea7ef1ecd 2500w" />

## Create a branch

Once you've staged changes, you can either modify the existing branch or create a new stacked branch. Enter a commit title and pressing create branch.

<img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=760fb20f3548f5767492790e842e3537" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c94a2d772e4373742e7736350fe9233a 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1bd5032208e75f44dd794f88d7bd01da 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=4a8d839d0860a2410902ac31ed519a24 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d6a1eaffb92a37701c34da464d7f9a3a 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d730f9de4d12c3bb779e0c1c9af3f98e 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/97450653-1708223392-screenshot-2024-02-17-at-8-59-06-pm.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b564358ca31a0c4637670b913baa5d34 2500w" />

Your new branch should now show up in the tree as checked out and *stacked* on top of the first:

<img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=569adfec1c8f81f2b43a2657e33d76b7" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=71817e8cfa196ff02d49d3c1d5e84ca0 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a14892499cfba5c090b0203125f70fcd 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=72081bef23be1b4ab10a66712b38af61 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=1cfc8e6b1417257f74b86642e29d55c8 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=676db73426cf17287919754dbe5c1412 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/3cefbd87-1708223406-screenshot-2024-02-17-at-8-59-12-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=4fc1c3454d28bf44c03ecfb89e04a010 2500w" />

## Submit your branch

Like the first guide, click the upload button next to your first PR to open a draft PR. After opening the PR, there will be a circle next to the branch showing the PR's status (in this case it's open).

<img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=2db0d108763fe7200998ff519eaf0078" data-og-width="2272" width="2272" data-og-height="1760" height="1760" data-path="images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a7bf2ad772a02b0017110ff6b44fdfe3 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=602f00ef1456ba79fb31fc1efa8f9061 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c1fb7c550396c9f7bf26efd0da1b9fdc 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=c8033838caa5df4596707239655d84f8 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=de345cbda3891ae8a9e2ca370dad27c0 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/144e344f-1708223423-screenshot-2024-02-17-at-8-59-23-pm.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=82b93c387d5b46466df4b96367c53356 2500w" />

That's it - you just created your first stack using the Graphite VS Code extension!


# Quick Start
Source: https://graphite-58cc94ce.mintlify.dev/docs/vs-code-extension-quick-start

Get started using the Graphite VS Code extension to stack pull requests.

## Understand elements of the VS Code extension

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8de2a4f7-1702403419-frame-10123329.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8bb463c49b6da47dd8861c5e87bab72c" data-og-width="1350" width="1350" data-og-height="1246" height="1246" data-path="images/8de2a4f7-1702403419-frame-10123329.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8de2a4f7-1702403419-frame-10123329.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=16e8b4dd88d4ac86c842d5e1af5a6ed2 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8de2a4f7-1702403419-frame-10123329.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7b14ede735e854a22d727033f57747c1 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8de2a4f7-1702403419-frame-10123329.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e5ef697d585d3e89b317932596445afa 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8de2a4f7-1702403419-frame-10123329.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b17aed70606b9a7c0a76cc551b0a071f 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8de2a4f7-1702403419-frame-10123329.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f880d9be58c625ddec62ea2735dae258 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8de2a4f7-1702403419-frame-10123329.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=40b1ea01e521ecd6200ef7dc261e1c10 2500w" />
</Frame>

## Walkthrough video

<Frame>
  <iframe width="750" height="360" src="https://www.youtube.com/embed/TCFa0Sf_5X8?si=uLxzTYILcwrg27rW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

## Check out a branch

There are two ways to check out branch in the VS Code extension:

1. Double-click the branch on the stack view

2. Focus a branch (single-click a branch such that it has a blue outline) and click "check out" in the branch info panel

A checked out branch will be indicated by a blue background/a pointer on the left side of the stack view.

## Focus a branch

Focusing a branch allows you to see what's been changed in the branch without checking it out. To focus a branch, single-click the branch in the visualization such that it has a blue outline. Focusing a branch adjusts the branch info panel so that it shows the files touched by that branch.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/36c613bb-1702403792-video-to-gif-converter.gif?s=396f57854367d789c378154c9f0f0e20" data-og-width="600" width="600" data-og-height="788" height="788" data-path="images/36c613bb-1702403792-video-to-gif-converter.gif" data-optimize="true" data-opv="3" />
</Frame>

## View uncommitted changes

Uncommitted changes are represented by a node labeled "uncommitted changes" on the stack view. To see your uncommitted changes in the extension, focus the "uncommitted changes" node as you would any other branch. The branch info panel will adjust to a staging environment with your local changes.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/355db816-1702403994-frame-10123330.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=15b28ed2c4d12c6063d06e3f8bf35648" data-og-width="1350" width="1350" data-og-height="928" height="928" data-path="images/355db816-1702403994-frame-10123330.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/355db816-1702403994-frame-10123330.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=04c80db62bddd3467cea8874a4608a51 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/355db816-1702403994-frame-10123330.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a3b5a23a831c3f98290efb4f8d6775b8 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/355db816-1702403994-frame-10123330.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b1055c4b7acce61f494eaf8f13b0df2c 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/355db816-1702403994-frame-10123330.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b6be292fa487bbe6484246c331d35e58 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/355db816-1702403994-frame-10123330.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d44a2f08ac05c38dc07f7f674e60a4f4 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/355db816-1702403994-frame-10123330.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=a934de0b537e095f56fddbaf11c10fcb 2500w" />
</Frame>

## Staging and unstaging files

Toggling the checkbox near each file in the uncommitted changes panel will stage or unstage that file independently. Hovering over the file will give you the option to view the diff, or delete those changes.

There are additional options to "stage all," "unstage all," and "delete all changes."

## Creating a new branch/modifying a branch

After staging relevant changes, you can **create a new branch** by entering a commit message and clicking "create new branch."

To modify an existing branch, ensure you have the desired branch checked out, stage relevant changes, check the "modify \<branch-name>" checkbox, and click "commit to the current branch."

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/91b2ce0b-1702404673-frame-10123331.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=37c450a94784890d17a1a0f8b6e9ed9a" data-og-width="1350" width="1350" data-og-height="1174" height="1174" data-path="images/91b2ce0b-1702404673-frame-10123331.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/91b2ce0b-1702404673-frame-10123331.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e81d88374e2a321cb3cc7afe39acab77 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/91b2ce0b-1702404673-frame-10123331.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e971517131f629f0b180e0359ef6424c 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/91b2ce0b-1702404673-frame-10123331.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=70f4af05263018c5a4cdb0312c819dae 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/91b2ce0b-1702404673-frame-10123331.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=98c5b929f040f7f422625d9cf367e496 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/91b2ce0b-1702404673-frame-10123331.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b141e8b1ae0c5ae7d51794cfca9f23c7 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/91b2ce0b-1702404673-frame-10123331.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=617480709e6db0dbf4fe5417eca9b3cd 2500w" />
</Frame>

### Setting default modify behavior

When modifying a branch, you can either create a new commit on that branch, or modify the previous commit on that branch. You can set your preferred behavior in the extension's settings:

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ac32c075-1702404784-frame-10123332.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=266b97279b92107f0bee04913381268f" data-og-width="1224" width="1224" data-og-height="528" height="528" data-path="images/ac32c075-1702404784-frame-10123332.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ac32c075-1702404784-frame-10123332.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e3d1cde2e52dd435fe36d72da5589e2a 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ac32c075-1702404784-frame-10123332.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5bd43ef3ba2486021d8bfedd7a55c31f 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ac32c075-1702404784-frame-10123332.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a53324885b14ff8b67ab218fd598ff7d 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ac32c075-1702404784-frame-10123332.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ea1469ce7604a7b58d7e01365be12390 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ac32c075-1702404784-frame-10123332.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=58c6478e6da6e37d77e6c7135c414fef 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ac32c075-1702404784-frame-10123332.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f7f01c4df16fe2afdbdef01bca1acd92 2500w" />
</Frame>

Note that if your preferred modify behavior is commit, you'll be prompted to enter a commit message before creating the commit. If the default behavior is amend, you won't be prompted to do so.

## Drag to move/rebase branches

You can re-arrange branches by dragging them onto a new parent.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/19c44dee-1702413095-video-to-gif-converter-1.gif?s=08c83cf86f1421e4ae302889fec68bf0" data-og-width="600" width="600" data-og-height="810" height="810" data-path="images/19c44dee-1702413095-video-to-gif-converter-1.gif" data-optimize="true" data-opv="3" />
</Frame>

## Tracking and getting branches

You can track branches onto a parent by clicking the "cloud" icon in the upper right hand corner of the extension. This is equivalent to the CLI's `gt track` and `gt get` commands.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e85d5acb-1705600738-frame-10123333.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=706d8c45ef70af72ddb957f71da5185f" data-og-width="1350" width="1350" data-og-height="1246" height="1246" data-path="images/e85d5acb-1705600738-frame-10123333.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e85d5acb-1705600738-frame-10123333.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2e99dcdc7461b1139e6ae5a259808cad 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e85d5acb-1705600738-frame-10123333.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=5299e8110c7c05feabc87742d2b6cc04 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e85d5acb-1705600738-frame-10123333.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=fb76fe544b3d7c6fbeb636e258567cb4 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e85d5acb-1705600738-frame-10123333.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=e3fc863ac916bb782b10786a83ca9394 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e85d5acb-1705600738-frame-10123333.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=d69c6837de87515a701a5fd3e6872bac 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/e85d5acb-1705600738-frame-10123333.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8a74f9cf3774b01fb10d61a49c272ce3 2500w" />
</Frame>


# Why You Should Use Graphite
Source: https://graphite-58cc94ce.mintlify.dev/docs/why-you-should-use-graphite

One end-to-end tool to simplify and accelerate your team’s developer workflow.

Teams that use stacked pull requests deliver high quality software faster. Graphite is the integrated developer platform that helps teams on GitHub stack.

Graphite puts developer experience first, giving you all of the features you’ve been missing on GitHub: stacked pull requests, intelligent notifications, an advanced, filtered PR inbox, and a completely redesigned CLI that automates tedious complexity like squashing and rebasing.

“Stacking” with Graphite empowers you to:

* **Stay unblocked**. With [stacking](https://stacking.dev), you can keep moving forward and never wait for a code review again.

* **Upgrade from vanilla Git**. Create pull requests much faster and [automate away tedious Git complexity](/comparing-git-and-gt) such as squashing, rebasing, and cleaning up stale branches.

* **Get even more out of the tools you love**. Easily manage stacks of PRs with a [CLI](/cli-overview), web app, and [VS Code extension](/vs-code-extension) that are built for speed and simplicity.

* **Stay on top of feedback & review requests**. Filter out the noise with targeted, actionable [notifications in Slack](/slack-notifications) when you need to act on a PR.

With Graphite, engineers spend more time shipping code and less time wrestling with their workflow.

## Graphite is built for teams

Graphite is designed to make your developer experience even better as your team grows. And with real-time syncing with GitHub, you can use Graphite even if the rest of your team doesn’t yet.

Among active users, we see an **overall decrease of 65% in time elapsed between merged pull requests** once they start using Graphite. Across companies, we found that it takes on average **16% less time before a PR is reviewed**, compared to before they started using Graphite.

Fast-growing companies like Ramp, say [it’s significantly easier to review PRs](https://graphite.com/customer/ramp) with Graphite because you’re only looking at the portion of the PR that’s relevant to you.

<Frame caption="">
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=33f7e9d13f3bf6b331a71ca535066ba7" data-og-width="1730" width="1730" data-og-height="1040" height="1040" data-path="images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=d08e4899acbd7c1778252ad53abbf279 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=408621d2f4a53af4ba507f00816d6085 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=11cea2284acbf478a7ecb4669949bdb6 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e34846f70980ad8c3f6a4c584a424bc3 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=b1ce2937b50bb7e016984890774ce0ec 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/15e1f856-1702072526-1695073379-graphite-ramp-case-study-graphic.webp?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=058c734b60980966a6b903541d7c3b83 2500w" />
</Frame>

### Write better code with Graphite

* **High-quality code review**: stacking encourages smaller pull requests, meaning less context is needed for reviewers to provide meaningful feedback.

* **Faster code review**: you can see the PRs awaiting your review either through the [PR inbox](/use-pr-inbox) or customizable and actionable Slack notifications.

* **A “greener” trunk branch**: Graphite's stack-aware [Merge Queue](/graphite-merge-queue) helps teams ship faster while keeping their trunk branch green.

* **Useful metrics:** with everyone using Graphite, your team can see how your [Insights](/insights) (like number of review cycles until merge, or time until review) improve over time.

* **Memes!** add color to code review with your own [memes and GIFs](/memes-and-macros#upload-new-memes).

### How to help your team get started

It’s easy to share Graphite with your teammates. Use the *Invite others* option in the bottom left of the Graphite App to send a link or email invitation.

You can also set up a demo! [Reach out to our Sales team here](https://graphite.com/contact-us) to schedule.


