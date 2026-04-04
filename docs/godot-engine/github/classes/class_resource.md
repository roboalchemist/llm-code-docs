:github_url: hide



# Resource

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [Animation<class_Animation>], [AnimationLibrary<class_AnimationLibrary>], [AnimationNode<class_AnimationNode>], [AnimationNodeStateMachinePlayback<class_AnimationNodeStateMachinePlayback>], [AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>], [AudioBusLayout<class_AudioBusLayout>], [AudioEffect<class_AudioEffect>], [AudioStream<class_AudioStream>], [BitMap<class_BitMap>], [BoneMap<class_BoneMap>], [ButtonGroup<class_ButtonGroup>], [CameraAttributes<class_CameraAttributes>], [ColorPalette<class_ColorPalette>], [Compositor<class_Compositor>], [CompositorEffect<class_CompositorEffect>], [CryptoKey<class_CryptoKey>], [Curve<class_Curve>], [Curve2D<class_Curve2D>], [Curve3D<class_Curve3D>], [EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>], [EditorSettings<class_EditorSettings>], [Environment<class_Environment>], [FoldableGroup<class_FoldableGroup>], [Font<class_Font>], [GDExtension<class_GDExtension>], [GLTFAccessor<class_GLTFAccessor>], [GLTFAnimation<class_GLTFAnimation>], [GLTFBufferView<class_GLTFBufferView>], [GLTFCamera<class_GLTFCamera>], [GLTFDocument<class_GLTFDocument>], [GLTFDocumentExtension<class_GLTFDocumentExtension>], [GLTFLight<class_GLTFLight>], [GLTFMesh<class_GLTFMesh>], [GLTFNode<class_GLTFNode>], [GLTFPhysicsBody<class_GLTFPhysicsBody>], [GLTFPhysicsShape<class_GLTFPhysicsShape>], [GLTFSkeleton<class_GLTFSkeleton>], [GLTFSkin<class_GLTFSkin>], [GLTFSpecGloss<class_GLTFSpecGloss>], [GLTFState<class_GLTFState>], [GLTFTexture<class_GLTFTexture>], [GLTFTextureSampler<class_GLTFTextureSampler>], [Gradient<class_Gradient>], [Image<class_Image>], [ImporterMesh<class_ImporterMesh>], [InputEvent<class_InputEvent>], [JointLimitation3D<class_JointLimitation3D>], [JSON<class_JSON>], [LabelSettings<class_LabelSettings>], [LightmapGIData<class_LightmapGIData>], [Material<class_Material>], [Mesh<class_Mesh>], [MeshLibrary<class_MeshLibrary>], [MissingResource<class_MissingResource>], [MultiMesh<class_MultiMesh>], [NavigationMesh<class_NavigationMesh>], [NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>], [NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>], [NavigationPolygon<class_NavigationPolygon>], [Noise<class_Noise>], [Occluder3D<class_Occluder3D>], [OccluderPolygon2D<class_OccluderPolygon2D>], [OggPacketSequence<class_OggPacketSequence>], [OpenXRAction<class_OpenXRAction>], [OpenXRActionMap<class_OpenXRActionMap>], [OpenXRActionSet<class_OpenXRActionSet>], [OpenXRBindingModifier<class_OpenXRBindingModifier>], [OpenXRHapticBase<class_OpenXRHapticBase>], [OpenXRInteractionProfile<class_OpenXRInteractionProfile>], [OpenXRIPBinding<class_OpenXRIPBinding>], [PackedDataContainer<class_PackedDataContainer>], [PackedScene<class_PackedScene>], [PhysicsMaterial<class_PhysicsMaterial>], [PolygonPathFinder<class_PolygonPathFinder>], [RDShaderFile<class_RDShaderFile>], [RDShaderSPIRV<class_RDShaderSPIRV>], [RichTextEffect<class_RichTextEffect>], [SceneReplicationConfig<class_SceneReplicationConfig>], [Script<class_Script>], [Shader<class_Shader>], [ShaderInclude<class_ShaderInclude>], [Shape2D<class_Shape2D>], [Shape3D<class_Shape3D>], [Shortcut<class_Shortcut>], [SkeletonModification2D<class_SkeletonModification2D>], [SkeletonModificationStack2D<class_SkeletonModificationStack2D>], [SkeletonProfile<class_SkeletonProfile>], [Skin<class_Skin>], [Sky<class_Sky>], [SpriteFrames<class_SpriteFrames>], [StyleBox<class_StyleBox>], [SyntaxHighlighter<class_SyntaxHighlighter>], [Texture<class_Texture>], [Theme<class_Theme>], [TileMapPattern<class_TileMapPattern>], [TileSet<class_TileSet>], [TileSetSource<class_TileSetSource>], [Translation<class_Translation>], [VideoStream<class_VideoStream>], [VideoStreamPlayback<class_VideoStreamPlayback>], [VisualShaderNode<class_VisualShaderNode>], [VoxelGIData<class_VoxelGIData>], [World2D<class_World2D>], [World3D<class_World3D>], [X509Certificate<class_X509Certificate>]

Base class for serializable objects.


## Description

Resource is the base class for all Godot-specific resource types, serving primarily as data containers. Since they inherit from [RefCounted<class_RefCounted>], resources are reference-counted and freed when no longer in use. They can also be nested within other resources, and saved on disk. [PackedScene<class_PackedScene>], one of the most common [Object<class_Object>]\ s in a Godot project, is also a resource, uniquely capable of storing and instantiating the [Node<class_Node>]\ s it contains as many times as desired.

In GDScript, resources can loaded from disk by their [resource_path<class_Resource_property_resource_path>] using [@GDScript.load()<class_@GDScript_method_load>] or [@GDScript.preload()<class_@GDScript_method_preload>].

The engine keeps a global cache of all loaded resources, referenced by paths (see [ResourceLoader.has_cached()<class_ResourceLoader_method_has_cached>]). A resource will be cached when loaded for the first time and removed from cache once all references are released. When a resource is cached, subsequent loads using its path will return the cached reference.

\ **Note:** In C#, resources will not be freed instantly after they are no longer in use. Instead, garbage collection will run periodically and will free resources that are no longer in use. This means that unused resources will remain in memory for a while before being removed.


## Tutorials

- [../tutorials/scripting/resources](Resources .md)

- [../tutorials/best_practices/node_alternatives](When and how to avoid using nodes for everything .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`resource_local_to_scene<class_Resource_property_resource_local_to_scene>`   | ``false`` |
> +-----------------------------+-----------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>` | :ref:`resource_name<class_Resource_property_resource_name>`                       | ``""``    |
> +-----------------------------+-----------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>` | :ref:`resource_path<class_Resource_property_resource_path>`                       | ``""``    |
> +-----------------------------+-----------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>` | :ref:`resource_scene_unique_id<class_Resource_property_resource_scene_unique_id>` |           |
> +-----------------------------+-----------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`           | :ref:`_get_rid<class_Resource_private_method__get_rid>`\ (\ ) |virtual| |const|                                                                                   |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`_reset_state<class_Resource_private_method__reset_state>`\ (\ ) |virtual|                                                                                   |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`_set_path_cache<class_Resource_private_method__set_path_cache>`\ (\ path\: :ref:`String<class_String>`\ ) |virtual| |const|                                 |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`_setup_local_to_scene<class_Resource_private_method__setup_local_to_scene>`\ (\ ) |virtual|                                                                 |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Resource<class_Resource>` | :ref:`duplicate<class_Resource_method_duplicate>`\ (\ deep\: :ref:`bool<class_bool>` = false\ ) |const|                                                           |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Resource<class_Resource>` | :ref:`duplicate_deep<class_Resource_method_duplicate_deep>`\ (\ deep_subresources_mode\: :ref:`DeepDuplicateMode<enum_Resource_DeepDuplicateMode>` = 1\ ) |const| |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`emit_changed<class_Resource_method_emit_changed>`\ (\ )                                                                                                     |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`     | :ref:`generate_scene_unique_id<class_Resource_method_generate_scene_unique_id>`\ (\ ) |static|                                                                    |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`     | :ref:`get_id_for_path<class_Resource_method_get_id_for_path>`\ (\ path\: :ref:`String<class_String>`\ ) |const|                                                   |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Node<class_Node>`         | :ref:`get_local_scene<class_Resource_method_get_local_scene>`\ (\ ) |const|                                                                                       |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`           | :ref:`get_rid<class_Resource_method_get_rid>`\ (\ ) |const|                                                                                                       |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`is_built_in<class_Resource_method_is_built_in>`\ (\ ) |const|                                                                                               |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`reset_state<class_Resource_method_reset_state>`\ (\ )                                                                                                       |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`set_id_for_path<class_Resource_method_set_id_for_path>`\ (\ path\: :ref:`String<class_String>`, id\: :ref:`String<class_String>`\ )                         |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`set_path_cache<class_Resource_method_set_path_cache>`\ (\ path\: :ref:`String<class_String>`\ )                                                             |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`setup_local_to_scene<class_Resource_method_setup_local_to_scene>`\ (\ )                                                                                     |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`take_over_path<class_Resource_method_take_over_path>`\ (\ path\: :ref:`String<class_String>`\ )                                                             |
> +---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**changed**\ (\ ) [🔗<class_Resource_signal_changed>]

Emitted when the resource changes, usually when one of its properties is modified. See also [emit_changed()<class_Resource_method_emit_changed>].

\ **Note:** This signal is not emitted automatically for properties of custom resources. If necessary, a setter needs to be created to emit the signal.


----



**setup_local_to_scene_requested**\ (\ ) [🔗<class_Resource_signal_setup_local_to_scene_requested>]

**Deprecated:** This signal is only emitted when the resource is created. Override [_setup_local_to_scene()<class_Resource_private_method__setup_local_to_scene>] instead.

Emitted by a newly duplicated resource with [resource_local_to_scene<class_Resource_property_resource_local_to_scene>] set to `true`.


----


## Enumerations



enum **DeepDuplicateMode**: [🔗<enum_Resource_DeepDuplicateMode>]



[DeepDuplicateMode<enum_Resource_DeepDuplicateMode>] **DEEP_DUPLICATE_NONE** = `0`

No subresorces at all are duplicated. This is useful even in a deep duplication to have all the arrays and dictionaries duplicated but still pointing to the original resources.



[DeepDuplicateMode<enum_Resource_DeepDuplicateMode>] **DEEP_DUPLICATE_INTERNAL** = `1`

Only subresources without a path or with a scene-local path will be duplicated.



[DeepDuplicateMode<enum_Resource_DeepDuplicateMode>] **DEEP_DUPLICATE_ALL** = `2`

Every subresource found will be duplicated, even if it has a non-local path. In other words, even potentially big resources stored separately will be duplicated.


----


## Property Descriptions



[bool<class_bool>] **resource_local_to_scene** = `false` [🔗<class_Resource_property_resource_local_to_scene>]


- |void| **set_local_to_scene**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_local_to_scene**\ (\ )

If `true`, the resource is duplicated for each instance of all scenes using it. At run-time, the resource can be modified in one scene without affecting other instances (see [PackedScene.instantiate()<class_PackedScene_method_instantiate>]).

\ **Note:** Changing this property at run-time has no effect on already created duplicate resources.


----



[String<class_String>] **resource_name** = `""` [🔗<class_Resource_property_resource_name>]


- |void| **set_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_name**\ (\ )

An optional name for this resource. When defined, its value is displayed to represent the resource in the Inspector dock. For built-in scripts, the name is displayed as part of the tab name in the script editor.

\ **Note:** Some resource formats do not support resource names. You can still set the name in the editor or via code, but it will be lost when the resource is reloaded. For example, only built-in scripts can have a resource name, while scripts stored in separate files cannot.


----



[String<class_String>] **resource_path** = `""` [🔗<class_Resource_property_resource_path>]


- |void| **set_path**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_path**\ (\ )

The unique path to this resource. If it has been saved to disk, the value will be its filepath. If the resource is exclusively contained within a scene, the value will be the [PackedScene<class_PackedScene>]'s filepath, followed by a unique identifier.

\ **Note:** Setting this property manually may fail if a resource with the same path has already been previously loaded. If necessary, use [take_over_path()<class_Resource_method_take_over_path>].


----



[String<class_String>] **resource_scene_unique_id** [🔗<class_Resource_property_resource_scene_unique_id>]


- |void| **set_scene_unique_id**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_scene_unique_id**\ (\ )

A unique identifier relative to the this resource's scene. If left empty, the ID is automatically generated when this resource is saved inside a [PackedScene<class_PackedScene>]. If the resource is not inside a scene, this property is empty by default.

\ **Note:** When the [PackedScene<class_PackedScene>] is saved, if multiple resources in the same scene use the same ID, only the earliest resource in the scene hierarchy keeps the original ID. The other resources are assigned new IDs from [generate_scene_unique_id()<class_Resource_method_generate_scene_unique_id>].

\ **Note:** Setting this property does not emit the [changed<class_Resource_signal_changed>] signal.

\ **Warning:** When setting, the ID must only consist of letters, numbers, and underscores. Otherwise, it will fail and default to a randomly generated ID.


----


## Method Descriptions



[RID<class_RID>] **_get_rid**\ (\ ) |virtual| |const| [🔗<class_Resource_private_method__get_rid>]

Override this method to return a custom [RID<class_RID>] when [get_rid()<class_Resource_method_get_rid>] is called.


----



|void| **_reset_state**\ (\ ) |virtual| [🔗<class_Resource_private_method__reset_state>]

For resources that store state in non-exported properties, such as via [Object._validate_property()<class_Object_private_method__validate_property>] or [Object._get_property_list()<class_Object_private_method__get_property_list>], this method must be implemented to clear them.


----



|void| **_set_path_cache**\ (\ path\: [String<class_String>]\ ) |virtual| |const| [🔗<class_Resource_private_method__set_path_cache>]

Override this method to execute additional logic after [set_path_cache()<class_Resource_method_set_path_cache>] is called on this object.


----



|void| **_setup_local_to_scene**\ (\ ) |virtual| [🔗<class_Resource_private_method__setup_local_to_scene>]

Override this method to customize the newly duplicated resource created from [PackedScene.instantiate()<class_PackedScene_method_instantiate>], if the original's [resource_local_to_scene<class_Resource_property_resource_local_to_scene>] is set to `true`.

\ **Example:** Set a random `damage` value to every local resource from an instantiated scene:

::

    extends Resource

    var damage = 0

    func _setup_local_to_scene():
        damage = randi_range(10, 40)


----



[Resource<class_Resource>] **duplicate**\ (\ deep\: [bool<class_bool>] = false\ ) |const| [🔗<class_Resource_method_duplicate>]

Duplicates this resource, returning a new resource with its `export`\ ed or [@GlobalScope.PROPERTY_USAGE_STORAGE<class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE>] properties copied from the original.

If `deep` is `false`, a **shallow** copy is returned: nested [Array<class_Array>], [Dictionary<class_Dictionary>], and **Resource** properties are not duplicated and are shared with the original resource.

If `deep` is `true`, a **deep** copy is returned: all nested arrays, dictionaries, and packed arrays are also duplicated (recursively). Any **Resource** found inside will only be duplicated if it's local, like [DEEP_DUPLICATE_INTERNAL<class_Resource_constant_DEEP_DUPLICATE_INTERNAL>] used with [duplicate_deep()<class_Resource_method_duplicate_deep>].

The following exceptions apply:

- Subresource properties with the [@GlobalScope.PROPERTY_USAGE_ALWAYS_DUPLICATE<class_@GlobalScope_constant_PROPERTY_USAGE_ALWAYS_DUPLICATE>] flag are always duplicated (recursively or not, depending on `deep`).

- Subresource properties with the [@GlobalScope.PROPERTY_USAGE_NEVER_DUPLICATE<class_@GlobalScope_constant_PROPERTY_USAGE_NEVER_DUPLICATE>] flag are never duplicated.

\ **Note:** For custom resources, this method will fail if [Object._init()<class_Object_private_method__init>] has been defined with required parameters.

\ **Note:** When duplicating with `deep` set to `true`, each resource found, including the one on which this method is called, will be only duplicated once and referenced as many times as needed in the duplicate. For instance, if you are duplicating resource A that happens to have resource B referenced twice, you'll get a new resource A' referencing a new resource B' twice.


----



[Resource<class_Resource>] **duplicate_deep**\ (\ deep_subresources_mode\: [DeepDuplicateMode<enum_Resource_DeepDuplicateMode>] = 1\ ) |const| [🔗<class_Resource_method_duplicate_deep>]

Duplicates this resource, deeply, like [duplicate()<class_Resource_method_duplicate>] when passing `true`, with extra control over how subresources are handled.


----



|void| **emit_changed**\ (\ ) [🔗<class_Resource_method_emit_changed>]

Emits the [changed<class_Resource_signal_changed>] signal. This method is called automatically for some built-in resources.

\ **Note:** For custom resources, it's recommended to call this method whenever a meaningful change occurs, such as a modified property. This ensures that custom [Object<class_Object>]\ s depending on the resource are properly updated.

::

    var damage:
        set(new_value):
            if damage != new_value:
                damage = new_value
                emit_changed()


----



[String<class_String>] **generate_scene_unique_id**\ (\ ) |static| [🔗<class_Resource_method_generate_scene_unique_id>]

Generates a unique identifier for a resource to be contained inside a [PackedScene<class_PackedScene>], based on the current date, time, and a random value. The returned string is only composed of letters (`a` to `y`) and numbers (`0` to `8`). See also [resource_scene_unique_id<class_Resource_property_resource_scene_unique_id>].


----



[String<class_String>] **get_id_for_path**\ (\ path\: [String<class_String>]\ ) |const| [🔗<class_Resource_method_get_id_for_path>]

From the internal cache for scene-unique IDs, returns the ID of this resource for the scene at `path`. If there is no entry, an empty string is returned. Useful to keep scene-unique IDs the same when implementing a VCS-friendly custom resource format by extending [ResourceFormatLoader<class_ResourceFormatLoader>] and [ResourceFormatSaver<class_ResourceFormatSaver>].

\ **Note:** This method is only implemented when running in an editor context. At runtime, it returns an empty string.


----



[Node<class_Node>] **get_local_scene**\ (\ ) |const| [🔗<class_Resource_method_get_local_scene>]

If [resource_local_to_scene<class_Resource_property_resource_local_to_scene>] is set to `true` and the resource has been loaded from a [PackedScene<class_PackedScene>] instantiation, returns the root [Node<class_Node>] of the scene where this resource is used. Otherwise, returns `null`.


----



[RID<class_RID>] **get_rid**\ (\ ) |const| [🔗<class_Resource_method_get_rid>]

Returns the [RID<class_RID>] of this resource (or an empty RID). Many resources (such as [Texture2D<class_Texture2D>], [Mesh<class_Mesh>], and so on) are high-level abstractions of resources stored in a specialized server ([DisplayServer<class_DisplayServer>], [RenderingServer<class_RenderingServer>], etc.), so this function will return the original [RID<class_RID>].


----



[bool<class_bool>] **is_built_in**\ (\ ) |const| [🔗<class_Resource_method_is_built_in>]

Returns `true` if the resource is saved on disk as a part of another resource's file.


----



|void| **reset_state**\ (\ ) [🔗<class_Resource_method_reset_state>]

Makes the resource clear its non-exported properties. See also [_reset_state()<class_Resource_private_method__reset_state>]. Useful when implementing a custom resource format by extending [ResourceFormatLoader<class_ResourceFormatLoader>] and [ResourceFormatSaver<class_ResourceFormatSaver>].


----



|void| **set_id_for_path**\ (\ path\: [String<class_String>], id\: [String<class_String>]\ ) [🔗<class_Resource_method_set_id_for_path>]

In the internal cache for scene-unique IDs, sets the ID of this resource to `id` for the scene at `path`. If `id` is empty, the cache entry for `path` is cleared. Useful to keep scene-unique IDs the same when implementing a VCS-friendly custom resource format by extending [ResourceFormatLoader<class_ResourceFormatLoader>] and [ResourceFormatSaver<class_ResourceFormatSaver>].

\ **Note:** This method is only implemented when running in an editor context.


----



|void| **set_path_cache**\ (\ path\: [String<class_String>]\ ) [🔗<class_Resource_method_set_path_cache>]

Sets the resource's path to `path` without involving the resource cache. Useful for handling [CacheMode<enum_ResourceFormatLoader_CacheMode>] values when implementing a custom resource format by extending [ResourceFormatLoader<class_ResourceFormatLoader>] and [ResourceFormatSaver<class_ResourceFormatSaver>].


----



|void| **setup_local_to_scene**\ (\ ) [🔗<class_Resource_method_setup_local_to_scene>]

**Deprecated:** This method should only be called internally.

Calls [_setup_local_to_scene()<class_Resource_private_method__setup_local_to_scene>]. If [resource_local_to_scene<class_Resource_property_resource_local_to_scene>] is set to `true`, this method is automatically called from [PackedScene.instantiate()<class_PackedScene_method_instantiate>] by the newly duplicated resource within the scene instance.


----



|void| **take_over_path**\ (\ path\: [String<class_String>]\ ) [🔗<class_Resource_method_take_over_path>]

Sets the [resource_path<class_Resource_property_resource_path>] to `path`, potentially overriding an existing cache entry for this path. Further attempts to load an overridden resource by path will instead return this resource.

