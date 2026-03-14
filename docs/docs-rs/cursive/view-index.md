cursive
# Module view 
Source 
## Modules§
scrollCore mechanisms to implement scrolling.
## Structs§
CannotFocusError indicating a view could not take focus.MarginsFour values representing each direction.ScrollBaseDeprecatedProvide scrolling functionalities to a view.SizeCacheCache around a one-dimensional layout result.ViewNotFoundError indicating a view was not found.
## Enums§
OffsetSingle-dimensional offset policy.ScrollStrategyDefines the scrolling behaviour on content or size changeSelectorSelects a single view (if any) in the tree.SizeConstraintSingle-dimensional constraint on a view size.
## Traits§
AnyViewA view that can be downcasted to its concrete type.FinderProvides `call_on<V: View>` to views.IntoBoxedViewRepresents a type that can be made into a `Box<View>`.NameableMakes a view wrappable in an `NamedView`.ResizableMakes a view wrappable in a `ResizedView`.ScrollableMakes a view wrappable in a `ScrollView`.ViewMain trait defining a view behaviour.ViewWrapperGeneric wrapper around a view.
## Type Aliases§
PositionLocation of the view on screen