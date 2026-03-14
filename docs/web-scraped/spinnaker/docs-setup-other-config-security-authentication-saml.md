# Source: https://spinnaker.io/docs/setup/other_config/security/authentication/saml/

Title: SAML 2.0

URL Source: https://spinnaker.io/docs/setup/other_config/security/authentication/saml/

Markdown Content:
SAML 2.0 | Spinnaker
===============

Spinnaker talks from cdCon 2025 now available!

[Browse Playlist](https://www.youtube.com/playlist?list=PL2KXbZ9-EY9Qvfxh3i9YtiGLqNFHId1qM)

[![Image 1: Spinnaker Logo Horizontal](https://spinnaker.io/images/spinnaker-logo-horizontal.png)](https://spinnaker.io/)

*   [Docs](https://spinnaker.io/docs/)
*   [Community](https://spinnaker.io/docs/community/)
*   [Success Stories](https://spinnaker.io/success-stories/)
*   [Blog](https://blog.spinnaker.io/)
*   [Versions](https://spinnaker.io/docs/releases/versions/)
*   [GitHub](https://github.com/spinnaker)

*   [Documentation](https://spinnaker.io/docs/)

    *           *   [Concepts](https://spinnaker.io/docs/concepts/)

        
            *                   *   [Clusters](https://spinnaker.io/docs/concepts/clusters/)

                

                *   [Pipelines](https://spinnaker.io/docs/concepts/pipelines/)

                

                *   [Providers](https://spinnaker.io/docs/concepts/concepts-providers/)

                

                *   [Spinnaker eBook](https://spinnaker.io/docs/concepts/ebook/)

                

        *   [Setup](https://spinnaker.io/docs/setup/)

        
            *   [Quickstart](https://spinnaker.io/docs/setup/quickstart/)
                *   [Install](https://spinnaker.io/docs/setup/install/)

                
                    *   [Install Halyard](https://spinnaker.io/docs/setup/install/halyard/)
                        *   [Choose Cloud Providers](https://spinnaker.io/docs/setup/install/providers/)

                        
                            *                                   *   [AWS](https://spinnaker.io/docs/setup/install/providers/aws/)

                                
                                    *   [Amazon EC2](https://spinnaker.io/docs/setup/install/providers/aws/aws-ec2/)[Amazon ECS](https://spinnaker.io/docs/setup/install/providers/aws/aws-ecs/)[AWS Concepts](https://spinnaker.io/docs/setup/install/providers/aws/aws-concepts/)

                                *   [Kubernetes](https://spinnaker.io/docs/setup/install/providers/kubernetes-v2/)

                                
                                    *   [Alibaba K8s](https://spinnaker.io/docs/setup/install/providers/kubernetes-v2/ack/)[EKS](https://spinnaker.io/docs/setup/install/providers/kubernetes-v2/aws-eks/)[GKE](https://spinnaker.io/docs/setup/install/providers/kubernetes-v2/gke/)[K8s Provider](https://spinnaker.io/docs/setup/install/providers/kubernetes-v2/k8s-provider/)[Oracle K8s](https://spinnaker.io/docs/setup/install/providers/kubernetes-v2/oke/)

[Azure](https://spinnaker.io/docs/setup/install/providers/azure/)[Cloud Foundry](https://spinnaker.io/docs/setup/install/providers/cf/)[DC/OS](https://spinnaker.io/docs/setup/install/providers/dcos/)[Docker Registry](https://spinnaker.io/docs/setup/install/providers/docker-registry/)[Google App Engine](https://spinnaker.io/docs/setup/install/providers/appengine/)[Google Cloud Run](https://spinnaker.io/docs/setup/install/providers/cloudrun/)[Google Compute Engine](https://spinnaker.io/docs/setup/install/providers/gce/)[Oracle](https://spinnaker.io/docs/setup/install/providers/oracle/)

[Choose your Environment](https://spinnaker.io/docs/setup/install/environment/)
                        *   [External Storage](https://spinnaker.io/docs/setup/install/storage/)

                        
                            *   [External Storage Overview](https://spinnaker.io/docs/setup/install/storage/storage-overview/)[Amazon S3](https://spinnaker.io/docs/setup/install/storage/s3/)[Azure Storage](https://spinnaker.io/docs/setup/install/storage/azs/)[Google Cloud Storage](https://spinnaker.io/docs/setup/install/storage/gcs/)[Minio](https://spinnaker.io/docs/setup/install/storage/minio/)[Oracle Object Storage](https://spinnaker.io/docs/setup/install/storage/oracle/)[Redis](https://spinnaker.io/docs/setup/install/storage/redis/)

[Deploy Spinnaker and Connect to the UI](https://spinnaker.io/docs/setup/install/deploy/)[Back Up Your Config](https://spinnaker.io/docs/setup/install/backups/)[Halyard FAQ](https://spinnaker.io/docs/setup/install/faq/)[Configuration](https://spinnaker.io/docs/setup/install/configuration/)[Upgrading](https://spinnaker.io/docs/setup/install/upgrades/)

                *   [Configure Everything Else](https://spinnaker.io/docs/setup/other_config/)

                
                    *                           *   [Server Group Launch Settings](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/)

                        
                            *                                   *   [AWS EC2 Server Group Launch Settings](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/)

                                
                                    *   [AWS EC2 Launch Templates Setup](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates-setup/)[AWS EC2 Launch Templates](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/)

                        *   [Configure Artifacts](https://spinnaker.io/docs/setup/other_config/artifacts/)

                        
                            *   [Configure a Git Repo Artifact Account](https://spinnaker.io/docs/setup/other_config/artifacts/gitrepo/)[Configure a GitHub artifact account](https://spinnaker.io/docs/setup/other_config/artifacts/github/)[Configure a GitLab artifact account](https://spinnaker.io/docs/setup/other_config/artifacts/gitlab/)[Configure Bitbucket Artifact Credentials](https://spinnaker.io/docs/setup/other_config/artifacts/bitbucket/)[Configure Helm Artifact account](https://spinnaker.io/docs/setup/other_config/artifacts/helm/)[Configure HTTP Artifact Credentials](https://spinnaker.io/docs/setup/other_config/artifacts/http/)[Configure Maven Artifact Credentials](https://spinnaker.io/docs/setup/other_config/artifacts/maven/)[Configure S3 Artifact](https://spinnaker.io/docs/setup/other_config/artifacts/s3/)[Configuring GCS Artifact Credentials](https://spinnaker.io/docs/setup/other_config/artifacts/gcs/)[Configuring Oracle Object Storage Artifact Credentials](https://spinnaker.io/docs/setup/other_config/artifacts/oracle/)

                        *   [Bakery](https://spinnaker.io/docs/setup/other_config/bakery/)

                        
                            *   [Google Compute Engine](https://spinnaker.io/docs/setup/other_config/bakery/google/)[Oracle Cloud Infrastructure](https://spinnaker.io/docs/setup/other_config/bakery/oracle/)

                        *   [Security](https://spinnaker.io/docs/setup/other_config/security/)

                        
                            *                                   *   [Authorization (RBAC)](https://spinnaker.io/docs/setup/other_config/security/authorization/)

                                
                                    *   [Google Groups with G Suite](https://spinnaker.io/docs/setup/other_config/security/authorization/google-groups/)[LDAP](https://spinnaker.io/docs/setup/other_config/security/authorization/ldap/)[Pipeline Permissions](https://spinnaker.io/docs/setup/other_config/security/authorization/pipeline-permissions/)[SAML](https://spinnaker.io/docs/setup/other_config/security/authorization/saml/)[Service Accounts](https://spinnaker.io/docs/setup/other_config/security/authorization/service-accounts/)[GitHub Teams](https://spinnaker.io/docs/setup/other_config/security/authorization/github-teams/)

[Administrator functionality](https://spinnaker.io/docs/setup/other_config/security/admin/)
                                *   [Authentication](https://spinnaker.io/docs/setup/other_config/security/authentication/)

                                
                                    *   [LDAP](https://spinnaker.io/docs/setup/other_config/security/authentication/ldap/)
                                        *   [OAuth 2.0](https://spinnaker.io/docs/setup/other_config/security/authentication/oauth/)

                                        
                                            *   [Azure](https://spinnaker.io/docs/setup/other_config/security/authentication/oauth/azure/)[G Suite](https://spinnaker.io/docs/setup/other_config/security/authentication/oauth/google/)[GitHub Organizations](https://spinnaker.io/docs/setup/other_config/security/authentication/oauth/github/)[OAuth 2.0 Configuration](https://spinnaker.io/docs/setup/other_config/security/authentication/oauth/config/)[Oracle Cloud](https://spinnaker.io/docs/setup/other_config/security/authentication/oauth/oracle/)

[SAML 2.0](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/)[X.509 Client Certificates](https://spinnaker.io/docs/setup/other_config/security/authentication/x509/)

[SSL](https://spinnaker.io/docs/setup/other_config/security/ssl/)

                        *   [Set Up Triggers](https://spinnaker.io/docs/setup/other_config/triggers/)

                        
                            *                                   *   [Configuring GitHub Webhooks](https://spinnaker.io/docs/setup/other_config/triggers/github/)

                                

[Amazon AWS Pub/Sub](https://spinnaker.io/docs/setup/other_config/triggers/amazon/)[Google Cloud Pub/Sub](https://spinnaker.io/docs/setup/other_config/triggers/google/)

[Install Spin CLI](https://spinnaker.io/docs/setup/other_config/spin/)
                        *   [CI](https://spinnaker.io/docs/setup/other_config/ci/)

                        
                            *   [AWS CodeBuild](https://spinnaker.io/docs/setup/other_config/ci/codebuild/)[Fiat Permissions](https://spinnaker.io/docs/setup/other_config/ci/fiat_permissions/)[Google Cloud Build](https://spinnaker.io/docs/setup/other_config/ci/gcb/)[Jenkins](https://spinnaker.io/docs/setup/other_config/ci/jenkins/)[Travis CI](https://spinnaker.io/docs/setup/other_config/ci/travis/)[Wercker](https://spinnaker.io/docs/setup/other_config/ci/wercker/)

                        *   [Logging](https://spinnaker.io/docs/setup/other_config/logging/)

                        

                        *   [Monitoring](https://spinnaker.io/docs/setup/other_config/monitoring/)

                        

[Canary](https://spinnaker.io/docs/setup/other_config/canary/)
                        *   [Additional Features](https://spinnaker.io/docs/setup/other_config/features/)

                        
                            *   [Configuring the Script Stage](https://spinnaker.io/docs/setup/other_config/features/script-stage/)[Enable Slack Support Channels](https://spinnaker.io/docs/setup/other_config/features/slack-support/)[Notifications and Events Guide](https://spinnaker.io/docs/setup/other_config/features/notifications/)[User Data Files and Metadata](https://spinnaker.io/docs/setup/other_config/features/user-data/)

[Clouddriver Account Management](https://spinnaker.io/docs/setup/other_config/accounts/)[External Account Configuration](https://spinnaker.io/docs/setup/other_config/configuration/)

                *   [Productionize Spinnaker](https://spinnaker.io/docs/setup/productionize/)

                
                    *                           *   [Configure Caching](https://spinnaker.io/docs/setup/productionize/caching/)

                        
                            *   [Configure Spinnaker's Usage of Redis](https://spinnaker.io/docs/setup/productionize/caching/configure-redis-usage/)[Externalize Redis](https://spinnaker.io/docs/setup/productionize/caching/externalize-redis/)

                        *   [Configure Scaling](https://spinnaker.io/docs/setup/productionize/scaling/)

                        
                            *   [Horizontally Scale Spinnaker Services](https://spinnaker.io/docs/setup/productionize/scaling/horizontal-scaling/)

                        *   [Persistence](https://spinnaker.io/docs/setup/productionize/persistence/)

                        
                            *   [Set up Clouddriver to use SQL](https://spinnaker.io/docs/setup/productionize/persistence/clouddriver-sql/)[Set up Front50 to use SQL](https://spinnaker.io/docs/setup/productionize/persistence/front50-sql/)[Set up Orca to use SQL](https://spinnaker.io/docs/setup/productionize/persistence/orca-sql/)

        *   [Guides](https://spinnaker.io/docs/guides/)

        
            *                   *   [Development Guides](https://spinnaker.io/docs/guides/developer/)

                
                    *                           *   [Extending Spinnaker](https://spinnaker.io/docs/guides/developer/extending/)

                        
                            *   [Integrate your CI](https://spinnaker.io/docs/guides/developer/extending/integrate-your-ci/)[Kubernetes CRD Extensions](https://spinnaker.io/docs/guides/developer/extending/crd-extensions/)[Writing a New Stage](https://spinnaker.io/docs/guides/developer/extending/new-stage/)

                        *   [Plugin Creator Guide](https://spinnaker.io/docs/guides/developer/plugin-creator/)

                        
                            *   [Backend Service Extension Points](https://spinnaker.io/docs/guides/developer/plugin-creator/plugin-backend/)[Frontend Plugin Development](https://spinnaker.io/docs/guides/developer/plugin-creator/plugin-frontend/)[Plugin Compatibility Testing](https://spinnaker.io/docs/guides/developer/plugin-creator/testing/compatibility-testing/)[Plugin Project Configuration](https://spinnaker.io/docs/guides/developer/plugin-creator/project-config/)[Test a Pipeline Stage Plugin](https://spinnaker.io/docs/guides/developer/plugin-creator/testing/plugin-deck-test/)

                *   [Operator Guides](https://spinnaker.io/docs/guides/operator/)

                
                    *   [Custom CAs for Webhooks](https://spinnaker.io/docs/guides/operator/webhook-custom-trust-store/)[Custom Job Stages](https://spinnaker.io/docs/guides/operator/custom-job-stages/)[Custom Webhook Stages](https://spinnaker.io/docs/guides/operator/custom-webhook-stages/)[Deploy Custom Spinnaker Builds](https://spinnaker.io/docs/guides/operator/custom-boms/)[Echo: Cassandra to In-Memory](https://spinnaker.io/docs/guides/operator/echo-cassandra-to-in-memory/)[Front50: Cassandra to Object Store](https://spinnaker.io/docs/guides/operator/front50-cassandra-to-obj-store/)[Front50: Cassandra to Redis](https://spinnaker.io/docs/guides/operator/front50-cassandra-to-redis/)[Hiding Stages](https://spinnaker.io/docs/guides/operator/hiding-stages/)[Orca: Redis to SQL](https://spinnaker.io/docs/guides/operator/orca-redis-to-sql/)

                *   [Runbooks](https://spinnaker.io/docs/guides/runbooks/)

                
                    *   [API Rate Limiting](https://spinnaker.io/docs/guides/runbooks/api-rate-limiting/)[Caching: Account Name Based Sharding](https://spinnaker.io/docs/guides/runbooks/caching-account-name-based-sharding/)[Orca: QoS](https://spinnaker.io/docs/guides/runbooks/orca-quality-of-service/)[Orca: Zombie Executions](https://spinnaker.io/docs/guides/runbooks/orca-zombie-executions/)[Sharding Spinnaker](https://spinnaker.io/docs/guides/runbooks/sharding-spinnaker/)

                *   [spin CLI Guide](https://spinnaker.io/docs/guides/spin/)

                
                    *   [Manage Apps](https://spinnaker.io/docs/guides/spin/app/)[Manage Canary](https://spinnaker.io/docs/guides/spin/canary-configs/)[Manage Pipeline Templates](https://spinnaker.io/docs/guides/spin/pipeline-templates/)[Manage Pipelines](https://spinnaker.io/docs/guides/spin/pipeline/)

                *   [Tutorials](https://spinnaker.io/docs/guides/tutorials/)

                
                    *                           *   [Codelabs](https://spinnaker.io/docs/guides/tutorials/codelabs/)

                        
                            *   [Online Codelabs](https://spinnaker.io/docs/guides/tutorials/codelabs/web-labs/)[App Engine: Source to Prod](https://spinnaker.io/docs/guides/tutorials/codelabs/appengine-source-to-prod/)[Azure VM Scale Sets: Source to Prod](https://spinnaker.io/docs/guides/tutorials/codelabs/azure-vmss-source-to-prod/)[Bake and Deploy Pipeline](https://spinnaker.io/docs/guides/tutorials/codelabs/bake-and-deploy-pipeline/)[CD to K8s on Oracle](https://spinnaker.io/docs/guides/tutorials/codelabs/oracle-kubernetes-source-to-prod/)[Continuous Delivery to Kubernetes on Azure](https://spinnaker.io/docs/guides/tutorials/codelabs/azure-kubernetes-source-to-prod/)[DC/OS: Source to Prod](https://spinnaker.io/docs/guides/tutorials/codelabs/dcos-source-to-prod/)[Deploy Artifacts from Artifactory to CF](https://spinnaker.io/docs/guides/tutorials/codelabs/artifactory-to-cf/)[Deploy GCS Pub/Sub Artifacts to App Engine](https://spinnaker.io/docs/guides/tutorials/codelabs/pubsub-to-appengine/)[Deploy GCS Pub/Sub Artifacts to CF](https://spinnaker.io/docs/guides/tutorials/codelabs/pubsub-to-cf/)[GCE Source To Prod](https://spinnaker.io/docs/guides/tutorials/codelabs/gce-source-to-prod/)[Intro: Hello Deployment](https://spinnaker.io/docs/guides/tutorials/codelabs/hello-deployment/)[K8s Source to Prod](https://spinnaker.io/docs/guides/tutorials/codelabs/kubernetes-v2-source-to-prod/)[OCI Source to Prod](https://spinnaker.io/docs/guides/tutorials/codelabs/oci-source-to-prod/)[Safe Deployments](https://spinnaker.io/docs/guides/tutorials/codelabs/safe-deployments/)

[Videos](https://spinnaker.io/docs/guides/tutorials/videos/)

                *   [User Guides](https://spinnaker.io/docs/guides/user/)

                
                    *   [Get Started](https://spinnaker.io/docs/guides/user/get-started/)
                        *   [Application User Guide](https://spinnaker.io/docs/guides/user/applications/)

                        
                            *   [Configure an application](https://spinnaker.io/docs/guides/user/applications/configure/)[Create an application](https://spinnaker.io/docs/guides/user/applications/create/)[Delete an application](https://spinnaker.io/docs/guides/user/applications/delete/)

                        *   [Canary Analysis](https://spinnaker.io/docs/guides/user/canary/)

                        
                            *   [Canary Overview](https://spinnaker.io/docs/guides/user/canary/canary-overview/)
                                *   [Best practices](https://spinnaker.io/docs/guides/user/canary/best-practices/)

                                

                                *   [Canary judgment](https://spinnaker.io/docs/guides/user/canary/judge/)

                                

                                *   [Config](https://spinnaker.io/docs/guides/user/canary/config/)

                                
                                    *   [Configure a canary](https://spinnaker.io/docs/guides/user/canary/config/canary-config/)[Filter templates](https://spinnaker.io/docs/guides/user/canary/config/filter-templates/)

                                *   [Canary stage](https://spinnaker.io/docs/guides/user/canary/stage/)

                                

                        *   [General Purpose Tagging Guide](https://spinnaker.io/docs/guides/user/tagging/)

                        

                        *   [Instance Links](https://spinnaker.io/docs/guides/user/instance-links/)

                        

                        *   [Kubernetes](https://spinnaker.io/docs/guides/user/kubernetes-v2/)

                        
                            *   [Annotation-Driven UI](https://spinnaker.io/docs/guides/user/kubernetes-v2/annotations-ui/)[Automated Rollbacks](https://spinnaker.io/docs/guides/user/kubernetes-v2/automated-rollbacks/)[Best Practices](https://spinnaker.io/docs/guides/user/kubernetes-v2/best-practices/)[Deploy Helm Charts](https://spinnaker.io/docs/guides/user/kubernetes-v2/deploy-helm/)[Deploy Kubernetes Manifests](https://spinnaker.io/docs/guides/user/kubernetes-v2/deploy-manifest/)[Manage Traffic](https://spinnaker.io/docs/guides/user/kubernetes-v2/traffic-management/)[Parameterize Kubernetes Manifests](https://spinnaker.io/docs/guides/user/kubernetes-v2/parameterize-manifests/)[Patch Kubernetes Manifests](https://spinnaker.io/docs/guides/user/kubernetes-v2/patch-manifest/)[Rollout Strategies](https://spinnaker.io/docs/guides/user/kubernetes-v2/rollout-strategies/)[Run Job (Manifest)](https://spinnaker.io/docs/guides/user/kubernetes-v2/run-job-manifest/)[Use Kustomize for Manifests](https://spinnaker.io/docs/guides/user/kubernetes-v2/kustomize-manifests/)

                        *   [Managed Delivery](https://spinnaker.io/docs/guides/user/managed-delivery/)

                        
                            *   [Overview](https://spinnaker.io/docs/guides/user/managed-delivery/managed-delivery-overview/)[Getting Started](https://spinnaker.io/docs/guides/user/managed-delivery/getting-started/)[API](https://spinnaker.io/docs/guides/user/managed-delivery/api/)[Artifacts](https://spinnaker.io/docs/guides/user/managed-delivery/artifacts/)[Delivery Configs](https://spinnaker.io/docs/guides/user/managed-delivery/delivery-configs/)[Env Constraints](https://spinnaker.io/docs/guides/user/managed-delivery/environment-constraints/)[Git-Based Workflows](https://spinnaker.io/docs/guides/user/managed-delivery/git-based-workflows/)[Mark an Artifact as Bad](https://spinnaker.io/docs/guides/user/managed-delivery/marking-as-bad/)[Pin an Environment](https://spinnaker.io/docs/guides/user/managed-delivery/pinning/)[Resource Status](https://spinnaker.io/docs/guides/user/managed-delivery/resource-status/)[FAQ](https://spinnaker.io/docs/guides/user/managed-delivery/faq/)[CI Features](https://spinnaker.io/docs/guides/user/managed-delivery/ci-features/)

                        *   [Pipeline User Guide](https://spinnaker.io/docs/guides/user/pipeline/)

                        
                            *                                   *   [Managing Pipelines](https://spinnaker.io/docs/guides/user/pipeline/managing-pipelines/)

                                

                                *   [Pipeline Expressions Guide](https://spinnaker.io/docs/guides/user/pipeline/expressions/)

                                

                                *   [Using Pipeline Templates](https://spinnaker.io/docs/guides/user/pipeline/pipeline-templates/)

                                
                                    *   [Enable Pipeline Templates](https://spinnaker.io/docs/guides/user/pipeline/pipeline-templates/enable/)[Create a Pipeline Template](https://spinnaker.io/docs/guides/user/pipeline/pipeline-templates/create/)[Inherit from a Template](https://spinnaker.io/docs/guides/user/pipeline/pipeline-templates/override/)[Create a Pipeline from a Template](https://spinnaker.io/docs/guides/user/pipeline/pipeline-templates/instantiate/)[Visualize a Hydrated Pipeline](https://spinnaker.io/docs/guides/user/pipeline/pipeline-templates/plan/)

                                *   [Triggers Overview](https://spinnaker.io/docs/guides/user/pipeline/triggers/)

                                
                                    *   [Bitbucket](https://spinnaker.io/docs/guides/user/pipeline/triggers/bitbucket-events/)
                                        *   [CDEvents](https://spinnaker.io/docs/guides/user/pipeline/triggers/cdevents/)

                                        

                                        *   [GCS](https://spinnaker.io/docs/guides/user/pipeline/triggers/gcs/)

                                        

                                        *   [GitHub](https://spinnaker.io/docs/guides/user/pipeline/triggers/github/)

                                        

                                        *   [Jenkins](https://spinnaker.io/docs/guides/user/pipeline/triggers/jenkins/)

                                        

                                        *   [JFrog Artifactory](https://spinnaker.io/docs/guides/user/pipeline/triggers/artifactory/)

                                        

                                        *   [Pub/Sub Messages](https://spinnaker.io/docs/guides/user/pipeline/triggers/pubsub/)

                                        

                                        *   [Webhooks](https://spinnaker.io/docs/guides/user/pipeline/triggers/webhooks/)

                                        

                                *   [Search for Triggered Pipeline Executions](https://spinnaker.io/docs/guides/user/pipeline/searching/)

                                

                        *   [Plugin User Guide](https://spinnaker.io/docs/guides/user/plugins-users/)

                        
                            *   [Plugin Deployment Example](https://spinnaker.io/docs/guides/user/plugins-users/plugin-deploy-example/)

        *   [Reference](https://spinnaker.io/docs/reference/)

        
            *                   *   [Architecture](https://spinnaker.io/docs/reference/architecture/)

                
                    *   [Overview](https://spinnaker.io/docs/reference/architecture/microservices-overview/)
                        *   [Authentication & Authorization](https://spinnaker.io/docs/reference/architecture/authz_authn/)

                        
                            *   [Authentication Architecture](https://spinnaker.io/docs/reference/architecture/authz_authn/authentication/)[Authorization Architecture](https://spinnaker.io/docs/reference/architecture/authz_authn/authorization/)

[Life of a Bake](https://spinnaker.io/docs/reference/architecture/loab/)[Life of a Deployment](https://spinnaker.io/docs/reference/architecture/load/)

                *   [API](https://spinnaker.io/docs/reference/api/)

                
                    *                           *   [Service APIs](https://spinnaker.io/docs/reference/api/service-plugin-apis/)

                        
                            *                                   *   [Orca](https://spinnaker.io/docs/reference/api/service-plugin-apis/orca-api/)

                                

[Swagger UI](https://spinnaker.io/docs/reference/api/swagger-ui/)

                *   [Halyard](https://spinnaker.io/docs/reference/halyard/)

                
                    *   [Commands](https://spinnaker.io/docs/reference/halyard/commands/)[Component Sizing](https://spinnaker.io/docs/reference/halyard/component-sizing/)[Custom Settings](https://spinnaker.io/docs/reference/halyard/custom/)[High Availability](https://spinnaker.io/docs/reference/halyard/high-availability/)
                        *   [Secrets](https://spinnaker.io/docs/reference/halyard/secrets/)

                        
                            *   [Secrets in GCS](https://spinnaker.io/docs/reference/halyard/secrets/gcs-secrets/)[Secrets in Google Secret Manager](https://spinnaker.io/docs/reference/halyard/secrets/secret-manager-secrets/)[Secrets in S3](https://spinnaker.io/docs/reference/halyard/secrets/s3-secrets/)

[Monitoring](https://spinnaker.io/docs/reference/monitoring/)
                *   [Providers](https://spinnaker.io/docs/reference/providers/)

                
                    *   [Amazon ECS](https://spinnaker.io/docs/reference/providers/ecs/)[Amazon Web Services](https://spinnaker.io/docs/reference/providers/aws/)[Azure](https://spinnaker.io/docs/reference/providers/azure/)[Cloud Foundry](https://spinnaker.io/docs/reference/providers/cf/)[Google App Engine](https://spinnaker.io/docs/reference/providers/appengine/)[Google Cloud Run](https://spinnaker.io/docs/reference/providers/cloudrun/)[Google Compute Engine](https://spinnaker.io/docs/reference/providers/gce/)[Kubernetes (Legacy)](https://spinnaker.io/docs/reference/providers/kubernetes/)[Kubernetes Provider](https://spinnaker.io/docs/reference/providers/kubernetes-v2/)[Oracle Cloud](https://spinnaker.io/docs/reference/providers/oracle/)

                *   [Spinnaker Artifacts](https://spinnaker.io/docs/reference/ref-artifacts/)

                
                    *   [Artifacts from Build Triggers](https://spinnaker.io/docs/reference/ref-artifacts/from-build-triggers/)[Artifacts In App Engine](https://spinnaker.io/docs/reference/ref-artifacts/in-appengine/)[Artifacts In Cloud Foundry](https://spinnaker.io/docs/reference/ref-artifacts/in-cloud-foundry/)[Artifacts In Kubernetes](https://spinnaker.io/docs/reference/ref-artifacts/in-kubernetes-v2/)
                        *   [In Pipelines](https://spinnaker.io/docs/reference/ref-artifacts/in-pipelines/)

                        

                        *   [Types of Artifacts](https://spinnaker.io/docs/reference/ref-artifacts/types/)

                        
                            *   [Bitbucket File](https://spinnaker.io/docs/reference/ref-artifacts/types/bitbucket-file/)[Debian Package](https://spinnaker.io/docs/reference/ref-artifacts/types/debian-package/)[Docker Image](https://spinnaker.io/docs/reference/ref-artifacts/types/docker-image/)[Embedded Base64](https://spinnaker.io/docs/reference/ref-artifacts/types/embedded-base64/)[GCS Object](https://spinnaker.io/docs/reference/ref-artifacts/types/gcs-object/)[Git Repo](https://spinnaker.io/docs/reference/ref-artifacts/types/git-repo/)[GitHub File](https://spinnaker.io/docs/reference/ref-artifacts/types/github-file/)[GitLab File](https://spinnaker.io/docs/reference/ref-artifacts/types/gitlab-file/)[HTTP File](https://spinnaker.io/docs/reference/ref-artifacts/types/http-file/)[Kubernetes Object](https://spinnaker.io/docs/reference/ref-artifacts/types/kubernetes-object/)[Maven Artifact](https://spinnaker.io/docs/reference/ref-artifacts/types/maven-artifact/)[Oracle Object](https://spinnaker.io/docs/reference/ref-artifacts/types/oracle-object/)[S3 Object](https://spinnaker.io/docs/reference/ref-artifacts/types/s3-object/)

                *   [Spinnaker Artifacts - Legacy UI](https://spinnaker.io/docs/reference/artifacts-legacy/)

                
                    *   [Artifacts from Build Triggers](https://spinnaker.io/docs/reference/artifacts-legacy/from-build-triggers/)[Artifacts In App Engine (Legacy)](https://spinnaker.io/docs/reference/artifacts-legacy/in-appengine/)[Artifacts In Kubernetes (Legacy)](https://spinnaker.io/docs/reference/artifacts-legacy/in-kubernetes-v2/)[Artifacts In Pipelines (Legacy)](https://spinnaker.io/docs/reference/artifacts-legacy/in-pipelines/)
                        *   [Types of Artifacts](https://spinnaker.io/docs/reference/artifacts-legacy/types/)

                        
                            *   [Bitbucket File](https://spinnaker.io/docs/reference/artifacts-legacy/types/bitbucket-file/)[Docker Image](https://spinnaker.io/docs/reference/artifacts-legacy/types/docker-image/)[Embedded base64](https://spinnaker.io/docs/reference/artifacts-legacy/types/embedded-base64/)[GCS Object](https://spinnaker.io/docs/reference/artifacts-legacy/types/gcs-object/)[Git Repo](https://spinnaker.io/docs/reference/artifacts-legacy/types/git-repo/)[GitHub File](https://spinnaker.io/docs/reference/artifacts-legacy/types/github-file/)[Gitlab File](https://spinnaker.io/docs/reference/artifacts-legacy/types/gitlab-file/)[HTTP File](https://spinnaker.io/docs/reference/artifacts-legacy/types/http-file/)[Kubernetes Object](https://spinnaker.io/docs/reference/artifacts-legacy/types/kubernetes-object/)[Oracle Object](https://spinnaker.io/docs/reference/artifacts-legacy/types/oracle-object/)[S3 Object](https://spinnaker.io/docs/reference/artifacts-legacy/types/s3-object/)

                *   [Spinnaker Pipeline Reference](https://spinnaker.io/docs/reference/pipeline/)

                
                    *                           *   [Pipeline Expressions](https://spinnaker.io/docs/reference/pipeline/expressions/)

                        

                        *   [Pipeline Stages](https://spinnaker.io/docs/reference/pipeline/stages/)

                        

                        *   [Pipeline Templates](https://spinnaker.io/docs/reference/pipeline/templates/)

                        

        *   [Community](https://spinnaker.io/docs/community/)

        
            *                   *   [Contributing](https://spinnaker.io/docs/community/contributing/)

                
                    *                           *   [Code](https://spinnaker.io/docs/community/contributing/code/)

                        
                            *   [Build Statuses](https://spinnaker.io/docs/community/contributing/code/build-statuses/)[Nightly Builds](https://spinnaker.io/docs/community/contributing/code/nightly-builds/)[Releasing A Patch](https://spinnaker.io/docs/community/contributing/code/releasing/)[Code Languages, Libraries, and Conventions](https://spinnaker.io/docs/community/contributing/code/back-end-code/)
                                *   [Developer How Tos](https://spinnaker.io/docs/community/contributing/code/developer-guides/)

                                
                                    *                                           *   [Dev Env](https://spinnaker.io/docs/community/contributing/code/developer-guides/dev-env/)

                                        
                                            *   [Getting Set Up](https://spinnaker.io/docs/community/contributing/code/developer-guides/dev-env/getting-set-up/)[Kork Library](https://spinnaker.io/docs/community/contributing/code/developer-guides/dev-env/kork-library/)
                                                *   [Provider Setups](https://spinnaker.io/docs/community/contributing/code/developer-guides/dev-env/provider-setups/)

                                                
                                                    *   [Dev on AWS](https://spinnaker.io/docs/community/contributing/code/developer-guides/dev-env/provider-setups/aws-dev-setup/)

                                        *   [Service Overviews](https://spinnaker.io/docs/community/contributing/code/developer-guides/service-overviews/)

                                        
                                            *   [Orca Internals](https://spinnaker.io/docs/community/contributing/code/developer-guides/service-overviews/orca/)

                                        *   [Extending Spinnaker](https://spinnaker.io/docs/community/contributing/code/developer-guides/extending/)

                                        
                                            *   [Kubernetes CRD Extensions](https://spinnaker.io/docs/community/contributing/code/developer-guides/extending/crd-extensions/)[Writing a New Stage](https://spinnaker.io/docs/community/contributing/code/developer-guides/extending/new-stage/)

                                        *   [Plugin Creators](https://spinnaker.io/docs/community/contributing/code/developer-guides/plugin-creators/)

                                        
                                            *   [Plugin Creators Overview](https://spinnaker.io/docs/community/contributing/code/developer-guides/plugin-creators/overview/)[Plugin Project Config](https://spinnaker.io/docs/community/contributing/code/developer-guides/plugin-creators/project-config/)[Stage Plugin Details](https://spinnaker.io/docs/community/contributing/code/developer-guides/plugin-creators/stage-plugin-walkthrough/)

[Managing Deprecations](https://spinnaker.io/docs/community/contributing/code/managing-deprecations/)[Pull Requests and Changes](https://spinnaker.io/docs/community/contributing/code/submitting/)

                        *   [Docs](https://spinnaker.io/docs/community/contributing/docs/)

                        
                            *   [Documentation Style Guide](https://spinnaker.io/docs/community/contributing/docs/docs-style-guide/)[Make a Change Using a Local Clone](https://spinnaker.io/docs/community/contributing/docs/local-clone/)[Make a Change Using the GitHub Web UI](https://spinnaker.io/docs/community/contributing/docs/github-changes/)[Reviewing Pull Requests](https://spinnaker.io/docs/community/contributing/docs/reviewing-prs/)

[Getting Started as a Content Contributor](https://spinnaker.io/docs/community/contributing/content-contributing/)[Code Of Conduct](https://spinnaker.io/docs/community/contributing/code-of-conduct/)

                *   [Get Help](https://spinnaker.io/docs/community/get-help/)

                
                    *                           *   [FAQ](https://spinnaker.io/docs/community/get-help/faqs/)

                        

                        *   [Governance](https://spinnaker.io/docs/community/get-help/governance/)

                        
                            *   [Spinnaker Special Interest Groups](https://spinnaker.io/docs/community/get-help/governance/sigs/)

                *   [Stay Informed](https://spinnaker.io/docs/community/stay-informed/)

                
                    *                           *   [Security](https://spinnaker.io/docs/community/stay-informed/security/)

                        

                        *   [Usage Statistics](https://spinnaker.io/docs/community/stay-informed/stats/)

                        

[Captain's Log: The State of Spinnaker](https://spinnaker.io/docs/community/stay-informed/captains-log/)
                        *   [News](https://spinnaker.io/docs/community/stay-informed/news/)

                        
                            *                                   *   [Newsletter](https://spinnaker.io/docs/community/stay-informed/news/newsletter/)

                                
                                    *   [Flying Edition 1](https://spinnaker.io/docs/community/stay-informed/news/newsletter/edition1/)[Flying Edition 2](https://spinnaker.io/docs/community/stay-informed/news/newsletter/edition2/)[Flying Edition 3](https://spinnaker.io/docs/community/stay-informed/news/newsletter/edition3/)

                                *   [Videos](https://spinnaker.io/docs/community/stay-informed/news/videos/)

                                

                *   [Security](https://spinnaker.io/docs/community/security/)

                

                *   [Google Summer of Code](https://spinnaker.io/docs/community/gsoc/)

                
                    *   [try.spinnaker.io](https://spinnaker.io/docs/community/gsoc/projects/2021/try-spinnaker-io/)

        *   [Releases](https://spinnaker.io/docs/releases/)

        
            *   [Next Release Preview](https://spinnaker.io/docs/releases/next-release-preview/)[Patching Changelogs](https://spinnaker.io/docs/releases/patching-changelogs/)[Release Cadence](https://spinnaker.io/docs/releases/release-cadence/)[Release Manager](https://spinnaker.io/docs/releases/release-manager-runbook/)[Roadmap](https://spinnaker.io/docs/releases/roadmap/)[Support Policy](https://spinnaker.io/docs/releases/support-policy/)[Versions](https://spinnaker.io/docs/releases/versions/)

[Edit this page](https://github.com/spinnaker/spinnaker.io/edit/master/content/en/docs/setup/other_config/security/authentication/saml/index.md)[Create documentation issue](https://github.com/spinnaker/spinnaker.io/issues/new?title=SAML%202.0)[Create project issue](https://github.com/spinnaker/spinnaker/issues/new)

*   [Identity provider setup](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/#identity-provider-setup)
*   [New SAML Integration 2025.x.x](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/#new-saml-integration-2025xx)
*   [Network architecture and SSL termination](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/#network-architecture-and-ssl-termination)
*   [Workflow](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/#workflow)
*   [Next steps](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/#next-steps)
*   [Troubleshooting](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/#troubleshooting)

1.   [Documentation](https://spinnaker.io/docs/)
2.   [Setup](https://spinnaker.io/docs/setup/)
3.   [Configure Everything Else](https://spinnaker.io/docs/setup/other_config/)
4.   [Security](https://spinnaker.io/docs/setup/other_config/security/)
5.   [Authentication](https://spinnaker.io/docs/setup/other_config/security/authentication/)
6.   [SAML 2.0](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/)

SAML 2.0
========

Spinnaker supports using a SAML identity provider for single sign-on authentication.

Security Assertion Markup Language (SAML) is an XML based way to implement single sign-on (SSO).

A cryptographically signed XML document (known as a “SAML Assertion”) is sent to the API gateway server (Gate) with your identifying information, such as username and group membership.

Gate verifies the XML document’s signature using a `metadata` file, and if successful, it associates the identifying information with the user and allows the user to proceed as authenticated.

Identity provider setup
-----------------------

1.   In your SAML Identity Provider (IdP), download the `metadata.xml` file. Some providers expose this as a URL. It may look something like this:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<md:EntityDescriptor 
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"    
    entityID="https://accounts.google.com/o/saml2?idpid=SomeValueHere" 
    validUntil="2021-05-16T15:17:27.000Z">
  <md:IDPSSODescriptor 
      WantAuthnRequestsSigned="false" 
      protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:KeyDescriptor use="signing">
      <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:X509Data>
          <ds:X509Certificate>
MIIDdDCCAlygAwIBAgIGAVS/Sw5yMA0GCSqGSIb3DQEBCwUAMHsxFDASBgNVBAoTC0dvb2dsZSBJ
bmMuMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MQ8wDQYDVQQDEwZHb29nbGUxGDAWBgNVBAsTD0dv
b2dsZSBGb3IgV29yazELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWEwHhcNMTYwNTE3
MTUxNzI3WhcNMjEwNTE2MTUxNzI3WjB7MRQwEgYDVQQKEwtHb29nbGUgSW5jLjEWMBQGA1UEBxMN
TW91bnRhaW4gVmlldzEPMA0GA1UEAxMGR29vZ2xlMRgwFgYDVQQLEw9Hb29nbGUgRm9yIFdvcmsx
CzAJBgNVBAYTblVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMIIBIjANBgkqhkiG9w0BAQEF46OCAQ8A
MIIBCgKCAQEA4JsnpS0ZBzb7DtlU7Zop7l+Kgr7NzusKWcEC6MOsFa4Dlt7jxv4ScKZ/61M5WKxd
5YX0ol1rPokpNztj+Zk7OXrG8lDic0DpeDutc9pcq0+9/NYFF7WR7TDjh4B7Txnq7SerSB78fT8d
4rK7Bd+cu/cBIyAAyZ5tLeLbmTnHAk093Y9vF3mdWQnfAhx4ldOfstF6G/d2ev7I5xjSKzQuH6Ew
3bb3HLcM4uEVevOfNAlh1KoV4vQr+qzbc9UEFcPRwzuTwGa6QjfspWW7NgXKbHHC+X6a+gqJrke/
6l2VvHaQBJ7oIyt4PCdel2cnUkvuxvzHPYedh1AgrIiSP1brSQIDAQABMA0GCSqGSI34DQEBCwUA
A4IBAQCPqMAIau+pRDs2NZG1nGfyEMDfs0qop6FBa/wTNis75tLvay9MUlxXkTxm9aVxgggjEyc6
XtDjpV0onrH0jBnSc+vRI1GFQ48EO3owy3uBIeR1aMy13ZwAA+KVizeoOrXBJbvIUZHo0yfKRzIu
gtM58j58BdAFeYo+X9ds/ysvZ8FIGTLqMl/A3oO/yBNDjXR9Izoqgm7RX0JJXGL9Y1AgmEjxyqo9
MhxZAGxOHm9HZWWfVMcoe8p62mRJ2zf4lkNPBnDHrQ8MDPSsXewAuiSnRBDLxhdBgyThT/KW7Q06
rGa6Dp0rntKWzZE3hGQS0AdsnuFY/OXbmkNG9WUrUg5x
          </ds:X509Certificate>
        </ds:X509Data>
      </ds:KeyInfo>
    </md:KeyDescriptor>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
    <md:SingleSignOnService 
        Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" 
        Location="https://accounts.google.com/o/saml2/idp?idpid=SomeValueHere"/>
    <md:SingleSignOnService 
        Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" 
        Location="https://accounts.google.com/o/saml2/idp?idpid=SomeValueHere"/>
  </md:IDPSSODescriptor>
</md:EntityDescriptor>
``` 
2.   Create a Spinnaker SAML application.

3.   Specify the login URL as `https://localhost:8084/saml/SSO`. Replace “localhost” with Gate’s address, if known.

4.   Specify a unique entity ID (we’ll use `spinnaker.test` in our example).

5.   Enable the users you’d like to have access to your Spinnaker instance.

6.   Generate a keystore and key in a new Java Keystore with some password:

```
keytool -genkey -v -keystore saml.jks -alias saml -keyalg RSA -keysize 2048 -validity 10000
```
7.   Execute the following halyard commands and redeploy Gate:

```
KEYSTORE_PATH= # /path/to/keystore.jks
KEYSTORE_PASSWORD=hunter2
METADATA_PATH= # /path/to/metadata.xml
SERVICE_ADDR_URL=https://localhost:8084
ISSUER_ID=spinnaker.test
   
hal config security authn saml edit \
  --keystore $KEYSTORE_PATH \
  --keystore-alias saml \
  --keystore-password $KEYSTORE_PASSWORD \
  --metadata $METADATA_PATH \
  --issuer-id $ISSUER_ID \
  --service-address-url $SERVICE_ADDR_URL
     
hal config security authn saml enable
```

New SAML Integration 2025.x.x
-----------------------------

Starting with Spinnaker 2025.x.x, a new SAML integration mechanism has been introduced to improve compatibility, simplify configuration, and align with modern identity provider (IdP) standards. This replaces some of the legacy configuration approaches used in earlier versions of Spinnaker.

The below approach applies to certain IDPs that support signing credentials (Okta is NOT one of these). This is a required change for keycloak and a few other providers. Note alternatively to using a custom volume map, you can use [encryptedFile secret](https://spinnaker.io/docs/reference/halyard/secrets/) store references.

create configMap

```
kubectl create configmap configmap-saml --from-file=<your_metadata>.xml --from-file=<your_cert>.pem --from-file=<your_priv>.pem
```

service-settings/gate.yml

```
kubernetes:
  volumes:
  - id: configmap-saml
    type: configMap
    mounthPath: /opt/spinnaker/saml
```

profiles/gate-local.yml

```
saml:
  enabled: true
  issuerId: <Client>
  metadataUrl: file:/opt/spinnaker/saml/<your_cert>.xml
  sign-requests: true
  signing-credentials:
  - certificate-location: file:/opt/spinnaker/saml/<your_cert>.pem
    private-key-location: file:/opt/spinnaker/saml/<your_priv>.pem
```

.hal/config

```
saml:
  # below enabled and issuerId is not needed but it is not a big deal if you still placed it on your hal config
  #enabled: true
  #issuerId: <Client>
  serviceAddress: <your_gate_url>

  # you can add a userinfomappings if you want
```

Network architecture and SSL termination
----------------------------------------

During the SAML [workflow](https://spinnaker.io/docs/reference/architecture/authz_authn/authentication/#workflow) , Gate makes an intelligent guess on how to assemble a URI to itself, called the _Assertion Consumer Service URL_. Sometimes this guess is wrong when Spinnaker is deployed in concert with other networking components, such as an SSL-terminating load balancer, or in the case of the [Quickstart](https://spinnaker.io/docs/setup/quickstart) images, a fronting Apache instance.

To override the values to assemble the URL, use the following `hal` command:

```bash
hal config security authn saml edit --service-address-url https://my-real-gate-address.com:8084
```

Please check on the [SSL Documentation](https://spinnaker.io/docs/setup/other_config/security/ssl) for more information.

> For the Quickstart images, append `/gate` to the `--service-address-url`. All other configurations can omit this setting.

Workflow
--------

The SAML workflow below reflects the process when the user navigates to _Spinnaker first_, is redirected to the SAML IdP for login, and redirected back to Spinnaker. Some SAML providers will allow the user login to the _SAML provider first_, and click a link to be taken to Spinnaker.

sequenceDiagram participant Deck participant Gate participant IdentityProvider Deck->>+Gate: GET /something/protected Gate->>-Deck: HTTP 302 to https://idp.url/?SAMLRequest=... Deck->>+IdentityProvider: GET https://idp.url/?SAMLRequest=... IdentityProvider->>-Deck: Returns login page

1.   User attempts to access a protected resource.

2.   Gate redirects to the SAML provider, passing a few query params:

    *   `SAMLRequest`: a Gzip’ed XML authentication request.
    *   `SigAlg`: The algorithm used to generate the `Signature` parameter.
    *   `Signature`: A digest of the `SAMLRequest` using the `SigAlg` algorithm and the server’s key.

> Within the `SAMLRequest` is the _Assertion Consumer Service URL_, with is the URL to your Gate instance. See [here](https://spinnaker.io/docs/setup/other_config/security/authentication/saml/#network-architecture-and-ssl-termination) for how to override this value.

3.   SAML provider prompts user for username & password.

sequenceDiagram participant Deck participant Gate participant IdentityProvider Deck->>+IdentityProvider: User sends credentials IdentityProvider->>-Deck: HTTP 200 with self-submitting form to POST https://gate.url Deck->>+Gate: POST /saml/SSO with { SAMLResponse: ... } Note right of Gate: User identity verified Note right of Gate: Gate extracts data based on userInfoMapping Gate->>-Deck: HTTP 302 /something/protected 
4.   A SAML response must be POSTed to `/saml/SSO`, and most browsers won’t re-POST when given an HTTP 302. Instead, providers sometimes return a page (with HTTP 200) that has a self-submitting HTML form to POST to Gate’s `/saml/SSO` endpoint.

5.   Gate verifies the message’s integrity by checking its signature, and thus verifying the user’s identity information.

6.   Gate determines the username and/or email address, and optionally extracts group membership (if sent by the IdP).

7.   With the user’s identity verified, Gate redirects the user to the originally requested URL.

Next steps
----------

Now that you’ve authenticated the user, proceed to setting up their [authorization](https://spinnaker.io/docs/setup/other_config/security/authorization/) .

Troubleshooting
---------------

*   Review the general [authentication guide](https://spinnaker.io/docs/setup/other_config/security/authentication) .

*   Review the authentication [reference guide](https://spinnaker.io/docs/reference/architecture/authz_authn/authentication) .

*   Use an [incognito window](https://spinnaker.io/docs/setup/other_config/security/authentication#incognito-mode) .

Last modified September 9, 2025: [docs(SAML): Add New SAML Integration for version 2025.x.x (#547) (d2d0a43)](https://github.com/spinnaker/spinnaker.io/commit/d2d0a435458666adb315a76ae315eb262c171d7b)

* * *

*   [](http://github.com/spinnaker)
*   [](https://join.slack.com/t/spinnakerteam/shared_invite/zt-3f4dqg66a-hX~tWeWPL3Sfnj3F8Ie2xg)
*   [](https://twitter.com/spinnakerio)

[![Image 2: CD Foundation logo](https://spinnaker.io/images/cdf-color.png)](https://cd.foundation/)[![Image 3: Deploys by Netlify](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)

© 2026 Copyright © 2020 The Linux Foundation®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://www.linuxfoundation.org/trademark-usage) page. Linux is a registered trademark of Linus Torvalds. All Rights Reserved

[Privacy Policy](http://www.linuxfoundation.org/privacy) | [Terms of Use](http://www.linuxfoundation.org/terms)
