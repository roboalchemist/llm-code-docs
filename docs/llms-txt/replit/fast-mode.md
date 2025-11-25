# Source: https://docs.replit.com/replitai/fast-mode.md

# Fast Mode

> Make targeted changes in seconds with Agent's Fast mode. Up to 5x faster. Free for a limited time.

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

Fast mode is a lightning-quick version of Replit Agent optimized for targeted changes. Get visual tweaks, bug fixes, and reasonable-sized features in 10-60 seconds instead of waiting minutes. Perfect for rapid iteration and pair programming.

<Tip>
  **Free for a limited time!** Fast mode is 100% free for all users during the limited-time promotional period. Try it now to experience faster development at no cost.

  *As of November 19, 2025, this promotion is active but may end at any time.*
</Tip>

## What is Fast Mode?

Fast mode is a specialized Agent experience designed for speed and precision. While the full Agent excels at creating comprehensive applications and implementing complex features, Fast mode focuses on quick, scoped changes that don't require extensive planning or testing.

<Note>
  **Fast mode requires an existing app or project.** Use Fast mode to make changes within apps you've already created. To build a new app from scratch, use the full Agent experience.
</Note>

Think of Fast mode as your pair programming partner for those moments when you need focused changes within your existing app. It's built to keep you in flow without having to step away from your computer while waiting for longer builds to complete.

Fast mode is primarily accessed via the lightning bolt (⚡) icon in the Agent prompt box, and can also be toggled through the Autonomy level control in Agent Tools.

<Frame>
  <img src="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-disabled.png?fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=069f37aceb5107f5b7179918f49d04d5" alt="Agent input box showing the lightning bolt Fast mode icon available for selection" data-og-width="1377" width="1377" data-og-height="276" height="276" data-path="images/replitai/fast-mode-disabled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-disabled.png?w=280&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=936a22130cd47d411e75f70853636684 280w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-disabled.png?w=560&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=9403413b13a4182ae2a156c263574880 560w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-disabled.png?w=840&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=d82a7eff2017401e6e47e79dd1d7807e 840w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-disabled.png?w=1100&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=09c3ee135085bfc30dc1bf5dac34ca82 1100w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-disabled.png?w=1650&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=1d6a84a923643efe189a4c15f52804b1 1650w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-disabled.png?w=2500&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=ac4e82ea4e079cbc87f5c5611a97c510 2500w" />
</Frame>

## When to Use Fast Mode

Fast mode is ideal for:

* **Visual tweaks**: Adjusting colors, spacing, fonts, or layout elements
* **Reasonable-sized features**: Adding search bars, creating loading states, building form validation, or adding sorting functionality
* **Quick fixes**: Correcting typos, fixing broken links, or addressing minor bugs
* **Rapid iteration**: Making a series of focused changes while actively developing
* **Scoped updates**: When you know exactly what you want changed and don't need extensive planning

Fast mode may not be suitable for:

* **Creating new apps**: Fast mode only works within existing apps—use full Agent to start from scratch
* **Complex features**: Multi-file changes that require architectural decisions
* **Large-scale refactoring**: Restructuring code across multiple components
* **New integrations**: Adding third-party APIs or services
* **Database schema changes**: Modifying data structures or relationships

For these larger tasks, use the full Agent experience which includes comprehensive planning, testing, and validation.

## Features

Fast mode delivers a streamlined development experience with the following capabilities:

* **Lightning-fast execution**: Complete most changes in 10-60 seconds
* **Targeted modifications**: Makes only the changes you request without expanding scope
* **Cost-effective development**: Significantly cheaper than full Agent builds (free during promotional period)
* **Real-time pair programming**: Stay at your computer and keep building without long waits
* **Predictable results**: Focused changes mean fewer surprises and more control

## How to Use Fast Mode

### Primary Access: Lightning Bolt Button

The quickest way to toggle Fast mode is using the lightning bolt (⚡) icon in the Agent prompt box:

<Frame>
  <img src="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-enabled-input-box.png?fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=b0bf5f5634bb2a29767062db68f4a92a" alt="Agent input box with Fast mode enabled, showing 'Quick, lightweight changes (free for a limited time)' text and highlighted lightning bolt icon" data-og-width="1377" width="1377" data-og-height="264" height="264" data-path="images/replitai/fast-mode-enabled-input-box.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-enabled-input-box.png?w=280&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=63f703aafb50b767896a769d14065557 280w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-enabled-input-box.png?w=560&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=53818514ade45474d539518e300a67ab 560w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-enabled-input-box.png?w=840&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=1aa0aef073f101b35b2e71d8f980dfdb 840w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-enabled-input-box.png?w=1100&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=134889d1fa804b1a9380296aecd1a6a2 1100w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-enabled-input-box.png?w=1650&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=8755ee7fc52147385e899286458226ab 1650w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-enabled-input-box.png?w=2500&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=b1c0a4724d0981df2c2a5d4d98b2698b 2500w" />
</Frame>

1. Open Agent in your Replit App
2. Click the ⚡ icon in the prompt box to enable Fast mode
3. Make your request—keep it focused and specific
4. Toggle off when you need full Agent for complex tasks

### Alternative Access: Agent Tools

You can also access Fast mode from Agent Tools:

<Frame>
  <img src="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-agent-tools.png?fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=8d397ff3e42d9ecf1d06bde090653663" alt="Agent Tools panel showing Fast mode option with 'Make lightweight changes, quickly' description and Autonomous option below with autonomy level controls" data-og-width="2296" width="2296" data-og-height="2072" height="2072" data-path="images/replitai/fast-mode-agent-tools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-agent-tools.png?w=280&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=13b94e1c470c5553ce9bf7eff64da27e 280w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-agent-tools.png?w=560&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=0a60398c2ff91ae7b124cf4845a3dddb 560w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-agent-tools.png?w=840&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=c2932c6a9d94ecb8a314a8e6d3d62c78 840w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-agent-tools.png?w=1100&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=d78a56d39bfa9c96b951f4a6b570a56a 1100w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-agent-tools.png?w=1650&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=02e6dcc034d6861585c9de20de3e5dda 1650w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-agent-tools.png?w=2500&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=8348820fe9b0229380e57dec60f0e831 2500w" />
</Frame>

Open the Agent Tools panel and select **Fast** from the options. Fast mode and Autonomous mode are two distinct approaches: choose Fast when you want quick results while staying at your computer, or Autonomous when you prefer more reliable, longer builds and can step away for a few minutes or more.

### Example Prompts

**Good for Fast mode:**

* "Change the submit button text from 'Send' to 'Submit Application'"
* "Increase the padding in the card component to 24px"
* "Add email validation to the signup form"
* "Make the sidebar background color darker"
* "Add a search bar to filter the product list"
* "Create a loading spinner when data is fetching"

**Use full Agent for:**

* "Build a new todo app from scratch"
* "Redesign the entire user dashboard"
* "Add user authentication with Replit Auth"
* "Integrate Stripe payment processing"
* "Add a Linear connector"

## How Fast Mode Works

Fast mode uses a streamlined version of Agent's AI technology that's optimized for speed and scoped changes:

1. **Focused analysis**: Fast mode analyzes only the relevant files for your specific request
2. **Direct implementation**: Makes changes immediately without extensive planning phases
3. **Streamlined execution**: Skips comprehensive testing and architecture review for faster results
4. **Quick validation**: Performs basic checks to ensure changes don't break existing functionality

This approach allows Fast mode to deliver results up to 5x faster for scoped requests while maintaining quality for the types of focused, well-defined changes it's designed to handle.

### What's Different in Fast Mode

To achieve faster speeds, Fast mode disables certain features:

**Disabled in Fast mode:**

* **Autonomy levels**: Fast mode and Autonomous mode are mutually exclusive—choose Fast for speed or Autonomous for reliability
* **App Testing**: No automated browser testing
* **Architect**: No architectural analysis
* **High Power models**: Uses faster, more efficient models

**Still available:**

* **Web search**: Access real-time information
* **Other Agent tools**: File operations, code editing, image generation, and more

## Pricing

<Tip>
  **100% free for everyone!** Fast mode is completely free for all Replit users—whether you're on a free account, Core, or Teams. As of November 19, 2025, this promotion is active but may end at any time.
</Tip>

During the promotional period, you'll see "Free" displayed in your Agent usage summary:

<Frame>
  <img src="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-free-during-promo.png?fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=5ab2c86e30a2c396840a3650d74b8819" alt="Agent usage summary showing time worked, work done, and Agent Usage marked as Free during promotional period" data-og-width="2048" width="2048" data-og-height="1424" height="1424" data-path="images/replitai/fast-mode-free-during-promo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-free-during-promo.png?w=280&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=fb07ad3dfcd4377006f60568d00e4e08 280w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-free-during-promo.png?w=560&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=2431be8b2b2a6204f308c3be5a1f72f0 560w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-free-during-promo.png?w=840&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=274b1b2cb1f980304e949b4f6021903f 840w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-free-during-promo.png?w=1100&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=650694c82396480e189cc7cf048b69f8 1100w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-free-during-promo.png?w=1650&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=6532a58d5effa0149c75492d58d381d3 1650w, https://mintcdn.com/replit/fUBynrgsw7g2R6xj/images/replitai/fast-mode-free-during-promo.png?w=2500&fit=max&auto=format&n=fUBynrgsw7g2R6xj&q=85&s=425a987914bd07d483fc27d8bda5289d 2500w" />
</Frame>

After the promotional period ends, Fast mode will offer significant cost savings compared to full Agent builds, with effort-based pricing that charges less for focused, scoped requests.

## Use Cases

**Visual iteration**: Quickly try different colors, spacing, and layouts while actively designing

**Reasonable-sized features**: Add scoped functionality like search filters, form validation, or loading states

**Bug fixes**: Polish details rapidly before launch

## Comparison: Fast Mode vs. Full Agent

| Feature         | Fast Mode                      | Full Agent                        |
| --------------- | ------------------------------ | --------------------------------- |
| **Speed**       | 10-60 seconds                  | 3-10+ minutes                     |
| **Best for**    | Targeted, scoped changes       | Complex features and full apps    |
| **Scope**       | Focused, well-defined requests | Multi-file, architectural changes |
| **Testing**     | Basic validation               | Comprehensive App Testing         |
| **Code Review** | None                           | Available with autonomy levels    |
| **Planning**    | Minimal                        | Detailed task lists and proposals |
| **Cost**        | Lower (free during promo)      | Higher for complex builds         |

## Tips for Success

* **Use Fast mode for iteration** and full Agent for new features
* **Keep requests specific** for the fastest results
* **Switch modes when needed**: If your change requires multiple files or complex logic, toggle off Fast mode
* **Review changes immediately** while context is fresh

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="How long will Fast mode be free?">
    Fast mode is free for a limited time as part of our promotional launch. The promotion can end at any time, so start using Fast mode today at no cost!
  </Accordion>

  <Accordion title="Can I use Fast mode with full Agent in the same project?">
    Absolutely! Toggle Fast mode on for quick changes and off for complex features. You can switch between them at any time based on what you need.
  </Accordion>

  <Accordion title="What if my Fast mode request is too complex?">
    Agent will let you know if a request needs full Agent mode. You can then either simplify your request or toggle off Fast mode for that task.
  </Accordion>

  <Accordion title="Does Fast mode work with all programming languages and frameworks?">
    Yes! Fast mode supports the same languages and frameworks as full Agent.
  </Accordion>
</AccordionGroup>

## Next Steps

Ready to experience faster development with Fast mode?

1. **Try Fast mode now**: Open any Replit App and enable Fast mode to make your first quick change
2. **Learn effective prompting**: Review the [vibe coding guide](/tutorials/how-to-vibe-code) for tips on working with AI
3. **Explore Agent capabilities**: Learn about [full Agent mode](/replitai/agent) for building comprehensive features
4. **Understand pricing**: Review [AI billing](/billing/ai-billing) to understand costs after the promotional period

Start building faster today with Fast mode—completely free for a limited time!
