# Source: https://docs.blender.org/api/current/bpy.ops.export_scene.html

Title: Export Scene Operators - Blender Python API

URL Source: https://docs.blender.org/api/current/bpy.ops.export_scene.html

Published Time: Fri, 24 Oct 2025 01:50:14 GMT

Markdown Content:
Export Scene Operators - Blender Python API
===============
- [x] - [x] 

Hide navigation sidebar

 

Hide table of contents sidebar

 [Skip to content](https://docs.blender.org/api/current/bpy.ops.export_scene.html#furo-main-content)

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
    *   [Export Scene Operators](https://docs.blender.org/api/current/bpy.ops.export_scene.html#)
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
    *   [Object Operators](https://docs.blender.org/api/current/bpy.ops.object.html)
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

*   [](https://docs.blender.org/api/current/bpy.ops.export_scene.html)

Note

You are not using the most up to date version of the documentation. [](https://docs.blender.org/api/current/bpy.ops.export_scene.html#) is the newest version.

[Back to top](https://docs.blender.org/api/current/bpy.ops.export_scene.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

 

Export Scene Operators[¶](https://docs.blender.org/api/current/bpy.ops.export_scene.html#module-bpy.ops.export_scene "Link to this heading")
============================================================================================================================================

bpy.ops.export_scene.fbx(_*_, _filepath=''_, _check\_existing=True_, _filter\_glob='*.fbx'_, _use\_selection=False_, _use\_visible=False_, _use\_active\_collection=False_, _collection=''_, _global\_scale=1.0_, _apply\_unit\_scale=True_, _apply\_scale\_options='FBX\_SCALE\_NONE'_, _use\_space\_transform=True_, _bake\_space\_transform=False_, _object\_types={'ARMATURE','CAMERA','EMPTY','LIGHT','MESH','OTHER'}_, _use\_mesh\_modifiers=True_, _use\_mesh\_modifiers\_render=True_, _mesh\_smooth\_type='OFF'_, _colors\_type='SRGB'_, _prioritize\_active\_color=False_, _use\_subsurf=False_, _use\_mesh\_edges=False_, _use\_tspace=False_, _use\_triangles=False_, _use\_custom\_props=False_, _add\_leaf\_bones=True_, _primary\_bone\_axis='Y'_, _secondary\_bone\_axis='X'_, _use\_armature\_deform\_only=False_, _armature\_nodetype='NULL'_, _bake\_anim=True_, _bake\_anim\_use\_all\_bones=True_, _bake\_anim\_use\_nla\_strips=True_, _bake\_anim\_use\_all\_actions=True_, _bake\_anim\_force\_startend\_keying=True_, _bake\_anim\_step=1.0_, _bake\_anim\_simplify\_factor=1.0_, _path\_mode='AUTO'_, _embed\_textures=False_, _batch\_mode='OFF'_, _use\_batch\_own\_dir=True_, _use\_metadata=True_, _axis\_forward='-Z'_, _axis\_up='Y'_)[¶](https://docs.blender.org/api/current/bpy.ops.export_scene.html#bpy.ops.export_scene.fbx "Link to this definition")
Write a FBX file

Parameters:
*   **filepath** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – File Path, Filepath used for exporting the file

*   **check_existing** (_boolean_ _,_ _(_ _optional_ _)_) – Check Existing, Check and warn on overwriting existing files

*   **filter_glob** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – filter_glob

*   **use_selection** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Export selected and visible objects only

*   **use_visible** (_boolean_ _,_ _(_ _optional_ _)_) – Visible Objects, Export visible objects only

*   **use_active_collection** (_boolean_ _,_ _(_ _optional_ _)_) – Active Collection, Export only objects from the active collection (and its children)

*   **collection** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Source Collection, Export only objects from this collection (and its children)

*   **global_scale** (_float in_ _[_ _0.001_ _,_ _1000_ _]_ _,_ _(_ _optional_ _)_) – Scale, Scale all data (Some importers do not support scaled armatures!)

*   **apply_unit_scale** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)

*   **apply_scale_options** (enum in [`'FBX_SCALE_NONE'`, `'FBX_SCALE_UNITS'`, `'FBX_SCALE_CUSTOM'`, `'FBX_SCALE_ALL'`], (optional)) –

Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)

    *   `FBX_SCALE_NONE` All Local – Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.

    *   `FBX_SCALE_UNITS` FBX Units Scale – Apply custom scaling to each object transformation, and units scaling to FBX scale.

    *   `FBX_SCALE_CUSTOM` FBX Custom Scale – Apply custom scaling to FBX scale, and units scaling to each object transformation.

    *   `FBX_SCALE_ALL` FBX All – Apply custom scaling and units scaling to FBX scale.

*   **use_space_transform** (_boolean_ _,_ _(_ _optional_ _)_) – Use Space Transform, Apply global space transform to the object rotations. When disabled only the axis space is written to the file and all object transforms are left as-is

*   **bake_space_transform** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)

*   **object_types** (enum set in {`'EMPTY'`, `'CAMERA'`, `'LIGHT'`, `'ARMATURE'`, `'MESH'`, `'OTHER'`}, (optional)) –

Object Types, Which kind of object to export

    *   `EMPTY` Empty.

    *   `CAMERA` Camera.

    *   `LIGHT` Lamp.

    *   `ARMATURE` Armature – WARNING: not supported in dupli/group instances.

    *   `MESH` Mesh.

    *   `OTHER` Other – Other geometry types, like curve, metaball, etc. (converted to meshes).

*   **use_mesh_modifiers** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys

*   **use_mesh_modifiers_render** (_boolean_ _,_ _(_ _optional_ _)_) – Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)

*   **mesh_smooth_type** (enum in [`'OFF'`, `'FACE'`, `'EDGE'`, `'SMOOTH_GROUP'`], (optional)) –

Smoothing, Export smoothing information (prefer ‘Normals Only’ option if your target importer understands custom normals)

    *   `OFF` Normals Only – Export only normals instead of writing edge or face smoothing data.

    *   `FACE` Face – Write face smoothing.

    *   `EDGE` Edge – Write edge smoothing.

    *   `SMOOTH_GROUP` Smoothing Groups – Write face smoothing groups.

*   **colors_type** (enum in [`'NONE'`, `'SRGB'`, `'LINEAR'`], (optional)) –

Vertex Colors, Export vertex color attributes

    *   `NONE` None – Do not export color attributes.

    *   `SRGB` sRGB – Export colors in sRGB color space.

    *   `LINEAR` Linear – Export colors in linear color space.

*   **prioritize_active_color** (_boolean_ _,_ _(_ _optional_ _)_) – Prioritize Active Color, Make sure active color will be exported first. Could be important since some other software can discard other color attributes besides the first one

*   **use_subsurf** (_boolean_ _,_ _(_ _optional_ _)_) – Export Subdivision Surface, Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if ‘Apply Modifiers’ is enabled)

*   **use_mesh_edges** (_boolean_ _,_ _(_ _optional_ _)_) – Loose Edges, Export loose edges (as two-vertices polygons)

*   **use_tspace** (_boolean_ _,_ _(_ _optional_ _)_) – Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)

*   **use_triangles** (_boolean_ _,_ _(_ _optional_ _)_) – Triangulate Faces, Convert all faces to triangles

*   **use_custom_props** (_boolean_ _,_ _(_ _optional_ _)_) – Custom Properties, Export custom properties

*   **add_leaf_bones** (_boolean_ _,_ _(_ _optional_ _)_) – Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)

*   **primary_bone_axis** (enum in [`'X'`, `'Y'`, `'Z'`, `'-X'`, `'-Y'`, `'-Z'`], (optional)) – Primary Bone Axis

*   **secondary_bone_axis** (enum in [`'X'`, `'Y'`, `'Z'`, `'-X'`, `'-Y'`, `'-Z'`], (optional)) – Secondary Bone Axis

*   **use_armature_deform_only** (_boolean_ _,_ _(_ _optional_ _)_) – Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)

*   **armature_nodetype** (enum in [`'NULL'`, `'ROOT'`, `'LIMBNODE'`], (optional)) –

Armature FBXNode Type, FBX type of node (object) used to represent Blender’s armatures (use the Null type unless you experience issues with the other app, as other choices may not import back perfectly into Blender…)

    *   `NULL` Null – ‘Null’ FBX node, similar to Blender’s Empty (default).

    *   `ROOT` Root – ‘Root’ FBX node, supposed to be the root of chains of bones….

    *   `LIMBNODE` LimbNode – ‘LimbNode’ FBX node, a regular joint between two bones….

*   **bake_anim** (_boolean_ _,_ _(_ _optional_ _)_) – Baked Animation, Export baked keyframe animation

*   **bake_anim_use_all_bones** (_boolean_ _,_ _(_ _optional_ _)_) – Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)

*   **bake_anim_use_nla_strips** (_boolean_ _,_ _(_ _optional_ _)_) – NLA Strips, Export each non-muted NLA strip as a separated FBX’s AnimStack, if any, instead of global scene animation

*   **bake_anim_use_all_actions** (_boolean_ _,_ _(_ _optional_ _)_) – All Actions, Export each action as a separated FBX’s AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)

*   **bake_anim_force_startend_keying** (_boolean_ _,_ _(_ _optional_ _)_) – Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels

*   **bake_anim_step** (_float in_ _[_ _0.01_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – Sampling Rate, How often to evaluate animated values (in frames)

*   **bake_anim_simplify_factor** (_float in_ _[_ _0_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)

*   **path_mode** (enum in [`'AUTO'`, `'ABSOLUTE'`, `'RELATIVE'`, `'MATCH'`, `'STRIP'`, `'COPY'`], (optional)) –

Path Mode, Method used to reference paths

    *   `AUTO` Auto – Use relative paths with subdirectories only.

    *   `ABSOLUTE` Absolute – Always write absolute paths.

    *   `RELATIVE` Relative – Write relative paths where possible.

    *   `MATCH` Match – Match absolute/relative setting with input path.

    *   `STRIP` Strip – Filename only.

    *   `COPY` Copy – Copy the file to the destination path (or subdirectory).

*   **embed_textures** (_boolean_ _,_ _(_ _optional_ _)_) – Embed Textures, Embed textures in FBX binary file (only for “Copy” path mode!)

*   **batch_mode** (enum in [`'OFF'`, `'SCENE'`, `'COLLECTION'`, `'SCENE_COLLECTION'`, `'ACTIVE_SCENE_COLLECTION'`], (optional)) –

Batch Mode

    *   `OFF` Off – Active scene to file.

    *   `SCENE` Scene – Each scene as a file.

    *   `COLLECTION` Collection – Each collection (data-block ones) as a file, does not include content of children collections.

    *   `SCENE_COLLECTION` Scene Collections – Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections.

    *   `ACTIVE_SCENE_COLLECTION` Active Scene Collections – Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections.

*   **use_batch_own_dir** (_boolean_ _,_ _(_ _optional_ _)_) – Batch Own Dir, Create a dir for each exported file

*   **use_metadata** (_boolean_ _,_ _(_ _optional_ _)_) – Use Metadata

*   **axis_forward** (enum in [`'X'`, `'Y'`, `'Z'`, `'-X'`, `'-Y'`, `'-Z'`], (optional)) – Forward

*   **axis_up** (enum in [`'X'`, `'Y'`, `'Z'`, `'-X'`, `'-Y'`, `'-Z'`], (optional)) – Up

File:
[addons_core/io_scene_fbx/__init__.py:598](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_fbx/__init__.py#L598)

bpy.ops.export_scene.gltf(_*_, _filepath=''_, _check\_existing=True_, _export\_import\_convert\_lighting\_mode='SPEC'_, _gltf\_export\_id=''_, _export\_use\_gltfpack=False_, _export\_gltfpack\_tc=True_, _export\_gltfpack\_tq=8_, _export\_gltfpack\_si=1.0_, _export\_gltfpack\_sa=False_, _export\_gltfpack\_slb=False_, _export\_gltfpack\_vp=14_, _export\_gltfpack\_vt=12_, _export\_gltfpack\_vn=8_, _export\_gltfpack\_vc=8_, _export\_gltfpack\_vpi='Integer'_, _export\_gltfpack\_noq=True_, _export\_gltfpack\_kn=False_, _export\_format=''_, _ui\_tab='GENERAL'_, _export\_copyright=''_, _export\_image\_format='AUTO'_, _export\_image\_add\_webp=False_, _export\_image\_webp\_fallback=False_, _export\_texture\_dir=''_, _export\_jpeg\_quality=75_, _export\_image\_quality=75_, _export\_keep\_originals=False_, _export\_texcoords=True_, _export\_normals=True_, _export\_gn\_mesh=False_, _export\_draco\_mesh\_compression\_enable=False_, _export\_draco\_mesh\_compression\_level=6_, _export\_draco\_position\_quantization=14_, _export\_draco\_normal\_quantization=10_, _export\_draco\_texcoord\_quantization=12_, _export\_draco\_color\_quantization=10_, _export\_draco\_generic\_quantization=12_, _export\_tangents=False_, _export\_materials='EXPORT'_, _export\_unused\_images=False_, _export\_unused\_textures=False_, _export\_vertex\_color='MATERIAL'_, _export\_vertex\_color\_name='Color'_, _export\_all\_vertex\_colors=True_, _export\_active\_vertex\_color\_when\_no\_material=True_, _export\_attributes=False_, _use\_mesh\_edges=False_, _use\_mesh\_vertices=False_, _export\_cameras=False_, _use\_selection=False_, _use\_visible=False_, _use\_renderable=False_, _use\_active\_collection\_with\_nested=True_, _use\_active\_collection=False_, _use\_active\_scene=False_, _collection=''_, _at\_collection\_center=False_, _export\_extras=False_, _export\_yup=True_, _export\_apply=False_, _export\_shared\_accessors=False_, _export\_animations=True_, _export\_frame\_range=False_, _export\_frame\_step=1_, _export\_force\_sampling=True_, _export\_sampling\_interpolation\_fallback='LINEAR'_, _export\_pointer\_animation=False_, _export\_animation\_mode='ACTIONS'_, _export\_nla\_strips\_merged\_animation\_name='Animation'_, _export\_def\_bones=False_, _export\_hierarchy\_flatten\_bones=False_, _export\_hierarchy\_flatten\_objs=False_, _export\_armature\_object\_remove=False_, _export\_leaf\_bone=False_, _export\_optimize\_animation\_size=True_, _export\_optimize\_animation\_keep\_anim\_armature=True_, _export\_optimize\_animation\_keep\_anim\_object=False_, _export\_optimize\_disable\_viewport=False_, _export\_negative\_frame='SLIDE'_, _export\_anim\_slide\_to\_zero=False_, _export\_bake\_animation=False_, _export\_merge\_animation='ACTION'_, _export\_anim\_single\_armature=True_, _export\_reset\_pose\_bones=True_, _export\_current\_frame=False_, _export\_rest\_position\_armature=True_, _export\_anim\_scene\_split\_object=True_, _export\_skins=True_, _export\_influence\_nb=4_, _export\_all\_influences=False_, _export\_morph=True_, _export\_morph\_normal=True_, _export\_morph\_tangent=False_, _export\_morph\_animation=True_, _export\_morph\_reset\_sk\_data=True_, _export\_lights=False_, _export\_try\_sparse\_sk=True_, _export\_try\_omit\_sparse\_sk=False_, _export\_gpu\_instances=False_, _export\_action\_filter=False_, _export\_convert\_animation\_pointer=False_, _export\_nla\_strips=True_, _export\_original\_specular=False_, _will\_save\_settings=False_, _export\_hierarchy\_full\_collections=False_, _export\_extra\_animations=False_, _export\_loglevel=-1_, _filter\_glob='*.glb'_)[¶](https://docs.blender.org/api/current/bpy.ops.export_scene.html#bpy.ops.export_scene.gltf "Link to this definition")
Export scene as glTF 2.0 file

Parameters:
*   **filepath** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – File Path, Filepath used for exporting the file

*   **check_existing** (_boolean_ _,_ _(_ _optional_ _)_) – Check Existing, Check and warn on overwriting existing files

*   **export_import_convert_lighting_mode** (enum in [`'SPEC'`, `'COMPAT'`, `'RAW'`], (optional)) –

Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights

    *   `SPEC` Standard – Physically-based glTF lighting units (cd, lx, nt).

    *   `COMPAT` Unitless – Non-physical, unitless lighting. Useful when exposure controls are not available.

    *   `RAW` Raw (Deprecated) – Blender lighting strengths with no conversion.

*   **gltf_export_id** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Identifier, Identifier of caller (in case of add-on calling this exporter). Can be useful in case of Extension added by other add-ons

*   **export_use_gltfpack** (_boolean_ _,_ _(_ _optional_ _)_) – Use Gltfpack, Use gltfpack to simplify the mesh and/or compress its textures

*   **export_gltfpack_tc** (_boolean_ _,_ _(_ _optional_ _)_) – KTX2 Compression, Convert all textures to KTX2 with BasisU supercompression

*   **export_gltfpack_tq** (_int in_ _[_ _1_ _,_ _10_ _]_ _,_ _(_ _optional_ _)_) – Texture Encoding Quality, Texture encoding quality

*   **export_gltfpack_si** (_float in_ _[_ _0_ _,_ _1_ _]_ _,_ _(_ _optional_ _)_) – Mesh Simplification Ratio, Simplify meshes targeting triangle count ratio

*   **export_gltfpack_sa** (_boolean_ _,_ _(_ _optional_ _)_) – Aggressive Mesh Simplification, Aggressively simplify to the target ratio disregarding quality

*   **export_gltfpack_slb** (_boolean_ _,_ _(_ _optional_ _)_) – Lock Mesh Border Vertices, Lock border vertices during simplification to avoid gaps on connected meshes

*   **export_gltfpack_vp** (_int in_ _[_ _1_ _,_ _16_ _]_ _,_ _(_ _optional_ _)_) – Position Quantization, Use N-bit quantization for positions

*   **export_gltfpack_vt** (_int in_ _[_ _1_ _,_ _16_ _]_ _,_ _(_ _optional_ _)_) – Texture Coordinate Quantization, Use N-bit quantization for texture coordinates

*   **export_gltfpack_vn** (_int in_ _[_ _1_ _,_ _16_ _]_ _,_ _(_ _optional_ _)_) – Normal/Tangent Quantization, Use N-bit quantization for normals and tangents

*   **export_gltfpack_vc** (_int in_ _[_ _1_ _,_ _16_ _]_ _,_ _(_ _optional_ _)_) – Vertex Color Quantization, Use N-bit quantization for colors

*   **export_gltfpack_vpi** (enum in [`'Integer'`, `'Normalized'`, `'Floating-point'`], (optional)) –

Vertex Position Attributes, Type to use for vertex position attributes

    *   `Integer` Integer – Use integer attributes for positions.

    *   `Normalized` Normalized – Use normalized attributes for positions.

    *   `Floating-point` Floating-point – Use floating-point attributes for positions.

*   **export_gltfpack_noq** (_boolean_ _,_ _(_ _optional_ _)_) – Disable Quantization, Disable quantization; produces much larger glTF files with no extensions

*   **export_gltfpack_kn** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Named Nodes, Restrict some optimization to keep named nodes and meshes attached to named nodes so that named nodes can be transformed externally

*   **export_format** (_enum in_ _[_ _]_ _,_ _(_ _optional_ _)_) – Format, Output format. Binary is most efficient, but JSON may be easier to edit later

*   **ui_tab** (enum in [`'GENERAL'`, `'MESHES'`, `'OBJECTS'`, `'ANIMATION'`], (optional)) –

ui_tab, Export setting categories

    *   `GENERAL` General – General settings.

    *   `MESHES` Meshes – Mesh settings.

    *   `OBJECTS` Objects – Object settings.

    *   `ANIMATION` Animation – Animation settings.

*   **export_copyright** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Copyright, Legal rights and conditions for the model

*   **export_image_format** (enum in [`'AUTO'`, `'JPEG'`, `'WEBP'`, `'NONE'`], (optional)) –

Images, Output format for images. PNG is lossless and generally preferred, but JPEG might be preferable for web applications due to the smaller file size. Alternatively they can be omitted if they are not needed

    *   `AUTO` Automatic – Save PNGs as PNGs, JPEGs as JPEGs, WebPs as WebPs. For other formats, use PNG.

    *   `JPEG` JPEG Format (.jpg) – Save images as JPEGs. (Images that need alpha are saved as PNGs though.) Be aware of a possible loss in quality.

    *   `WEBP` WebP Format – Save images as WebPs as main image (no fallback).

    *   `NONE` None – Don’t export images.

*   **export_image_add_webp** (_boolean_ _,_ _(_ _optional_ _)_) – Create WebP, Creates WebP textures for every texture. For already WebP textures, nothing happens

*   **export_image_webp_fallback** (_boolean_ _,_ _(_ _optional_ _)_) – WebP Fallback, For all WebP textures, create a PNG fallback texture

*   **export_texture_dir** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Textures, Folder to place texture files in. Relative to the .gltf file

*   **export_jpeg_quality** (_int in_ _[_ _0_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – JPEG Quality, Quality of JPEG export

*   **export_image_quality** (_int in_ _[_ _0_ _,_ _100_ _]_ _,_ _(_ _optional_ _)_) – Image Quality, Quality of image export

*   **export_keep_originals** (_boolean_ _,_ _(_ _optional_ _)_) – Keep Original, Keep original textures files if possible. WARNING: if you use more than one texture, where pbr standard requires only one, only one texture will be used. This can lead to unexpected results

*   **export_texcoords** (_boolean_ _,_ _(_ _optional_ _)_) – UVs, Export UVs (texture coordinates) with meshes

*   **export_normals** (_boolean_ _,_ _(_ _optional_ _)_) – Normals, Export vertex normals with meshes

*   **export_gn_mesh** (_boolean_ _,_ _(_ _optional_ _)_) – Geometry Nodes Instances (Experimental), Export Geometry nodes instance meshes

*   **export_draco_mesh_compression_enable** (_boolean_ _,_ _(_ _optional_ _)_) – Draco Mesh Compression, Compress mesh using Draco

*   **export_draco_mesh_compression_level** (_int in_ _[_ _0_ _,_ _10_ _]_ _,_ _(_ _optional_ _)_) – Compression Level, Compression level (0 = most speed, 6 = most compression, higher values currently not supported)

*   **export_draco_position_quantization** (_int in_ _[_ _0_ _,_ _30_ _]_ _,_ _(_ _optional_ _)_) – Position Quantization Bits, Quantization bits for position values (0 = no quantization)

*   **export_draco_normal_quantization** (_int in_ _[_ _0_ _,_ _30_ _]_ _,_ _(_ _optional_ _)_) – Normal Quantization Bits, Quantization bits for normal values (0 = no quantization)

*   **export_draco_texcoord_quantization** (_int in_ _[_ _0_ _,_ _30_ _]_ _,_ _(_ _optional_ _)_) – Texcoord Quantization Bits, Quantization bits for texture coordinate values (0 = no quantization)

*   **export_draco_color_quantization** (_int in_ _[_ _0_ _,_ _30_ _]_ _,_ _(_ _optional_ _)_) – Color Quantization Bits, Quantization bits for color values (0 = no quantization)

*   **export_draco_generic_quantization** (_int in_ _[_ _0_ _,_ _30_ _]_ _,_ _(_ _optional_ _)_) – Generic Quantization Bits, Quantization bits for generic values like weights or joints (0 = no quantization)

*   **export_tangents** (_boolean_ _,_ _(_ _optional_ _)_) – Tangents, Export vertex tangents with meshes

*   **export_materials** (enum in [`'EXPORT'`, `'PLACEHOLDER'`, `'VIEWPORT'`, `'NONE'`], (optional)) –

Materials, Export materials

    *   `EXPORT` Export – Export all materials used by included objects.

    *   `PLACEHOLDER` Placeholder – Do not export materials, but write multiple primitive groups per mesh, keeping material slot information.

    *   `VIEWPORT` Viewport – Export minimal materials as defined in Viewport display properties.

    *   `NONE` No export – Do not export materials, and combine mesh primitive groups, losing material slot information.

*   **export_unused_images** (_boolean_ _,_ _(_ _optional_ _)_) – Unused Images, Export images not assigned to any material

*   **export_unused_textures** (_boolean_ _,_ _(_ _optional_ _)_) – Prepare Unused Textures, Export image texture nodes not assigned to any material. This feature is not standard and needs an external extension to be included in the glTF file

*   **export_vertex_color** (enum in [`'MATERIAL'`, `'ACTIVE'`, `'NAME'`, `'NONE'`], (optional)) –

Use Vertex Color, How to export vertex color

    *   `MATERIAL` Material – Export vertex color when used by material.

    *   `ACTIVE` Active – Export active vertex color.

    *   `NAME` Name – Export vertex color with this name.

    *   `NONE` None – Do not export vertex color.

*   **export_vertex_color_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Vertex Color Name, Name of vertex color to export

*   **export_all_vertex_colors** (_boolean_ _,_ _(_ _optional_ _)_) – Export All Vertex Colors, Export all vertex colors, even if not used by any material. If no Vertex Color is used in the mesh materials, a fake COLOR_0 will be created, in order to keep material unchanged

*   **export_active_vertex_color_when_no_material** (_boolean_ _,_ _(_ _optional_ _)_) – Export Active Vertex Color When No Material, When there is no material on object, export active vertex color

*   **export_attributes** (_boolean_ _,_ _(_ _optional_ _)_) – Attributes, Export Attributes (when starting with underscore)

*   **use_mesh_edges** (_boolean_ _,_ _(_ _optional_ _)_) – Loose Edges, Export loose edges as lines, using the material from the first material slot

*   **use_mesh_vertices** (_boolean_ _,_ _(_ _optional_ _)_) – Loose Points, Export loose points as glTF points, using the material from the first material slot

*   **export_cameras** (_boolean_ _,_ _(_ _optional_ _)_) – Cameras, Export cameras

*   **use_selection** (_boolean_ _,_ _(_ _optional_ _)_) – Selected Objects, Export selected objects only

*   **use_visible** (_boolean_ _,_ _(_ _optional_ _)_) – Visible Objects, Export visible objects only

*   **use_renderable** (_boolean_ _,_ _(_ _optional_ _)_) – Renderable Objects, Export renderable objects only

*   **use_active_collection_with_nested** (_boolean_ _,_ _(_ _optional_ _)_) – Include Nested Collections, Include active collection and nested collections

*   **use_active_collection** (_boolean_ _,_ _(_ _optional_ _)_) – Active Collection, Export objects in the active collection only

*   **use_active_scene** (_boolean_ _,_ _(_ _optional_ _)_) – Active Scene, Export active scene only

*   **collection** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Source Collection, Export only objects from this collection (and its children)

*   **at_collection_center** (_boolean_ _,_ _(_ _optional_ _)_) – Export at Collection Center, Export at Collection center of mass of root objects of the collection

*   **export_extras** (_boolean_ _,_ _(_ _optional_ _)_) – Custom Properties, Export custom properties as glTF extras

*   **export_yup** (_boolean_ _,_ _(_ _optional_ _)_) – +Y Up, Export using glTF convention, +Y up

*   **export_apply** (_boolean_ _,_ _(_ _optional_ _)_) – Apply Modifiers, Apply modifiers (excluding Armatures) to mesh objects -WARNING: prevents exporting shape keys

*   **export_shared_accessors** (_boolean_ _,_ _(_ _optional_ _)_) – Shared Accessors, Export Primitives using shared accessors for attributes

*   **export_animations** (_boolean_ _,_ _(_ _optional_ _)_) – Animations, Exports active actions and NLA tracks as glTF animations

*   **export_frame_range** (_boolean_ _,_ _(_ _optional_ _)_) – Limit to Playback Range, Clips animations to selected playback range

*   **export_frame_step** (_int in_ _[_ _1_ _,_ _120_ _]_ _,_ _(_ _optional_ _)_) – Sampling Rate, How often to evaluate animated values (in frames)

*   **export_force_sampling** (_boolean_ _,_ _(_ _optional_ _)_) – Always Sample Animations, Apply sampling to all animations

*   **export_sampling_interpolation_fallback** (enum in [`'LINEAR'`, `'STEP'`], (optional)) –

Sampling Interpolation Fallback, Interpolation fallback for sampled animations, when the property is not keyed

    *   `LINEAR` Linear – Linear interpolation between keyframes.

    *   `STEP` Step – No interpolation between keyframes.

*   **export_pointer_animation** (_boolean_ _,_ _(_ _optional_ _)_) – Export Animation Pointer (Experimental), Export material, Light & Camera animation as Animation Pointer. Available only for baked animation mode ‘NLA Tracks’ and ‘Scene’

*   **export_animation_mode** (enum in [`'ACTIONS'`, `'ACTIVE_ACTIONS'`, `'BROADCAST'`, `'NLA_TRACKS'`, `'SCENE'`], (optional)) –

Animation Mode, Export Animation mode

    *   `ACTIONS` Actions – Export actions (actives and on NLA tracks) as separate animations.

    *   `ACTIVE_ACTIONS` Active actions merged – All the currently assigned actions become one glTF animation.

    *   `BROADCAST` Broadcast actions – Broadcast all compatible actions to all objects. Animated objects will get all actions compatible with them, others will get no animation at all.

    *   `NLA_TRACKS` NLA Tracks – Export individual NLA Tracks as separate animation.

    *   `SCENE` Scene – Export baked scene as a single animation.

*   **export_nla_strips_merged_animation_name** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – Merged Animation Name, Name of single glTF animation to be exported

*   **export_def_bones** (_boolean_ _,_ _(_ _optional_ _)_) – Export Deformation Bones Only, Export Deformation bones only

*   **export_hierarchy_flatten_bones** (_boolean_ _,_ _(_ _optional_ _)_) – Flatten Bone Hierarchy, Flatten Bone Hierarchy. Useful in case of non decomposable transformation matrix

*   **export_hierarchy_flatten_objs** (_boolean_ _,_ _(_ _optional_ _)_) – Flatten Object Hierarchy, Flatten Object Hierarchy. Useful in case of non decomposable transformation matrix

*   **export_armature_object_remove** (_boolean_ _,_ _(_ _optional_ _)_) – Remove Armature Object, Remove Armature object if possible. If Armature has multiple root bones, object will not be removed

*   **export_leaf_bone** (_boolean_ _,_ _(_ _optional_ _)_) – Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)

*   **export_optimize_animation_size** (_boolean_ _,_ _(_ _optional_ _)_) – Optimize Animation Size, Reduce exported file size by removing duplicate keyframes

*   **export_optimize_animation_keep_anim_armature** (_boolean_ _,_ _(_ _optional_ _)_) – Force Keeping Channels for Bones, If all keyframes are identical in a rig, force keeping the minimal animation. When off, all possible channels for the bones will be exported, even if empty (minimal animation, 2 keyframes)

*   **export_optimize_animation_keep_anim_object** (_boolean_ _,_ _(_ _optional_ _)_) – Force Keeping Channel for Objects, If all keyframes are identical for object transformations, force keeping the minimal animation

*   **export_optimize_disable_viewport** (_boolean_ _,_ _(_ _optional_ _)_) – Disable Viewport for Other Objects, When exporting animations, disable viewport for other objects, for performance

*   **export_negative_frame** (enum in [`'SLIDE'`, `'CROP'`], (optional)) –

Negative Frames, Negative Frames are slid or cropped

    *   `SLIDE` Slide – Slide animation to start at frame 0.

    *   `CROP` Crop – Keep only frames above frame 0.

*   **export_anim_slide_to_zero** (_boolean_ _,_ _(_ _optional_ _)_) – Set All glTF Animation Starting at 0, Set all glTF animation starting at 0.0s. Can be useful for looping animations

*   **export_bake_animation** (_boolean_ _,_ _(_ _optional_ _)_) – Bake All Objects Animations, Force exporting animation on every object. Can be useful when using constraints or driver. Also useful when exporting only selection

*   **export_merge_animation** (enum in [`'NLA_TRACK'`, `'ACTION'`, `'NONE'`], (optional)) –

Merge Animation, Merge Animations

    *   `NLA_TRACK` NLA Track Names – Merge by NLA Track Names.

    *   `ACTION` Actions – Merge by Actions.

    *   `NONE` No Merge – Do Not Merge Animations.

*   **export_anim_single_armature** (_boolean_ _,_ _(_ _optional_ _)_) – Export all Armature Actions, Export all actions, bound to a single armature. WARNING: Option does not support exports including multiple armatures

*   **export_reset_pose_bones** (_boolean_ _,_ _(_ _optional_ _)_) – Reset Pose Bones Between Actions, Reset pose bones between each action exported. This is needed when some bones are not keyed on some animations

*   **export_current_frame** (_boolean_ _,_ _(_ _optional_ _)_) – Use Current Frame as Object Rest Transformations, Export the scene in the current animation frame. When off, frame 0 is used as rest transformations for objects

*   **export_rest_position_armature** (_boolean_ _,_ _(_ _optional_ _)_) – Use Rest Position Armature, Export armatures using rest position as joints’ rest pose. When off, current frame pose is used as rest pose

*   **export_anim_scene_split_object** (_boolean_ _,_ _(_ _optional_ _)_) – Split Animation by Object, Export Scene as seen in Viewport, But split animation by Object

*   **export_skins** (_boolean_ _,_ _(_ _optional_ _)_) – Skinning, Export skinning (armature) data

*   **export_influence_nb** (_int in_ _[_ _1_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Bone Influences, Choose how many Bone influences to export

*   **export_all_influences** (_boolean_ _,_ _(_ _optional_ _)_) – Include All Bone Influences, Allow export of all joint vertex influences. Models may appear incorrectly in many viewers

*   **export_morph** (_boolean_ _,_ _(_ _optional_ _)_) – Shape Keys, Export shape keys (morph targets)

*   **export_morph_normal** (_boolean_ _,_ _(_ _optional_ _)_) – Shape Key Normals, Export vertex normals with shape keys (morph targets)

*   **export_morph_tangent** (_boolean_ _,_ _(_ _optional_ _)_) – Shape Key Tangents, Export vertex tangents with shape keys (morph targets)

*   **export_morph_animation** (_boolean_ _,_ _(_ _optional_ _)_) – Shape Key Animations, Export shape keys animations (morph targets)

*   **export_morph_reset_sk_data** (_boolean_ _,_ _(_ _optional_ _)_) – Reset Shape Keys Between Actions, Reset shape keys between each action exported. This is needed when some SK channels are not keyed on some animations

*   **export_lights** (_boolean_ _,_ _(_ _optional_ _)_) – Punctual Lights, Export directional, point, and spot lights. Uses “KHR_lights_punctual” glTF extension

*   **export_try_sparse_sk** (_boolean_ _,_ _(_ _optional_ _)_) – Use Sparse Accessor if Better, Try using Sparse Accessor if it saves space

*   **export_try_omit_sparse_sk** (_boolean_ _,_ _(_ _optional_ _)_) – Omitting Sparse Accessor if Data is Empty, Omitting Sparse Accessor if data is empty

*   **export_gpu_instances** (_boolean_ _,_ _(_ _optional_ _)_) – GPU Instances, Export using EXT_mesh_gpu_instancing. Limited to children of a given Empty. Multiple materials might be omitted

*   **export_action_filter** (_boolean_ _,_ _(_ _optional_ _)_) – Filter Actions, Filter Actions to be exported

*   **export_convert_animation_pointer** (_boolean_ _,_ _(_ _optional_ _)_) – Convert TRS/Weights to Animation Pointer, Export TRS and weights as Animation Pointer. Using KHR_animation_pointer extension

*   **export_nla_strips** (_boolean_ _,_ _(_ _optional_ _)_) – Group by NLA Track, When on, multiple actions become part of the same glTF animation if they’re pushed onto NLA tracks with the same name. When off, all the currently assigned actions become one glTF animation

*   **export_original_specular** (_boolean_ _,_ _(_ _optional_ _)_) – Export Original PBR Specular, Export original glTF PBR Specular, instead of Blender Principled Shader Specular

*   **will_save_settings** (_boolean_ _,_ _(_ _optional_ _)_) – Remember Export Settings, Store glTF export settings in the Blender project

*   **export_hierarchy_full_collections** (_boolean_ _,_ _(_ _optional_ _)_) – Full Collection Hierarchy, Export full hierarchy, including intermediate collections

*   **export_extra_animations** (_boolean_ _,_ _(_ _optional_ _)_) – Prepare Extra Animations, Export additional animations.This feature is not standard and needs an external extension to be included in the glTF file

*   **export_loglevel** (_int in_ _[_ _-inf_ _,_ _inf_ _]_ _,_ _(_ _optional_ _)_) – Log Level, Log Level

*   **filter_glob** (_string_ _,_ _(_ _optional_ _,_ _never None_ _)_) – filter_glob

File:
[addons_core/io_scene_gltf2/__init__.py:1084](https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/__init__.py#L1084)

[Next Extensions Operators](https://docs.blender.org/api/current/bpy.ops.extensions.html)[Previous Export Anim Operators](https://docs.blender.org/api/current/bpy.ops.export_anim.html)

 Copyright © Blender Authors 

 Made with [Furo](https://github.com/pradyunsg/furo)

*   [Report issue on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.export_scene.rst%60%0D%0ABlender+Version%3A+%605.0%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F5.0%2Fbpy.ops.export_scene.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

 On this page 

*   [Export Scene Operators](https://docs.blender.org/api/current/bpy.ops.export_scene.html#)
    *   [`fbx()`](https://docs.blender.org/api/current/bpy.ops.export_scene.html#bpy.ops.export_scene.fbx)
    *   [`gltf()`](https://docs.blender.org/api/current/bpy.ops.export_scene.html#bpy.ops.export_scene.gltf)
