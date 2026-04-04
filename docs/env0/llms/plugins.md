# Source: https://docs.envzero.com/guides/integrations/plugins.md

# Source: https://docs.envzero.com/changelogs/2022/12/plugins.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ➕ Plugins

> With env zero, you can keep your development organization's best practices for managing and executing Infrastructure as Code. Today we are happy to announce that we developed Plugins to make software development lifecycle tools and processes easier to integrate.

With env zero, you can keep your development organization's best practices for managing and executing Infrastructure as Code. Today we are happy to announce that we developed Plugins to make software development lifecycle tools and processes easier to integrate.

## ✨ Usage ✨

> 📘 This is an opt-in feature
>
> In order to use a plugin in your env0.yaml file, you need to set its version to 2. If you wish to change an existing env0.yaml file to version 2, please follow the [migration guide](/guides/admin-guide/custom-flows/version-2-schema)

Using env zero plugins is done via your env0.yaml file. This is an example of how to use the [OPA plugin](https://github.com/env0/env0-opa-plugin):

```yaml  theme={null}
version: 2
deploy:
  steps:
    terraformPlan:
      after:
        - name: OPA
          use: https://github.com/env0/env0-opa-plugin
          input:
            path: bundle-file-path
            flags: --fail --format=raw
            query: data.example.violation[x]
```

[Check out env0's supported plugins and integrations](/guides/integrations/plugins).

## ✨ Custom Plugins ✨

You can also quickly create an env0 plugin of your own. To get started:

1. Open a new public Git repository.
2. Create an *env0.plugin.yaml* file that describes and configures your plugin's execution runtime and required inputs.
3. Use it in your *env0.yaml* file.

[Read more about how to create a custom env0 plugin file](/guides/integrations/plugins).

> 🚧 Self-Hosted Agents
>
> If you'd like to enable this feature on your self-hosted agent, please update to the latest version.

## Suggested Blog Content

[What is tfsec: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-tfsec)

[What is Checkov: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-checkov)

[What is Terrascan: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tools-what-is-terrascan)

[Best IaC Scanning Tools](https://www.env0.com/blog/best-iac-scan-tool)

Built with [Mintlify](https://mintlify.com).
