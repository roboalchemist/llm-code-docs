Package jakarta.faces.application

# Class NavigationHandler

java.lang.Object
jakarta.faces.application.NavigationHandler

Direct Known Subclasses:
`ConfigurableNavigationHandler`, `NavigationHandlerWrapper`

---

public abstract class NavigationHandler
extends Object

 A **NavigationHandler** is passed the
 outcome string returned by an application action invoked for this application, and will use this (along with related
 state information) to choose the view to be displayed next.

 A default implementation of `NavigationHandler` must be provided by the Jakarta Faces
 implementation, which will be utilized unless `setNavigationHandler()` is called to establish a different
 one. An implementation of this class must be thread-safe. This default
 instance will compare the view identifier of the current view, the specified action binding, and the specified
 outcome against any navigation rules provided in `faces-config.xml` file(s). If a navigation case matches,
 the current view will be changed by a call to `FacesContext.setViewRoot()`. Note that a `null`
 outcome value will never match any navigation rule, so it can be used as an indicator that the current view should be
 redisplayed.

-

## Constructor Summary

Constructors

Constructor
Description
`NavigationHandler()`

-

## Method Summary

Modifier and Type
Method
Description
`NavigationCase`
`getNavigationCase(FacesContext context,
 String fromAction,
 String outcome)`

 Return the `NavigationCase` representing the navigation that would be taken had
 `handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case.

`NavigationCase`
`getNavigationCase(FacesContext context,
 String fromAction,
 String outcome,
 String toFlowDocumentId)`

 Return the `NavigationCase` representing the navigation that would be taken had
 `handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case.

`Map<String,Set<NavigationCase>>`
`getNavigationCases()`

 Return a `Map<String,
 Set<NavigationCase>>` where the keys are `<from-view-id>` values and the values are
 `Set<NavigationCase>` where each element in the Set is a `NavigationCase` that applies to
 that `<from-view-id>`.

`abstract void`
`handleNavigation(FacesContext context,
 String fromAction,
 String outcome)`

 Perform navigation processing based on the state information in the
 specified `FacesContext`, plus the outcome string returned by an executed application action.

`void`
`handleNavigation(FacesContext context,
 String fromAction,
 String outcome,
 String toFlowDocumentId)`

 Overloaded variant of
 `handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` that allows the
 caller to provide the defining document id for a flow to be entered by this navigation.

`void`
`inspectFlow(FacesContext context,
 Flow flow)`

 Called by the flow system to cause the flow to be inspected for navigation rules.

`void`
`performNavigation(String outcome)`

 A convenience method to signal the Jakarta Faces implementation to perform navigation with the provided
 outcome.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### NavigationHandler

public NavigationHandler()

-

## Method Details

-

### handleNavigation

public abstract void handleNavigation(FacesContext context,
 String fromAction,
 String outcome)

 Perform navigation processing based on the state information in the
 specified `FacesContext`, plus the outcome string returned by an executed application action.

 If the implementation class also extends `ConfigurableNavigationHandler`, the implementation must guarantee
 that the logic used in a call to `ConfigurableNavigationHandler.getNavigationCase(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` is used in this method to
 determine the correct navigation.

 This method must set the render targets (used in partial rendering) to `render all` invoking
 `PartialViewContext.setRenderAll(boolean)`) if the view identifier has changed as the result of an
 application action (to take into account `Ajax requests`).

Parameters:
`context` - The `FacesContext` for the current request
`fromAction` - The action binding expression that was evaluated to retrieve the specified outcome, or
 `null` if the outcome was acquired by some other means
`outcome` - The logical outcome returned by a previous invoked application action (which may be `null`)
Throws:
`NullPointerException` - if `context` is `null`

-

### handleNavigation

public void handleNavigation(FacesContext context,
 String fromAction,
 String outcome,
 String toFlowDocumentId)

 Overloaded variant of
 `handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` that allows the
 caller to provide the defining document id for a flow to be entered by this navigation. For backward compatibility
 with decorated `NavigationHandler` implementations that conform to an earlier version of the specification, an
 implementation is provided that calls through to
 `handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)`, ignoring the
 `toFlowDocumentId` parameter.

Parameters:
`context` - The `FacesContext` for the current request
`fromAction` - The action binding expression that was evaluated to retrieve the specified outcome, or
 `null` if the outcome was acquired by some other means
`outcome` - The logical outcome returned by a previous invoked application action (which may be `null`)
`toFlowDocumentId` - The defining document id of the flow into which this navigation will cause entry.
Throws:
`NullPointerException` - if `context` is `null`

-

### getNavigationCase

public NavigationCase getNavigationCase(FacesContext context,
 String fromAction,
 String outcome)

 Return the `NavigationCase` representing the navigation that would be taken had
 `handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case.

 Historically this method was declared in `ConfigurableNavigationHandler` since 2.0.
 For backward compatibility with earlier implementations, a default implementation is provided which returns `null`.

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
5.0

-

### getNavigationCase

public NavigationCase getNavigationCase(FacesContext context,
 String fromAction,
 String outcome,
 String toFlowDocumentId)

 Return the `NavigationCase` representing the navigation that would be taken had
 `handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` been called with the same arguments or `null` if there is no
 such case. Implementations that comply the version of the specification in which this method was introduced must
 override this method. For compatibility with decorated implementations that comply with an earlier version of the
 specification, an implementation is provided that simply calls through to
 `getNavigationCase(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)`, ignoring the
 `toFlowDocumentId` parameter.

 Historically this method was declared in `ConfigurableNavigationHandler` since 2.2.

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
5.0

-

### getNavigationCases

public Map<String,Set<NavigationCase>> getNavigationCases()

 Return a `Map<String,
 Set<NavigationCase>>` where the keys are `<from-view-id>` values and the values are
 `Set<NavigationCase>` where each element in the Set is a `NavigationCase` that applies to
 that `<from-view-id>`. The implementation must support live modifications to this `Map`.

 Historically this method was declared in `ConfigurableNavigationHandler` since 2.0.
 For backward compatibility with earlier implementations, a default implementation is provided which returns an empty map.

Returns:
a map with navigation cases.
Since:
5.0

-

### performNavigation

public void performNavigation(String outcome)

 A convenience method to signal the Jakarta Faces implementation to perform navigation with the provided
 outcome. When the NavigationHandler is invoked, the current viewId is treated as the "from viewId" and the "from
 action" is null.

 Historically this method was declared in `ConfigurableNavigationHandler` since 2.0.

Parameters:
`outcome` - the provided outcome.
Throws:
`IllegalStateException` - if this method is called after this instance has been released
Since:
5.0

-

### inspectFlow

public void inspectFlow(FacesContext context,
 Flow flow)

 Called by the flow system to cause the flow to be inspected for navigation rules.

 Historically this method was declared in `ConfigurableNavigationHandler` since 2.2.
 For backward compatibility with earlier implementations, a default implementation is provided which does nothing.

Parameters:
`context` - the Faces context.
`flow` - the flow.
Since:
5.0
