# OpenXRSpatialEntityExtension in English

# OpenXRSpatialEntityExtension

Experimental:This class may be changed or removed in future versions.
Inherits:OpenXRExtensionWrapper<Object
OpenXR extension that handles spatial entities.

## Description

OpenXR extension that handles spatial entities and, when enabled, allows querying those spatial entities. This extension will also automatically manageXRTrackerobjects for static entities.

## Methods

| RID | add_spatial_entity(spatial_context:RID, entity_id:int, entity:int) |
|---|---|
| OpenXRFutureResult | create_spatial_context(capability_configurations:Array[OpenXRSpatialCapabilityConfigurationBaseHeader], next:OpenXRStructureBase= null, user_callback:Callable= Callable()) |
| OpenXRFutureResult | discover_spatial_entities(spatial_context:RID, component_types:PackedInt64Array, next:OpenXRStructureBase= null, user_callback:Callable= Callable()) |
| RID | find_spatial_entity(entity_id:int) |
| void | free_spatial_context(spatial_context:RID) |
| void | free_spatial_entity(entity:RID) |
| void | free_spatial_snapshot(spatial_snapshot:RID) |
| PackedFloat32Array | get_float_buffer(spatial_snapshot:RID, buffer_id:int)const |
| int | get_spatial_context_handle(spatial_context:RID)const |
| bool | get_spatial_context_ready(spatial_context:RID)const |
| RID | get_spatial_entity_context(entity:RID)const |
| int | get_spatial_entity_id(entity:RID)const |
| RID | get_spatial_snapshot_context(spatial_snapshot:RID)const |
| int | get_spatial_snapshot_handle(spatial_snapshot:RID)const |
| String | get_string(spatial_snapshot:RID, buffer_id:int)const |
| PackedByteArray | get_uint8_buffer(spatial_snapshot:RID, buffer_id:int)const |
| PackedInt32Array | get_uint16_buffer(spatial_snapshot:RID, buffer_id:int)const |
| PackedInt32Array | get_uint32_buffer(spatial_snapshot:RID, buffer_id:int)const |
| PackedVector2Array | get_vector2_buffer(spatial_snapshot:RID, buffer_id:int)const |
| PackedVector3Array | get_vector3_buffer(spatial_snapshot:RID, buffer_id:int)const |
| RID | make_spatial_entity(spatial_context:RID, entity_id:int) |
| bool | query_snapshot(spatial_snapshot:RID, component_data:Array[OpenXRSpatialComponentData], next:OpenXRStructureBase= null) |
| bool | supports_capability(capability:Capability) |
| bool | supports_component_type(capability:Capability, component_type:ComponentType) |
| RID | update_spatial_entities(spatial_context:RID, entities:Array[RID], component_types:PackedInt64Array, next:OpenXRStructureBase= null) |

add_spatial_entity(spatial_context:RID, entity_id:int, entity:int)
OpenXRFutureResult
create_spatial_context(capability_configurations:Array[OpenXRSpatialCapabilityConfigurationBaseHeader], next:OpenXRStructureBase= null, user_callback:Callable= Callable())
OpenXRFutureResult
discover_spatial_entities(spatial_context:RID, component_types:PackedInt64Array, next:OpenXRStructureBase= null, user_callback:Callable= Callable())
find_spatial_entity(entity_id:int)
void
free_spatial_context(spatial_context:RID)
void
free_spatial_entity(entity:RID)
void
free_spatial_snapshot(spatial_snapshot:RID)
PackedFloat32Array
get_float_buffer(spatial_snapshot:RID, buffer_id:int)const
get_spatial_context_handle(spatial_context:RID)const
bool
get_spatial_context_ready(spatial_context:RID)const
get_spatial_entity_context(entity:RID)const
get_spatial_entity_id(entity:RID)const
get_spatial_snapshot_context(spatial_snapshot:RID)const
get_spatial_snapshot_handle(spatial_snapshot:RID)const
String
get_string(spatial_snapshot:RID, buffer_id:int)const
PackedByteArray
get_uint8_buffer(spatial_snapshot:RID, buffer_id:int)const
PackedInt32Array
get_uint16_buffer(spatial_snapshot:RID, buffer_id:int)const
PackedInt32Array
get_uint32_buffer(spatial_snapshot:RID, buffer_id:int)const
PackedVector2Array
get_vector2_buffer(spatial_snapshot:RID, buffer_id:int)const
PackedVector3Array
get_vector3_buffer(spatial_snapshot:RID, buffer_id:int)const
make_spatial_entity(spatial_context:RID, entity_id:int)
bool
query_snapshot(spatial_snapshot:RID, component_data:Array[OpenXRSpatialComponentData], next:OpenXRStructureBase= null)
bool
supports_capability(capability:Capability)
bool
supports_component_type(capability:Capability, component_type:ComponentType)
update_spatial_entities(spatial_context:RID, entities:Array[RID], component_types:PackedInt64Array, next:OpenXRStructureBase= null)

## Signals

spatial_discovery_recommended(spatial_context:RID)🔗
Emitted when OpenXR recommends running a discovery query because entities managed by this spatial context have (likely) changed.

## Enumerations

enumCapability:🔗
CapabilityCAPABILITY_PLANE_TRACKING=1000741000
Plane tracking capability.
CapabilityCAPABILITY_MARKER_TRACKING_QR_CODE=1000743000
QR code based marker tracking capability.
CapabilityCAPABILITY_MARKER_TRACKING_MICRO_QR_CODE=1000743001
Micro QR code based marker tracking capability.
CapabilityCAPABILITY_MARKER_TRACKING_ARUCO_MARKER=1000743002
Aruco marker based marker tracking capability.
CapabilityCAPABILITY_MARKER_TRACKING_APRIL_TAG=1000743003
April tag based marker tracking capability.
CapabilityCAPABILITY_ANCHOR=1000762000
Anchor capability.
enumComponentType:🔗
ComponentTypeCOMPONENT_TYPE_BOUNDED_2D=1
Component that provides the 2D bounds for a spatial entity. The corresponding list structure isXrSpatialComponentBounded2DListEXT; the corresponding data structure isXrSpatialBounded2DDataEXT.
ComponentTypeCOMPONENT_TYPE_BOUNDED_3D=2
Component that provides the 3D bounds for a spatial entity. The corresponding list structure isXrSpatialComponentBounded3DListEXT; the corresponding data structure isXrBoxf.
ComponentTypeCOMPONENT_TYPE_PARENT=3
Component that provides the XrSpatialEntityIdEXT of the parent for a spatial entity. The corresponding list structure isXrSpatialComponentParentListEXT; the corresponding data structure isXrSpatialEntityIdEXT.
ComponentTypeCOMPONENT_TYPE_MESH_3D=4
Component that provides a 3D mesh for a spatial entity. The corresponding list structure isXrSpatialComponentMesh3DListEXT; the corresponding data structure isXrSpatialMeshDataEXT.
ComponentTypeCOMPONENT_TYPE_PLANE_ALIGNMENT=1000741000
Component that provides the plane alignment enum for a spatial entity. The corresponding list structure isXrSpatialComponentPlaneAlignmentListEXT; the corresponding data structure isXrSpatialPlaneAlignmentEXT(Added by theXR_EXT_spatial_plane_trackingextension).
ComponentTypeCOMPONENT_TYPE_MESH_2D=1000741001
Component that provides a 2D mesh for a spatial entity. The corresponding list structure isXrSpatialComponentMesh2DListEXT; the corresponding data structure isXrSpatialMeshDataEXT(Added by theXR_EXT_spatial_plane_trackingextension).
ComponentTypeCOMPONENT_TYPE_POLYGON_2D=1000741002
Component that provides a 2D boundary polygon for a spatial entity. The corresponding list structure isXrSpatialComponentPolygon2DListEXT; the corresponding data structure isXrSpatialPolygon2DDataEXT(Added by theXR_EXT_spatial_plane_trackingextension).
ComponentTypeCOMPONENT_TYPE_PLANE_SEMANTIC_LABEL=1000741003
Component that provides a semantic label for a plane. The corresponding list structure isXrSpatialComponentPlaneSemanticLabelListEXT; the corresponding data structure isXrSpatialPlaneSemanticLabelEXT(Added by theXR_EXT_spatial_plane_trackingextension).
ComponentTypeCOMPONENT_TYPE_MARKER=1000743000
A component describing the marker type, ID and location. The corresponding list structure isXrSpatialComponentMarkerListEXT; the corresponding data structure isXrSpatialMarkerDataEXT(Added by theXR_EXT_spatial_marker_trackingextension).
ComponentTypeCOMPONENT_TYPE_ANCHOR=1000762000
Component that provides the location for an anchor. The corresponding list structure isXrSpatialComponentAnchorListEXT; the corresponding data structure isXrPosef(Added by theXR_EXT_spatial_anchorextension).
ComponentTypeCOMPONENT_TYPE_PERSISTENCE=1000763000
Component that provides the persisted UUID for a spatial entity. The corresponding list structure isXrSpatialComponentPersistenceListEXT;thecorrespondingdatastructureis[code]XrSpatialPersistenceDataEXT(Added by theXR_EXT_spatial_persistenceextension).

## Method Descriptions

RIDadd_spatial_entity(spatial_context:RID, entity_id:int, entity:int)🔗
Registers an entity that was created directly on the OpenXR runtime.
OpenXRFutureResultcreate_spatial_context(capability_configurations:Array[OpenXRSpatialCapabilityConfigurationBaseHeader], next:OpenXRStructureBase= null, user_callback:Callable= Callable())🔗
Creates a new spatial context that handles entities for the provided capability configurations.capability_configurationsis an array ofOpenXRSpatialCapabilityConfigurationBaseHeaderwith the needed capability configuration data.
nextis an optional parameter that can contain additional information for creating our spatial context.
Note:This is an asynchronous method and returns anOpenXRFutureResultobject with which to track the status, discarding this object will not cancel the creation process. On successuser_callbackwill be called if specified. The result data for this function is theRIDfor our spatial context.
OpenXRFutureResultdiscover_spatial_entities(spatial_context:RID, component_types:PackedInt64Array, next:OpenXRStructureBase= null, user_callback:Callable= Callable())🔗
Starts a new discovery query, this will gather all objects tracked by thespatial_contextthat have at least one of the component types specified incomponent_types.
nextis an optional parameter that can contain additional information for executing the discovery query.
Note:This is an asynchronous method and returns anOpenXRFutureResultobject with which to track the status, discarding this object will not cancel the discovery process. On successuser_callbackwill be called if specified. The result data for this function is theRIDfor our snapshot.
RIDfind_spatial_entity(entity_id:int)🔗
Returns theRIDfor the specified spatial entity ID.
voidfree_spatial_context(spatial_context:RID)🔗
Frees a spatial context previously created when callingcreate_spatial_context(). If the spatial context creation is still ongoing, the asynchronous process is cancelled.
voidfree_spatial_entity(entity:RID)🔗
Frees an entity previously created when callingadd_spatial_entity()ormake_spatial_entity().
voidfree_spatial_snapshot(spatial_snapshot:RID)🔗
Frees a spatial snapshot previously created when callingdiscover_spatial_entities(). If the spatial snapshot creation is still ongoing, the asynchronous process is cancelled.
PackedFloat32Arrayget_float_buffer(spatial_snapshot:RID, buffer_id:int)const🔗
Returns a buffer with floats from a buffer that was retrieved when taking a snapshot.
intget_spatial_context_handle(spatial_context:RID)const🔗
Returns the OpenXR spatial context handle for this snapshot.
Note:This method is intended to be used from GDExtensions that implement spatial entity capability handlers.
boolget_spatial_context_ready(spatial_context:RID)const🔗
Returnstrueif the spatial context finished its creation and is ready to be used.
RIDget_spatial_entity_context(entity:RID)const🔗
Returns the spatial context for this entity.
intget_spatial_entity_id(entity:RID)const🔗
Returns the internalXrSpatialEntityIdEXTassociated with the entity.
RIDget_spatial_snapshot_context(spatial_snapshot:RID)const🔗
Returns the spatial context related to this spatial snapshot.
intget_spatial_snapshot_handle(spatial_snapshot:RID)const🔗
Returns the OpenXR spatial snapshot handle for this snapshot.
Note:This method is intended to be used from GDExtensions that implement spatial entity capability handlers.
Stringget_string(spatial_snapshot:RID, buffer_id:int)const🔗
Returns a string from a buffer that was retrieved when taking a snapshot.
PackedByteArrayget_uint8_buffer(spatial_snapshot:RID, buffer_id:int)const🔗
Returns a buffer with 8 bit ints from a buffer that was retrieved when taking a snapshot.
PackedInt32Arrayget_uint16_buffer(spatial_snapshot:RID, buffer_id:int)const🔗
Returns a buffer with 16 bit ints from a buffer that was retrieved when taking a snapshot.
PackedInt32Arrayget_uint32_buffer(spatial_snapshot:RID, buffer_id:int)const🔗
Returns a buffer with 32 bit ints from a buffer that was retrieved when taking a snapshot.
PackedVector2Arrayget_vector2_buffer(spatial_snapshot:RID, buffer_id:int)const🔗
Returns a buffer withVector2entries from a buffer that was retrieved when taking a snapshot.
PackedVector3Arrayget_vector3_buffer(spatial_snapshot:RID, buffer_id:int)const🔗
Returns a buffer withVector3entries from a buffer that was retrieved when taking a snapshot.
RIDmake_spatial_entity(spatial_context:RID, entity_id:int)🔗
Creates a new entity for thisentity_id. Thespatial_contextshould match the context that discovered the entity.
boolquery_snapshot(spatial_snapshot:RID, component_data:Array[OpenXRSpatialComponentData], next:OpenXRStructureBase= null)🔗
Queries the snapshot data. This will find all entities in the snapshot that contain all requested components incomponent_data. The objects held withincomponent_datawill then be populated with the queried data.component_datamust always have an object ofOpenXRSpatialQueryResultDataas the first entry.
nextis an optional parameter that can contain additional information passed when setting our query conditions.
boolsupports_capability(capability:Capability)🔗
Returnstrueif this spatial entitycapabilityis supported by the hardware used.
boolsupports_component_type(capability:Capability, component_type:ComponentType)🔗
Returnstrueif thiscapabilitysupports thecomponent_type.
RIDupdate_spatial_entities(spatial_context:RID, entities:Array[RID], component_types:PackedInt64Array, next:OpenXRStructureBase= null)🔗
Performs a snapshot for a limited number of entities. This is NOT an asynchronous method and will return the snapshot immediately.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
