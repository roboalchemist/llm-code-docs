# Package jakarta.faces.event

---

package jakarta.faces.event

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
AbortProcessingException

 An exception that may be thrown by event listeners to terminate the processing of the current event.

ActionEvent

 An `ActionEvent` represents the activation of a user interface component (such as a `UICommand`).

ActionListener

 A listener interface for receiving
 `ActionEvent`s.

ActionListenerWrapper

 Provides a simple implementation of `ActionListener` that can be subclassed by developers wishing to provide
 specialized behavior to an existing `ActionListener` instance.

AfterPhase

 This qualifier allows you to observe after phase events via CDI.

AfterPhase.Literal

 Supports inline instantiation of the `AfterPhase` qualifier.

AjaxBehaviorEvent

 **AjaxBehaviorEvent** represents the component behavior
 specific to `Ajax`).

AjaxBehaviorListener

 By implementing this class, an object indicates that it is a listener for one or more kinds of
 `BehaviorEvent`s.

BeforePhase

 This qualifier allows you to observe before phase events via CDI.

BeforePhase.Literal

 Supports inline instantiation of the `BeforePhase` qualifier.

BehaviorEvent

 **BehaviorEvent** is the event that can be generated from
 component `Behavior`.

BehaviorEvent.FacesComponentEvent

 Behavior events supported by Faces components.

BehaviorListener

 A generic base interface for event listeners for various types of `BehaviorEvent`s.

ComponentSystemEvent

 **ComponentSystemEvent** is the base class for
 `SystemEvent`s that are specific to a `UIComponent` instance.

ComponentSystemEventListener

 Implementors of this class do not need an `isListenerForSource()` method because they are only installed
 on specific component instances, therefore the `isListenerForSource()` method is implicit.

ExceptionQueuedEvent

 The system event facility will create an instance of this class whenever
 `Application.publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` is called with `ExceptionQueuedEvent.class` as
 `systemEventClass` argument.

ExceptionQueuedEventContext

 This helper class provides context to the `ExceptionQueuedEvent` regarding the state of the system at the point
 in time when the `ExceptionQueuedEvent` occurs and links the `ExceptionQueuedEvent` to the
 `ExceptionHandler` by virtue of implementing `SystemEventListener`.

FacesEvent

 **FacesEvent** is the base class for user interface and application events that can be fired by
 `UIComponent`s.

FacesListener

 A generic base interface for event listeners for various types of `FacesEvent`s.

ListenerFor

 Classes tagged with this annotation are installed as listeners using the method
 `Application.subscribeToEvent(java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Class<?>, jakarta.faces.event.SystemEventListener)` or
 `UIComponent.subscribeToEvent(java.lang.Class<? extends jakarta.faces.event.SystemEvent>, jakarta.faces.event.ComponentSystemEventListener)` (depending on the circumstances, described below).

ListenersFor

 Container annotation to specify multiple `ListenerFor` annotations on a single class.

MethodExpressionActionListener

 **MethodExpressionActionListener** is an `ActionListener` that wraps a
 `MethodExpression`.

MethodExpressionValueChangeListener

 **MethodExpressionValueChangeListener** is a `ValueChangeListener` that wraps
 a `MethodExpression`.

NamedEvent

 The presence of this annotation on a class automatically registers the class with the runtime as a
 `ComponentSystemEvent` for use with the `<f:event />` tag in a page.

PhaseEvent

 **PhaseEvent** represents the beginning or ending of processing for a particular phase of the request
 processing lifecycle, for the request encapsulated by the specified `FacesContext`.

PhaseId

 Enum of the legal values that may be returned by the
 `getPhaseId()` method of the `FacesEvent` interface.

PhaseListener

 An interface implemented by objects that wish to be notified at the beginning and ending of processing for each
 standard phase of the request processing lifecycle.

PostAddToViewEvent

 When an instance of this event is passed to
 `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener
 implementation may assume that the `source` of this event instance is a `UIComponent` instance and
 that either that instance or an ancestor of that instance was just added to the view.

PostConstructApplicationEvent

 This event must be published by the runtime after all configuration resources have been parsed and processed.

PostConstructViewMapEvent

 This event must be published by a call to {jakarta.faces.application.Application#publishEvent} when the view map is
 first created.

PostKeepFlashValueEvent

 This event must be published by a call to `Application.publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` when a value is
 kept in the flash.

PostPutFlashValueEvent

 This event must be published by a call to `Application.publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` when a value is
 stored in the flash.

PostRenderViewEvent

 When an instance of this event is passed to `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or
 `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener implementation may assume that the
 `source` of this event instance is the `UIViewRoot` instance that has just been rendered.

PostRestoreStateEvent

 When an instance of this event is passed to `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or
 `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener implementation may assume that the
 `source` of this event instance is in a tree that has just had its state restored.

PostValidateEvent

 When an instance of this event is passed to `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or
 `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener implementation may assume that the
 `source` of this event instance is the `UIComponent` instance that is that has just been validated.

PreClearFlashEvent

 This event must be published by a call to `Application.publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` before the flash
 is cleared.

PreDestroyApplicationEvent

 This event must be published by the runtime *before* the factories associated with this `Application`
 are released.

PreDestroyViewMapEvent

 This event must be published by a call to `Application.publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` when the
 `clear` method is called on the map returned from `UIViewRoot.getViewMap()`.

PreRemoveFlashValueEvent

 This event must be published by a call to `Application.publishEvent(jakarta.faces.context.FacesContext, java.lang.Class<? extends jakarta.faces.event.SystemEvent>, java.lang.Object)` when a value is
 removed from the flash.

PreRemoveFromViewEvent

 When an instance of this event is passed to `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or
 `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener implementation may assume that the
 `source` of this event instance is a `UIComponent` instance that is about to be removed from the
 view.

PreRenderComponentEvent

 When an instance of this event is passed to `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or
 `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener implementation may assume that the
 `source` of this event instance is the `UIComponent` instance that is about to be rendered and that
 it is safe to call `UIComponent.getParent()`, `UIComponent.getClientId()`, and other methods that depend upon
 the component instance being in the view.

PreRenderViewEvent

 When an instance of this event is passed to `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or
 `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener implementation may assume that the
 `source` of this event instance is the `UIViewRoot` instance that is about to be rendered.

PreValidateEvent

 When an instance of this event is passed to `SystemEventListener.processEvent(jakarta.faces.event.SystemEvent)` or
 `ComponentSystemEventListener.processEvent(jakarta.faces.event.ComponentSystemEvent)`, the listener implementation may assume that the
 `source` of this event instance is the `UIComponent` instance that is about to be validated.

ScopeContext
Deprecated, for removal: This API element is subject to removal in a future version.
without replacement as this is nowhere used anymore since 4.0.

SystemEvent

 **SystemEvent** is the base class for non-application
 specific events that can be fired by arbitrary objects.

SystemEventListener

 By implementing this class, an object indicates that it is a listener for one or more kinds of `SystemEvent`s.

SystemEventListenerHolder

 Classes that implement this interface agree to maintain a list of `SystemEventListener` instances for each kind
 of `SystemEvent` they can generate.

ValueChangeEvent<T>

 A `ValueChangeEvent` is a notification that the local value of the source component has been change as a result
 of user interface activity.

ValueChangeListener<T>

 A listener interface for receiving `ValueChangeEvent`s.

ViewMapListener

 Marker interface for `SystemEvent`s that indicate the view map has been created
 (`PostConstructViewMapEvent`, or destroyed (`PreDestroyViewMapEvent`).

WebsocketEvent

 This web socket event will be fired when a new `<f:websocket>` has been
 `@``WebsocketEvent.Opened` or `@``WebsocketEvent.Closed`.

WebsocketEvent.Closed

 Indicates that a `<f:websocket>` has closed.

WebsocketEvent.Closed.Literal

 Supports inline instantiation of the `WebsocketEvent.Closed` qualifier.

WebsocketEvent.Opened

 Indicates that a `<f:websocket>` has opened.

WebsocketEvent.Opened.Literal

 Supports inline instantiation of the `WebsocketEvent.Opened` qualifier.
