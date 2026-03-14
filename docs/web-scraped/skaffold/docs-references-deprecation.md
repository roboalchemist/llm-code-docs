# Source: https://skaffold.dev/docs/references/deprecation/

Title: Deprecation Policy

URL Source: https://skaffold.dev/docs/references/deprecation/

Markdown Content:
This document sets out the deprecation policy for Skaffold, and outlines how the Skaffold project will approach the introduction of breaking changes over time.

Deprecation policy applies only to Stable Builds. Bleeding Edge builds may have less stable implementations.

Deprecations to a flag or CLI command require the following notification periods, depending on the release track:

| Release Track | Deprecation Period |
| --- | --- |
| Alpha (experimental) | 0 releases |
| Beta (pre-release) | 3 months or 1 release (whichever is longer) |
| GA (generally available) | 6 months or 1 release (whichever is longer) |

**Breaking changes** A breaking change is when the primary functionality of a feature changes in a way that the user has to make changes to their workflows/configuration.

*   **Breaking config change**: In case of Skaffold’s pipeline config (skaffold.yaml) a breaking change between an old and new version occurs when the skaffold binary cannot parse the input yaml with auto-upgrade. This can happen when the new version removes a feature or when the new version introduces a mandatory field with no default value
*   **Breaking functional change**: functional changes that force user workflow changes even when the config is the same or upgradeable.

How do we deprecate things?
---------------------------

A “deprecation event” would coincide with a release.

1.   We document the deprecation in the following places if applicable

    1.   deprecation policy - this document
    2.   [Document on this site](https://skaffold.dev/docs/) changes in relevant sections
    3.   [Release notes](https://github.com/GoogleContainerTools/skaffold/blob/main/CHANGELOG.md)
    4.   [Command help](https://skaffold.dev/docs/references/cli/)
    5.   Log messages
    6.   [skaffold yaml reference](https://skaffold.dev/docs/references/yaml/)

2.   if applicable, [inspired by the Kubernetes policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecating-a-flag-or-cli):

> Rule #6: Deprecated CLI elements must emit warnings (optionally disable) when used.

Current maturity of skaffold
----------------------------

Skaffold and its features are considered GA unless specified (in this document, CLI reference, config YAML reference or in docs in skaffold.dev).

 Skaffold is constantly evolving with the tools space, we want to be able to experiment and sometimes change things. In order to be transparent about the maturity of feature areas and things that might change we offer the feature level maturity matrix that we keep up to date.

Skaffold.yaml (pipeline config)
-------------------------------

You can safely depend on the skaffold config with the assumption that skaffold will auto-upgrade to the latest version:

*   Removal and other non-upgradeable changes are subject to the deprecation policy for all (even new) features under the config.
*   Auto-upgradeable changes are not considered breaking changes.

Skaffold features
-----------------

We are committed to design for auto-upgradeable changes in the config. However the **behavior** of individual component might suffer breaking changes depending on maturity.

The following is the maturity of the larger feature areas:

| area | maturity | description |
| --- | --- | --- |
| [Skaffold API](https://skaffold.dev/docs/design/api) | beta | Control API, Event API and State API |
| [Build](https://skaffold.dev/docs/builders/) | GA | Build images based on multiple build tools in a configurable way |
| [Cleanup](https://skaffold.dev/docs/cleanup) | GA | `skaffold delete` removes everything deployed `skaffold run` from the cluster, and prunes locally |
| [Completion](https://skaffold.dev/docs/references/deprecation/) | GA | generate completion scripts for bash, zsh |
| [Debug](https://skaffold.dev/docs/workflows/debug) | GA | Language-aware reconfiguration of containers on the fly to become debuggable |
| [Default-repo](https://skaffold.dev/docs/environment/image-registries/) | GA | specify a default image repository & rewrite image names to default repo |
| [Deploy](https://skaffold.dev/docs/deployers) | beta | Deploy a set of deployables as your applications and replace the image name with the built images |
| [Dev](https://skaffold.dev/docs/workflows/dev) | GA | Continuous development |
| [skaffold fix](https://skaffold.dev/docs/references/deprecation/) | beta | Upgrade an older skaffold config to the current version |
| [Generate tekton pipelines](https://skaffold.dev/docs/references/deprecation/) | alpha | User can generate a starter tekton pipeline using skaffold |
| [Global config](https://skaffold.dev/docs/design/global-config/) | GA | store user preferences in a separate preferences file |
| [Lifecycle Hooks](https://skaffold.dev/docs/lifecycle-hooks/) | beta | Run code triggered by different events during the skaffold process lifecycle. |
| [Init](https://skaffold.dev/docs/init) | beta | Initialize a skaffold.yaml file based on the contents of the current directory |
| [Insecure registry handling](https://skaffold.dev/docs/environment/image-registries/#insecure-image-registries) | GA | Target registries for built images which are not secure |
| [Log tailing](https://skaffold.dev/docs/log-tailing) | GA | automated log tailing of deployed pods |
| [Port-forwarding](https://skaffold.dev/docs/port-forwarding/) | GA | Port forward application to localhost |
| [Profiles](https://skaffold.dev/docs/environment/profiles/) | GA | Create different pipeline configurations based on overrides and patches defined in one or more profiles |
| [Render](https://skaffold.dev/docs/renderers) | beta | Renders a set of resources in your applications and replace the image name with the built images |
| [skaffold run](https://skaffold.dev/docs/workflows/ci-cd) | GA | One-off build & deployment of the skaffold application |
| [Filesync](https://skaffold.dev/docs/filesync) | GA | Instead of rebuilding, copy the changed files in the running container |
| [Tagpolicy](https://skaffold.dev/docs/taggers) | GA | Automated tagging |
| [Templating](https://skaffold.dev/docs/environment/templating/) | GA | certain fields of skaffold.yaml can be parametrized with environment and built-in variables |
| [Test](https://skaffold.dev/docs/testers) | GA | Run tests as part of your pipeline |
| [Test](https://skaffold.dev/docs/testers/structure) | GA | Run structure tests as part of your pipeline |
| [Trigger](https://skaffold.dev/docs/references/deprecation/) | GA | Feature area: Trigger configured actions when source files change |
| [skaffold verify](https://skaffold.dev/docs/references/deprecation/) | GA | User can run post deployment tests via skaffold monitored test containers |
| [version](https://skaffold.dev/docs/references/deprecation/) | GA | get the version string of the current skaffold binary |

Exceptions
----------

No policy can cover every possible situation. This policy is a living document, and will evolve over time. In practice, there will be situations that do not fit neatly into this policy, or for which this policy becomes a serious impediment. Examples could be getting fixes fast for a serious vulnerability, a destructive bug or requirements that might be imposed by third parties (such as legal requirements). Such situations should be discussed on the given bugs / feature requests and during Skaffold Office Hours, always bearing in mind that Skaffold is committed to being a stable system that, as much as possible, never breaks users. Exceptions will always be announced in all relevant release notes.

Current deprecation notices
---------------------------

04/07/2021: Release v1.22.0 deprecates the `--render-only` and `--render-output` flags from `skaffold run` and `skaffold dev`, in favor of simply using the `skaffold render` command directly. 05/05/2021: Release v1.23.0 deprecates the `--add-skaffold-labels` flag from `skaffold render`, and implicitly deprecates the addition of Skaffold-internal labels to any Kubernetes resources hydrated by Skaffold through `skaffold render`.

Past deprecation notices
------------------------

10/21/2019: With release v0.41.0 we mark for deprecation the `$IMAGES` environment variable passed to custom builders. Variable `$IMAGE` should be used instead.

**This environment variable flag was removed in version v1.22.0.**

03/15/2019: With release v0.25.0 we mark for deprecation the `flags` field in kaniko (`KanikoArtifact.AdditionalFlags`), instead Kaniko’s additional flags will now be represented as unique fields under `kaniko` per artifact (`KanikoArtifact` type).

**This field was removed in version 1.0.0.**

02/15/2019: With release v0.23.0 we mark for deprecation the following env variables in the `envTemplate` tagger:

*   `DIGEST`
*   `DIGEST_ALGO`
*   `DIGEST_HEX`

Currently these variables resolve to `_DEPRECATED_<envvar>_`, and the new tagging mechanism adds a digest to the image name thus it shouldn’t break existing configurations.

**This compatibility behavior was removed in version v1.22.0.**
