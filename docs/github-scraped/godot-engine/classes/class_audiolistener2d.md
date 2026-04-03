:github_url: hide

> **META**
	:keywords: sound



# AudioListener2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Overrides the location sounds are heard from.


## Description

Once added to the scene tree and enabled using [make_current()<class_AudioListener2D_method_make_current>], this node will override the location sounds are heard from. Only one **AudioListener2D** can be current. Using [make_current()<class_AudioListener2D_method_make_current>] will disable the previous **AudioListener2D**.

If there is no active **AudioListener2D** in the current [Viewport<class_Viewport>], center of the screen will be used as a hearing point for the audio. **AudioListener2D** needs to be inside [SceneTree<class_SceneTree>] to function.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------+
> | |void|                  | :ref:`clear_current<class_AudioListener2D_method_clear_current>`\ (\ )   |
> +-------------------------+--------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_current<class_AudioListener2D_method_is_current>`\ (\ ) |const| |
> +-------------------------+--------------------------------------------------------------------------+
> | |void|                  | :ref:`make_current<class_AudioListener2D_method_make_current>`\ (\ )     |
> +-------------------------+--------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **clear_current**\ (\ ) [🔗<class_AudioListener2D_method_clear_current>]

Disables the **AudioListener2D**. If it's not set as current, this method will have no effect.


----



[bool<class_bool>] **is_current**\ (\ ) |const| [🔗<class_AudioListener2D_method_is_current>]

Returns `true` if this **AudioListener2D** is currently active.


----



|void| **make_current**\ (\ ) [🔗<class_AudioListener2D_method_make_current>]

Makes the **AudioListener2D** active, setting it as the hearing point for the sounds. If there is already another active **AudioListener2D**, it will be disabled.

This method will have no effect if the **AudioListener2D** is not added to [SceneTree<class_SceneTree>].

