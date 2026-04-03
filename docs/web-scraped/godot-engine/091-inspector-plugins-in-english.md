# Inspector plugins in English

# Inspector plugins

The inspector dock allows you to create custom widgets to edit properties
through plugins. This can be beneficial when working with custom datatypes and
resources, although you can use the feature to change the inspector widgets for
built-in types. You can design custom controls for specific properties, entire
objects, and even separate controls associated with particular datatypes.
This guide explains how to use theEditorInspectorPluginandEditorPropertyclasses to create a custom interface for integers,
replacing the default behavior with a button that generates random values
between 0 and 99.
The default behavior on the left and the end result on the right.

## Setting up your plugin

Create a new empty plugin to get started.
See also
SeeMaking pluginsguide to set up your new plugin.
Let's assume you've called your plugin foldermy_inspector_plugin. If so,
you should end up with a newaddons/my_inspector_pluginfolder that contains
two files:plugin.cfgandplugin.gd.
As before,plugin.gdis a script extendingEditorPluginand you
need to introduce new code for its_enter_treeand_exit_treemethods.
To set up your inspector plugin, you must load its script, then create and add
the instance by callingadd_inspector_plugin(). If the plugin is disabled,
you should remove the instance you have added by callingremove_inspector_plugin().
Note
Here, you are loading a script and not a packed scene. Therefore you
should usenew()instead ofinstantiate().

```
# plugin.gd
@tool
extends EditorPlugin

var plugin

func _enter_tree():
    plugin = preload("res://addons/my_inspector_plugin/my_inspector_plugin.gd").new()
    add_inspector_plugin(plugin)

func _exit_tree():
    remove_inspector_plugin(plugin)
```

```
// Plugin.cs
#if TOOLS
using Godot;

[Tool]
public partial class Plugin : EditorPlugin
{
    private MyInspectorPlugin _plugin;

    public override void _EnterTree()
    {
        _plugin = new MyInspectorPlugin();
        AddInspectorPlugin(_plugin);
    }

    public override void _ExitTree()
    {
        RemoveInspectorPlugin(_plugin);
    }
}
#endif
```

## Interacting with the inspector

To interact with the inspector dock, yourmy_inspector_plugin.gdscript must
extend theEditorInspectorPluginclass. This class provides several
virtual methods that affect how the inspector handles properties.
To have any effect at all, the script must implement the_can_handle()method. This function is called for each editedObjectand must
returntrueif this plugin should handle the object or its properties.
Note
This includes anyResourceattached to the object.
You can implement four other methods to add controls to the inspector at
specific positions. The_parse_begin()and_parse_end()methods are called
only once at the beginning and the end of parsing for each object, respectively.
They can add controls at the top or bottom of the inspector layout by callingadd_custom_control().
As the editor parses the object, it calls the_parse_category()and_parse_property()methods. There, in addition toadd_custom_control(),
you can call bothadd_property_editor()andadd_property_editor_for_multiple_properties(). Use these last two methods to
specifically addEditorProperty-based controls.

```
# my_inspector_plugin.gd
extends EditorInspectorPlugin

var RandomIntEditor = preload("res://addons/my_inspector_plugin/random_int_editor.gd")

func _can_handle(object):
    # We support all objects in this example.
    return true

func _parse_property(object, type, name, hint_type, hint_string, usage_flags, wide):
    # We handle properties of type integer.
    if type == TYPE_INT:
        # Create an instance of the custom property editor and register
        # it to a specific property path.
        add_property_editor(name, RandomIntEditor.new())
        # Inform the editor to remove the default property editor for
        # this property type.
        return true
    else:
        return false
```

```
// MyInspectorPlugin.cs
#if TOOLS
using Godot;

public partial class MyInspectorPlugin : EditorInspectorPlugin
{
    public override bool _CanHandle(GodotObject @object)
    {
        // We support all objects in this example.
        return true;
    }

    public override bool _ParseProperty(GodotObject @object, Variant.Type type,
        string name, PropertyHint hintType, string hintString,
        PropertyUsageFlags usageFlags, bool wide)
    {
        // We handle properties of type integer.
        if (type == Variant.Type.Int)
        {
            // Create an instance of the custom property editor and register
            // it to a specific property path.
            AddPropertyEditor(name, new RandomIntEditor());
            // Inform the editor to remove the default property editor for
            // this property type.
            return true;
        }

        return false;
    }
}
#endif
```

## Adding an interface to edit properties

TheEditorPropertyclass is a special type ofControlthat can interact with the inspector dock's edited objects. It doesn't display
anything but can house any other control nodes, including complex scenes.
There are three essential parts to the script extendingEditorProperty:

- You must define the_init()method to set up the control nodes'
structure.
You must define the_init()method to set up the control nodes'
structure.
- You should implement the_update_property()to handle changes to the data
from the outside.
You should implement the_update_property()to handle changes to the data
from the outside.
- A signal must be emitted at some point to inform the inspector that the
control has changed the property usingemit_changed.
A signal must be emitted at some point to inform the inspector that the
control has changed the property usingemit_changed.
You can display your custom widget in two ways. Use just the defaultadd_child()method to display it to the right of the property name, and useadd_child()followed byset_bottom_editor()to position it below the name.

```
# random_int_editor.gd
extends EditorProperty

# The main control for editing the property.
var property_control = Button.new()
# An internal value of the property.
var current_value = 0
# A guard against internal changes when the property is updated.
var updating = false

func _init():
    # Add the control as a direct child of EditorProperty node.
    add_child(property_control)
    # Make sure the control is able to retain the focus.
    add_focusable(property_control)
    # Setup the initial state and connect to the signal to track changes.
    refresh_control_text()
    property_control.pressed.connect(_on_button_pressed)

func _on_button_pressed():
    # Ignore the signal if the property is currently being updated.
    if (updating):
        return

    # Generate a new random integer between 0 and 99.
    current_value = randi() % 100
    refresh_control_text()
    emit_changed(get_edited_property(), current_value)

func _update_property():
    # Read the current value from the property.
    var new_value = get_edited_object()[get_edited_property()]
    if (new_value == current_value):
        return

    # Update the control with the new value.
    updating = true
    current_value = new_value
    refresh_control_text()
    updating = false

func refresh_control_text():
    property_control.text = "Value: " + str(current_value)
```

```
// RandomIntEditor.cs
#if TOOLS
using Godot;

public partial class RandomIntEditor : EditorProperty
{
    // The main control for editing the property.
    private Button _propertyControl = new Button();
    // An internal value of the property.
    private int _currentValue = 0;
    // A guard against internal changes when the property is updated.
    private bool _updating = false;

    public RandomIntEditor()
    {
        // Add the control as a direct child of EditorProperty node.
        AddChild(_propertyControl);
        // Make sure the control is able to retain the focus.
        AddFocusable(_propertyControl);
        // Setup the initial state and connect to the signal to track changes.
        RefreshControlText();
        _propertyControl.Pressed += OnButtonPressed;
    }

    private void OnButtonPressed()
    {
        // Ignore the signal if the property is currently being updated.
        if (_updating)
        {
            return;
        }

        // Generate a new random integer between 0 and 99.
        _currentValue = (int)GD.Randi() % 100;
        RefreshControlText();
        EmitChanged(GetEditedProperty(), _currentValue);
    }

    public override void _UpdateProperty()
    {
        // Read the current value from the property.
        var newValue = (int)GetEditedObject().Get(GetEditedProperty());
        if (newValue == _currentValue)
        {
            return;
        }

        // Update the control with the new value.
        _updating = true;
        _currentValue = newValue;
        RefreshControlText();
        _updating = false;
    }

    private void RefreshControlText()
    {
        _propertyControl.Text = $"Value: {_currentValue}";
    }
}
#endif
```

Using the example code above you should be able to make a custom widget that
replaces the defaultSpinBoxcontrol for integers with aButtonthat generates random values.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
