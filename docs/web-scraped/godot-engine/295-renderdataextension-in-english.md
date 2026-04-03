# RenderDataExtension in English

# RenderDataExtension
Inherits:RenderData<Object
This class allows for a RenderData implementation to be made in GDExtension.

## Description
This class allows for a RenderData implementation to be made in GDExtension.

## Methods

| RID | _get_camera_attributes()virtualconst |
|---|---|
| RID | _get_environment()virtualconst |
| RenderSceneBuffers | _get_render_scene_buffers()virtualconst |
| RenderSceneData | _get_render_scene_data()virtualconst |

_get_camera_attributes()virtualconst
_get_environment()virtualconst
RenderSceneBuffers
_get_render_scene_buffers()virtualconst
RenderSceneData
_get_render_scene_data()virtualconst

## Method Descriptions
RID_get_camera_attributes()virtualconst🔗
Implement this in GDExtension to return theRIDfor the implementation's camera attributes object.
RID_get_environment()virtualconst🔗
Implement this in GDExtension to return theRIDof the implementation's environment object.
RenderSceneBuffers_get_render_scene_buffers()virtualconst🔗
Implement this in GDExtension to return the implementation'sRenderSceneBuffersobject.
RenderSceneData_get_render_scene_data()virtualconst🔗
Implement this in GDExtension to return the implementation'sRenderSceneDataExtensionobject.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.