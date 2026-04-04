:github_url: hide



# EditorResourceConversionPlugin

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Plugin for adding custom converters from one resource format to another in the editor resource picker context menu; for example, converting a [StandardMaterial3D<class_StandardMaterial3D>] to a [ShaderMaterial<class_ShaderMaterial>].


## Description

**EditorResourceConversionPlugin** is invoked when the context menu is brought up for a resource in the editor inspector. Relevant conversion plugins will appear as menu options to convert the given resource to a target type.

Below shows an example of a basic plugin that will convert an [ImageTexture<class_ImageTexture>] to a [PortableCompressedTexture2D<class_PortableCompressedTexture2D>].


> **TABS**
>

    extends EditorResourceConversionPlugin

    func _handles(resource: Resource):
        return resource is ImageTexture

    func _converts_to():
        return "PortableCompressedTexture2D"

    func _convert(itex: Resource):
        var ptex = PortableCompressedTexture2D.new()
        ptex.create_from_image(itex.get_image(), PortableCompressedTexture2D.COMPRESSION_MODE_LOSSLESS)
        return ptex



To use an **EditorResourceConversionPlugin**, register it using the [EditorPlugin.add_resource_conversion_plugin()<class_EditorPlugin_method_add_resource_conversion_plugin>] method first.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Resource<class_Resource>` | :ref:`_convert<class_EditorResourceConversionPlugin_private_method__convert>`\ (\ resource\: :ref:`Resource<class_Resource>`\ ) |virtual| |const| |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`     | :ref:`_converts_to<class_EditorResourceConversionPlugin_private_method__converts_to>`\ (\ ) |virtual| |const|                                     |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`_handles<class_EditorResourceConversionPlugin_private_method__handles>`\ (\ resource\: :ref:`Resource<class_Resource>`\ ) |virtual| |const| |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Resource<class_Resource>] **_convert**\ (\ resource\: [Resource<class_Resource>]\ ) |virtual| |const| [🔗<class_EditorResourceConversionPlugin_private_method__convert>]

Takes an input [Resource<class_Resource>] and converts it to the type given in [_converts_to()<class_EditorResourceConversionPlugin_private_method__converts_to>]. The returned [Resource<class_Resource>] is the result of the conversion, and the input [Resource<class_Resource>] remains unchanged.


----



[String<class_String>] **_converts_to**\ (\ ) |virtual| |const| [🔗<class_EditorResourceConversionPlugin_private_method__converts_to>]

Returns the class name of the target type of [Resource<class_Resource>] that this plugin converts source resources to.


----



[bool<class_bool>] **_handles**\ (\ resource\: [Resource<class_Resource>]\ ) |virtual| |const| [🔗<class_EditorResourceConversionPlugin_private_method__handles>]

Called to determine whether a particular [Resource<class_Resource>] can be converted to the target resource type by this plugin.

