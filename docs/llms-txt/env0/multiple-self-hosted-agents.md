# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/multiple-self-hosted-agents.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running Multiple Self-Hosted Agents

> Run multiple self-hosted and SaaS agents in a single env zero organization with per-project assignment

With env zero, you can use both self-hosted and SaaS agents within the same organization and assign agents at the project level, allowing for flexibility and smooth transitions between agent types.

This hybrid setup lets you configure the most suitable agent type for each project, optimizing scalability, resource management, and overall workflow efficiency.

If you’re using multiple self-hosted agents in the same organization, you can configure which agent will be used for each of your Projects, to ensure that deployments are aligned with the unique needs of each Project.

A common use case for a hybrid agent setup - where some projects run on a self-hosted agent while others use the env zero Cloud Agent - is utilizing the [env zero provider](https://search.opentofu.org/provider/env0/env0/latest) to provision all env zero resources. You can configure a single project with the env zero Cloud Agent to provision all other projects and resources through the env zero provider, while the remaining projects operate on a self-hosted agent to manage actual cloud infrastructure deployments.

<Info>
  **You can also choose to keep working with the `env zero Cloud Agent`.**

  However, please note that it does not support certain version control systems (GitHub Enterprise, GitLab Enterprise and Bitbucket Server) and [secret variables for self hosted agents](/guides/admin-guide/variables/#secrets). Make sure to verify compatibility with your specific environment before selecting this option.
</Info>

Projects not assigned to deploy with a specific agent will be deployed using the Organization's default self-hosted agent.

To assign Agents to Projects, go to your Organization Settings page, and choose the Agents tab.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/self-hosted-kubernetes-agent/50263ba6d97f9c5403c869d90bcf0e7e46edc8706bbe8ed1a156852e0766d1fc-screenshot_2024-09-12_at_13.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=9724b1fef0b57c9ec9658fcf76e1b1e8" alt="Interface screenshot showing configuration options" width="1329" height="417" data-path="images/guides/admin-guide/self-hosted-kubernetes-agent/50263ba6d97f9c5403c869d90bcf0e7e46edc8706bbe8ed1a156852e0766d1fc-screenshot_2024-09-12_at_13.png" />
</Frame>

"Edit Organization Settings” permissions are necessary to assign agents to projects.

Built with [Mintlify](https://mintlify.com).
