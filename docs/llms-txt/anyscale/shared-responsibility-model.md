# Source: https://docs.anyscale.com/administration/security-and-compliance/shared-responsibility-model.md

# Shared responsibility model

[View Markdown](/administration/security-and-compliance/shared-responsibility-model.md)

# Shared responsibility model

Anyscale uses a shared responsibility model with its customers. Anyscale maintains the integrity of the control plane while customers work alongside Anyscale to maintain the integrity of the data plane.

note

The [Anyscale Security Addendum](https://www.anyscale.com/security-addendum) provides additional details on the standards, protocols, and policies upheld by Anyscale. The following list highlights important characteristics of the control plane and data plane but shouldn't be considered exhaustive.

## Anyscale responsibilities[​](#anyscale-responsibilities "Direct link to Anyscale responsibilities")

### Service availability[​](#service-availability "Direct link to Service availability")

The Anyscale Control Plane architecture incorporates modern cloud best practices. Automated alerting and 24/7 monitoring features verify the operational health of Anyscale systems and page relevant on-call personnel in the event of incidents. Periodic backups and snapshots of critical components occur and disaster recovery exercises occur on a regularly scheduled basis.

### Separation of environments[​](#separation-of-environments "Direct link to Separation of environments")

Anyscale leverages multiple environments to test and deploy Anyscale systems, allowing for automated testing as part of the deployment process. Permissions for Anyscale employees are centrally managed and delegated through relevant permission sets within an identity provider.

### Encryption[​](#encryption "Direct link to Encryption")

Wherever possible, Anyscale encrypts data in transit and at rest using industry standard encryption protocols. Storage devices are encrypted using ciphers such as AES 256 with envelope keys rotated by accredited key management services. Network communication is encrypted using at minimum TLS 1.2.

### Packages, patching, and vulnerability management (of the control plane)[​](#packages-patching-and-vulnerability-management-of-the-control-plane "Direct link to Packages, patching, and vulnerability management (of the control plane)")

The automated build pipeline includes tooling to inspect for known security vulnerabilities and apply relevant patches to comply with Anyscale security policies. For every commit, the pipeline uses scanning tooling and conducts tests to ensure compliance, and blocks the commit when compliance is not met. Anyscale leverages an immutable infrastructure deployment paradigm so that patches and other updates are applied with every release. For certain components of the Control Plane, Anyscale leverages provider managed patch updates or fully managed services.

## Customer responsibilities[​](#customer-responsibilities "Direct link to Customer responsibilities")

### Cloud integrity (self-hosted clouds)[​](#cloud-integrity-self-hosted-clouds "Direct link to Cloud integrity (self-hosted clouds)")

Anyscale deploys infrastructure into the customer data plane using Anyscale Self-hosted Clouds. The customer is responsible for ensuring that the configuration of these clouds doesn't drift outside of the resources specified in the [cloud configuration documentation](/admin/cloud.md). Modifications to IAM policies, network routes, encryption keys, or other policies may result in unexpected behavior. Consult your Anyscale account team before making these changes.

### Workload isolation[​](#workload-isolation "Direct link to Workload isolation")

Anyscale Clouds can be considered soft isolation containers within the Anyscale organization. Because multiple clouds can be deployed in the same organization, customers can deploy clouds in multiple cloud provider regions and accounts. The ability to deploy workloads using a common interface makes it easy to promote workloads from development to staging to production clouds hosted in separate environments with access to different data stores. Additionally, using clouds as an isolation boundary minimizes the risk of resource contention within an account while reducing security risks.

Wherever possible, deploy Anyscale clouds into dedicated environments for further isolation.

### Packages, patching, and vulnerability management (in the data plane)[​](#packages-patching-and-vulnerability-management-in-the-data-plane "Direct link to Packages, patching, and vulnerability management (in the data plane)")

Anyscale Clusters can run with a specified [container image](/container-image.md) that is considered immutable after build time. Upon cluster launch, setup scripting downloads the necessary packages and software required to run the managed Ray clusters; this includes Anyscale components. Customers have the ability to further install or update packages within the cluster based on application specifications. The customer is responsible for terminating clusters that fall out of policy with their governance models and/or updating container images to include the latest security patches.

For more information about the packages installed in the Anyscale base images, see the [documentation references](/admin/cloud.md).

### Ray versioning[​](#ray-versioning "Direct link to Ray versioning")

Ray clusters are launched with a specific version of Ray that is specified at runtime. Anyscale and Ray capabilities continue to evolve and improve in terms of capabilities, observability, and performance. The customer is responsible for ensuring that Ray workloads are running supported versions of Ray on Anyscale.

### Protecting sensitive data[​](#protecting-sensitive-data "Direct link to Protecting sensitive data")

Customers are responsible for ensuring that their sensitive data is not unintentionally exposed. Customers should ensure that text that is shown in plain text (that is cloud names, environment variables, etc.) does not contain any sensitive information. Additionally, customers should ensure that appropriate access restrictions and logging mechanisms are deployed on their data stores to prevent access or unauthorized data movement.

### Secret management[​](#secret-management "Direct link to Secret management")

Secrets are a common component of many modern applications, however Anyscale doesn't provide a native mechanism for secrets management. Customers should leverage centralized secrets management solutions to prevent storing secrets as environment variables in container images. Container images are by default visible to users within the customer account. Additional IAM policies can be attached to the IAM roles associated to Ray clusters to access cloud service provider hosted secret management solutions. See [Secret management on Anyscale](/secrets.md).
