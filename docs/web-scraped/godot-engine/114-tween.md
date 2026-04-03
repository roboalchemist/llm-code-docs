# Tween

# Tween

Inherits:RefCounted<Object
Lightweight object used for general-purpose animation via script, usingTweeners.

## Description

Tweens are mostly useful for animations requiring a numerical property to be interpolated over a range of values. The nametweencomes fromin-betweening, an animation technique where you specifykeyframesand the computer interpolates the frames that appear between them. Animating something with aTweenis called tweening.
Tweenis more suited thanAnimationPlayerfor animations where you don't know the final values in advance. For example, interpolating a dynamically-chosen camera zoom value is best done with aTween; it would be difficult to do the same thing with anAnimationPlayernode. Tweens are also more light-weight thanAnimationPlayer, so they are very much suited for simple animations or general tasks that don't require visual tweaking provided by the editor. They can be used in a "fire-and-forget" manner for some logic that normally would be done by code. You can e.g. make something shoot periodically by using a loopedCallbackTweenerwith a delay.
ATweencan be created by using eitherSceneTree.create_tween()orNode.create_tween().Tweens created manually (i.e. by usingTween.new()) are invalid and can't be used for tweening values.
A tween animation is created by addingTweeners to theTweenobject, usingtween_property(),tween_interval(),tween_callback()ortween_method():

```
var tween = get_tree().create_tween()
tween.tween_property($Sprite, "modulate", Color.RED, 1.0)
tween.tween_property($Sprite, "scale", Vector2(), 1.0)
tween.tween_callback($Sprite.queue_free)
```

```
Tween tween = GetTree().CreateTween();
tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f);
tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f);
tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));
```

This sequence will make the$Spritenode turn red, then shrink, before finally callingNode.queue_free()to free the sprite.Tweeners are executed one after another by default. This behavior can be changed usingparallel()andset_parallel().
When aTweeneris created with one of thetween_*methods, a chained method call can be used to tweak the properties of thisTweener. For example, if you want to set a different transition type in the above example, you can useset_trans():

```
var tween = get_tree().create_tween()
tween.tween_property($Sprite, "modulate", Color.RED, 1.0).set_trans(Tween.TRANS_SINE)
tween.tween_property($Sprite, "scale", Vector2(), 1.0).set_trans(Tween.TRANS_BOUNCE)
tween.tween_callback($Sprite.queue_free)
```

```
Tween tween = GetTree().CreateTween();
tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f).SetTrans(Tween.TransitionType.Sine);
tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f).SetTrans(Tween.TransitionType.Bounce);
tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));
```

Most of theTweenmethods can be chained this way too. In the following example theTweenis bound to the running script's node and a default transition is set for itsTweeners:

```
var tween = get_tree().create_tween().bind_node(self).set_trans(Tween.TRANS_ELASTIC)
tween.tween_property($Sprite, "modulate", Color.RED, 1.0)
tween.tween_property($Sprite, "scale", Vector2(), 1.0)
tween.tween_callback($Sprite.queue_free)
```

```
var tween = GetTree().CreateTween().BindNode(this).SetTrans(Tween.TransitionType.Elastic);
tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f);
tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f);
tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));
```

Another interesting use forTweens is animating arbitrary sets of objects:

```
var tween = create_tween()
for sprite in get_children():
    tween.tween_property(sprite, "position", Vector2(0, 0), 1.0)
```

```
Tween tween = CreateTween();
foreach (Node sprite in GetChildren())
    tween.TweenProperty(sprite, "position", Vector2.Zero, 1.0f);
```

In the example above, all children of a node are moved one after another to position(0,0).
You should avoid using more than oneTweenper object's property. If two or more tweens animate one property at the same time, the last one created will take priority and assign the final value. If you want to interrupt and restart an animation, consider assigning theTweento a variable:

```
var tween
func animate():
    if tween:
        tween.kill() # Abort the previous animation.
    tween = create_tween()
```

```
private Tween _tween;

public void Animate()
{
    if (_tween != null)
        _tween.Kill(); // Abort the previous animation
    _tween = CreateTween();
}
```

SomeTweeners use transitions and eases. The first accepts aTransitionTypeconstant, and refers to the way the timing of the animation is handled (seeeasings.netfor some examples). The second accepts anEaseTypeconstant, and controls where thetrans_typeis applied to the interpolation (in the beginning, the end, or both). If you don't know which transition and easing to pick, you can try differentTransitionTypeconstants withEASE_IN_OUT, and use the one that looks best.
Tween easing and transition types cheatsheet
Note:Tweens are not designed to be reused and trying to do so results in an undefined behavior. Create a new Tween for each animation and every time you replay an animation from start. Keep in mind that Tweens start immediately, so only create a Tween when you want to start animating.
Note:The tween is processed after all of the nodes in the current frame, i.e. node'sNode._process()method would be called before the tween (orNode._physics_process()depending on the value passed toset_process_mode()).

## Methods

| Tween | bind_node(node:Node) |
|---|---|
| Tween | chain() |
| bool | custom_step(delta:float) |
| int | get_loops_left()const |
| float | get_total_elapsed_time()const |
| Variant | interpolate_value(initial_value:Variant, delta_value:Variant, elapsed_time:float, duration:float, trans_type:TransitionType, ease_type:EaseType)static |
| bool | is_running() |
| bool | is_valid() |
| void | kill() |
| Tween | parallel() |
| void | pause() |
| void | play() |
| Tween | set_ease(ease:EaseType) |
| Tween | set_ignore_time_scale(ignore:bool= true) |
| Tween | set_loops(loops:int= 0) |
| Tween | set_parallel(parallel:bool= true) |
| Tween | set_pause_mode(mode:TweenPauseMode) |
| Tween | set_process_mode(mode:TweenProcessMode) |
| Tween | set_speed_scale(speed:float) |
| Tween | set_trans(trans:TransitionType) |
| void | stop() |
| CallbackTweener | tween_callback(callback:Callable) |
| IntervalTweener | tween_interval(time:float) |
| MethodTweener | tween_method(method:Callable, from:Variant, to:Variant, duration:float) |
| PropertyTweener | tween_property(object:Object, property:NodePath, final_val:Variant, duration:float) |
| SubtweenTweener | tween_subtween(subtween:Tween) |

Tween
bind_node(node:Node)
Tween
chain()
bool
custom_step(delta:float)
get_loops_left()const
float
get_total_elapsed_time()const
Variant
interpolate_value(initial_value:Variant, delta_value:Variant, elapsed_time:float, duration:float, trans_type:TransitionType, ease_type:EaseType)static
bool
is_running()
bool
is_valid()
void
kill()
Tween
parallel()
void
pause()
void
play()
Tween
set_ease(ease:EaseType)
Tween
set_ignore_time_scale(ignore:bool= true)
Tween
set_loops(loops:int= 0)
Tween
set_parallel(parallel:bool= true)
Tween
set_pause_mode(mode:TweenPauseMode)
Tween
set_process_mode(mode:TweenProcessMode)
Tween
set_speed_scale(speed:float)
Tween
set_trans(trans:TransitionType)
void
stop()
CallbackTweener
tween_callback(callback:Callable)
IntervalTweener
tween_interval(time:float)
MethodTweener
tween_method(method:Callable, from:Variant, to:Variant, duration:float)
PropertyTweener
tween_property(object:Object, property:NodePath, final_val:Variant, duration:float)
SubtweenTweener
tween_subtween(subtween:Tween)

## Signals

finished()🔗
Emitted when theTweenhas finished all tweening. Never emitted when theTweenis set to infinite looping (seeset_loops()).
loop_finished(loop_count:int)🔗
Emitted when a full loop is complete (seeset_loops()), providing the loop index. This signal is not emitted after the final loop, usefinishedinstead for this case.
step_finished(idx:int)🔗
Emitted when one step of theTweenis complete, providing the step index. One step is either a singleTweeneror a group ofTweeners running in parallel.

## Enumerations

enumTweenProcessMode:🔗
TweenProcessModeTWEEN_PROCESS_PHYSICS=0
TheTweenupdates after each physics frame (seeNode._physics_process()).
TweenProcessModeTWEEN_PROCESS_IDLE=1
TheTweenupdates after each process frame (seeNode._process()).
enumTweenPauseMode:🔗
TweenPauseModeTWEEN_PAUSE_BOUND=0
If theTweenhas a bound node, it will process when that node can process (seeNode.process_mode). Otherwise it's the same asTWEEN_PAUSE_STOP.
TweenPauseModeTWEEN_PAUSE_STOP=1
IfSceneTreeis paused, theTweenwill also pause.
TweenPauseModeTWEEN_PAUSE_PROCESS=2
TheTweenwill process regardless of whetherSceneTreeis paused.
enumTransitionType:🔗
TransitionTypeTRANS_LINEAR=0
The animation is interpolated linearly.
TransitionTypeTRANS_SINE=1
The animation is interpolated using a sine function.
TransitionTypeTRANS_QUINT=2
The animation is interpolated with a quintic (to the power of 5) function.
TransitionTypeTRANS_QUART=3
The animation is interpolated with a quartic (to the power of 4) function.
TransitionTypeTRANS_QUAD=4
The animation is interpolated with a quadratic (to the power of 2) function.
TransitionTypeTRANS_EXPO=5
The animation is interpolated with an exponential (to the power of x) function.
TransitionTypeTRANS_ELASTIC=6
The animation is interpolated with elasticity, wiggling around the edges.
TransitionTypeTRANS_CUBIC=7
The animation is interpolated with a cubic (to the power of 3) function.
TransitionTypeTRANS_CIRC=8
The animation is interpolated with a function using square roots.
TransitionTypeTRANS_BOUNCE=9
The animation is interpolated by bouncing at the end.
TransitionTypeTRANS_BACK=10
The animation is interpolated backing out at ends.
TransitionTypeTRANS_SPRING=11
The animation is interpolated like a spring towards the end.
enumEaseType:🔗
EaseTypeEASE_IN=0
The interpolation starts slowly and speeds up towards the end.
EaseTypeEASE_OUT=1
The interpolation starts quickly and slows down towards the end.
EaseTypeEASE_IN_OUT=2
A combination ofEASE_INandEASE_OUT. The interpolation is slowest at both ends.
EaseTypeEASE_OUT_IN=3
A combination ofEASE_INandEASE_OUT. The interpolation is fastest at both ends.

## Method Descriptions

Tweenbind_node(node:Node)🔗
Binds thisTweenwith the givennode.Tweens are processed directly by theSceneTree, so they run independently of the animated nodes. When you bind aNodewith theTween, theTweenwill halt the animation when the object is not inside tree and theTweenwill be automatically killed when the bound object is freed. AlsoTWEEN_PAUSE_BOUNDwill make the pausing behavior dependent on the bound node.
For a shorter way to create and bind aTween, you can useNode.create_tween().
Tweenchain()🔗
Used to chain twoTweeners afterset_parallel()is called withtrue.

```
var tween = create_tween().set_parallel(true)
tween.tween_property(...)
tween.tween_property(...) # Will run parallelly with above.
tween.chain().tween_property(...) # Will run after two above are finished.
```

```
Tween tween = CreateTween().SetParallel(true);
tween.TweenProperty(...);
tween.TweenProperty(...); // Will run parallelly with above.
tween.Chain().TweenProperty(...); // Will run after two above are finished.
```

boolcustom_step(delta:float)🔗
Processes theTweenby the givendeltavalue, in seconds. This is mostly useful for manual control when theTweenis paused. It can also be used to end theTweenanimation immediately, by settingdeltalonger than the whole duration of theTweenanimation.
Returnstrueif theTweenstill hasTweeners that haven't finished.
intget_loops_left()const🔗
Returns the number of remaining loops for thisTween(seeset_loops()). A return value of-1indicates an infinitely loopingTween, and a return value of0indicates that theTweenhas already finished.
floatget_total_elapsed_time()const🔗
Returns the total time in seconds theTweenhas been animating (i.e. the time since it started, not counting pauses etc.). The time is affected byset_speed_scale(), andstop()will reset it to0.
Note:As it results from accumulating frame deltas, the time returned after theTweenhas finished animating will be slightly greater than the actualTweenduration.
Variantinterpolate_value(initial_value:Variant, delta_value:Variant, elapsed_time:float, duration:float, trans_type:TransitionType, ease_type:EaseType)static🔗
This method can be used for manual interpolation of a value, when you don't wantTweento do animating for you. It's similar to@GlobalScope.lerp(), but with support for custom transition and easing.
initial_valueis the starting value of the interpolation.
delta_valueis the change of the value in the interpolation, i.e. it's equal tofinal_value-initial_value.
elapsed_timeis the time in seconds that passed after the interpolation started and it's used to control the position of the interpolation. E.g. when it's equal to half of theduration, the interpolated value will be halfway between initial and final values. This value can also be greater thandurationor lower than 0, which will extrapolate the value.
durationis the total time of the interpolation.
Note:Ifdurationis equal to0, the method will always return the final value, regardless ofelapsed_timeprovided.
boolis_running()🔗
Returns whether theTweenis currently running, i.e. it wasn't paused and it's not finished.
boolis_valid()🔗
Returns whether theTweenis valid. A validTweenis aTweencontained by the scene tree (i.e. the array fromSceneTree.get_processed_tweens()will contain thisTween). ATweenmight become invalid when it has finished tweening, is killed, or when created withTween.new(). InvalidTweens can't haveTweeners appended.
voidkill()🔗
Aborts all tweening operations and invalidates theTween.
Tweenparallel()🔗
Makes the nextTweenerrun parallelly to the previous one.

```
var tween = create_tween()
tween.tween_property(...)
tween.parallel().tween_property(...)
tween.parallel().tween_property(...)
```

```
Tween tween = CreateTween();
tween.TweenProperty(...);
tween.Parallel().TweenProperty(...);
tween.Parallel().TweenProperty(...);
```

AllTweeners in the example will run at the same time.
You can make theTweenparallel by default by usingset_parallel().
voidpause()🔗
Pauses the tweening. The animation can be resumed by usingplay().
Note:If a Tween is paused and not bound to any node, it will exist indefinitely until manually started or invalidated. If you lose a reference to such Tween, you can retrieve it usingSceneTree.get_processed_tweens().
voidplay()🔗
Resumes a paused or stoppedTween.
Tweenset_ease(ease:EaseType)🔗
Sets the default ease type forPropertyTweeners andMethodTweeners appended after this method.
Before this method is called, the default ease type isEASE_IN_OUT.

```
var tween = create_tween()
tween.tween_property(self, "position", Vector2(300, 0), 0.5) # Uses EASE_IN_OUT.
tween.set_ease(Tween.EASE_IN)
tween.tween_property(self, "rotation_degrees", 45.0, 0.5) # Uses EASE_IN.
```

Tweenset_ignore_time_scale(ignore:bool= true)🔗
Ifignoreistrue, the tween will ignoreEngine.time_scaleand update with the real, elapsed time. This affects allTweeners and their delays. Default value isfalse.
Tweenset_loops(loops:int= 0)🔗
Sets the number of times the tweening sequence will be repeated, i.e.set_loops(2)will run the animation twice.
Calling this method without arguments will make theTweenrun infinitely, until either it is killed withkill(), theTween's bound node is freed, or all the animated objects have been freed (which makes further animation impossible).
Warning:Make sure to always add some duration/delay when using infinite loops. To prevent the game freezing, 0-duration looped animations (e.g. a singleCallbackTweenerwith no delay) are stopped after a small number of loops, which may produce unexpected results. If aTween's lifetime depends on some node, always usebind_node().
Tweenset_parallel(parallel:bool= true)🔗
Ifparallelistrue, theTweeners appended after this method will by default run simultaneously, as opposed to sequentially.
Note:Just like withparallel(), the tweener added right before this method will also be part of the parallel step.

```
tween.tween_property(self, "position", Vector2(300, 0), 0.5)
tween.set_parallel()
tween.tween_property(self, "modulate", Color.GREEN, 0.5) # Runs together with the position tweener.
```

Tweenset_pause_mode(mode:TweenPauseMode)🔗
Determines the behavior of theTweenwhen theSceneTreeis paused.
Default value isTWEEN_PAUSE_BOUND.
Tweenset_process_mode(mode:TweenProcessMode)🔗
Determines whether theTweenshould run after process frames (seeNode._process()) or physics frames (seeNode._physics_process()).
Default value isTWEEN_PROCESS_IDLE.
Tweenset_speed_scale(speed:float)🔗
Scales the speed of tweening. This affects allTweeners and their delays.
Tweenset_trans(trans:TransitionType)🔗
Sets the default transition type forPropertyTweeners andMethodTweeners appended after this method.
Before this method is called, the default transition type isTRANS_LINEAR.

```
var tween = create_tween()
tween.tween_property(self, "position", Vector2(300, 0), 0.5) # Uses TRANS_LINEAR.
tween.set_trans(Tween.TRANS_SINE)
tween.tween_property(self, "rotation_degrees", 45.0, 0.5) # Uses TRANS_SINE.
```

voidstop()🔗
Stops the tweening and resets theTweento its initial state. This will not remove any appendedTweeners.
Note:This doesnotreset targets ofPropertyTweeners to their values when theTweenfirst started.

```
var tween = create_tween()

# Will move from 0 to 500 over 1 second.
position.x = 0.0
tween.tween_property(self, "position:x", 500, 1.0)

# Will be at (about) 250 when the timer finishes.
await get_tree().create_timer(0.5).timeout

# Will now move from (about) 250 to 500 over 1 second,
# thus at half the speed as before.
tween.stop()
tween.play()
```

Note:If a Tween is stopped and not bound to any node, it will exist indefinitely until manually started or invalidated. If you lose a reference to such Tween, you can retrieve it usingSceneTree.get_processed_tweens().
CallbackTweenertween_callback(callback:Callable)🔗
Creates and appends aCallbackTweener. This method can be used to call an arbitrary method in any object. UseCallable.bind()to bind additional arguments for the call.
Example:Object that keeps shooting every 1 second:

```
var tween = get_tree().create_tween().set_loops()
tween.tween_callback(shoot).set_delay(1.0)
```

```
Tween tween = GetTree().CreateTween().SetLoops();
tween.TweenCallback(Callable.From(Shoot)).SetDelay(1.0f);
```

Example:Turning a sprite red and then blue, with 2 second delay:

```
var tween = get_tree().create_tween()
tween.tween_callback($Sprite.set_modulate.bind(Color.RED)).set_delay(2)
tween.tween_callback($Sprite.set_modulate.bind(Color.BLUE)).set_delay(2)
```

```
Tween tween = GetTree().CreateTween();
Sprite2D sprite = GetNode<Sprite2D>("Sprite");
tween.TweenCallback(Callable.From(() => sprite.Modulate = Colors.Red)).SetDelay(2.0f);
tween.TweenCallback(Callable.From(() => sprite.Modulate = Colors.Blue)).SetDelay(2.0f);
```

IntervalTweenertween_interval(time:float)🔗
Creates and appends anIntervalTweener. This method can be used to create delays in the tween animation, as an alternative to using the delay in otherTweeners, or when there's no animation (in which case theTweenacts as a timer).timeis the length of the interval, in seconds.
Example:Creating an interval in code execution:

```
# ... some code
await create_tween().tween_interval(2).finished
# ... more code
```

```
// ... some code
await ToSignal(CreateTween().TweenInterval(2.0f), Tween.SignalName.Finished);
// ... more code
```

Example:Creating an object that moves back and forth and jumps every few seconds:

```
var tween = create_tween().set_loops()
tween.tween_property($Sprite, "position:x", 200.0, 1.0).as_relative()
tween.tween_callback(jump)
tween.tween_interval(2)
tween.tween_property($Sprite, "position:x", -200.0, 1.0).as_relative()
tween.tween_callback(jump)
tween.tween_interval(2)
```

```
Tween tween = CreateTween().SetLoops();
tween.TweenProperty(GetNode("Sprite"), "position:x", 200.0f, 1.0f).AsRelative();
tween.TweenCallback(Callable.From(Jump));
tween.TweenInterval(2.0f);
tween.TweenProperty(GetNode("Sprite"), "position:x", -200.0f, 1.0f).AsRelative();
tween.TweenCallback(Callable.From(Jump));
tween.TweenInterval(2.0f);
```

MethodTweenertween_method(method:Callable, from:Variant, to:Variant, duration:float)🔗
Creates and appends aMethodTweener. This method is similar to a combination oftween_callback()andtween_property(). It calls a method over time with a tweened value provided as an argument. The value is tweened betweenfromandtoover the time specified byduration, in seconds. UseCallable.bind()to bind additional arguments for the call. You can useMethodTweener.set_ease()andMethodTweener.set_trans()to tweak the easing and transition of the value orMethodTweener.set_delay()to delay the tweening.
Example:Making a 3D object look from one point to another point:

```
var tween = create_tween()
tween.tween_method(look_at.bind(Vector3.UP), Vector3(-1, 0, -1), Vector3(1, 0, -1), 1.0) # The look_at() method takes up vector as second argument.
```

```
Tween tween = CreateTween();
tween.TweenMethod(Callable.From((Vector3 target) => LookAt(target, Vector3.Up)), new Vector3(-1.0f, 0.0f, -1.0f), new Vector3(1.0f, 0.0f, -1.0f), 1.0f); // Use lambdas to bind additional arguments for the call.
```

Example:Setting the text of aLabel, using an intermediate method and after a delay:

```
func _ready():
    var tween = create_tween()
    tween.tween_method(set_label_text, 0, 10, 1.0).set_delay(1.0)

func set_label_text(value: int):
    $Label.text = "Counting " + str(value)
```

```
public override void _Ready()
{
    base._Ready();

    Tween tween = CreateTween();
    tween.TweenMethod(Callable.From<int>(SetLabelText), 0.0f, 10.0f, 1.0f).SetDelay(1.0f);
}

private void SetLabelText(int value)
{
    GetNode<Label>("Label").Text = $"Counting {value}";
}
```

PropertyTweenertween_property(object:Object, property:NodePath, final_val:Variant, duration:float)🔗
Creates and appends aPropertyTweener. This method tweens apropertyof anobjectbetween an initial value andfinal_valin a span of time equal toduration, in seconds. The initial value by default is the property's value at the time the tweening of thePropertyTweenerstarts.

```
var tween = create_tween()
tween.tween_property($Sprite, "position", Vector2(100, 200), 1.0)
tween.tween_property($Sprite, "position", Vector2(200, 300), 1.0)
```

```
Tween tween = CreateTween();
tween.TweenProperty(GetNode("Sprite"), "position", new Vector2(100.0f, 200.0f), 1.0f);
tween.TweenProperty(GetNode("Sprite"), "position", new Vector2(200.0f, 300.0f), 1.0f);
```

will move the sprite to position (100, 200) and then to (200, 300). If you usePropertyTweener.from()orPropertyTweener.from_current(), the starting position will be overwritten by the given value instead. See other methods inPropertyTweenerto see how the tweening can be tweaked further.
Note:You can find the correct property name by hovering over the property in the Inspector. You can also provide the components of a property directly by using"property:component"(eg.position:x), where it would only apply to that particular component.
Example:Moving an object twice from the same position, with different transition types:

```
var tween = create_tween()
tween.tween_property($Sprite, "position", Vector2.RIGHT * 300, 1.0).as_relative().set_trans(Tween.TRANS_SINE)
tween.tween_property($Sprite, "position", Vector2.RIGHT * 300, 1.0).as_relative().from_current().set_trans(Tween.TRANS_EXPO)
```

```
Tween tween = CreateTween();
tween.TweenProperty(GetNode("Sprite"), "position", Vector2.Right * 300.0f, 1.0f).AsRelative().SetTrans(Tween.TransitionType.Sine);
tween.TweenProperty(GetNode("Sprite"), "position", Vector2.Right * 300.0f, 1.0f).AsRelative().FromCurrent().SetTrans(Tween.TransitionType.Expo);
```

SubtweenTweenertween_subtween(subtween:Tween)🔗
Creates and appends aSubtweenTweener. This method can be used to nestsubtweenwithin thisTween, allowing for the creation of more complex and composable sequences.

```
# Subtween will rotate the object.
var subtween = create_tween()
subtween.tween_property(self, "rotation_degrees", 45.0, 1.0)
subtween.tween_property(self, "rotation_degrees", 0.0, 1.0)

# Parent tween will execute the subtween as one of its steps.
var tween = create_tween()
tween.tween_property(self, "position:x", 500, 3.0)
tween.tween_subtween(subtween)
tween.tween_property(self, "position:x", 300, 2.0)
```

Note:The methodspause(),stop(), andset_loops()can cause the parentTweento get stuck on the subtween step; see the documentation for those methods for more information.
Note:The pause and process modes set byset_pause_mode()andset_process_mode()onsubtweenwill be overridden by the parentTween's settings.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
