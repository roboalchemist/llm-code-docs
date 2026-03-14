# Package jakarta.faces.flow.builder

---

package jakarta.faces.flow.builder

-

Related Packages

Package
Description
jakarta.faces.flow

-

Class
Description
FlowBuilder

 A Java language API for building `Flow`s.

FlowBuilderParameter

 The presence of this annotation on a CDI producer method for the `FlowDefinition` annotation causes the
 `FlowBuilder` to be passed to that method.

FlowBuilderParameter.Literal

 Supports inline instantiation of the `FlowBuilderParameter` qualifier.

FlowCallBuilder

 Create a flow call node in the current `Flow`.

FlowDefinition

 The presence of this annotation on a CDI producer method indicates that the method will produce a flow.

FlowDefinition.Literal

 Supports inline instantiation of the `FlowDefinition` qualifier.

MethodCallBuilder

 Create a method call node in the current `Flow`.

NavigationCaseBuilder

 Create a navigation case in the current `Flow`.

NodeBuilder

 Base interface for building all kinds of flow nodes.

ReturnBuilder

 Create a return node in the current `Flow`.

SwitchBuilder

 Create a switch node in the current `Flow`.

SwitchCaseBuilder

 Create a case in the current switch.

ViewBuilder

 Create a view node in the current `Flow`.
