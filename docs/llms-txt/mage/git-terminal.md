# Source: https://docs.mage.ai/guides/data-sync/git-terminal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Git terminal with built-in authentication and shortcuts

> Mage Pro supports Git-based version control, making it easy to  collaborate, track changes, and manage code across environments.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="git-terminal" />

### Introduction

The Git Terminal is a browser based terminal with built in Git authentication,
directly integrated into Mage Pro. It provides standard Git functionality with
real-time collaboration features, eliminating the need to switch between tools for
version control operations. Multiple team members can work simultaneously in
the same terminal session, sharing commands and coordinating development work.

### Location

From the home page, hover over the left popout navigation menu and click
“Version control.” You will then be taken to a terminal screen directly integrated
with Git.

<Frame>
  <img alt="Git terminal navigation" src="https://raw.githubusercontent.com/mage-ai/assets/main/dev-ux/applications/version-control-nav.png" />
</Frame>

### Integration

The Git Terminal connects with your existing development workflow. Key integration points include:

* GitHub, GitLab, and other Git providers
* Maintains authentication across sessions
* Works within existing Mage Pro workflow

<Frame>
  <img alt="Mage Pro Git terminal" src="https://mage-ai.github.io/assets/pro/features/git-terminal-md.jpg" />
</Frame>

### Use Cases

Use the Git Terminal in your development environment to push changes to GitHub for source version control after making modifications to pipelines, blocks, or configurations in the Mage UI. Essential use cases include:

* Before deploying changes to save work to version control
* For regular commits to maintain code history and backup

### Authentication

Before using the Git Terminal, you must first authenticate with GitHub through the Deploy App. This one-time setup enables all Git operations within Mage Pro.

**Quick Setup:**

1. Navigate to **Deployments** → **Connect repository**
2. Complete GitHub OAuth authentication
3. Configure your repository connection

*For detailed authentication steps, see the [Version control guide](https://docs.mage.ai/guides/data-sync/version-control-guide).*

Once authenticated, the Git Terminal automatically uses your credentials for all Git operations without requiring additional setup.

### Usage

The Git Terminal supports all standard Git operations you're familiar with. Run standard Git commands such as:

```python  theme={"system"}
git status                    # Check current changes
git add .                     # Stage all changes  
git commit -m "message"       # Commit with description
git push origin main          # Push to remote repository
```

### Conclusion

The Git Terminal streamlines your development workflow by bringing version control directly into the Mage Pro environment.
With built-in authentication, real-time collaboration, and standard Git functionality, teams can maintain professional development
practices without the complexity of managing separate tools. This integrated approach enables faster development cycles while ensuring
code changes are properly tracked and shared across your team.


Built with [Mintlify](https://mintlify.com).