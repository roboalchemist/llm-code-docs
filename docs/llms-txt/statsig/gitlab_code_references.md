# Source: https://docs.statsig.com/integrations/gitlab_code_references.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitLab Code References

## Overview

The Statsig GitLab Integration allows you to find [Feature Gate](/feature-flags/overview) and [Dynamic Config](/dynamic-config) references within your codebase on the Statsig Console. The integration leverages the GitLab API to access only references to the Feature Gate or Dynamic Config without storing any sensitive information.

## Configuration

Create a new GitLab access token, either [project](https://docs.gitlab.com/user/project/settings/project_access_tokens/) or [personal](https://docs.gitlab.com/user/profile/personal_access_tokens/), with the `read_api` scope.

Then, login to the Statsig Console and navigate to the Github Code References integration on the Integrations page.
This can be found in **Project Settings** > **Integrations Tab** > **GitLab Code References**.

The Integration should provide additional instructions on how to enable GitLab Code References.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/zcWYH0v3JzGIvVat/images/gitlab_code_references/gitlab_integration.png?fit=max&auto=format&n=zcWYH0v3JzGIvVat&q=85&s=19309bb877ef693785f34e1cba0f4639" alt="GitLab integration configuration interface" width="806" height="1044" data-path="images/gitlab_code_references/gitlab_integration.png" />
</Frame>

After inputting your token and organization name the integration will verify it can access repositories and notify you if there are any problems.

Finally, navigate to the Feature Gates or Dynamic Configs pages on the Statsig Console and select a gate or dynamic config. Under the Diagnostics tab click on the View Code References link to see your code References!

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/zcWYH0v3JzGIvVat/images/gitlab_code_references/feature_gate_view.png?fit=max&auto=format&n=zcWYH0v3JzGIvVat&q=85&s=0b8117e7f5bc40c4304659327235dbc1" alt="Feature gate diagnostics page with GitLab code references link" width="1318" height="179" data-path="images/gitlab_code_references/feature_gate_view.png" />
</Frame>

Code References will appear based on the feature gate or dynamic config page you are on. Code References can be filtered by repository and file extension.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/zcWYH0v3JzGIvVat/images/gitlab_code_references/code_references.png?fit=max&auto=format&n=zcWYH0v3JzGIvVat&q=85&s=738510841202772bf731cefb45f2ebac" alt="GitLab code references table listing files and repositories" width="1005" height="1083" data-path="images/gitlab_code_references/code_references.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).