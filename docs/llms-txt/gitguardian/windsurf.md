# Source: https://docs.gitguardian.com/ggshield-docs/integrations/ide-integrations/windsurf.md

# Windsurf Extension

> Guide to installing and configuring the GitGuardian Windsurf extension for real-time secret detection in the Windsurf IDE.

The GitGuardian Windsurf extension enhances code security by detecting and preventing the inclusion of sensitive information, such as API keys and credentials, directly within your development environment. This tool integrates seamlessly into Windsurf, providing real-time feedback to developers and promoting secure coding practices.

The extension leverages the bundled GitGuardian CLI (`ggshield`) to scan your code for over 500 types of secrets as you write or modify it, ensuring immediate awareness and action when potential security issues are detected.

![Windsurf GitGuardian extension detecting a secret showing hover details](/img/ggshield/ide-integrations/windsurf.png)

*The GitGuardian extension detecting AWS keys in Windsurf, showing detailed information about the secret when hovering.*

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6RGoHXxwOLc?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; fullscreen; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

## Key Features

- **Real-Time Secret Detection**: Automatically scans your code as you type, highlighting secrets instantly with clear visual indicators.
- **Guided Remediation**: Provides actionable recommendations to fix detected secrets directly within Windsurf.
- **Developer-Friendly Integration**: Simple one-click installation with built-in CLI and automatic scanning on save.
- **False Positive Management**: Easily mark false positives through `.gitguardian.yaml` configuration.

## Installation

From the extension marketplace:

1. Open Windsurf
2. Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`)
3. Search for "GitGuardian"
4. Click "Install" on the "GitGuardian Secret Security" extension
5. Restart Windsurf if prompted

## Configuration

### Authentication

After installation, you'll need to authenticate with GitGuardian:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Type "GitGuardian: Authenticate" and select it
3. Follow the authentication flow to connect your GitGuardian account

### Settings

The extension can be configured through Windsurf settings:

1. Go to Windsurf â Settings â Extensions (or `Ctrl+,` / `Cmd+,`)
2. Search for "GitGuardian"
3. Configure the available options:

#### For SaaS Users
- **API URL**: Uses GitGuardian's default API endpoint
- **Authentication**: Use the built-in authentication flow

#### For Self-Hosted Users
- **API URL**: Enter your custom GitGuardian instance URL
- **API Key**: Enter your [Personal Access Token](../../../api-docs/personal-access-tokens) from your self-hosted instance

To configure for self-hosted instances:

```json
{
  "gitguardian.apiUrl": "https://your-gitguardian-instance.com",
  "gitguardian.apiKey": "your-personal-access-token"
}
```

## Usage and Results

The extension automatically scans files on save and displays results in three ways:
- Highlights secrets directly in your code
- Shows warning icons in the status bar
- Lists issues in the Problems panel (`Ctrl+Shift+M` or `Cmd+Shift+M`)

To ignore false positives, add paths to `.gitguardian.yaml`:
```yaml
paths-ignore:
  - "tests/samples/*"
  - "docs/examples.md"

version: 2
```

:::info
Customize the remediation message and add your own to offer developers precise guidance for resolving their code issues and continuing their work.

**Read more here - GitGuardian CLI custom remediation message**
:::

## Troubleshooting

Common solutions:
- Verify authentication and internet connection
- For self-hosted instances, check API key and URL
- Restart your IDE if issues persist
- Exclude large directories in `.gitguardian.yaml` for better performance

Need help? Check our [documentation](../../getting-started.md), [GitHub repository](https://github.com/GitGuardian/gitguardian-vscode), or contact [support](mailto:support@gitguardian.com).
