# Package jakarta.faces.push

---

package jakarta.faces.push

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
Push

 The CDI annotation `@``Push` allows you to inject a `PushContext` associated with a given
 `<f:websocket>` channel in any container managed artifact in WAR.

Push.Literal

 Supports inline instantiation of the `Push` qualifier.

PushContext

 CDI interface to send a message object to the push socket channel as identified by `@``Push`.
