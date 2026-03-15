# Source: https://docs.firehydrant.com/docs/service-catalog-basics.md

# Service Catalog Basics

## What is a Service Catalog?

A Service Catalog is a detailed list of the technical services (enterprise applications, task-specific tools, microservices, and so on) used by your organization internally and externally. Cataloging—and tracking changes to—all of the services within your system can immensely help streamline your incident management processes.

FireHydrant's Service Catalog configuration options, including the ability to ingest services and service metadata from third-party systems, make it easy to set up a detailed record of all your services and automatically refresh data about each service.

A major benefit of the Service Catalog is that it lets you track which incidents affect services. This allows customizing how you respond to incidents based on the services impacted.

### Service Catalog Categories

Within FireHydrant, your Service Catalog is divided into four main categories:

* Environments
* Functionalities
* Services
* Change Events

By detailing different services, functionalities, environments, and change events, you create a way to track your digital properties. When these properties are well-cataloged, you can quickly determine where an incident occurs.

> 📘 Note:
>
> You can also access your service catalog programmatically using [FireHydrant's API](https://developers.firehydrant.com/) or via Configuration-as-code with [Terraform](https://registry.terraform.io/providers/firehydrant/firehydrant/latest/docs).

## Environments

<Image alt="Creating an Environment from scratch" align="center" width="650px" src="https://files.readme.io/72b4668-image.png">
  Creating an Environment from scratch
</Image>

Environments are a generic way to break up your application. Some users may do this by region (for example, `us-east-1`), while others may use the development stage (for example, "Production" vs "Staging"), etc. It's flexible and completely dependent on your needs.

To create and manage environments: 

1. Navigate to **Catalog** in the navbar.
2. Click on **Environments**, **Add environment**, then **Start from scratch**.
3. Fill in the details and click "Create environment." Environments have the following fields:
   1. **Name** - The name of the environment
   2. **Description** - A description of the environment
   3. **Integration Links** - Link to external components from configured providers. Importing from a third party will automatically handle this linking. See [Import and Link Components](https://docs.firehydrant.com/docs/import-and-link-components) for more details.

## Functionalities

<Image alt="Creating a Functionality from scratch" align="center" width="650px" src="https://files.readme.io/baba790-image.png">
  Creating a Functionality from scratch
</Image>

Functionalities are best considered business functions or application capabilities and encompass many underlying technical services. For example, the "IAM & Login" Functionality might consist of `federation-service` and `authentication-service`.

To create and manage functionalities:

1. Navigate to **Catalog** in the navbar.
2. Click on **Functionalities**, **Add functionality** then **Start from scratch**.
3. Fill in the details and click "Create functionality." Functionalities have the following fields:
   1. **Name** - A name for the Functionality
   2. **Description** - A description of the Functionality
   3. **Related services** - The added capability with Functionalities is that they can be linked with Services. This allows you to declare a general issue (e.g., the User Interface is unresponsive) and automatically pull in related services and their teams to the incident.
   4. **Owning team** - Selecting an owning team for a Functionality restricts editing the Functionality to only members of that team (and Owners in your organization). To learn more, visit [Associating Teams](https://docs.firehydrant.com/docs/associating-teams).
   5. **Responding teams** - Teams expected to respond to any incidents involving this Functionality.
      1. **Auto-add responding team** - If at least one responding team is configured, you can check this option to automatically pull in the responding team(s) for this Functionality when an incident impacts it.
   6. **Labels** - Allows setting custom key-value metadata on components. Service Catalog labels are not to be confused with [Incident Labels](https://docs.firehydrant.com/docs/incident-labels), as they are separate.
   7. **External Links** - Allows setting any custom external links for this particular component. These links will always be visible when viewing this component in the UI.
   8. **Integration Links** - Functionalities can be linked to external components from third-party applications. If you import a Functionality from a third party, then this will automatically be configured according to which app you imported from. Otherwise, you can manually configure additional integration links here. To learn more, visit [Import and Link Components](https://docs.firehydrant.com/docs/import-and-link-components).
   9. **Automatically alert if added to an incident** - If you have this Functionality linked to an external component from an [alerting provider](/docs/integrations-overview#alerting-integrations), you can check this box to automatically page that linked component whenever this Functionality is added to an incident.

## Services

<Image alt="Creating a Service from scratch" align="center" width="650px" src="https://files.readme.io/d6e0d95-image.png">
  Creating a Service from scratch
</Image>

A service is a technical function within your system. Typically, one or more services will compose a Functionality and directly contribute to its function. It could be a microservice, a mono-repository, or a library you maintain. You can add services manually or ingest them into your service catalog.

To create and manage services:

1. Navigate to **Catalog** in the navbar.
2. Click on **Services**, **Add service**, then **Start from scratch**.
3. Fill in the details and click "Create service." Most of the fields here are identical to Functionalities above, so we will only list additional fields that are unique to Services:
   1. **Tier** - Service Tiers indicate the significance or importance of a Service for business operations. FireHydrant provides values from Tier 0 to Tier 5, where zero is business critical, and five is largely unimportant. People may also use Service Tiers to indicate how customer impacting a service is.
   2. **Functionalities** - The added capability with Services is that they can be linked with Functionalities. This allows you to declare a general issue with the linked Functionality, and this Service (and its responding team(s)) can automatically be added to the incident via the [Auto-Add Services Related to Functionality](https://docs.firehydrant.com/docs/runbook-step-auto-add-services-related-to-functionality) Runbook step.
   3. **Connected Checklists** - You can link Services with related [Readiness Checklists](https://docs.firehydrant.com/docs/readiness-checklists), which can be useful for ensuring Service incident readiness and compliance.

## Change Events

The vast majority of incidents and breakages occur due to changes in systems. FireHydrant allows tracking such events via Change Events. Change events can be associated with Services and Environments.

To learn more, visit [Change Events](https://docs.firehydrant.com/docs/change-events).

## Next Steps

Learn a bit more about specific Service Catalog capabilities:

* [Import and Link Components](https://docs.firehydrant.com/docs/import-and-link-components) goes into more detail about how to import and link components and what capabilities this unlocks
* [Associating Teams](https://docs.firehydrant.com/docs/associating-teams) provides more information about how to pull in the right people for particular components more quickly
* [Service Dependencies](https://docs.firehydrant.com/docs/service-dependencies) allow you to configure inter-service dependencies, which can be important to understand during incidents

In addition, there are other ways to manage your Service Catalog:

* You can populate your Service Catalog by ingesting details from a YAML in a repository. See our article about [Automatic Service Ingestion](https://docs.firehydrant.com/docs/automatic-service-ingestion)
* As mentioned above, you can also manage your Service Catalog via [API](https://developers.firehydrant.com/#/) as well as via [Terraform](https://registry.terraform.io/providers/firehydrant/firehydrant/latest/docs)