# Source: https://docs.blender.org/api/current/bpy.ops.object.html

Title: Object Operators - Blender Python API

URL Source: https://docs.blender.org/api/current/bpy.ops.object.html

Published Time: Fri, 24 Oct 2025 01:50:14 GMT

Markdown Content:
Object Operators - Blender Python API
===============
- [x] - [x] 

Hide navigation sidebar

 

Hide table of contents sidebar

 [Skip to content](https://docs.blender.org/api/current/bpy.ops.object.html#furo-main-content)

Toggle site navigation sidebar

 

[Blender Python API](https://docs.blender.org/api/current/index.html)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

 

[![Image 1: Logo](https://docs.blender.org/api/current/_static/blender_logo.svg) Blender Python API](https://docs.blender.org/api/current/index.html)

Documentation

*   [Quickstart](https://docs.blender.org/api/current/info_quickstart.html)
*   [API Overview](https://docs.blender.org/api/current/info_overview.html)
*   [API Reference Usage](https://docs.blender.org/api/current/info_api_reference.html)
*   [Best Practice](https://docs.blender.org/api/current/info_best_practice.html)
*   [Tips and Tricks](https://docs.blender.org/api/current/info_tips_and_tricks.html)
*   [Gotchas](https://docs.blender.org/api/current/info_gotcha.html)- [x] Toggle navigation of Gotchas  
    *   [Troubleshooting Errors & Crashes](https://docs.blender.org/api/current/info_gotchas_crashes.html)
    *   [Python Threads are Not Supported](https://docs.blender.org/api/current/info_gotchas_threading.html)
    *   [Internal Data & Their Python Objects](https://docs.blender.org/api/current/info_gotchas_internal_data_and_python_objects.html)
    *   [Using Operators](https://docs.blender.org/api/current/info_gotchas_operators.html)
    *   [Modes and Mesh Access](https://docs.blender.org/api/current/info_gotchas_meshes.html)
    *   [Bones & Armatures](https://docs.blender.org/api/current/info_gotchas_armatures_and_bones.html)
    *   [File Paths & String Encoding](https://docs.blender.org/api/current/info_gotchas_file_paths_and_encoding.html)

*   [Advanced](https://docs.blender.org/api/current/info_advanced.html)- [x] Toggle navigation of Advanced  
    *   [Blender as a Python Module](https://docs.blender.org/api/current/info_advanced_blender_as_bpy.html)

*   [Change Log](https://docs.blender.org/api/current/change_log.html)

Application Modules

*   [Context Access (bpy.context)](https://docs.blender.org/api/current/bpy.context.html)
*   [Data Access (bpy.data)](https://docs.blender.org/api/current/bpy.data.html)
*   [Message Bus (bpy.msgbus)](https://docs.blender.org/api/current/bpy.msgbus.html)
*   [Operators (bpy.ops)](https://docs.blender.org/api/current/bpy.ops.html)- [x] Toggle navigation of Operators (bpy.ops)  
    *   [Action Operators](https://docs.blender.org/api/current/bpy.ops.action.html)
    *   [Anim Operators](https://docs.blender.org/api/current/bpy.ops.anim.html)
    *   [Armature Operators](https://docs.blender.org/api/current/bpy.ops.armature.html)
    *   [Asset Operators](https://docs.blender.org/api/current/bpy.ops.asset.html)
    *   [Boid Operators](https://docs.blender.org/api/current/bpy.ops.boid.html)
    *   [Brush Operators](https://docs.blender.org/api/current/bpy.ops.brush.html)
    *   [Buttons Operators](https://docs.blender.org/api/current/bpy.ops.buttons.html)
    *   [Cachefile Operators](https://docs.blender.org/api/current/bpy.ops.cachefile.html)
    *   [Camera Operators](https://docs.blender.org/api/current/bpy.ops.camera.html)
    *   [Clip Operators](https://docs.blender.org/api/current/bpy.ops.clip.html)
    *   [Cloth Operators](https://docs.blender.org/api/current/bpy.ops.cloth.html)
    *   [Collection Operators](https://docs.blender.org/api/current/bpy.ops.collection.html)
    *   [Console Operators](https://docs.blender.org/api/current/bpy.ops.console.html)
    *   [Constraint Operators](https://docs.blender.org/api/current/bpy.ops.constraint.html)
    *   [Curve Operators](https://docs.blender.org/api/current/bpy.ops.curve.html)
    *   [Curves Operators](https://docs.blender.org/api/current/bpy.ops.curves.html)
    *   [Cycles Operators](https://docs.blender.org/api/current/bpy.ops.cycles.html)
    *   [Dpaint Operators](https://docs.blender.org/api/current/bpy.ops.dpaint.html)
    *   [Ed Operators](https://docs.blender.org/api/current/bpy.ops.ed.html)
    *   [Export Anim Operators](https://docs.blender.org/api/current/bpy.ops.export_anim.html)
    *   [Export Scene Operators](https://docs.blender.org/api/current/bpy.ops.export_scene.html)
    *   [Extensions Operators](https://docs.blender.org/api/current/bpy.ops.extensions.html)
    *   [File Operators](https://docs.blender.org/api/current/bpy.ops.file.html)
    *   [Fluid Operators](https://docs.blender.org/api/current/bpy.ops.fluid.html)
    *   [Font Operators](https://docs.blender.org/api/current/bpy.ops.font.html)
    *   [Geometry Operators](https://docs.blender.org/api/current/bpy.ops.geometry.html)
    *   [Gizmogroup Operators](https://docs.blender.org/api/current/bpy.ops.gizmogroup.html)
    *   [Gpencil Operators](https://docs.blender.org/api/current/bpy.ops.gpencil.html)
    *   [Graph Operators](https://docs.blender.org/api/current/bpy.ops.graph.html)
    *   [Grease Pencil Operators](https://docs.blender.org/api/current/bpy.ops.grease_pencil.html)
    *   [Image Operators](https://docs.blender.org/api/current/bpy.ops.image.html)
    *   [Import Anim Operators](https://docs.blender.org/api/current/bpy.ops.import_anim.html)
    *   [Import Curve Operators](https://docs.blender.org/api/current/bpy.ops.import_curve.html)
    *   [Import Scene Operators](https://docs.blender.org/api/current/bpy.ops.import_scene.html)
    *   [Info Operators](https://docs.blender.org/api/current/bpy.ops.info.html)
    *   [Lattice Operators](https://docs.blender.org/api/current/bpy.ops.lattice.html)
    *   [Marker Operators](https://docs.blender.org/api/current/bpy.ops.marker.html)
    *   [Mask Operators](https://docs.blender.org/api/current/bpy.ops.mask.html)
    *   [Material Operators](https://docs.blender.org/api/current/bpy.ops.material.html)
    *   [Mball Operators](https://docs.blender.org/api/current/bpy.ops.mball.html)
    *   [Mesh Operators](https://docs.blender.org/api/current/bpy.ops.mesh.html)
    *   [Nla Operators](https://docs.blender.org/api/current/bpy.ops.nla.html)
    *   [Node Operators](https://docs.blender.org/api/current/bpy.ops.node.html)
    *   [Object Operators](https://docs.blender.org/api/current/bpy.ops.object.html#)
    *   [Outliner Operators](https://docs.blender.org/api/current/bpy.ops.outliner.html)
    *   [Paint Operators](https://docs.blender.org/api/current/bpy.ops.paint.html)
    *   [Paintcurve Operators](https://docs.blender.org/api/current/bpy.ops.paintcurve.html)
    *   [Palette Operators](https://docs.blender.org/api/current/bpy.ops.palette.html)
    *   [Particle Operators](https://docs.blender.org/api/current/bpy.ops.particle.html)
    *   [Pointcloud Operators](https://docs.blender.org/api/current/bpy.ops.pointcloud.html)
    *   [Pose Operators](https://docs.blender.org/api/current/bpy.ops.pose.html)
    *   [Poselib Operators](https://docs.blender.org/api/current/bpy.ops.poselib.html)
    *   [Preferences Operators](https://docs.blender.org/api/current/bpy.ops.preferences.html)
    *   [Ptcache Operators](https://docs.blender.org/api/current/bpy.ops.ptcache.html)
    *   [Render Operators](https://docs.blender.org/api/current/bpy.ops.render.html)
    *   [Rigidbody Operators](https://docs.blender.org/api/current/bpy.ops.rigidbody.html)
    *   [Scene Operators](https://docs.blender.org/api/current/bpy.ops.scene.html)
    *   [Screen Operators](https://docs.blender.org/api/current/bpy.ops.screen.html)
    *   [Script Operators](https://docs.blender.org/api/current/bpy.ops.script.html)
    *   [Sculpt Operators](https://docs.blender.org/api/current/bpy.ops.sculpt.html)
    *   [Sculpt Curves Operators](https://docs.blender.org/api/current/bpy.ops.sculpt_curves.html)
    *   [Sequencer Operators](https://docs.blender.org/api/current/bpy.ops.sequencer.html)
    *   [Sound Operators](https://docs.blender.org/api/current/bpy.ops.sound.html)
    *   [Spreadsheet Operators](https://docs.blender.org/api/current/bpy.ops.spreadsheet.html)
    *   [Surface Operators](https://docs.blender.org/api/current/bpy.ops.surface.html)
    *   [Text Operators](https://docs.blender.org/api/current/bpy.ops.text.html)
    *   [Text Editor Operators](https://docs.blender.org/api/current/bpy.ops.text_editor.html)
    *   [Texture Operators](https://docs.blender.org/api/current/bpy.ops.texture.html)
    *   [Transform Operators](https://docs.blender.org/api/current/bpy.ops.transform.html)
    *   [Ui Operators](https://docs.blender.org/api/current/bpy.ops.ui.html)
    *   [Uilist Operators](https://docs.blender.org/api/current/bpy.ops.uilist.html)
    *   [Uv Operators](https://docs.blender.org/api/current/bpy.ops.uv.html)
    *   [View2D Operators](https://docs.blender.org/api/current/bpy.ops.view2d.html)
    *   [View3D Operators](https://docs.blender.org/api/current/bpy.ops.view3d.html)
    *   [Wm Operators](https://docs.blender.org/api/current/bpy.ops.wm.html)
    *   [Workspace Operators](https://docs.blender.org/api/current/bpy.ops.workspace.html)
    *   [World Operators](https://docs.blender.org/api/current/bpy.ops.world.html)

*   [Types (bpy.types)](https://docs.blender.org/api/current/bpy.types.html)- [x] Toggle navigation of Types (bpy.types)  
    *   [AOV(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AOV.html)
    *   [AOVs(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AOVs.html)
    *   [ASSETBROWSER_UL_metadata_tags(UIList)](https://docs.blender.org/api/current/bpy.types.ASSETBROWSER_UL_metadata_tags.html)
    *   [Action(ID)](https://docs.blender.org/api/current/bpy.types.Action.html)
    *   [ActionChannelbag(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionChannelbag.html)
    *   [ActionChannelbagFCurves(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionChannelbagFCurves.html)
    *   [ActionChannelbagGroups(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionChannelbagGroups.html)
    *   [ActionChannelbags(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionChannelbags.html)
    *   [ActionConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.ActionConstraint.html)
    *   [ActionGroup(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionGroup.html)
    *   [ActionKeyframeStrip(ActionStrip)](https://docs.blender.org/api/current/bpy.types.ActionKeyframeStrip.html)
    *   [ActionLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionLayer.html)
    *   [ActionLayers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionLayers.html)
    *   [ActionPoseMarkers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionPoseMarkers.html)
    *   [ActionSlot(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionSlot.html)
    *   [ActionSlots(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionSlots.html)
    *   [ActionStrip(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionStrip.html)
    *   [ActionStrips(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ActionStrips.html)
    *   [AddStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.AddStrip.html)
    *   [Addon(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Addon.html)
    *   [AddonPreferences(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AddonPreferences.html)
    *   [Addons(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Addons.html)
    *   [AdjustmentStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.AdjustmentStrip.html)
    *   [AlphaOverStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.AlphaOverStrip.html)
    *   [AlphaUnderStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.AlphaUnderStrip.html)
    *   [AnimData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnimData.html)
    *   [AnimDataDrivers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnimDataDrivers.html)
    *   [AnimViz(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnimViz.html)
    *   [AnimVizMotionPaths(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnimVizMotionPaths.html)
    *   [Annotation(ID)](https://docs.blender.org/api/current/bpy.types.Annotation.html)
    *   [AnnotationFrame(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnnotationFrame.html)
    *   [AnnotationFrames(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnnotationFrames.html)
    *   [AnnotationLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnnotationLayer.html)
    *   [AnnotationLayers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnnotationLayers.html)
    *   [AnnotationStroke(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnnotationStroke.html)
    *   [AnnotationStrokePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnnotationStrokePoint.html)
    *   [AnyType(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AnyType.html)
    *   [Area(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Area.html)
    *   [AreaLight(Light)](https://docs.blender.org/api/current/bpy.types.AreaLight.html)
    *   [AreaSpaces(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AreaSpaces.html)
    *   [Armature(ID)](https://docs.blender.org/api/current/bpy.types.Armature.html)
    *   [ArmatureBones(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ArmatureBones.html)
    *   [ArmatureConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.ArmatureConstraint.html)
    *   [ArmatureConstraintTargets(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ArmatureConstraintTargets.html)
    *   [ArmatureEditBones(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ArmatureEditBones.html)
    *   [ArmatureModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ArmatureModifier.html)
    *   [ArrayModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ArrayModifier.html)
    *   [AssetLibraryCollection(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetLibraryCollection.html)
    *   [AssetLibraryReference(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetLibraryReference.html)
    *   [AssetMetaData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetMetaData.html)
    *   [AssetRepresentation(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetRepresentation.html)
    *   [AssetShelf(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetShelf.html)
    *   [AssetTag(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetTag.html)
    *   [AssetTags(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetTags.html)
    *   [AssetWeakReference(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AssetWeakReference.html)
    *   [Attribute(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Attribute.html)
    *   [AttributeGroupCurves(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AttributeGroupCurves.html)
    *   [AttributeGroupGreasePencil(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AttributeGroupGreasePencil.html)
    *   [AttributeGroupGreasePencilDrawing(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AttributeGroupGreasePencilDrawing.html)
    *   [AttributeGroupMesh(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AttributeGroupMesh.html)
    *   [AttributeGroupPointCloud(bpy_struct)](https://docs.blender.org/api/current/bpy.types.AttributeGroupPointCloud.html)
    *   [BakeSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BakeSettings.html)
    *   [BevelModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.BevelModifier.html)
    *   [BezierSplinePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BezierSplinePoint.html)
    *   [BlendData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendData.html)
    *   [BlendDataActions(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataActions.html)
    *   [BlendDataAnnotations(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataAnnotations.html)
    *   [BlendDataArmatures(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataArmatures.html)
    *   [BlendDataBrushes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataBrushes.html)
    *   [BlendDataCacheFiles(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataCacheFiles.html)
    *   [BlendDataCameras(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataCameras.html)
    *   [BlendDataCollections(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataCollections.html)
    *   [BlendDataCurves(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataCurves.html)
    *   [BlendDataFonts(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataFonts.html)
    *   [BlendDataGreasePencilsV3(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataGreasePencilsV3.html)
    *   [BlendDataHairCurves(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataHairCurves.html)
    *   [BlendDataImages(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataImages.html)
    *   [BlendDataLattices(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataLattices.html)
    *   [BlendDataLibraries(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataLibraries.html)
    *   [BlendDataLights(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataLights.html)
    *   [BlendDataLineStyles(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataLineStyles.html)
    *   [BlendDataMasks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataMasks.html)
    *   [BlendDataMaterials(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataMaterials.html)
    *   [BlendDataMeshes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataMeshes.html)
    *   [BlendDataMetaBalls(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataMetaBalls.html)
    *   [BlendDataMovieClips(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataMovieClips.html)
    *   [BlendDataNodeTrees(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataNodeTrees.html)
    *   [BlendDataObjects(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataObjects.html)
    *   [BlendDataPaintCurves(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataPaintCurves.html)
    *   [BlendDataPalettes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataPalettes.html)
    *   [BlendDataParticles(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataParticles.html)
    *   [BlendDataPointClouds(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataPointClouds.html)
    *   [BlendDataProbes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataProbes.html)
    *   [BlendDataScenes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataScenes.html)
    *   [BlendDataScreens(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataScreens.html)
    *   [BlendDataSounds(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataSounds.html)
    *   [BlendDataSpeakers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataSpeakers.html)
    *   [BlendDataTexts(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataTexts.html)
    *   [BlendDataTextures(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataTextures.html)
    *   [BlendDataVolumes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataVolumes.html)
    *   [BlendDataWindowManagers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataWindowManagers.html)
    *   [BlendDataWorkSpaces(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataWorkSpaces.html)
    *   [BlendDataWorlds(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendDataWorlds.html)
    *   [BlendFileColorspace(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendFileColorspace.html)
    *   [BlendImportContext(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendImportContext.html)
    *   [BlendImportContextItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendImportContextItem.html)
    *   [BlendImportContextItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendImportContextItems.html)
    *   [BlendImportContextLibraries(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendImportContextLibraries.html)
    *   [BlendImportContextLibrary(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlendImportContextLibrary.html)
    *   [BlendTexture(Texture)](https://docs.blender.org/api/current/bpy.types.BlendTexture.html)
    *   [BlenderRNA(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BlenderRNA.html)
    *   [BoidRule(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoidRule.html)
    *   [BoidRuleAverageSpeed(BoidRule)](https://docs.blender.org/api/current/bpy.types.BoidRuleAverageSpeed.html)
    *   [BoidRuleAvoid(BoidRule)](https://docs.blender.org/api/current/bpy.types.BoidRuleAvoid.html)
    *   [BoidRuleAvoidCollision(BoidRule)](https://docs.blender.org/api/current/bpy.types.BoidRuleAvoidCollision.html)
    *   [BoidRuleFight(BoidRule)](https://docs.blender.org/api/current/bpy.types.BoidRuleFight.html)
    *   [BoidRuleFollowLeader(BoidRule)](https://docs.blender.org/api/current/bpy.types.BoidRuleFollowLeader.html)
    *   [BoidRuleGoal(BoidRule)](https://docs.blender.org/api/current/bpy.types.BoidRuleGoal.html)
    *   [BoidSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoidSettings.html)
    *   [BoidState(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoidState.html)
    *   [Bone(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Bone.html)
    *   [BoneCollection(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoneCollection.html)
    *   [BoneCollectionMemberships(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoneCollectionMemberships.html)
    *   [BoneCollections(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoneCollections.html)
    *   [BoneColor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoneColor.html)
    *   [BoolAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.BoolAttribute.html)
    *   [BoolAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BoolAttributeValue.html)
    *   [BoolProperty(Property)](https://docs.blender.org/api/current/bpy.types.BoolProperty.html)
    *   [BooleanModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.BooleanModifier.html)
    *   [BrightContrastModifier(StripModifier)](https://docs.blender.org/api/current/bpy.types.BrightContrastModifier.html)
    *   [Brush(ID)](https://docs.blender.org/api/current/bpy.types.Brush.html)
    *   [BrushCapabilities(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BrushCapabilities.html)
    *   [BrushCapabilitiesImagePaint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BrushCapabilitiesImagePaint.html)
    *   [BrushCapabilitiesSculpt(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BrushCapabilitiesSculpt.html)
    *   [BrushCapabilitiesVertexPaint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BrushCapabilitiesVertexPaint.html)
    *   [BrushCapabilitiesWeightPaint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BrushCapabilitiesWeightPaint.html)
    *   [BrushCurvesSculptSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BrushCurvesSculptSettings.html)
    *   [BrushGpencilSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.BrushGpencilSettings.html)
    *   [BrushTextureSlot(TextureSlot)](https://docs.blender.org/api/current/bpy.types.BrushTextureSlot.html)
    *   [BuildModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.BuildModifier.html)
    *   [ByteColorAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.ByteColorAttribute.html)
    *   [ByteColorAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ByteColorAttributeValue.html)
    *   [ByteIntAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.ByteIntAttribute.html)
    *   [ByteIntAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ByteIntAttributeValue.html)
    *   [CLIP_UL_tracking_objects(UIList)](https://docs.blender.org/api/current/bpy.types.CLIP_UL_tracking_objects.html)
    *   [CURVES_UL_attributes(UIList)](https://docs.blender.org/api/current/bpy.types.CURVES_UL_attributes.html)
    *   [CacheFile(ID)](https://docs.blender.org/api/current/bpy.types.CacheFile.html)
    *   [CacheFileLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CacheFileLayer.html)
    *   [CacheFileLayers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CacheFileLayers.html)
    *   [CacheObjectPath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CacheObjectPath.html)
    *   [CacheObjectPaths(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CacheObjectPaths.html)
    *   [Camera(ID)](https://docs.blender.org/api/current/bpy.types.Camera.html)
    *   [CameraBackgroundImage(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CameraBackgroundImage.html)
    *   [CameraBackgroundImages(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CameraBackgroundImages.html)
    *   [CameraDOFSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CameraDOFSettings.html)
    *   [CameraSolverConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.CameraSolverConstraint.html)
    *   [CameraStereoData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CameraStereoData.html)
    *   [CastModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.CastModifier.html)
    *   [ChannelDriverVariables(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ChannelDriverVariables.html)
    *   [ChildOfConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.ChildOfConstraint.html)
    *   [ChildParticle(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ChildParticle.html)
    *   [ClampToConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.ClampToConstraint.html)
    *   [ClothCollisionSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ClothCollisionSettings.html)
    *   [ClothModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ClothModifier.html)
    *   [ClothSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ClothSettings.html)
    *   [ClothSolverResult(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ClothSolverResult.html)
    *   [CloudsTexture(Texture)](https://docs.blender.org/api/current/bpy.types.CloudsTexture.html)
    *   [Collection(ID)](https://docs.blender.org/api/current/bpy.types.Collection.html)
    *   [CollectionChild(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollectionChild.html)
    *   [CollectionChildren(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollectionChildren.html)
    *   [CollectionExport(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollectionExport.html)
    *   [CollectionExports(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollectionExports.html)
    *   [CollectionLightLinking(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollectionLightLinking.html)
    *   [CollectionObject(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollectionObject.html)
    *   [CollectionObjects(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollectionObjects.html)
    *   [CollectionProperty(Property)](https://docs.blender.org/api/current/bpy.types.CollectionProperty.html)
    *   [CollisionModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.CollisionModifier.html)
    *   [CollisionSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CollisionSettings.html)
    *   [ColorBalanceModifier(StripModifier)](https://docs.blender.org/api/current/bpy.types.ColorBalanceModifier.html)
    *   [ColorManagedDisplaySettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorManagedDisplaySettings.html)
    *   [ColorManagedInputColorspaceSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorManagedInputColorspaceSettings.html)
    *   [ColorManagedSequencerColorspaceSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorManagedSequencerColorspaceSettings.html)
    *   [ColorManagedViewSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorManagedViewSettings.html)
    *   [ColorMapping(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorMapping.html)
    *   [ColorMixStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.ColorMixStrip.html)
    *   [ColorRamp(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorRamp.html)
    *   [ColorRampElement(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorRampElement.html)
    *   [ColorRampElements(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ColorRampElements.html)
    *   [ColorStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.ColorStrip.html)
    *   [CompositorNode(NodeInternal)](https://docs.blender.org/api/current/bpy.types.CompositorNode.html)
    *   [CompositorNodeAlphaOver(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeAlphaOver.html)
    *   [CompositorNodeAntiAliasing(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeAntiAliasing.html)
    *   [CompositorNodeBilateralblur(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeBilateralblur.html)
    *   [CompositorNodeBlur(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeBlur.html)
    *   [CompositorNodeBokehBlur(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeBokehBlur.html)
    *   [CompositorNodeBokehImage(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeBokehImage.html)
    *   [CompositorNodeBoxMask(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeBoxMask.html)
    *   [CompositorNodeBrightContrast(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeBrightContrast.html)
    *   [CompositorNodeChannelMatte(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeChannelMatte.html)
    *   [CompositorNodeChromaMatte(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeChromaMatte.html)
    *   [CompositorNodeColorBalance(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeColorBalance.html)
    *   [CompositorNodeColorCorrection(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeColorCorrection.html)
    *   [CompositorNodeColorMatte(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeColorMatte.html)
    *   [CompositorNodeColorSpill(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeColorSpill.html)
    *   [CompositorNodeCombineColor(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeCombineColor.html)
    *   [CompositorNodeConvertColorSpace(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeConvertColorSpace.html)
    *   [CompositorNodeConvertToDisplay(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeConvertToDisplay.html)
    *   [CompositorNodeConvolve(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeConvolve.html)
    *   [CompositorNodeCornerPin(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeCornerPin.html)
    *   [CompositorNodeCrop(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeCrop.html)
    *   [CompositorNodeCryptomatte(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeCryptomatte.html)
    *   [CompositorNodeCryptomatteV2(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeCryptomatteV2.html)
    *   [CompositorNodeCurveRGB(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeCurveRGB.html)
    *   [CompositorNodeCustomGroup(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeCustomGroup.html)
    *   [CompositorNodeDBlur(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDBlur.html)
    *   [CompositorNodeDefocus(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDefocus.html)
    *   [CompositorNodeDenoise(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDenoise.html)
    *   [CompositorNodeDespeckle(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDespeckle.html)
    *   [CompositorNodeDiffMatte(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDiffMatte.html)
    *   [CompositorNodeDilateErode(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDilateErode.html)
    *   [CompositorNodeDisplace(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDisplace.html)
    *   [CompositorNodeDistanceMatte(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDistanceMatte.html)
    *   [CompositorNodeDoubleEdgeMask(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeDoubleEdgeMask.html)
    *   [CompositorNodeEllipseMask(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeEllipseMask.html)
    *   [CompositorNodeExposure(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeExposure.html)
    *   [CompositorNodeFilter(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeFilter.html)
    *   [CompositorNodeFlip(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeFlip.html)
    *   [CompositorNodeGamma(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeGamma.html)
    *   [CompositorNodeGlare(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeGlare.html)
    *   [CompositorNodeGroup(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeGroup.html)
    *   [CompositorNodeHueCorrect(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeHueCorrect.html)
    *   [CompositorNodeHueSat(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeHueSat.html)
    *   [CompositorNodeIDMask(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeIDMask.html)
    *   [CompositorNodeImage(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeImage.html)
    *   [CompositorNodeImageCoordinates(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeImageCoordinates.html)
    *   [CompositorNodeImageInfo(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeImageInfo.html)
    *   [CompositorNodeInpaint(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeInpaint.html)
    *   [CompositorNodeInvert(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeInvert.html)
    *   [CompositorNodeKeying(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeKeying.html)
    *   [CompositorNodeKeyingScreen(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeKeyingScreen.html)
    *   [CompositorNodeKuwahara(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeKuwahara.html)
    *   [CompositorNodeLensdist(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeLensdist.html)
    *   [CompositorNodeLevels(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeLevels.html)
    *   [CompositorNodeLumaMatte(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeLumaMatte.html)
    *   [CompositorNodeMapUV(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeMapUV.html)
    *   [CompositorNodeMask(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeMask.html)
    *   [CompositorNodeMovieClip(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeMovieClip.html)
    *   [CompositorNodeMovieDistortion(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeMovieDistortion.html)
    *   [CompositorNodeNormal(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeNormal.html)
    *   [CompositorNodeNormalize(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeNormalize.html)
    *   [CompositorNodeOutputFile(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeOutputFile.html)
    *   [CompositorNodePixelate(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodePixelate.html)
    *   [CompositorNodePlaneTrackDeform(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodePlaneTrackDeform.html)
    *   [CompositorNodePosterize(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodePosterize.html)
    *   [CompositorNodePremulKey(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodePremulKey.html)
    *   [CompositorNodeRGB(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeRGB.html)
    *   [CompositorNodeRGBToBW(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeRGBToBW.html)
    *   [CompositorNodeRLayers(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeRLayers.html)
    *   [CompositorNodeRelativeToPixel(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeRelativeToPixel.html)
    *   [CompositorNodeRotate(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeRotate.html)
    *   [CompositorNodeScale(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeScale.html)
    *   [CompositorNodeSceneTime(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeSceneTime.html)
    *   [CompositorNodeSeparateColor(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeSeparateColor.html)
    *   [CompositorNodeSetAlpha(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeSetAlpha.html)
    *   [CompositorNodeSplit(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeSplit.html)
    *   [CompositorNodeStabilize(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeStabilize.html)
    *   [CompositorNodeSwitch(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeSwitch.html)
    *   [CompositorNodeSwitchView(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeSwitchView.html)
    *   [CompositorNodeTime(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeTime.html)
    *   [CompositorNodeTonemap(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeTonemap.html)
    *   [CompositorNodeTrackPos(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeTrackPos.html)
    *   [CompositorNodeTransform(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeTransform.html)
    *   [CompositorNodeTranslate(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeTranslate.html)
    *   [CompositorNodeTree(NodeTree)](https://docs.blender.org/api/current/bpy.types.CompositorNodeTree.html)
    *   [CompositorNodeVecBlur(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeVecBlur.html)
    *   [CompositorNodeViewer(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeViewer.html)
    *   [CompositorNodeZcombine(CompositorNode)](https://docs.blender.org/api/current/bpy.types.CompositorNodeZcombine.html)
    *   [ConsoleLine(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ConsoleLine.html)
    *   [Constraint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Constraint.html)
    *   [ConstraintTarget(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ConstraintTarget.html)
    *   [ConstraintTargetBone(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ConstraintTargetBone.html)
    *   [Context(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Context.html)
    *   [CopyLocationConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.CopyLocationConstraint.html)
    *   [CopyRotationConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.CopyRotationConstraint.html)
    *   [CopyScaleConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.CopyScaleConstraint.html)
    *   [CopyTransformsConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.CopyTransformsConstraint.html)
    *   [CorrectiveSmoothModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.CorrectiveSmoothModifier.html)
    *   [CrossStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.CrossStrip.html)
    *   [CryptomatteEntry(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CryptomatteEntry.html)
    *   [Curve(ID)](https://docs.blender.org/api/current/bpy.types.Curve.html)
    *   [CurveMap(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveMap.html)
    *   [CurveMapPoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveMapPoint.html)
    *   [CurveMapPoints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveMapPoints.html)
    *   [CurveMapping(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveMapping.html)
    *   [CurveModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.CurveModifier.html)
    *   [CurvePaintSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurvePaintSettings.html)
    *   [CurvePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurvePoint.html)
    *   [CurveProfile(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveProfile.html)
    *   [CurveProfilePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveProfilePoint.html)
    *   [CurveProfilePoints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveProfilePoints.html)
    *   [CurveSlice(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveSlice.html)
    *   [CurveSplines(bpy_struct)](https://docs.blender.org/api/current/bpy.types.CurveSplines.html)
    *   [Curves(ID)](https://docs.blender.org/api/current/bpy.types.Curves.html)
    *   [CurvesModifier(StripModifier)](https://docs.blender.org/api/current/bpy.types.CurvesModifier.html)
    *   [CurvesSculpt(Paint)](https://docs.blender.org/api/current/bpy.types.CurvesSculpt.html)
    *   [DATA_UL_bone_collections(UIList)](https://docs.blender.org/api/current/bpy.types.DATA_UL_bone_collections.html)
    *   [DampedTrackConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.DampedTrackConstraint.html)
    *   [DataTransferModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.DataTransferModifier.html)
    *   [DecimateModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.DecimateModifier.html)
    *   [Depsgraph(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Depsgraph.html)
    *   [DepsgraphObjectInstance(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DepsgraphObjectInstance.html)
    *   [DepsgraphUpdate(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DepsgraphUpdate.html)
    *   [DisplaceModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.DisplaceModifier.html)
    *   [DisplaySafeAreas(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DisplaySafeAreas.html)
    *   [DistortedNoiseTexture(Texture)](https://docs.blender.org/api/current/bpy.types.DistortedNoiseTexture.html)
    *   [DopeSheet(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DopeSheet.html)
    *   [Driver(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Driver.html)
    *   [DriverTarget(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DriverTarget.html)
    *   [DriverVariable(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DriverVariable.html)
    *   [DynamicPaintBrushSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DynamicPaintBrushSettings.html)
    *   [DynamicPaintCanvasSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DynamicPaintCanvasSettings.html)
    *   [DynamicPaintModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.DynamicPaintModifier.html)
    *   [DynamicPaintSurface(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DynamicPaintSurface.html)
    *   [DynamicPaintSurfaces(bpy_struct)](https://docs.blender.org/api/current/bpy.types.DynamicPaintSurfaces.html)
    *   [EQCurveMappingData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.EQCurveMappingData.html)
    *   [EdgeSplitModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.EdgeSplitModifier.html)
    *   [EditBone(bpy_struct)](https://docs.blender.org/api/current/bpy.types.EditBone.html)
    *   [EffectStrip(Strip)](https://docs.blender.org/api/current/bpy.types.EffectStrip.html)
    *   [EffectorWeights(bpy_struct)](https://docs.blender.org/api/current/bpy.types.EffectorWeights.html)
    *   [EnumProperty(Property)](https://docs.blender.org/api/current/bpy.types.EnumProperty.html)
    *   [EnumPropertyItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.EnumPropertyItem.html)
    *   [EvaluateClosureNodeViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.EvaluateClosureNodeViewerPathElem.html)
    *   [Event(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Event.html)
    *   [ExplodeModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ExplodeModifier.html)
    *   [FCurve(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FCurve.html)
    *   [FCurveKeyframePoints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FCurveKeyframePoints.html)
    *   [FCurveModifiers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FCurveModifiers.html)
    *   [FCurveSample(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FCurveSample.html)
    *   [FFmpegSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FFmpegSettings.html)
    *   [FILEBROWSER_UL_dir(UIList)](https://docs.blender.org/api/current/bpy.types.FILEBROWSER_UL_dir.html)
    *   [FModifier(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FModifier.html)
    *   [FModifierCycles(FModifier)](https://docs.blender.org/api/current/bpy.types.FModifierCycles.html)
    *   [FModifierEnvelope(FModifier)](https://docs.blender.org/api/current/bpy.types.FModifierEnvelope.html)
    *   [FModifierEnvelopeControlPoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FModifierEnvelopeControlPoint.html)
    *   [FModifierEnvelopeControlPoints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FModifierEnvelopeControlPoints.html)
    *   [FModifierFunctionGenerator(FModifier)](https://docs.blender.org/api/current/bpy.types.FModifierFunctionGenerator.html)
    *   [FModifierGenerator(FModifier)](https://docs.blender.org/api/current/bpy.types.FModifierGenerator.html)
    *   [FModifierLimits(FModifier)](https://docs.blender.org/api/current/bpy.types.FModifierLimits.html)
    *   [FModifierNoise(FModifier)](https://docs.blender.org/api/current/bpy.types.FModifierNoise.html)
    *   [FModifierStepped(FModifier)](https://docs.blender.org/api/current/bpy.types.FModifierStepped.html)
    *   [FieldSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FieldSettings.html)
    *   [FileAssetSelectIDFilter(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FileAssetSelectIDFilter.html)
    *   [FileAssetSelectParams(FileSelectParams)](https://docs.blender.org/api/current/bpy.types.FileAssetSelectParams.html)
    *   [FileBrowserFSMenuEntry(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FileBrowserFSMenuEntry.html)
    *   [FileHandler(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FileHandler.html)
    *   [FileSelectEntry(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FileSelectEntry.html)
    *   [FileSelectIDFilter(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FileSelectIDFilter.html)
    *   [FileSelectParams(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FileSelectParams.html)
    *   [Float2Attribute(Attribute)](https://docs.blender.org/api/current/bpy.types.Float2Attribute.html)
    *   [Float2AttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Float2AttributeValue.html)
    *   [Float4x4Attribute(Attribute)](https://docs.blender.org/api/current/bpy.types.Float4x4Attribute.html)
    *   [Float4x4AttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Float4x4AttributeValue.html)
    *   [FloatAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.FloatAttribute.html)
    *   [FloatAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FloatAttributeValue.html)
    *   [FloatColorAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.FloatColorAttribute.html)
    *   [FloatColorAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FloatColorAttributeValue.html)
    *   [FloatProperty(Property)](https://docs.blender.org/api/current/bpy.types.FloatProperty.html)
    *   [FloatVectorAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.FloatVectorAttribute.html)
    *   [FloatVectorAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FloatVectorAttributeValue.html)
    *   [FloatVectorValueReadOnly(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FloatVectorValueReadOnly.html)
    *   [FloorConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.FloorConstraint.html)
    *   [FluidDomainSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FluidDomainSettings.html)
    *   [FluidEffectorSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FluidEffectorSettings.html)
    *   [FluidFlowSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FluidFlowSettings.html)
    *   [FluidModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.FluidModifier.html)
    *   [FollowPathConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.FollowPathConstraint.html)
    *   [FollowTrackConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.FollowTrackConstraint.html)
    *   [ForeachGeometryElementGenerationItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ForeachGeometryElementGenerationItem.html)
    *   [ForeachGeometryElementInputItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ForeachGeometryElementInputItem.html)
    *   [ForeachGeometryElementMainItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ForeachGeometryElementMainItem.html)
    *   [ForeachGeometryElementZoneViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.ForeachGeometryElementZoneViewerPathElem.html)
    *   [FreestyleLineSet(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FreestyleLineSet.html)
    *   [FreestyleLineStyle(ID)](https://docs.blender.org/api/current/bpy.types.FreestyleLineStyle.html)
    *   [FreestyleModuleSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FreestyleModuleSettings.html)
    *   [FreestyleModules(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FreestyleModules.html)
    *   [FreestyleSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.FreestyleSettings.html)
    *   [Function(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Function.html)
    *   [FunctionNode(NodeInternal)](https://docs.blender.org/api/current/bpy.types.FunctionNode.html)
    *   [FunctionNodeAlignEulerToVector(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
    *   [FunctionNodeAlignRotationToVector(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignRotationToVector.html)
    *   [FunctionNodeAxesToRotation(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeAxesToRotation.html)
    *   [FunctionNodeAxisAngleToRotation(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeAxisAngleToRotation.html)
    *   [FunctionNodeBitMath(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeBitMath.html)
    *   [FunctionNodeBooleanMath(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
    *   [FunctionNodeCombineColor(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)
    *   [FunctionNodeCombineMatrix(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineMatrix.html)
    *   [FunctionNodeCombineTransform(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineTransform.html)
    *   [FunctionNodeCompare(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
    *   [FunctionNodeEulerToRotation(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeEulerToRotation.html)
    *   [FunctionNodeFindInString(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeFindInString.html)
    *   [FunctionNodeFloatToInt(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)
    *   [FunctionNodeFormatString(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeFormatString.html)
    *   [FunctionNodeHashValue(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeHashValue.html)
    *   [FunctionNodeInputBool(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)
    *   [FunctionNodeInputColor(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)
    *   [FunctionNodeInputInt(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html)
    *   [FunctionNodeInputRotation(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputRotation.html)
    *   [FunctionNodeInputSpecialCharacters(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)
    *   [FunctionNodeInputString(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputString.html)
    *   [FunctionNodeInputVector(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)
    *   [FunctionNodeIntegerMath(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeIntegerMath.html)
    *   [FunctionNodeInvertMatrix(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInvertMatrix.html)
    *   [FunctionNodeInvertRotation(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeInvertRotation.html)
    *   [FunctionNodeMatchString(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeMatchString.html)
    *   [FunctionNodeMatrixDeterminant(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeMatrixDeterminant.html)
    *   [FunctionNodeMatrixMultiply(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeMatrixMultiply.html)
    *   [FunctionNodeProjectPoint(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeProjectPoint.html)
    *   [FunctionNodeQuaternionToRotation(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeQuaternionToRotation.html)
    *   [FunctionNodeRandomValue(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
    *   [FunctionNodeReplaceString(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)
    *   [FunctionNodeRotateEuler(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
    *   [FunctionNodeRotateRotation(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateRotation.html)
    *   [FunctionNodeRotateVector(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateVector.html)
    *   [FunctionNodeRotationToAxisAngle(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotationToAxisAngle.html)
    *   [FunctionNodeRotationToEuler(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotationToEuler.html)
    *   [FunctionNodeRotationToQuaternion(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotationToQuaternion.html)
    *   [FunctionNodeSeparateColor(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
    *   [FunctionNodeSeparateMatrix(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateMatrix.html)
    *   [FunctionNodeSeparateTransform(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateTransform.html)
    *   [FunctionNodeSliceString(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
    *   [FunctionNodeStringLength(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)
    *   [FunctionNodeStringToValue(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringToValue.html)
    *   [FunctionNodeTransformDirection(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeTransformDirection.html)
    *   [FunctionNodeTransformPoint(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeTransformPoint.html)
    *   [FunctionNodeTransposeMatrix(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeTransposeMatrix.html)
    *   [FunctionNodeValueToString(FunctionNode)](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)
    *   [GPENCIL_UL_annotation_layer(UIList)](https://docs.blender.org/api/current/bpy.types.GPENCIL_UL_annotation_layer.html)
    *   [GPENCIL_UL_matslots(UIList)](https://docs.blender.org/api/current/bpy.types.GPENCIL_UL_matslots.html)
    *   [GPencilInterpolateSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GPencilInterpolateSettings.html)
    *   [GPencilSculptGuide(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GPencilSculptGuide.html)
    *   [GPencilSculptSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GPencilSculptSettings.html)
    *   [GREASE_PENCIL_UL_attributes(UIList)](https://docs.blender.org/api/current/bpy.types.GREASE_PENCIL_UL_attributes.html)
    *   [GREASE_PENCIL_UL_masks(UIList)](https://docs.blender.org/api/current/bpy.types.GREASE_PENCIL_UL_masks.html)
    *   [GammaCrossStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.GammaCrossStrip.html)
    *   [GaussianBlurStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.GaussianBlurStrip.html)
    *   [GeometryAttributeConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.GeometryAttributeConstraint.html)
    *   [GeometryNode(NodeInternal)](https://docs.blender.org/api/current/bpy.types.GeometryNode.html)
    *   [GeometryNodeAccumulateField(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
    *   [GeometryNodeAttributeDomainSize(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
    *   [GeometryNodeAttributeStatistic(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
    *   [GeometryNodeBake(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeBake.html)
    *   [GeometryNodeBlurAttribute(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)
    *   [GeometryNodeBoundBox(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
    *   [GeometryNodeCameraInfo(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCameraInfo.html)
    *   [GeometryNodeCaptureAttribute(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
    *   [GeometryNodeCollectionInfo(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
    *   [GeometryNodeConvexHull(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
    *   [GeometryNodeCornersOfEdge(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfEdge.html)
    *   [GeometryNodeCornersOfFace(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)
    *   [GeometryNodeCornersOfVertex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)
    *   [GeometryNodeCurveArc(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
    *   [GeometryNodeCurveEndpointSelection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
    *   [GeometryNodeCurveHandleTypeSelection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
    *   [GeometryNodeCurveLength(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
    *   [GeometryNodeCurveOfPoint(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)
    *   [GeometryNodeCurvePrimitiveBezierSegment(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
    *   [GeometryNodeCurvePrimitiveCircle(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
    *   [GeometryNodeCurvePrimitiveLine(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
    *   [GeometryNodeCurvePrimitiveQuadrilateral(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
    *   [GeometryNodeCurveQuadraticBezier(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)
    *   [GeometryNodeCurveSetHandles(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
    *   [GeometryNodeCurveSpiral(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
    *   [GeometryNodeCurveSplineType(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
    *   [GeometryNodeCurveStar(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
    *   [GeometryNodeCurveToMesh(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)
    *   [GeometryNodeCurveToPoints(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
    *   [GeometryNodeCurvesToGreasePencil(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvesToGreasePencil.html)
    *   [GeometryNodeCustomGroup(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeCustomGroup.html)
    *   [GeometryNodeDeformCurvesOnSurface(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)
    *   [GeometryNodeDeleteGeometry(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)
    *   [GeometryNodeDistributePointsInGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInGrid.html)
    *   [GeometryNodeDistributePointsInVolume(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)
    *   [GeometryNodeDistributePointsOnFaces(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
    *   [GeometryNodeDualMesh(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)
    *   [GeometryNodeDuplicateElements(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
    *   [GeometryNodeEdgePathsToCurves(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)
    *   [GeometryNodeEdgePathsToSelection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)
    *   [GeometryNodeEdgesOfCorner(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)
    *   [GeometryNodeEdgesOfVertex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)
    *   [GeometryNodeEdgesToFaceGroups(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesToFaceGroups.html)
    *   [GeometryNodeExtrudeMesh(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
    *   [GeometryNodeFaceOfCorner(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)
    *   [GeometryNodeFieldAtIndex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
    *   [GeometryNodeFieldAverage(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAverage.html)
    *   [GeometryNodeFieldMinAndMax(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldMinAndMax.html)
    *   [GeometryNodeFieldOnDomain(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
    *   [GeometryNodeFieldToGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldToGrid.html)
    *   [GeometryNodeFieldToGridItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldToGridItem.html)
    *   [GeometryNodeFieldToGridItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldToGridItems.html)
    *   [GeometryNodeFieldVariance(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldVariance.html)
    *   [GeometryNodeFillCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
    *   [GeometryNodeFilletCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
    *   [GeometryNodeFlipFaces(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)
    *   [GeometryNodeForeachGeometryElementInput(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeForeachGeometryElementInput.html)
    *   [GeometryNodeForeachGeometryElementOutput(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeForeachGeometryElementOutput.html)
    *   [GeometryNodeGeometryToInstance(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
    *   [GeometryNodeGetNamedGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGetNamedGrid.html)
    *   [GeometryNodeGizmoDial(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGizmoDial.html)
    *   [GeometryNodeGizmoLinear(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGizmoLinear.html)
    *   [GeometryNodeGizmoTransform(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGizmoTransform.html)
    *   [GeometryNodeGreasePencilToCurves(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGreasePencilToCurves.html)
    *   [GeometryNodeGridAdvect(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridAdvect.html)
    *   [GeometryNodeGridCurl(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridCurl.html)
    *   [GeometryNodeGridDivergence(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridDivergence.html)
    *   [GeometryNodeGridGradient(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridGradient.html)
    *   [GeometryNodeGridInfo(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridInfo.html)
    *   [GeometryNodeGridLaplacian(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridLaplacian.html)
    *   [GeometryNodeGridPrune(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridPrune.html)
    *   [GeometryNodeGridToMesh(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridToMesh.html)
    *   [GeometryNodeGridVoxelize(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGridVoxelize.html)
    *   [GeometryNodeGroup(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeGroup.html)
    *   [GeometryNodeImageInfo(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageInfo.html)
    *   [GeometryNodeImageTexture(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)
    *   [GeometryNodeImportCSV(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImportCSV.html)
    *   [GeometryNodeImportOBJ(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImportOBJ.html)
    *   [GeometryNodeImportPLY(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImportPLY.html)
    *   [GeometryNodeImportSTL(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImportSTL.html)
    *   [GeometryNodeImportText(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImportText.html)
    *   [GeometryNodeImportVDB(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeImportVDB.html)
    *   [GeometryNodeIndexOfNearest(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeIndexOfNearest.html)
    *   [GeometryNodeIndexSwitch(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeIndexSwitch.html)
    *   [GeometryNodeInputActiveCamera(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputActiveCamera.html)
    *   [GeometryNodeInputCollection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCollection.html)
    *   [GeometryNodeInputCurveHandlePositions(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
    *   [GeometryNodeInputCurveTilt(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)
    *   [GeometryNodeInputEdgeSmooth(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputEdgeSmooth.html)
    *   [GeometryNodeInputID(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
    *   [GeometryNodeInputImage(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputImage.html)
    *   [GeometryNodeInputIndex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
    *   [GeometryNodeInputInstanceBounds(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceBounds.html)
    *   [GeometryNodeInputInstanceRotation(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)
    *   [GeometryNodeInputInstanceScale(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)
    *   [GeometryNodeInputMaterial(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)
    *   [GeometryNodeInputMaterialIndex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)
    *   [GeometryNodeInputMeshEdgeAngle(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
    *   [GeometryNodeInputMeshEdgeNeighbors(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
    *   [GeometryNodeInputMeshEdgeVertices(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
    *   [GeometryNodeInputMeshFaceArea(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)
    *   [GeometryNodeInputMeshFaceIsPlanar(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)
    *   [GeometryNodeInputMeshFaceNeighbors(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
    *   [GeometryNodeInputMeshIsland(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)
    *   [GeometryNodeInputMeshVertexNeighbors(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)
    *   [GeometryNodeInputNamedAttribute(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
    *   [GeometryNodeInputNamedLayerSelection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedLayerSelection.html)
    *   [GeometryNodeInputNormal(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
    *   [GeometryNodeInputObject(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputObject.html)
    *   [GeometryNodeInputPosition(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
    *   [GeometryNodeInputRadius(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
    *   [GeometryNodeInputSceneTime(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
    *   [GeometryNodeInputShadeSmooth(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)
    *   [GeometryNodeInputShortestEdgePaths(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)
    *   [GeometryNodeInputSplineCyclic(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)
    *   [GeometryNodeInputSplineResolution(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)
    *   [GeometryNodeInputTangent(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)
    *   [GeometryNodeInputVoxelIndex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputVoxelIndex.html)
    *   [GeometryNodeInstanceOnPoints(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
    *   [GeometryNodeInstanceTransform(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceTransform.html)
    *   [GeometryNodeInstancesToPoints(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
    *   [GeometryNodeInterpolateCurves(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeInterpolateCurves.html)
    *   [GeometryNodeIsViewport(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)
    *   [GeometryNodeJoinGeometry(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
    *   [GeometryNodeList(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeList.html)
    *   [GeometryNodeListGetItem(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeListGetItem.html)
    *   [GeometryNodeListLength(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeListLength.html)
    *   [GeometryNodeMaterialSelection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
    *   [GeometryNodeMenuSwitch(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMenuSwitch.html)
    *   [GeometryNodeMergeByDistance(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
    *   [GeometryNodeMergeLayers(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeLayers.html)
    *   [GeometryNodeMeshBoolean(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
    *   [GeometryNodeMeshCircle(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
    *   [GeometryNodeMeshCone(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)
    *   [GeometryNodeMeshCube(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)
    *   [GeometryNodeMeshCylinder(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)
    *   [GeometryNodeMeshFaceSetBoundaries(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)
    *   [GeometryNodeMeshGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)
    *   [GeometryNodeMeshIcoSphere(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
    *   [GeometryNodeMeshLine(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
    *   [GeometryNodeMeshToCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
    *   [GeometryNodeMeshToDensityGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToDensityGrid.html)
    *   [GeometryNodeMeshToPoints(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
    *   [GeometryNodeMeshToSDFGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToSDFGrid.html)
    *   [GeometryNodeMeshToVolume(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)
    *   [GeometryNodeMeshUVSphere(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)
    *   [GeometryNodeObjectInfo(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
    *   [GeometryNodeOffsetCornerInFace(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)
    *   [GeometryNodeOffsetPointInCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)
    *   [GeometryNodePoints(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)
    *   [GeometryNodePointsOfCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)
    *   [GeometryNodePointsToCurves(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToCurves.html)
    *   [GeometryNodePointsToSDFGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToSDFGrid.html)
    *   [GeometryNodePointsToVertices(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
    *   [GeometryNodePointsToVolume(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)
    *   [GeometryNodeProximity(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
    *   [GeometryNodeRaycast(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
    *   [GeometryNodeRealizeInstances(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
    *   [GeometryNodeRemoveAttribute(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
    *   [GeometryNodeRepeatInput(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeRepeatInput.html)
    *   [GeometryNodeRepeatOutput(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeRepeatOutput.html)
    *   [GeometryNodeReplaceMaterial(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
    *   [GeometryNodeResampleCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
    *   [GeometryNodeReverseCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
    *   [GeometryNodeRotateInstances(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
    *   [GeometryNodeSDFGridBoolean(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFGridBoolean.html)
    *   [GeometryNodeSDFGridFillet(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFGridFillet.html)
    *   [GeometryNodeSDFGridLaplacian(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFGridLaplacian.html)
    *   [GeometryNodeSDFGridMean(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFGridMean.html)
    *   [GeometryNodeSDFGridMeanCurvature(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFGridMeanCurvature.html)
    *   [GeometryNodeSDFGridMedian(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFGridMedian.html)
    *   [GeometryNodeSDFGridOffset(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFGridOffset.html)
    *   [GeometryNodeSampleCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
    *   [GeometryNodeSampleGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleGrid.html)
    *   [GeometryNodeSampleGridIndex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleGridIndex.html)
    *   [GeometryNodeSampleIndex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
    *   [GeometryNodeSampleNearest(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)
    *   [GeometryNodeSampleNearestSurface(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
    *   [GeometryNodeSampleUVSurface(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
    *   [GeometryNodeScaleElements(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
    *   [GeometryNodeScaleInstances(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
    *   [GeometryNodeSelfObject(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)
    *   [GeometryNodeSeparateComponents(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
    *   [GeometryNodeSeparateGeometry(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
    *   [GeometryNodeSetCurveHandlePositions(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
    *   [GeometryNodeSetCurveNormal(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)
    *   [GeometryNodeSetCurveRadius(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
    *   [GeometryNodeSetCurveTilt(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
    *   [GeometryNodeSetGeometryName(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetGeometryName.html)
    *   [GeometryNodeSetGreasePencilColor(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetGreasePencilColor.html)
    *   [GeometryNodeSetGreasePencilDepth(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetGreasePencilDepth.html)
    *   [GeometryNodeSetGreasePencilSoftness(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetGreasePencilSoftness.html)
    *   [GeometryNodeSetGridBackground(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetGridBackground.html)
    *   [GeometryNodeSetGridTransform(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetGridTransform.html)
    *   [GeometryNodeSetID(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
    *   [GeometryNodeSetInstanceTransform(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetInstanceTransform.html)
    *   [GeometryNodeSetMaterial(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
    *   [GeometryNodeSetMaterialIndex(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
    *   [GeometryNodeSetMeshNormal(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMeshNormal.html)
    *   [GeometryNodeSetPointRadius(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
    *   [GeometryNodeSetPosition(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
    *   [GeometryNodeSetShadeSmooth(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)
    *   [GeometryNodeSetSplineCyclic(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
    *   [GeometryNodeSetSplineResolution(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
    *   [GeometryNodeSimulationInput(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSimulationInput.html)
    *   [GeometryNodeSimulationOutput(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSimulationOutput.html)
    *   [GeometryNodeSortElements(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSortElements.html)
    *   [GeometryNodeSplineLength(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
    *   [GeometryNodeSplineParameter(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
    *   [GeometryNodeSplitEdges(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)
    *   [GeometryNodeSplitToInstances(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitToInstances.html)
    *   [GeometryNodeStoreNamedAttribute(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
    *   [GeometryNodeStoreNamedGrid(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedGrid.html)
    *   [GeometryNodeStringJoin(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
    *   [GeometryNodeStringToCurves(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
    *   [GeometryNodeSubdivideCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
    *   [GeometryNodeSubdivideMesh(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)
    *   [GeometryNodeSubdivisionSurface(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)
    *   [GeometryNodeSwitch(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
    *   [GeometryNodeTool3DCursor(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeTool3DCursor.html)
    *   [GeometryNodeToolActiveElement(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeToolActiveElement.html)
    *   [GeometryNodeToolFaceSet(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeToolFaceSet.html)
    *   [GeometryNodeToolMousePosition(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeToolMousePosition.html)
    *   [GeometryNodeToolSelection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeToolSelection.html)
    *   [GeometryNodeToolSetFaceSet(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeToolSetFaceSet.html)
    *   [GeometryNodeToolSetSelection(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeToolSetSelection.html)
    *   [GeometryNodeTransform(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
    *   [GeometryNodeTranslateInstances(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)
    *   [GeometryNodeTree(NodeTree)](https://docs.blender.org/api/current/bpy.types.GeometryNodeTree.html)
    *   [GeometryNodeTriangulate(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)
    *   [GeometryNodeTrimCurve(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
    *   [GeometryNodeUVPackIslands(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)
    *   [GeometryNodeUVTangent(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVTangent.html)
    *   [GeometryNodeUVUnwrap(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)
    *   [GeometryNodeVertexOfCorner(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)
    *   [GeometryNodeViewer(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    *   [GeometryNodeViewportTransform(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewportTransform.html)
    *   [GeometryNodeVolumeCube(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)
    *   [GeometryNodeVolumeToMesh(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)
    *   [GeometryNodeWarning(GeometryNode)](https://docs.blender.org/api/current/bpy.types.GeometryNodeWarning.html)
    *   [GeometrySet](https://docs.blender.org/api/current/bpy.types.GeometrySet.html)
    *   [Gizmo(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Gizmo.html)
    *   [GizmoGroup(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GizmoGroup.html)
    *   [GizmoGroupProperties(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GizmoGroupProperties.html)
    *   [GizmoProperties(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GizmoProperties.html)
    *   [Gizmos(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Gizmos.html)
    *   [GlowStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.GlowStrip.html)
    *   [GpPaint(Paint)](https://docs.blender.org/api/current/bpy.types.GpPaint.html)
    *   [GpSculptPaint(Paint)](https://docs.blender.org/api/current/bpy.types.GpSculptPaint.html)
    *   [GpVertexPaint(Paint)](https://docs.blender.org/api/current/bpy.types.GpVertexPaint.html)
    *   [GpWeightPaint(Paint)](https://docs.blender.org/api/current/bpy.types.GpWeightPaint.html)
    *   [GreasePencil(ID)](https://docs.blender.org/api/current/bpy.types.GreasePencil.html)
    *   [GreasePencilArmatureModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilArmatureModifier.html)
    *   [GreasePencilArrayModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilArrayModifier.html)
    *   [GreasePencilBuildModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilBuildModifier.html)
    *   [GreasePencilColorModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilColorModifier.html)
    *   [GreasePencilDashModifierData(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilDashModifierData.html)
    *   [GreasePencilDashModifierSegment(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilDashModifierSegment.html)
    *   [GreasePencilDrawing(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilDrawing.html)
    *   [GreasePencilEnvelopeModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilEnvelopeModifier.html)
    *   [GreasePencilFrame(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilFrame.html)
    *   [GreasePencilFrames(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilFrames.html)
    *   [GreasePencilHookModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilHookModifier.html)
    *   [GreasePencilLatticeModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilLatticeModifier.html)
    *   [GreasePencilLayer(GreasePencilTreeNode)](https://docs.blender.org/api/current/bpy.types.GreasePencilLayer.html)
    *   [GreasePencilLayerGroup(GreasePencilTreeNode)](https://docs.blender.org/api/current/bpy.types.GreasePencilLayerGroup.html)
    *   [GreasePencilLayerMask(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilLayerMask.html)
    *   [GreasePencilLayerMasks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilLayerMasks.html)
    *   [GreasePencilLengthModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilLengthModifier.html)
    *   [GreasePencilLineartModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilLineartModifier.html)
    *   [GreasePencilMirrorModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilMirrorModifier.html)
    *   [GreasePencilMultiplyModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilMultiplyModifier.html)
    *   [GreasePencilNoiseModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilNoiseModifier.html)
    *   [GreasePencilOffsetModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilOffsetModifier.html)
    *   [GreasePencilOpacityModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilOpacityModifier.html)
    *   [GreasePencilOutlineModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilOutlineModifier.html)
    *   [GreasePencilShrinkwrapModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilShrinkwrapModifier.html)
    *   [GreasePencilSimplifyModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilSimplifyModifier.html)
    *   [GreasePencilSmoothModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilSmoothModifier.html)
    *   [GreasePencilSubdivModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilSubdivModifier.html)
    *   [GreasePencilTextureModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilTextureModifier.html)
    *   [GreasePencilThickModifierData(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilThickModifierData.html)
    *   [GreasePencilTimeModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilTimeModifier.html)
    *   [GreasePencilTimeModifierSegment(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilTimeModifierSegment.html)
    *   [GreasePencilTintModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilTintModifier.html)
    *   [GreasePencilTreeNode(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilTreeNode.html)
    *   [GreasePencilWeightAngleModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilWeightAngleModifier.html)
    *   [GreasePencilWeightProximityModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.GreasePencilWeightProximityModifier.html)
    *   [GreasePencilv3LayerGroup(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilv3LayerGroup.html)
    *   [GreasePencilv3Layers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.GreasePencilv3Layers.html)
    *   [GroupNodeViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.GroupNodeViewerPathElem.html)
    *   [Header(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Header.html)
    *   [Histogram(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Histogram.html)
    *   [HookModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.HookModifier.html)
    *   [HueCorrectModifier(StripModifier)](https://docs.blender.org/api/current/bpy.types.HueCorrectModifier.html)
    *   [HydraRenderEngine(RenderEngine)](https://docs.blender.org/api/current/bpy.types.HydraRenderEngine.html)
    *   [ID(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ID.html)
    *   [IDMaterials(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IDMaterials.html)
    *   [IDOverrideLibrary(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IDOverrideLibrary.html)
    *   [IDOverrideLibraryProperties(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IDOverrideLibraryProperties.html)
    *   [IDOverrideLibraryProperty(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IDOverrideLibraryProperty.html)
    *   [IDOverrideLibraryPropertyOperation(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IDOverrideLibraryPropertyOperation.html)
    *   [IDOverrideLibraryPropertyOperations(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IDOverrideLibraryPropertyOperations.html)
    *   [IDPropertyWrapPtr(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IDPropertyWrapPtr.html)
    *   [IDViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.IDViewerPathElem.html)
    *   [IKParam(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IKParam.html)
    *   [IMAGE_AST_brush_paint(AssetShelf)](https://docs.blender.org/api/current/bpy.types.IMAGE_AST_brush_paint.html)
    *   [IMAGE_FH_drop_handler(FileHandler)](https://docs.blender.org/api/current/bpy.types.IMAGE_FH_drop_handler.html)
    *   [IMAGE_UL_render_slots(UIList)](https://docs.blender.org/api/current/bpy.types.IMAGE_UL_render_slots.html)
    *   [IMAGE_UL_udim_tiles(UIList)](https://docs.blender.org/api/current/bpy.types.IMAGE_UL_udim_tiles.html)
    *   [IO_FH_gltf2(FileHandler)](https://docs.blender.org/api/current/bpy.types.IO_FH_gltf2.html)
    *   [IO_FH_svg_as_curves(FileHandler)](https://docs.blender.org/api/current/bpy.types.IO_FH_svg_as_curves.html)
    *   [Image(ID)](https://docs.blender.org/api/current/bpy.types.Image.html)
    *   [ImageFormatSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ImageFormatSettings.html)
    *   [ImagePackedFile(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ImagePackedFile.html)
    *   [ImagePaint(Paint)](https://docs.blender.org/api/current/bpy.types.ImagePaint.html)
    *   [ImagePreview(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ImagePreview.html)
    *   [ImageStrip(Strip)](https://docs.blender.org/api/current/bpy.types.ImageStrip.html)
    *   [ImageTexture(Texture)](https://docs.blender.org/api/current/bpy.types.ImageTexture.html)
    *   [ImageUser(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ImageUser.html)
    *   [IndexSwitchItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IndexSwitchItem.html)
    *   [InlineShaderNodes](https://docs.blender.org/api/current/bpy.types.InlineShaderNodes.html)
    *   [Int2Attribute(Attribute)](https://docs.blender.org/api/current/bpy.types.Int2Attribute.html)
    *   [Int2AttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Int2AttributeValue.html)
    *   [IntAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.IntAttribute.html)
    *   [IntAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.IntAttributeValue.html)
    *   [IntProperty(Property)](https://docs.blender.org/api/current/bpy.types.IntProperty.html)
    *   [Itasc(IKParam)](https://docs.blender.org/api/current/bpy.types.Itasc.html)
    *   [Key(ID)](https://docs.blender.org/api/current/bpy.types.Key.html)
    *   [KeyConfig(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyConfig.html)
    *   [KeyConfigPreferences(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyConfigPreferences.html)
    *   [KeyConfigurations(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyConfigurations.html)
    *   [KeyMap(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyMap.html)
    *   [KeyMapItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyMapItem.html)
    *   [KeyMapItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyMapItems.html)
    *   [KeyMaps(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyMaps.html)
    *   [Keyframe(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Keyframe.html)
    *   [KeyingSet(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyingSet.html)
    *   [KeyingSetInfo(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyingSetInfo.html)
    *   [KeyingSetPath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyingSetPath.html)
    *   [KeyingSetPaths(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyingSetPaths.html)
    *   [KeyingSets(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyingSets.html)
    *   [KeyingSetsAll(bpy_struct)](https://docs.blender.org/api/current/bpy.types.KeyingSetsAll.html)
    *   [KinematicConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.KinematicConstraint.html)
    *   [LaplacianDeformModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.LaplacianDeformModifier.html)
    *   [LaplacianSmoothModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.LaplacianSmoothModifier.html)
    *   [Lattice(ID)](https://docs.blender.org/api/current/bpy.types.Lattice.html)
    *   [LatticeModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.LatticeModifier.html)
    *   [LatticePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LatticePoint.html)
    *   [LayerCollection(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LayerCollection.html)
    *   [LayerObjects(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LayerObjects.html)
    *   [LayoutPanelState(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LayoutPanelState.html)
    *   [Library(ID)](https://docs.blender.org/api/current/bpy.types.Library.html)
    *   [LibraryWeakReference(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LibraryWeakReference.html)
    *   [Light(ID)](https://docs.blender.org/api/current/bpy.types.Light.html)
    *   [LightProbe(ID)](https://docs.blender.org/api/current/bpy.types.LightProbe.html)
    *   [LightProbePlane(LightProbe)](https://docs.blender.org/api/current/bpy.types.LightProbePlane.html)
    *   [LightProbeSphere(LightProbe)](https://docs.blender.org/api/current/bpy.types.LightProbeSphere.html)
    *   [LightProbeVolume(LightProbe)](https://docs.blender.org/api/current/bpy.types.LightProbeVolume.html)
    *   [Lightgroup(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Lightgroup.html)
    *   [Lightgroups(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Lightgroups.html)
    *   [LimitDistanceConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.LimitDistanceConstraint.html)
    *   [LimitLocationConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.LimitLocationConstraint.html)
    *   [LimitRotationConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.LimitRotationConstraint.html)
    *   [LimitScaleConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.LimitScaleConstraint.html)
    *   [LineStyleAlphaModifier(LineStyleModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier.html)
    *   [LineStyleAlphaModifier_AlongStroke(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_AlongStroke.html)
    *   [LineStyleAlphaModifier_CreaseAngle(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_CreaseAngle.html)
    *   [LineStyleAlphaModifier_Curvature_3D(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_Curvature_3D.html)
    *   [LineStyleAlphaModifier_DistanceFromCamera(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_DistanceFromCamera.html)
    *   [LineStyleAlphaModifier_DistanceFromObject(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_DistanceFromObject.html)
    *   [LineStyleAlphaModifier_Material(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_Material.html)
    *   [LineStyleAlphaModifier_Noise(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_Noise.html)
    *   [LineStyleAlphaModifier_Tangent(LineStyleAlphaModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_Tangent.html)
    *   [LineStyleAlphaModifiers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifiers.html)
    *   [LineStyleColorModifier(LineStyleModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier.html)
    *   [LineStyleColorModifier_AlongStroke(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_AlongStroke.html)
    *   [LineStyleColorModifier_CreaseAngle(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_CreaseAngle.html)
    *   [LineStyleColorModifier_Curvature_3D(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_Curvature_3D.html)
    *   [LineStyleColorModifier_DistanceFromCamera(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_DistanceFromCamera.html)
    *   [LineStyleColorModifier_DistanceFromObject(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_DistanceFromObject.html)
    *   [LineStyleColorModifier_Material(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_Material.html)
    *   [LineStyleColorModifier_Noise(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_Noise.html)
    *   [LineStyleColorModifier_Tangent(LineStyleColorModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_Tangent.html)
    *   [LineStyleColorModifiers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LineStyleColorModifiers.html)
    *   [LineStyleGeometryModifier(LineStyleModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier.html)
    *   [LineStyleGeometryModifier_2DOffset(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_2DOffset.html)
    *   [LineStyleGeometryModifier_2DTransform(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_2DTransform.html)
    *   [LineStyleGeometryModifier_BackboneStretcher(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_BackboneStretcher.html)
    *   [LineStyleGeometryModifier_BezierCurve(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_BezierCurve.html)
    *   [LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_Blueprint.html)
    *   [LineStyleGeometryModifier_GuidingLines(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_GuidingLines.html)
    *   [LineStyleGeometryModifier_PerlinNoise1D(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_PerlinNoise1D.html)
    *   [LineStyleGeometryModifier_PerlinNoise2D(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_PerlinNoise2D.html)
    *   [LineStyleGeometryModifier_Polygonalization(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_Polygonalization.html)
    *   [LineStyleGeometryModifier_Sampling(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_Sampling.html)
    *   [LineStyleGeometryModifier_Simplification(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_Simplification.html)
    *   [LineStyleGeometryModifier_SinusDisplacement(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_SinusDisplacement.html)
    *   [LineStyleGeometryModifier_SpatialNoise(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_SpatialNoise.html)
    *   [LineStyleGeometryModifier_TipRemover(LineStyleGeometryModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_TipRemover.html)
    *   [LineStyleGeometryModifiers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifiers.html)
    *   [LineStyleModifier(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LineStyleModifier.html)
    *   [LineStyleTextureSlot(TextureSlot)](https://docs.blender.org/api/current/bpy.types.LineStyleTextureSlot.html)
    *   [LineStyleTextureSlots(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LineStyleTextureSlots.html)
    *   [LineStyleThicknessModifier(LineStyleModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier.html)
    *   [LineStyleThicknessModifier_AlongStroke(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_AlongStroke.html)
    *   [LineStyleThicknessModifier_Calligraphy(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_Calligraphy.html)
    *   [LineStyleThicknessModifier_CreaseAngle(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_CreaseAngle.html)
    *   [LineStyleThicknessModifier_Curvature_3D(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_Curvature_3D.html)
    *   [LineStyleThicknessModifier_DistanceFromCamera(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_DistanceFromCamera.html)
    *   [LineStyleThicknessModifier_DistanceFromObject(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_DistanceFromObject.html)
    *   [LineStyleThicknessModifier_Material(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_Material.html)
    *   [LineStyleThicknessModifier_Noise(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_Noise.html)
    *   [LineStyleThicknessModifier_Tangent(LineStyleThicknessModifier)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_Tangent.html)
    *   [LineStyleThicknessModifiers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifiers.html)
    *   [Linesets(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Linesets.html)
    *   [LockedTrackConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.LockedTrackConstraint.html)
    *   [LoopColors(bpy_struct)](https://docs.blender.org/api/current/bpy.types.LoopColors.html)
    *   [MASK_UL_layers(UIList)](https://docs.blender.org/api/current/bpy.types.MASK_UL_layers.html)
    *   [MATERIAL_UL_matslots(UIList)](https://docs.blender.org/api/current/bpy.types.MATERIAL_UL_matslots.html)
    *   [MESH_UL_attributes(UIList)](https://docs.blender.org/api/current/bpy.types.MESH_UL_attributes.html)
    *   [MESH_UL_color_attributes(UIList)](https://docs.blender.org/api/current/bpy.types.MESH_UL_color_attributes.html)
    *   [MESH_UL_color_attributes_selector(UIList)](https://docs.blender.org/api/current/bpy.types.MESH_UL_color_attributes_selector.html)
    *   [MESH_UL_uvmaps(UIList)](https://docs.blender.org/api/current/bpy.types.MESH_UL_uvmaps.html)
    *   [MESH_UL_vgroups(UIList)](https://docs.blender.org/api/current/bpy.types.MESH_UL_vgroups.html)
    *   [Macro(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Macro.html)
    *   [MagicTexture(Texture)](https://docs.blender.org/api/current/bpy.types.MagicTexture.html)
    *   [MaintainVolumeConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.MaintainVolumeConstraint.html)
    *   [MarbleTexture(Texture)](https://docs.blender.org/api/current/bpy.types.MarbleTexture.html)
    *   [Mask(ID)](https://docs.blender.org/api/current/bpy.types.Mask.html)
    *   [MaskLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskLayer.html)
    *   [MaskLayers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskLayers.html)
    *   [MaskModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.MaskModifier.html)
    *   [MaskParent(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskParent.html)
    *   [MaskSpline(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskSpline.html)
    *   [MaskSplinePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskSplinePoint.html)
    *   [MaskSplinePointUW(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskSplinePointUW.html)
    *   [MaskSplinePoints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskSplinePoints.html)
    *   [MaskSplines(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaskSplines.html)
    *   [MaskStrip(Strip)](https://docs.blender.org/api/current/bpy.types.MaskStrip.html)
    *   [MaskStripModifier(StripModifier)](https://docs.blender.org/api/current/bpy.types.MaskStripModifier.html)
    *   [Material(ID)](https://docs.blender.org/api/current/bpy.types.Material.html)
    *   [MaterialGPencilStyle(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaterialGPencilStyle.html)
    *   [MaterialLineArt(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaterialLineArt.html)
    *   [MaterialSlot(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MaterialSlot.html)
    *   [Menu(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Menu.html)
    *   [Mesh(ID)](https://docs.blender.org/api/current/bpy.types.Mesh.html)
    *   [MeshCacheModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.MeshCacheModifier.html)
    *   [MeshDeformModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.MeshDeformModifier.html)
    *   [MeshEdge(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshEdge.html)
    *   [MeshEdges(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshEdges.html)
    *   [MeshLoop(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshLoop.html)
    *   [MeshLoopColor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshLoopColor.html)
    *   [MeshLoopColorLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshLoopColorLayer.html)
    *   [MeshLoopTriangle(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshLoopTriangle.html)
    *   [MeshLoopTriangles(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshLoopTriangles.html)
    *   [MeshLoops(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshLoops.html)
    *   [MeshNormalValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshNormalValue.html)
    *   [MeshPolygon(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshPolygon.html)
    *   [MeshPolygons(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshPolygons.html)
    *   [MeshSequenceCacheModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.MeshSequenceCacheModifier.html)
    *   [MeshSkinVertex(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshSkinVertex.html)
    *   [MeshSkinVertexLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshSkinVertexLayer.html)
    *   [MeshStatVis(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshStatVis.html)
    *   [MeshToVolumeModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.MeshToVolumeModifier.html)
    *   [MeshUVLoop(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshUVLoop.html)
    *   [MeshUVLoopLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshUVLoopLayer.html)
    *   [MeshVertex(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshVertex.html)
    *   [MeshVertices(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MeshVertices.html)
    *   [MetaBall(ID)](https://docs.blender.org/api/current/bpy.types.MetaBall.html)
    *   [MetaBallElements(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MetaBallElements.html)
    *   [MetaElement(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MetaElement.html)
    *   [MetaStrip(Strip)](https://docs.blender.org/api/current/bpy.types.MetaStrip.html)
    *   [MirrorModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.MirrorModifier.html)
    *   [Modifier(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Modifier.html)
    *   [ModifierViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.ModifierViewerPathElem.html)
    *   [MotionPath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MotionPath.html)
    *   [MotionPathVert(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MotionPathVert.html)
    *   [MovieClip(ID)](https://docs.blender.org/api/current/bpy.types.MovieClip.html)
    *   [MovieClipProxy(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieClipProxy.html)
    *   [MovieClipScopes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieClipScopes.html)
    *   [MovieClipStrip(Strip)](https://docs.blender.org/api/current/bpy.types.MovieClipStrip.html)
    *   [MovieClipUser(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieClipUser.html)
    *   [MovieReconstructedCamera(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieReconstructedCamera.html)
    *   [MovieStrip(Strip)](https://docs.blender.org/api/current/bpy.types.MovieStrip.html)
    *   [MovieTracking(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTracking.html)
    *   [MovieTrackingCamera(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingCamera.html)
    *   [MovieTrackingDopesheet(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingDopesheet.html)
    *   [MovieTrackingMarker(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingMarker.html)
    *   [MovieTrackingMarkers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingMarkers.html)
    *   [MovieTrackingObject(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingObject.html)
    *   [MovieTrackingObjectPlaneTracks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingObjectPlaneTracks.html)
    *   [MovieTrackingObjectTracks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingObjectTracks.html)
    *   [MovieTrackingObjects(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingObjects.html)
    *   [MovieTrackingPlaneMarker(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingPlaneMarker.html)
    *   [MovieTrackingPlaneMarkers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingPlaneMarkers.html)
    *   [MovieTrackingPlaneTrack(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingPlaneTrack.html)
    *   [MovieTrackingPlaneTracks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingPlaneTracks.html)
    *   [MovieTrackingReconstructedCameras(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingReconstructedCameras.html)
    *   [MovieTrackingReconstruction(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingReconstruction.html)
    *   [MovieTrackingSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingSettings.html)
    *   [MovieTrackingStabilization(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingStabilization.html)
    *   [MovieTrackingTrack(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingTrack.html)
    *   [MovieTrackingTracks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.MovieTrackingTracks.html)
    *   [MulticamStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.MulticamStrip.html)
    *   [MultiplyStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.MultiplyStrip.html)
    *   [MultiresModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.MultiresModifier.html)
    *   [MusgraveTexture(Texture)](https://docs.blender.org/api/current/bpy.types.MusgraveTexture.html)
    *   [NDOFMotionEventData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NDOFMotionEventData.html)
    *   [NODE_AST_compositor(AssetShelf)](https://docs.blender.org/api/current/bpy.types.NODE_AST_compositor.html)
    *   [NODE_FH_image_node(FileHandler)](https://docs.blender.org/api/current/bpy.types.NODE_FH_image_node.html)
    *   [NlaStrip(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NlaStrip.html)
    *   [NlaStripFCurves(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NlaStripFCurves.html)
    *   [NlaStrips(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NlaStrips.html)
    *   [NlaTrack(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NlaTrack.html)
    *   [NlaTracks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NlaTracks.html)
    *   [Node(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Node.html)
    *   [NodeClosureInput(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeClosureInput.html)
    *   [NodeClosureInputItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeClosureInputItem.html)
    *   [NodeClosureInputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeClosureInputItems.html)
    *   [NodeClosureOutput(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeClosureOutput.html)
    *   [NodeClosureOutputItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeClosureOutputItem.html)
    *   [NodeClosureOutputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeClosureOutputItems.html)
    *   [NodeCombineBundle(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeCombineBundle.html)
    *   [NodeCombineBundleItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeCombineBundleItem.html)
    *   [NodeCombineBundleItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeCombineBundleItems.html)
    *   [NodeCompositorFileOutputItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeCompositorFileOutputItem.html)
    *   [NodeCompositorFileOutputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeCompositorFileOutputItems.html)
    *   [NodeCustomGroup(Node)](https://docs.blender.org/api/current/bpy.types.NodeCustomGroup.html)
    *   [NodeEnableOutput(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeEnableOutput.html)
    *   [NodeEnumItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeEnumItem.html)
    *   [NodeEvaluateClosure(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeEvaluateClosure.html)
    *   [NodeEvaluateClosureInputItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeEvaluateClosureInputItem.html)
    *   [NodeEvaluateClosureInputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeEvaluateClosureInputItems.html)
    *   [NodeEvaluateClosureOutputItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeEvaluateClosureOutputItem.html)
    *   [NodeEvaluateClosureOutputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeEvaluateClosureOutputItems.html)
    *   [NodeFrame(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeFrame.html)
    *   [NodeFunctionFormatStringItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeFunctionFormatStringItem.html)
    *   [NodeFunctionFormatStringItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeFunctionFormatStringItems.html)
    *   [NodeGeometryBakeItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryBakeItem.html)
    *   [NodeGeometryBakeItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryBakeItems.html)
    *   [NodeGeometryCaptureAttributeItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryCaptureAttributeItem.html)
    *   [NodeGeometryCaptureAttributeItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryCaptureAttributeItems.html)
    *   [NodeGeometryForeachGeometryElementGenerationItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryForeachGeometryElementGenerationItems.html)
    *   [NodeGeometryForeachGeometryElementInputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryForeachGeometryElementInputItems.html)
    *   [NodeGeometryForeachGeometryElementMainItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryForeachGeometryElementMainItems.html)
    *   [NodeGeometryRepeatOutputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryRepeatOutputItems.html)
    *   [NodeGeometrySimulationOutputItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometrySimulationOutputItems.html)
    *   [NodeGeometryViewerItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryViewerItem.html)
    *   [NodeGeometryViewerItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeGeometryViewerItems.html)
    *   [NodeGroup(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeGroup.html)
    *   [NodeGroupInput(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeGroupInput.html)
    *   [NodeGroupOutput(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeGroupOutput.html)
    *   [NodeIndexSwitchItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeIndexSwitchItems.html)
    *   [NodeInputs(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeInputs.html)
    *   [NodeInstanceHash(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeInstanceHash.html)
    *   [NodeInternal(Node)](https://docs.blender.org/api/current/bpy.types.NodeInternal.html)
    *   [NodeInternalSocketTemplate(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeInternalSocketTemplate.html)
    *   [NodeJoinBundle(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeJoinBundle.html)
    *   [NodeLink(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeLink.html)
    *   [NodeLinks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeLinks.html)
    *   [NodeMenuSwitchItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeMenuSwitchItems.html)
    *   [NodeOutputs(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeOutputs.html)
    *   [NodeReroute(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeReroute.html)
    *   [NodeSeparateBundle(NodeInternal)](https://docs.blender.org/api/current/bpy.types.NodeSeparateBundle.html)
    *   [NodeSeparateBundleItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeSeparateBundleItem.html)
    *   [NodeSeparateBundleItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeSeparateBundleItems.html)
    *   [NodeSocket(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeSocket.html)
    *   [NodeSocketBool(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketBool.html)
    *   [NodeSocketBundle(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketBundle.html)
    *   [NodeSocketClosure(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketClosure.html)
    *   [NodeSocketCollection(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketCollection.html)
    *   [NodeSocketColor(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketColor.html)
    *   [NodeSocketFloat(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloat.html)
    *   [NodeSocketFloatAngle(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatAngle.html)
    *   [NodeSocketFloatColorTemperature(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatColorTemperature.html)
    *   [NodeSocketFloatDistance(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatDistance.html)
    *   [NodeSocketFloatFactor(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatFactor.html)
    *   [NodeSocketFloatFrequency(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatFrequency.html)
    *   [NodeSocketFloatPercentage(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatPercentage.html)
    *   [NodeSocketFloatTime(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatTime.html)
    *   [NodeSocketFloatTimeAbsolute(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatTimeAbsolute.html)
    *   [NodeSocketFloatUnsigned(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatUnsigned.html)
    *   [NodeSocketFloatWavelength(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketFloatWavelength.html)
    *   [NodeSocketGeometry(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketGeometry.html)
    *   [NodeSocketImage(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketImage.html)
    *   [NodeSocketInt(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketInt.html)
    *   [NodeSocketIntFactor(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketIntFactor.html)
    *   [NodeSocketIntPercentage(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketIntPercentage.html)
    *   [NodeSocketIntUnsigned(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketIntUnsigned.html)
    *   [NodeSocketMaterial(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketMaterial.html)
    *   [NodeSocketMatrix(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketMatrix.html)
    *   [NodeSocketMenu(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketMenu.html)
    *   [NodeSocketObject(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketObject.html)
    *   [NodeSocketRotation(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketRotation.html)
    *   [NodeSocketShader(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketShader.html)
    *   [NodeSocketStandard(NodeSocket)](https://docs.blender.org/api/current/bpy.types.NodeSocketStandard.html)
    *   [NodeSocketString(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketString.html)
    *   [NodeSocketStringFilePath(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketStringFilePath.html)
    *   [NodeSocketTexture(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketTexture.html)
    *   [NodeSocketVector(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVector.html)
    *   [NodeSocketVector2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVector2D.html)
    *   [NodeSocketVector4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVector4D.html)
    *   [NodeSocketVectorAcceleration(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorAcceleration.html)
    *   [NodeSocketVectorAcceleration2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorAcceleration2D.html)
    *   [NodeSocketVectorAcceleration4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorAcceleration4D.html)
    *   [NodeSocketVectorDirection(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorDirection.html)
    *   [NodeSocketVectorDirection2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorDirection2D.html)
    *   [NodeSocketVectorDirection4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorDirection4D.html)
    *   [NodeSocketVectorEuler(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorEuler.html)
    *   [NodeSocketVectorEuler2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorEuler2D.html)
    *   [NodeSocketVectorEuler4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorEuler4D.html)
    *   [NodeSocketVectorFactor(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorFactor.html)
    *   [NodeSocketVectorFactor2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorFactor2D.html)
    *   [NodeSocketVectorFactor4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorFactor4D.html)
    *   [NodeSocketVectorPercentage(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorPercentage.html)
    *   [NodeSocketVectorPercentage2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorPercentage2D.html)
    *   [NodeSocketVectorPercentage4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorPercentage4D.html)
    *   [NodeSocketVectorTranslation(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorTranslation.html)
    *   [NodeSocketVectorTranslation2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorTranslation2D.html)
    *   [NodeSocketVectorTranslation4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorTranslation4D.html)
    *   [NodeSocketVectorVelocity(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorVelocity.html)
    *   [NodeSocketVectorVelocity2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorVelocity2D.html)
    *   [NodeSocketVectorVelocity4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorVelocity4D.html)
    *   [NodeSocketVectorXYZ(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorXYZ.html)
    *   [NodeSocketVectorXYZ2D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorXYZ2D.html)
    *   [NodeSocketVectorXYZ4D(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVectorXYZ4D.html)
    *   [NodeSocketVirtual(NodeSocketStandard)](https://docs.blender.org/api/current/bpy.types.NodeSocketVirtual.html)
    *   [NodeTree(ID)](https://docs.blender.org/api/current/bpy.types.NodeTree.html)
    *   [NodeTreeInterface(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterface.html)
    *   [NodeTreeInterfaceItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceItem.html)
    *   [NodeTreeInterfacePanel(NodeTreeInterfaceItem)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfacePanel.html)
    *   [NodeTreeInterfaceSocket(NodeTreeInterfaceItem)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocket.html)
    *   [NodeTreeInterfaceSocketBool(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketBool.html)
    *   [NodeTreeInterfaceSocketBundle(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketBundle.html)
    *   [NodeTreeInterfaceSocketClosure(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketClosure.html)
    *   [NodeTreeInterfaceSocketCollection(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketCollection.html)
    *   [NodeTreeInterfaceSocketColor(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketColor.html)
    *   [NodeTreeInterfaceSocketFloat(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloat.html)
    *   [NodeTreeInterfaceSocketFloatAngle(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatAngle.html)
    *   [NodeTreeInterfaceSocketFloatColorTemperature(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatColorTemperature.html)
    *   [NodeTreeInterfaceSocketFloatDistance(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatDistance.html)
    *   [NodeTreeInterfaceSocketFloatFactor(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatFactor.html)
    *   [NodeTreeInterfaceSocketFloatFrequency(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatFrequency.html)
    *   [NodeTreeInterfaceSocketFloatPercentage(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatPercentage.html)
    *   [NodeTreeInterfaceSocketFloatTime(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatTime.html)
    *   [NodeTreeInterfaceSocketFloatTimeAbsolute(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatTimeAbsolute.html)
    *   [NodeTreeInterfaceSocketFloatUnsigned(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatUnsigned.html)
    *   [NodeTreeInterfaceSocketFloatWavelength(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketFloatWavelength.html)
    *   [NodeTreeInterfaceSocketGeometry(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketGeometry.html)
    *   [NodeTreeInterfaceSocketImage(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketImage.html)
    *   [NodeTreeInterfaceSocketInt(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketInt.html)
    *   [NodeTreeInterfaceSocketIntFactor(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketIntFactor.html)
    *   [NodeTreeInterfaceSocketIntPercentage(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketIntPercentage.html)
    *   [NodeTreeInterfaceSocketIntUnsigned(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketIntUnsigned.html)
    *   [NodeTreeInterfaceSocketMaterial(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketMaterial.html)
    *   [NodeTreeInterfaceSocketMatrix(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketMatrix.html)
    *   [NodeTreeInterfaceSocketMenu(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketMenu.html)
    *   [NodeTreeInterfaceSocketObject(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketObject.html)
    *   [NodeTreeInterfaceSocketRotation(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketRotation.html)
    *   [NodeTreeInterfaceSocketShader(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketShader.html)
    *   [NodeTreeInterfaceSocketString(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketString.html)
    *   [NodeTreeInterfaceSocketStringFilePath(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketStringFilePath.html)
    *   [NodeTreeInterfaceSocketTexture(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketTexture.html)
    *   [NodeTreeInterfaceSocketVector(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVector.html)
    *   [NodeTreeInterfaceSocketVector2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVector2D.html)
    *   [NodeTreeInterfaceSocketVector4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVector4D.html)
    *   [NodeTreeInterfaceSocketVectorAcceleration(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorAcceleration.html)
    *   [NodeTreeInterfaceSocketVectorAcceleration2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorAcceleration2D.html)
    *   [NodeTreeInterfaceSocketVectorAcceleration4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorAcceleration4D.html)
    *   [NodeTreeInterfaceSocketVectorDirection(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorDirection.html)
    *   [NodeTreeInterfaceSocketVectorDirection2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorDirection2D.html)
    *   [NodeTreeInterfaceSocketVectorDirection4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorDirection4D.html)
    *   [NodeTreeInterfaceSocketVectorEuler(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorEuler.html)
    *   [NodeTreeInterfaceSocketVectorEuler2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorEuler2D.html)
    *   [NodeTreeInterfaceSocketVectorEuler4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorEuler4D.html)
    *   [NodeTreeInterfaceSocketVectorFactor(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorFactor.html)
    *   [NodeTreeInterfaceSocketVectorFactor2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorFactor2D.html)
    *   [NodeTreeInterfaceSocketVectorFactor4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorFactor4D.html)
    *   [NodeTreeInterfaceSocketVectorPercentage(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorPercentage.html)
    *   [NodeTreeInterfaceSocketVectorPercentage2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorPercentage2D.html)
    *   [NodeTreeInterfaceSocketVectorPercentage4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorPercentage4D.html)
    *   [NodeTreeInterfaceSocketVectorTranslation(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorTranslation.html)
    *   [NodeTreeInterfaceSocketVectorTranslation2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorTranslation2D.html)
    *   [NodeTreeInterfaceSocketVectorTranslation4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorTranslation4D.html)
    *   [NodeTreeInterfaceSocketVectorVelocity(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorVelocity.html)
    *   [NodeTreeInterfaceSocketVectorVelocity2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorVelocity2D.html)
    *   [NodeTreeInterfaceSocketVectorVelocity4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorVelocity4D.html)
    *   [NodeTreeInterfaceSocketVectorXYZ(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorXYZ.html)
    *   [NodeTreeInterfaceSocketVectorXYZ2D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorXYZ2D.html)
    *   [NodeTreeInterfaceSocketVectorXYZ4D(NodeTreeInterfaceSocket)](https://docs.blender.org/api/current/bpy.types.NodeTreeInterfaceSocketVectorXYZ4D.html)
    *   [NodeTreePath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodeTreePath.html)
    *   [Nodes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Nodes.html)
    *   [NodesModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.NodesModifier.html)
    *   [NodesModifierBake(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodesModifierBake.html)
    *   [NodesModifierBakeDataBlocks(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodesModifierBakeDataBlocks.html)
    *   [NodesModifierBakes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodesModifierBakes.html)
    *   [NodesModifierDataBlock(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodesModifierDataBlock.html)
    *   [NodesModifierPanel(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodesModifierPanel.html)
    *   [NodesModifierPanels(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodesModifierPanels.html)
    *   [NodesModifierWarning(bpy_struct)](https://docs.blender.org/api/current/bpy.types.NodesModifierWarning.html)
    *   [NoiseTexture(Texture)](https://docs.blender.org/api/current/bpy.types.NoiseTexture.html)
    *   [NormalEditModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.NormalEditModifier.html)
    *   [Object(ID)](https://docs.blender.org/api/current/bpy.types.Object.html)
    *   [ObjectBase(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ObjectBase.html)
    *   [ObjectConstraints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ObjectConstraints.html)
    *   [ObjectDisplay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ObjectDisplay.html)
    *   [ObjectLightLinking(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ObjectLightLinking.html)
    *   [ObjectLineArt(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ObjectLineArt.html)
    *   [ObjectModifiers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ObjectModifiers.html)
    *   [ObjectShaderFx(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ObjectShaderFx.html)
    *   [ObjectSolverConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.ObjectSolverConstraint.html)
    *   [OceanModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.OceanModifier.html)
    *   [Operator(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Operator.html)
    *   [OperatorFileListElement(PropertyGroup)](https://docs.blender.org/api/current/bpy.types.OperatorFileListElement.html)
    *   [OperatorMacro(bpy_struct)](https://docs.blender.org/api/current/bpy.types.OperatorMacro.html)
    *   [OperatorMousePath(PropertyGroup)](https://docs.blender.org/api/current/bpy.types.OperatorMousePath.html)
    *   [OperatorOptions(bpy_struct)](https://docs.blender.org/api/current/bpy.types.OperatorOptions.html)
    *   [OperatorProperties(bpy_struct)](https://docs.blender.org/api/current/bpy.types.OperatorProperties.html)
    *   [OperatorStrokeElement(PropertyGroup)](https://docs.blender.org/api/current/bpy.types.OperatorStrokeElement.html)
    *   [PARTICLE_UL_particle_systems(UIList)](https://docs.blender.org/api/current/bpy.types.PARTICLE_UL_particle_systems.html)
    *   [PHYSICS_UL_dynapaint_surfaces(UIList)](https://docs.blender.org/api/current/bpy.types.PHYSICS_UL_dynapaint_surfaces.html)
    *   [POINTCLOUD_UL_attributes(UIList)](https://docs.blender.org/api/current/bpy.types.POINTCLOUD_UL_attributes.html)
    *   [POSE_UL_selection_set(UIList)](https://docs.blender.org/api/current/bpy.types.POSE_UL_selection_set.html)
    *   [PackedFile(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PackedFile.html)
    *   [Paint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Paint.html)
    *   [PaintCurve(ID)](https://docs.blender.org/api/current/bpy.types.PaintCurve.html)
    *   [PaintModeSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PaintModeSettings.html)
    *   [Palette(ID)](https://docs.blender.org/api/current/bpy.types.Palette.html)
    *   [PaletteColor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PaletteColor.html)
    *   [PaletteColors(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PaletteColors.html)
    *   [Panel(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Panel.html)
    *   [Particle(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Particle.html)
    *   [ParticleBrush(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleBrush.html)
    *   [ParticleDupliWeight(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleDupliWeight.html)
    *   [ParticleEdit(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleEdit.html)
    *   [ParticleHairKey(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleHairKey.html)
    *   [ParticleInstanceModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ParticleInstanceModifier.html)
    *   [ParticleKey(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleKey.html)
    *   [ParticleSettings(ID)](https://docs.blender.org/api/current/bpy.types.ParticleSettings.html)
    *   [ParticleSettingsTextureSlot(TextureSlot)](https://docs.blender.org/api/current/bpy.types.ParticleSettingsTextureSlot.html)
    *   [ParticleSettingsTextureSlots(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleSettingsTextureSlots.html)
    *   [ParticleSystem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleSystem.html)
    *   [ParticleSystemModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ParticleSystemModifier.html)
    *   [ParticleSystems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleSystems.html)
    *   [ParticleTarget(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ParticleTarget.html)
    *   [PathCompare(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PathCompare.html)
    *   [PathCompareCollection(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PathCompareCollection.html)
    *   [PivotConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.PivotConstraint.html)
    *   [Point(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Point.html)
    *   [PointCache(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PointCache.html)
    *   [PointCacheItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PointCacheItem.html)
    *   [PointCaches(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PointCaches.html)
    *   [PointCloud(ID)](https://docs.blender.org/api/current/bpy.types.PointCloud.html)
    *   [PointLight(Light)](https://docs.blender.org/api/current/bpy.types.PointLight.html)
    *   [PointerProperty(Property)](https://docs.blender.org/api/current/bpy.types.PointerProperty.html)
    *   [Pose(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Pose.html)
    *   [PoseBone(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PoseBone.html)
    *   [PoseBoneConstraints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PoseBoneConstraints.html)
    *   [Preferences(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Preferences.html)
    *   [PreferencesApps(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesApps.html)
    *   [PreferencesEdit(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesEdit.html)
    *   [PreferencesExperimental(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesExperimental.html)
    *   [PreferencesExtensions(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesExtensions.html)
    *   [PreferencesFilePaths(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesFilePaths.html)
    *   [PreferencesInput(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesInput.html)
    *   [PreferencesKeymap(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesKeymap.html)
    *   [PreferencesSystem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesSystem.html)
    *   [PreferencesView(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PreferencesView.html)
    *   [PrimitiveBoolean(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PrimitiveBoolean.html)
    *   [PrimitiveFloat(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PrimitiveFloat.html)
    *   [PrimitiveInt(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PrimitiveInt.html)
    *   [PrimitiveString(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PrimitiveString.html)
    *   [Property(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Property.html)
    *   [PropertyGroup(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PropertyGroup.html)
    *   [PropertyGroupItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.PropertyGroupItem.html)
    *   [QuaternionAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.QuaternionAttribute.html)
    *   [QuaternionAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.QuaternionAttributeValue.html)
    *   [RENDER_UL_renderviews(UIList)](https://docs.blender.org/api/current/bpy.types.RENDER_UL_renderviews.html)
    *   [RaytraceEEVEE(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RaytraceEEVEE.html)
    *   [ReadOnlyInteger(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ReadOnlyInteger.html)
    *   [Region(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Region.html)
    *   [RegionView3D(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RegionView3D.html)
    *   [RemeshModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.RemeshModifier.html)
    *   [RenderEngine(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderEngine.html)
    *   [RenderLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderLayer.html)
    *   [RenderPass(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderPass.html)
    *   [RenderPasses(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderPasses.html)
    *   [RenderResult(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderResult.html)
    *   [RenderSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderSettings.html)
    *   [RenderSlot(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderSlot.html)
    *   [RenderSlots(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderSlots.html)
    *   [RenderView(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderView.html)
    *   [RenderViews(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RenderViews.html)
    *   [RepeatItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RepeatItem.html)
    *   [RepeatZoneViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.RepeatZoneViewerPathElem.html)
    *   [RetimingKey(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RetimingKey.html)
    *   [RetimingKeys(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RetimingKeys.html)
    *   [RigidBodyConstraint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RigidBodyConstraint.html)
    *   [RigidBodyObject(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RigidBodyObject.html)
    *   [RigidBodyWorld(bpy_struct)](https://docs.blender.org/api/current/bpy.types.RigidBodyWorld.html)
    *   [SCENE_UL_gltf2_filter_action(UIList)](https://docs.blender.org/api/current/bpy.types.SCENE_UL_gltf2_filter_action.html)
    *   [SCENE_UL_keying_set_paths(UIList)](https://docs.blender.org/api/current/bpy.types.SCENE_UL_keying_set_paths.html)
    *   [SEQUENCER_FH_image_strip(FileHandler)](https://docs.blender.org/api/current/bpy.types.SEQUENCER_FH_image_strip.html)
    *   [SEQUENCER_FH_movie_strip(FileHandler)](https://docs.blender.org/api/current/bpy.types.SEQUENCER_FH_movie_strip.html)
    *   [SEQUENCER_FH_sound_strip(FileHandler)](https://docs.blender.org/api/current/bpy.types.SEQUENCER_FH_sound_strip.html)
    *   [SPHFluidSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SPHFluidSettings.html)
    *   [Scene(ID)](https://docs.blender.org/api/current/bpy.types.Scene.html)
    *   [SceneDisplay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SceneDisplay.html)
    *   [SceneEEVEE(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SceneEEVEE.html)
    *   [SceneGpencil(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SceneGpencil.html)
    *   [SceneHydra(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SceneHydra.html)
    *   [SceneObjects(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SceneObjects.html)
    *   [SceneRenderView(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SceneRenderView.html)
    *   [SceneStrip(Strip)](https://docs.blender.org/api/current/bpy.types.SceneStrip.html)
    *   [Scopes(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Scopes.html)
    *   [Screen(ID)](https://docs.blender.org/api/current/bpy.types.Screen.html)
    *   [ScrewModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ScrewModifier.html)
    *   [ScriptDirectory(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ScriptDirectory.html)
    *   [ScriptDirectoryCollection(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ScriptDirectoryCollection.html)
    *   [Sculpt(Paint)](https://docs.blender.org/api/current/bpy.types.Sculpt.html)
    *   [SelectedUvElement(PropertyGroup)](https://docs.blender.org/api/current/bpy.types.SelectedUvElement.html)
    *   [SequenceEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SequenceEditor.html)
    *   [SequenceTimelineChannel(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SequenceTimelineChannel.html)
    *   [SequencerCacheOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SequencerCacheOverlay.html)
    *   [SequencerCompositorModifierData(StripModifier)](https://docs.blender.org/api/current/bpy.types.SequencerCompositorModifierData.html)
    *   [SequencerPreviewOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SequencerPreviewOverlay.html)
    *   [SequencerTimelineOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SequencerTimelineOverlay.html)
    *   [SequencerTonemapModifierData(StripModifier)](https://docs.blender.org/api/current/bpy.types.SequencerTonemapModifierData.html)
    *   [SequencerToolSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SequencerToolSettings.html)
    *   [ShaderFx(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ShaderFx.html)
    *   [ShaderFxBlur(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxBlur.html)
    *   [ShaderFxColorize(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxColorize.html)
    *   [ShaderFxFlip(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxFlip.html)
    *   [ShaderFxGlow(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxGlow.html)
    *   [ShaderFxPixel(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxPixel.html)
    *   [ShaderFxRim(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxRim.html)
    *   [ShaderFxShadow(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxShadow.html)
    *   [ShaderFxSwirl(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxSwirl.html)
    *   [ShaderFxWave(ShaderFx)](https://docs.blender.org/api/current/bpy.types.ShaderFxWave.html)
    *   [ShaderNode(NodeInternal)](https://docs.blender.org/api/current/bpy.types.ShaderNode.html)
    *   [ShaderNodeAddShader(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeAddShader.html)
    *   [ShaderNodeAmbientOcclusion(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeAmbientOcclusion.html)
    *   [ShaderNodeAttribute(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeAttribute.html)
    *   [ShaderNodeBackground(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBackground.html)
    *   [ShaderNodeBevel(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBevel.html)
    *   [ShaderNodeBlackbody(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBlackbody.html)
    *   [ShaderNodeBrightContrast(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBrightContrast.html)
    *   [ShaderNodeBsdfAnisotropic(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfAnisotropic.html)
    *   [ShaderNodeBsdfDiffuse(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfDiffuse.html)
    *   [ShaderNodeBsdfGlass(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfGlass.html)
    *   [ShaderNodeBsdfHair(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfHair.html)
    *   [ShaderNodeBsdfHairPrincipled(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfHairPrincipled.html)
    *   [ShaderNodeBsdfMetallic(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfMetallic.html)
    *   [ShaderNodeBsdfPrincipled(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfPrincipled.html)
    *   [ShaderNodeBsdfRayPortal(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfRayPortal.html)
    *   [ShaderNodeBsdfRefraction(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfRefraction.html)
    *   [ShaderNodeBsdfSheen(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfSheen.html)
    *   [ShaderNodeBsdfToon(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfToon.html)
    *   [ShaderNodeBsdfTranslucent(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfTranslucent.html)
    *   [ShaderNodeBsdfTransparent(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfTransparent.html)
    *   [ShaderNodeBump(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeBump.html)
    *   [ShaderNodeCameraData(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeCameraData.html)
    *   [ShaderNodeClamp(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
    *   [ShaderNodeCombineColor(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineColor.html)
    *   [ShaderNodeCombineXYZ(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
    *   [ShaderNodeCustomGroup(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeCustomGroup.html)
    *   [ShaderNodeDisplacement(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeDisplacement.html)
    *   [ShaderNodeEeveeSpecular(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeEeveeSpecular.html)
    *   [ShaderNodeEmission(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeEmission.html)
    *   [ShaderNodeFloatCurve(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)
    *   [ShaderNodeFresnel(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeFresnel.html)
    *   [ShaderNodeGamma(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeGamma.html)
    *   [ShaderNodeGroup(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeGroup.html)
    *   [ShaderNodeHairInfo(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeHairInfo.html)
    *   [ShaderNodeHoldout(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeHoldout.html)
    *   [ShaderNodeHueSaturation(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeHueSaturation.html)
    *   [ShaderNodeInvert(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeInvert.html)
    *   [ShaderNodeLayerWeight(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeLayerWeight.html)
    *   [ShaderNodeLightFalloff(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeLightFalloff.html)
    *   [ShaderNodeLightPath(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeLightPath.html)
    *   [ShaderNodeMapRange(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
    *   [ShaderNodeMapping(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapping.html)
    *   [ShaderNodeMath(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
    *   [ShaderNodeMix(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
    *   [ShaderNodeMixRGB(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
    *   [ShaderNodeMixShader(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixShader.html)
    *   [ShaderNodeNewGeometry(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeNewGeometry.html)
    *   [ShaderNodeNormal(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeNormal.html)
    *   [ShaderNodeNormalMap(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeNormalMap.html)
    *   [ShaderNodeObjectInfo(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeObjectInfo.html)
    *   [ShaderNodeOutputAOV(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputAOV.html)
    *   [ShaderNodeOutputLight(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputLight.html)
    *   [ShaderNodeOutputLineStyle(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputLineStyle.html)
    *   [ShaderNodeOutputMaterial(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputMaterial.html)
    *   [ShaderNodeOutputWorld(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputWorld.html)
    *   [ShaderNodeParticleInfo(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeParticleInfo.html)
    *   [ShaderNodePointInfo(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodePointInfo.html)
    *   [ShaderNodeRGB(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGB.html)
    *   [ShaderNodeRGBCurve(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
    *   [ShaderNodeRGBToBW(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBToBW.html)
    *   [ShaderNodeRadialTiling(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeRadialTiling.html)
    *   [ShaderNodeScript(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeScript.html)
    *   [ShaderNodeSeparateColor(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateColor.html)
    *   [ShaderNodeSeparateXYZ(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
    *   [ShaderNodeShaderToRGB(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeShaderToRGB.html)
    *   [ShaderNodeSqueeze(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeSqueeze.html)
    *   [ShaderNodeSubsurfaceScattering(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeSubsurfaceScattering.html)
    *   [ShaderNodeTangent(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTangent.html)
    *   [ShaderNodeTexBrick(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)
    *   [ShaderNodeTexChecker(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
    *   [ShaderNodeTexCoord(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexCoord.html)
    *   [ShaderNodeTexEnvironment(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexEnvironment.html)
    *   [ShaderNodeTexGabor(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGabor.html)
    *   [ShaderNodeTexGradient(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)
    *   [ShaderNodeTexIES(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexIES.html)
    *   [ShaderNodeTexImage(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexImage.html)
    *   [ShaderNodeTexMagic(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
    *   [ShaderNodeTexNoise(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
    *   [ShaderNodeTexSky(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexSky.html)
    *   [ShaderNodeTexVoronoi(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
    *   [ShaderNodeTexWave(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
    *   [ShaderNodeTexWhiteNoise(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
    *   [ShaderNodeTree(NodeTree)](https://docs.blender.org/api/current/bpy.types.ShaderNodeTree.html)
    *   [ShaderNodeUVAlongStroke(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeUVAlongStroke.html)
    *   [ShaderNodeUVMap(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeUVMap.html)
    *   [ShaderNodeValToRGB(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
    *   [ShaderNodeValue(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)
    *   [ShaderNodeVectorCurve(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)
    *   [ShaderNodeVectorDisplacement(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorDisplacement.html)
    *   [ShaderNodeVectorMath(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
    *   [ShaderNodeVectorRotate(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
    *   [ShaderNodeVectorTransform(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorTransform.html)
    *   [ShaderNodeVertexColor(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVertexColor.html)
    *   [ShaderNodeVolumeAbsorption(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeAbsorption.html)
    *   [ShaderNodeVolumeCoefficients(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeCoefficients.html)
    *   [ShaderNodeVolumeInfo(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeInfo.html)
    *   [ShaderNodeVolumePrincipled(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumePrincipled.html)
    *   [ShaderNodeVolumeScatter(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeScatter.html)
    *   [ShaderNodeWavelength(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeWavelength.html)
    *   [ShaderNodeWireframe(ShaderNode)](https://docs.blender.org/api/current/bpy.types.ShaderNodeWireframe.html)
    *   [ShapeKey(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ShapeKey.html)
    *   [ShapeKeyBezierPoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ShapeKeyBezierPoint.html)
    *   [ShapeKeyCurvePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ShapeKeyCurvePoint.html)
    *   [ShapeKeyPoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ShapeKeyPoint.html)
    *   [Short2Attribute(Attribute)](https://docs.blender.org/api/current/bpy.types.Short2Attribute.html)
    *   [Short2AttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Short2AttributeValue.html)
    *   [ShrinkwrapConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.ShrinkwrapConstraint.html)
    *   [ShrinkwrapModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.ShrinkwrapModifier.html)
    *   [SimpleDeformModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SimpleDeformModifier.html)
    *   [SimulationStateItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SimulationStateItem.html)
    *   [SimulationZoneViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.SimulationZoneViewerPathElem.html)
    *   [SkinModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SkinModifier.html)
    *   [SmoothModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SmoothModifier.html)
    *   [SoftBodyModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SoftBodyModifier.html)
    *   [SoftBodySettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SoftBodySettings.html)
    *   [SolidifyModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SolidifyModifier.html)
    *   [Sound(ID)](https://docs.blender.org/api/current/bpy.types.Sound.html)
    *   [SoundEqualizerModifier(StripModifier)](https://docs.blender.org/api/current/bpy.types.SoundEqualizerModifier.html)
    *   [SoundStrip(Strip)](https://docs.blender.org/api/current/bpy.types.SoundStrip.html)
    *   [Space(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Space.html)
    *   [SpaceClipEditor(Space)](https://docs.blender.org/api/current/bpy.types.SpaceClipEditor.html)
    *   [SpaceClipOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpaceClipOverlay.html)
    *   [SpaceConsole(Space)](https://docs.blender.org/api/current/bpy.types.SpaceConsole.html)
    *   [SpaceDopeSheetEditor(Space)](https://docs.blender.org/api/current/bpy.types.SpaceDopeSheetEditor.html)
    *   [SpaceDopeSheetOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpaceDopeSheetOverlay.html)
    *   [SpaceFileBrowser(Space)](https://docs.blender.org/api/current/bpy.types.SpaceFileBrowser.html)
    *   [SpaceGraphEditor(Space)](https://docs.blender.org/api/current/bpy.types.SpaceGraphEditor.html)
    *   [SpaceImageEditor(Space)](https://docs.blender.org/api/current/bpy.types.SpaceImageEditor.html)
    *   [SpaceImageOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpaceImageOverlay.html)
    *   [SpaceInfo(Space)](https://docs.blender.org/api/current/bpy.types.SpaceInfo.html)
    *   [SpaceNLA(Space)](https://docs.blender.org/api/current/bpy.types.SpaceNLA.html)
    *   [SpaceNodeEditor(Space)](https://docs.blender.org/api/current/bpy.types.SpaceNodeEditor.html)
    *   [SpaceNodeEditorPath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpaceNodeEditorPath.html)
    *   [SpaceNodeOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpaceNodeOverlay.html)
    *   [SpaceOutliner(Space)](https://docs.blender.org/api/current/bpy.types.SpaceOutliner.html)
    *   [SpacePreferences(Space)](https://docs.blender.org/api/current/bpy.types.SpacePreferences.html)
    *   [SpaceProperties(Space)](https://docs.blender.org/api/current/bpy.types.SpaceProperties.html)
    *   [SpaceSequenceEditor(Space)](https://docs.blender.org/api/current/bpy.types.SpaceSequenceEditor.html)
    *   [SpaceSpreadsheet(Space)](https://docs.blender.org/api/current/bpy.types.SpaceSpreadsheet.html)
    *   [SpaceTextEditor(Space)](https://docs.blender.org/api/current/bpy.types.SpaceTextEditor.html)
    *   [SpaceUVEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpaceUVEditor.html)
    *   [SpaceView3D(Space)](https://docs.blender.org/api/current/bpy.types.SpaceView3D.html)
    *   [Speaker(ID)](https://docs.blender.org/api/current/bpy.types.Speaker.html)
    *   [SpeedControlStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.SpeedControlStrip.html)
    *   [Spline(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Spline.html)
    *   [SplineBezierPoints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SplineBezierPoints.html)
    *   [SplineIKConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.SplineIKConstraint.html)
    *   [SplinePoint(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SplinePoint.html)
    *   [SplinePoints(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SplinePoints.html)
    *   [SpotLight(Light)](https://docs.blender.org/api/current/bpy.types.SpotLight.html)
    *   [SpreadsheetColumn(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpreadsheetColumn.html)
    *   [SpreadsheetColumnID(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpreadsheetColumnID.html)
    *   [SpreadsheetRowFilter(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpreadsheetRowFilter.html)
    *   [SpreadsheetTable(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpreadsheetTable.html)
    *   [SpreadsheetTableID(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpreadsheetTableID.html)
    *   [SpreadsheetTableIDGeometry(SpreadsheetTableID)](https://docs.blender.org/api/current/bpy.types.SpreadsheetTableIDGeometry.html)
    *   [SpreadsheetTables(bpy_struct)](https://docs.blender.org/api/current/bpy.types.SpreadsheetTables.html)
    *   [Stereo3dDisplay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Stereo3dDisplay.html)
    *   [Stereo3dFormat(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Stereo3dFormat.html)
    *   [StretchToConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.StretchToConstraint.html)
    *   [StringAttribute(Attribute)](https://docs.blender.org/api/current/bpy.types.StringAttribute.html)
    *   [StringAttributeValue(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StringAttributeValue.html)
    *   [StringProperty(Property)](https://docs.blender.org/api/current/bpy.types.StringProperty.html)
    *   [Strip(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Strip.html)
    *   [StripColorBalance(StripColorBalanceData)](https://docs.blender.org/api/current/bpy.types.StripColorBalance.html)
    *   [StripColorBalanceData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripColorBalanceData.html)
    *   [StripCrop(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripCrop.html)
    *   [StripElement(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripElement.html)
    *   [StripElements(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripElements.html)
    *   [StripModifier(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripModifier.html)
    *   [StripModifiers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripModifiers.html)
    *   [StripProxy(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripProxy.html)
    *   [StripTransform(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripTransform.html)
    *   [StripsMeta(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripsMeta.html)
    *   [StripsTopLevel(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StripsTopLevel.html)
    *   [Struct(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Struct.html)
    *   [StucciTexture(Texture)](https://docs.blender.org/api/current/bpy.types.StucciTexture.html)
    *   [StudioLight(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StudioLight.html)
    *   [StudioLights(bpy_struct)](https://docs.blender.org/api/current/bpy.types.StudioLights.html)
    *   [SubsurfModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SubsurfModifier.html)
    *   [SubtractStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.SubtractStrip.html)
    *   [SunLight(Light)](https://docs.blender.org/api/current/bpy.types.SunLight.html)
    *   [SurfaceCurve(Curve)](https://docs.blender.org/api/current/bpy.types.SurfaceCurve.html)
    *   [SurfaceDeformModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SurfaceDeformModifier.html)
    *   [SurfaceModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.SurfaceModifier.html)
    *   [TEXTURE_UL_texpaintslots(UIList)](https://docs.blender.org/api/current/bpy.types.TEXTURE_UL_texpaintslots.html)
    *   [TEXTURE_UL_texslots(UIList)](https://docs.blender.org/api/current/bpy.types.TEXTURE_UL_texslots.html)
    *   [TexMapping(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TexMapping.html)
    *   [TexPaintSlot(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TexPaintSlot.html)
    *   [Text(ID)](https://docs.blender.org/api/current/bpy.types.Text.html)
    *   [TextBox(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TextBox.html)
    *   [TextCharacterFormat(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TextCharacterFormat.html)
    *   [TextCurve(Curve)](https://docs.blender.org/api/current/bpy.types.TextCurve.html)
    *   [TextLine(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TextLine.html)
    *   [TextStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.TextStrip.html)
    *   [Texture(ID)](https://docs.blender.org/api/current/bpy.types.Texture.html)
    *   [TextureNode(NodeInternal)](https://docs.blender.org/api/current/bpy.types.TextureNode.html)
    *   [TextureNodeAt(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeAt.html)
    *   [TextureNodeBricks(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeBricks.html)
    *   [TextureNodeChecker(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeChecker.html)
    *   [TextureNodeCombineColor(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeCombineColor.html)
    *   [TextureNodeCompose(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeCompose.html)
    *   [TextureNodeCoordinates(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeCoordinates.html)
    *   [TextureNodeCurveRGB(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeCurveRGB.html)
    *   [TextureNodeCurveTime(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeCurveTime.html)
    *   [TextureNodeDecompose(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeDecompose.html)
    *   [TextureNodeDistance(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeDistance.html)
    *   [TextureNodeGroup(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeGroup.html)
    *   [TextureNodeHueSaturation(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeHueSaturation.html)
    *   [TextureNodeImage(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeImage.html)
    *   [TextureNodeInvert(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeInvert.html)
    *   [TextureNodeMath(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeMath.html)
    *   [TextureNodeMixRGB(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeMixRGB.html)
    *   [TextureNodeOutput(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeOutput.html)
    *   [TextureNodeRGBToBW(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeRGBToBW.html)
    *   [TextureNodeRotate(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeRotate.html)
    *   [TextureNodeScale(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeScale.html)
    *   [TextureNodeSeparateColor(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeSeparateColor.html)
    *   [TextureNodeTexBlend(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexBlend.html)
    *   [TextureNodeTexClouds(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexClouds.html)
    *   [TextureNodeTexDistNoise(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexDistNoise.html)
    *   [TextureNodeTexMagic(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexMagic.html)
    *   [TextureNodeTexMarble(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexMarble.html)
    *   [TextureNodeTexMusgrave(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexMusgrave.html)
    *   [TextureNodeTexNoise(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexNoise.html)
    *   [TextureNodeTexStucci(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexStucci.html)
    *   [TextureNodeTexVoronoi(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexVoronoi.html)
    *   [TextureNodeTexWood(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexWood.html)
    *   [TextureNodeTexture(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTexture.html)
    *   [TextureNodeTranslate(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeTranslate.html)
    *   [TextureNodeTree(NodeTree)](https://docs.blender.org/api/current/bpy.types.TextureNodeTree.html)
    *   [TextureNodeValToNor(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeValToNor.html)
    *   [TextureNodeValToRGB(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeValToRGB.html)
    *   [TextureNodeViewer(TextureNode)](https://docs.blender.org/api/current/bpy.types.TextureNodeViewer.html)
    *   [TextureSlot(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TextureSlot.html)
    *   [Theme(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Theme.html)
    *   [ThemeBoneColorSet(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeBoneColorSet.html)
    *   [ThemeClipEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeClipEditor.html)
    *   [ThemeCollectionColor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeCollectionColor.html)
    *   [ThemeCommon(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeCommon.html)
    *   [ThemeCommonAnim(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeCommonAnim.html)
    *   [ThemeCommonCurves(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeCommonCurves.html)
    *   [ThemeConsole(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeConsole.html)
    *   [ThemeDopeSheet(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeDopeSheet.html)
    *   [ThemeFileBrowser(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeFileBrowser.html)
    *   [ThemeFontStyle(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeFontStyle.html)
    *   [ThemeGradientColors(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeGradientColors.html)
    *   [ThemeGraphEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeGraphEditor.html)
    *   [ThemeImageEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeImageEditor.html)
    *   [ThemeInfo(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeInfo.html)
    *   [ThemeNLAEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeNLAEditor.html)
    *   [ThemeNodeEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeNodeEditor.html)
    *   [ThemeOutliner(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeOutliner.html)
    *   [ThemePreferences(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemePreferences.html)
    *   [ThemeProperties(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeProperties.html)
    *   [ThemeRegions(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeRegions.html)
    *   [ThemeRegionsAssetShelf(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeRegionsAssetShelf.html)
    *   [ThemeRegionsChannels(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeRegionsChannels.html)
    *   [ThemeRegionsScrubbing(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeRegionsScrubbing.html)
    *   [ThemeRegionsSidebars(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeRegionsSidebars.html)
    *   [ThemeSequenceEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeSequenceEditor.html)
    *   [ThemeSpaceGeneric(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeSpaceGeneric.html)
    *   [ThemeSpaceGradient(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeSpaceGradient.html)
    *   [ThemeSpreadsheet(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeSpreadsheet.html)
    *   [ThemeStatusBar(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeStatusBar.html)
    *   [ThemeStripColor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeStripColor.html)
    *   [ThemeStyle(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeStyle.html)
    *   [ThemeTextEditor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeTextEditor.html)
    *   [ThemeTopBar(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeTopBar.html)
    *   [ThemeUserInterface(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeUserInterface.html)
    *   [ThemeView3D(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeView3D.html)
    *   [ThemeWidgetColors(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeWidgetColors.html)
    *   [ThemeWidgetStateColors(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ThemeWidgetStateColors.html)
    *   [TimelineMarker(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TimelineMarker.html)
    *   [TimelineMarkers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TimelineMarkers.html)
    *   [Timer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Timer.html)
    *   [ToolSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ToolSettings.html)
    *   [TrackToConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.TrackToConstraint.html)
    *   [TransformCacheConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.TransformCacheConstraint.html)
    *   [TransformConstraint(Constraint)](https://docs.blender.org/api/current/bpy.types.TransformConstraint.html)
    *   [TransformOrientation(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TransformOrientation.html)
    *   [TransformOrientationSlot(bpy_struct)](https://docs.blender.org/api/current/bpy.types.TransformOrientationSlot.html)
    *   [TriangulateModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.TriangulateModifier.html)
    *   [UDIMTile(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UDIMTile.html)
    *   [UDIMTiles(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UDIMTiles.html)
    *   [UILayout(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UILayout.html)
    *   [UIList(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UIList.html)
    *   [UIPieMenu(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UIPieMenu.html)
    *   [UIPopover(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UIPopover.html)
    *   [UIPopupMenu(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UIPopupMenu.html)
    *   [UI_UL_list(UIList)](https://docs.blender.org/api/current/bpy.types.UI_UL_list.html)
    *   [USDHook(bpy_struct)](https://docs.blender.org/api/current/bpy.types.USDHook.html)
    *   [USERPREF_UL_asset_libraries(UIList)](https://docs.blender.org/api/current/bpy.types.USERPREF_UL_asset_libraries.html)
    *   [USERPREF_UL_extension_repos(UIList)](https://docs.blender.org/api/current/bpy.types.USERPREF_UL_extension_repos.html)
    *   [UVLoopLayers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UVLoopLayers.html)
    *   [UVProjectModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.UVProjectModifier.html)
    *   [UVProjector(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UVProjector.html)
    *   [UVWarpModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.UVWarpModifier.html)
    *   [UnifiedPaintSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UnifiedPaintSettings.html)
    *   [UnitSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UnitSettings.html)
    *   [UnknownType(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UnknownType.html)
    *   [UserAssetLibrary(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UserAssetLibrary.html)
    *   [UserExtensionRepo(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UserExtensionRepo.html)
    *   [UserExtensionRepoCollection(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UserExtensionRepoCollection.html)
    *   [UserSolidLight(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UserSolidLight.html)
    *   [UvSculpt(bpy_struct)](https://docs.blender.org/api/current/bpy.types.UvSculpt.html)
    *   [VIEW3D_AST_brush_gpencil_paint(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_gpencil_paint.html)
    *   [VIEW3D_AST_brush_gpencil_sculpt(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_gpencil_sculpt.html)
    *   [VIEW3D_AST_brush_gpencil_vertex(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_gpencil_vertex.html)
    *   [VIEW3D_AST_brush_gpencil_weight(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_gpencil_weight.html)
    *   [VIEW3D_AST_brush_sculpt(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_sculpt.html)
    *   [VIEW3D_AST_brush_sculpt_curves(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_sculpt_curves.html)
    *   [VIEW3D_AST_brush_texture_paint(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_texture_paint.html)
    *   [VIEW3D_AST_brush_vertex_paint(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_vertex_paint.html)
    *   [VIEW3D_AST_brush_weight_paint(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_weight_paint.html)
    *   [VIEW3D_AST_pose_library(AssetShelf)](https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_pose_library.html)
    *   [VIEW3D_FH_camera_background_image(FileHandler)](https://docs.blender.org/api/current/bpy.types.VIEW3D_FH_camera_background_image.html)
    *   [VIEW3D_FH_empty_image(FileHandler)](https://docs.blender.org/api/current/bpy.types.VIEW3D_FH_empty_image.html)
    *   [VIEW3D_FH_vdb_volume(FileHandler)](https://docs.blender.org/api/current/bpy.types.VIEW3D_FH_vdb_volume.html)
    *   [VIEWLAYER_UL_aov(UIList)](https://docs.blender.org/api/current/bpy.types.VIEWLAYER_UL_aov.html)
    *   [VIEWLAYER_UL_linesets(UIList)](https://docs.blender.org/api/current/bpy.types.VIEWLAYER_UL_linesets.html)
    *   [VOLUME_UL_grids(UIList)](https://docs.blender.org/api/current/bpy.types.VOLUME_UL_grids.html)
    *   [VectorFont(ID)](https://docs.blender.org/api/current/bpy.types.VectorFont.html)
    *   [VertexGroup(bpy_struct)](https://docs.blender.org/api/current/bpy.types.VertexGroup.html)
    *   [VertexGroupElement(bpy_struct)](https://docs.blender.org/api/current/bpy.types.VertexGroupElement.html)
    *   [VertexGroups(bpy_struct)](https://docs.blender.org/api/current/bpy.types.VertexGroups.html)
    *   [VertexPaint(Paint)](https://docs.blender.org/api/current/bpy.types.VertexPaint.html)
    *   [VertexWeightEditModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.VertexWeightEditModifier.html)
    *   [VertexWeightMixModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.VertexWeightMixModifier.html)
    *   [VertexWeightProximityModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.VertexWeightProximityModifier.html)
    *   [View2D(bpy_struct)](https://docs.blender.org/api/current/bpy.types.View2D.html)
    *   [View3DCursor(bpy_struct)](https://docs.blender.org/api/current/bpy.types.View3DCursor.html)
    *   [View3DOverlay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.View3DOverlay.html)
    *   [View3DShading(bpy_struct)](https://docs.blender.org/api/current/bpy.types.View3DShading.html)
    *   [ViewLayer(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ViewLayer.html)
    *   [ViewLayerEEVEE(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ViewLayerEEVEE.html)
    *   [ViewLayers(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ViewLayers.html)
    *   [ViewerNodeViewerPathElem(ViewerPathElem)](https://docs.blender.org/api/current/bpy.types.ViewerNodeViewerPathElem.html)
    *   [ViewerPath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ViewerPath.html)
    *   [ViewerPathElem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.ViewerPathElem.html)
    *   [Volume(ID)](https://docs.blender.org/api/current/bpy.types.Volume.html)
    *   [VolumeDisplaceModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.VolumeDisplaceModifier.html)
    *   [VolumeDisplay(bpy_struct)](https://docs.blender.org/api/current/bpy.types.VolumeDisplay.html)
    *   [VolumeGrid(bpy_struct)](https://docs.blender.org/api/current/bpy.types.VolumeGrid.html)
    *   [VolumeGrids(bpy_struct)](https://docs.blender.org/api/current/bpy.types.VolumeGrids.html)
    *   [VolumeRender(bpy_struct)](https://docs.blender.org/api/current/bpy.types.VolumeRender.html)
    *   [VolumeToMeshModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.VolumeToMeshModifier.html)
    *   [VoronoiTexture(Texture)](https://docs.blender.org/api/current/bpy.types.VoronoiTexture.html)
    *   [WORKSPACE_UL_addons_items(UIList)](https://docs.blender.org/api/current/bpy.types.WORKSPACE_UL_addons_items.html)
    *   [WalkNavigation(bpy_struct)](https://docs.blender.org/api/current/bpy.types.WalkNavigation.html)
    *   [WarpModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.WarpModifier.html)
    *   [WaveModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.WaveModifier.html)
    *   [WeightedNormalModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.WeightedNormalModifier.html)
    *   [WeldModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.WeldModifier.html)
    *   [WhiteBalanceModifier(StripModifier)](https://docs.blender.org/api/current/bpy.types.WhiteBalanceModifier.html)
    *   [Window(bpy_struct)](https://docs.blender.org/api/current/bpy.types.Window.html)
    *   [WindowManager(ID)](https://docs.blender.org/api/current/bpy.types.WindowManager.html)
    *   [WipeStrip(EffectStrip)](https://docs.blender.org/api/current/bpy.types.WipeStrip.html)
    *   [WireframeModifier(Modifier)](https://docs.blender.org/api/current/bpy.types.WireframeModifier.html)
    *   [WoodTexture(Texture)](https://docs.blender.org/api/current/bpy.types.WoodTexture.html)
    *   [WorkSpace(ID)](https://docs.blender.org/api/current/bpy.types.WorkSpace.html)
    *   [WorkSpaceTool(bpy_struct)](https://docs.blender.org/api/current/bpy.types.WorkSpaceTool.html)
    *   [World(ID)](https://docs.blender.org/api/current/bpy.types.World.html)
    *   [WorldLighting(bpy_struct)](https://docs.blender.org/api/current/bpy.types.WorldLighting.html)
    *   [WorldMistSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.WorldMistSettings.html)
    *   [XrActionMap(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrActionMap.html)
    *   [XrActionMapBinding(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrActionMapBinding.html)
    *   [XrActionMapBindings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrActionMapBindings.html)
    *   [XrActionMapItem(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrActionMapItem.html)
    *   [XrActionMapItems(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrActionMapItems.html)
    *   [XrActionMaps(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrActionMaps.html)
    *   [XrComponentPath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrComponentPath.html)
    *   [XrComponentPaths(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrComponentPaths.html)
    *   [XrEventData(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrEventData.html)
    *   [XrNavigation(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrNavigation.html)
    *   [XrSessionSettings(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrSessionSettings.html)
    *   [XrSessionState(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrSessionState.html)
    *   [XrUserPath(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrUserPath.html)
    *   [XrUserPaths(bpy_struct)](https://docs.blender.org/api/current/bpy.types.XrUserPaths.html)
    *   [bpy_prop_collection](https://docs.blender.org/api/current/bpy.types.bpy_prop_collection.html)
    *   [bpy_prop_collection_idprop](https://docs.blender.org/api/current/bpy.types.bpy_prop_collection_idprop.html)
    *   [bpy_struct](https://docs.blender.org/api/current/bpy.types.bpy_struct.html)
    *   [wmOwnerID(bpy_struct)](https://docs.blender.org/api/current/bpy.types.wmOwnerID.html)
    *   [wmOwnerIDs(bpy_struct)](https://docs.blender.org/api/current/bpy.types.wmOwnerIDs.html)
    *   [wmTools(bpy_struct)](https://docs.blender.org/api/current/bpy.types.wmTools.html)
    *   [Shared Enum Types](https://docs.blender.org/api/current/bpy_types_enum_items/index.html)- [x] Toggle navigation of Shared Enum Types  
        *   [Id Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/id_type_items.html)
        *   [Object Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_mode_items.html)
        *   [Workspace Object Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/workspace_object_mode_items.html)
        *   [Object Empty Drawtype Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_empty_drawtype_items.html)
        *   [Object Gpencil Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_gpencil_type_items.html)
        *   [Metaelem Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/metaelem_type_items.html)
        *   [Color Space Convert Default Items](https://docs.blender.org/api/current/bpy_types_enum_items/color_space_convert_default_items.html)
        *   [Proportional Falloff Items](https://docs.blender.org/api/current/bpy_types_enum_items/proportional_falloff_items.html)
        *   [Proportional Falloff Curve Only Items](https://docs.blender.org/api/current/bpy_types_enum_items/proportional_falloff_curve_only_items.html)
        *   [Snap Source Items](https://docs.blender.org/api/current/bpy_types_enum_items/snap_source_items.html)
        *   [Snap Element Items](https://docs.blender.org/api/current/bpy_types_enum_items/snap_element_items.html)
        *   [Snap Animation Element Items](https://docs.blender.org/api/current/bpy_types_enum_items/snap_animation_element_items.html)
        *   [Curve Fit Method Items](https://docs.blender.org/api/current/bpy_types_enum_items/curve_fit_method_items.html)
        *   [Mesh Select Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/mesh_select_mode_items.html)
        *   [Mesh Select Mode Uv Items](https://docs.blender.org/api/current/bpy_types_enum_items/mesh_select_mode_uv_items.html)
        *   [Mesh Delimit Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/mesh_delimit_mode_items.html)
        *   [Space Graph Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/space_graph_mode_items.html)
        *   [Space File Browse Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/space_file_browse_mode_items.html)
        *   [Space Sequencer View Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/space_sequencer_view_type_items.html)
        *   [Space Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html)
        *   [Space Image Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/space_image_mode_items.html)
        *   [Space Image Mode All Items](https://docs.blender.org/api/current/bpy_types_enum_items/space_image_mode_all_items.html)
        *   [Space Action Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/space_action_mode_items.html)
        *   [Fileselect Params Sort Items](https://docs.blender.org/api/current/bpy_types_enum_items/fileselect_params_sort_items.html)
        *   [Region Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html)
        *   [Object Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_modifier_type_items.html)
        *   [Constraint Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/constraint_type_items.html)
        *   [Boidrule Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/boidrule_type_items.html)
        *   [Strip Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/strip_modifier_type_items.html)
        *   [Strip Video Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/strip_video_modifier_type_items.html)
        *   [Strip Sound Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/strip_sound_modifier_type_items.html)
        *   [Strip Scale Method Items](https://docs.blender.org/api/current/bpy_types_enum_items/strip_scale_method_items.html)
        *   [Object Shaderfx Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_shaderfx_type_items.html)
        *   [Modifier Triangulate Quad Method Items](https://docs.blender.org/api/current/bpy_types_enum_items/modifier_triangulate_quad_method_items.html)
        *   [Modifier Triangulate Ngon Method Items](https://docs.blender.org/api/current/bpy_types_enum_items/modifier_triangulate_ngon_method_items.html)
        *   [Modifier Shrinkwrap Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/modifier_shrinkwrap_mode_items.html)
        *   [Shrinkwrap Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/shrinkwrap_type_items.html)
        *   [Shrinkwrap Face Cull Items](https://docs.blender.org/api/current/bpy_types_enum_items/shrinkwrap_face_cull_items.html)
        *   [Node Warning Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_warning_type_items.html)
        *   [Image Type All Items](https://docs.blender.org/api/current/bpy_types_enum_items/image_type_all_items.html)
        *   [Image Color Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/image_color_mode_items.html)
        *   [Image Color Depth Items](https://docs.blender.org/api/current/bpy_types_enum_items/image_color_depth_items.html)
        *   [Image Generated Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/image_generated_type_items.html)
        *   [Normal Space Items](https://docs.blender.org/api/current/bpy_types_enum_items/normal_space_items.html)
        *   [Normal Swizzle Items](https://docs.blender.org/api/current/bpy_types_enum_items/normal_swizzle_items.html)
        *   [Bake Save Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_save_mode_items.html)
        *   [Bake Margin Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_margin_type_items.html)
        *   [Bake Target Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_target_items.html)
        *   [Views Format Items](https://docs.blender.org/api/current/bpy_types_enum_items/views_format_items.html)
        *   [Views Format Multilayer Items](https://docs.blender.org/api/current/bpy_types_enum_items/views_format_multilayer_items.html)
        *   [Views Format Multiview Items](https://docs.blender.org/api/current/bpy_types_enum_items/views_format_multiview_items.html)
        *   [Stereo3D Display Items](https://docs.blender.org/api/current/bpy_types_enum_items/stereo3d_display_items.html)
        *   [Stereo3D Anaglyph Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/stereo3d_anaglyph_type_items.html)
        *   [Stereo3D Interlace Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/stereo3d_interlace_type_items.html)
        *   [Exr Codec Items](https://docs.blender.org/api/current/bpy_types_enum_items/exr_codec_items.html)
        *   [Color Sets Items](https://docs.blender.org/api/current/bpy_types_enum_items/color_sets_items.html)
        *   [Beztriple Keyframe Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/beztriple_keyframe_type_items.html)
        *   [Beztriple Interpolation Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/beztriple_interpolation_mode_items.html)
        *   [Beztriple Interpolation Easing Items](https://docs.blender.org/api/current/bpy_types_enum_items/beztriple_interpolation_easing_items.html)
        *   [Fcurve Auto Smoothing Items](https://docs.blender.org/api/current/bpy_types_enum_items/fcurve_auto_smoothing_items.html)
        *   [Keyframe Handle Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/keyframe_handle_type_items.html)
        *   [Driver Target Rotation Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/driver_target_rotation_mode_items.html)
        *   [Keyingset Path Grouping Items](https://docs.blender.org/api/current/bpy_types_enum_items/keyingset_path_grouping_items.html)
        *   [Keying Flag Items](https://docs.blender.org/api/current/bpy_types_enum_items/keying_flag_items.html)
        *   [Keying Flag Api Items](https://docs.blender.org/api/current/bpy_types_enum_items/keying_flag_api_items.html)
        *   [Fmodifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/fmodifier_type_items.html)
        *   [Motionpath Bake Location Items](https://docs.blender.org/api/current/bpy_types_enum_items/motionpath_bake_location_items.html)
        *   [Motionpath Display Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/motionpath_display_type_items.html)
        *   [Motionpath Range Items](https://docs.blender.org/api/current/bpy_types_enum_items/motionpath_range_items.html)
        *   [Event Value Items](https://docs.blender.org/api/current/bpy_types_enum_items/event_value_items.html)
        *   [Event Direction Items](https://docs.blender.org/api/current/bpy_types_enum_items/event_direction_items.html)
        *   [Event Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/event_type_items.html)
        *   [Event Type Mask Items](https://docs.blender.org/api/current/bpy_types_enum_items/event_type_mask_items.html)
        *   [Operator Type Flag Items](https://docs.blender.org/api/current/bpy_types_enum_items/operator_type_flag_items.html)
        *   [Operator Return Items](https://docs.blender.org/api/current/bpy_types_enum_items/operator_return_items.html)
        *   [Operator Property Tag Items](https://docs.blender.org/api/current/bpy_types_enum_items/operator_property_tag_items.html)
        *   [Brush Automasking Flag Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_automasking_flag_items.html)
        *   [Brush Sculpt Brush Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_sculpt_brush_type_items.html)
        *   [Brush Vertex Brush Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_vertex_brush_type_items.html)
        *   [Brush Weight Brush Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_weight_brush_type_items.html)
        *   [Brush Gpencil Types Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_gpencil_types_items.html)
        *   [Brush Gpencil Vertex Types Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_gpencil_vertex_types_items.html)
        *   [Brush Gpencil Sculpt Types Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_gpencil_sculpt_types_items.html)
        *   [Brush Gpencil Weight Types Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_gpencil_weight_types_items.html)
        *   [Brush Curves Sculpt Brush Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_curves_sculpt_brush_type_items.html)
        *   [Brush Image Brush Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_image_brush_type_items.html)
        *   [Brush Curve Preset Items](https://docs.blender.org/api/current/bpy_types_enum_items/brush_curve_preset_items.html)
        *   [Grease Pencil Selectmode Items](https://docs.blender.org/api/current/bpy_types_enum_items/grease_pencil_selectmode_items.html)
        *   [Stroke Depth Order Items](https://docs.blender.org/api/current/bpy_types_enum_items/stroke_depth_order_items.html)
        *   [Axis Xy Items](https://docs.blender.org/api/current/bpy_types_enum_items/axis_xy_items.html)
        *   [Axis Xyz Items](https://docs.blender.org/api/current/bpy_types_enum_items/axis_xyz_items.html)
        *   [Axis Flag Xyz Items](https://docs.blender.org/api/current/bpy_types_enum_items/axis_flag_xyz_items.html)
        *   [Symmetrize Direction Items](https://docs.blender.org/api/current/bpy_types_enum_items/symmetrize_direction_items.html)
        *   [Texture Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/texture_type_items.html)
        *   [Light Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/light_type_items.html)
        *   [Lightprobes Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/lightprobes_type_items.html)
        *   [Unpack Method Items](https://docs.blender.org/api/current/bpy_types_enum_items/unpack_method_items.html)
        *   [Object Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_type_items.html)
        *   [Object Rotation Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_rotation_mode_items.html)
        *   [Object Type Curve Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_type_curve_items.html)
        *   [Rigidbody Object Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/rigidbody_object_type_items.html)
        *   [Rigidbody Object Shape Items](https://docs.blender.org/api/current/bpy_types_enum_items/rigidbody_object_shape_items.html)
        *   [Rigidbody Constraint Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/rigidbody_constraint_type_items.html)
        *   [Object Axis Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_axis_items.html)
        *   [Bake Pass Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_pass_type_items.html)
        *   [Bake Pass Filter Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_pass_filter_type_items.html)
        *   [Keymap Propvalue Items](https://docs.blender.org/api/current/bpy_types_enum_items/keymap_propvalue_items.html)
        *   [Operator Context Items](https://docs.blender.org/api/current/bpy_types_enum_items/operator_context_items.html)
        *   [Wm Report Items](https://docs.blender.org/api/current/bpy_types_enum_items/wm_report_items.html)
        *   [Wm Job Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/wm_job_type_items.html)
        *   [Property Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_type_items.html)
        *   [Property Subtype Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_subtype_items.html)
        *   [Property Subtype String Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_subtype_string_items.html)
        *   [Property Subtype Number Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_subtype_number_items.html)
        *   [Property Subtype Number Array Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_subtype_number_array_items.html)
        *   [Property Unit Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_unit_items.html)
        *   [Property Flag Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_flag_items.html)
        *   [Property Flag Enum Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_flag_enum_items.html)
        *   [Property Override Flag Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_override_flag_items.html)
        *   [Property Override Flag Collection Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_override_flag_collection_items.html)
        *   [Property String Search Flag Items](https://docs.blender.org/api/current/bpy_types_enum_items/property_string_search_flag_items.html)
        *   [Shading Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/shading_type_items.html)
        *   [Navigation Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/navigation_mode_items.html)
        *   [Node Socket In Out Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_socket_in_out_items.html)
        *   [Node Socket Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_socket_type_items.html)
        *   [Node Tree Interface Item Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_tree_interface_item_type_items.html)
        *   [Node Socket Structure Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_socket_structure_type_items.html)
        *   [Node Math Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_math_items.html)
        *   [Mapping Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/mapping_type_items.html)
        *   [Node Vec Math Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_vec_math_items.html)
        *   [Node Boolean Math Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_boolean_math_items.html)
        *   [Node Compare Operation Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_compare_operation_items.html)
        *   [Node Integer Math Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_integer_math_items.html)
        *   [Node Float To Int Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_float_to_int_items.html)
        *   [Node Map Range Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_map_range_items.html)
        *   [Node Clamp Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_clamp_items.html)
        *   [Node Compositor Extension Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_compositor_extension_items.html)
        *   [Node Compositor Interpolation Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_compositor_interpolation_items.html)
        *   [Ramp Blend Items](https://docs.blender.org/api/current/bpy_types_enum_items/ramp_blend_items.html)
        *   [Prop Dynamicpaint Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/prop_dynamicpaint_type_items.html)
        *   [Clip Editor Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/clip_editor_mode_items.html)
        *   [Icon Items](https://docs.blender.org/api/current/bpy_types_enum_items/icon_items.html)
        *   [Uilist Layout Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/uilist_layout_type_items.html)
        *   [Linestyle Color Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/linestyle_color_modifier_type_items.html)
        *   [Linestyle Alpha Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/linestyle_alpha_modifier_type_items.html)
        *   [Linestyle Thickness Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/linestyle_thickness_modifier_type_items.html)
        *   [Linestyle Geometry Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/linestyle_geometry_modifier_type_items.html)
        *   [Window Cursor Items](https://docs.blender.org/api/current/bpy_types_enum_items/window_cursor_items.html)
        *   [Dt Method Vertex Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_vertex_items.html)
        *   [Dt Method Edge Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_edge_items.html)
        *   [Dt Method Loop Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_loop_items.html)
        *   [Dt Method Poly Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_poly_items.html)
        *   [Dt Mix Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_mix_mode_items.html)
        *   [Dt Layers Select Src Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_layers_select_src_items.html)
        *   [Dt Layers Select Dst Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_layers_select_dst_items.html)
        *   [Context Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/context_mode_items.html)
        *   [Preference Section Items](https://docs.blender.org/api/current/bpy_types_enum_items/preference_section_items.html)
        *   [Attribute Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_type_items.html)
        *   [Color Attribute Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/color_attribute_type_items.html)
        *   [Attribute Type With Auto Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_type_with_auto_items.html)
        *   [Attribute Domain Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_items.html)
        *   [Attribute Domain Edge Face Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_edge_face_items.html)
        *   [Attribute Domain Only Mesh Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_only_mesh_items.html)
        *   [Attribute Domain Only Mesh No Edge Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_only_mesh_no_edge_items.html)
        *   [Attribute Domain Only Mesh No Corner Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_only_mesh_no_corner_items.html)
        *   [Attribute Domain Point Face Curve Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_point_face_curve_items.html)
        *   [Attribute Domain Point Edge Face Curve Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_point_edge_face_curve_items.html)
        *   [Attribute Curves Domain Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_curves_domain_items.html)
        *   [Color Attribute Domain Items](https://docs.blender.org/api/current/bpy_types_enum_items/color_attribute_domain_items.html)
        *   [Attribute Domain Without Corner Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_without_corner_items.html)
        *   [Attribute Domain With Auto Items](https://docs.blender.org/api/current/bpy_types_enum_items/attribute_domain_with_auto_items.html)
        *   [Geometry Component Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/geometry_component_type_items.html)
        *   [Node Combsep Color Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_combsep_color_items.html)
        *   [Node Socket Data Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_socket_data_type_items.html)
        *   [Node Geometry Curve Handle Side Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_geometry_curve_handle_side_items.html)
        *   [Node Geometry Mesh Circle Fill Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/node_geometry_mesh_circle_fill_type_items.html)
        *   [Volume Grid Data Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/volume_grid_data_type_items.html)
        *   [Collection Color Items](https://docs.blender.org/api/current/bpy_types_enum_items/collection_color_items.html)
        *   [Strip Color Items](https://docs.blender.org/api/current/bpy_types_enum_items/strip_color_items.html)
        *   [Subdivision Uv Smooth Items](https://docs.blender.org/api/current/bpy_types_enum_items/subdivision_uv_smooth_items.html)
        *   [Subdivision Boundary Smooth Items](https://docs.blender.org/api/current/bpy_types_enum_items/subdivision_boundary_smooth_items.html)
        *   [Transform Orientation Items](https://docs.blender.org/api/current/bpy_types_enum_items/transform_orientation_items.html)
        *   [Velocity Unit Items](https://docs.blender.org/api/current/bpy_types_enum_items/velocity_unit_items.html)
        *   [Curves Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/curves_type_items.html)
        *   [Curves Handle Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/curves_handle_type_items.html)
        *   [Curve Normal Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/curve_normal_mode_items.html)
        *   [Geometry Nodes Gizmo Color Items](https://docs.blender.org/api/current/bpy_types_enum_items/geometry_nodes_gizmo_color_items.html)
        *   [Geometry Nodes Linear Gizmo Draw Style Items](https://docs.blender.org/api/current/bpy_types_enum_items/geometry_nodes_linear_gizmo_draw_style_items.html)
        *   [Particle Edit Hair Brush Items](https://docs.blender.org/api/current/bpy_types_enum_items/particle_edit_hair_brush_items.html)
        *   [Particle Edit Disconnected Hair Brush Items](https://docs.blender.org/api/current/bpy_types_enum_items/particle_edit_disconnected_hair_brush_items.html)
        *   [Keyframe Paste Offset Items](https://docs.blender.org/api/current/bpy_types_enum_items/keyframe_paste_offset_items.html)
        *   [Keyframe Paste Offset Value Items](https://docs.blender.org/api/current/bpy_types_enum_items/keyframe_paste_offset_value_items.html)
        *   [Keyframe Paste Merge Items](https://docs.blender.org/api/current/bpy_types_enum_items/keyframe_paste_merge_items.html)
        *   [Transform Pivot Full Items](https://docs.blender.org/api/current/bpy_types_enum_items/transform_pivot_full_items.html)
        *   [Transform Mode Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/transform_mode_type_items.html)
        *   [Nla Mode Extend Items](https://docs.blender.org/api/current/bpy_types_enum_items/nla_mode_extend_items.html)
        *   [Nla Mode Blend Items](https://docs.blender.org/api/current/bpy_types_enum_items/nla_mode_blend_items.html)
        *   [Keyblock Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/keyblock_type_items.html)
        *   [Asset Library Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/asset_library_type_items.html)
        *   [File Path Foreach Flag Items](https://docs.blender.org/api/current/bpy_types_enum_items/file_path_foreach_flag_items.html)

    *   [Types with Custom Property Support](https://docs.blender.org/api/current/bpy_types_custom_properties.html)

*   [Utilities (bpy.utils)](https://docs.blender.org/api/current/bpy.utils.html)- [x] Toggle navigation of Utilities (bpy.utils)  
    *   [bpy.utils submodule (bpy.utils.previews)](https://docs.blender.org/api/current/bpy.utils.previews.html)
    *   [bpy.utils submodule (bpy.utils.units)](https://docs.blender.org/api/current/bpy.utils.units.html)

*   [Path Utilities (bpy.path)](https://docs.blender.org/api/current/bpy.path.html)
*   [Application Data (bpy.app)](https://docs.blender.org/api/current/bpy.app.html)- [x] Toggle navigation of Application Data (bpy.app)  
    *   [Application Handlers (bpy.app.handlers)](https://docs.blender.org/api/current/bpy.app.handlers.html)
    *   [Application Translations (bpy.app.translations)](https://docs.blender.org/api/current/bpy.app.translations.html)
    *   [Application Icons (bpy.app.icons)](https://docs.blender.org/api/current/bpy.app.icons.html)
    *   [Application Timers (bpy.app.timers)](https://docs.blender.org/api/current/bpy.app.timers.html)

*   [Property Definitions (bpy.props)](https://docs.blender.org/api/current/bpy.props.html)

Standalone Modules

*   [Audio System (aud)](https://docs.blender.org/api/current/aud.html)
*   [Additional Math Functions (bl_math)](https://docs.blender.org/api/current/bl_math.html)
*   [Font Drawing (blf)](https://docs.blender.org/api/current/blf.html)
*   [BMesh Module (bmesh)](https://docs.blender.org/api/current/bmesh.html)- [x] Toggle navigation of BMesh Module (bmesh)  
    *   [BMesh Operators (bmesh.ops)](https://docs.blender.org/api/current/bmesh.ops.html)
    *   [BMesh Types (bmesh.types)](https://docs.blender.org/api/current/bmesh.types.html)
    *   [BMesh Utilities (bmesh.utils)](https://docs.blender.org/api/current/bmesh.utils.html)
    *   [BMesh Geometry Utilities (bmesh.geometry)](https://docs.blender.org/api/current/bmesh.geometry.html)

*   [Extra Utilities (bpy_extras)](https://docs.blender.org/api/current/bpy_extras.html)- [x] Toggle navigation of Extra Utilities (bpy_extras)  
    *   [bpy_extras submodule (bpy_extras.anim_utils)](https://docs.blender.org/api/current/bpy_extras.anim_utils.html)
    *   [bpy_extras submodule (bpy_extras.asset_utils)](https://docs.blender.org/api/current/bpy_extras.asset_utils.html)
    *   [bpy_extras submodule (bpy_extras.object_utils)](https://docs.blender.org/api/current/bpy_extras.object_utils.html)
    *   [bpy_extras submodule (bpy_extras.io_utils)](https://docs.blender.org/api/current/bpy_extras.io_utils.html)
    *   [bpy_extras submodule (bpy_extras.image_utils)](https://docs.blender.org/api/current/bpy_extras.image_utils.html)
    *   [bpy_extras submodule (bpy_extras.keyconfig_utils)](https://docs.blender.org/api/current/bpy_extras.keyconfig_utils.html)
    *   [bpy_extras submodule (bpy_extras.mesh_utils)](https://docs.blender.org/api/current/bpy_extras.mesh_utils.html)
    *   [bpy_extras submodule (bpy_extras.node_utils)](https://docs.blender.org/api/current/bpy_extras.node_utils.html)
    *   [bpy_extras submodule (bpy_extras.view3d_utils)](https://docs.blender.org/api/current/bpy_extras.view3d_utils.html)
    *   [bpy_extras submodule (bpy_extras.id_map_utils)](https://docs.blender.org/api/current/bpy_extras.id_map_utils.html)

*   [Freestyle Module (freestyle)](https://docs.blender.org/api/current/freestyle.html)- [x] Toggle navigation of Freestyle Module (freestyle)  
    *   [Freestyle Types (freestyle.types)](https://docs.blender.org/api/current/freestyle.types.html)
    *   [Freestyle Predicates (freestyle.predicates)](https://docs.blender.org/api/current/freestyle.predicates.html)
    *   [Freestyle Functions (freestyle.functions)](https://docs.blender.org/api/current/freestyle.functions.html)
    *   [Freestyle Chaining Iterators (freestyle.chainingiterators)](https://docs.blender.org/api/current/freestyle.chainingiterators.html)
    *   [Freestyle Shaders (freestyle.shaders)](https://docs.blender.org/api/current/freestyle.shaders.html)
    *   [Freestyle Utilities (freestyle.utils)](https://docs.blender.org/api/current/freestyle.utils.html)- [x] Toggle navigation of Freestyle Utilities (freestyle.utils)  
        *   [freestyle.utils submodule (freestyle.utils.ContextFunctions)](https://docs.blender.org/api/current/freestyle.utils.ContextFunctions.html)

*   [GPU Module (gpu)](https://docs.blender.org/api/current/gpu.html)- [x] Toggle navigation of GPU Module (gpu)  
    *   [GPU Types (gpu.types)](https://docs.blender.org/api/current/gpu.types.html)
    *   [GPU Matrix Utilities (gpu.matrix)](https://docs.blender.org/api/current/gpu.matrix.html)
    *   [GPU Select Utilities (gpu.select)](https://docs.blender.org/api/current/gpu.select.html)
    *   [GPU Shader Utilities (gpu.shader)](https://docs.blender.org/api/current/gpu.shader.html)
    *   [GPU State Utilities (gpu.state)](https://docs.blender.org/api/current/gpu.state.html)
    *   [GPU Texture Utilities (gpu.texture)](https://docs.blender.org/api/current/gpu.texture.html)
    *   [GPU Platform Utilities (gpu.platform)](https://docs.blender.org/api/current/gpu.platform.html)
    *   [GPU Capabilities Utilities (gpu.capabilities)](https://docs.blender.org/api/current/gpu.capabilities.html)

*   [GPU Utilities (gpu_extras)](https://docs.blender.org/api/current/gpu_extras.html)- [x] Toggle navigation of GPU Utilities (gpu_extras)  
    *   [gpu_extras submodule (gpu_extras.batch)](https://docs.blender.org/api/current/gpu_extras.batch.html)
    *   [gpu_extras submodule (gpu_extras.presets)](https://docs.blender.org/api/current/gpu_extras.presets.html)

*   [ID Property Access (idprop.types)](https://docs.blender.org/api/current/idprop.types.html)
*   [Image Buffer (imbuf)](https://docs.blender.org/api/current/imbuf.html)- [x] Toggle navigation of Image Buffer (imbuf)  
    *   [Image Buffer Types (imbuf.types)](https://docs.blender.org/api/current/imbuf.types.html)

*   [Math Types & Utilities (mathutils)](https://docs.blender.org/api/current/mathutils.html)- [x] Toggle navigation of Math Types & Utilities (mathutils)  
    *   [Geometry Utilities (mathutils.geometry)](https://docs.blender.org/api/current/mathutils.geometry.html)
    *   [BVHTree Utilities (mathutils.bvhtree)](https://docs.blender.org/api/current/mathutils.bvhtree.html)
    *   [KDTree Utilities (mathutils.kdtree)](https://docs.blender.org/api/current/mathutils.kdtree.html)
    *   [Interpolation Utilities (mathutils.interpolate)](https://docs.blender.org/api/current/mathutils.interpolate.html)
    *   [Noise Utilities (mathutils.noise)](https://docs.blender.org/api/current/mathutils.noise.html)

*    5.0 

Versions 
    *   Loading...

*   [](https://docs.blender.org/api/current/bpy.ops.object.html)

Note

You are not using the most up to date version of the documentation. [](https://docs.blender.org/api/current/bpy.ops.object.html#) is the newest version.

[Back to top](https://docs.blender.org/api/current/bpy.ops.object.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

 

Object Operators[¶](https://docs.blender.org/api/current/bpy.ops.object.html#module-bpy.ops.object "Link to this heading")
==========================================================================================================================

bpy.ops.object.add(_*_, _radius=1.0_, _type='EMPTY'_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.add "Link to this definition")
Add an object to the scene

Parameters:
*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **type** (enum in [Object Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_type_items.html#rna-enum-object-type-items), (optional)) – Type

*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.add_modifier_menu()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.add_modifier_menu "Link to this definition")
Undocumented, consider [contributing](https://developer.blender.org/).

File:
[startup/bl_ui/properties_data_modifier.py:303](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/properties_data_modifier.py#L303)

bpy.ops.object.add_named(_*_, _linked=False_, _name=''_, _session\_uid=0_, _matrix=((0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0))_, _drop\_x=0_, _drop\_y=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.add_named "Link to this definition")
Add named object

Parameters:
*   **linked** (_boolean_ _,_ _(_ _optional_ _)_) – Linked, Duplicate object but not object data, linking to the original data

*   **name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Name of the data-block to use by the operator

*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **matrix** ([`mathutils.Matrix`](https://docs.blender.org/api/current/mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – Matrix

*   **drop_x** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

*   **drop_y** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.align(_*_, _bb\_quality=True_, _align\_mode='OPT\_2'_, _relative\_to='OPT\_4'_, _align\_axis={}_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.align "Link to this definition")
Align objects

Parameters:
*   **bb_quality** (_boolean_ _,_ _(_ _optional_ _)_) – High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale

*   **align_mode** (enum in [`'OPT_1'`, `'OPT_2'`, `'OPT_3'`], (optional)) – Align Mode, Side of object to use for alignment

*   **relative_to** (enum in [`'OPT_1'`, `'OPT_2'`, `'OPT_3'`, `'OPT_4'`], (optional)) –

Relative To, Reference location to align to

    *   `OPT_1` Scene Origin – Use the scene origin as the position for the selected objects to align to.

    *   `OPT_2` 3D Cursor – Use the 3D cursor as the position for the selected objects to align to.

    *   `OPT_3` Selection – Use the selected objects as the position for the selected objects to align to.

    *   `OPT_4` Active – Use the active object as the position for the selected objects to align to.

*   **align_axis** (enum set in {`'X'`, `'Y'`, `'Z'`}, (optional)) – Align, Align to axis

File:
[startup/bl_operators/object_align.py:386](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_align.py#L386)

bpy.ops.object.anim_transforms_to_deltas()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.anim_transforms_to_deltas "Link to this definition")
Convert object animation for normal transforms to delta transforms

File:
[startup/bl_operators/object.py:822](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L822)

bpy.ops.object.armature_add(_*_, _radius=1.0_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.armature_add "Link to this definition")
Add an armature object to the scene

Parameters:
*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.assign_property_defaults(_*_, _process\_data=True_, _process\_bones=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.assign_property_defaults "Link to this definition")
Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing

Parameters:
*   **process_data** (_boolean_ _,_ _(_ _optional_ _)_) – Process data properties

*   **process_bones** (_boolean_ _,_ _(_ _optional_ _)_) – Process bone properties

File:
[startup/bl_operators/object.py:979](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L979)

bpy.ops.object.bake(_*_, _type='COMBINED'_, _pass\_filter={}_, _filepath=''_, _width=512_, _height=512_, _margin=16_, _margin\_type='EXTEND'_, _use\_selected\_to\_active=False_, _max\_ray\_distance=0.0_, _cage\_extrusion=0.0_, _cage\_object=''_, _normal\_space='TANGENT'_, _normal\_r='POS\_X'_, _normal\_g='POS\_Y'_, _normal\_b='POS\_Z'_, _target='IMAGE\_TEXTURES'_, _save\_mode='INTERNAL'_, _use\_clear=False_, _use\_cage=False_, _use\_split\_materials=False_, _use\_automatic\_name=False_, _uv\_layer=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.bake "Link to this definition")
Bake image textures of selected objects

Parameters:
*   **type** (enum in [Bake Pass Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_pass_type_items.html#rna-enum-bake-pass-type-items), (optional)) – Type, Type of pass to bake, some of them may not be supported by the current render engine

*   **pass_filter** (enum set in [Bake Pass Filter Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_pass_filter_type_items.html#rna-enum-bake-pass-filter-type-items), (optional)) – Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes

*   **filepath** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – File Path, Image filepath to use when saving externally

*   **width** (_int in_ _[_ _1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Width, Horizontal dimension of the baking map (external only)

*   **height** (_int in_ _[_ _1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Height, Vertical dimension of the baking map (external only)

*   **margin** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Margin, Extends the baked result as a post process filter

*   **margin_type** (enum in [Bake Margin Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_margin_type_items.html#rna-enum-bake-margin-type-items), (optional)) – Margin Type, Which algorithm to use to generate the margin

*   **use_selected_to_active** (_boolean_ _,_ _(_ _optional_ _)_) – Selected to Active, Bake shading on the surface of selected objects to the active object

*   **max_ray_distance** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit

*   **cage_extrusion** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes

*   **cage_object** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion

*   **normal_space** (enum in [Normal Space Items](https://docs.blender.org/api/current/bpy_types_enum_items/normal_space_items.html#rna-enum-normal-space-items), (optional)) – Normal Space, Choose normal space for baking

*   **normal_r** (enum in [Normal Swizzle Items](https://docs.blender.org/api/current/bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-items), (optional)) – R, Axis to bake in red channel

*   **normal_g** (enum in [Normal Swizzle Items](https://docs.blender.org/api/current/bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-items), (optional)) – G, Axis to bake in green channel

*   **normal_b** (enum in [Normal Swizzle Items](https://docs.blender.org/api/current/bpy_types_enum_items/normal_swizzle_items.html#rna-enum-normal-swizzle-items), (optional)) – B, Axis to bake in blue channel

*   **target** (enum in [Bake Target Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_target_items.html#rna-enum-bake-target-items), (optional)) – Target, Where to output the baked map

*   **save_mode** (enum in [Bake Save Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/bake_save_mode_items.html#rna-enum-bake-save-mode-items), (optional)) – Save Mode, Where to save baked image textures

*   **use_clear** (_boolean_ _,_ _(_ _optional_ _)_) – Clear, Clear images before baking (only for internal saving)

*   **use_cage** (_boolean_ _,_ _(_ _optional_ _)_) – Cage, Cast rays to active object from a cage

*   **use_split_materials** (_boolean_ _,_ _(_ _optional_ _)_) – Split Materials, Split baked maps per material, using material name in output file (external only)

*   **use_automatic_name** (_boolean_ _,_ _(_ _optional_ _)_) – Automatic Name, Automatically name the output file with the pass type

*   **uv_layer** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – UV Layer, UV layer to override active

bpy.ops.object.bake_image()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.bake_image "Link to this definition")
Bake image textures of selected objects

bpy.ops.object.camera_add(_*_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.camera_add "Link to this definition")
Add a camera object to the scene

Parameters:
*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.camera_custom_update()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.camera_custom_update "Link to this definition")
Update custom camera with new parameters from the shader

bpy.ops.object.clear_override_library()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.clear_override_library "Link to this definition")
Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable

bpy.ops.object.collection_add()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_add "Link to this definition")
Add an object to a new collection

bpy.ops.object.collection_external_asset_drop(_*_, _session\_uid=0_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_, _use\_instance=True_, _drop\_x=0_, _drop\_y=0_, _collection=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_external_asset_drop "Link to this definition")
Add the dragged collection to the scene

Parameters:
*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

*   **use_instance** (_boolean_ _,_ _(_ _optional_ _)_) – Instance, Add the dropped collection as collection instance

*   **drop_x** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

*   **drop_y** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

*   **collection** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Collection

bpy.ops.object.collection_instance_add(_*_, _name='Collection'_, _collection=''_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_, _session\_uid=0_, _drop\_x=0_, _drop\_y=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_instance_add "Link to this definition")
Add a collection instance

Parameters:
*   **name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Collection name to add

*   **collection** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Collection

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **drop_x** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

*   **drop_y** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.collection_link(_*_, _collection=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_link "Link to this definition")
Add an object to an existing collection

Parameters:
**collection** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Collection

bpy.ops.object.collection_objects_select()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_objects_select "Link to this definition")
Select all objects in collection

bpy.ops.object.collection_remove()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_remove "Link to this definition")
Remove the active object from this collection

bpy.ops.object.collection_unlink()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_unlink "Link to this definition")
Unlink the collection from all objects

bpy.ops.object.constraint_add(_*_, _type=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraint_add "Link to this definition")
Add a constraint to the active object

Parameters:
**type** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Type

bpy.ops.object.constraint_add_with_targets(_*_, _type=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraint_add_with_targets "Link to this definition")
Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

Parameters:
**type** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Type

bpy.ops.object.constraints_clear()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraints_clear "Link to this definition")
Clear all constraints from the selected objects

bpy.ops.object.constraints_copy()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraints_copy "Link to this definition")
Copy constraints to other selected objects

bpy.ops.object.convert(_*_, _target='MESH'_, _keep\_original=False_, _merge\_customdata=True_, _thickness=5_, _faces=True_, _offset=0.01_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.convert "Link to this definition")
Convert selected objects to another type

Parameters:
*   **target** (enum in [`'CURVE'`, `'MESH'`, `'POINTCLOUD'`, `'CURVES'`, `'GREASEPENCIL'`], (optional)) –

Target, Type of object to convert to

    *   `CURVE` Curve – Curve from Mesh or Text objects.

    *   `MESH` Mesh – Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects.

    *   `POINTCLOUD` Point Cloud – Point Cloud from Mesh objects.

    *   `CURVES` Curves – Curves from evaluated curve data.

    *   `GREASEPENCIL` Grease Pencil – Grease Pencil from Curve or Mesh objects.

*   **keep_original** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Original, Keep original objects instead of replacing them

*   **merge_customdata** (_boolean_ _,_ _(_ _optional_ _)_) – Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers

*   **thickness** (_int in_ _[_ _1_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – Thickness

*   **faces** (_boolean_ _,_ _(_ _optional_ _)_) – Export Faces, Export faces as filled strokes

*   **offset** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Stroke Offset, Offset strokes from fill

bpy.ops.object.copy_global_transform()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.copy_global_transform "Link to this definition")
Copies the matrix of the currently active object or pose bone to the clipboard. Uses world-space matrices

File:
[startup/bl_operators/copy_global_transform.py:150](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L150)

bpy.ops.object.copy_relative_transform()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.copy_relative_transform "Link to this definition")
Copies the matrix of the currently active object or pose bone to the clipboard. Uses matrices relative to a specific object or the active scene camera

File:
[startup/bl_operators/copy_global_transform.py:180](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L180)

bpy.ops.object.correctivesmooth_bind(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.correctivesmooth_bind "Link to this definition")
Bind base pose in Corrective Smooth modifier

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.curves_empty_hair_add(_*_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.curves_empty_hair_add "Link to this definition")
Add an empty curve object to the scene with the selected mesh as surface

Parameters:
*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.curves_random_add(_*_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.curves_random_add "Link to this definition")
Add a curves object with random curves to the scene

Parameters:
*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.data_instance_add(_*_, _name=''_, _session\_uid=0_, _type='ACTION'_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_, _drop\_x=0_, _drop\_y=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.data_instance_add "Link to this definition")
Add an object data instance

Parameters:
*   **name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Name of the data-block to use by the operator

*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **type** (enum in [Id Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/id_type_items.html#rna-enum-id-type-items), (optional)) – Type

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

*   **drop_x** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

*   **drop_y** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.data_transfer(_*_, _use\_reverse\_transfer=False_, _use\_freeze=False_, _data\_type=''_, _use\_create=True_, _vert\_mapping='NEAREST'_, _edge\_mapping='NEAREST'_, _loop\_mapping='NEAREST\_POLYNOR'_, _poly\_mapping='NEAREST'_, _use\_auto\_transform=False_, _use\_object\_transform=True_, _use\_max\_distance=False_, _max\_distance=1.0_, _ray\_radius=0.0_, _islands\_precision=0.1_, _layers\_select\_src='ACTIVE'_, _layers\_select\_dst='ACTIVE'_, _mix\_mode='REPLACE'_, _mix\_factor=1.0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.data_transfer "Link to this definition")
Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

Parameters:
*   **use_reverse_transfer** (_boolean_ _,_ _(_ _optional_ _)_) – Reverse Transfer, Transfer from selected objects to active one

*   **use_freeze** (_boolean_ _,_ _(_ _optional_ _)_) – Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry

*   **data_type** (enum in [`'VGROUP_WEIGHTS'`, `'BEVEL_WEIGHT_VERT'`, `'COLOR_VERTEX'`, `'SHARP_EDGE'`, `'SEAM'`, `'CREASE'`, `'BEVEL_WEIGHT_EDGE'`, `'FREESTYLE_EDGE'`, `'CUSTOM_NORMAL'`, `'COLOR_CORNER'`, `'UV'`, `'SMOOTH'`, `'FREESTYLE_FACE'`], (optional)) –

Data Type, Which data to transfer

    *   `VGROUP_WEIGHTS` Vertex Group(s) – Transfer active or all vertex groups.

    *   `BEVEL_WEIGHT_VERT` Bevel Weight – Transfer bevel weights.

    *   `COLOR_VERTEX` Colors – Color Attributes.

    *   `SHARP_EDGE` Sharp – Transfer sharp mark.

    *   `SEAM` UV Seam – Transfer UV seam mark.

    *   `CREASE` Subdivision Crease – Transfer crease values.

    *   `BEVEL_WEIGHT_EDGE` Bevel Weight – Transfer bevel weights.

    *   `FREESTYLE_EDGE` Freestyle Mark – Transfer Freestyle edge mark.

    *   `CUSTOM_NORMAL` Custom Normals – Transfer custom normals.

    *   `COLOR_CORNER` Colors – Color Attributes.

    *   `UV` UVs – Transfer UV layers.

    *   `SMOOTH` Smooth – Transfer flat/smooth mark.

    *   `FREESTYLE_FACE` Freestyle Mark – Transfer Freestyle face mark.

*   **use_create** (_boolean_ _,_ _(_ _optional_ _)_) – Create Data, Add data layers on destination meshes if needed

*   **vert_mapping** (enum in [Dt Method Vertex Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_vertex_items.html#rna-enum-dt-method-vertex-items), (optional)) – Vertex Mapping, Method used to map source vertices to destination ones

*   **edge_mapping** (enum in [Dt Method Edge Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_edge_items.html#rna-enum-dt-method-edge-items), (optional)) – Edge Mapping, Method used to map source edges to destination ones

*   **loop_mapping** (enum in [Dt Method Loop Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_loop_items.html#rna-enum-dt-method-loop-items), (optional)) – Face Corner Mapping, Method used to map source faces’ corners to destination ones

*   **poly_mapping** (enum in [Dt Method Poly Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_method_poly_items.html#rna-enum-dt-method-poly-items), (optional)) – Face Mapping, Method used to map source faces to destination ones

*   **use_auto_transform** (_boolean_ _,_ _(_ _optional_ _)_) – Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects

*   **use_object_transform** (_boolean_ _,_ _(_ _optional_ _)_) – Object Transform, Evaluate source and destination meshes in global space

*   **use_max_distance** (_boolean_ _,_ _(_ _optional_ _)_) – Only Neighbor Geometry, Source elements must be closer than given distance from destination one

*   **max_distance** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings

*   **ray_radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Ray Radius, ‘Width’ of rays (especially useful when raycasting against vertices or edges)

*   **islands_precision** (_float in_ _[_ _0_ _,_ _10_ _]_ _,_ _(_ _optional_ _)_) – Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)

*   **layers_select_src** (enum in [Dt Layers Select Src Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-layers-select-src-items), (optional)) – Source Layers Selection, Which layers to transfer, in case of multi-layers types

*   **layers_select_dst** (enum in [Dt Layers Select Dst Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-layers-select-dst-items), (optional)) – Destination Layers Matching, How to match source and destination layers

*   **mix_mode** (enum in [Dt Mix Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_mix_mode_items.html#rna-enum-dt-mix-mode-items), (optional)) – Mix Mode, How to affect destination elements with source values

*   **mix_factor** (_float in_ _[_ _0_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)

bpy.ops.object.datalayout_transfer(_*_, _modifier=''_, _data\_type=''_, _use\_delete=False_, _layers\_select\_src='ACTIVE'_, _layers\_select\_dst='ACTIVE'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.datalayout_transfer "Link to this definition")
Transfer layout of data layer(s) from active to selected meshes

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **data_type** (enum in [`'VGROUP_WEIGHTS'`, `'BEVEL_WEIGHT_VERT'`, `'COLOR_VERTEX'`, `'SHARP_EDGE'`, `'SEAM'`, `'CREASE'`, `'BEVEL_WEIGHT_EDGE'`, `'FREESTYLE_EDGE'`, `'CUSTOM_NORMAL'`, `'COLOR_CORNER'`, `'UV'`, `'SMOOTH'`, `'FREESTYLE_FACE'`], (optional)) –

Data Type, Which data to transfer

    *   `VGROUP_WEIGHTS` Vertex Group(s) – Transfer active or all vertex groups.

    *   `BEVEL_WEIGHT_VERT` Bevel Weight – Transfer bevel weights.

    *   `COLOR_VERTEX` Colors – Color Attributes.

    *   `SHARP_EDGE` Sharp – Transfer sharp mark.

    *   `SEAM` UV Seam – Transfer UV seam mark.

    *   `CREASE` Subdivision Crease – Transfer crease values.

    *   `BEVEL_WEIGHT_EDGE` Bevel Weight – Transfer bevel weights.

    *   `FREESTYLE_EDGE` Freestyle Mark – Transfer Freestyle edge mark.

    *   `CUSTOM_NORMAL` Custom Normals – Transfer custom normals.

    *   `COLOR_CORNER` Colors – Color Attributes.

    *   `UV` UVs – Transfer UV layers.

    *   `SMOOTH` Smooth – Transfer flat/smooth mark.

    *   `FREESTYLE_FACE` Freestyle Mark – Transfer Freestyle face mark.

*   **use_delete** (_boolean_ _,_ _(_ _optional_ _)_) – Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source

*   **layers_select_src** (enum in [Dt Layers Select Src Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_layers_select_src_items.html#rna-enum-dt-layers-select-src-items), (optional)) – Source Layers Selection, Which layers to transfer, in case of multi-layers types

*   **layers_select_dst** (enum in [Dt Layers Select Dst Items](https://docs.blender.org/api/current/bpy_types_enum_items/dt_layers_select_dst_items.html#rna-enum-dt-layers-select-dst-items), (optional)) – Destination Layers Matching, How to match source and destination layers

bpy.ops.object.delete(_*_, _use\_global=False_, _confirm=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.delete "Link to this definition")
Delete selected objects

Parameters:
*   **use_global** (_boolean_ _,_ _(_ _optional_ _)_) – Delete Globally, Remove object from all scenes

*   **confirm** (_boolean_ _,_ _(_ _optional_ _)_) – Confirm, Prompt for confirmation

bpy.ops.object.delete_fix_to_camera_keys()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.delete_fix_to_camera_keys "Link to this definition")
Delete all keys that were generated by the ‘Fix to Scene Camera’ operator

File:
[startup/bl_operators/copy_global_transform.py:639](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L639)

bpy.ops.object.drop_geometry_nodes(_*_, _session\_uid=0_, _show\_datablock\_in\_modifier=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.drop_geometry_nodes "Link to this definition")
Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:
*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the geometry node group being dropped

*   **show_datablock_in_modifier** (_boolean_ _,_ _(_ _optional_ _)_) – Show the data-block selector in the modifier

bpy.ops.object.drop_named_material(_*_, _name=''_, _session\_uid=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.drop_named_material "Link to this definition")
Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:
*   **name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Name of the data-block to use by the operator

*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.object.duplicate(_*_, _linked=False_, _mode='TRANSLATION'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicate "Link to this definition")
Duplicate selected objects

Parameters:
*   **linked** (_boolean_ _,_ _(_ _optional_ _)_) – Linked, Duplicate object but not object data, linking to the original data

*   **mode** (enum in [Transform Mode Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/transform_mode_type_items.html#rna-enum-transform-mode-type-items), (optional)) – Mode

bpy.ops.object.duplicate_move(_*_, _OBJECT\_OT\_duplicate=None_, _TRANSFORM\_OT\_translate=None_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicate_move "Link to this definition")
Duplicate the selected objects and move them

Parameters:
*   **OBJECT_OT_duplicate** (`OBJECT_OT_duplicate`, (optional)) – Duplicate Objects, Duplicate selected objects

*   **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.object.duplicate_move_linked(_*_, _OBJECT\_OT\_duplicate=None_, _TRANSFORM\_OT\_translate=None_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicate_move_linked "Link to this definition")
Duplicate the selected objects, but not their object data, and move them

Parameters:
*   **OBJECT_OT_duplicate** (`OBJECT_OT_duplicate`, (optional)) – Duplicate Objects, Duplicate selected objects

*   **TRANSFORM_OT_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.object.duplicates_make_real(_*_, _use\_base\_parent=False_, _use\_hierarchy=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicates_make_real "Link to this definition")
Make instanced objects attached to this object real

Parameters:
*   **use_base_parent** (_boolean_ _,_ _(_ _optional_ _)_) – Parent, Parent newly created objects to the original instancer

*   **use_hierarchy** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Hierarchy, Maintain parent child relationships

bpy.ops.object.editmode_toggle()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.editmode_toggle "Link to this definition")
Toggle object’s edit mode

bpy.ops.object.effector_add(_*_, _type='FORCE'_, _radius=1.0_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.effector_add "Link to this definition")
Add an empty object with a physics effector to the scene

Parameters:
*   **type** (enum in [`'FORCE'`, `'WIND'`, `'VORTEX'`, `'MAGNET'`, `'HARMONIC'`, `'CHARGE'`, `'LENNARDJ'`, `'TEXTURE'`, `'GUIDE'`, `'BOID'`, `'TURBULENCE'`, `'DRAG'`, `'FLUID'`], (optional)) – Type

*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.empty_add(_*_, _type='PLAIN\_AXES'_, _radius=1.0_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.empty_add "Link to this definition")
Add an empty object to the scene

Parameters:
*   **type** (enum in [Object Empty Drawtype Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_empty_drawtype_items.html#rna-enum-object-empty-drawtype-items), (optional)) – Type

*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.empty_image_add(_*_, _filepath=''_, _hide\_props\_region=True_, _check\_existing=False_, _filter\_blender=False_, _filter\_backup=False_, _filter\_image=True_, _filter\_movie=True_, _filter\_python=False_, _filter\_font=False_, _filter\_sound=False_, _filter\_text=False_, _filter\_archive=False_, _filter\_btx=False_, _filter\_alembic=False_, _filter\_usd=False_, _filter\_obj=False_, _filter\_volume=False_, _filter\_folder=True_, _filter\_blenlib=False_, _filemode=9_, _relative\_path=True_, _show\_multiview=False_, _use\_multiview=False_, _display\_type='DEFAULT'_, _sort\_method=''_, _name=''_, _session\_uid=0_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_, _background=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.empty_image_add "Link to this definition")
Add an empty image type to scene with data

Parameters:
*   **filepath** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – File Path, Path to file

*   **hide_props_region** (_boolean_ _,_ _(_ _optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

*   **check_existing** (_boolean_ _,_ _(_ _optional_ _)_) – Check Existing, Check and warn on overwriting existing files

*   **filter_blender** (_boolean_ _,_ _(_ _optional_ _)_) – Filter .blend files

*   **filter_backup** (_boolean_ _,_ _(_ _optional_ _)_) – Filter .blend files

*   **filter_image** (_boolean_ _,_ _(_ _optional_ _)_) – Filter image files

*   **filter_movie** (_boolean_ _,_ _(_ _optional_ _)_) – Filter movie files

*   **filter_python** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Python files

*   **filter_font** (_boolean_ _,_ _(_ _optional_ _)_) – Filter font files

*   **filter_sound** (_boolean_ _,_ _(_ _optional_ _)_) – Filter sound files

*   **filter_text** (_boolean_ _,_ _(_ _optional_ _)_) – Filter text files

*   **filter_archive** (_boolean_ _,_ _(_ _optional_ _)_) – Filter archive files

*   **filter_btx** (_boolean_ _,_ _(_ _optional_ _)_) – Filter btx files

*   **filter_alembic** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Alembic files

*   **filter_usd** (_boolean_ _,_ _(_ _optional_ _)_) – Filter USD files

*   **filter_obj** (_boolean_ _,_ _(_ _optional_ _)_) – Filter OBJ files

*   **filter_volume** (_boolean_ _,_ _(_ _optional_ _)_) – Filter OpenVDB volume files

*   **filter_folder** (_boolean_ _,_ _(_ _optional_ _)_) – Filter folders

*   **filter_blenlib** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Blender IDs

*   **filemode** (_int in_ _[_ _1_ _,_ _9_ _]_ _,_ _(_ _optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

*   **relative_path** (_boolean_ _,_ _(_ _optional_ _)_) – Relative Path, Select the file relative to the blend file

*   **show_multiview** (_boolean_ _,_ _(_ _optional_ _)_) – Enable Multi-View

*   **use_multiview** (_boolean_ _,_ _(_ _optional_ _)_) – Use Multi-View

*   **display_type** (enum in [`'DEFAULT'`, `'LIST_VERTICAL'`, `'LIST_HORIZONTAL'`, `'THUMBNAIL'`], (optional)) –

Display Type

    *   `DEFAULT` Default – Automatically determine display type for files.

    *   `LIST_VERTICAL` Short List – Display files as short list.

    *   `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    *   `THUMBNAIL` Thumbnails – Display files as thumbnails.

*   **sort_method** (enum in [`'DEFAULT'`, `'FILE_SORT_ALPHA'`, `'FILE_SORT_EXTENSION'`, `'FILE_SORT_TIME'`, `'FILE_SORT_SIZE'`, `'ASSET_CATALOG'`], (optional)) –

File sorting mode

    *   `DEFAULT` Default – Automatically determine sort method for files.

    *   `FILE_SORT_ALPHA` Name – Sort the file list alphabetically.

    *   `FILE_SORT_EXTENSION` Extension – Sort the file list by extension/type.

    *   `FILE_SORT_TIME` Modified Date – Sort files by modification time.

    *   `FILE_SORT_SIZE` Size – Sort files by size.

    *   `ASSET_CATALOG` Asset Catalog – Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..

*   **name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Name of the data-block to use by the operator

*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

*   **background** (_boolean_ _,_ _(_ _optional_ _)_) – Put in Background, Make the image render behind all objects

bpy.ops.object.explode_refresh(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.explode_refresh "Link to this definition")
Refresh data in the Explode modifier

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.fix_to_camera(_*_, _use\_location=True_, _use\_rotation=True_, _use\_scale=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.fix_to_camera "Link to this definition")
Generate new keys to fix the selected object/bone to the camera on unkeyed frames

Parameters:
*   **use_location** (_boolean_ _,_ _(_ _optional_ _)_) – Location, Create Location keys when fixing to the scene camera

*   **use_rotation** (_boolean_ _,_ _(_ _optional_ _)_) – Rotation, Create Rotation keys when fixing to the scene camera

*   **use_scale** (_boolean_ _,_ _(_ _optional_ _)_) – Scale, Create Scale keys when fixing to the scene camera

File:
[startup/bl_operators/copy_global_transform.py:639](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L639)

bpy.ops.object.forcefield_toggle()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.forcefield_toggle "Link to this definition")
Toggle object’s force field

bpy.ops.object.geometry_node_bake_delete_single(_*_, _session\_uid=0_, _modifier\_name=''_, _bake\_id=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_delete_single "Link to this definition")
Delete baked data of a single bake node or simulation

Parameters:
*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **modifier_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier Name, Name of the modifier that contains the node

*   **bake_id** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Bake ID, Nested node id of the node

bpy.ops.object.geometry_node_bake_pack_single(_*_, _session\_uid=0_, _modifier\_name=''_, _bake\_id=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_pack_single "Link to this definition")
Pack baked data from disk into the .blend file

Parameters:
*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **modifier_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier Name, Name of the modifier that contains the node

*   **bake_id** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Bake ID, Nested node id of the node

bpy.ops.object.geometry_node_bake_single(_*_, _session\_uid=0_, _modifier\_name=''_, _bake\_id=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_single "Link to this definition")
Bake a single bake node or simulation

Parameters:
*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **modifier_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier Name, Name of the modifier that contains the node

*   **bake_id** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Bake ID, Nested node id of the node

bpy.ops.object.geometry_node_bake_unpack_single(_*_, _session\_uid=0_, _modifier\_name=''_, _bake\_id=0_, _method='USE\_LOCAL'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_unpack_single "Link to this definition")
Unpack baked data from the .blend file to disk

Parameters:
*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **modifier_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier Name, Name of the modifier that contains the node

*   **bake_id** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Bake ID, Nested node id of the node

*   **method** (enum in [`'USE_LOCAL'`, `'WRITE_LOCAL'`, `'USE_ORIGINAL'`, `'WRITE_ORIGINAL'`], (optional)) – Method, How to unpack

bpy.ops.object.geometry_node_tree_copy_assign()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_tree_copy_assign "Link to this definition")
Duplicate the active geometry node group and assign it to the active modifier

bpy.ops.object.geometry_nodes_input_attribute_toggle(_*_, _input\_name=''_, _modifier\_name=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_nodes_input_attribute_toggle "Link to this definition")
Switch between an attribute and a single value to define the data for every element

Parameters:
*   **input_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Input Name

*   **modifier_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier Name

bpy.ops.object.geometry_nodes_move_to_nodes(_*_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_nodes_move_to_nodes "Link to this definition")
Move inputs and outputs from in the modifier to a new node group

Parameters:
**use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

File:
[startup/bl_operators/geometry_nodes.py:280](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L280)

bpy.ops.object.grease_pencil_add(_*_, _type='EMPTY'_, _use\_in\_front=True_, _stroke\_depth\_offset=0.05_, _use\_lights=True_, _stroke\_depth\_order='3D'_, _radius=1.0_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_add "Link to this definition")
Add a Grease Pencil object to the scene

Parameters:
*   **type** (enum in [Object Gpencil Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_gpencil_type_items.html#rna-enum-object-gpencil-type-items), (optional)) – Type

*   **use_in_front** (_boolean_ _,_ _(_ _optional_ _)_) – Show In Front, Show Line Art Grease Pencil in front of everything

*   **stroke_depth_offset** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Stroke Offset, Stroke offset for the Line Art modifier

*   **use_lights** (_boolean_ _,_ _(_ _optional_ _)_) – Use Lights, Use lights for this Grease Pencil object

*   **stroke_depth_order** (enum in [`'2D'`, `'3D'`], (optional)) –

Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed ‘In Front’)

    *   `2D` 2D Layers – Display strokes using Grease Pencil layers to define order.

    *   `3D` 3D Location – Display strokes using real 3D position in 3D space.

*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.grease_pencil_dash_modifier_segment_add(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_dash_modifier_segment_add "Link to this definition")
Add a segment to the dash modifier

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.grease_pencil_dash_modifier_segment_move(_*_, _modifier=''_, _type='UP'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_dash_modifier_segment_move "Link to this definition")
Move the active dash segment up or down

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **type** (enum in [`'UP'`, `'DOWN'`], (optional)) – Type

bpy.ops.object.grease_pencil_dash_modifier_segment_remove(_*_, _modifier=''_, _index=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_dash_modifier_segment_remove "Link to this definition")
Remove the active segment from the dash modifier

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **index** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Index, Index of the segment to remove

bpy.ops.object.grease_pencil_time_modifier_segment_add(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_time_modifier_segment_add "Link to this definition")
Add a segment to the time modifier

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.grease_pencil_time_modifier_segment_move(_*_, _modifier=''_, _type='UP'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_time_modifier_segment_move "Link to this definition")
Move the active time segment up or down

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **type** (enum in [`'UP'`, `'DOWN'`], (optional)) – Type

bpy.ops.object.grease_pencil_time_modifier_segment_remove(_*_, _modifier=''_, _index=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_time_modifier_segment_remove "Link to this definition")
Remove the active segment from the time modifier

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **index** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Index, Index of the segment to remove

bpy.ops.object.hide_collection(_*_, _collection\_index=-1_, _toggle=False_, _extend=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_collection "Link to this definition")
Show only objects in collection (Shift to extend)

Parameters:
*   **collection_index** (_int in_ _[_ _-1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Collection Index, Index of the collection to change visibility

*   **toggle** (_boolean_ _,_ _(_ _optional_ _)_) – Toggle, Toggle visibility

*   **extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend visibility

bpy.ops.object.hide_render_clear_all()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_render_clear_all "Link to this definition")
Reveal all render objects by setting the hide render flag

File:
[startup/bl_operators/object.py:729](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L729)

bpy.ops.object.hide_view_clear(_*_, _select=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_view_clear "Link to this definition")
Reveal temporarily hidden objects

Parameters:
**select** (_boolean_ _,_ _(_ _optional_ _)_) – Select, Select revealed objects

bpy.ops.object.hide_view_set(_*_, _unselected=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_view_set "Link to this definition")
Temporarily hide objects from the viewport

Parameters:
**unselected** (_boolean_ _,_ _(_ _optional_ _)_) – Unselected, Hide unselected rather than selected objects

bpy.ops.object.hook_add_newob()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_add_newob "Link to this definition")
Hook selected vertices to a newly created object

bpy.ops.object.hook_add_selob(_*_, _use\_bone=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_add_selob "Link to this definition")
Hook selected vertices to the first selected object

Parameters:
**use_bone** (_boolean_ _,_ _(_ _optional_ _)_) – Active Bone, Assign the hook to the hook object’s active bone

bpy.ops.object.hook_assign(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_assign "Link to this definition")
Assign the selected vertices to a hook

Parameters:
**modifier** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Modifier, Modifier number to assign to

bpy.ops.object.hook_recenter(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_recenter "Link to this definition")
Set hook center to cursor position

Parameters:
**modifier** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Modifier, Modifier number to assign to

bpy.ops.object.hook_remove(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_remove "Link to this definition")
Remove a hook from the active object

Parameters:
**modifier** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Modifier, Modifier number to remove

bpy.ops.object.hook_reset(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_reset "Link to this definition")
Recalculate and clear offset transformation

Parameters:
**modifier** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Modifier, Modifier number to assign to

bpy.ops.object.hook_select(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_select "Link to this definition")
Select affected vertices on mesh

Parameters:
**modifier** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Modifier, Modifier number to remove

bpy.ops.object.instance_offset_from_cursor()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.instance_offset_from_cursor "Link to this definition")
Set offset used for collection instances based on cursor position

File:
[startup/bl_operators/object.py:914](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L914)

bpy.ops.object.instance_offset_from_object()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.instance_offset_from_object "Link to this definition")
Set offset used for collection instances based on the active object position

File:
[startup/bl_operators/object.py:946](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L946)

bpy.ops.object.instance_offset_to_cursor()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.instance_offset_to_cursor "Link to this definition")
Set cursor position to the offset used for collection instances

File:
[startup/bl_operators/object.py:929](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L929)

bpy.ops.object.isolate_type_render()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.isolate_type_render "Link to this definition")
Hide unselected render objects of same type as active by setting the hide render flag

File:
[startup/bl_operators/object.py:709](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L709)

bpy.ops.object.join()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.join "Link to this definition")
Join selected objects into active object

bpy.ops.object.join_shapes(_*_, _use\_mirror=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.join_shapes "Link to this definition")
Add the vertex positions of selected objects as shape keys or update existing shape keys with matching names

Parameters:
**use_mirror** (_boolean_ _,_ _(_ _optional_ _)_) – Mirror, Mirror the new shape key values

bpy.ops.object.join_uvs()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.join_uvs "Link to this definition")
Transfer UV Maps from active to selected objects (needs matching geometry)

File:
[startup/bl_operators/object.py:610](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L610)

bpy.ops.object.laplaciandeform_bind(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.laplaciandeform_bind "Link to this definition")
Bind mesh to system in laplacian deform modifier

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.lattice_add_to_selected(_*_, _fit\_to\_selected=True_, _radius=1.0_, _margin=0.0_, _add\_modifiers=True_, _resolution\_u=2_, _resolution\_v=2_, _resolution\_w=2_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lattice_add_to_selected "Link to this definition")
Add a lattice and use it to deform selected objects

Parameters:
*   **fit_to_selected** (_boolean_ _,_ _(_ _optional_ _)_) – Fit to Selected, Resize lattice to fit selected deformable objects

*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **margin** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Margin, Add margin to lattice dimensions

*   **add_modifiers** (_boolean_ _,_ _(_ _optional_ _)_) – Add Modifiers, Automatically add lattice modifiers to selected objects

*   **resolution_u** (_int in_ _[_ _1_ _,_ _64_ _]_ _,_ _(_ _optional_ _)_) – Resolution U, Lattice resolution in U direction

*   **resolution_v** (_int in_ _[_ _1_ _,_ _64_ _]_ _,_ _(_ _optional_ _)_) – V, Lattice resolution in V direction

*   **resolution_w** (_int in_ _[_ _1_ _,_ _64_ _]_ _,_ _(_ _optional_ _)_) – W, Lattice resolution in W direction

*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.light_add(_*_, _type='POINT'_, _radius=1.0_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_add "Link to this definition")
Add a light object to the scene

Parameters:
*   **type** (enum in [Light Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/light_type_items.html#rna-enum-light-type-items), (optional)) – Type

*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.light_linking_blocker_collection_new()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_blocker_collection_new "Link to this definition")
Create new light linking collection used by the active emitter

bpy.ops.object.light_linking_blockers_link(_*_, _link\_state='INCLUDE'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_blockers_link "Link to this definition")
Light link selected blockers to the active emitter object

Parameters:
**link_state** (enum in [`'INCLUDE'`, `'EXCLUDE'`], (optional)) –

Link State, State of the shadow linking

*   `INCLUDE` Include – Include selected blockers to cast shadows from the active emitter.

*   `EXCLUDE` Exclude – Exclude selected blockers from casting shadows from the active emitter.

bpy.ops.object.light_linking_blockers_select()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_blockers_select "Link to this definition")
Select all objects which block light from this emitter

bpy.ops.object.light_linking_receiver_collection_new()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_receiver_collection_new "Link to this definition")
Create new light linking collection used by the active emitter

bpy.ops.object.light_linking_receivers_link(_*_, _link\_state='INCLUDE'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_receivers_link "Link to this definition")
Light link selected receivers to the active emitter object

Parameters:
**link_state** (enum in [`'INCLUDE'`, `'EXCLUDE'`], (optional)) –

Link State, State of the light linking

*   `INCLUDE` Include – Include selected receivers to receive light from the active emitter.

*   `EXCLUDE` Exclude – Exclude selected receivers from receiving light from the active emitter.

bpy.ops.object.light_linking_receivers_select()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_receivers_select "Link to this definition")
Select all objects which receive light from this emitter

bpy.ops.object.light_linking_unlink_from_collection()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_unlink_from_collection "Link to this definition")
Remove this object or collection from the light linking collection

bpy.ops.object.lightprobe_add(_*_, _type='SPHERE'_, _radius=1.0_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lightprobe_add "Link to this definition")
Add a light probe object

Parameters:
*   **type** (enum in [`'SPHERE'`, `'PLANE'`, `'VOLUME'`], (optional)) –

Type

    *   `SPHERE` Sphere – Light probe that captures precise lighting from all directions at a single point in space.

    *   `PLANE` Plane – Light probe that captures incoming light from a single direction on a plane.

    *   `VOLUME` Volume – Light probe that captures low frequency lighting inside a volume.

*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.lightprobe_cache_bake(_*_, _subset='ALL'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lightprobe_cache_bake "Link to this definition")
Bake irradiance volume light cache

Parameters:
**subset** (enum in [`'ALL'`, `'SELECTED'`, `'ACTIVE'`], (optional)) –

Subset, Subset of probes to update

*   `ALL` All Volumes – Bake all light probe volumes.

*   `SELECTED` Selected Only – Only bake selected light probe volumes.

*   `ACTIVE` Active Only – Only bake the active light probe volume.

bpy.ops.object.lightprobe_cache_free(_*_, _subset='SELECTED'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lightprobe_cache_free "Link to this definition")
Delete cached indirect lighting

Parameters:
**subset** (enum in [`'ALL'`, `'SELECTED'`, `'ACTIVE'`], (optional)) –

Subset, Subset of probes to update

*   `ALL` All Light Probes – Delete all light probes’ baked lighting data.

*   `SELECTED` Selected Only – Only delete selected light probes’ baked lighting data.

*   `ACTIVE` Active Only – Only delete the active light probe’s baked lighting data.

bpy.ops.object.lineart_bake_strokes(_*_, _bake\_all=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lineart_bake_strokes "Link to this definition")
Bake Line Art for current Grease Pencil object

Parameters:
**bake_all** (_boolean_ _,_ _(_ _optional_ _)_) – Bake All, Bake all Line Art modifiers

bpy.ops.object.lineart_clear(_*_, _clear\_all=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lineart_clear "Link to this definition")
Clear all strokes in current Grease Pencil object

Parameters:
**clear_all** (_boolean_ _,_ _(_ _optional_ _)_) – Clear All, Clear all Line Art modifier bakes

bpy.ops.object.link_to_collection(_*_, _collection\_uid=-1_, _is\_new=False_, _new\_collection\_name=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.link_to_collection "Link to this definition")
Link objects to a collection

Parameters:
*   **collection_uid** (_int in_ _[_ _-1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Collection UID, Session UID of the collection to link to

*   **is_new** (_boolean_ _,_ _(_ _optional_ _)_) – New, Link objects to a new collection

*   **new_collection_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Name of the newly added collection

bpy.ops.object.location_clear(_*_, _clear\_delta=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.location_clear "Link to this definition")
Clear the object’s location

Parameters:
**clear_delta** (_boolean_ _,_ _(_ _optional_ _)_) – Clear Delta, Clear delta location in addition to clearing the normal location transform

bpy.ops.object.make_dupli_face()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_dupli_face "Link to this definition")
Convert objects into instanced faces

File:
[startup/bl_operators/object.py:692](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L692)

bpy.ops.object.make_links_data(_*_, _type='OBDATA'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_links_data "Link to this definition")
Transfer data from active object to selected objects

Parameters:
**type** (enum in [`'OBDATA'`, `'MATERIAL'`, `'ANIMATION'`, `'GROUPS'`, `'DUPLICOLLECTION'`, `'FONTS'`, `'MODIFIERS'`, `'EFFECTS'`], (optional)) –

Type

*   `OBDATA` Link Object Data – Replace assigned Object Data.

*   `MATERIAL` Link Materials – Replace assigned Materials.

*   `ANIMATION` Link Animation Data – Replace assigned Animation Data.

*   `GROUPS` Link Collections – Replace assigned Collections.

*   `DUPLICOLLECTION` Link Instance Collection – Replace assigned Collection Instance.

*   `FONTS` Link Fonts to Text – Replace Text object Fonts.

*   `MODIFIERS` Copy Modifiers – Replace Modifiers.

*   `EFFECTS` Copy Grease Pencil Effects – Replace Grease Pencil Effects.

bpy.ops.object.make_links_scene(_*_, _scene=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_links_scene "Link to this definition")
Link selection to another scene

Parameters:
**scene** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Scene

bpy.ops.object.make_local(_*_, _type='SELECT\_OBJECT'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_local "Link to this definition")
Make library linked data-blocks local to this file

Parameters:
**type** (enum in [`'SELECT_OBJECT'`, `'SELECT_OBDATA'`, `'SELECT_OBDATA_MATERIAL'`, `'ALL'`], (optional)) – Type

bpy.ops.object.make_override_library(_*_, _collection=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_override_library "Link to this definition")
Create a local override of the selected linked objects, and their hierarchy of dependencies

Parameters:
**collection** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Override Collection, Session UID of the directly linked collection containing the selected object, to make an override from

bpy.ops.object.make_single_user(_*_, _type='SELECTED\_OBJECTS'_, _object=False_, _obdata=False_, _material=False_, _animation=False_, _obdata\_animation=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_single_user "Link to this definition")
Make linked data local to each object

Parameters:
*   **type** (enum in [`'SELECTED_OBJECTS'`, `'ALL'`], (optional)) – Type

*   **object** (_boolean_ _,_ _(_ _optional_ _)_) – Object, Make single user objects

*   **obdata** (_boolean_ _,_ _(_ _optional_ _)_) – Object Data, Make single user object data

*   **material** (_boolean_ _,_ _(_ _optional_ _)_) – Materials, Make materials local to each data-block

*   **animation** (_boolean_ _,_ _(_ _optional_ _)_) – Object Animation, Make object animation data local to each object

*   **obdata_animation** (_boolean_ _,_ _(_ _optional_ _)_) – Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object

bpy.ops.object.material_slot_add()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_add "Link to this definition")
Add a new material slot

bpy.ops.object.material_slot_assign()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_assign "Link to this definition")
Assign active material slot to selection

bpy.ops.object.material_slot_copy()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_copy "Link to this definition")
Copy material to selected objects

bpy.ops.object.material_slot_deselect()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_deselect "Link to this definition")
Deselect by active material slot

bpy.ops.object.material_slot_move(_*_, _direction='UP'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_move "Link to this definition")
Move the active material up/down in the list

Parameters:
**direction** (enum in [`'UP'`, `'DOWN'`], (optional)) – Direction, Direction to move the active material towards

bpy.ops.object.material_slot_remove()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_remove "Link to this definition")
Remove the selected material slot

bpy.ops.object.material_slot_remove_all()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_remove_all "Link to this definition")
Remove all materials

bpy.ops.object.material_slot_remove_unused()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_remove_unused "Link to this definition")
Remove unused material slots

bpy.ops.object.material_slot_select()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_select "Link to this definition")
Select by active material slot

bpy.ops.object.meshdeform_bind(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.meshdeform_bind "Link to this definition")
Bind mesh to cage in mesh deform modifier

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.metaball_add(_*_, _type='BALL'_, _radius=2.0_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.metaball_add "Link to this definition")
Add an metaball object to the scene

Parameters:
*   **type** (enum in [Metaelem Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/metaelem_type_items.html#rna-enum-metaelem-type-items), (optional)) – Primitive

*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.mode_set(_*_, _mode='OBJECT'_, _toggle=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.mode_set "Link to this definition")
Sets the object interaction mode

Parameters:
*   **mode** (enum in [Object Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_mode_items.html#rna-enum-object-mode-items), (optional)) – Mode

*   **toggle** (_boolean_ _,_ _(_ _optional_ _)_) – Toggle

bpy.ops.object.mode_set_with_submode(_*_, _mode='OBJECT'_, _toggle=False_, _mesh\_select\_mode={}_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.mode_set_with_submode "Link to this definition")
Sets the object interaction mode

Parameters:
*   **mode** (enum in [Object Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_mode_items.html#rna-enum-object-mode-items), (optional)) – Mode

*   **toggle** (_boolean_ _,_ _(_ _optional_ _)_) – Toggle

*   **mesh_select_mode** (enum set in [Mesh Select Mode Items](https://docs.blender.org/api/current/bpy_types_enum_items/mesh_select_mode_items.html#rna-enum-mesh-select-mode-items), (optional)) – Mesh Mode

bpy.ops.object.modifier_add(_*_, _type='SUBSURF'_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_add "Link to this definition")
Add a procedural operation/effect to the active object

Parameters:
*   **type** (enum in [Object Modifier Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_modifier_type_items.html#rna-enum-object-modifier-type-items), (optional)) – Type

*   **use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_add_node_group(_*_, _asset\_library\_type='LOCAL'_, _asset\_library\_identifier=''_, _relative\_asset\_identifier=''_, _session\_uid=0_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_add_node_group "Link to this definition")
Add a procedural operation/effect to the active object

Parameters:
*   **asset_library_type** (enum in [Asset Library Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/asset_library_type_items.html#rna-enum-asset-library-type-items), (optional)) – Asset Library Type

*   **asset_library_identifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Asset Library Identifier

*   **relative_asset_identifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Relative Asset Identifier

*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UID, Session UID of the data-block to use by the operator

*   **use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_apply(_*_, _modifier=''_, _report=False_, _merge\_customdata=True_, _single\_user=False_, _all\_keyframes=False_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_apply "Link to this definition")
Apply modifier and remove from the stack

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **report** (_boolean_ _,_ _(_ _optional_ _)_) – Report, Create a notification after the operation

*   **merge_customdata** (_boolean_ _,_ _(_ _optional_ _)_) – Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers

*   **single_user** (_boolean_ _,_ _(_ _optional_ _)_) – Make Data Single User, Make the object’s data single user if needed

*   **all_keyframes** (_boolean_ _,_ _(_ _optional_ _)_) – Apply to all keyframes, For Grease Pencil objects, apply the modifier to all the keyframes

*   **use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_apply_as_shapekey(_*_, _keep\_modifier=False_, _modifier=''_, _report=False_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_apply_as_shapekey "Link to this definition")
Apply modifier as a new shape key and remove from the stack

Parameters:
*   **keep_modifier** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Modifier, Do not remove the modifier from stack

*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **report** (_boolean_ _,_ _(_ _optional_ _)_) – Report, Create a notification after the operation

*   **use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_convert(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_convert "Link to this definition")
Convert particles to a mesh object

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.modifier_copy(_*_, _modifier=''_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_copy "Link to this definition")
Duplicate modifier at the same position in the stack

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_copy_to_selected(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_copy_to_selected "Link to this definition")
Copy the modifier from the active object to all selected objects

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.modifier_move_down(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_move_down "Link to this definition")
Move modifier down in the stack

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.modifier_move_to_index(_*_, _modifier=''_, _index=0_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_move_to_index "Link to this definition")
Change the modifier’s index in the stack so it evaluates after the set number of others

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **index** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Index, The index to move the modifier to

*   **use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_move_up(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_move_up "Link to this definition")
Move modifier up in the stack

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.modifier_remove(_*_, _modifier=''_, _report=False_, _use\_selected\_objects=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_remove "Link to this definition")
Remove a modifier from the active object

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **report** (_boolean_ _,_ _(_ _optional_ _)_) – Report, Create a notification after the operation

*   **use_selected_objects** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Affect all selected objects instead of just the active object

bpy.ops.object.modifier_set_active(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_set_active "Link to this definition")
Activate the modifier to use as the context

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.modifiers_clear()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifiers_clear "Link to this definition")
Clear all modifiers from the selected objects

bpy.ops.object.modifiers_copy_to_selected()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifiers_copy_to_selected "Link to this definition")
Copy modifiers to other selected objects

bpy.ops.object.move_to_collection(_*_, _collection\_uid=-1_, _is\_new=False_, _new\_collection\_name=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.move_to_collection "Link to this definition")
Move objects to a collection

Parameters:
*   **collection_uid** (_int in_ _[_ _-1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Collection UID, Session UID of the collection to move to

*   **is_new** (_boolean_ _,_ _(_ _optional_ _)_) – New, Move objects to a new collection

*   **new_collection_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Name of the newly added collection

bpy.ops.object.multires_base_apply(_*_, _modifier=''_, _apply\_heuristic=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_base_apply "Link to this definition")
Modify the base mesh to conform to the displaced mesh

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **apply_heuristic** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Subdivision Heuristic, Whether or not the final base mesh positions will be slightly altered to account for a new subdivision modifier being added

bpy.ops.object.multires_external_pack()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_external_pack "Link to this definition")
Pack displacements from an external file

bpy.ops.object.multires_external_save(_*_, _filepath=''_, _hide\_props\_region=True_, _check\_existing=True_, _filter\_blender=False_, _filter\_backup=False_, _filter\_image=False_, _filter\_movie=False_, _filter\_python=False_, _filter\_font=False_, _filter\_sound=False_, _filter\_text=False_, _filter\_archive=False_, _filter\_btx=True_, _filter\_alembic=False_, _filter\_usd=False_, _filter\_obj=False_, _filter\_volume=False_, _filter\_folder=True_, _filter\_blenlib=False_, _filemode=9_, _relative\_path=True_, _display\_type='DEFAULT'_, _sort\_method=''_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_external_save "Link to this definition")
Save displacements to an external file

Parameters:
*   **filepath** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – File Path, Path to file

*   **hide_props_region** (_boolean_ _,_ _(_ _optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

*   **check_existing** (_boolean_ _,_ _(_ _optional_ _)_) – Check Existing, Check and warn on overwriting existing files

*   **filter_blender** (_boolean_ _,_ _(_ _optional_ _)_) – Filter .blend files

*   **filter_backup** (_boolean_ _,_ _(_ _optional_ _)_) – Filter .blend files

*   **filter_image** (_boolean_ _,_ _(_ _optional_ _)_) – Filter image files

*   **filter_movie** (_boolean_ _,_ _(_ _optional_ _)_) – Filter movie files

*   **filter_python** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Python files

*   **filter_font** (_boolean_ _,_ _(_ _optional_ _)_) – Filter font files

*   **filter_sound** (_boolean_ _,_ _(_ _optional_ _)_) – Filter sound files

*   **filter_text** (_boolean_ _,_ _(_ _optional_ _)_) – Filter text files

*   **filter_archive** (_boolean_ _,_ _(_ _optional_ _)_) – Filter archive files

*   **filter_btx** (_boolean_ _,_ _(_ _optional_ _)_) – Filter btx files

*   **filter_alembic** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Alembic files

*   **filter_usd** (_boolean_ _,_ _(_ _optional_ _)_) – Filter USD files

*   **filter_obj** (_boolean_ _,_ _(_ _optional_ _)_) – Filter OBJ files

*   **filter_volume** (_boolean_ _,_ _(_ _optional_ _)_) – Filter OpenVDB volume files

*   **filter_folder** (_boolean_ _,_ _(_ _optional_ _)_) – Filter folders

*   **filter_blenlib** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Blender IDs

*   **filemode** (_int in_ _[_ _1_ _,_ _9_ _]_ _,_ _(_ _optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

*   **relative_path** (_boolean_ _,_ _(_ _optional_ _)_) – Relative Path, Select the file relative to the blend file

*   **display_type** (enum in [`'DEFAULT'`, `'LIST_VERTICAL'`, `'LIST_HORIZONTAL'`, `'THUMBNAIL'`], (optional)) –

Display Type

    *   `DEFAULT` Default – Automatically determine display type for files.

    *   `LIST_VERTICAL` Short List – Display files as short list.

    *   `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    *   `THUMBNAIL` Thumbnails – Display files as thumbnails.

*   **sort_method** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – File sorting mode

*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.multires_higher_levels_delete(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_higher_levels_delete "Link to this definition")
Deletes the higher resolution mesh, potential loss of detail

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.multires_rebuild_subdiv(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_rebuild_subdiv "Link to this definition")
Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.multires_reshape(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_reshape "Link to this definition")
Copy vertex coordinates from other object

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.multires_subdivide(_*_, _modifier=''_, _mode='CATMULL\_CLARK'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_subdivide "Link to this definition")
Add a new level of subdivision

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **mode** (enum in [`'CATMULL_CLARK'`, `'SIMPLE'`, `'LINEAR'`], (optional)) –

Subdivision Mode, How the mesh is going to be subdivided to create a new level

    *   `CATMULL_CLARK` Catmull-Clark – Create a new level using Catmull-Clark subdivisions.

    *   `SIMPLE` Simple – Create a new level using simple subdivisions.

    *   `LINEAR` Linear – Create a new level using linear interpolation of the sculpted displacement.

bpy.ops.object.multires_unsubdivide(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_unsubdivide "Link to this definition")
Rebuild a lower subdivision level of the current base mesh

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.ocean_bake(_*_, _modifier=''_, _free=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.ocean_bake "Link to this definition")
Bake an image sequence of ocean data

Parameters:
*   **modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

*   **free** (_boolean_ _,_ _(_ _optional_ _)_) – Free, Free the bake, rather than generating it

bpy.ops.object.origin_clear()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.origin_clear "Link to this definition")
Clear the object’s origin

bpy.ops.object.origin_set(_*_, _type='GEOMETRY\_ORIGIN'_, _center='MEDIAN'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.origin_set "Link to this definition")
Set the object’s origin, by either moving the data, or set to center of data, or use 3D cursor

Parameters:
*   **type** (enum in [`'GEOMETRY_ORIGIN'`, `'ORIGIN_GEOMETRY'`, `'ORIGIN_CURSOR'`, `'ORIGIN_CENTER_OF_MASS'`, `'ORIGIN_CENTER_OF_VOLUME'`], (optional)) –

Type

    *   `GEOMETRY_ORIGIN` Geometry to Origin – Move object geometry to object origin.

    *   `ORIGIN_GEOMETRY` Origin to Geometry – Calculate the center of geometry based on the current pivot point (median, otherwise bounding box).

    *   `ORIGIN_CURSOR` Origin to 3D Cursor – Move object origin to position of the 3D cursor.

    *   `ORIGIN_CENTER_OF_MASS` Origin to Center of Mass (Surface) – Calculate the center of mass from the surface area.

    *   `ORIGIN_CENTER_OF_VOLUME` Origin to Center of Mass (Volume) – Calculate the center of mass from the volume (must be manifold geometry with consistent normals).

*   **center** (enum in [`'MEDIAN'`, `'BOUNDS'`], (optional)) – Center

bpy.ops.object.parent_clear(_*_, _type='CLEAR'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_clear "Link to this definition")
Clear the object’s parenting

Parameters:
**type** (enum in [`'CLEAR'`, `'CLEAR_KEEP_TRANSFORM'`, `'CLEAR_INVERSE'`], (optional)) –

Type

*   `CLEAR` Clear Parent – Completely clear the parenting relationship, including involved modifiers if any.

*   `CLEAR_KEEP_TRANSFORM` Clear and Keep Transformation – As ‘Clear Parent’, but keep the current visual transformations of the object.

*   `CLEAR_INVERSE` Clear Parent Inverse – Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.

bpy.ops.object.parent_inverse_apply()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_inverse_apply "Link to this definition")
Apply the object’s parent inverse to its data

bpy.ops.object.parent_no_inverse_set(_*_, _keep\_transform=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_no_inverse_set "Link to this definition")
Set the object’s parenting without setting the inverse parent correction

Parameters:
**keep_transform** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Transform, Preserve the world transform throughout parenting

bpy.ops.object.parent_set(_*_, _type='OBJECT'_, _xmirror=False_, _keep\_transform=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_set "Link to this definition")
Set the object’s parenting

Parameters:
*   **type** (enum in [`'OBJECT'`, `'ARMATURE'`, `'ARMATURE_NAME'`, `'ARMATURE_AUTO'`, `'ARMATURE_ENVELOPE'`, `'BONE'`, `'BONE_RELATIVE'`, `'CURVE'`, `'FOLLOW'`, `'PATH_CONST'`, `'LATTICE'`, `'VERTEX'`, `'VERTEX_TRI'`], (optional)) – Type

*   **xmirror** (_boolean_ _,_ _(_ _optional_ _)_) – X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation

*   **keep_transform** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Transform, Apply transformation before parenting

bpy.ops.object.particle_system_add()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.particle_system_add "Link to this definition")
Add a particle system

bpy.ops.object.particle_system_remove()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.particle_system_remove "Link to this definition")
Remove the selected particle system

bpy.ops.object.paste_transform(_*_, _method='CURRENT'_, _bake\_step=0_, _use\_mirror=False_, _mirror\_axis\_loc='x'_, _mirror\_axis\_rot='z'_, _use\_relative=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paste_transform "Link to this definition")
Pastes the matrix from the clipboard to the currently active pose bone or object. Uses world-space matrices

Parameters:
*   **method** (enum in [`'CURRENT'`, `'EXISTING_KEYS'`, `'BAKE'`], (optional)) –

Paste Method, Update the current transform, selected keyframes, or even create new keys

    *   `CURRENT` Current Transform – Paste onto the current values only, only manipulating the animation data if auto-keying is enabled.

    *   `EXISTING_KEYS` Selected Keys – Paste onto frames that have a selected key, potentially creating new keys on those frames.

    *   `BAKE` Bake on Key Range – Paste onto all frames between the first and last selected key, creating new keyframes if necessary.

*   **bake_step** (_int in_ _[_ _1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Frame Step, Only used for baking. Step=1 creates a key on every frame, step=2 bakes on 2s, etc

*   **use_mirror** (_boolean_ _,_ _(_ _optional_ _)_) – Mirror Transform, When pasting, mirror the transform relative to a specific object or bone

*   **mirror_axis_loc** (enum in [`'x'`, `'y'`, `'z'`], (optional)) – Location Axis, Coordinate axis used to mirror the location part of the transform

*   **mirror_axis_rot** (enum in [`'x'`, `'y'`, `'z'`], (optional)) – Rotation Axis, Coordinate axis used to mirror the rotation part of the transform

*   **use_relative** (_boolean_ _,_ _(_ _optional_ _)_) – Use Relative Paste, When pasting, assume the pasted matrix is relative to another object (set in the user interface)

File:
[startup/bl_operators/copy_global_transform.py:325](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L325)

bpy.ops.object.paths_calculate(_*_, _display\_type='RANGE'_, _range='SCENE'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_calculate "Link to this definition")
Generate motion paths for the selected objects

Parameters:
*   **display_type** (enum in [Motionpath Display Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/motionpath_display_type_items.html#rna-enum-motionpath-display-type-items), (optional)) – Display Type

*   **range** (enum in [Motionpath Range Items](https://docs.blender.org/api/current/bpy_types_enum_items/motionpath_range_items.html#rna-enum-motionpath-range-items), (optional)) – Computation Range

bpy.ops.object.paths_clear(_*_, _only\_selected=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_clear "Link to this definition")
Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:
**only_selected** (_boolean_ _,_ _(_ _optional_ _)_) – Only Selected, Only clear motion paths of selected objects

bpy.ops.object.paths_update()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_update "Link to this definition")
Recalculate motion paths for selected objects

bpy.ops.object.paths_update_visible()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_update_visible "Link to this definition")
Recalculate all visible motion paths for objects and poses

bpy.ops.object.pointcloud_random_add(_*_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.pointcloud_random_add "Link to this definition")
Add a point cloud object to the scene

Parameters:
*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.posemode_toggle()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.posemode_toggle "Link to this definition")
Enable or disable posing/selecting bones

bpy.ops.object.quadriflow_remesh(_*_, _use\_mesh\_symmetry=True_, _use\_preserve\_sharp=False_, _use\_preserve\_boundary=False_, _preserve\_attributes=False_, _smooth\_normals=False_, _mode='FACES'_, _target\_ratio=1.0_, _target\_edge\_length=0.1_, _target\_faces=4000_, _mesh\_area=-1.0_, _seed=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quadriflow_remesh "Link to this definition")
Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

Parameters:
*   **use_mesh_symmetry** (_boolean_ _,_ _(_ _optional_ _)_) – Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration

*   **use_preserve_sharp** (_boolean_ _,_ _(_ _optional_ _)_) – Preserve Sharp, Try to preserve sharp features on the mesh

*   **use_preserve_boundary** (_boolean_ _,_ _(_ _optional_ _)_) – Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh

*   **preserve_attributes** (_boolean_ _,_ _(_ _optional_ _)_) – Preserve Attributes, Reproject attributes onto the new mesh

*   **smooth_normals** (_boolean_ _,_ _(_ _optional_ _)_) – Smooth Normals, Set the output mesh normals to smooth

*   **mode** (enum in [`'RATIO'`, `'EDGE'`, `'FACES'`], (optional)) –

Mode, How to specify the amount of detail for the new mesh

    *   `RATIO` Ratio – Specify target number of faces relative to the current mesh.

    *   `EDGE` Edge Length – Input target edge length in the new mesh.

    *   `FACES` Faces – Input target number of faces in the new mesh.

*   **target_ratio** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Ratio, Relative number of faces compared to the current mesh

*   **target_edge_length** (_float in_ _[_ _1e-07_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Edge Length, Target edge length in the new mesh

*   **target_faces** (_int in_ _[_ _1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Number of Faces, Approximate number of faces (quads) in the new mesh

*   **mesh_area** (_float in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Old Object Face Area, This property is only used to cache the object area for later calculations

*   **seed** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh

bpy.ops.object.quick_explode(_*_, _style='EXPLODE'_, _amount=100_, _frame\_duration=50_, _frame\_start=1_, _frame\_end=10_, _velocity=1.0_, _fade=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_explode "Link to this definition")
Make selected objects explode

Parameters:
*   **style** (enum in [`'EXPLODE'`, `'BLEND'`], (optional)) – Explode Style

*   **amount** (_int in_ _[_ _2_ _,_ _10000_ _]_ _,_ _(_ _optional_ _)_) – Number of Pieces

*   **frame_duration** (_int in_ _[_ _1_ _,_ _300000_ _]_ _,_ _(_ _optional_ _)_) – Duration

*   **frame_start** (_int in_ _[_ _1_ _,_ _300000_ _]_ _,_ _(_ _optional_ _)_) – Start Frame

*   **frame_end** (_int in_ _[_ _1_ _,_ _300000_ _]_ _,_ _(_ _optional_ _)_) – End Frame

*   **velocity** (_float in_ _[_ _0_ _,_ _300000_ _]_ _,_ _(_ _optional_ _)_) – Outwards Velocity

*   **fade** (_boolean_ _,_ _(_ _optional_ _)_) – Fade, Fade the pieces over time

File:
[startup/bl_operators/object_quick_effects.py:273](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L273)

bpy.ops.object.quick_fur(_*_, _density='MEDIUM'_, _length=0.1_, _radius=0.001_, _view\_percentage=1.0_, _apply\_hair\_guides=True_, _use\_noise=True_, _use\_frizz=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_fur "Link to this definition")
Add a fur setup to the selected objects

Parameters:
*   **density** (enum in [`'LOW'`, `'MEDIUM'`, `'HIGH'`], (optional)) – Density

*   **length** (_float in_ _[_ _0.001_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – Length

*   **radius** (_float in_ _[_ _0_ _,_ _10_ _]_ _,_ _(_ _optional_ _)_) – Hair Radius

*   **view_percentage** (_float in_ _[_ _0_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – View Percentage

*   **apply_hair_guides** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Hair Guides

*   **use_noise** (_boolean_ _,_ _(_ _optional_ _)_) – Noise

*   **use_frizz** (_boolean_ _,_ _(_ _optional_ _)_) – Frizz

File:
[startup/bl_operators/object_quick_effects.py:92](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L92)

bpy.ops.object.quick_liquid(_*_, _show\_flows=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_liquid "Link to this definition")
Make selected objects liquid

Parameters:
**show_flows** (_boolean_ _,_ _(_ _optional_ _)_) – Render Liquid Objects, Keep the liquid objects visible during rendering

File:
[startup/bl_operators/object_quick_effects.py:553](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L553)

bpy.ops.object.quick_smoke(_*_, _style='SMOKE'_, _show\_flows=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_smoke "Link to this definition")
Use selected objects as smoke emitters

Parameters:
*   **style** (enum in [`'SMOKE'`, `'FIRE'`, `'BOTH'`], (optional)) – Smoke Style

*   **show_flows** (_boolean_ _,_ _(_ _optional_ _)_) – Render Smoke Objects, Keep the smoke objects visible during rendering

File:
[startup/bl_operators/object_quick_effects.py:447](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L447)

bpy.ops.object.randomize_transform(_*_, _random\_seed=0_, _use\_delta=False_, _use\_loc=True_, _loc=(0.0,0.0,0.0)_, _use\_rot=True_, _rot=(0.0,0.0,0.0)_, _use\_scale=True_, _scale\_even=False_, _scale=(1.0,1.0,1.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.randomize_transform "Link to this definition")
Randomize objects location, rotation, and scale

Parameters:
*   **random_seed** (_int in_ _[_ _0_ _,_ _10000_ _]_ _,_ _(_ _optional_ _)_) – Random Seed, Seed value for the random generator

*   **use_delta** (_boolean_ _,_ _(_ _optional_ _)_) – Transform Delta, Randomize delta transform values instead of regular transform

*   **use_loc** (_boolean_ _,_ _(_ _optional_ _)_) – Randomize Location, Randomize the location values

*   **loc** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-100, 100], (optional)) – Location, Maximum distance the objects can spread over each axis

*   **use_rot** (_boolean_ _,_ _(_ _optional_ _)_) – Randomize Rotation, Randomize the rotation values

*   **rot** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-3.14159, 3.14159], (optional)) – Rotation, Maximum rotation over each axis

*   **use_scale** (_boolean_ _,_ _(_ _optional_ _)_) – Randomize Scale, Randomize the scale values

*   **scale_even** (_boolean_ _,_ _(_ _optional_ _)_) – Scale Even, Use the same scale value for all axis

*   **scale** (_float array_ _of_ _3 items in_ _[_ _-100_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – Scale, Maximum scale randomization over each axis

File:
[startup/bl_operators/object_randomize_transform.py:161](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_randomize_transform.py#L161)

bpy.ops.object.reset_override_library()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.reset_override_library "Link to this definition")
Reset the selected local overrides to their linked references values

bpy.ops.object.rotation_clear(_*_, _clear\_delta=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.rotation_clear "Link to this definition")
Clear the object’s rotation

Parameters:
**clear_delta** (_boolean_ _,_ _(_ _optional_ _)_) – Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform

bpy.ops.object.scale_clear(_*_, _clear\_delta=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.scale_clear "Link to this definition")
Clear the object’s scale

Parameters:
**clear_delta** (_boolean_ _,_ _(_ _optional_ _)_) – Clear Delta, Clear delta scale in addition to clearing the normal scale transform

bpy.ops.object.select_all(_*_, _action='TOGGLE'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_all "Link to this definition")
Change selection of all visible objects in scene

Parameters:
**action** (enum in [`'TOGGLE'`, `'SELECT'`, `'DESELECT'`, `'INVERT'`], (optional)) –

Action, Selection action to execute

*   `TOGGLE` Toggle – Toggle selection for all elements.

*   `SELECT` Select – Select all elements.

*   `DESELECT` Deselect – Deselect all elements.

*   `INVERT` Invert – Invert selection of all elements.

bpy.ops.object.select_by_type(_*_, _extend=False_, _type='MESH'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_by_type "Link to this definition")
Select all visible objects that are of a type

Parameters:
*   **extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend selection instead of deselecting everything first

*   **type** (enum in [Object Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_type_items.html#rna-enum-object-type-items), (optional)) – Type

bpy.ops.object.select_camera(_*_, _extend=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_camera "Link to this definition")
Select the active camera

Parameters:
**extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend the selection

File:
[startup/bl_operators/object.py:122](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L122)

bpy.ops.object.select_grouped(_*_, _extend=False_, _type='CHILDREN\_RECURSIVE'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_grouped "Link to this definition")
Select all visible objects grouped by various properties

Parameters:
*   **extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend selection instead of deselecting everything first

*   **type** (enum in [`'CHILDREN_RECURSIVE'`, `'CHILDREN'`, `'PARENT'`, `'SIBLINGS'`, `'TYPE'`, `'COLLECTION'`, `'HOOK'`, `'PASS'`, `'COLOR'`, `'KEYINGSET'`, `'LIGHT_TYPE'`], (optional)) –

Type

    *   `CHILDREN_RECURSIVE` Children.

    *   `CHILDREN` Immediate Children.

    *   `PARENT` Parent.

    *   `SIBLINGS` Siblings – Shared parent.

    *   `TYPE` Type – Shared object type.

    *   `COLLECTION` Collection – Shared collection.

    *   `HOOK` Hook.

    *   `PASS` Pass – Render pass index.

    *   `COLOR` Color – Object color.

    *   `KEYINGSET` Keying Set – Objects included in active Keying Set.

    *   `LIGHT_TYPE` Light Type – Matching light types.

bpy.ops.object.select_hierarchy(_*_, _direction='PARENT'_, _extend=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_hierarchy "Link to this definition")
Select object relative to the active object’s position in the hierarchy

Parameters:
*   **direction** (enum in [`'PARENT'`, `'CHILD'`], (optional)) – Direction, Direction to select in the hierarchy

*   **extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend the existing selection

File:
[startup/bl_operators/object.py:172](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L172)

bpy.ops.object.select_less()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_less "Link to this definition")
Deselect objects at the boundaries of parent/child relationships

bpy.ops.object.select_linked(_*_, _extend=False_, _type='OBDATA'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_linked "Link to this definition")
Select all visible objects that are linked

Parameters:
*   **extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend selection instead of deselecting everything first

*   **type** (enum in [`'OBDATA'`, `'MATERIAL'`, `'DUPGROUP'`, `'PARTICLE'`, `'LIBRARY'`, `'LIBRARY_OBDATA'`], (optional)) – Type

bpy.ops.object.select_mirror(_*_, _extend=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_mirror "Link to this definition")
Select the mirror objects of the selected object e.g. “L.sword” and “R.sword”

Parameters:
**extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend selection instead of deselecting everything first

bpy.ops.object.select_more()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_more "Link to this definition")
Select connected parent/child objects

bpy.ops.object.select_pattern(_*_, _pattern='*'_, _case\_sensitive=False_, _extend=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_pattern "Link to this definition")
Select objects matching a naming pattern

Parameters:
*   **pattern** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Pattern, Name filter using ‘*’, ‘?’ and ‘[abc]’ unix style wildcards

*   **case_sensitive** (_boolean_ _,_ _(_ _optional_ _)_) – Case Sensitive, Do a case sensitive compare

*   **extend** (_boolean_ _,_ _(_ _optional_ _)_) – Extend, Extend the existing selection

File:
[startup/bl_operators/object.py:45](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L45)

bpy.ops.object.select_random(_*_, _ratio=0.5_, _seed=0_, _action='SELECT'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_random "Link to this definition")
Select or deselect random visible objects

Parameters:
*   **ratio** (_float in_ _[_ _0_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – Ratio, Portion of items to select randomly

*   **seed** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Random Seed, Seed for the random number generator

*   **action** (enum in [`'SELECT'`, `'DESELECT'`], (optional)) –

Action, Selection action to execute

    *   `SELECT` Select – Select all elements.

    *   `DESELECT` Deselect – Deselect all elements.

bpy.ops.object.select_same_collection(_*_, _collection=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_same_collection "Link to this definition")
Select object in the same collection

Parameters:
**collection** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Collection, Name of the collection to select

bpy.ops.object.shade_auto_smooth(_*_, _use\_auto\_smooth=True_, _angle=0.523599_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_auto_smooth "Link to this definition")
Add modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces

Parameters:
*   **use_auto_smooth** (_boolean_ _,_ _(_ _optional_ _)_) – Auto Smooth, Add modifier to set edge sharpness automatically

*   **angle** (_float in_ _[_ _0_ _,_ _3.14159_ _]_ _,_ _(_ _optional_ _)_) – Angle, Maximum angle between face normals that will be considered as smooth

bpy.ops.object.shade_flat(_*_, _keep\_sharp\_edges=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_flat "Link to this definition")
Render and display faces uniform, using face normals

Parameters:
**keep_sharp_edges** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Sharp Edges, Don’t remove sharp edges, which are redundant with faces shaded smooth

bpy.ops.object.shade_smooth(_*_, _keep\_sharp\_edges=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_smooth "Link to this definition")
Render and display faces smooth, using interpolated vertex normals

Parameters:
**keep_sharp_edges** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Sharp Edges, Don’t remove sharp edges. Tagged edges will remain sharp

bpy.ops.object.shade_smooth_by_angle(_*_, _angle=0.523599_, _keep\_sharp\_edges=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_smooth_by_angle "Link to this definition")
Set the sharpness of mesh edges based on the angle between the neighboring faces

Parameters:
*   **angle** (_float in_ _[_ _0_ _,_ _3.14159_ _]_ _,_ _(_ _optional_ _)_) – Angle, Maximum angle between face normals that will be considered as smooth

*   **keep_sharp_edges** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Sharp Edges, Only add sharp edges instead of clearing existing tags first

bpy.ops.object.shaderfx_add(_*_, _type='FX\_BLUR'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_add "Link to this definition")
Add a visual effect to the active object

Parameters:
**type** (enum in [Object Shaderfx Type Items](https://docs.blender.org/api/current/bpy_types_enum_items/object_shaderfx_type_items.html#rna-enum-object-shaderfx-type-items), (optional)) – Type

bpy.ops.object.shaderfx_copy(_*_, _shaderfx=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_copy "Link to this definition")
Duplicate effect at the same position in the stack

Parameters:
**shaderfx** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Shader, Name of the shaderfx to edit

bpy.ops.object.shaderfx_move_down(_*_, _shaderfx=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_move_down "Link to this definition")
Move effect down in the stack

Parameters:
**shaderfx** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Shader, Name of the shaderfx to edit

bpy.ops.object.shaderfx_move_to_index(_*_, _shaderfx=''_, _index=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_move_to_index "Link to this definition")
Change the effect’s position in the list so it evaluates after the set number of others

Parameters:
*   **shaderfx** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Shader, Name of the shaderfx to edit

*   **index** (_int in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Index, The index to move the effect to

bpy.ops.object.shaderfx_move_up(_*_, _shaderfx=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_move_up "Link to this definition")
Move effect up in the stack

Parameters:
**shaderfx** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Shader, Name of the shaderfx to edit

bpy.ops.object.shaderfx_remove(_*_, _shaderfx=''_, _report=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_remove "Link to this definition")
Remove a effect from the active Grease Pencil object

Parameters:
*   **shaderfx** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Shader, Name of the shaderfx to edit

*   **report** (_boolean_ _,_ _(_ _optional_ _)_) – Report, Create a notification after the operation

bpy.ops.object.shape_key_add(_*_, _from\_mix=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_add "Link to this definition")
Add shape key to the object

Parameters:
**from_mix** (_boolean_ _,_ _(_ _optional_ _)_) – From Mix, Create the new shape key from the existing mix of keys

bpy.ops.object.shape_key_clear()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_clear "Link to this definition")
Reset the weights of all shape keys to 0 or to the closest value respecting the limits

bpy.ops.object.shape_key_copy()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_copy "Link to this definition")
Duplicate the active shape key

bpy.ops.object.shape_key_lock(_*_, _action='LOCK'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_lock "Link to this definition")
Change the lock state of all shape keys of active object

Parameters:
**action** (enum in [`'LOCK'`, `'UNLOCK'`], (optional)) –

Action, Lock action to execute on vertex groups

*   `LOCK` Lock – Lock all shape keys.

*   `UNLOCK` Unlock – Unlock all shape keys.

bpy.ops.object.shape_key_make_basis()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_make_basis "Link to this definition")
Make this shape key the new basis key, effectively applying it to the mesh. Note that this applies the shape key at its 100% value

bpy.ops.object.shape_key_mirror(_*_, _use\_topology=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_mirror "Link to this definition")
Mirror the current shape key along the local X axis

Parameters:
**use_topology** (_boolean_ _,_ _(_ _optional_ _)_) – Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)

bpy.ops.object.shape_key_move(_*_, _type='TOP'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_move "Link to this definition")
Move selected shape keys up/down in the list

Parameters:
**type** (enum in [`'TOP'`, `'UP'`, `'DOWN'`, `'BOTTOM'`], (optional)) –

Type

*   `TOP` Top – Top of the list.

*   `UP` Up.

*   `DOWN` Down.

*   `BOTTOM` Bottom – Bottom of the list.

bpy.ops.object.shape_key_remove(_*_, _all=False_, _apply\_mix=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_remove "Link to this definition")
Remove shape key from the object

Parameters:
*   **all** (_boolean_ _,_ _(_ _optional_ _)_) – All, Remove all shape keys

*   **apply_mix** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Mix, Apply current mix of shape keys to the geometry before removing them

bpy.ops.object.shape_key_retime()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_retime "Link to this definition")
Resets the timing for absolute shape keys

bpy.ops.object.shape_key_transfer(_*_, _mode='OFFSET'_, _use\_clamp=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_transfer "Link to this definition")
Copy the active shape key of another selected object to this one

Parameters:
*   **mode** (enum in [`'OFFSET'`, `'RELATIVE_FACE'`, `'RELATIVE_EDGE'`], (optional)) –

Transformation Mode, Relative shape positions to the new shape method

    *   `OFFSET` Offset – Apply the relative positional offset.

    *   `RELATIVE_FACE` Relative Face – Calculate relative position (using faces).

    *   `RELATIVE_EDGE` Relative Edge – Calculate relative position (using edges).

*   **use_clamp** (_boolean_ _,_ _(_ _optional_ _)_) – Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape

File:
[startup/bl_operators/object.py:502](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L502)

bpy.ops.object.simulation_nodes_cache_bake(_*_, _selected=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.simulation_nodes_cache_bake "Link to this definition")
Bake simulations in geometry nodes modifiers

Parameters:
**selected** (_boolean_ _,_ _(_ _optional_ _)_) – Selected, Bake cache on all selected objects

bpy.ops.object.simulation_nodes_cache_calculate_to_frame(_*_, _selected=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.simulation_nodes_cache_calculate_to_frame "Link to this definition")
Calculate simulations in geometry nodes modifiers from the start to current frame

Parameters:
**selected** (_boolean_ _,_ _(_ _optional_ _)_) – Selected, Calculate all selected objects instead of just the active object

bpy.ops.object.simulation_nodes_cache_delete(_*_, _selected=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.simulation_nodes_cache_delete "Link to this definition")
Delete cached/baked simulations in geometry nodes modifiers

Parameters:
**selected** (_boolean_ _,_ _(_ _optional_ _)_) – Selected, Delete cache on all selected objects

bpy.ops.object.skin_armature_create(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_armature_create "Link to this definition")
Create an armature that parallels the skin layout

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.skin_loose_mark_clear(_*_, _action='MARK'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_loose_mark_clear "Link to this definition")
Mark/clear selected vertices as loose

Parameters:
**action** (enum in [`'MARK'`, `'CLEAR'`], (optional)) –

Action

*   `MARK` Mark – Mark selected vertices as loose.

*   `CLEAR` Clear – Set selected vertices as not loose.

bpy.ops.object.skin_radii_equalize()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_radii_equalize "Link to this definition")
Make skin radii of selected vertices equal on each axis

bpy.ops.object.skin_root_mark()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_root_mark "Link to this definition")
Mark selected vertices as roots

bpy.ops.object.speaker_add(_*_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.speaker_add "Link to this definition")
Add a speaker object to the scene

Parameters:
*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.subdivision_set(_*_, _level=1_, _relative=False_, _ensure\_modifier=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.subdivision_set "Link to this definition")
Sets a Subdivision Surface level (1 to 5)

Parameters:
*   **level** (_int in_ _[_ _-100_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – Level

*   **relative** (_boolean_ _,_ _(_ _optional_ _)_) – Relative, Apply the subdivision surface level as an offset relative to the current level

*   **ensure_modifier** (_boolean_ _,_ _(_ _optional_ _)_) – Ensure Modifier, Create the corresponding modifier if it does not exist

File:
[startup/bl_operators/object.py:245](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L245)

bpy.ops.object.surfacedeform_bind(_*_, _modifier=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.surfacedeform_bind "Link to this definition")
Bind mesh to target in surface deform modifier

Parameters:
**modifier** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Modifier, Name of the modifier to edit

bpy.ops.object.text_add(_*_, _radius=1.0_, _enter\_editmode=False_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.text_add "Link to this definition")
Add a text object to the scene

Parameters:
*   **radius** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Radius

*   **enter_editmode** (_boolean_ _,_ _(_ _optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.track_clear(_*_, _type='CLEAR'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.track_clear "Link to this definition")
Clear tracking constraint or flag from object

Parameters:
**type** (enum in [`'CLEAR'`, `'CLEAR_KEEP_TRANSFORM'`], (optional)) – Type

bpy.ops.object.track_set(_*_, _type='DAMPTRACK'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.track_set "Link to this definition")
Make the object track another object, using various methods/constraints

Parameters:
**type** (enum in [`'DAMPTRACK'`, `'TRACKTO'`, `'LOCKTRACK'`], (optional)) – Type

bpy.ops.object.transfer_mode(_*_, _use\_flash\_on\_transfer=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transfer_mode "Link to this definition")
Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

Parameters:
**use_flash_on_transfer** (_boolean_ _,_ _(_ _optional_ _)_) – Flash On Transfer, Flash the target object when transferring the mode

bpy.ops.object.transform_apply(_*_, _location=True_, _rotation=True_, _scale=True_, _properties=True_, _isolate\_users=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transform_apply "Link to this definition")
Apply the object’s transformation to its data

Parameters:
*   **location** (_boolean_ _,_ _(_ _optional_ _)_) – Location

*   **rotation** (_boolean_ _,_ _(_ _optional_ _)_) – Rotation

*   **scale** (_boolean_ _,_ _(_ _optional_ _)_) – Scale

*   **properties** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope

*   **isolate_users** (_boolean_ _,_ _(_ _optional_ _)_) – Isolate Multi User Data, Create new object-data users if needed

bpy.ops.object.transform_axis_target()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transform_axis_target "Link to this definition")
Interactively point cameras and lights to a location (Ctrl translates)

bpy.ops.object.transform_to_mouse(_*_, _name=''_, _session\_uid=0_, _matrix=((0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0),(0.0,0.0,0.0,0.0))_, _drop\_x=0_, _drop\_y=0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transform_to_mouse "Link to this definition")
Snap selected item(s) to the mouse location

Parameters:
*   **name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Name, Object name to place (uses the active object when this and ‘session_uid’ are unset)

*   **session_uid** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Session UUID, Session UUID of the object to place (uses the active object when this and ‘name’ are unset)

*   **matrix** ([`mathutils.Matrix`](https://docs.blender.org/api/current/mathutils.html#mathutils.Matrix "mathutils.Matrix") of 4 * 4 items in [-inf, inf], (optional)) – Matrix

*   **drop_x** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop X, X-coordinate (screen space) to place the new object under

*   **drop_y** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Drop Y, Y-coordinate (screen space) to place the new object under

bpy.ops.object.transforms_to_deltas(_*_, _mode='ALL'_, _reset\_values=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transforms_to_deltas "Link to this definition")
Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

Parameters:
*   **mode** (enum in [`'ALL'`, `'LOC'`, `'ROT'`, `'SCALE'`], (optional)) –

Mode, Which transforms to transfer

    *   `ALL` All Transforms – Transfer location, rotation, and scale transforms.

    *   `LOC` Location – Transfer location transforms only.

    *   `ROT` Rotation – Transfer rotation transforms only.

    *   `SCALE` Scale – Transfer scale transforms only.

*   **reset_values** (_boolean_ _,_ _(_ _optional_ _)_) – Reset Values, Clear transform values after transferring to deltas

File:
[startup/bl_operators/object.py:764](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L764)

bpy.ops.object.unlink_data()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.unlink_data "Link to this definition")
Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.object.update_shapes(_*_, _use\_mirror=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.update_shapes "Link to this definition")
Update existing shape keys with the vertex positions of selected objects with matching names

Parameters:
**use_mirror** (_boolean_ _,_ _(_ _optional_ _)_) – Mirror, Mirror the new shape key values

bpy.ops.object.vertex_group_add()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_add "Link to this definition")
Add a new vertex group to the active object

bpy.ops.object.vertex_group_assign()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_assign "Link to this definition")
Assign the selected vertices to the active vertex group

bpy.ops.object.vertex_group_assign_new()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_assign_new "Link to this definition")
Assign the selected vertices to a new vertex group

bpy.ops.object.vertex_group_clean(_*_, _group\_select\_mode=''_, _limit=0.0_, _keep\_single=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_clean "Link to this definition")
Remove vertex group assignments which are not required

Parameters:
*   **group_select_mode** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Subset, Define which subset of groups shall be used

*   **limit** (_float in_ _[_ _0_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – Limit, Remove vertices which weight is below or equal to this limit

*   **keep_single** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Single, Keep verts assigned to at least one group when cleaning

bpy.ops.object.vertex_group_copy()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_copy "Link to this definition")
Make a copy of the active vertex group

bpy.ops.object.vertex_group_copy_to_selected()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_copy_to_selected "Link to this definition")
Replace vertex groups of selected objects by vertex groups of active object

bpy.ops.object.vertex_group_deselect()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_deselect "Link to this definition")
Deselect all selected vertices assigned to the active vertex group

bpy.ops.object.vertex_group_invert(_*_, _group\_select\_mode=''_, _auto\_assign=True_, _auto\_remove=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_invert "Link to this definition")
Invert active vertex group’s weights

Parameters:
*   **group_select_mode** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Subset, Define which subset of groups shall be used

*   **auto_assign** (_boolean_ _,_ _(_ _optional_ _)_) – Add Weights, Add vertices from groups that have zero weight before inverting

*   **auto_remove** (_boolean_ _,_ _(_ _optional_ _)_) – Remove Weights, Remove vertices from groups that have zero weight after inverting

bpy.ops.object.vertex_group_levels(_*_, _group\_select\_mode=''_, _offset=0.0_, _gain=1.0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_levels "Link to this definition")
Add some offset and multiply with some gain the weights of the active vertex group

Parameters:
*   **group_select_mode** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Subset, Define which subset of groups shall be used

*   **offset** (_float in_ _[_ _-1_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – Offset, Value to add to weights

*   **gain** (_float in_ _[_ _0_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Gain, Value to multiply weights by

bpy.ops.object.vertex_group_limit_total(_*_, _group\_select\_mode=''_, _limit=4_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_limit_total "Link to this definition")
Limit deform weights associated with a vertex to a specified number by removing lowest weights

Parameters:
*   **group_select_mode** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Subset, Define which subset of groups shall be used

*   **limit** (_int in_ _[_ _1_ _,_ _32_ _]_ _,_ _(_ _optional_ _)_) – Limit, Maximum number of deform weights

bpy.ops.object.vertex_group_lock(_*_, _action='TOGGLE'_, _mask='ALL'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_lock "Link to this definition")
Change the lock state of all or some vertex groups of active object

Parameters:
*   **action** (enum in [`'TOGGLE'`, `'LOCK'`, `'UNLOCK'`, `'INVERT'`], (optional)) –

Action, Lock action to execute on vertex groups

    *   `TOGGLE` Toggle – Unlock all vertex groups if there is at least one locked group, lock all in other case.

    *   `LOCK` Lock – Lock all vertex groups.

    *   `UNLOCK` Unlock – Unlock all vertex groups.

    *   `INVERT` Invert – Invert the lock state of all vertex groups.

*   **mask** (enum in [`'ALL'`, `'SELECTED'`, `'UNSELECTED'`, `'INVERT_UNSELECTED'`], (optional)) –

Mask, Apply the action based on vertex group selection

    *   `ALL` All – Apply action to all vertex groups.

    *   `SELECTED` Selected – Apply to selected vertex groups.

    *   `UNSELECTED` Unselected – Apply to unselected vertex groups.

    *   `INVERT_UNSELECTED` Invert Unselected – Apply the opposite of Lock/Unlock to unselected vertex groups.

bpy.ops.object.vertex_group_mirror(_*_, _mirror\_weights=True_, _flip\_group\_names=True_, _all\_groups=False_, _use\_topology=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_mirror "Link to this definition")
Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

Parameters:
*   **mirror_weights** (_boolean_ _,_ _(_ _optional_ _)_) – Mirror Weights, Mirror weights

*   **flip_group_names** (_boolean_ _,_ _(_ _optional_ _)_) – Flip Group Names, Flip vertex group names

*   **all_groups** (_boolean_ _,_ _(_ _optional_ _)_) – All Groups, Mirror all vertex groups weights

*   **use_topology** (_boolean_ _,_ _(_ _optional_ _)_) – Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)

bpy.ops.object.vertex_group_move(_*_, _direction='UP'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_move "Link to this definition")
Move the active vertex group up/down in the list

Parameters:
**direction** (enum in [`'UP'`, `'DOWN'`], (optional)) – Direction, Direction to move the active vertex group towards

bpy.ops.object.vertex_group_normalize()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_normalize "Link to this definition")
Normalize weights of the active vertex group, so that the highest ones are now 1.0

bpy.ops.object.vertex_group_normalize_all(_*_, _group\_select\_mode=''_, _lock\_active=True_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_normalize_all "Link to this definition")
Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

Parameters:
*   **group_select_mode** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Subset, Define which subset of groups shall be used

*   **lock_active** (_boolean_ _,_ _(_ _optional_ _)_) – Lock Active, Keep the values of the active group while normalizing others

bpy.ops.object.vertex_group_quantize(_*_, _group\_select\_mode=''_, _steps=4_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_quantize "Link to this definition")
Set weights to a fixed number of steps

Parameters:
*   **group_select_mode** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Subset, Define which subset of groups shall be used

*   **steps** (_int in_ _[_ _1_ _,_ _1000_ _]_ _,_ _(_ _optional_ _)_) – Steps, Number of steps between 0 and 1

bpy.ops.object.vertex_group_remove(_*_, _all=False_, _all\_unlocked=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_remove "Link to this definition")
Delete the active or all vertex groups from the active object

Parameters:
*   **all** (_boolean_ _,_ _(_ _optional_ _)_) – All, Remove all vertex groups

*   **all_unlocked** (_boolean_ _,_ _(_ _optional_ _)_) – All Unlocked, Remove all unlocked vertex groups

bpy.ops.object.vertex_group_remove_from(_*_, _use\_all\_groups=False_, _use\_all\_verts=False_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_remove_from "Link to this definition")
Remove the selected vertices from active or all vertex group(s)

Parameters:
*   **use_all_groups** (_boolean_ _,_ _(_ _optional_ _)_) – All Groups, Remove from all groups

*   **use_all_verts** (_boolean_ _,_ _(_ _optional_ _)_) – All Vertices, Clear the active group

bpy.ops.object.vertex_group_select()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_select "Link to this definition")
Select all the vertices assigned to the active vertex group

bpy.ops.object.vertex_group_set_active(_*_, _group=''_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_set_active "Link to this definition")
Set the active vertex group

Parameters:
**group** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Group, Vertex group to set as active

bpy.ops.object.vertex_group_smooth(_*_, _group\_select\_mode=''_, _factor=0.5_, _repeat=1_, _expand=0.0_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_smooth "Link to this definition")
Smooth weights for selected vertices

Parameters:
*   **group_select_mode** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Subset, Define which subset of groups shall be used

*   **factor** (_float in_ _[_ _0_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – Factor

*   **repeat** (_int in_ _[_ _1_ _,_ _10000_ _]_ _,_ _(_ _optional_ _)_) – Iterations

*   **expand** (_float in_ _[_ _-1_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – Expand/Contract, Expand/contract weights

bpy.ops.object.vertex_group_sort(_*_, _sort\_type='NAME'_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_sort "Link to this definition")
Sort vertex groups

Parameters:
**sort_type** (enum in [`'NAME'`, `'BONE_HIERARCHY'`], (optional)) – Sort Type, Sort type

bpy.ops.object.vertex_parent_set()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_parent_set "Link to this definition")
Parent selected objects to the selected vertices

bpy.ops.object.vertex_weight_copy()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_copy "Link to this definition")
Copy weights from active to selected

bpy.ops.object.vertex_weight_delete(_*_, _weight\_group=-1_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_delete "Link to this definition")
Delete this weight from the vertex (disabled if vertex group is locked)

Parameters:
**weight_group** (_int in_ _[_ _-1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Weight Index, Index of source weight in active vertex group

bpy.ops.object.vertex_weight_normalize_active_vertex()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_normalize_active_vertex "Link to this definition")
Normalize active vertex’s weights

bpy.ops.object.vertex_weight_paste(_*_, _weight\_group=-1_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_paste "Link to this definition")
Copy this group’s weight to other selected vertices (disabled if vertex group is locked)

Parameters:
**weight_group** (_int in_ _[_ _-1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Weight Index, Index of source weight in active vertex group

bpy.ops.object.vertex_weight_set_active(_*_, _weight\_group=-1_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_set_active "Link to this definition")
Set as active vertex group

Parameters:
**weight_group** (_int in_ _[_ _-1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Weight Index, Index of source weight in active vertex group

bpy.ops.object.visual_geometry_to_objects()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.visual_geometry_to_objects "Link to this definition")
Convert geometry and instances into editable objects and collections

bpy.ops.object.visual_transform_apply()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.visual_transform_apply "Link to this definition")
Apply the object’s visual transformation to its data

bpy.ops.object.volume_add(_*_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.volume_add "Link to this definition")
Add a volume object to the scene

Parameters:
*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.volume_import(_*_, _filepath=''_, _directory=''_, _files=None_, _hide\_props\_region=True_, _check\_existing=False_, _filter\_blender=False_, _filter\_backup=False_, _filter\_image=False_, _filter\_movie=False_, _filter\_python=False_, _filter\_font=False_, _filter\_sound=False_, _filter\_text=False_, _filter\_archive=False_, _filter\_btx=False_, _filter\_alembic=False_, _filter\_usd=False_, _filter\_obj=False_, _filter\_volume=True_, _filter\_folder=True_, _filter\_blenlib=False_, _filemode=9_, _relative\_path=True_, _display\_type='DEFAULT'_, _sort\_method=''_, _use\_sequence\_detection=True_, _align='WORLD'_, _location=(0.0,0.0,0.0)_, _rotation=(0.0,0.0,0.0)_, _scale=(0.0,0.0,0.0)_)[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.volume_import "Link to this definition")
Import OpenVDB volume file

Parameters:
*   **filepath** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – File Path, Path to file

*   **directory** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Directory, Directory of the file

*   **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files

*   **hide_props_region** (_boolean_ _,_ _(_ _optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

*   **check_existing** (_boolean_ _,_ _(_ _optional_ _)_) – Check Existing, Check and warn on overwriting existing files

*   **filter_blender** (_boolean_ _,_ _(_ _optional_ _)_) – Filter .blend files

*   **filter_backup** (_boolean_ _,_ _(_ _optional_ _)_) – Filter .blend files

*   **filter_image** (_boolean_ _,_ _(_ _optional_ _)_) – Filter image files

*   **filter_movie** (_boolean_ _,_ _(_ _optional_ _)_) – Filter movie files

*   **filter_python** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Python files

*   **filter_font** (_boolean_ _,_ _(_ _optional_ _)_) – Filter font files

*   **filter_sound** (_boolean_ _,_ _(_ _optional_ _)_) – Filter sound files

*   **filter_text** (_boolean_ _,_ _(_ _optional_ _)_) – Filter text files

*   **filter_archive** (_boolean_ _,_ _(_ _optional_ _)_) – Filter archive files

*   **filter_btx** (_boolean_ _,_ _(_ _optional_ _)_) – Filter btx files

*   **filter_alembic** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Alembic files

*   **filter_usd** (_boolean_ _,_ _(_ _optional_ _)_) – Filter USD files

*   **filter_obj** (_boolean_ _,_ _(_ _optional_ _)_) – Filter OBJ files

*   **filter_volume** (_boolean_ _,_ _(_ _optional_ _)_) – Filter OpenVDB volume files

*   **filter_folder** (_boolean_ _,_ _(_ _optional_ _)_) – Filter folders

*   **filter_blenlib** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Blender IDs

*   **filemode** (_int in_ _[_ _1_ _,_ _9_ _]_ _,_ _(_ _optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

*   **relative_path** (_boolean_ _,_ _(_ _optional_ _)_) – Relative Path, Select the file relative to the blend file

*   **display_type** (enum in [`'DEFAULT'`, `'LIST_VERTICAL'`, `'LIST_HORIZONTAL'`, `'THUMBNAIL'`], (optional)) –

Display Type

    *   `DEFAULT` Default – Automatically determine display type for files.

    *   `LIST_VERTICAL` Short List – Display files as short list.

    *   `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    *   `THUMBNAIL` Thumbnails – Display files as thumbnails.

*   **sort_method** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – File sorting mode

*   **use_sequence_detection** (_boolean_ _,_ _(_ _optional_ _)_) – Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names)

*   **align** (enum in [`'WORLD'`, `'VIEW'`, `'CURSOR'`], (optional)) –

Align, The alignment of the new object

    *   `WORLD` World – Align the new object to the world.

    *   `VIEW` View – Align the new object to the view.

    *   `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

*   **location** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

*   **rotation** ([`mathutils.Euler`](https://docs.blender.org/api/current/mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

*   **scale** ([`mathutils.Vector`](https://docs.blender.org/api/current/mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.object.voxel_remesh()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.voxel_remesh "Link to this definition")
Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

bpy.ops.object.voxel_size_edit()[¶](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.voxel_size_edit "Link to this definition")
Modify the mesh voxel size interactively used in the voxel remesher

[Next Outliner Operators](https://docs.blender.org/api/current/bpy.ops.outliner.html)[Previous Node Operators](https://docs.blender.org/api/current/bpy.ops.node.html)

 Copyright © Blender Authors 

 Made with [Furo](https://github.com/pradyunsg/furo)

*   [Report issue on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.object.rst%60%0D%0ABlender+Version%3A+%605.0%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F5.0%2Fbpy.ops.object.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

 On this page 

*   [Object Operators](https://docs.blender.org/api/current/bpy.ops.object.html#)
    *   [`add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.add)
    *   [`add_modifier_menu()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.add_modifier_menu)
    *   [`add_named()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.add_named)
    *   [`align()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.align)
    *   [`anim_transforms_to_deltas()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.anim_transforms_to_deltas)
    *   [`armature_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.armature_add)
    *   [`assign_property_defaults()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.assign_property_defaults)
    *   [`bake()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.bake)
    *   [`bake_image()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.bake_image)
    *   [`camera_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.camera_add)
    *   [`camera_custom_update()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.camera_custom_update)
    *   [`clear_override_library()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.clear_override_library)
    *   [`collection_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_add)
    *   [`collection_external_asset_drop()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_external_asset_drop)
    *   [`collection_instance_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_instance_add)
    *   [`collection_link()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_link)
    *   [`collection_objects_select()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_objects_select)
    *   [`collection_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_remove)
    *   [`collection_unlink()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.collection_unlink)
    *   [`constraint_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraint_add)
    *   [`constraint_add_with_targets()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraint_add_with_targets)
    *   [`constraints_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraints_clear)
    *   [`constraints_copy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.constraints_copy)
    *   [`convert()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.convert)
    *   [`copy_global_transform()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.copy_global_transform)
    *   [`copy_relative_transform()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.copy_relative_transform)
    *   [`correctivesmooth_bind()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.correctivesmooth_bind)
    *   [`curves_empty_hair_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.curves_empty_hair_add)
    *   [`curves_random_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.curves_random_add)
    *   [`data_instance_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.data_instance_add)
    *   [`data_transfer()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.data_transfer)
    *   [`datalayout_transfer()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.datalayout_transfer)
    *   [`delete()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.delete)
    *   [`delete_fix_to_camera_keys()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.delete_fix_to_camera_keys)
    *   [`drop_geometry_nodes()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.drop_geometry_nodes)
    *   [`drop_named_material()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.drop_named_material)
    *   [`duplicate()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicate)
    *   [`duplicate_move()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicate_move)
    *   [`duplicate_move_linked()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicate_move_linked)
    *   [`duplicates_make_real()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.duplicates_make_real)
    *   [`editmode_toggle()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.editmode_toggle)
    *   [`effector_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.effector_add)
    *   [`empty_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.empty_add)
    *   [`empty_image_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.empty_image_add)
    *   [`explode_refresh()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.explode_refresh)
    *   [`fix_to_camera()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.fix_to_camera)
    *   [`forcefield_toggle()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.forcefield_toggle)
    *   [`geometry_node_bake_delete_single()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_delete_single)
    *   [`geometry_node_bake_pack_single()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_pack_single)
    *   [`geometry_node_bake_single()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_single)
    *   [`geometry_node_bake_unpack_single()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_bake_unpack_single)
    *   [`geometry_node_tree_copy_assign()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_node_tree_copy_assign)
    *   [`geometry_nodes_input_attribute_toggle()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_nodes_input_attribute_toggle)
    *   [`geometry_nodes_move_to_nodes()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.geometry_nodes_move_to_nodes)
    *   [`grease_pencil_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_add)
    *   [`grease_pencil_dash_modifier_segment_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_dash_modifier_segment_add)
    *   [`grease_pencil_dash_modifier_segment_move()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_dash_modifier_segment_move)
    *   [`grease_pencil_dash_modifier_segment_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_dash_modifier_segment_remove)
    *   [`grease_pencil_time_modifier_segment_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_time_modifier_segment_add)
    *   [`grease_pencil_time_modifier_segment_move()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_time_modifier_segment_move)
    *   [`grease_pencil_time_modifier_segment_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.grease_pencil_time_modifier_segment_remove)
    *   [`hide_collection()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_collection)
    *   [`hide_render_clear_all()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_render_clear_all)
    *   [`hide_view_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_view_clear)
    *   [`hide_view_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hide_view_set)
    *   [`hook_add_newob()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_add_newob)
    *   [`hook_add_selob()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_add_selob)
    *   [`hook_assign()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_assign)
    *   [`hook_recenter()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_recenter)
    *   [`hook_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_remove)
    *   [`hook_reset()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_reset)
    *   [`hook_select()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.hook_select)
    *   [`instance_offset_from_cursor()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.instance_offset_from_cursor)
    *   [`instance_offset_from_object()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.instance_offset_from_object)
    *   [`instance_offset_to_cursor()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.instance_offset_to_cursor)
    *   [`isolate_type_render()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.isolate_type_render)
    *   [`join()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.join)
    *   [`join_shapes()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.join_shapes)
    *   [`join_uvs()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.join_uvs)
    *   [`laplaciandeform_bind()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.laplaciandeform_bind)
    *   [`lattice_add_to_selected()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lattice_add_to_selected)
    *   [`light_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_add)
    *   [`light_linking_blocker_collection_new()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_blocker_collection_new)
    *   [`light_linking_blockers_link()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_blockers_link)
    *   [`light_linking_blockers_select()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_blockers_select)
    *   [`light_linking_receiver_collection_new()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_receiver_collection_new)
    *   [`light_linking_receivers_link()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_receivers_link)
    *   [`light_linking_receivers_select()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_receivers_select)
    *   [`light_linking_unlink_from_collection()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.light_linking_unlink_from_collection)
    *   [`lightprobe_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lightprobe_add)
    *   [`lightprobe_cache_bake()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lightprobe_cache_bake)
    *   [`lightprobe_cache_free()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lightprobe_cache_free)
    *   [`lineart_bake_strokes()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lineart_bake_strokes)
    *   [`lineart_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.lineart_clear)
    *   [`link_to_collection()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.link_to_collection)
    *   [`location_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.location_clear)
    *   [`make_dupli_face()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_dupli_face)
    *   [`make_links_data()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_links_data)
    *   [`make_links_scene()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_links_scene)
    *   [`make_local()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_local)
    *   [`make_override_library()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_override_library)
    *   [`make_single_user()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.make_single_user)
    *   [`material_slot_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_add)
    *   [`material_slot_assign()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_assign)
    *   [`material_slot_copy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_copy)
    *   [`material_slot_deselect()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_deselect)
    *   [`material_slot_move()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_move)
    *   [`material_slot_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_remove)
    *   [`material_slot_remove_all()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_remove_all)
    *   [`material_slot_remove_unused()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_remove_unused)
    *   [`material_slot_select()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.material_slot_select)
    *   [`meshdeform_bind()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.meshdeform_bind)
    *   [`metaball_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.metaball_add)
    *   [`mode_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.mode_set)
    *   [`mode_set_with_submode()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.mode_set_with_submode)
    *   [`modifier_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_add)
    *   [`modifier_add_node_group()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_add_node_group)
    *   [`modifier_apply()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_apply)
    *   [`modifier_apply_as_shapekey()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_apply_as_shapekey)
    *   [`modifier_convert()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_convert)
    *   [`modifier_copy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_copy)
    *   [`modifier_copy_to_selected()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_copy_to_selected)
    *   [`modifier_move_down()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_move_down)
    *   [`modifier_move_to_index()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_move_to_index)
    *   [`modifier_move_up()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_move_up)
    *   [`modifier_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_remove)
    *   [`modifier_set_active()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifier_set_active)
    *   [`modifiers_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifiers_clear)
    *   [`modifiers_copy_to_selected()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.modifiers_copy_to_selected)
    *   [`move_to_collection()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.move_to_collection)
    *   [`multires_base_apply()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_base_apply)
    *   [`multires_external_pack()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_external_pack)
    *   [`multires_external_save()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_external_save)
    *   [`multires_higher_levels_delete()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_higher_levels_delete)
    *   [`multires_rebuild_subdiv()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_rebuild_subdiv)
    *   [`multires_reshape()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_reshape)
    *   [`multires_subdivide()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_subdivide)
    *   [`multires_unsubdivide()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.multires_unsubdivide)
    *   [`ocean_bake()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.ocean_bake)
    *   [`origin_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.origin_clear)
    *   [`origin_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.origin_set)
    *   [`parent_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_clear)
    *   [`parent_inverse_apply()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_inverse_apply)
    *   [`parent_no_inverse_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_no_inverse_set)
    *   [`parent_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.parent_set)
    *   [`particle_system_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.particle_system_add)
    *   [`particle_system_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.particle_system_remove)
    *   [`paste_transform()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paste_transform)
    *   [`paths_calculate()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_calculate)
    *   [`paths_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_clear)
    *   [`paths_update()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_update)
    *   [`paths_update_visible()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.paths_update_visible)
    *   [`pointcloud_random_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.pointcloud_random_add)
    *   [`posemode_toggle()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.posemode_toggle)
    *   [`quadriflow_remesh()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quadriflow_remesh)
    *   [`quick_explode()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_explode)
    *   [`quick_fur()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_fur)
    *   [`quick_liquid()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_liquid)
    *   [`quick_smoke()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.quick_smoke)
    *   [`randomize_transform()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.randomize_transform)
    *   [`reset_override_library()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.reset_override_library)
    *   [`rotation_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.rotation_clear)
    *   [`scale_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.scale_clear)
    *   [`select_all()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_all)
    *   [`select_by_type()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_by_type)
    *   [`select_camera()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_camera)
    *   [`select_grouped()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_grouped)
    *   [`select_hierarchy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_hierarchy)
    *   [`select_less()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_less)
    *   [`select_linked()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_linked)
    *   [`select_mirror()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_mirror)
    *   [`select_more()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_more)
    *   [`select_pattern()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_pattern)
    *   [`select_random()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_random)
    *   [`select_same_collection()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.select_same_collection)
    *   [`shade_auto_smooth()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_auto_smooth)
    *   [`shade_flat()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_flat)
    *   [`shade_smooth()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_smooth)
    *   [`shade_smooth_by_angle()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shade_smooth_by_angle)
    *   [`shaderfx_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_add)
    *   [`shaderfx_copy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_copy)
    *   [`shaderfx_move_down()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_move_down)
    *   [`shaderfx_move_to_index()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_move_to_index)
    *   [`shaderfx_move_up()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_move_up)
    *   [`shaderfx_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shaderfx_remove)
    *   [`shape_key_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_add)
    *   [`shape_key_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_clear)
    *   [`shape_key_copy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_copy)
    *   [`shape_key_lock()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_lock)
    *   [`shape_key_make_basis()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_make_basis)
    *   [`shape_key_mirror()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_mirror)
    *   [`shape_key_move()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_move)
    *   [`shape_key_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_remove)
    *   [`shape_key_retime()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_retime)
    *   [`shape_key_transfer()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.shape_key_transfer)
    *   [`simulation_nodes_cache_bake()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.simulation_nodes_cache_bake)
    *   [`simulation_nodes_cache_calculate_to_frame()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.simulation_nodes_cache_calculate_to_frame)
    *   [`simulation_nodes_cache_delete()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.simulation_nodes_cache_delete)
    *   [`skin_armature_create()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_armature_create)
    *   [`skin_loose_mark_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_loose_mark_clear)
    *   [`skin_radii_equalize()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_radii_equalize)
    *   [`skin_root_mark()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.skin_root_mark)
    *   [`speaker_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.speaker_add)
    *   [`subdivision_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.subdivision_set)
    *   [`surfacedeform_bind()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.surfacedeform_bind)
    *   [`text_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.text_add)
    *   [`track_clear()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.track_clear)
    *   [`track_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.track_set)
    *   [`transfer_mode()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transfer_mode)
    *   [`transform_apply()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transform_apply)
    *   [`transform_axis_target()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transform_axis_target)
    *   [`transform_to_mouse()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transform_to_mouse)
    *   [`transforms_to_deltas()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.transforms_to_deltas)
    *   [`unlink_data()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.unlink_data)
    *   [`update_shapes()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.update_shapes)
    *   [`vertex_group_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_add)
    *   [`vertex_group_assign()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_assign)
    *   [`vertex_group_assign_new()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_assign_new)
    *   [`vertex_group_clean()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_clean)
    *   [`vertex_group_copy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_copy)
    *   [`vertex_group_copy_to_selected()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_copy_to_selected)
    *   [`vertex_group_deselect()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_deselect)
    *   [`vertex_group_invert()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_invert)
    *   [`vertex_group_levels()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_levels)
    *   [`vertex_group_limit_total()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_limit_total)
    *   [`vertex_group_lock()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_lock)
    *   [`vertex_group_mirror()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_mirror)
    *   [`vertex_group_move()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_move)
    *   [`vertex_group_normalize()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_normalize)
    *   [`vertex_group_normalize_all()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_normalize_all)
    *   [`vertex_group_quantize()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_quantize)
    *   [`vertex_group_remove()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_remove)
    *   [`vertex_group_remove_from()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_remove_from)
    *   [`vertex_group_select()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_select)
    *   [`vertex_group_set_active()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_set_active)
    *   [`vertex_group_smooth()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_smooth)
    *   [`vertex_group_sort()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_group_sort)
    *   [`vertex_parent_set()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_parent_set)
    *   [`vertex_weight_copy()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_copy)
    *   [`vertex_weight_delete()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_delete)
    *   [`vertex_weight_normalize_active_vertex()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_normalize_active_vertex)
    *   [`vertex_weight_paste()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_paste)
    *   [`vertex_weight_set_active()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.vertex_weight_set_active)
    *   [`visual_geometry_to_objects()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.visual_geometry_to_objects)
    *   [`visual_transform_apply()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.visual_transform_apply)
    *   [`volume_add()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.volume_add)
    *   [`volume_import()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.volume_import)
    *   [`voxel_remesh()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.voxel_remesh)
    *   [`voxel_size_edit()`](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.voxel_size_edit)
