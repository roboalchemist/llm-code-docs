# EditorResourceTooltipPlugin in English

# EditorResourceTooltipPlugin
Inherits:RefCounted<Object
A plugin that advanced tooltip for its handled resource type.

## Description
Resource tooltip plugins are used byFileSystemDockto generate customized tooltips for specific resources. E.g. tooltip for aTexture2Ddisplays a bigger preview and the texture's dimensions.
A plugin must be first registered withFileSystemDock.add_resource_tooltip_plugin(). When the user hovers a resource in filesystem dock which is handled by the plugin,_make_tooltip_for_path()is called to create the tooltip. It works similarly toControl._make_custom_tooltip().

## Methods

| bool | _handles(type:String)virtualconst |
|---|---|
| Control | _make_tooltip_for_path(path:String, metadata:Dictionary, base:Control)virtualconst |
| void | request_thumbnail(path:String, control:TextureRect)const |

bool
_handles(type:String)virtualconst
Control
_make_tooltip_for_path(path:String, metadata:Dictionary, base:Control)virtualconst
void
request_thumbnail(path:String, control:TextureRect)const

## Method Descriptions
bool_handles(type:String)virtualconst🔗
Returntrueif the plugin is going to handle the givenResourcetype.
Control_make_tooltip_for_path(path:String, metadata:Dictionary, base:Control)virtualconst🔗
Create and return a tooltip that will be displayed when the user hovers a resource under the givenpathin filesystem dock.
Themetadatadictionary is provided by preview generator (seeEditorResourcePreviewGenerator._generate()).
baseis the base default tooltip, which is aVBoxContainerwith a file name, type and size labels. If another plugin handled the same file type,basewill be output from the previous plugin. For best result, make sure the base tooltip is part of the returnedControl.
Note:It's unadvised to useResourceLoader.load(), especially with heavy resources like models or textures, because it will make the editor unresponsive when creating the tooltip. You can userequest_thumbnail()if you want to display a preview in your tooltip.
Note:If you decide to discard thebase, make sure to callNode.queue_free(), because it's not freed automatically.
```
func _make_tooltip_for_path(path, metadata, base):
    var t_rect = TextureRect.new()
    request_thumbnail(path, t_rect)
    base.add_child(t_rect) # The TextureRect will appear at the bottom of the tooltip.
    return base
```
voidrequest_thumbnail(path:String, control:TextureRect)const🔗
Requests a thumbnail for the givenTextureRect. The thumbnail is created asynchronously byEditorResourcePreviewand automatically set when available.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.