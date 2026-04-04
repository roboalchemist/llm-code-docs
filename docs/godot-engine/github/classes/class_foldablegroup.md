:github_url: hide

> **META**
	:keywords: expandable, collapsible, collapse



# FoldableGroup

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A group of foldable containers that doesn't allow more than one container to be expanded at a time.


## Description

A group of [FoldableContainer<class_FoldableContainer>]-derived nodes. Only one container can be expanded at a time.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`allow_folding_all<class_FoldableGroup_property_allow_folding_all>` | ``false``                                                                             |
> +-------------------------+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | resource_local_to_scene                                                  | ``true`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +-------------------------+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`FoldableContainer<class_FoldableContainer>`\] | :ref:`get_containers<class_FoldableGroup_method_get_containers>`\ (\ ) |const|                 |
> +--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
> | :ref:`FoldableContainer<class_FoldableContainer>`                              | :ref:`get_expanded_container<class_FoldableGroup_method_get_expanded_container>`\ (\ ) |const| |
> +--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
>

----


## Signals



**expanded**\ (\ container\: [FoldableContainer<class_FoldableContainer>]\ ) [🔗<class_FoldableGroup_signal_expanded>]

Emitted when one of the containers of the group is expanded.


----


## Property Descriptions



[bool<class_bool>] **allow_folding_all** = `false` [🔗<class_FoldableGroup_property_allow_folding_all>]


- |void| **set_allow_folding_all**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_allow_folding_all**\ (\ )

If `true`, it is possible to fold all containers in this FoldableGroup.


----


## Method Descriptions



[Array<class_Array>]\[[FoldableContainer<class_FoldableContainer>]\] **get_containers**\ (\ ) |const| [🔗<class_FoldableGroup_method_get_containers>]

Returns an [Array<class_Array>] of [FoldableContainer<class_FoldableContainer>]\ s that have this as their FoldableGroup (see [FoldableContainer.foldable_group<class_FoldableContainer_property_foldable_group>]). This is equivalent to [ButtonGroup<class_ButtonGroup>] but for FoldableContainers.


----



[FoldableContainer<class_FoldableContainer>] **get_expanded_container**\ (\ ) |const| [🔗<class_FoldableGroup_method_get_expanded_container>]

Returns the current expanded container.

