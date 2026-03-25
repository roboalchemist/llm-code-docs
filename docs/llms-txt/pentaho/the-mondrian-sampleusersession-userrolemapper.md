# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server/the-mondrian-sampleusersession-userrolemapper.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server/the-mondrian-sampleusersession-userrolemapper.md

# The Mondrian-SampleUserSession-UserRoleMapper

This mapper retrieves OLAP schema roles from a named HTTP session variable. In the below example, the session is stored in a variable called **MondrianUserRoles**.

```xml
<bean id="Mondrian-UserRoleMapper"
    name="Mondrian-SampleUserSession-UserRoleMapper"
    class="org.pentaho.platform.plugin.action.mondrian.mapper.
    MondrianUserSessionUserRoleListMapper"
    scope="singleton">
        <property name="sessionProperty" value="MondrianUserRoles" />
</bean>
```
