# Package jakarta.faces.lifecycle

---

package jakarta.faces.lifecycle

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
ClientWindow

 This class represents a client window, which may be a browser tab, browser window, browser pop-up, portlet, or
 anything else that can display a `UIComponent` hierarchy rooted at a
 `UIViewRoot`.

ClientWindowFactory

 Create `ClientWindow` instances based on the incoming request.

ClientWindowScoped

ClientWindowScoped is a CDI scope that causes the runtime to consider classes
 with this annotation to be in the scope of the current `ClientWindow`.

ClientWindowWrapper

 Wrapper for `ClientWindow`

Lifecycle

 **Lifecycle** manages the processing of the entire lifecycle of a
 particular Jakarta Faces request.

LifecycleFactory

 **LifecycleFactory** is a factory object that creates
 (if needed) and returns `Lifecycle` instances.

LifecycleWrapper

 Provides a simple implementation of `Lifecycle` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `Lifecycle` instance.
