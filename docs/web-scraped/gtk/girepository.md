# Source: https://docs.gtk.org/girepository/

Title: GIRepository-3.0

URL Source: https://docs.gtk.org/girepository/

Markdown Content:
### Namespace

GIRepository is a library providing access to typelibs and introspection data which describes C APIs

#### Dependencies [](https://docs.gtk.org/girepository/#dependencies)

**GLib**—2.0 The base utility library
[Browse documentation](https://docs.gtk.org/glib/)
**GModule**—2.0 Portable API for dynamically loading modules
[Browse documentation](https://docs.gtk.org/gmodule/)
**GObject**—2.0 The base type system library
[Browse documentation](https://docs.gtk.org/gobject/)
**Gio**—2.0 Useful classes for general purpose I/O, networking, IPC, settings, etc.
[Browse documentation](https://docs.gtk.org/gio/)

*   [Migrating from girepository-1.0 to girepository-2.0](https://docs.gtk.org/girepository/migrating-gi.html)
*   [Classes Hierarchy](https://docs.gtk.org/girepository/classes_hierarchy.html)

[ArgInfo](https://docs.gtk.org/girepository/class.ArgInfo.html "ArgInfo")`GIArgInfo` represents an argument of a callable.

since: 2.80
[BaseInfo](https://docs.gtk.org/girepository/class.BaseInfo.html "BaseInfo")`GIBaseInfo` is the common base struct of all other Info structs accessible through the `GIRepository`API.

since: 2.80
[CallableInfo](https://docs.gtk.org/girepository/class.CallableInfo.html "CallableInfo")`GICallableInfo` represents an entity which is callable.

since: 2.80
[CallbackInfo](https://docs.gtk.org/girepository/class.CallbackInfo.html "CallbackInfo")`GICallbackInfo` represents a callback.

since: 2.80
[ConstantInfo](https://docs.gtk.org/girepository/class.ConstantInfo.html "ConstantInfo")`GIConstantInfo` represents a constant.

since: 2.80
[EnumInfo](https://docs.gtk.org/girepository/class.EnumInfo.html "EnumInfo")A `GIEnumInfo` represents an enumeration.

since: 2.80
[FieldInfo](https://docs.gtk.org/girepository/class.FieldInfo.html "FieldInfo")A `GIFieldInfo` struct represents a field of a struct, union, or object.

since: 2.80
[FlagsInfo](https://docs.gtk.org/girepository/class.FlagsInfo.html "FlagsInfo")A `GIFlagsInfo` represents an enumeration which defines flag values (independently set bits).

since: 2.80
[FunctionInfo](https://docs.gtk.org/girepository/class.FunctionInfo.html "FunctionInfo")`GIFunctionInfo` represents a function, method or constructor.

since: 2.80
[InterfaceInfo](https://docs.gtk.org/girepository/class.InterfaceInfo.html "InterfaceInfo")`GIInterfaceInfo` represents a `GInterface` type.

since: 2.80
[ObjectInfo](https://docs.gtk.org/girepository/class.ObjectInfo.html "ObjectInfo")`GIObjectInfo` represents a classed type.

since: 2.80
[PropertyInfo](https://docs.gtk.org/girepository/class.PropertyInfo.html "PropertyInfo")`GIPropertyInfo` represents a property in a `GObject`.

since: 2.80
[RegisteredTypeInfo](https://docs.gtk.org/girepository/class.RegisteredTypeInfo.html "RegisteredTypeInfo")`GIRegisteredTypeInfo` represents an entity with a `GType` associated.

since: 2.80
[Repository](https://docs.gtk.org/girepository/class.Repository.html "Repository")`GIRepository` is used to manage repositories of namespaces. Namespaces are represented on disk by type libraries (`.typelib` files).

since: 2.80
[SignalInfo](https://docs.gtk.org/girepository/class.SignalInfo.html "SignalInfo")`GISignalInfo` represents a signal.

since: 2.80
[StructInfo](https://docs.gtk.org/girepository/class.StructInfo.html "StructInfo")`GIStructInfo` represents a generic C structure type.

since: 2.80
[TypeInfo](https://docs.gtk.org/girepository/class.TypeInfo.html "TypeInfo")`GITypeInfo` represents a type, including information about direction and transfer.

since: 2.80
[UnionInfo](https://docs.gtk.org/girepository/class.UnionInfo.html "UnionInfo")`GIUnionInfo` represents a union type.

since: 2.80
[UnresolvedInfo](https://docs.gtk.org/girepository/class.UnresolvedInfo.html "UnresolvedInfo")`GIUnresolvedInfo` represents an unresolved symbol.

since: 2.80
[ValueInfo](https://docs.gtk.org/girepository/class.ValueInfo.html "ValueInfo")A `GIValueInfo` represents a value in an enumeration.

since: 2.80
[VFuncInfo](https://docs.gtk.org/girepository/class.VFuncInfo.html "VFuncInfo")`GIVFuncInfo` represents a virtual function.

since: 2.80

[AttributeIter](https://docs.gtk.org/girepository/struct.AttributeIter.html "AttributeIter")An opaque structure used to iterate over attributes in a `GIBaseInfo` struct.

since: 2.80
[BaseInfoStack](https://docs.gtk.org/girepository/struct.BaseInfoStack.html "BaseInfoStack")
[Typelib](https://docs.gtk.org/girepository/struct.Typelib.html "Typelib")`GITypelib` represents a loaded `.typelib` file, which contains a description of a single module’s API.

since: 2.80

[Argument](https://docs.gtk.org/girepository/union.Argument.html "Argument")Stores an argument of varying type.

since: 2.80

[ArrayType](https://docs.gtk.org/girepository/enum.ArrayType.html "ArrayType")The type of array in a `GITypeInfo`.

since: 2.80
[Direction](https://docs.gtk.org/girepository/enum.Direction.html "Direction")The direction of a `GIArgInfo`.

since: 2.80
[RepositoryError](https://docs.gtk.org/girepository/enum.RepositoryError.html "RepositoryError")An error code used with `GI_REPOSITORY_ERROR` in a `GError` returned from a `GIRepository` routine.

since: 2.80
[ScopeType](https://docs.gtk.org/girepository/enum.ScopeType.html "ScopeType")Scope type of a `GIArgInfo` representing callback, determines how the callback is invoked and is used to decided when the invoke structs can be freed.

since: 2.80
[Transfer](https://docs.gtk.org/girepository/enum.Transfer.html "Transfer")`GITransfer` specifies who’s responsible for freeing the resources after an ownership transfer is complete.

since: 2.80
[TypeTag](https://docs.gtk.org/girepository/enum.TypeTag.html "TypeTag")The type tag of a `GITypeInfo`.

since: 2.80

#### Error Domains [](https://docs.gtk.org/girepository/#domains)

[InvokeError](https://docs.gtk.org/girepository/error.InvokeError.html "InvokeError")An error occurring while invoking a function via `gi_function_info_invoke()`.

since: 2.80

[DEPRECATED_ENUMERATOR_IN_2_26_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_26_FOR.html "DEPRECATED_ENUMERATOR_IN_2_26_FOR")
[DEPRECATED_ENUMERATOR_IN_2_28_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_28_FOR.html "DEPRECATED_ENUMERATOR_IN_2_28_FOR")
[DEPRECATED_ENUMERATOR_IN_2_30_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_30_FOR.html "DEPRECATED_ENUMERATOR_IN_2_30_FOR")
[DEPRECATED_ENUMERATOR_IN_2_32_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_32_FOR.html "DEPRECATED_ENUMERATOR_IN_2_32_FOR")
[DEPRECATED_ENUMERATOR_IN_2_34_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_34_FOR.html "DEPRECATED_ENUMERATOR_IN_2_34_FOR")
[DEPRECATED_ENUMERATOR_IN_2_36_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_36_FOR.html "DEPRECATED_ENUMERATOR_IN_2_36_FOR")
[DEPRECATED_ENUMERATOR_IN_2_38_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_38_FOR.html "DEPRECATED_ENUMERATOR_IN_2_38_FOR")
[DEPRECATED_ENUMERATOR_IN_2_40_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_40_FOR.html "DEPRECATED_ENUMERATOR_IN_2_40_FOR")
[DEPRECATED_ENUMERATOR_IN_2_42_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_42_FOR.html "DEPRECATED_ENUMERATOR_IN_2_42_FOR")
[DEPRECATED_ENUMERATOR_IN_2_44_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_44_FOR.html "DEPRECATED_ENUMERATOR_IN_2_44_FOR")
[DEPRECATED_ENUMERATOR_IN_2_46_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_46_FOR.html "DEPRECATED_ENUMERATOR_IN_2_46_FOR")
[DEPRECATED_ENUMERATOR_IN_2_48_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_48_FOR.html "DEPRECATED_ENUMERATOR_IN_2_48_FOR")
[DEPRECATED_ENUMERATOR_IN_2_50_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_50_FOR.html "DEPRECATED_ENUMERATOR_IN_2_50_FOR")
[DEPRECATED_ENUMERATOR_IN_2_52_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_52_FOR.html "DEPRECATED_ENUMERATOR_IN_2_52_FOR")
[DEPRECATED_ENUMERATOR_IN_2_54_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_54_FOR.html "DEPRECATED_ENUMERATOR_IN_2_54_FOR")
[DEPRECATED_ENUMERATOR_IN_2_56_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_56_FOR.html "DEPRECATED_ENUMERATOR_IN_2_56_FOR")
[DEPRECATED_ENUMERATOR_IN_2_58_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_58_FOR.html "DEPRECATED_ENUMERATOR_IN_2_58_FOR")
[DEPRECATED_ENUMERATOR_IN_2_60_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_60_FOR.html "DEPRECATED_ENUMERATOR_IN_2_60_FOR")
[DEPRECATED_ENUMERATOR_IN_2_62_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_62_FOR.html "DEPRECATED_ENUMERATOR_IN_2_62_FOR")
[DEPRECATED_ENUMERATOR_IN_2_64_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_64_FOR.html "DEPRECATED_ENUMERATOR_IN_2_64_FOR")
[DEPRECATED_ENUMERATOR_IN_2_66_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_66_FOR.html "DEPRECATED_ENUMERATOR_IN_2_66_FOR")
[DEPRECATED_ENUMERATOR_IN_2_68_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_68_FOR.html "DEPRECATED_ENUMERATOR_IN_2_68_FOR")
[DEPRECATED_ENUMERATOR_IN_2_70_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_70_FOR.html "DEPRECATED_ENUMERATOR_IN_2_70_FOR")
[DEPRECATED_ENUMERATOR_IN_2_72_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_72_FOR.html "DEPRECATED_ENUMERATOR_IN_2_72_FOR")
[DEPRECATED_ENUMERATOR_IN_2_74_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_74_FOR.html "DEPRECATED_ENUMERATOR_IN_2_74_FOR")
[DEPRECATED_ENUMERATOR_IN_2_76_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_76_FOR.html "DEPRECATED_ENUMERATOR_IN_2_76_FOR")
[DEPRECATED_ENUMERATOR_IN_2_78_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_78_FOR.html "DEPRECATED_ENUMERATOR_IN_2_78_FOR")
[DEPRECATED_ENUMERATOR_IN_2_80_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_80_FOR.html "DEPRECATED_ENUMERATOR_IN_2_80_FOR")
[DEPRECATED_ENUMERATOR_IN_2_82_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_82_FOR.html "DEPRECATED_ENUMERATOR_IN_2_82_FOR")
[DEPRECATED_ENUMERATOR_IN_2_84_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_84_FOR.html "DEPRECATED_ENUMERATOR_IN_2_84_FOR")
[DEPRECATED_ENUMERATOR_IN_2_86_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_86_FOR.html "DEPRECATED_ENUMERATOR_IN_2_86_FOR")
[DEPRECATED_ENUMERATOR_IN_2_88_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_ENUMERATOR_IN_2_88_FOR.html "DEPRECATED_ENUMERATOR_IN_2_88_FOR")
[DEPRECATED_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_FOR.html "DEPRECATED_FOR")
[DEPRECATED_IN_2_26_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_26_FOR.html "DEPRECATED_IN_2_26_FOR")
[DEPRECATED_IN_2_28_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_28_FOR.html "DEPRECATED_IN_2_28_FOR")
[DEPRECATED_IN_2_30_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_30_FOR.html "DEPRECATED_IN_2_30_FOR")
[DEPRECATED_IN_2_32_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_32_FOR.html "DEPRECATED_IN_2_32_FOR")
[DEPRECATED_IN_2_34_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_34_FOR.html "DEPRECATED_IN_2_34_FOR")
[DEPRECATED_IN_2_36_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_36_FOR.html "DEPRECATED_IN_2_36_FOR")
[DEPRECATED_IN_2_38_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_38_FOR.html "DEPRECATED_IN_2_38_FOR")
[DEPRECATED_IN_2_40_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_40_FOR.html "DEPRECATED_IN_2_40_FOR")
[DEPRECATED_IN_2_42_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_42_FOR.html "DEPRECATED_IN_2_42_FOR")
[DEPRECATED_IN_2_44_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_44_FOR.html "DEPRECATED_IN_2_44_FOR")
[DEPRECATED_IN_2_46_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_46_FOR.html "DEPRECATED_IN_2_46_FOR")
[DEPRECATED_IN_2_48_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_48_FOR.html "DEPRECATED_IN_2_48_FOR")
[DEPRECATED_IN_2_50_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_50_FOR.html "DEPRECATED_IN_2_50_FOR")
[DEPRECATED_IN_2_52_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_52_FOR.html "DEPRECATED_IN_2_52_FOR")
[DEPRECATED_IN_2_54_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_54_FOR.html "DEPRECATED_IN_2_54_FOR")
[DEPRECATED_IN_2_56_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_56_FOR.html "DEPRECATED_IN_2_56_FOR")
[DEPRECATED_IN_2_58_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_58_FOR.html "DEPRECATED_IN_2_58_FOR")
[DEPRECATED_IN_2_60_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_60_FOR.html "DEPRECATED_IN_2_60_FOR")
[DEPRECATED_IN_2_62_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_62_FOR.html "DEPRECATED_IN_2_62_FOR")
[DEPRECATED_IN_2_64_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_64_FOR.html "DEPRECATED_IN_2_64_FOR")
[DEPRECATED_IN_2_66_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_66_FOR.html "DEPRECATED_IN_2_66_FOR")
[DEPRECATED_IN_2_68_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_68_FOR.html "DEPRECATED_IN_2_68_FOR")
[DEPRECATED_IN_2_70_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_70_FOR.html "DEPRECATED_IN_2_70_FOR")
[DEPRECATED_IN_2_72_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_72_FOR.html "DEPRECATED_IN_2_72_FOR")
[DEPRECATED_IN_2_74_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_74_FOR.html "DEPRECATED_IN_2_74_FOR")
[DEPRECATED_IN_2_76_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_76_FOR.html "DEPRECATED_IN_2_76_FOR")
[DEPRECATED_IN_2_78_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_78_FOR.html "DEPRECATED_IN_2_78_FOR")
[DEPRECATED_IN_2_80_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_80_FOR.html "DEPRECATED_IN_2_80_FOR")
[DEPRECATED_IN_2_82_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_82_FOR.html "DEPRECATED_IN_2_82_FOR")
[DEPRECATED_IN_2_84_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_84_FOR.html "DEPRECATED_IN_2_84_FOR")
[DEPRECATED_IN_2_86_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_86_FOR.html "DEPRECATED_IN_2_86_FOR")
[DEPRECATED_IN_2_88_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_IN_2_88_FOR.html "DEPRECATED_IN_2_88_FOR")
[DEPRECATED_MACRO_IN_2_26_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_26_FOR.html "DEPRECATED_MACRO_IN_2_26_FOR")
[DEPRECATED_MACRO_IN_2_28_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_28_FOR.html "DEPRECATED_MACRO_IN_2_28_FOR")
[DEPRECATED_MACRO_IN_2_30_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_30_FOR.html "DEPRECATED_MACRO_IN_2_30_FOR")
[DEPRECATED_MACRO_IN_2_32_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_32_FOR.html "DEPRECATED_MACRO_IN_2_32_FOR")
[DEPRECATED_MACRO_IN_2_34_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_34_FOR.html "DEPRECATED_MACRO_IN_2_34_FOR")
[DEPRECATED_MACRO_IN_2_36_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_36_FOR.html "DEPRECATED_MACRO_IN_2_36_FOR")
[DEPRECATED_MACRO_IN_2_38_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_38_FOR.html "DEPRECATED_MACRO_IN_2_38_FOR")
[DEPRECATED_MACRO_IN_2_40_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_40_FOR.html "DEPRECATED_MACRO_IN_2_40_FOR")
[DEPRECATED_MACRO_IN_2_42_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_42_FOR.html "DEPRECATED_MACRO_IN_2_42_FOR")
[DEPRECATED_MACRO_IN_2_44_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_44_FOR.html "DEPRECATED_MACRO_IN_2_44_FOR")
[DEPRECATED_MACRO_IN_2_46_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_46_FOR.html "DEPRECATED_MACRO_IN_2_46_FOR")
[DEPRECATED_MACRO_IN_2_48_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_48_FOR.html "DEPRECATED_MACRO_IN_2_48_FOR")
[DEPRECATED_MACRO_IN_2_50_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_50_FOR.html "DEPRECATED_MACRO_IN_2_50_FOR")
[DEPRECATED_MACRO_IN_2_52_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_52_FOR.html "DEPRECATED_MACRO_IN_2_52_FOR")
[DEPRECATED_MACRO_IN_2_54_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_54_FOR.html "DEPRECATED_MACRO_IN_2_54_FOR")
[DEPRECATED_MACRO_IN_2_56_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_56_FOR.html "DEPRECATED_MACRO_IN_2_56_FOR")
[DEPRECATED_MACRO_IN_2_58_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_58_FOR.html "DEPRECATED_MACRO_IN_2_58_FOR")
[DEPRECATED_MACRO_IN_2_60_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_60_FOR.html "DEPRECATED_MACRO_IN_2_60_FOR")
[DEPRECATED_MACRO_IN_2_62_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_62_FOR.html "DEPRECATED_MACRO_IN_2_62_FOR")
[DEPRECATED_MACRO_IN_2_64_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_64_FOR.html "DEPRECATED_MACRO_IN_2_64_FOR")
[DEPRECATED_MACRO_IN_2_66_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_66_FOR.html "DEPRECATED_MACRO_IN_2_66_FOR")
[DEPRECATED_MACRO_IN_2_68_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_68_FOR.html "DEPRECATED_MACRO_IN_2_68_FOR")
[DEPRECATED_MACRO_IN_2_70_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_70_FOR.html "DEPRECATED_MACRO_IN_2_70_FOR")
[DEPRECATED_MACRO_IN_2_72_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_72_FOR.html "DEPRECATED_MACRO_IN_2_72_FOR")
[DEPRECATED_MACRO_IN_2_74_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_74_FOR.html "DEPRECATED_MACRO_IN_2_74_FOR")
[DEPRECATED_MACRO_IN_2_76_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_76_FOR.html "DEPRECATED_MACRO_IN_2_76_FOR")
[DEPRECATED_MACRO_IN_2_78_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_78_FOR.html "DEPRECATED_MACRO_IN_2_78_FOR")
[DEPRECATED_MACRO_IN_2_80_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_80_FOR.html "DEPRECATED_MACRO_IN_2_80_FOR")
[DEPRECATED_MACRO_IN_2_82_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_82_FOR.html "DEPRECATED_MACRO_IN_2_82_FOR")
[DEPRECATED_MACRO_IN_2_84_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_84_FOR.html "DEPRECATED_MACRO_IN_2_84_FOR")
[DEPRECATED_MACRO_IN_2_86_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_86_FOR.html "DEPRECATED_MACRO_IN_2_86_FOR")
[DEPRECATED_MACRO_IN_2_88_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_MACRO_IN_2_88_FOR.html "DEPRECATED_MACRO_IN_2_88_FOR")
[DEPRECATED_TYPE_IN_2_26_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_26_FOR.html "DEPRECATED_TYPE_IN_2_26_FOR")
[DEPRECATED_TYPE_IN_2_28_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_28_FOR.html "DEPRECATED_TYPE_IN_2_28_FOR")
[DEPRECATED_TYPE_IN_2_30_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_30_FOR.html "DEPRECATED_TYPE_IN_2_30_FOR")
[DEPRECATED_TYPE_IN_2_32_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_32_FOR.html "DEPRECATED_TYPE_IN_2_32_FOR")
[DEPRECATED_TYPE_IN_2_34_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_34_FOR.html "DEPRECATED_TYPE_IN_2_34_FOR")
[DEPRECATED_TYPE_IN_2_36_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_36_FOR.html "DEPRECATED_TYPE_IN_2_36_FOR")
[DEPRECATED_TYPE_IN_2_38_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_38_FOR.html "DEPRECATED_TYPE_IN_2_38_FOR")
[DEPRECATED_TYPE_IN_2_40_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_40_FOR.html "DEPRECATED_TYPE_IN_2_40_FOR")
[DEPRECATED_TYPE_IN_2_42_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_42_FOR.html "DEPRECATED_TYPE_IN_2_42_FOR")
[DEPRECATED_TYPE_IN_2_44_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_44_FOR.html "DEPRECATED_TYPE_IN_2_44_FOR")
[DEPRECATED_TYPE_IN_2_46_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_46_FOR.html "DEPRECATED_TYPE_IN_2_46_FOR")
[DEPRECATED_TYPE_IN_2_48_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_48_FOR.html "DEPRECATED_TYPE_IN_2_48_FOR")
[DEPRECATED_TYPE_IN_2_50_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_50_FOR.html "DEPRECATED_TYPE_IN_2_50_FOR")
[DEPRECATED_TYPE_IN_2_52_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_52_FOR.html "DEPRECATED_TYPE_IN_2_52_FOR")
[DEPRECATED_TYPE_IN_2_54_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_54_FOR.html "DEPRECATED_TYPE_IN_2_54_FOR")
[DEPRECATED_TYPE_IN_2_56_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_56_FOR.html "DEPRECATED_TYPE_IN_2_56_FOR")
[DEPRECATED_TYPE_IN_2_58_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_58_FOR.html "DEPRECATED_TYPE_IN_2_58_FOR")
[DEPRECATED_TYPE_IN_2_60_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_60_FOR.html "DEPRECATED_TYPE_IN_2_60_FOR")
[DEPRECATED_TYPE_IN_2_62_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_62_FOR.html "DEPRECATED_TYPE_IN_2_62_FOR")
[DEPRECATED_TYPE_IN_2_64_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_64_FOR.html "DEPRECATED_TYPE_IN_2_64_FOR")
[DEPRECATED_TYPE_IN_2_66_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_66_FOR.html "DEPRECATED_TYPE_IN_2_66_FOR")
[DEPRECATED_TYPE_IN_2_68_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_68_FOR.html "DEPRECATED_TYPE_IN_2_68_FOR")
[DEPRECATED_TYPE_IN_2_70_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_70_FOR.html "DEPRECATED_TYPE_IN_2_70_FOR")
[DEPRECATED_TYPE_IN_2_72_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_72_FOR.html "DEPRECATED_TYPE_IN_2_72_FOR")
[DEPRECATED_TYPE_IN_2_74_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_74_FOR.html "DEPRECATED_TYPE_IN_2_74_FOR")
[DEPRECATED_TYPE_IN_2_76_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_76_FOR.html "DEPRECATED_TYPE_IN_2_76_FOR")
[DEPRECATED_TYPE_IN_2_78_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_78_FOR.html "DEPRECATED_TYPE_IN_2_78_FOR")
[DEPRECATED_TYPE_IN_2_80_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_80_FOR.html "DEPRECATED_TYPE_IN_2_80_FOR")
[DEPRECATED_TYPE_IN_2_82_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_82_FOR.html "DEPRECATED_TYPE_IN_2_82_FOR")
[DEPRECATED_TYPE_IN_2_84_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_84_FOR.html "DEPRECATED_TYPE_IN_2_84_FOR")
[DEPRECATED_TYPE_IN_2_86_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_86_FOR.html "DEPRECATED_TYPE_IN_2_86_FOR")
[DEPRECATED_TYPE_IN_2_88_FOR](https://docs.gtk.org/girepository/func.DEPRECATED_TYPE_IN_2_88_FOR.html "DEPRECATED_TYPE_IN_2_88_FOR")
[UNAVAILABLE](https://docs.gtk.org/girepository/func.UNAVAILABLE.html "UNAVAILABLE")
[UNAVAILABLE_STATIC_INLINE](https://docs.gtk.org/girepository/func.UNAVAILABLE_STATIC_INLINE.html "UNAVAILABLE_STATIC_INLINE")
[VFUNC_INFO](https://docs.gtk.org/girepository/func.VFUNC_INFO.html "VFUNC_INFO")Casts a `GIVFuncInfo` or derived pointer into a `(GIVFuncInfo*)` pointer.

since: 2.80
