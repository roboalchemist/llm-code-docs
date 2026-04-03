:github_url: hide



# RDFramebufferPass

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Framebuffer pass attachment description (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This class contains the list of attachment descriptions for a framebuffer pass. Each points with an index to a previously supplied list of texture attachments.

Multipass framebuffers can optimize some configurations in mobile. On desktop, they provide little to no advantage.

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`color_attachments<class_RDFramebufferPass_property_color_attachments>`       | ``PackedInt32Array()`` |
> +-------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`int<class_int>`                           | :ref:`depth_attachment<class_RDFramebufferPass_property_depth_attachment>`         | ``-1``                 |
> +-------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`input_attachments<class_RDFramebufferPass_property_input_attachments>`       | ``PackedInt32Array()`` |
> +-------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`preserve_attachments<class_RDFramebufferPass_property_preserve_attachments>` | ``PackedInt32Array()`` |
> +-------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`resolve_attachments<class_RDFramebufferPass_property_resolve_attachments>`   | ``PackedInt32Array()`` |
> +-------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
>

----


## Constants



**ATTACHMENT_UNUSED** = `-1` [🔗<class_RDFramebufferPass_constant_ATTACHMENT_UNUSED>]

Attachment is unused.


----


## Property Descriptions



[PackedInt32Array<class_PackedInt32Array>] **color_attachments** = `PackedInt32Array()` [🔗<class_RDFramebufferPass_property_color_attachments>]


- |void| **set_color_attachments**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_color_attachments**\ (\ )

Color attachments in order starting from 0. If this attachment is not used by the shader, pass ATTACHMENT_UNUSED to skip.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[int<class_int>] **depth_attachment** = `-1` [🔗<class_RDFramebufferPass_property_depth_attachment>]


- |void| **set_depth_attachment**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_depth_attachment**\ (\ )

Depth attachment. ATTACHMENT_UNUSED should be used if no depth buffer is required for this pass.


----



[PackedInt32Array<class_PackedInt32Array>] **input_attachments** = `PackedInt32Array()` [🔗<class_RDFramebufferPass_property_input_attachments>]


- |void| **set_input_attachments**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_input_attachments**\ (\ )

Used for multipass framebuffers (more than one render pass). Converts an attachment to an input. Make sure to also supply it properly in the [RDUniform<class_RDUniform>] for the uniform set.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[PackedInt32Array<class_PackedInt32Array>] **preserve_attachments** = `PackedInt32Array()` [🔗<class_RDFramebufferPass_property_preserve_attachments>]


- |void| **set_preserve_attachments**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_preserve_attachments**\ (\ )

Attachments to preserve in this pass (otherwise they are erased).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[PackedInt32Array<class_PackedInt32Array>] **resolve_attachments** = `PackedInt32Array()` [🔗<class_RDFramebufferPass_property_resolve_attachments>]


- |void| **set_resolve_attachments**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_resolve_attachments**\ (\ )

If the color attachments are multisampled, non-multisampled resolve attachments can be provided.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.

