# Source: https://docs.port.io/solutions/resource-self-service/create-golden-paths.md

# Create golden paths

Golden paths are a foundational element of effective platform engineering.<br /><!-- -->They are your organization's standardized, opinionated way of doing things that developers actually want to use. Think of them as the "happy path" that guides developers toward best practices while eliminating decision fatigue and reducing cognitive load.

## Why golden paths matter[â](#why-golden-paths-matter "Direct link to Why golden paths matter")

As a platform engineer, you're constantly balancing standardization with developer productivity. Golden paths solve this by providing:

* **Consistency at scale**: Every team follows the same patterns, making your platform predictable and maintainable.
* **Reduced cognitive load**: Developers don't waste time deciding between 47 different ways to create a service.
* **Built-in compliance**: Security, observability, and operational requirements are baked into the path.
* **Faster onboarding**: New developers can be productive immediately without learning tribal knowledge.
* **Reduced support burden**: Fewer "how do I..." questions and fewer production issues from misconfigurations.

## The golden path philosophy[â](#the-golden-path-philosophy "Direct link to The golden path philosophy")

Golden paths aren't designed to restrict choice, they're focused on making the right choice the easy choice. When you provide a clear, well-documented approach that follows your organization's standards, developers will naturally gravitate toward it because it's easier, faster and safer than figuring things out on their own.

The best golden paths are:

* **Opinionated but flexible**: Clear defaults with escape hatches for edge cases.
* **Self-service**: No tickets, no approvals, just instant gratification.
* **Well-documented**: Clear examples and troubleshooting guides.
* **Continuously improved**: Feedback loops that make the path better over time.

## From chaos to clarity[â](#from-chaos-to-clarity "Direct link to From chaos to clarity")

Without golden paths, you get:

* 47 different ways to create a service
* Inconsistent security configurations
* Missing observability instrumentation
* Production issues from misconfigurations
* Endless support requests

With golden paths, you get:

* A few approved patterns to do the majority of things correctly
* Consistent, secure, observable services
* Happy, productive developers
* More time for platform innovation

Golden paths transform your platform from a collection of tools into a cohesive developer experience that scales with your organization.

## Opinions on golden paths[â](#opinions-on-golden-paths "Direct link to Opinions on golden paths")

### Scaffold new respositories and services[â](#scaffold-new-respositories-and-services "Direct link to Scaffold new respositories and services")

There is no better opportunity to set up developers up for success, than a greenfield use case, where the developer is configuring a new repository or service. At this point, you as a platform engineer can give them all the best configuration out of the box, such that it's easier for them to ship their code with confidence from the outset.

[Scaffolding with Port](https://www.youtube.com/embed/sE6XI0XDtQI)

* [Scaffold a New Service](/guides/all/scaffold-a-new-service.md): Learn how to quickly generate a new service with all the recommended defaults and best practices built in.
* [Deploy New Service and Infra](/guides/all/create-eks-cluster-and-deploy-app.md): See how to deploy a new service and its infrastructure together, enabling fast, reliable onboarding for new projects.

### Cloud resources[â](#cloud-resources "Direct link to Cloud resources")

#### Architectural patterns[â](#architectural-patterns "Direct link to Architectural patterns")

Before diving into guides, it's important to pause and outline the two general patterns that exist for self-service actions (for Cloud Resources). With the adoption of Infrastructure as Code, many organizations maintain that the source-of-truth for their infrastructure configuration in their Git repositories, rather than in their cloud environments directly.

It's important to build self-service that conforms with your organizational standards and best practices. Failing to match your ways of working will just lead to further resource sprawl and complexity for your Platform Engineering team.

We'll explore 2 types of self-service below - RESTful Self-Service and Gitops-based Self-Service.

![RESTful vs GitOps flows](/img/solutions/resource-self-service/restful-vs-gitops.png)

##### RESTful self-service[â](#restful-self-service "Direct link to RESTful self-service")

RESTful self-service actions directly create resources in your cloud provider or other upstream systems through their APIs. This approach is straightforward and immediateâwhen a developer requests a resource through Port's self-service interface, the action makes API calls to create the resource directly in the target system (like AWS, Azure, or GCP). This pattern works well for organizations that prefer direct resource creation or when you need immediate provisioning without the overhead of Git-based workflows. The trade-off is that you lose the audit trail and version control benefits that come with GitOps, but you gain simplicity and speed for teams that don't need the full GitOps workflow.

* [Create an S3 Bucket via a CI Job, with either Terraform or cloud SDKs](/guides/all/s3-using-webhook.md): Learn how to provision an S3 bucket instantly.
* [Deploy EC2, RDS and S3 Resources with CloudFormation Templates](/guides/all/deploy-cloudformation-template.md): Create EC2 and RDS instances or S3 buckets using Cloudformation templates in a Github Action.
* [Create an EC2 Instance with Terraform](/guides/all/create-an-ec2-instance.md): Create an EC2 instance with Terraform in a Github Action.
* [Create Azure Storage Account with Terraform with Github Actions](/guides/all/create-azure-resource.md): Create an Azure Storage Account using Terraform in a Github Action.
* [Create and Attach an EBS Volume](/guides/all/add-ec2-volume.md): Provision a new EBS instance and attach to an EC2 Instance using Terraform in a GitLab pipeline.
* [Create Azure Storage Account with Terraform from Jenkins](/guides/all/deploy-azure-resource.md): Create an Azure Storage Account using Terraform in a Jenkins Pipeline.
* [Manage Kubernetes Namespaces](/guides/all/manage-kubernetes-namespaces.md): Enable developers to create and manage Kubernetes namespaces without manual intervention. Implemented with GitLab pipelines and Slack notifications.
* [Streamline IaC with AI](/guides/all/streamline-iac-with-ai.md): Use Port AI agents to automate IaC provisioning and management.

![Autoscaling Dashboard Example](/img/self-service-actions/setup-backend/gitlab-pipeline/testAddingDisk.png)

##### GitOps-based self-service[â](#gitops-based-self-service "Direct link to GitOps-based self-service")

GitOps-based self-service actions create resources by leveraging your existing Infrastructure as Code (IaC) files and modules. Here, an existing GitOps pipeline (like ArgoCD, Flux, or Terraform Cloud) picks up the changes and provisions the resources in the target cloud environment. This approach maintains the benefits of version control, audit trails, and the ability to review changes through pull requests, while still providing developers with a streamlined self-service experience. The trade-off is that resource creation takes longer due to the GitOps pipeline cycle, but you gain better governance, compliance, and the ability to enforce organizational standards through code review processes.

* [Create Cloud Resource Using IaC](/guides/all/create-cloud-resource-using-iac.md): Provision cloud resources by updating Infrastructure as Code files and letting your GitOps pipeline handle deployment.
* [Deploy S3 Bucket CrossPlane](/guides/all/deploy-s3-bucket-crossplane.md): Use CrossPlane to declaratively manage and deploy S3 buckets through GitOps workflows.
* [Create Github Pull Request](/guides/all/create-github-pull-request.md): Automate the creation of Github pull requests to trigger infrastructure changes and reviews.

### Create secrets[â](#create-secrets "Direct link to Create secrets")

Secret leakage remains a huge issue in the industry. The fact that developers have to manually handle secrets is like a process in a nuclear plant requiring the manual handling of uranium. It's an error prone workflow, that often leads to a security incident and in worse cases, supply chain security issues and data loss.

The best protection against secret leakage is the design of a secure workflow, in which secrets are securely handled and developers are unlikely to make an error.

#### Add secrets to Github from your portal[â](#add-secrets-to-github-from-your-portal "Direct link to Add secrets to Github from your portal")

* [How to securely create a Github Secret](/guides/all/create-github-secret.md): Follow this guide to add secrets to your Github repositories safely and prevent accidental exposure.

#### Integrate Port with AKeyless[â](#integrate-port-with-akeyless "Direct link to Integrate Port with AKeyless")

[Secure Secrets Management](https://www.youtube.com/embed/QO45jaeAA2o)

## Real-world benefits[â](#real-world-benefits "Direct link to Real-world benefits")

Golden paths provide a standardized, secure, and efficient way for developers to provision resources and services. By implementing golden paths in Port, organizations can achieve:

* **Reduced cognitive load**: Developers don't need to understand complex infrastructure details or remember specific commands
* **Faster provisioning**: Self-service actions eliminate back-and-forth with platform teams for common requests
* **Consistent standards**: Every resource follows organizational best practices and security policies
* **Better governance**: All resource creation is tracked, auditable, and follows approved patterns
* **Reduced errors**: Predefined templates and validation prevent common mistakes and misconfigurations
* **Improved developer experience**: Teams can focus on building features rather than managing infrastructure complexity

Golden paths transform your platform engineering team from a bottleneck into an enabler, allowing developers to move faster while maintaining the security and compliance standards your organization requires.
