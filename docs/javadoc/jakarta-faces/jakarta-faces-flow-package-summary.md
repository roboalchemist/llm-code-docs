# Package jakarta.faces.flow

---

package jakarta.faces.flow

-

Related Packages

Package
Description
jakarta.faces

jakarta.faces.flow.builder

-

Class
Description
Flow

 **Flow** is the runtime representation of a Faces Flow.

FlowCallNode

A flow call node.

FlowHandler

 **FlowHandler** is the main entry point that enables the runtime to
 interact with the faces flows feature.

FlowHandlerFactory

 **FlowHandlerFactory** is used by the `Application` to create the
 singleton instance of `FlowHandler`.

FlowHandlerFactoryWrapper

 **FlowHandlerFactoryWrapper** provides a simple implementation of `FlowHandlerFactory` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `FlowHandlerFactory` instance.

FlowNode

 **FlowNode** is the base class for all nodes in a faces flow graph.

FlowScoped

 **FlowScoped** is a CDI scope that causes the runtime to consider classes
 with this annotation to be in the scope of the specified `Flow`.

MethodCallNode

 Represents a method call node in the flow graph.

Parameter

 Represents a parameter in any of several places where parameters are needed when processing flows.

ReturnNode

 Represents a return node in the flow graph.

SwitchCase

 Represents a case within a switch node in the flow graph.

SwitchNode

 Represents a switch node in the flow graph.

ViewNode

 **ViewNode** is the class that represents a VDL view in a faces flow graph.
