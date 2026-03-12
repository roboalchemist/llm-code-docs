# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows/repository-workflows.md

# Repository Workflows

In addition to personal workflows saved locally on your machine, Qodo IDE Plugin also supports **repository-level workflows**.\
These workflows are stored in your repository so that all collaborators working on the same codebase can access and use them.

**Location**

Repository workflows are defined inside your project under the following folder in the root folder of your repository:

```
.qodo/workflows/
```

Each file in this folder represents a workflow definition and follows the same TOML format as personal workflows.

**How it works**

When you open a repository in Qodo:

* Qodo automatically detects any workflow files under `.qodo/workflows/`.
* These workflows appear in your **Workflows list**, grouped under the repository they belong to.
* You can run them the same way as your personal workflows (for example, by typing `/workflow-name`).
* When you commit and push these workflow files, they become part of the repository — allowing every contributor to use and improve them.

**Use cases**

* Maintain **shared, repo-specific workflows** (for example, workflows tailored to that codebase’s style, structure, or conventions).
* Ensure **consistency** across team members by version-controlling the same set of workflows.
* Avoid local setup or exporting — workflows are automatically available to everyone working on the repository.

**Notes**

* Repository workflows have the same structure and capabilities as personal workflows.
* To edit a repository workflow, modify the TOML file directly and commit your changes.

***
