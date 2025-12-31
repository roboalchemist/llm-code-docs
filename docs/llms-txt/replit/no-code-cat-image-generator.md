# Source: https://docs.replit.com/getting-started/quickstarts/no-code-cat-image-generator.md

# Create a cat image generator

> Build a fun image generator in 5 minutes using Replit's AI tools. Perfect for beginners exploring no-code development.

Learn how to create apps without writing code. This guide shows you how to build a playful cat image generator using Replit's AI tools.

## What you'll learn

<CardGroup cols={2}>
  <Card title="AI Development" icon="wand-magic-sparkles">
    Create apps through natural language conversations
  </Card>

  <Card title="No-Code Building" icon="code">
    Build without writing code
  </Card>

  <Card title="Tool Selection" icon="screwdriver-wrench">
    Choose the right AI tool for each task
  </Card>

  <Card title="Deployment" icon="rocket">
    Take your app live in minutes
  </Card>
</CardGroup>

<Note>
  You'll need a Replit account and Core subscription to access Agent.
</Note>

<Frame type="glass">
  <iframe src="https://www.youtube.com/embed/ji8C1LxWyXU" title="Build a Cat Generator App in 5 Minutes" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen height="400" width="100%" />
</Frame>

## Start with Agent

<Steps>
  <Step title="Open Replit">
    Head to [Replit](https://replit.com) and sign in. You'll see the prompt editor where you can instruct Agent.

    <Frame type="glass">
      <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/prompt.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f54d31b1878ca5877bc5cfbac8655637" alt="Replit's AI prompt interface showing where to enter instructions for the Agent" data-og-width="3412" width="3412" data-og-height="2672" height="2672" data-path="images/getting-started/build-without-code-cat-generator/prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/prompt.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=05d40645e24f2ff097f4403ddfc01d84 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/prompt.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=68496669a1f6d4d4e4bc768140b80c10 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/prompt.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=8e896f445527a151c6617134293037df 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/prompt.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=78f809a562be0034321c72e763e03553 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/prompt.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6b546229e42ce130a6ab570bdc3b78f4 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/prompt.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=df77cc6d91563c0ae29ec2b429b59b0f 2500w" />
    </Frame>
  </Step>

  <Step title="Create your prompt">
    Start with a simple request:

    ```text  theme={null}
    Let's build a cat generator that displays a random image of a cat from the internet 
    every time I press a button.
    ```

    <Tip>
      Use the "Improve Prompt" button to add more details to your request.
    </Tip>
  </Step>

  <Step title="Review the plan">
    Agent will outline a development plan using Flask and JavaScript. Don't worry about the technical terms—Agent handles the complexity for you.

    <Frame type="glass">
      <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-plan.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6d0e96bbcc978708d8919c223ec20d50" alt="Agent's proposed development plan for creating the cat generator application" data-og-width="3412" width="3412" data-og-height="2672" height="2672" data-path="images/getting-started/build-without-code-cat-generator/agent-plan.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-plan.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=44d7d67b9a50960c268ac16e93a1025a 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-plan.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b58ba0f159a30c426104a33f5fc4c6c0 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-plan.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2e5dafe13af364114033619a80782957 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-plan.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ef6695597f15bb613f97b02a4d610b16 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-plan.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=127e22ef3cf2206bc614f6adf00edd6e 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-plan.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c7b146b6d9f7e7cda510e2ca5d22af24 2500w" />
    </Frame>
  </Step>
</Steps>

## Develop iteratively

### Using Agent for major changes

Agent excels at structural changes and core functionality. Try improving the UI:

```text  theme={null}
Can you change the UI to be more beautiful and playful? Use cat emojis to improve 
the appearance of the app.
```

<Frame type="glass">
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=7577292b23df0ba4e393253107d79b15" alt="Agent interface showing UI improvement suggestions with emoji additions" data-og-width="3412" width="3412" data-og-height="2672" height="2672" data-path="images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6d26fcdb5585826231007f96777fa053 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=70d6c87934b57fcaf095c8ae7ac7d5a3 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=8953fbbfb46041eaa03ff5817306f004 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=fa37a4636133902be9db00d37aa10326 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=477f670ed7e41bf142fbf97cc3dfcda6 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/agent-making-style-improvements.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=32efa6a410fe7c96a701c038bec982c4 2500w" />
</Frame>

### Refining with Assistant

Switch to Assistant for targeted improvements. For example, add dark mode:

```text  theme={null}
Can we add a dark mode to the app with a toggle button to switch between dark 
and light mode?
```

<Frame type="glass">
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2ade567d75bf5d6aa11e49378ebdf22a" alt="Preview of code changes made by Assistant for implementing dark mode" data-og-width="3412" width="3412" data-og-height="2672" height="2672" data-path="images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2c77b30bcdc802c606007cc0ecad0960 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=4167df879e5aa5b9284d2b4eb5d2ca6c 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ce4d87c8b73ada54078c43ed01fb4cbc 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b254d02dbee0efe5b06fda88a3a7c68c 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=3e7ee0ddf784eefdae52accd6cb2d430 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-preview-edits.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=a5f7ba11e35659f391648371f9d421a1 2500w" />
</Frame>

<Tip>
  Ask Assistant to explain how your app works:

  ```text  theme={null}
  Help me understand the framework this app is built on.
  ```
</Tip>

<Frame type="glass">
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=3e9cd5dd02a7d5a8c7708db7d25c7d71" alt="Assistant explaining the application's framework and architecture" data-og-width="3412" width="3412" data-og-height="2672" height="2672" data-path="images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=40c5af4cd8531b2ea1c77a1d91249950 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=70f3cd07a77a1684917c5f19ee833c91 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=9ca1c3d7afa27578148ad8f4e8aa73b9 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=a5a3308933efd4d97ca5bc56b5022520 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d8672f3dec7ec3fe8321e057708cc743 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/assistant-ask-about-architecture.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=7a5fe85d2a7f49f35a9c06bd5f7ea695 2500w" />
</Frame>

## Publish your app

<Steps>
  <Step title="Start publishing">
    Select **Publish** in the top navigation.
  </Step>

  <Step title="Configure">
    1. Choose the recommended publishing option
    2. Name your app (e.g., "whisker-wonder")
    3. Select **Publish**
  </Step>

  <Step title="Go live">
    Wait 2-3 minutes for publishing. Your app will be available at `your-app-name.replit.app`.

    <Frame type="glass">
      <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/deploy.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f1ce2c914182a1b05f7b79ff2047e2de" alt="Step-by-step publishing process showing how to publish the cat generator app" data-og-width="3412" width="3412" data-og-height="2672" height="2672" data-path="images/getting-started/build-without-code-cat-generator/deploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/deploy.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=fd71f7b4372b073f349492fded31052e 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/deploy.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=05d92c5bea1bfc513e931f4993f723c7 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/deploy.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6632e3d90929fa92b6457c04c6d784fe 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/deploy.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=cc334fb2b9b0b27cc7daf09ae782081e 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/deploy.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b42f3f6d705e7d6a0f37309669c148c3 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/build-without-code-cat-generator/deploy.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=20690b9fe1575f0794a78d011c1d6612 2500w" />
    </Frame>
  </Step>
</Steps>

## Best practices

<CardGroup cols={2}>
  <Card title="Development tips">
    * Start simple and iterate
    * Don't worry about technical details initially
    * Provide context in prompts
  </Card>

  <Card title="Tool selection">
    * Use Agent for broad changes
    * Switch to Assistant for specific improvements
    * Test locally before publishing
  </Card>
</CardGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="Databases" icon="database" href="/cloud-services/storage-and-databases/sql-database">
    Add data persistence with ReplDB
  </Card>

  <Card title="Cloud Services" icon="cloud" href="/category/replit-deployments">
    Learn about publishing options
  </Card>

  <Card title="Custom Domain" icon="globe" href="/cloud-services/deployments/custom-domains">
    Set up your own domain name
  </Card>
</CardGroup>

## Related guides

<CardGroup cols={2}>
  <Card title="Create a file converter" icon="file-arrow-up" href="/getting-started/quickstarts/build-with-ai">
    Build a file conversion app using Agent and Assistant
  </Card>

  <Card title="Create a Slack summarizer" icon="slack" href="/getting-started/quickstarts/ai-slack-channel-summarizer">
    Build a bot that summarizes Slack channels with AI
  </Card>
</CardGroup>

<Note>
  Want to learn more about Replit's AI tools? Check out [Replit AI](/category/replit-ai/).
</Note>
