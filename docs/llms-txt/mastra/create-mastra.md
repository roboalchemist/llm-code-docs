# Source: https://mastra.ai/reference/cli/create-mastra

# create-mastra

The `create-mastra` command **creates** a new standalone Mastra project. Use this command to scaffold a complete Mastra setup in a dedicated directory. You can run it with additional flags to customize the setup process.

## Usage

**npm**:

```bash
npx create-mastra@latest
```

**pnpm**:

```bash
pnpm dlx create-mastra@latest
```

**Yarn**:

```bash
yarn dlx create-mastra@latest
```

**Bun**:

```bash
bun x create-mastra@latest
```

`create-mastra` automatically runs in _interactive_ mode, but you can also specify your project name and template with command line arguments.

**npm**:

```bash
npx create-mastra@latest my-mastra-project -- --template coding-agent
```

**pnpm**:

```bash
pnpm dlx create-mastra@latest my-mastra-project -- --template coding-agent
```

**Yarn**:

```bash
yarn dlx create-mastra@latest my-mastra-project -- --template coding-agent
```

**Bun**:

```bash
bun x create-mastra@latest my-mastra-project -- --template coding-agent
```

Check out the [full list](https://mastra.ai/api/templates.json) of templates and use the `slug` as input to the `--template` CLI flag.

You can also use any GitHub repo as a template (it has to be a valid Mastra project):

```bash
npx create-mastra@latest my-mastra-project -- --template mastra-ai/template-coding-agent
```

You can install Mastra skills for specific agents during project creation:

**npm**:

```bash
npx create-mastra@latest my-project -- --default --skills claude-code,cursor
```

**pnpm**:

```bash
pnpm dlx create-mastra@latest my-project -- --default --skills claude-code,cursor
```

**Yarn**:

```bash
yarn dlx create-mastra@latest my-project -- --default --skills claude-code,cursor
```

**Bun**:

```bash
bun x create-mastra@latest my-project -- --default --skills claude-code,cursor
```

## CLI flags

Instead of an interactive prompt you can also define these CLI flags.

**--version** (`boolean`): Output the version number

**--project-name** (`string`): Project name that will be used in package.json and as the project directory name

**--default** (`boolean`): Quick start with defaults (src, OpenAI, no examples)

**--components** (`string`): Comma-separated list of components (agents, tools, workflows, scorers)

**--llm** (`string`): Default model provider (openai, anthropic, groq, google, or cerebras)

**--llm-api-key** (`string`): API key for the model provider

**--example** (`boolean`): Include example code

**--no-example** (`boolean`): Do not include example code

**--template** (`string`): Create project from a template (use template name, public GitHub URL, or leave blank to select from list)

**--timeout** (`number`): Configurable timeout for package installation, defaults to 60000 ms

**--dir** (`string`): Target directory for Mastra source code (default: src/)

**--mcp** (`string`): MCP Server for code editor (cursor, cursor-global, windsurf, vscode)

**--skills** (`string`): Comma-separated list of agents to install Mastra skills for (e.g., claude-code,cursor,windsurf)

**--help** (`boolean`): Display help for command

## Telemetry

By default, Mastra collects anonymous information about your project like your OS, Mastra version or Node.js version. You can read the [source code](https://github.com/mastra-ai/mastra/blob/main/packages/cli/src/analytics/index.ts) to check what's collected.

You can opt out of the CLI analytics by setting an environment variable:

```bash
MASTRA_TELEMETRY_DISABLED=1
```

You can also set this while using other `mastra` commands:

```bash
MASTRA_TELEMETRY_DISABLED=1 npx create-mastra@latest
```