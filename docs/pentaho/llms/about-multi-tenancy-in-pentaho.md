# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/multi-tenancy/about-multi-tenancy-in-pentaho.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/multi-tenancy/about-multi-tenancy-in-pentaho.md

# About multi-tenancy in Pentaho

## What is multi-tenancy?

Multi-tenancy is an architecture in which individuals or groups share the same instance of a software application, but have separate data and content. These multiple individuals or groups are referred to as tenants. In a multi-tenancy architecture, customers share infrastructures, applications, or databases to gain performance advantages while reducing overhead. A provider defines the rules for the tenants within the system. Each tenant can be restricted to see only her own secure data and content while using the same software. Note that multi-tenancy differs from multi-instance architecture which is based on maintaining separate copies of the software to serves separate clients.

The focus of this article is to explain how multi-tenancy is achieved using Pentaho Enterprise Business Analytics software.

## Multi-tenancy in Pentaho

Pentaho has three categories of multi-tenancy:

* **Data multi-tenancy**

  allows developers and integrators to apply custom security and business rules to control access to data.
* **Content multi-tenancy**

  separates content, such as reports and folders, among tenants.
* **UI multi-tenancy**

  presents different styles of the user interface for each tenant.

There are two required components to make multi-tenancy work. Users need to be associated with tenants via roles, tenant IDs, or other identifiers which indicate what content and data users see. Similarly, there must be something in the data that can be used to restrict access. The combination of user information and data make the multi-tenancy approaches described here possible. Since these approaches are data model and data-driven, they are very flexible.

## Preparing for multi-tenancy in Pentaho

Before you can apply multi-tenancy to your Pentaho system, you need to associate users to a tenant. The most likely methods are to assign a specific role to users who belong to the same tenant or to designate a session variable which identifies the tenant ID. Other approaches include associating users with some data, such as geographic region or business unit. The association of a user with tenant identifiers is accomplished through one of the following approaches:

* The user information can be set via single sign-on if it is used. This approach has the advantage of requiring a single point to set user ID, roles, and tenant info. However, if users will be scheduling their own content, this approach will not work because the SSO filter is not called by the scheduler.
* A session startup action that is run when a user session is created. The advantage to this approach is that the action is called by the scheduler. The downside is that an action sequence is required, which means understanding a new technology.

You can use an action sequence to add an indicator to the user's session which identifies the user as a member of the tenant.
