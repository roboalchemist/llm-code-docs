# Users

**Source:** [https://developer.wordpress.org/plugin/users/](https://developer.wordpress.org/plugin/users/)



# Users




## In this article


Table of Contents- Roles and Capabilities
- The Principle of Least Privileges



↑Back to top



AUseris an access account with corresponding capabilities within the WordPress installation. Each WordPress user has, at the bare minimum, a username, password and email address.


Once a user account is created, that user may log in using the WordPress Admin (or programmatically) to access WordPress functions and data. WordPress stores the Users in theuserstable.


## Roles and Capabilities


Users are assignedroles, and each role has a set ofcapabilities.


You can create new roles with their own set of capabilities. Custom capabilities can also be created and assigned to existing roles or new roles.


In WordPress, developers can take advantage of user roles to limit the set of actions an account can perform.


## The Principle of Least Privileges


WordPress adheres to the principal of least privileges, the practice of giving a useronlythe privileges that are essential for performing the desired work. You should follow this lead when possible by creating roles where appropriate and checking capabilities before performing sensitive tasks.





First published


September 24, 2014


Last updated


December 14, 2023



[PreviousWorking with Custom TaxonomiesPrevious: Working with Custom Taxonomies](https://developer.wordpress.org/plugins/taxonomies/working-with-custom-taxonomies/)
[NextRoles and CapabilitiesNext: Roles and Capabilities](https://developer.wordpress.org/plugins/users/roles-and-capabilities/)


