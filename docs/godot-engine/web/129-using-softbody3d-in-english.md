# Using SoftBody3D in English

# Using SoftBody3D

Soft bodies (orsoft-body dynamics) simulate movement, changing shape and other
physical properties of deformable objects. For example, this can be used to simulate
cloth or to create more realistic characters.

## Physics engine considerations

Support for soft bodies is generally more robust in Jolt Physics compared to GodotPhysics3D.
You can switch physics engines by changingPhysics > 3D > Physics Enginein the Project Settings. Projects created in Godot 4.6 and later use Jolt Physics
by default, but existing projects will have to be switched over manually.
Additionally,physics interpolationcurrently
does not affect soft bodies. If you want soft body simulation to look smoother at
higher framerates, you'll have to increase thePhysics > Common > Physics Ticks per Secondproject setting, which comes at a performance cost.

## Basic setup

ASoftBody3Dnode is used for soft body simulations.
Unlike other physics body nodes likeRigidBody3DorStaticBody3D, it doesnothave aCollisionShape3Dor aMeshInstance3Dchild node. Instead, the collision shape is derived from the mesh assigned to the node.
This mesh is also directly used for rendering, which means you don't need to
create any child nodes for a functional, visible setup.
We will create a bouncy cube to demonstrate the setup of a soft body.
Create a new scene with a Node3D node as root. Then, create a SoftBody3D node.
Add a BoxMesh in theMeshproperty of the node in the inspector
and increase the subdivision of the mesh for simulation.
The subdivision level determines the precision level of the deformation,
with higher values allowing for smaller and more detailed deformations,
at the cost of performance. In this example, we'll set it to 3 on each axis:
Adjusting BoxMesh properties in the inspector
Now, set the parameters to obtain the type of soft body you aim for.
Try to keep theSimulation Precisionabove 5; otherwise,
the soft body may collapse.
Adjusting SoftBody3D simulation properties in the inspector
Note
Handle some parameters with care, as some values can lead to strange results.
For example, if the shape is not completely closed and you set pressure
to a value greater than0.0, the soft body will fly around like a plastic bag
under strong wind.
Run the scene to view the simulation. Here's an example of what it should look like:
To improve the simulation's result, increase theSimulation Precision.
This can give a significant improvement at the cost of performance.
Alternatively, you can increase thePhysics > Common > Physics Ticks per Secondproject setting, which will also affect soft body simulation quality.

## Cloak simulation

Let's make a cloak in the Platformer 3D demo.
Note
You can download the Platformer 3D demo onGitHuborthe Asset Library.
Open theplayer/player.tscnscene, add aSoftBody3Dnode below the root node,
then assign a PlaneMesh resource to it in itsMeshproperty.
Open the PlaneMesh's properties and set the size to(0.5,1.0),
then setSubdivide WidthandSubdivide Depthto5. Adjust the
SoftBody3D node's position and rotation so that the plane appears to be close to
the character's back. You should end up with something like this:
Subdividing the PlaneMesh and placing it on the character's back
Subdivision generates a more tessellated mesh for better simulations.
However, higher subdivision levels will impact performance. Try
to find a balance between performance and quality. This depends on the number
of soft body simulations that you expect to be active at a given time,
as well as the distance between the camera and the soft body.
Add aBoneAttachment3Dnode under the skeleton
node and select the Neck bone to attach the cloak to the character skeleton.
Note
The BoneAttachment3D node is used to attach objects to a bone of an armature.
The attached object will follow the bone's movement. For example, a character's
held weapon can be attached this way.
Donotmove the SoftBody3D node under the BoneAttachment3D node as of now.
Instead, we'll configure itspinned pointsto follow the BoneAttachment3D node.
Configuring the BoneAttachment3D node in the inspector
To create pinned points, select the upper vertices in the SoftBody3D node. A pinned
point appears blue in the 3D editor viewport:
Pinning the SoftBody3D's points in the inspector
The pinned joints can be found in SoftBody3D'sAttachmentssection,
which is under theCollisionsection that must be expanded first.
Choose the BoneAttachment3D node as theSpatial Attachment Pathfor each
pinned joint. The pinned joints are now attached to the neck.
To assign the properties faster, you can drag-and-drop the BoneAttachment3D node
from the scene tree dock to theSpatial Attachment Pathproperty field.
Note that you may have to deselect then reselect the SoftBody3D node for theAttachmentssection to appear.
Configuring pinned points to be attached to the BoneAttachment3D node in the SoftBody3D inspector
The last step is to avoid clipping by adding the CharacterBody3DPlayer(the scene's root node)
to theParent Collision Ignoreproperty of the SoftBody3D.
Setting up the collision exception in the SoftBody3D inspector
Play the scene and the cloak should simulate correctly.
Final result when running the project's main scene
This covers the basic settings of a soft body simulation. Experiment with the parameters
to achieve the effect you are aiming for when making your game.
Note
The cloak will not appear when viewed from certain angles due to backface culling.
To resolve this, you can disable backface culling by assigning a new StandardMaterial3D,
then setting its cull mode toDisabled. This will make the material render
both sides of the plane.

## Using imported meshes

TheSave to Fileoption in the Advanced Import Settings dialog allows you
to save a mesh to a standalone resource file that you can then attach to
SoftBody3D nodes.
You may also want to disable LOD generation or change the LOD generation options
when importing a mesh for use with SoftBody3D. The default import settings
will produce an LOD that merges adjacent faces that are nearly flat with
respect to each other, even at very close render distances. This works well for
static meshes, but is often undesirable for use with SoftBody3D if you want
these faces to be able to bend and move with respect to each other, instead of
being rendered as a single plane.
SeeImport configurationandMesh level of detail (LOD)for more details.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
