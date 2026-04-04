# Source: https://docs.socket.dev/docs/socket-mcp-for-claude-desktop.md

# Socket MCP for Claude Desktop

Socket MCP is available in Claude Desktop's official Extensions directory:

<Image align="center" width="75% " src="https://files.readme.io/92fcecc57b2e8eebcf5569c217d81a32c474358179b9f1d2d324766508965120-image.png" />

Step-by-step instructions:

1. **Open Claude Desktop:** Navigate to Settings > Extensions > Browse extensions to access the Extensions directory
2. **Find Socket MCP:** Look for "Socket MCP" in the list of available Desktop Extensions
3. **Click "Install:"** Claude will display the extension's capabilities/tools and request confirmation
4. **Enter Socket API key:** You need a Socket API key to use Socket MCP. You can create one following the instructions [here](https://github.com/SocketDev/socket-mcp#getting-an-api-key).
5. **Start using Socket MCP:** Example: "Check the security of react"

## Using Socket MCP

#### Understanding Security Scores

Socket provides scores from 0 to 100 for each security dimension. While there are no official thresholds, scores between 90 and 100 indicate a strong security profile. Scores from 70 to 80 suggest minor concerns but are generally acceptable. When scores fall between 50 and 60, you should review the package carefully before using it. Anything below 50 warrants looking for alternatives. Your acceptable thresholds may vary based on project requirements.

#### Practical Examples

**Checking a new dependency:**

<Image align="center" width="75% " src="https://files.readme.io/bb86168ec6307d83e0f7cc78e9e1cd05404944ac629f9be41a5a7e9201eeab95-image.png" />

**Evaluating packages with issues:**

<Image align="center" width="75% " src="https://files.readme.io/e65dcfacba265cbf494dd8238dc45e37cce34677acd8c9de11ace9946f09c74f-image.png" />

## Customizing Your Workflow

#### Setting Claude Rules

Add rules to Claude (Settings > Profile > personal preferences) for automatic security checks:

```
# Security Checks

When I mention adding a dependency or generating code that has new dependencies:
1. Check their security score with Socket MCP
2. Alert me if any score is below 0.8
3. Suggest alternatives for low-scoring packages

When reviewing code:
- Scan imports and required packages
- Flag packages with vulnerability scores below 0.9
```