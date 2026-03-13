# Package jakarta.faces.component.visit

---

package jakarta.faces.component.visit

-

Related Packages

Package
Description
jakarta.faces.component

jakarta.faces.component.behavior

jakarta.faces.component.html

 Specialized user interface component classes for HTML.

jakarta.faces.component.search

-

Class
Description
VisitCallback

 A simple callback interface that enables taking action on a specific UIComponent (either facet or child) during a
 component tree visit.

VisitContext

 A context object that is used to hold state relating to performing a component tree visit.

VisitContextFactory

 Provide for separation of interface and implementation for the
 `VisitContext` contract.

VisitContextWrapper

 Provides a simple implementation of `VisitContext` that can be
 subclassed by developers wishing to provide specialized behavior to an existing `VisitContext` instance.

VisitHint

 An enum that specifies hints that impact the behavior of a component tree
 visit.

VisitResult

 An enum that specifies the possible results of a call to `VisitCallback.visit(jakarta.faces.component.visit.VisitContext, jakarta.faces.component.UIComponent)`.
