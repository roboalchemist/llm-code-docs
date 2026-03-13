# Package jakarta.faces.render

---

package jakarta.faces.render

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
ClientBehaviorRenderer

 A **ClientBehaviorRenderer** produces the client-side script that implements a
 `ClientBehavior`'s client-side logic.

FacesBehaviorRenderer

 The presence of this annotation on a class automatically registers the class with the runtime as a `ClientBehaviorRenderer`.

FacesRenderer

 The presence of this annotation on a class automatically registers the class with the runtime as a `Renderer`.

Renderer<T extends UIComponent>

 A **Renderer** converts the internal representation of
 `UIComponent`s into the output stream (or writer) associated with the response we are creating for a particular
 request.

RendererWrapper

 Provides a simple implementation of `Renderer` that can be subclassed
 by developers wishing to provide specialized behavior to an existing `Renderer` instance.

RenderKit

 **RenderKit** represents a collection of `Renderer`
 instances that, together, know how to render Jakarta Faces `UIComponent` instances for a specific
 client.

RenderKitFactory

 **RenderKitFactory** is a factory object that
 registers and returns `RenderKit` instances.

RenderKitWrapper

 Provides a simple implementation of `RenderKit` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `RenderKit` instance.

ResponseStateManager

 **ResponseStateManager** is the helper class to
 `StateManager` that knows the specific rendering technology being used to generate
 the response.
