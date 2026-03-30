# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/faq.md

# FAQ

Common questions and answers about using Tabnine CLI.

### General

<details>

<summary>What is Tabnine CLI?</summary>

Tabnine CLI is an AI-powered coding assistant that runs in your terminal. It helps you write, understand, and improve code using advanced AI models.

</details>

<details>

<summary>What can Tabnine CLI do?</summary>

* Answer questions about your code
* Review and improve code quality
* Generate new code
* Search large codebases (Remote Code Search)
* Provide best practices (Coaching Guidelines)
* Read, write, and analyze files
* Execute shell commands safely

</details>

<details>

<summary>Do I need an internet connection?</summary>

**You need access to your Tabnine services endpoint (cloud or self‑hosted)**. Public internet isn’t required if your organization runs Tabnine in an air‑gapped environment.

</details>

### Getting Started

<details>

<summary>How do I start Tabnine CLI?</summary>

Simply run:

```bash
tabnine
```

This starts interactive mode.

</details>

### Using Tabnine CLI

<details>

<summary>How do I reference files in prompts?</summary>

Use the `@` symbol:

```
> Explain what @src/index.ts does
> Review @src/utils/validator.ts
```

</details>

<details>

<summary>What commands are available?</summary>

Type `/help` to see all commands. Key ones:

* `/help` - Show help
* `/model` - Change AI model
* `/settings` - Configure
* `/clear` - Clear conversation
* `/exit` - Exit

</details>

<details>

<summary>How do I change the AI model?</summary>

```
> /model
```

Select from the available models.

</details>

<details>

<summary>Can Tabnine CLI modify my files?</summary>

Yes, but only with your explicit confirmation. It will:

* Review proposed changes: Tabnine CLI shows the proposed changes to the file(s).
* Ask for confirmation: You must explicitly approve the changes.
* Apply changes: Changes are applied only if you approve them.

</details>

<details>

<summary>How do I use Tabnine CLI in scripts?</summary>

Non-interactive mode:

```bash
# Simple output
tabnine -p "Your prompt here"

# JSON output
tabnine -p "Your prompt" --output-format json

# Pipe input
cat file.js | tabnine -p "Review this code"
```

</details>

<details>

<summary>How do I exit Tabnine CLI?</summary>

Press `Ctrl+C` or type:

```
> /exit
```

</details>

### Features

<details>

<summary>What is Remote Code Search?</summary>

Remote Code Search lets you search across large codebases using Tabnine's cloud indexing. It's fast, semantic, and works across millions of lines of code.

[**→ Learn more**](https://docs.tabnine.com/main/getting-started/context-engine)

</details>

<details>

<summary>What are Coaching Guidelines?</summary>

AI-powered coding best practices tailored to your codebase. Get security recommendations, architecture patterns, and code quality guidance.

[**→ Learn more**](https://docs.tabnine.com/main/getting-started/context-engine/admin-console/coaching-guidelines-v)

</details>

<details>

<summary>What tools are built-in?</summary>

* File operations (read, write, search)
* Shell commands
* Remote Code Search
* Coaching Guidelines
* Code analysis

[**→ See all tools**](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/built-in-tools)

</details>

### Enterprise/Corporate

<details>

<summary>Does Tabnine CLI work behind a proxy?</summary>

Yes. For Node.js 24+:

```bash
export NODE_USE_ENV_PROXY=1
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
tabnine
```

</details>

<details>

<summary>How do I use custom CA certificates?</summary>

```bash
export NODE_USE_SYSTEM_CA=1

# Or
export NODE_EXTRA_CA_CERTS=/path/to/ca-bundle.crt
tabnine
```

</details>

### Troubleshooting

<details>

<summary>Why doesn’t Tabnine CLI work with the agent?</summary>

Tabnine CLI requires **Tabnine Agents** to be enabled for your team.

If Agents aren’t enabled for your team, agent workflows and tools won’t work (even if sign-in works).

Ask your Tabnine admin to enable Agents for your team in the Admin Console, then restart Tabnine CLI.

</details>

<details>

<summary>Why is Tabnine CLI slow?</summary>

Common causes:

* Slow network connection
* Large file context
* Complex prompts

Solutions:

* Check network speed
* Be more specific in prompts
* Reduce file references
* Try a different model with `/model`

</details>

<details>

<summary>"Command not found: tabnine"</summary>

Verify Tabnine CLI is installed and in your PATH. See the [**Installation Guide**](https://docs.tabnine.com/main/getting-started/tabnine-cli/getting-started/installation) for setup instructions.

</details>

<details>

<summary>How do I enable debug mode?</summary>

```bash
DEBUG=1 tabnine
```

Or in interactive mode:

```
> /debug on
```

</details>

<details>

<summary>Why can't Tabnine CLI access my files?</summary>

* Check file permissions.
* Ensure the user running Tabnine has permission to read the files.
* Verify working directory.
* Confirm you're in the correct working directory.
* Use absolute or correct relative paths.
* Try absolute paths or adjust relative paths to point to the correct files.

</details>

### Performance

<details>

<summary>How can I make Tabnine CLI faster?</summary>

* Be specific in prompts
* Narrow prompts to reduce processing.
* Limit file context
* Reduce the number or size of referenced files.
* Choose faster models
* Select models optimized for latency via /model.
* Use local search for recent changes
* Prefer local search when working with very recent edits.
* Check network connection
* Ensure stable and fast network access.

</details>

<details>

<summary>Does Tabnine CLI cache responses?</summary>

Yes, recent queries and context are cached automatically.

</details>

<details>

<summary>How much memory does it use?</summary>

Typically 50-200 MB depending on:

* Conversation history
* Files referenced
* Model complexity

</details>

### Privacy & Security

<details>

<summary>What data does Tabnine CLI send?</summary>

Sent:

* Your prompts
* Referenced file content

Not Sent:

* Entire codebase
* Unreferenced files
* Secrets/credentials

</details>

<details>

<summary>Is my code stored on Tabnine servers?</summary>

Code in prompts may be processed and logged for service improvement. See Tabnine's privacy policy for details.

</details>

<details>

<summary>How secure is authentication?</summary>

Tabnine CLI uses secure authentication with HTTPS encryption.

</details>

### Advanced

<details>

<summary>Can I customize AI behavior?</summary>

Yes, use `TABNINE.md` in your project root:

```markdown
# Project Context

This is a TypeScript Node.js project.

## Conventions
- Use async/await
- Add JSDoc to exports
- Write tests in __tests__/
```

</details>

<details>

<summary>Can I use multiple Tabnine accounts?</summary>

Yes, by manually swapping credential files if needed.

</details>

<details>

<summary>Can I run multiple instances?</summary>

Yes, each terminal session can run its own instance.

</details>

<details>

<summary>Can I use Tabnine CLI with other tools?</summary>

Yes:

```bash
# Pipe input
cat file.js | tabnine -p "Review this"

# In scripts
result=$(tabnine -p "..." --output-format json)

# With git
git diff | tabnine -p "Summarize changes"
```

</details>

### Common Errors

<details>

<summary>"Failed to connect to Tabnine API"</summary>

1. Check internet: `ping api.tabnine.com`
2. Check proxy settings
3. Verify firewall allows port 443
4. Try debug mode: `DEBUG=1 tabnine`

</details>

<details>

<summary>"Remote Code Search not supported"</summary>

* Your account may not have access
* Contact Tabnine support

</details>

### Getting More Help

<details>

<summary>Where can I get more help?</summary>

* In-App Help: Type `/help` in Tabnine CLI
* Troubleshooting: See Common Issues
* Report Issues: Use `/bug` command

</details>

***

Didn't find your answer? Use the `/bug` command in Tabnine CLI to report issues or ask questions.
