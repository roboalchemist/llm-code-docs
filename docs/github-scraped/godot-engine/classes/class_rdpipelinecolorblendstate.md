:github_url: hide



# RDPipelineColorBlendState

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Pipeline color blend state (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`Array<class_Array>`\[:ref:`RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>`\] | :ref:`attachments<class_RDPipelineColorBlendState_property_attachments>`         | ``[]``                |
> +--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`                                                                                          | :ref:`blend_constant<class_RDPipelineColorBlendState_property_blend_constant>`   | ``Color(0, 0, 0, 1)`` |
> +--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                                                                            | :ref:`enable_logic_op<class_RDPipelineColorBlendState_property_enable_logic_op>` | ``false``             |
> +--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`LogicOperation<enum_RenderingDevice_LogicOperation>`                                                         | :ref:`logic_op<class_RDPipelineColorBlendState_property_logic_op>`               | ``0``                 |
> +--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Array<class_Array>]\[[RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>]\] **attachments** = `[]` [🔗<class_RDPipelineColorBlendState_property_attachments>]


- |void| **set_attachments**\ (\ value\: [Array<class_Array>]\[[RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>]\]\ )
- [Array<class_Array>]\[[RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>]\] **get_attachments**\ (\ )

The attachments that are blended together.


----



[Color<class_Color>] **blend_constant** = `Color(0, 0, 0, 1)` [🔗<class_RDPipelineColorBlendState_property_blend_constant>]


- |void| **set_blend_constant**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_blend_constant**\ (\ )

The constant color to blend with. See also [RenderingDevice.draw_list_set_blend_constants()<class_RenderingDevice_method_draw_list_set_blend_constants>].


----



[bool<class_bool>] **enable_logic_op** = `false` [🔗<class_RDPipelineColorBlendState_property_enable_logic_op>]


- |void| **set_enable_logic_op**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_logic_op**\ (\ )

If `true`, performs the logic operation defined in [logic_op<class_RDPipelineColorBlendState_property_logic_op>].


----



[LogicOperation<enum_RenderingDevice_LogicOperation>] **logic_op** = `0` [🔗<class_RDPipelineColorBlendState_property_logic_op>]


- |void| **set_logic_op**\ (\ value\: [LogicOperation<enum_RenderingDevice_LogicOperation>]\ )
- [LogicOperation<enum_RenderingDevice_LogicOperation>] **get_logic_op**\ (\ )

The logic operation to perform for blending. Only effective if [enable_logic_op<class_RDPipelineColorBlendState_property_enable_logic_op>] is `true`.

