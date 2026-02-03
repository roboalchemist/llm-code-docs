# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/medstack-migration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MedStack to Aptible Migration Guide

> Learn how to migrate resources from MedStack to Aptible

# Overview

[Aptible](https://www.aptible.com/) is a PaaS (Platform as a Service) that provides developers with managed infrastructure and everything that they need to launch and scale apps that are secure, reliable, and compliant — with no need to manage infrastructure.

This guide will cover the differences between MedStack Control and Aptible and suggestions for how to migrate applications and resources.

# PaaS concepts

### Environment separation

In MedStack, environment separation is done using Clusters. In Aptible, data can be isolated using [Stacks](https://www.aptible.com/docs/core-concepts/architecture/stacks#stacks) and [Environments](https://www.aptible.com/docs/core-concepts/architecture/environments).

**Stacks**: A Stack in Aptible is most closely equivalent to a Cluster in MedStack. A Stack is an isolated network that contains the infrastructure required to run apps and databases on Aptible. A Shared Stack is a stack suitable for non-production workloads that do not contain PHI.

**Environments**: An Environment is a logical separation of resources. It can be used to group resources used in different stages of development (e.g., staging vs. prod) or to apply role-based permissions.

### Orchestration

In MedStack, orchestration is done via Docker Swarm. Aptible uses a built-in orchestration model that requires less management — you specify the size and number of containers to use for your application, and Aptible manages the allocation to underlying infrastructure nodes automatically. This means that you don’t have direct access to Nodes or resource pinning, but you don’t have to manage your resources in a way that requires access.

### Applications

In Aptible, you can **set up** applications via Git-based deploys where we build your Docker image based on your provided Dockerfile, or based on your pre-built Docker image, and define service name and command in a Procfile as needed. Configurations can be set in the UI or through the CLI.

To **deploy** the application, you can use `aptible deploy` or you can set up CI/CD for automated deployments from a repository.

To **scale** an application, you can use manual horizontal scaling (number of containers) and vertical scaling (size and profile of container). We also offer vertical and horizontal autoscaling, both available in beta.

### Databases and storage

MedStack is built on top of Azure. Aptible is built on top of AWS.

Our **managed database** offerings include support for PostgreSQL and MySQL, as well as other databases such as Redis, MongoDB, and [more](https://www.aptible.com/docs/core-concepts/managed-databases/overview). If you currently host any of the latter as database containers, you can host them as managed databases in Aptible.

Aptible doesn’t yet support **object storage**; for that, we recommend maintaining your storage in Azure and setting up connections from your hosted application in Aptible. For support for persistent volumes, please reach out to us.

### Downtime mitigation

Aptible’s [release process](https://www.aptible.com/docs/core-concepts/apps/deploying-apps/releases/overview#lifecycle) minimizes downtime while optimizing for container health. The platform runs [container health checks](https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#health-check-lifecycle) during deployment and throughout the lifetime of the container.

### Metrics and logs

Aptible provides container [metrics](https://www.aptible.com/docs/core-concepts/observability/metrics/overview) and [logs](https://www.aptible.com/docs/core-concepts/observability/logs/overview) as part of the platform. You can view these within the Aptible UI, or you can set up [metrics](https://www.aptible.com/docs/core-concepts/observability/metrics/metrics-drains/overview) and [logs drains](https://www.aptible.com/docs/core-concepts/observability/logs/log-drains/overview) to your preferred destination.

# Compliance

**Compliance frameworks**: Aptible’s platform is designed to help businesses meet strict data privacy and security requirements. We offer built-in guardrails and infrastructure security controls that comply with the requirements of compliance frameworks such as HIPAA, HITRUST, PIPEDA, and [more](https://trust.aptible.com/). Compliance is built into how Aptible manages infrastructure, so no additional work is required to ensure that your application is compliant.

**Audit support**: We offer a [Security & Compliance dashboard](https://www.aptible.com/docs/core-concepts/security-compliance/security-compliance-dashboard/overview) that covers documentation and proof of infrastructure controls in the case of an audit.

**Security questionnaires**: In general, we don’t fill out security questionnaires on behalf of our customers. The Security & Compliance dashboard can be used as a resource to answer questionnaires. Our support team is available to answer specific one-off questions when needed.

# Pricing

MedStack’s pricing is primarily based on a platform fee with added pass-through infrastructure costs. Aptible’s pricing model differs slightly. Plan costs are mainly based on infrastructure usage, with a small platform fee for some plans.

Most companies will want to leverage our Production plan, which starts with a \$499/mo base fee and additional unit-based costs for resources.

For more details, see our [pricing page](https://www.aptible.com/pricing).

During the migration period, we will provide an extended free trial to allow you to leverage the necessary capabilities to try out and validate a migration of your services.

# Migrating a MedStack service to Aptible

This section walks through how to replicate and test your service on Aptible, prepare your database migration, and plan and execute a production migration plan.

### Create an Aptible account

* Create an Aptible account ([https://app.aptible.com/signup](https://app.aptible.com/signup)). Use a company email so that you automatically qualify for a free trial.
* Message Aptible support at [support@aptible.com](mailto:support@aptible.com) to let us know that you’re a MedStack customer and have created a trial account, and we will remove some customary resource limits from the free trial so that you can make a full deployment, validate for functionality, and estimate your pricing on Aptible.

### Replicate a MedStack staging service on Aptible

* [Create an Environment](https://www.aptible.com/docs/how-to-guides/platform-guides/create-environment#how-to-create-environments) in one of the available Stacks in your account
* Create required App(s): an Aptible App may contain one or more services that utilize the same Docker image
  * An App with multiple services can be defined using the [Procfile](https://www.aptible.com/docs/how-to-guides/app-guides/define-services#step-01-providing-a-procfile) standard
    * The Procfile file should be placed at **`/.aptible/Procfile`** in your pre-built Docker image
* Add any pre or post-release commands to [.aptible.yml](https://www.aptible.com/docs/core-concepts/apps/deploying-apps/releases/aptible-yml):
  * `before_release` is a common place to put commands like database migration tasks
  * .aptible.yml should be placed in **`/.aptible/.aptible.yml`** in your pre-built Docker image
* Set up config variables
  * Aptible makes use of environment variables to configure your apps. These settings can be modified via the [Aptible CLI](https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-config-set) via `aptible config:set` or via the Configuration tab of your App in the web dashboard
* Add credentials for your Docker registry source
  * Docker credentials can be [provided via the command line](https://www.aptible.com/docs/core-concepts/apps/deploying-apps/image/deploying-with-docker-image/overview#private-registry-authentication) as arguments with the `aptible deploy` command
  * They can also be provided as secrets in your CI/CD workflow ([Github Actions Example](https://www.aptible.com/docs/how-to-guides/app-guides/how-to-deploy-aptible-ci-cd#deploying-with-docker))

### Deploy and validate your staging application

* Deploy your application using:
  * [`aptible deploy`](https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-deploy#aptible-deploy) for Direct Docker Deployment using the Aptible CLI
  * Github Actions ([example](https://www.aptible.com/docs/how-to-guides/app-guides/how-to-deploy-aptible-ci-cd#deploying-with-docker))
  * Or, via git push if you are having us build your Docker Image by providing a Dockerfile in your git repo
* Add Endpoint(s)
  * An [Aptible Endpoint](https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/overview) provides load balancer functionality for your App’s services.
  * We support a [“default domain” endpoint](https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/default-domain) where you can have an [on-aptible.com](http://on-aptible.com) domain used for your test services without configuring a custom domain.
  * You can also configure [custom domain Endpoints](https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#custom-domain), for which we can automatically provision certificates, or you can bring your own custom SSL certificates.
* Validate your App(s)

### Prepare your database migration

* Test the migration of your database to Aptible
  * This can be done via dump and restore methods:
    * PostgreSQL: using pg\_dump
    ```ruby  theme={null}
    pg_dump -h [source_host] -p [source_port] -U [source_user] -W [source_database] > source_db_dump.sql

    psql -h [destination_host] -p [destination_port] -U [destination_user] -W [destination_database] < source_db_dump.sql
    ```

### Complete your Aptible setup

* Familiarize yourself with Aptible [activity](https://www.aptible.com/docs/core-concepts/observability/activity), [logs](https://www.aptible.com/docs/core-concepts/observability/logs/overview), [metrics](https://www.aptible.com/docs/core-concepts/observability/metrics/overview#metrics)
* (Optional) Set up [log](https://www.aptible.com/docs/core-concepts/observability/logs/log-drains/overview#log-drains) and [metric drains](https://www.aptible.com/docs/core-concepts/observability/metrics/metrics-drains/overview)
* Invite your team and [set up roles](https://www.aptible.com/docs/core-concepts/security-compliance/access-permissions)
* [Contact Aptible Support](https://contact.aptible.com/) to validate your production migration plan and set up a [Dedicated Stack](https://www.aptible.com/docs/core-concepts/architecture/stacks#dedicated-stacks-isolated) to host your production resources.

### Plan, Test and Execute the Migration

* Plan for the downtime required to migrate the database and perform DNS cutover for services behind load balancers to Aptible Endpoints. The total estimated downtime can be calculated by performing test database migrations and rehearsing manual migration steps.
* Key Points to consider in the Migration plan:
  * Be able to put app(s) in maintenance mode: before migrating databases for production systems, have a method available to ensure that no app services are connecting to the database for writes. Barring this, at least be able to scale app services to zero containers to take the app offline.
  * Consider modifying the DNS TTL on the records to be modified to value of 5 minutes or less.
  * Perform the database migration, and enable the Aptible app, potentially using a secondary [Default Domain Endpoint](https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/default-domain) for testing, or using local /etc/hosts to override DNS temporarily.
  * Once the validation is complete, make the DNS record change to point your domain records to the new Aptible destination(s).
  * Monitor logs to ensure that requests transition fully to the Aptible Endpoint(s) (observe that requests cease at the MedStack Load Balancer, and appear in logs at the Aptible Endpoint).
