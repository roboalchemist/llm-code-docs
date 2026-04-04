:github_url: hide



# UndoRedo

**Inherits:** [Object<class_Object>]

Provides a high-level interface for implementing undo and redo operations.


## Description

UndoRedo works by registering methods and property changes inside "actions". You can create an action, then provide ways to do and undo this action using function calls and property changes, then commit the action.

When an action is committed, all of the `do_*` methods will run. If the [undo()<class_UndoRedo_method_undo>] method is used, the `undo_*` methods will run. If the [redo()<class_UndoRedo_method_redo>] method is used, once again, all of the `do_*` methods will run.

Here's an example on how to add an action:


> **TABS**
>

    var undo_redo = UndoRedo.new()

    func do_something():
        pass # Put your code here.

    func undo_something():
        pass # Put here the code that reverts what's done by "do_something()".

    func _on_my_button_pressed():
        var node = get_node("MyNode2D")
        undo_redo.create_action("Move the node")
        undo_redo.add_do_method(do_something)
        undo_redo.add_undo_method(undo_something)
        undo_redo.add_do_property(node, "position", Vector2(100, 100))
        undo_redo.add_undo_property(node, "position", node.position)
        undo_redo.commit_action()


    private UndoRedo _undoRedo;

    public override void _Ready()
    {
        _undoRedo = new UndoRedo();
    }

    public void DoSomething()
    {
        // Put your code here.
    }

    public void UndoSomething()
    {
        // Put here the code that reverts what's done by "DoSomething()".
    }

    private void OnMyButtonPressed()
    {
        var node = GetNode<Node2D>("MyNode2D");
        _undoRedo.CreateAction("Move the node");
        _undoRedo.AddDoMethod(new Callable(this, MethodName.DoSomething));
        _undoRedo.AddUndoMethod(new Callable(this, MethodName.UndoSomething));
        _undoRedo.AddDoProperty(node, "position", new Vector2(100, 100));
        _undoRedo.AddUndoProperty(node, "position", node.Position);
        _undoRedo.CommitAction();
    }



Before calling any of the `add_(un)do_*` methods, you need to first call [create_action()<class_UndoRedo_method_create_action>]. Afterwards you need to call [commit_action()<class_UndoRedo_method_commit_action>].

If you don't need to register a method, you can leave [add_do_method()<class_UndoRedo_method_add_do_method>] and [add_undo_method()<class_UndoRedo_method_add_undo_method>] out; the same goes for properties. You can also register more than one method/property.

If you are making an [EditorPlugin<class_EditorPlugin>] and want to integrate into the editor's undo history, use [EditorUndoRedoManager<class_EditorUndoRedoManager>] instead.

If you are registering multiple properties/method which depend on one another, be aware that by default undo operation are called in the same order they have been added. Therefore instead of grouping do operation with their undo operations it is better to group do on one side and undo on the other as shown below.


> **TABS**
>

    undo_redo.create_action("Add object")

    # DO
    undo_redo.add_do_method(_create_object)
    undo_redo.add_do_method(_add_object_to_singleton)

    # UNDO
    undo_redo.add_undo_method(_remove_object_from_singleton)
    undo_redo.add_undo_method(_destroy_that_object)

    undo_redo.commit_action()


    _undo_redo.CreateAction("Add object");

    // DO
    _undo_redo.AddDoMethod(new Callable(this, MethodName.CreateObject));
    _undo_redo.AddDoMethod(new Callable(this, MethodName.AddObjectToSingleton));

    // UNDO
    _undo_redo.AddUndoMethod(new Callable(this, MethodName.RemoveObjectFromSingleton));
    _undo_redo.AddUndoMethod(new Callable(this, MethodName.DestroyThatObject));

    _undo_redo.CommitAction();




## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+-----------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`max_steps<class_UndoRedo_property_max_steps>` | ``0`` |
> +-----------------------+-----------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_do_method<class_UndoRedo_method_add_do_method>`\ (\ callable\: :ref:`Callable<class_Callable>`\ )                                                                                                          |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_do_property<class_UndoRedo_method_add_do_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ )                     |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_do_reference<class_UndoRedo_method_add_do_reference>`\ (\ object\: :ref:`Object<class_Object>`\ )                                                                                                          |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_undo_method<class_UndoRedo_method_add_undo_method>`\ (\ callable\: :ref:`Callable<class_Callable>`\ )                                                                                                      |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_undo_property<class_UndoRedo_method_add_undo_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ )                 |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_undo_reference<class_UndoRedo_method_add_undo_reference>`\ (\ object\: :ref:`Object<class_Object>`\ )                                                                                                      |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`clear_history<class_UndoRedo_method_clear_history>`\ (\ increase_version\: :ref:`bool<class_bool>` = true\ )                                                                                                   |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`commit_action<class_UndoRedo_method_commit_action>`\ (\ execute\: :ref:`bool<class_bool>` = true\ )                                                                                                            |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`create_action<class_UndoRedo_method_create_action>`\ (\ name\: :ref:`String<class_String>`, merge_mode\: :ref:`MergeMode<enum_UndoRedo_MergeMode>` = 0, backward_undo_ops\: :ref:`bool<class_bool>` = false\ ) |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`end_force_keep_in_merge_ends<class_UndoRedo_method_end_force_keep_in_merge_ends>`\ (\ )                                                                                                                        |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_action_name<class_UndoRedo_method_get_action_name>`\ (\ id\: :ref:`int<class_int>`\ )                                                                                                                      |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_current_action<class_UndoRedo_method_get_current_action>`\ (\ )                                                                                                                                            |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_current_action_name<class_UndoRedo_method_get_current_action_name>`\ (\ ) |const|                                                                                                                          |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_history_count<class_UndoRedo_method_get_history_count>`\ (\ )                                                                                                                                              |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_version<class_UndoRedo_method_get_version>`\ (\ ) |const|                                                                                                                                                  |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`has_redo<class_UndoRedo_method_has_redo>`\ (\ ) |const|                                                                                                                                                        |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`has_undo<class_UndoRedo_method_has_undo>`\ (\ ) |const|                                                                                                                                                        |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`is_committing_action<class_UndoRedo_method_is_committing_action>`\ (\ ) |const|                                                                                                                                |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`redo<class_UndoRedo_method_redo>`\ (\ )                                                                                                                                                                        |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`start_force_keep_in_merge_ends<class_UndoRedo_method_start_force_keep_in_merge_ends>`\ (\ )                                                                                                                    |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`undo<class_UndoRedo_method_undo>`\ (\ )                                                                                                                                                                        |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**version_changed**\ (\ ) [🔗<class_UndoRedo_signal_version_changed>]

Called when [undo()<class_UndoRedo_method_undo>] or [redo()<class_UndoRedo_method_redo>] was called.


----


## Enumerations



enum **MergeMode**: [🔗<enum_UndoRedo_MergeMode>]



[MergeMode<enum_UndoRedo_MergeMode>] **MERGE_DISABLE** = `0`

Makes "do"/"undo" operations stay in separate actions.



[MergeMode<enum_UndoRedo_MergeMode>] **MERGE_ENDS** = `1`

Merges this action with the previous one if they have the same name. Keeps only the first action's "undo" operations and the last action's "do" operations. Useful for sequential changes to a single value.



[MergeMode<enum_UndoRedo_MergeMode>] **MERGE_ALL** = `2`

Merges this action with the previous one if they have the same name.


----


## Property Descriptions



[int<class_int>] **max_steps** = `0` [🔗<class_UndoRedo_property_max_steps>]


- |void| **set_max_steps**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_steps**\ (\ )

The maximum number of steps that can be stored in the undo/redo history. If the number of stored steps exceeds this limit, older steps are removed from history and can no longer be reached by calling [undo()<class_UndoRedo_method_undo>]. A value of `0` or lower means no limit.


----


## Method Descriptions



|void| **add_do_method**\ (\ callable\: [Callable<class_Callable>]\ ) [🔗<class_UndoRedo_method_add_do_method>]

Register a [Callable<class_Callable>] that will be called when the action is committed.


----



|void| **add_do_property**\ (\ object\: [Object<class_Object>], property\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_UndoRedo_method_add_do_property>]

Register a `property` that would change its value to `value` when the action is committed.


----



|void| **add_do_reference**\ (\ object\: [Object<class_Object>]\ ) [🔗<class_UndoRedo_method_add_do_reference>]

Register a reference to an object that will be erased if the "do" history is deleted. This is useful for objects added by the "do" action and removed by the "undo" action.

When the "do" history is deleted, if the object is a [RefCounted<class_RefCounted>], it will be unreferenced. Otherwise, it will be freed. Do not use for resources.

::

    var node = Node2D.new()
    undo_redo.create_action("Add node")
    undo_redo.add_do_method(add_child.bind(node))
    undo_redo.add_do_reference(node)
    undo_redo.add_undo_method(remove_child.bind(node))
    undo_redo.commit_action()


----



|void| **add_undo_method**\ (\ callable\: [Callable<class_Callable>]\ ) [🔗<class_UndoRedo_method_add_undo_method>]

Register a [Callable<class_Callable>] that will be called when the action is undone.


----



|void| **add_undo_property**\ (\ object\: [Object<class_Object>], property\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_UndoRedo_method_add_undo_property>]

Register a `property` that would change its value to `value` when the action is undone.


----



|void| **add_undo_reference**\ (\ object\: [Object<class_Object>]\ ) [🔗<class_UndoRedo_method_add_undo_reference>]

Register a reference to an object that will be erased if the "undo" history is deleted. This is useful for objects added by the "undo" action and removed by the "do" action.

When the "undo" history is deleted, if the object is a [RefCounted<class_RefCounted>], it will be unreferenced. Otherwise, it will be freed. Do not use for resources.

::

    var node = $Node2D
    undo_redo.create_action("Remove node")
    undo_redo.add_do_method(remove_child.bind(node))
    undo_redo.add_undo_method(add_child.bind(node))
    undo_redo.add_undo_reference(node)
    undo_redo.commit_action()


----



|void| **clear_history**\ (\ increase_version\: [bool<class_bool>] = true\ ) [🔗<class_UndoRedo_method_clear_history>]

Clear the undo/redo history and associated references.

Passing `false` to `increase_version` will prevent the version number from increasing when the history is cleared.


----



|void| **commit_action**\ (\ execute\: [bool<class_bool>] = true\ ) [🔗<class_UndoRedo_method_commit_action>]

Commit the action. If `execute` is `true` (which it is by default), all "do" methods/properties are called/set when this function is called.


----



|void| **create_action**\ (\ name\: [String<class_String>], merge_mode\: [MergeMode<enum_UndoRedo_MergeMode>] = 0, backward_undo_ops\: [bool<class_bool>] = false\ ) [🔗<class_UndoRedo_method_create_action>]

Create a new action. After this is called, do all your calls to [add_do_method()<class_UndoRedo_method_add_do_method>], [add_undo_method()<class_UndoRedo_method_add_undo_method>], [add_do_property()<class_UndoRedo_method_add_do_property>], and [add_undo_property()<class_UndoRedo_method_add_undo_property>], then commit the action with [commit_action()<class_UndoRedo_method_commit_action>].

The way actions are merged is dictated by `merge_mode`.

The way undo operation are ordered in actions is dictated by `backward_undo_ops`. When `backward_undo_ops` is `false` undo option are ordered in the same order they were added. Which means the first operation to be added will be the first to be undone.


----



|void| **end_force_keep_in_merge_ends**\ (\ ) [🔗<class_UndoRedo_method_end_force_keep_in_merge_ends>]

Stops marking operations as to be processed even if the action gets merged with another in the [MERGE_ENDS<class_UndoRedo_constant_MERGE_ENDS>] mode. See [start_force_keep_in_merge_ends()<class_UndoRedo_method_start_force_keep_in_merge_ends>].


----



[String<class_String>] **get_action_name**\ (\ id\: [int<class_int>]\ ) [🔗<class_UndoRedo_method_get_action_name>]

Gets the action name from its index.


----



[int<class_int>] **get_current_action**\ (\ ) [🔗<class_UndoRedo_method_get_current_action>]

Gets the index of the current action.


----



[String<class_String>] **get_current_action_name**\ (\ ) |const| [🔗<class_UndoRedo_method_get_current_action_name>]

Gets the name of the current action, equivalent to `get_action_name(get_current_action())`.


----



[int<class_int>] **get_history_count**\ (\ ) [🔗<class_UndoRedo_method_get_history_count>]

Returns how many elements are in the history.


----



[int<class_int>] **get_version**\ (\ ) |const| [🔗<class_UndoRedo_method_get_version>]

Gets the version. Every time a new action is committed, the **UndoRedo**'s version number is increased automatically.

This is useful mostly to check if something changed from a saved version.


----



[bool<class_bool>] **has_redo**\ (\ ) |const| [🔗<class_UndoRedo_method_has_redo>]

Returns `true` if a "redo" action is available.


----



[bool<class_bool>] **has_undo**\ (\ ) |const| [🔗<class_UndoRedo_method_has_undo>]

Returns `true` if an "undo" action is available.


----



[bool<class_bool>] **is_committing_action**\ (\ ) |const| [🔗<class_UndoRedo_method_is_committing_action>]

Returns `true` if the **UndoRedo** is currently committing the action, i.e. running its "do" method or property change (see [commit_action()<class_UndoRedo_method_commit_action>]).


----



[bool<class_bool>] **redo**\ (\ ) [🔗<class_UndoRedo_method_redo>]

Redo the last action.


----



|void| **start_force_keep_in_merge_ends**\ (\ ) [🔗<class_UndoRedo_method_start_force_keep_in_merge_ends>]

Marks the next "do" and "undo" operations to be processed even if the action gets merged with another in the [MERGE_ENDS<class_UndoRedo_constant_MERGE_ENDS>] mode. Return to normal operation using [end_force_keep_in_merge_ends()<class_UndoRedo_method_end_force_keep_in_merge_ends>].


----



[bool<class_bool>] **undo**\ (\ ) [🔗<class_UndoRedo_method_undo>]

Undo the last action.

