# Source: https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/

Title: Dependent Watches

URL Source: https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/

Markdown Content:
Dependent Watches | Operator SDK
===============
[![Image 1](https://sdk.operatorframework.io/build/images/logo-sm.svg)](https://sdk.operatorframework.io/)
*   [Home](https://sdk.operatorframework.io/)
*   [Build](https://sdk.operatorframework.io/build/ "Build")
*   [Documentation](https://sdk.operatorframework.io/docs/ "Documentation")
*   [Releases](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/#)[master](https://master.sdk.operatorframework.io/)[Latest Release](https://sdk.operatorframework.io/)[v1.42](https://v1-42-x.sdk.operatorframework.io/)[v1.41](https://v1-41-x.sdk.operatorframework.io/)[v1.40](https://v1-40-x.sdk.operatorframework.io/)[v1.39](https://v1-39-x.sdk.operatorframework.io/)[v1.38](https://v1-38-x.sdk.operatorframework.io/)[v1.37](https://v1-37-x.sdk.operatorframework.io/)[v1.36](https://v1-36-x.sdk.operatorframework.io/)[v1.35](https://v1-35-x.sdk.operatorframework.io/)[v1.34](https://v1-34-x.sdk.operatorframework.io/)[v1.33](https://v1-33-x.sdk.operatorframework.io/)[v1.32](https://v1-32-x.sdk.operatorframework.io/)[v1.31](https://v1-31-x.sdk.operatorframework.io/)[v1.30](https://v1-30-x.sdk.operatorframework.io/)[v1.29](https://v1-29-x.sdk.operatorframework.io/)[v1.28](https://v1-28-x.sdk.operatorframework.io/)[v1.27](https://v1-27-x.sdk.operatorframework.io/)[v1.26](https://v1-26-x.sdk.operatorframework.io/)[v1.25](https://github.com/operator-framework/operator-sdk/tree/v1.25.x/website/content/en/docs)[v1.24](https://github.com/operator-framework/operator-sdk/tree/v1.24.x/website/content/en/docs)[v1.23](https://github.com/operator-framework/operator-sdk/tree/v1.23.x/website/content/en/docs)[v1.22](https://github.com/operator-framework/operator-sdk/tree/v1.22.x/website/content/en/docs)[v1.21](https://github.com/operator-framework/operator-sdk/tree/v1.21.x/website/content/en/docs)[v1.20](https://github.com/operator-framework/operator-sdk/tree/v1.20.x/website/content/en/docs)[v1.19](https://github.com/operator-framework/operator-sdk/tree/v1.19.x/website/content/en/docs)[v1.18](https://github.com/operator-framework/operator-sdk/tree/v1.18.x/website/content/en/docs)[v1.17](https://github.com/operator-framework/operator-sdk/tree/v1.17.x/website/content/en/docs)[v1.16](https://github.com/operator-framework/operator-sdk/tree/v1.16.x/website/content/en/docs)[v1.15](https://github.com/operator-framework/operator-sdk/tree/v1.15.x/website/content/en/docs)[v1.14](https://github.com/operator-framework/operator-sdk/tree/v1.14.x/website/content/en/docs)[v1.13](https://github.com/operator-framework/operator-sdk/tree/v1.13.x/website/content/en/docs)[v1.12](https://github.com/operator-framework/operator-sdk/tree/v1.12.x/website/content/en/docs)[v1.11](https://github.com/operator-framework/operator-sdk/tree/v1.11.x/website/content/en/docs)[v1.10](https://github.com/operator-framework/operator-sdk/tree/v1.10.x/website/content/en/docs)[v1.9](https://github.com/operator-framework/operator-sdk/tree/v1.9.x/website/content/en/docs)[v1.8](https://github.com/operator-framework/operator-sdk/tree/v1.8.x/website/content/en/docs)[v1.7](https://github.com/operator-framework/operator-sdk/tree/v1.7.x/website/content/en/docs)[v1.6](https://github.com/operator-framework/operator-sdk/tree/v1.6.x/website/content/en/docs)[v1.5](https://github.com/operator-framework/operator-sdk/tree/v1.5.x/website/content/en/docs)[v1.4](https://github.com/operator-framework/operator-sdk/tree/v1.4.x/website/content/en/docs)[v1.3](https://github.com/operator-framework/operator-sdk/tree/v1.3.x/website/content/en/docs)[v1.2](https://github.com/operator-framework/operator-sdk/tree/v1.2.x/website/content/en/docs)[v1.1](https://github.com/operator-framework/operator-sdk/tree/v1.1.x/website/content/en/docs)[v1.0](https://github.com/operator-framework/operator-sdk/tree/v1.0.x/website/content/en/docs)[v0.19](https://github.com/operator-framework/operator-sdk/tree/v0.19.x/website/content/en/docs)[v0.18](https://github.com/operator-framework/operator-sdk/tree/v0.18.x/website/content/en/docs)[v0.17](https://github.com/operator-framework/operator-sdk/tree/v0.17.x/doc) 

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

        

[Edit this page](https://github.com/operator-framework/operator-sdk/edit/master/website/content/en/docs/building-operators/ansible/reference/dependent-watches.md)[Create documentation issue](https://github.com/operator-framework/operator-sdk/issues/new?title=Dependent%20Watches)

*       *   [What are dependent resources?](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/#what-are-dependent-resources)
    *   [Why the `watchDependentResources` option?](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/#why-the-watchdependentresources-option)
    *   [How is this achieved?](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/#how-is-this-achieved)
    *   [Example](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/#example)

1.   [Documentation](https://sdk.operatorframework.io/docs/)
2.   [Building Operators](https://sdk.operatorframework.io/docs/building-operators/)
3.   [Ansible](https://sdk.operatorframework.io/docs/building-operators/ansible/)
4.   [Reference](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/)
5.   [Dependent Watches](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/)

Dependent Watches
=================

This document describes the `watchDependentResources` option in [`watches.yaml`](https://sdk.operatorframework.io/docs/building-operators/ansible/reference/dependent-watches/#example) file. It delves into what dependent resources are, why the option is required, how it is achieved and finally gives an example.

### What are dependent resources?

In most cases, an operator creates a bunch of Kubernetes resources in the cluster, that helps deploy and manage the application. For instance, the [etcd-operator](https://github.com/coreos/etcd-operator/blob/master/doc/gif/demo.gif) creates two services and a number of pods for a single `EtcdCluster` CR. In this case, all the Kubernetes resources created by the operator for a CR is defined as dependent resources.

### Why the `watchDependentResources` option?

Often, an operator needs to watch dependent resources. To achieve this, a developer would set the field, `watchDependentResources` to `True` in the `watches.yaml` file. If enabled, a change in a dependent resource will trigger the reconciliation loop causing Ansible code to run.

For example, since the _etcd-operator_ needs to ensure that all the pods are up and running, it needs to know when a pod changes. Enabling the dependent watches option would trigger the reconciliation loop to run. The Ansible logic needs to handle these cases and make sure that all the dependent resources are in the desired state as declared by the `CR spec`

`Note: By default it is enabled when using ansible-operator`

### How is this achieved?

The `ansible-operator` base image achieves this by leveraging the concept of [owner-references](https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/). Whenever a Kubernetes resource is created by Ansible code, the `ansible-operator`'s `proxy` module injects `owner-references` into the resource being created. The `owner-references` means the resource is owned by the CR for which reconciliation is taking place.

Whenever the `watchDependentResources` field is enabled, the `ansible-operator` will watch all the resources owned by the CR, registering callbacks to their change events. Upon a change, the callback will enqueue a `ReconcileRequest` for the CR. The enqueued reconciliation request will trigger the `Reconcile` function of the controller which will execute the ansible logic for reconciliation.

### Example

This is an example of a watches file with the `watchDependentResources` field set to `True`

```yaml
- version: v1alpha1
  group: app.example.com
  kind: AppService
  playbook: playbook.yml
  maxRunnerArtifacts: 30
  reconcilePeriod: 5s
  manageStatus: False
  watchDependentResources: True
```

Last modified July 17, 2020: [[docs] Reorganize hugo doc site (#3382) (1248c1ca)](https://github.com/operator-framework/operator-sdk/commit/1248c1ca2e0b7b7162471349daddb731657fe117)

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
