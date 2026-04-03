# @GlobalScope in English

# @GlobalScope
Global scope constants and functions.

## Description
A list of global scope enumerated constants and built-in functions. This is all that resides in the globals, constants regarding error codes, keycodes, property hints, etc.
Singletons are also documented here, since they can be accessed from anywhere.
For the entries that can only be accessed from scripts written in GDScript, see@GDScript.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Tutorials
- Random number generation
Random number generation

## Properties

| AudioServer | AudioServer |
|---|---|
| CameraServer | CameraServer |
| ClassDB | ClassDB |
| DisplayServer | DisplayServer |
| EditorInterface | EditorInterface |
| Engine | Engine |
| EngineDebugger | EngineDebugger |
| GDExtensionManager | GDExtensionManager |
| Geometry2D | Geometry2D |
| Geometry3D | Geometry3D |
| IP | IP |
| Input | Input |
| InputMap | InputMap |
| JavaClassWrapper | JavaClassWrapper |
| JavaScriptBridge | JavaScriptBridge |
| Marshalls | Marshalls |
| NativeMenu | NativeMenu |
| NavigationMeshGenerator | NavigationMeshGenerator |
| NavigationServer2D | NavigationServer2D |
| NavigationServer2DManager | NavigationServer2DManager |
| NavigationServer3D | NavigationServer3D |
| NavigationServer3DManager | NavigationServer3DManager |
| OS | OS |
| Performance | Performance |
| PhysicsServer2D | PhysicsServer2D |
| PhysicsServer2DManager | PhysicsServer2DManager |
| PhysicsServer3D | PhysicsServer3D |
| PhysicsServer3DManager | PhysicsServer3DManager |
| ProjectSettings | ProjectSettings |
| RenderingServer | RenderingServer |
| ResourceLoader | ResourceLoader |
| ResourceSaver | ResourceSaver |
| ResourceUID | ResourceUID |
| TextServerManager | TextServerManager |
| ThemeDB | ThemeDB |
| Time | Time |
| TranslationServer | TranslationServer |
| WorkerThreadPool | WorkerThreadPool |
| XRServer | XRServer |

AudioServer
AudioServer
CameraServer
CameraServer
ClassDB
ClassDB
DisplayServer
DisplayServer
EditorInterface
EditorInterface
Engine
Engine
EngineDebugger
EngineDebugger
GDExtensionManager
GDExtensionManager
Geometry2D
Geometry2D
Geometry3D
Geometry3D
Input
Input
InputMap
InputMap
JavaClassWrapper
JavaClassWrapper
JavaScriptBridge
JavaScriptBridge
Marshalls
Marshalls
NativeMenu
NativeMenu
NavigationMeshGenerator
NavigationMeshGenerator
NavigationServer2D
NavigationServer2D
NavigationServer2DManager
NavigationServer2DManager
NavigationServer3D
NavigationServer3D
NavigationServer3DManager
NavigationServer3DManager
Performance
Performance
PhysicsServer2D
PhysicsServer2D
PhysicsServer2DManager
PhysicsServer2DManager
PhysicsServer3D
PhysicsServer3D
PhysicsServer3DManager
PhysicsServer3DManager
ProjectSettings
ProjectSettings
RenderingServer
RenderingServer
ResourceLoader
ResourceLoader
ResourceSaver
ResourceSaver
ResourceUID
ResourceUID
TextServerManager
TextServerManager
ThemeDB
ThemeDB
Time
Time
TranslationServer
TranslationServer
WorkerThreadPool
WorkerThreadPool
XRServer
XRServer

## Methods

| Variant | abs(x:Variant) |
|---|---|
| float | absf(x:float) |
| int | absi(x:int) |
| float | acos(x:float) |
| float | acosh(x:float) |
| float | angle_difference(from:float, to:float) |
| float | asin(x:float) |
| float | asinh(x:float) |
| float | atan(x:float) |
| float | atan2(y:float, x:float) |
| float | atanh(x:float) |
| float | bezier_derivative(start:float, control_1:float, control_2:float, end:float, t:float) |
| float | bezier_interpolate(start:float, control_1:float, control_2:float, end:float, t:float) |
| Variant | bytes_to_var(bytes:PackedByteArray) |
| Variant | bytes_to_var_with_objects(bytes:PackedByteArray) |
| Variant | ceil(x:Variant) |
| float | ceilf(x:float) |
| int | ceili(x:float) |
| Variant | clamp(value:Variant, min:Variant, max:Variant) |
| float | clampf(value:float, min:float, max:float) |
| int | clampi(value:int, min:int, max:int) |
| float | cos(angle_rad:float) |
| float | cosh(x:float) |
| float | cubic_interpolate(from:float, to:float, pre:float, post:float, weight:float) |
| float | cubic_interpolate_angle(from:float, to:float, pre:float, post:float, weight:float) |
| float | cubic_interpolate_angle_in_time(from:float, to:float, pre:float, post:float, weight:float, to_t:float, pre_t:float, post_t:float) |
| float | cubic_interpolate_in_time(from:float, to:float, pre:float, post:float, weight:float, to_t:float, pre_t:float, post_t:float) |
| float | db_to_linear(db:float) |
| float | deg_to_rad(deg:float) |
| float | ease(x:float, curve:float) |
| String | error_string(error:int) |
| float | exp(x:float) |
| Variant | floor(x:Variant) |
| float | floorf(x:float) |
| int | floori(x:float) |
| float | fmod(x:float, y:float) |
| float | fposmod(x:float, y:float) |
| int | hash(variable:Variant) |
| Object | instance_from_id(instance_id:int) |
| float | inverse_lerp(from:float, to:float, weight:float) |
| bool | is_equal_approx(a:float, b:float) |
| bool | is_finite(x:float) |
| bool | is_inf(x:float) |
| bool | is_instance_id_valid(id:int) |
| bool | is_instance_valid(instance:Variant) |
| bool | is_nan(x:float) |
| bool | is_same(a:Variant, b:Variant) |
| bool | is_zero_approx(x:float) |
| Variant | lerp(from:Variant, to:Variant, weight:Variant) |
| float | lerp_angle(from:float, to:float, weight:float) |
| float | lerpf(from:float, to:float, weight:float) |
| float | linear_to_db(lin:float) |
| float | log(x:float) |
| Variant | max(...)vararg |
| float | maxf(a:float, b:float) |
| int | maxi(a:int, b:int) |
| Variant | min(...)vararg |
| float | minf(a:float, b:float) |
| int | mini(a:int, b:int) |
| float | move_toward(from:float, to:float, delta:float) |
| int | nearest_po2(value:int) |
| float | pingpong(value:float, length:float) |
| int | posmod(x:int, y:int) |
| float | pow(base:float, exp:float) |
| void | print(...)vararg |
| void | print_rich(...)vararg |
| void | print_verbose(...)vararg |
| void | printerr(...)vararg |
| void | printraw(...)vararg |
| void | prints(...)vararg |
| void | printt(...)vararg |
| void | push_error(...)vararg |
| void | push_warning(...)vararg |
| float | rad_to_deg(rad:float) |
| PackedInt64Array | rand_from_seed(seed:int) |
| float | randf() |
| float | randf_range(from:float, to:float) |
| float | randfn(mean:float, deviation:float) |
| int | randi() |
| int | randi_range(from:int, to:int) |
| void | randomize() |
| float | remap(value:float, istart:float, istop:float, ostart:float, ostop:float) |
| int | rid_allocate_id() |
| RID | rid_from_int64(base:int) |
| float | rotate_toward(from:float, to:float, delta:float) |
| Variant | round(x:Variant) |
| float | roundf(x:float) |
| int | roundi(x:float) |
| void | seed(base:int) |
| Variant | sign(x:Variant) |
| float | signf(x:float) |
| int | signi(x:int) |
| float | sin(angle_rad:float) |
| float | sinh(x:float) |
| float | smoothstep(from:float, to:float, x:float) |
| Variant | snapped(x:Variant, step:Variant) |
| float | snappedf(x:float, step:float) |
| int | snappedi(x:float, step:int) |
| float | sqrt(x:float) |
| int | step_decimals(x:float) |
| String | str(...)vararg |
| Variant | str_to_var(string:String) |
| float | tan(angle_rad:float) |
| float | tanh(x:float) |
| Variant | type_convert(variant:Variant, type:int) |
| String | type_string(type:int) |
| int | typeof(variable:Variant) |
| PackedByteArray | var_to_bytes(variable:Variant) |
| PackedByteArray | var_to_bytes_with_objects(variable:Variant) |
| String | var_to_str(variable:Variant) |
| Variant | weakref(obj:Variant) |
| Variant | wrap(value:Variant, min:Variant, max:Variant) |
| float | wrapf(value:float, min:float, max:float) |
| int | wrapi(value:int, min:int, max:int) |

Variant
abs(x:Variant)
float
absf(x:float)
absi(x:int)
float
acos(x:float)
float
acosh(x:float)
float
angle_difference(from:float, to:float)
float
asin(x:float)
float
asinh(x:float)
float
atan(x:float)
float
atan2(y:float, x:float)
float
atanh(x:float)
float
bezier_derivative(start:float, control_1:float, control_2:float, end:float, t:float)
float
bezier_interpolate(start:float, control_1:float, control_2:float, end:float, t:float)
Variant
bytes_to_var(bytes:PackedByteArray)
Variant
bytes_to_var_with_objects(bytes:PackedByteArray)
Variant
ceil(x:Variant)
float
ceilf(x:float)
ceili(x:float)
Variant
clamp(value:Variant, min:Variant, max:Variant)
float
clampf(value:float, min:float, max:float)
clampi(value:int, min:int, max:int)
float
cos(angle_rad:float)
float
cosh(x:float)
float
cubic_interpolate(from:float, to:float, pre:float, post:float, weight:float)
float
cubic_interpolate_angle(from:float, to:float, pre:float, post:float, weight:float)
float
cubic_interpolate_angle_in_time(from:float, to:float, pre:float, post:float, weight:float, to_t:float, pre_t:float, post_t:float)
float
cubic_interpolate_in_time(from:float, to:float, pre:float, post:float, weight:float, to_t:float, pre_t:float, post_t:float)
float
db_to_linear(db:float)
float
deg_to_rad(deg:float)
float
ease(x:float, curve:float)
String
error_string(error:int)
float
exp(x:float)
Variant
floor(x:Variant)
float
floorf(x:float)
floori(x:float)
float
fmod(x:float, y:float)
float
fposmod(x:float, y:float)
hash(variable:Variant)
Object
instance_from_id(instance_id:int)
float
inverse_lerp(from:float, to:float, weight:float)
bool
is_equal_approx(a:float, b:float)
bool
is_finite(x:float)
bool
is_inf(x:float)
bool
is_instance_id_valid(id:int)
bool
is_instance_valid(instance:Variant)
bool
is_nan(x:float)
bool
is_same(a:Variant, b:Variant)
bool
is_zero_approx(x:float)
Variant
lerp(from:Variant, to:Variant, weight:Variant)
float
lerp_angle(from:float, to:float, weight:float)
float
lerpf(from:float, to:float, weight:float)
float
linear_to_db(lin:float)
float
log(x:float)
Variant
max(...)vararg
float
maxf(a:float, b:float)
maxi(a:int, b:int)
Variant
min(...)vararg
float
minf(a:float, b:float)
mini(a:int, b:int)
float
move_toward(from:float, to:float, delta:float)
nearest_po2(value:int)
float
pingpong(value:float, length:float)
posmod(x:int, y:int)
float
pow(base:float, exp:float)
void
print(...)vararg
void
print_rich(...)vararg
void
print_verbose(...)vararg
void
printerr(...)vararg
void
printraw(...)vararg
void
prints(...)vararg
void
printt(...)vararg
void
push_error(...)vararg
void
push_warning(...)vararg
float
rad_to_deg(rad:float)
PackedInt64Array
rand_from_seed(seed:int)
float
randf()
float
randf_range(from:float, to:float)
float
randfn(mean:float, deviation:float)
randi()
randi_range(from:int, to:int)
void
randomize()
float
remap(value:float, istart:float, istop:float, ostart:float, ostop:float)
rid_allocate_id()
rid_from_int64(base:int)
float
rotate_toward(from:float, to:float, delta:float)
Variant
round(x:Variant)
float
roundf(x:float)
roundi(x:float)
void
seed(base:int)
Variant
sign(x:Variant)
float
signf(x:float)
signi(x:int)
float
sin(angle_rad:float)
float
sinh(x:float)
float
smoothstep(from:float, to:float, x:float)
Variant
snapped(x:Variant, step:Variant)
float
snappedf(x:float, step:float)
snappedi(x:float, step:int)
float
sqrt(x:float)
step_decimals(x:float)
String
str(...)vararg
Variant
str_to_var(string:String)
float
tan(angle_rad:float)
float
tanh(x:float)
Variant
type_convert(variant:Variant, type:int)
String
type_string(type:int)
typeof(variable:Variant)
PackedByteArray
var_to_bytes(variable:Variant)
PackedByteArray
var_to_bytes_with_objects(variable:Variant)
String
var_to_str(variable:Variant)
Variant
weakref(obj:Variant)
Variant
wrap(value:Variant, min:Variant, max:Variant)
float
wrapf(value:float, min:float, max:float)
wrapi(value:int, min:int, max:int)

## Enumerations
enumSide:🔗
SideSIDE_LEFT=0
Left side, usually used forControlorStyleBox-derived classes.
SideSIDE_TOP=1
Top side, usually used forControlorStyleBox-derived classes.
SideSIDE_RIGHT=2
Right side, usually used forControlorStyleBox-derived classes.
SideSIDE_BOTTOM=3
Bottom side, usually used forControlorStyleBox-derived classes.
enumCorner:🔗
CornerCORNER_TOP_LEFT=0
Top-left corner.
CornerCORNER_TOP_RIGHT=1
Top-right corner.
CornerCORNER_BOTTOM_RIGHT=2
Bottom-right corner.
CornerCORNER_BOTTOM_LEFT=3
Bottom-left corner.
enumOrientation:🔗
OrientationVERTICAL=1
General vertical alignment, usually used forSeparator,ScrollBar,Slider, etc.
OrientationHORIZONTAL=0
General horizontal alignment, usually used forSeparator,ScrollBar,Slider, etc.
enumClockDirection:🔗
ClockDirectionCLOCKWISE=0
Clockwise rotation. Used by some methods (e.g.Image.rotate_90()).
ClockDirectionCOUNTERCLOCKWISE=1
Counter-clockwise rotation. Used by some methods (e.g.Image.rotate_90()).
enumHorizontalAlignment:🔗
HorizontalAlignmentHORIZONTAL_ALIGNMENT_LEFT=0
Horizontal left alignment, usually for text-derived classes.
HorizontalAlignmentHORIZONTAL_ALIGNMENT_CENTER=1
Horizontal center alignment, usually for text-derived classes.
HorizontalAlignmentHORIZONTAL_ALIGNMENT_RIGHT=2
Horizontal right alignment, usually for text-derived classes.
HorizontalAlignmentHORIZONTAL_ALIGNMENT_FILL=3
Expand row to fit width, usually for text-derived classes.
enumVerticalAlignment:🔗
VerticalAlignmentVERTICAL_ALIGNMENT_TOP=0
Vertical top alignment, usually for text-derived classes.
VerticalAlignmentVERTICAL_ALIGNMENT_CENTER=1
Vertical center alignment, usually for text-derived classes.
VerticalAlignmentVERTICAL_ALIGNMENT_BOTTOM=2
Vertical bottom alignment, usually for text-derived classes.
VerticalAlignmentVERTICAL_ALIGNMENT_FILL=3
Expand rows to fit height, usually for text-derived classes.
enumInlineAlignment:🔗
InlineAlignmentINLINE_ALIGNMENT_TOP_TO=0
Aligns the top of the inline object (e.g. image, table) to the position of the text specified byINLINE_ALIGNMENT_TO_*constant.
InlineAlignmentINLINE_ALIGNMENT_CENTER_TO=1
Aligns the center of the inline object (e.g. image, table) to the position of the text specified byINLINE_ALIGNMENT_TO_*constant.
InlineAlignmentINLINE_ALIGNMENT_BASELINE_TO=3
Aligns the baseline (user defined) of the inline object (e.g. image, table) to the position of the text specified byINLINE_ALIGNMENT_TO_*constant.
InlineAlignmentINLINE_ALIGNMENT_BOTTOM_TO=2
Aligns the bottom of the inline object (e.g. image, table) to the position of the text specified byINLINE_ALIGNMENT_TO_*constant.
InlineAlignmentINLINE_ALIGNMENT_TO_TOP=0
Aligns the position of the inline object (e.g. image, table) specified byINLINE_ALIGNMENT_*_TOconstant to the top of the text.
InlineAlignmentINLINE_ALIGNMENT_TO_CENTER=4
Aligns the position of the inline object (e.g. image, table) specified byINLINE_ALIGNMENT_*_TOconstant to the center of the text.
InlineAlignmentINLINE_ALIGNMENT_TO_BASELINE=8
Aligns the position of the inline object (e.g. image, table) specified byINLINE_ALIGNMENT_*_TOconstant to the baseline of the text.
InlineAlignmentINLINE_ALIGNMENT_TO_BOTTOM=12
Aligns inline object (e.g. image, table) to the bottom of the text.
InlineAlignmentINLINE_ALIGNMENT_TOP=0
Aligns top of the inline object (e.g. image, table) to the top of the text. Equivalent toINLINE_ALIGNMENT_TOP_TO|INLINE_ALIGNMENT_TO_TOP.
InlineAlignmentINLINE_ALIGNMENT_CENTER=5
Aligns center of the inline object (e.g. image, table) to the center of the text. Equivalent toINLINE_ALIGNMENT_CENTER_TO|INLINE_ALIGNMENT_TO_CENTER.
InlineAlignmentINLINE_ALIGNMENT_BOTTOM=14
Aligns bottom of the inline object (e.g. image, table) to the bottom of the text. Equivalent toINLINE_ALIGNMENT_BOTTOM_TO|INLINE_ALIGNMENT_TO_BOTTOM.
InlineAlignmentINLINE_ALIGNMENT_IMAGE_MASK=3
A bit mask forINLINE_ALIGNMENT_*_TOalignment constants.
InlineAlignmentINLINE_ALIGNMENT_TEXT_MASK=12
A bit mask forINLINE_ALIGNMENT_TO_*alignment constants.
enumEulerOrder:🔗
EulerOrderEULER_ORDER_XYZ=0
Specifies that Euler angles should be in XYZ order. When composing, the order is X, Y, Z. When decomposing, the order is reversed, first Z, then Y, and X last.
EulerOrderEULER_ORDER_XZY=1
Specifies that Euler angles should be in XZY order. When composing, the order is X, Z, Y. When decomposing, the order is reversed, first Y, then Z, and X last.
EulerOrderEULER_ORDER_YXZ=2
Specifies that Euler angles should be in YXZ order. When composing, the order is Y, X, Z. When decomposing, the order is reversed, first Z, then X, and Y last.
EulerOrderEULER_ORDER_YZX=3
Specifies that Euler angles should be in YZX order. When composing, the order is Y, Z, X. When decomposing, the order is reversed, first X, then Z, and Y last.
EulerOrderEULER_ORDER_ZXY=4
Specifies that Euler angles should be in ZXY order. When composing, the order is Z, X, Y. When decomposing, the order is reversed, first Y, then X, and Z last.
EulerOrderEULER_ORDER_ZYX=5
Specifies that Euler angles should be in ZYX order. When composing, the order is Z, Y, X. When decomposing, the order is reversed, first X, then Y, and Z last.
enumKey:🔗
KeyKEY_NONE=0
Enum value which doesn't correspond to any key. This is used to initializeKeyproperties with a generic state.
KeyKEY_SPECIAL=4194304
Keycodes with this bit applied are non-printable.
KeyKEY_ESCAPE=4194305
Escape key.
KeyKEY_TAB=4194306
Tab key.
KeyKEY_BACKTAB=4194307
Shift + Tab key.
KeyKEY_BACKSPACE=4194308
Backspace key.
KeyKEY_ENTER=4194309
Return key (on the main keyboard).
KeyKEY_KP_ENTER=4194310
Enter key on the numeric keypad.
KeyKEY_INSERT=4194311
Insert key.
KeyKEY_DELETE=4194312
Delete key.
KeyKEY_PAUSE=4194313
Pause key.
KeyKEY_PRINT=4194314
Print Screen key.
KeyKEY_SYSREQ=4194315
System Request key.
KeyKEY_CLEAR=4194316
Clear key.
KeyKEY_HOME=4194317
Home key.
KeyKEY_END=4194318
End key.
KeyKEY_LEFT=4194319
Left arrow key.
KeyKEY_UP=4194320
Up arrow key.
KeyKEY_RIGHT=4194321
Right arrow key.
KeyKEY_DOWN=4194322
Down arrow key.
KeyKEY_PAGEUP=4194323
Page Up key.
KeyKEY_PAGEDOWN=4194324
Page Down key.
KeyKEY_SHIFT=4194325
Shift key.
KeyKEY_CTRL=4194326
Control key.
KeyKEY_META=4194327
Meta key.
KeyKEY_ALT=4194328
Alt key.
KeyKEY_CAPSLOCK=4194329
Caps Lock key.
KeyKEY_NUMLOCK=4194330
Num Lock key.
KeyKEY_SCROLLLOCK=4194331
Scroll Lock key.
KeyKEY_F1=4194332
F1 key.
KeyKEY_F2=4194333
F2 key.
KeyKEY_F3=4194334
F3 key.
KeyKEY_F4=4194335
F4 key.
KeyKEY_F5=4194336
F5 key.
KeyKEY_F6=4194337
F6 key.
KeyKEY_F7=4194338
F7 key.
KeyKEY_F8=4194339
F8 key.
KeyKEY_F9=4194340
F9 key.
KeyKEY_F10=4194341
F10 key.
KeyKEY_F11=4194342
F11 key.
KeyKEY_F12=4194343
F12 key.
KeyKEY_F13=4194344
F13 key.
KeyKEY_F14=4194345
F14 key.
KeyKEY_F15=4194346
F15 key.
KeyKEY_F16=4194347
F16 key.
KeyKEY_F17=4194348
F17 key.
KeyKEY_F18=4194349
F18 key.
KeyKEY_F19=4194350
F19 key.
KeyKEY_F20=4194351
F20 key.
KeyKEY_F21=4194352
F21 key.
KeyKEY_F22=4194353
F22 key.
KeyKEY_F23=4194354
F23 key.
KeyKEY_F24=4194355
F24 key.
KeyKEY_F25=4194356
F25 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F26=4194357
F26 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F27=4194358
F27 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F28=4194359
F28 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F29=4194360
F29 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F30=4194361
F30 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F31=4194362
F31 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F32=4194363
F32 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F33=4194364
F33 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F34=4194365
F34 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_F35=4194366
F35 key. Only supported on macOS and Linux due to a Windows limitation.
KeyKEY_KP_MULTIPLY=4194433
Multiply (*) key on the numeric keypad.
KeyKEY_KP_DIVIDE=4194434
Divide (/) key on the numeric keypad.
KeyKEY_KP_SUBTRACT=4194435
Subtract (-) key on the numeric keypad.
KeyKEY_KP_PERIOD=4194436
Period (.) key on the numeric keypad.
KeyKEY_KP_ADD=4194437
Add (+) key on the numeric keypad.
KeyKEY_KP_0=4194438
Number 0 on the numeric keypad.
KeyKEY_KP_1=4194439
Number 1 on the numeric keypad.
KeyKEY_KP_2=4194440
Number 2 on the numeric keypad.
KeyKEY_KP_3=4194441
Number 3 on the numeric keypad.
KeyKEY_KP_4=4194442
Number 4 on the numeric keypad.
KeyKEY_KP_5=4194443
Number 5 on the numeric keypad.
KeyKEY_KP_6=4194444
Number 6 on the numeric keypad.
KeyKEY_KP_7=4194445
Number 7 on the numeric keypad.
KeyKEY_KP_8=4194446
Number 8 on the numeric keypad.
KeyKEY_KP_9=4194447
Number 9 on the numeric keypad.
KeyKEY_MENU=4194370
Context menu key.
KeyKEY_HYPER=4194371
Hyper key. (On Linux/X11 only).
KeyKEY_HELP=4194373
Help key.
KeyKEY_BACK=4194376
Back key.
KeyKEY_FORWARD=4194377
Forward key.
KeyKEY_STOP=4194378
Media stop key.
KeyKEY_REFRESH=4194379
Refresh key.
KeyKEY_VOLUMEDOWN=4194380
Volume down key.
KeyKEY_VOLUMEMUTE=4194381
Mute volume key.
KeyKEY_VOLUMEUP=4194382
Volume up key.
KeyKEY_MEDIAPLAY=4194388
Media play key.
KeyKEY_MEDIASTOP=4194389
Media stop key.
KeyKEY_MEDIAPREVIOUS=4194390
Previous song key.
KeyKEY_MEDIANEXT=4194391
Next song key.
KeyKEY_MEDIARECORD=4194392
Media record key.
KeyKEY_HOMEPAGE=4194393
Home page key.
KeyKEY_FAVORITES=4194394
Favorites key.
KeyKEY_SEARCH=4194395
Search key.
KeyKEY_STANDBY=4194396
Standby key.
KeyKEY_OPENURL=4194397
Open URL / Launch Browser key.
KeyKEY_LAUNCHMAIL=4194398
Launch Mail key.
KeyKEY_LAUNCHMEDIA=4194399
Launch Media key.
KeyKEY_LAUNCH0=4194400
Launch Shortcut 0 key.
KeyKEY_LAUNCH1=4194401
Launch Shortcut 1 key.
KeyKEY_LAUNCH2=4194402
Launch Shortcut 2 key.
KeyKEY_LAUNCH3=4194403
Launch Shortcut 3 key.
KeyKEY_LAUNCH4=4194404
Launch Shortcut 4 key.
KeyKEY_LAUNCH5=4194405
Launch Shortcut 5 key.
KeyKEY_LAUNCH6=4194406
Launch Shortcut 6 key.
KeyKEY_LAUNCH7=4194407
Launch Shortcut 7 key.
KeyKEY_LAUNCH8=4194408
Launch Shortcut 8 key.
KeyKEY_LAUNCH9=4194409
Launch Shortcut 9 key.
KeyKEY_LAUNCHA=4194410
Launch Shortcut A key.
KeyKEY_LAUNCHB=4194411
Launch Shortcut B key.
KeyKEY_LAUNCHC=4194412
Launch Shortcut C key.
KeyKEY_LAUNCHD=4194413
Launch Shortcut D key.
KeyKEY_LAUNCHE=4194414
Launch Shortcut E key.
KeyKEY_LAUNCHF=4194415
Launch Shortcut F key.
KeyKEY_GLOBE=4194416
"Globe" key on Mac / iPad keyboard.
KeyKEY_KEYBOARD=4194417
"On-screen keyboard" key on iPad keyboard.
KeyKEY_JIS_EISU=4194418
英数 key on Mac keyboard.
KeyKEY_JIS_KANA=4194419
かな key on Mac keyboard.
KeyKEY_UNKNOWN=8388607
Unknown key.
KeyKEY_SPACE=32
Space key.
KeyKEY_EXCLAM=33
Exclamation mark (!) key.
KeyKEY_QUOTEDBL=34
Double quotation mark (") key.
KeyKEY_NUMBERSIGN=35
Number sign orhash(#) key.
KeyKEY_DOLLAR=36
Dollar sign ($) key.
KeyKEY_PERCENT=37
Percent sign (%) key.
KeyKEY_AMPERSAND=38
Ampersand (&) key.
KeyKEY_APOSTROPHE=39
Apostrophe (') key.
KeyKEY_PARENLEFT=40
Left parenthesis (() key.
KeyKEY_PARENRIGHT=41
Right parenthesis (``)``) key.
KeyKEY_ASTERISK=42
Asterisk (*) key.
KeyKEY_PLUS=43
Plus (+) key.
KeyKEY_COMMA=44
Comma (,) key.
KeyKEY_MINUS=45
Minus (-) key.
KeyKEY_PERIOD=46
Period (.) key.
KeyKEY_SLASH=47
Slash (/) key.
KeyKEY_0=48
Number 0 key.
KeyKEY_1=49
Number 1 key.
KeyKEY_2=50
Number 2 key.
KeyKEY_3=51
Number 3 key.
KeyKEY_4=52
Number 4 key.
KeyKEY_5=53
Number 5 key.
KeyKEY_6=54
Number 6 key.
KeyKEY_7=55
Number 7 key.
KeyKEY_8=56
Number 8 key.
KeyKEY_9=57
Number 9 key.
KeyKEY_COLON=58
Colon (:) key.
KeyKEY_SEMICOLON=59
Semicolon (;) key.
KeyKEY_LESS=60
Less-than sign (<) key.
KeyKEY_EQUAL=61
Equal sign (=) key.
KeyKEY_GREATER=62
Greater-than sign (>) key.
KeyKEY_QUESTION=63
Question mark (?) key.
KeyKEY_AT=64
At sign (@) key.
KeyKEY_A=65
A key.
KeyKEY_B=66
B key.
KeyKEY_C=67
C key.
KeyKEY_D=68
D key.
KeyKEY_E=69
E key.
KeyKEY_F=70
F key.
KeyKEY_G=71
G key.
KeyKEY_H=72
H key.
KeyKEY_I=73
I key.
KeyKEY_J=74
J key.
KeyKEY_K=75
K key.
KeyKEY_L=76
L key.
KeyKEY_M=77
M key.
KeyKEY_N=78
N key.
KeyKEY_O=79
O key.
KeyKEY_P=80
P key.
KeyKEY_Q=81
Q key.
KeyKEY_R=82
R key.
KeyKEY_S=83
S key.
KeyKEY_T=84
T key.
KeyKEY_U=85
U key.
KeyKEY_V=86
V key.
KeyKEY_W=87
W key.
KeyKEY_X=88
X key.
KeyKEY_Y=89
Y key.
KeyKEY_Z=90
Z key.
KeyKEY_BRACKETLEFT=91
Left bracket ([lb]) key.
KeyKEY_BACKSLASH=92
Backslash (\) key.
KeyKEY_BRACKETRIGHT=93
Right bracket ([rb]) key.
KeyKEY_ASCIICIRCUM=94
Caret (^) key.
KeyKEY_UNDERSCORE=95
Underscore (_) key.
KeyKEY_QUOTELEFT=96
Backtick (`) key.
KeyKEY_BRACELEFT=123
Left brace ({) key.
KeyKEY_BAR=124
Vertical bar orpipe(|) key.
KeyKEY_BRACERIGHT=125
Right brace (}) key.
KeyKEY_ASCIITILDE=126
Tilde (~) key.
KeyKEY_YEN=165
Yen symbol (¥) key.
KeyKEY_SECTION=167
Section sign (§) key.
flagsKeyModifierMask:🔗
KeyModifierMaskKEY_CODE_MASK=8388607
Key Code mask.
KeyModifierMaskKEY_MODIFIER_MASK=2130706432
Modifier key mask.
KeyModifierMaskKEY_MASK_CMD_OR_CTRL=16777216
Automatically remapped toKEY_METAon macOS andKEY_CTRLon other platforms, this mask is never set in the actual events, and should be used for key mapping only.
KeyModifierMaskKEY_MASK_SHIFT=33554432
Shift key mask.
KeyModifierMaskKEY_MASK_ALT=67108864
Alt or Option (on macOS) key mask.
KeyModifierMaskKEY_MASK_META=134217728
Command (on macOS) or Meta/Windows key mask.
KeyModifierMaskKEY_MASK_CTRL=268435456
Control key mask.
KeyModifierMaskKEY_MASK_KPAD=536870912
Keypad key mask.
KeyModifierMaskKEY_MASK_GROUP_SWITCH=1073741824
Group Switch key mask.
enumKeyLocation:🔗
KeyLocationKEY_LOCATION_UNSPECIFIED=0
Used for keys which only appear once, or when a comparison doesn't need to differentiate theLEFTandRIGHTversions.
For example, when usingInputEvent.is_match(), an event which hasKEY_LOCATION_UNSPECIFIEDwill match anyKeyLocationon the passed event.
KeyLocationKEY_LOCATION_LEFT=1
A key which is to the left of its twin.
KeyLocationKEY_LOCATION_RIGHT=2
A key which is to the right of its twin.
enumMouseButton:🔗
MouseButtonMOUSE_BUTTON_NONE=0
Enum value which doesn't correspond to any mouse button. This is used to initializeMouseButtonproperties with a generic state.
MouseButtonMOUSE_BUTTON_LEFT=1
Primary mouse button, usually assigned to the left button.
MouseButtonMOUSE_BUTTON_RIGHT=2
Secondary mouse button, usually assigned to the right button.
MouseButtonMOUSE_BUTTON_MIDDLE=3
Middle mouse button.
MouseButtonMOUSE_BUTTON_WHEEL_UP=4
Mouse wheel scrolling up.
MouseButtonMOUSE_BUTTON_WHEEL_DOWN=5
Mouse wheel scrolling down.
MouseButtonMOUSE_BUTTON_WHEEL_LEFT=6
Mouse wheel left button (only present on some mice).
MouseButtonMOUSE_BUTTON_WHEEL_RIGHT=7
Mouse wheel right button (only present on some mice).
MouseButtonMOUSE_BUTTON_XBUTTON1=8
Extra mouse button 1. This is sometimes present, usually to the sides of the mouse.
MouseButtonMOUSE_BUTTON_XBUTTON2=9
Extra mouse button 2. This is sometimes present, usually to the sides of the mouse.
flagsMouseButtonMask:🔗
MouseButtonMaskMOUSE_BUTTON_MASK_LEFT=1
Primary mouse button mask, usually for the left button.
MouseButtonMaskMOUSE_BUTTON_MASK_RIGHT=2
Secondary mouse button mask, usually for the right button.
MouseButtonMaskMOUSE_BUTTON_MASK_MIDDLE=4
Middle mouse button mask.
MouseButtonMaskMOUSE_BUTTON_MASK_MB_XBUTTON1=128
Extra mouse button 1 mask.
MouseButtonMaskMOUSE_BUTTON_MASK_MB_XBUTTON2=256
Extra mouse button 2 mask.
enumJoyButton:🔗
JoyButtonJOY_BUTTON_INVALID=-1
An invalid game controller button.
JoyButtonJOY_BUTTON_A=0
Game controller SDL button A. Corresponds to the bottom action button: Sony Cross, Xbox A, Nintendo B.
JoyButtonJOY_BUTTON_B=1
Game controller SDL button B. Corresponds to the right action button: Sony Circle, Xbox B, Nintendo A.
JoyButtonJOY_BUTTON_X=2
Game controller SDL button X. Corresponds to the left action button: Sony Square, Xbox X, Nintendo Y.
JoyButtonJOY_BUTTON_Y=3
Game controller SDL button Y. Corresponds to the top action button: Sony Triangle, Xbox Y, Nintendo X.
JoyButtonJOY_BUTTON_BACK=4
Game controller SDL back button. Corresponds to the Sony Select, Xbox Back, Nintendo - button.
JoyButtonJOY_BUTTON_GUIDE=5
Game controller SDL guide button. Corresponds to the Sony PS, Xbox Home button.
JoyButtonJOY_BUTTON_START=6
Game controller SDL start button. Corresponds to the Sony Options, Xbox Menu, Nintendo + button.
JoyButtonJOY_BUTTON_LEFT_STICK=7
Game controller SDL left stick button. Corresponds to the Sony L3, Xbox L/LS button.
JoyButtonJOY_BUTTON_RIGHT_STICK=8
Game controller SDL right stick button. Corresponds to the Sony R3, Xbox R/RS button.
JoyButtonJOY_BUTTON_LEFT_SHOULDER=9
Game controller SDL left shoulder button. Corresponds to the Sony L1, Xbox LB button.
JoyButtonJOY_BUTTON_RIGHT_SHOULDER=10
Game controller SDL right shoulder button. Corresponds to the Sony R1, Xbox RB button.
JoyButtonJOY_BUTTON_DPAD_UP=11
Game controller D-pad up button.
JoyButtonJOY_BUTTON_DPAD_DOWN=12
Game controller D-pad down button.
JoyButtonJOY_BUTTON_DPAD_LEFT=13
Game controller D-pad left button.
JoyButtonJOY_BUTTON_DPAD_RIGHT=14
Game controller D-pad right button.
JoyButtonJOY_BUTTON_MISC1=15
Game controller SDL miscellaneous button. Corresponds to Xbox share button, PS5 microphone button, Nintendo Switch capture button.
JoyButtonJOY_BUTTON_PADDLE1=16
Game controller SDL paddle 1 button.
JoyButtonJOY_BUTTON_PADDLE2=17
Game controller SDL paddle 2 button.
JoyButtonJOY_BUTTON_PADDLE3=18
Game controller SDL paddle 3 button.
JoyButtonJOY_BUTTON_PADDLE4=19
Game controller SDL paddle 4 button.
JoyButtonJOY_BUTTON_TOUCHPAD=20
Game controller SDL touchpad button.
JoyButtonJOY_BUTTON_SDL_MAX=21
The number of SDL game controller buttons.
JoyButtonJOY_BUTTON_MAX=128
The maximum number of game controller buttons supported by the engine. The actual limit may be lower on specific platforms:
- Android:Up to 36 buttons.
Android:Up to 36 buttons.
- Linux:Up to 80 buttons.
Linux:Up to 80 buttons.
- WindowsandmacOS:Up to 128 buttons.
WindowsandmacOS:Up to 128 buttons.
enumJoyAxis:🔗
JoyAxisJOY_AXIS_INVALID=-1
An invalid game controller axis.
JoyAxisJOY_AXIS_LEFT_X=0
Game controller left joystick x-axis.
JoyAxisJOY_AXIS_LEFT_Y=1
Game controller left joystick y-axis.
JoyAxisJOY_AXIS_RIGHT_X=2
Game controller right joystick x-axis.
JoyAxisJOY_AXIS_RIGHT_Y=3
Game controller right joystick y-axis.
JoyAxisJOY_AXIS_TRIGGER_LEFT=4
Game controller left trigger axis.
JoyAxisJOY_AXIS_TRIGGER_RIGHT=5
Game controller right trigger axis.
JoyAxisJOY_AXIS_SDL_MAX=6
The number of SDL game controller axes.
JoyAxisJOY_AXIS_MAX=10
The maximum number of game controller axes: OpenVR supports up to 5 Joysticks making a total of 10 axes.
enumMIDIMessage:🔗
MIDIMessageMIDI_MESSAGE_NONE=0
Does not correspond to any MIDI message. This is the default value ofInputEventMIDI.message.
MIDIMessageMIDI_MESSAGE_NOTE_OFF=8
MIDI message sent when a note is released.
Note:Not all MIDI devices send this message; some may sendMIDI_MESSAGE_NOTE_ONwithInputEventMIDI.velocityset to0.
MIDIMessageMIDI_MESSAGE_NOTE_ON=9
MIDI message sent when a note is pressed.
MIDIMessageMIDI_MESSAGE_AFTERTOUCH=10
MIDI message sent to indicate a change in pressure while a note is being pressed down, also called aftertouch.
MIDIMessageMIDI_MESSAGE_CONTROL_CHANGE=11
MIDI message sent when a controller value changes. In a MIDI device, a controller is any input that doesn't play notes. These may include sliders for volume, balance, and panning, as well as switches and pedals. See theGeneral MIDI specificationfor a small list.
MIDIMessageMIDI_MESSAGE_PROGRAM_CHANGE=12
MIDI message sent when the MIDI device changes its current instrument (also calledprogramorpreset).
MIDIMessageMIDI_MESSAGE_CHANNEL_PRESSURE=13
MIDI message sent to indicate a change in pressure for the whole channel. Some MIDI devices may send this instead ofMIDI_MESSAGE_AFTERTOUCH.
MIDIMessageMIDI_MESSAGE_PITCH_BEND=14
MIDI message sent when the value of the pitch bender changes, usually a wheel on the MIDI device.
MIDIMessageMIDI_MESSAGE_SYSTEM_EXCLUSIVE=240
MIDI system exclusive (SysEx) message. This type of message is not standardized and it's highly dependent on the MIDI device sending it.
Note:Getting this message's data fromInputEventMIDIis not implemented.
MIDIMessageMIDI_MESSAGE_QUARTER_FRAME=241
MIDI message sent every quarter frame to keep connected MIDI devices synchronized. Related toMIDI_MESSAGE_TIMING_CLOCK.
Note:Getting this message's data fromInputEventMIDIis not implemented.
MIDIMessageMIDI_MESSAGE_SONG_POSITION_POINTER=242
MIDI message sent to jump onto a new position in the current sequence or song.
Note:Getting this message's data fromInputEventMIDIis not implemented.
MIDIMessageMIDI_MESSAGE_SONG_SELECT=243
MIDI message sent to select a sequence or song to play.
Note:Getting this message's data fromInputEventMIDIis not implemented.
MIDIMessageMIDI_MESSAGE_TUNE_REQUEST=246
MIDI message sent to request a tuning calibration. Used on analog synthesizers. Most modern MIDI devices do not need this message.
MIDIMessageMIDI_MESSAGE_TIMING_CLOCK=248
MIDI message sent 24 times afterMIDI_MESSAGE_QUARTER_FRAME, to keep connected MIDI devices synchronized.
MIDIMessageMIDI_MESSAGE_START=250
MIDI message sent to start the current sequence or song from the beginning.
MIDIMessageMIDI_MESSAGE_CONTINUE=251
MIDI message sent to resume from the point the current sequence or song was paused.
MIDIMessageMIDI_MESSAGE_STOP=252
MIDI message sent to pause the current sequence or song.
MIDIMessageMIDI_MESSAGE_ACTIVE_SENSING=254
MIDI message sent repeatedly while the MIDI device is idle, to tell the receiver that the connection is alive. Most MIDI devices do not send this message.
MIDIMessageMIDI_MESSAGE_SYSTEM_RESET=255
MIDI message sent to reset a MIDI device to its default state, as if it was just turned on. It should not be sent when the MIDI device is being turned on.
enumError:🔗
ErrorOK=0
Methods that returnErrorreturnOKwhen no error occurred.
SinceOKhas value0, and all other error constants are positive integers, it can also be used in boolean checks.
```
var error = method_that_returns_error()
if error != OK:
    printerr("Failure!")

# Or, alternatively:
if error:
    printerr("Still failing!")
```
Note:Many functions do not return an error code, but will print error messages to standard output.
ErrorFAILED=1
Generic error.
ErrorERR_UNAVAILABLE=2
Unavailable error.
ErrorERR_UNCONFIGURED=3
Unconfigured error.
ErrorERR_UNAUTHORIZED=4
Unauthorized error.
ErrorERR_PARAMETER_RANGE_ERROR=5
Parameter range error.
ErrorERR_OUT_OF_MEMORY=6
Out of memory (OOM) error.
ErrorERR_FILE_NOT_FOUND=7
File: Not found error.
ErrorERR_FILE_BAD_DRIVE=8
File: Bad drive error.
ErrorERR_FILE_BAD_PATH=9
File: Bad path error.
ErrorERR_FILE_NO_PERMISSION=10
File: No permission error.
ErrorERR_FILE_ALREADY_IN_USE=11
File: Already in use error.
ErrorERR_FILE_CANT_OPEN=12
File: Can't open error.
ErrorERR_FILE_CANT_WRITE=13
File: Can't write error.
ErrorERR_FILE_CANT_READ=14
File: Can't read error.
ErrorERR_FILE_UNRECOGNIZED=15
File: Unrecognized error.
ErrorERR_FILE_CORRUPT=16
File: Corrupt error.
ErrorERR_FILE_MISSING_DEPENDENCIES=17
File: Missing dependencies error.
ErrorERR_FILE_EOF=18
File: End of file (EOF) error.
ErrorERR_CANT_OPEN=19
Can't open error.
ErrorERR_CANT_CREATE=20
Can't create error.
ErrorERR_QUERY_FAILED=21
Query failed error.
ErrorERR_ALREADY_IN_USE=22
Already in use error.
ErrorERR_LOCKED=23
Locked error.
ErrorERR_TIMEOUT=24
Timeout error.
ErrorERR_CANT_CONNECT=25
Can't connect error.
ErrorERR_CANT_RESOLVE=26
Can't resolve error.
ErrorERR_CONNECTION_ERROR=27
Connection error.
ErrorERR_CANT_ACQUIRE_RESOURCE=28
Can't acquire resource error.
ErrorERR_CANT_FORK=29
Can't fork process error.
ErrorERR_INVALID_DATA=30
Invalid data error.
ErrorERR_INVALID_PARAMETER=31
Invalid parameter error.
ErrorERR_ALREADY_EXISTS=32
Already exists error.
ErrorERR_DOES_NOT_EXIST=33
Does not exist error.
ErrorERR_DATABASE_CANT_READ=34
Database: Read error.
ErrorERR_DATABASE_CANT_WRITE=35
Database: Write error.
ErrorERR_COMPILATION_FAILED=36
Compilation failed error.
ErrorERR_METHOD_NOT_FOUND=37
Method not found error.
ErrorERR_LINK_FAILED=38
Linking failed error.
ErrorERR_SCRIPT_FAILED=39
Script failed error.
ErrorERR_CYCLIC_LINK=40
Cycling link (import cycle) error.
ErrorERR_INVALID_DECLARATION=41
Invalid declaration error.
ErrorERR_DUPLICATE_SYMBOL=42
Duplicate symbol error.
ErrorERR_PARSE_ERROR=43
Parse error.
ErrorERR_BUSY=44
Busy error.
ErrorERR_SKIP=45
Skip error.
ErrorERR_HELP=46
Help error. Used internally when passing--versionor--helpas executable options.
ErrorERR_BUG=47
Bug error, caused by an implementation issue in the method.
Note:If a built-in method returns this code, please open an issue onthe GitHub Issue Tracker.
ErrorERR_PRINTER_ON_FIRE=48
Printer on fire error (This is an easter egg, no built-in methods return this error code).
enumPropertyHint:🔗
PropertyHintPROPERTY_HINT_NONE=0
The property has no hint for the editor.
PropertyHintPROPERTY_HINT_RANGE=1
Hints that anintorfloatproperty should be within a range specified via the hint string"min,max"or"min,max,step". The hint string can optionally include"or_greater"and/or"or_less"to allow manual input going respectively above the max or below the min values.
Example:"-360,360,1,or_greater,or_less".
Additionally, other keywords can be included:"exp"for exponential range editing,"radians_as_degrees"for editing radian angles in degrees (the range values are also in degrees),"degrees"to hint at an angle,"prefer_slider"to show the slider for integers,"hide_control"to hide the slider or up-down arrows, and"suffix:px/s"to display a suffix indicating the value's unit (e.g.px/sfor pixels per second).
PropertyHintPROPERTY_HINT_ENUM=2
Hints that anint,String, orStringNameproperty is an enumerated value to pick in a list specified via a hint string.
The hint string is a comma separated list of names such as"Hello,Something,Else". Whitespace isnotremoved from either end of a name. For integer properties, the first name in the list has value 0, the next 1, and so on. Explicit values can also be specified by appending:integerto the name, e.g."Zero,One,Three:3,Four,Six:6".
PropertyHintPROPERTY_HINT_ENUM_SUGGESTION=3
Hints that aStringorStringNameproperty can be an enumerated value to pick in a list specified via a hint string such as"Hello,Something,Else". SeePROPERTY_HINT_ENUMfor details.
UnlikePROPERTY_HINT_ENUM, a property with this hint still accepts arbitrary values and can be empty. The list of values serves to suggest possible values.
PropertyHintPROPERTY_HINT_EXP_EASING=4
Hints that afloatproperty should be edited via an exponential easing function. The hint string can include"attenuation"to flip the curve horizontally and/or"positive_only"to exclude in/out easing and limit values to be greater than or equal to zero.
PropertyHintPROPERTY_HINT_LINK=5
Hints that a vector property should allow its components to be linked. For example, this allowsVector2.xandVector2.yto be edited together.
PropertyHintPROPERTY_HINT_FLAGS=6
Hints that anintproperty is a bitmask with named bit flags.
The hint string is a comma separated list of names such as"Bit0,Bit1,Bit2,Bit3". Whitespace isnotremoved from either end of a name. The first name in the list has value 1, the next 2, then 4, 8, 16 and so on. Explicit values can also be specified by appending:integerto the name, e.g."A:4,B:8,C:16". You can also combine several flags ("A:4,B:8,AB:12,C:16").
Note:A flag value must be at least1and at most2**32-1.
Note:UnlikePROPERTY_HINT_ENUM, the previous explicit value is not taken into account. For the hint"A:16,B,C", A is 16, B is 2, C is 4.
PropertyHintPROPERTY_HINT_LAYERS_2D_RENDER=7
Hints that anintproperty is a bitmask using the optionally named 2D render layers.
PropertyHintPROPERTY_HINT_LAYERS_2D_PHYSICS=8
Hints that anintproperty is a bitmask using the optionally named 2D physics layers.
PropertyHintPROPERTY_HINT_LAYERS_2D_NAVIGATION=9
Hints that anintproperty is a bitmask using the optionally named 2D navigation layers.
PropertyHintPROPERTY_HINT_LAYERS_3D_RENDER=10
Hints that anintproperty is a bitmask using the optionally named 3D render layers.
PropertyHintPROPERTY_HINT_LAYERS_3D_PHYSICS=11
Hints that anintproperty is a bitmask using the optionally named 3D physics layers.
PropertyHintPROPERTY_HINT_LAYERS_3D_NAVIGATION=12
Hints that anintproperty is a bitmask using the optionally named 3D navigation layers.
PropertyHintPROPERTY_HINT_LAYERS_AVOIDANCE=37
Hints that an integer property is a bitmask using the optionally named avoidance layers.
PropertyHintPROPERTY_HINT_FILE=13
Hints that aStringproperty is a path to a file. Editing it will show a file dialog for picking the path. The hint string can be a set of filters with wildcards like"*.png,*.jpg". By default the file will be stored as UID whenever available. You can useResourceUIDmethods to convert it back to path. For storing a raw path, usePROPERTY_HINT_FILE_PATH.
PropertyHintPROPERTY_HINT_DIR=14
Hints that aStringproperty is a path to a directory. Editing it will show a file dialog for picking the path.
PropertyHintPROPERTY_HINT_GLOBAL_FILE=15
Hints that aStringproperty is an absolute path to a file outside the project folder. Editing it will show a file dialog for picking the path. The hint string can be a set of filters with wildcards, like"*.png,*.jpg".
PropertyHintPROPERTY_HINT_GLOBAL_DIR=16
Hints that aStringproperty is an absolute path to a directory outside the project folder. Editing it will show a file dialog for picking the path.
PropertyHintPROPERTY_HINT_RESOURCE_TYPE=17
Hints that a property is an instance of aResource-derived type, optionally specified via the hint string (e.g."Texture2D"). Editing it will show a popup menu of valid resource types to instantiate.
PropertyHintPROPERTY_HINT_MULTILINE_TEXT=18
Hints that aStringproperty is text with line breaks. Editing it will show a text input field where line breaks can be typed.
The hint string can be set to"monospace"to force the input field to use a monospaced font.
If the hint string"no_wrap"is set, the input field will not wrap lines at boundaries, instead resorting to making the area scrollable.
PropertyHintPROPERTY_HINT_EXPRESSION=19
Hints that aStringproperty is anExpression.
PropertyHintPROPERTY_HINT_PLACEHOLDER_TEXT=20
Hints that aStringproperty should show a placeholder text on its input field, if empty. The hint string is the placeholder text to use.
PropertyHintPROPERTY_HINT_COLOR_NO_ALPHA=21
Hints that aColorproperty should be edited without affecting its transparency (Color.ais not editable).
PropertyHintPROPERTY_HINT_OBJECT_ID=22
Hints that the property's value is an object encoded as object ID, with its type specified in the hint string. Used by the debugger.
PropertyHintPROPERTY_HINT_TYPE_STRING=23
If a property isString, hints that the property represents a particular type (class). This allows to select a type from the create dialog. The property will store the selected type as a string.
If a property isArray, hints the editor how to show elements. Thehint_stringmust encode nested types using":"and"/".
If a property isDictionary, hints the editor how to show elements. Thehint_stringis the same asArray, with a";"separating the key and value.
```
# Array of elem_type.
hint_string = "%d:" % [elem_type]
hint_string = "%d/%d:%s" % [elem_type, elem_hint, elem_hint_string]
# Two-dimensional array of elem_type (array of arrays of elem_type).
hint_string = "%d:%d:" % [TYPE_ARRAY, elem_type]
hint_string = "%d:%d/%d:%s" % [TYPE_ARRAY, elem_type, elem_hint, elem_hint_string]
# Three-dimensional array of elem_type (array of arrays of arrays of elem_type).
hint_string = "%d:%d:%d:" % [TYPE_ARRAY, TYPE_ARRAY, elem_type]
hint_string = "%d:%d:%d/%d:%s" % [TYPE_ARRAY, TYPE_ARRAY, elem_type, elem_hint, elem_hint_string]
```
```
// Array of elemType.
hintString = $"{elemType:D}:";
hintString = $"{elemType:}/{elemHint:D}:{elemHintString}";
// Two-dimensional array of elemType (array of arrays of elemType).
hintString = $"{Variant.Type.Array:D}:{elemType:D}:";
hintString = $"{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}";
// Three-dimensional array of elemType (array of arrays of arrays of elemType).
hintString = $"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}:";
hintString = $"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}";
```
Examples:
```
hint_string = "%d:" % [TYPE_INT] # Array of integers.
hint_string = "%d/%d:1,10,1" % [TYPE_INT, PROPERTY_HINT_RANGE] # Array of integers (in range from 1 to 10).
hint_string = "%d/%d:Zero,One,Two" % [TYPE_INT, PROPERTY_HINT_ENUM] # Array of integers (an enum).
hint_string = "%d/%d:Zero,One,Three:3,Six:6" % [TYPE_INT, PROPERTY_HINT_ENUM] # Array of integers (an enum).
hint_string = "%d/%d:*.png" % [TYPE_STRING, PROPERTY_HINT_FILE] # Array of strings (file paths).
hint_string = "%d/%d:Texture2D" % [TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE] # Array of textures.

hint_string = "%d:%d:" % [TYPE_ARRAY, TYPE_FLOAT] # Two-dimensional array of floats.
hint_string = "%d:%d/%d:" % [TYPE_ARRAY, TYPE_STRING, PROPERTY_HINT_MULTILINE_TEXT] # Two-dimensional array of multiline strings.
hint_string = "%d:%d/%d:-1,1,0.1" % [TYPE_ARRAY, TYPE_FLOAT, PROPERTY_HINT_RANGE] # Two-dimensional array of floats (in range from -1 to 1).
hint_string = "%d:%d/%d:Texture2D" % [TYPE_ARRAY, TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE] # Two-dimensional array of textures.
```
```
hintString = $"{Variant.Type.Int:D}/{PropertyHint.Range:D}:1,10,1"; // Array of integers (in range from 1 to 10).
hintString = $"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Two"; // Array of integers (an enum).
hintString = $"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Three:3,Six:6"; // Array of integers (an enum).
hintString = $"{Variant.Type.String:D}/{PropertyHint.File:D}:*.png"; // Array of strings (file paths).
hintString = $"{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D"; // Array of textures.

hintString = $"{Variant.Type.Array:D}:{Variant.Type.Float:D}:"; // Two-dimensional array of floats.
hintString = $"{Variant.Type.Array:D}:{Variant.Type.String:D}/{PropertyHint.MultilineText:D}:"; // Two-dimensional array of multiline strings.
hintString = $"{Variant.Type.Array:D}:{Variant.Type.Float:D}/{PropertyHint.Range:D}:-1,1,0.1"; // Two-dimensional array of floats (in range from -1 to 1).
hintString = $"{Variant.Type.Array:D}:{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D"; // Two-dimensional array of textures.
```
Note:The trailing colon is required for properly detecting built-in types.
PropertyHintPROPERTY_HINT_NODE_PATH_TO_EDITED_NODE=24
Deprecated:This hint is not used by the engine.
PropertyHintPROPERTY_HINT_OBJECT_TOO_BIG=25
Hints that an object is too big to be sent via the debugger.
PropertyHintPROPERTY_HINT_NODE_PATH_VALID_TYPES=26
Hints that the hint string specifies valid node types for property of typeNodePath.
PropertyHintPROPERTY_HINT_SAVE_FILE=27
Hints that aStringproperty is a path to a file. Editing it will show a file dialog for picking the path for the file to be saved at. The dialog has access to the project's directory. The hint string can be a set of filters with wildcards like"*.png,*.jpg". See alsoFileDialog.filters.
PropertyHintPROPERTY_HINT_GLOBAL_SAVE_FILE=28
Hints that aStringproperty is a path to a file. Editing it will show a file dialog for picking the path for the file to be saved at. The dialog has access to the entire filesystem. The hint string can be a set of filters with wildcards like"*.png,*.jpg". See alsoFileDialog.filters.
PropertyHintPROPERTY_HINT_INT_IS_OBJECTID=29
Deprecated:This hint is not used by the engine.
PropertyHintPROPERTY_HINT_INT_IS_POINTER=30
Hints that anintproperty is a pointer. Used by GDExtension.
PropertyHintPROPERTY_HINT_ARRAY_TYPE=31
Hints that a property is anArraywith the stored type specified in the hint string. The hint string contains the type of the array (e.g."String").
Use the hint string format fromPROPERTY_HINT_TYPE_STRINGfor more control over the stored type.
PropertyHintPROPERTY_HINT_DICTIONARY_TYPE=38
Hints that a property is aDictionarywith the stored types specified in the hint string. The hint string contains the key and value types separated by a semicolon (e.g."int;String").
Use the hint string format fromPROPERTY_HINT_TYPE_STRINGfor more control over the stored types.
PropertyHintPROPERTY_HINT_LOCALE_ID=32
Hints that a string property is a locale code. Editing it will show a locale dialog for picking language and country.
PropertyHintPROPERTY_HINT_LOCALIZABLE_STRING=33
Hints that a dictionary property is string translation map. Dictionary keys are locale codes and, values are translated strings.
PropertyHintPROPERTY_HINT_NODE_TYPE=34
Hints that a property is an instance of aNode-derived type, optionally specified via the hint string (e.g."Node2D"). Editing it will show a dialog for picking a node from the scene.
PropertyHintPROPERTY_HINT_HIDE_QUATERNION_EDIT=35
Hints that a quaternion property should disable the temporary euler editor.
PropertyHintPROPERTY_HINT_PASSWORD=36
Hints that a string property is a password, and every character is replaced with the secret character.
PropertyHintPROPERTY_HINT_TOOL_BUTTON=39
Hints that aCallableproperty should be displayed as a clickable button. When the button is pressed, the callable is called. The hint string specifies the button text and optionally an icon from the"EditorIcons"theme type.
```
"Click me!" - A button with the text "Click me!" and the default "Callable" icon.
"Click me!,ColorRect" - A button with the text "Click me!" and the "ColorRect" icon.
```
Note:ACallablecannot be properly serialized and stored in a file, so it is recommended to usePROPERTY_USAGE_EDITORinstead ofPROPERTY_USAGE_DEFAULT.
PropertyHintPROPERTY_HINT_ONESHOT=40
Hints that a property will be changed on its own after setting, such asAudioStreamPlayer.playingorGPUParticles3D.emitting.
PropertyHintPROPERTY_HINT_GROUP_ENABLE=42
Hints that a boolean property will enable the feature associated with the group that it occurs in. The property will be displayed as a checkbox on the group header. Only works within a group or subgroup.
By default, disabling the property hides all properties in the group. Use the optional hint string"checkbox_only"to disable this behavior.
PropertyHintPROPERTY_HINT_INPUT_NAME=43
Hints that aStringorStringNameproperty is the name of an input action. This allows the selection of any action name from the Input Map in the Project Settings. The hint string may contain two options separated by commas:
- If it contains"show_builtin", built-in input actions are included in the selection.
If it contains"show_builtin", built-in input actions are included in the selection.
- If it contains"loose_mode", loose mode is enabled. This allows inserting any action name even if it's not present in the input map.
If it contains"loose_mode", loose mode is enabled. This allows inserting any action name even if it's not present in the input map.
PropertyHintPROPERTY_HINT_FILE_PATH=44
LikePROPERTY_HINT_FILE, but the property is stored as a raw path, not UID. That means the reference will be broken if you move the file. Consider usingPROPERTY_HINT_FILEwhen possible.
PropertyHintPROPERTY_HINT_MAX=45
Represents the size of thePropertyHintenum.
flagsPropertyUsageFlags:🔗
PropertyUsageFlagsPROPERTY_USAGE_NONE=0
The property is not stored, and does not display in the editor. This is the default for non-exported properties.
PropertyUsageFlagsPROPERTY_USAGE_STORAGE=2
The property is serialized and saved in the scene file (default for exported properties).
PropertyUsageFlagsPROPERTY_USAGE_EDITOR=4
The property is shown in theEditorInspector(default for exported properties).
PropertyUsageFlagsPROPERTY_USAGE_INTERNAL=8
The property is excluded from the class reference.
PropertyUsageFlagsPROPERTY_USAGE_CHECKABLE=16
The property can be checked in theEditorInspector.
PropertyUsageFlagsPROPERTY_USAGE_CHECKED=32
The property is checked in theEditorInspector.
PropertyUsageFlagsPROPERTY_USAGE_GROUP=64
Used to group properties together in the editor. SeeEditorInspector.
PropertyUsageFlagsPROPERTY_USAGE_CATEGORY=128
Used to categorize properties together in the editor.
PropertyUsageFlagsPROPERTY_USAGE_SUBGROUP=256
Used to group properties together in the editor in a subgroup (under a group). SeeEditorInspector.
PropertyUsageFlagsPROPERTY_USAGE_CLASS_IS_BITFIELD=512
The property is a bitfield, i.e. it contains multiple flags represented as bits.
PropertyUsageFlagsPROPERTY_USAGE_NO_INSTANCE_STATE=1024
The property does not save its state inPackedScene.
PropertyUsageFlagsPROPERTY_USAGE_RESTART_IF_CHANGED=2048
Editing the property prompts the user for restarting the editor.
PropertyUsageFlagsPROPERTY_USAGE_SCRIPT_VARIABLE=4096
The property is a script variable.PROPERTY_USAGE_SCRIPT_VARIABLEcan be used to distinguish between exported script variables from built-in variables (which don't have this usage flag). By default,PROPERTY_USAGE_SCRIPT_VARIABLEisnotapplied to variables that are created by overridingObject._get_property_list()in a script.
PropertyUsageFlagsPROPERTY_USAGE_STORE_IF_NULL=8192
The property value of typeObjectwill be stored even if its value isnull.
PropertyUsageFlagsPROPERTY_USAGE_UPDATE_ALL_IF_MODIFIED=16384
If this property is modified, all inspector fields will be refreshed.
PropertyUsageFlagsPROPERTY_USAGE_SCRIPT_DEFAULT_VALUE=32768
Deprecated:This flag is not used by the engine.
PropertyUsageFlagsPROPERTY_USAGE_CLASS_IS_ENUM=65536
The property is a variable of enum type, i.e. it only takes named integer constants from its associated enumeration.
PropertyUsageFlagsPROPERTY_USAGE_NIL_IS_VARIANT=131072
If property hasnilas default value, its type will beVariant.
PropertyUsageFlagsPROPERTY_USAGE_ARRAY=262144
The property is the element count of a property array, i.e. a list of groups of related properties. Properties defined with this usage also need a specificclass_namefield in the form oflabel,prefix. The field may also include additional comma-separated options:
- page_size=N: OverridesEditorSettings.interface/inspector/max_array_dictionary_items_per_pagefor this array.
page_size=N: OverridesEditorSettings.interface/inspector/max_array_dictionary_items_per_pagefor this array.
- add_button_text=text: The text displayed by the "Add Element" button.
add_button_text=text: The text displayed by the "Add Element" button.
- static: The elements can't be re-arranged.
static: The elements can't be re-arranged.
- const: New elements can't be added.
const: New elements can't be added.
- numbered: An index will appear next to each element.
numbered: An index will appear next to each element.
- unfoldable: The array can't be folded.
unfoldable: The array can't be folded.
- swap_method=method_name: The method that will be called when two elements switch places. The method should take 2intparameters, which will be indices of the elements being swapped.
swap_method=method_name: The method that will be called when two elements switch places. The method should take 2intparameters, which will be indices of the elements being swapped.
Note that making a full-fledged property array requires boilerplate code involvingObject._get_property_list().
PropertyUsageFlagsPROPERTY_USAGE_ALWAYS_DUPLICATE=524288
When duplicating a resource withResource.duplicate(), and this flag is set on a property of that resource, the property should always be duplicated, regardless of thesubresourcesbool parameter.
PropertyUsageFlagsPROPERTY_USAGE_NEVER_DUPLICATE=1048576
When duplicating a resource withResource.duplicate(), and this flag is set on a property of that resource, the property should never be duplicated, regardless of thesubresourcesbool parameter.
PropertyUsageFlagsPROPERTY_USAGE_HIGH_END_GFX=2097152
The property is only shown in the editor if modern renderers are supported (the Compatibility rendering method is excluded).
PropertyUsageFlagsPROPERTY_USAGE_NODE_PATH_FROM_SCENE_ROOT=4194304
TheNodePathproperty will always be relative to the scene's root. Mostly useful for local resources.
PropertyUsageFlagsPROPERTY_USAGE_RESOURCE_NOT_PERSISTENT=8388608
Use when a resource is created on the fly, i.e. the getter will always return a different instance.ResourceSaverneeds this information to properly save such resources.
PropertyUsageFlagsPROPERTY_USAGE_KEYING_INCREMENTS=16777216
Inserting an animation key frame of this property will automatically increment the value, allowing to easily keyframe multiple values in a row.
PropertyUsageFlagsPROPERTY_USAGE_DEFERRED_SET_RESOURCE=33554432
Deprecated:This flag is not used by the engine.
PropertyUsageFlagsPROPERTY_USAGE_EDITOR_INSTANTIATE_OBJECT=67108864
When this property is aResourceand base object is aNode, a resource instance will be automatically created whenever the node is created in the editor.
PropertyUsageFlagsPROPERTY_USAGE_EDITOR_BASIC_SETTING=134217728
The property is considered a basic setting and will appear even when advanced mode is disabled. Used for project settings.
PropertyUsageFlagsPROPERTY_USAGE_READ_ONLY=268435456
The property is read-only in theEditorInspector.
PropertyUsageFlagsPROPERTY_USAGE_SECRET=536870912
An export preset property with this flag contains confidential information and is stored separately from the rest of the export preset configuration.
PropertyUsageFlagsPROPERTY_USAGE_DEFAULT=6
Default usage (storage and editor).
PropertyUsageFlagsPROPERTY_USAGE_NO_EDITOR=2
Default usage but without showing the property in the editor (storage).
flagsMethodFlags:🔗
MethodFlagsMETHOD_FLAG_NORMAL=1
Flag for a normal method.
MethodFlagsMETHOD_FLAG_EDITOR=2
Flag for an editor method.
MethodFlagsMETHOD_FLAG_CONST=4
Flag for a constant method.
MethodFlagsMETHOD_FLAG_VIRTUAL=8
Flag for a virtual method.
MethodFlagsMETHOD_FLAG_VARARG=16
Flag for a method with a variable number of arguments.
MethodFlagsMETHOD_FLAG_STATIC=32
Flag for a static method.
MethodFlagsMETHOD_FLAG_OBJECT_CORE=64
Used internally. Allows to not dump core virtual methods (such asObject._notification()) to the JSON API.
MethodFlagsMETHOD_FLAG_VIRTUAL_REQUIRED=128
Flag for a virtual method that is required. In GDScript, this flag is set for abstract functions.
MethodFlagsMETHOD_FLAGS_DEFAULT=1
Default method flags (normal).
enumVariant.Type:🔗
Variant.TypeTYPE_NIL=0
Variable isnull.
Variant.TypeTYPE_BOOL=1
Variable is of typebool.
Variant.TypeTYPE_INT=2
Variable is of typeint.
Variant.TypeTYPE_FLOAT=3
Variable is of typefloat.
Variant.TypeTYPE_STRING=4
Variable is of typeString.
Variant.TypeTYPE_VECTOR2=5
Variable is of typeVector2.
Variant.TypeTYPE_VECTOR2I=6
Variable is of typeVector2i.
Variant.TypeTYPE_RECT2=7
Variable is of typeRect2.
Variant.TypeTYPE_RECT2I=8
Variable is of typeRect2i.
Variant.TypeTYPE_VECTOR3=9
Variable is of typeVector3.
Variant.TypeTYPE_VECTOR3I=10
Variable is of typeVector3i.
Variant.TypeTYPE_TRANSFORM2D=11
Variable is of typeTransform2D.
Variant.TypeTYPE_VECTOR4=12
Variable is of typeVector4.
Variant.TypeTYPE_VECTOR4I=13
Variable is of typeVector4i.
Variant.TypeTYPE_PLANE=14
Variable is of typePlane.
Variant.TypeTYPE_QUATERNION=15
Variable is of typeQuaternion.
Variant.TypeTYPE_AABB=16
Variable is of typeAABB.
Variant.TypeTYPE_BASIS=17
Variable is of typeBasis.
Variant.TypeTYPE_TRANSFORM3D=18
Variable is of typeTransform3D.
Variant.TypeTYPE_PROJECTION=19
Variable is of typeProjection.
Variant.TypeTYPE_COLOR=20
Variable is of typeColor.
Variant.TypeTYPE_STRING_NAME=21
Variable is of typeStringName.
Variant.TypeTYPE_NODE_PATH=22
Variable is of typeNodePath.
Variant.TypeTYPE_RID=23
Variable is of typeRID.
Variant.TypeTYPE_OBJECT=24
Variable is of typeObject.
Variant.TypeTYPE_CALLABLE=25
Variable is of typeCallable.
Variant.TypeTYPE_SIGNAL=26
Variable is of typeSignal.
Variant.TypeTYPE_DICTIONARY=27
Variable is of typeDictionary.
Variant.TypeTYPE_ARRAY=28
Variable is of typeArray.
Variant.TypeTYPE_PACKED_BYTE_ARRAY=29
Variable is of typePackedByteArray.
Variant.TypeTYPE_PACKED_INT32_ARRAY=30
Variable is of typePackedInt32Array.
Variant.TypeTYPE_PACKED_INT64_ARRAY=31
Variable is of typePackedInt64Array.
Variant.TypeTYPE_PACKED_FLOAT32_ARRAY=32
Variable is of typePackedFloat32Array.
Variant.TypeTYPE_PACKED_FLOAT64_ARRAY=33
Variable is of typePackedFloat64Array.
Variant.TypeTYPE_PACKED_STRING_ARRAY=34
Variable is of typePackedStringArray.
Variant.TypeTYPE_PACKED_VECTOR2_ARRAY=35
Variable is of typePackedVector2Array.
Variant.TypeTYPE_PACKED_VECTOR3_ARRAY=36
Variable is of typePackedVector3Array.
Variant.TypeTYPE_PACKED_COLOR_ARRAY=37
Variable is of typePackedColorArray.
Variant.TypeTYPE_PACKED_VECTOR4_ARRAY=38
Variable is of typePackedVector4Array.
Variant.TypeTYPE_MAX=39
Represents the size of theVariant.Typeenum.
enumVariant.Operator:🔗
Variant.OperatorOP_EQUAL=0
Equality operator (==).
Variant.OperatorOP_NOT_EQUAL=1
Inequality operator (!=).
Variant.OperatorOP_LESS=2
Less than operator (<).
Variant.OperatorOP_LESS_EQUAL=3
Less than or equal operator (<=).
Variant.OperatorOP_GREATER=4
Greater than operator (>).
Variant.OperatorOP_GREATER_EQUAL=5
Greater than or equal operator (>=).
Variant.OperatorOP_ADD=6
Addition operator (+).
Variant.OperatorOP_SUBTRACT=7
Subtraction operator (-).
Variant.OperatorOP_MULTIPLY=8
Multiplication operator (*).
Variant.OperatorOP_DIVIDE=9
Division operator (/).
Variant.OperatorOP_NEGATE=10
Unary negation operator (-).
Variant.OperatorOP_POSITIVE=11
Unary plus operator (+).
Variant.OperatorOP_MODULE=12
Remainder/modulo operator (%).
Variant.OperatorOP_POWER=13
Power operator (**).
Variant.OperatorOP_SHIFT_LEFT=14
Left shift operator (<<).
Variant.OperatorOP_SHIFT_RIGHT=15
Right shift operator (>>).
Variant.OperatorOP_BIT_AND=16
Bitwise AND operator (&).
Variant.OperatorOP_BIT_OR=17
Bitwise OR operator (|).
Variant.OperatorOP_BIT_XOR=18
Bitwise XOR operator (^).
Variant.OperatorOP_BIT_NEGATE=19
Bitwise NOT operator (~).
Variant.OperatorOP_AND=20
Logical AND operator (andor&&).
Variant.OperatorOP_OR=21
Logical OR operator (oror||).
Variant.OperatorOP_XOR=22
Logical XOR operator (not implemented in GDScript).
Variant.OperatorOP_NOT=23
Logical NOT operator (notor!).
Variant.OperatorOP_IN=24
Logical IN operator (in).
Variant.OperatorOP_MAX=25
Represents the size of theVariant.Operatorenum.

## Property Descriptions
AudioServerAudioServer🔗
TheAudioServersingleton.
CameraServerCameraServer🔗
TheCameraServersingleton.
ClassDBClassDB🔗
TheClassDBsingleton.
DisplayServerDisplayServer🔗
TheDisplayServersingleton.
EditorInterfaceEditorInterface🔗
TheEditorInterfacesingleton.
Note:Only available in editor builds.
EngineEngine🔗
TheEnginesingleton.
EngineDebuggerEngineDebugger🔗
TheEngineDebuggersingleton.
GDExtensionManagerGDExtensionManager🔗
TheGDExtensionManagersingleton.
Geometry2DGeometry2D🔗
TheGeometry2Dsingleton.
Geometry3DGeometry3D🔗
TheGeometry3Dsingleton.
IPIP🔗
TheIPsingleton.
InputInput🔗
TheInputsingleton.
InputMapInputMap🔗
TheInputMapsingleton.
JavaClassWrapperJavaClassWrapper🔗
TheJavaClassWrappersingleton.
Note:Only implemented on Android.
JavaScriptBridgeJavaScriptBridge🔗
TheJavaScriptBridgesingleton.
Note:Only implemented on the Web platform.
MarshallsMarshalls🔗
TheMarshallssingleton.
NativeMenuNativeMenu🔗
TheNativeMenusingleton.
Note:Only implemented on macOS.
NavigationMeshGeneratorNavigationMeshGenerator🔗
TheNavigationMeshGeneratorsingleton.
NavigationServer2DNavigationServer2D🔗
TheNavigationServer2Dsingleton.
NavigationServer2DManagerNavigationServer2DManager🔗
TheNavigationServer2DManagersingleton.
NavigationServer3DNavigationServer3D🔗
TheNavigationServer3Dsingleton.
NavigationServer3DManagerNavigationServer3DManager🔗
TheNavigationServer3DManagersingleton.
OSOS🔗
TheOSsingleton.
PerformancePerformance🔗
ThePerformancesingleton.
PhysicsServer2DPhysicsServer2D🔗
ThePhysicsServer2Dsingleton.
PhysicsServer2DManagerPhysicsServer2DManager🔗
ThePhysicsServer2DManagersingleton.
PhysicsServer3DPhysicsServer3D🔗
ThePhysicsServer3Dsingleton.
PhysicsServer3DManagerPhysicsServer3DManager🔗
ThePhysicsServer3DManagersingleton.
ProjectSettingsProjectSettings🔗
TheProjectSettingssingleton.
RenderingServerRenderingServer🔗
TheRenderingServersingleton.
ResourceLoaderResourceLoader🔗
TheResourceLoadersingleton.
ResourceSaverResourceSaver🔗
TheResourceSaversingleton.
ResourceUIDResourceUID🔗
TheResourceUIDsingleton.
TextServerManagerTextServerManager🔗
TheTextServerManagersingleton.
ThemeDBThemeDB🔗
TheThemeDBsingleton.
TimeTime🔗
TheTimesingleton.
TranslationServerTranslationServer🔗
TheTranslationServersingleton.
WorkerThreadPoolWorkerThreadPool🔗
TheWorkerThreadPoolsingleton.
XRServerXRServer🔗
TheXRServersingleton.

## Method Descriptions
Variantabs(x:Variant)🔗
Returns the absolute value of aVariantparameterx(i.e. non-negative value). Supported types:int,float,Vector2,Vector2i,Vector3,Vector3i,Vector4,Vector4i.
```
var a = abs(-1)
# a is 1

var b = abs(-1.2)
# b is 1.2

var c = abs(Vector2(-3.5, -4))
# c is (3.5, 4)

var d = abs(Vector2i(-5, -6))
# d is (5, 6)

var e = abs(Vector3(-7, 8.5, -3.8))
# e is (7, 8.5, 3.8)

var f = abs(Vector3i(-7, -8, -9))
# f is (7, 8, 9)
```
Note:For better type safety, useabsf(),absi(),Vector2.abs(),Vector2i.abs(),Vector3.abs(),Vector3i.abs(),Vector4.abs(), orVector4i.abs().
floatabsf(x:float)🔗
Returns the absolute value of float parameterx(i.e. positive value).
```
# a is 1.2
var a = absf(-1.2)
```
intabsi(x:int)🔗
Returns the absolute value of int parameterx(i.e. positive value).
```
# a is 1
var a = absi(-1)
```
floatacos(x:float)🔗
Returns the arc cosine ofxin radians. Use to get the angle of cosinex.xwill be clamped between-1.0and1.0(inclusive), in order to preventacos()from returning@GDScript.NAN.
```
# c is 0.523599 or 30 degrees if converted with rad_to_deg(c)
var c = acos(0.866025)
```
floatacosh(x:float)🔗
Returns the hyperbolic arc (also called inverse) cosine ofx, returning a value in radians. Use it to get the angle from an angle's cosine in hyperbolic space ifxis larger or equal to 1. For values ofxlower than 1, it will return 0, in order to preventacosh()from returning@GDScript.NAN.
```
var a = acosh(2) # Returns 1.31695789692482
cosh(a) # Returns 2

var b = acosh(-1) # Returns 0
```
floatangle_difference(from:float, to:float)🔗
Returns the difference between the two angles (in radians), in the range of[-PI,+PI]. Whenfromandtoare opposite, returns-PIiffromis smaller thanto, orPIotherwise.
floatasin(x:float)🔗
Returns the arc sine ofxin radians. Use to get the angle of sinex.xwill be clamped between-1.0and1.0(inclusive), in order to preventasin()from returning@GDScript.NAN.
```
# s is 0.523599 or 30 degrees if converted with rad_to_deg(s)
var s = asin(0.5)
```
floatasinh(x:float)🔗
Returns the hyperbolic arc (also called inverse) sine ofx, returning a value in radians. Use it to get the angle from an angle's sine in hyperbolic space.
```
var a = asinh(0.9) # Returns 0.8088669356527824
sinh(a) # Returns 0.9
```
floatatan(x:float)🔗
Returns the arc tangent ofxin radians. Use it to get the angle from an angle's tangent in trigonometry.
The method cannot know in which quadrant the angle should fall. Seeatan2()if you have bothyandx.
```
var a = atan(0.5) # a is 0.463648
```
Ifxis between-PI/2andPI/2(inclusive),atan(tan(x))is equal tox.
floatatan2(y:float, x:float)🔗
Returns the arc tangent ofy/xin radians. Use to get the angle of tangenty/x. To compute the value, the method takes into account the sign of both arguments in order to determine the quadrant.
Important note: The Y coordinate comes first, by convention.
```
var a = atan2(0, -1) # a is 3.141593
```
floatatanh(x:float)🔗
Returns the hyperbolic arc (also called inverse) tangent ofx, returning a value in radians. Use it to get the angle from an angle's tangent in hyperbolic space ifxis between -1 and 1 (non-inclusive).
In mathematics, the inverse hyperbolic tangent is only defined for -1 <x< 1 in the real set, so values equal or lower to -1 forxreturn negative@GDScript.INFand values equal or higher than 1 return positive@GDScript.INFin order to preventatanh()from returning@GDScript.NAN.
```
var a = atanh(0.9) # Returns 1.47221948958322
tanh(a) # Returns 0.9

var b = atanh(-2) # Returns -inf
tanh(b) # Returns -1
```
floatbezier_derivative(start:float, control_1:float, control_2:float, end:float, t:float)🔗
Returns the derivative at the giventon a one-dimensionalBézier curvedefined by the givencontrol_1,control_2, andendpoints.
floatbezier_interpolate(start:float, control_1:float, control_2:float, end:float, t:float)🔗
Returns the point at the giventon a one-dimensionalBézier curvedefined by the givencontrol_1,control_2, andendpoints.
Variantbytes_to_var(bytes:PackedByteArray)🔗
Decodes a byte array back to aVariantvalue, without decoding objects.
Note:If you need object deserialization, seebytes_to_var_with_objects().
Variantbytes_to_var_with_objects(bytes:PackedByteArray)🔗
Decodes a byte array back to aVariantvalue. Decoding objects is allowed.
Warning:Deserialized object can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats (remote code execution).
Variantceil(x:Variant)🔗
Roundsxupward (towards positive infinity), returning the smallest whole number that is not less thanx. Supported types:int,float,Vector2,Vector2i,Vector3,Vector3i,Vector4,Vector4i.
```
var i = ceil(1.45) # i is 2.0
i = ceil(1.001)    # i is 2.0
```
See alsofloor(),round(), andsnapped().
Note:For better type safety, useceilf(),ceili(),Vector2.ceil(),Vector3.ceil(), orVector4.ceil().
floatceilf(x:float)🔗
Roundsxupward (towards positive infinity), returning the smallest whole number that is not less thanx.
A type-safe version ofceil(), returning afloat.
intceili(x:float)🔗
Roundsxupward (towards positive infinity), returning the smallest whole number that is not less thanx.
A type-safe version ofceil(), returning anint.
Variantclamp(value:Variant, min:Variant, max:Variant)🔗
Clamps thevalue, returning aVariantnot less thanminand not more thanmax. Any values that can be compared with the less than and greater than operators will work.
```
var a = clamp(-10, -1, 5)
# a is -1

var b = clamp(8.1, 0.9, 5.5)
# b is 5.5
```
Note:For better type safety, useclampf(),clampi(),Vector2.clamp(),Vector2i.clamp(),Vector3.clamp(),Vector3i.clamp(),Vector4.clamp(),Vector4i.clamp(), orColor.clamp()(not currently supported by this method).
Note:When using this on vectors it willnotperform component-wise clamping, and will pickminifvalue<minormaxifvalue>max. To perform component-wise clamping use the methods listed above.
floatclampf(value:float, min:float, max:float)🔗
Clamps thevalue, returning afloatnot less thanminand not more thanmax.
```
var speed = 42.1
var a = clampf(speed, 1.0, 20.5) # a is 20.5

speed = -10.0
var b = clampf(speed, -1.0, 1.0) # b is -1.0
```
intclampi(value:int, min:int, max:int)🔗
Clamps thevalue, returning anintnot less thanminand not more thanmax.
```
var speed = 42
var a = clampi(speed, 1, 20) # a is 20

speed = -10
var b = clampi(speed, -1, 1) # b is -1
```
floatcos(angle_rad:float)🔗
Returns the cosine of angleangle_radin radians.
```
cos(PI * 2)         # Returns 1.0
cos(PI)             # Returns -1.0
cos(deg_to_rad(90)) # Returns 0.0
```
floatcosh(x:float)🔗
Returns the hyperbolic cosine ofxin radians.
```
print(cosh(1)) # Prints 1.543081
```
floatcubic_interpolate(from:float, to:float, pre:float, post:float, weight:float)🔗
Cubic interpolates between two values by the factor defined inweightwithpreandpostvalues.
floatcubic_interpolate_angle(from:float, to:float, pre:float, post:float, weight:float)🔗
Cubic interpolates between two rotation values with shortest path by the factor defined inweightwithpreandpostvalues. See alsolerp_angle().
floatcubic_interpolate_angle_in_time(from:float, to:float, pre:float, post:float, weight:float, to_t:float, pre_t:float, post_t:float)🔗
Cubic interpolates between two rotation values with shortest path by the factor defined inweightwithpreandpostvalues. See alsolerp_angle().
It can perform smoother interpolation thancubic_interpolate()by the time values.
floatcubic_interpolate_in_time(from:float, to:float, pre:float, post:float, weight:float, to_t:float, pre_t:float, post_t:float)🔗
Cubic interpolates between two values by the factor defined inweightwithpreandpostvalues.
It can perform smoother interpolation thancubic_interpolate()by the time values.
floatdb_to_linear(db:float)🔗
Converts from decibels to linear energy (audio).
floatdeg_to_rad(deg:float)🔗
Converts an angle expressed in degrees to radians.
```
var r = deg_to_rad(180) # r is 3.141593
```
floatease(x:float, curve:float)🔗
Returns an "eased" value ofxbased on an easing function defined withcurve. This easing function is based on an exponent. Thecurvecan be any floating-point number, with specific values leading to the following behaviors:
```
- Lower than -1.0 (exclusive): Ease in-out
- -1.0: Linear
- Between -1.0 and 0.0 (exclusive): Ease out-in
- 0.0: Constant
- Between 0.0 to 1.0 (exclusive): Ease out
- 1.0: Linear
- Greater than 1.0 (exclusive): Ease in
```
ease() curve values cheatsheet
See alsosmoothstep(). If you need to perform more advanced transitions, useTween.interpolate_value().
Stringerror_string(error:int)🔗
Returns a human-readable name for the givenErrorcode.
```
print(OK)                              # Prints 0
print(error_string(OK))                # Prints "OK"
print(error_string(ERR_BUSY))          # Prints "Busy"
print(error_string(ERR_OUT_OF_MEMORY)) # Prints "Out of memory"
```
floatexp(x:float)🔗
The natural exponential function. It raises the mathematical constanteto the power ofxand returns it.
ehas an approximate value of 2.71828, and can be obtained withexp(1).
For exponents to other bases use the methodpow().
```
var a = exp(2) # Approximately 7.39
```
Variantfloor(x:Variant)🔗
Roundsxdownward (towards negative infinity), returning the largest whole number that is not more thanx. Supported types:int,float,Vector2,Vector2i,Vector3,Vector3i,Vector4,Vector4i.
```
var a = floor(2.99) # a is 2.0
a = floor(-2.99)    # a is -3.0
```
See alsoceil(),round(), andsnapped().
Note:For better type safety, usefloorf(),floori(),Vector2.floor(),Vector3.floor(), orVector4.floor().
floatfloorf(x:float)🔗
Roundsxdownward (towards negative infinity), returning the largest whole number that is not more thanx.
A type-safe version offloor(), returning afloat.
intfloori(x:float)🔗
Roundsxdownward (towards negative infinity), returning the largest whole number that is not more thanx.
A type-safe version offloor(), returning anint.
Note:This function isnotthe same asint(x), which rounds towards 0.
floatfmod(x:float, y:float)🔗
Returns the floating-point remainder ofxdivided byy, keeping the sign ofx.
```
var remainder = fmod(7, 5.5) # remainder is 1.5
```
For the integer remainder operation, use the%operator.
floatfposmod(x:float, y:float)🔗
Returns the floating-point modulus ofxdivided byy, wrapping equally in positive and negative.
```
print(" (x)  (fmod(x, 1.5))   (fposmod(x, 1.5))")
for i in 7:
    var x = i * 0.5 - 1.5
    print("%4.1f           %4.1f  | %4.1f" % [x, fmod(x, 1.5), fposmod(x, 1.5)])
```
Prints:
```
 (x)  (fmod(x, 1.5))   (fposmod(x, 1.5))
-1.5           -0.0  |  0.0
-1.0           -1.0  |  0.5
-0.5           -0.5  |  1.0
 0.0            0.0  |  0.0
 0.5            0.5  |  0.5
 1.0            1.0  |  1.0
 1.5            0.0  |  0.0
```
inthash(variable:Variant)🔗
Returns the integer hash of the passedvariable.
```
print(hash("a")) # Prints 177670
```
```
GD.Print(GD.Hash("a")); // Prints 177670
```
Objectinstance_from_id(instance_id:int)🔗
Returns theObjectthat corresponds toinstance_id. All Objects have a unique instance ID. See alsoObject.get_instance_id().
```
var drink = "water"

func _ready():
    var id = get_instance_id()
    var instance = instance_from_id(id)
    print(instance.drink) # Prints "water"
```
```
public partial class MyNode : Node
{
    public string Drink { get; set; } = "water";

    public override void _Ready()
    {
        ulong id = GetInstanceId();
        var instance = (MyNode)InstanceFromId(Id);
        GD.Print(instance.Drink); // Prints "water"
    }
}
```
floatinverse_lerp(from:float, to:float, weight:float)🔗
Returns an interpolation or extrapolation factor considering the range specified infromandto, and the interpolated value specified inweight. The returned value will be between0.0and1.0ifweightis betweenfromandto(inclusive). Ifweightis located outside this range, then an extrapolation factor will be returned (return value lower than0.0or greater than1.0). Useclamp()on the result ofinverse_lerp()if this is not desired.
```
# The interpolation ratio in the `lerp()` call below is 0.75.
var middle = lerp(20, 30, 0.75)
# middle is now 27.5.

# Now, we pretend to have forgotten the original ratio and want to get it back.
var ratio = inverse_lerp(20, 30, 27.5)
# ratio is now 0.75.
```
See alsolerp(), which performs the reverse of this operation, andremap()to map a continuous series of values to another.
boolis_equal_approx(a:float, b:float)🔗
Returnstrueifaandbare approximately equal to each other.
Here, "approximately equal" means thataandbare within a small internal epsilon of each other, which scales with the magnitude of the numbers.
Infinity values of the same sign are considered equal.
boolis_finite(x:float)🔗
Returns whetherxis a finite value, i.e. it is not@GDScript.NAN, positive infinity, or negative infinity. See alsois_inf()andis_nan().
boolis_inf(x:float)🔗
Returnstrueifxis either positive infinity or negative infinity. See alsois_finite()andis_nan().
boolis_instance_id_valid(id:int)🔗
Returnstrueif the Object that corresponds toidis a valid object (e.g. has not been deleted from memory). All Objects have a unique instance ID.
boolis_instance_valid(instance:Variant)🔗
Returnstrueifinstanceis a valid Object (e.g. has not been deleted from memory).
boolis_nan(x:float)🔗
Returnstrueifxis a NaN ("Not a Number" or invalid) value. This method is needed as@GDScript.NANis not equal to itself, which meansx==NANcan't be used to check whether a value is a NaN.
boolis_same(a:Variant, b:Variant)🔗
Returnstrue, for value types, ifaandbshare the same value. Returnstrue, for reference types, if the references ofaandbare the same.
```
# Vector2 is a value type
var vec2_a = Vector2(0, 0)
var vec2_b = Vector2(0, 0)
var vec2_c = Vector2(1, 1)
is_same(vec2_a, vec2_a)  # true
is_same(vec2_a, vec2_b)  # true
is_same(vec2_a, vec2_c)  # false

# Array is a reference type
var arr_a = []
var arr_b = []
is_same(arr_a, arr_a)  # true
is_same(arr_a, arr_b)  # false
```
These areVariantvalue types:null,bool,int,float,String,StringName,Vector2,Vector2i,Vector3,Vector3i,Vector4,Vector4i,Rect2,Rect2i,Transform2D,Transform3D,Plane,Quaternion,AABB,Basis,Projection,Color,NodePath,RID,CallableandSignal.
These areVariantreference types:Object,Dictionary,Array,PackedByteArray,PackedInt32Array,PackedInt64Array,PackedFloat32Array,PackedFloat64Array,PackedStringArray,PackedVector2Array,PackedVector3Array,PackedVector4Array, andPackedColorArray.
boolis_zero_approx(x:float)🔗
Returnstrueifxis zero or almost zero. The comparison is done using a tolerance calculation with a small internal epsilon.
This function is faster than usingis_equal_approx()with one value as zero.
Variantlerp(from:Variant, to:Variant, weight:Variant)🔗
Linearly interpolates between two values by the factor defined inweight. To perform interpolation,weightshould be between0.0and1.0(inclusive). However, values outside this range are allowed and can be used to performextrapolation. If this is not desired, useclampf()to limitweight.
Bothfromandtomust be the same type. Supported types:int,float,Vector2,Vector3,Vector4,Color,Quaternion,Basis,Transform2D,Transform3D.
```
lerp(0, 4, 0.75) # Returns 3.0
```
See alsoinverse_lerp()which performs the reverse of this operation. To perform eased interpolation withlerp(), combine it withease()orsmoothstep(). See alsoremap()to map a continuous series of values to another.
Note:For better type safety, uselerpf(),Vector2.lerp(),Vector3.lerp(),Vector4.lerp(),Color.lerp(),Quaternion.slerp(),Basis.slerp(),Transform2D.interpolate_with(), orTransform3D.interpolate_with().
floatlerp_angle(from:float, to:float, weight:float)🔗
Linearly interpolates between two angles (in radians) by aweightvalue between 0.0 and 1.0.
Similar tolerp(), but interpolates correctly when the angles wrap around@GDScript.TAU. To perform eased interpolation withlerp_angle(), combine it withease()orsmoothstep().
```
extends Sprite
var elapsed = 0.0
func _process(delta):
    var min_angle = deg_to_rad(0.0)
    var max_angle = deg_to_rad(90.0)
    rotation = lerp_angle(min_angle, max_angle, elapsed)
    elapsed += delta
```
Note:This function lerps through the shortest path betweenfromandto. However, when these two angles are approximatelyPI+k*TAUapart for any integerk, it's not obvious which way they lerp due to floating-point precision errors. For example,lerp_angle(0,PI,weight)lerps counter-clockwise, whilelerp_angle(0,PI+5*TAU,weight)lerps clockwise.
floatlerpf(from:float, to:float, weight:float)🔗
Linearly interpolates between two values by the factor defined inweight. To perform interpolation,weightshould be between0.0and1.0(inclusive). However, values outside this range are allowed and can be used to performextrapolation. If this is not desired, useclampf()on the result of this function.
```
lerpf(0, 4, 0.75) # Returns 3.0
```
See alsoinverse_lerp()which performs the reverse of this operation. To perform eased interpolation withlerp(), combine it withease()orsmoothstep().
floatlinear_to_db(lin:float)🔗
Converts from linear energy to decibels (audio). Since volume is not normally linear, this can be used to implement volume sliders that behave as expected.
Example:Change the Master bus's volume through aSlidernode, which ranges from0.0to1.0:
```
AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Master"), linear_to_db($Slider.value))
```
floatlog(x:float)🔗
Returns thenatural logarithmofx(base[i]e[/i], withebeing approximately 2.71828). This is the amount of time needed to reach a certain level of continuous growth.
Note:This is not the same as the "log" function on most calculators, which uses a base 10 logarithm. To use base 10 logarithm, uselog(x)/log(10).
```
log(10) # Returns 2.302585
```
Note:The logarithm of0returns-inf, while negative values return-nan.
Variantmax(...)vararg🔗
Returns the maximum of the given numeric values. This function can take any number of arguments.
```
max(1, 7, 3, -6, 5) # Returns 7
```
Note:When using this on vectors it willnotperform component-wise maximum, and will pick the largest value when compared usingx<y. To perform component-wise maximum, useVector2.max(),Vector2i.max(),Vector3.max(),Vector3i.max(),Vector4.max(), andVector4i.max().
floatmaxf(a:float, b:float)🔗
Returns the maximum of twofloatvalues.
```
maxf(3.6, 24)   # Returns 24.0
maxf(-3.99, -4) # Returns -3.99
```
intmaxi(a:int, b:int)🔗
Returns the maximum of twointvalues.
```
maxi(1, 2)   # Returns 2
maxi(-3, -4) # Returns -3
```
Variantmin(...)vararg🔗
Returns the minimum of the given numeric values. This function can take any number of arguments.
```
min(1, 7, 3, -6, 5) # Returns -6
```
Note:When using this on vectors it willnotperform component-wise minimum, and will pick the smallest value when compared usingx<y. To perform component-wise minimum, useVector2.min(),Vector2i.min(),Vector3.min(),Vector3i.min(),Vector4.min(), andVector4i.min().
floatminf(a:float, b:float)🔗
Returns the minimum of twofloatvalues.
```
minf(3.6, 24)   # Returns 3.6
minf(-3.99, -4) # Returns -4.0
```
intmini(a:int, b:int)🔗
Returns the minimum of twointvalues.
```
mini(1, 2)   # Returns 1
mini(-3, -4) # Returns -4
```
floatmove_toward(from:float, to:float, delta:float)🔗
Movesfromtowardtoby thedeltaamount. Will not go pastto.
Use a negativedeltavalue to move away.
```
move_toward(5, 10, 4)    # Returns 9
move_toward(10, 5, 4)    # Returns 6
move_toward(5, 10, 9)    # Returns 10
move_toward(10, 5, -1.5) # Returns 11.5
```
intnearest_po2(value:int)🔗
Returns the smallest integer power of 2 that is greater than or equal tovalue.
```
nearest_po2(3) # Returns 4
nearest_po2(4) # Returns 4
nearest_po2(5) # Returns 8

nearest_po2(0)  # Returns 0 (this may not be expected)
nearest_po2(-1) # Returns 0 (this may not be expected)
```
Warning:Due to its implementation, this method returns0rather than1for values less than or equal to0, with an exception forvaluebeing the smallest negative 64-bit integer (-9223372036854775808) in which case thevalueis returned unchanged.
floatpingpong(value:float, length:float)🔗
Wrapsvaluebetween0and thelength. If the limit is reached, the next value the function returns is decreased to the0side or increased to thelengthside (like a triangle wave). Iflengthis less than zero, it becomes positive.
```
pingpong(-3.0, 3.0) # Returns 3.0
pingpong(-2.0, 3.0) # Returns 2.0
pingpong(-1.0, 3.0) # Returns 1.0
pingpong(0.0, 3.0)  # Returns 0.0
pingpong(1.0, 3.0)  # Returns 1.0
pingpong(2.0, 3.0)  # Returns 2.0
pingpong(3.0, 3.0)  # Returns 3.0
pingpong(4.0, 3.0)  # Returns 2.0
pingpong(5.0, 3.0)  # Returns 1.0
pingpong(6.0, 3.0)  # Returns 0.0
```
intposmod(x:int, y:int)🔗
Returns the integer modulus ofxdivided byythat wraps equally in positive and negative.
```
print("#(i)  (i % 3)   (posmod(i, 3))")
for i in range(-3, 4):
    print("%2d       %2d  | %2d" % [i, i % 3, posmod(i, 3)])
```
Prints:
```
(i)  (i % 3)   (posmod(i, 3))
-3        0  |  0
-2       -2  |  1
-1       -1  |  2
 0        0  |  0
 1        1  |  1
 2        2  |  2
 3        0  |  0
```
floatpow(base:float, exp:float)🔗
Returns the result ofbaseraised to the power ofexp.
In GDScript, this is the equivalent of the**operator.
```
pow(2, 5)   # Returns 32.0
pow(4, 1.5) # Returns 8.0
```
voidprint(...)vararg🔗
Converts one or more arguments of any type to string in the best way possible and prints them to the console.
```
var a = [1, 2, 3]
print("a", "b", a) # Prints "ab[1, 2, 3]"
```
```
Godot.Collections.Array a = [1, 2, 3];
GD.Print("a", "b", a); // Prints "ab[1, 2, 3]"
```
Note:Consider usingpush_error()andpush_warning()to print error and warning messages instead ofprint()orprint_rich(). This distinguishes them from print messages used for debugging purposes, while also displaying a stack trace when an error or warning is printed. See alsoEngine.print_to_stdoutandProjectSettings.application/run/disable_stdout.
voidprint_rich(...)vararg🔗
Converts one or more arguments of any type to string in the best way possible and prints them to the console.
The following BBCode tags are supported:b,i,u,s,indent,code,url,center,right,color,bgcolor,fgcolor.
URL tags only support URLs wrapped by a URL tag, not URLs with a different title.
When printing to standard output, the supported subset of BBCode is converted to ANSI escape codes for the terminal emulator to display. Support for ANSI escape codes varies across terminal emulators, especially for italic and strikethrough. In standard output,codeis represented with faint text but without any font change. Unsupported tags are left as-is in standard output.
```
print_rich("[color=green][b]Hello world![/b][/color]") # Prints "Hello world!", in green with a bold font.
```
```
GD.PrintRich("[color=green][b]Hello world![/b][/color]"); // Prints "Hello world!", in green with a bold font.
```
Note:Consider usingpush_error()andpush_warning()to print error and warning messages instead ofprint()orprint_rich(). This distinguishes them from print messages used for debugging purposes, while also displaying a stack trace when an error or warning is printed.
Note:Output displayed in the editor supports clickable[url=address]text[/url]tags. The[url]tag'saddressvalue is handled byOS.shell_open()when clicked.
voidprint_verbose(...)vararg🔗
If verbose mode is enabled (OS.is_stdout_verbose()returningtrue), converts one or more arguments of any type to string in the best way possible and prints them to the console.
voidprinterr(...)vararg🔗
Prints one or more arguments to strings in the best way possible to standard error line.
```
printerr("prints to stderr")
```
```
GD.PrintErr("prints to stderr");
```
voidprintraw(...)vararg🔗
Prints one or more arguments to strings in the best way possible to the OS terminal. Unlikeprint(), no newline is automatically added at the end.
Note:The OS terminal isnotthe same as the editor's Output dock. The output sent to the OS terminal can be seen when running Godot from a terminal. On Windows, this requires using theconsole.exeexecutable.
```
# Prints "ABC" to terminal.
printraw("A")
printraw("B")
printraw("C")
```
```
// Prints "ABC" to terminal.
GD.PrintRaw("A");
GD.PrintRaw("B");
GD.PrintRaw("C");
```
voidprints(...)vararg🔗
Prints one or more arguments to the console with a space between each argument.
```
prints("A", "B", "C") # Prints "A B C"
```
```
GD.PrintS("A", "B", "C"); // Prints "A B C"
```
voidprintt(...)vararg🔗
Prints one or more arguments to the console with a tab between each argument.
```
printt("A", "B", "C") # Prints "A       B       C"
```
```
GD.PrintT("A", "B", "C"); // Prints "A       B       C"
```
voidpush_error(...)vararg🔗
Pushes an error message to Godot's built-in debugger and to the OS terminal.
```
push_error("test error") # Prints "test error" to debugger and terminal as an error.
```
```
GD.PushError("test error"); // Prints "test error" to debugger and terminal as an error.
```
Note:This function does not pause project execution. To print an error message and pause project execution in debug builds, useassert(false,"testerror")instead.
voidpush_warning(...)vararg🔗
Pushes a warning message to Godot's built-in debugger and to the OS terminal.
```
push_warning("test warning") # Prints "test warning" to debugger and terminal as a warning.
```
```
GD.PushWarning("test warning"); // Prints "test warning" to debugger and terminal as a warning.
```
floatrad_to_deg(rad:float)🔗
Converts an angle expressed in radians to degrees.
```
rad_to_deg(0.523599) # Returns 30
rad_to_deg(PI)       # Returns 180
rad_to_deg(PI * 2)   # Returns 360
```
PackedInt64Arrayrand_from_seed(seed:int)🔗
Given aseed, returns aPackedInt64Arrayof size2, where its first element is the randomizedintvalue, and the second element is the same asseed. Passing the sameseedconsistently returns the same array.
Note:"Seed" here refers to the internal state of the pseudo random number generator, currently implemented as a 64 bit integer.
```
var a = rand_from_seed(4)

print(a[0]) # Prints 2879024997
print(a[1]) # Prints 4
```
floatrandf()🔗
Returns a random floating-point value between0.0and1.0(inclusive).
```
randf() # Returns e.g. 0.375671
```
```
GD.Randf(); // Returns e.g. 0.375671
```
floatrandf_range(from:float, to:float)🔗
Returns a random floating-point value betweenfromandto(inclusive).
```
randf_range(0, 20.5) # Returns e.g. 7.45315
randf_range(-10, 10) # Returns e.g. -3.844535
```
```
GD.RandRange(0.0, 20.5);   // Returns e.g. 7.45315
GD.RandRange(-10.0, 10.0); // Returns e.g. -3.844535
```
floatrandfn(mean:float, deviation:float)🔗
Returns anormally-distributed, pseudo-random floating-point value from the specifiedmeanand a standarddeviation. This is also known as a Gaussian distribution.
Note:This method uses theBox-Muller transformalgorithm.
intrandi()🔗
Returns a random unsigned 32-bit integer. Use remainder to obtain a random value in the interval[0,N-1](where N is smaller than 2^32).
```
randi()           # Returns random integer between 0 and 2^32 - 1
randi() % 20      # Returns random integer between 0 and 19
randi() % 100     # Returns random integer between 0 and 99
randi() % 100 + 1 # Returns random integer between 1 and 100
```
```
GD.Randi();           // Returns random integer between 0 and 2^32 - 1
GD.Randi() % 20;      // Returns random integer between 0 and 19
GD.Randi() % 100;     // Returns random integer between 0 and 99
GD.Randi() % 100 + 1; // Returns random integer between 1 and 100
```
intrandi_range(from:int, to:int)🔗
Returns a random signed 32-bit integer betweenfromandto(inclusive). Iftois lesser thanfrom, they are swapped.
```
randi_range(0, 1)      # Returns either 0 or 1
randi_range(-10, 1000) # Returns random integer between -10 and 1000
```
```
GD.RandRange(0, 1);      // Returns either 0 or 1
GD.RandRange(-10, 1000); // Returns random integer between -10 and 1000
```
voidrandomize()🔗
Randomizes the seed (or the internal state) of the random number generator. The current implementation uses a number based on the device's time.
Note:This function is called automatically when the project is run. If you need to fix the seed to have consistent, reproducible results, useseed()to initialize the random number generator.
floatremap(value:float, istart:float, istop:float, ostart:float, ostop:float)🔗
Maps avaluefrom range[istart,istop]to[ostart,ostop]. See alsolerp()andinverse_lerp(). Ifvalueis outside[istart,istop], then the resulting value will also be outside[ostart,ostop]. If this is not desired, useclamp()on the result of this function.
```
remap(75, 0, 100, -1, 1) # Returns 0.5
```
For complex use cases where multiple ranges are needed, consider usingCurveorGradientinstead.
Note:Ifistart==istop, the return value is undefined (most likely NaN, INF, or -INF).
intrid_allocate_id()🔗
Allocates a unique ID which can be used by the implementation to construct an RID. This is used mainly from native extensions to implement servers.
RIDrid_from_int64(base:int)🔗
Creates an RID from abase. This is used mainly from native extensions to build servers.
floatrotate_toward(from:float, to:float, delta:float)🔗
Rotatesfromtowardtoby thedeltaamount. Will not go pastto.
Similar tomove_toward(), but interpolates correctly when the angles wrap around@GDScript.TAU.
Ifdeltais negative, this function will rotate away fromto, toward the opposite angle, and will not go past the opposite angle.
Variantround(x:Variant)🔗
Roundsxto the nearest whole number, with halfway cases rounded away from 0. Supported types:int,float,Vector2,Vector2i,Vector3,Vector3i,Vector4,Vector4i.
```
round(2.4) # Returns 2
round(2.5) # Returns 3
round(2.6) # Returns 3
```
See alsofloor(),ceil(), andsnapped().
Note:For better type safety, useroundf(),roundi(),Vector2.round(),Vector3.round(), orVector4.round().
floatroundf(x:float)🔗
Roundsxto the nearest whole number, with halfway cases rounded away from 0.
A type-safe version ofround(), returning afloat.
introundi(x:float)🔗
Roundsxto the nearest whole number, with halfway cases rounded away from 0.
A type-safe version ofround(), returning anint.
voidseed(base:int)🔗
Sets the seed for the random number generator tobase. Setting the seed manually can ensure consistent, repeatable results for most random functions.
```
var my_seed = "Godot Rocks".hash()
seed(my_seed)
var a = randf() + randi()
seed(my_seed)
var b = randf() + randi()
# a and b are now identical
```
```
ulong mySeed = (ulong)GD.Hash("Godot Rocks");
GD.Seed(mySeed);
var a = GD.Randf() + GD.Randi();
GD.Seed(mySeed);
var b = GD.Randf() + GD.Randi();
// a and b are now identical
```
Variantsign(x:Variant)🔗
Returns the same type ofVariantasx, with-1for negative values,1for positive values, and0for zeros. Fornanvalues it returns 0.
Supported types:int,float,Vector2,Vector2i,Vector3,Vector3i,Vector4,Vector4i.
```
sign(-6.0) # Returns -1
sign(0.0)  # Returns 0
sign(6.0)  # Returns 1
sign(NAN)  # Returns 0

sign(Vector3(-6.0, 0.0, 6.0)) # Returns (-1, 0, 1)
```
Note:For better type safety, usesignf(),signi(),Vector2.sign(),Vector2i.sign(),Vector3.sign(),Vector3i.sign(),Vector4.sign(), orVector4i.sign().
floatsignf(x:float)🔗
Returns-1.0ifxis negative,1.0ifxis positive, and0.0ifxis zero. Fornanvalues ofxit returns 0.0.
```
signf(-6.5) # Returns -1.0
signf(0.0)  # Returns 0.0
signf(6.5)  # Returns 1.0
signf(NAN)  # Returns 0.0
```
intsigni(x:int)🔗
Returns-1ifxis negative,1ifxis positive, and0ifxis zero.
```
signi(-6) # Returns -1
signi(0)  # Returns 0
signi(6)  # Returns 1
```
floatsin(angle_rad:float)🔗
Returns the sine of angleangle_radin radians.
```
sin(0.523599)       # Returns 0.5
sin(deg_to_rad(90)) # Returns 1.0
```
floatsinh(x:float)🔗
Returns the hyperbolic sine ofx.
```
var a = log(2.0) # Returns 0.693147
sinh(a) # Returns 0.75
```
floatsmoothstep(from:float, to:float, x:float)🔗
Returns a smooth cubic Hermite interpolation between0and1.
For positive ranges (whenfrom<=to) the return value is0whenx<=from, and1whenx>=to. Ifxlies betweenfromandto, the return value follows an S-shaped curve that smoothly transitions from0to1.
For negative ranges (whenfrom>to) the function is mirrored and returns1whenx<=toand0whenx>=from.
This S-shaped curve is the cubic Hermite interpolator, given byf(y)=3*y^2-2*y^3wherey=(x-from)/(to-from).
```
smoothstep(0, 2, -5.0) # Returns 0.0
smoothstep(0, 2, 0.5) # Returns 0.15625
smoothstep(0, 2, 1.0) # Returns 0.5
smoothstep(0, 2, 2.0) # Returns 1.0
```
Compared toease()with a curve value of-1.6521,smoothstep()returns the smoothest possible curve with no sudden changes in the derivative. If you need to perform more advanced transitions, useTweenorAnimationPlayer.
Comparison between smoothstep() and ease(x, -1.6521) return values
Smoothstep() return values with positive, zero, and negative ranges
Variantsnapped(x:Variant, step:Variant)🔗
Returns the multiple ofstepthat is the closest tox. This can also be used to round a floating-point number to an arbitrary number of decimals.
The returned value is the same type ofVariantasstep. Supported types:int,float,Vector2,Vector2i,Vector3,Vector3i,Vector4,Vector4i.
```
snapped(100, 32)  # Returns 96
snapped(3.14159, 0.01)  # Returns 3.14

snapped(Vector2(34, 70), Vector2(8, 8))  # Returns (32, 72)
```
See alsoceil(),floor(), andround().
Note:For better type safety, usesnappedf(),snappedi(),Vector2.snapped(),Vector2i.snapped(),Vector3.snapped(),Vector3i.snapped(),Vector4.snapped(), orVector4i.snapped().
floatsnappedf(x:float, step:float)🔗
Returns the multiple ofstepthat is the closest tox. This can also be used to round a floating-point number to an arbitrary number of decimals.
A type-safe version ofsnapped(), returning afloat.
```
snappedf(32.0, 2.5)  # Returns 32.5
snappedf(3.14159, 0.01)  # Returns 3.14
```
intsnappedi(x:float, step:int)🔗
Returns the multiple ofstepthat is the closest tox.
A type-safe version ofsnapped(), returning anint.
```
snappedi(53, 16)  # Returns 48
snappedi(4096, 100)  # Returns 4100
```
floatsqrt(x:float)🔗
Returns the square root ofx, wherexis a non-negative number.
```
sqrt(9)     # Returns 3
sqrt(10.24) # Returns 3.2
sqrt(-1)    # Returns NaN
```
Note:Negative values ofxreturn NaN ("Not a Number"). In C#, if you need negative inputs, useSystem.Numerics.Complex.
intstep_decimals(x:float)🔗
Returns the position of the first non-zero digit, after the decimal point. Note that the maximum return value is 10, which is a design decision in the implementation.
```
var n = step_decimals(5)       # n is 0
n = step_decimals(1.0005)      # n is 4
n = step_decimals(0.000000005) # n is 9
```
Stringstr(...)vararg🔗
Converts one or more arguments of anyVarianttype to aStringin the best way possible.
```
var a = [10, 20, 30]
var b = str(a)
print(len(a)) # Prints 3 (the number of elements in the array).
print(len(b)) # Prints 12 (the length of the string "[10, 20, 30]").
```
Variantstr_to_var(string:String)🔗
Converts a formattedstringthat was returned byvar_to_str()to the originalVariant.
```
var data = '{ "a": 1, "b": 2 }' # data is a String
var dict = str_to_var(data)     # dict is a Dictionary
print(dict["a"])                # Prints 1
```
```
string data = "{ \"a\": 1, \"b\": 2 }";           // data is a string
var dict = GD.StrToVar(data).AsGodotDictionary(); // dict is a Dictionary
GD.Print(dict["a"]);                              // Prints 1
```
floattan(angle_rad:float)🔗
Returns the tangent of angleangle_radin radians.
```
tan(deg_to_rad(45)) # Returns 1
```
floattanh(x:float)🔗
Returns the hyperbolic tangent ofx.
```
var a = log(2.0) # Returns 0.693147
tanh(a)          # Returns 0.6
```
Varianttype_convert(variant:Variant, type:int)🔗
Converts the givenvariantto the giventype, using theVariant.Typevalues. This method is generous with how it handles types, it can automatically convert between array types, convert numericStrings toint, and converting most things toString.
If the type conversion cannot be done, this method will return the default value for that type, for example convertingRect2toVector2will always returnVector2.ZERO. This method will never show error messages as long astypeis a valid Variant type.
The returned value is aVariant, but the data inside and its type will be the same as the requested type.
```
type_convert("Hi!", TYPE_INT) # Returns 0
type_convert("123", TYPE_INT) # Returns 123
type_convert(123.4, TYPE_INT) # Returns 123
type_convert(5, TYPE_VECTOR2) # Returns (0, 0)
type_convert("Hi!", TYPE_NIL) # Returns null
```
Stringtype_string(type:int)🔗
Returns a human-readable name of the giventype, using theVariant.Typevalues.
```
print(TYPE_INT) # Prints 2
print(type_string(TYPE_INT)) # Prints "int"
print(type_string(TYPE_STRING)) # Prints "String"
```
See alsotypeof().
inttypeof(variable:Variant)🔗
Returns the internal type of the givenvariable, using theVariant.Typevalues.
```
var json = JSON.new()
json.parse('["a", "b", "c"]')
var result = json.get_data()
if typeof(result) == TYPE_ARRAY:
    print(result[0]) # Prints "a"
else:
    print("Unexpected result!")
```
See alsotype_string().
PackedByteArrayvar_to_bytes(variable:Variant)🔗
Encodes aVariantvalue to a byte array, without encoding objects. Deserialization can be done withbytes_to_var().
Note:If you need object serialization, seevar_to_bytes_with_objects().
Note:EncodingCallableis not supported and will result in an empty value, regardless of the data.
PackedByteArrayvar_to_bytes_with_objects(variable:Variant)🔗
Encodes aVariantvalue to a byte array. Encoding objects is allowed (and can potentially include executable code). Deserialization can be done withbytes_to_var_with_objects().
Note:EncodingCallableis not supported and will result in an empty value, regardless of the data.
Stringvar_to_str(variable:Variant)🔗
Converts aVariantvariableto a formattedStringthat can then be parsed usingstr_to_var().
```
var a = { "a": 1, "b": 2 }
print(var_to_str(a))
```
```
var a = new Godot.Collections.Dictionary { ["a"] = 1, ["b"] = 2 };
GD.Print(GD.VarToStr(a));
```
Prints:
```
{
    "a": 1,
    "b": 2
}
```
Note:ConvertingSignalorCallableis not supported and will result in an empty value for these types, regardless of their data.
Variantweakref(obj:Variant)🔗
Returns aWeakRefinstance holding a weak reference toobj. Returns an emptyWeakRefinstance ifobjisnull. Prints an error and returnsnullifobjis neitherObject-derived nornull.
A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else. However, until the object is actually destroyed the weak reference may return the object even if there are no strong references to it.
Variantwrap(value:Variant, min:Variant, max:Variant)🔗
Wraps theVariantvaluebetweenminandmax.minisinclusivewhilemaxisexclusive. This can be used for creating loop-like behavior or infinite surfaces.
Variant typesintandfloatare supported. If any of the arguments isfloat, this function returns afloat, otherwise it returns anint.
```
var a = wrap(4, 5, 10)
# a is 9 (int)

var a = wrap(7, 5, 10)
# a is 7 (int)

var a = wrap(10.5, 5, 10)
# a is 5.5 (float)
```
floatwrapf(value:float, min:float, max:float)🔗
Wraps the floatvaluebetweenminandmax.minisinclusivewhilemaxisexclusive. This can be used for creating loop-like behavior or infinite surfaces.
```
# Infinite loop between 5.0 and 9.9
value = wrapf(value + 0.1, 5.0, 10.0)
```
```
# Infinite rotation (in radians)
angle = wrapf(angle + 0.1, 0.0, TAU)
```
```
# Infinite rotation (in radians)
angle = wrapf(angle + 0.1, -PI, PI)
```
Note:Ifminis0, this is equivalent tofposmod(), so prefer using that instead.wrapf()is more flexible than using thefposmod()approach by giving the user control over the minimum value.
intwrapi(value:int, min:int, max:int)🔗
Wraps the integervaluebetweenminandmax.minisinclusivewhilemaxisexclusive. This can be used for creating loop-like behavior or infinite surfaces.
```
# Infinite loop between 5 and 9
frame = wrapi(frame + 1, 5, 10)
```
```
# result is -2
var result = wrapi(-6, -5, -1)
```

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.