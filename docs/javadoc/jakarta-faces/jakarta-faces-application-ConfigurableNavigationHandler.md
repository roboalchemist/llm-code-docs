Package jakarta.faces.application

# Class ConfigurableNavigationHandler

java.lang.Object
jakarta.faces.application.NavigationHandler
jakarta.faces.application.ConfigurableNavigationHandler

Direct Known Subclasses:
`ConfigurableNavigationHandlerWrapper`

---

@Deprecated(since="5.0",
            forRemoval=true)
public abstract class ConfigurableNavigationHandler
extends NavigationHandler
Deprecated, for removal: This API element is subject to removal in a future version.
Use `NavigationHandler` instead. The methods have been merged.

 **ConfigurableNavigationHandler** extends the contract of
 `NavigationHandler` to allow runtime inspection of the `NavigationCase`s that make up the rule-base for
 navigation. An implementation compliant with the version of the specification in which this class was introduced (or
 a later version) must make it so that its `NavigationHandler` is an extension of this class.

Since:
2.0

-

## Constructor Summary

Constructors

Constructor
Description
`ConfigurableNavigationHandler()`

Deprecated, for removal: This API element is subject to removal in a future version.

-

## Method Summary

Modifier and Type
Method
Description
`abstract NavigationCase`
`getNavigationCase(FacesContext context,
 String fromAction,
 String outcome)`

Deprecated, for removal: This API element is subject to removal in a future version.

 Return the `NavigationCase` representing the navigation that would be taken had
 `NavigationHandler.handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case.

`NavigationCase`
`getNavigationCase(FacesContext context,
 String fromAction,
 String outcome,
 String toFlowDocumentId)`

Deprecated, for removal: This API element is subject to removal in a future version.

 Return the `NavigationCase` representing the navigation that would be taken had
 `NavigationHandler.handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case.

`abstract Map<String,Set<NavigationCase>>`
`getNavigationCases()`

Deprecated, for removal: This API element is subject to removal in a future version.

 Return a `Map<String,
 Set<NavigationCase>>` where the keys are `<from-view-id>` values and the values are
 `Set<NavigationCase>` where each element in the Set is a `NavigationCase` that applies to
 that `<from-view-id>`.

`void`
`inspectFlow(FacesContext context,
 Flow flow)`

Deprecated, for removal: This API element is subject to removal in a future version.

 Called by the flow system to cause the flow to be inspected for navigation rules.

`void`
`performNavigation(String outcome)`

Deprecated, for removal: This API element is subject to removal in a future version.

 A convenience method to signal the Jakarta Faces implementation to perform navigation with the provided
 outcome.

### Methods inherited from class jakarta.faces.application.NavigationHandler

`handleNavigation, handleNavigation`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ConfigurableNavigationHandler

public ConfigurableNavigationHandler()
Deprecated, for removal: This API element is subject to removal in a future version.

-

## Method Details

-

### getNavigationCase

public abstract NavigationCase getNavigationCase(FacesContext context,
 String fromAction,
 String outcome)
Deprecated, for removal: This API element is subject to removal in a future version.

 Return the `NavigationCase` representing the navigation that would be taken had
 `NavigationHandler.handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case.

Overrides:
`getNavigationCase` in class `NavigationHandler`
Parameters:
`context` - The `FacesContext` for the current request
`fromAction` - The action binding expression that was evaluated to retrieve the specified outcome, or
 `null` if the outcome was acquired by some other means
`outcome` - The logical outcome returned by a previous invoked application action (which may be `null`)
Returns:
the navigation case, or `null`.
Throws:
`NullPointerException` - if `context` is `null`
Since:
2.0

-

### getNavigationCase

public NavigationCase getNavigationCase(FacesContext context,
 String fromAction,
 String outcome,
 String toFlowDocumentId)
Deprecated, for removal: This API element is subject to removal in a future version.

 Return the `NavigationCase` representing the navigation that would be taken had
 `NavigationHandler.handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case. Implementations that comply the version of the specification in which this method was introduced must
 override this method. For compatibility with decorated implementations that comply with an earlier version of the
 specification, an implementation is provided that simply calls through to
 `getNavigationCase(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)`, ignoring the
 `toFlowDocumentId` parameter.

Overrides:
`getNavigationCase` in class `NavigationHandler`
Parameters:
`context` - The `FacesContext` for the current request
`fromAction` - The action binding expression that was evaluated to retrieve the specified outcome, or
 `null` if the outcome was acquired by some other means
`outcome` - The logical outcome returned by a previous invoked application action (which may be `null`)
`toFlowDocumentId` - The value of the `toFlowDocumentId` property for the navigation case (which may be
 `null`)
Returns:
the navigation case, or `null`.
Throws:
`NullPointerException` - if `context` is `null`
Since:
2.2

-

### getNavigationCases

public abstract Map<String,Set<NavigationCase>> getNavigationCases()
Deprecated, for removal: This API element is subject to removal in a future version.

 Return a `Map<String,
 Set<NavigationCase>>` where the keys are `<from-view-id>` values and the values are
 `Set<NavigationCase>` where each element in the Set is a `NavigationCase` that applies to
 that `<from-view-id>`. The implementation must support live modifications to this `Map`.

Overrides:
`getNavigationCases` in class `NavigationHandler`
Returns:
a map with navigation cases.
Since:
2.0

-

### performNavigation

public void performNavigation(String outcome)
Deprecated, for removal: This API element is subject to removal in a future version.

 A convenience method to signal the Jakarta Faces implementation to perform navigation with the provided
 outcome. When the NavigationHandler is invoked, the current viewId is treated as the "from viewId" and the "from
 action" is null.

Overrides:
`performNavigation` in class `NavigationHandler`
Parameters:
`outcome` - the provided outcome.
Throws:
`IllegalStateException` - if this method is called after this instance has been released

-

### inspectFlow

public void inspectFlow(FacesContext context,
 Flow flow)
Deprecated, for removal: This API element is subject to removal in a future version.

 Called by the flow system to cause the flow to be inspected for navigation rules. For backward compatibility with
 earlier implementations, an empty method is provided.

Overrides:
`inspectFlow` in class `NavigationHandler`
Parameters:
`context` - the Faces context.
`flow` - the flow.
Since:
2.2
