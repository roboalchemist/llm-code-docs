# Source: https://docs.windsurf.com/windsurf/cascade/modes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.windsurf.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cascade Modes

> Cascade offers multiple distinct modes, each optimized for different types of tasks.

Cascade offers three distinct modes, each with a different set of capabilities designed for specific workflows.

| Mode               | Use case                            | Tools             |
| ------------------ | ----------------------------------- | ----------------- |
| [Code](#code-mode) | Complex features, refactoring       | All tools enabled |
| [Plan](#plan-mode) | Complex features requiring planning | All tools enabled |
| [Ask](#ask-mode)   | Learning, planning, questions       | Search tools only |

You can switch between different modes using the mode toggle below the Cascade input box, or by using the keyboard shortcut `⌘+.` (Mac) or `Ctrl+.` (Windows/Linux).

## Code Mode

**Code mode** is Windsurf's default fully agentic mode, designed for making changes to your codebase.

In Code mode, Cascade can:

* Create, edit, and delete files
* Run terminal commands
* Search and analyze your codebase
* Install dependencies
* Execute multi-step tasks autonomously

Use Code mode when you want Cascade to actively work on your project and implement changes.

<Tip>We recommend you use Code mode as your default mode for most tasks.</Tip>

## Plan Mode

**Plan mode** helps you think through complex tasks by developing a detailed implementation plan before writing any code.

In Plan mode, Cascade will:

* Explore your codebase to understand the current state
* Ask clarifying questions to ensure the plan aligns with your goals
* Provide multiple options for you to choose from with an interactive interface
* Present a detailed plan, written in an external Markdown file, with implementation steps

When Cascade is finished, you can click "Implement" on the plan file to automatically switch to Code mode and begin implementing the plan.

<Frame caption="In plan mode, Cascade often asks multiple choice questions to clarify your requirements">
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/7b7uIe0WThZtJJHO/assets/windsurf/cascade/cascade-questions.png?fit=max&auto=format&n=7b7uIe0WThZtJJHO&q=85&s=e78c8a5a8227b5f8fbba3b81ca069454" data-og-width="1196" width="1196" data-og-height="698" height="698" data-path="assets/windsurf/cascade/cascade-questions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/7b7uIe0WThZtJJHO/assets/windsurf/cascade/cascade-questions.png?w=280&fit=max&auto=format&n=7b7uIe0WThZtJJHO&q=85&s=08bccdaae726dee086d122081c527f82 280w, https://mintcdn.com/codeium/7b7uIe0WThZtJJHO/assets/windsurf/cascade/cascade-questions.png?w=560&fit=max&auto=format&n=7b7uIe0WThZtJJHO&q=85&s=efbb40cd51d9df9cfffeb0210394b445 560w, https://mintcdn.com/codeium/7b7uIe0WThZtJJHO/assets/windsurf/cascade/cascade-questions.png?w=840&fit=max&auto=format&n=7b7uIe0WThZtJJHO&q=85&s=85174b0bdfe144716188dfadd0ec364c 840w, https://mintcdn.com/codeium/7b7uIe0WThZtJJHO/assets/windsurf/cascade/cascade-questions.png?w=1100&fit=max&auto=format&n=7b7uIe0WThZtJJHO&q=85&s=9a78bc1bcac0b39a63a7949ad92d914b 1100w, https://mintcdn.com/codeium/7b7uIe0WThZtJJHO/assets/windsurf/cascade/cascade-questions.png?w=1650&fit=max&auto=format&n=7b7uIe0WThZtJJHO&q=85&s=8417e01498e8add4613e710459a85a50 1650w, https://mintcdn.com/codeium/7b7uIe0WThZtJJHO/assets/windsurf/cascade/cascade-questions.png?w=2500&fit=max&auto=format&n=7b7uIe0WThZtJJHO&q=85&s=fb7a5eee038f7f50d77cfcc19f98eff6 2500w" />
</Frame>

### Continuing from a plan

The markdown file created in plan mode can be particularly useful for continuing work across multiple sessions.

Plans are stored in your `~/.windsurf/plans` directory and are available in the [@mentions](/chat/overview#%40-mentions) menu.
By mentioning a plan file, you can continue implementation with a fresh context.

This can be particularly useful when an initial implementation went awry: just discard the original changes, tweak the plan file, and click "Implement" to attempt implementation again in a new conversation.

### Exiting plan mode

There are multiple different ways to move from planning to implementation:

* Click the "Implement" button on the plan file
* Change your mode to Code mode in the input box
* Let the agent *automatically* switch to Code mode when it detects that you're ready to implement

## Ask Mode

**Ask mode** is a read-only mode optimized for questions and exploration.

In ask mode, Cascade can search and analyze your codebase, but cannot make any changes.
