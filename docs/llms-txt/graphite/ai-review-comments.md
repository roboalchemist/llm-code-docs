# Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-review-comments.md

# Review comments

> Understanding Graphite Agent's feedback and how to get the most value from it

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
