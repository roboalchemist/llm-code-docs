# Source: https://docs.xano.com/xanoscript/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Intro to XanoScript

> Introduction to XanoScript

## What is XanoScript?

At Xano, we set out to create a language that combines the structure of JSON/XML/YAML with the flexibility of TypeScript—without the overhead and inconsistency that often slows teams down.

## I thought Xano was No-Code / Low-Code?

You **never** have to write XanoScript to use Xano, but it’s there when you need it.

Xano is a no-code/low-code platform at its core, and our visual builder is designed to make backend development accessible to everyone. However, as teams grow, and developers are building in new ways, we recognized the need for a more structured, code-first approach that still integrates seamlessly and maintains parity with our visual tools.

Read more about why we built XanoScript in [this blog post](https://www.xano.com/news/xanoscript-for-building-backends/).

## Why XanoScript Exists

The result is XanoScript: a markup language that lets you configure Xano programmatically while still supporting visual development. It gives you code-level control of your backend in a way that’s structured, collaborative, and AI-friendly.

## Why XanoScript Matters

<CardGroup cols={1}>
  <Card title="Flexible Workflow" icon="shuffle" horizontal>
    Start in Xano’s visual editor, continue in XanoScript, or switch back and forth anytime. Use VS Code, Cursor, or your preferred AI model.
  </Card>

  <Card title="Unified Configuration" icon="layer-group" horizontal>
    Define everything—database, APIs, business logic, background tasks, deployment—in a single consistent language.
  </Card>

  <Card title="Built for Collaboration" icon="users" horizontal>
    Developers write code, while product managers and non-technical teammates work visually in Xano. Both stay aligned in real time.
  </Card>

  <Card title="AI-Powered Development" icon="bolt" horizontal>
    Unlike one-off AI generators, XanoScript lets you generate, deploy, and iterate continuously—visually or with code—without starting over.
  </Card>

  <Card title="Accessible Yet Powerful" icon="code" horizontal>
    If you understand JSON, YAML, or JavaScript—or already use Xano—you’re ready to build with XanoScript.
  </Card>
</CardGroup>

## What You Can Do with XanoScript

<CardGroup cols={2}>
  <Card title="AI-Generated Code" icon="robot">
    Generate XanoScript with your favorite AI models and import it directly into Xano.
  </Card>

  <Card title="Instant Backend Deployment" icon="rocket">
    Spin up a backend using AI, deploy instantly, and iterate visually as you go.
  </Card>

  <Card title="Seamless Visual & Code Workflow" icon="hammer-brush">
    Start visually in Xano, expand into code, and switch between both at any time.
  </Card>

  <Card title="Universal Integration" icon="cubes">
    Use XanoScript anywhere in Xano—from database design to function stacks.
  </Card>
</CardGroup>

## Getting Started with XanoScript

### Explore XanoScript in your workspaces

Everything you've already built in Xano has XanoScript already written.

* Click the ⋮ icon in the top-right corner of your screen, and choose Settings.
* Click XanoScript in the menu that opens.

### Build with XanoScript

When using the visual builder in Xano, you're already writing XanoScript without any extra effort. If you prefer to work code-first, you can develop in XanoScript inside of Xano or an IDE of your choice. Any time you're creating something new in Xano, you can select the XanoScript option.

<CardGroup cols={1}>
  <Card title="Look for the Use XanoScript option" icon="code">
    This option will be available when creating most new objects in Xano, such as APIs, Custom Functions, Background Tasks, and more.<br />

        <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/introduction-20251002-122904.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=cd407eea6dc63989ad9fafb96eb93eba" alt="introduction-20251002-122904" width="964" height="1011" data-path="images/introduction-20251002-122904.png" />
  </Card>

  <Card title="Look for the XanoScript option" icon="code">
    In some object types, such as AI Agents that open with a settings panel immediately, you'll see a XanoScript option at the top of the panel.<br />

        <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/introduction-20251002-123221.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=6015e568b243e6f0fec3675d32b174f5" alt="introduction-20251002-123221" width="761" height="579" data-path="images/introduction-20251002-123221.png" />
  </Card>

  <Card title="Use the VS Code Extension" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/vscode.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=c9ca342a4c7cc10adcf78c89f822c596" width="100" height="100" data-path="images/icons/vscode.svg">
    You can also use the VS Code extension to write XanoScript in an IDE of your choice. You should be able to use any IDE that supports VS Code extensions, such as Cursor or Windsurf, as well as VS Code itself.

    **Get the VS Code extension [here](https://marketplace.visualstudio.com/items?itemName=xano.xanoscript)**
  </Card>

  <a id="writexs" />

  <Card title="Learn how XanoScript is written" icon="code">
    You can learn how each object is written in XanoScript by reviewing the individual pages for each object type. Select one below to get started.
    <Callout icon="table" color="#6B99FA">**XanoScript in the Database**<br /><br /><Icon icon="link" iconType="light" /> [Database Tables](/xanoscript/db)<br /><Icon icon="link" iconType="light" /> [Database Triggers](/xanoscript/triggers)<br /><Icon icon="link" iconType="light" /> [Database Views](/xanoscript/db#section-3%3A-views)</Callout>

    <Callout icon="webhook" color="#6B99FA">**XanoScript for Logic / Workflows**<br /><br /><Icon icon="link" iconType="light" /> [APIs](/xanoscript/api)<br /><Icon icon="link" iconType="light" /> [Custom Functions](/xanoscript/custom-functions)<br /><Icon icon="link" iconType="light" /> [Addons](/xanoscript/addons)<br /><Icon icon="link" iconType="light" /> [Background Tasks](/xanoscript/tasks)<br /><Icon icon="link" iconType="light" /> [Triggers](/xanoscript/triggers)<br /><Icon icon="link" iconType="light" /> [Middleware](/xanoscript/middleware)<br /><Icon icon="link" iconType="light" /> [Workflow and Unit Tests](/xanoscript/tests)</Callout>

    <Callout icon="robot" color="#6B99FA">**XanoScript for AI**<br /><br /><Icon icon="link" iconType="light" /> [AI Agents](/xanoscript/agents)<br /><Icon icon="link" iconType="light" /> [MCP Servers](/xanoscript/mcp-servers)<br /><Icon icon="link" iconType="light" /> [Tools for Agents and MCP Servers](/xanoscript/ai-tools)</Callout>

    <Callout icon="gear" color="#6B99FA">**Other**<br /><br /><Icon icon="link" iconType="light" /> [Workspace Settings](/xanoscript/workspace-settings)<br /><Icon icon="link" iconType="light" /> [MCP Servers](/xanoscript/mcp-servers)<br /><Icon icon="link" iconType="light" /> [Tools for Agents and MCP Servers](/xanoscript/ai-tools)</Callout>
    You can also learn more about how each of our functions and filters is written using XanoScript in our function and filter references.

    <CardGroup cols={3}>
      <Card title="Function Reference" href="/xanoscript/function-reference" />

      <Card title="Filter Reference" href="/xanoscript/filter-reference" />

      <Card title="Data Types" href="/xanoscript/field-type-reference" />
    </CardGroup>
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).