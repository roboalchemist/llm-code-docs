:github_url: hide



# Container

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [AspectRatioContainer<class_AspectRatioContainer>], [BoxContainer<class_BoxContainer>], [CenterContainer<class_CenterContainer>], [EditorProperty<class_EditorProperty>], [FlowContainer<class_FlowContainer>], [FoldableContainer<class_FoldableContainer>], [GraphElement<class_GraphElement>], [GridContainer<class_GridContainer>], [MarginContainer<class_MarginContainer>], [PanelContainer<class_PanelContainer>], [ScrollContainer<class_ScrollContainer>], [SplitContainer<class_SplitContainer>], [SubViewportContainer<class_SubViewportContainer>], [TabContainer<class_TabContainer>]

Base class for all GUI containers.


## Description

Base class for all GUI containers. A **Container** automatically arranges its child controls in a certain way. This class can be inherited to make custom container types.


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------+--------------+-----------------------------------------------------------------------+
> | :ref:`MouseFilter<enum_Control_MouseFilter>` | mouse_filter | ``1`` (overrides :ref:`Control<class_Control_property_mouse_filter>`) |
> +----------------------------------------------+--------------+-----------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`_get_allowed_size_flags_horizontal<class_Container_private_method__get_allowed_size_flags_horizontal>`\ (\ ) |virtual| |const|              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`_get_allowed_size_flags_vertical<class_Container_private_method__get_allowed_size_flags_vertical>`\ (\ ) |virtual| |const|                  |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`fit_child_in_rect<class_Container_method_fit_child_in_rect>`\ (\ child\: :ref:`Control<class_Control>`, rect\: :ref:`Rect2<class_Rect2>`\ ) |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`queue_sort<class_Container_method_queue_sort>`\ (\ )                                                                                        |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**pre_sort_children**\ (\ ) [🔗<class_Container_signal_pre_sort_children>]

Emitted when children are going to be sorted.


----



**sort_children**\ (\ ) [🔗<class_Container_signal_sort_children>]

Emitted when sorting the children is needed.


----


## Constants



**NOTIFICATION_PRE_SORT_CHILDREN** = `50` [🔗<class_Container_constant_NOTIFICATION_PRE_SORT_CHILDREN>]

Notification just before children are going to be sorted, in case there's something to process beforehand.



**NOTIFICATION_SORT_CHILDREN** = `51` [🔗<class_Container_constant_NOTIFICATION_SORT_CHILDREN>]

Notification for when sorting the children, it must be obeyed immediately.


----


## Method Descriptions



[PackedInt32Array<class_PackedInt32Array>] **_get_allowed_size_flags_horizontal**\ (\ ) |virtual| |const| [🔗<class_Container_private_method__get_allowed_size_flags_horizontal>]

Implement to return a list of allowed horizontal [SizeFlags<enum_Control_SizeFlags>] for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

\ **Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN<class_Control_constant_SIZE_SHRINK_BEGIN>]. As such, this value is always implicitly allowed.


----



[PackedInt32Array<class_PackedInt32Array>] **_get_allowed_size_flags_vertical**\ (\ ) |virtual| |const| [🔗<class_Container_private_method__get_allowed_size_flags_vertical>]

Implement to return a list of allowed vertical [SizeFlags<enum_Control_SizeFlags>] for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

\ **Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN<class_Control_constant_SIZE_SHRINK_BEGIN>]. As such, this value is always implicitly allowed.


----



|void| **fit_child_in_rect**\ (\ child\: [Control<class_Control>], rect\: [Rect2<class_Rect2>]\ ) [🔗<class_Container_method_fit_child_in_rect>]

Fit a child control in a given rect. This is mainly a helper for creating custom container classes.


----



|void| **queue_sort**\ (\ ) [🔗<class_Container_method_queue_sort>]

Queue resort of the contained children. This is called automatically anyway, but can be called upon request.

