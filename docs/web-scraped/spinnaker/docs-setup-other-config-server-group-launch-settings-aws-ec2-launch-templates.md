# Source: https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/

Title: AWS EC2 Launch Templates

URL Source: https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/

Markdown Content:
AWS EC2 Launch Templates | Spinnaker
===============

Spinnaker talks from cdCon 2025 now available!

[Browse Playlist](https://www.youtube.com/playlist?list=PL2KXbZ9-EY9Qvfxh3i9YtiGLqNFHId1qM)

[![Image 3: Spinnaker Logo Horizontal](https://spinnaker.io/images/spinnaker-logo-horizontal.png)](https://spinnaker.io/)

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

[Edit this page](https://github.com/spinnaker/spinnaker.io/edit/master/content/en/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates.md)[Create documentation issue](https://github.com/spinnaker/spinnaker.io/issues/new?title=AWS%20EC2%20Launch%20Templates)[Create project issue](https://github.com/spinnaker/spinnaker/issues/new)

*   [Feature Configuration](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/#feature-configuration)
    *   [Launch Template Only Parameters](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/#launch-template-only-parameters)
    *   [Additional Features](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/#additional-features)

*   [Use Cases & Sample API Requests](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/#use-cases--sample-api-requests)

1.   [Documentation](https://spinnaker.io/docs/)
2.   [Setup](https://spinnaker.io/docs/setup/)
3.   [Configure Everything Else](https://spinnaker.io/docs/setup/other_config/)
4.   [Server Group Launch Settings](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/)
5.   [AWS EC2 Server Group Launch Settings](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/)
6.   [AWS EC2 Launch Templates](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates/)

AWS EC2 Launch Templates
========================

AWS EC2 Launch Template Features, Use Cases and Sample API Requests

> Launch Template Support must be enabled in order to use the features described in this page. Follow guidelines [here](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/launch-templates-setup) to enable the feature set.

> Note: The features supported in the UI (Deck) come with tool tips that can help you learn the new features. Consider trying them out in Deck, especially if they are new to you.

Feature Configuration
---------------------

Once launch templates support is enabled in Clouddriver, a new set of features are unlocked. Some of them are tied to the EC2 launch template directly like `IMDSV2` and others require a launch template to be used in order to support features like `SpotAllocationStrategy` ( [MixedInstancesPolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html) features).

Review the sections below for details about the features and sample use cases along with Spinnaker API requests.

### Launch Template Only Parameters

Review the sections below to determine which features you want to enable in the Spinnaker UI / Deck. Users will see enabled features as options when configuring a Server Group.

| Feature | Description | Deck Setting | Clouddriver API Request Parameter | Release Version | Default value in Spinnaker |
| --- | --- | --- | --- | --- | --- |
| IPv6 | ASGs associate an IPv6 address to their instances. | _enableIPv6_ | _associateIPv6Address_ | _v1.21_ | no default |
| IMDSv2 | Helps mitigate AWS credential theft from the exploitation of SSRF vulnerabilities in web applications. This is only supported by modern SDKs. Learn more from [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html). | _enableIMDSv2_ | _requireIMDSv2_ | _v1.21_ | false |
| CreditSpecification | The credit option for CPU usage of the instance. Valid for burstable performance EC2 instances only. Learn more from [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html). | _enableCpuCredits_ | _unlimitedCpuCredits_ | _v1.24_ | [default _false_](https://github.com/spinnaker/clouddriver/blob/master/clouddriver-aws/src/main/groovy/com/netflix/spinnaker/clouddriver/aws/deploy/handlers/BasicAmazonDeployHandler.groovy#L488) used only when all instance types in request support bursting. |

### Additional Features

Enabling launch template support also unlocks additional features offered by Amazon EC2 Auto Scaling that facilitate diversified server groups:

*   Multiple instance types
*   Multiple purchase options (On-Demand / Spot) with proportion control
*   Allocation strategies
*   Capacity rebalancing

Follow [AWS recommended best practices for EC2 Spot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) to improve your experience with EC2 Spot.

Motivation to diversify instances in your Server Group:

*   Reduce costs by diversifying instances across purchase options and Spot allocation strategies. See AWS docs to learn more about [how to use Spot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) .
*   Reduce costs and optimize resources with instance weighting.
*   Enhance availability by deploying your application across multiple instance types running in multiple Availability Zones.
*   Enhance availability by proactively augmenting your fleet with a new Spot instance from an optimal pool, before a running instance is interrupted by EC2, by enabling [capacity rebalance](https://docs.aws.amazon.com/autoscaling/ec2/userguide/capacity-rebalance.html) .
*   Reduce probability of [InsufficientInstanceCapacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html#troubleshooting-launch-capacity) exceptions with flexible instance configuration.

Using one or more parameters in the table below will automatically create Server Groups with instances distribution configuration specified, and will use AWS defaults for the parameters not specified. Note that a number of these parameters complement each other. So, combining them can greatly enhance your AWS experience.

| Category | Feature / Clouddriver API Request Parameter | Description | AWS Default | Clouddriver Release Version | Deck Setting | Deck Release Version |
| --- | --- | --- | --- | --- | --- | --- |
| Multiple instance types with instance weighting and priority, with launch template overrides. Properties overridden will replace the same properties in launch template. AWS docs: [Instance Weighting](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html) | _launchTemplateOverridesForInstanceType.instanceType_ | Instance Type to override | no default | v1.26 | Instance Types / LaunchTemplate -> Instance Types | v1.28 |
| _launchTemplateOverridesForInstanceType.weightedCapacity_ | The number of capacity units for the specified instance type in terms of virtual CPUs, memory, storage, throughput, or other relative performance characteristic. The capacity units count toward the desired capacity. | 1 i.e. if no weighted capacity is specified, all instance types (large or small) are treated as the same weight. |
| _launchTemplateOverridesForInstanceType.priority_ | Optional priority for instance type. Lower the number, higher the priority. If unset, the launch template override has the lowest priority. The order of instance types in the list of launch template overrides sent to AWS is set from highest to lowest priority. Valid values: integer > 0. | first to last in list | v1.27 |
| On-Demand AWS docs: [Instances Distribution](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html) | _onDemandAllocationStrategy_ | Indicates how to allocate instance types to fulfill On-Demand capacity. The only valid value is _prioritized_. This strategy uses the order of instance types in the launch template overrides to define the launch priority of each instance type. The first instance type in the list is prioritized higher than the last. | _prioritized_ | v1.26 | Instance Types -> Instances Distribution / Instances Distribution |
| _onDemandBaseCapacity_ | The minimum amount of the Server Group's capacity that must be fulfilled by On-Demand Instances. **NOTE**: _If weights are specified for the instance types in the overrides, set the value of OnDemandBaseCapacity in terms of the number of capacity units, and not number of instances._ | 0 |
| _onDemandPercentageAboveBaseCapacity_ | The percentages of On-Demand Instances and Spot Instances for additional capacity beyond _OnDemandBaseCapacity_. | 100 i.e. only On-Demand instances |
| Spot AWS docs: * [Instance Distribution](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html) * [ASG Capacity Rebalance](https://docs.aws.amazon.com/autoscaling/ec2/userguide/capacity-rebalance.html) * [EC2 Instance Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html) | _spotAllocationStrategy_ | Indicates how to allocate instances across Spot Instance pools. 2 strategies: 1) capacity-optimized (recommended): instances launched using Spot pools that are optimally chosen based on the available Spot capacity. 2) lowest-price: instances launched using Spot pools with the lowest price, and evenly allocated across the number of Spot pools specified in spotInstancePools. | _lowest-price_ |
| _spotInstancePools_ | The number of Spot Instance pools across which to allocate Spot Instances. The Spot pools are determined from the different instance types in the overrides. Only applicable with 'lowest-price' spotAllocationStrategy. | 2 |
| _spotPrice_ | The maximum price per unit hour that the user is willing to pay for a Spot Instance. | On-Demand price for the configuration |
| _capacityRebalance_ | Enable to allow Amazon EC2 Auto Scaling to attempt proactive replacement of Spot Instances in the server group that have received a rebalance recommendation (i.e. at elevated risk of interruption), **before** they are interrupted by AWS EC2. Note: Enabling this feature could exceed the server group's max capacity for a brief period of time, leading to higher costs. Learn more in AWS docs. | false i.e. disabled | v1.27 | Advanced Settings -> capcity rebalance | v1.27 |

Use Cases & Sample API Requests
-------------------------------

#### Create a Server Group with launch template

After enabling the launch template feature set in Clouddriver and/or Deck, set `setLaunchTemplate` to true in order to indicate Spinnaker to create your Server Group with an EC2 launch template.

```bash
curl -H 'Content-Type: application/json' -d '{ "job": [
  {
    "type": "createServerGroup",
    "cloudProvider": "aws",
    "account": "my-aws-account",
    "application": "myAwsApp",
    "stack": "myStack",
    "credentials": "my-aws-account",
    "subnetType": "public-subnet",
    "availabilityZones": {"us-west-1": ["us-west-1a","us-west-1b","us-west-1c"]},
    "amiName": "ami-12345",
    "capacity": {"desired": 3,"max": 5,"min": 3},
    "iamRole":"MyInstanceProfile",
    "instanceType":"t3.large",
    "setLaunchTemplate": true,
    "requireIMDSv2": true,
    "unlimitedCpuCredits": true
  }], "application": "myAwsApp", "description": "Create New Server Group in cluster myAwsApp"}' -X POST http://my-spinnaker-gate:8084/tasks
```

Let’s say, the Server Group created was named `myAwsApp-myStack-v005`. It is backed by EC2 launch template with IMDSv2 enabled and unlimited CPU credits.

#### Convert a Server Group with launch template to use mixed instances policy, with multiple instance types and capacity weighting

The Spinnaker operation, `modifyServerGroupLaunchTemplate`/ `updateLaunchTemplate` also supports updating a Server Group backed by launch template to use mixed instances policy when one or more mixed instances policy parameters listed above is specified.

```bash
curl -H 'Content-Type: application/json' -d '{ "job": [ 
  {
    "type": "updateLaunchTemplate",
    "cloudProvider": "aws",
    "account": "my-aws-account",
    "application": "myAwsApp",
    "stack": "myStack",
    "credentials": "my-aws-account",
    "region": "eu-central-1",
    "asgName": "myAwsApp-myStack-v005",
    "launchTemplateOverridesForInstanceType": [
      {"instanceType":"t2.large","weightedCapacity":"1"},
      {"instanceType":"t3.large","weightedCapacity":"1"},
      {"instanceType":"t2.xlarge","weightedCapacity":"2"},
      {"instanceType":"t3.xlarge","weightedCapacity":"2"}] 
  }], "application": "myAwsApp", "description": "Modify Server Group in cluster myAwsApp"}' -X POST http://my-spinnaker-gate:8084/tasks
```

Note: instance weighting is requested by vCPUs.

AWS docs:

*   [multiple instance types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html)
*   [instance weighting](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html)

#### Diversify instances in a Server Group across purchase options (On-Demand and Spot), multiple instance types with priority assignment:

```bash
curl -H 'Content-Type: application/json' -d '{ "job": [ 
  {
    "type": "createServerGroup",
    "cloudProvider": "aws",
    "account": "my-aws-account",
    "application": "myAwsApp",
    "stack": "myStack",
    "credentials": "my-aws-account",
    "availabilityZones": {"us-west-1": ["us-west-1a","us-west-1b","us-west-1c"]},
    "amiName": "ami-12345",
    "capacity": {"desired": 3,"max": 5,"min": 3},
    "iamRole":"MyInstanceProfile",
    "instanceType":"m4.large",
    "setLaunchTemplate": true,
    "onDemandBaseCapacity":1,
    "onDemandPercentageAboveBaseCapacity":50,
    "spotAllocationStrategy":"capacity-optimized",
    "launchTemplateOverridesForInstanceType": [
      {"instanceType":"m5.large","weightedCapacity":"1","priority": 2},
      {"instanceType":"m5.xlarge","weightedCapacity":"2","priority": 1}] 
  }], "application": "myAwsApp", "description": "Create New Server Group in cluster myAwsApp"}' -X POST http://my-spinnaker-gate:8084/tasks
```

See capacity type for instances in Deck:

![Image 4: Capacity Type On-Demand](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/capacity_type_ondemand.png)![Image 5: Capacity Type Spot](https://spinnaker.io/docs/setup/other_config/server-group-launch-settings/aws-ec2/capacity_type_spot.png)

AWS docs:

*   [instances distribution in ASG](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html)
*   [allocation strategies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html#asg-allocation-strategies)

#### Create a Server Group with AWS recommended best practices for EC2 Spot

The best practices followed in the example:

*   use multiple instance types
*   use `capacity-optimized` Spot allocation strategy to indicate AWS to provision instances from the most-available Spot capacity pools
*   use default maximum price for Spot i.e. On-Demand price
*   mix in previous generation instance types
*   use proactive capacity rebalancing (works best with `capacity-optimized` spotAllocationStrategy)

```bash
curl -H 'Content-Type: application/json' -d '{ "job": [ 
  {
    "type": "createServerGroup",
    "cloudProvider": "aws",
    "account": "my-aws-account",
    "application": "myAwsApp",
    "stack": "myStack",
    "credentials": "my-aws-account",
    "subnetType": "public-subnet",
    "availabilityZones": {"us-west-1": ["us-west-1a","us-west-1b","us-west-1c"]},
    "amiName": "ami-12345",
    "capacity": {"desired": 3,"max": 5,"min": 3},
    "iamRole":"MyInstanceProfile",
    "instanceType":"m4.large",
    "setLaunchTemplate": true,
    "onDemandPercentageAboveBaseCapacity":50,
    "onDemandBaseCapacity":1,
    "spotAllocationStrategy":"capacity-optimized",
    "capacityRebalance": true,
    "launchTemplateOverridesForInstanceType": [
      {"instanceType":"m4.large","weightedCapacity":"1"},
      {"instanceType":"m5.large","weightedCapacity":"1"},
      {"instanceType":"m4.xlarge","weightedCapacity":"2"},
      {"instanceType":"m5.xlarge","weightedCapacity":"2"}] 
  }], "application": "myAwsApp", "description": "Create New Server Group in cluster myAwsApp"}' -X POST http://my-spinnaker-gate:8084/tasks
```

Note: instance weighting requested by vCPUs

AWS docs:

*   [Best practices for ASG with Spot instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html#asg-spot-best-practices)
*   [Best practices for EC2 Spot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html)

Last modified July 8, 2022: [Update launch-templates.md (#209) (6a52e08)](https://github.com/spinnaker/spinnaker.io/commit/6a52e0881214adc251a85461c0e0c63527b29fc8)

* * *

*   [](http://github.com/spinnaker)
*   [](https://join.slack.com/t/spinnakerteam/shared_invite/zt-3f4dqg66a-hX~tWeWPL3Sfnj3F8Ie2xg)
*   [](https://twitter.com/spinnakerio)

[![Image 6: CD Foundation logo](https://spinnaker.io/images/cdf-color.png)](https://cd.foundation/)[![Image 7: Deploys by Netlify](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)

© 2026 Copyright © 2020 The Linux Foundation®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://www.linuxfoundation.org/trademark-usage) page. Linux is a registered trademark of Linus Torvalds. All Rights Reserved

[Privacy Policy](http://www.linuxfoundation.org/privacy) | [Terms of Use](http://www.linuxfoundation.org/terms)
