# Source: https://docs.replit.com/getting-started/quickstarts/build-with-ai.md

# Create a file converter with AI

> Build a file conversion app in 15 minutes using Replit's AI tools. Learn how to use Agent and Assistant to create apps through natural language.

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

Learn how to replace line-by-line coding with AI-powered conversations. This guide shows you how to effectively communicate your vision and leverage Replit's AI tools to bring your ideas to life.

## What you'll learn

<CardGroup cols={2}>
  <Card title="AI Tool Mastery" icon="wand-magic-sparkles">
    Use Agent and Assistant effectively for different development tasks
  </Card>

  <Card title="Clear Communication" icon="comments">
    Learn the art of describing your vision to AI tools
  </Card>

  <Card title="Best Practices" icon="list-check">
    Discover how to provide context and specifications effectively
  </Card>

  <Card title="Rapid Development" icon="rocket">
    Build and publish a working app in just 15 minutes
  </Card>
</CardGroup>

<Note>
  You'll need a Replit account and Core subscription to access Agent.
</Note>

<AccordionGroup>
  <Accordion title="Quick access">
    * [View the finished template](https://replit.com/@matt/msftmd-Office-Markdown-Converter?v=1\&utm_source=matt\&utm_medium=youtube\&utm_campaign=msftmd-app)
    * [Try the live demo](https://msftmd.replit.app/)
  </Accordion>
</AccordionGroup>

<Frame type="glass">
  <iframe src="https://www.youtube.com/embed/JNH2g53T3zE" title="Building a File Converter App with AI Tools" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen height="400" width="100%" />
</Frame>

## Start with Agent

<Steps>
  <Step title="Understand the library">
    We'll use [MarkItDown](https://github.com/microsoft/markitdown), Microsoft's file conversion library. Since it's new, provide Agent with context about its capabilities:

    <AiPrompt>
      MarkItDown is a utility for converting various files to Markdown (e.g., for indexing, text analysis, etc). It supports:

      * PDF
      * PowerPoint
      * Word
      * Excel
      * Images (EXIF metadata and OCR)
      * Audio (EXIF metadata and speech transcription)
      * HTML
      * Text-based formats (CSV, JSON, XML)
      * ZIP files (iterates over contents)

      [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)
    </AiPrompt>

    <Tip>
      Hover over URLs and select "copy content" to give Agent additional context.
    </Tip>
  </Step>

  <Step title="Create your prompt">
    Craft a clear prompt explaining your vision:

    <AiPrompt>
      I'd like to build a simple app that converts office files to markdown. It should have a drag and drop interface and be both desktop and mobile friendly.
    </AiPrompt>
  </Step>

  <Step title="Review the plan">
    Agent will create a development plan outlining:

    * Required files
    * Code structure
    * Implementation steps

    <Frame type="glass">
      <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/02-approve-plan.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=42f3bdef25ac30df361cb12d64e68eaa" alt="Reviewing and approving Agent's initial plan" data-og-width="1896" width="1896" data-og-height="2004" height="2004" data-path="images/getting-started/building-with-ai/02-approve-plan.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/02-approve-plan.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=aa6c8f828c8217519d3f16ceb9105704 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/02-approve-plan.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=94016d6078a411eebd84361f0a1aa3ce 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/02-approve-plan.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=bd207a8e0a8e537a4ea0cdc6ddd34ef7 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/02-approve-plan.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=32241029f9022446691e66cfbdcd5ee6 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/02-approve-plan.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b79e0cbfcfcdae80866f699341d2b3fc 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/02-approve-plan.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=df6a648bcc20b8cf12bc5584c27fc0ae 2500w" />
    </Frame>
  </Step>
</Steps>

## Develop iteratively

### Using Agent for major changes

Agent excels at handling structural changes and core functionality. When you encounter issues:

1. Copy error messages directly into the chat
2. Be descriptive about what's not working
3. Provide clear requirements for new features

<Frame type="glass">
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/04-fix-errors-paste.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=49132ee62a6f26940d8df50c1368e702" alt="Fixing JSON parse error by sharing with Agent" data-og-width="1896" width="1896" data-og-height="2004" height="2004" data-path="images/getting-started/building-with-ai/04-fix-errors-paste.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/04-fix-errors-paste.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=af3da2bb9de02b93f5d932c3c461e241 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/04-fix-errors-paste.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=792baf8a597d04bd4c4274c4134dc8a7 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/04-fix-errors-paste.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=312771e122d771af7504a71d480455a3 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/04-fix-errors-paste.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=4f02a6000f78fac643e7a96876d3f723 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/04-fix-errors-paste.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=dbcf45b5ed47ddcb365a9c80a4207190 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/04-fix-errors-paste.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6c79ef32b697108a792f48618f966fdf 2500w" />
</Frame>

Example prompts for adding features:

<AiPrompt>
  * Make the app more responsive and mobile friendly, the copy and download buttons are cut off on narrow screens
</AiPrompt>

### Refining with Assistant

Switch to Assistant for detailed improvements and UI refinements. Use the `@` symbol to reference specific files:

<AiPrompt>
  * Remove 'Powered by MarkItDown Library' and add a description to the top of the app
  * Add a footer with links to social profiles
</AiPrompt>

<Tip>
  Use web development terms like "responsive," "mobile-friendly," and "grid interface" to communicate effectively.
</Tip>

## Publish your app

<Steps>
  <Step title="Start publishing">
    Select **Publish** or search for "Deployments" in the command bar.
  </Step>

  <Step title="Configure resources">
    For auto-scale published apps, configure:

    * Basic resources (1 CPU, 1GB RAM per instance)
    * Maximum machines (start with 6)
    * Environment variables
    * Run commands
  </Step>

  <Step title="Launch">
    1. Name your app
    2. Select **Publish**
    3. Wait 1-5 minutes for it to go live
    4. Access your app via the provided URL
  </Step>
</Steps>

## Best practices

<CardGroup cols={2}>
  <Card title="Use Agent for">
    * Initial setup
    * Core functionality
    * Major structural changes
    * Error resolution
  </Card>

  <Card title="Use Assistant for">
    * UI refinements
    * Small feature additions
    * Code optimization
    * Documentation
  </Card>
</CardGroup>

<Note>
  Success with AI tools depends more on clear communication than coding expertise. Focus on describing your vision effectively using web development terminology.
</Note>

## Resources

<CardGroup cols={3}>
  <Card title="Template" icon="code" href="https://replit.com/@matt/msftmd-Office-Markdown-Converter?v=1&utm_source=matt&utm_medium=youtube&utm_campaign=msftmd-app">
    Fork the template
  </Card>

  <Card title="Demo" icon="play" href="https://msftmd.replit.app/">
    Try the live demo
  </Card>

  <Card title="Tutorial" icon="video" href="#">
    Watch the video above
  </Card>
</CardGroup>

<Frame type="glass">
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/msftmd.jpg?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b5244db8793852c7b37d85ee9123a933" alt="Published file converter app interface" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/getting-started/building-with-ai/msftmd.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/msftmd.jpg?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d1831f9ab7b57b19eccf966491c66417 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/msftmd.jpg?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c66a929a74756804d9d2f84f3d42bb70 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/msftmd.jpg?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=4c0e268a0bf5f93255be0b065663fe6c 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/msftmd.jpg?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ed3dc02b2e2a46d0d04feb9544ff3938 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/msftmd.jpg?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=42d6ebd6ed5381d277df1851a8586ebc 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/building-with-ai/msftmd.jpg?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b3b95d39d059de1e8261e76e5e6af498 2500w" />
</Frame>
