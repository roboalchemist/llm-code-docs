# Source: https://docs.replit.com/tutorials/create-apps-with-grok-3.md

# Publish a Grok 3 app on Replit in 5 minutes

> Learn how to use Grok 3 and Replit to build and publish a brick breaker game without writing a single line of code.

export const AuthorCard = ({img = "https://replit.com/cdn-cgi/image/width=256,quality=80,format=auto/https://storage.googleapis.com/replit/images/1730840970400_e885f16578bbbb227adbfeb7b979be34.jpeg", href = "https://youtube.com/@mattpalmer", name = "Matt Palmer", role = "Head of Developer Relations"}) => {
  return <a href={href} target="_blank" className="card block not-prose font-normal group relative my-2 ring-2 ring-transparent rounded-xl bg-white/50 dark:bg-codeblock/50 border border-gray-100 shadow-md dark:shadow-none shadow-gray-300/10 dark:border-gray-800/50 overflow-hidden cursor-pointer hover:!border-primary dark:hover:!border-primary-light">
      <div className="flex items-center gap-2 p-4">
        <div className="flex-shrink-0">
          <img src={img} alt={name} className="w-12 h-12 rounded-full object-cover" />
        </div>
        <div className="flex-grow">
          <h3 className="text-base font-semibold mb-0.5 text-inherit">{name}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400 m-0">{role}</p>
        </div>
      </div>
    </a>;
};

<AuthorCard />

Have you ever wished you could create a fun, playable game without writing a single line of code?

With Grok 3 and Replit, you can turn this wish into reality in just minutes.

<Frame>
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/pvOsDB3xUWg" title="Create a Brick Breaker Game Without Code" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

## What you'll build

In this guide, you'll learn how to:

* Create a functioning brick breaker game using AI
* Publish your game online with zero coding knowledge
* Combine Grok 3 and Replit to build real applications
* Share your creation with friends through a public URL

## What you'll need

Before getting started, you'll need:

* A [Replit account](https://replit.com/signup)
* An X account logged into [grok.com](https://grok.com)

That's it! No programming experience, no special software, no complicated setups.

## Building your game step by step

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-1.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8ff08b95593913f6ba2f3150e92e9503" alt="Replit interface showing Grok 3 code and Replit Assistant setting up the server" data-og-width="5120" width="5120" data-og-height="2880" height="2880" data-path="images/tutorials/brick-breaker-grok-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-1.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c79caeb2359e481fb717eda734c1d7e0 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-1.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=38ebb31349548145b6026ba963057bc6 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-1.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=2922affb935f8fb8e286eac80c591979 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-1.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=447d4fbe6572e614cf99f822451f6816 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-1.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=4ddef80200520f4e3241d38372db2006 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-1.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=7944989e54a9db37d7b9cbee16c569f3 2500w" />
</Frame>

<Steps>
  <Step title="Generate your game code with Grok 3">
    Ask Grok 3: **"Help me create a brick breaker game with HTML."** Grok 3 will
    quickly generate all the HTML code needed for a functioning game. Don't
    worry about understanding the code—that's the beauty of this process!
  </Step>

  <Step title="Set up your Replit environment">
    * Log into Replit - From the homepage, create a Node app - Create a new file
      called `game.html` - Paste the code Grok generated into this file Replit's
      [Workspace](/category/workspace-features) makes it incredibly easy to manage
      your files and see real-time updates.
  </Step>

  <Step title="Configure your app with Replit Assistant">
    * Go to Assistant in Replit - Type "serve the game in @game.html" (the @
      symbol mentions the file) - Select enter [Replit
      Assistant](https://docs.replit.com/replitai/assistant) will automatically
      configure the app settings, install any needed dependencies, and set up a
      server around your game in index.js.
  </Step>

  <Step title="Test your game locally">
    After applying all the changes, your brick breaker game will be running in
    your browser. You can play it right away in the
    [Webview](https://docs.replit.com/replit-workspace/workspace-features/webview)
    to make sure everything works properly!
  </Step>

  <Step title="Publish your game to the internet">
    * Select the **Publish** button - Name your project (e.g.,
      "brick-breaker-grok") - Let Replit handle all the technical publishing
      details - Wait about two minutes for publishing to complete Replit's
      [Deployments](https://docs.replit.com/cloud-services/deployments/about-deployments)
      system takes care of setting up servers, configuring domains, and ensuring
      your game runs smoothly online.
  </Step>
</Steps>

## The result: Your own publicly available game

Once published, your game is accessible to anyone through a public URL (like brickbreakergrok.replit.app). This isn't just running on your computer—it's a Replit App on the internet that anyone can play!

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-2.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9f2cd22dbc3aa41042071a739aa25075" alt="The published brick breaker game running with blue bricks, ball, and paddle" data-og-width="5120" width="5120" data-og-height="2880" height="2880" data-path="images/tutorials/brick-breaker-grok-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-2.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=4e03c3f8c50d5bdd59eeb9f68d32180f 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-2.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f51c493e96797a3129569ffea650482a 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-2.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9838a69d5d89a757c20eb7e7637e3247 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-2.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=5d6cd15ea4ec4390b6385696132be631 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-2.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=01c42927ff469ef78dd0d057234e3874 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/brick-breaker-grok-2.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f544d9b7ac3084c82d17af6fca1532b7 2500w" />
</Frame>

You can even [monitor your published app](https://docs.replit.com/cloud-services/deployments/monitoring-a-deployment) to see how many people are playing your game and how it's performing.

## Why this matters

This simple demonstration shows how dramatically technology has evolved. Just a few years ago, creating and publishing a game would have required:

* Learning multiple programming languages
* Understanding web servers and hosting
* Dealing with complex publishing processes

Today, you can do it all through conversation with AI and a few clicks. Replit is the fastest way to go from idea to app.

## Take your game further

<AccordionGroup>
  <Accordion title="Customize your game">
    Use Replit Assistant to help you customize your game: - Change colors,
    graphics, and game elements - Adjust difficulty levels - Add sound effects
    or background music Simply describe what you want to change, and Assistant
    will help implement it.
  </Accordion>

  <Accordion title="Add advanced features">
    Take your game to the next level with: - Score tracking and leaderboards -
    Multiple game levels - Power-ups and special abilities Ask Assistant: "Help
    me add a scoring system to my brick breaker game"
  </Accordion>

  <Accordion title="Share and promote">
    Once your game is published: - Add a [custom
    domain](https://docs.replit.com/cloud-services/deployments/custom-domains)
    for a professional touch - Share the link on social media - Get feedback
    from friends and family Replit makes updating your published app simple -
    just make changes and republish.
  </Accordion>
</AccordionGroup>

## What will you build next?

The brick breaker game is just the beginning. Using the same approach, you could create:

* Interactive quizzes
* Simple productivity tools
* Personal websites
* And much more!

## Your next steps

Ready to build your own app without writing code?

1. [Create a Replit account](https://replit.com/signup) if you haven't already
2. Visit [grok.com](https://grok.com) and log in with your X account
3. Follow the steps in this guide to create your first application
4. Share your creation with friends and family

Happy building!
