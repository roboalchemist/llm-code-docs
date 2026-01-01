Read the F****** Manual

Topic: $ARGUMENTS

Use the `llm-code-docs-agent` to find and read documentation for this topic.

## Steps

1. **Determine the topic**: If no topic specified, infer from the current conversation context or the project folder (check package.json, pyproject.toml, go.mod, etc.).

2. **Search for existing docs**:
   ```bash
   ls ~/github/llm-code-docs/docs/llms-txt/ | grep -i <topic>
   grep -i <topic> ~/github/llm-code-docs/index.yaml
   ```

3. **If docs exist**: Read them from `~/github/llm-code-docs/docs/`

4. **If docs don't exist**:
   - Pull the latest version: `cd ~/github/llm-code-docs && git pull`
   - Search again
   - If still not found, offer to add docs using `/WTFM <topic>` (don't do it automatically!)