cursive
# Module builder 
Source 
## Structs§
BlueprintDescribes how to build a view.CallbackBlueprintDescribes how to build a callback.ConfigErrorError caused by an invalid config.ContextEverything needed to prepare a view from a config.NoConfigA wrapper around a value that cannot be parsed from config, but can still be stored/retrieved
in a context.ResolveOnceWrapper around a value that makes it Cloneable, but can only be resolved once.WrapperBlueprintDescribes how to build a view wrapper.
## Enums§
ErrorError during config parsing.
## Traits§
ResolvableTrait for types that can be resolved from a context.
## Functions§
resolve_onceReturn a variable-maker (for use in store_with)
## Type Aliases§
BareBuilderCan build a view from a config.BareVarBuilderCan build a callbackBareWrapperBuilderCan build a wrapper from a config.BoxedVarBuilderBoxed variable builderConfigType of a config item.ObjectType of a config object.WrapperCan wrap a view.