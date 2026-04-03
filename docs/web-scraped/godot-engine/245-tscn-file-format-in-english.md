# TSCN file format in English

# TSCN file format

The TSCN (text scene) file format represents a single scene tree inside
Godot. Unlike binary SCN files, TSCN files have the advantage of being mostly
human-readable and easy for version control systems to manage.
The ESCN (exported scene) file format is identical to the TSCN file format, but
is used to indicate to Godot that the file has been exported from another
program and should not be edited by the user from within Godot.
Unlike SCN and TSCN files, during import, ESCN files are compiled to binary
SCN files stored inside the.godot/imported/folder.
This reduces the data size and speeds up loading, as binary formats are faster
to load compared to text-based formats.
To make files more compact, properties equal to the default value are not stored
in scene/resource files. It is possible to write them manually, but they will be
discarded when saving the file.
For those looking for a complete description, the parsing is handled in the fileresource_format_text.cppin theResourceFormatLoaderTextclass.
Note
The scene and resource file formats have changed significantly in Godot 4,
with the introduction of string-based UIDs to replace incremental integer
IDs.
Mesh, skeleton and animation data is also stored differently compared to Godot 3.
You can read about some of the changes in this article:Animation data rework for 4.0
Scenes and resources saved with Godot 4.x containformat=3in their
header, whereas Godot 3.x usesformat=2instead.

## File structure

There are five main sections inside the TSCN file:

- File descriptor
File descriptor
- External resources
External resources
- Internal resources
Internal resources
- Nodes
Nodes
- Connections
Connections
The file descriptor looks like[gd_sceneformat=3uid="uid://cecaux1sm7mo0"]and should be the first entry in the file. Note that scenes saved before Godot 4.6
will also have aload_steps=<int>attribute in the file descriptor. This
attribute is now deprecated and should be ignored if present.
uidis a unique string-based identifier representing the scene. This is
used by the engine to track files that are moved around, even while the editor
is closed. Scripts can also load UID-based resources using theuid://path
prefix to avoid relying on filesystem paths. This makes it possible to move
around a file in the project, but still be able to load it in scripts without
having to modify the script. Godot does not use external files to keep track of
IDs, which means no central metadata storage location is required within the
project. Seethis pull requestfor detailed information.
These sections should appear in order, but it can be hard to distinguish them.
The only difference between them is the first element in the heading for all of
the items in the section. For example, the heading of all external resources
should start with[ext_resource...].
A TSCN file may contain single-line comments starting with a semicolon (;).
However, comments will be discarded when saving the file using the Godot editor.
Whitespace within a TSCN file is not significant (except within strings), but
extraneous whitespace will be discarded when saving the file.

### Entries inside the file

A heading looks like[<resource_type>key1=value1key2=value2key3=value3...]where resource_type is one of:

- ext_resource
ext_resource
- sub_resource
sub_resource
- node
node
- connection
connection
Below every heading comes zero or morekey=valuepairs. The
values can be complex datatypes such as Arrays, Transforms, Colors, and
so on. For example, a Node3D looks like:

```
[node name="Cube" type="Node3D" unique_id=224283918]
transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 2, 3)
```

## The scene tree

The scene tree is made up of… nodes! The heading of each node consists of its
name, parent, a unique ID (used to track nodes even if they are moved or
renamed), and most of the time, a type. For example:[nodename="PlayerCamera"type="Camera"parent="Player/Head"unique_id=1697057368]
Note thatunique_idis only present in scenes saved with Godot 4.6 or later.
Therefore, it is not guaranteed to be present.
Other valid keywords include:
> instanceinstance_placeholderownerindex(sets the order of appearance in the tree; if absent, inherited nodes will take precedence over plain ones)groups

- instance
instance
- instance_placeholder
instance_placeholder
- owner
owner
- index(sets the order of appearance in the tree; if absent, inherited nodes will take precedence over plain ones)
index(sets the order of appearance in the tree; if absent, inherited nodes will take precedence over plain ones)
- groups
groups
The first node in the file, which is also the scene root, mustnothave aparent="Path/To/Node"entry in its heading. All scene files should have
exactlyonescene root. If it doesn't, Godot will fail to import the file.
The parent path of other nodes should be absolute, but shouldn't contain
the scene root's name. If the node is a direct child of the scene root,
the path should be".". Here is an example scene tree
(but without any node content):

```
[node name="Player" type="Node3D" unique_id=1155673912]                    ; The scene root
[node name="Arm" type="Node3D" parent="." unique_id=1010797352]            ; Parented to the scene root
[node name="Hand" type="Node3D" parent="Arm" unique_id=536436825]          ; Child of "Arm"
[node name="Finger" type="Node3D" parent="Arm/Hand" unique_id=1732647084]  ; Child of "Hand"
```

To make the file structure easier to grasp, you can save a file with any
given node or resource and then inspect it yourself in an external editor. You
can also make incremental changes in the Godot editor, and keep an external
text editor open on the.tscnor.tresfile with auto-reload enabled
to see what changes.
Here is an example of a scene containing a RigidBody3D-based ball with
collision, visuals (mesh + light) and a camera parented to the RigidBody3D:

```
[gd_scene format=3 uid="uid://cecaux1sm7mo0"]

[sub_resource type="SphereShape3D" id="SphereShape3D_tj6p1"]

[sub_resource type="SphereMesh" id="SphereMesh_4w3ye"]

[sub_resource type="StandardMaterial3D" id="StandardMaterial3D_k54se"]
albedo_color = Color(1, 0.639216, 0.309804, 1)

[node name="Ball" type="RigidBody3D" unique_id=1358867382]

[node name="CollisionShape3D" type="CollisionShape3D" parent="." unique_id=1279975976]
shape = SubResource("SphereShape3D_tj6p1")

[node name="MeshInstance3D" type="MeshInstance3D" parent="." unique_id=558852834]
mesh = SubResource("SphereMesh_4w3ye")
surface_material_override/0 = SubResource("StandardMaterial3D_k54se")

[node name="OmniLight3D" type="OmniLight3D" parent="." unique_id=1581292810]
light_color = Color(1, 0.698039, 0.321569, 1)
omni_range = 10.0

[node name="Camera3D" type="Camera3D" parent="." unique_id=795715540]
transform = Transform3D(1, 0, 0, 0, 0.939693, 0.34202, 0, -0.34202, 0.939693, 0, 1, 3)
```

### NodePath

A tree structure is not enough to represent the whole scene. Godot uses aNodePath(Path/To/Node)structure to refer to another node or attribute of
the node anywhere in the scene tree. Paths are relative to the current node,
withNodePath(".")pointing to the current node andNodePath("")pointing to no node at all.
For instance, MeshInstance3D usesNodePath()to point to its skeleton.
Likewise, Animation tracks useNodePath()to point to node properties to
animate.
NodePath can also point to a property using a:property_namesuffix, and
even point to a specific component for vector, transform and color types. This
is used by Animation resources to point to specific properties to animate. For
example,NodePath("MeshInstance3D:scale.x")points to thexcomponent of
thescaleVector3 property in MeshInstance3D.
For example, theskeletonproperty in the MeshInstance3D node calledmeshpoints to its parent,Armature01:

```
[node name="mesh" type="MeshInstance3D" parent="Armature01" unique_id=1638249225]
skeleton = NodePath("..")
```

### Skeleton3D

TheSkeleton3Dnode inherits the Node3D node, but may also have a
list of bones described in key-value pairs in the formatbones/<id>/<attribute>=value. The bone attributes consist of:

- position: Vector3
position: Vector3
- rotation: Quaternion
rotation: Quaternion
- scale: Vector3
scale: Vector3
These attributes are all optional. For instance, a bone may only definepositionorrotationwithout defining the other properties.
Here's an example of a skeleton node with two bones:

```
[node name="Skeleton3D" type="Skeleton3D" parent="PlayerModel/Robot_Skeleton" index="0" unique_id=542985694]
bones/1/position = Vector3(0.114471, 2.19771, -0.197845)
bones/1/rotation = Quaternion(0.191422, -0.0471201, -0.00831942, 0.980341)
bones/2/position = Vector3(-2.59096e-05, 0.236002, 0.000347473)
bones/2/rotation = Quaternion(-0.0580488, 0.0310587, -0.0085914, 0.997794)
bones/2/scale = Vector3(0.9276, 0.9276, 0.9276)
```

### BoneAttachment3D

TheBoneAttachment3Dnode is an intermediate node to describe some
node being parented to a single bone in a Skeleton node. The BoneAttachment has
abone_name="nameofbone"property, as well as a property for the matching
bone index.
An example of aMarker3Dnode parented to a bone in Skeleton:

```
[node name="GunBone" type="BoneAttachment3D" parent="PlayerModel/Robot_Skeleton/Skeleton3D" index="5" unique_id=63481392]
transform = Transform3D(0.333531, 0.128981, -0.933896, 0.567174, 0.763886, 0.308015, 0.753209, -0.632331, 0.181604, -0.323915, 1.07098, 0.0497144)
bone_name = "hand.R"
bone_idx = 55

[node name="ShootFrom" type="Marker3D" parent="PlayerModel/Robot_Skeleton/Skeleton3D/GunBone" unique_id=679926736]
transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.4, 0)
```

### AnimationPlayer

TheAnimationPlayernode works with one or more animation libraries
stored inAnimationLibraryresources. An animation library is a
collection of individualAnimationresources, whose structure is
documentedhere.
This split between animations themselves and animation libraries was done in
Godot 4, so that animations can be imported separately from 3D meshes, which is
a common workflow in 3D animation software. See theoriginal pull requestfor details.
If the library name is empty, then it acts as the unique source of animations
for this AnimationPlayer. This allows using<animation_name>directly to
play animations from script. If you name the library, then you must play it as<library_name>/<animation_name>. This ensures backwards compatibility and
keeps the existing workflow if you don't want to use multiple animation
libraries.

## Resources

Resources are components that make up the nodes. For example, a MeshInstance3D
node will have an accompanying ArrayMesh resource. The ArrayMesh resource
may be either internal or external to the TSCN file.
References to the resources are handled by unique string-based IDs in the
resource's heading. This is different from theuidproperty, which each
external resource also has (but subresources don't).
External resources and internal resources are referred to withExtResource("id")andSubResource("id"), respectively. Because there
have different methods to refer to internal and external resources, you can have
the same ID for both an internal and external resource.
For example, to refer to the resource[ext_resourcetype="Material"uid="uid://c4cp0al3ljsjv"path="res://material.tres"id="1_7bt6s"],
you would useExtResource("1_7bt6s").

### External resources

External resources are links to resources not contained within the TSCN file
itself. An external resource consists of a path, a type, a UID (used to map its
filesystem location to a unique identifier) and an ID (used to refer to the
resource in the scene file).
Godot always generates absolute paths relative to the resource directory and
thus prefixed withres://, but paths relative to the TSCN file's location
are also valid.
Some example external resources are:

```
[ext_resource type="Texture2D" uid="uid://ccbm14ebjmpy1" path="res://gradient.tres" id="2_eorut"]
[ext_resource type="Material" uid="uid://c4cp0al3ljsjv" path="material.tres" id="1_7bt6s"]
```

Like TSCN files, a TRES file may contain single-line comments starting with a
semicolon (;). However, comments will be discarded when saving the resource
using the Godot editor.
Whitespace within a TRES file is not significant (except within strings), but
extraneous whitespace will be discarded when saving the file.

### Internal resources

A TSCN file can contain meshes, materials and other data. These are contained in
theinternal resourcessection of the file. The heading for an internal
resource looks similar to those of external resources, except that it doesn't
have a path. Internal resources also havekey=valuepairs under each
heading. For example, a capsule collision shape looks like:

```
[sub_resource type="CapsuleShape3D" id="CapsuleShape3D_fdxgg"]
radius = 1.0
height = 3.0
```

Some internal resources contain links to other internal resources (such as a
mesh having a material). In this case, the referring resource must appearbeforethe reference to it. This means that order matters in the file's
internal resources section.

### ArrayMesh

An ArrayMesh consists of several surfaces contained in the_surfacesarray
(notice the leading underscore). Each surface's data is stored in a dictionary
with the following keys:

- aabb: The computed axis-aligned bounding box for visibility.
aabb: The computed axis-aligned bounding box for visibility.
- attribute_data: Vertex attribute data, such as normals, tangents, vertex
colors, UV1, UV2 and custom vertex data.
attribute_data: Vertex attribute data, such as normals, tangents, vertex
colors, UV1, UV2 and custom vertex data.
- bone_aabbs: The axis-aligned bounding box of each bone for visibility.
bone_aabbs: The axis-aligned bounding box of each bone for visibility.
- format: The surface's buffer format.
format: The surface's buffer format.
- index_count: The number of indices in the surface. This must matchindex_data's size.
index_count: The number of indices in the surface. This must matchindex_data's size.
- index_data: The index data, which determines which vertices fromvertex_dataare drawn.
index_data: The index data, which determines which vertices fromvertex_dataare drawn.
- lods: Level of detail variations, stored as an array. Each LOD level
represents two values in the array. The first value is the percentage of
screen space the LOD level is most suited for (edge length); the second value
is the list of indices that should be drawn for the given LOD level.
lods: Level of detail variations, stored as an array. Each LOD level
represents two values in the array. The first value is the percentage of
screen space the LOD level is most suited for (edge length); the second value
is the list of indices that should be drawn for the given LOD level.
- material: The material used when drawing the surface.
material: The material used when drawing the surface.
- name: The surface's name. This can be used in scripts and is imported from
3D DCCs.
name: The surface's name. This can be used in scripts and is imported from
3D DCCs.
- primitive: The surface's primitive type, matching theMesh.PrimitiveTypeGodot enum.0= points,1= lines,2= line
strip,3= triangles (most common),4= triangle strip.
primitive: The surface's primitive type, matching theMesh.PrimitiveTypeGodot enum.0= points,1= lines,2= line
strip,3= triangles (most common),4= triangle strip.
- skin_data: Bone weight data.
skin_data: Bone weight data.
- vertex_count: Number of vertices in the surface. This must matchvertex_data's size.
vertex_count: Number of vertices in the surface. This must matchvertex_data's size.
- vertex_data: The vertex position data.
vertex_data: The vertex position data.
Here's an example of an ArrayMesh saved to its own.tresfile. Some fields were shortened with...for brevity:

```
[gd_resource type="ArrayMesh" format=3 uid="uid://dww8o7hsqrhx5"]

[ext_resource type="Material" path="res://player/model/playerobot.tres" id="1_r3bjq"]

[resource]
resource_name = "player_Sphere_016"
_surfaces = [{
"aabb": AABB(-0.207928, 1.21409, -0.14545, 0.415856, 0.226569, 0.223374),
"attribute_data": PackedByteArray(63, 121, ..., 117, 63),
"bone_aabbs": [AABB(0, 0, 0, -1, -1, -1), ..., AABB(-0.207928, 1.21409, -0.14545, 0.134291, 0.226569, 0.223374)],
"format": 7191,
"index_count": 1224,
"index_data": PackedByteArray(30, 0, ..., 150, 4),
"lods": [0.0382013, PackedByteArray(33, 1, ..., 150, 4)],
"material": ExtResource("1_r3bjq"),
"name": "playerobot",
"primitive": 3,
"skin_data": PackedByteArray(15, 0, ..., 0, 0),
"vertex_count": 1250,
"vertex_data": PackedByteArray(196, 169, ..., 11, 38)
}]
blend_shape_mode = 0
```

### Animation

Each animation has the following properties:

- length: The animation's length in seconds. Note that keyframes may be
placed outside the[0;length]interval, but they may have no effect
depending on the interpolation mode chosen.
length: The animation's length in seconds. Note that keyframes may be
placed outside the[0;length]interval, but they may have no effect
depending on the interpolation mode chosen.
- loop_mode:0= no looping,1= wrap-around looping,2=
clamped looping.
loop_mode:0= no looping,1= wrap-around looping,2=
clamped looping.
- step: The step size to use when editing this animation in the editor.
This is only used in the editor; it doesn't affect animation playback in any way.
step: The step size to use when editing this animation in the editor.
This is only used in the editor; it doesn't affect animation playback in any way.
Each track is described by a list of key-value pairs in the formattracks/<id>/<attribute>. Each track includes:
- type: The track's type. This defines what kind of properties may be
animated by this track, and how it'll be exposed to the user in the editor.
Valid types arevalue(generic property track),position_3d,rotation_3d,scale_3d,blend_shape(optimized 3D animation
tracks),method(method call tracks),bezier(Bezier curve tracks),audio(audio playback tracks),animation(tracks that play other
animations).
type: The track's type. This defines what kind of properties may be
animated by this track, and how it'll be exposed to the user in the editor.
Valid types arevalue(generic property track),position_3d,rotation_3d,scale_3d,blend_shape(optimized 3D animation
tracks),method(method call tracks),bezier(Bezier curve tracks),audio(audio playback tracks),animation(tracks that play other
animations).
- imported:trueif the track was created from an imported 3D scene,falseif it was manually created by the user in the Godot editor or using
a script.
imported:trueif the track was created from an imported 3D scene,falseif it was manually created by the user in the Godot editor or using
a script.
- enabled:trueif the track is effective,falseif it was disabled
in the editor.
enabled:trueif the track is effective,falseif it was disabled
in the editor.
- path: Path to the node property that will be affected by the track. The
property is written after the node path with a:separator.
path: Path to the node property that will be affected by the track. The
property is written after the node path with a:separator.
- interp: The interpolation mode to use.0= nearest,1= linear,2= cubic,3= linear angle,4= cubic angle.
interp: The interpolation mode to use.0= nearest,1= linear,2= cubic,3= linear angle,4= cubic angle.
- loop_wrap:trueif the track is designed to wrap around when the
animation is looping,falseif the track clamps to the first/last
keyframes.
loop_wrap:trueif the track is designed to wrap around when the
animation is looping,falseif the track clamps to the first/last
keyframes.
- keys: The animation track's values. This attribute's structure depends on thetype.
keys: The animation track's values. This attribute's structure depends on thetype.
Here is a scene containing an AnimationPlayer that scales down a cube over time
using a generic property track. The AnimationLibrary workflow was not used, so
the animation library has an empty name (but the animation is still given ascale_downname). Note that theRESETtrack was not created in this
AnimationPlayer for brevity:

```
[gd_scene format=3 uid="uid://cdyt3nktp6y6"]

[sub_resource type="Animation" id="Animation_r2qdp"]
resource_name = "scale_down"
length = 1.5
loop_mode = 2
step = 0.05
tracks/0/type = "value"
tracks/0/imported = false
tracks/0/enabled = true
tracks/0/path = NodePath("Box:scale")
tracks/0/interp = 1
tracks/0/loop_wrap = true
tracks/0/keys = {
"times": PackedFloat32Array(0, 1),
"transitions": PackedFloat32Array(1, 1),
"update": 0,
"values": [Vector3(1, 1, 1), Vector3(0, 0, 0)]
}

[sub_resource type="AnimationLibrary" id="AnimationLibrary_4qx36"]
_data = {
"scale_down": SubResource("Animation_r2qdp")
}

[sub_resource type="BoxMesh" id="BoxMesh_u688r"]

[node name="Node3D" type="Node3D" unique_id=2076735200]

[node name="AnimationPlayer" type="AnimationPlayer" parent="." unique_id=2139773137]
autoplay = "scale_down"
libraries = {
"": SubResource("AnimationLibrary_4qx36")
}

[node name="Box" type="MeshInstance3D" parent="." unique_id=711004519]
mesh = SubResource("BoxMesh_u688r")
```

For generic propertyvaluetracks,keysis a dictionary containing 3
arrays with positions intimes(PackedFloat32Array), easing values intransitions(PackedFloat32Array) and values invalues(Array). There is
an additionalupdateproperty, which is an integer with the values0=
continuous,1= discrete,2= capture.
Here is a second Animation resource that makes use of the 3D Position and 3D
Rotation tracks. These tracks (in addition to the 3D Scale track) replace
Transform tracks from Godot 3. They are optimized for fast playback and can
optionally be compressed.
The downside of these optimized track types is that they can't use custom easing
values. Instead, all keyframes use linear interpolation. That said, you can
still opt for using nearest or cubic interpolation for all keyframes in a given
track by changing the track's interpolation mode.

```
[sub_resource type="Animation" id="Animation_r2qdp"]
resource_name = "move_and_rotate"
length = 1.5
loop_mode = 2
step = 0.05
tracks/0/type = "position_3d"
tracks/0/imported = false
tracks/0/enabled = true
tracks/0/path = NodePath("Box")
tracks/0/interp = 1
tracks/0/loop_wrap = true
tracks/0/keys = PackedFloat32Array(0, 1, 0, 0, 0, 1.5, 1, 1.5, 1, 0)
tracks/1/type = "rotation_3d"
tracks/1/imported = false
tracks/1/enabled = true
tracks/1/path = NodePath("Box")
tracks/1/interp = 1
tracks/1/loop_wrap = true
tracks/1/keys = PackedFloat32Array(0, 1, 0.211, -0.047, 0.211, 0.953, 1.5, 1, 0.005, 0.976, -0.216, 0.022)
```

For 3D position, rotation and scale tracks,keysis a PackedFloat32Array
with all values stored in a sequence.
In the visual guide below,Tis the keyframe's time in seconds since the
start of the animation,Eis the keyframe's transition (currently always1). For 3D position and scale tracks,X,Y,Zare the Vector3's
coordinates. For 3D rotation tracks,X,Y,ZandWare the
Quaternion's coordinates.

```
# For 3D position and scale, which use Vector3:
tracks/<id>/keys = PackedFloat32Array(T, E,   X, Y, Z,      T, E,   X, Y, Z, ...)

# For 3D rotation, which use Quaternion:
tracks/<id>/keys = PackedFloat32Array(T, E,   X, Y, Z, W,      T, E,   X, Y, Z, W, ...)
```

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
