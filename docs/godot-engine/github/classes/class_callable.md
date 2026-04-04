:github_url: hide



# Callable

A built-in type representing a method or a standalone function.


## Description

**Callable** is a built-in [Variant<class_Variant>] type that represents a function. It can either be a method within an [Object<class_Object>] instance, or a custom callable used for different purposes (see [is_custom()<class_Callable_method_is_custom>]). Like all [Variant<class_Variant>] types, it can be stored in variables and passed to other functions. It is most commonly used for signal callbacks.


> **TABS**
>

    func print_args(arg1, arg2, arg3 = ""):
        prints(arg1, arg2, arg3)

    func test():
        var callable = Callable(self, "print_args")
        callable.call("hello", "world")  # Prints "hello world ".
        callable.call(Vector2.UP, 42, callable)  # Prints "(0.0, -1.0) 42 Node(node.gd)::print_args"
        callable.call("invalid")  # Invalid call, should have at least 2 arguments.


    // Default parameter values are not supported.
    public void PrintArgs(Variant arg1, Variant arg2, Variant arg3 = default)
    {
        GD.PrintS(arg1, arg2, arg3);
    }

    public void Test()
    {
        // Invalid calls fail silently.
        Callable callable = new Callable(this, MethodName.PrintArgs);
        callable.Call("hello", "world"); // Default parameter values are not supported, should have 3 arguments.
        callable.Call(Vector2.Up, 42, callable); // Prints "(0, -1) 42 Node(Node.cs)::PrintArgs"
        callable.Call("invalid"); // Invalid call, should have 3 arguments.
    }



In GDScript, it's possible to create lambda functions within a method. Lambda functions are custom callables that are not associated with an [Object<class_Object>] instance. Optionally, lambda functions can also be named. The name will be displayed in the debugger, or when calling [get_method()<class_Callable_method_get_method>].

::

    func _init():
        var my_lambda = func (message):
            print(message)

        # Prints "Hello everyone!"
        my_lambda.call("Hello everyone!")

        # Prints "Attack!", when the button_pressed signal is emitted.
        button_pressed.connect(func(): print("Attack!"))

In GDScript, you can access methods and global functions as **Callable**\ s:

::

    tween.tween_callback(node.queue_free)  # Object methods.
    tween.tween_callback(array.clear)  # Methods of built-in types.
    tween.tween_callback(print.bind("Test"))  # Global functions.

\ **Note:** [Dictionary<class_Dictionary>] does not support the above due to ambiguity with keys.

::

    var dictionary = { "hello": "world" }

    # This will not work, `clear` is treated as a key.
    tween.tween_callback(dictionary.clear)

    # This will work.
    tween.tween_callback(Callable.create(dictionary, "clear"))

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Constructors

> **TABLE**
> :widths: auto
>
> +---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Callable<class_Callable>` | :ref:`Callable<class_Callable_constructor_Callable>`\ (\ )                                                                                     |
> +---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Callable<class_Callable>` | :ref:`Callable<class_Callable_constructor_Callable>`\ (\ from\: :ref:`Callable<class_Callable>`\ )                                             |
> +---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Callable<class_Callable>` | :ref:`Callable<class_Callable_constructor_Callable>`\ (\ object\: :ref:`Object<class_Object>`, method\: :ref:`StringName<class_StringName>`\ ) |
> +---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Callable<class_Callable>`     | :ref:`bind<class_Callable_method_bind>`\ (\ ...\ ) |vararg| |const|                                                                               |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Callable<class_Callable>`     | :ref:`bindv<class_Callable_method_bindv>`\ (\ arguments\: :ref:`Array<class_Array>`\ )                                                            |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`       | :ref:`call<class_Callable_method_call>`\ (\ ...\ ) |vararg| |const|                                                                               |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`call_deferred<class_Callable_method_call_deferred>`\ (\ ...\ ) |vararg| |const|                                                             |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`       | :ref:`callv<class_Callable_method_callv>`\ (\ arguments\: :ref:`Array<class_Array>`\ ) |const|                                                    |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Callable<class_Callable>`     | :ref:`create<class_Callable_method_create>`\ (\ variant\: :ref:`Variant<class_Variant>`, method\: :ref:`StringName<class_StringName>`\ ) |static| |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`get_argument_count<class_Callable_method_get_argument_count>`\ (\ ) |const|                                                                 |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`           | :ref:`get_bound_arguments<class_Callable_method_get_bound_arguments>`\ (\ ) |const|                                                               |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`get_bound_arguments_count<class_Callable_method_get_bound_arguments_count>`\ (\ ) |const|                                                   |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>` | :ref:`get_method<class_Callable_method_get_method>`\ (\ ) |const|                                                                                 |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`         | :ref:`get_object<class_Callable_method_get_object>`\ (\ ) |const|                                                                                 |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`get_object_id<class_Callable_method_get_object_id>`\ (\ ) |const|                                                                           |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`get_unbound_arguments_count<class_Callable_method_get_unbound_arguments_count>`\ (\ ) |const|                                               |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`hash<class_Callable_method_hash>`\ (\ ) |const|                                                                                             |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_custom<class_Callable_method_is_custom>`\ (\ ) |const|                                                                                   |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_null<class_Callable_method_is_null>`\ (\ ) |const|                                                                                       |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_standard<class_Callable_method_is_standard>`\ (\ ) |const|                                                                               |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_valid<class_Callable_method_is_valid>`\ (\ ) |const|                                                                                     |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`rpc<class_Callable_method_rpc>`\ (\ ...\ ) |vararg| |const|                                                                                 |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`rpc_id<class_Callable_method_rpc_id>`\ (\ peer_id\: :ref:`int<class_int>`, ...\ ) |vararg| |const|                                          |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Callable<class_Callable>`     | :ref:`unbind<class_Callable_method_unbind>`\ (\ argcount\: :ref:`int<class_int>`\ ) |const|                                                       |
> +-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator !=<class_Callable_operator_neq_Callable>`\ (\ right\: :ref:`Callable<class_Callable>`\ ) |
> +-------------------------+---------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator ==<class_Callable_operator_eq_Callable>`\ (\ right\: :ref:`Callable<class_Callable>`\ )  |
> +-------------------------+---------------------------------------------------------------------------------------------------------+
>

----


## Constructor Descriptions



[Callable<class_Callable>] **Callable**\ (\ ) [🔗<class_Callable_constructor_Callable>]

Constructs an empty **Callable**, with no object nor method bound.


----


[Callable<class_Callable>] **Callable**\ (\ from\: [Callable<class_Callable>]\ )

Constructs a **Callable** as a copy of the given **Callable**.


----


[Callable<class_Callable>] **Callable**\ (\ object\: [Object<class_Object>], method\: [StringName<class_StringName>]\ )

Creates a new **Callable** for the method named `method` in the specified `object`.

\ **Note:** For methods of built-in [Variant<class_Variant>] types, use [create()<class_Callable_method_create>] instead.


----


## Method Descriptions



[Callable<class_Callable>] **bind**\ (\ ...\ ) |vararg| |const| [🔗<class_Callable_method_bind>]

Returns a copy of this **Callable** with one or more arguments bound. When called, the bound arguments are passed *after* the arguments supplied by [call()<class_Callable_method_call>]. See also [unbind()<class_Callable_method_unbind>].

\ **Note:** When this method is chained with other similar methods, the order in which the argument list is modified is read from right to left.


----



[Callable<class_Callable>] **bindv**\ (\ arguments\: [Array<class_Array>]\ ) [🔗<class_Callable_method_bindv>]

Returns a copy of this **Callable** with one or more arguments bound, reading them from an array. When called, the bound arguments are passed *after* the arguments supplied by [call()<class_Callable_method_call>]. See also [unbind()<class_Callable_method_unbind>].

\ **Note:** When this method is chained with other similar methods, the order in which the argument list is modified is read from right to left.


----



[Variant<class_Variant>] **call**\ (\ ...\ ) |vararg| |const| [🔗<class_Callable_method_call>]

Calls the method represented by this **Callable**. Arguments can be passed and should match the method's signature.


----



|void| **call_deferred**\ (\ ...\ ) |vararg| |const| [🔗<class_Callable_method_call_deferred>]

Calls the method represented by this **Callable** in deferred mode, i.e. at the end of the current frame. Arguments can be passed and should match the method's signature.


> **TABS**
>

    func _ready():
        grab_focus.call_deferred()


    public override void _Ready()
    {
        Callable.From(GrabFocus).CallDeferred();
    }



\ **Note:** Deferred calls are processed at idle time. Idle time happens mainly at the end of process and physics frames. In it, deferred calls will be run until there are none left, which means you can defer calls from other deferred calls and they'll still be run in the current idle time cycle. This means you should not call a method deferred from itself (or from a method called by it), as this causes infinite recursion the same way as if you had called the method directly.

See also [Object.call_deferred()<class_Object_method_call_deferred>].


----



[Variant<class_Variant>] **callv**\ (\ arguments\: [Array<class_Array>]\ ) |const| [🔗<class_Callable_method_callv>]

Calls the method represented by this **Callable**. Unlike [call()<class_Callable_method_call>], this method expects all arguments to be contained inside the `arguments` [Array<class_Array>].


----



[Callable<class_Callable>] **create**\ (\ variant\: [Variant<class_Variant>], method\: [StringName<class_StringName>]\ ) |static| [🔗<class_Callable_method_create>]

Creates a new **Callable** for the method named `method` in the specified `variant`. To represent a method of a built-in [Variant<class_Variant>] type, a custom callable is used (see [is_custom()<class_Callable_method_is_custom>]). If `variant` is [Object<class_Object>], then a standard callable will be created instead.

\ **Note:** This method is always necessary for the [Dictionary<class_Dictionary>] type, as property syntax is used to access its entries. You may also use this method when `variant`'s type is not known in advance (for polymorphism).


----



[int<class_int>] **get_argument_count**\ (\ ) |const| [🔗<class_Callable_method_get_argument_count>]

Returns the total number of arguments this **Callable** should take, including optional arguments. This means that any arguments bound with [bind()<class_Callable_method_bind>] are *subtracted* from the result, and any arguments unbound with [unbind()<class_Callable_method_unbind>] are *added* to the result.


----



[Array<class_Array>] **get_bound_arguments**\ (\ ) |const| [🔗<class_Callable_method_get_bound_arguments>]

Returns the array of arguments bound via successive [bind()<class_Callable_method_bind>] or [unbind()<class_Callable_method_unbind>] calls. These arguments will be added *after* the arguments passed to the call, from which [get_unbound_arguments_count()<class_Callable_method_get_unbound_arguments_count>] arguments on the right have been previously excluded.

::

    func get_effective_arguments(callable, call_args):
        assert(call_args.size() - callable.get_unbound_arguments_count() >= 0)
        var result = call_args.slice(0, call_args.size() - callable.get_unbound_arguments_count())
        result.append_array(callable.get_bound_arguments())
        return result


----



[int<class_int>] **get_bound_arguments_count**\ (\ ) |const| [🔗<class_Callable_method_get_bound_arguments_count>]

Returns the total amount of arguments bound via successive [bind()<class_Callable_method_bind>] or [unbind()<class_Callable_method_unbind>] calls. This is the same as the size of the array returned by [get_bound_arguments()<class_Callable_method_get_bound_arguments>]. See [get_bound_arguments()<class_Callable_method_get_bound_arguments>] for details.

\ **Note:** The [get_bound_arguments_count()<class_Callable_method_get_bound_arguments_count>] and [get_unbound_arguments_count()<class_Callable_method_get_unbound_arguments_count>] methods can both return positive values.


----



[StringName<class_StringName>] **get_method**\ (\ ) |const| [🔗<class_Callable_method_get_method>]

Returns the name of the method represented by this **Callable**. If the callable is a GDScript lambda function, returns the function's name or `"<anonymous lambda>"`.


----



[Object<class_Object>] **get_object**\ (\ ) |const| [🔗<class_Callable_method_get_object>]

Returns the object on which this **Callable** is called.


----



[int<class_int>] **get_object_id**\ (\ ) |const| [🔗<class_Callable_method_get_object_id>]

Returns the ID of this **Callable**'s object (see [Object.get_instance_id()<class_Object_method_get_instance_id>]).


----



[int<class_int>] **get_unbound_arguments_count**\ (\ ) |const| [🔗<class_Callable_method_get_unbound_arguments_count>]

Returns the total amount of arguments unbound via successive [bind()<class_Callable_method_bind>] or [unbind()<class_Callable_method_unbind>] calls. See [get_bound_arguments()<class_Callable_method_get_bound_arguments>] for details.

\ **Note:** The [get_bound_arguments_count()<class_Callable_method_get_bound_arguments_count>] and [get_unbound_arguments_count()<class_Callable_method_get_unbound_arguments_count>] methods can both return positive values.


----



[int<class_int>] **hash**\ (\ ) |const| [🔗<class_Callable_method_hash>]

Returns the 32-bit hash value of this **Callable**'s object.

\ **Note:** **Callable**\ s with equal content will always produce identical hash values. However, the reverse is not true. Returning identical hash values does *not* imply the callables are equal, because different callables can have identical hash values due to hash collisions. The engine uses a 32-bit hash algorithm for [hash()<class_Callable_method_hash>].


----



[bool<class_bool>] **is_custom**\ (\ ) |const| [🔗<class_Callable_method_is_custom>]

Returns `true` if this **Callable** is a custom callable. Custom callables are used:

- for binding/unbinding arguments (see [bind()<class_Callable_method_bind>] and [unbind()<class_Callable_method_unbind>]);

- for representing methods of built-in [Variant<class_Variant>] types (see [create()<class_Callable_method_create>]);

- for representing global, lambda, and RPC functions in GDScript;

- for other purposes in the core, GDExtension, and C#.


----



[bool<class_bool>] **is_null**\ (\ ) |const| [🔗<class_Callable_method_is_null>]

Returns `true` if this **Callable** has no target to call the method on. Equivalent to `callable == Callable()`.

\ **Note:** This is *not* the same as `not is_valid()` and using `not is_null()` will *not* guarantee that this callable can be called. Use [is_valid()<class_Callable_method_is_valid>] instead.


----



[bool<class_bool>] **is_standard**\ (\ ) |const| [🔗<class_Callable_method_is_standard>]

Returns `true` if this **Callable** is a standard callable. This method is the opposite of [is_custom()<class_Callable_method_is_custom>]. Returns `false` if this callable is a lambda function.


----



[bool<class_bool>] **is_valid**\ (\ ) |const| [🔗<class_Callable_method_is_valid>]

Returns `true` if the callable's object exists and has a valid method name assigned, or is a custom callable.


----



|void| **rpc**\ (\ ...\ ) |vararg| |const| [🔗<class_Callable_method_rpc>]

Perform an RPC (Remote Procedure Call) on all connected peers. This is used for multiplayer and is normally not available, unless the function being called has been marked as *RPC* (using [@GDScript.@rpc<class_@GDScript_annotation_@rpc>] or [Node.rpc_config()<class_Node_method_rpc_config>]). Calling this method on unsupported functions will result in an error. See [Node.rpc()<class_Node_method_rpc>].


----



|void| **rpc_id**\ (\ peer_id\: [int<class_int>], ...\ ) |vararg| |const| [🔗<class_Callable_method_rpc_id>]

Perform an RPC (Remote Procedure Call) on a specific peer ID (see multiplayer documentation for reference). This is used for multiplayer and is normally not available unless the function being called has been marked as *RPC* (using [@GDScript.@rpc<class_@GDScript_annotation_@rpc>] or [Node.rpc_config()<class_Node_method_rpc_config>]). Calling this method on unsupported functions will result in an error. See [Node.rpc_id()<class_Node_method_rpc_id>].


----



[Callable<class_Callable>] **unbind**\ (\ argcount\: [int<class_int>]\ ) |const| [🔗<class_Callable_method_unbind>]

Returns a copy of this **Callable** with a number of arguments unbound. In other words, when the new callable is called the last few arguments supplied by the user are ignored, according to `argcount`. The remaining arguments are passed to the callable. This allows to use the original callable in a context that attempts to pass more arguments than this callable can handle, e.g. a signal with a fixed number of arguments. See also [bind()<class_Callable_method_bind>].

\ **Note:** When this method is chained with other similar methods, the order in which the argument list is modified is read from right to left.

::

    func _ready():
        foo.unbind(1).call(1, 2) # Calls foo(1).
        foo.bind(3, 4).unbind(1).call(1, 2) # Calls foo(1, 3, 4), note that it does not change the arguments from bind.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [Callable<class_Callable>]\ ) [🔗<class_Callable_operator_neq_Callable>]

Returns `true` if both **Callable**\ s invoke different targets.


----



[bool<class_bool>] **operator ==**\ (\ right\: [Callable<class_Callable>]\ ) [🔗<class_Callable_operator_eq_Callable>]

Returns `true` if both **Callable**\ s invoke the same custom target.

