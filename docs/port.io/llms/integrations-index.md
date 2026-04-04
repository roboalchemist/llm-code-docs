# Source: https://docs.port.io/integrations-index.md

# Integrations index

This page contains a list of Port's available integrations, organized by the platform/product.

## AI Agents[â](#ai-agents "Direct link to AI Agents")

### GitHub Copilot[â](#github-copilot "Direct link to GitHub Copilot")

* [Ingest Copilot usage metrics into your catalog](/build-your-software-catalog/sync-data-to-catalog/ai-agents/github-copilot/.md)

## ArgoCD[â](#argocd "Direct link to ArgoCD")

* [ArgoCD exporter and webhook integration](/build-your-software-catalog/sync-data-to-catalog/argocd/.md)
* [ArgoCD events](/build-your-software-catalog/sync-data-to-catalog/argocd/.md#argocd-events)
* [Rollback ArgoCD deployment](/guides/all/rollback-argocd-deployment.md)
* [Self-service action to synchronize ArgoCD application](/guides/all/sync-argocd-app.md)

## Checkmarx[â](#checkmarx "Direct link to Checkmarx")

* [Ingest Checkmarx KICS scan into your catalog](/guides/all/ingest-checkmarx-kics-scan-into-your-catalog.md)

## CircleCI[â](#circleci "Direct link to CircleCI")

* [Sync CircleCI workflows](/build-your-software-catalog/custom-integration/api/ci-cd/circleci-workflow/.md)
* [CircleCI actions](/actions-and-automations/setup-backend/webhook/circle-ci/.md)

## Cloud providers[â](#cloud-providers "Direct link to Cloud providers")

### AWS[â](#aws "Direct link to AWS")

* [AWS integration](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/.md)
* [Map AWS Resources to your integration](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/examples/.md)
* [Deploy AWS resources using AWS CloudFormation](/guides/all/deploy-cloudformation-template.md)
* [Terraform manage S3 buckets lifecycle](/guides/all/s3-bucket.md)
* [Terraform manage developer environment](/guides/all/create-dev-env.md)
* [Connect ECR repository to Service](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/aws-exporter/examples/connect-ecr-repo-to-service-using-tags.md)
* [Script to ingest ECR Images and Repositories](https://github.com/port-labs/example-ecr-images)
* [Self-service action to create EC2 instance](/guides/all/create-an-ec2-instance.md)
* [Provision AWS cloud resource using Terraform Plan and Apply](/guides/all/terraform-plan-and-apply-aws-resource.md)
* [Add tags to ECR repository](/guides/all/add-tags-to-ecr-repository.md)
* [Generate ECR image with tags](/guides/all/push-image-to-ecr.md)

### Azure[â](#azure "Direct link to Azure")

* [Azure exporter](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/.md)
* [Azure Active Directory (AD) SSO](/sso-rbac/self-serve-sso.md)
* [Map resource groups, storage groups, compute resources database resources and more](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates/.md)
* [Add tags to Azure resources](/guides/all/tag-azure-resource.md)

### GCP[â](#gcp "Direct link to GCP")

* [GCP integration](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/gcp/.md)
* [Sync Projects, buckets, service accounts, compute instances and more](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/gcp/examples/mapping_extra_resources.md)

#### Google cloud build[â](#google-cloud-build "Direct link to Google cloud build")

* [Cloud build self-service action](/actions-and-automations/setup-backend/webhook/cloudbuild-pipeline/.md)

## CodeFresh[â](#codefresh "Direct link to CodeFresh")

* [CodeFresh workflow template](/build-your-software-catalog/custom-integration/api/ci-cd/codefresh-workflow-template/.md)

## Codecov[â](#codecov "Direct link to Codecov")

* [Codecov coverage script and webhook](/build-your-software-catalog/custom-integration/webhook/examples/codecov.md)

## Cookiecutter[â](#cookiecutter "Direct link to Cookiecutter")

* [Cookiecutter GitHub scaffolder using GitHub workflows](/guides/all/scaffold-a-new-service.md?git-provider=github)
* [Cookiecutter GitHub scaffolder using Jenkins pipelines](/guides/all/scaffold-github-using-cookiecutter.md)
* [Cookiecutter GitHub scaffolder using FastAPI backend](/actions-and-automations/setup-backend/webhook/examples/software-templates.md)
* [Cookiecutter GitLab scaffolder using GitLab pipelines](/guides/all/scaffold-a-new-service.md?git-provider=gitlab)
* [Cookiecutter Bitbucket scaffolder using Jenkins pipelines](/guides/all/scaffold-bitbucket-using-cookiecutter.md)
* [Cookiecutter Azure DevOps scaffolder using Azure DevOps pipelines](/guides/all/scaffold-repositories-using-cookiecutter.md)

## Datadog[â](#datadog "Direct link to Datadog")

* [Datadog integration](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/datadog/.md)
* [Embed dashboards from Datadog](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/.md#datadog-dashboard)
* [Self-service action to trigger Datadog incident](/guides/all/trigger-datadog-incident.md)

## Dynatrace[â](#dynatrace "Direct link to Dynatrace")

* [Dynatrace integration](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/dynatrace/.md)

## FireHydrant[â](#firehydrant "Direct link to FireHydrant")

* [FireHydrant integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/firehydrant.md)
* [Self-service actions to create or trigger a FireHydrant incident](/guides/all/manage-firehydrant-incidents.md)

## Git[â](#git "Direct link to Git")

### Azure DevOps[â](#azure-devops "Direct link to Azure DevOps")

* [Sync Azure pipelines](/build-your-software-catalog/custom-integration/api/ci-cd/azure-pipelines/.md)
* [Azure pipelines self-service actions](/actions-and-automations/setup-backend/azure-pipeline/.md)
* [Cookiecutter Azure DevOps scaffolder using Azure DevOps pipelines](/guides/all/scaffold-repositories-using-cookiecutter.md)

### Bitbucket[â](#bitbucket "Direct link to Bitbucket")

* [Bitbucket App (Deprecated)](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/.md)

  * [GitOps](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/gitops/.md)
  * [Sync repositories, file contents, pull-requests, monorepos and more](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/examples.md)

* [Bitbucket Cloud](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-cloud/.md)

  * [GitOps](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-cloud/gitops/.md)
  * [Sync repositories, file contents, pull-requests, monorepos and more](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-cloud/examples.md)

* [Bitbucket scaffolder](/guides/all/scaffold-bitbucket-using-cookiecutter.md)

* [Bitbucket Server Integration](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-server/.md)

* [Bitbucket Server GitOps with webhooks](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-server/gitops.md)

### GitHub[â](#github "Direct link to GitHub")

* [GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md)
* [GitHub self-hosted app](/build-your-software-catalog/sync-data-to-catalog/git/github/self-hosted-installation.md)
* [GitHub GitOps](/build-your-software-catalog/sync-data-to-catalog/git/github/gitops/.md)
* [GitHub action for GitHub workflow](/build-your-software-catalog/custom-integration/api/ci-cd/github-workflow/.md)
* [GitHub workflow self-service actions](/actions-and-automations/setup-backend/github-workflow/.md)
* [Sync repositories, file contents, pull-requests, workflows, teams and more](/build-your-software-catalog/sync-data-to-catalog/git/github/examples/.md)
* [Sync Dependabot](/build-your-software-catalog/sync-data-to-catalog/git/github/examples/.md#mapping-repositories-and-dependabot-alerts)
* [GitHub scaffolder using GitHub workflows](/guides/all/scaffold-a-new-service.md?git-provider=github)
* [GitHub scaffolder using Jenkins pipelines](/guides/all/scaffold-github-using-cookiecutter.md)
* [GitHub scaffolder using FastAPI backend](/actions-and-automations/setup-backend/webhook/examples/software-templates.md)
* [Deploy AWS resources using AWS CloudFormation](/guides/all/deploy-cloudformation-template.md)
* [Deploy Azure resources using Terraform](/guides/all/create-azure-resource.md)
* [Create GitHub secret using GitHub workflows](/guides/all/create-github-secret.md)
* [Script to ingest GitHub packages](https://github.com/port-labs/example-github-packages)
* [Lock service deployment](/guides/all/lock-and-unlock-services-in-port.md)
* [Nudge PR reviewers](/guides/all/nudge-pr-reviewers.md)
* [Promote to production](/guides/all/promote-to-production.md)
* [Self-service action to lock and unlock a service](/guides/all/lock-and-unlock-services-in-port.md)
* [Connect GitHub Codeowners with Service, Team and User](/guides/all/connect-github-codeowners-with-service-team-and-user.md)
* [Ingest Javascript packages into your catalog using GitHub file ingesting feature](/guides/all/ingest-javascript-packages-into-your-catalog.md)

### GitLab[â](#gitlab "Direct link to GitLab")

* [GitLab app](/build-your-software-catalog/sync-data-to-catalog/git/gitlab/.md)
* [GitLab GitOps](/build-your-software-catalog/sync-data-to-catalog/git/gitlab/gitops/.md)
* [GitLab advanced file search and search checks](/build-your-software-catalog/sync-data-to-catalog/git/gitlab/mapping_extensions.md)
* [Sync GitLab pipelines](/build-your-software-catalog/custom-integration/api/ci-cd/gitlab-pipelines/.md)
* [GitLab pipeline self-service actions](/actions-and-automations/setup-backend/gitlab-pipeline/.md)
* [GitLab scaffolder](/guides/all/scaffold-a-new-service.md?git-provider=gitlab)
* [Sync projects, file contents, merge-requests and more](/build-your-software-catalog/sync-data-to-catalog/git/gitlab/examples.md)

### GitOps using Port CRDs[â](#gitops-using-port-crds "Direct link to GitOps using Port CRDs")

* [Mapping resources using Port CRDs](/build-your-software-catalog/sync-data-to-catalog/git/gitops-using-port-crd.md)

## Grafana[â](#grafana "Direct link to Grafana")

* [Embed dashboards from Grafana](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/authentication.md#examples)
* [Grafana webhook](/build-your-software-catalog/custom-integration/webhook/examples/grafana.md)

## Incident IO[â](#incident-io "Direct link to Incident IO")

* [Sync Port Services to Incident IO](/guides/all/sync-service-entities-to-incident-io.md)

## Infrastructure as Code (IaC)[â](#infrastructure-as-code-iac "Direct link to Infrastructure as Code (IaC)")

### Pulumi[â](#pulumi "Direct link to Pulumi")

* [Pulumi provider](/build-your-software-catalog/custom-integration/iac/pulumi/.md)
* [Pulumi managed blueprint](/build-your-software-catalog/customize-integrations/configure-data-model/Iac/pulumi-managed-blueprint.md)

### Terraform[â](#terraform "Direct link to Terraform")

* [Terraform provider](/build-your-software-catalog/custom-integration/iac/terraform/.md)
* [Terraform managed blueprint](/build-your-software-catalog/customize-integrations/configure-data-model/Iac/terraform-managed-blueprint.md)
* [Create cloud resources using IaC](/guides/all/create-cloud-resource-using-iac.md)
* [Terraform manage S3 buckets lifecycle](/guides/all/s3-bucket.md)
* [Terraform manage developer environment](/guides/all/create-dev-env.md)
* [Terraform no-code resource provisioning using self-service actions](/actions-and-automations/setup-backend/webhook/examples/terraform-no-code-resource-provisioning.md)
* [Import Terraform state using webhook](/build-your-software-catalog/custom-integration/webhook/examples/packages/terraform.md)

### Terraform Cloud[â](#terraform-cloud "Direct link to Terraform Cloud")

* [Terraform cloud](/build-your-software-catalog/sync-data-to-catalog/terraform-cloud/.md)
* [Terraform cloud actions](/actions-and-automations/setup-backend/webhook/terraform-cloud/.md)

## Jenkins[â](#jenkins "Direct link to Jenkins")

* [Jenkins Integration](/build-your-software-catalog/sync-data-to-catalog/cicd/jenkins/.md)
* [Sync Jenkins pipelines via API](/build-your-software-catalog/custom-integration/api/ci-cd/jenkins-deployment/.md)
* [Jenkins pipeline self-service actions](/actions-and-automations/setup-backend/jenkins-pipeline/.md)
* [GitHub scaffolder using Jenkins](/guides/all/scaffold-github-using-cookiecutter.md)
* [Bitbucket scaffolder using Jenkins](/guides/all/scaffold-bitbucket-using-cookiecutter.md)
* [Create Github pull request](/guides/all/create-github-pull-request.md)

## JFrog[â](#jfrog "Direct link to JFrog")

* [Sync JFrog Artifacts, Docker tags, and build entities](/build-your-software-catalog/custom-integration/webhook/examples/jfrog.md)
* [Script to ingest JFrog X-ray alerts, repositories and artifacts](https://github.com/port-labs/example-jfrog-xray-alerts)
* [Script to ingest JFrog container image builds and repositories](https://github.com/port-labs/example-jfrog-container-images)

## Jira[â](#jira "Direct link to Jira")

* [Jira integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md)
* [Jira Server integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira-server/.md)
* [Jira webhook](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md#alternative-installation-via-webhook)
* [Jira Server webhook](/build-your-software-catalog/sync-data-to-catalog/project-management/jira-server/.md#alternative-option---using-the-webhook-integration)
* [Initiate scorecards handling with Jira issues](/scorecards/manage-using-3rd-party-apps/jira.md)

## Kafka[â](#kafka "Direct link to Kafka")

* [Kafka integration](/build-your-software-catalog/sync-data-to-catalog/event-processing/kafka.md)
* [Kafka queue for self-service actions](/actions-and-automations/setup-backend/kafka/.md)

## Kratix (by Syntasso)[â](#kratix-by-syntasso "Direct link to Kratix (by Syntasso)")

* [Combine Kratix and Port](https://www.syntasso.io/solutions/port-and-kratix)
* [Combine Kratix and Port (demo video)](https://www.youtube.com/watch?v=7nKx4CnEvoY)

## KubeCost[â](#kubecost "Direct link to KubeCost")

* [KubeCost integration](/build-your-software-catalog/sync-data-to-catalog/cloud-cost/kubecost/.md)

## Kubernetes[â](#kubernetes "Direct link to Kubernetes")

* [K8s exporter](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/.md)
* [Map Istio](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/istio.md)
* [Map Knative](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/knative.md)
* [Map Red Hat Openshift](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/openshift.md)
* [Map Trivy](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/trivy.md)
* [Ingest Trivy vulnerabilities into your catalog using GitHub file ingesting feature](/guides/all/ingest-trivy-vulnerabilities-into-your-catalog.md)
* [Map Kyverno](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/kyverno.md)
* [Map FluxCD](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/fluxcd.md)
* [Map CRDs](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/custom-crds.md)
* [Port entity CRD](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/port-crd.md)
* [Create and managed Kubernetes cluster](/guides/all/manage-clusters.md)
* [Change deployment replica count](/guides/all/change-replica-count.md)

## LeanIX[â](#leanix "Direct link to LeanIX")

* [Script that synchronizes data from LeanIX into Port](https://github.com/port-labs/LeanIX-Sync)

## Linear[â](#linear "Direct link to Linear")

* [Linear integration](/build-your-software-catalog/sync-data-to-catalog/project-management/linear/.md)
* [Linear webhook](/build-your-software-catalog/sync-data-to-catalog/project-management/linear/.md#alternative-installation-via-webhook)

## New Relic[â](#new-relic "Direct link to New Relic")

* [New Relic integration](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/newrelic/.md)
* [Embed dashboards from New Relic](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/.md#new-relic-chart)

## Octopus Deploy[â](#octopus-deploy "Direct link to Octopus Deploy")

* [Octopus Deploy integration](/build-your-software-catalog/sync-data-to-catalog/cicd/octopus-deploy/.md)

## OpenCost[â](#opencost "Direct link to OpenCost")

* [OpenCost integration](/build-your-software-catalog/sync-data-to-catalog/cloud-cost/opencost.md)

## OpsGenie[â](#opsgenie "Direct link to OpsGenie")

* [OpsGenie integration and webhook](/build-your-software-catalog/sync-data-to-catalog/incident-management/opsgenie/.md)
* [Self-service action to trigger an OpsGenie incident](https://docs.port.io/guides/all/create-an-opsgenie-incident)

## PagerDuty[â](#pagerduty "Direct link to PagerDuty")

* [PagerDuty integration and webhook](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md)

* [Ensure production readiness](/guides/all/ensure-production-readiness.md)

* [Self-service action to escalate a PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/escalate-an-incident)

* [Self-service action to trigger a PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/interact-with-pagerduty-incidents)

* [Self-service action to change a PagerDuty incident owner](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-pagerduty-incident-owner)

* [Self-service action to create a PagerDuty service from Port](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/create-pagerduty-service)

* [Self-service action to acknowledge a PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/acknowledge-incident)

* [Self-service action to change a PagerDuty oncall](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-on-call-user)

* [Self-service action to resolve a PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/resolve-incident)

* PagerDuty Incident Management

  <!-- -->

  * [Automation to handle PagerDuty incidents](https://docs.port.io/guides/all/create-slack-channel-for-reported-incident)
  * [Self-service action to resolve Pagerduty incidents](https://docs.port.io/guides-and-tutorials/resolve-pagerduty-incident) - including Slack channel notification and closing GitHub issue.

## Prometheus[â](#prometheus "Direct link to Prometheus")

* [Prometheus webhook](/build-your-software-catalog/custom-integration/webhook/examples/prometheus.md)

## SBOM[â](#sbom "Direct link to SBOM")

* [Ingest software bill of material (SBOM) into your catalog](/guides/all/ingest-software-bill-of-materials-sbom-into-your-catalog.md)

## ServiceNow[â](#servicenow "Direct link to ServiceNow")

* [ServiceNow integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/servicenow.md)
* [Self-service action to trigger ServiceNow incident](/guides/all/trigger-servicenow-incident.md)

## Sentry[â](#sentry "Direct link to Sentry")

* [Sentry integration and webhook](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/sentry/.md)

## Slack[â](#slack "Direct link to Slack")

* [Manual approval for self-service actions](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/.md#slack)
* [Scorecard notifications](/scorecards/manage-using-3rd-party-apps/slack.md)
* [Broadcast message to API consumers](/guides/all/broadcast-api-consumers-message.md)

## Snyk[â](#snyk "Direct link to Snyk")

* [Snyk integration and webhook](/build-your-software-catalog/sync-data-to-catalog/code-quality-security/snyk/.md)

## SonarQube / SonarCloud[â](#sonarqube--sonarcloud "Direct link to SonarQube / SonarCloud")

* [SonarQube/SonarCloud integration](/build-your-software-catalog/sync-data-to-catalog/code-quality-security/sonarqube/.md)
* [SonarCloud webhook](/build-your-software-catalog/sync-data-to-catalog/code-quality-security/sonarqube/.md#alternative-installation-via-webhook)
* [Connect GitHub PR to SonarQube analysis](/guides/all/connect-github-pr-with-sonar-analysis.md)

## Split[â](#split "Direct link to Split")

* [Split webhook](/build-your-software-catalog/custom-integration/webhook/examples/split.md)

## SSO[â](#sso "Direct link to SSO")

* [Manage your SSO connection](/sso-rbac/self-serve-sso.md)

## StackHawk[â](#stackhawk "Direct link to StackHawk")

* [StackHawk webhook](/build-your-software-catalog/custom-integration/webhook/examples/stackhawk.md)

## Statuspage[â](#statuspage "Direct link to Statuspage")

* [Statuspage integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/statuspage/.md)
* [Visualize and manage your Statuspage incidents and components](/guides/all/visualize-and-manage-statuspage-incidents.md)

## Swagger[â](#swagger "Direct link to Swagger")

* [Ingest Swagger paths into your catalog](/guides/all/ingest-swagger-paths-into-your-catalog.md)

## Webhook[â](#webhook "Direct link to Webhook")

* [Create generic webhook for 3rd-party](/build-your-software-catalog/custom-integration/webhook/.md)

## Wiz[â](#wiz "Direct link to Wiz")

* [Wiz integration](/build-your-software-catalog/sync-data-to-catalog/code-quality-security/wiz/.md)
