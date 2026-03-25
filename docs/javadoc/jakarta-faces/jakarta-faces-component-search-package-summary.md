# Package jakarta.faces.component.search

---

package jakarta.faces.component.search

-

Related Packages

Package
Description
jakarta.faces.component

jakarta.faces.component.behavior

jakarta.faces.component.html

 Specialized user interface component classes for HTML.

jakarta.faces.component.visit

-

Class
Description
ComponentNotFoundException

 Typed `FacesException` for the `SearchExpressionHandler`, if a component can't be resolved.

SearchExpressionContext

 A context object that is used to hold state relating to resolve a search expression.

SearchExpressionContextFactory

 Provide for separation of interface and implementation for the `SearchExpressionContext` contract.

SearchExpressionHandler

The **SearchExpressionHandler** is responsible for resolving *search
 expression(s)*

SearchExpressionHandlerWrapper

 Provides a simple implementation of `SearchExpressionHandler` that can be subclassed by developers wishing to
 provide specialized behavior to an existing `SearchExpressionHandler` instance.

SearchExpressionHint

 An enum that specifies hints that impact the behavior of a component tree search.

SearchKeywordContext

 **SearchKeywordContext** provides context information that may be useful to
 `SearchKeywordResolver.resolve(jakarta.faces.component.search.SearchKeywordContext, jakarta.faces.component.UIComponent, java.lang.String)` implementations.

SearchKeywordResolver

 A **SearchKeywordResolver** is responsible for resolving a single keyword.

UntargetableComponent

Components implementing this interface are ignored by the algorithm - especially in
 the implementation of `@child(n)`, `@next` and `@previous`.
