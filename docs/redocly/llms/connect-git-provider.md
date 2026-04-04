# Source: https://redocly.com/docs/realm/reunite/project/connect-git/connect-git-provider.md

# Connect a Git provider

Connecting a Git provider establishes a connection between your Redocly project and a Git repository hosting provider.
Git is a widely used distributed version control system that allows multiple developers to collaborate on a project by managing changes to source code and other files.
Git providers offer online Git hosting services, so teams can collaborate from around the world.
If you already have your project files stored in a repository hosted by a Git provider, you can connect either the entire repository or a folder in that repository.

Redocly integrates with popular Git providers such as GitHub and GitLab.
When you open a pull request, or commit and push to these services, Redocly is notified automatically and can be configured to perform an action, like rebuild the project for a preview or production build.
The files in your remote Git repository and Redocly are synced, so any changes saved in Redocly or your remote repository are reflected in the published project.

You can connect your Redocly project to the following Git repository hosting providers:

- [GitHub](/docs/realm/reunite/project/connect-git/github)
- [GitLab and GitLab self-managed](/docs/realm/reunite/project/connect-git/gitlab)
- [Azure DevOps](/docs/realm/reunite/project/connect-git/azure-devops)
- [Bitbucket Cloud](/docs/realm/reunite/project/connect-git/bitbucket-cloud)


Self-hosted Git providers
If you have a self-hosted instance of GitLab, or are on GitHub Enterprise you may need to allow certain IP addresses to connect to Redocly.

Allow these IP addresses to ensure that Redocly can deploy previews and production updates based on changes you and your contributors make:

**US region:**


```sh
3.211.34.228
44.206.14.241
54.156.60.142
```

**EU region:**


```sh
3.78.112.49
52.58.255.31
3.66.111.193
```

## Resources

- **[Manage self-hosted Git providers](/docs/realm/reunite/project/connect-git/manage-self-hosted)** - Set up and configure self-hosted Git repositories for enterprise environments and custom infrastructure
- **[Include remote content](/docs/realm/reunite/project/remote-content)** - Integrate content from external repositories and sources into your Reunite projects for centralized documentation
- **[Use the Editor](/docs/realm/reunite/project/use-editor)** - Explore Reunite's collaborative editing tools for creating and managing content with real-time collaboration features
- **[Projects overview](/docs/realm/reunite/project/projects)** - View feedback, deployment details, and project settings for comprehensive project management in Reunite
- **[Configuration reference](/docs/realm/config)** - Complete redocly.yaml configuration options for customizing project behavior, deployment, and integration settings