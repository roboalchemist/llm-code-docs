# Source: https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors

Title: Visitors - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors

Markdown Content:
This is documentation for **v14**, which is no longer actively maintained.

For up-to-date documentation, see the

[latest stable version](https://chillicream.com/docs/hotchocolate/v15/api-reference/visitors).

Hot Chocolate creates an abstract syntax tree for every incoming request. The execution engine evaluates this syntax tree in many different ways. Validation is a good example. Every incoming request has to be validated. The execution engine has to be sure that the semantic of the requested document is correct. A set of rules is applied to the syntax tree, to find potential semantic flaws.

Usually, you do not have to access the _AST_ directly. The AST only becomes significant, when you want to change execution behavior based on the structure of the query. For example features like _Filtering_, _Sorting_, or _Selection_, analyze the incoming query and generate expressions based on it.

Hot Chocolate provides you with different APIs that support you to traverse these trees. The `SyntaxWalker` is a visitor that has built-in all the logic to _walk down a syntax tree_.

The `SyntaxWalker` is completely stateless. All the state is on a context object that is passed along. The generic argument `TContext` of `SyntaxWalker<TContext>` denotes the type of the context.

To start the visitation of a _GraphQL_ syntax tree, you have to pass the node and the context the visitation should start from to the visitors `Visit` method.

* * *

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors#visitation)Visitation
---------------------------------------------------------------------------------------------

To start the visitation of a _GraphQL_ syntax tree, you have to pass the node and the context the visitation should start from to the visitors `Visit` method. On its way down the syntax tree, the visitor _enters_ a node. The visitor then gets the children of the current node and _enters_ its children. Once the visitor reached a leaf node, it starts walking back up the tree and _leaves_ all the nodes. The visitor provides a virtual `Enter` and a virtual `Leave` method for all _GraphQL_ AST nodes. These methods are called from the visitor as it _enters_ or _leaves_ a node.

The syntax walker provides a few methods in addition to the `Enter` and `Leave` methods. For these two methods, there are also convenience methods that are called right _before_ and _after_ the method call. Namely, `OnBeforeEnter`, `OnAfterEnter`, `OnBeforeLeave`, `OnAfterLeave`. These methods can modify the current `TContext`. These _before_ and _after_ methods are good places to initialize state that is used in the main _enter_ or _leave_ method. e.g. before entering a `FieldNode`, you may want to peek the latest type from the context and get the instance of the `ObjectField` corresponding to `FieldNode` of this type. You may also want to push this type onto the context to then use it in the `Enter` method.

> **⚠️ NOTE:** In the following sequence diagram the participants do **NOT** represent any object instances. Furthermore, many steps are hidden in this example. The visualization below should just give you provide you visual insight on the order of the methods being called.

GraphQL

query GetFoos {

foo {

bar

}

}

1.   We start walking down the tree and _enter_. 

 Call the `csharp±OnBeforeEnter(OperationDefinitionNode node, TContext context)`
2.   Call the `csharp±Enter(OperationDefinitionNode node, TContext context)`
3.   Call the `csharp±OnAfterEnter(OperationDefinitionNode node, TContext context)`
4.   Call the `csharp±VisitChildren(OperationDefinitionNode node, TContext context)`
5.   Call the `csharp±OnBeforeEnter(ObjectFieldNode node, TContext context)`
6.   Call the `csharp±Enter(ObjectFieldNode node, TContext context)`
7.   Call the `csharp±OnAfterEnter(ObjectFieldNode node, TContext context)`
8.   Call the `csharp±VisitChildren(ObjectFieldNode node, TContext context)`
9.   We walk back up the tree and _leave_
10.   Call the `csharp±OnBeforeLeave(ObjectFieldNode node, TContext context)`
11.   Call the `csharp±Leave(ObjectFieldNode node, TContext context)`
12.   Call the `csharp±OnAfterLeave(ObjectFieldNode node, TContext context)`
13.   We walk back up the tree and _leave_.
14.   Call the `csharp±OnBeforeLeave(OperationDefinitionNode node, TContext context)`
15.   Call the `csharp±Leave(OperationDefinitionNode node, TContext context)`
16.   Call the `csharp±OnAfterLeave(OperationDefinitionNode node, TContext context)`

* * *

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors#visitor-actions)Visitor Actions
-------------------------------------------------------------------------------------------------------

The _Enter_ and _Leave_ methods return visitor actions. These methods control the visitors' next step in the visitation. Visitor actions can be used to _skip_ further visitation and step back up, or to _continue_ and walk the current branch of the tree further down.

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors#continue)Continue
-----------------------------------------------------------------------------------------

If `Continue` is returned from the `Enter` or `Leave` method visitation on the current branch continues.

In the following example `Continue` is returned from the onEnter method. The visitor calls `VisitChildren` and continues by _entering_ the selection set.

GraphQL

query {

foo {

bar

baz @onEnter(return: CONTINUE) {

quux

}

qux

}

}

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors#skip)Skip
---------------------------------------------------------------------------------

If `Skip` is returned from the `Enter` or `Leave` method, further visitation on this node stops.

In the following example `Skip` is returned from the onEnter method. The visitor skips the field _baz_. It continues visitation by _entering_ the field _qux_.

GraphQL

query {

foo {

bar

baz @onEnter(return: SKIP) {

quux

}

qux

}

}

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors#skipandleave)SkipAndLeave
-------------------------------------------------------------------------------------------------

If `SkipAndLeave` is returned from the `Enter` method, further visitation on this node stops. Instead of directly calling the next `Enter` method. The visitor calls the `Leave` method of the current node first.

In the following example `SkipAndLeave` is returned from the onEnter method. The visitor skips the field _baz_. Before it continues visitation with the field _qux_ it _leaves_ the field _baz_ by calling `Leave`

GraphQL

query {

foo {

bar

baz @onEnter(return: SKIPANDLEAVE) {

quux

}

qux

}

}

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors#break)Break
-----------------------------------------------------------------------------------

If `Break` is returned from the `Enter` or `Leave` method, further visitation on this branch stops.

In the following example `Break` is returned from the onEnter method. The visitor immediately starts walking back up. The visitor calls the `Leave` on `foo` instead of visiting the selections set of _baz_ it skips _baz_ and _qux_.

GraphQL

query {

foo {

bar

baz @onEnter(return: BREAK) {

quux

}

qux

}

}

Last updated on **2026-02-17** by**Tobias Tengler**
