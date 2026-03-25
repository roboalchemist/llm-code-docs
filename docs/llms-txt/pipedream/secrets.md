# Source: https://pipedream.com/docs/projects/secrets.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Project Variables and Secrets

Environment variables defined at the global workspace level are accessible to all workspace members and workflows within the workspace. To restrict access to sensitive variables or secrets, define them at the project-level and [configure access controls for the project](/projects/access-controls/#managing-access).

[See here](/workflows/environment-variables/) for info on creating, managing, and using environment variables and secrets.

<Note>
  **Project variables override workspace variables**. When the same variable is defined at both the workspace and project levels (for example, `process.env.BASE_DOMAIN`), the **project** variable takes precedence.
</Note>

Built with [Mintlify](https://mintlify.com).
