:github_url: hide



# ResourceImporter

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [EditorImportPlugin<class_EditorImportPlugin>], [ResourceImporterBitMap<class_ResourceImporterBitMap>], [ResourceImporterBMFont<class_ResourceImporterBMFont>], [ResourceImporterCSVTranslation<class_ResourceImporterCSVTranslation>], [ResourceImporterDynamicFont<class_ResourceImporterDynamicFont>], [ResourceImporterImage<class_ResourceImporterImage>], [ResourceImporterImageFont<class_ResourceImporterImageFont>], [ResourceImporterLayeredTexture<class_ResourceImporterLayeredTexture>], [ResourceImporterMP3<class_ResourceImporterMP3>], [ResourceImporterOBJ<class_ResourceImporterOBJ>], [ResourceImporterOggVorbis<class_ResourceImporterOggVorbis>], [ResourceImporterScene<class_ResourceImporterScene>], [ResourceImporterShaderFile<class_ResourceImporterShaderFile>], [ResourceImporterSVG<class_ResourceImporterSVG>], [ResourceImporterTexture<class_ResourceImporterTexture>], [ResourceImporterTextureAtlas<class_ResourceImporterTextureAtlas>], [ResourceImporterWAV<class_ResourceImporterWAV>]

Base class for resource importers.


## Description

This is the base class for Godot's resource importers. To implement your own resource importers using editor plugins, see [EditorImportPlugin<class_EditorImportPlugin>].


## Tutorials

- [../tutorials/plugins/editor/import_plugins](Import plugins .md)


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`_get_build_dependencies<class_ResourceImporter_private_method__get_build_dependencies>`\ (\ path\: :ref:`String<class_String>`\ ) |virtual| |const| |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ImportOrder**: [🔗<enum_ResourceImporter_ImportOrder>]



[ImportOrder<enum_ResourceImporter_ImportOrder>] **IMPORT_ORDER_DEFAULT** = `0`

The default import order.



[ImportOrder<enum_ResourceImporter_ImportOrder>] **IMPORT_ORDER_SCENE** = `100`

The import order for scenes, which ensures scenes are imported *after* all other core resources such as textures. Custom importers should generally have an import order lower than `100` to avoid issues when importing scenes that rely on custom resources.


----


## Method Descriptions



[PackedStringArray<class_PackedStringArray>] **_get_build_dependencies**\ (\ path\: [String<class_String>]\ ) |virtual| |const| [🔗<class_ResourceImporter_private_method__get_build_dependencies>]

Called when the engine compilation profile editor wants to check what build options an imported resource needs. For example, [ResourceImporterDynamicFont<class_ResourceImporterDynamicFont>] has a property called [ResourceImporterDynamicFont.multichannel_signed_distance_field<class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field>], that depends on the engine to be build with the "msdfgen" module. If that resource happened to be a custom one, it would be handled like this:

::

    func _get_build_dependencies(path):
        var resource = load(path)
        var dependencies = PackedStringArray()

        if resource.multichannel_signed_distance_field:
            dependencies.push_back("module_msdfgen_enabled")

        return dependencies

