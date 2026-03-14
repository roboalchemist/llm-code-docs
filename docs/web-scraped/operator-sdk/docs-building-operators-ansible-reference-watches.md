# Source: https://sdk.operatorframework.io/docs/building-operators/ansible/reference/watches/

Title: Ansible Operator Watches

URL Source: https://sdk.operatorframework.io/docs/building-operators/ansible/reference/watches/

Markdown Content:
Ansible Operator Watches | Operator SDK
===============
[![Image 1](https://sdk.operatorframework.io/build/images/logo-sm.svg)](https://sdk.operatorframework.io/)
*   [Home](https://sdk.operatorframework.io/)
*   [Build](https://sdk.operatorframework.io/build/ "Build")
*   [Documentation](https://sdk.operatorframework.io/docs/ "Documentation")
*   [Releases](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/watches/#)[master](https://master.sdk.operatorframework.io/)[Latest Release](https://sdk.operatorframework.io/)[v1.42](https://v1-42-x.sdk.operatorframework.io/)[v1.41](https://v1-41-x.sdk.operatorframework.io/)[v1.40](https://v1-40-x.sdk.operatorframework.io/)[v1.39](https://v1-39-x.sdk.operatorframework.io/)[v1.38](https://v1-38-x.sdk.operatorframework.io/)[v1.37](https://v1-37-x.sdk.operatorframework.io/)[v1.36](https://v1-36-x.sdk.operatorframework.io/)[v1.35](https://v1-35-x.sdk.operatorframework.io/)[v1.34](https://v1-34-x.sdk.operatorframework.io/)[v1.33](https://v1-33-x.sdk.operatorframework.io/)[v1.32](https://v1-32-x.sdk.operatorframework.io/)[v1.31](https://v1-31-x.sdk.operatorframework.io/)[v1.30](https://v1-30-x.sdk.operatorframework.io/)[v1.29](https://v1-29-x.sdk.operatorframework.io/)[v1.28](https://v1-28-x.sdk.operatorframework.io/)[v1.27](https://v1-27-x.sdk.operatorframework.io/)[v1.26](https://v1-26-x.sdk.operatorframework.io/)[v1.25](https://github.com/operator-framework/operator-sdk/tree/v1.25.x/website/content/en/docs)[v1.24](https://github.com/operator-framework/operator-sdk/tree/v1.24.x/website/content/en/docs)[v1.23](https://github.com/operator-framework/operator-sdk/tree/v1.23.x/website/content/en/docs)[v1.22](https://github.com/operator-framework/operator-sdk/tree/v1.22.x/website/content/en/docs)[v1.21](https://github.com/operator-framework/operator-sdk/tree/v1.21.x/website/content/en/docs)[v1.20](https://github.com/operator-framework/operator-sdk/tree/v1.20.x/website/content/en/docs)[v1.19](https://github.com/operator-framework/operator-sdk/tree/v1.19.x/website/content/en/docs)[v1.18](https://github.com/operator-framework/operator-sdk/tree/v1.18.x/website/content/en/docs)[v1.17](https://github.com/operator-framework/operator-sdk/tree/v1.17.x/website/content/en/docs)[v1.16](https://github.com/operator-framework/operator-sdk/tree/v1.16.x/website/content/en/docs)[v1.15](https://github.com/operator-framework/operator-sdk/tree/v1.15.x/website/content/en/docs)[v1.14](https://github.com/operator-framework/operator-sdk/tree/v1.14.x/website/content/en/docs)[v1.13](https://github.com/operator-framework/operator-sdk/tree/v1.13.x/website/content/en/docs)[v1.12](https://github.com/operator-framework/operator-sdk/tree/v1.12.x/website/content/en/docs)[v1.11](https://github.com/operator-framework/operator-sdk/tree/v1.11.x/website/content/en/docs)[v1.10](https://github.com/operator-framework/operator-sdk/tree/v1.10.x/website/content/en/docs)[v1.9](https://github.com/operator-framework/operator-sdk/tree/v1.9.x/website/content/en/docs)[v1.8](https://github.com/operator-framework/operator-sdk/tree/v1.8.x/website/content/en/docs)[v1.7](https://github.com/operator-framework/operator-sdk/tree/v1.7.x/website/content/en/docs)[v1.6](https://github.com/operator-framework/operator-sdk/tree/v1.6.x/website/content/en/docs)[v1.5](https://github.com/operator-framework/operator-sdk/tree/v1.5.x/website/content/en/docs)[v1.4](https://github.com/operator-framework/operator-sdk/tree/v1.4.x/website/content/en/docs)[v1.3](https://github.com/operator-framework/operator-sdk/tree/v1.3.x/website/content/en/docs)[v1.2](https://github.com/operator-framework/operator-sdk/tree/v1.2.x/website/content/en/docs)[v1.1](https://github.com/operator-framework/operator-sdk/tree/v1.1.x/website/content/en/docs)[v1.0](https://github.com/operator-framework/operator-sdk/tree/v1.0.x/website/content/en/docs)[v0.19](https://github.com/operator-framework/operator-sdk/tree/v0.19.x/website/content/en/docs)[v0.18](https://github.com/operator-framework/operator-sdk/tree/v0.18.x/website/content/en/docs)[v0.17](https://github.com/operator-framework/operator-sdk/tree/v0.17.x/doc) 

*   [Documentation](https://sdk.operatorframework.io/docs/)

    *           *   [Overview](https://sdk.operatorframework.io/docs/overview/)

        
            *   [Project Layout](https://sdk.operatorframework.io/docs/overview/project-layout/)[Cheat Sheet](https://sdk.operatorframework.io/docs/overview/cheat-sheet/)[Capability Levels](https://sdk.operatorframework.io/docs/overview/operator-capabilities/)

        *   [Installation](https://sdk.operatorframework.io/docs/installation/)

        

        *   [Building Operators](https://sdk.operatorframework.io/docs/building-operators/)

        
            *                   *   [Ansible](https://sdk.operatorframework.io/docs/building-operators/ansible/)

                
                    *   [Installation](https://sdk.operatorframework.io/docs/building-operators/ansible/installation/)[Quickstart](https://sdk.operatorframework.io/docs/building-operators/ansible/quickstart/)[Tutorial](https://sdk.operatorframework.io/docs/building-operators/ansible/tutorial/)[Testing with Molecule](https://sdk.operatorframework.io/docs/building-operators/ansible/testing-guide/)[Development Tips](https://sdk.operatorframework.io/docs/building-operators/ansible/development-tips/)[Migrating from pre-v1.0.0 to latest](https://sdk.operatorframework.io/docs/building-operators/ansible/migration/)
                        *   [Reference](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/)

                        
                            *   [Advanced Options](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/advanced_options/)[Base Images](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/ansible-base-images/)[Dependent Watches](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/)[Finalizers](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/)[Information Flow](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/information-flow-ansible-operator/)[Metrics](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/internal_metrics/)[Proxy Vars](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/proxy-vars/)[Retroactively Owned Resources](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/retroactively-owned-resources/)[Scaffolding](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/scaffolding/)[Watches](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/watches/)[Webhooks](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/webhooks/)

                *   [Go](https://sdk.operatorframework.io/docs/building-operators/golang/)

                
                    *   [Installation](https://sdk.operatorframework.io/docs/building-operators/golang/installation/)[Quickstart](https://sdk.operatorframework.io/docs/building-operators/golang/quickstart/)[Tutorial](https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/)[Webhook](https://sdk.operatorframework.io/docs/building-operators/golang/webhook/)[Operator Scope](https://sdk.operatorframework.io/docs/building-operators/golang/operator-scope/)[CRD Scope](https://sdk.operatorframework.io/docs/building-operators/golang/crds-scope/)[Testing with EnvTest](https://sdk.operatorframework.io/docs/building-operators/golang/testing/)[Advanced Topics](https://sdk.operatorframework.io/docs/building-operators/golang/advanced-topics/)
                        *   [Reference](https://sdk.operatorframework.io/docs/building-operators/golang/references/)

                        
                            *   [Controller Runtime Client API](https://sdk.operatorframework.io/docs/building-operators/golang/references/client/)[Logging](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/)[Proxy Vars](https://sdk.operatorframework.io/docs/building-operators/golang/references/proxy-vars/)[Using Predicates for Event Filtering](https://sdk.operatorframework.io/docs/building-operators/golang/references/event-filtering/)[API Markers](https://sdk.operatorframework.io/docs/building-operators/golang/references/markers/)[OpenAPI validation](https://sdk.operatorframework.io/docs/building-operators/golang/references/openapi-validation/)

[Migrating from pre-v1.0.0 to latest](https://sdk.operatorframework.io/docs/building-operators/golang/migration/)

                *   [Helm](https://sdk.operatorframework.io/docs/building-operators/helm/)

                
                    *   [Installation](https://sdk.operatorframework.io/docs/building-operators/helm/installation/)[Quickstart](https://sdk.operatorframework.io/docs/building-operators/helm/quickstart/)[Migrating from pre-v1.0.0 to latest](https://sdk.operatorframework.io/docs/building-operators/helm/migration/)[Tutorial](https://sdk.operatorframework.io/docs/building-operators/helm/tutorial/)
                        *   [Reference](https://sdk.operatorframework.io/docs/building-operators/helm/reference/)

                        
                            *   [Proxy Vars](https://sdk.operatorframework.io/docs/building-operators/helm/reference/proxy-vars/)[Define Watches](https://sdk.operatorframework.io/docs/building-operators/helm/reference/watches/)
                                *   [Advanced Features](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/)

                                
                                    *   [Override Values](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/)[Maximum Concurrent Reconciles](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/max_concurrent_reconciles/)[Custom Resource Annotations](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/annotations/)

        *   [Testing Operators](https://sdk.operatorframework.io/docs/testing-operators/)

        
            *                   *   [Scorecard](https://sdk.operatorframework.io/docs/testing-operators/scorecard/)

                
                    *   [Writing Custom Scorecard Tests](https://sdk.operatorframework.io/docs/testing-operators/scorecard/custom-tests/)[Writing Kuttl Scorecard Tests](https://sdk.operatorframework.io/docs/testing-operators/scorecard/kuttl-tests/)

        *   [Upgrade SDK Version](https://sdk.operatorframework.io/docs/upgrading-sdk-version/)

        
            *   [Backport Policy](https://sdk.operatorframework.io/docs/upgrading-sdk-version/backport-policy/)[v1.42.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.42.0/)[v1.41.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.41.0/)[v1.40.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.40.0/)[v1.39.2](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.39.2/)[v1.39.1](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.39.1/)[v1.39.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.39.0/)[v1.38.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.38.0/)[v1.37.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.37.0/)[v1.36.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.36.0/)[v1.35.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.35.0/)[v1.34.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.34.0/)[v1.33.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.33.0/)[v1.32.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.32.0/)[v1.31.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.31.0/)[v1.30.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.30.0/)[v1.29.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.29.0/)[v1.28.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.28.0/)[v1.27.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.27.0/)[v1.26.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.26.0/)[v1.25.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.25.0/)[v1.24.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.24.0/)[v1.23.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.23.0/)[v1.22.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.22.0/)[v1.21.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.21.0/)[v1.20.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.20.0/)[v1.19.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.19.0/)[v1.18.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.18.0/)[v1.17.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.17.0/)[v1.16.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.16.0/)[v1.15.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.15.0/)[v1.14.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.14.0/)[v1.13.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.13.0/)[v1.12.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.12.0/)[v1.11.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.11.0/)[v1.10.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.10.0/)[v1.9.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.9.0/)[v1.8.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.8.0/)[v1.7.1](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.7.1/)[v1.7.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.7.0/)[v1.6.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.6.0/)[v1.6.1](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.6.1/)[v1.5.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.5.0/)[v1.4.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.4.0/)[v1.3.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.3.0/)[v1.2.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.2.0/)[v1.1.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.1.0/)[v1.0.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v1.0.0/)[v0.19.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v0.19.0/)[v0.18.0](https://sdk.operatorframework.io/docs/upgrading-sdk-version/v0.18.0/)

        *   [Commands](https://sdk.operatorframework.io/docs/cli/)

        
            *   [operator-sdk](https://sdk.operatorframework.io/docs/cli/operator-sdk/)[operator-sdk alpha](https://sdk.operatorframework.io/docs/cli/operator-sdk_alpha/)[operator-sdk alpha config-3alpha-to-3](https://sdk.operatorframework.io/docs/cli/operator-sdk_alpha_config-3alpha-to-3/)[operator-sdk alpha generate](https://sdk.operatorframework.io/docs/cli/operator-sdk_alpha_generate/)[operator-sdk bundle](https://sdk.operatorframework.io/docs/cli/operator-sdk_bundle/)[operator-sdk bundle validate](https://sdk.operatorframework.io/docs/cli/operator-sdk_bundle_validate/)[operator-sdk cleanup](https://sdk.operatorframework.io/docs/cli/operator-sdk_cleanup/)[operator-sdk completion](https://sdk.operatorframework.io/docs/cli/operator-sdk_completion/)[operator-sdk completion bash](https://sdk.operatorframework.io/docs/cli/operator-sdk_completion_bash/)[operator-sdk completion fish](https://sdk.operatorframework.io/docs/cli/operator-sdk_completion_fish/)[operator-sdk completion powershell](https://sdk.operatorframework.io/docs/cli/operator-sdk_completion_powershell/)[operator-sdk completion zsh](https://sdk.operatorframework.io/docs/cli/operator-sdk_completion_zsh/)[operator-sdk create](https://sdk.operatorframework.io/docs/cli/operator-sdk_create/)[operator-sdk create api](https://sdk.operatorframework.io/docs/cli/operator-sdk_create_api/)[operator-sdk create webhook](https://sdk.operatorframework.io/docs/cli/operator-sdk_create_webhook/)[operator-sdk edit](https://sdk.operatorframework.io/docs/cli/operator-sdk_edit/)[operator-sdk generate](https://sdk.operatorframework.io/docs/cli/operator-sdk_generate/)[operator-sdk generate bundle](https://sdk.operatorframework.io/docs/cli/operator-sdk_generate_bundle/)[operator-sdk generate kustomize](https://sdk.operatorframework.io/docs/cli/operator-sdk_generate_kustomize/)[operator-sdk generate kustomize manifests](https://sdk.operatorframework.io/docs/cli/operator-sdk_generate_kustomize_manifests/)[operator-sdk init](https://sdk.operatorframework.io/docs/cli/operator-sdk_init/)[operator-sdk olm](https://sdk.operatorframework.io/docs/cli/operator-sdk_olm/)[operator-sdk olm install](https://sdk.operatorframework.io/docs/cli/operator-sdk_olm_install/)[operator-sdk olm status](https://sdk.operatorframework.io/docs/cli/operator-sdk_olm_status/)[operator-sdk olm uninstall](https://sdk.operatorframework.io/docs/cli/operator-sdk_olm_uninstall/)[operator-sdk pkgman-to-bundle](https://sdk.operatorframework.io/docs/cli/operator-sdk_pkgman-to-bundle/)[operator-sdk run](https://sdk.operatorframework.io/docs/cli/operator-sdk_run/)[operator-sdk run bundle](https://sdk.operatorframework.io/docs/cli/operator-sdk_run_bundle/)[operator-sdk run bundle-upgrade](https://sdk.operatorframework.io/docs/cli/operator-sdk_run_bundle-upgrade/)[operator-sdk scorecard](https://sdk.operatorframework.io/docs/cli/operator-sdk_scorecard/)[operator-sdk version](https://sdk.operatorframework.io/docs/cli/operator-sdk_version/)

        *   [OLM Integration](https://sdk.operatorframework.io/docs/olm-integration/)

        
            *   [Bundle Quickstart](https://sdk.operatorframework.io/docs/olm-integration/quickstart-bundle/)[Bundle Tutorial](https://sdk.operatorframework.io/docs/olm-integration/tutorial-bundle/)[Package Manifests Quickstart](https://sdk.operatorframework.io/docs/olm-integration/tutorial-package-manifests/)[CLI Overview](https://sdk.operatorframework.io/docs/olm-integration/cli-overview/)[Generating Manifests and Metadata](https://sdk.operatorframework.io/docs/olm-integration/generation/)[Testing Deployment](https://sdk.operatorframework.io/docs/olm-integration/testing-deployment/)

        *   [Advanced Topics](https://sdk.operatorframework.io/docs/advanced-topics/)

        
            *   [Custom Bundle Validation](https://sdk.operatorframework.io/docs/advanced-topics/custom-bundle-validation/)[Multiple Architectures](https://sdk.operatorframework.io/docs/advanced-topics/multi-arch/)[Multiple Service Accounts](https://sdk.operatorframework.io/docs/advanced-topics/multi-sa/)

        *   [Best Practices](https://sdk.operatorframework.io/docs/best-practices/)

        
            *   [Best practices](https://sdk.operatorframework.io/docs/best-practices/best-practices/)[Common suggestions](https://sdk.operatorframework.io/docs/best-practices/common-recommendation/)[Resource Pruning](https://sdk.operatorframework.io/docs/best-practices/resource-pruning/)[Multi-Tenancy](https://sdk.operatorframework.io/docs/best-practices/multi-tenancy/)[Designing Lean Operators](https://sdk.operatorframework.io/docs/best-practices/designing-lean-operators/)[Managing Resources](https://sdk.operatorframework.io/docs/best-practices/managing-resources/)[Pod Security Standards](https://sdk.operatorframework.io/docs/best-practices/pod-security-standards/)[Observability Best Practices](https://sdk.operatorframework.io/docs/best-practices/observability-best-practices/)

        *   [Contribution Guide](https://sdk.operatorframework.io/docs/contribution-guidelines/)

        
            *   [Development](https://sdk.operatorframework.io/docs/contribution-guidelines/developer-guide/)[Releasing](https://sdk.operatorframework.io/docs/contribution-guidelines/releasing/)[Reporting Issues](https://sdk.operatorframework.io/docs/contribution-guidelines/reporting-issues/)[Testing](https://sdk.operatorframework.io/docs/contribution-guidelines/testing/)[Plugins](https://sdk.operatorframework.io/docs/contribution-guidelines/plugins/)[Documentation](https://sdk.operatorframework.io/docs/contribution-guidelines/documentation/)[Changelog](https://sdk.operatorframework.io/docs/contribution-guidelines/changelog/)[Issue Lifecycle](https://sdk.operatorframework.io/docs/contribution-guidelines/issue-lifecycle/)[Opening Pull Requests](https://sdk.operatorframework.io/docs/contribution-guidelines/opening-pull-requests/)[FAQ](https://sdk.operatorframework.io/docs/contribution-guidelines/faq/)

        *   [FAQ](https://sdk.operatorframework.io/docs/faqs/)

        

[Edit this page](https://github.com/operator-framework/operator-sdk/edit/master/website/content/en/docs/building-operators/ansible/reference/watches.md)[Create documentation issue](https://github.com/operator-framework/operator-sdk/issues/new?title=Ansible%20Operator%20Watches)

1.   [Documentation](https://sdk.operatorframework.io/docs/)
2.   [Building Operators](https://sdk.operatorframework.io/docs/building-operators/)
3.   [Ansible](https://sdk.operatorframework.io/docs/building-operators/ansible/)
4.   [Reference](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/)
5.   [Watches](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/watches/)

Ansible Operator Watches
========================

The Watches file contains a list of mappings from custom resources, identified by it’s Group, Version, and Kind, to an Ansible Role or Playbook. The Operator expects this mapping file in a predefined location: `/opt/ansible/watches.yaml` These resources, as well as child resources (determined by owner references) will be monitored for updates and cached.

*   **group**: The group of the Custom Resource that you will be watching.
*   **version**: The version of the Custom Resource that you will be watching.
*   **kind**: The kind of the Custom Resource that you will be watching.
*   **role** (default): Specifies a role to be executed. This field is mutually exclusive with the “playbook” field. This field can be: 
    *   an absolute path to a role directory.
    *   a relative path within one of the directories specified by `ANSIBLE_ROLES_PATH` environment variable or `ansible-roles-path` flag.
    *   a relative path within the current working directory, which defaults to `/opt/ansible/roles`.
    *   a fully qualified collection name of an installed Ansible collection. Ansible collections are installed to `~/.ansible/collections` or `/usr/share/ansible/collections` by default. If they are installed elsewhere, use the `ANSIBLE_COLLECTIONS_PATH` environment variable or the `ansible-collections-path` flag

*   **playbook**: This is the playbook name that you have added to the container. This playbook is expected to be simply a way to call roles. This field is mutually exclusive with the “role” field. When running locally, the playbook is expected to be in the current project directory.
*   **vars**: This is an arbitrary map of key-value pairs. The contents will be passed as `extra_vars` to the playbook or role specified for this watch.
*   **reconcilePeriod** (optional): The maximum interval that the operator will wait before beginning another reconcile, even if no watched events are received. When an operator watches many resources, each reconcile can become expensive, and a low value here can actually reduce performance. Typically, this option should only be used in advanced use cases where `watchDependentResources` is set to `False` and when is not possible to use the watch feature. E.g To manage external resources that don’t emit Kubernetes events. The format for the duration string is a sequence of decimal numbers, each with optional fraction and a unit suffix, such as “300ms”, “1.5h” or “2h45m”. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Defaults to 10 hours.
*   **manageStatus** (optional): When true (default), the operator will manage the status of the CR generically. Set to false, the status of the CR is managed elsewhere, by the specified role/playbook or in a separate controller.
*   **blacklist**: A list of child resources (by GVK) that will not be watched or cached.

An example Watches file:

```yaml
---
# Simple example mapping Foo to the Foo role
- version: v1alpha1
  group: foo.example.com
  kind: Foo
  role: Foo

# Simple example mapping Bar to a playbook
- version: v1alpha1
  group: bar.example.com
  kind: Bar
  playbook: playbook.yml

# More complex example for our Baz kind
# Here we will disable requeuing and be managing the CR status in the playbook,
# and specify additional variables.
- version: v1alpha1
  group: baz.example.com
  kind: Baz
  playbook: baz.yml
  manageStatus: False
  vars:
    foo: bar

# ConfigMaps owned by a Memcached CR will not be watched or cached.
- version: v1alpha1
  group: cache.example.com
  kind: Memcached
  role: /opt/ansible/roles/memcached
  blacklist:
    - group: ""
      version: v1
      kind: ConfigMap

# Example usage with a role from an installed Ansible collection
- version: v1alpha1
  group: bar.example.com
  kind: Bar
  role: myNamespace.myCollection.myRole

# Example filtering of resources with specific labels
- version: v1alpha1
  group: bar.example.com
  kind: Bar
  playbook: playbook.yml
  selector:
    matchLabels:
      foo: bar
    matchExpressions:
      - {key: foo, operator: In, values: [bar]}
      - {key: baz, operator: Exists, values: []}
```

The advanced features can be enabled by adding them to your watches file per GVK. They can go below the `group`, `version`, `kind` and `playbook` or `role`.

Some features can be overridden per resource via an annotation on that CR. The options that are overridable will have the annotation specified below.

| Feature | Yaml Key | Description | Annotation for override | default | Documentation |
| --- | --- | --- | --- | --- | --- |
| Reconcile Period | `reconcilePeriod` | time between reconcile runs for a particular CR | ansible.sdk.operatorframework.io/reconcile-period | 10h |  |
| Manage Status | `manageStatus` | Allows the ansible operator to manage the conditions section of each resource’s status section. |  | true |  |
| Watching Dependent Resources | `watchDependentResources` | Allows the ansible operator to dynamically watch resources that are created by ansible |  | true | [dependent watches](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches) |
| Watching Cluster-Scoped Resources | `watchClusterScopedResources` | Allows the ansible operator to watch cluster-scoped resources that are created by ansible |  | false |  |
| Max Runner Artifacts | `maxRunnerArtifacts` | Manages the number of [artifact directories](https://ansible-runner.readthedocs.io/en/latest/intro.html#runner-artifacts-directory-hierarchy) that ansible runner will keep in the operator container for each individual resource. | ansible.sdk.operatorframework.io/max-runner-artifacts | 20 |  |
| Finalizer | `finalizer` | Sets a finalizer on the CR and maps a deletion event to a playbook or role |  |  | [finalizers](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers) |
| Selector | `selector` | Identifies a set of objects based on their labels |  | None Applied | [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) |
| Automatic Case Conversion | `snakeCaseParameters` | Determines whether to convert the CR spec from camelCase to snake_case before passing the contents to Ansible as extra_vars |  | true |  |
| Watching Annotations Changes | `watchAnnotationsChanges` | Allows the ansible operator to trigger reconciliations on annotations changes on watched resources |  | false |  |

#### Example

```YaML
---
- version: v1alpha1
  group: app.example.com
  kind: AppService
  playbook: playbook.yml
  maxRunnerArtifacts: 30
  reconcilePeriod: 5s
  manageStatus: False
  watchDependentResources: False
  snakeCaseParameters: False
  finalizer:
    name: app.example.com/finalizer
    vars:
      state: absent
```

**Note:** By using the command `operator-sdk add api` you are able to add additional CRDs to the project API, which can aid in designing your solution using concepts such as encapsulation, single responsibility principle, and cohesion, which could make the project easier to read, debug, and maintain. With this approach, you are able to customize and optimize the configurations more specifically per GVK via the `watches.yaml` file.

**Example:**

```YaML
---
- version: v1alpha1
  group: app.example.com
  kind: AppService
  playbook: playbook.yml
  maxRunnerArtifacts: 30
  reconcilePeriod: 5s
  manageStatus: False
  watchDependentResources: False
  finalizer:
    name: app.example.com/finalizer
    vars:
      state: absent

- version: v1alpha1
  group: app.example.com
  kind: Database
  playbook: playbook.yml
  watchDependentResources: True
  manageStatus: True
```

Last modified May 30, 2023: [state default reconcilePeriod value in ansible docs (#6449) (1f711f5a)](https://github.com/operator-framework/operator-sdk/commit/1f711f5ae88bcd4fd861ed1dafea0619e3398de2)

![Image 2](https://sdk.operatorframework.io/build/images/logo.svg)
The Operator Framework is an open source toolkit to manage Kubernetes native applications, called Operators, in an effective, automated, and scalable way.

*   [Operator Framework](https://github.com/operator-framework)
*   [Operator Lifecycle Manager](https://github.com/operator-framework/operator-lifecycle-manager)
*   [OperatorHub](https://operatorhub.io/)

#### Connect with us!

*   [](https://groups.google.com/forum/#!forum/operator-framework)
*   [](https://github.com/operator-framework/operator-sdk)

Copyright © 2020

[![Image 3: Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
