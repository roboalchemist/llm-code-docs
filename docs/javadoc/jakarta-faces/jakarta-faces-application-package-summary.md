# Package jakarta.faces.application

---

package jakarta.faces.application

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
Application

 **Application** represents a per-web-application singleton object where applications based
 on Jakarta Faces (or implementations wishing to provide extended functionality) can register application-wide
 singletons that provide functionality required by Jakarta Faces.

ApplicationConfigurationPopulator

 This class defines a `java.util.ServiceLoader` service which enables programmatic configuration of the Jakarta
 Server Faces runtime using the existing Application Configuration Resources schema.

ApplicationFactory

 **ApplicationFactory** is a factory object that
 creates (if needed) and returns `Application` instances.

ApplicationWrapper

 Provides a simple implementation of `Application` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `Application` instance.

ConfigurableNavigationHandler
Deprecated, for removal: This API element is subject to removal in a future version.
Use `NavigationHandler` instead.

ConfigurableNavigationHandlerWrapper
Deprecated, for removal: This API element is subject to removal in a future version.
Use `NavigationHandlerWrapper` instead.

FacesMessage

 **FacesMessage** represents a single validation (or other) message, which is typically associated with a
 particular component in the view.

FacesMessage.Severity

 Enum used to represent message severity levels.

NavigationCase

 **NavigationCase** represents a `<navigation-case>` in
 the navigation rule base, as well as the `<from-view-id>` with
 which this `<navigation-case>` is a sibling.

NavigationCaseWrapper

 Provides a simple implementation of `NavigationCase` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `NavigationCase` instance.

NavigationHandler

 A **NavigationHandler** is passed the
 outcome string returned by an application action invoked for this application, and will use this (along with related
 state information) to choose the view to be displayed next.

NavigationHandlerWrapper

 **NavigationHandlerWrapper** provides a simple implementation of
 `NavigationHandler` that can be subclassed by developers wishing to provide specialized behavior to an existing
 `NavigationHandler` instance.

ProjectStage

 This class enables a feature similar to the `RAILS_ENV` feature of the Ruby on Rails web framework.

ProtectedViewException

 This exception is thrown by the runtime when a violation of the view protection mechanism is encountered.

Resource

 An instance of
 `Resource` is a Java object representation of the artifact that is served up in response to a *resource
 request* from the client.

ResourceDependencies

 Container annotation to specify multiple `ResourceDependency` annotations on a single class.

ResourceDependency

 Instances of `UIComponent` or `Renderer` that have this
 annotation (or `ResourceDependencies` attached at the class level will automatically have a resource dependency
 added so that the named resource will be present in user agent's view of the `UIViewRoot` in which this
 component or renderer is used.

ResourceHandler

 **ResourceHandler** is the
 run-time API by which `UIComponent` and `Renderer`
 instances, and the `ViewDeclarationLanguage` can reference
 `Resource` instances. An implementation of this class must be thread-safe.

ResourceHandlerWrapper

 Provides a simple
 implementation of `ResourceHandler` that can be subclassed by developers wishing to provide specialized
 behavior to an existing `ResourceHandler` instance.

ResourceVisitOption

 Defines the resource traversal options.

ResourceWrapper

 Provides a simple implementation of `Resource`
 that can be subclassed by developers wishing to provide specialized behavior to an existing `Resource`
 instance.

StateManager

 **StateManager** directs the process of saving and restoring the view between requests.

StateManager.StateSavingMethod

 Allowed values for the initialization parameter named by the "jakarta.faces.STATE_SAVING_METHOD".

StateManagerWrapper

 Provides a simple implementation of `StateManager` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `StateManager` instance.

ViewExpiredException

 Implementations must throw this `FacesException` when attempting to restore the view
 `StateManagementStrategy.restoreView(FacesContext, String, String)` results in failure on postback.

ViewHandler

 **
 ViewHandler** is the pluggablity mechanism for allowing implementations of or applications using the
 Jakarta Faces Specification to provide their own handling of the activities in the *Render Response*
 and *Restore View* phases of the request processing lifecycle.

ViewHandlerWrapper

 Provides a simple implementation of `ViewHandler` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `ViewHandler` instance.

ViewResource

 Superclass of `Resource` that is only for use with views.

ViewVisitOption

 Defines the view traversal options.
