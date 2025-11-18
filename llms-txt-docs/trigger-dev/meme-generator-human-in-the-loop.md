# Source: https://trigger.dev/docs/guides/example-projects/meme-generator-human-in-the-loop.md

# Meme generator with human-in-the-loop approval

> This example project creates memes using OpenAI's DALL-E 3 with a human-in-the-loop approval workflow built using Trigger.dev waitpoint tokens.

## Overview

This demo is a full stack example that uses the following:

* A [Next.js](https://nextjs.org/) app, with an [endpoint](https://github.com/triggerdotdev/examples/blob/main/meme-generator-human-in-the-loop/src/app/endpoints/\[slug]/page.tsx) for approving the generated memes
* [Trigger.dev](https://trigger.dev) tasks to generate the images and orchestrate the waitpoint workflow
* [OpenAI DALL-E 3](https://platform.openai.com/docs/guides/images) for generating the images
* A [Slack app](https://api.slack.com/quickstart) for the human-in-the-loop step, with the approval buttons linked to the endpoint

## GitHub repo

<Card title="View the meme generator human-in-the-loop example repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/meme-generator-human-in-the-loop">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Post to Slack

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/slack-meme-approval.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=b1f4a27701fd8f2899e4454f7bb72e91" alt="Meme Generator with Human-in-the-Loop Approval" data-og-width="1073" width="1073" data-og-height="900" height="900" data-path="images/slack-meme-approval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/slack-meme-approval.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=cdc950328aa47c2b6bc01350bca4ee98 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/slack-meme-approval.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a4a89e890e1380f99abad6142284dd44 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/slack-meme-approval.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=661bae7ff1423a52296186cac080e225 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/slack-meme-approval.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=df8f583f34558590e910bfdce86d3f28 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/slack-meme-approval.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3628c0b4def34c6423ac6f09464bd3ed 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/slack-meme-approval.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=4f9d0357cc10f5c9f5e57203987102c5 2500w" />

## Relevant code

* **Meme generator task**:

  * The [memegenerator.ts](https://github.com/triggerdotdev/examples/blob/main/meme-generator-human-in-the-loop/src/trigger/memegenerator.ts) task:
    * Generates two meme variants using DALL-E 3
    * Uses [batchTriggerAndWait](/triggering#yourtask-batchtriggerandwait) to generate multiple meme variants simultaneously (this is because you can only generate 1 image at a time with DALL-E 3)
    * Creates a [waitpoint token](/wait-for-token)
    * Sends the generated images with approval buttons to Slack for review
    * Handles the approval workflow

* **Approval Endpoint**:
  * The waitpoint approval handling is in [page.tsx](https://github.com/triggerdotdev/examples/blob/main/meme-generator-human-in-the-loop/src/app/endpoints/\[slug]/page.tsx), which processes:
    * User selections from Slack buttons
    * Waitpoint completion with the chosen meme variant
    * Success/failure feedback to the approver

## Learn more

To learn more, take a look at the following resources:

* [Waitpoint tokens](/wait-for-token) - learn about waitpoint tokens in Trigger.dev and human-in-the-loop flows
* [OpenAI DALL-E API](https://platform.openai.com/docs/guides/images) - learn about the DALL-E image generation API
* [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
* [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks) - learn about integrating with Slack
