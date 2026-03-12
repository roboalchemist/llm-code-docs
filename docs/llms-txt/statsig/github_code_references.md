# Source: https://docs.statsig.com/integrations/github_code_references.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Github Code References

<Warning>
  ### Deprecated: PAT-based Integration

  We have deprecated the Personal Access Token (PAT) based integration in favor of our new GitHub App-based integration. The new integration provides improved security and functionality, including AI-powered features like Knowledge Graph. Please migrate to the [GitHub AI Integration](/integrations/github-ai-integration) for the best experience.
</Warning>

## Overview

The Statsig Github Integration allows you to find [Feature Gate](/feature-flags/overview) and [Dynamic Config](/dynamic-config) references within your codebase on the Statsig Console. The integration leverages the Github API to access only references to the Feature Gate or Dynamic Config without storing any sensitive information.

## Configuration

Create a new Github developer token, either Classic or Fine Grained, with at least read access to the organization or repositories that you use Statsig.
This can be found in Github under **Settings** > **Developer Settings** > **Personal Access Token**.

Then, login to the Statsig Console and navigate to the Github Code References integration on the Integrations page.
This can be found in **Project Settings** > **Integrations Tab** > **Github Code References**.

The Integration should provide additional instructions on how to enable Github Code References.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/zcWYH0v3JzGIvVat/images/github_code_references/github_integration.png?fit=max&auto=format&n=zcWYH0v3JzGIvVat&q=85&s=6bcec0453598d8ac3f9eb1992a2c1e46" alt="GitHub integration configuration interface" width="738" height="1286" data-path="images/github_code_references/github_integration.png" />
</Frame>

After inputting your token and organization name the integration will verify it can access repositories and notify you if there are any problems.

Finally, navigate to the Feature Gates or Dynamic Configs pages on the Statsig Console and select a gate or dynamic config. Under the Diagnostics tab click on the View Code References link to see your code References!

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/zcWYH0v3JzGIvVat/images/github_code_references/feature_gate_view.png?fit=max&auto=format&n=zcWYH0v3JzGIvVat&q=85&s=fdfb075c27a54c3287a0461abcc68081" alt="Feature gate diagnostics tab showing code references link" width="839" height="202" data-path="images/github_code_references/feature_gate_view.png" />
</Frame>

Code References will appear based on the feature gate or dynamic config page you are on. Code References can be filtered by repository and file extension.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/zcWYH0v3JzGIvVat/images/github_code_references/code_references.png?fit=max&auto=format&n=zcWYH0v3JzGIvVat&q=85&s=bc12279c1ca980068c38445877b6edb9" alt="Code references panel listing repositories and files" width="907" height="491" data-path="images/github_code_references/code_references.png" />
</Frame>

### Github Code References Action

We also have a [Github Action](https://github.com/statsig-io/github-code-references) that can scan your repositories for gates and dynamic configs, then create a PR replacing [Stale Gates](/feature-flags/permanent-and-stale-gates).


Built with [Mintlify](https://mintlify.com).