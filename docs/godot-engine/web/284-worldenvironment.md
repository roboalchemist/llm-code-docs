# WorldEnvironment

# WorldEnvironment
Inherits:Node<Object
Default environment properties for the entire scene (post-processing effects, lighting and background settings).

## Description
TheWorldEnvironmentnode is used to configure the defaultEnvironmentfor the scene.
The parameters defined in theWorldEnvironmentcan be overridden by anEnvironmentnode set on the currentCamera3D. Additionally, only oneWorldEnvironmentmay be instantiated in a given scene at a time.
TheWorldEnvironmentallows the user to specify default lighting parameters (e.g. ambient lighting), various post-processing effects (e.g. SSAO, DOF, Tonemapping), and how to draw the background (e.g. solid color, skybox). Usually, these are added in order to improve the realism/color balance of the scene.

## Tutorials
- Environment and post-processing
Environment and post-processing
- 3D Material Testers Demo
3D Material Testers Demo
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| CameraAttributes | camera_attributes |
|---|---|
| Compositor | compositor |
| Environment | environment |

CameraAttributes
camera_attributes
Compositor
compositor
Environment
environment

## Property Descriptions
CameraAttributescamera_attributes🔗
- voidset_camera_attributes(value:CameraAttributes)
voidset_camera_attributes(value:CameraAttributes)
- CameraAttributesget_camera_attributes()
CameraAttributesget_camera_attributes()
The defaultCameraAttributesresource to use if none set on theCamera3D.
Compositorcompositor🔗
- voidset_compositor(value:Compositor)
voidset_compositor(value:Compositor)
- Compositorget_compositor()
Compositorget_compositor()
The defaultCompositorresource to use if none set on theCamera3D.
Environmentenvironment🔗
- voidset_environment(value:Environment)
voidset_environment(value:Environment)
- Environmentget_environment()
Environmentget_environment()
TheEnvironmentresource used by thisWorldEnvironment, defining the default properties.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.