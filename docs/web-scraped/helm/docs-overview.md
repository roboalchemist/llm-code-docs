# Source: https://helm.sh/docs/overview

Title: Helm 4 Overview | Helm

URL Source: https://helm.sh/docs/overview

Markdown Content:
Helm v4 represents a significant evolution from v3, introducing breaking changes, new architectural patterns, and enhanced functionality while maintaining backwards compatibility for charts.

For more information about the planned Helm 4 release phases, see [Path to Helm v4](https://helm.sh/blog/path-to-helm-v4/).

What's New[​](https://helm.sh/docs/overview#whats-new "Direct link to What's New")
----------------------------------------------------------------------------------

This section provides an overview of what's new in Helm 4, including breaking changes, major new features, and other improvements. For complete technical details, see the [Full Changelog](https://helm.sh/docs/changelog).

### Summary[​](https://helm.sh/docs/overview#summary "Direct link to Summary")

*   **New features**: Wasm-based plugins, kstatus watcher, OCI digest support, multi-doc values, JSON arguments
*   **Architecture changes**: Plugin system completely redesigned, package restructuring, CLI flag renaming, move to versioned packages, chart v3 support, content-based caching
*   **Modernization**: slog migration, Go 1.24 update, dependency cleanup
*   **Security**: Enhanced OCI/registry support, TLS improvements

### Breaking Changes[​](https://helm.sh/docs/overview#breaking-changes "Direct link to Breaking Changes")

#### Post-renderers implemented as plugins[​](https://helm.sh/docs/overview#post-renderers-implemented-as-plugins "Direct link to Post-renderers implemented as plugins")

Post-renderers are implemented as plugins. With this change, it is no longer possible to pass an executable directly to `helm render --post-renderer`, but a plugin name must be passed. This might require updates to any existing post-renderer workflows.

#### Registry login does not accept full URLs[​](https://helm.sh/docs/overview#registry-login-does-not-accept-full-urls "Direct link to Registry login does not accept full URLs")

The `helm registry login` command must be done with the domain name only in v4. This is so login can be scoped at different levels on a registry in the future.

### New Features[​](https://helm.sh/docs/overview#new-features "Direct link to New Features")

#### Plugin System Overhaul[​](https://helm.sh/docs/overview#plugin-system-overhaul "Direct link to Plugin System Overhaul")

Helm 4 introduces an optional WebAssembly-based runtime for enhanced security and expanded capabilities. Existing plugins continue to work, but the new runtime opens up more of Helm's core behavior for plugin customization. Helm 4 launches with three plugin types: CLI plugins, getter plugins, and post-renderer plugins, plus a system that enables new plugin types for customizing additional core functionality. See [HIP-0026 plugin system](https://github.com/helm/community/blob/main/hips/hip-0026.md) and [Helm 4 example plugins](https://github.com/scottrigby/h4-example-plugins).

tip

Existing plugins work as before. The new WebAssembly runtime is optional but recommended for enhanced security.

#### Better resource monitoring[​](https://helm.sh/docs/overview#better-resource-monitoring "Direct link to Better resource monitoring")

New kstatus integration shows detailed status of your deployments. Test with complex applications to see if it catches issues better.

#### Enhanced OCI Support[​](https://helm.sh/docs/overview#enhanced-oci-support "Direct link to Enhanced OCI Support")

Install charts by digest for better supply chain security. For example, `helm install myapp oci://registry.example.com/charts/app@sha256:abc123...`. Charts with non-matching digests are not installed.

#### Multi-Document Values[​](https://helm.sh/docs/overview#multi-document-values "Direct link to Multi-Document Values")

Split complex values across multiple YAML files. Perfect for testing different environment configs.

#### Server-Side Apply[​](https://helm.sh/docs/overview#server-side-apply "Direct link to Server-Side Apply")

Better conflict resolution when multiple tools manage the same resources. Test in environments with operators or other controllers.

#### Custom Template Functions[​](https://helm.sh/docs/overview#custom-template-functions "Direct link to Custom Template Functions")

Extend Helm's templating with your own functions through plugins. Great for organization-specific templating needs.

#### Post-Renderers as Plugins[​](https://helm.sh/docs/overview#post-renderers-as-plugins "Direct link to Post-Renderers as Plugins")

Post-renderers are implemented as plugins, providing better integration and more capabilities.

#### Stable SDK API[​](https://helm.sh/docs/overview#stable-sdk-api "Direct link to Stable SDK API")

API breaking changes are now complete. Test it, break it, give us feedback! The API also enables additional chart versions, opening possibilities for new features in the upcoming Charts v3.

#### Charts v3[​](https://helm.sh/docs/overview#charts-v3 "Direct link to Charts v3")

Coming soon. v2 charts continue to work unchanged.

### Improvements[​](https://helm.sh/docs/overview#improvements "Direct link to Improvements")

#### Performance[​](https://helm.sh/docs/overview#performance "Direct link to Performance")

Faster dependency resolution and new content-based chart caching.

#### Error Messages[​](https://helm.sh/docs/overview#error-messages "Direct link to Error Messages")

Clearer, more helpful error output.

#### Registry Authentication[​](https://helm.sh/docs/overview#registry-authentication "Direct link to Registry Authentication")

Better OAuth and token support for private registries.

#### CLI Flags renamed[​](https://helm.sh/docs/overview#cli-flags-renamed "Direct link to CLI Flags renamed")

Some common CLI flags are renamed to better clarify their operation. The existing flags remain, but emit a deprecated warning:

*   `--atomic` → `--rollback-on-failure`
*   `--force` → `--force-replace`

Update any automation that uses these renamed CLI flags.

Upgrading to Helm 4[​](https://helm.sh/docs/overview#upgrading-to-helm-4 "Direct link to Upgrading to Helm 4")
--------------------------------------------------------------------------------------------------------------

While we work hard to make Helm 4 rock-solid for everyone, Helm 4 is brand new. To that end, before upgrading, we've added some tips below for specific things to look out for when testing Helm 4 with your existing workflows. As always, we welcome all feedback about what works, what breaks, and what could be better.

### High Priority[​](https://helm.sh/docs/overview#high-priority "Direct link to High Priority")

*   Test your existing charts and releases to verify that they still work with v4.
*   Test all 3 plugin types (CLI, getter, post-renderer).
*   Try building WebAssembly plugins with the new runtime (see [example plugins](https://github.com/scottrigby/h4-example-plugins))
*   SDK users: test the now-stable API. Try to break it and share your feedback.
*   Test your CI/CD pipelines and fix any script errors from the renamed CLI flags.
*   Test your post-renderer integrations.
*   Test registry authentication and chart installation in your OCI workflows.

### Other[​](https://helm.sh/docs/overview#other "Direct link to Other")

*   Test other new features, including multi-document values, digest-based installs, and custom template functions.
*   Test the performance of Helm 4 with large, complex charts to see if it is noticeably faster for your workloads.
*   Try breaking things intentionally to see if the updated error messages are helpful.

### Feedback[​](https://helm.sh/docs/overview#feedback "Direct link to Feedback")

*   What other plugin types would you like to see added to customize Helm core functionality?
*   With the API supporting additional chart versions, what new features would you want in Charts v3?

How to Give Feedback[​](https://helm.sh/docs/overview#how-to-give-feedback "Direct link to How to Give Feedback")
-----------------------------------------------------------------------------------------------------------------

Find issues? Have suggestions? We want to hear from you before the November release:

### GitHub Issues[​](https://helm.sh/docs/overview#github-issues "Direct link to GitHub Issues")

Review the [list of open issues and feature requests](https://github.com/helm/helm/issues) in the Helm repo. Add comments on the existing items, or [create new](https://github.com/helm/helm/issues/new/choose) issues and requests.

Join [Kubernetes Slack](https://slack.kubernetes.io/) channels:

*   `#helm-dev` for development discussions
*   `#helm-users` for user support and testing feedback

### Weekly Dev Meetings[​](https://helm.sh/docs/overview#weekly-dev-meetings "Direct link to Weekly Dev Meetings")

Join live discussion with maintainers every Thursday 9:30am PT on [Zoom](https://zoom.us/j/696660622?pwd=MGsraXZ1UkVlTkJLc1B5U05KN053QT09).

For more options, see the Helm community [communication details](https://github.com/helm/community/blob/main/communication.md).
