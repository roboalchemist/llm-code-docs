# VisibleOnScreenEnabler2D in English

# VisibleOnScreenEnabler2D

Inherits:VisibleOnScreenNotifier2D<Node2D<CanvasItem<Node<Object
A rectangular region of 2D space that, when visible on screen, enables a target node.

## Description

VisibleOnScreenEnabler2Dcontains a rectangular region of 2D space and a target node. The target node will be automatically enabled (via itsNode.process_modeproperty) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.
SeeVisibleOnScreenNotifier2Dif you only want to be notified when the region is visible on screen.
Note:VisibleOnScreenEnabler2Duses the render culling code to determine whether it's visible on screen, so it won't function unlessCanvasItem.visibleis set totrue.

## Properties

| EnableMode | enable_mode | 0 |
|---|---|---|
| NodePath | enable_node_path | NodePath("..") |

EnableMode
enable_mode
NodePath
enable_node_path
NodePath("..")

## Enumerations

enumEnableMode:🔗
EnableModeENABLE_MODE_INHERIT=0
Corresponds toNode.PROCESS_MODE_INHERIT.
EnableModeENABLE_MODE_ALWAYS=1
Corresponds toNode.PROCESS_MODE_ALWAYS.
EnableModeENABLE_MODE_WHEN_PAUSED=2
Corresponds toNode.PROCESS_MODE_WHEN_PAUSED.

## Property Descriptions

EnableModeenable_mode=0🔗

- voidset_enable_mode(value:EnableMode)
voidset_enable_mode(value:EnableMode)
- EnableModeget_enable_mode()
EnableModeget_enable_mode()
Determines how the target node is enabled. Corresponds toProcessMode. When the node is disabled, it always usesNode.PROCESS_MODE_DISABLED.
NodePathenable_node_path=NodePath("..")🔗
- voidset_enable_node_path(value:NodePath)
voidset_enable_node_path(value:NodePath)
- NodePathget_enable_node_path()
NodePathget_enable_node_path()
The path to the target node, relative to theVisibleOnScreenEnabler2D. The target node is cached; it's only assigned when setting this property (if theVisibleOnScreenEnabler2Dis inside the scene tree) and every time theVisibleOnScreenEnabler2Denters the scene tree. If the path is empty, no node will be affected. If the path is invalid, an error is also generated.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
