# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server/the-mondrian-samplelookupmap-userrolemapper.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server/the-mondrian-samplelookupmap-userrolemapper.md

# The Mondrian-SampleLookupMap-UserRoleMapper

This mapper provides a translation table (in the form of a `<map>` element) to associate Pentaho Server roles with OLAP schema roles. The lookups take the form of key/value pairs where the key is the Pentaho Server's Business Analytics role, and the value is the OLAP schema role. In the example below, the `ceo` role in the Pentaho Server maps to the `California manager` role in the schema.

```xml
<bean id="Mondrian-UserRoleMapper"
        name="Mondrian-SampleLookupMap-UserRoleMapper"
        class="org.pentaho.platform.plugin.action.mondrian.mapper.
        MondrianLookupMapUserRoleListMapper"
        scope="singleton">
    <property name="lookupMap">
        <map>
            <entry key="ceo" value="California manager" />
            <entry key="cto" value="M_CTO" />
            <entry key="dev" value="M_DEV" />
        </map>
    </property>
</bean>
```
