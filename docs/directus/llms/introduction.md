# Source: https://directus.io/docs/raw/cloud/getting-started/introduction.md

# Directus Cloud

> Whether you're a hobbyist, startup, or enterprise, our flexible Directus Cloud platform lets you get up and running with Directus quickly.

Whether you're a hobbyist, startup, or enterprise, our flexible Directus Cloud platform lets you get up and running with Directus quickly. We do all the heavy lifting of managing your infrastructure and software updates.

[Directus Cloud](https://directus.cloud) is a hosting platform for [Directus projects](/cloud/projects/create) which handles data storage, hosting, updates and scalability so you can focus on building your digital apps and experiences. There are three tiers of cloud projects: Starter, Professional, and Enterprise.

<cta-cloud>



</cta-cloud>

The Cloud Dashboard is allows you to manage three key components: accounts, [teams](/cloud/getting-started/teams), and [projects](/cloud/projects/create). Once logged in to Directus Cloud, create or join a team, and your account will become a member of that team. Once that's complete, you can create projects within a team.

Accounts can be members on multiple teams. All team members have permissions to manage the team's projects, including billing, other team members, and the team itself. Teams can have multiple team members and multiple projects. Projects can only be managed by one team and cannot be transferred to new teams.

## Project Tiers

<table>
<thead>
  <tr>
    <th>
      
    </th>
    
    <th>
      Starter
    </th>
    
    <th>
      Professional
    </th>
    
    <th>
      Enterprise
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Included Studio Users
    </td>
    
    <td>
      1
    </td>
    
    <td>
      5
    </td>
    
    <td>
      Contact us
    </td>
  </tr>
  
  <tr>
    <td>
      API Requests
    </td>
    
    <td>
      50,000
    </td>
    
    <td>
      250,000
    </td>
    
    <td>
      *
    </td>
  </tr>
  
  <tr>
    <td>
      Database Entries
    </td>
    
    <td>
      5,000
    </td>
    
    <td>
      75,000
    </td>
    
    <td>
      *
    </td>
  </tr>
  
  <tr>
    <td>
      Maximum Studio Users
    </td>
    
    <td>
      5
    </td>
    
    <td>
      15
    </td>
    
    <td>
      *
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Support**<br />


Enterprise projects include support from the Directus team.

</callout>

### Multi-tenancy

Tenancy refers to how client data is stored within a database. In single-tenancy architecture, a database stores data from only one tenant. In multi-tenancy architecture, a database stores data from multiple tenants, with mechanisms in place to protect data privacy. In the context of Directus Cloud, each project represents a tenant.

**Non-Enterprise Projects**

Professional projects are created using a multi-tenant architecture. However, if your neighbor's project gets busy, it will not impact your project, because each professional project is scoped to one container per project with dedicated minimum resources.

Projects also have the ability to scale beyond this minimum allocation based on currently available resources within the multi-tenant pool. However, these additional resources are not guaranteed and are offered on a dynamic first-come, first-serve basis. For end-to-end, single-tenant infrastructure with fully dedicated resources, [contact us about our enterprise tier](https://directus.io/contact)

**Enterprise**

Databases on enterprise projects are single-tenant, 100% dedicated to your project - no neighbors! Ready to upgrade to enterprise? [Contact us](https://directus.io/contact).

<callout icon="material-symbols:info-outline">

This section refers to how your cloud project is stored alongside other cloud projects and has nothing to do with how you design your project's data model. You can implement single or multi-tenant architecture within any Directus Cloud project.

</callout>
