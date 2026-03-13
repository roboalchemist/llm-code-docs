Package jakarta.faces.application

# Class Application

java.lang.Object
jakarta.faces.application.Application

Direct Known Subclasses:
`ApplicationWrapper`

---

public abstract class Application
extends Object

 **Application** represents a per-web-application singleton object where applications based
 on Jakarta Faces (or implementations wishing to provide extended functionality) can register application-wide
 singletons that provide functionality required by Jakarta Faces. Default implementations of each object are
 provided for cases where the application does not choose to customize the behavior.

 The instance of `Application` is created by calling the `getApplication()` method of
 `ApplicationFactory`. Because this instance is shared, it must be implemented in a thread-safe manner.

 The application also acts as a factory for several types of Objects specified in the Faces Configuration file. Please
 see `createComponent(java.lang.String)`, `createConverter(java.lang.String)`, and
 `createValidator(java.lang.String)`.

-

## Constructor Summary

Constructors

Constructor
Description
`Application()`

-

## Method Summary

Modifier and Type
Method
Description
`void`
`addBehavior(String behaviorId,
 String behaviorClass)`

 Register a new mapping of behavior id to the name of the corresponding
 `Behavior` class.

`abstract void`
`addComponent(String componentType,
 String componentClass)`

 Register a new mapping of component type to the name of the corresponding `UIComponent` class.

`abstract void`
`addConverter(Class<?> targetClass,
 String converterClass)`

 Register a new converter class that is capable of performing conversions for the specified target class.

`abstract void`
`addConverter(String converterId,
 String converterClass)`

 Register a new mapping of converter id to the name of the corresponding `Converter` class.

`void`
`addDefaultValidatorId(String validatorId)`

 Register a validator by its id that is applied to all `UIInput` components in a view.

`void`
`addELContextListener(jakarta.el.ELContextListener listener)`

 Provide a way for Faces applications to register an `ELContextListener` that will be notified on creation
 of `ELContext` instances.

`void`
`addELResolver(jakarta.el.ELResolver resolver)`

 Cause an the argument `resolver` to be added to the
 resolver chain as specified in section 5.3.2 "ELResolver" of the Jakarta Faces Specification Document.

`void`
`addSearchKeywordResolver(SearchKeywordResolver resolver)`

 Cause the argument `resolver` to be added to the head of the resolver chain.

`abstract void`
`addValidator(String validatorId,
 String validatorClass)`

 Register a new mapping of validator id to the name of the corresponding `Validator` class.

`Behavior`
`createBehavior(String behaviorId)`

 Instantiate and return a new `Behavior` instance of the class specified
 by a previous call to `addBehavior()` for the specified behavior id.

`UIComponent`
`createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType)`

 Call the `getValue()` method on the specified
 `ValueExpression`.

`UIComponent`
`createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType,
 String rendererType)`

 Like `createComponent(ValueExpression, FacesContext, String)` except the `Renderer` for the
 component to be returned must be inspected for the annotations mentioned in
 `createComponent(ValueExpression, FacesContext, String)` as specified in the documentation for that method.

`UIComponent`
`createComponent(FacesContext context,
 Resource componentResource)`

 Instantiate and return a new `UIComponent` instance from the
 argument `Resource`.

`UIComponent`
`createComponent(FacesContext context,
 String componentType,
 String rendererType)`

 Like `createComponent(String)` except the `Renderer` for the component to be returned must be
 inspected for the annotations mentioned in `createComponent(ValueExpression, FacesContext, String)` as
 specified in the documentation for that method.

`abstract UIComponent`
`createComponent(String componentType)`

 Instantiate and return a new `UIComponent` instance of the class
 specified by a previous call to `addComponent()` for the specified component type.

`abstract <T> Converter<T>`
`createConverter(Class<T> targetClass)`

 Instantiate and return a new `Converter` instance of the class that
 has registered itself as capable of performing conversions for objects of the specified type.

`abstract <T> Converter<T>`
`createConverter(String converterId)`

 Instantiate and return a new `Converter` instance of the class
 specified by a previous call to `addConverter()` for the specified converter id.

`abstract <T> Validator<T>`
`createValidator(String validatorId)`

 Instantiate and return a new `Validator` instance of the class
 specified by a previous call to `addValidator()` for the specified validator id.

`<T> T`
`evaluateExpressionGet(FacesContext context,
 String expression,
 Class<? extends T> expectedType)`

 Get a value by evaluating an expression.

`abstract ActionListener`
`getActionListener()`

 Return the default `ActionListener` to be registered for all
 `ActionSource` components in this application.

`Iterator<String>`
`getBehaviorIds()`

 Return an `Iterator` over the set of currently registered behavior ids for this `Application`.

`abstract Iterator<String>`
`getComponentTypes()`

 Return an `Iterator` over the set of currently defined component types for this `Application`.

`abstract Iterator<String>`
`getConverterIds()`

 Return an `Iterator` over the set of currently registered converter ids for this `Application`.

`abstract Iterator<Class<?>>`
`getConverterTypes()`

 Return an `Iterator` over the set of `Class` instances for which `Converter` classes have
 been explicitly registered.

`abstract Locale`
`getDefaultLocale()`

 Return the default `Locale` for this application.

`abstract String`
`getDefaultRenderKitId()`

 Return the `renderKitId` to be used for rendering this application.

`Map<String,String>`
`getDefaultValidatorInfo()`

 Return an immutable `Map` over the set of currently registered default validator IDs and their class name
 for this `Application`.

`jakarta.el.ELContextListener[]`
`getELContextListeners()`

 If no calls have been made to `addELContextListener(jakarta.el.ELContextListener)`, this method must return an empty array.

`jakarta.el.ELResolver`
`getELResolver()`

 Return the singleton `ELResolver` instance to be used for all Jakarta Expression Language resolution.

`jakarta.el.ExpressionFactory`
`getExpressionFactory()`

 Return the `ExpressionFactory` instance for this application.

`FlowHandler`
`getFlowHandler()`

 Return the thread-safe singleton `FlowHandler` for this application.

`abstract String`
`getMessageBundle()`

 Return the fully qualified class name of the `ResourceBundle` to be used for Jakarta Faces messages
 for this application.

`abstract NavigationHandler`
`getNavigationHandler()`

 Return the `NavigationHandler` instance that will be passed the outcome returned by any invoked application
 action for this web application.

`ProjectStage`
`getProjectStage()`

 Return the project stage for the currently running application instance.

`ResourceBundle`
`getResourceBundle(FacesContext ctx,
 String name)`

 Find a `ResourceBundle` as defined in the application configuration resources under the specified name.

`ResourceHandler`
`getResourceHandler()`

 Return the singleton, stateless, thread-safe `ResourceHandler` for this application.

`SearchExpressionHandler`
`getSearchExpressionHandler()`

 Return the thread-safe singleton `SearchExpressionHandler` for this application.

`SearchKeywordResolver`
`getSearchKeywordResolver()`

 Return the singleton `SearchKeywordResolver` instance to be used for all search keyword resolution.

`abstract StateManager`
`getStateManager()`

 Return the `StateManager` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle.

`abstract Iterator<Locale>`
`getSupportedLocales()`

 Return an `Iterator` over the supported `Locale`s for this appication.

`abstract Iterator<String>`
`getValidatorIds()`

 Return an `Iterator` over the set of currently registered validator ids for this `Application`.

`abstract ViewHandler`
`getViewHandler()`

 Return the `ViewHandler` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle.

`void`
`publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceBaseType,
 Object source)`

 This method functions exactly like `publishEvent(FacesContext,Class,Object)`, except the run-time must use the
 argument `sourceBaseType` to find the matching listener instead of using the `Class` of the
 `source` argument.

`void`
`publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Object source)`

 If `FacesContext.isProcessingEvents()` is `true` and there are one or more
 listeners for events of the type represented by `systemEventClass`, call those listeners, passing
 `source` as the source of the event.

`void`
`removeELContextListener(jakarta.el.ELContextListener listener)`

 Remove the argument `listener` from the list of `ELContextListener`s.

`abstract void`
`setActionListener(ActionListener listener)`

 Set the default `ActionListener` to be registered for all `ActionSource`
 components.

`abstract void`
`setDefaultLocale(Locale locale)`

 Set the default `Locale` for this application.

`abstract void`
`setDefaultRenderKitId(String renderKitId)`

 Set the `renderKitId` to be used to render this application.

`void`
`setFlowHandler(FlowHandler newHandler)`

 Set the `FlowHandler` instance used by the `NavigationHandler` to satisfy the requirements of the faces
 flows feature.

`abstract void`
`setMessageBundle(String bundle)`

 Set the fully qualified class name of the `ResourceBundle` to be used for Jakarta Faces messages
 for this application.

`abstract void`
`setNavigationHandler(NavigationHandler handler)`

 Set the `NavigationHandler` instance that will be passed the outcome returned by any invoked application action
 for this web application.

`void`
`setResourceHandler(ResourceHandler resourceHandler)`

 Set the `ResourceHandler` instance that will be utilized for rendering the markup for resources, and for
 satisfying client requests to serve up resources.

`void`
`setSearchExpressionHandler(SearchExpressionHandler searchExpressionHandler)`

 Set the `SearchExpressionHandler` instance used by the application.

`abstract void`
`setStateManager(StateManager manager)`

 Set the `StateManager` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle.

`abstract void`
`setSupportedLocales(Collection<Locale> locales)`

 Set the `Locale` instances representing the supported `Locale`s for this application.

`abstract void`
`setViewHandler(ViewHandler handler)`

 Set the `ViewHandler` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle.

`void`
`subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)`

 Install the listener instance referenced by argument `listener`
 into application as a listener for events of type `systemEventClass`.

`void`
`subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)`

 Install the listener instance referenced by argument `listener`
 into the application as a listener for events of type `systemEventClass` that originate from objects of
 type `sourceClass`.

`void`
`unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)`

 Remove the listener instance referenced by argument `listener`
 from the application as a listener for events of type `systemEventClass`.

`void`
`unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)`

 Remove the listener instance referenced by argument `listener`
 from the application as a listener for events of type `systemEventClass` that originate from objects of
 type `sourceClass`.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### Application

public Application()

-

## Method Details

-

### getActionListener

public abstract ActionListener getActionListener()

 Return the default `ActionListener` to be registered for all
 `ActionSource` components in this application. If not explicitly set, a default
 implementation must be provided that performs the functions as specified in the
 section 7.1.1 "ActionListener Property" in the chapter 7 "Application Integration" of the Jakarta Faces Specification Document.

 Note that the specification for the default `ActionListener` contiues to call for the use of a
 **deprecated** property (`action`) and class (`MethodBinding`). Unfortunately,
 this is necessary because the default `ActionListener` must continue to work with components that do not
 implement `ActionSource`, and only implement
 `ActionSource`.

Returns:
the action listener.

-

### setActionListener

public abstract void setActionListener(ActionListener listener)

 Set the default `ActionListener` to be registered for all `ActionSource`
 components.

Parameters:
`listener` - The new default `ActionListener`
Throws:
`NullPointerException` - if `listener` is `null`

-

### getDefaultLocale

public abstract Locale getDefaultLocale()

 Return the default `Locale` for this application. If not explicitly set, `null` is returned.

Returns:
the default Locale, or `null`.

-

### setDefaultLocale

public abstract void setDefaultLocale(Locale locale)

 Set the default `Locale` for this application.

Parameters:
`locale` - The new default `Locale`
Throws:
`NullPointerException` - if `locale` is `null`

-

### getDefaultRenderKitId

public abstract String getDefaultRenderKitId()

 Return the `renderKitId` to be used for rendering this application. If not explicitly set,
 `null` is returned.

Returns:
the default render kit id, or `null`.

-

### setDefaultRenderKitId

public abstract void setDefaultRenderKitId(String renderKitId)

 Set the `renderKitId` to be used to render this application. Unless the client has provided a custom
 `ViewHandler` that supports the use of multiple `RenderKit` instances in the same
 application, this method must only be called at application startup, before any Faces requests have been processed.
 This is a limitation of the current Specification, and may be lifted in a future release.

Parameters:
`renderKitId` - the render kit id to set.

-

### getMessageBundle

public abstract String getMessageBundle()

 Return the fully qualified class name of the `ResourceBundle` to be used for Jakarta Faces messages
 for this application. If not explicitly set, `null` is returned.

Returns:
the message bundle class name, or `null`.

-

### setMessageBundle

public abstract void setMessageBundle(String bundle)

 Set the fully qualified class name of the `ResourceBundle` to be used for Jakarta Faces messages
 for this application. See the JavaDocs for the `java.util.ResourceBundle` class for more information about
 the syntax for resource bundle names.

Parameters:
`bundle` - Base name of the resource bundle to be used
Throws:
`NullPointerException` - if `bundle` is `null`

-

### getNavigationHandler

public abstract NavigationHandler getNavigationHandler()

 Return the `NavigationHandler` instance that will be passed the outcome returned by any invoked application
 action for this web application. If not explicitly set, a default implementation must be provided that performs the
 functions described in the `NavigationHandler` class description.

    - The `NavigationHandler` implementation is declared in the application configuration resources by
 giving the fully qualified class name as the value of the `<navigation-handler>` element within the
 `<application>` element.

 The runtime must employ the decorator pattern as for every other pluggable artifact in Jakarta Faces.

Returns:
the navigation handler.

-

### setNavigationHandler

public abstract void setNavigationHandler(NavigationHandler handler)

 Set the `NavigationHandler` instance that will be passed the outcome returned by any invoked application action
 for this web application.

Parameters:
`handler` - The new `NavigationHandler` instance
Throws:
`NullPointerException` - if `handler` is `null`

-

### getResourceHandler

public ResourceHandler getResourceHandler()

 Return the singleton, stateless, thread-safe `ResourceHandler` for this application. The Jakarta Faces
 implementation must support the following techniques for declaring an alternate implementation of
 `ResourceHandler`.

    - 

 The `ResourceHandler` implementation is declared in the application configuration resources by giving the
 fully qualified class name as the value of the `<resource-handler>` element within the
 `<application>` element.

 In all of the above cases, the runtime must employ the decorator pattern as for every other pluggable artifact in
 Jakarta Faces.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function

 .

Returns:
the resource handler.
Since:
2.0

-

### setResourceHandler

public void setResourceHandler(ResourceHandler resourceHandler)

 Set the `ResourceHandler` instance that will be utilized for rendering the markup for resources, and for
 satisfying client requests to serve up resources.

Parameters:
`resourceHandler` - The new `ResourceHandler` instance
Throws:
`IllegalStateException` - if this method is called after at least one request has been processed by the
 `Lifecycle` instance for this application.
`NullPointerException` - if `resourceHandler` is `null`
Since:
2.0

-

### getResourceBundle

public ResourceBundle getResourceBundle(FacesContext ctx,
 String name)

 Find a `ResourceBundle` as defined in the application configuration resources under the specified name. If
 a `ResourceBundle` was defined for the name, return an instance that uses the locale of the current
 `UIViewRoot`.

 The default implementation throws `UnsupportedOperationException` and is provided for the sole purpose of
 not breaking existing applications that extend this class.

Parameters:
`ctx` - the Faces context.
`name` - the name of the resource bundle.
Returns:
the resource bundle.
Throws:
`FacesException` - if a bundle was defined, but not resolvable
`NullPointerException` - if ctx == null || name == null
Since:
1.2

-

### getProjectStage

public ProjectStage getProjectStage()

 Return the project stage for the currently running application instance. The default value is
 `ProjectStage.Production`

 The implementation of this method must perform the following algorithm or an equivalent with the same end result to
 determine the value to return.

 If the value has already been determined by a previous call to this method, simply return that value.

 Look for a `JNDI` environment entry under the key given by the value of
 `ProjectStage.PROJECT_STAGE_JNDI_NAME` (return type of `java.lang.String`). If found, continue with
 the algorithm below, otherwise, look for an entry in the `initParamMap` of the
 `ExternalContext` from the current `FacesContext` with the key given by the value of
 `ProjectStage.PROJECT_STAGE_PARAM_NAME`

 If a value is found, see if an enum constant can be obtained by calling `ProjectStage.valueOf()`, passing
 the value from the `initParamMap`. If this succeeds without exception, save the value and return it.

 If not found, or any of the previous attempts to discover the enum constant value have failed, log a descriptive
 error message, assign the value as `ProjectStage.Production` and return it.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function

 .

Returns:
the project stage.
Since:
2.0

-

### addELResolver

public void addELResolver(jakarta.el.ELResolver resolver)

 Cause an the argument `resolver` to be added to the
 resolver chain as specified in section 5.3.2 "ELResolver" of the Jakarta Faces Specification Document.

 It is not possible to remove an `ELResolver` registered with this method, once it has been registered.

 It is illegal to register an `ELResolver` after the application has received any requests from the client.
 If an attempt is made to register a listener after that time, an `IllegalStateException` must be thrown.
 This restriction is in place to allow the Jakarta Server Pages container to optimize for the common case where no
 additional `ELResolver`s are in the chain, aside from the standard ones. It is permissible to add
 `ELResolver`s before or after initialization to a `CompositeELResolver` that is already in the
 chain.

 The default implementation throws `UnsupportedOperationException` and is provided for the sole purpose of
 not breaking existing applications that extend `Application`.

Parameters:
`resolver` - the Jakarta Expression Language resolver to add.
Throws:
`IllegalStateException` - if called after the first request to the
 `FacesServlet` has been serviced.
Since:
1.2

-

### getELResolver

public jakarta.el.ELResolver getELResolver()

 Return the singleton `ELResolver` instance to be used for all Jakarta Expression Language resolution. This is
 actually an instance of `CompositeELResolver` that must contain the following
 `ELResolver` instances in the following order:

    - 

 `ELResolver` instances declared using the <el-resolver> element in the application configuration
 resources.

    - 

 An `implementation` that wraps the head of the legacy `VariableResolver` chain, as per section
 *VariableResolver ChainWrapper* in Chapter 5 in the spec document.

    - 

 An `implementation` that wraps the head of the legacy `PropertyResolver` chain, as per section
 *PropertyResolver ChainWrapper* in Chapter 5 in the spec document.

    - 

 Any `ELResolver` instances added by calls to `addELResolver(jakarta.el.ELResolver)`.

 The default implementation throws `UnsupportedOperationException` and is provided for the sole purpose of
 not breaking existing applications that extend `Application`.

Returns:
the Jakarta Expression Language resolver.
Since:
1.2

-

### getFlowHandler

public FlowHandler getFlowHandler()

 Return the thread-safe singleton `FlowHandler` for this application. For implementations declaring compliance
 with version 2.2 of the specification, this method must never return `null`, even if the application has no
 flows. This is necessary to enable dynamic flow creation during the application's lifetime.

 All implementations that declare compliance with version 2.2 of the specification must implement this method. For the
 purpose of backward compatibility with environments that extend `
Application` but do not override this method, an implementation is provided that returns `null`. Due to the
 decoratable nature of `Application`, code calling this method should always check for a `null` return.

Returns:
the flow handler.
Since:
2.2

-

### setFlowHandler

public void setFlowHandler(FlowHandler newHandler)

 Set the `FlowHandler` instance used by the `NavigationHandler` to satisfy the requirements of the faces
 flows feature.

Parameters:
`newHandler` - the flow handler to set.
Throws:
`NullPointerException` - if newHandler is `null`
`IllegalStateException` - if this method is called after at least one request has been processed by the
 `Lifecycle` instance for this application.
Since:
2.2

-

### getViewHandler

public abstract ViewHandler getViewHandler()

 Return the `ViewHandler` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle. If not explicitly set, a default implementation must be
 provided that performs the functions described in the `ViewHandler` description in the Jakarta Faces
 Specification.

Returns:
the view handler.

-

### setViewHandler

public abstract void setViewHandler(ViewHandler handler)

 Set the `ViewHandler` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle.

Parameters:
`handler` - The new `ViewHandler` instance
Throws:
`IllegalStateException` - if this method is called after at least one request has been processed by the
 `Lifecycle` instance for this application.
`NullPointerException` - if `handler` is `null`

-

### getStateManager

public abstract StateManager getStateManager()

 Return the `StateManager` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle. If not explicitly set, a default implementation must be
 provided that performs the functions described in the `StateManager` description in the Jakarta Faces
 Specification.

Returns:
the state manager.

-

### setStateManager

public abstract void setStateManager(StateManager manager)

 Set the `StateManager` instance that will be utilized during the *Restore View* and *Render
 Response* phases of the request processing lifecycle.

Parameters:
`manager` - The new `StateManager` instance
Throws:
`IllegalStateException` - if this method is called after at least one request has been processed by the
 `Lifecycle` instance for this application.
`NullPointerException` - if `manager` is `null`

-

### addBehavior

public void addBehavior(String behaviorId,
 String behaviorClass)

 Register a new mapping of behavior id to the name of the corresponding
 `Behavior` class. This allows subsequent calls to `createBehavior()` to serve as a factory for
 `Behavior` instances.

Parameters:
`behaviorId` - The behavior id to be registered
`behaviorClass` - The fully qualified class name of the corresponding `Behavior` implementation
Throws:
`NullPointerException` - if `behaviorId` or `behaviorClass` is `null`
Since:
2.0

-

### createBehavior

public Behavior createBehavior(String behaviorId)
                        throws FacesException

 Instantiate and return a new `Behavior` instance of the class specified
 by a previous call to `addBehavior()` for the specified behavior id.

Parameters:
`behaviorId` - The behavior id for which to create and return a new `Behavior` instance
Returns:
the behavior.
Throws:
`FacesException` - if the `Behavior` cannot be created
`NullPointerException` - if `behaviorId` is `null`

-

### getBehaviorIds

public Iterator<String> getBehaviorIds()

 Return an `Iterator` over the set of currently registered behavior ids for this `Application`.

Returns:
an iterator with behavior ids.

-

### addComponent

public abstract void addComponent(String componentType,
 String componentClass)

 Register a new mapping of component type to the name of the corresponding `UIComponent` class. This allows
 subsequent calls to `createComponent()` to serve as a factory for `UIComponent` instances.

Parameters:
`componentType` - The component type to be registered
`componentClass` - The fully qualified class name of the corresponding `UIComponent` implementation
Throws:
`NullPointerException` - if `componentType` or `componentClass` is `null`

-

### createComponent

public abstract UIComponent createComponent(String componentType)
                                     throws FacesException

 Instantiate and return a new `UIComponent` instance of the class
 specified by a previous call to `addComponent()` for the specified component type.

 Before the component instance is returned, it must be inspected for the presence of a
 `ListenerFor` (or `ListenersFor`) or `ResourceDependency`
 (or `ResourceDependencies`) annotation. If any of these annotations are present, the action listed in
 `ListenerFor` or `ResourceDependency` must be taken on the component, before it is
 returned from this method. This variant of `createComponent` must **not** inspect the
 `Renderer` for the component to be returned for any of the afore mentioned annotations.
 Such inspection is the province of `createComponent(ValueExpression, FacesContext, String, String)` or
 `createComponent(FacesContext, String, String)`.

Parameters:
`componentType` - The component type for which to create and return a new `UIComponent` instance
Returns:
the UI component.
Throws:
`FacesException` - if a `UIComponent` of the specified type cannot be created
`NullPointerException` - if `componentType` is `null`

-

### createComponent

public UIComponent createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType)
                            throws FacesException

 Call the `getValue()` method on the specified
 `ValueExpression`. If it returns a `UIComponent` instance, return it as the value of this method. If it
 does not, instantiate a new `UIComponent` instance of the specified component type, pass the new component to
 the `setValue()` method of the specified `ValueExpression`, and return it.

 Before the component instance is returned, it must be inspected for the presence of a
 `ListenerFor` (or `ListenersFor`) or `ResourceDependency`
 (or `ResourceDependencies`) annotation. If any of these annotations are present, the action listed in
 `ListenerFor` or `ResourceDependency` must be taken on the component, before it is
 returned from this method. This variant of `createComponent` must **not** inspect the
 `Renderer` for the component to be returned for any of the afore mentioned annotations.
 Such inspection is the province of `createComponent(ValueExpression, FacesContext, String, String)` or
 `createComponent(FacesContext, String, String)`.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function.

Parameters:
`componentExpression` - `ValueExpression` representing a component value expression (typically specified by
 the `component` attribute of a custom tag)
`context` - `FacesContext` for the current request
`componentType` - Component type to create if the `ValueExpression` does not return a component instance
Returns:
the UI component.
Throws:
`FacesException` - if a `UIComponent` cannot be created
`NullPointerException` - if any parameter is `null`
Since:
1.2

-

### createComponent

public UIComponent createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType,
 String rendererType)

 Like `createComponent(ValueExpression, FacesContext, String)` except the `Renderer` for the
 component to be returned must be inspected for the annotations mentioned in
 `createComponent(ValueExpression, FacesContext, String)` as specified in the documentation for that method.
 The `Renderer` instance to inspect must be obtained by calling `FacesContext.getRenderKit()` and
 calling `RenderKit.getRenderer(java.lang.String, java.lang.String)` on the result, passing the argument
 `componentType` as the first argument and the result of calling `UIComponent.getFamily()` on the newly
 created component as the second argument. If no such `Renderer` can be found, a message must be logged
 with a helpful error message. Otherwise, `UIComponent.setRendererType(java.lang.String)` must be called on the newly created
 `UIComponent` instance, passing the argument `rendererType` as the argument.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function.

Parameters:
`componentExpression` - `ValueExpression` representing a component value expression (typically specified by
 the `component` attribute of a custom tag)
`context` - `FacesContext` for the current request
`componentType` - Component type to create if the `ValueExpression` does not return a component instance
`rendererType` - The renderer-type of the `Renderer` that will render this component. A
 `null` value must be accepted for this parameter.
Returns:
the UI component.
Throws:
`FacesException` - if a `UIComponent` cannot be created
`NullPointerException` - if any of the parameters `componentExpression`, `context`, or
 `componentType` are `null`
Since:
2.0

-

### createComponent

public UIComponent createComponent(FacesContext context,
 String componentType,
 String rendererType)

 Like `createComponent(String)` except the `Renderer` for the component to be returned must be
 inspected for the annotations mentioned in `createComponent(ValueExpression, FacesContext, String)` as
 specified in the documentation for that method. The `Renderer` instance to inspect must be obtained by
 calling `FacesContext.getRenderKit()` and calling `RenderKit.getRenderer(java.lang.String, java.lang.String)` on the
 result, passing the argument `componentType` as the first argument and the result of calling
 `UIComponent.getFamily()` on the newly created component as the second argument. If no such `Renderer`
 can be found, a message must be logged with a helpful error message. Otherwise, `UIComponent.setRendererType(java.lang.String)`
 must be called on the newly created `UIComponent` instance, passing the argument `rendererType`
 as the argument.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function

 .

Parameters:
`context` - `FacesContext` for the current request
`componentType` - Component type to create
`rendererType` - The renderer-type of the `Renderer` that will render this component. A
 `null` value must be accepted for this parameter.
Returns:
the UI component.
Throws:
`FacesException` - if a `UIComponent` cannot be created
`NullPointerException` - if any of the parameters `context`, or `componentType` are
 `null`
Since:
2.0

-

### createComponent

public UIComponent createComponent(FacesContext context,
 Resource componentResource)

 Instantiate and return a new `UIComponent` instance from the
 argument `Resource`. An algorithm semantically equivalent to the following must be followed to instantiate the
 `UIComponent` to return.

    - 

 Obtain a reference to the `ViewDeclarationLanguage` for this `Application` instance by calling
 `ViewHandler.getViewDeclarationLanguage(jakarta.faces.context.FacesContext, java.lang.String)`, passing the `viewId` found by calling
 `UIViewRoot.getViewId()` on the `UIViewRoot` in the
 argument `FacesContext`.

    - 

 Obtain a reference to the *composite component metadata* for this composite component by calling
 `ViewDeclarationLanguage.getComponentMetadata(jakarta.faces.context.FacesContext, jakarta.faces.application.Resource)`, passing the `facesContext` and
 `componentResource` arguments to this method. This version of the Jakarta Faces Specification uses
 JavaBeans as the API to the component metadata.

    - 

 Determine if the component author declared a `componentType` for this component instance by obtaining the
 `BeanDescriptor` from the component metadata and calling its `getValue()` method, passing
 `UIComponent.COMPOSITE_COMPONENT_TYPE_KEY` as the argument. If non-`null`, the result must be a
 `ValueExpression` whose value is the `component-type` of the `UIComponent` to be
 created for this `Resource` component. Call through to `createComponent(java.lang.String)` to
 create the component.

    - 

 Otherwise, determine if a script based component for this `Resource` can be found by calling
 `ViewDeclarationLanguage.getScriptComponentResource(jakarta.faces.context.FacesContext, jakarta.faces.application.Resource)`. If the result is non-`null`, and is a script
 written in a language satisfying the content type `text/javascript`, create a
 `UIComponent` instance from the script resource.

    - 

 Otherwise, let *library-name* be the return from calling `Resource.getLibraryName()` on the argument
 `componentResource` and *resource-name* be the return from calling `Resource.getResourceName()`
 on the argument `componentResource`. Create a fully qualified Java class name by removing any file
 extension from *resource-name* and let *fqcn* be `*library-name* + "." +
     *resource-name*`. If a class with the name of *fqcn* cannot be found, take no action and continue
 to the next step. If any of `InstantiationException`, `IllegalAccessException`, or
 `ClassCastException` are thrown, wrap the exception in a `FacesException` and re-throw it. If
 any other exception is thrown, log the exception and continue to the next step.

    - 

 If none of the previous steps have yielded a `UIComponent` instance, call
 `createComponent(java.lang.String)` passing "`jakarta.faces.NamingContainer`" as the argument.

    - 

 Call `UIComponent.setRendererType(java.lang.String)` on the `UIComponent` instance, passing
 "`jakarta.faces.Composite`" as the argument.

    - 

 Store the argument `Resource` in the attributes `Map` of the `UIComponent` under the
 key, `Resource.COMPONENT_RESOURCE_KEY`.

    - 

 Store *composite component metadata* in the attributes `Map` of the `UIComponent` under
 the key, `UIComponent.BEANINFO_KEY`.

 Before the component instance is returned, it must be inspected for the presence of a
 `ListenerFor` annotation. If this annotation is present, the action listed in
 `ListenerFor` must be taken on the component, before it is returned from this method.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function.

Parameters:
`context` - `FacesContext` for the current request
`componentResource` - A `Resource` that points to a source file that provides an implementation of a
 component.
Returns:
the UI component.
Throws:
`FacesException` - if a `UIComponent` from the `Resource` cannot be created
`NullPointerException` - if any parameter is `null`
`NullPointerException` - if unable, for any reason, to obtain a `ViewDeclarationLanguage` instance as
 described above.
Since:
2.0

-

### getComponentTypes

public abstract Iterator<String> getComponentTypes()

 Return an `Iterator` over the set of currently defined component types for this `Application`.

Returns:
an iterator with component types.

-

### addConverter

public abstract void addConverter(String converterId,
 String converterClass)

 Register a new mapping of converter id to the name of the corresponding `Converter` class. This allows
 subsequent calls to `createConverter()` to serve as a factory for `Converter` instances.

Parameters:
`converterId` - The converter id to be registered
`converterClass` - The fully qualified class name of the corresponding `Converter` implementation
Throws:
`NullPointerException` - if `converterId` or `converterClass` is `null`

-

### addConverter

public abstract void addConverter(Class<?> targetClass,
 String converterClass)

 Register a new converter class that is capable of performing conversions for the specified target class.

Parameters:
`targetClass` - The class for which this converter is registered
`converterClass` - The fully qualified class name of the corresponding `Converter` implementation
Throws:
`NullPointerException` - if `targetClass` or `converterClass` is `null`

-

### createConverter

public abstract <T> Converter<T> createConverter(String converterId)

 Instantiate and return a new `Converter` instance of the class
 specified by a previous call to `addConverter()` for the specified converter id.

 If the `toLowerCase()` of the `String` represenation of the value of the
 "`jakarta.faces.DATETIMECONVERTER_DEFAULT_TIMEZONE_IS_SYSTEM_TIMEZONE`" application configuration
 parameter is "`true`" (without the quotes) and the `Converter` instance to be returned is an
 instance of `DateTimeConverter`,
 `DateTimeConverter.setTimeZone(java.util.TimeZone)` must be called, passing the return from
 `TimeZone.getDefault()`.

 The argument `converter` must be inspected for the presence of the
 `ResourceDependency` annotation. If the `ResourceDependency` annotation is
 present, the action described in `ResourceDependency` must be taken. If the
 `ResourceDependency` annotation is not present, the argument `converter` must be inspected for
 the presence of the `ResourceDependencies` annotation. If the
 `ResourceDependencies` annotation is present, the action described in `ResourceDependencies`
 must be taken.

Type Parameters:
`T` - The generic type of object value to convert.
Parameters:
`converterId` - The converter id for which to create and return a new `Converter` instance
Returns:
the converter.
Throws:
`FacesException` - if the `Converter` cannot be created
`NullPointerException` - if `converterId` is `null`

-

### createConverter

public abstract <T> Converter<T> createConverter(Class<T> targetClass)

 Instantiate and return a new `Converter` instance of the class that
 has registered itself as capable of performing conversions for objects of the specified type. If no such
 `Converter` class can be identified, return `null`.

 To locate an appropriate `Converter` class, the following algorithm is performed, stopping as soon as an
 appropriate `Converter` class is found:

    - Locate a `Converter` registered for the target class itself.
 
    - Locate a `Converter` registered for interfaces that are implemented by the target class (directly or
 indirectly).

    - Locate a `Converter` registered for the superclass (if any) of the target class, recursively working up the
 inheritance hierarchy.

 If the `Converter` has a single argument constructor that accepts a `Class`, instantiate the
 `Converter` using that constructor, passing the argument `targetClass` as the sole argument.
 Otherwise, simply use the zero-argument constructor.

 If the `toLowerCase()` of the `String` represenation of the value of the
 "`jakarta.faces.DATETIMECONVERTER_DEFAULT_TIMEZONE_IS_SYSTEM_TIMEZONE`" application configuration
 parameter is "`true`" (without the quotes) and the `Converter` instance to be returned is an
 instance of `DateTimeConverter`,
 `DateTimeConverter.setTimeZone(java.util.TimeZone)` must be called, passing the return from
 `TimeZone.getDefault()`.

Type Parameters:
`T` - The generic type of object value to convert.
Parameters:
`targetClass` - Target class for which to return a `Converter`
Returns:
the converter.
Throws:
`FacesException` - if the `Converter` cannot be created
`NullPointerException` - if `targetClass` is `null`

-

### getConverterIds

public abstract Iterator<String> getConverterIds()

 Return an `Iterator` over the set of currently registered converter ids for this `Application`.

Returns:
an iterator with converter ids.

-

### getConverterTypes

public abstract Iterator<Class<?>> getConverterTypes()

 Return an `Iterator` over the set of `Class` instances for which `Converter` classes have
 been explicitly registered.

Returns:
an iterator with converter types.

-

### addDefaultValidatorId

public void addDefaultValidatorId(String validatorId)

 Register a validator by its id that is applied to all `UIInput` components in a view. The validator to
 most often serve this role is the `BeanValidator`. The usage contract for this method assumes that the
 validator has been registered using the normal “by-id” registration mechanism.

 An implementation is provided that takes no action so that users that decorate the `Application` continue
 to work.

Parameters:
`validatorId` - the validator id.
Since:
2.0

-

### getDefaultValidatorInfo

public Map<String,String> getDefaultValidatorInfo()

 Return an immutable `Map` over the set of currently registered default validator IDs and their class name
 for this `Application`.

 An implementation is provided that returns `Collections.emptyMap` so that users that decorate the
 `Application` continue to work.

Returns:
a map of default validator information.
Since:
2.0

-

### getExpressionFactory

public jakarta.el.ExpressionFactory getExpressionFactory()

 Return the `ExpressionFactory` instance for this application. This instance is used by the convenience method
 `evaluateExpressionGet(jakarta.faces.context.FacesContext, java.lang.String, java.lang.Class<? extends T>)`.

 The implementation must return the `ExpressionFactory` from the Expression Language container by calling
 `jakarta.el.ELManager.getExpressionFactory()`.

 An implementation is provided that throws `UnsupportedOperationException` so that users that decorate the
 `Application` continue to work.

Returns:
the expression factory.
Since:
1.2

-

### evaluateExpressionGet

public <T> T evaluateExpressionGet(FacesContext context,
 String expression,
 Class<? extends T> expectedType)
                            throws jakarta.el.ELException

 Get a value by evaluating an expression.

 Call `getExpressionFactory()` then call `ExpressionFactory.createValueExpression(jakarta.el.ELContext, java.lang.String, java.lang.Class<?>)` passing the argument
 `expression` and `expectedType`. Call `FacesContext.getELContext()` and pass it to
 `ValueExpression.getValue(jakarta.el.ELContext)`, returning the result.

 An implementation is provided that throws `UnsupportedOperationException` so that users that decorate the
 `Application` continue to work.

Type Parameters:
`T` - the return type.
Parameters:
`context` - the Faces context.
`expression` - the expression.
`expectedType` - the expected type.
Returns:
the result of the evaluation.
Throws:
`jakarta.el.ELException`

-

### getSupportedLocales

public abstract Iterator<Locale> getSupportedLocales()

 Return an `Iterator` over the supported `Locale`s for this appication.

Returns:
an iterator of the supported locales.

-

### setSupportedLocales

public abstract void setSupportedLocales(Collection<Locale> locales)

 Set the `Locale` instances representing the supported `Locale`s for this application.

Parameters:
`locales` - The set of supported `Locale`s for this application
Throws:
`NullPointerException` - if the argument `newLocales` is `null`.

-

### addELContextListener

public void addELContextListener(jakarta.el.ELContextListener listener)

 Provide a way for Faces applications to register an `ELContextListener` that will be notified on creation
 of `ELContext` instances. This listener will be called once per request.

 An implementation is provided that throws `UnsupportedOperationException` so that users that decorate the
 `Application` continue to work.

Parameters:
`listener` - the Jakarta Expression Language context listener to add.
Since:
1.2

-

### removeELContextListener

public void removeELContextListener(jakarta.el.ELContextListener listener)

 Remove the argument `listener` from the list of `ELContextListener`s. If `listener` is
 null, no exception is thrown and no action is performed. If `listener` is not in the list, no exception is
 thrown and no action is performed.

 An implementation is provided that throws `UnsupportedOperationException` so that users that decorate the
 `Application` continue to work.

Parameters:
`listener` - the Jakarta Expression Language context listener to remove.
Since:
1.2

-

### getELContextListeners

public jakarta.el.ELContextListener[] getELContextListeners()

 If no calls have been made to `addELContextListener(jakarta.el.ELContextListener)`, this method must return an empty array.

 Otherwise, return an array representing the list of listeners added by calls to `addELContextListener(jakarta.el.ELContextListener)`.

 An implementation is provided that throws `UnsupportedOperationException` so that users that decorate the
 `Application` continue to work.

Returns:
an array of Jakarta Expression Language context listeners.
Since:
1.2

-

### addValidator

public abstract void addValidator(String validatorId,
 String validatorClass)

 Register a new mapping of validator id to the name of the corresponding `Validator` class. This allows
 subsequent calls to `createValidator()` to serve as a factory for `Validator` instances.

Parameters:
`validatorId` - The validator id to be registered
`validatorClass` - The fully qualified class name of the corresponding `Validator` implementation
Throws:
`NullPointerException` - if `validatorId` or `validatorClass` is `null`

-

### createValidator

public abstract <T> Validator<T> createValidator(String validatorId)
                                          throws FacesException

 Instantiate and return a new `Validator` instance of the class
 specified by a previous call to `addValidator()` for the specified validator id.

 The argument `validator` must be inspected for the presence of the
 `ResourceDependency` annotation. If the `ResourceDependency` annotation is
 present, the action described in `ResourceDependency` must be taken. If the
 `ResourceDependency` annotation is not present, the argument `validator` must be inspected for
 the presence of the `ResourceDependencies` annotation. If the
 `ResourceDependencies` annotation is present, the action described in `ResourceDependencies`
 must be taken.

Type Parameters:
`T` - The generic type of object value to validate.
Parameters:
`validatorId` - The validator id for which to create and return a new `Validator` instance
Returns:
the validator.
Throws:
`FacesException` - if a `Validator` of the specified id cannot be created
`NullPointerException` - if `validatorId` is `null`

-

### getValidatorIds

public abstract Iterator<String> getValidatorIds()

 Return an `Iterator` over the set of currently registered validator ids for this `Application`.

Returns:
an iterator of validator ids.

-

### publishEvent

public void publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Object source)

 If `FacesContext.isProcessingEvents()` is `true` and there are one or more
 listeners for events of the type represented by `systemEventClass`, call those listeners, passing
 `source` as the source of the event. The implementation should be as fast as possible in determining
 whether or not a listener for the given `systemEventClass` and `source` has been installed, and
 should return immediately once such a determination has been made. The implementation of `publishEvent`
 must honor the requirements stated in `subscribeToEvent(java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Class<?>, jakarta.faces.event.SystemEventListener)` regarding the storage and retrieval of listener
 instances. Specifically, if `subscribeToEvent(Class,Class,SystemEventListener)` was called, the
 `sourceClass` argument must match exactly the `Class` of the `source` argument in
 the call to `publishEvent()`. The implementation must not do any inheritance hierarachy inspection when
 looking for a match between the `sourceClass` passed to
 `subscribeToEvent(Class,Class,SystemEventListener)` and the `sourceClass` passed to
 `publishEvent()` in order to find any listeners to which the event should be published. In the case where
 the `Class` of the `source` argument does not match the `Class` of the
 `sourceClass` used when the listener was subscribed using `subscribeToEvent()`,
 `publishEvent(FacesContext,Class,Class,Object)` can be used to provide the `Class` used to perform
 the listener lookup and match.

 The default implementation must implement an algorithm semantically equivalent to the following to locate listener
 instances and to invoke them.

    - 

 If the `source` argument implements `SystemEventListenerHolder`, call
 `SystemEventListenerHolder.getListenersForEventClass(java.lang.Class<? extends jakarta.faces.event.SystemEvent>)` on it, passing the
 `systemEventClass` argument. If the list is not empty, perform algorithm *traverseListenerList* on
 the list.

    - 

 If any *view* level listeners have been installed by previous calls to
 `subscribeToEvent(Class, Class, jakarta.faces.event.SystemEventListener)` on the
 `UIViewRoot`, perform algorithm *traverseListenerList* on the list of listeners
 for that event installed on the `UIViewRoot`.

    - 

 If any `Application` level listeners have been installed by previous calls to
 `subscribeToEvent(Class, Class, jakarta.faces.event.SystemEventListener)`, perform algorithm
 *traverseListenerList* on the list.

    - 

 If any `Application` level listeners have been installed by previous calls to
 `subscribeToEvent(Class, jakarta.faces.event.SystemEventListener)`, perform algorithm
 *traverseListenerList* on the list.

    - 

 Finally fire the system event as a synchronous CDI event.
 If the `source` of this non-component system event is an instance of `UIViewRoot`, then fire an additional synchronous CDI event
 selecting the `View` qualifier having the current `UIViewRoot.getViewId()` as value.

 If the act of invoking the `processListener` method causes an
 `AbortProcessingException` to be thrown, processing of the listeners must be aborted, no
 further processing of the listeners for this event must take place, and the exception must be logged with
 `Level.SEVERE`.

 Algorithm *traverseListenerList*: For each listener in the list,

    - 

 Call `SystemEventListener.isListenerForSource(java.lang.Object)`, passing the `source` argument.
 If this returns `false`, take no action on the listener.

    - 

 Otherwise, if the event to be passed to the listener instances has not yet been constructed, construct the event,
 passing `source` as the argument to the one-argument constructor that takes an `Object`. This
 same event instance must be passed to all listener instances.

    - 

 Call `SystemEvent.isAppropriateListener(jakarta.faces.event.FacesListener)`, passing the listener instance as the argument. If
 this returns `false`, take no action on the listener.

    - 

 Call `SystemEvent.processListener(jakarta.faces.event.FacesListener)`, passing the listener instance.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function

 .

Parameters:
`context` - the `FacesContext` for the current request
`systemEventClass` - The `Class` of event that is being published.
`source` - The source for the event of type `systemEventClass`.
Throws:
`NullPointerException` - if either `context`, `systemEventClass` or `source` is
 `null`
Since:
2.0

-

### publishEvent

public void publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceBaseType,
 Object source)

 This method functions exactly like `publishEvent(FacesContext,Class,Object)`, except the run-time must use the
 argument `sourceBaseType` to find the matching listener instead of using the `Class` of the
 `source` argument.

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function

 .

Parameters:
`context` - the `FacesContext` for the current request
`systemEventClass` - The `Class` of event that is being published.
`sourceBaseType` - The `Class` of the source event that must be used to lookup the listener to which
 this event must be published. If this argument is `null` the return from `source.getClass()`
 must be used as the `sourceBaseType`.
`source` - The source for the event of type `systemEventClass`.
Throws:
`NullPointerException` - if any arguments except for `sourceBaseType` are `null`
Since:
2.0

-

### subscribeToEvent

public void subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)

 Install the listener instance referenced by argument `listener`
 into the application as a listener for events of type `systemEventClass` that originate from objects of
 type `sourceClass`.

 If argument `sourceClass` is non-`null`, `sourceClass` and
 `systemEventClass` must be used to store the argument `listener` in the application in such a
 way that the `listener` can be quickly looked up by the implementation of `publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` given
 `systemEventClass` and an instance of the `Class` referenced by `sourceClass`. If
 argument `sourceClass` is `null`, the `listener` must be discoverable by the
 implementation of `publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` given only `systemEventClass`.

 It is valid to call this method **during** the processing of an event which was subscribed to by a
 previous call to this method.

Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`sourceClass` - the `Class` of the instance which causes events of type `systemEventClass`
 to be fired. May be `null`.
`listener` - the implementation of `SystemEventListener` whose
 `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` method must be called when events of type
 `systemEventClass` are fired.
Throws:
`NullPointerException` - if any combination of `systemEventClass`, or `listener` are
 `null`.
Since:
2.0

-

### subscribeToEvent

public void subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)

 Install the listener instance referenced by argument `listener`
 into application as a listener for events of type `systemEventClass`. The default implementation simply
 calls through to `subscribeToEvent(Class, Class, jakarta.faces.event.SystemEventListener)` passing
 `null` as the `sourceClass` argument

 A default implementation is provided that throws `UnsupportedOperationException` so that users that
 decorate `Application` can continue to function

 .

Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`listener` - the implementation of `SystemEventListener` whose
 `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` method must be called when events of type
 `systemEventClass` are fired.

 See `subscribeToEvent(java.lang.Class,java.lang.Class,jakarta.faces.event.SystemEventListener)` for an
 additional requirement regarding when it is valid to call this method.

Throws:
`NullPointerException` - if any combination of `systemEventClass`, or `listener` are
 `null`.
Since:
2.0

-

### unsubscribeFromEvent

public void unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)

 Remove the listener instance referenced by argument `listener`
 from the application as a listener for events of type `systemEventClass` that originate from objects of
 type `sourceClass`. See `subscribeToEvent(Class, Class, jakarta.faces.event.SystemEventListener)`
 for the specification of how the listener is stored, and therefore, how it must be removed.

 See `subscribeToEvent(java.lang.Class,java.lang.Class,jakarta.faces.event.SystemEventListener)` for an
 additional requirement regarding when it is valid to call this method.

Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`sourceClass` - the `Class` of the instance which causes events of type `systemEventClass`
 to be fired. May be `null`.
`listener` - the implementation of `SystemEventListener` to remove from the internal
 data structure.
Throws:
`NullPointerException` - if any combination of `systemEventClass`, or
 `listener` are `null`.
Since:
2.0

-

### unsubscribeFromEvent

public void unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)

 Remove the listener instance referenced by argument `listener`
 from the application as a listener for events of type `systemEventClass`. The default implementation
 simply calls through to `unsubscribeFromEvent(Class, jakarta.faces.event.SystemEventListener)` passing
 `null` as the `sourceClass` argument

 See `subscribeToEvent(java.lang.Class,java.lang.Class,jakarta.faces.event.SystemEventListener)` for an
 additional requirement regarding when it is valid to call this method.

Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`listener` - the implementation of `SystemEventListener` to remove from the internal
 data structure.
Throws:
`NullPointerException` - if any combination of `systemEventClass`, or
 `listener` are `null`.
Since:
2.0

-

### getSearchExpressionHandler

public SearchExpressionHandler getSearchExpressionHandler()

 Return the thread-safe singleton `SearchExpressionHandler` for this application.

Returns:
the `SearchExpressionHandler`.
Since:
2.3

-

### setSearchExpressionHandler

public void setSearchExpressionHandler(SearchExpressionHandler searchExpressionHandler)

 Set the `SearchExpressionHandler` instance used by the application.

Parameters:
`searchExpressionHandler` - the `SearchExpressionHandler`.
Throws:
`NullPointerException` - if searchExpressionHandler is `null`
`IllegalStateException` - if this method is called after at least one request has been processed by the
 `Lifecycle` instance for this application.
Since:
2.3

-

### addSearchKeywordResolver

public void addSearchKeywordResolver(SearchKeywordResolver resolver)

 Cause the argument `resolver` to be added to the head of the resolver chain.

 It is not possible to remove a `SearchKeywordResolver` registered with this method, once it has been
 registered.

 The default implementation throws `UnsupportedOperationException` and is provided for the sole purpose of
 not breaking existing applications that extend `Application`.

Parameters:
`resolver` - the SearchKeywordResolver to add.
Throws:
`IllegalStateException` - if called after the first request to the `FacesServlet` has
 been serviced.
`NullPointerException` - when resolver is null.
Since:
2.3

-

### getSearchKeywordResolver

public SearchKeywordResolver getSearchKeywordResolver()

 Return the singleton `SearchKeywordResolver` instance to be used for all search keyword resolution. This is
 actually an instance of a composite SearchKeywordResolver that must contain the following
 `SearchKeywordResolver` instances in the following order:

    - 

 `SearchKeywordResolver` instances declared using the <search-keyword-resolver> element in the
 application configuration resources.

    - 

 Any `SearchKeywordResolver` instances added by calls to `addSearchKeywordResolver(jakarta.faces.component.search.SearchKeywordResolver)`.

    - 

 The `SearchKeywordResolver` implementations for `@all`, `@child(n)`,
 `@form`, `@id(...)`, `@namingcontainer`, `@next`, `@none`,
 `@parent`, `@previous`, `@root` and `@this`.

 The default implementation throws `UnsupportedOperationException` and is provided for the sole purpose of
 not breaking existing applications that extend `Application`.

Returns:
the `SearchKeywordResolver`.
Since:
2.3
