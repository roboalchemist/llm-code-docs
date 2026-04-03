# EditorResourcePicker in English

# EditorResourcePicker

Inherits:HBoxContainer<BoxContainer<Container<Control<CanvasItem<Node<Object
Inherited By:EditorScriptPicker
Godot editor's control for selectingResourcetype properties.

## Description

ThisControlnode is used in the editor's Inspector dock to allow editing ofResourcetype properties. It provides options for creating, loading, saving and converting resources. Can be used withEditorInspectorPluginto recreate the same behavior.
Note:ThisControldoes not include any editor for the resource, as editing is controlled by the Inspector dock itself or sub-Inspectors.

## Properties

| String | base_type | "" |
|---|---|---|
| bool | editable | true |
| Resource | edited_resource |  |
| bool | toggle_mode | false |

String
base_type
bool
editable
true
Resource
edited_resource
bool
toggle_mode
false

## Methods

| bool | _handle_menu_selected(id:int)virtual |
|---|---|
| void | _set_create_options(menu_node:Object)virtual |
| PackedStringArray | get_allowed_types()const |
| void | set_toggle_pressed(pressed:bool) |

bool
_handle_menu_selected(id:int)virtual
void
_set_create_options(menu_node:Object)virtual
PackedStringArray
get_allowed_types()const
void
set_toggle_pressed(pressed:bool)

## Signals

resource_changed(resource:Resource)🔗
Emitted when the value of the edited resource was changed.
resource_selected(resource:Resource, inspect:bool)🔗
Emitted when the resource value was set and user clicked to edit it. Wheninspectistrue, the signal was caused by the context menu "Edit" or "Inspect" option.

## Property Descriptions

Stringbase_type=""🔗

- voidset_base_type(value:String)
voidset_base_type(value:String)
- Stringget_base_type()
Stringget_base_type()
The base type of allowed resource types. Can be a comma-separated list of several options.
booleditable=true🔗
- voidset_editable(value:bool)
voidset_editable(value:bool)
- boolis_editable()
boolis_editable()
Iftrue, the value can be selected and edited.
Resourceedited_resource🔗
- voidset_edited_resource(value:Resource)
voidset_edited_resource(value:Resource)
- Resourceget_edited_resource()
Resourceget_edited_resource()
The edited resource value.
booltoggle_mode=false🔗
- voidset_toggle_mode(value:bool)
voidset_toggle_mode(value:bool)
- boolis_toggle_mode()
boolis_toggle_mode()
Iftrue, the main button with the resource preview works in the toggle mode. Useset_toggle_pressed()to manually set the state.

## Method Descriptions

bool_handle_menu_selected(id:int)virtual🔗
This virtual method can be implemented to handle context menu items not handled by default. See_set_create_options().
void_set_create_options(menu_node:Object)virtual🔗
This virtual method is called when updating the context menu ofEditorResourcePicker. Implement this method to override the "New ..." items with your own options.menu_nodeis a reference to thePopupMenunode.
Note:Implement_handle_menu_selected()to handle these custom items.
PackedStringArrayget_allowed_types()const🔗
Returns a list of all allowed types and subtypes corresponding to thebase_type. If thebase_typeis empty, an empty list is returned.
voidset_toggle_pressed(pressed:bool)🔗
Sets the toggle mode state for the main button. Works only iftoggle_modeis set totrue.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
