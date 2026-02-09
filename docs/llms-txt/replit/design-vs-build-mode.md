# Source: https://docs.replit.com/tutorials/design-vs-build-mode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Design vs. App Mode

> Learn the difference between Design and App modes in Replit, and when to use each for your projects.

Replit offers two ways to create apps: **Design Mode** and **App Mode**. The best part? You can use them together—start with a beautiful design, refine it, then convert to a fully functional app when you're ready.

## What is Design Mode?

[Design Mode](/replitai/design-mode) lets you create beautiful, interactive websites and app designs in just a few minutes. Simply describe your idea and Replit builds it for you.

Design Mode is perfect for:

* **Testing your ideas quickly**: Visualize your app's design before building functionality
* **Creating polished websites**: Landing pages, portfolios, restaurant menus, event pages
* **Fine-tuning your design**: Adjust colors, layouts, and content instantly

<Info>
  Design Mode apps look and feel like real apps, but they don't store data or connect to external services yet. When you're happy with how everything looks, you can convert your design into a full app with one click. The steps below show you how.
</Info>

## What is App Mode?

App Mode creates real, working applications that can save data, let people sign in, and connect to other services.

Use App Mode when your app needs to:

* **User accounts**: Let people create accounts and log in
* **Save information**: Store data like orders, messages, or user preferences
* **Connect to other services**: Process payments, send emails, or pull in data from other apps
* **Handle complex tasks**: Run an online store, manage bookings, or power a dashboard

## See the difference in action

This comparison shows the same restaurant menu built in both modes using an identical prompt. Switch between tabs to see what each mode created:

<Card>
  <Tabs>
    <Tab title="Design Mode">
      <Frame aspectRatio="16/9">
        <video autoPlay muted loop playsInline aria-label="Design Mode restaurant menu example showing polished design with elegant typography built in one minute" style={{ width: '100%', height: '100%', objectFit: 'contain' }} src="https://cdn.replit.com/sanity/design-mode-menu-trimmed.mp4" />
      </Frame>

      <Info>
        **Design Mode** — Built in 1 minute
      </Info>

      * Beautiful, polished design
      * Elegant typography and layout
      * Perfect for showcasing your vision
      * Static menu (no ordering functionality)
    </Tab>

    <Tab title="App Mode">
      <Frame aspectRatio="16/9">
        <video autoPlay muted loop playsInline aria-label="App Mode restaurant menu example showing fully functional ordering system with database built in seven minutes" style={{ width: '100%', height: '100%', objectFit: 'contain' }} src="https://cdn.replit.com/sanity/app-mode-menu-trimmed.mp4" />
      </Frame>

      <Info>
        **App Mode** — Built in 7 minutes
      </Info>

      * Simple design
      * Fully functional ordering system
      * Database for orders and inventory
      * Ready for production use
    </Tab>
  </Tabs>
</Card>

## Using both modes together

**Design Mode and App Mode are built to work together**. You don't have to choose one or the other. You can start with design and evolve into a full app.

<Steps>
  <Step title="Design first">
    Start in Design Mode to quickly visualize your idea. Focus on how your app looks and feels—the layout, colors, buttons, and user experience.
  </Step>

  <Step title="Refine and iterate">
    Use the [Visual Editor](/replitai/visual-editor) to click directly on elements and adjust them, or chat with Agent to describe changes you want. The changes will appear immediately.

    <Frame>
      <video autoPlay muted loop playsInline aria-label="Demonstration of using the select element tool to click and adjust design elements" src="https://cdn.replit.com/sanity/visual-editor-asset.mp4" />
    </Frame>
  </Step>

  <Step title="Convert to a full app">
    When you're happy with your design and ready to add real functionality, click the **Design** button on the top left, then click **"Convert to App"** in the menu. Agent will add the ability to save data, handle user accounts, and connect to services—all while keeping your design intact.

    <Frame>
      <video autoPlay muted loop playsInline aria-label="Demonstration of converting a Design Mode project to App Mode by clicking Design button and selecting Convert to App" src="https://cdn.replit.com/sanity/convert-to-full-app-mode.mp4" />
    </Frame>

    <Note>
      Agent will prompt you to convert to App Mode when you try to add a database or advanced features.
    </Note>
  </Step>

  <Step title="Publish and share">
    Once your app is built, publish it so anyone can access it online. Replit handles all the technical infrastructure so your app works reliably for your audience.
  </Step>
</Steps>

## When to use each mode

<CardGroup cols={2}>
  <Card title="Start with Design Mode" icon="paintbrush">
    * You want to see your idea quickly
    * You're creating a simple website
    * You want to test different designs
    * Speed is your priority
  </Card>

  <Card title="Go straight to App Mode" icon="cube">
    * You know exactly what you need
    * Your app must save data from day one
    * People need to log in
    * You're connecting to other services
  </Card>
</CardGroup>

<Tip>
  **Not sure which to pick?** Start with Design Mode. It's faster, and you can always convert to App Mode later. Your work is never wasted—it carries over when you upgrade.
</Tip>

## Key differences

| Feature                    | Design Mode                 | App Mode                           |
| -------------------------- | --------------------------- | ---------------------------------- |
| **Speed**                  | A few minutes               | About 10 minutes for complete apps |
| **Data storage**           | Visual only (no saving)     | Saves and retrieves real data      |
| **User accounts**          | Shows what login looks like | Actual login functionality         |
| **Connecting to services** | Not available               | Payments, emails, external data    |
| **Hosting**                | Simple static hosting       | Scales with your audience          |

## Next steps

<CardGroup cols={2}>
  <Card title="Design Mode" icon="paintbrush" href="/replitai/design-mode">
    Learn more about creating designs
  </Card>

  <Card title="Visual Editor" icon="edit" href="/replitai/visual-editor">
    Make visual changes with clicks
  </Card>

  <Card title="Agent" icon="robot" href="/replitai/agent">
    Explore what Agent can build for you
  </Card>

  <Card title="Vibe Coding 101" icon="graduation-cap" href="/tutorials/vibe-coding-101">
    Learn the complete workflow
  </Card>
</CardGroup>
