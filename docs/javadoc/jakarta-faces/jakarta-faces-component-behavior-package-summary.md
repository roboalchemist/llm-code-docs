# Package jakarta.faces.component.behavior

---

package jakarta.faces.component.behavior

-

Related Packages

Package
Description
jakarta.faces.component

jakarta.faces.component.html

 Specialized user interface component classes for HTML.

jakarta.faces.component.search

jakarta.faces.component.visit

-

Class
Description
AjaxBehavior

 An instance of this class is added as a
 `ClientBehavior` to a component using the
 `ClientBehaviorHolder.addClientBehavior(java.lang.String, jakarta.faces.component.behavior.ClientBehavior)` contract that components implement.

Behavior

 The **Behavior** interface is the root API of the component behavior model.

BehaviorBase

 **BehaviorBase** is a convenience base class that provides a default implementation of the
 `Behavior` contract.

ClientBehavior

 **ClientBehavior** is the base contract for `Behavior`s that attach script content to client-side
 events exposed by `ClientBehaviorHolder` components.

ClientBehaviorBase

 **ClientBehaviorBase** is a convenience base class that implements the default concrete behavior of all
 methods defined by `ClientBehavior`.

ClientBehaviorContext

 **ClientBehaviorContext** provides context information that may be useful
 to `ClientBehavior.getScript(jakarta.faces.component.behavior.ClientBehaviorContext)` implementations.

ClientBehaviorContext.Parameter

 **Parameter** instances represent name/value pairs that "submitting" ClientBehavior implementations
 should include when posting back into the Faces lifecycle.

ClientBehaviorHint

 An enum that specifies hints that describes the behavior of ClientBehavior implementations.

ClientBehaviorHolder

 The **ClientBehaviorHolder** interface may be implemented by any concrete
 `UIComponent` that wishes to support client behaviors as defined by
 `ClientBehavior`.

FacesBehavior

 The presence of this annotation on a class automatically registers the class with the runtime as a `Behavior`.

FacesBehavior.Literal

 Supports inline instantiation of the `FacesBehavior` qualifier.
