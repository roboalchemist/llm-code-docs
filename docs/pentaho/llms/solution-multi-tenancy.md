# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/multi-tenancy/solution-multi-tenancy.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/multi-tenancy/solution-multi-tenancy.md

# Solution multi-tenancy

The following sections discuss solution multi-tenancy:

* Roles and Access Control Lists (ACLs)
* Multi-Tenancy at the content level
* Custom voters
* Managing ACLs via a web service

## Roles and Access Control Lists (ACLs)

Pentaho uses roles and user IDs to enforce authorization to content in the solution repository. For multi-tenancy, roles are typically used instead of user IDs. A role for a user should be thought of as a piece of metadata about the user and is simply a group which the user belongs to. User roles are set as part of the authentication and identification process when a user logs in. For example, a user might be in the 'West and Sales Managers group'.

Access Control Lists (ACLs) are used to define which users or roles have access to content in the solution repository. As with roles, ACLs should be thought of as metadata about the repository content. An ACL might be that Sales Managers can read and edit content in the Sales Managers folder, but not delete it.

When a user attempts to perform a task with content, an ACL voter will determine if the user can perform the action. The voter compares the ACL against the user’s ID and roles to determine the user's access permissions. For example, if Sam is assigned the role of 'Sales Manager' and the Sales Manager role can read files in the Sales Managers folder, then Sam can see the content in that folder. However, Sam is not assigned the HR role, and since the HR folder is only viewable by users assigned the HR role, Sam cannot see the content in the HR folder.

For more information on roles and ACLs, see **Use Pentaho security** the **Pentaho Business Analytics** document.

This feature can be used for multi-tenancy as well. Each user is assigned a role which associates that user with a tenant-specific folder which only that user can see. There also may be folders which are viewable by all tenants. When a user logs on to the system, that user can only see shared folders and the folders for their tenant.

The approach described works for many cases, but does not accommodate complex access rules. For this reason, a better approach is often to use custom access voters. The next sections will describe how to create custom voters and how to manage ACLs without using the User Console.

## Multi-tenancy at the content level

You can use the ACL system to manage access to content by tenant. If content needs to be restricted by more complex rules such as by tenant and then by role within the tenant, you can create a custom access voter by implementing `IRepositoryAccessVoter`. The only method that needs to be implemented is the `hasAccess()` method.

#### Reference

IRepositoryAccessVoter: <https://javadoc.pentaho.com/bi-platform102/pentaho-platform-api-10.2.0.0-218-javadoc/org/pentaho/platform/api/repository2/unified/IRepositoryAccessVoter.html>

## Custom voters

Pentaho, through the Spring-based bean injection, allows you to apply a different AccessVoter, which can apply custom logic to determine access for users. For example, you may have common reports that all users can access based on roles, as well as solution folders for specific tenants or business units. The ACL can allow a user to see all the common reports, but only the tenant folders for which that user has access. Additional fine-grained access control rules can be added as needed. Therefore, it is possible to have more than one `AccessVoter` and to have them chained. All instances of AccessVoters are managed by `AccessVoterManager`. When implementing a new `AccessVoter`, consider the following:

* All users with the role of **Administrator** will bypass the `AccessVoter` logic.
* AccessVoters are chained, and their order is specified in the `repository.spring.xml` for the `repositoryAccessVoterManager` bean:

  ```xml
  <bean class="org.pentaho.platform.repository2.unified.RepositoryAccessVoterManager" id="repositoryAccessVoterManager">
    <constructor-arg ref="tenantedAccessVoter/>
    <constructor-arg ref="authorizationPolicy"/>
    <constructor-arg ref="repositoryAdminUsername"/>
  </bean>
  ```
* A user will have access to a resource if all AccessVoters in the chain allow access. The first `AccessVoter` in the chain that rejects access will break the chain, and the user will not have access to the resource.

To implement a new `AccessVoter`, you need to write a java class which implements `IRepositoryAccessVoter`. This interface is for all resources stored in Pentaho’s repository. The only method that needs to be implemented is the `hasAccess()` method, which is called for each object the user tries to access. In the following listing, the tenantid is retrieved from the session and then compared to the folder name. All tenants will have an individualized directory under `/public/tenants/*$\{tenantid\}*`. If the folder name matches the tenantid, the user is granted access; otherwise, access is denied.

```java
  public boolean hasAccess(RepositoryFile file, RepositoryFilePermission operation, 
                              RepositoryFileAcl acl, IPentahoSession session) {
     String tenantid = (String)session.getAttribute("tenantid");
     String [] topLevelDirs = getTopLevelDirNames(file);
     // a dir pattern name of /public/tenants/tenantid
     if ((topLevelDirs != null ) && (topLevelDirs.length > 3)) {  
        if ( "public".equals(topLevelDirs[1])) {
           if ("tenants".equals(topLevelDirs[2])) {
              return tenantid.equals(topLevelDirs[3]);
           }
        }
     }
     return true; // leave it up to the server level ACL 
  }

  protected String [] getTopLevelDirNames(RepositoryFile f){
      String fullpath = f.getPath();
      if (fullpath != null){
          String [] dirs = fullpath.split("/");
          return dirs;
      } else {
          return null;
      }
  }
```

## Managing ACLs via a web service

As a part of multi-tenant solution, there is often a need create and manage files and folders in an unattended fashion. Pentaho has `SolutionRepositoryService` with a RESTful interface that allows third party scripts and applications to create new folders as well as set ACLs. Detailed information on this service can be found in the Pentaho SDK package, which can be downloaded from the [Pentaho support site](https://support.pentaho.com/home).
