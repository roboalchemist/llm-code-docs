# Source: https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/

Title: Logging

URL Source: https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/

Markdown Content:
Logging | Operator SDK
===============
[![Image 1](https://sdk.operatorframework.io/build/images/logo-sm.svg)](https://sdk.operatorframework.io/)
*   [Home](https://sdk.operatorframework.io/)
*   [Build](https://sdk.operatorframework.io/build/ "Build")
*   [Documentation](https://sdk.operatorframework.io/docs/ "Documentation")
*   [Releases](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#)[master](https://master.sdk.operatorframework.io/)[Latest Release](https://sdk.operatorframework.io/)[v1.42](https://v1-42-x.sdk.operatorframework.io/)[v1.41](https://v1-41-x.sdk.operatorframework.io/)[v1.40](https://v1-40-x.sdk.operatorframework.io/)[v1.39](https://v1-39-x.sdk.operatorframework.io/)[v1.38](https://v1-38-x.sdk.operatorframework.io/)[v1.37](https://v1-37-x.sdk.operatorframework.io/)[v1.36](https://v1-36-x.sdk.operatorframework.io/)[v1.35](https://v1-35-x.sdk.operatorframework.io/)[v1.34](https://v1-34-x.sdk.operatorframework.io/)[v1.33](https://v1-33-x.sdk.operatorframework.io/)[v1.32](https://v1-32-x.sdk.operatorframework.io/)[v1.31](https://v1-31-x.sdk.operatorframework.io/)[v1.30](https://v1-30-x.sdk.operatorframework.io/)[v1.29](https://v1-29-x.sdk.operatorframework.io/)[v1.28](https://v1-28-x.sdk.operatorframework.io/)[v1.27](https://v1-27-x.sdk.operatorframework.io/)[v1.26](https://v1-26-x.sdk.operatorframework.io/)[v1.25](https://github.com/operator-framework/operator-sdk/tree/v1.25.x/website/content/en/docs)[v1.24](https://github.com/operator-framework/operator-sdk/tree/v1.24.x/website/content/en/docs)[v1.23](https://github.com/operator-framework/operator-sdk/tree/v1.23.x/website/content/en/docs)[v1.22](https://github.com/operator-framework/operator-sdk/tree/v1.22.x/website/content/en/docs)[v1.21](https://github.com/operator-framework/operator-sdk/tree/v1.21.x/website/content/en/docs)[v1.20](https://github.com/operator-framework/operator-sdk/tree/v1.20.x/website/content/en/docs)[v1.19](https://github.com/operator-framework/operator-sdk/tree/v1.19.x/website/content/en/docs)[v1.18](https://github.com/operator-framework/operator-sdk/tree/v1.18.x/website/content/en/docs)[v1.17](https://github.com/operator-framework/operator-sdk/tree/v1.17.x/website/content/en/docs)[v1.16](https://github.com/operator-framework/operator-sdk/tree/v1.16.x/website/content/en/docs)[v1.15](https://github.com/operator-framework/operator-sdk/tree/v1.15.x/website/content/en/docs)[v1.14](https://github.com/operator-framework/operator-sdk/tree/v1.14.x/website/content/en/docs)[v1.13](https://github.com/operator-framework/operator-sdk/tree/v1.13.x/website/content/en/docs)[v1.12](https://github.com/operator-framework/operator-sdk/tree/v1.12.x/website/content/en/docs)[v1.11](https://github.com/operator-framework/operator-sdk/tree/v1.11.x/website/content/en/docs)[v1.10](https://github.com/operator-framework/operator-sdk/tree/v1.10.x/website/content/en/docs)[v1.9](https://github.com/operator-framework/operator-sdk/tree/v1.9.x/website/content/en/docs)[v1.8](https://github.com/operator-framework/operator-sdk/tree/v1.8.x/website/content/en/docs)[v1.7](https://github.com/operator-framework/operator-sdk/tree/v1.7.x/website/content/en/docs)[v1.6](https://github.com/operator-framework/operator-sdk/tree/v1.6.x/website/content/en/docs)[v1.5](https://github.com/operator-framework/operator-sdk/tree/v1.5.x/website/content/en/docs)[v1.4](https://github.com/operator-framework/operator-sdk/tree/v1.4.x/website/content/en/docs)[v1.3](https://github.com/operator-framework/operator-sdk/tree/v1.3.x/website/content/en/docs)[v1.2](https://github.com/operator-framework/operator-sdk/tree/v1.2.x/website/content/en/docs)[v1.1](https://github.com/operator-framework/operator-sdk/tree/v1.1.x/website/content/en/docs)[v1.0](https://github.com/operator-framework/operator-sdk/tree/v1.0.x/website/content/en/docs)[v0.19](https://github.com/operator-framework/operator-sdk/tree/v0.19.x/website/content/en/docs)[v0.18](https://github.com/operator-framework/operator-sdk/tree/v0.18.x/website/content/en/docs)[v0.17](https://github.com/operator-framework/operator-sdk/tree/v0.17.x/doc) 

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

        

[Edit this page](https://github.com/operator-framework/operator-sdk/edit/master/website/content/en/docs/building-operators/golang/references/logging.md)[Create documentation issue](https://github.com/operator-framework/operator-sdk/issues/new?title=Logging)

*   [Default zap logger](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#default-zap-logger)
    *   [A simple example](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#a-simple-example)

*   [Custom zap logger](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#custom-zap-logger)
    *   [Example](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#example)
    *   [Setting flags when running locally](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#setting-flags-when-running-locally)
    *   [Setting flags when deploying to a cluster](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#setting-flags-when-deploying-to-a-cluster)

*   [Creating a structured log statement](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#creating-a-structured-log-statement)
*   [Non-default logging](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/#non-default-logging)

1.   [Documentation](https://sdk.operatorframework.io/docs/)
2.   [Building Operators](https://sdk.operatorframework.io/docs/building-operators/)
3.   [Go](https://sdk.operatorframework.io/docs/building-operators/golang/)
4.   [Reference](https://sdk.operatorframework.io/docs/building-operators/golang/references/)
5.   [Logging](https://sdk.operatorframework.io/docs/building-operators/golang/references/logging/)

Logging
=======

Overview
========

Operator SDK-generated operators use the [`logr`](https://pkg.go.dev/github.com/go-logr/logr) interface to log. This log interface has several backends such as [`zap`](https://pkg.go.dev/github.com/go-logr/zapr), which the SDK uses in generated code by default. [`logr.Logger`](https://pkg.go.dev/github.com/go-logr/logr#Logger) exposes structured logging methods that help create machine-readable logs and adding a wealth of information to log records.

Default zap logger
------------------

Operator SDK uses a `zap`-based `logr` backend when scaffolding new projects. To assist with configuring and using this logger, the SDK includes several helper functions.

In the simple example below, we add the zap flagset to the operator’s command line flags with `BindFlags()`, and then set the controller-runtime logger with `zap.Options{}`.

By default, `zap.Options{}` will return a logger that is ready for production use. It uses a JSON encoder, logs starting at the `info` level. To customize the default behavior, users can use the zap flagset and specify flags on the command line. The zap flagset includes the following flags that can be used to configure the logger:

*   `--zap-devel`: Development Mode defaults(encoder=consoleEncoder,logLevel=Debug,stackTraceLevel=Warn) Production Mode defaults(encoder=jsonEncoder,logLevel=Info,stackTraceLevel=Error)
*   `--zap-encoder`: Zap log encoding (‘json’ or ‘console’)
*   `--zap-log-level`: Zap Level to configure the verbosity of logging. Can be one of ‘debug’, ‘info’, ‘error’, or any integer value > 0 which corresponds to custom debug levels of increasing verbosity”)
*   `--zap-stacktrace-level`: Zap Level at and above which stacktraces are captured (one of ‘info’ or ‘error’)

Consult the controller-runtime [godocs](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/log/zap#Options.BindFlags) for more detailed flag information.

### A simple example

Operators set the logger for all operator logging in `main.go`. To illustrate how this works, try out this simple example:

```Go
package main

import (
	"sigs.k8s.io/controller-runtime/pkg/log/zap"
	logf "sigs.k8s.io/controller-runtime/pkg/log"
)

var globalLog = logf.Log.WithName("global")
func main() {
	// Add the zap logger flag set to the CLI. The flag set must
	// be added before calling flag.Parse().
	opts := zap.Options{}
	opts.BindFlags(flag.CommandLine)
	flag.Parse()

	logger := zap.New(zap.UseFlagOptions(&opts))
	logf.SetLogger(logger)

	scopedLog := logf.Log.WithName("scoped")

	globalLog.Info("Printing at INFO level")
	globalLog.V(1).Info("Printing at DEBUG level")
	scopedLog.Info("Printing at INFO level")
	scopedLog.V(1).Info("Printing at DEBUG level")
}
```

#### Output using the defaults

```console
$ go run main.go
INFO[0000] Running the operator locally in namespace default.
{"level":"info","ts":1587741740.407766,"logger":"global","msg":"Printing at INFO level"}
{"level":"info","ts":1587741740.407855,"logger":"scoped","msg":"Printing at INFO level"}
```

#### Output overriding the log level to 1 (debug)

```console
$ go run main.go --zap-log-level=debug
INFO[0000] Running the operator locally in namespace default.
{"level":"info","ts":1587741837.602911,"logger":"global","msg":"Printing at INFO level"}
{"level":"debug","ts":1587741837.602964,"logger":"global","msg":"Printing at DEBUG level"}
{"level":"info","ts":1587741837.6029708,"logger":"scoped","msg":"Printing at INFO level"}
{"level":"debug","ts":1587741837.602973,"logger":"scoped","msg":"Printing at DEBUG level"}
```

Custom zap logger
-----------------

In order to use a custom zap logger, [`zap`](https://github.com/kubernetes-sigs/controller-runtime/tree/master/pkg/log/zap) from controller-runtime can be utilized to wrap it in a `logr` implementation.

Below is an example illustrating the use of [`zap-logfmt`](https://github.com/jsternberg/zap-logfmt) in logging.

### Example

In your `main.go` file, replace the current implementation for logs inside the `main` function:

```Go
...
// Add the zap logger flag set to the CLI. The flag set must
// be added before calling flag.Parse().
	opts := zap.Options{}
	opts.BindFlags(flag.CommandLine)
	flag.Parse()

	logger := zap.New(zap.UseFlagOptions(&opts))
	logf.SetLogger(logger)
...
```

With:

```Go
import(
	...
	zaplogfmt "github.com/sykesm/zap-logfmt"
	uzap "go.uber.org/zap"
	"go.uber.org/zap/zapcore"
	logf "sigs.k8s.io/controller-runtime/pkg/log"
	"sigs.k8s.io/controller-runtime/pkg/log/zap"
	...
)
	configLog := uzap.NewProductionEncoderConfig()
	configLog.EncodeTime = func(ts time.Time, encoder zapcore.PrimitiveArrayEncoder) {
		encoder.AppendString(ts.UTC().Format(time.RFC3339Nano))
	}
	logfmtEncoder := zaplogfmt.NewEncoder(configLog)

	// Construct a new logr.logger.
	logger := zap.New(zap.UseDevMode(true), zap.WriteTo(os.Stdout), zap.Encoder(logfmtEncoder))
	logf.SetLogger(logger)
```

**NOTE**: For this example, you will need to add the module `"github.com/sykesm/zap-logfmt"` to your project. Run `go get -u github.com/sykesm/zap-logfmt`.

#### Output using custom zap logger

```console
$ go run main.go
ts=2020-04-30T20:35:59.551268Z level=info logger=global msg="Printing at INFO level"
ts=2020-04-30T20:35:59.551314Z level=debug logger=global msg="Printing at DEBUG level"
ts=2020-04-30T20:35:59.551318Z level=info logger=scoped msg="Printing at INFO level"
ts=2020-04-30T20:35:59.55132Z level=debug logger=scoped msg="Printing at DEBUG level"
```

By using `sigs.k8s.io/controller-runtime/pkg/log`, your logger is propagated through `controller-runtime`. Any logs produced by `controller-runtime` code will be through your logger, and therefore have the same formatting and destination.

### Setting flags when running locally

When running locally with `make run ENABLE_WEBHOOKS=false`, you can use the `ARGS` var to pass additional flags to your operator, including the zap flags. For example:

```console
$ make run ARGS="--zap-encoder=console" ENABLE_WEBHOOKS=false
```

Make sure to have your `run` target to take `ARGS` as shown below in `Makefile`.

```makefile
# Run against the configured Kubernetes cluster in ~/.kube/config
run: manifests generate fmt vet
	go run ./main.go $(ARGS)
```

### Setting flags when deploying to a cluster

When deploying your operator to a cluster you can set additional flags using an `args` array in your operator’s `container` spec in the file `config/default/manager_metrics_patch.yaml` For example:

```yaml
- op: add
  path: /spec/template/spec/containers/0/args/0
  value: --zap-log-level=debug 
- op: add
  path: /spec/template/spec/containers/0/args/0
  value: --zap-encoder=console
```

Creating a structured log statement
-----------------------------------

There are two ways to create structured logs with `logr`. You can create new loggers using `log.WithValues(keyValues)` that include `keyValues`, a list of key-value pair `interface{}`'s, in each log record. Alternatively you can include `keyValues` directly in a log statement, as all `logr` log statements take some message and `keyValues`. The signature of `logr.Error()` has an `error`-type parameter, which can be `nil`.

An example from [`memcached_controller.go`](https://github.com/operator-framework/operator-sdk/blob/v1.2.0/testdata/go/memcached-operator/controllers/memcached_controller.go):

```Go
package memcached

import (
  ctrllog "sigs.k8s.io/controller-runtime/pkg/log"
)

// MemcachedReconciler reconciles a Memcached object
type MemcachedReconciler struct {
	client.Client
	Log    logr.Logger
	Scheme *runtime.Scheme
}

func (r *MemcachedReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
	log := ctrllog.FromContext(ctx)

	// Fetch the Memcached instance
	memcached := &cachev1alpha1.Memcached{}
	err := r.Get(ctx, req.NamespacedName, memcached)
	if err != nil {
		if errors.IsNotFound(err) {
			// Request object not found, could have been deleted after reconcile request.
			// Owned objects are automatically garbage collected. For additional cleanup logic use finalizers.
			// Return and don't requeue
			log.Info("Memcached resource not found. Ignoring since object must be deleted")
			return ctrl.Result{}, nil
		}
		// Error reading the object - requeue the request.
		log.Error(err, "Failed to get Memcached")
		return ctrl.Result{}, err
	}

	// Check if the deployment already exists, if not create a new one
	found := &appsv1.Deployment{}
	err = r.Get(ctx, types.NamespacedName{Name: memcached.Name, Namespace: memcached.Namespace}, found)
	if err != nil && errors.IsNotFound(err) {
		// Define a new deployment
		dep := r.deploymentForMemcached(memcached)
		log.Info("Creating a new Deployment", "Deployment.Namespace", dep.Namespace, "Deployment.Name", dep.Name)
		err = r.Create(ctx, dep)
		if err != nil {
			log.Error(err, "Failed to create new Deployment", "Deployment.Namespace", dep.Namespace, "Deployment.Name", dep.Name)
			return ctrl.Result{}, err
		}
		// Deployment created successfully - return and requeue
		return ctrl.Result{Requeue: true}, nil
	} else if err != nil {
		log.Error(err, "Failed to get Deployment")
		return ctrl.Result{}, err
	}

	...
}
```

Log records will look like the following (from `log.Error()` above):

```
2020-04-27T09:14:15.939-0400	ERROR	controllers.Memcached	Failed to create new Deployment	{"memcached": "default/memcached-sample", "Deployment.Namespace": "default", "Deployment.Name": "memcached-sample"}
```

Non-default logging
-------------------

If you do not want to use `logr` as your logging tool, you can remove `logr`-specific statements without issue from your operator’s code, including the `logr` setup code in `main.go`, and add your own. Note that removing `logr` setup code will prevent `controller-runtime` from logging.

Last modified November 19, 2024: [removing kube-rbac-proxy from website docs (#6864) (b049c1ca)](https://github.com/operator-framework/operator-sdk/commit/b049c1ca371c76da6ed6a9e903b7975cf9f5229d)

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
