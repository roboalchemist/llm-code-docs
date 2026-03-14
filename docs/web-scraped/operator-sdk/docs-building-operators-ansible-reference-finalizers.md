# Source: https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/

Title: Ansible Operator Finalizers

URL Source: https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/

Markdown Content:
Ansible Operator Finalizers | Operator SDK
===============
[![Image 1](https://sdk.operatorframework.io/build/images/logo-sm.svg)](https://sdk.operatorframework.io/)
*   [Home](https://sdk.operatorframework.io/)
*   [Build](https://sdk.operatorframework.io/build/ "Build")
*   [Documentation](https://sdk.operatorframework.io/docs/ "Documentation")
*   [Releases](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/#)[master](https://master.sdk.operatorframework.io/)[Latest Release](https://sdk.operatorframework.io/)[v1.42](https://v1-42-x.sdk.operatorframework.io/)[v1.41](https://v1-41-x.sdk.operatorframework.io/)[v1.40](https://v1-40-x.sdk.operatorframework.io/)[v1.39](https://v1-39-x.sdk.operatorframework.io/)[v1.38](https://v1-38-x.sdk.operatorframework.io/)[v1.37](https://v1-37-x.sdk.operatorframework.io/)[v1.36](https://v1-36-x.sdk.operatorframework.io/)[v1.35](https://v1-35-x.sdk.operatorframework.io/)[v1.34](https://v1-34-x.sdk.operatorframework.io/)[v1.33](https://v1-33-x.sdk.operatorframework.io/)[v1.32](https://v1-32-x.sdk.operatorframework.io/)[v1.31](https://v1-31-x.sdk.operatorframework.io/)[v1.30](https://v1-30-x.sdk.operatorframework.io/)[v1.29](https://v1-29-x.sdk.operatorframework.io/)[v1.28](https://v1-28-x.sdk.operatorframework.io/)[v1.27](https://v1-27-x.sdk.operatorframework.io/)[v1.26](https://v1-26-x.sdk.operatorframework.io/)[v1.25](https://github.com/operator-framework/operator-sdk/tree/v1.25.x/website/content/en/docs)[v1.24](https://github.com/operator-framework/operator-sdk/tree/v1.24.x/website/content/en/docs)[v1.23](https://github.com/operator-framework/operator-sdk/tree/v1.23.x/website/content/en/docs)[v1.22](https://github.com/operator-framework/operator-sdk/tree/v1.22.x/website/content/en/docs)[v1.21](https://github.com/operator-framework/operator-sdk/tree/v1.21.x/website/content/en/docs)[v1.20](https://github.com/operator-framework/operator-sdk/tree/v1.20.x/website/content/en/docs)[v1.19](https://github.com/operator-framework/operator-sdk/tree/v1.19.x/website/content/en/docs)[v1.18](https://github.com/operator-framework/operator-sdk/tree/v1.18.x/website/content/en/docs)[v1.17](https://github.com/operator-framework/operator-sdk/tree/v1.17.x/website/content/en/docs)[v1.16](https://github.com/operator-framework/operator-sdk/tree/v1.16.x/website/content/en/docs)[v1.15](https://github.com/operator-framework/operator-sdk/tree/v1.15.x/website/content/en/docs)[v1.14](https://github.com/operator-framework/operator-sdk/tree/v1.14.x/website/content/en/docs)[v1.13](https://github.com/operator-framework/operator-sdk/tree/v1.13.x/website/content/en/docs)[v1.12](https://github.com/operator-framework/operator-sdk/tree/v1.12.x/website/content/en/docs)[v1.11](https://github.com/operator-framework/operator-sdk/tree/v1.11.x/website/content/en/docs)[v1.10](https://github.com/operator-framework/operator-sdk/tree/v1.10.x/website/content/en/docs)[v1.9](https://github.com/operator-framework/operator-sdk/tree/v1.9.x/website/content/en/docs)[v1.8](https://github.com/operator-framework/operator-sdk/tree/v1.8.x/website/content/en/docs)[v1.7](https://github.com/operator-framework/operator-sdk/tree/v1.7.x/website/content/en/docs)[v1.6](https://github.com/operator-framework/operator-sdk/tree/v1.6.x/website/content/en/docs)[v1.5](https://github.com/operator-framework/operator-sdk/tree/v1.5.x/website/content/en/docs)[v1.4](https://github.com/operator-framework/operator-sdk/tree/v1.4.x/website/content/en/docs)[v1.3](https://github.com/operator-framework/operator-sdk/tree/v1.3.x/website/content/en/docs)[v1.2](https://github.com/operator-framework/operator-sdk/tree/v1.2.x/website/content/en/docs)[v1.1](https://github.com/operator-framework/operator-sdk/tree/v1.1.x/website/content/en/docs)[v1.0](https://github.com/operator-framework/operator-sdk/tree/v1.0.x/website/content/en/docs)[v0.19](https://github.com/operator-framework/operator-sdk/tree/v0.19.x/website/content/en/docs)[v0.18](https://github.com/operator-framework/operator-sdk/tree/v0.18.x/website/content/en/docs)[v0.17](https://github.com/operator-framework/operator-sdk/tree/v0.17.x/doc) 

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

        

[Edit this page](https://github.com/operator-framework/operator-sdk/edit/master/website/content/en/docs/building-operators/ansible/reference/finalizers.md)[Create documentation issue](https://github.com/operator-framework/operator-sdk/issues/new?title=Ansible%20Operator%20Finalizers)

*   

*   [Examples](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/#examples)
    *   [Run top-level playbook or role with new variables](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/#run-top-level-playbook-or-role-with-new-variables)
    *   [Run a different playbook or role](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/#run-a-different-playbook-or-role)
    *   [Run a different playbook or role with vars](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/#run-a-different-playbook-or-role-with-vars)

1.   [Documentation](https://sdk.operatorframework.io/docs/)
2.   [Building Operators](https://sdk.operatorframework.io/docs/building-operators/)
3.   [Ansible](https://sdk.operatorframework.io/docs/building-operators/ansible/)
4.   [Reference](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/)
5.   [Finalizers](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/finalizers/)

Ansible Operator Finalizers
===========================

The default behavior of an Ansible Operator is to delete all resources the operator created during reconciliation when a managed resource is marked for deletion. This behavior is usually sufficient for applications that exist only in Kubernetes, but sometimes it is necessary to perform more complex operations (for example, when your action performed against a third party API needs to be undone). These more complex cases can still be handled by Ansible Operator, through the use of a [finalizer](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#finalizers).

Finalizers allow controllers (such as an Ansible Operator) to implement asynchronous pre-delete hooks. This allows custom logic to run after a resource has been marked for deletion, but before the resource has actually been deleted from the Kubernetes cluster. For Ansible Operator, this hook takes the form of an Ansible playbook or role. You can define the mapping from your finalizer to a playbook or role by simply setting the `finalizer` field on the entry in your `watches.yaml`. You can also choose to re-run your top-level playbook or role with different variables set. The `watches.yaml` finalizer configuration accepts the following options:

See [Ansible watches documentation](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/watches/) for more information.

#### name

`name` is required.

This is the name of the finalizer. This is basically an arbitrary string, the existence of any finalizer string on a resource will prevent that resource from being deleted until the finalizer is removed. Ansible Operator will remove this string from the list of finalizers on successful execution of the specified role or playbook. A typical finalizer will be `<qualified-group>/finalizer`, where `<qualified-group>` is the fully qualified group of the resource being managed.

#### playbook

One of `playbook`, `role`, or `vars` must be provided. If `playbook` is not provided, it will default to the playbook specified at the top level of the `watches.yaml` entry.

This field is identical to the top-level `playbook` field. It requires an absolute path to a playbook on the operator’s file system.

#### role

One of `playbook`, `role`, or `vars` must be provided. If `role` is not provided, it will default to the role specified at the top level of the [`watches.yaml`][watches] entry.

This field is identical to the top-level `role` field.

#### vars

One of `playbook`, `role`, or `vars` must be provided.

`vars` is an arbitrary map of key-value pairs. The contents of `vars` will be passed as `extra_vars` to the playbook or role specified in the finalizer block, or at the top-level if neither `playbook` or `role` was set for the finalizer.

Examples
--------

Here are a few examples of `watches.yaml` files that specify a finalizer:

### Run top-level playbook or role with new variables

```yaml
---
- version: v1alpha1
  group: app.example.com
  kind: Database
  playbook: /opt/ansible/playbook.yml
  finalizer:
    name: app.example.com/finalizer
    vars:
      state: absent
```

This example will run `playbook.yml` when the Custom Resource is deleted. Because `vars` is set, the playbook will be run with `state` set to `absent`. Inside the playbook, the author can check this value and perform whatever cleanup is necessary.

```yaml
---
- version: v1alpha1
  group: app.example.com
  kind: Database
  role: database
  finalizer:
    name: app.example.com/finalizer
    vars:
      state: absent
```

This example is nearly identical to the first, except it will run the `/opt/ansible/roles/database` role, rather than a playbook, with the `state` variable set to `absent`.

### Run a different playbook or role

```yaml
---
- version: v1alpha1
  group: app.example.com
  kind: Database
  playbook: playbook.yml
  finalizer:
    name: app.example.com/finalizer
    role: teardown_database
```

This example will run the `/opt/ansible/roles/teardown_database` role when the Custom Resource is deleted.

```yaml
---
- version: v1alpha1
  group: app.example.com
  kind: Database
  playbook: playbook.yml
  finalizer:
    name: app.example.com/finalizer
    playbook: destroy.yml
```

This example will run the `/opt/ansible/destroy.yml` playbook when the Custom Resource is deleted.

```yaml
---
- version: v1alpha1
  group: app.example.com
  kind: Database
  playbook: playbook.yml
  finalizer:
    name: app.example.com/finalizer
    role: myNamespace.myCollection.myRole
```

This example will run the `myRole` when the Custom Resource is deleted. (The collection must have been installed.)

### Run a different playbook or role with vars

You can set `playbook` or `role` and `vars` at the same time. This can be useful if only a small part of your logic handles interacting with the component that requires cleanup. Rather than run all the logic again, you can specify only to run the role or playbook that handled the interaction, with a different variable set.

```yaml
---
- version: v1alpha1
  group: app.example.com
  kind: Database
  playbook: playbook.yml
  finalizer:
    name: app.example.com/finalizer
    role: manage_credentials
    vars:
      state: revoked
```

For this example, assume our application configures automated backups to a third party service. On deletion, all we want to do is revoke the credentials used to backup the data. We run just the `/opt/ansible/roles/manage_credentials` role, which is imported by our playbook to create the credentials in the first place, but we pass the `state: revoked` option, which causes the role to invalidate our credentials. For everything else in our application, automatic deletion of dependent resources will be sufficient, so we can exit successfully and let the operator remove our finalizer and allow the resource to be deleted.

Last modified February 3, 2021: [*: format finalizers correctly (ee7e682a)](https://github.com/operator-framework/operator-sdk/commit/ee7e682a2025f77824f1bd8ee97321320af1492f)

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
