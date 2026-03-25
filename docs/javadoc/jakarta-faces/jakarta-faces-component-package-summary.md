# Package jakarta.faces.component

---

package jakarta.faces.component

-

Related Packages

Package
Description
jakarta.faces

jakarta.faces.component.behavior

jakarta.faces.component.html

 Specialized user interface component classes for HTML.

jakarta.faces.component.search

jakarta.faces.component.visit

-

Class
Description
ActionSource

 **ActionSource** is an interface that may be implemented by any concrete `UIComponent` that wishes
 to be a source of `ActionEvent`s, including the ability to invoke application actions via the default
 `ActionListener` mechanism.

ActionSource2
Deprecated, for removal: This API element is subject to removal in a future version.
Use `ActionSource` instead.

ContextCallback

 A simple callback interace that enables taking action on a specific UIComponent (either facet or child) in the view
 while preserving any contextual state for that component instance in the view.

Doctype

 **Doctype** is an interface that must be implemented by any `UIComponent` that represents a document type declaration.

EditableValueHolder

 **EditableValueHolder** is an extension of
 ValueHolder that describes additional features supported by editable components, including `ValueChangeEvent`s
 and `Validator`s.

FacesComponent

 The presence of this annotation on a class that extends `UIComponent`
 must cause the runtime to register this class as a component suitable for inclusion in a view.

NamingContainer

 **NamingContainer** is an interface that must be implemented by any
 `UIComponent` that wants to be a naming container.

PartialStateHolder

 Components that want to leverage the partial state saving feature must implement this interface instead of
 implementing `StateHolder`, from which this interface inherits.

StateHelper

 Define a `Map`-like contract that makes it easier for components to implement `PartialStateHolder`.

StateHolder

 This interface is implemented by classes that need to save their
 state between requests.

TransientStateHelper

 Define a `Map`-like contract that makes it easier for components to implement
 `TransientStateHolder`.

TransientStateHolder

 This interface is implemented by classes that need to save state that is expected to be available only within the
 scope of the current request.

UIColumn

 **UIColumn** is a `UIComponent` that represents a single column of data within a parent
 `UIData` component.

UICommand

 **UICommand** is a `UIComponent` that represents a user interface component which, when activated
 by the user, triggers an application specific "command" or "action".

UIComponent

 **UIComponent** is the base class for all user interface components in Jakarta Server
 Faces.

UIComponentBase

 **UIComponentBase** is a
 convenience base class that implements the default concrete behavior of all methods defined by `UIComponent`.

UIData

 **UIData** is a
 `UIComponent` that supports data binding to a collection of data objects represented by a `DataModel`
 instance, which is the current value of this component itself (typically established via a `ValueExpression`).

UIForm

 **UIForm** is a `UIComponent` that represents an input form to be
 presented to the user, and whose child components represent (among other things) the input fields to be included when
 the form is submitted.

UIGraphic

 **UIGraphic** is a `UIComponent` that displays a graphical image to the user.

UIImportConstants

UIInput

 **UIInput** is a `UIComponent` that represents a component that both
 displays output to the user (like `UIOutput` components do) and processes request parameters on the subsequent
 request that need to be decoded.

UIInput.ValidateEmptyFields

 Allowed values for the initialization parameter named by the "jakarta.faces.VALIDATE_EMPTY_FIELDS" constant.

UIMessage

 This component is responsible for displaying messages for a specific
 `UIComponent`, identified by a `clientId`  or component id
 relative to the closest ancestor `NamingContainer`.

UIMessages

 The renderer for this component is responsible for obtaining the messages from the `FacesContext` and
 displaying them to the user.

UINamingContainer

 **UINamingContainer** is a convenience base class for components that wish
 to implement `NamingContainer` functionality.

UIOutcomeTarget

 This component is paired with the `jakarta.faces.Button` or
 `jakarta.faces.Link` renderers and encapsulates properties relating to the rendering of outcomes directly
 to the response.

UIOutput

 **UIOutput** is a `UIComponent` that has a
 value, optionally retrieved from a model tier bean via a value expression, that is displayed to the user.

UIPanel

 **UIPanel** is a `UIComponent` that manages the layout of its child components.

UIParameter

 **UIParameter** is a `UIComponent` that represents an optionally named configuration parameter for
 a parent component.

UISelectBoolean

 **UISelectBoolean** is a `UIComponent` that represents a single boolean (`true` or
 `false`) value.

UISelectItem

 **UISelectItem** is a component that may be
 nested inside a `UISelectMany` or `UISelectOne` component, and causes the addition of a
 `SelectItem` instance to the list of available options for the parent component.

UISelectItemGroup

 **UISelectItemGroup** is a component that may be nested inside a `UISelectMany` or `UISelectOne` component, and causes the addition
 of one `SelectItemGroup` of one or more `SelectItem` instances to the list of available options in the parent component.

UISelectItemGroups

 **UISelectItemGroups** is a component that may be nested inside a `UISelectMany` or `UISelectOne` component, and causes the addition
 of one or more `SelectItemGroup` of one or more `SelectItem` instances to the list of available options in the parent component.

UISelectItems

 **UISelectItems** is a component that may be nested inside a `UISelectMany` or `UISelectOne`
 component, and causes the addition of one or more `SelectItem` instances to the list of available options in
 the parent component.

UISelectMany

 **UISelectMany** is a `UIComponent` that
 represents the user's choice of a zero or more items from among a discrete set of available options.

UISelectOne

 **UISelectOne** is a `UIComponent` that represents the user's choice
 of zero or one items from among a discrete set of available options.

UIViewAction

 **UIViewAction** represents a method invocation that occurs during the
 request processing lifecycle, usually in response to an initial request, as opposed to a postback.

UIViewParameter

 **UIViewParameter** represents a binding between a
 request parameter and a model property or `UIViewRoot` property.

UIViewParameter.Reference

 Inner class to encapsulate a `UIViewParameter` instance so that it may be safely referenced regardless of
 whether or not the current view is the same as the view in which this `UIViewParameter` resides.

UIViewRoot

 **UIViewRoot** is the UIComponent that represents the root of
 the UIComponent tree.

UIWebsocket

 The `<f:websocket>` tag opens an one-way (server to client) websocket based push connection in
 client side which can be reached from server side via `PushContext` interface injected in any CDI/container
 managed artifact via `@``Push` annotation.

UniqueIdVendor

 **UniqueIdVendor** is an interface implemented by `UIComponents` that also implement
 `NamingContainer` so that they can provide unique ids based on their own clientId.

UpdateModelException

 This exception indicates a failure to update the model and is created to wrap any exception that occurs during
 `UIInput.updateModel(jakarta.faces.context.FacesContext)`.

ValueHolder

 **ValueHolder** is an interface that may be implemented by any concrete
 `UIComponent` that wishes to support a local value, as well as access data in the model tier via a *value
 expression*, and support conversion between String and the model tier data's native data type.
