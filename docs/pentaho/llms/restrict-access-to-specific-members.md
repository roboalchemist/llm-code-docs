# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/restrict-access-to-specific-members.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/restrict-access-to-specific-members.md

# Restrict Access to Specific Members

You can restrict access to parts of a schema by implementing an element to define access to a hierarchy.

Access is restricted to parts of a schema by implementing the **\<HierarchyGrant>** element to define access to a hierarchy, as shown in the following example:

```xml
<Role name="California manager">
    <SchemaGrant access="none">
        <CubeGrant cube="Sales" access="all">
            <HierarchyGrant hierarchy="[Store]" access="custom" topLevel="[Store].[Store Country]">
                <MemberGrant member="[Store].[USA].[CA]" access="all"/>
                <MemberGrant member="[Store].[USA].[CA].[Los Angeles]" access="none"/>
            </HierarchyGrant>
            <HierarchyGrant hierarchy="[Customers]" access="custom" topLevel="[Customers].[State Province]" bottomLevel="[Customers].[City]">
                <MemberGrant member="[Customers].[USA].[CA]" access="all"/>
                <MemberGrant member="[Customers].[USA].[CA].[Los Angeles]" access="none"/>
            </HierarchyGrant>
            <HierarchyGrant hierarchy="[Gender]" access="none"/>
        </CubeGrant>
    </SchemaGrant>
</Role>
```

The **access** attribute can be one of the following types:

* all: all members are visible.
* none: the hierarchy's very existence is hidden from the user.
* custom: customized to your own specifications.

With custom access, you can use the `topLevel` attribute to define the highest visible level (preventing users from seeing too much of the 'big picture,' such as viewing revenues rolled up to the Store or Country level); or use the `bottomLevel` attribute to define the lowest visible level (preventing users from looking at an individual customer's details); or control which sets of members a user can see by defining nested `<MemberGrant>` elements.

You can only define a `<MemberGrant>` element if its enclosing `<HierarchyGrant>` has `access="custom"`. Member grants give (or remove) access to a given member and all of its children. Here are the rules:

* Members inherit access from their parents. If you deny access to California, you will not be able to see San Francisco.
* Grants are order-dependent. If you grant access to USA, then deny access to Oregon, then you will not be able to see Oregon or Portland. But if you were to deny access to Oregon, then grant access to USA, you can effectively see everything.
* A member is visible if any of its children are visible. Suppose you deny access to USA, then grant access to California. You will be able to see USA, and California, but none of the other states. The totals against USA will still reflect all states, however.
* Member grants don't override the hierarchy grant's top- and bottom-levels. If you set `topLevel="[Store].[Store State]"`, and grant access to California, you will not be able to see USA.
