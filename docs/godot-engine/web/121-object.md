# Object

# Object

Inherited By:AudioServer,CameraServer,ClassDB,DisplayServer,EditorFileSystemDirectory,EditorInterface,EditorPaths,EditorSelection,EditorUndoRedoManager,EditorVCSInterface,Engine,EngineDebugger,FramebufferCacheRD,GDExtensionManager,Geometry2D,Geometry3D,GodotInstance,Input,InputMap,IP,JavaClassWrapper,JavaScriptBridge,JNISingleton,JSONRPC,MainLoop,Marshalls,MovieWriter,NativeMenu,NavigationMeshGenerator,NavigationServer2D,NavigationServer2DManager,NavigationServer3D,NavigationServer3DManager,Node,OpenXRExtensionWrapper,OpenXRInteractionProfileMetadata,OS,Performance,PhysicsDirectBodyState2D,PhysicsDirectBodyState3D,PhysicsDirectSpaceState2D,PhysicsDirectSpaceState3D,PhysicsServer2D,PhysicsServer2DManager,PhysicsServer3D,PhysicsServer3DManager,PhysicsServer3DRenderingServerHandler,ProjectSettings,RefCounted,RenderData,RenderingDevice,RenderingServer,RenderSceneData,ResourceLoader,ResourceSaver,ResourceUID,ScriptLanguage,ShaderIncludeDB,TextServerManager,ThemeDB,TileData,Time,TranslationServer,TreeItem,UndoRedo,UniformSetCacheRD,WorkerThreadPool,XRServer,XRVRS
Base class for all other classes in the engine.

## Description

An advancedVarianttype. All classes in the engine inherit from Object. Each class may define new properties, methods or signals, which are available to all inheriting classes. For example, aSprite2Dinstance is able to callNode.add_child()because it inherits fromNode.
You can create new instances, usingObject.new()in GDScript, ornewGodotObjectin C#.
To delete an Object instance, callfree(). This is necessary for most classes inheriting Object, because they do not manage memory on their own, and will otherwise cause memory leaks when no longer in use. There are a few classes that perform memory management. For example,RefCounted(and by extensionResource) deletes itself when no longer referenced, andNodedeletes its children when freed.
Objects can have aScriptattached to them. Once theScriptis instantiated, it effectively acts as an extension to the base class, allowing it to define and inherit new properties, methods and signals.
Inside aScript,_get_property_list()may be overridden to customize properties in several ways. This allows them to be available to the editor, display as lists of options, sub-divide into groups, save on disk, etc. Scripting languages offer easier ways to customize properties, such as with the@GDScript.@exportannotation.
Godot is very dynamic. An object's script, and therefore its properties, methods and signals, can be changed at run-time. Because of this, there can be occasions where, for example, a property required by a method may not exist. To prevent run-time errors, see methods such asset(),get(),call(),has_method(),has_signal(), etc. Note that these methods aremuchslower than direct references.
In GDScript, you can also check if a given property, method, or signal name exists in an object with theinoperator:

```
var node = Node.new()
print("name" in node)         # Prints true
print("get_parent" in node)   # Prints true
print("tree_entered" in node) # Prints true
print("unknown" in node)      # Prints false
```

Notifications areintconstants commonly sent and received by objects. For example, on every rendered frame, theSceneTreenotifies nodes inside the tree with aNode.NOTIFICATION_PROCESS. The nodes receive it and may callNode._process()to update. To make use of notifications, seenotification()and_notification().
Lastly, every object can also contain metadata (data about data).set_meta()can be useful to store information that the object itself does not depend on. To keep your code clean, making excessive use of metadata is discouraged.
Note:Unlike references to aRefCounted, references to an object stored in a variable can become invalid without being set tonull. To check if an object has been deleted, donotcompare it againstnull. Instead, use@GlobalScope.is_instance_valid(). It's also recommended to inherit fromRefCountedfor classes storing data instead ofObject.
Note:Thescriptis not exposed like most properties. To set or get an object'sScriptin code, useset_script()andget_script(), respectively.
Note:In a boolean context, anObjectwill evaluate tofalseif it is equal tonullor it has been freed. Otherwise, anObjectwill always evaluate totrue. See also@GlobalScope.is_instance_valid().

## Tutorials

- Object class introduction
Object class introduction
- When and how to avoid using nodes for everything
When and how to avoid using nodes for everything
- Object notifications
Object notifications

## Methods

| Variant | _get(property:StringName)virtual |
|---|---|
| Array[Dictionary] | _get_property_list()virtual |
| void | _init()virtual |
| Variant | _iter_get(iter:Variant)virtual |
| bool | _iter_init(iter:Array)virtual |
| bool | _iter_next(iter:Array)virtual |
| void | _notification(what:int)virtual |
| bool | _property_can_revert(property:StringName)virtual |
| Variant | _property_get_revert(property:StringName)virtual |
| bool | _set(property:StringName, value:Variant)virtual |
| String | _to_string()virtual |
| void | _validate_property(property:Dictionary)virtual |
| void | add_user_signal(signal:String, arguments:Array= []) |
| Variant | call(method:StringName, ...)vararg |
| Variant | call_deferred(method:StringName, ...)vararg |
| Variant | callv(method:StringName, arg_array:Array) |
| bool | can_translate_messages()const |
| void | cancel_free() |
| Error | connect(signal:StringName, callable:Callable, flags:int= 0) |
| void | disconnect(signal:StringName, callable:Callable) |
| Error | emit_signal(signal:StringName, ...)vararg |
| void | free() |
| Variant | get(property:StringName)const |
| String | get_class()const |
| Array[Dictionary] | get_incoming_connections()const |
| Variant | get_indexed(property_path:NodePath)const |
| int | get_instance_id()const |
| Variant | get_meta(name:StringName, default:Variant= null)const |
| Array[StringName] | get_meta_list()const |
| int | get_method_argument_count(method:StringName)const |
| Array[Dictionary] | get_method_list()const |
| Array[Dictionary] | get_property_list()const |
| Variant | get_script()const |
| Array[Dictionary] | get_signal_connection_list(signal:StringName)const |
| Array[Dictionary] | get_signal_list()const |
| StringName | get_translation_domain()const |
| bool | has_connections(signal:StringName)const |
| bool | has_meta(name:StringName)const |
| bool | has_method(method:StringName)const |
| bool | has_signal(signal:StringName)const |
| bool | has_user_signal(signal:StringName)const |
| bool | is_blocking_signals()const |
| bool | is_class(class:String)const |
| bool | is_connected(signal:StringName, callable:Callable)const |
| bool | is_queued_for_deletion()const |
| void | notification(what:int, reversed:bool= false) |
| void | notify_property_list_changed() |
| bool | property_can_revert(property:StringName)const |
| Variant | property_get_revert(property:StringName)const |
| void | remove_meta(name:StringName) |
| void | remove_user_signal(signal:StringName) |
| void | set(property:StringName, value:Variant) |
| void | set_block_signals(enable:bool) |
| void | set_deferred(property:StringName, value:Variant) |
| void | set_indexed(property_path:NodePath, value:Variant) |
| void | set_message_translation(enable:bool) |
| void | set_meta(name:StringName, value:Variant) |
| void | set_script(script:Variant) |
| void | set_translation_domain(domain:StringName) |
| String | to_string() |
| String | tr(message:StringName, context:StringName= &"")const |
| String | tr_n(message:StringName, plural_message:StringName, n:int, context:StringName= &"")const |

Variant
_get(property:StringName)virtual
Array[Dictionary]
_get_property_list()virtual
void
_init()virtual
Variant
_iter_get(iter:Variant)virtual
bool
_iter_init(iter:Array)virtual
bool
_iter_next(iter:Array)virtual
void
_notification(what:int)virtual
bool
_property_can_revert(property:StringName)virtual
Variant
_property_get_revert(property:StringName)virtual
bool
_set(property:StringName, value:Variant)virtual
String
_to_string()virtual
void
_validate_property(property:Dictionary)virtual
void
add_user_signal(signal:String, arguments:Array= [])
Variant
call(method:StringName, ...)vararg
Variant
call_deferred(method:StringName, ...)vararg
Variant
callv(method:StringName, arg_array:Array)
bool
can_translate_messages()const
void
cancel_free()
Error
connect(signal:StringName, callable:Callable, flags:int= 0)
void
disconnect(signal:StringName, callable:Callable)
Error
emit_signal(signal:StringName, ...)vararg
void
free()
Variant
get(property:StringName)const
String
get_class()const
Array[Dictionary]
get_incoming_connections()const
Variant
get_indexed(property_path:NodePath)const
get_instance_id()const
Variant
get_meta(name:StringName, default:Variant= null)const
Array[StringName]
get_meta_list()const
get_method_argument_count(method:StringName)const
Array[Dictionary]
get_method_list()const
Array[Dictionary]
get_property_list()const
Variant
get_script()const
Array[Dictionary]
get_signal_connection_list(signal:StringName)const
Array[Dictionary]
get_signal_list()const
StringName
get_translation_domain()const
bool
has_connections(signal:StringName)const
bool
has_meta(name:StringName)const
bool
has_method(method:StringName)const
bool
has_signal(signal:StringName)const
bool
has_user_signal(signal:StringName)const
bool
is_blocking_signals()const
bool
is_class(class:String)const
bool
is_connected(signal:StringName, callable:Callable)const
bool
is_queued_for_deletion()const
void
notification(what:int, reversed:bool= false)
void
notify_property_list_changed()
bool
property_can_revert(property:StringName)const
Variant
property_get_revert(property:StringName)const
void
remove_meta(name:StringName)
void
remove_user_signal(signal:StringName)
void
set(property:StringName, value:Variant)
void
set_block_signals(enable:bool)
void
set_deferred(property:StringName, value:Variant)
void
set_indexed(property_path:NodePath, value:Variant)
void
set_message_translation(enable:bool)
void
set_meta(name:StringName, value:Variant)
void
set_script(script:Variant)
void
set_translation_domain(domain:StringName)
String
to_string()
String
tr(message:StringName, context:StringName= &"")const
String
tr_n(message:StringName, plural_message:StringName, n:int, context:StringName= &"")const

## Signals

property_list_changed()🔗
Emitted whennotify_property_list_changed()is called.
script_changed()🔗
Emitted when the object's script is changed.
Note:When this signal is emitted, the new script is not initialized yet. If you need to access the new script, defer connections to this signal withCONNECT_DEFERRED.

## Enumerations

enumConnectFlags:🔗
ConnectFlagsCONNECT_DEFERRED=1
Deferred connections trigger theirCallables on idle time (at the end of the frame), rather than instantly.
ConnectFlagsCONNECT_PERSIST=2
Persisting connections are stored when the object is serialized (such as when usingPackedScene.pack()). In the editor, connections created through the Signals dock are always persisting.
Note:Connections to lambda functions (that is, when the function code is embedded in theconnect()call) cannot be made persistent.
ConnectFlagsCONNECT_ONE_SHOT=4
One-shot connections disconnect themselves after emission.
ConnectFlagsCONNECT_REFERENCE_COUNTED=8
Reference-counted connections can be assigned to the sameCallablemultiple times. Each disconnection decreases the internal counter. The signal fully disconnects only when the counter reaches 0.
ConnectFlagsCONNECT_APPEND_SOURCE_OBJECT=16
On signal emission, the source object is automatically appended after the original arguments of the signal, regardless of the connectedCallable's unbinds which affect only the original arguments of the signal (seeCallable.unbind(),Callable.get_unbound_arguments_count()).

```
extends Object

signal test_signal

func test():
    print(self) # Prints e.g. <Object#35332818393>
    test_signal.connect(prints.unbind(1), CONNECT_APPEND_SOURCE_OBJECT)
    test_signal.emit("emit_arg_1", "emit_arg_2") # Prints emit_arg_1 <Object#35332818393>
```

## Constants

NOTIFICATION_POSTINITIALIZE=0🔗
Notification received when the object is initialized, before its script is attached. Used internally.
NOTIFICATION_PREDELETE=1🔗
Notification received when the object is about to be deleted. Can be used like destructors in object-oriented programming languages.
This notification is sent in reversed order.
NOTIFICATION_EXTENSION_RELOADED=2🔗
Notification received when the object finishes hot reloading. This notification is only sent for extensions classes and derived.

## Method Descriptions

Variant_get(property:StringName)virtual🔗
Override this method to customize the behavior ofget(). Should return the givenproperty's value, ornullif thepropertyshould be handled normally.
Combined with_set()and_get_property_list(), this method allows defining custom properties, which is particularly useful for editor plugins.
Note:This method is not called when getting built-in properties of an object, including properties defined with@GDScript.@export.

```
func _get(property):
    if property == "fake_property":
        print("Getting my property!")
        return 4

func _get_property_list():
    return [
        { "name": "fake_property", "type": TYPE_INT }
    ]
```

```
public override Variant _Get(StringName property)
{
    if (property == "FakeProperty")
    {
        GD.Print("Getting my property!");
        return 4;
    }
    return default;
}

public override Godot.Collections.Array<Godot.Collections.Dictionary> _GetPropertyList()
{
    return
    [
        new Godot.Collections.Dictionary()
        {
            { "name", "FakeProperty" },
            { "type", (int)Variant.Type.Int },
        },
    ];
}
```

Note:Unlike other virtual methods, this method is called automatically for every script that overrides it. This means that the base implementation should not be called viasuperin GDScript or its equivalents in other languages. The bottom-most sub-class will be called first, with subsequent calls ascending the class hierarchy. The call chain will stop on the first class that returns a non-nullvalue.
Array[Dictionary]_get_property_list()virtual🔗
Override this method to provide a custom list of additional properties to handle by the engine.
Should return a property list, as anArrayof dictionaries. The result is added to the array ofget_property_list(), and should be formatted in the same way. EachDictionarymust at least contain thenameandtypeentries.
You can use_property_can_revert()and_property_get_revert()to customize the default values of the properties added by this method.
The example below displays a list of numbers shown as words going fromZEROtoFIVE, withnumber_countcontrolling the size of the list:

```
@tool
extends Node

@export var number_count = 3:
    set(nc):
        number_count = nc
        numbers.resize(number_count)
        notify_property_list_changed()

var numbers = PackedInt32Array([0, 0, 0])

func _get_property_list():
    var properties = []

    for i in range(number_count):
        properties.append({
            "name": "number_%d" % i,
            "type": TYPE_INT,
            "hint": PROPERTY_HINT_ENUM,
            "hint_string": "ZERO,ONE,TWO,THREE,FOUR,FIVE",
        })

    return properties

func _get(property):
    if property.begins_with("number_"):
        var index = property.get_slice("_", 1).to_int()
        return numbers[index]

func _set(property, value):
    if property.begins_with("number_"):
        var index = property.get_slice("_", 1).to_int()
        numbers[index] = value
        return true
    return false
```

```
[Tool]
public partial class MyNode : Node
{
    private int _numberCount;

    [Export]
    public int NumberCount
    {
        get => _numberCount;
        set
        {
            _numberCount = value;
            _numbers.Resize(_numberCount);
            NotifyPropertyListChanged();
        }
    }

    private Godot.Collections.Array<int> _numbers = [];

    public override Godot.Collections.Array<Godot.Collections.Dictionary> _GetPropertyList()
    {
        Godot.Collections.Array<Godot.Collections.Dictionary> properties = [];

        for (int i = 0; i < _numberCount; i++)
        {
            properties.Add(new Godot.Collections.Dictionary()
            {
                { "name", $"number_{i}" },
                { "type", (int)Variant.Type.Int },
                { "hint", (int)PropertyHint.Enum },
                { "hint_string", "Zero,One,Two,Three,Four,Five" },
            });
        }

        return properties;
    }

    public override Variant _Get(StringName property)
    {
        string propertyName = property.ToString();
        if (propertyName.StartsWith("number_"))
        {
            int index = int.Parse(propertyName.Substring("number_".Length));
            return _numbers[index];
        }
        return default;
    }

    public override bool _Set(StringName property, Variant value)
    {
        string propertyName = property.ToString();
        if (propertyName.StartsWith("number_"))
        {
            int index = int.Parse(propertyName.Substring("number_".Length));
            _numbers[index] = value.As<int>();
            return true;
        }
        return false;
    }
}
```

Note:This method is intended for advanced purposes. For most common use cases, the scripting languages offer easier ways to handle properties. See@GDScript.@export,@GDScript.@export_enum,@GDScript.@export_group, etc. If you want to customize exported properties, use_validate_property().
Note:If the object's script is not@GDScript.@tool, this method will not be called in the editor.
Note:Unlike other virtual methods, this method is called automatically for every script that overrides it. This means that the base implementation should not be called viasuperin GDScript or its equivalents in other languages. The bottom-most sub-class will be called first, with subsequent calls ascending the class hierarchy.
void_init()virtual🔗
Called when the object's script is instantiated, oftentimes after the object is initialized in memory (throughObject.new()in GDScript, ornewGodotObjectin C#). It can be also defined to take in parameters. This method is similar to a constructor in most programming languages.
Note:If_init()is defined withrequiredparameters, the Object with script may only be created directly. If any other means (such asPackedScene.instantiate()orNode.duplicate()) are used, the script's initialization will fail.
Variant_iter_get(iter:Variant)virtual🔗
Returns the current iterable value.iterstores the iteration state, but unlike_iter_init()and_iter_next()the state is supposed to be read-only, so there is noArraywrapper.
Tip:In GDScript, you can use a subtype ofVariantas the return type for_iter_get(). The specified type will be used to set the type of the iterator variable inforloops, enhancing type safety.
bool_iter_init(iter:Array)virtual🔗
Initializes the iterator.iterstores the iteration state. Since GDScript does not support passing arguments by reference, a single-element array is used as a wrapper. Returnstrueso long as the iterator has not reached the end.

```
class MyRange:
    var _from
    var _to

    func _init(from, to):
        assert(from <= to)
        _from = from
        _to = to

    func _iter_init(iter):
        iter[0] = _from
        return iter[0] < _to

    func _iter_next(iter):
        iter[0] += 1
        return iter[0] < _to

    func _iter_get(iter):
        return iter

func _ready():
    var my_range = MyRange.new(2, 5)
    for x in my_range:
        print(x) # Prints 2, 3, 4.
```

Note:Alternatively, you can ignoreiterand use the object's state instead, seeonline docsfor an example. Note that in this case you will not be able to reuse the same iterator instance in nested loops. Also, make sure you reset the iterator state in this method if you want to reuse the same instance multiple times.
bool_iter_next(iter:Array)virtual🔗
Moves the iterator to the next iteration.iterstores the iteration state. Since GDScript does not support passing arguments by reference, a single-element array is used as a wrapper. Returnstrueso long as the iterator has not reached the end.
void_notification(what:int)virtual🔗
Called when the object receives a notification, which can be identified inwhatby comparing it with a constant. See alsonotification().

```
func _notification(what):
    if what == NOTIFICATION_PREDELETE:
        print("Goodbye!")
```

```
public override void _Notification(int what)
{
    if (what == NotificationPredelete)
    {
        GD.Print("Goodbye!");
    }
}
```

Note:The baseObjectdefines a few notifications (NOTIFICATION_POSTINITIALIZEandNOTIFICATION_PREDELETE). Inheriting classes such asNodedefine a lot more notifications, which are also received by this method.
Note:Unlike other virtual methods, this method is called automatically for every script that overrides it. This means that the base implementation should not be called viasuperin GDScript or its equivalents in other languages. Call order depends on thereversedargument ofnotification()and varies between different notifications. Most notifications are sent in the forward order (i.e. Object class first, most derived class last).
bool_property_can_revert(property:StringName)virtual🔗
Override this method to customize the givenproperty's revert behavior. Should returntrueif thepropertyhas a custom default value and is revertible in the Inspector dock. Use_property_get_revert()to specify theproperty's default value.
Note:This method must return consistently, regardless of the current value of theproperty.
Note:Unlike other virtual methods, this method is called automatically for every script that overrides it. This means that the base implementation should not be called viasuperin GDScript or its equivalents in other languages. The bottom-most sub-class will be called first, with subsequent calls ascending the class hierarchy. The call chain will stop on the first class that returnstrue.
Variant_property_get_revert(property:StringName)virtual🔗
Override this method to customize the givenproperty's revert behavior. Should return the default value for theproperty. If the default value differs from theproperty's current value, a revert icon is displayed in the Inspector dock.
Note:_property_can_revert()must also be overridden for this method to be called.
Note:Unlike other virtual methods, this method is called automatically for every script that overrides it. This means that the base implementation should not be called viasuperin GDScript or its equivalents in other languages. The bottom-most sub-class will be called first, with subsequent calls ascending the class hierarchy. The call chain will stop on the first class that returns a non-nullvalue.
bool_set(property:StringName, value:Variant)virtual🔗
Override this method to customize the behavior ofset(). Should set thepropertytovalueand returntrue, orfalseif thepropertyshould be handled normally. Theexactway to set thepropertyis up to this method's implementation.
Combined with_get()and_get_property_list(), this method allows defining custom properties, which is particularly useful for editor plugins.
Note:This method is not called when setting built-in properties of an object, including properties defined with@GDScript.@export.

```
var internal_data = {}

func _set(property, value):
    if property == "fake_property":
        # Storing the value in the fake property.
        internal_data["fake_property"] = value
        return true
    return false

func _get_property_list():
    return [
        { "name": "fake_property", "type": TYPE_INT }
    ]
```

```
private Godot.Collections.Dictionary _internalData = new Godot.Collections.Dictionary();

public override bool _Set(StringName property, Variant value)
{
    if (property == "FakeProperty")
    {
        // Storing the value in the fake property.
        _internalData["FakeProperty"] = value;
        return true;
    }

    return false;
}

public override Godot.Collections.Array<Godot.Collections.Dictionary> _GetPropertyList()
{
    return
    [
        new Godot.Collections.Dictionary()
        {
            { "name", "FakeProperty" },
            { "type", (int)Variant.Type.Int },
        },
    ];
}
```

Note:Unlike other virtual methods, this method is called automatically for every script that overrides it. This means that the base implementation should not be called viasuperin GDScript or its equivalents in other languages. The bottom-most sub-class will be called first, with subsequent calls ascending the class hierarchy. The call chain will stop on the first class that returnstrue.
String_to_string()virtual🔗
Override this method to customize the return value ofto_string(), and therefore the object's representation as aString.

```
func _to_string():
    return "Welcome to Godot 4!"

func _init():
    print(self)       # Prints "Welcome to Godot 4!"
    var a = str(self) # a is "Welcome to Godot 4!"
```

void_validate_property(property:Dictionary)virtual🔗
Override this method to customize existing properties. Every property info goes through this method, except properties added with_get_property_list(). The dictionary contents is the same as in_get_property_list().

```
@tool
extends Node

@export var is_number_editable: bool:
    set(value):
        is_number_editable = value
        notify_property_list_changed()
@export var number: int

func _validate_property(property: Dictionary):
    if property.name == "number" and not is_number_editable:
        property.usage |= PROPERTY_USAGE_READ_ONLY
```

```
[Tool]
public partial class MyNode : Node
{
    private bool _isNumberEditable;

    [Export]
    public bool IsNumberEditable
    {
        get => _isNumberEditable;
        set
        {
            _isNumberEditable = value;
            NotifyPropertyListChanged();
        }
    }

    [Export]
    public int Number { get; set; }

    public override void _ValidateProperty(Godot.Collections.Dictionary property)
    {
        if (property["name"].AsStringName() == PropertyName.Number && !IsNumberEditable)
        {
            var usage = property["usage"].As<PropertyUsageFlags>() | PropertyUsageFlags.ReadOnly;
            property["usage"] = (int)usage;
        }
    }
}
```

voidadd_user_signal(signal:String, arguments:Array= [])🔗
Adds a user-defined signal namedsignal. Optional arguments for the signal can be added as anArrayof dictionaries, each defining anameStringand atypeint(seeVariant.Type). See alsohas_user_signal()andremove_user_signal().

```
add_user_signal("hurt", [
    { "name": "damage", "type": TYPE_INT },
    { "name": "source", "type": TYPE_OBJECT }
])
```

```
AddUserSignal("Hurt",
[
    new Godot.Collections.Dictionary()
    {
        { "name", "damage" },
        { "type", (int)Variant.Type.Int },
    },
    new Godot.Collections.Dictionary()
    {
        { "name", "source" },
        { "type", (int)Variant.Type.Object },
    },
]);
```

Variantcall(method:StringName, ...)vararg🔗
Calls themethodon the object and returns the result. This method supports a variable number of arguments, so parameters can be passed as a comma separated list.

```
var node = Node3D.new()
node.call("rotate", Vector3(1.0, 0.0, 0.0), 1.571)
```

```
var node = new Node3D();
node.Call(Node3D.MethodName.Rotate, new Vector3(1f, 0f, 0f), 1.571f);
```

Note:In C#,methodmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theMethodNameclass to avoid allocating a newStringNameon each call.
Variantcall_deferred(method:StringName, ...)vararg🔗
Calls themethodon the object during idle time. Always returnsnull,notthe method's result.
Idle time happens mainly at the end of process and physics frames. In it, deferred calls will be run until there are none left, which means you can defer calls from other deferred calls and they'll still be run in the current idle time cycle. This means you should not call a method deferred from itself (or from a method called by it), as this causes infinite recursion the same way as if you had called the method directly.
This method supports a variable number of arguments, so parameters can be passed as a comma separated list.

```
var node = Node3D.new()
node.call_deferred("rotate", Vector3(1.0, 0.0, 0.0), 1.571)
```

```
var node = new Node3D();
node.CallDeferred(Node3D.MethodName.Rotate, new Vector3(1f, 0f, 0f), 1.571f);
```

For methods that are deferred from the same thread, the order of execution at idle time is identical to the order in whichcall_deferredwas called.
See alsoCallable.call_deferred().
Note:In C#,methodmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theMethodNameclass to avoid allocating a newStringNameon each call.
Note:If you're looking to delay the function call by a frame, refer to theSceneTree.process_frameandSceneTree.physics_framesignals.

```
var node = Node3D.new()
# Make a Callable and bind the arguments to the node's rotate() call.
var callable = node.rotate.bind(Vector3(1.0, 0.0, 0.0), 1.571)
# Connect the callable to the process_frame signal, so it gets called in the next process frame.
# CONNECT_ONE_SHOT makes sure it only gets called once instead of every frame.
get_tree().process_frame.connect(callable, CONNECT_ONE_SHOT)
```

Variantcallv(method:StringName, arg_array:Array)🔗
Calls themethodon the object and returns the result. Unlikecall(), this method expects all parameters to be contained insidearg_array.

```
var node = Node3D.new()
node.callv("rotate", [Vector3(1.0, 0.0, 0.0), 1.571])
```

```
var node = new Node3D();
node.Callv(Node3D.MethodName.Rotate, [new Vector3(1f, 0f, 0f), 1.571f]);
```

Note:In C#,methodmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theMethodNameclass to avoid allocating a newStringNameon each call.
boolcan_translate_messages()const🔗
Returnstrueif the object is allowed to translate messages withtr()andtr_n(). See alsoset_message_translation().
voidcancel_free()🔗
If this method is called duringNOTIFICATION_PREDELETE, this object will reject being freed and will remain allocated. This is mostly an internal function used for error handling to avoid the user from freeing objects when they are not intended to.
Errorconnect(signal:StringName, callable:Callable, flags:int= 0)🔗
Connects asignalby name to acallable. Optionalflagscan be also added to configure the connection's behavior (seeConnectFlagsconstants).
A signal can only be connected once to the sameCallable. If the signal is already connected, this method returns@GlobalScope.ERR_INVALID_PARAMETERand generates an error, unless the signal is connected withCONNECT_REFERENCE_COUNTED. To prevent this, useis_connected()first to check for existing connections.
Note:If thecallable's object is freed, the connection will be lost.
Note:In GDScript, it is generally recommended to connect signals withSignal.connect()instead.
Note:This method, and all other signal-related methods, are thread-safe.
voiddisconnect(signal:StringName, callable:Callable)🔗
Disconnects asignalby name from a givencallable. If the connection does not exist, generates an error. Useis_connected()to make sure that the connection exists.
Erroremit_signal(signal:StringName, ...)vararg🔗
Emits the givensignalby name. The signal must exist, so it should be a built-in signal of this class or one of its inherited classes, or a user-defined signal (seeadd_user_signal()). This method supports a variable number of arguments, so parameters can be passed as a comma separated list.
Returns@GlobalScope.ERR_UNAVAILABLEifsignaldoes not exist or the parameters are invalid.

```
emit_signal("hit", "sword", 100)
emit_signal("game_over")
```

```
EmitSignal(SignalName.Hit, "sword", 100);
EmitSignal(SignalName.GameOver);
```

Note:In C#,signalmust be in snake_case when referring to built-in Godot signals. Prefer using the names exposed in theSignalNameclass to avoid allocating a newStringNameon each call.
voidfree()🔗
Deletes the object from memory. Pre-existing references to the object become invalid, and any attempt to access them will result in a runtime error. Checking the references with@GlobalScope.is_instance_valid()will returnfalse. This is equivalent to thememdeletefunction in GDExtension C++.
Variantget(property:StringName)const🔗
Returns theVariantvalue of the givenproperty. If thepropertydoes not exist, this method returnsnull.

```
var node = Node2D.new()
node.rotation = 1.5
var a = node.get("rotation") # a is 1.5
```

```
var node = new Node2D();
node.Rotation = 1.5f;
var a = node.Get(Node2D.PropertyName.Rotation); // a is 1.5
```

Note:In C#,propertymust be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in thePropertyNameclass to avoid allocating a newStringNameon each call.
Stringget_class()const🔗
Returns the object's built-in class name, as aString. See alsois_class().
Note:This method ignoresclass_namedeclarations. If this object's script has defined aclass_name, the base, built-in class name is returned instead.
Array[Dictionary]get_incoming_connections()const🔗
Returns anArrayof signal connections received by this object. Each connection is represented as aDictionarythat contains three entries:

- signalis a reference to theSignal;
signalis a reference to theSignal;
- callableis a reference to theCallable;
callableis a reference to theCallable;
- flagsis a combination ofConnectFlags.
flagsis a combination ofConnectFlags.
Variantget_indexed(property_path:NodePath)const🔗
Gets the object's property indexed by the givenproperty_path. The path should be aNodePathrelative to the current object and can use the colon character (:) to access nested properties.
Examples:"position:x"or"material:next_pass:blend_mode".

```
var node = Node2D.new()
node.position = Vector2(5, -10)
var a = node.get_indexed("position")   # a is Vector2(5, -10)
var b = node.get_indexed("position:y") # b is -10
```

```
var node = new Node2D();
node.Position = new Vector2(5, -10);
var a = node.GetIndexed("position");   // a is Vector2(5, -10)
var b = node.GetIndexed("position:y"); // b is -10
```

Note:In C#,property_pathmust be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in thePropertyNameclass to avoid allocating a newStringNameon each call.
Note:This method does not support actual paths to nodes in theSceneTree, only sub-property paths. In the context of nodes, useNode.get_node_and_resource()instead.
intget_instance_id()const🔗
Returns the object's unique instance ID. This ID can be saved inEncodedObjectAsID, and can be used to retrieve this object instance with@GlobalScope.instance_from_id().
Note:This ID is only useful during the current session. It won't correspond to a similar object if the ID is sent over a network, or loaded from a file at a later time.
Variantget_meta(name:StringName, default:Variant= null)const🔗
Returns the object's metadata value for the given entryname. If the entry does not exist, returnsdefault. Ifdefaultisnull, an error is also generated.
Note:A metadata's name must be a valid identifier as perStringName.is_valid_identifier()method.
Note:Metadata that has a name starting with an underscore (_) is considered editor-only. Editor-only metadata is not displayed in the Inspector and should not be edited, although it can still be found by this method.
Array[StringName]get_meta_list()const🔗
Returns the object's metadata entry names as anArrayofStringNames.
intget_method_argument_count(method:StringName)const🔗
Returns the number of arguments of the givenmethodby name.
Note:In C#,methodmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theMethodNameclass to avoid allocating a newStringNameon each call.
Array[Dictionary]get_method_list()const🔗
Returns this object's methods and their signatures as anArrayof dictionaries. EachDictionarycontains the following entries:

- nameis the name of the method, as aString;
nameis the name of the method, as aString;
- argsis anArrayof dictionaries representing the arguments;
argsis anArrayof dictionaries representing the arguments;
- default_argsis the default arguments as anArrayof variants;
default_argsis the default arguments as anArrayof variants;
- flagsis a combination ofMethodFlags;
flagsis a combination ofMethodFlags;
- idis the method's internal identifierint;
idis the method's internal identifierint;
- returnis the returned value, as aDictionary;
returnis the returned value, as aDictionary;
Note:The dictionaries ofargsandreturnare formatted identically to the results ofget_property_list(), although not all entries are used.
Array[Dictionary]get_property_list()const🔗
Returns the object's property list as anArrayof dictionaries. EachDictionarycontains the following entries:
- nameis the property's name, as aString;
nameis the property's name, as aString;
- class_nameis an emptyStringName, unless the property is@GlobalScope.TYPE_OBJECTand it inherits from a class;
class_nameis an emptyStringName, unless the property is@GlobalScope.TYPE_OBJECTand it inherits from a class;
- typeis the property's type, as anint(seeVariant.Type);
typeis the property's type, as anint(seeVariant.Type);
- hintishowthe property is meant to be edited (seePropertyHint);
hintishowthe property is meant to be edited (seePropertyHint);
- hint_stringdepends on the hint (seePropertyHint);
hint_stringdepends on the hint (seePropertyHint);
- usageis a combination ofPropertyUsageFlags.
usageis a combination ofPropertyUsageFlags.
Note:In GDScript, all class members are treated as properties. In C# and GDExtension, it may be necessary to explicitly mark class members as Godot properties using decorators or attributes.
Variantget_script()const🔗
Returns the object'sScriptinstance, ornullif no script is attached.
Array[Dictionary]get_signal_connection_list(signal:StringName)const🔗
Returns anArrayof connections for the givensignalname. Each connection is represented as aDictionarythat contains three entries:
- signalis a reference to theSignal;
signalis a reference to theSignal;
- callableis a reference to the connectedCallable;
callableis a reference to the connectedCallable;
- flagsis a combination ofConnectFlags.
flagsis a combination ofConnectFlags.
Array[Dictionary]get_signal_list()const🔗
Returns the list of existing signals as anArrayof dictionaries.
Note:Due to the implementation, eachDictionaryis formatted very similarly to the returned values ofget_method_list().
StringNameget_translation_domain()const🔗
Returns the name of the translation domain used bytr()andtr_n(). See alsoTranslationServer.
boolhas_connections(signal:StringName)const🔗
Returnstrueif any connection exists on the givensignalname.
Note:In C#,signalmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theSignalNameclass to avoid allocating a newStringNameon each call.
boolhas_meta(name:StringName)const🔗
Returnstrueif a metadata entry is found with the givenname. See alsoget_meta(),set_meta()andremove_meta().
Note:A metadata's name must be a valid identifier as perStringName.is_valid_identifier()method.
Note:Metadata that has a name starting with an underscore (_) is considered editor-only. Editor-only metadata is not displayed in the Inspector and should not be edited, although it can still be found by this method.
boolhas_method(method:StringName)const🔗
Returnstrueif the givenmethodname exists in the object.
Note:In C#,methodmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theMethodNameclass to avoid allocating a newStringNameon each call.
boolhas_signal(signal:StringName)const🔗
Returnstrueif the givensignalname exists in the object.
Note:In C#,signalmust be in snake_case when referring to built-in Godot signals. Prefer using the names exposed in theSignalNameclass to avoid allocating a newStringNameon each call.
boolhas_user_signal(signal:StringName)const🔗
Returnstrueif the given user-definedsignalname exists. Only signals added withadd_user_signal()are included. See alsoremove_user_signal().
boolis_blocking_signals()const🔗
Returnstrueif the object is blocking its signals from being emitted. Seeset_block_signals().
boolis_class(class:String)const🔗
Returnstrueif the object inherits from the givenclass. See alsoget_class().

```
var sprite2d = Sprite2D.new()
sprite2d.is_class("Sprite2D") # Returns true
sprite2d.is_class("Node")     # Returns true
sprite2d.is_class("Node3D")   # Returns false
```

```
var sprite2D = new Sprite2D();
sprite2D.IsClass("Sprite2D"); // Returns true
sprite2D.IsClass("Node");     // Returns true
sprite2D.IsClass("Node3D");   // Returns false
```

Note:This method ignoresclass_namedeclarations in the object's script.
boolis_connected(signal:StringName, callable:Callable)const🔗
Returnstrueif a connection exists between the givensignalname andcallable.
Note:In C#,signalmust be in snake_case when referring to built-in Godot signals. Prefer using the names exposed in theSignalNameclass to avoid allocating a newStringNameon each call.
boolis_queued_for_deletion()const🔗
Returnstrueif theNode.queue_free()method was called for the object.
voidnotification(what:int, reversed:bool= false)🔗
Sends the givenwhatnotification to all classes inherited by the object, triggering calls to_notification(), starting from the highest ancestor (theObjectclass) and going down to the object's script.
Ifreversedistrue, the call order is reversed.

```
var player = Node2D.new()
player.set_script(load("res://player.gd"))

player.notification(NOTIFICATION_ENTER_TREE)
# The call order is Object -> Node -> Node2D -> player.gd.

player.notification(NOTIFICATION_ENTER_TREE, true)
# The call order is player.gd -> Node2D -> Node -> Object.
```

```
var player = new Node2D();
player.SetScript(GD.Load("res://player.gd"));

player.Notification(NotificationEnterTree);
// The call order is GodotObject -> Node -> Node2D -> player.gd.

player.Notification(NotificationEnterTree, true);
// The call order is player.gd -> Node2D -> Node -> GodotObject.
```

voidnotify_property_list_changed()🔗
Emits theproperty_list_changedsignal. This is mainly used to refresh the editor, so that the Inspector and editor plugins are properly updated.
boolproperty_can_revert(property:StringName)const🔗
Returnstrueif the givenpropertyhas a custom default value. Useproperty_get_revert()to get theproperty's default value.
Note:This method is used by the Inspector dock to display a revert icon. The object must implement_property_can_revert()to customize the default value. If_property_can_revert()is not implemented, this method returnsfalse.
Variantproperty_get_revert(property:StringName)const🔗
Returns the custom default value of the givenproperty. Useproperty_can_revert()to check if thepropertyhas a custom default value.
Note:This method is used by the Inspector dock to display a revert icon. The object must implement_property_get_revert()to customize the default value. If_property_get_revert()is not implemented, this method returnsnull.
voidremove_meta(name:StringName)🔗
Removes the given entrynamefrom the object's metadata. See alsohas_meta(),get_meta()andset_meta().
Note:A metadata's name must be a valid identifier as perStringName.is_valid_identifier()method.
Note:Metadata that has a name starting with an underscore (_) is considered editor-only. Editor-only metadata is not displayed in the Inspector and should not be edited, although it can still be found by this method.
voidremove_user_signal(signal:StringName)🔗
Removes the given user signalsignalfrom the object. See alsoadd_user_signal()andhas_user_signal().
voidset(property:StringName, value:Variant)🔗
Assignsvalueto the givenproperty. If the property does not exist or the givenvalue's type doesn't match, nothing happens.

```
var node = Node2D.new()
node.set("global_scale", Vector2(8, 2.5))
print(node.global_scale) # Prints (8.0, 2.5)
```

```
var node = new Node2D();
node.Set(Node2D.PropertyName.GlobalScale, new Vector2(8, 2.5f));
GD.Print(node.GlobalScale); // Prints (8, 2.5)
```

Note:In C#,propertymust be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in thePropertyNameclass to avoid allocating a newStringNameon each call.
voidset_block_signals(enable:bool)🔗
If set totrue, the object becomes unable to emit signals. As such,emit_signal()and signal connections will not work, until it is set tofalse.
voidset_deferred(property:StringName, value:Variant)🔗
Assignsvalueto the givenproperty, at the end of the current frame. This is equivalent to callingset()throughcall_deferred().

```
var node = Node2D.new()
add_child(node)

node.rotation = 1.5
node.set_deferred("rotation", 3.0)
print(node.rotation) # Prints 1.5

await get_tree().process_frame
print(node.rotation) # Prints 3.0
```

```
var node = new Node2D();
node.Rotation = 1.5f;
node.SetDeferred(Node2D.PropertyName.Rotation, 3f);
GD.Print(node.Rotation); // Prints 1.5

await ToSignal(GetTree(), SceneTree.SignalName.ProcessFrame);
GD.Print(node.Rotation); // Prints 3.0
```

Note:In C#,propertymust be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in thePropertyNameclass to avoid allocating a newStringNameon each call.
voidset_indexed(property_path:NodePath, value:Variant)🔗
Assigns a newvalueto the property identified by theproperty_path. The path should be aNodePathrelative to this object, and can use the colon character (:) to access nested properties.

```
var node = Node2D.new()
node.set_indexed("position", Vector2(42, 0))
node.set_indexed("position:y", -10)
print(node.position) # Prints (42.0, -10.0)
```

```
var node = new Node2D();
node.SetIndexed("position", new Vector2(42, 0));
node.SetIndexed("position:y", -10);
GD.Print(node.Position); // Prints (42, -10)
```

Note:In C#,property_pathmust be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in thePropertyNameclass to avoid allocating a newStringNameon each call.
voidset_message_translation(enable:bool)🔗
If set totrue, allows the object to translate messages withtr()andtr_n(). Enabled by default. See alsocan_translate_messages().
voidset_meta(name:StringName, value:Variant)🔗
Adds or changes the entrynameinside the object's metadata. The metadatavaluecan be anyVariant, although some types cannot be serialized correctly.
Ifvalueisnull, the entry is removed. This is the equivalent of usingremove_meta(). See alsohas_meta()andget_meta().
Note:A metadata's name must be a valid identifier as perStringName.is_valid_identifier()method.
Note:Metadata that has a name starting with an underscore (_) is considered editor-only. Editor-only metadata is not displayed in the Inspector and should not be edited, although it can still be found by this method.
voidset_script(script:Variant)🔗
Attachesscriptto the object, and instantiates it. As a result, the script's_init()is called. AScriptis used to extend the object's functionality.
If a script already exists, its instance is detached, and its property values and state are lost. Built-in property values are still kept.
voidset_translation_domain(domain:StringName)🔗
Sets the name of the translation domain used bytr()andtr_n(). See alsoTranslationServer.
Stringto_string()🔗
Returns aStringrepresenting the object. Defaults to"<ClassName#RID>". Override_to_string()to customize the string representation of the object.
Stringtr(message:StringName, context:StringName= &"")const🔗
Translates amessage, using the translation catalogs configured in the Project Settings. Furthercontextcan be specified to help with the translation. Note that mostControlnodes automatically translate their strings, so this method is mostly useful for formatted strings or custom drawn text.
Ifcan_translate_messages()isfalse, or no translation is available, this method returns themessagewithout changes. Seeset_message_translation().
For detailed examples, seeInternationalizing games.
Note:This method can't be used without anObjectinstance, as it requires thecan_translate_messages()method. To translate strings in a static context, useTranslationServer.translate().
Stringtr_n(message:StringName, plural_message:StringName, n:int, context:StringName= &"")const🔗
Translates amessageorplural_message, using the translation catalogs configured in the Project Settings. Furthercontextcan be specified to help with the translation.
Ifcan_translate_messages()isfalse, or no translation is available, this method returnsmessageorplural_message, without changes. Seeset_message_translation().
Thenis the number, or amount, of the message's subject. It is used by the translation system to fetch the correct plural form for the current language.
For detailed examples, seeLocalization using gettext.
Note:Negative andfloatnumbers may not properly apply to some countable subjects. It's recommended to handle these cases withtr().
Note:This method can't be used without anObjectinstance, as it requires thecan_translate_messages()method. To translate strings in a static context, useTranslationServer.translate_plural().

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
