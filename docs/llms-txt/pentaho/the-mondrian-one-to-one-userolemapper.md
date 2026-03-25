# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server/the-mondrian-one-to-one-userolemapper.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server/the-mondrian-one-to-one-userolemapper.md

# The Mondrian One-To-One UseRoleMapper

The **Mondrian-One-To-One-UserRoleMapper** maps each role name in the Pentaho Server to roles defined in the OLAP schema. Therefore, the mapper assumes that the roles defined in your OLAP schema are mirrored in the Pentaho Server. For example, if you have a role called `CTO` in your schema, and a role called `CTO`in the Pentaho Server, this role mapper would be appropriate.

```xml
<bean id="Mondrian-UserRoleMapper"
name="Mondrian-One-To-One-UserRoleMapper"
class="org.pentaho.platform.plugin.action.mondrian.mapper​.MondrianOneToOneUserRoleListMapper"
scope="singleton" />
```
