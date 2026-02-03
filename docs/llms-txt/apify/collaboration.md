# Source: https://docs.apify.com/platform/collaboration.md

# Collaboration

**Learn how to collaborate with other users and manage permissions for organizations or private resources such as Actors, Actor runs, and storages.**

***

Apify was built from the ground up as a collaborative platform. Whether you’re publishing your Actor in Apify Store or sharing a dataset with a teammate, collaboration is deeply integrated into how Apify works. You can share your resources (like Actors, runs, or storages) with others, manage permissions, or invite collaborators to your organization. By default, each system resource you create is only available to you, the owner. However, you can grant access to other users, making it easy to collaborate effectively and securely.

While most resources can be shared by assigning permissions (see [Access Rights](https://docs.apify.com/platform/collaboration/access-rights.md)), some resources can also be shared simply by using their unique links or IDs. There are two types of resources in terms of sharing:

* *Resources that require explicit access by default:*

  * [Actors](https://docs.apify.com/platform/actors/running.md), [tasks](https://docs.apify.com/platform/actors/running/tasks.md)
  * Can be shared only by inviting collaborators using [Access Rights](https://docs.apify.com/platform/collaboration/access-rights.md)) or using [Organization Accounts](https://docs.apify.com/platform/collaboration/organization-account.md)

* *Resources supporting both explicit access and link sharing:*

  * Actor runs, Actor builds and storage resources (datasets, key-value stores, request queues)
  * Can be shared by inviting collaborators or simply by sharing a unique direct link

You can control access to your resources in four ways:

|                                                                                                         |                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[Access rights](https://docs.apify.com/platform/collaboration/access-rights.md)**                     | Enables you to grant access to another user for a certain resource you own. This way, you can share results with your client, or two engineers can collaborate on developing one Actor.                                                                                                                                                                |
| **[Share resources by link](https://docs.apify.com/platform/collaboration/general-resource-access.md)** | Certain resources (runs, builds and storages) can by shared just by their link. Anyone with their ID is able to access them. This is configurable via [General resource access](https://docs.apify.com/platform/collaboration/general-resource-access.md)                                                                                              |
| **[Organization account](https://docs.apify.com/platform/collaboration/organization-account.md)**       | Apify's organization account allows multiple engineers to collaborate on team projects with role-specific access permissions.                                                                                                                                                                                                                          |
| **[Publishing in Apify Store](https://docs.apify.com/platform/actors/publishing.md)**                   | Another way to share your Actor with other users is to publish it in [Apify Store](https://apify.com/store). When publishing your Actor, you can make it a Paid Actor and get paid by the users benefiting from your tool. For more information, read the [publishing and monetization](https://docs.apify.com/platform/actors/publishing.md) section. |
