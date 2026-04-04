# EditorInspectorPlugin

# EditorInspectorPlugin

Inherits:RefCounted<Object
Plugin for adding custom property editors on the inspector.

## Description

EditorInspectorPluginallows adding custom property editors toEditorInspector.
When an object is edited, the_can_handle()function is called and must returntrueif the object type is supported.
If supported, the function_parse_begin()will be called, allowing to place custom controls at the beginning of the class.
Subsequently, the_parse_category()and_parse_property()are called for every category and property. They offer the ability to add custom controls to the inspector too.
Finally,_parse_end()will be called.
On each of these calls, the "add" functions can be called.
To useEditorInspectorPlugin, register it using theEditorPlugin.add_inspector_plugin()method first.

## Tutorials

- Inspector plugins
Inspector plugins

## Methods

| bool | _can_handle(object:Object)virtualconst |
|---|---|
| void | _parse_begin(object:Object)virtual |
| void | _parse_category(object:Object, category:String)virtual |
| void | _parse_end(object:Object)virtual |
| void | _parse_group(object:Object, group:String)virtual |
| bool | _parse_property(object:Object, type:Variant.Type, name:String, hint_type:PropertyHint, hint_string:String, usage_flags:BitField[PropertyUsageFlags], wide:bool)virtual |
| void | add_custom_control(control:Control) |
| void | add_property_editor(property:String, editor:Control, add_to_end:bool= false, label:String= "") |
| void | add_property_editor_for_multiple_properties(label:String, properties:PackedStringArray, editor:Control) |

bool
_can_handle(object:Object)virtualconst
void
_parse_begin(object:Object)virtual
void
_parse_category(object:Object, category:String)virtual
void
_parse_end(object:Object)virtual
void
_parse_group(object:Object, group:String)virtual
bool
_parse_property(object:Object, type:Variant.Type, name:String, hint_type:PropertyHint, hint_string:String, usage_flags:BitField[PropertyUsageFlags], wide:bool)virtual
void
add_custom_control(control:Control)
void
add_property_editor(property:String, editor:Control, add_to_end:bool= false, label:String= "")
void
add_property_editor_for_multiple_properties(label:String, properties:PackedStringArray, editor:Control)

## Method Descriptions

bool_can_handle(object:Object)virtualconst🔗
Returnstrueif this object can be handled by this plugin.
void_parse_begin(object:Object)virtual🔗
Called to allow adding controls at the beginning of the property list forobject.
void_parse_category(object:Object, category:String)virtual🔗
Called to allow adding controls at the beginning of a category in the property list forobject.
void_parse_end(object:Object)virtual🔗
Called to allow adding controls at the end of the property list forobject.
void_parse_group(object:Object, group:String)virtual🔗
Called to allow adding controls at the beginning of a group or a sub-group in the property list forobject.
bool_parse_property(object:Object, type:Variant.Type, name:String, hint_type:PropertyHint, hint_string:String, usage_flags:BitField[PropertyUsageFlags], wide:bool)virtual🔗
Called to allow adding property-specific editors to the property list forobject. The added editor control must extendEditorProperty. Returningtrueremoves the built-in editor for this property, otherwise allows to insert a custom editor before the built-in one.
voidadd_custom_control(control:Control)🔗
Adds a custom control, which is not necessarily a property editor.
voidadd_property_editor(property:String, editor:Control, add_to_end:bool= false, label:String= "")🔗
Adds a property editor for an individual property. Theeditorcontrol must extendEditorProperty.
There can be multiple property editors for a property. Ifadd_to_endistrue, this newly added editor will be displayed after all the other editors of the property whoseadd_to_endisfalse. For example, the editor uses this parameter to add an "Edit Region" button forSprite2D.region_rectbelow the regularRect2editor.
labelcan be used to choose a custom label for the property editor in the inspector. If left empty, the label is computed from the name of the property instead.
voidadd_property_editor_for_multiple_properties(label:String, properties:PackedStringArray, editor:Control)🔗
Adds an editor that allows modifying multiple properties. Theeditorcontrol must extendEditorProperty.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
