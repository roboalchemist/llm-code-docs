# EditorNode3DGizmo in English

# EditorNode3DGizmo

Inherits:Node3DGizmo<RefCounted<Object
Gizmo for editingNode3Dobjects.

## Description

Gizmo that is used for providing custom visualization and editing (handles and subgizmos) forNode3Dobjects. Can be overridden to create custom gizmos, but for simple gizmos creating anEditorNode3DGizmoPluginis usually recommended.

## Methods

| void | _begin_handle_action(id:int, secondary:bool)virtual |
|---|---|
| void | _commit_handle(id:int, secondary:bool, restore:Variant, cancel:bool)virtual |
| void | _commit_subgizmos(ids:PackedInt32Array, restores:Array[Transform3D], cancel:bool)virtual |
| String | _get_handle_name(id:int, secondary:bool)virtualconst |
| Variant | _get_handle_value(id:int, secondary:bool)virtualconst |
| Transform3D | _get_subgizmo_transform(id:int)virtualconst |
| bool | _is_handle_highlighted(id:int, secondary:bool)virtualconst |
| void | _redraw()virtual |
| void | _set_handle(id:int, secondary:bool, camera:Camera3D, point:Vector2)virtual |
| void | _set_subgizmo_transform(id:int, transform:Transform3D)virtual |
| PackedInt32Array | _subgizmos_intersect_frustum(camera:Camera3D, frustum:Array[Plane])virtualconst |
| int | _subgizmos_intersect_ray(camera:Camera3D, point:Vector2)virtualconst |
| void | add_collision_segments(segments:PackedVector3Array) |
| void | add_collision_triangles(triangles:TriangleMesh) |
| void | add_handles(handles:PackedVector3Array, material:Material, ids:PackedInt32Array, billboard:bool= false, secondary:bool= false) |
| void | add_lines(lines:PackedVector3Array, material:Material, billboard:bool= false, modulate:Color= Color(1, 1, 1, 1)) |
| void | add_mesh(mesh:Mesh, material:Material= null, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton:SkinReference= null) |
| void | add_unscaled_billboard(material:Material, default_scale:float= 1, modulate:Color= Color(1, 1, 1, 1)) |
| void | clear() |
| Node3D | get_node_3d()const |
| EditorNode3DGizmoPlugin | get_plugin()const |
| PackedInt32Array | get_subgizmo_selection()const |
| bool | is_subgizmo_selected(id:int)const |
| void | set_hidden(hidden:bool) |
| void | set_node_3d(node:Node) |

void
_begin_handle_action(id:int, secondary:bool)virtual
void
_commit_handle(id:int, secondary:bool, restore:Variant, cancel:bool)virtual
void
_commit_subgizmos(ids:PackedInt32Array, restores:Array[Transform3D], cancel:bool)virtual
String
_get_handle_name(id:int, secondary:bool)virtualconst
Variant
_get_handle_value(id:int, secondary:bool)virtualconst
Transform3D
_get_subgizmo_transform(id:int)virtualconst
bool
_is_handle_highlighted(id:int, secondary:bool)virtualconst
void
_redraw()virtual
void
_set_handle(id:int, secondary:bool, camera:Camera3D, point:Vector2)virtual
void
_set_subgizmo_transform(id:int, transform:Transform3D)virtual
PackedInt32Array
_subgizmos_intersect_frustum(camera:Camera3D, frustum:Array[Plane])virtualconst
_subgizmos_intersect_ray(camera:Camera3D, point:Vector2)virtualconst
void
add_collision_segments(segments:PackedVector3Array)
void
add_collision_triangles(triangles:TriangleMesh)
void
add_handles(handles:PackedVector3Array, material:Material, ids:PackedInt32Array, billboard:bool= false, secondary:bool= false)
void
add_lines(lines:PackedVector3Array, material:Material, billboard:bool= false, modulate:Color= Color(1, 1, 1, 1))
void
add_mesh(mesh:Mesh, material:Material= null, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton:SkinReference= null)
void
add_unscaled_billboard(material:Material, default_scale:float= 1, modulate:Color= Color(1, 1, 1, 1))
void
clear()
Node3D
get_node_3d()const
EditorNode3DGizmoPlugin
get_plugin()const
PackedInt32Array
get_subgizmo_selection()const
bool
is_subgizmo_selected(id:int)const
void
set_hidden(hidden:bool)
void
set_node_3d(node:Node)

## Method Descriptions

void_begin_handle_action(id:int, secondary:bool)virtual🔗
There is currently no description for this method. Please help us bycontributing one!
void_commit_handle(id:int, secondary:bool, restore:Variant, cancel:bool)virtual🔗
Override this method to commit a handle being edited (handles must have been previously added byadd_handles()). This usually means creating anUndoRedoaction for the change, using the current handle value as "do" and therestoreargument as "undo".
If thecancelargument istrue, therestorevalue should be directly set, without anyUndoRedoaction.
Thesecondaryargument istruewhen the committed handle is secondary (seeadd_handles()for more information).
void_commit_subgizmos(ids:PackedInt32Array, restores:Array[Transform3D], cancel:bool)virtual🔗
Override this method to commit a group of subgizmos being edited (see_subgizmos_intersect_ray()and_subgizmos_intersect_frustum()). This usually means creating anUndoRedoaction for the change, using the current transforms as "do" and therestorestransforms as "undo".
If thecancelargument istrue, therestorestransforms should be directly set, without anyUndoRedoaction.
String_get_handle_name(id:int, secondary:bool)virtualconst🔗
Override this method to return the name of an edited handle (handles must have been previously added byadd_handles()). Handles can be named for reference to the user when editing.
Thesecondaryargument istruewhen the requested handle is secondary (seeadd_handles()for more information).
Variant_get_handle_value(id:int, secondary:bool)virtualconst🔗
Override this method to return the current value of a handle. This value will be requested at the start of an edit and used as therestoreargument in_commit_handle().
Thesecondaryargument istruewhen the requested handle is secondary (seeadd_handles()for more information).
Transform3D_get_subgizmo_transform(id:int)virtualconst🔗
Override this method to return the current transform of a subgizmo. This transform will be requested at the start of an edit and used as therestoreargument in_commit_subgizmos().
bool_is_handle_highlighted(id:int, secondary:bool)virtualconst🔗
Override this method to returntruewhenever the given handle should be highlighted in the editor.
Thesecondaryargument istruewhen the requested handle is secondary (seeadd_handles()for more information).
void_redraw()virtual🔗
Override this method to add all the gizmo elements whenever a gizmo update is requested. It's common to callclear()at the beginning of this method and then add visual elements depending on the node's properties.
void_set_handle(id:int, secondary:bool, camera:Camera3D, point:Vector2)virtual🔗
Override this method to update the node properties when the user drags a gizmo handle (previously added withadd_handles()). The providedpointis the mouse position in screen coordinates and thecameracan be used to convert it to raycasts.
Thesecondaryargument istruewhen the edited handle is secondary (seeadd_handles()for more information).
void_set_subgizmo_transform(id:int, transform:Transform3D)virtual🔗
Override this method to update the node properties during subgizmo editing (see_subgizmos_intersect_ray()and_subgizmos_intersect_frustum()). Thetransformis given in theNode3D's local coordinate system.
PackedInt32Array_subgizmos_intersect_frustum(camera:Camera3D, frustum:Array[Plane])virtualconst🔗
Override this method to allow selecting subgizmos using mouse drag box selection. Given acameraand afrustum, this method should return which subgizmos are contained within the frustum. Thefrustumargument consists of an array with all thePlanes that make up the selection frustum. The returned value should contain a list of unique subgizmo identifiers, which can have any non-negative value and will be used in other virtual methods like_get_subgizmo_transform()or_commit_subgizmos().
int_subgizmos_intersect_ray(camera:Camera3D, point:Vector2)virtualconst🔗
Override this method to allow selecting subgizmos using mouse clicks. Given acameraand apointin screen coordinates, this method should return which subgizmo should be selected. The returned value should be a unique subgizmo identifier, which can have any non-negative value and will be used in other virtual methods like_get_subgizmo_transform()or_commit_subgizmos().
voidadd_collision_segments(segments:PackedVector3Array)🔗
Adds the specifiedsegmentsto the gizmo's collision shape for picking. Call this method during_redraw().
voidadd_collision_triangles(triangles:TriangleMesh)🔗
Adds collision triangles to the gizmo for picking. ATriangleMeshcan be generated from a regularMeshtoo. Call this method during_redraw().
voidadd_handles(handles:PackedVector3Array, material:Material, ids:PackedInt32Array, billboard:bool= false, secondary:bool= false)🔗
Adds a list of handles (points) which can be used to edit the properties of the gizmo'sNode3D. Theidsargument can be used to specify a custom identifier for each handle, if an empty array is passed, the ids will be assigned automatically from thehandlesargument order.
Thesecondaryargument marks the added handles as secondary, meaning they will normally have lower selection priority than regular handles. When the user is holding the shift key secondary handles will switch to have higher priority than regular handles. This change in priority can be used to place multiple handles at the same point while still giving the user control on their selection.
There are virtual methods which will be called upon editing of these handles. Call this method during_redraw().
voidadd_lines(lines:PackedVector3Array, material:Material, billboard:bool= false, modulate:Color= Color(1, 1, 1, 1))🔗
Adds lines to the gizmo (as sets of 2 points), with a given material. The lines are used for visualizing the gizmo. Call this method during_redraw().
voidadd_mesh(mesh:Mesh, material:Material= null, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton:SkinReference= null)🔗
Adds a mesh to the gizmo with the specifiedmaterial, localtransformandskeleton. Call this method during_redraw().
voidadd_unscaled_billboard(material:Material, default_scale:float= 1, modulate:Color= Color(1, 1, 1, 1))🔗
Adds an unscaled billboard for visualization and selection. Call this method during_redraw().
voidclear()🔗
Removes everything in the gizmo including meshes, collisions and handles.
Node3Dget_node_3d()const🔗
Returns theNode3Dnode associated with this gizmo.
EditorNode3DGizmoPluginget_plugin()const🔗
Returns theEditorNode3DGizmoPluginthat owns this gizmo. It's useful to retrieve materials usingEditorNode3DGizmoPlugin.get_material().
PackedInt32Arrayget_subgizmo_selection()const🔗
Returns a list of the currently selected subgizmos. Can be used to highlight selected elements during_redraw().
boolis_subgizmo_selected(id:int)const🔗
Returnstrueif the given subgizmo is currently selected. Can be used to highlight selected elements during_redraw().
voidset_hidden(hidden:bool)🔗
Sets the gizmo's hidden state. Iftrue, the gizmo will be hidden. Iffalse, it will be shown.
voidset_node_3d(node:Node)🔗
Sets the referenceNode3Dnode for the gizmo.nodemust inherit fromNode3D.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
