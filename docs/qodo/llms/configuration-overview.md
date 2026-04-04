# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview.md

# Customize the Code Review Experience

Customize the code review experience so it matches your team’s standards, workflows, and tolerance for noise.

You don’t need to configure everything to get value from Qodo. Most teams start with the defaults and selectively customize only what they need.

Configuration allows you to:

* Filter out noise from irrelevant pull requests
* Guide Qodo’s feedback to align with your team’s practices
* Maintain consistent review behavior across projects and repositories
* Improve the quality, relevance, and focus of review feedback

### What can be configured?

Qodo configuration allows you to control several aspects of the review experience:

#### How reviews run

* Which review commands are available
* Whether reviews run manually or automatically
* When reviews run (for example, on draft PRs, published PRs and additional commits)

#### How feedback appears

* Where comments appear (PR conversation summary or inline comments on file changes)
* Severity thresholds for inline feedback
* Control the number of surfaced findings

Qodo feedback is embedded directly within the Git provider experience and integrates with the provider’s native comment system. Available display options may vary depending on the provider’s capabilities.

#### What Qodo reviews

* Which repositories, branches, folders, or files are included
* Which pull requests should be ignored
* Which tickets or labels should be excluded

#### How Qodo behaves

* Custom instructions for review output
* Persistent review comments
* Feature-level behavior (for example, suggestion tracking or CI feedback)

### Supported configuration locations

Qodo settings can be defined at multiple levels, each corresponding to a different location. These settings can be configured using a `.pr_agent.toml` file or through the Qodo Portal.

Supported locations:

* **Repository Wiki** (`.pr_agent.toml`)
* **Repository Root** (`.pr_agent.toml`)
* **Organization settings repository** (`pr-agent-settings`)
* **Project settings repository** (`pr-agent-settings`)
* **Qodo portal** ([Configuration](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/portal-configuration) page)

{% hint style="success" %}
**Enterprise** customers can configure environment-level settings.
{% endhint %}

#### Configuration precedence

When settings are defined in more than one location, Qodo applies them in the following order (highest precedence first):

1. Repository Wiki (Wiki availability depends on the Git provider, as not all providers support a wiki feature.
2. Repository Root
3. Organization/ Project settings repository (`pr-agent-settings`)
4. Qodo Portal

This hierarchy enables organizations to define shared defaults while still allowing repository-specific overrides when needed.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FhAkPzO418NDTbeZZmeyg%2FQodo_image.png?alt=media&#x26;token=9fa00623-d779-4fe1-873f-2297a0e08790" alt="" width="563"><figcaption></figcaption></figure>

#### FAQ

<details>

<summary>Which settings take precedence if configuration exists in multiple locations?</summary>

Repository-level settings override both project-level and organization-level defaults.

</details>

<details>

<summary>What happens if both project-level and organization-level settings exist?</summary>

Project-level settings take precedence over organization-level settings.

</details>

<details>

<summary>How does Qodo locate the <code>pr-agent-settings</code> repository in GitLab subgroup structures?</summary>

For repositories nested within multiple subgroups, Qodo searches only **one level up** for a `pr-agent-settings` repository.

</details>

<details>

<summary>Do settings configured in the Qodo portal override repository configuration?</summary>

No. Settings defined in the Qodo portal have the lowest precedence and are overridden by repository, project, or organization-level configuration.

</details>

### Supported configuration methods

You can select the configuration method that best fits your workflow:

* **Wiki configuration** (`.pr_agent.toml`)\
  Does not require committing changes to the codebase. Changes take effect immediately.
* **Repository-level configuration** (`.pr_agent.toml`)\
  Applies only to a specific repository. Requires committing a `.pr_agent.toml` file to the default branch.
* **Organization or project-level configuration** (`pr-agent-settings`)\
  Defines defaults that apply across multiple repositories.
* **Portal configuration** (Qodo portal)\
  Managed through the Qodo Portal interface. These settings apply only when no configuration is defined in the repository wiki, repository root, or organization settings repository.

### Get started

Get detailed instructions on the configuration methods that suits your workflow:

* [**Configure Using `.pr_agent.toml`**](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/configuration-file)
* [**Configure Using the Qodo Portal**](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/portal-configuration)
