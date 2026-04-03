# WebXRInterface in English

# WebXRInterface
Inherits:XRInterface<RefCounted<Object
XR interface using WebXR.

## Description
WebXR is an open standard that allows creating VR and AR applications that run in the web browser.
As such, this interface is only available when running in Web exports.
WebXR supports a wide range of devices, from the very capable (like Valve Index, HTC Vive, Oculus Rift and Quest) down to the much less capable (like Google Cardboard, Oculus Go, GearVR, or plain smartphones).
Since WebXR is based on JavaScript, it makes extensive use of callbacks, which means thatWebXRInterfaceis forced to use signals, where other XR interfaces would instead use functions that return a result immediately. This makesWebXRInterfacequite a bit more complicated to initialize than other XR interfaces.
Here's the minimum code required to start an immersive VR session:
```
extends Node3D

var webxr_interface
var vr_supported = false

func _ready():
    # We assume this node has a button as a child.
    # This button is for the user to consent to entering immersive VR mode.
    $Button.pressed.connect(self._on_button_pressed)

    webxr_interface = XRServer.find_interface("WebXR")
    if webxr_interface:
        # WebXR uses a lot of asynchronous callbacks, so we connect to various
        # signals in order to receive them.
        webxr_interface.session_supported.connect(self._webxr_session_supported)
        webxr_interface.session_started.connect(self._webxr_session_started)
        webxr_interface.session_ended.connect(self._webxr_session_ended)
        webxr_interface.session_failed.connect(self._webxr_session_failed)

        # This returns immediately - our _webxr_session_supported() method
        # (which we connected to the "session_supported" signal above) will
        # be called sometime later to let us know if it's supported or not.
        webxr_interface.is_session_supported("immersive-vr")

func _webxr_session_supported(session_mode, supported):
    if session_mode == 'immersive-vr':
        vr_supported = supported

func _on_button_pressed():
    if not vr_supported:
        OS.alert("Your browser doesn't support VR")
        return

    # We want an immersive VR session, as opposed to AR ('immersive-ar') or a
    # simple 3DoF viewer ('viewer').
    webxr_interface.session_mode = 'immersive-vr'
    # 'bounded-floor' is room scale, 'local-floor' is a standing or sitting
    # experience (it puts you 1.6m above the ground if you have 3DoF headset),
    # whereas as 'local' puts you down at the XROrigin.
    # This list means it'll first try to request 'bounded-floor', then
    # fallback on 'local-floor' and ultimately 'local', if nothing else is
    # supported.
    webxr_interface.requested_reference_space_types = 'bounded-floor, local-floor, local'
    # In order to use 'local-floor' or 'bounded-floor' we must also
    # mark the features as required or optional. By including 'hand-tracking'
    # as an optional feature, it will be enabled if supported.
    webxr_interface.required_features = 'local-floor'
    webxr_interface.optional_features = 'bounded-floor, hand-tracking'

    # This will return false if we're unable to even request the session,
    # however, it can still fail asynchronously later in the process, so we
    # only know if it's really succeeded or failed when our
    # _webxr_session_started() or _webxr_session_failed() methods are called.
    if not webxr_interface.initialize():
        OS.alert("Failed to initialize")
        return

func _webxr_session_started():
    $Button.visible = false
    # This tells Godot to start rendering to the headset.
    get_viewport().use_xr = true
    # This will be the reference space type you ultimately got, out of the
    # types that you requested above. This is useful if you want the game to
    # work a little differently in 'bounded-floor' versus 'local-floor'.
    print("Reference space type: ", webxr_interface.reference_space_type)
    # This will be the list of features that were successfully enabled
    # (except on browsers that don't support this property).
    print("Enabled features: ", webxr_interface.enabled_features)

func _webxr_session_ended():
    $Button.visible = true
    # If the user exits immersive mode, then we tell Godot to render to the web
    # page again.
    get_viewport().use_xr = false

func _webxr_session_failed(message):
    OS.alert("Failed to initialize: " + message)
```
There are a couple ways to handle "controller" input:
- UsingXRController3Dnodes and theirXRController3D.button_pressedandXRController3D.button_releasedsignals. This is how controllers are typically handled in XR apps in Godot, however, this will only work with advanced VR controllers like the Oculus Touch or Index controllers, for example.
UsingXRController3Dnodes and theirXRController3D.button_pressedandXRController3D.button_releasedsignals. This is how controllers are typically handled in XR apps in Godot, however, this will only work with advanced VR controllers like the Oculus Touch or Index controllers, for example.
- Using theselect,squeezeand related signals. This method will work for both advanced VR controllers, and non-traditional input sources like a tap on the screen, a spoken voice command or a button press on the device itself.
Using theselect,squeezeand related signals. This method will work for both advanced VR controllers, and non-traditional input sources like a tap on the screen, a spoken voice command or a button press on the device itself.
You can use both methods to allow your game or app to support a wider or narrower set of devices and input methods, or to allow more advanced interactions with more advanced devices.

## Tutorials
- How to make a VR game for WebXR with Godot 4
How to make a VR game for WebXR with Godot 4

## Properties

| String | enabled_features |
|---|---|
| String | optional_features |
| String | reference_space_type |
| String | requested_reference_space_types |
| String | required_features |
| String | session_mode |
| String | visibility_state |

String
enabled_features
String
optional_features
String
reference_space_type
String
requested_reference_space_types
String
required_features
String
session_mode
String
visibility_state

## Methods

| Array | get_available_display_refresh_rates()const |
|---|---|
| float | get_display_refresh_rate()const |
| TargetRayMode | get_input_source_target_ray_mode(input_source_id:int)const |
| XRControllerTracker | get_input_source_tracker(input_source_id:int)const |
| bool | is_input_source_active(input_source_id:int)const |
| void | is_session_supported(session_mode:String) |
| void | set_display_refresh_rate(refresh_rate:float) |

Array
get_available_display_refresh_rates()const
float
get_display_refresh_rate()const
TargetRayMode
get_input_source_target_ray_mode(input_source_id:int)const
XRControllerTracker
get_input_source_tracker(input_source_id:int)const
bool
is_input_source_active(input_source_id:int)const
void
is_session_supported(session_mode:String)
void
set_display_refresh_rate(refresh_rate:float)

## Signals
display_refresh_rate_changed()🔗
Emitted after the display's refresh rate has changed.
reference_space_reset()🔗
Emitted to indicate that the reference space has been reset or reconfigured.
When (or whether) this is emitted depends on the user's browser or device, but may include when the user has changed the dimensions of their play space (which you may be able to access viaXRInterface.get_play_area()) or pressed/held a button to recenter their position.
SeeWebXR's XRReferenceSpace reset eventfor more information.
select(input_source_id:int)🔗
Emitted after one of the input sources has finished its "primary action".
Useget_input_source_tracker()andget_input_source_target_ray_mode()to get more information about the input source.
selectend(input_source_id:int)🔗
Emitted when one of the input sources has finished its "primary action".
Useget_input_source_tracker()andget_input_source_target_ray_mode()to get more information about the input source.
selectstart(input_source_id:int)🔗
Emitted when one of the input source has started its "primary action".
Useget_input_source_tracker()andget_input_source_target_ray_mode()to get more information about the input source.
session_ended()🔗
Emitted when the user ends the WebXR session (which can be done using UI from the browser or device).
At this point, you should doget_viewport().use_xr=falseto instruct Godot to resume rendering to the screen.
session_failed(message:String)🔗
Emitted byXRInterface.initialize()if the session fails to start.
messagemay optionally contain an error message from WebXR, or an empty string if no message is available.
session_started()🔗
Emitted byXRInterface.initialize()if the session is successfully started.
At this point, it's safe to doget_viewport().use_xr=trueto instruct Godot to start rendering to the XR device.
session_supported(session_mode:String, supported:bool)🔗
Emitted byis_session_supported()to indicate if the givensession_modeis supported or not.
squeeze(input_source_id:int)🔗
Emitted after one of the input sources has finished its "primary squeeze action".
Useget_input_source_tracker()andget_input_source_target_ray_mode()to get more information about the input source.
squeezeend(input_source_id:int)🔗
Emitted when one of the input sources has finished its "primary squeeze action".
Useget_input_source_tracker()andget_input_source_target_ray_mode()to get more information about the input source.
squeezestart(input_source_id:int)🔗
Emitted when one of the input sources has started its "primary squeeze action".
Useget_input_source_tracker()andget_input_source_target_ray_mode()to get more information about the input source.
visibility_state_changed()🔗
Emitted whenvisibility_statehas changed.

## Enumerations
enumTargetRayMode:🔗
TargetRayModeTARGET_RAY_MODE_UNKNOWN=0
We don't know the target ray mode.
TargetRayModeTARGET_RAY_MODE_GAZE=1
Target ray originates at the viewer's eyes and points in the direction they are looking.
TargetRayModeTARGET_RAY_MODE_TRACKED_POINTER=2
Target ray from a handheld pointer, most likely a VR touch controller.
TargetRayModeTARGET_RAY_MODE_SCREEN=3
Target ray from touch screen, mouse or other tactile input device.

## Property Descriptions
Stringenabled_features🔗
- Stringget_enabled_features()
Stringget_enabled_features()
A comma-separated list of features that were successfully enabled byXRInterface.initialize()when setting up the WebXR session.
This may include features requested by settingrequired_featuresandoptional_features, and will only be available aftersession_startedhas been emitted.
Note:This may not be support by all web browsers, in which case it will be an empty string.
Stringoptional_features🔗
- voidset_optional_features(value:String)
voidset_optional_features(value:String)
- Stringget_optional_features()
Stringget_optional_features()
A comma-seperated list of optional features used byXRInterface.initialize()when setting up the WebXR session.
If a user's browser or device doesn't support one of the given features, initialization will continue, but you won't be able to use the requested feature.
This doesn't have any effect on the interface when already initialized.
See the MDN documentation onWebXR's session featuresfor a list of possible values.
Stringreference_space_type🔗
- Stringget_reference_space_type()
Stringget_reference_space_type()
The reference space type (from the list of requested types set in therequested_reference_space_typesproperty), that was ultimately used byXRInterface.initialize()when setting up the WebXR session.
Possible values come fromWebXR's XRReferenceSpaceType. If you want to use a particular reference space type, it must be listed in eitherrequired_featuresoroptional_features.
Stringrequested_reference_space_types🔗
- voidset_requested_reference_space_types(value:String)
voidset_requested_reference_space_types(value:String)
- Stringget_requested_reference_space_types()
Stringget_requested_reference_space_types()
A comma-seperated list of reference space types used byXRInterface.initialize()when setting up the WebXR session.
The reference space types are requested in order, and the first one supported by the user's device or browser will be used. Thereference_space_typeproperty contains the reference space type that was ultimately selected.
This doesn't have any effect on the interface when already initialized.
Possible values come fromWebXR's XRReferenceSpaceType. If you want to use a particular reference space type, it must be listed in eitherrequired_featuresoroptional_features.
Stringrequired_features🔗
- voidset_required_features(value:String)
voidset_required_features(value:String)
- Stringget_required_features()
Stringget_required_features()
A comma-seperated list of required features used byXRInterface.initialize()when setting up the WebXR session.
If a user's browser or device doesn't support one of the given features, initialization will fail andsession_failedwill be emitted.
This doesn't have any effect on the interface when already initialized.
See the MDN documentation onWebXR's session featuresfor a list of possible values.
Stringsession_mode🔗
- voidset_session_mode(value:String)
voidset_session_mode(value:String)
- Stringget_session_mode()
Stringget_session_mode()
The session mode used byXRInterface.initialize()when setting up the WebXR session.
This doesn't have any effect on the interface when already initialized.
Possible values come fromWebXR's XRSessionMode, including:"immersive-vr","immersive-ar", and"inline".
Stringvisibility_state🔗
- Stringget_visibility_state()
Stringget_visibility_state()
Indicates if the WebXR session's imagery is visible to the user.
Possible values come fromWebXR's XRVisibilityState, including"hidden","visible", and"visible-blurred".

## Method Descriptions
Arrayget_available_display_refresh_rates()const🔗
Returns display refresh rates supported by the current HMD. Only returned if this feature is supported by the web browser and after the interface has been initialized.
floatget_display_refresh_rate()const🔗
Returns the display refresh rate for the current HMD. Not supported on all HMDs and browsers. It may not report an accurate value until after usingset_display_refresh_rate().
TargetRayModeget_input_source_target_ray_mode(input_source_id:int)const🔗
Returns the target ray mode for the giveninput_source_id.
This can help interpret the input coming from that input source. SeeXRInputSource.targetRayModefor more information.
XRControllerTrackerget_input_source_tracker(input_source_id:int)const🔗
Gets anXRControllerTrackerfor the giveninput_source_id.
In the context of WebXR, an input source can be an advanced VR controller like the Oculus Touch or Index controllers, or even a tap on the screen, a spoken voice command or a button press on the device itself. When a non-traditional input source is used, interpret the position and orientation of theXRPositionalTrackeras a ray pointing at the object the user wishes to interact with.
Use this method to get information about the input source that triggered one of these signals:
- selectstart
selectstart
- select
select
- selectend
selectend
- squeezestart
squeezestart
- squeeze
squeeze
- squeezestart
squeezestart
boolis_input_source_active(input_source_id:int)const🔗
Returnstrueif there is an active input source with the giveninput_source_id.
voidis_session_supported(session_mode:String)🔗
Checks if the givensession_modeis supported by the user's browser.
Possible values come fromWebXR's XRSessionMode, including:"immersive-vr","immersive-ar", and"inline".
This method returns nothing, instead it emits thesession_supportedsignal with the result.
voidset_display_refresh_rate(refresh_rate:float)🔗
Sets the display refresh rate for the current HMD. Not supported on all HMDs and browsers. It won't take effect right away until afterdisplay_refresh_rate_changedis emitted.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.