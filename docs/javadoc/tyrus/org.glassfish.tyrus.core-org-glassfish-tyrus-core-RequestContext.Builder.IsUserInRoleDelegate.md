Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Interface RequestContext.Builder.IsUserInRoleDelegate

Enclosing class:
`RequestContext.Builder`

---

public static interface RequestContext.Builder.IsUserInRoleDelegate
Is user in role delegate.

 Cannot easily query ServletContext or HttpServletRequest for this information, since it is stored only as
 object.

-

## Method Summary

Modifier and Type
Method
Description
`boolean`
`isUserInRole(String role)`

Returns a boolean indicating whether the authenticated user is included in the specified logical "role".

-

## Method Details

-

### isUserInRole

boolean isUserInRole(String role)
Returns a boolean indicating whether the authenticated user is included in the specified logical "role".
 Roles and role membership can be defined using deployment descriptors. If the user has not been
 authenticated, the method returns false.

Parameters:
`role` - a String specifying the name of the role.
Returns:
a boolean indicating whether the user making this request belongs to a given role; false if the
 user has not been authenticated.
