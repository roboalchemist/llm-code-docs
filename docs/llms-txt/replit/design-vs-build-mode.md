# Source: https://docs.replit.com/tutorials/design-vs-build-mode.md

# Design vs. Build Mode

> Learn the difference between Design and Build modes in Replit, and when to use each for your projects.

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

Replit gives you two ways to create apps: **Design Mode** and **Build Mode**. The best part? You can use them together—start with a beautiful design, perfect it, then upgrade to a fully functional app when you're ready.

<YouTubeEmbed videoId="MLqYxlyWw3M" />

## What is Design Mode?

[Design Mode](/replitai/design-mode) lets you create beautiful, interactive websites and app designs in just a few minutes. Think of it as a smart design tool that understands what you want. Just describe your idea and Replit will build a beautiful design for you.

Design Mode is perfect for:

* **Testing your ideas quickly**: See what your app could look like before committing to building it
* **Creating simple websites**: Landing pages, portfolios, restaurant menus, event pages
* **Refining the look and feel**: Adjust colors, layouts, and content instantly

<Info>
  Designs created in Design Mode look and feel like real apps, but they don't store data or connect to external services yet. When you're happy with how everything looks, you can convert your design into a full app with one click.
</Info>

## What is Build Mode?

Build Mode creates complete, working applications—the kind that can save information, recognize users, and connect to other services.

Use Build Mode when your app needs to:

* **Remember users**: Let people create accounts and log in
* **Save information**: Store data like orders, messages, or user preferences
* **Connect to other services**: Process payments, send emails, or pull in data from other apps
* **Handle complex tasks**: Run an online store, manage bookings, or power a dashboard

## Using both modes together

**Design Mode and Build Mode are built to work together**. You don't have to choose one or the other. You can start with design and evolve into a full app.

<Steps>
  <Step title="Design first">
    Start in Design Mode to quickly visualize your idea. Focus on how your app looks and feels—the layout, colors, buttons, and user experience. Make changes instantly until it looks exactly right.
  </Step>

  <Step title="Refine and iterate">
    Use the [Visual Editor](/replitai/visual-editor) to click directly on elements and adjust them, or chat with Agent to describe changes you want. There's no waiting—changes appear immediately.
  </Step>

  <Step title="Convert to a full app">
    When you're happy with your design and ready to add real functionality, click **"Convert to App"**. Your design becomes the foundation for a complete application. Agent will add the ability to save data, handle user accounts, and connect to services—all while keeping your design intact.

    <Frame>
      <img src="https://mintcdn.com/replit/4g3URu-HpYwFA1bc/images/tutorials/convert-design-mode-to-build-mode.webp?fit=max&auto=format&n=4g3URu-HpYwFA1bc&q=85&s=72dd5d0e74f4bcbcd1aafc3abc7d52f8" alt="Converting a design to a full app in Replit" data-og-width="1132" width="1132" data-og-height="648" height="648" data-path="images/tutorials/convert-design-mode-to-build-mode.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/4g3URu-HpYwFA1bc/images/tutorials/convert-design-mode-to-build-mode.webp?w=280&fit=max&auto=format&n=4g3URu-HpYwFA1bc&q=85&s=1d5c0702e5322d60df931dca30bdbb35 280w, https://mintcdn.com/replit/4g3URu-HpYwFA1bc/images/tutorials/convert-design-mode-to-build-mode.webp?w=560&fit=max&auto=format&n=4g3URu-HpYwFA1bc&q=85&s=044d3285a8867a9d38eb736b280372eb 560w, https://mintcdn.com/replit/4g3URu-HpYwFA1bc/images/tutorials/convert-design-mode-to-build-mode.webp?w=840&fit=max&auto=format&n=4g3URu-HpYwFA1bc&q=85&s=4420a2cf7ce620b082aa148e960a30b9 840w, https://mintcdn.com/replit/4g3URu-HpYwFA1bc/images/tutorials/convert-design-mode-to-build-mode.webp?w=1100&fit=max&auto=format&n=4g3URu-HpYwFA1bc&q=85&s=7aca3445caa7023a2c167fb899ce95b1 1100w, https://mintcdn.com/replit/4g3URu-HpYwFA1bc/images/tutorials/convert-design-mode-to-build-mode.webp?w=1650&fit=max&auto=format&n=4g3URu-HpYwFA1bc&q=85&s=760b7de9c3be3b02c4e5865e4525f162 1650w, https://mintcdn.com/replit/4g3URu-HpYwFA1bc/images/tutorials/convert-design-mode-to-build-mode.webp?w=2500&fit=max&auto=format&n=4g3URu-HpYwFA1bc&q=85&s=088462c819f2384ded99997f300cd2e1 2500w" />
    </Frame>
  </Step>

  <Step title="Deploy and share">
    Once your app is built, deploy it so anyone can access it online. Replit handles all the technical infrastructure—servers, security, and scaling—so your app works reliably for your users.
  </Step>
</Steps>

## When to use each mode

<CardGroup cols={2}>
  <Card title="Start with Design Mode" icon="paintbrush">
    * You want to see your idea quickly
    * You're creating a simple website
    * You want to test different looks
    * Speed is your priority
  </Card>

  <Card title="Go straight to Build Mode" icon="cube">
    * You know exactly what you need
    * Your app must save data from day one
    * Users need to log in
    * You're connecting to other services
  </Card>
</CardGroup>

<Tip>
  **Not sure which to pick?** Start with Design Mode. It's faster, and you can always convert to Build Mode later. Your work is never wasted—it carries over when you upgrade.
</Tip>

## Key differences

| Feature                    | Design Mode                 | Build Mode                         |
| -------------------------- | --------------------------- | ---------------------------------- |
| **Speed**                  | A few minutes               | About 10 minutes for complete apps |
| **Data storage**           | Visual only (no saving)     | Saves and retrieves real data      |
| **User accounts**          | Shows what login looks like | Actual login functionality         |
| **Connecting to services** | Not available               | Payments, emails, external data    |
| **Hosting**                | Simple static hosting       | Scales with your users             |

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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.replit.com/llms.txt