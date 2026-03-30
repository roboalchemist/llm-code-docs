Package jakarta.faces.application

# Class ApplicationWrapper

java.lang.Object
jakarta.faces.application.Application
jakarta.faces.application.ApplicationWrapper

All Implemented Interfaces:
`FacesWrapper<Application>`

---

public abstract class ApplicationWrapper
extends Application
implements FacesWrapper<Application>

 Provides a simple implementation of `Application` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `Application` instance. The
 default implementation of all methods is to call through to the wrapped `Application`.

 Usage: extend this class and push the implementation being wrapped to the constructor and use `getWrapped()` to
 access the instance being wrapped.

Since:
2.0

-

## Constructor Summary

Constructors

Constructor
Description
`ApplicationWrapper()`

Deprecated.
Use the other constructor taking the implementation being wrapped.

`ApplicationWrapper(Application wrapped)`

 If this application has been decorated, the implementation doing the decorating should push the implementation being
 wrapped to this constructor.

-

## Method Summary

Modifier and Type
Method
Description
`void`
`addBehavior(String behaviorId,
 String behaviorClass)`

 The default behavior of this method is to call `Application.addBehavior(String, String)` on the wrapped
 `Application` object.

`void`
`addComponent(String componentType,
 String componentClass)`

 The default behavior of this method is to call `Application.addComponent(String, String)` on the wrapped
 `Application` object.

`void`
`addConverter(Class<?> targetClass,
 String converterClass)`

 The default behavior of this method is to call `Application.addConverter(Class, String)` on the wrapped
 `Application` object.

`void`
`addConverter(String converterId,
 String converterClass)`

 The default behavior of this method is to call `Application.addConverter(String, String)` on the wrapped
 `Application` object.

`void`
`addDefaultValidatorId(String validatorId)`

 The default behavior of this method is to call `Application.addDefaultValidatorId(String)` on the wrapped
 `Application` object.

`void`
`addELContextListener(jakarta.el.ELContextListener listener)`

 The default behavior of this method is to call `Application.addELContextListener(jakarta.el.ELContextListener)`
 on the wrapped `Application` object.

`void`
`addELResolver(jakarta.el.ELResolver resolver)`

 The default behavior of this method is to call
 `Application.addELResolver(jakarta.el.ELResolver)` on the wrapped `Application` object.

`void`
`addSearchKeywordResolver(SearchKeywordResolver resolver)`

 Cause the argument `resolver` to be added to the head of the resolver chain.

`void`
`addValidator(String validatorId,
 String validatorClass)`

 The default behavior of this method is to call `Application.addValidator(String, String)` on the wrapped
 `Application` object.

`Behavior`
`createBehavior(String behaviorId)`

 The default behavior of this method is to call `Application.createBehavior(String)` on the wrapped
 `Application` object.

`UIComponent`
`createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType)`

 The default behavior of this method is to call
 `Application.createComponent(jakarta.el.ValueExpression, jakarta.faces.context.FacesContext, String)` on the
 wrapped `Application` object.

`UIComponent`
`createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType,
 String rendererType)`

 The default behavior of this method is to call
 `Application.createComponent(jakarta.el.ValueExpression, jakarta.faces.context.FacesContext, String, String)`
 on the wrapped `Application` object.

`UIComponent`
`createComponent(FacesContext context,
 Resource componentResource)`

 The default behavior of this method is to call
 `Application.createComponent(jakarta.faces.context.FacesContext, Resource)` on the wrapped `Application`
 object.

`UIComponent`
`createComponent(FacesContext context,
 String componentType,
 String rendererType)`

 The default behavior of this method is to call
 `Application.createComponent(jakarta.faces.context.FacesContext, String, String)` on the wrapped
 `Application` object.

`UIComponent`
`createComponent(String componentType)`

 The default behavior of this method is to call `Application.createComponent(String)` on the wrapped
 `Application` object.

`<T> Converter<T>`
`createConverter(Class<T> targetClass)`

 The default behavior of this method is to call `Application.createConverter(Class)` on the wrapped
 `Application` object.

`<T> Converter<T>`
`createConverter(String converterId)`

 The default behavior of this method is to call `Application.createConverter(String)` on the wrapped
 `Application` object.

`<T> Validator<T>`
`createValidator(String validatorId)`

 The default behavior of this method is to call `Application.createValidator(String)` on the wrapped
 `Application` object.

`<T> T`
`evaluateExpressionGet(FacesContext context,
 String expression,
 Class<? extends T> expectedType)`

 The default behavior of this method is to call
 `Application.evaluateExpressionGet(jakarta.faces.context.FacesContext, String, Class)` on the wrapped
 `Application` object.

`ActionListener`
`getActionListener()`

 The default behavior of this method is to call `Application.getActionListener()` on the wrapped
 `Application` object.

`Iterator<String>`
`getBehaviorIds()`

 The default behavior of this method is to call `Application.getBehaviorIds()` on the wrapped `Application`
 object.

`Iterator<String>`
`getComponentTypes()`

 The default behavior of this method is to call `Application.getComponentTypes()` on the wrapped
 `Application` object.

`Iterator<String>`
`getConverterIds()`

 The default behavior of this method is to call `Application.getConverterIds()` on the wrapped `Application`
 object.

`Iterator<Class<?>>`
`getConverterTypes()`

 The default behavior of this method is to call `Application.getConverterTypes()` on the wrapped
 `Application` object.

`Locale`
`getDefaultLocale()`

 The default behavior of this method is to call `Application.getDefaultLocale()` on the wrapped
 `Application` object.

`String`
`getDefaultRenderKitId()`

 The default behavior of this method is to call `Application.getDefaultRenderKitId()` on the wrapped
 `Application` object.

`Map<String,String>`
`getDefaultValidatorInfo()`

 The default behavior of this method is to call `Application.getDefaultValidatorInfo()` on the wrapped
 `Application` object.

`jakarta.el.ELContextListener[]`
`getELContextListeners()`

 The default behavior of this method is to call `Application.getELContextListeners()` on the wrapped
 `Application` object.

`jakarta.el.ELResolver`
`getELResolver()`

 The default behavior of this method is to call `Application.getELResolver()` on the wrapped `Application`
 object.

`jakarta.el.ExpressionFactory`
`getExpressionFactory()`

 The default behavior of this method is to call `Application.getExpressionFactory()` on the wrapped
 `Application` object.

`FlowHandler`
`getFlowHandler()`

 Return the thread-safe singleton `FlowHandler` for this application.

`String`
`getMessageBundle()`

 The default behavior of this method is to call `Application.getMessageBundle()` on the wrapped
 `Application` object.

`NavigationHandler`
`getNavigationHandler()`

 The default behavior of this method is to call `Application.getNavigationHandler()` on the wrapped
 `Application` object.

`ProjectStage`
`getProjectStage()`

 The default behavior of this method is to call `Application.getProjectStage()` on the wrapped `Application`
 object.

`ResourceBundle`
`getResourceBundle(FacesContext ctx,
 String name)`

 The default behavior of this method is to call
 `Application.getResourceBundle(jakarta.faces.context.FacesContext, String)` on the wrapped `Application`
 object.

`ResourceHandler`
`getResourceHandler()`

 The default behavior of this method is to call `Application.getResourceHandler()` on the wrapped
 `Application` object.

`SearchExpressionHandler`
`getSearchExpressionHandler()`

 Return the thread-safe singleton `SearchExpressionHandler` for this application.

`SearchKeywordResolver`
`getSearchKeywordResolver()`

 Return the singleton `SearchKeywordResolver` instance to be used for all search keyword resolution.

`StateManager`
`getStateManager()`

 The default behavior of this method is to call `Application.getStateManager()` on the wrapped `Application`
 object.

`Iterator<Locale>`
`getSupportedLocales()`

 The default behavior of this method is to call `Application.getSupportedLocales()` on the wrapped
 `Application` object.

`Iterator<String>`
`getValidatorIds()`

 The default behavior of this method is to call `Application.getValidatorIds()` on the wrapped `Application`
 object.

`ViewHandler`
`getViewHandler()`

 The default behavior of this method is to call `Application.getViewHandler()` on the wrapped `Application`
 object.

`Application`
`getWrapped()`

 A class that implements this interface uses this method to return an instance of the class being wrapped.

`void`
`publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceBaseType,
 Object source)`

 The default behavior of this method is to call
 `Application.publishEvent(jakarta.faces.context.FacesContext, Class, Class, Object)` on the wrapped
 `Application` object.

`void`
`publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Object source)`

 The default behavior of this method is to call
 `Application.publishEvent(jakarta.faces.context.FacesContext, Class, Object)` on the wrapped
 `Application` object.

`void`
`removeELContextListener(jakarta.el.ELContextListener listener)`

 The default behavior of this method is to call
 `Application.removeELContextListener(jakarta.el.ELContextListener)` on the wrapped `Application` object.

`void`
`setActionListener(ActionListener listener)`

 The default behavior of this method is to call
 `Application.setActionListener(jakarta.faces.event.ActionListener)` on the wrapped `Application` object.

`void`
`setDefaultLocale(Locale locale)`

 The default behavior of this method is to call `Application.setDefaultLocale(java.util.Locale)` on the wrapped
 `Application` object.

`void`
`setDefaultRenderKitId(String renderKitId)`

 The default behavior of this method is to call `Application.setDefaultRenderKitId(String)` on the wrapped
 `Application` object.

`void`
`setFlowHandler(FlowHandler newHandler)`

 Set the `FlowHandler` instance used by the `NavigationHandler` to satisfy the requirements of the faces
 flows feature.

`void`
`setMessageBundle(String bundle)`

 The default behavior of this method is to call `Application.setMessageBundle(String)` on the wrapped
 `Application` object.

`void`
`setNavigationHandler(NavigationHandler handler)`

 The default behavior of this method is to call `Application.setNavigationHandler(NavigationHandler)` on the
 wrapped `Application` object.

`void`
`setResourceHandler(ResourceHandler resourceHandler)`

 The default behavior of this method is to call
 `Application.setResourceHandler(ResourceHandler)` on the wrapped `Application` object.

`void`
`setSearchExpressionHandler(SearchExpressionHandler searchExpressionHandler)`

 Set the `SearchExpressionHandler` instance used by the application.

`void`
`setStateManager(StateManager manager)`

 The default behavior of this method is to call
 `Application.setStateManager(StateManager)` on the wrapped `Application` object.

`void`
`setSupportedLocales(Collection<Locale> locales)`

 The default behavior of this method is to call `Application.setSupportedLocales(java.util.Collection)` on the
 wrapped `Application` object.

`void`
`setViewHandler(ViewHandler handler)`

 The default behavior of this method is to call
 `Application.setViewHandler(ViewHandler)` on the wrapped `Application` object.

`void`
`subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)`

 The default behavior of this method is to call
 `Application.subscribeToEvent(Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

`void`
`subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)`

 The default behavior of this method is to call
 `Application.subscribeToEvent(Class, Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

`void`
`unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)`

 The default behavior of this method is to call
 `Application.unsubscribeFromEvent(Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

`void`
`unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)`

 The default behavior of this method is to call
 `Application.unsubscribeFromEvent(Class, Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ApplicationWrapper

@Deprecated
public ApplicationWrapper()
Deprecated.
Use the other constructor taking the implementation being wrapped.

-

### ApplicationWrapper

public ApplicationWrapper(Application wrapped)

 If this application has been decorated, the implementation doing the decorating should push the implementation being
 wrapped to this constructor. The `getWrapped()` will then return the implementation being wrapped.

Parameters:
`wrapped` - The implementation being wrapped.
Since:
2.3

-

## Method Details

-

### getWrapped

public Application getWrapped()
Description copied from interface: `FacesWrapper`

 A class that implements this interface uses this method to return an instance of the class being wrapped.

Specified by:
`getWrapped` in interface `FacesWrapper<Application>`
Returns:
the wrapped instance.

-

### getActionListener

public ActionListener getActionListener()

 The default behavior of this method is to call `Application.getActionListener()` on the wrapped
 `Application` object.

Specified by:
`getActionListener` in class `Application`
Returns:
the action listener.

-

### setActionListener

public void setActionListener(ActionListener listener)

 The default behavior of this method is to call
 `Application.setActionListener(jakarta.faces.event.ActionListener)` on the wrapped `Application` object.

Specified by:
`setActionListener` in class `Application`
Parameters:
`listener` - The new default `ActionListener`

-

### getDefaultLocale

public Locale getDefaultLocale()

 The default behavior of this method is to call `Application.getDefaultLocale()` on the wrapped
 `Application` object.

Specified by:
`getDefaultLocale` in class `Application`
Returns:
the default Locale, or `null`.

-

### setDefaultLocale

public void setDefaultLocale(Locale locale)

 The default behavior of this method is to call `Application.setDefaultLocale(java.util.Locale)` on the wrapped
 `Application` object.

Specified by:
`setDefaultLocale` in class `Application`
Parameters:
`locale` - The new default `Locale`

-

### getDefaultRenderKitId

public String getDefaultRenderKitId()

 The default behavior of this method is to call `Application.getDefaultRenderKitId()` on the wrapped
 `Application` object.

Specified by:
`getDefaultRenderKitId` in class `Application`
Returns:
the default render kit id, or `null`.

-

### addDefaultValidatorId

public void addDefaultValidatorId(String validatorId)

 The default behavior of this method is to call `Application.addDefaultValidatorId(String)` on the wrapped
 `Application` object.

Overrides:
`addDefaultValidatorId` in class `Application`
Parameters:
`validatorId` - the validator id.

-

### getDefaultValidatorInfo

public Map<String,String> getDefaultValidatorInfo()

 The default behavior of this method is to call `Application.getDefaultValidatorInfo()` on the wrapped
 `Application` object.

Overrides:
`getDefaultValidatorInfo` in class `Application`
Returns:
a map of default validator information.

-

### setDefaultRenderKitId

public void setDefaultRenderKitId(String renderKitId)

 The default behavior of this method is to call `Application.setDefaultRenderKitId(String)` on the wrapped
 `Application` object.

Specified by:
`setDefaultRenderKitId` in class `Application`
Parameters:
`renderKitId` - the render kit id to set.

-

### getMessageBundle

public String getMessageBundle()

 The default behavior of this method is to call `Application.getMessageBundle()` on the wrapped
 `Application` object.

Specified by:
`getMessageBundle` in class `Application`
Returns:
the message bundle class name, or `null`.

-

### setMessageBundle

public void setMessageBundle(String bundle)

 The default behavior of this method is to call `Application.setMessageBundle(String)` on the wrapped
 `Application` object.

Specified by:
`setMessageBundle` in class `Application`
Parameters:
`bundle` - Base name of the resource bundle to be used

-

### getNavigationHandler

public NavigationHandler getNavigationHandler()

 The default behavior of this method is to call `Application.getNavigationHandler()` on the wrapped
 `Application` object.

Specified by:
`getNavigationHandler` in class `Application`
Returns:
the navigation handler.

-

### setNavigationHandler

public void setNavigationHandler(NavigationHandler handler)

 The default behavior of this method is to call `Application.setNavigationHandler(NavigationHandler)` on the
 wrapped `Application` object.

Specified by:
`setNavigationHandler` in class `Application`
Parameters:
`handler` - The new `NavigationHandler` instance

-

### getViewHandler

public ViewHandler getViewHandler()

 The default behavior of this method is to call `Application.getViewHandler()` on the wrapped `Application`
 object.

Specified by:
`getViewHandler` in class `Application`
Returns:
the view handler.

-

### setViewHandler

public void setViewHandler(ViewHandler handler)

 The default behavior of this method is to call
 `Application.setViewHandler(ViewHandler)` on the wrapped `Application` object.

Specified by:
`setViewHandler` in class `Application`
Parameters:
`handler` - The new `ViewHandler` instance
Throws:
`IllegalStateException` - if this method is called after at least one request
 has been processed by the `Lifecycle` instance for this application.
`NullPointerException` - if `manager` is `null`

-

### getStateManager

public StateManager getStateManager()

 The default behavior of this method is to call `Application.getStateManager()` on the wrapped `Application`
 object.

Specified by:
`getStateManager` in class `Application`
Returns:
the state manager.

-

### setStateManager

public void setStateManager(StateManager manager)

 The default behavior of this method is to call
 `Application.setStateManager(StateManager)` on the wrapped `Application` object.

Specified by:
`setStateManager` in class `Application`
Parameters:
`manager` - The new `StateManager` instance
Throws:
`IllegalStateException` - if this method is called after at least one request has
 been processed by the `Lifecycle` instance for this application.
`NullPointerException` - if `manager` is `null`

-

### addComponent

public void addComponent(String componentType,
 String componentClass)

 The default behavior of this method is to call `Application.addComponent(String, String)` on the wrapped
 `Application` object.

Specified by:
`addComponent` in class `Application`
Parameters:
`componentType` - The component type to be registered
`componentClass` - The fully qualified class name of the corresponding `UIComponent` implementation

-

### createComponent

public UIComponent createComponent(String componentType)
                            throws FacesException

 The default behavior of this method is to call `Application.createComponent(String)` on the wrapped
 `Application` object.

Specified by:
`createComponent` in class `Application`
Parameters:
`componentType` - The component type for which to create and return a new `UIComponent` instance
Returns:
the UI component.
Throws:
`FacesException` - if a `UIComponent` of the specified type cannot be created

-

### getComponentTypes

public Iterator<String> getComponentTypes()

 The default behavior of this method is to call `Application.getComponentTypes()` on the wrapped
 `Application` object.

Specified by:
`getComponentTypes` in class `Application`
Returns:
an iterator with component types.

-

### addConverter

public void addConverter(String converterId,
 String converterClass)

 The default behavior of this method is to call `Application.addConverter(String, String)` on the wrapped
 `Application` object.

Specified by:
`addConverter` in class `Application`
Parameters:
`converterId` - The converter id to be registered
`converterClass` - The fully qualified class name of the corresponding `Converter` implementation

-

### addConverter

public void addConverter(Class<?> targetClass,
 String converterClass)

 The default behavior of this method is to call `Application.addConverter(Class, String)` on the wrapped
 `Application` object.

Specified by:
`addConverter` in class `Application`
Parameters:
`targetClass` - The class for which this converter is registered
`converterClass` - The fully qualified class name of the corresponding `Converter` implementation

-

### createConverter

public <T> Converter<T> createConverter(String converterId)

 The default behavior of this method is to call `Application.createConverter(String)` on the wrapped
 `Application` object.

Specified by:
`createConverter` in class `Application`
Type Parameters:
`T` - The generic type of object value to convert.
Parameters:
`converterId` - The converter id for which to create and return a new `Converter` instance
Returns:
the converter.

-

### createConverter

public <T> Converter<T> createConverter(Class<T> targetClass)

 The default behavior of this method is to call `Application.createConverter(Class)` on the wrapped
 `Application` object.

Specified by:
`createConverter` in class `Application`
Type Parameters:
`T` - The generic type of object value to convert.
Parameters:
`targetClass` - Target class for which to return a `Converter`
Returns:
the converter.

-

### getConverterIds

public Iterator<String> getConverterIds()

 The default behavior of this method is to call `Application.getConverterIds()` on the wrapped `Application`
 object.

Specified by:
`getConverterIds` in class `Application`
Returns:
an iterator with converter ids.

-

### getConverterTypes

public Iterator<Class<?>> getConverterTypes()

 The default behavior of this method is to call `Application.getConverterTypes()` on the wrapped
 `Application` object.

Specified by:
`getConverterTypes` in class `Application`
Returns:
an iterator with converter types.

-

### getSupportedLocales

public Iterator<Locale> getSupportedLocales()

 The default behavior of this method is to call `Application.getSupportedLocales()` on the wrapped
 `Application` object.

Specified by:
`getSupportedLocales` in class `Application`
Returns:
an iterator of the supported locales.

-

### setSupportedLocales

public void setSupportedLocales(Collection<Locale> locales)

 The default behavior of this method is to call `Application.setSupportedLocales(java.util.Collection)` on the
 wrapped `Application` object.

Specified by:
`setSupportedLocales` in class `Application`
Parameters:
`locales` - The set of supported `Locale`s for this application

-

### addBehavior

public void addBehavior(String behaviorId,
 String behaviorClass)

 The default behavior of this method is to call `Application.addBehavior(String, String)` on the wrapped
 `Application` object.

Overrides:
`addBehavior` in class `Application`
Parameters:
`behaviorId` - The behavior id to be registered
`behaviorClass` - The fully qualified class name of the corresponding `Behavior` implementation

-

### createBehavior

public Behavior createBehavior(String behaviorId)
                        throws FacesException

 The default behavior of this method is to call `Application.createBehavior(String)` on the wrapped
 `Application` object.

Overrides:
`createBehavior` in class `Application`
Parameters:
`behaviorId` - The behavior id for which to create and return a new `Behavior` instance
Returns:
the behavior.
Throws:
`FacesException` - if the `Behavior` cannot be created

-

### getBehaviorIds

public Iterator<String> getBehaviorIds()

 The default behavior of this method is to call `Application.getBehaviorIds()` on the wrapped `Application`
 object.

Overrides:
`getBehaviorIds` in class `Application`
Returns:
an iterator with behavior ids.

-

### addValidator

public void addValidator(String validatorId,
 String validatorClass)

 The default behavior of this method is to call `Application.addValidator(String, String)` on the wrapped
 `Application` object.

Specified by:
`addValidator` in class `Application`
Parameters:
`validatorId` - The validator id to be registered
`validatorClass` - The fully qualified class name of the corresponding `Validator` implementation

-

### createValidator

public <T> Validator<T> createValidator(String validatorId)
                                 throws FacesException

 The default behavior of this method is to call `Application.createValidator(String)` on the wrapped
 `Application` object.

Specified by:
`createValidator` in class `Application`
Type Parameters:
`T` - The generic type of object value to validate.
Parameters:
`validatorId` - The validator id for which to create and return a new `Validator` instance
Returns:
the validator.
Throws:
`FacesException` - if a `Validator` of the specified id cannot be created

-

### getValidatorIds

public Iterator<String> getValidatorIds()

 The default behavior of this method is to call `Application.getValidatorIds()` on the wrapped `Application`
 object.

Specified by:
`getValidatorIds` in class `Application`
Returns:
an iterator of validator ids.

-

### getResourceHandler

public ResourceHandler getResourceHandler()

 The default behavior of this method is to call `Application.getResourceHandler()` on the wrapped
 `Application` object.

Overrides:
`getResourceHandler` in class `Application`
Returns:
the resource handler.

-

### setResourceHandler

public void setResourceHandler(ResourceHandler resourceHandler)

 The default behavior of this method is to call
 `Application.setResourceHandler(ResourceHandler)` on the wrapped `Application` object.

 This method can throw `IllegalStateException` and `NullPointerException`.

Overrides:
`setResourceHandler` in class `Application`
Parameters:
`resourceHandler` - The new `ResourceHandler` instance
Throws:
`IllegalStateException` - if this method is called after at least one request has
 been processed by the `Lifecycle` instance for this application.
`NullPointerException` - if `resourceHandler` is `null`

-

### getResourceBundle

public ResourceBundle getResourceBundle(FacesContext ctx,
 String name)

 The default behavior of this method is to call
 `Application.getResourceBundle(jakarta.faces.context.FacesContext, String)` on the wrapped `Application`
 object.

Overrides:
`getResourceBundle` in class `Application`
Parameters:
`ctx` - the Faces context.
`name` - the name of the resource bundle.
Returns:
the resource bundle.

-

### getProjectStage

public ProjectStage getProjectStage()

 The default behavior of this method is to call `Application.getProjectStage()` on the wrapped `Application`
 object.

Overrides:
`getProjectStage` in class `Application`
Returns:
the project stage.

-

### addELResolver

public void addELResolver(jakarta.el.ELResolver resolver)

 The default behavior of this method is to call
 `Application.addELResolver(jakarta.el.ELResolver)` on the wrapped `Application` object.

Overrides:
`addELResolver` in class `Application`
Parameters:
`resolver` - the Jakarta Expression Language resolver to add.
Throws:
`IllegalStateException` - if called after the first request to the
 `FacesServlet` has been serviced.

-

### getELResolver

public jakarta.el.ELResolver getELResolver()

 The default behavior of this method is to call `Application.getELResolver()` on the wrapped `Application`
 object.

Overrides:
`getELResolver` in class `Application`
Returns:
the Jakarta Expression Language resolver.

-

### createComponent

public UIComponent createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType)
                            throws FacesException

 The default behavior of this method is to call
 `Application.createComponent(jakarta.el.ValueExpression, jakarta.faces.context.FacesContext, String)` on the
 wrapped `Application` object.

Overrides:
`createComponent` in class `Application`
Parameters:
`componentExpression` - `ValueExpression` representing a component value expression (typically specified by
 the `component` attribute of a custom tag)
`context` - `FacesContext` for the current request
`componentType` - Component type to create if the `ValueExpression` does not return a component instance
Returns:
the UI component.
Throws:
`FacesException` - if a `UIComponent` cannot be created

-

### createComponent

public UIComponent createComponent(jakarta.el.ValueExpression componentExpression,
 FacesContext context,
 String componentType,
 String rendererType)

 The default behavior of this method is to call
 `Application.createComponent(jakarta.el.ValueExpression, jakarta.faces.context.FacesContext, String, String)`
 on the wrapped `Application` object.

Overrides:
`createComponent` in class `Application`
Parameters:
`componentExpression` - `ValueExpression` representing a component value expression (typically specified by
 the `component` attribute of a custom tag)
`context` - `FacesContext` for the current request
`componentType` - Component type to create if the `ValueExpression` does not return a component instance
`rendererType` - The renderer-type of the `Renderer` that will render this component. A
 `null` value must be accepted for this parameter.
Returns:
the UI component.

-

### createComponent

public UIComponent createComponent(FacesContext context,
 String componentType,
 String rendererType)

 The default behavior of this method is to call
 `Application.createComponent(jakarta.faces.context.FacesContext, String, String)` on the wrapped
 `Application` object.

Overrides:
`createComponent` in class `Application`
Parameters:
`context` - `FacesContext` for the current request
`componentType` - Component type to create
`rendererType` - The renderer-type of the `Renderer` that will render this component. A
 `null` value must be accepted for this parameter.
Returns:
the UI component.

-

### createComponent

public UIComponent createComponent(FacesContext context,
 Resource componentResource)

 The default behavior of this method is to call
 `Application.createComponent(jakarta.faces.context.FacesContext, Resource)` on the wrapped `Application`
 object.

Overrides:
`createComponent` in class `Application`
Parameters:
`context` - `FacesContext` for the current request
`componentResource` - A `Resource` that points to a source file that provides an implementation of a
 component.
Returns:
the UI component.

-

### getExpressionFactory

public jakarta.el.ExpressionFactory getExpressionFactory()

 The default behavior of this method is to call `Application.getExpressionFactory()` on the wrapped
 `Application` object.

Overrides:
`getExpressionFactory` in class `Application`
Returns:
the expression factory.

-

### getFlowHandler

public FlowHandler getFlowHandler()
Description copied from class: `Application`

 Return the thread-safe singleton `FlowHandler` for this application. For implementations declaring compliance
 with version 2.2 of the specification, this method must never return `null`, even if the application has no
 flows. This is necessary to enable dynamic flow creation during the application's lifetime.

 All implementations that declare compliance with version 2.2 of the specification must implement this method. For the
 purpose of backward compatibility with environments that extend `
Application` but do not override this method, an implementation is provided that returns `null`. Due to the
 decoratable nature of `Application`, code calling this method should always check for a `null` return.

Overrides:
`getFlowHandler` in class `Application`
Returns:
the flow handler.

-

### setFlowHandler

public void setFlowHandler(FlowHandler newHandler)
Description copied from class: `Application`

 Set the `FlowHandler` instance used by the `NavigationHandler` to satisfy the requirements of the faces
 flows feature.

Overrides:
`setFlowHandler` in class `Application`
Parameters:
`newHandler` - the flow handler to set.

-

### evaluateExpressionGet

public <T> T evaluateExpressionGet(FacesContext context,
 String expression,
 Class<? extends T> expectedType)
                            throws jakarta.el.ELException

 The default behavior of this method is to call
 `Application.evaluateExpressionGet(jakarta.faces.context.FacesContext, String, Class)` on the wrapped
 `Application` object.

Overrides:
`evaluateExpressionGet` in class `Application`
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

### addELContextListener

public void addELContextListener(jakarta.el.ELContextListener listener)

 The default behavior of this method is to call `Application.addELContextListener(jakarta.el.ELContextListener)`
 on the wrapped `Application` object.

Overrides:
`addELContextListener` in class `Application`
Parameters:
`listener` - the Jakarta Expression Language context listener to add.

-

### removeELContextListener

public void removeELContextListener(jakarta.el.ELContextListener listener)

 The default behavior of this method is to call
 `Application.removeELContextListener(jakarta.el.ELContextListener)` on the wrapped `Application` object.

Overrides:
`removeELContextListener` in class `Application`
Parameters:
`listener` - the Jakarta Expression Language context listener to remove.

-

### getELContextListeners

public jakarta.el.ELContextListener[] getELContextListeners()

 The default behavior of this method is to call `Application.getELContextListeners()` on the wrapped
 `Application` object.

Overrides:
`getELContextListeners` in class `Application`
Returns:
an array of Jakarta Expression Language context listeners.

-

### publishEvent

public void publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Object source)

 The default behavior of this method is to call
 `Application.publishEvent(jakarta.faces.context.FacesContext, Class, Object)` on the wrapped
 `Application` object.

Overrides:
`publishEvent` in class `Application`
Parameters:
`context` - the `FacesContext` for the current request
`systemEventClass` - The `Class` of event that is being published.
`source` - The source for the event of type `systemEventClass`.

-

### publishEvent

public void publishEvent(FacesContext context,
 Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceBaseType,
 Object source)

 The default behavior of this method is to call
 `Application.publishEvent(jakarta.faces.context.FacesContext, Class, Class, Object)` on the wrapped
 `Application` object.

Overrides:
`publishEvent` in class `Application`
Parameters:
`context` - the `FacesContext` for the current request
`systemEventClass` - The `Class` of event that is being published.
`sourceBaseType` - The `Class` of the source event that must be used to lookup the listener to which
 this event must be published. If this argument is `null` the return from `source.getClass()`
 must be used as the `sourceBaseType`.
`source` - The source for the event of type `systemEventClass`.

-

### subscribeToEvent

public void subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)

 The default behavior of this method is to call
 `Application.subscribeToEvent(Class, Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

Overrides:
`subscribeToEvent` in class `Application`
Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`sourceClass` - the `Class` of the instance which causes events of type `systemEventClass`
 to be fired. May be `null`.
`listener` - the implementation of `SystemEventListener` whose
 `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` method must be called when events of type
 `systemEventClass` are fired.

-

### subscribeToEvent

public void subscribeToEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)

 The default behavior of this method is to call
 `Application.subscribeToEvent(Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

Overrides:
`subscribeToEvent` in class `Application`
Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`listener` - the implementation of `SystemEventListener` whose
 `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` method must be called when events of type
 `systemEventClass` are fired.

 See `Application.subscribeToEvent(java.lang.Class,java.lang.Class,jakarta.faces.event.SystemEventListener)` for an
 additional requirement regarding when it is valid to call this method.

-

### unsubscribeFromEvent

public void unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 Class<?> sourceClass,
 SystemEventListener listener)

 The default behavior of this method is to call
 `Application.unsubscribeFromEvent(Class, Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

Overrides:
`unsubscribeFromEvent` in class `Application`
Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`sourceClass` - the `Class` of the instance which causes events of type `systemEventClass`
 to be fired. May be `null`.
`listener` - the implementation of `SystemEventListener` to remove from the internal
 data structure.

-

### unsubscribeFromEvent

public void unsubscribeFromEvent(Class<? extends SystemEvent> systemEventClass,
 SystemEventListener listener)

 The default behavior of this method is to call
 `Application.unsubscribeFromEvent(Class, jakarta.faces.event.SystemEventListener)` on the wrapped
 `Application` object.

Overrides:
`unsubscribeFromEvent` in class `Application`
Parameters:
`systemEventClass` - the `Class` of event for which `listener` must be fired.
`listener` - the implementation of `SystemEventListener` to remove from the internal
 data structure.

-

### getSearchExpressionHandler

public SearchExpressionHandler getSearchExpressionHandler()
Description copied from class: `Application`

 Return the thread-safe singleton `SearchExpressionHandler` for this application.

Overrides:
`getSearchExpressionHandler` in class `Application`
Returns:
the `SearchExpressionHandler`.

-

### setSearchExpressionHandler

public void setSearchExpressionHandler(SearchExpressionHandler searchExpressionHandler)
Description copied from class: `Application`

 Set the `SearchExpressionHandler` instance used by the application.

Overrides:
`setSearchExpressionHandler` in class `Application`
Parameters:
`searchExpressionHandler` - the `SearchExpressionHandler`.

-

### addSearchKeywordResolver

public void addSearchKeywordResolver(SearchKeywordResolver resolver)
Description copied from class: `Application`

 Cause the argument `resolver` to be added to the head of the resolver chain.

 It is not possible to remove a `SearchKeywordResolver` registered with this method, once it has been
 registered.

 The default implementation throws `UnsupportedOperationException` and is provided for the sole purpose of
 not breaking existing applications that extend `Application`.

Overrides:
`addSearchKeywordResolver` in class `Application`
Parameters:
`resolver` - the SearchKeywordResolver to add.

-

### getSearchKeywordResolver

public SearchKeywordResolver getSearchKeywordResolver()
Description copied from class: `Application`

 Return the singleton `SearchKeywordResolver` instance to be used for all search keyword resolution. This is
 actually an instance of a composite SearchKeywordResolver that must contain the following
 `SearchKeywordResolver` instances in the following order:

    - 

 `SearchKeywordResolver` instances declared using the <search-keyword-resolver> element in the
 application configuration resources.

    - 

 Any `SearchKeywordResolver` instances added by calls to `Application.addSearchKeywordResolver(jakarta.faces.component.search.SearchKeywordResolver)`.

    - 

 The `SearchKeywordResolver` implementations for `@all`, `@child(n)`,
 `@form`, `@id(...)`, `@namingcontainer`, `@next`, `@none`,
 `@parent`, `@previous`, `@root` and `@this`.

 The default implementation throws `UnsupportedOperationException` and is provided for the sole purpose of
 not breaking existing applications that extend `Application`.

Overrides:
`getSearchKeywordResolver` in class `Application`
Returns:
the `SearchKeywordResolver`.
