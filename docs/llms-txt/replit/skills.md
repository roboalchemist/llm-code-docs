# Source: https://docs.replit.com/replitai/skills.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Skills

> Extend Agent with reusable capabilities that automate tasks and add specialized functionality to your projects.

Teach Agent how you want to build. Skills let you share your preferences, patterns, and expertise with Agent—whether you're starting a new project or building on existing work.

<Frame>
  <img src="https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=40cfad1b65f6ac824942013881bbfcc0" alt="Agent Skills pane showing installed skills" data-og-width="3306" width="3306" data-og-height="1994" height="1994" data-path="images/replitai/agent-skills-pane.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=280&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=3f03b53dc97049d3222f927df1b4a362 280w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=560&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=c2457d30caf0c0e6e544bb285d3c670f 560w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=840&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=8002eab13df013737024d05daf914cae 840w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=1100&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=9390ca4678ad6de2df53496783d19915 1100w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=1650&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=38d1481e11e75c0b4438e51a3d2bc06b 1650w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=2500&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=b5b27c283645c9e9e84dc508bdac973c 2500w" />
</Frame>

## What are skills

Skills teach Agent how you work. As you build together, you create useful context about your project, but that context normally disappears when the chat ends. Skills preserve what you've learned so Agent can apply it consistently. Tasks that were previously inconsistent become more reliable, producing better results each time.

For example, a design system skill ensures Agent uses your exact colors and spacing rules. A bug fix skill captures solutions so Agent remembers them for next time.

## When to use skills

You can create skills for anything, from how you structure your code to how you write your docs. Here are some examples to get you started:

| Use Case                        | Example Scenario                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Design systems**              | Create a skill for your design system so Agent uses consistent colors, spacing, and components                        |
| **New frameworks**              | Add a skill for Remotion when building video features or other specialized libraries                                  |
| **Media creation**              | Teach Agent photography principles for AI-generated images                                                            |
| **Learning how your app works** | After fixing a complex bug together, create a skill that captures what you both learned about your app's architecture |

## Adding skills to your project

Skills become part of your project once they're added to the `/.agent/skills` directory. You can create skills naturally through conversation with Agent, install pre-built skills from the community, or write custom skills for specialized needs.

### Create with Agent

The most natural way to create skills is through conversation. After solving a problem together, ask Agent to capture what it learned. The skill writes itself from shared context.

```
Create a skill for my design system using these color palettes and spacing rules
```

You can also ask Agent to research and create skills for new domains:

```
Research best practices for video generation with Remotion and create a skill
```

### Upload and manage custom skills

You can upload and manage skills directly through the Workspace. Open the Skills pane to view installed skills, upload custom skill files, or remove skills you no longer need.

<Frame>
  <img src="https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=40cfad1b65f6ac824942013881bbfcc0" alt="Agent Skills pane showing installed skills" data-og-width="3306" width="3306" data-og-height="1994" height="1994" data-path="images/replitai/agent-skills-pane.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=280&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=3f03b53dc97049d3222f927df1b4a362 280w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=560&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=c2457d30caf0c0e6e544bb285d3c670f 560w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=840&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=8002eab13df013737024d05daf914cae 840w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=1100&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=9390ca4678ad6de2df53496783d19915 1100w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=1650&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=38d1481e11e75c0b4438e51a3d2bc06b 1650w, https://mintcdn.com/replit/7Pe5VcYQ70BUgsrr/images/replitai/agent-skills-pane.png?w=2500&fit=max&auto=format&n=7Pe5VcYQ70BUgsrr&q=85&s=b5b27c283645c9e9e84dc508bdac973c 2500w" />
</Frame>

For advanced use cases, write your own skills following the [Agent Skills specification](https://agentskills.io/specification). This gives you complete control over Agent's behavior for specific scenarios.

### Install from the skills directory

The [Agent Skills directory](https://skills.sh) offers community-contributed skills you can install directly. Replit supports installation via the [npx skills CLI](https://github.com/vercel-labs/skills):

```bash  theme={null}
npx skills <skill> -a replit
```

This installs the skill into your project's `/.agent/skills` directory.

<Warning>
  Skills contain arbitrary content and code. Always review the source before
  installing a skill from external sources.
</Warning>

## Technical reference

Skills are stored in your project's `/.agent/skills` directory. Each skill follows the [Agent Skills specification](https://agentskills.io/specification), which defines the structure and format for skill files.

Agent reads all skills in this directory and considers them when working on tasks. Skills persist in your project, so they remain available across Agent sessions and can be committed to version control for team sharing.

Skills can be scoped to different levels:

* **Project-level**: Specific to one codebase, versioned with your code in `/.agent/skills`
* **User-level**: Your personal toolkit that follows you across projects
* **Enterprise** (coming soon): Company-wide standards and shared knowledge

<Note>
  Skills work best when they capture specific, repeatable patterns rather than
  general guidance. Focus on concrete workflows, established conventions, and
  proven solutions from your project.
</Note>

## Working with other AI coding tools

<Accordion title="Import skills from other AI coding tools">
  If you work across multiple AI coding tools, [rulesync](https://github.com/dyoshikawa/rulesync) has Replit support and helps you maintain consistent configurations.

  You can import skills from other AI coding assistants:

  ```bash  theme={null}
  npx rulesync init
  npx rulesync import --targets claudecode --features skills
  npx rulesync generate --targets replit --features skills
  ```

  This allows you to maintain a single set of skills that work across different development environments.
</Accordion>

## Next steps

Skills complement Agent's core capabilities by adding project-specific knowledge:

* Learn more about [Agent](/replitai/agent) and how it builds applications
* Explore other [AI-powered features](/category/replit-ai) available in Replit
* Review the [Agent Skills specification](https://agentskills.io/specification) to understand skill structure
* For examples of custom skills, see [Anthropic's skills repository](https://github.com/anthropics/skills)
* Browse community skills at [skills.sh](https://skills.sh)
