# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/getting-started/use-cases-and-examples.md

# Use Cases and Examples

## Make any IDE Agentic with Qodo CLI tool

You can turn any IDE into an agentic development environment using the terminal-based Qodo CLI tool. Here's how:

1. **Open your IDE of choice** (e.g., Visual Studio, Eclipse).
2. **Open the integrated terminal** within the IDE.
3. **Start Qodo CLI tool** by running:

   ```bash
   qodo
   ```

   This launches the CLI in standard terminal mode.
4. For a more interactive experience, run the CLI with the UI flag:

   ```bash
   qodo --ui
   ```

   This provides a richer interface for interacting with the agent.

With these steps, your IDE becomes an agentic workspace, enabling seamless collaboration with Qodo's capabilities right from your development environment.

***

## Qodo Aware: Remote Codebase Intelligence

{% hint style="info" %}
**Note:** This feature is available for Enterprise users only.
{% endhint %}

Qodo Aware can help you better understand your company's code and answer more complex questions about your projects.

Using Retrieval-Augmented Generation (RAG), a technique that combines retrieval-based methods with generative models to enhance the quality and relevance of generated content, Qodo Aware can understand your company's codebase better, gain deeper context about your projects and answer more complicated or specific questions.

For more information on Qodo Aware, contact [Qodo support](https://docs.qodo.ai/qodo-documentation/support-and-developers-community).

***

### Leverage Qodo Merge: Review and Implement AI Suggestions from Your Terminal

{% hint style="info" %}
**Note:** This feature is available for Qodo Merge users only.
{% endhint %}

Qodo utilizes Qodo Git integration suggestions to bring AI-powered code suggestions directly to your terminal. Review, implement, and manage Qodo Merge suggestions without leaving your development environment.

<figure><img src="https://3224296714-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE9WGt1PJng9hG0nmGaiF%2Fuploads%2FgYqNUHKwAatAFewvW2tO%2Fimage.png?alt=media&#x26;token=714401fd-030a-4e19-a859-018de2ed16b4" alt=""><figcaption></figcaption></figure>

{% embed url="<https://qodo-merge-docs.qodo.ai/qodo-merge-cli/>" %}

***

## Built-in Agents

Add Qodo's ready-to-use agents to your CLI, designed to support a wide range of developer workflows out of the box:

### Increase Test Coverage: Automated Test Coverage Agent

Automated test coverage bot for GitHub PRs - analyzes changes, generates meaningful passing tests, and creates follow-up PRs.

This agent is a GitHub Workflow that invokes the [Qodo CLI tool Action](https://github.com/qodo-ai/qodo-gen-cli?tab=readme-ov-file#github-action) with a custom agent.

#### What does the Test Coverage Agent do?

* The workflow is triggered when a `qodo-cover` label is added to an open PR
* It uses the [qodo-cover prompt](https://github.com/qodo-ai/agents/blob/main/agents/qodo-cover/agent.toml) to:
  * Analyze which changed files need test coverage
  * Generate appropriate tests for uncovered code
  * Create a follow-up PR with the new tests targeting the original PR branch
* Targets a desired coverage threshold of 80%

You get high-quality test coverage with almost no manual work. Instead of spending hours writing boilerplate tests, the agent creates them for you and sends a clean PR ready to review and merge.

{% hint style="info" %}
**Note**: this agent requires the [`QODO_API_KEY`](https://docs.qodo.ai/qodo-documentation/qodo-gen-cli/getting-started/setup-and-quickstart#api-key) secret set in your repository.
{% endhint %}

{% embed url="<https://github.com/qodo-ai/agents/blob/main/agents/qodo-cover>" %}

### Documentation Agent

Release notes are often skipped or written last minute, leading to incomplete or unclear changelogs. This agent automates the process by generating release notes from your Git history.

```yaml
# .github/workflows/qodo-release-notes.yml
name: Release Notes Generator


on:
  workflow_dispatch:
    inputs:
      target_tag:
        description: "Generate notes up to (and including) this tag; blank = HEAD"
        required: false


permissions:
  contents: write
  pull-requests: write
  issues: read
  id-token: write


jobs:
  release_notes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4


      - name: Qodo release-notes agent
        uses: qodo-ai/qodo-gen-cli@v1
        with:
          prompt: qodo-release-notes
          # agentfile: "${{ github.workspace }}/agent.toml"
          key-value-pairs: |
            target_tag=${{ github.event.inputs.target_tag }}
            notes_file=RELEASE_NOTES.md
        env:
          QODO_API_KEY: ${{ secrets.QODO_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

#### What does the Documentation Agent do?

It defines a manually-dispatched bot that generates release notes for a given PR tag.

The bot analyzes all commits, PRs and issues since the last release, and create a new PR that updates the release notes file with the new release notes.

You can configure this agent in the [agent configuration](https://github.com/qodo-ai/qodo-gen-cli/blob/main/examples/agents/release.toml).

{% hint style="info" %}
**Note**: this agent requires the [`QODO_API_KEY`](https://docs.qodo.ai/qodo-documentation/qodo-gen-cli/getting-started/setup-and-quickstart#api-key) secret set in your repository.
{% endhint %}
