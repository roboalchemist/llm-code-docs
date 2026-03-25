Package jakarta.faces

# Interface FacesWrapper<T>

Type Parameters:
`T` - the wrapped type.

All Known Implementing Classes:
`ActionListenerWrapper`, `ApplicationFactory`, `ApplicationWrapper`, `ClientWindowFactory`, `ClientWindowWrapper`, `ConfigurableNavigationHandlerWrapper`, `ExceptionHandlerFactory`, `ExceptionHandlerWrapper`, `ExternalContextFactory`, `ExternalContextWrapper`, `FaceletCacheFactory`, `FacesContextFactory`, `FacesContextWrapper`, `FacesServletFactory`, `FlashFactory`, `FlashWrapper`, `FlowHandlerFactoryWrapper`, `LifecycleFactory`, `LifecycleWrapper`, `NavigationCaseWrapper`, `NavigationHandlerWrapper`, `PartialResponseWriter`, `PartialResponseWriterWrapper`, `PartialViewContextFactory`, `PartialViewContextWrapper`, `RendererWrapper`, `RenderKitFactory`, `RenderKitWrapper`, `ResourceHandlerWrapper`, `ResourceWrapper`, `ResponseWriterWrapper`, `SearchExpressionContextFactory`, `SearchExpressionHandlerWrapper`, `StateManagerWrapper`, `TagHandlerDelegateFactory`, `ViewDeclarationLanguageFactory`, `ViewDeclarationLanguageWrapper`, `ViewHandlerWrapper`, `VisitContextFactory`, `VisitContextWrapper`

---

public interface FacesWrapper<T>

 Any wrapper class in Jakarta Faces that must provide access to the
 object it wraps must implement this interface.

 The expected usage of all subclasses is to provide a constructor that takes an instance of type `T`, which
 sets the instance variable that is returned from the `getWrapped()` method.

Since:
2.0

-

## Method Summary

Modifier and Type
Method
Description
`T`
`getWrapped()`

 A class that implements this interface uses this method to return an instance of the class being wrapped.

-

## Method Details

-

### getWrapped

T getWrapped()

 A class that implements this interface uses this method to return an instance of the class being wrapped.

Returns:
the wrapped instance.
Since:
2.0
