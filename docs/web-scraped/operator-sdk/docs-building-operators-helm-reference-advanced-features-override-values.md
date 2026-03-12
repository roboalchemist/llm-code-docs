# Source: https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/

Title: Setting Override Values in Helm-based Operators

URL Source: https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/

Markdown Content:
Setting Override Values in Helm-based Operators | Operator SDK
===============
[![Image 1](https://sdk.operatorframework.io/build/images/logo-sm.svg)](https://sdk.operatorframework.io/)
*   [Home](https://sdk.operatorframework.io/)
*   [Build](https://sdk.operatorframework.io/build/ "Build")
*   [Documentation](https://sdk.operatorframework.io/docs/ "Documentation")
*   [Releases](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/#)[master](https://master.sdk.operatorframework.io/)[Latest Release](https://sdk.operatorframework.io/)[v1.42](https://v1-42-x.sdk.operatorframework.io/)[v1.41](https://v1-41-x.sdk.operatorframework.io/)[v1.40](https://v1-40-x.sdk.operatorframework.io/)[v1.39](https://v1-39-x.sdk.operatorframework.io/)[v1.38](https://v1-38-x.sdk.operatorframework.io/)[v1.37](https://v1-37-x.sdk.operatorframework.io/)[v1.36](https://v1-36-x.sdk.operatorframework.io/)[v1.35](https://v1-35-x.sdk.operatorframework.io/)[v1.34](https://v1-34-x.sdk.operatorframework.io/)[v1.33](https://v1-33-x.sdk.operatorframework.io/)[v1.32](https://v1-32-x.sdk.operatorframework.io/)[v1.31](https://v1-31-x.sdk.operatorframework.io/)[v1.30](https://v1-30-x.sdk.operatorframework.io/)[v1.29](https://v1-29-x.sdk.operatorframework.io/)[v1.28](https://v1-28-x.sdk.operatorframework.io/)[v1.27](https://v1-27-x.sdk.operatorframework.io/)[v1.26](https://v1-26-x.sdk.operatorframework.io/)[v1.25](https://github.com/operator-framework/operator-sdk/tree/v1.25.x/website/content/en/docs)[v1.24](https://github.com/operator-framework/operator-sdk/tree/v1.24.x/website/content/en/docs)[v1.23](https://github.com/operator-framework/operator-sdk/tree/v1.23.x/website/content/en/docs)[v1.22](https://github.com/operator-framework/operator-sdk/tree/v1.22.x/website/content/en/docs)[v1.21](https://github.com/operator-framework/operator-sdk/tree/v1.21.x/website/content/en/docs)[v1.20](https://github.com/operator-framework/operator-sdk/tree/v1.20.x/website/content/en/docs)[v1.19](https://github.com/operator-framework/operator-sdk/tree/v1.19.x/website/content/en/docs)[v1.18](https://github.com/operator-framework/operator-sdk/tree/v1.18.x/website/content/en/docs)[v1.17](https://github.com/operator-framework/operator-sdk/tree/v1.17.x/website/content/en/docs)[v1.16](https://github.com/operator-framework/operator-sdk/tree/v1.16.x/website/content/en/docs)[v1.15](https://github.com/operator-framework/operator-sdk/tree/v1.15.x/website/content/en/docs)[v1.14](https://github.com/operator-framework/operator-sdk/tree/v1.14.x/website/content/en/docs)[v1.13](https://github.com/operator-framework/operator-sdk/tree/v1.13.x/website/content/en/docs)[v1.12](https://github.com/operator-framework/operator-sdk/tree/v1.12.x/website/content/en/docs)[v1.11](https://github.com/operator-framework/operator-sdk/tree/v1.11.x/website/content/en/docs)[v1.10](https://github.com/operator-framework/operator-sdk/tree/v1.10.x/website/content/en/docs)[v1.9](https://github.com/operator-framework/operator-sdk/tree/v1.9.x/website/content/en/docs)[v1.8](https://github.com/operator-framework/operator-sdk/tree/v1.8.x/website/content/en/docs)[v1.7](https://github.com/operator-framework/operator-sdk/tree/v1.7.x/website/content/en/docs)[v1.6](https://github.com/operator-framework/operator-sdk/tree/v1.6.x/website/content/en/docs)[v1.5](https://github.com/operator-framework/operator-sdk/tree/v1.5.x/website/content/en/docs)[v1.4](https://github.com/operator-framework/operator-sdk/tree/v1.4.x/website/content/en/docs)[v1.3](https://github.com/operator-framework/operator-sdk/tree/v1.3.x/website/content/en/docs)[v1.2](https://github.com/operator-framework/operator-sdk/tree/v1.2.x/website/content/en/docs)[v1.1](https://github.com/operator-framework/operator-sdk/tree/v1.1.x/website/content/en/docs)[v1.0](https://github.com/operator-framework/operator-sdk/tree/v1.0.x/website/content/en/docs)[v0.19](https://github.com/operator-framework/operator-sdk/tree/v0.19.x/website/content/en/docs)[v0.18](https://github.com/operator-framework/operator-sdk/tree/v0.18.x/website/content/en/docs)[v0.17](https://github.com/operator-framework/operator-sdk/tree/v0.17.x/doc) 

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

        

[Edit this page](https://github.com/operator-framework/operator-sdk/edit/master/website/content/en/docs/building-operators/helm/reference/advanced_features/override_values.md)[Create documentation issue](https://github.com/operator-framework/operator-sdk/issues/new?title=Setting%20Override%20Values%20in%20Helm-based%20Operators)

*   [Basic usage](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/#basic-usage)
*   [Using environment variables](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/#using-environment-variables)
*   [Using Go templates](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/#using-go-templates)
*   [Event generation](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/#event-generation)

1.   [Documentation](https://sdk.operatorframework.io/docs/)
2.   [Building Operators](https://sdk.operatorframework.io/docs/building-operators/)
3.   [Helm](https://sdk.operatorframework.io/docs/building-operators/helm/)
4.   [Reference](https://sdk.operatorframework.io/docs/building-operators/helm/reference/)
5.   [Advanced Features](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/)
6.   [Override Values](https://sdk.operatorframework.io/docs/building-operators/helm/reference/advanced_features/override_values/)

Setting Override Values in Helm-based Operators
===============================================

Learn how to set override values and pass environment variables to your Helm chart.

Sometimes it is useful to pass down environment variables from the Operators `Deployment` all the way to the helm charts templates. This allows the Operator to be configured at a global level at runtime. This is new compared to dealing with the helm CLI as they usually don’t have access to any environment variables in the context of Tiller (helm v2) or the helm binary (helm v3) for security reasons.

With the helm Operator this becomes possible by override values. This enforces that certain template values provided by the chart’s default `values.yaml` or by a CR spec are always set when rendering the chart. If the value is set by a CR it gets overridden by the global override value. The override value can be static but can also refer to an environment variable and use go templates. Using override values is currently the only way to pass down environment variables to the chart.

An example use case of this is when your helm chart references container images by chart variables, which is a good practice. If your Operator is deployed in a disconnected environment (no network access to the default images location) you can use this mechanism to set them globally at the Operator level using environment variables versus individually per CR / chart release.

> Note that it is strongly recommended to reference container images in your chart by helm variables and then also associate these with an environment variable of your Operator like shown below. This allows your Operator to be mirrored for offline usage when packaged for OLM.

Basic usage
-----------

To configure your operator with override values, add an `overrideValues` map to your `watches.yaml` file for the GVK and chart you need to override. For example, to change the repository used by the nginx chart, you would update your `watches.yaml` to the following:

```yaml
# Use the 'create api' subcommand to add watches to this file.
- group: example.com
  version: v1alpha1
  kind: Nginx
  chart: helm-charts/nginx
  overrideValues:
    image.repository: quay.io/mycustomrepo/myimage
```

By setting `image.repository` to `quay.io/mycustomrepo/myimage` you are ensuring that `quay.io/mycustomrepo/myimage` will always be used instead of the chart’s default repository (`nginx`). If the CR attempts to set this value, it will be ignored.

Using environment variables
---------------------------

It is also possible to reference environment variables in the `overrideValues` section:

```yaml
overrideValues:
    image.repository: $IMAGE_REPOSITORY # or ${IMAGE_REPOSITORY}
```

By using an environment variable reference in `overrideValues` you enable these override values to be set at runtime by configuring the environment variable on the operator deployment. For example, in `config/manager/manager.yaml` you could add the following snippet to the container spec:

```yaml
env:
  - name: IMAGE_REPOSITORY
    value: quay.io/mycustomrepo/myimage
```

If an environment variable reference is listed in `overrideValues`, but is not present in the environment when the operator runs, it will resolve to an empty string and override all other values. Therefore, these environment variables should _always_ be set. It is suggested to update the Dockerfile to set these environment variables to the same defaults that are defined by the chart.

Using Go templates
------------------

Lastly, you can use Go `text/template` strings along with [slim-sprig](https://go-task.github.io/slim-sprig/) functions to provide even more flexibility when building override values.

For example, consider a situation where your operator has an environment variable, `$IMAGE`, set to `quay.io/mycustomrepo/myimage:latest`. You can use sprig template functions to split that environment variable into its repo and tag:

```yaml
overrideValues:
    image.repository: '{{ ("$IMAGE" | split ":")._0 }}'
    image.tag: '{{ ("$IMAGE" | split ":")._1 }}'
```

The resulting override values sent to the helm installation would look like:

```yaml
overrideValues:
    image.repository: quay.io/mycustomrepo/myimage
    image.tag: latest
```

Event generation
----------------

To warn users that their CR settings may be ignored, the Helm operator creates events on the CR that include the name and value of each overridden value. For example:

```
$ kubectl describe nginxes.example.com
...
Events:
  Type     Reason               Age   From              Message
  ----     ------               ----  ----              -------
  Warning  OverrideValuesInUse  1m    nginx-controller  Chart value "image.repository" overridden to "quay.io/mycustomrepo" by operator's watches.yaml
```

Last modified December 1, 2021: [Reorder sentence (#5408) (d56d3d7c)](https://github.com/operator-framework/operator-sdk/commit/d56d3d7c9d173f9a64acb4964cc1c8b8702143eb)

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
