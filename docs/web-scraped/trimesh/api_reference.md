# trimesh¶

  * [trimesh.exchange](trimesh.exchange.html)
    * [trimesh.exchange.gltf](trimesh.exchange.gltf.html)
      * [trimesh.exchange.gltf.extensions](trimesh.exchange.gltf.extensions.html)
        * [gltf_extensions.py](trimesh.exchange.gltf.extensions.html#gltf-extensions-py)
        * [`MaterialContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext)
          * [`MaterialContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.data)
          * [`MaterialContext.images`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.images)
          * [`MaterialContext.parse_textures`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.parse_textures)
        * [`PrimitiveContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext)
          * [`PrimitiveContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.accessors)
          * [`PrimitiveContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.data)
          * [`PrimitiveContext.mesh_kwargs`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.mesh_kwargs)
          * [`PrimitiveContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.primitive)
        * [`PrimitiveExportContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext)
          * [`PrimitiveExportContext.buffer_items`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.buffer_items)
          * [`PrimitiveExportContext.include_normals`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.include_normals)
          * [`PrimitiveExportContext.mesh`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.mesh)
          * [`PrimitiveExportContext.name`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.name)
          * [`PrimitiveExportContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.primitive)
          * [`PrimitiveExportContext.tree`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.tree)
        * [`PrimitivePreprocessContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext)
          * [`PrimitivePreprocessContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.accessors)
          * [`PrimitivePreprocessContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.data)
          * [`PrimitivePreprocessContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.primitive)
          * [`PrimitivePreprocessContext.views`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.views)
        * [`TextureSourceContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext)
          * [`TextureSourceContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext.data)
        * [`handle_extensions()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.handle_extensions)
        * [`register_handler()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.register_handler)
      * [gltf/__init__.py](trimesh.exchange.gltf.html#gltf-init-py)
      * [`export_glb()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.export_glb)
      * [`export_gltf()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.export_gltf)
      * [`get_schema()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.get_schema)
      * [`load_glb()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.load_glb)
      * [`load_gltf()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.load_gltf)
      * [`validate()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.validate)
    * [trimesh.exchange.binvox](trimesh.exchange.binvox.html)
      * [`Binvox`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox)
        * [`Binvox.rle_data`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.rle_data)
        * [`Binvox.scale`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.scale)
        * [`Binvox.shape`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.shape)
        * [`Binvox.translate`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.translate)
      * [`Binvoxer`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer)
        * [`Binvoxer.SUPPORTED_INPUT_TYPES`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.SUPPORTED_INPUT_TYPES)
        * [`Binvoxer.SUPPORTED_OUTPUT_TYPES`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.SUPPORTED_OUTPUT_TYPES)
        * [`Binvoxer.__init__()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.__init__)
        * [`Binvoxer.file_type`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.file_type)
      * [`binvox_bytes()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.binvox_bytes)
      * [`binvox_header()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.binvox_header)
      * [`export_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.export_binvox)
      * [`load_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.load_binvox)
      * [`parse_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.parse_binvox)
      * [`voxel_from_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.voxel_from_binvox)
      * [`voxelize_mesh()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.voxelize_mesh)
    * [trimesh.exchange.cascade](trimesh.exchange.cascade.html)
      * [`load_step()`](trimesh.exchange.cascade.html#trimesh.exchange.cascade.load_step)
    * [trimesh.exchange.dae](trimesh.exchange.dae.html)
      * [`export_collada()`](trimesh.exchange.dae.html#trimesh.exchange.dae.export_collada)
      * [`load_collada()`](trimesh.exchange.dae.html#trimesh.exchange.dae.load_collada)
      * [`load_zae()`](trimesh.exchange.dae.html#trimesh.exchange.dae.load_zae)
    * [trimesh.exchange.export](trimesh.exchange.export.html)
      * [`export_dict()`](trimesh.exchange.export.html#trimesh.exchange.export.export_dict)
      * [`export_dict64()`](trimesh.exchange.export.html#trimesh.exchange.export.export_dict64)
      * [`export_mesh()`](trimesh.exchange.export.html#trimesh.exchange.export.export_mesh)
      * [`export_scene()`](trimesh.exchange.export.html#trimesh.exchange.export.export_scene)
      * [`scene_to_dict()`](trimesh.exchange.export.html#trimesh.exchange.export.scene_to_dict)
    * [trimesh.exchange.load](trimesh.exchange.load.html)
      * [`available_formats()`](trimesh.exchange.load.html#trimesh.exchange.load.available_formats)
      * [`load()`](trimesh.exchange.load.html#trimesh.exchange.load.load)
      * [`load_mesh()`](trimesh.exchange.load.html#trimesh.exchange.load.load_mesh)
      * [`load_remote()`](trimesh.exchange.load.html#trimesh.exchange.load.load_remote)
      * [`load_scene()`](trimesh.exchange.load.html#trimesh.exchange.load.load_scene)
      * [`mesh_formats()`](trimesh.exchange.load.html#trimesh.exchange.load.mesh_formats)
    * [trimesh.exchange.misc](trimesh.exchange.misc.html)
      * [`load_dict()`](trimesh.exchange.misc.html#trimesh.exchange.misc.load_dict)
      * [`load_meshio()`](trimesh.exchange.misc.html#trimesh.exchange.misc.load_meshio)
    * [trimesh.exchange.obj](trimesh.exchange.obj.html)
      * [`export_obj()`](trimesh.exchange.obj.html#trimesh.exchange.obj.export_obj)
      * [`load_obj()`](trimesh.exchange.obj.html#trimesh.exchange.obj.load_obj)
      * [`parse_mtl()`](trimesh.exchange.obj.html#trimesh.exchange.obj.parse_mtl)
    * [trimesh.exchange.off](trimesh.exchange.off.html)
      * [`export_off()`](trimesh.exchange.off.html#trimesh.exchange.off.export_off)
      * [`load_off()`](trimesh.exchange.off.html#trimesh.exchange.off.load_off)
    * [trimesh.exchange.ply](trimesh.exchange.ply.html)
      * [`export_draco()`](trimesh.exchange.ply.html#trimesh.exchange.ply.export_draco)
      * [`export_ply()`](trimesh.exchange.ply.html#trimesh.exchange.ply.export_ply)
      * [`load_draco()`](trimesh.exchange.ply.html#trimesh.exchange.ply.load_draco)
      * [`load_ply()`](trimesh.exchange.ply.html#trimesh.exchange.ply.load_ply)
    * [trimesh.exchange.stl](trimesh.exchange.stl.html)
      * [`HeaderError`](trimesh.exchange.stl.html#trimesh.exchange.stl.HeaderError)
      * [`export_stl()`](trimesh.exchange.stl.html#trimesh.exchange.stl.export_stl)
      * [`export_stl_ascii()`](trimesh.exchange.stl.html#trimesh.exchange.stl.export_stl_ascii)
      * [`load_stl()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl)
      * [`load_stl_ascii()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl_ascii)
      * [`load_stl_binary()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl_binary)
    * [trimesh.exchange.threedxml](trimesh.exchange.threedxml.html)
      * [threedxml.py](trimesh.exchange.threedxml.html#threedxml-py)
      * [`load_3DXML()`](trimesh.exchange.threedxml.html#trimesh.exchange.threedxml.load_3DXML)
      * [`print_element()`](trimesh.exchange.threedxml.html#trimesh.exchange.threedxml.print_element)
    * [trimesh.exchange.threemf](trimesh.exchange.threemf.html)
      * [`export_3MF()`](trimesh.exchange.threemf.html#trimesh.exchange.threemf.export_3MF)
      * [`load_3MF()`](trimesh.exchange.threemf.html#trimesh.exchange.threemf.load_3MF)
    * [trimesh.exchange.urdf](trimesh.exchange.urdf.html)
      * [`export_urdf()`](trimesh.exchange.urdf.html#trimesh.exchange.urdf.export_urdf)
    * [trimesh.exchange.xaml](trimesh.exchange.xaml.html)
      * [xaml.py](trimesh.exchange.xaml.html#xaml-py)
      * [`load_XAML()`](trimesh.exchange.xaml.html#trimesh.exchange.xaml.load_XAML)
    * [trimesh.exchange.xyz](trimesh.exchange.xyz.html)
      * [`export_xyz()`](trimesh.exchange.xyz.html#trimesh.exchange.xyz.export_xyz)
      * [`load_xyz()`](trimesh.exchange.xyz.html#trimesh.exchange.xyz.load_xyz)
    * [trimesh/exchange](trimesh.exchange.html#module-trimesh.exchange)
  * [trimesh.interfaces](trimesh.interfaces.html)
    * [trimesh.interfaces.blender](trimesh.interfaces.blender.html)
      * [`boolean()`](trimesh.interfaces.blender.html#trimesh.interfaces.blender.boolean)
      * [`unwrap()`](trimesh.interfaces.blender.html#trimesh.interfaces.blender.unwrap)
    * [trimesh.interfaces.generic](trimesh.interfaces.generic.html)
      * [`MeshScript`](trimesh.interfaces.generic.html#trimesh.interfaces.generic.MeshScript)
        * [`MeshScript.__init__()`](trimesh.interfaces.generic.html#trimesh.interfaces.generic.MeshScript.__init__)
        * [`MeshScript.run()`](trimesh.interfaces.generic.html#trimesh.interfaces.generic.MeshScript.run)
  * [trimesh.path](trimesh.path.html)
    * [trimesh.path.exchange](trimesh.path.exchange.html)
      * [trimesh.path.exchange.dxf](trimesh.path.exchange.dxf.html)
        * [`bulge_to_arcs()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.bulge_to_arcs)
        * [`convert_entities()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.convert_entities)
        * [`export_dxf()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.export_dxf)
        * [`get_key()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.get_key)
        * [`load_dxf()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.load_dxf)
      * [trimesh.path.exchange.export](trimesh.path.exchange.export.html)
        * [`export_dict()`](trimesh.path.exchange.export.html#trimesh.path.exchange.export.export_dict)
        * [`export_path()`](trimesh.path.exchange.export.html#trimesh.path.exchange.export.export_path)
      * [trimesh.path.exchange.load](trimesh.path.exchange.load.html)
        * [`load_path()`](trimesh.path.exchange.load.html#trimesh.path.exchange.load.load_path)
        * [`path_formats()`](trimesh.path.exchange.load.html#trimesh.path.exchange.load.path_formats)
      * [trimesh.path.exchange.misc](trimesh.path.exchange.misc.html)
        * [`dict_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.dict_to_path)
        * [`edges_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.edges_to_path)
        * [`faces_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.faces_to_path)
        * [`lines_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.lines_to_path)
        * [`linestrings_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.linestrings_to_path)
        * [`polygon_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.polygon_to_path)
      * [trimesh.path.exchange.svg_io](trimesh.path.exchange.svg_io.html)
        * [`element_transform()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.element_transform)
        * [`export_svg()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.export_svg)
        * [`svg_to_path()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.svg_to_path)
        * [`transform_to_matrices()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.transform_to_matrices)
    * [trimesh.path.arc](trimesh.path.arc.html)
      * [`ArcInfo`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo)
        * [`ArcInfo.__init__()`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.__init__)
        * [`ArcInfo.angles`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.angles)
        * [`ArcInfo.center`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.center)
        * [`ArcInfo.normal`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.normal)
        * [`ArcInfo.radius`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.radius)
        * [`ArcInfo.span`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.span)
      * [`arc_center()`](trimesh.path.arc.html#trimesh.path.arc.arc_center)
      * [`discretize_arc()`](trimesh.path.arc.html#trimesh.path.arc.discretize_arc)
      * [`to_threepoint()`](trimesh.path.arc.html#trimesh.path.arc.to_threepoint)
    * [trimesh.path.creation](trimesh.path.creation.html)
      * [`box_outline()`](trimesh.path.creation.html#trimesh.path.creation.box_outline)
      * [`circle()`](trimesh.path.creation.html#trimesh.path.creation.circle)
      * [`circle_pattern()`](trimesh.path.creation.html#trimesh.path.creation.circle_pattern)
      * [`grid()`](trimesh.path.creation.html#trimesh.path.creation.grid)
      * [`rectangle()`](trimesh.path.creation.html#trimesh.path.creation.rectangle)
    * [trimesh.path.curve](trimesh.path.curve.html)
      * [`binomial()`](trimesh.path.curve.html#trimesh.path.curve.binomial)
      * [`discretize_bezier()`](trimesh.path.curve.html#trimesh.path.curve.discretize_bezier)
      * [`discretize_bspline()`](trimesh.path.curve.html#trimesh.path.curve.discretize_bspline)
    * [trimesh.path.entities](trimesh.path.entities.html)
      * [entities.py](trimesh.path.entities.html#entities-py)
      * [`Arc`](trimesh.path.entities.html#trimesh.path.entities.Arc)
        * [`Arc.bounds()`](trimesh.path.entities.html#trimesh.path.entities.Arc.bounds)
        * [`Arc.center()`](trimesh.path.entities.html#trimesh.path.entities.Arc.center)
        * [`Arc.closed`](trimesh.path.entities.html#trimesh.path.entities.Arc.closed)
        * [`Arc.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Arc.discrete)
        * [`Arc.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Arc.is_valid)
        * [`Arc.length()`](trimesh.path.entities.html#trimesh.path.entities.Arc.length)
      * [`BSpline`](trimesh.path.entities.html#trimesh.path.entities.BSpline)
        * [`BSpline.__init__()`](trimesh.path.entities.html#trimesh.path.entities.BSpline.__init__)
        * [`BSpline.discrete()`](trimesh.path.entities.html#trimesh.path.entities.BSpline.discrete)
        * [`BSpline.to_dict()`](trimesh.path.entities.html#trimesh.path.entities.BSpline.to_dict)
      * [`Bezier`](trimesh.path.entities.html#trimesh.path.entities.Bezier)
        * [`Bezier.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Bezier.discrete)
      * [`Curve`](trimesh.path.entities.html#trimesh.path.entities.Curve)
        * [`Curve.nodes`](trimesh.path.entities.html#trimesh.path.entities.Curve.nodes)
      * [`Entity`](trimesh.path.entities.html#trimesh.path.entities.Entity)
        * [`Entity.__init__()`](trimesh.path.entities.html#trimesh.path.entities.Entity.__init__)
        * [`Entity.bounds()`](trimesh.path.entities.html#trimesh.path.entities.Entity.bounds)
        * [`Entity.closed`](trimesh.path.entities.html#trimesh.path.entities.Entity.closed)
        * [`Entity.copy()`](trimesh.path.entities.html#trimesh.path.entities.Entity.copy)
        * [`Entity.end_points`](trimesh.path.entities.html#trimesh.path.entities.Entity.end_points)
        * [`Entity.explode()`](trimesh.path.entities.html#trimesh.path.entities.Entity.explode)
        * [`Entity.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Entity.is_valid)
        * [`Entity.layer`](trimesh.path.entities.html#trimesh.path.entities.Entity.layer)
        * [`Entity.length()`](trimesh.path.entities.html#trimesh.path.entities.Entity.length)
        * [`Entity.metadata`](trimesh.path.entities.html#trimesh.path.entities.Entity.metadata)
        * [`Entity.nodes`](trimesh.path.entities.html#trimesh.path.entities.Entity.nodes)
        * [`Entity.reverse()`](trimesh.path.entities.html#trimesh.path.entities.Entity.reverse)
        * [`Entity.to_dict()`](trimesh.path.entities.html#trimesh.path.entities.Entity.to_dict)
      * [`Line`](trimesh.path.entities.html#trimesh.path.entities.Line)
        * [`Line.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Line.discrete)
        * [`Line.explode()`](trimesh.path.entities.html#trimesh.path.entities.Line.explode)
        * [`Line.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Line.is_valid)
        * [`Line.to_dict()`](trimesh.path.entities.html#trimesh.path.entities.Line.to_dict)
      * [`Text`](trimesh.path.entities.html#trimesh.path.entities.Text)
        * [`Text.__init__()`](trimesh.path.entities.html#trimesh.path.entities.Text.__init__)
        * [`Text.angle()`](trimesh.path.entities.html#trimesh.path.entities.Text.angle)
        * [`Text.closed`](trimesh.path.entities.html#trimesh.path.entities.Text.closed)
        * [`Text.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Text.discrete)
        * [`Text.end_points`](trimesh.path.entities.html#trimesh.path.entities.Text.end_points)
        * [`Text.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Text.is_valid)
        * [`Text.length()`](trimesh.path.entities.html#trimesh.path.entities.Text.length)
        * [`Text.nodes`](trimesh.path.entities.html#trimesh.path.entities.Text.nodes)
        * [`Text.normal`](trimesh.path.entities.html#trimesh.path.entities.Text.normal)
        * [`Text.origin`](trimesh.path.entities.html#trimesh.path.entities.Text.origin)
        * [`Text.plot()`](trimesh.path.entities.html#trimesh.path.entities.Text.plot)
        * [`Text.vector`](trimesh.path.entities.html#trimesh.path.entities.Text.vector)
    * [trimesh.path.intersections](trimesh.path.intersections.html)
      * [`line_line()`](trimesh.path.intersections.html#trimesh.path.intersections.line_line)
    * [trimesh.path.packing](trimesh.path.packing.html)
      * [packing.py](trimesh.path.packing.html#packing-py)
      * [`RectangleBin`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin)
        * [`RectangleBin.__init__()`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin.__init__)
        * [`RectangleBin.extents`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin.extents)
        * [`RectangleBin.insert()`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin.insert)
      * [`bounds_overlap()`](trimesh.path.packing.html#trimesh.path.packing.bounds_overlap)
      * [`images()`](trimesh.path.packing.html#trimesh.path.packing.images)
      * [`meshes()`](trimesh.path.packing.html#trimesh.path.packing.meshes)
      * [`paths()`](trimesh.path.packing.html#trimesh.path.packing.paths)
      * [`polygons()`](trimesh.path.packing.html#trimesh.path.packing.polygons)
      * [`rectangles()`](trimesh.path.packing.html#trimesh.path.packing.rectangles)
      * [`rectangles_single()`](trimesh.path.packing.html#trimesh.path.packing.rectangles_single)
      * [`roll_transform()`](trimesh.path.packing.html#trimesh.path.packing.roll_transform)
      * [`visualize()`](trimesh.path.packing.html#trimesh.path.packing.visualize)
    * [trimesh.path.path](trimesh.path.path.html)
      * [path.py](trimesh.path.path.html#path-py)
      * [`Path`](trimesh.path.path.html#trimesh.path.path.Path)
        * [`Path.__init__()`](trimesh.path.path.html#trimesh.path.path.Path.__init__)
        * [`Path.apply_layer()`](trimesh.path.path.html#trimesh.path.path.Path.apply_layer)
        * [`Path.apply_transform()`](trimesh.path.path.html#trimesh.path.path.Path.apply_transform)
        * [`Path.bounds`](trimesh.path.path.html#trimesh.path.path.Path.bounds)
        * [`Path.centroid`](trimesh.path.path.html#trimesh.path.path.Path.centroid)
        * [`Path.colors`](trimesh.path.path.html#trimesh.path.path.Path.colors)
        * [`Path.convert_units()`](trimesh.path.path.html#trimesh.path.path.Path.convert_units)
        * [`Path.copy()`](trimesh.path.path.html#trimesh.path.path.Path.copy)
        * [`Path.dangling`](trimesh.path.path.html#trimesh.path.path.Path.dangling)
        * [`Path.discrete`](trimesh.path.path.html#trimesh.path.path.Path.discrete)
        * [`Path.entities`](trimesh.path.path.html#trimesh.path.path.Path.entities)
        * [`Path.explode()`](trimesh.path.path.html#trimesh.path.path.Path.explode)
        * [`Path.export()`](trimesh.path.path.html#trimesh.path.path.Path.export)
        * [`Path.extents`](trimesh.path.path.html#trimesh.path.path.Path.extents)
        * [`Path.fill_gaps()`](trimesh.path.path.html#trimesh.path.path.Path.fill_gaps)
        * [`Path.identifier_hash`](trimesh.path.path.html#trimesh.path.path.Path.identifier_hash)
        * [`Path.is_closed`](trimesh.path.path.html#trimesh.path.path.Path.is_closed)
        * [`Path.is_empty`](trimesh.path.path.html#trimesh.path.path.Path.is_empty)
        * [`Path.kdtree`](trimesh.path.path.html#trimesh.path.path.Path.kdtree)
        * [`Path.layers`](trimesh.path.path.html#trimesh.path.path.Path.layers)
        * [`Path.length`](trimesh.path.path.html#trimesh.path.path.Path.length)
        * [`Path.merge_vertices()`](trimesh.path.path.html#trimesh.path.path.Path.merge_vertices)
        * [`Path.paths`](trimesh.path.path.html#trimesh.path.path.Path.paths)
        * [`Path.process()`](trimesh.path.path.html#trimesh.path.path.Path.process)
        * [`Path.referenced_vertices`](trimesh.path.path.html#trimesh.path.path.Path.referenced_vertices)
        * [`Path.remove_duplicate_entities()`](trimesh.path.path.html#trimesh.path.path.Path.remove_duplicate_entities)
        * [`Path.remove_entities()`](trimesh.path.path.html#trimesh.path.path.Path.remove_entities)
        * [`Path.remove_invalid()`](trimesh.path.path.html#trimesh.path.path.Path.remove_invalid)
        * [`Path.remove_unreferenced_vertices()`](trimesh.path.path.html#trimesh.path.path.Path.remove_unreferenced_vertices)
        * [`Path.replace_vertex_references()`](trimesh.path.path.html#trimesh.path.path.Path.replace_vertex_references)
        * [`Path.rezero()`](trimesh.path.path.html#trimesh.path.path.Path.rezero)
        * [`Path.scene()`](trimesh.path.path.html#trimesh.path.path.Path.scene)
        * [`Path.to_dict()`](trimesh.path.path.html#trimesh.path.path.Path.to_dict)
        * [`Path.vertex_graph`](trimesh.path.path.html#trimesh.path.path.Path.vertex_graph)
        * [`Path.vertex_nodes`](trimesh.path.path.html#trimesh.path.path.Path.vertex_nodes)
        * [`Path.vertices`](trimesh.path.path.html#trimesh.path.path.Path.vertices)
      * [`Path2D`](trimesh.path.path.html#trimesh.path.path.Path2D)
        * [`Path2D.apply_obb()`](trimesh.path.path.html#trimesh.path.path.Path2D.apply_obb)
        * [`Path2D.apply_scale()`](trimesh.path.path.html#trimesh.path.path.Path2D.apply_scale)
        * [`Path2D.area`](trimesh.path.path.html#trimesh.path.path.Path2D.area)
        * [`Path2D.body_count`](trimesh.path.path.html#trimesh.path.path.Path2D.body_count)
        * [`Path2D.connected_paths()`](trimesh.path.path.html#trimesh.path.path.Path2D.connected_paths)
        * [`Path2D.convex_hull`](trimesh.path.path.html#trimesh.path.path.Path2D.convex_hull)
        * [`Path2D.enclosure`](trimesh.path.path.html#trimesh.path.path.Path2D.enclosure)
        * [`Path2D.enclosure_directed`](trimesh.path.path.html#trimesh.path.path.Path2D.enclosure_directed)
        * [`Path2D.enclosure_shell`](trimesh.path.path.html#trimesh.path.path.Path2D.enclosure_shell)
        * [`Path2D.extrude()`](trimesh.path.path.html#trimesh.path.path.Path2D.extrude)
        * [`Path2D.identifier`](trimesh.path.path.html#trimesh.path.path.Path2D.identifier)
        * [`Path2D.medial_axis()`](trimesh.path.path.html#trimesh.path.path.Path2D.medial_axis)
        * [`Path2D.obb`](trimesh.path.path.html#trimesh.path.path.Path2D.obb)
        * [`Path2D.path_valid`](trimesh.path.path.html#trimesh.path.path.Path2D.path_valid)
        * [`Path2D.plot_discrete()`](trimesh.path.path.html#trimesh.path.path.Path2D.plot_discrete)
        * [`Path2D.plot_entities()`](trimesh.path.path.html#trimesh.path.path.Path2D.plot_entities)
        * [`Path2D.polygons_closed`](trimesh.path.path.html#trimesh.path.path.Path2D.polygons_closed)
        * [`Path2D.polygons_full`](trimesh.path.path.html#trimesh.path.path.Path2D.polygons_full)
        * [`Path2D.rasterize()`](trimesh.path.path.html#trimesh.path.path.Path2D.rasterize)
        * [`Path2D.root`](trimesh.path.path.html#trimesh.path.path.Path2D.root)
        * [`Path2D.sample()`](trimesh.path.path.html#trimesh.path.path.Path2D.sample)
        * [`Path2D.show()`](trimesh.path.path.html#trimesh.path.path.Path2D.show)
        * [`Path2D.simplify()`](trimesh.path.path.html#trimesh.path.path.Path2D.simplify)
        * [`Path2D.simplify_spline()`](trimesh.path.path.html#trimesh.path.path.Path2D.simplify_spline)
        * [`Path2D.split()`](trimesh.path.path.html#trimesh.path.path.Path2D.split)
        * [`Path2D.to_3D()`](trimesh.path.path.html#trimesh.path.path.Path2D.to_3D)
        * [`Path2D.triangulate()`](trimesh.path.path.html#trimesh.path.path.Path2D.triangulate)
      * [`Path3D`](trimesh.path.path.html#trimesh.path.path.Path3D)
        * [`Path3D.convex_hull`](trimesh.path.path.html#trimesh.path.path.Path3D.convex_hull)
        * [`Path3D.identifier`](trimesh.path.path.html#trimesh.path.path.Path3D.identifier)
        * [`Path3D.show()`](trimesh.path.path.html#trimesh.path.path.Path3D.show)
        * [`Path3D.to_2D()`](trimesh.path.path.html#trimesh.path.path.Path3D.to_2D)
        * [`Path3D.to_planar()`](trimesh.path.path.html#trimesh.path.path.Path3D.to_planar)
    * [trimesh.path.polygons](trimesh.path.polygons.html)
      * [`edges_to_polygons()`](trimesh.path.polygons.html#trimesh.path.polygons.edges_to_polygons)
      * [`enclosure_tree()`](trimesh.path.polygons.html#trimesh.path.polygons.enclosure_tree)
      * [`identifier()`](trimesh.path.polygons.html#trimesh.path.polygons.identifier)
      * [`medial_axis()`](trimesh.path.polygons.html#trimesh.path.polygons.medial_axis)
      * [`paths_to_polygons()`](trimesh.path.polygons.html#trimesh.path.polygons.paths_to_polygons)
      * [`plot()`](trimesh.path.polygons.html#trimesh.path.polygons.plot)
      * [`polygon_bounds()`](trimesh.path.polygons.html#trimesh.path.polygons.polygon_bounds)
      * [`polygon_obb()`](trimesh.path.polygons.html#trimesh.path.polygons.polygon_obb)
      * [`polygon_scale()`](trimesh.path.polygons.html#trimesh.path.polygons.polygon_scale)
      * [`polygons_obb()`](trimesh.path.polygons.html#trimesh.path.polygons.polygons_obb)
      * [`projected()`](trimesh.path.polygons.html#trimesh.path.polygons.projected)
      * [`random_polygon()`](trimesh.path.polygons.html#trimesh.path.polygons.random_polygon)
      * [`repair_invalid()`](trimesh.path.polygons.html#trimesh.path.polygons.repair_invalid)
      * [`resample_boundaries()`](trimesh.path.polygons.html#trimesh.path.polygons.resample_boundaries)
      * [`sample()`](trimesh.path.polygons.html#trimesh.path.polygons.sample)
      * [`second_moments()`](trimesh.path.polygons.html#trimesh.path.polygons.second_moments)
      * [`stack_boundaries()`](trimesh.path.polygons.html#trimesh.path.polygons.stack_boundaries)
      * [`transform_polygon()`](trimesh.path.polygons.html#trimesh.path.polygons.transform_polygon)
    * [trimesh.path.raster](trimesh.path.raster.html)
      * [raster.py](trimesh.path.raster.html#raster-py)
      * [`rasterize()`](trimesh.path.raster.html#trimesh.path.raster.rasterize)
    * [trimesh.path.repair](trimesh.path.repair.html)
      * [repair.py](trimesh.path.repair.html#repair-py)
      * [`fill_gaps()`](trimesh.path.repair.html#trimesh.path.repair.fill_gaps)
    * [trimesh.path.segments](trimesh.path.segments.html)
      * [segments.py](trimesh.path.segments.html#segments-py)
      * [`clean()`](trimesh.path.segments.html#trimesh.path.segments.clean)
      * [`colinear_pairs()`](trimesh.path.segments.html#trimesh.path.segments.colinear_pairs)
      * [`extrude()`](trimesh.path.segments.html#trimesh.path.segments.extrude)
      * [`length()`](trimesh.path.segments.html#trimesh.path.segments.length)
      * [`parameters_to_segments()`](trimesh.path.segments.html#trimesh.path.segments.parameters_to_segments)
      * [`resample()`](trimesh.path.segments.html#trimesh.path.segments.resample)
      * [`segments_to_parameters()`](trimesh.path.segments.html#trimesh.path.segments.segments_to_parameters)
      * [`split()`](trimesh.path.segments.html#trimesh.path.segments.split)
      * [`to_svg()`](trimesh.path.segments.html#trimesh.path.segments.to_svg)
      * [`unique()`](trimesh.path.segments.html#trimesh.path.segments.unique)
    * [trimesh.path.simplify](trimesh.path.simplify.html)
      * [`fit_circle_check()`](trimesh.path.simplify.html#trimesh.path.simplify.fit_circle_check)
      * [`is_circle()`](trimesh.path.simplify.html#trimesh.path.simplify.is_circle)
      * [`merge_colinear()`](trimesh.path.simplify.html#trimesh.path.simplify.merge_colinear)
      * [`points_to_spline_entity()`](trimesh.path.simplify.html#trimesh.path.simplify.points_to_spline_entity)
      * [`resample_spline()`](trimesh.path.simplify.html#trimesh.path.simplify.resample_spline)
      * [`simplify_basic()`](trimesh.path.simplify.html#trimesh.path.simplify.simplify_basic)
      * [`simplify_spline()`](trimesh.path.simplify.html#trimesh.path.simplify.simplify_spline)
    * [trimesh.path.traversal](trimesh.path.traversal.html)
      * [`PathSample`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample)
        * [`PathSample.__init__()`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample.__init__)
        * [`PathSample.sample()`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample.sample)
        * [`PathSample.truncate()`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample.truncate)
      * [`closed_paths()`](trimesh.path.traversal.html#trimesh.path.traversal.closed_paths)
      * [`discretize_path()`](trimesh.path.traversal.html#trimesh.path.traversal.discretize_path)
      * [`resample_path()`](trimesh.path.traversal.html#trimesh.path.traversal.resample_path)
      * [`split()`](trimesh.path.traversal.html#trimesh.path.traversal.split)
      * [`vertex_graph()`](trimesh.path.traversal.html#trimesh.path.traversal.vertex_graph)
      * [`vertex_to_entity_path()`](trimesh.path.traversal.html#trimesh.path.traversal.vertex_to_entity_path)
    * [trimesh.path.util](trimesh.path.util.html)
      * [`concatenate()`](trimesh.path.util.html#trimesh.path.util.concatenate)
    * [trimesh.path](trimesh.path.html#module-trimesh.path)
    * [`Path2D`](trimesh.path.html#trimesh.path.Path2D)
      * [`Path2D.apply_obb()`](trimesh.path.html#trimesh.path.Path2D.apply_obb)
      * [`Path2D.apply_scale()`](trimesh.path.html#trimesh.path.Path2D.apply_scale)
      * [`Path2D.area`](trimesh.path.html#trimesh.path.Path2D.area)
      * [`Path2D.body_count`](trimesh.path.html#trimesh.path.Path2D.body_count)
      * [`Path2D.connected_paths()`](trimesh.path.html#trimesh.path.Path2D.connected_paths)
      * [`Path2D.convex_hull`](trimesh.path.html#trimesh.path.Path2D.convex_hull)
      * [`Path2D.enclosure`](trimesh.path.html#trimesh.path.Path2D.enclosure)
      * [`Path2D.enclosure_directed`](trimesh.path.html#trimesh.path.Path2D.enclosure_directed)
      * [`Path2D.enclosure_shell`](trimesh.path.html#trimesh.path.Path2D.enclosure_shell)
      * [`Path2D.extrude()`](trimesh.path.html#trimesh.path.Path2D.extrude)
      * [`Path2D.identifier`](trimesh.path.html#trimesh.path.Path2D.identifier)
      * [`Path2D.medial_axis()`](trimesh.path.html#trimesh.path.Path2D.medial_axis)
      * [`Path2D.obb`](trimesh.path.html#trimesh.path.Path2D.obb)
      * [`Path2D.path_valid`](trimesh.path.html#trimesh.path.Path2D.path_valid)
      * [`Path2D.plot_discrete()`](trimesh.path.html#trimesh.path.Path2D.plot_discrete)
      * [`Path2D.plot_entities()`](trimesh.path.html#trimesh.path.Path2D.plot_entities)
      * [`Path2D.polygons_closed`](trimesh.path.html#trimesh.path.Path2D.polygons_closed)
      * [`Path2D.polygons_full`](trimesh.path.html#trimesh.path.Path2D.polygons_full)
      * [`Path2D.rasterize()`](trimesh.path.html#trimesh.path.Path2D.rasterize)
      * [`Path2D.root`](trimesh.path.html#trimesh.path.Path2D.root)
      * [`Path2D.sample()`](trimesh.path.html#trimesh.path.Path2D.sample)
      * [`Path2D.show()`](trimesh.path.html#trimesh.path.Path2D.show)
      * [`Path2D.simplify()`](trimesh.path.html#trimesh.path.Path2D.simplify)
      * [`Path2D.simplify_spline()`](trimesh.path.html#trimesh.path.Path2D.simplify_spline)
      * [`Path2D.split()`](trimesh.path.html#trimesh.path.Path2D.split)
      * [`Path2D.to_3D()`](trimesh.path.html#trimesh.path.Path2D.to_3D)
      * [`Path2D.triangulate()`](trimesh.path.html#trimesh.path.Path2D.triangulate)
    * [`Path3D`](trimesh.path.html#trimesh.path.Path3D)
      * [`Path3D.convex_hull`](trimesh.path.html#trimesh.path.Path3D.convex_hull)
      * [`Path3D.identifier`](trimesh.path.html#trimesh.path.Path3D.identifier)
      * [`Path3D.show()`](trimesh.path.html#trimesh.path.Path3D.show)
      * [`Path3D.to_2D()`](trimesh.path.html#trimesh.path.Path3D.to_2D)
      * [`Path3D.to_planar()`](trimesh.path.html#trimesh.path.Path3D.to_planar)
  * [trimesh.ray](trimesh.ray.html)
    * [trimesh.ray.ray_pyembree](trimesh.ray.ray_pyembree.html)
      * [`RayMeshIntersector`](trimesh.ray.ray_pyembree.html#trimesh.ray.ray_pyembree.RayMeshIntersector)
        * [`RayMeshIntersector.__init__()`](trimesh.ray.ray_pyembree.html#trimesh.ray.ray_pyembree.RayMeshIntersector.__init__)
        * [`RayMeshIntersector.contains_points()`](trimesh.ray.ray_pyembree.html#trimesh.ray.ray_pyembree.RayMeshIntersector.contains_points)
        * [`RayMeshIntersector.intersects_any()`](trimesh.ray.ray_pyembree.html#trimesh.ray.ray_pyembree.RayMeshIntersector.intersects_any)
        * [`RayMeshIntersector.intersects_first()`](trimesh.ray.ray_pyembree.html#trimesh.ray.ray_pyembree.RayMeshIntersector.intersects_first)
        * [`RayMeshIntersector.intersects_id()`](trimesh.ray.ray_pyembree.html#trimesh.ray.ray_pyembree.RayMeshIntersector.intersects_id)
        * [`RayMeshIntersector.intersects_location()`](trimesh.ray.ray_pyembree.html#trimesh.ray.ray_pyembree.RayMeshIntersector.intersects_location)
    * [trimesh.ray.ray_triangle](trimesh.ray.ray_triangle.html)
      * [`RayMeshIntersector`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.RayMeshIntersector)
        * [`RayMeshIntersector.__init__()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.RayMeshIntersector.__init__)
        * [`RayMeshIntersector.contains_points()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.RayMeshIntersector.contains_points)
        * [`RayMeshIntersector.intersects_any()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.RayMeshIntersector.intersects_any)
        * [`RayMeshIntersector.intersects_first()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.RayMeshIntersector.intersects_first)
        * [`RayMeshIntersector.intersects_id()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.RayMeshIntersector.intersects_id)
        * [`RayMeshIntersector.intersects_location()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.RayMeshIntersector.intersects_location)
      * [`ray_bounds()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.ray_bounds)
      * [`ray_triangle_candidates()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.ray_triangle_candidates)
      * [`ray_triangle_id()`](trimesh.ray.ray_triangle.html#trimesh.ray.ray_triangle.ray_triangle_id)
    * [trimesh.ray.ray_util](trimesh.ray.ray_util.html)
  * [trimesh.resources](trimesh.resources.html)
    * [`get_bytes()`](trimesh.resources.html#trimesh.resources.get_bytes)
    * [`get_json()`](trimesh.resources.html#trimesh.resources.get_json)
    * [`get_schema()`](trimesh.resources.html#trimesh.resources.get_schema)
    * [`get_stream()`](trimesh.resources.html#trimesh.resources.get_stream)
    * [`get_string()`](trimesh.resources.html#trimesh.resources.get_string)
  * [trimesh.scene](trimesh.scene.html)
    * [trimesh.scene.cameras](trimesh.scene.cameras.html)
      * [`Camera`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera)
        * [`Camera.K`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.K)
        * [`Camera.__init__()`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.__init__)
        * [`Camera.angles()`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.angles)
        * [`Camera.copy()`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.copy)
        * [`Camera.focal`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.focal)
        * [`Camera.fov`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.fov)
        * [`Camera.look_at()`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.look_at)
        * [`Camera.resolution`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.resolution)
        * [`Camera.to_rays()`](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera.to_rays)
      * [`camera_to_rays()`](trimesh.scene.cameras.html#trimesh.scene.cameras.camera_to_rays)
      * [`look_at()`](trimesh.scene.cameras.html#trimesh.scene.cameras.look_at)
      * [`ray_pixel_coords()`](trimesh.scene.cameras.html#trimesh.scene.cameras.ray_pixel_coords)
    * [trimesh.scene.lighting](trimesh.scene.lighting.html)
      * [lighting.py](trimesh.scene.lighting.html#lighting-py)
      * [`DirectionalLight`](trimesh.scene.lighting.html#trimesh.scene.lighting.DirectionalLight)
        * [`DirectionalLight.name`](trimesh.scene.lighting.html#trimesh.scene.lighting.DirectionalLight.name)
        * [`DirectionalLight.color`](trimesh.scene.lighting.html#trimesh.scene.lighting.DirectionalLight.color)
        * [`DirectionalLight.intensity`](trimesh.scene.lighting.html#trimesh.scene.lighting.DirectionalLight.intensity)
        * [`DirectionalLight.radius`](trimesh.scene.lighting.html#trimesh.scene.lighting.DirectionalLight.radius)
        * [`DirectionalLight.__init__()`](trimesh.scene.lighting.html#trimesh.scene.lighting.DirectionalLight.__init__)
      * [`Light`](trimesh.scene.lighting.html#trimesh.scene.lighting.Light)
        * [`Light.name`](trimesh.scene.lighting.html#trimesh.scene.lighting.Light.name)
        * [`Light.color`](trimesh.scene.lighting.html#trimesh.scene.lighting.Light.color)
        * [`Light.intensity`](trimesh.scene.lighting.html#trimesh.scene.lighting.Light.intensity)
        * [`Light.radius`](trimesh.scene.lighting.html#trimesh.scene.lighting.Light.radius)
        * [`Light.__init__()`](trimesh.scene.lighting.html#trimesh.scene.lighting.Light.__init__)
        * [`Light.color`](trimesh.scene.lighting.html#id0)
        * [`Light.intensity`](trimesh.scene.lighting.html#id1)
        * [`Light.radius`](trimesh.scene.lighting.html#id2)
      * [`PointLight`](trimesh.scene.lighting.html#trimesh.scene.lighting.PointLight)
        * [`PointLight.name`](trimesh.scene.lighting.html#trimesh.scene.lighting.PointLight.name)
        * [`PointLight.color`](trimesh.scene.lighting.html#trimesh.scene.lighting.PointLight.color)
        * [`PointLight.intensity`](trimesh.scene.lighting.html#trimesh.scene.lighting.PointLight.intensity)
        * [`PointLight.radius`](trimesh.scene.lighting.html#trimesh.scene.lighting.PointLight.radius)
        * [`PointLight.__init__()`](trimesh.scene.lighting.html#trimesh.scene.lighting.PointLight.__init__)
      * [`SpotLight`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight)
        * [`SpotLight.name`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight.name)
        * [`SpotLight.color`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight.color)
        * [`SpotLight.intensity`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight.intensity)
        * [`SpotLight.radius`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight.radius)
        * [`SpotLight.innerConeAngle`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight.innerConeAngle)
        * [`SpotLight.outerConeAngle`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight.outerConeAngle)
        * [`SpotLight.__init__()`](trimesh.scene.lighting.html#trimesh.scene.lighting.SpotLight.__init__)
        * [`SpotLight.innerConeAngle`](trimesh.scene.lighting.html#id3)
        * [`SpotLight.outerConeAngle`](trimesh.scene.lighting.html#id4)
      * [`autolight()`](trimesh.scene.lighting.html#trimesh.scene.lighting.autolight)
    * [trimesh.scene.scene](trimesh.scene.scene.html)
      * [`Scene`](trimesh.scene.scene.html#trimesh.scene.scene.Scene)
        * [`Scene.__init__()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.__init__)
        * [`Scene.add_geometry()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.add_geometry)
        * [`Scene.apply_transform()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.apply_transform)
        * [`Scene.area`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.area)
        * [`Scene.bounds`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.bounds)
        * [`Scene.bounds_corners`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.bounds_corners)
        * [`Scene.camera`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.camera)
        * [`Scene.camera_rays()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.camera_rays)
        * [`Scene.camera_transform`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.camera_transform)
        * [`Scene.center_mass`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.center_mass)
        * [`Scene.centroid`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.centroid)
        * [`Scene.convert_units()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.convert_units)
        * [`Scene.convex_hull`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.convex_hull)
        * [`Scene.copy()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.copy)
        * [`Scene.delete_geometry()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.delete_geometry)
        * [`Scene.dump()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.dump)
        * [`Scene.duplicate_nodes`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.duplicate_nodes)
        * [`Scene.explode()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.explode)
        * [`Scene.export()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.export)
        * [`Scene.extents`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.extents)
        * [`Scene.geometry_identifiers`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.geometry_identifiers)
        * [`Scene.has_camera`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.has_camera)
        * [`Scene.identifier_hash`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.identifier_hash)
        * [`Scene.is_empty`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.is_empty)
        * [`Scene.is_valid`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.is_valid)
        * [`Scene.lights`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.lights)
        * [`Scene.moment_inertia`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.moment_inertia)
        * [`Scene.moment_inertia_frame()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.moment_inertia_frame)
        * [`Scene.reconstruct_instances()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.reconstruct_instances)
        * [`Scene.rezero()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.rezero)
        * [`Scene.save_image()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.save_image)
        * [`Scene.scale`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.scale)
        * [`Scene.scaled()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.scaled)
        * [`Scene.set_camera()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.set_camera)
        * [`Scene.show()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.show)
        * [`Scene.simplify_quadric_decimation()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.simplify_quadric_decimation)
        * [`Scene.strip_visuals()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.strip_visuals)
        * [`Scene.subscene()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.subscene)
        * [`Scene.to_geometry()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.to_geometry)
        * [`Scene.to_mesh()`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.to_mesh)
        * [`Scene.triangles`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.triangles)
        * [`Scene.triangles_node`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.triangles_node)
        * [`Scene.units`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.units)
        * [`Scene.volume`](trimesh.scene.scene.html#trimesh.scene.scene.Scene.volume)
      * [`append_scenes()`](trimesh.scene.scene.html#trimesh.scene.scene.append_scenes)
      * [`reconstruct_instances()`](trimesh.scene.scene.html#trimesh.scene.scene.reconstruct_instances)
      * [`split_scene()`](trimesh.scene.scene.html#trimesh.scene.scene.split_scene)
    * [trimesh.scene.transforms](trimesh.scene.transforms.html)
      * [`EnforcedForest`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest)
        * [`EnforcedForest.__init__()`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest.__init__)
        * [`EnforcedForest.add_edge()`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest.add_edge)
        * [`EnforcedForest.children`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest.children)
        * [`EnforcedForest.nodes`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest.nodes)
        * [`EnforcedForest.remove_node()`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest.remove_node)
        * [`EnforcedForest.shortest_path()`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest.shortest_path)
        * [`EnforcedForest.successors()`](trimesh.scene.transforms.html#trimesh.scene.transforms.EnforcedForest.successors)
      * [`SceneGraph`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph)
        * [`SceneGraph.__init__()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.__init__)
        * [`SceneGraph.clear()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.clear)
        * [`SceneGraph.copy()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.copy)
        * [`SceneGraph.from_edgelist()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.from_edgelist)
        * [`SceneGraph.geometry_nodes`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.geometry_nodes)
        * [`SceneGraph.get()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.get)
        * [`SceneGraph.load()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.load)
        * [`SceneGraph.nodes`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.nodes)
        * [`SceneGraph.nodes_geometry`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.nodes_geometry)
        * [`SceneGraph.remove_geometries()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.remove_geometries)
        * [`SceneGraph.show()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.show)
        * [`SceneGraph.to_edgelist()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.to_edgelist)
        * [`SceneGraph.to_flattened()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.to_flattened)
        * [`SceneGraph.to_gltf()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.to_gltf)
        * [`SceneGraph.to_networkx()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.to_networkx)
        * [`SceneGraph.update()`](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph.update)
      * [`kwargs_to_matrix()`](trimesh.scene.transforms.html#trimesh.scene.transforms.kwargs_to_matrix)
    * [`Camera`](trimesh.scene.html#trimesh.scene.Camera)
      * [`Camera.K`](trimesh.scene.html#trimesh.scene.Camera.K)
      * [`Camera.__init__()`](trimesh.scene.html#trimesh.scene.Camera.__init__)
      * [`Camera.angles()`](trimesh.scene.html#trimesh.scene.Camera.angles)
      * [`Camera.copy()`](trimesh.scene.html#trimesh.scene.Camera.copy)
      * [`Camera.focal`](trimesh.scene.html#trimesh.scene.Camera.focal)
      * [`Camera.fov`](trimesh.scene.html#trimesh.scene.Camera.fov)
      * [`Camera.look_at()`](trimesh.scene.html#trimesh.scene.Camera.look_at)
      * [`Camera.resolution`](trimesh.scene.html#trimesh.scene.Camera.resolution)
      * [`Camera.to_rays()`](trimesh.scene.html#trimesh.scene.Camera.to_rays)
    * [`Scene`](trimesh.scene.html#trimesh.scene.Scene)
      * [`Scene.__init__()`](trimesh.scene.html#trimesh.scene.Scene.__init__)
      * [`Scene.add_geometry()`](trimesh.scene.html#trimesh.scene.Scene.add_geometry)
      * [`Scene.apply_transform()`](trimesh.scene.html#trimesh.scene.Scene.apply_transform)
      * [`Scene.area`](trimesh.scene.html#trimesh.scene.Scene.area)
      * [`Scene.bounds`](trimesh.scene.html#trimesh.scene.Scene.bounds)
      * [`Scene.bounds_corners`](trimesh.scene.html#trimesh.scene.Scene.bounds_corners)
      * [`Scene.camera`](trimesh.scene.html#trimesh.scene.Scene.camera)
      * [`Scene.camera_rays()`](trimesh.scene.html#trimesh.scene.Scene.camera_rays)
      * [`Scene.camera_transform`](trimesh.scene.html#trimesh.scene.Scene.camera_transform)
      * [`Scene.center_mass`](trimesh.scene.html#trimesh.scene.Scene.center_mass)
      * [`Scene.centroid`](trimesh.scene.html#trimesh.scene.Scene.centroid)
      * [`Scene.convert_units()`](trimesh.scene.html#trimesh.scene.Scene.convert_units)
      * [`Scene.convex_hull`](trimesh.scene.html#trimesh.scene.Scene.convex_hull)
      * [`Scene.copy()`](trimesh.scene.html#trimesh.scene.Scene.copy)
      * [`Scene.delete_geometry()`](trimesh.scene.html#trimesh.scene.Scene.delete_geometry)
      * [`Scene.dump()`](trimesh.scene.html#trimesh.scene.Scene.dump)
      * [`Scene.duplicate_nodes`](trimesh.scene.html#trimesh.scene.Scene.duplicate_nodes)
      * [`Scene.explode()`](trimesh.scene.html#trimesh.scene.Scene.explode)
      * [`Scene.export()`](trimesh.scene.html#trimesh.scene.Scene.export)
      * [`Scene.extents`](trimesh.scene.html#trimesh.scene.Scene.extents)
      * [`Scene.geometry_identifiers`](trimesh.scene.html#trimesh.scene.Scene.geometry_identifiers)
      * [`Scene.has_camera`](trimesh.scene.html#trimesh.scene.Scene.has_camera)
      * [`Scene.identifier_hash`](trimesh.scene.html#trimesh.scene.Scene.identifier_hash)
      * [`Scene.is_empty`](trimesh.scene.html#trimesh.scene.Scene.is_empty)
      * [`Scene.is_valid`](trimesh.scene.html#trimesh.scene.Scene.is_valid)
      * [`Scene.lights`](trimesh.scene.html#trimesh.scene.Scene.lights)
      * [`Scene.moment_inertia`](trimesh.scene.html#trimesh.scene.Scene.moment_inertia)
      * [`Scene.moment_inertia_frame()`](trimesh.scene.html#trimesh.scene.Scene.moment_inertia_frame)
      * [`Scene.reconstruct_instances()`](trimesh.scene.html#trimesh.scene.Scene.reconstruct_instances)
      * [`Scene.rezero()`](trimesh.scene.html#trimesh.scene.Scene.rezero)
      * [`Scene.save_image()`](trimesh.scene.html#trimesh.scene.Scene.save_image)
      * [`Scene.scale`](trimesh.scene.html#trimesh.scene.Scene.scale)
      * [`Scene.scaled()`](trimesh.scene.html#trimesh.scene.Scene.scaled)
      * [`Scene.set_camera()`](trimesh.scene.html#trimesh.scene.Scene.set_camera)
      * [`Scene.show()`](trimesh.scene.html#trimesh.scene.Scene.show)
      * [`Scene.simplify_quadric_decimation()`](trimesh.scene.html#trimesh.scene.Scene.simplify_quadric_decimation)
      * [`Scene.strip_visuals()`](trimesh.scene.html#trimesh.scene.Scene.strip_visuals)
      * [`Scene.subscene()`](trimesh.scene.html#trimesh.scene.Scene.subscene)
      * [`Scene.to_geometry()`](trimesh.scene.html#trimesh.scene.Scene.to_geometry)
      * [`Scene.to_mesh()`](trimesh.scene.html#trimesh.scene.Scene.to_mesh)
      * [`Scene.triangles`](trimesh.scene.html#trimesh.scene.Scene.triangles)
      * [`Scene.triangles_node`](trimesh.scene.html#trimesh.scene.Scene.triangles_node)
      * [`Scene.units`](trimesh.scene.html#trimesh.scene.Scene.units)
      * [`Scene.volume`](trimesh.scene.html#trimesh.scene.Scene.volume)
    * [`split_scene()`](trimesh.scene.html#trimesh.scene.split_scene)
  * [trimesh.viewer](trimesh.viewer.html)
    * [trimesh.viewer.notebook](trimesh.viewer.notebook.html)
      * [notebook.py](trimesh.viewer.notebook.html#notebook-py)
      * [`in_notebook()`](trimesh.viewer.notebook.html#trimesh.viewer.notebook.in_notebook)
      * [`scene_to_html()`](trimesh.viewer.notebook.html#trimesh.viewer.notebook.scene_to_html)
      * [`scene_to_mo_notebook()`](trimesh.viewer.notebook.html#trimesh.viewer.notebook.scene_to_mo_notebook)
      * [`scene_to_notebook()`](trimesh.viewer.notebook.html#trimesh.viewer.notebook.scene_to_notebook)
    * [trimesh.viewer.trackball](trimesh.viewer.trackball.html)
      * [`Trackball`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball)
        * [`Trackball.STATE_PAN`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.STATE_PAN)
        * [`Trackball.STATE_ROLL`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.STATE_ROLL)
        * [`Trackball.STATE_ROTATE`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.STATE_ROTATE)
        * [`Trackball.STATE_ZOOM`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.STATE_ZOOM)
        * [`Trackball.__init__()`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.__init__)
        * [`Trackball.down()`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.down)
        * [`Trackball.drag()`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.drag)
        * [`Trackball.pose`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.pose)
        * [`Trackball.resize()`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.resize)
        * [`Trackball.rotate()`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.rotate)
        * [`Trackball.scroll()`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.scroll)
        * [`Trackball.set_state()`](trimesh.viewer.trackball.html#trimesh.viewer.trackball.Trackball.set_state)
    * [trimesh.viewer.widget](trimesh.viewer.widget.html)
    * [trimesh.viewer.windowed](trimesh.viewer.windowed.html)
    * [viewer](trimesh.viewer.html#viewer)
    * [`in_notebook()`](trimesh.viewer.html#trimesh.viewer.in_notebook)
    * [`scene_to_html()`](trimesh.viewer.html#trimesh.viewer.scene_to_html)
    * [`scene_to_mo_notebook()`](trimesh.viewer.html#trimesh.viewer.scene_to_mo_notebook)
    * [`scene_to_notebook()`](trimesh.viewer.html#trimesh.viewer.scene_to_notebook)
  * [trimesh.visual](trimesh.visual.html)
    * [trimesh.visual.base](trimesh.visual.base.html)
      * [base.py](trimesh.visual.base.html#base-py)
      * [`Visuals`](trimesh.visual.base.html#trimesh.visual.base.Visuals)
        * [`Visuals.concatenate()`](trimesh.visual.base.html#trimesh.visual.base.Visuals.concatenate)
        * [`Visuals.copy()`](trimesh.visual.base.html#trimesh.visual.base.Visuals.copy)
        * [`Visuals.kind`](trimesh.visual.base.html#trimesh.visual.base.Visuals.kind)
        * [`Visuals.update_faces()`](trimesh.visual.base.html#trimesh.visual.base.Visuals.update_faces)
        * [`Visuals.update_vertices()`](trimesh.visual.base.html#trimesh.visual.base.Visuals.update_vertices)
    * [trimesh.visual.color](trimesh.visual.color.html)
      * [color.py](trimesh.visual.color.html#color-py)
      * [Goals](trimesh.visual.color.html#goals)
      * [`ColorVisuals`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals)
        * [`ColorVisuals.__init__()`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.__init__)
        * [`ColorVisuals.concatenate()`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.concatenate)
        * [`ColorVisuals.copy()`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.copy)
        * [`ColorVisuals.defined`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.defined)
        * [`ColorVisuals.face_colors`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.face_colors)
        * [`ColorVisuals.face_subset()`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.face_subset)
        * [`ColorVisuals.kind`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.kind)
        * [`ColorVisuals.main_color`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.main_color)
        * [`ColorVisuals.to_texture()`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.to_texture)
        * [`ColorVisuals.transparency`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.transparency)
        * [`ColorVisuals.update_faces()`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.update_faces)
        * [`ColorVisuals.update_vertices()`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.update_vertices)
        * [`ColorVisuals.vertex_colors`](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals.vertex_colors)
      * [`VertexColor`](trimesh.visual.color.html#trimesh.visual.color.VertexColor)
        * [`VertexColor.__init__()`](trimesh.visual.color.html#trimesh.visual.color.VertexColor.__init__)
        * [`VertexColor.concatenate()`](trimesh.visual.color.html#trimesh.visual.color.VertexColor.concatenate)
        * [`VertexColor.copy()`](trimesh.visual.color.html#trimesh.visual.color.VertexColor.copy)
        * [`VertexColor.kind`](trimesh.visual.color.html#trimesh.visual.color.VertexColor.kind)
        * [`VertexColor.update_faces()`](trimesh.visual.color.html#trimesh.visual.color.VertexColor.update_faces)
        * [`VertexColor.update_vertices()`](trimesh.visual.color.html#trimesh.visual.color.VertexColor.update_vertices)
        * [`VertexColor.vertex_colors`](trimesh.visual.color.html#trimesh.visual.color.VertexColor.vertex_colors)
      * [`color_to_uv()`](trimesh.visual.color.html#trimesh.visual.color.color_to_uv)
      * [`colors_to_materials()`](trimesh.visual.color.html#trimesh.visual.color.colors_to_materials)
      * [`face_to_vertex_color()`](trimesh.visual.color.html#trimesh.visual.color.face_to_vertex_color)
      * [`hex_to_rgba()`](trimesh.visual.color.html#trimesh.visual.color.hex_to_rgba)
      * [`hsv_to_rgba()`](trimesh.visual.color.html#trimesh.visual.color.hsv_to_rgba)
      * [`interpolate()`](trimesh.visual.color.html#trimesh.visual.color.interpolate)
      * [`linear_color_map()`](trimesh.visual.color.html#trimesh.visual.color.linear_color_map)
      * [`linear_to_srgb()`](trimesh.visual.color.html#trimesh.visual.color.linear_to_srgb)
      * [`random_color()`](trimesh.visual.color.html#trimesh.visual.color.random_color)
      * [`srgb_to_linear()`](trimesh.visual.color.html#trimesh.visual.color.srgb_to_linear)
      * [`to_float()`](trimesh.visual.color.html#trimesh.visual.color.to_float)
      * [`to_rgba()`](trimesh.visual.color.html#trimesh.visual.color.to_rgba)
      * [`uv_to_color()`](trimesh.visual.color.html#trimesh.visual.color.uv_to_color)
      * [`uv_to_interpolated_color()`](trimesh.visual.color.html#trimesh.visual.color.uv_to_interpolated_color)
      * [`vertex_to_face_color()`](trimesh.visual.color.html#trimesh.visual.color.vertex_to_face_color)
    * [trimesh.visual.gloss](trimesh.visual.gloss.html)
      * [`specular_to_pbr()`](trimesh.visual.gloss.html#trimesh.visual.gloss.specular_to_pbr)
    * [trimesh.visual.material](trimesh.visual.material.html)
      * [material.py](trimesh.visual.material.html#material-py)
      * [`Material`](trimesh.visual.material.html#trimesh.visual.material.Material)
        * [`Material.__init__()`](trimesh.visual.material.html#trimesh.visual.material.Material.__init__)
        * [`Material.copy()`](trimesh.visual.material.html#trimesh.visual.material.Material.copy)
        * [`Material.main_color`](trimesh.visual.material.html#trimesh.visual.material.Material.main_color)
        * [`Material.name`](trimesh.visual.material.html#trimesh.visual.material.Material.name)
      * [`MultiMaterial`](trimesh.visual.material.html#trimesh.visual.material.MultiMaterial)
        * [`MultiMaterial.__init__()`](trimesh.visual.material.html#trimesh.visual.material.MultiMaterial.__init__)
        * [`MultiMaterial.add()`](trimesh.visual.material.html#trimesh.visual.material.MultiMaterial.add)
        * [`MultiMaterial.get()`](trimesh.visual.material.html#trimesh.visual.material.MultiMaterial.get)
        * [`MultiMaterial.main_color`](trimesh.visual.material.html#trimesh.visual.material.MultiMaterial.main_color)
        * [`MultiMaterial.to_pbr()`](trimesh.visual.material.html#trimesh.visual.material.MultiMaterial.to_pbr)
      * [`PBRMaterial`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial)
        * [`PBRMaterial.__init__()`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.__init__)
        * [`PBRMaterial.alphaCutoff`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.alphaCutoff)
        * [`PBRMaterial.alphaMode`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.alphaMode)
        * [`PBRMaterial.baseColorFactor`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.baseColorFactor)
        * [`PBRMaterial.baseColorTexture`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.baseColorTexture)
        * [`PBRMaterial.copy()`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.copy)
        * [`PBRMaterial.doubleSided`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.doubleSided)
        * [`PBRMaterial.emissiveFactor`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.emissiveFactor)
        * [`PBRMaterial.emissiveTexture`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.emissiveTexture)
        * [`PBRMaterial.main_color`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.main_color)
        * [`PBRMaterial.metallicFactor`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.metallicFactor)
        * [`PBRMaterial.metallicRoughnessTexture`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.metallicRoughnessTexture)
        * [`PBRMaterial.name`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.name)
        * [`PBRMaterial.normalTexture`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.normalTexture)
        * [`PBRMaterial.occlusionTexture`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.occlusionTexture)
        * [`PBRMaterial.roughnessFactor`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.roughnessFactor)
        * [`PBRMaterial.to_color()`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.to_color)
        * [`PBRMaterial.to_simple()`](trimesh.visual.material.html#trimesh.visual.material.PBRMaterial.to_simple)
      * [`SimpleMaterial`](trimesh.visual.material.html#trimesh.visual.material.SimpleMaterial)
        * [`SimpleMaterial.__init__()`](trimesh.visual.material.html#trimesh.visual.material.SimpleMaterial.__init__)
        * [`SimpleMaterial.glossiness`](trimesh.visual.material.html#trimesh.visual.material.SimpleMaterial.glossiness)
        * [`SimpleMaterial.main_color`](trimesh.visual.material.html#trimesh.visual.material.SimpleMaterial.main_color)
        * [`SimpleMaterial.to_color()`](trimesh.visual.material.html#trimesh.visual.material.SimpleMaterial.to_color)
        * [`SimpleMaterial.to_obj()`](trimesh.visual.material.html#trimesh.visual.material.SimpleMaterial.to_obj)
        * [`SimpleMaterial.to_pbr()`](trimesh.visual.material.html#trimesh.visual.material.SimpleMaterial.to_pbr)
      * [`color_image()`](trimesh.visual.material.html#trimesh.visual.material.color_image)
      * [`empty_material()`](trimesh.visual.material.html#trimesh.visual.material.empty_material)
      * [`pack()`](trimesh.visual.material.html#trimesh.visual.material.pack)
    * [trimesh.visual.objects](trimesh.visual.objects.html)
      * [objects.py](trimesh.visual.objects.html#objects-py)
      * [`concatenate()`](trimesh.visual.objects.html#trimesh.visual.objects.concatenate)
      * [`create_visual()`](trimesh.visual.objects.html#trimesh.visual.objects.create_visual)
    * [trimesh.visual.texture](trimesh.visual.texture.html)
      * [`TextureVisuals`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals)
        * [`TextureVisuals.__init__()`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.__init__)
        * [`TextureVisuals.concatenate()`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.concatenate)
        * [`TextureVisuals.copy()`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.copy)
        * [`TextureVisuals.defined`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.defined)
        * [`TextureVisuals.face_subset()`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.face_subset)
        * [`TextureVisuals.kind`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.kind)
        * [`TextureVisuals.to_color()`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.to_color)
        * [`TextureVisuals.update_faces()`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.update_faces)
        * [`TextureVisuals.update_vertices()`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.update_vertices)
        * [`TextureVisuals.uv`](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals.uv)
      * [`power_resize()`](trimesh.visual.texture.html#trimesh.visual.texture.power_resize)
      * [`unmerge_faces()`](trimesh.visual.texture.html#trimesh.visual.texture.unmerge_faces)
    * [visual](trimesh.visual.html#visual)
    * [`ColorVisuals`](trimesh.visual.html#trimesh.visual.ColorVisuals)
      * [`ColorVisuals.__init__()`](trimesh.visual.html#trimesh.visual.ColorVisuals.__init__)
      * [`ColorVisuals.concatenate()`](trimesh.visual.html#trimesh.visual.ColorVisuals.concatenate)
      * [`ColorVisuals.copy()`](trimesh.visual.html#trimesh.visual.ColorVisuals.copy)
      * [`ColorVisuals.defined`](trimesh.visual.html#trimesh.visual.ColorVisuals.defined)
      * [`ColorVisuals.face_colors`](trimesh.visual.html#trimesh.visual.ColorVisuals.face_colors)
      * [`ColorVisuals.face_subset()`](trimesh.visual.html#trimesh.visual.ColorVisuals.face_subset)
      * [`ColorVisuals.kind`](trimesh.visual.html#trimesh.visual.ColorVisuals.kind)
      * [`ColorVisuals.main_color`](trimesh.visual.html#trimesh.visual.ColorVisuals.main_color)
      * [`ColorVisuals.to_texture()`](trimesh.visual.html#trimesh.visual.ColorVisuals.to_texture)
      * [`ColorVisuals.transparency`](trimesh.visual.html#trimesh.visual.ColorVisuals.transparency)
      * [`ColorVisuals.update_faces()`](trimesh.visual.html#trimesh.visual.ColorVisuals.update_faces)
      * [`ColorVisuals.update_vertices()`](trimesh.visual.html#trimesh.visual.ColorVisuals.update_vertices)
      * [`ColorVisuals.vertex_colors`](trimesh.visual.html#trimesh.visual.ColorVisuals.vertex_colors)
    * [`TextureVisuals`](trimesh.visual.html#trimesh.visual.TextureVisuals)
      * [`TextureVisuals.__init__()`](trimesh.visual.html#trimesh.visual.TextureVisuals.__init__)
      * [`TextureVisuals.concatenate()`](trimesh.visual.html#trimesh.visual.TextureVisuals.concatenate)
      * [`TextureVisuals.copy()`](trimesh.visual.html#trimesh.visual.TextureVisuals.copy)
      * [`TextureVisuals.defined`](trimesh.visual.html#trimesh.visual.TextureVisuals.defined)
      * [`TextureVisuals.face_subset()`](trimesh.visual.html#trimesh.visual.TextureVisuals.face_subset)
      * [`TextureVisuals.kind`](trimesh.visual.html#trimesh.visual.TextureVisuals.kind)
      * [`TextureVisuals.to_color()`](trimesh.visual.html#trimesh.visual.TextureVisuals.to_color)
      * [`TextureVisuals.update_faces()`](trimesh.visual.html#trimesh.visual.TextureVisuals.update_faces)
      * [`TextureVisuals.update_vertices()`](trimesh.visual.html#trimesh.visual.TextureVisuals.update_vertices)
      * [`TextureVisuals.uv`](trimesh.visual.html#trimesh.visual.TextureVisuals.uv)
    * [`create_visual()`](trimesh.visual.html#trimesh.visual.create_visual)
    * [`interpolate()`](trimesh.visual.html#trimesh.visual.interpolate)
    * [`linear_color_map()`](trimesh.visual.html#trimesh.visual.linear_color_map)
    * [`random_color()`](trimesh.visual.html#trimesh.visual.random_color)
    * [`to_rgba()`](trimesh.visual.html#trimesh.visual.to_rgba)
    * [`uv_to_color()`](trimesh.visual.html#trimesh.visual.uv_to_color)
    * [`uv_to_interpolated_color()`](trimesh.visual.html#trimesh.visual.uv_to_interpolated_color)
  * [trimesh.voxel](trimesh.voxel.html)
    * [trimesh.voxel.base](trimesh.voxel.base.html)
      * [voxel.py](trimesh.voxel.base.html#voxel-py)
      * [`VoxelGrid`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid)
        * [`VoxelGrid.__init__()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.__init__)
        * [`VoxelGrid.apply_transform()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.apply_transform)
        * [`VoxelGrid.as_boxes()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.as_boxes)
        * [`VoxelGrid.bounds`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.bounds)
        * [`VoxelGrid.copy()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.copy)
        * [`VoxelGrid.element_volume`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.element_volume)
        * [`VoxelGrid.encoding`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.encoding)
        * [`VoxelGrid.export()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.export)
        * [`VoxelGrid.extents`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.extents)
        * [`VoxelGrid.fill()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.fill)
        * [`VoxelGrid.filled_count`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.filled_count)
        * [`VoxelGrid.hollow()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.hollow)
        * [`VoxelGrid.identifier_hash`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.identifier_hash)
        * [`VoxelGrid.indices_to_points()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.indices_to_points)
        * [`VoxelGrid.is_empty`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.is_empty)
        * [`VoxelGrid.is_filled()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.is_filled)
        * [`VoxelGrid.marching_cubes`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.marching_cubes)
        * [`VoxelGrid.matrix`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.matrix)
        * [`VoxelGrid.pitch`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.pitch)
        * [`VoxelGrid.points`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.points)
        * [`VoxelGrid.points_to_indices()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.points_to_indices)
        * [`VoxelGrid.revoxelized()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.revoxelized)
        * [`VoxelGrid.scale`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.scale)
        * [`VoxelGrid.shape`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.shape)
        * [`VoxelGrid.show()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.show)
        * [`VoxelGrid.sparse_indices`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.sparse_indices)
        * [`VoxelGrid.strip()`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.strip)
        * [`VoxelGrid.transform`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.transform)
        * [`VoxelGrid.translation`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.translation)
        * [`VoxelGrid.volume`](trimesh.voxel.base.html#trimesh.voxel.base.VoxelGrid.volume)
    * [trimesh.voxel.creation](trimesh.voxel.creation.html)
      * [`local_voxelize()`](trimesh.voxel.creation.html#trimesh.voxel.creation.local_voxelize)
      * [`voxelize()`](trimesh.voxel.creation.html#trimesh.voxel.creation.voxelize)
    * [trimesh.voxel.encoding](trimesh.voxel.encoding.html)
      * [`BinaryRunLengthEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding)
        * [`BinaryRunLengthEncoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.__init__)
        * [`BinaryRunLengthEncoding.binary_run_length_data()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.binary_run_length_data)
        * [`BinaryRunLengthEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.copy)
        * [`BinaryRunLengthEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.dense)
        * [`BinaryRunLengthEncoding.from_brle()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.from_brle)
        * [`BinaryRunLengthEncoding.from_dense()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.from_dense)
        * [`BinaryRunLengthEncoding.from_rle()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.from_rle)
        * [`BinaryRunLengthEncoding.gather()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.gather)
        * [`BinaryRunLengthEncoding.gather_nd()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.gather_nd)
        * [`BinaryRunLengthEncoding.is_empty`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.is_empty)
        * [`BinaryRunLengthEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.mask)
        * [`BinaryRunLengthEncoding.run_length_data()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.run_length_data)
        * [`BinaryRunLengthEncoding.size`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.size)
        * [`BinaryRunLengthEncoding.sorted_gather()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.sorted_gather)
        * [`BinaryRunLengthEncoding.sparse_components`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.sparse_components)
        * [`BinaryRunLengthEncoding.sparse_indices`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.sparse_indices)
        * [`BinaryRunLengthEncoding.sparse_values`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.sparse_values)
        * [`BinaryRunLengthEncoding.stripped`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.stripped)
        * [`BinaryRunLengthEncoding.sum`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.BinaryRunLengthEncoding.sum)
      * [`DenseEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding)
        * [`DenseEncoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.__init__)
        * [`DenseEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.copy)
        * [`DenseEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.dense)
        * [`DenseEncoding.dtype`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.dtype)
        * [`DenseEncoding.flat`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.flat)
        * [`DenseEncoding.gather()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.gather)
        * [`DenseEncoding.gather_nd()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.gather_nd)
        * [`DenseEncoding.get_value()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.get_value)
        * [`DenseEncoding.is_empty`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.is_empty)
        * [`DenseEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.mask)
        * [`DenseEncoding.reshape()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.reshape)
        * [`DenseEncoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.shape)
        * [`DenseEncoding.size`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.size)
        * [`DenseEncoding.sparse_components`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.sparse_components)
        * [`DenseEncoding.sparse_indices`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.sparse_indices)
        * [`DenseEncoding.sparse_values`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.sparse_values)
        * [`DenseEncoding.sum`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.DenseEncoding.sum)
      * [`Encoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding)
        * [`Encoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.__init__)
        * [`Encoding.binary_run_length_data()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.binary_run_length_data)
        * [`Encoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.copy)
        * [`Encoding.data`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.data)
        * [`Encoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.dense)
        * [`Encoding.dtype`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.dtype)
        * [`Encoding.flat`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.flat)
        * [`Encoding.flip()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.flip)
        * [`Encoding.gather_nd()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.gather_nd)
        * [`Encoding.get_value()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.get_value)
        * [`Encoding.is_empty`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.is_empty)
        * [`Encoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.mask)
        * [`Encoding.mutable`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.mutable)
        * [`Encoding.ndims`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.ndims)
        * [`Encoding.reshape()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.reshape)
        * [`Encoding.run_length_data()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.run_length_data)
        * [`Encoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.shape)
        * [`Encoding.size`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.size)
        * [`Encoding.sparse_components`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.sparse_components)
        * [`Encoding.sparse_indices`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.sparse_indices)
        * [`Encoding.sparse_values`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.sparse_values)
        * [`Encoding.stripped`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.stripped)
        * [`Encoding.sum`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.sum)
        * [`Encoding.transpose()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.Encoding.transpose)
      * [`FlattenedEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlattenedEncoding)
        * [`FlattenedEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlattenedEncoding.copy)
        * [`FlattenedEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlattenedEncoding.dense)
        * [`FlattenedEncoding.flat`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlattenedEncoding.flat)
        * [`FlattenedEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlattenedEncoding.mask)
        * [`FlattenedEncoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlattenedEncoding.shape)
      * [`FlippedEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlippedEncoding)
        * [`FlippedEncoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlippedEncoding.__init__)
        * [`FlippedEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlippedEncoding.copy)
        * [`FlippedEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlippedEncoding.dense)
        * [`FlippedEncoding.flip()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlippedEncoding.flip)
        * [`FlippedEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlippedEncoding.mask)
        * [`FlippedEncoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.FlippedEncoding.shape)
      * [`LazyIndexMap`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap)
        * [`LazyIndexMap.dtype`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.dtype)
        * [`LazyIndexMap.gather_nd()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.gather_nd)
        * [`LazyIndexMap.get_value()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.get_value)
        * [`LazyIndexMap.is_empty`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.is_empty)
        * [`LazyIndexMap.size`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.size)
        * [`LazyIndexMap.sparse_indices`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.sparse_indices)
        * [`LazyIndexMap.sparse_values`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.sparse_values)
        * [`LazyIndexMap.sum`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.LazyIndexMap.sum)
      * [`RunLengthEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding)
        * [`RunLengthEncoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.__init__)
        * [`RunLengthEncoding.binary_run_length_data()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.binary_run_length_data)
        * [`RunLengthEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.copy)
        * [`RunLengthEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.dense)
        * [`RunLengthEncoding.dtype`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.dtype)
        * [`RunLengthEncoding.from_brle()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.from_brle)
        * [`RunLengthEncoding.from_dense()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.from_dense)
        * [`RunLengthEncoding.from_rle()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.from_rle)
        * [`RunLengthEncoding.gather()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.gather)
        * [`RunLengthEncoding.gather_nd()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.gather_nd)
        * [`RunLengthEncoding.get_value()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.get_value)
        * [`RunLengthEncoding.is_empty`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.is_empty)
        * [`RunLengthEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.mask)
        * [`RunLengthEncoding.ndims`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.ndims)
        * [`RunLengthEncoding.run_length_data()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.run_length_data)
        * [`RunLengthEncoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.shape)
        * [`RunLengthEncoding.size`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.size)
        * [`RunLengthEncoding.sorted_gather()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.sorted_gather)
        * [`RunLengthEncoding.sparse_components`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.sparse_components)
        * [`RunLengthEncoding.sparse_indices`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.sparse_indices)
        * [`RunLengthEncoding.sparse_values`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.sparse_values)
        * [`RunLengthEncoding.stripped`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.stripped)
        * [`RunLengthEncoding.sum`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.RunLengthEncoding.sum)
      * [`ShapedEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.ShapedEncoding)
        * [`ShapedEncoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.ShapedEncoding.__init__)
        * [`ShapedEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.ShapedEncoding.copy)
        * [`ShapedEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.ShapedEncoding.dense)
        * [`ShapedEncoding.flat`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.ShapedEncoding.flat)
        * [`ShapedEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.ShapedEncoding.mask)
        * [`ShapedEncoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.ShapedEncoding.shape)
      * [`SparseBinaryEncoding()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseBinaryEncoding)
      * [`SparseEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding)
        * [`SparseEncoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.__init__)
        * [`SparseEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.copy)
        * [`SparseEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.dense)
        * [`SparseEncoding.dtype`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.dtype)
        * [`SparseEncoding.from_dense()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.from_dense)
        * [`SparseEncoding.gather_nd()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.gather_nd)
        * [`SparseEncoding.get_value()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.get_value)
        * [`SparseEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.mask)
        * [`SparseEncoding.ndims`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.ndims)
        * [`SparseEncoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.shape)
        * [`SparseEncoding.size`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.size)
        * [`SparseEncoding.sparse_components`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.sparse_components)
        * [`SparseEncoding.sparse_indices`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.sparse_indices)
        * [`SparseEncoding.sparse_values`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.sparse_values)
        * [`SparseEncoding.stripped`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.stripped)
        * [`SparseEncoding.sum`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.SparseEncoding.sum)
      * [`TransposedEncoding`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding)
        * [`TransposedEncoding.__init__()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.__init__)
        * [`TransposedEncoding.copy()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.copy)
        * [`TransposedEncoding.data`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.data)
        * [`TransposedEncoding.dense`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.dense)
        * [`TransposedEncoding.gather()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.gather)
        * [`TransposedEncoding.get_value()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.get_value)
        * [`TransposedEncoding.mask()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.mask)
        * [`TransposedEncoding.perm`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.perm)
        * [`TransposedEncoding.shape`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.shape)
        * [`TransposedEncoding.transpose()`](trimesh.voxel.encoding.html#trimesh.voxel.encoding.TransposedEncoding.transpose)
    * [trimesh.voxel.morphology](trimesh.voxel.morphology.html)
      * [`binary_closing()`](trimesh.voxel.morphology.html#trimesh.voxel.morphology.binary_closing)
      * [`binary_dilation()`](trimesh.voxel.morphology.html#trimesh.voxel.morphology.binary_dilation)
      * [`fill()`](trimesh.voxel.morphology.html#trimesh.voxel.morphology.fill)
      * [`surface()`](trimesh.voxel.morphology.html#trimesh.voxel.morphology.surface)
    * [trimesh.voxel.ops](trimesh.voxel.ops.html)
      * [`boolean_sparse()`](trimesh.voxel.ops.html#trimesh.voxel.ops.boolean_sparse)
      * [`fill_base()`](trimesh.voxel.ops.html#trimesh.voxel.ops.fill_base)
      * [`fill_orthographic()`](trimesh.voxel.ops.html#trimesh.voxel.ops.fill_orthographic)
      * [`fill_voxelization()`](trimesh.voxel.ops.html#trimesh.voxel.ops.fill_voxelization)
      * [`indices_to_points()`](trimesh.voxel.ops.html#trimesh.voxel.ops.indices_to_points)
      * [`matrix_to_marching_cubes()`](trimesh.voxel.ops.html#trimesh.voxel.ops.matrix_to_marching_cubes)
      * [`matrix_to_points()`](trimesh.voxel.ops.html#trimesh.voxel.ops.matrix_to_points)
      * [`multibox()`](trimesh.voxel.ops.html#trimesh.voxel.ops.multibox)
      * [`points_to_indices()`](trimesh.voxel.ops.html#trimesh.voxel.ops.points_to_indices)
      * [`points_to_marching_cubes()`](trimesh.voxel.ops.html#trimesh.voxel.ops.points_to_marching_cubes)
      * [`sparse_to_matrix()`](trimesh.voxel.ops.html#trimesh.voxel.ops.sparse_to_matrix)
      * [`strip_array()`](trimesh.voxel.ops.html#trimesh.voxel.ops.strip_array)
    * [trimesh.voxel.runlength](trimesh.voxel.runlength.html)
      * [`brle_gather_1d()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_gather_1d)
      * [`brle_gatherer_1d()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_gatherer_1d)
      * [`brle_length()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_length)
      * [`brle_logical_not()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_logical_not)
      * [`brle_mask()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_mask)
      * [`brle_reverse()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_reverse)
      * [`brle_strip()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_strip)
      * [`brle_to_brle()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_to_brle)
      * [`brle_to_dense()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_to_dense)
      * [`brle_to_rle()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_to_rle)
      * [`brle_to_sparse()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.brle_to_sparse)
      * [`dense_to_brle()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.dense_to_brle)
      * [`dense_to_rle()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.dense_to_rle)
      * [`merge_brle_lengths()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.merge_brle_lengths)
      * [`merge_rle_lengths()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.merge_rle_lengths)
      * [`rle_gather_1d()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_gather_1d)
      * [`rle_gatherer_1d()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_gatherer_1d)
      * [`rle_length()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_length)
      * [`rle_mask()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_mask)
      * [`rle_reverse()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_reverse)
      * [`rle_strip()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_strip)
      * [`rle_to_brle()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_to_brle)
      * [`rle_to_dense()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_to_dense)
      * [`rle_to_rle()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_to_rle)
      * [`rle_to_sparse()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.rle_to_sparse)
      * [`sorted_brle_gather_1d()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.sorted_brle_gather_1d)
      * [`sorted_rle_gather_1d()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.sorted_rle_gather_1d)
      * [`split_long_brle_lengths()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.split_long_brle_lengths)
      * [`split_long_rle_lengths()`](trimesh.voxel.runlength.html#trimesh.voxel.runlength.split_long_rle_lengths)
    * [trimesh.voxel.transforms](trimesh.voxel.transforms.html)
      * [`Transform`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform)
        * [`Transform.__init__()`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.__init__)
        * [`Transform.apply_scale()`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.apply_scale)
        * [`Transform.apply_transform()`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.apply_transform)
        * [`Transform.apply_translation()`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.apply_translation)
        * [`Transform.copy()`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.copy)
        * [`Transform.inverse_matrix`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.inverse_matrix)
        * [`Transform.inverse_transform_points()`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.inverse_transform_points)
        * [`Transform.is_identity`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.is_identity)
        * [`Transform.matrix`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.matrix)
        * [`Transform.pitch`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.pitch)
        * [`Transform.scale`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.scale)
        * [`Transform.transform_points()`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.transform_points)
        * [`Transform.translation`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.translation)
        * [`Transform.unit_volume`](trimesh.voxel.transforms.html#trimesh.voxel.transforms.Transform.unit_volume)
    * [`VoxelGrid`](trimesh.voxel.html#trimesh.voxel.VoxelGrid)
      * [`VoxelGrid.__init__()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.__init__)
      * [`VoxelGrid.apply_transform()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.apply_transform)
      * [`VoxelGrid.as_boxes()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.as_boxes)
      * [`VoxelGrid.bounds`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.bounds)
      * [`VoxelGrid.copy()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.copy)
      * [`VoxelGrid.element_volume`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.element_volume)
      * [`VoxelGrid.encoding`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.encoding)
      * [`VoxelGrid.export()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.export)
      * [`VoxelGrid.extents`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.extents)
      * [`VoxelGrid.fill()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.fill)
      * [`VoxelGrid.filled_count`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.filled_count)
      * [`VoxelGrid.hollow()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.hollow)
      * [`VoxelGrid.identifier_hash`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.identifier_hash)
      * [`VoxelGrid.indices_to_points()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.indices_to_points)
      * [`VoxelGrid.is_empty`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.is_empty)
      * [`VoxelGrid.is_filled()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.is_filled)
      * [`VoxelGrid.marching_cubes`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.marching_cubes)
      * [`VoxelGrid.matrix`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.matrix)
      * [`VoxelGrid.pitch`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.pitch)
      * [`VoxelGrid.points`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.points)
      * [`VoxelGrid.points_to_indices()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.points_to_indices)
      * [`VoxelGrid.revoxelized()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.revoxelized)
      * [`VoxelGrid.scale`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.scale)
      * [`VoxelGrid.shape`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.shape)
      * [`VoxelGrid.show()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.show)
      * [`VoxelGrid.sparse_indices`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.sparse_indices)
      * [`VoxelGrid.strip()`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.strip)
      * [`VoxelGrid.transform`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.transform)
      * [`VoxelGrid.translation`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.translation)
      * [`VoxelGrid.volume`](trimesh.voxel.html#trimesh.voxel.VoxelGrid.volume)
  * [trimesh.base](trimesh.base.html)
    * [https://github.com/mikedh/trimesh](trimesh.base.html#https-github-com-mikedh-trimesh)
    * [`Trimesh`](trimesh.base.html#trimesh.base.Trimesh)
      * [`Trimesh.__init__()`](trimesh.base.html#trimesh.base.Trimesh.__init__)
      * [`Trimesh.apply_transform()`](trimesh.base.html#trimesh.base.Trimesh.apply_transform)
      * [`Trimesh.area`](trimesh.base.html#trimesh.base.Trimesh.area)
      * [`Trimesh.area_faces`](trimesh.base.html#trimesh.base.Trimesh.area_faces)
      * [`Trimesh.body_count`](trimesh.base.html#trimesh.base.Trimesh.body_count)
      * [`Trimesh.bounds`](trimesh.base.html#trimesh.base.Trimesh.bounds)
      * [`Trimesh.center_mass`](trimesh.base.html#trimesh.base.Trimesh.center_mass)
      * [`Trimesh.centroid`](trimesh.base.html#trimesh.base.Trimesh.centroid)
      * [`Trimesh.compute_stable_poses()`](trimesh.base.html#trimesh.base.Trimesh.compute_stable_poses)
      * [`Trimesh.contains()`](trimesh.base.html#trimesh.base.Trimesh.contains)
      * [`Trimesh.convert_units()`](trimesh.base.html#trimesh.base.Trimesh.convert_units)
      * [`Trimesh.convex_decomposition()`](trimesh.base.html#trimesh.base.Trimesh.convex_decomposition)
      * [`Trimesh.convex_hull`](trimesh.base.html#trimesh.base.Trimesh.convex_hull)
      * [`Trimesh.copy()`](trimesh.base.html#trimesh.base.Trimesh.copy)
      * [`Trimesh.density`](trimesh.base.html#trimesh.base.Trimesh.density)
      * [`Trimesh.difference()`](trimesh.base.html#trimesh.base.Trimesh.difference)
      * [`Trimesh.edges`](trimesh.base.html#trimesh.base.Trimesh.edges)
      * [`Trimesh.edges_face`](trimesh.base.html#trimesh.base.Trimesh.edges_face)
      * [`Trimesh.edges_sorted`](trimesh.base.html#trimesh.base.Trimesh.edges_sorted)
      * [`Trimesh.edges_sorted_tree`](trimesh.base.html#trimesh.base.Trimesh.edges_sorted_tree)
      * [`Trimesh.edges_sparse`](trimesh.base.html#trimesh.base.Trimesh.edges_sparse)
      * [`Trimesh.edges_unique`](trimesh.base.html#trimesh.base.Trimesh.edges_unique)
      * [`Trimesh.edges_unique_inverse`](trimesh.base.html#trimesh.base.Trimesh.edges_unique_inverse)
      * [`Trimesh.edges_unique_length`](trimesh.base.html#trimesh.base.Trimesh.edges_unique_length)
      * [`Trimesh.euler_number`](trimesh.base.html#trimesh.base.Trimesh.euler_number)
      * [`Trimesh.eval_cached()`](trimesh.base.html#trimesh.base.Trimesh.eval_cached)
      * [`Trimesh.export()`](trimesh.base.html#trimesh.base.Trimesh.export)
      * [`Trimesh.extents`](trimesh.base.html#trimesh.base.Trimesh.extents)
      * [`Trimesh.face_adjacency`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency)
      * [`Trimesh.face_adjacency_angles`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_angles)
      * [`Trimesh.face_adjacency_convex`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_convex)
      * [`Trimesh.face_adjacency_edges`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_edges)
      * [`Trimesh.face_adjacency_edges_tree`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_edges_tree)
      * [`Trimesh.face_adjacency_projections`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_projections)
      * [`Trimesh.face_adjacency_radius`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_radius)
      * [`Trimesh.face_adjacency_span`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_span)
      * [`Trimesh.face_adjacency_tree`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_tree)
      * [`Trimesh.face_adjacency_unshared`](trimesh.base.html#trimesh.base.Trimesh.face_adjacency_unshared)
      * [`Trimesh.face_angles`](trimesh.base.html#trimesh.base.Trimesh.face_angles)
      * [`Trimesh.face_angles_sparse`](trimesh.base.html#trimesh.base.Trimesh.face_angles_sparse)
      * [`Trimesh.face_neighborhood`](trimesh.base.html#trimesh.base.Trimesh.face_neighborhood)
      * [`Trimesh.face_normals`](trimesh.base.html#trimesh.base.Trimesh.face_normals)
      * [`Trimesh.faces`](trimesh.base.html#trimesh.base.Trimesh.faces)
      * [`Trimesh.faces_sparse`](trimesh.base.html#trimesh.base.Trimesh.faces_sparse)
      * [`Trimesh.faces_unique_edges`](trimesh.base.html#trimesh.base.Trimesh.faces_unique_edges)
      * [`Trimesh.facets`](trimesh.base.html#trimesh.base.Trimesh.facets)
      * [`Trimesh.facets_area`](trimesh.base.html#trimesh.base.Trimesh.facets_area)
      * [`Trimesh.facets_boundary`](trimesh.base.html#trimesh.base.Trimesh.facets_boundary)
      * [`Trimesh.facets_normal`](trimesh.base.html#trimesh.base.Trimesh.facets_normal)
      * [`Trimesh.facets_on_hull`](trimesh.base.html#trimesh.base.Trimesh.facets_on_hull)
      * [`Trimesh.facets_origin`](trimesh.base.html#trimesh.base.Trimesh.facets_origin)
      * [`Trimesh.fill_holes()`](trimesh.base.html#trimesh.base.Trimesh.fill_holes)
      * [`Trimesh.fix_normals()`](trimesh.base.html#trimesh.base.Trimesh.fix_normals)
      * [`Trimesh.identifier`](trimesh.base.html#trimesh.base.Trimesh.identifier)
      * [`Trimesh.identifier_hash`](trimesh.base.html#trimesh.base.Trimesh.identifier_hash)
      * [`Trimesh.integral_mean_curvature`](trimesh.base.html#trimesh.base.Trimesh.integral_mean_curvature)
      * [`Trimesh.intersection()`](trimesh.base.html#trimesh.base.Trimesh.intersection)
      * [`Trimesh.invert()`](trimesh.base.html#trimesh.base.Trimesh.invert)
      * [`Trimesh.is_convex`](trimesh.base.html#trimesh.base.Trimesh.is_convex)
      * [`Trimesh.is_empty`](trimesh.base.html#trimesh.base.Trimesh.is_empty)
      * [`Trimesh.is_volume`](trimesh.base.html#trimesh.base.Trimesh.is_volume)
      * [`Trimesh.is_watertight`](trimesh.base.html#trimesh.base.Trimesh.is_watertight)
      * [`Trimesh.is_winding_consistent`](trimesh.base.html#trimesh.base.Trimesh.is_winding_consistent)
      * [`Trimesh.kdtree`](trimesh.base.html#trimesh.base.Trimesh.kdtree)
      * [`Trimesh.mass`](trimesh.base.html#trimesh.base.Trimesh.mass)
      * [`Trimesh.mass_properties`](trimesh.base.html#trimesh.base.Trimesh.mass_properties)
      * [`Trimesh.merge_vertices()`](trimesh.base.html#trimesh.base.Trimesh.merge_vertices)
      * [`Trimesh.moment_inertia`](trimesh.base.html#trimesh.base.Trimesh.moment_inertia)
      * [`Trimesh.moment_inertia_frame()`](trimesh.base.html#trimesh.base.Trimesh.moment_inertia_frame)
      * [`Trimesh.mutable`](trimesh.base.html#trimesh.base.Trimesh.mutable)
      * [`Trimesh.nondegenerate_faces()`](trimesh.base.html#trimesh.base.Trimesh.nondegenerate_faces)
      * [`Trimesh.outline()`](trimesh.base.html#trimesh.base.Trimesh.outline)
      * [`Trimesh.principal_inertia_components`](trimesh.base.html#trimesh.base.Trimesh.principal_inertia_components)
      * [`Trimesh.principal_inertia_transform`](trimesh.base.html#trimesh.base.Trimesh.principal_inertia_transform)
      * [`Trimesh.principal_inertia_vectors`](trimesh.base.html#trimesh.base.Trimesh.principal_inertia_vectors)
      * [`Trimesh.process()`](trimesh.base.html#trimesh.base.Trimesh.process)
      * [`Trimesh.projected()`](trimesh.base.html#trimesh.base.Trimesh.projected)
      * [`Trimesh.referenced_vertices`](trimesh.base.html#trimesh.base.Trimesh.referenced_vertices)
      * [`Trimesh.register()`](trimesh.base.html#trimesh.base.Trimesh.register)
      * [`Trimesh.remove_infinite_values()`](trimesh.base.html#trimesh.base.Trimesh.remove_infinite_values)
      * [`Trimesh.remove_unreferenced_vertices()`](trimesh.base.html#trimesh.base.Trimesh.remove_unreferenced_vertices)
      * [`Trimesh.rezero()`](trimesh.base.html#trimesh.base.Trimesh.rezero)
      * [`Trimesh.sample()`](trimesh.base.html#trimesh.base.Trimesh.sample)
      * [`Trimesh.scene()`](trimesh.base.html#trimesh.base.Trimesh.scene)
      * [`Trimesh.section()`](trimesh.base.html#trimesh.base.Trimesh.section)
      * [`Trimesh.section_multiplane()`](trimesh.base.html#trimesh.base.Trimesh.section_multiplane)
      * [`Trimesh.show()`](trimesh.base.html#trimesh.base.Trimesh.show)
      * [`Trimesh.simplify_quadric_decimation()`](trimesh.base.html#trimesh.base.Trimesh.simplify_quadric_decimation)
      * [`Trimesh.slice_plane()`](trimesh.base.html#trimesh.base.Trimesh.slice_plane)
      * [`Trimesh.smooth_shaded`](trimesh.base.html#trimesh.base.Trimesh.smooth_shaded)
      * [`Trimesh.split()`](trimesh.base.html#trimesh.base.Trimesh.split)
      * [`Trimesh.subdivide()`](trimesh.base.html#trimesh.base.Trimesh.subdivide)
      * [`Trimesh.subdivide_loop()`](trimesh.base.html#trimesh.base.Trimesh.subdivide_loop)
      * [`Trimesh.subdivide_to_size()`](trimesh.base.html#trimesh.base.Trimesh.subdivide_to_size)
      * [`Trimesh.submesh()`](trimesh.base.html#trimesh.base.Trimesh.submesh)
      * [`Trimesh.symmetry`](trimesh.base.html#trimesh.base.Trimesh.symmetry)
      * [`Trimesh.symmetry_axis`](trimesh.base.html#trimesh.base.Trimesh.symmetry_axis)
      * [`Trimesh.symmetry_section`](trimesh.base.html#trimesh.base.Trimesh.symmetry_section)
      * [`Trimesh.to_dict()`](trimesh.base.html#trimesh.base.Trimesh.to_dict)
      * [`Trimesh.triangles`](trimesh.base.html#trimesh.base.Trimesh.triangles)
      * [`Trimesh.triangles_center`](trimesh.base.html#trimesh.base.Trimesh.triangles_center)
      * [`Trimesh.triangles_cross`](trimesh.base.html#trimesh.base.Trimesh.triangles_cross)
      * [`Trimesh.triangles_tree`](trimesh.base.html#trimesh.base.Trimesh.triangles_tree)
      * [`Trimesh.union()`](trimesh.base.html#trimesh.base.Trimesh.union)
      * [`Trimesh.unique_faces()`](trimesh.base.html#trimesh.base.Trimesh.unique_faces)
      * [`Trimesh.unmerge_vertices()`](trimesh.base.html#trimesh.base.Trimesh.unmerge_vertices)
      * [`Trimesh.unwrap()`](trimesh.base.html#trimesh.base.Trimesh.unwrap)
      * [`Trimesh.update_faces()`](trimesh.base.html#trimesh.base.Trimesh.update_faces)
      * [`Trimesh.update_vertices()`](trimesh.base.html#trimesh.base.Trimesh.update_vertices)
      * [`Trimesh.vertex_adjacency_graph`](trimesh.base.html#trimesh.base.Trimesh.vertex_adjacency_graph)
      * [`Trimesh.vertex_defects`](trimesh.base.html#trimesh.base.Trimesh.vertex_defects)
      * [`Trimesh.vertex_degree`](trimesh.base.html#trimesh.base.Trimesh.vertex_degree)
      * [`Trimesh.vertex_faces`](trimesh.base.html#trimesh.base.Trimesh.vertex_faces)
      * [`Trimesh.vertex_neighbors`](trimesh.base.html#trimesh.base.Trimesh.vertex_neighbors)
      * [`Trimesh.vertex_normals`](trimesh.base.html#trimesh.base.Trimesh.vertex_normals)
      * [`Trimesh.vertices`](trimesh.base.html#trimesh.base.Trimesh.vertices)
      * [`Trimesh.visual`](trimesh.base.html#trimesh.base.Trimesh.visual)
      * [`Trimesh.volume`](trimesh.base.html#trimesh.base.Trimesh.volume)
      * [`Trimesh.voxelized()`](trimesh.base.html#trimesh.base.Trimesh.voxelized)
  * [trimesh.boolean](trimesh.boolean.html)
    * [boolean.py](trimesh.boolean.html#boolean-py)
    * [`boolean_manifold()`](trimesh.boolean.html#trimesh.boolean.boolean_manifold)
    * [`difference()`](trimesh.boolean.html#trimesh.boolean.difference)
    * [`intersection()`](trimesh.boolean.html#trimesh.boolean.intersection)
    * [`union()`](trimesh.boolean.html#trimesh.boolean.union)
  * [trimesh.bounds](trimesh.bounds.html)
    * [`contains()`](trimesh.bounds.html#trimesh.bounds.contains)
    * [`corners()`](trimesh.bounds.html#trimesh.bounds.corners)
    * [`minimum_cylinder()`](trimesh.bounds.html#trimesh.bounds.minimum_cylinder)
    * [`oriented_bounds()`](trimesh.bounds.html#trimesh.bounds.oriented_bounds)
    * [`oriented_bounds_2D()`](trimesh.bounds.html#trimesh.bounds.oriented_bounds_2D)
    * [`to_extents()`](trimesh.bounds.html#trimesh.bounds.to_extents)
  * [trimesh.caching](trimesh.caching.html)
    * [caching.py](trimesh.caching.html#caching-py)
    * [`Cache`](trimesh.caching.html#trimesh.caching.Cache)
      * [`Cache.__init__()`](trimesh.caching.html#trimesh.caching.Cache.__init__)
      * [`Cache.clear()`](trimesh.caching.html#trimesh.caching.Cache.clear)
      * [`Cache.delete()`](trimesh.caching.html#trimesh.caching.Cache.delete)
      * [`Cache.id_set()`](trimesh.caching.html#trimesh.caching.Cache.id_set)
      * [`Cache.update()`](trimesh.caching.html#trimesh.caching.Cache.update)
      * [`Cache.verify()`](trimesh.caching.html#trimesh.caching.Cache.verify)
    * [`DataStore`](trimesh.caching.html#trimesh.caching.DataStore)
      * [`DataStore.__init__()`](trimesh.caching.html#trimesh.caching.DataStore.__init__)
      * [`DataStore.clear()`](trimesh.caching.html#trimesh.caching.DataStore.clear)
      * [`DataStore.is_empty()`](trimesh.caching.html#trimesh.caching.DataStore.is_empty)
      * [`DataStore.mutable`](trimesh.caching.html#trimesh.caching.DataStore.mutable)
      * [`DataStore.pop()`](trimesh.caching.html#trimesh.caching.DataStore.pop)
      * [`DataStore.update()`](trimesh.caching.html#trimesh.caching.DataStore.update)
    * [`DiskCache`](trimesh.caching.html#trimesh.caching.DiskCache)
      * [`DiskCache.__init__()`](trimesh.caching.html#trimesh.caching.DiskCache.__init__)
      * [`DiskCache.get()`](trimesh.caching.html#trimesh.caching.DiskCache.get)
    * [`TrackedArray`](trimesh.caching.html#trimesh.caching.TrackedArray)
      * [`TrackedArray.byteswap()`](trimesh.caching.html#trimesh.caching.TrackedArray.byteswap)
      * [`TrackedArray.fill()`](trimesh.caching.html#trimesh.caching.TrackedArray.fill)
      * [`TrackedArray.itemset()`](trimesh.caching.html#trimesh.caching.TrackedArray.itemset)
      * [`TrackedArray.mutable`](trimesh.caching.html#trimesh.caching.TrackedArray.mutable)
      * [`TrackedArray.partition()`](trimesh.caching.html#trimesh.caching.TrackedArray.partition)
      * [`TrackedArray.put()`](trimesh.caching.html#trimesh.caching.TrackedArray.put)
      * [`TrackedArray.setflags()`](trimesh.caching.html#trimesh.caching.TrackedArray.setflags)
      * [`TrackedArray.sort()`](trimesh.caching.html#trimesh.caching.TrackedArray.sort)
    * [`cache_decorator()`](trimesh.caching.html#trimesh.caching.cache_decorator)
    * [`hash_fallback()`](trimesh.caching.html#trimesh.caching.hash_fallback)
    * [`sha256()`](trimesh.caching.html#trimesh.caching.sha256)
    * [`tracked_array()`](trimesh.caching.html#trimesh.caching.tracked_array)
  * [trimesh.collision](trimesh.collision.html)
    * [`CollisionManager`](trimesh.collision.html#trimesh.collision.CollisionManager)
      * [`CollisionManager.__init__()`](trimesh.collision.html#trimesh.collision.CollisionManager.__init__)
      * [`CollisionManager.add_object()`](trimesh.collision.html#trimesh.collision.CollisionManager.add_object)
      * [`CollisionManager.in_collision_internal()`](trimesh.collision.html#trimesh.collision.CollisionManager.in_collision_internal)
      * [`CollisionManager.in_collision_other()`](trimesh.collision.html#trimesh.collision.CollisionManager.in_collision_other)
      * [`CollisionManager.in_collision_single()`](trimesh.collision.html#trimesh.collision.CollisionManager.in_collision_single)
      * [`CollisionManager.min_distance_internal()`](trimesh.collision.html#trimesh.collision.CollisionManager.min_distance_internal)
      * [`CollisionManager.min_distance_other()`](trimesh.collision.html#trimesh.collision.CollisionManager.min_distance_other)
      * [`CollisionManager.min_distance_single()`](trimesh.collision.html#trimesh.collision.CollisionManager.min_distance_single)
      * [`CollisionManager.remove_object()`](trimesh.collision.html#trimesh.collision.CollisionManager.remove_object)
      * [`CollisionManager.set_transform()`](trimesh.collision.html#trimesh.collision.CollisionManager.set_transform)
    * [`ContactData`](trimesh.collision.html#trimesh.collision.ContactData)
      * [`ContactData.__init__()`](trimesh.collision.html#trimesh.collision.ContactData.__init__)
      * [`ContactData.depth`](trimesh.collision.html#trimesh.collision.ContactData.depth)
      * [`ContactData.index()`](trimesh.collision.html#trimesh.collision.ContactData.index)
      * [`ContactData.normal`](trimesh.collision.html#trimesh.collision.ContactData.normal)
      * [`ContactData.point`](trimesh.collision.html#trimesh.collision.ContactData.point)
    * [`DistanceData`](trimesh.collision.html#trimesh.collision.DistanceData)
      * [`DistanceData.__init__()`](trimesh.collision.html#trimesh.collision.DistanceData.__init__)
      * [`DistanceData.distance`](trimesh.collision.html#trimesh.collision.DistanceData.distance)
      * [`DistanceData.index()`](trimesh.collision.html#trimesh.collision.DistanceData.index)
      * [`DistanceData.point()`](trimesh.collision.html#trimesh.collision.DistanceData.point)
    * [`mesh_to_BVH()`](trimesh.collision.html#trimesh.collision.mesh_to_BVH)
    * [`mesh_to_convex()`](trimesh.collision.html#trimesh.collision.mesh_to_convex)
    * [`scene_to_collision()`](trimesh.collision.html#trimesh.collision.scene_to_collision)
  * [trimesh.comparison](trimesh.comparison.html)
    * [comparison.py](trimesh.comparison.html#comparison-py)
    * [`identifier_hash()`](trimesh.comparison.html#trimesh.comparison.identifier_hash)
    * [`identifier_simple()`](trimesh.comparison.html#trimesh.comparison.identifier_simple)
  * [trimesh.constants](trimesh.constants.html)
    * [`ResolutionPath`](trimesh.constants.html#trimesh.constants.ResolutionPath)
      * [`ResolutionPath.__init__()`](trimesh.constants.html#trimesh.constants.ResolutionPath.__init__)
      * [`ResolutionPath.export`](trimesh.constants.html#trimesh.constants.ResolutionPath.export)
      * [`ResolutionPath.max_sections`](trimesh.constants.html#trimesh.constants.ResolutionPath.max_sections)
      * [`ResolutionPath.min_sections`](trimesh.constants.html#trimesh.constants.ResolutionPath.min_sections)
      * [`ResolutionPath.seg_angle`](trimesh.constants.html#trimesh.constants.ResolutionPath.seg_angle)
      * [`ResolutionPath.seg_frac`](trimesh.constants.html#trimesh.constants.ResolutionPath.seg_frac)
    * [`ToleranceMesh`](trimesh.constants.html#trimesh.constants.ToleranceMesh)
      * [`ToleranceMesh.__init__()`](trimesh.constants.html#trimesh.constants.ToleranceMesh.__init__)
      * [`ToleranceMesh.facet_threshold`](trimesh.constants.html#trimesh.constants.ToleranceMesh.facet_threshold)
      * [`ToleranceMesh.merge`](trimesh.constants.html#trimesh.constants.ToleranceMesh.merge)
      * [`ToleranceMesh.planar`](trimesh.constants.html#trimesh.constants.ToleranceMesh.planar)
      * [`ToleranceMesh.strict`](trimesh.constants.html#trimesh.constants.ToleranceMesh.strict)
      * [`ToleranceMesh.zero`](trimesh.constants.html#trimesh.constants.ToleranceMesh.zero)
    * [`TolerancePath`](trimesh.constants.html#trimesh.constants.TolerancePath)
      * [`TolerancePath.__init__()`](trimesh.constants.html#trimesh.constants.TolerancePath.__init__)
      * [`TolerancePath.aspect_frac`](trimesh.constants.html#trimesh.constants.TolerancePath.aspect_frac)
      * [`TolerancePath.merge`](trimesh.constants.html#trimesh.constants.TolerancePath.merge)
      * [`TolerancePath.merge_digits`](trimesh.constants.html#trimesh.constants.TolerancePath.merge_digits)
      * [`TolerancePath.planar`](trimesh.constants.html#trimesh.constants.TolerancePath.planar)
      * [`TolerancePath.radius_frac`](trimesh.constants.html#trimesh.constants.TolerancePath.radius_frac)
      * [`TolerancePath.radius_max`](trimesh.constants.html#trimesh.constants.TolerancePath.radius_max)
      * [`TolerancePath.radius_min`](trimesh.constants.html#trimesh.constants.TolerancePath.radius_min)
      * [`TolerancePath.seg_angle`](trimesh.constants.html#trimesh.constants.TolerancePath.seg_angle)
      * [`TolerancePath.seg_angle_frac`](trimesh.constants.html#trimesh.constants.TolerancePath.seg_angle_frac)
      * [`TolerancePath.seg_angle_min`](trimesh.constants.html#trimesh.constants.TolerancePath.seg_angle_min)
      * [`TolerancePath.seg_frac`](trimesh.constants.html#trimesh.constants.TolerancePath.seg_frac)
      * [`TolerancePath.strict`](trimesh.constants.html#trimesh.constants.TolerancePath.strict)
      * [`TolerancePath.tangent`](trimesh.constants.html#trimesh.constants.TolerancePath.tangent)
      * [`TolerancePath.zero`](trimesh.constants.html#trimesh.constants.TolerancePath.zero)
    * [`log_time()`](trimesh.constants.html#trimesh.constants.log_time)
  * [trimesh.convex](trimesh.convex.html)
    * [`QhullOptions`](trimesh.convex.html#trimesh.convex.QhullOptions)
      * [`QhullOptions.Pp`](trimesh.convex.html#trimesh.convex.QhullOptions.Pp)
      * [`QhullOptions.QJ`](trimesh.convex.html#trimesh.convex.QhullOptions.QJ)
      * [`QhullOptions.QR0`](trimesh.convex.html#trimesh.convex.QhullOptions.QR0)
      * [`QhullOptions.Qa`](trimesh.convex.html#trimesh.convex.QhullOptions.Qa)
      * [`QhullOptions.QbB`](trimesh.convex.html#trimesh.convex.QhullOptions.QbB)
      * [`QhullOptions.Qbb`](trimesh.convex.html#trimesh.convex.QhullOptions.Qbb)
      * [`QhullOptions.Qc`](trimesh.convex.html#trimesh.convex.QhullOptions.Qc)
      * [`QhullOptions.Qg`](trimesh.convex.html#trimesh.convex.QhullOptions.Qg)
      * [`QhullOptions.Qi`](trimesh.convex.html#trimesh.convex.QhullOptions.Qi)
      * [`QhullOptions.Qs`](trimesh.convex.html#trimesh.convex.QhullOptions.Qs)
      * [`QhullOptions.Qt`](trimesh.convex.html#trimesh.convex.QhullOptions.Qt)
      * [`QhullOptions.Qu`](trimesh.convex.html#trimesh.convex.QhullOptions.Qu)
      * [`QhullOptions.Qv`](trimesh.convex.html#trimesh.convex.QhullOptions.Qv)
      * [`QhullOptions.Qw`](trimesh.convex.html#trimesh.convex.QhullOptions.Qw)
      * [`QhullOptions.Qx`](trimesh.convex.html#trimesh.convex.QhullOptions.Qx)
      * [`QhullOptions.Qz`](trimesh.convex.html#trimesh.convex.QhullOptions.Qz)
      * [`QhullOptions.__init__()`](trimesh.convex.html#trimesh.convex.QhullOptions.__init__)
    * [`adjacency_projections()`](trimesh.convex.html#trimesh.convex.adjacency_projections)
    * [`convex_hull()`](trimesh.convex.html#trimesh.convex.convex_hull)
    * [`hull_points()`](trimesh.convex.html#trimesh.convex.hull_points)
    * [`is_convex()`](trimesh.convex.html#trimesh.convex.is_convex)
  * [trimesh.creation](trimesh.creation.html)
    * [creation.py](trimesh.creation.html#creation-py)
    * [`annulus()`](trimesh.creation.html#trimesh.creation.annulus)
    * [`axis()`](trimesh.creation.html#trimesh.creation.axis)
    * [`box()`](trimesh.creation.html#trimesh.creation.box)
    * [`camera_marker()`](trimesh.creation.html#trimesh.creation.camera_marker)
    * [`capsule()`](trimesh.creation.html#trimesh.creation.capsule)
    * [`cone()`](trimesh.creation.html#trimesh.creation.cone)
    * [`cylinder()`](trimesh.creation.html#trimesh.creation.cylinder)
    * [`extrude_polygon()`](trimesh.creation.html#trimesh.creation.extrude_polygon)
    * [`extrude_triangulation()`](trimesh.creation.html#trimesh.creation.extrude_triangulation)
    * [`icosahedron()`](trimesh.creation.html#trimesh.creation.icosahedron)
    * [`icosphere()`](trimesh.creation.html#trimesh.creation.icosphere)
    * [`random_soup()`](trimesh.creation.html#trimesh.creation.random_soup)
    * [`revolve()`](trimesh.creation.html#trimesh.creation.revolve)
    * [`sweep_polygon()`](trimesh.creation.html#trimesh.creation.sweep_polygon)
    * [`torus()`](trimesh.creation.html#trimesh.creation.torus)
    * [`triangulate_polygon()`](trimesh.creation.html#trimesh.creation.triangulate_polygon)
    * [`truncated_prisms()`](trimesh.creation.html#trimesh.creation.truncated_prisms)
    * [`uv_sphere()`](trimesh.creation.html#trimesh.creation.uv_sphere)
  * [trimesh.curvature](trimesh.curvature.html)
    * [curvature.py](trimesh.curvature.html#curvature-py)
    * [`discrete_gaussian_curvature_measure()`](trimesh.curvature.html#trimesh.curvature.discrete_gaussian_curvature_measure)
    * [`discrete_mean_curvature_measure()`](trimesh.curvature.html#trimesh.curvature.discrete_mean_curvature_measure)
    * [`face_angles_sparse()`](trimesh.curvature.html#trimesh.curvature.face_angles_sparse)
    * [`line_ball_intersection()`](trimesh.curvature.html#trimesh.curvature.line_ball_intersection)
    * [`sphere_ball_intersection()`](trimesh.curvature.html#trimesh.curvature.sphere_ball_intersection)
    * [`vertex_defects()`](trimesh.curvature.html#trimesh.curvature.vertex_defects)
  * [trimesh.decomposition](trimesh.decomposition.html)
    * [`convex_decomposition()`](trimesh.decomposition.html#trimesh.decomposition.convex_decomposition)
  * [trimesh.exceptions](trimesh.exceptions.html)
    * [exceptions.py](trimesh.exceptions.html#exceptions-py)
    * [`ExceptionWrapper`](trimesh.exceptions.html#trimesh.exceptions.ExceptionWrapper)
      * [`ExceptionWrapper.__init__()`](trimesh.exceptions.html#trimesh.exceptions.ExceptionWrapper.__init__)
  * [trimesh.geometry](trimesh.geometry.html)
    * [`align_vectors()`](trimesh.geometry.html#trimesh.geometry.align_vectors)
    * [`faces_to_edges()`](trimesh.geometry.html#trimesh.geometry.faces_to_edges)
    * [`index_sparse()`](trimesh.geometry.html#trimesh.geometry.index_sparse)
    * [`mean_vertex_normals()`](trimesh.geometry.html#trimesh.geometry.mean_vertex_normals)
    * [`plane_transform()`](trimesh.geometry.html#trimesh.geometry.plane_transform)
    * [`triangulate_quads()`](trimesh.geometry.html#trimesh.geometry.triangulate_quads)
    * [`vector_angle()`](trimesh.geometry.html#trimesh.geometry.vector_angle)
    * [`vertex_face_indices()`](trimesh.geometry.html#trimesh.geometry.vertex_face_indices)
    * [`weighted_vertex_normals()`](trimesh.geometry.html#trimesh.geometry.weighted_vertex_normals)
  * [trimesh.graph](trimesh.graph.html)
    * [graph.py](trimesh.graph.html#graph-py)
    * [`connected_component_labels()`](trimesh.graph.html#trimesh.graph.connected_component_labels)
    * [`connected_components()`](trimesh.graph.html#trimesh.graph.connected_components)
    * [`edges_to_coo()`](trimesh.graph.html#trimesh.graph.edges_to_coo)
    * [`face_adjacency()`](trimesh.graph.html#trimesh.graph.face_adjacency)
    * [`face_adjacency_radius()`](trimesh.graph.html#trimesh.graph.face_adjacency_radius)
    * [`face_adjacency_unshared()`](trimesh.graph.html#trimesh.graph.face_adjacency_unshared)
    * [`face_neighborhood()`](trimesh.graph.html#trimesh.graph.face_neighborhood)
    * [`facets()`](trimesh.graph.html#trimesh.graph.facets)
    * [`fill_traversals()`](trimesh.graph.html#trimesh.graph.fill_traversals)
    * [`graph_to_svg()`](trimesh.graph.html#trimesh.graph.graph_to_svg)
    * [`is_watertight()`](trimesh.graph.html#trimesh.graph.is_watertight)
    * [`multigraph_collect()`](trimesh.graph.html#trimesh.graph.multigraph_collect)
    * [`multigraph_paths()`](trimesh.graph.html#trimesh.graph.multigraph_paths)
    * [`neighbors()`](trimesh.graph.html#trimesh.graph.neighbors)
    * [`shared_edges()`](trimesh.graph.html#trimesh.graph.shared_edges)
    * [`smooth_shade()`](trimesh.graph.html#trimesh.graph.smooth_shade)
    * [`split()`](trimesh.graph.html#trimesh.graph.split)
    * [`traversals()`](trimesh.graph.html#trimesh.graph.traversals)
    * [`vertex_adjacency_graph()`](trimesh.graph.html#trimesh.graph.vertex_adjacency_graph)
  * [trimesh.grouping](trimesh.grouping.html)
    * [grouping.py](trimesh.grouping.html#grouping-py)
    * [`blocks()`](trimesh.grouping.html#trimesh.grouping.blocks)
    * [`boolean_rows()`](trimesh.grouping.html#trimesh.grouping.boolean_rows)
    * [`clusters()`](trimesh.grouping.html#trimesh.grouping.clusters)
    * [`float_to_int()`](trimesh.grouping.html#trimesh.grouping.float_to_int)
    * [`group()`](trimesh.grouping.html#trimesh.grouping.group)
    * [`group_distance()`](trimesh.grouping.html#trimesh.grouping.group_distance)
    * [`group_min()`](trimesh.grouping.html#trimesh.grouping.group_min)
    * [`group_rows()`](trimesh.grouping.html#trimesh.grouping.group_rows)
    * [`group_vectors()`](trimesh.grouping.html#trimesh.grouping.group_vectors)
    * [`hashable_rows()`](trimesh.grouping.html#trimesh.grouping.hashable_rows)
    * [`merge_runs()`](trimesh.grouping.html#trimesh.grouping.merge_runs)
    * [`merge_vertices()`](trimesh.grouping.html#trimesh.grouping.merge_vertices)
    * [`unique_bincount()`](trimesh.grouping.html#trimesh.grouping.unique_bincount)
    * [`unique_float()`](trimesh.grouping.html#trimesh.grouping.unique_float)
    * [`unique_ordered()`](trimesh.grouping.html#trimesh.grouping.unique_ordered)
    * [`unique_rows()`](trimesh.grouping.html#trimesh.grouping.unique_rows)
    * [`unique_value_in_row()`](trimesh.grouping.html#trimesh.grouping.unique_value_in_row)
  * [trimesh.inertia](trimesh.inertia.html)
    * [inertia.py](trimesh.inertia.html#inertia-py)
    * [`cylinder_inertia()`](trimesh.inertia.html#trimesh.inertia.cylinder_inertia)
    * [`points_inertia()`](trimesh.inertia.html#trimesh.inertia.points_inertia)
    * [`principal_axis()`](trimesh.inertia.html#trimesh.inertia.principal_axis)
    * [`radial_symmetry()`](trimesh.inertia.html#trimesh.inertia.radial_symmetry)
    * [`scene_inertia()`](trimesh.inertia.html#trimesh.inertia.scene_inertia)
    * [`sphere_inertia()`](trimesh.inertia.html#trimesh.inertia.sphere_inertia)
    * [`transform_inertia()`](trimesh.inertia.html#trimesh.inertia.transform_inertia)
  * [trimesh.intersections](trimesh.intersections.html)
    * [intersections.py](trimesh.intersections.html#intersections-py)
    * [`mesh_multiplane()`](trimesh.intersections.html#trimesh.intersections.mesh_multiplane)
    * [`mesh_plane()`](trimesh.intersections.html#trimesh.intersections.mesh_plane)
    * [`plane_lines()`](trimesh.intersections.html#trimesh.intersections.plane_lines)
    * [`planes_lines()`](trimesh.intersections.html#trimesh.intersections.planes_lines)
    * [`slice_faces_plane()`](trimesh.intersections.html#trimesh.intersections.slice_faces_plane)
    * [`slice_mesh_plane()`](trimesh.intersections.html#trimesh.intersections.slice_mesh_plane)
  * [trimesh.interval](trimesh.interval.html)
    * [interval.py](trimesh.interval.html#interval-py)
    * [`intersection()`](trimesh.interval.html#trimesh.interval.intersection)
    * [`union()`](trimesh.interval.html#trimesh.interval.union)
  * [trimesh.iteration](trimesh.iteration.html)
    * [`chain()`](trimesh.iteration.html#trimesh.iteration.chain)
    * [`reduce_cascade()`](trimesh.iteration.html#trimesh.iteration.reduce_cascade)
  * [trimesh.nsphere](trimesh.nsphere.html)
    * [nsphere.py](trimesh.nsphere.html#nsphere-py)
    * [`fit_nsphere()`](trimesh.nsphere.html#trimesh.nsphere.fit_nsphere)
    * [`is_nsphere()`](trimesh.nsphere.html#trimesh.nsphere.is_nsphere)
    * [`minimum_nsphere()`](trimesh.nsphere.html#trimesh.nsphere.minimum_nsphere)
  * [trimesh.parent](trimesh.parent.html)
    * [parent.py](trimesh.parent.html#parent-py)
    * [`Geometry`](trimesh.parent.html#trimesh.parent.Geometry)
      * [`Geometry.apply_scale()`](trimesh.parent.html#trimesh.parent.Geometry.apply_scale)
      * [`Geometry.apply_transform()`](trimesh.parent.html#trimesh.parent.Geometry.apply_transform)
      * [`Geometry.apply_translation()`](trimesh.parent.html#trimesh.parent.Geometry.apply_translation)
      * [`Geometry.bounds`](trimesh.parent.html#trimesh.parent.Geometry.bounds)
      * [`Geometry.copy()`](trimesh.parent.html#trimesh.parent.Geometry.copy)
      * [`Geometry.export()`](trimesh.parent.html#trimesh.parent.Geometry.export)
      * [`Geometry.extents`](trimesh.parent.html#trimesh.parent.Geometry.extents)
      * [`Geometry.identifier_hash`](trimesh.parent.html#trimesh.parent.Geometry.identifier_hash)
      * [`Geometry.is_empty`](trimesh.parent.html#trimesh.parent.Geometry.is_empty)
      * [`Geometry.metadata`](trimesh.parent.html#trimesh.parent.Geometry.metadata)
      * [`Geometry.scale`](trimesh.parent.html#trimesh.parent.Geometry.scale)
      * [`Geometry.show()`](trimesh.parent.html#trimesh.parent.Geometry.show)
      * [`Geometry.source`](trimesh.parent.html#trimesh.parent.Geometry.source)
      * [`Geometry.units`](trimesh.parent.html#trimesh.parent.Geometry.units)
    * [`Geometry3D`](trimesh.parent.html#trimesh.parent.Geometry3D)
      * [`Geometry3D.apply_obb()`](trimesh.parent.html#trimesh.parent.Geometry3D.apply_obb)
      * [`Geometry3D.bounding_box`](trimesh.parent.html#trimesh.parent.Geometry3D.bounding_box)
      * [`Geometry3D.bounding_box_oriented`](trimesh.parent.html#trimesh.parent.Geometry3D.bounding_box_oriented)
      * [`Geometry3D.bounding_cylinder`](trimesh.parent.html#trimesh.parent.Geometry3D.bounding_cylinder)
      * [`Geometry3D.bounding_primitive`](trimesh.parent.html#trimesh.parent.Geometry3D.bounding_primitive)
      * [`Geometry3D.bounding_sphere`](trimesh.parent.html#trimesh.parent.Geometry3D.bounding_sphere)
    * [`LoadSource`](trimesh.parent.html#trimesh.parent.LoadSource)
      * [`LoadSource.__init__()`](trimesh.parent.html#trimesh.parent.LoadSource.__init__)
      * [`LoadSource.file_name`](trimesh.parent.html#trimesh.parent.LoadSource.file_name)
      * [`LoadSource.file_obj`](trimesh.parent.html#trimesh.parent.LoadSource.file_obj)
      * [`LoadSource.file_path`](trimesh.parent.html#trimesh.parent.LoadSource.file_path)
      * [`LoadSource.file_type`](trimesh.parent.html#trimesh.parent.LoadSource.file_type)
      * [`LoadSource.resolver`](trimesh.parent.html#trimesh.parent.LoadSource.resolver)
      * [`LoadSource.was_opened`](trimesh.parent.html#trimesh.parent.LoadSource.was_opened)
  * [trimesh.permutate](trimesh.permutate.html)
    * [permutate.py](trimesh.permutate.html#permutate-py)
    * [`Permutator`](trimesh.permutate.html#trimesh.permutate.Permutator)
      * [`Permutator.__init__()`](trimesh.permutate.html#trimesh.permutate.Permutator.__init__)
      * [`Permutator.noise()`](trimesh.permutate.html#trimesh.permutate.Permutator.noise)
      * [`Permutator.tessellation()`](trimesh.permutate.html#trimesh.permutate.Permutator.tessellation)
      * [`Permutator.transform()`](trimesh.permutate.html#trimesh.permutate.Permutator.transform)
    * [`noise()`](trimesh.permutate.html#trimesh.permutate.noise)
    * [`tessellation()`](trimesh.permutate.html#trimesh.permutate.tessellation)
    * [`transform()`](trimesh.permutate.html#trimesh.permutate.transform)
  * [trimesh.points](trimesh.points.html)
    * [points.py](trimesh.points.html#points-py)
    * [`PointCloud`](trimesh.points.html#trimesh.points.PointCloud)
      * [`PointCloud.__init__()`](trimesh.points.html#trimesh.points.PointCloud.__init__)
      * [`PointCloud.apply_transform()`](trimesh.points.html#trimesh.points.PointCloud.apply_transform)
      * [`PointCloud.bounds`](trimesh.points.html#trimesh.points.PointCloud.bounds)
      * [`PointCloud.centroid`](trimesh.points.html#trimesh.points.PointCloud.centroid)
      * [`PointCloud.colors`](trimesh.points.html#trimesh.points.PointCloud.colors)
      * [`PointCloud.convex_hull`](trimesh.points.html#trimesh.points.PointCloud.convex_hull)
      * [`PointCloud.copy()`](trimesh.points.html#trimesh.points.PointCloud.copy)
      * [`PointCloud.export()`](trimesh.points.html#trimesh.points.PointCloud.export)
      * [`PointCloud.extents`](trimesh.points.html#trimesh.points.PointCloud.extents)
      * [`PointCloud.hash()`](trimesh.points.html#trimesh.points.PointCloud.hash)
      * [`PointCloud.identifier`](trimesh.points.html#trimesh.points.PointCloud.identifier)
      * [`PointCloud.identifier_hash`](trimesh.points.html#trimesh.points.PointCloud.identifier_hash)
      * [`PointCloud.is_empty`](trimesh.points.html#trimesh.points.PointCloud.is_empty)
      * [`PointCloud.kdtree`](trimesh.points.html#trimesh.points.PointCloud.kdtree)
      * [`PointCloud.merge_vertices()`](trimesh.points.html#trimesh.points.PointCloud.merge_vertices)
      * [`PointCloud.moment_inertia`](trimesh.points.html#trimesh.points.PointCloud.moment_inertia)
      * [`PointCloud.query()`](trimesh.points.html#trimesh.points.PointCloud.query)
      * [`PointCloud.scene()`](trimesh.points.html#trimesh.points.PointCloud.scene)
      * [`PointCloud.shape`](trimesh.points.html#trimesh.points.PointCloud.shape)
      * [`PointCloud.show()`](trimesh.points.html#trimesh.points.PointCloud.show)
      * [`PointCloud.vertices`](trimesh.points.html#trimesh.points.PointCloud.vertices)
      * [`PointCloud.weights`](trimesh.points.html#trimesh.points.PointCloud.weights)
    * [`k_means()`](trimesh.points.html#trimesh.points.k_means)
    * [`major_axis()`](trimesh.points.html#trimesh.points.major_axis)
    * [`plane_fit()`](trimesh.points.html#trimesh.points.plane_fit)
    * [`plot_points()`](trimesh.points.html#trimesh.points.plot_points)
    * [`point_plane_distance()`](trimesh.points.html#trimesh.points.point_plane_distance)
    * [`project_to_plane()`](trimesh.points.html#trimesh.points.project_to_plane)
    * [`radial_sort()`](trimesh.points.html#trimesh.points.radial_sort)
    * [`remove_close()`](trimesh.points.html#trimesh.points.remove_close)
    * [`tsp()`](trimesh.points.html#trimesh.points.tsp)
  * [trimesh.poses](trimesh.poses.html)
    * [poses.py](trimesh.poses.html#poses-py)
    * [`compute_stable_poses()`](trimesh.poses.html#trimesh.poses.compute_stable_poses)
  * [trimesh.primitives](trimesh.primitives.html)
    * [primitives.py](trimesh.primitives.html#primitives-py)
    * [`Box`](trimesh.primitives.html#trimesh.primitives.Box)
      * [`Box.__init__()`](trimesh.primitives.html#trimesh.primitives.Box.__init__)
      * [`Box.as_outline()`](trimesh.primitives.html#trimesh.primitives.Box.as_outline)
      * [`Box.is_oriented`](trimesh.primitives.html#trimesh.primitives.Box.is_oriented)
      * [`Box.sample_grid()`](trimesh.primitives.html#trimesh.primitives.Box.sample_grid)
      * [`Box.sample_volume()`](trimesh.primitives.html#trimesh.primitives.Box.sample_volume)
      * [`Box.to_dict()`](trimesh.primitives.html#trimesh.primitives.Box.to_dict)
      * [`Box.transform`](trimesh.primitives.html#trimesh.primitives.Box.transform)
      * [`Box.volume`](trimesh.primitives.html#trimesh.primitives.Box.volume)
    * [`Capsule`](trimesh.primitives.html#trimesh.primitives.Capsule)
      * [`Capsule.__init__()`](trimesh.primitives.html#trimesh.primitives.Capsule.__init__)
      * [`Capsule.area`](trimesh.primitives.html#trimesh.primitives.Capsule.area)
      * [`Capsule.direction`](trimesh.primitives.html#trimesh.primitives.Capsule.direction)
      * [`Capsule.to_dict()`](trimesh.primitives.html#trimesh.primitives.Capsule.to_dict)
      * [`Capsule.transform`](trimesh.primitives.html#trimesh.primitives.Capsule.transform)
      * [`Capsule.volume`](trimesh.primitives.html#trimesh.primitives.Capsule.volume)
    * [`Cylinder`](trimesh.primitives.html#trimesh.primitives.Cylinder)
      * [`Cylinder.__init__()`](trimesh.primitives.html#trimesh.primitives.Cylinder.__init__)
      * [`Cylinder.area`](trimesh.primitives.html#trimesh.primitives.Cylinder.area)
      * [`Cylinder.buffer()`](trimesh.primitives.html#trimesh.primitives.Cylinder.buffer)
      * [`Cylinder.direction`](trimesh.primitives.html#trimesh.primitives.Cylinder.direction)
      * [`Cylinder.moment_inertia`](trimesh.primitives.html#trimesh.primitives.Cylinder.moment_inertia)
      * [`Cylinder.segment`](trimesh.primitives.html#trimesh.primitives.Cylinder.segment)
      * [`Cylinder.to_dict()`](trimesh.primitives.html#trimesh.primitives.Cylinder.to_dict)
      * [`Cylinder.volume`](trimesh.primitives.html#trimesh.primitives.Cylinder.volume)
    * [`Extrusion`](trimesh.primitives.html#trimesh.primitives.Extrusion)
      * [`Extrusion.__init__()`](trimesh.primitives.html#trimesh.primitives.Extrusion.__init__)
      * [`Extrusion.area`](trimesh.primitives.html#trimesh.primitives.Extrusion.area)
      * [`Extrusion.bounding_box_oriented`](trimesh.primitives.html#trimesh.primitives.Extrusion.bounding_box_oriented)
      * [`Extrusion.buffer()`](trimesh.primitives.html#trimesh.primitives.Extrusion.buffer)
      * [`Extrusion.direction`](trimesh.primitives.html#trimesh.primitives.Extrusion.direction)
      * [`Extrusion.origin`](trimesh.primitives.html#trimesh.primitives.Extrusion.origin)
      * [`Extrusion.slide()`](trimesh.primitives.html#trimesh.primitives.Extrusion.slide)
      * [`Extrusion.to_dict()`](trimesh.primitives.html#trimesh.primitives.Extrusion.to_dict)
      * [`Extrusion.transform`](trimesh.primitives.html#trimesh.primitives.Extrusion.transform)
      * [`Extrusion.volume`](trimesh.primitives.html#trimesh.primitives.Extrusion.volume)
    * [`Primitive`](trimesh.primitives.html#trimesh.primitives.Primitive)
      * [`Primitive.__init__()`](trimesh.primitives.html#trimesh.primitives.Primitive.__init__)
      * [`Primitive.apply_transform()`](trimesh.primitives.html#trimesh.primitives.Primitive.apply_transform)
      * [`Primitive.copy()`](trimesh.primitives.html#trimesh.primitives.Primitive.copy)
      * [`Primitive.face_normals`](trimesh.primitives.html#trimesh.primitives.Primitive.face_normals)
      * [`Primitive.faces`](trimesh.primitives.html#trimesh.primitives.Primitive.faces)
      * [`Primitive.to_dict()`](trimesh.primitives.html#trimesh.primitives.Primitive.to_dict)
      * [`Primitive.to_mesh()`](trimesh.primitives.html#trimesh.primitives.Primitive.to_mesh)
      * [`Primitive.transform`](trimesh.primitives.html#trimesh.primitives.Primitive.transform)
      * [`Primitive.vertices`](trimesh.primitives.html#trimesh.primitives.Primitive.vertices)
    * [`PrimitiveAttributes`](trimesh.primitives.html#trimesh.primitives.PrimitiveAttributes)
      * [`PrimitiveAttributes.__init__()`](trimesh.primitives.html#trimesh.primitives.PrimitiveAttributes.__init__)
    * [`Sphere`](trimesh.primitives.html#trimesh.primitives.Sphere)
      * [`Sphere.__init__()`](trimesh.primitives.html#trimesh.primitives.Sphere.__init__)
      * [`Sphere.area`](trimesh.primitives.html#trimesh.primitives.Sphere.area)
      * [`Sphere.bounding_box_oriented`](trimesh.primitives.html#trimesh.primitives.Sphere.bounding_box_oriented)
      * [`Sphere.bounds`](trimesh.primitives.html#trimesh.primitives.Sphere.bounds)
      * [`Sphere.center`](trimesh.primitives.html#trimesh.primitives.Sphere.center)
      * [`Sphere.moment_inertia`](trimesh.primitives.html#trimesh.primitives.Sphere.moment_inertia)
      * [`Sphere.to_dict()`](trimesh.primitives.html#trimesh.primitives.Sphere.to_dict)
      * [`Sphere.volume`](trimesh.primitives.html#trimesh.primitives.Sphere.volume)
  * [trimesh.proximity](trimesh.proximity.html)
    * [proximity.py](trimesh.proximity.html#proximity-py)
    * [`NearestQueryResult`](trimesh.proximity.html#trimesh.proximity.NearestQueryResult)
      * [`NearestQueryResult.__init__()`](trimesh.proximity.html#trimesh.proximity.NearestQueryResult.__init__)
      * [`NearestQueryResult.has_normals()`](trimesh.proximity.html#trimesh.proximity.NearestQueryResult.has_normals)
    * [`ProximityQuery`](trimesh.proximity.html#trimesh.proximity.ProximityQuery)
      * [`ProximityQuery.__init__()`](trimesh.proximity.html#trimesh.proximity.ProximityQuery.__init__)
      * [`ProximityQuery.on_surface()`](trimesh.proximity.html#trimesh.proximity.ProximityQuery.on_surface)
      * [`ProximityQuery.signed_distance()`](trimesh.proximity.html#trimesh.proximity.ProximityQuery.signed_distance)
      * [`ProximityQuery.vertex()`](trimesh.proximity.html#trimesh.proximity.ProximityQuery.vertex)
    * [`closest_point()`](trimesh.proximity.html#trimesh.proximity.closest_point)
    * [`closest_point_naive()`](trimesh.proximity.html#trimesh.proximity.closest_point_naive)
    * [`longest_ray()`](trimesh.proximity.html#trimesh.proximity.longest_ray)
    * [`max_tangent_sphere()`](trimesh.proximity.html#trimesh.proximity.max_tangent_sphere)
    * [`nearby_faces()`](trimesh.proximity.html#trimesh.proximity.nearby_faces)
    * [`signed_distance()`](trimesh.proximity.html#trimesh.proximity.signed_distance)
    * [`thickness()`](trimesh.proximity.html#trimesh.proximity.thickness)
  * [trimesh.registration](trimesh.registration.html)
    * [registration.py](trimesh.registration.html#registration-py)
    * [`icp()`](trimesh.registration.html#trimesh.registration.icp)
    * [`mesh_other()`](trimesh.registration.html#trimesh.registration.mesh_other)
    * [`nricp_amberg()`](trimesh.registration.html#trimesh.registration.nricp_amberg)
    * [`nricp_sumner()`](trimesh.registration.html#trimesh.registration.nricp_sumner)
    * [`procrustes()`](trimesh.registration.html#trimesh.registration.procrustes)
  * [trimesh.remesh](trimesh.remesh.html)
    * [remesh.py](trimesh.remesh.html#remesh-py)
    * [`subdivide()`](trimesh.remesh.html#trimesh.remesh.subdivide)
    * [`subdivide_loop()`](trimesh.remesh.html#trimesh.remesh.subdivide_loop)
    * [`subdivide_to_size()`](trimesh.remesh.html#trimesh.remesh.subdivide_to_size)
  * [trimesh.rendering](trimesh.rendering.html)
    * [rendering.py](trimesh.rendering.html#rendering-py)
    * [`colors_to_gl()`](trimesh.rendering.html#trimesh.rendering.colors_to_gl)
    * [`convert_to_vertexlist()`](trimesh.rendering.html#trimesh.rendering.convert_to_vertexlist)
    * [`light_to_gl()`](trimesh.rendering.html#trimesh.rendering.light_to_gl)
    * [`material_to_texture()`](trimesh.rendering.html#trimesh.rendering.material_to_texture)
    * [`matrix_to_gl()`](trimesh.rendering.html#trimesh.rendering.matrix_to_gl)
    * [`mesh_to_vertexlist()`](trimesh.rendering.html#trimesh.rendering.mesh_to_vertexlist)
    * [`path_to_vertexlist()`](trimesh.rendering.html#trimesh.rendering.path_to_vertexlist)
    * [`points_to_vertexlist()`](trimesh.rendering.html#trimesh.rendering.points_to_vertexlist)
    * [`vector_to_gl()`](trimesh.rendering.html#trimesh.rendering.vector_to_gl)
  * [trimesh.repair](trimesh.repair.html)
    * [repair.py](trimesh.repair.html#repair-py)
    * [`broken_faces()`](trimesh.repair.html#trimesh.repair.broken_faces)
    * [`fill_holes()`](trimesh.repair.html#trimesh.repair.fill_holes)
    * [`fix_inversion()`](trimesh.repair.html#trimesh.repair.fix_inversion)
    * [`fix_normals()`](trimesh.repair.html#trimesh.repair.fix_normals)
    * [`fix_winding()`](trimesh.repair.html#trimesh.repair.fix_winding)
    * [`stitch()`](trimesh.repair.html#trimesh.repair.stitch)
  * [trimesh.resolvers](trimesh.resolvers.html)
    * [resolvers.py](trimesh.resolvers.html#resolvers-py)
    * [`FilePathResolver`](trimesh.resolvers.html#trimesh.resolvers.FilePathResolver)
      * [`FilePathResolver.__init__()`](trimesh.resolvers.html#trimesh.resolvers.FilePathResolver.__init__)
      * [`FilePathResolver.get()`](trimesh.resolvers.html#trimesh.resolvers.FilePathResolver.get)
      * [`FilePathResolver.keys()`](trimesh.resolvers.html#trimesh.resolvers.FilePathResolver.keys)
      * [`FilePathResolver.namespaced()`](trimesh.resolvers.html#trimesh.resolvers.FilePathResolver.namespaced)
      * [`FilePathResolver.write()`](trimesh.resolvers.html#trimesh.resolvers.FilePathResolver.write)
    * [`GithubResolver`](trimesh.resolvers.html#trimesh.resolvers.GithubResolver)
      * [`GithubResolver.__init__()`](trimesh.resolvers.html#trimesh.resolvers.GithubResolver.__init__)
      * [`GithubResolver.get()`](trimesh.resolvers.html#trimesh.resolvers.GithubResolver.get)
      * [`GithubResolver.keys()`](trimesh.resolvers.html#trimesh.resolvers.GithubResolver.keys)
      * [`GithubResolver.namespaced()`](trimesh.resolvers.html#trimesh.resolvers.GithubResolver.namespaced)
      * [`GithubResolver.write()`](trimesh.resolvers.html#trimesh.resolvers.GithubResolver.write)
      * [`GithubResolver.zipped`](trimesh.resolvers.html#trimesh.resolvers.GithubResolver.zipped)
    * [`Resolver`](trimesh.resolvers.html#trimesh.resolvers.Resolver)
      * [`Resolver.__init__()`](trimesh.resolvers.html#trimesh.resolvers.Resolver.__init__)
      * [`Resolver.get()`](trimesh.resolvers.html#trimesh.resolvers.Resolver.get)
      * [`Resolver.keys()`](trimesh.resolvers.html#trimesh.resolvers.Resolver.keys)
      * [`Resolver.namespaced()`](trimesh.resolvers.html#trimesh.resolvers.Resolver.namespaced)
      * [`Resolver.write()`](trimesh.resolvers.html#trimesh.resolvers.Resolver.write)
    * [`WebResolver`](trimesh.resolvers.html#trimesh.resolvers.WebResolver)
      * [`WebResolver.__init__()`](trimesh.resolvers.html#trimesh.resolvers.WebResolver.__init__)
      * [`WebResolver.get()`](trimesh.resolvers.html#trimesh.resolvers.WebResolver.get)
      * [`WebResolver.get_base()`](trimesh.resolvers.html#trimesh.resolvers.WebResolver.get_base)
      * [`WebResolver.keys()`](trimesh.resolvers.html#trimesh.resolvers.WebResolver.keys)
      * [`WebResolver.namespaced()`](trimesh.resolvers.html#trimesh.resolvers.WebResolver.namespaced)
      * [`WebResolver.write()`](trimesh.resolvers.html#trimesh.resolvers.WebResolver.write)
    * [`ZipResolver`](trimesh.resolvers.html#trimesh.resolvers.ZipResolver)
      * [`ZipResolver.__init__()`](trimesh.resolvers.html#trimesh.resolvers.ZipResolver.__init__)
      * [`ZipResolver.export()`](trimesh.resolvers.html#trimesh.resolvers.ZipResolver.export)
      * [`ZipResolver.get()`](trimesh.resolvers.html#trimesh.resolvers.ZipResolver.get)
      * [`ZipResolver.keys()`](trimesh.resolvers.html#trimesh.resolvers.ZipResolver.keys)
      * [`ZipResolver.namespaced()`](trimesh.resolvers.html#trimesh.resolvers.ZipResolver.namespaced)
      * [`ZipResolver.write()`](trimesh.resolvers.html#trimesh.resolvers.ZipResolver.write)
    * [`nearby_names()`](trimesh.resolvers.html#trimesh.resolvers.nearby_names)
  * [trimesh.sample](trimesh.sample.html)
    * [sample.py](trimesh.sample.html#sample-py)
    * [`sample_surface()`](trimesh.sample.html#trimesh.sample.sample_surface)
    * [`sample_surface_even()`](trimesh.sample.html#trimesh.sample.sample_surface_even)
    * [`sample_surface_sphere()`](trimesh.sample.html#trimesh.sample.sample_surface_sphere)
    * [`volume_mesh()`](trimesh.sample.html#trimesh.sample.volume_mesh)
    * [`volume_rectangular()`](trimesh.sample.html#trimesh.sample.volume_rectangular)
  * [trimesh.schemas](trimesh.schemas.html)
    * [schemas.py](trimesh.schemas.html#schemas-py)
    * [`resolve()`](trimesh.schemas.html#trimesh.schemas.resolve)
  * [trimesh.smoothing](trimesh.smoothing.html)
    * [`dilate_slope()`](trimesh.smoothing.html#trimesh.smoothing.dilate_slope)
    * [`filter_humphrey()`](trimesh.smoothing.html#trimesh.smoothing.filter_humphrey)
    * [`filter_laplacian()`](trimesh.smoothing.html#trimesh.smoothing.filter_laplacian)
    * [`filter_mut_dif_laplacian()`](trimesh.smoothing.html#trimesh.smoothing.filter_mut_dif_laplacian)
    * [`filter_taubin()`](trimesh.smoothing.html#trimesh.smoothing.filter_taubin)
    * [`get_vertices_normals()`](trimesh.smoothing.html#trimesh.smoothing.get_vertices_normals)
    * [`laplacian_calculation()`](trimesh.smoothing.html#trimesh.smoothing.laplacian_calculation)
  * [trimesh.transformations](trimesh.transformations.html)
    * [Requirements](trimesh.transformations.html#requirements)
    * [`Arcball`](trimesh.transformations.html#trimesh.transformations.Arcball)
      * [`Arcball.__init__()`](trimesh.transformations.html#trimesh.transformations.Arcball.__init__)
      * [`Arcball.constrain`](trimesh.transformations.html#trimesh.transformations.Arcball.constrain)
      * [`Arcball.down()`](trimesh.transformations.html#trimesh.transformations.Arcball.down)
      * [`Arcball.drag()`](trimesh.transformations.html#trimesh.transformations.Arcball.drag)
      * [`Arcball.matrix()`](trimesh.transformations.html#trimesh.transformations.Arcball.matrix)
      * [`Arcball.next()`](trimesh.transformations.html#trimesh.transformations.Arcball.next)
      * [`Arcball.place()`](trimesh.transformations.html#trimesh.transformations.Arcball.place)
      * [`Arcball.setaxes()`](trimesh.transformations.html#trimesh.transformations.Arcball.setaxes)
    * [`affine_matrix_from_points()`](trimesh.transformations.html#trimesh.transformations.affine_matrix_from_points)
    * [`angle_between_vectors()`](trimesh.transformations.html#trimesh.transformations.angle_between_vectors)
    * [`arcball_constrain_to_axis()`](trimesh.transformations.html#trimesh.transformations.arcball_constrain_to_axis)
    * [`arcball_map_to_sphere()`](trimesh.transformations.html#trimesh.transformations.arcball_map_to_sphere)
    * [`arcball_nearest_axis()`](trimesh.transformations.html#trimesh.transformations.arcball_nearest_axis)
    * [`clip_matrix()`](trimesh.transformations.html#trimesh.transformations.clip_matrix)
    * [`compose_matrix()`](trimesh.transformations.html#trimesh.transformations.compose_matrix)
    * [`concatenate_matrices()`](trimesh.transformations.html#trimesh.transformations.concatenate_matrices)
    * [`decompose_matrix()`](trimesh.transformations.html#trimesh.transformations.decompose_matrix)
    * [`euler_from_matrix()`](trimesh.transformations.html#trimesh.transformations.euler_from_matrix)
    * [`euler_from_quaternion()`](trimesh.transformations.html#trimesh.transformations.euler_from_quaternion)
    * [`euler_matrix()`](trimesh.transformations.html#trimesh.transformations.euler_matrix)
    * [`fix_rigid()`](trimesh.transformations.html#trimesh.transformations.fix_rigid)
    * [`flips_winding()`](trimesh.transformations.html#trimesh.transformations.flips_winding)
    * [`identity_matrix()`](trimesh.transformations.html#trimesh.transformations.identity_matrix)
    * [`inverse_matrix()`](trimesh.transformations.html#trimesh.transformations.inverse_matrix)
    * [`is_rigid()`](trimesh.transformations.html#trimesh.transformations.is_rigid)
    * [`is_same_quaternion()`](trimesh.transformations.html#trimesh.transformations.is_same_quaternion)
    * [`is_same_transform()`](trimesh.transformations.html#trimesh.transformations.is_same_transform)
    * [`orthogonalization_matrix()`](trimesh.transformations.html#trimesh.transformations.orthogonalization_matrix)
    * [`planar_matrix()`](trimesh.transformations.html#trimesh.transformations.planar_matrix)
    * [`planar_matrix_to_3D()`](trimesh.transformations.html#trimesh.transformations.planar_matrix_to_3D)
    * [`projection_from_matrix()`](trimesh.transformations.html#trimesh.transformations.projection_from_matrix)
    * [`projection_matrix()`](trimesh.transformations.html#trimesh.transformations.projection_matrix)
    * [`quaternion_about_axis()`](trimesh.transformations.html#trimesh.transformations.quaternion_about_axis)
    * [`quaternion_conjugate()`](trimesh.transformations.html#trimesh.transformations.quaternion_conjugate)
    * [`quaternion_from_euler()`](trimesh.transformations.html#trimesh.transformations.quaternion_from_euler)
    * [`quaternion_from_matrix()`](trimesh.transformations.html#trimesh.transformations.quaternion_from_matrix)
    * [`quaternion_imag()`](trimesh.transformations.html#trimesh.transformations.quaternion_imag)
    * [`quaternion_inverse()`](trimesh.transformations.html#trimesh.transformations.quaternion_inverse)
    * [`quaternion_matrix()`](trimesh.transformations.html#trimesh.transformations.quaternion_matrix)
    * [`quaternion_multiply()`](trimesh.transformations.html#trimesh.transformations.quaternion_multiply)
    * [`quaternion_real()`](trimesh.transformations.html#trimesh.transformations.quaternion_real)
    * [`quaternion_slerp()`](trimesh.transformations.html#trimesh.transformations.quaternion_slerp)
    * [`random_quaternion()`](trimesh.transformations.html#trimesh.transformations.random_quaternion)
    * [`random_rotation_matrix()`](trimesh.transformations.html#trimesh.transformations.random_rotation_matrix)
    * [`random_vector()`](trimesh.transformations.html#trimesh.transformations.random_vector)
    * [`reflection_from_matrix()`](trimesh.transformations.html#trimesh.transformations.reflection_from_matrix)
    * [`reflection_matrix()`](trimesh.transformations.html#trimesh.transformations.reflection_matrix)
    * [`rotation_from_matrix()`](trimesh.transformations.html#trimesh.transformations.rotation_from_matrix)
    * [`rotation_matrix()`](trimesh.transformations.html#trimesh.transformations.rotation_matrix)
    * [`scale_and_translate()`](trimesh.transformations.html#trimesh.transformations.scale_and_translate)
    * [`scale_from_matrix()`](trimesh.transformations.html#trimesh.transformations.scale_from_matrix)
    * [`scale_matrix()`](trimesh.transformations.html#trimesh.transformations.scale_matrix)
    * [`shear_from_matrix()`](trimesh.transformations.html#trimesh.transformations.shear_from_matrix)
    * [`shear_matrix()`](trimesh.transformations.html#trimesh.transformations.shear_matrix)
    * [`spherical_matrix()`](trimesh.transformations.html#trimesh.transformations.spherical_matrix)
    * [`superimposition_matrix()`](trimesh.transformations.html#trimesh.transformations.superimposition_matrix)
    * [`transform_around()`](trimesh.transformations.html#trimesh.transformations.transform_around)
    * [`transform_points()`](trimesh.transformations.html#trimesh.transformations.transform_points)
    * [`translation_from_matrix()`](trimesh.transformations.html#trimesh.transformations.translation_from_matrix)
    * [`translation_matrix()`](trimesh.transformations.html#trimesh.transformations.translation_matrix)
    * [`unit_vector()`](trimesh.transformations.html#trimesh.transformations.unit_vector)
    * [`vector_norm()`](trimesh.transformations.html#trimesh.transformations.vector_norm)
    * [`vector_product()`](trimesh.transformations.html#trimesh.transformations.vector_product)
  * [trimesh.triangles](trimesh.triangles.html)
    * [triangles.py](trimesh.triangles.html#triangles-py)
    * [`MassProperties`](trimesh.triangles.html#trimesh.triangles.MassProperties)
      * [`MassProperties.__init__()`](trimesh.triangles.html#trimesh.triangles.MassProperties.__init__)
      * [`MassProperties.center_mass`](trimesh.triangles.html#trimesh.triangles.MassProperties.center_mass)
      * [`MassProperties.density`](trimesh.triangles.html#trimesh.triangles.MassProperties.density)
      * [`MassProperties.inertia`](trimesh.triangles.html#trimesh.triangles.MassProperties.inertia)
      * [`MassProperties.mass`](trimesh.triangles.html#trimesh.triangles.MassProperties.mass)
      * [`MassProperties.volume`](trimesh.triangles.html#trimesh.triangles.MassProperties.volume)
    * [`all_coplanar()`](trimesh.triangles.html#trimesh.triangles.all_coplanar)
    * [`angles()`](trimesh.triangles.html#trimesh.triangles.angles)
    * [`any_coplanar()`](trimesh.triangles.html#trimesh.triangles.any_coplanar)
    * [`area()`](trimesh.triangles.html#trimesh.triangles.area)
    * [`barycentric_to_points()`](trimesh.triangles.html#trimesh.triangles.barycentric_to_points)
    * [`bounds_tree()`](trimesh.triangles.html#trimesh.triangles.bounds_tree)
    * [`closest_point()`](trimesh.triangles.html#trimesh.triangles.closest_point)
    * [`cross()`](trimesh.triangles.html#trimesh.triangles.cross)
    * [`extents()`](trimesh.triangles.html#trimesh.triangles.extents)
    * [`mass_properties()`](trimesh.triangles.html#trimesh.triangles.mass_properties)
    * [`nondegenerate()`](trimesh.triangles.html#trimesh.triangles.nondegenerate)
    * [`normals()`](trimesh.triangles.html#trimesh.triangles.normals)
    * [`points_to_barycentric()`](trimesh.triangles.html#trimesh.triangles.points_to_barycentric)
    * [`to_kwargs()`](trimesh.triangles.html#trimesh.triangles.to_kwargs)
    * [`windings_aligned()`](trimesh.triangles.html#trimesh.triangles.windings_aligned)
  * [trimesh.typed](trimesh.typed.html)
    * [`Any`](trimesh.typed.html#trimesh.typed.Any)
    * [`BinaryIO`](trimesh.typed.html#trimesh.typed.BinaryIO)
      * [`BinaryIO.write()`](trimesh.typed.html#trimesh.typed.BinaryIO.write)
    * [`Callable`](trimesh.typed.html#trimesh.typed.Callable)
    * [`Dict`](trimesh.typed.html#trimesh.typed.Dict)
    * [`Hashable`](trimesh.typed.html#trimesh.typed.Hashable)
    * [`IO`](trimesh.typed.html#trimesh.typed.IO)
      * [`IO.close()`](trimesh.typed.html#trimesh.typed.IO.close)
      * [`IO.closed`](trimesh.typed.html#trimesh.typed.IO.closed)
      * [`IO.fileno()`](trimesh.typed.html#trimesh.typed.IO.fileno)
      * [`IO.flush()`](trimesh.typed.html#trimesh.typed.IO.flush)
      * [`IO.isatty()`](trimesh.typed.html#trimesh.typed.IO.isatty)
      * [`IO.mode`](trimesh.typed.html#trimesh.typed.IO.mode)
      * [`IO.name`](trimesh.typed.html#trimesh.typed.IO.name)
      * [`IO.read()`](trimesh.typed.html#trimesh.typed.IO.read)
      * [`IO.readable()`](trimesh.typed.html#trimesh.typed.IO.readable)
      * [`IO.readline()`](trimesh.typed.html#trimesh.typed.IO.readline)
      * [`IO.readlines()`](trimesh.typed.html#trimesh.typed.IO.readlines)
      * [`IO.seek()`](trimesh.typed.html#trimesh.typed.IO.seek)
      * [`IO.seekable()`](trimesh.typed.html#trimesh.typed.IO.seekable)
      * [`IO.tell()`](trimesh.typed.html#trimesh.typed.IO.tell)
      * [`IO.truncate()`](trimesh.typed.html#trimesh.typed.IO.truncate)
      * [`IO.writable()`](trimesh.typed.html#trimesh.typed.IO.writable)
      * [`IO.write()`](trimesh.typed.html#trimesh.typed.IO.write)
      * [`IO.writelines()`](trimesh.typed.html#trimesh.typed.IO.writelines)
    * [`Iterable`](trimesh.typed.html#trimesh.typed.Iterable)
    * [`List`](trimesh.typed.html#trimesh.typed.List)
    * [`Mapping`](trimesh.typed.html#trimesh.typed.Mapping)
      * [`Mapping.get()`](trimesh.typed.html#trimesh.typed.Mapping.get)
      * [`Mapping.items()`](trimesh.typed.html#trimesh.typed.Mapping.items)
      * [`Mapping.keys()`](trimesh.typed.html#trimesh.typed.Mapping.keys)
      * [`Mapping.values()`](trimesh.typed.html#trimesh.typed.Mapping.values)
    * [`Sequence`](trimesh.typed.html#trimesh.typed.Sequence)
      * [`Sequence.count()`](trimesh.typed.html#trimesh.typed.Sequence.count)
      * [`Sequence.index()`](trimesh.typed.html#trimesh.typed.Sequence.index)
    * [`Set`](trimesh.typed.html#trimesh.typed.Set)
    * [`Tuple`](trimesh.typed.html#trimesh.typed.Tuple)
    * [`float64`](trimesh.typed.html#trimesh.typed.float64)
      * [`float64.as_integer_ratio()`](trimesh.typed.html#trimesh.typed.float64.as_integer_ratio)
      * [`float64.is_integer()`](trimesh.typed.html#trimesh.typed.float64.is_integer)
    * [`int64`](trimesh.typed.html#trimesh.typed.int64)
      * [`int64.bit_count()`](trimesh.typed.html#trimesh.typed.int64.bit_count)
  * [trimesh.units](trimesh.units.html)
    * [units.py](trimesh.units.html#units-py)
    * [`keys()`](trimesh.units.html#trimesh.units.keys)
    * [`to_inch()`](trimesh.units.html#trimesh.units.to_inch)
    * [`unit_conversion()`](trimesh.units.html#trimesh.units.unit_conversion)
    * [`units_from_metadata()`](trimesh.units.html#trimesh.units.units_from_metadata)
  * [trimesh.util](trimesh.util.html)
    * [`FunctionRegistry`](trimesh.util.html#trimesh.util.FunctionRegistry)
      * [`FunctionRegistry.__init__()`](trimesh.util.html#trimesh.util.FunctionRegistry.__init__)
    * [`allclose()`](trimesh.util.html#trimesh.util.allclose)
    * [`append_faces()`](trimesh.util.html#trimesh.util.append_faces)
    * [`array_to_encoded()`](trimesh.util.html#trimesh.util.array_to_encoded)
    * [`array_to_string()`](trimesh.util.html#trimesh.util.array_to_string)
    * [`attach_to_log()`](trimesh.util.html#trimesh.util.attach_to_log)
    * [`bounds_tree()`](trimesh.util.html#trimesh.util.bounds_tree)
    * [`comment_strip()`](trimesh.util.html#trimesh.util.comment_strip)
    * [`compress()`](trimesh.util.html#trimesh.util.compress)
    * [`concatenate()`](trimesh.util.html#trimesh.util.concatenate)
    * [`convert_like()`](trimesh.util.html#trimesh.util.convert_like)
    * [`decimal_to_digits()`](trimesh.util.html#trimesh.util.decimal_to_digits)
    * [`decode_keys()`](trimesh.util.html#trimesh.util.decode_keys)
    * [`decode_text()`](trimesh.util.html#trimesh.util.decode_text)
    * [`decompress()`](trimesh.util.html#trimesh.util.decompress)
    * [`diagonal_dot()`](trimesh.util.html#trimesh.util.diagonal_dot)
    * [`distance_to_end()`](trimesh.util.html#trimesh.util.distance_to_end)
    * [`encoded_to_array()`](trimesh.util.html#trimesh.util.encoded_to_array)
    * [`euclidean()`](trimesh.util.html#trimesh.util.euclidean)
    * [`generate_basis()`](trimesh.util.html#trimesh.util.generate_basis)
    * [`grid_arange()`](trimesh.util.html#trimesh.util.grid_arange)
    * [`grid_linspace()`](trimesh.util.html#trimesh.util.grid_linspace)
    * [`has_module()`](trimesh.util.html#trimesh.util.has_module)
    * [`is_binary_file()`](trimesh.util.html#trimesh.util.is_binary_file)
    * [`is_ccw()`](trimesh.util.html#trimesh.util.is_ccw)
    * [`is_file()`](trimesh.util.html#trimesh.util.is_file)
    * [`is_instance_named()`](trimesh.util.html#trimesh.util.is_instance_named)
    * [`is_pathlib()`](trimesh.util.html#trimesh.util.is_pathlib)
    * [`is_sequence()`](trimesh.util.html#trimesh.util.is_sequence)
    * [`is_shape()`](trimesh.util.html#trimesh.util.is_shape)
    * [`is_string()`](trimesh.util.html#trimesh.util.is_string)
    * [`isclose()`](trimesh.util.html#trimesh.util.isclose)
    * [`jsonify()`](trimesh.util.html#trimesh.util.jsonify)
    * [`make_sequence()`](trimesh.util.html#trimesh.util.make_sequence)
    * [`multi_dict()`](trimesh.util.html#trimesh.util.multi_dict)
    * [`pairwise()`](trimesh.util.html#trimesh.util.pairwise)
    * [`row_norm()`](trimesh.util.html#trimesh.util.row_norm)
    * [`sigfig_int()`](trimesh.util.html#trimesh.util.sigfig_int)
    * [`sigfig_round()`](trimesh.util.html#trimesh.util.sigfig_round)
    * [`spherical_to_vector()`](trimesh.util.html#trimesh.util.spherical_to_vector)
    * [`split_extension()`](trimesh.util.html#trimesh.util.split_extension)
    * [`stack_3D()`](trimesh.util.html#trimesh.util.stack_3D)
    * [`stack_lines()`](trimesh.util.html#trimesh.util.stack_lines)
    * [`structured_array_to_string()`](trimesh.util.html#trimesh.util.structured_array_to_string)
    * [`submesh()`](trimesh.util.html#trimesh.util.submesh)
    * [`to_ascii()`](trimesh.util.html#trimesh.util.to_ascii)
    * [`tolist()`](trimesh.util.html#trimesh.util.tolist)
    * [`triangle_fans_to_faces()`](trimesh.util.html#trimesh.util.triangle_fans_to_faces)
    * [`triangle_strips_to_faces()`](trimesh.util.html#trimesh.util.triangle_strips_to_faces)
    * [`type_bases()`](trimesh.util.html#trimesh.util.type_bases)
    * [`type_named()`](trimesh.util.html#trimesh.util.type_named)
    * [`unique_id()`](trimesh.util.html#trimesh.util.unique_id)
    * [`unique_name()`](trimesh.util.html#trimesh.util.unique_name)
    * [`unitize()`](trimesh.util.html#trimesh.util.unitize)
    * [`vector_hemisphere()`](trimesh.util.html#trimesh.util.vector_hemisphere)
    * [`vector_to_spherical()`](trimesh.util.html#trimesh.util.vector_to_spherical)
    * [`vstack_empty()`](trimesh.util.html#trimesh.util.vstack_empty)
    * [`wrap_as_stream()`](trimesh.util.html#trimesh.util.wrap_as_stream)
    * [`write_encoded()`](trimesh.util.html#trimesh.util.write_encoded)
    * [`zero_pad()`](trimesh.util.html#trimesh.util.zero_pad)
  * [trimesh.version](trimesh.version.html)

## <https://github.com/mikedh/trimesh>¶

Trimesh is a pure Python (2.7- 3.3+) library for loading and using triangular meshes with an emphasis on watertight meshes. The goal of the library is to provide a fully featured Trimesh object which allows for easy manipulation and analysis, in the style of the Polygon object in the Shapely library.

_class _trimesh.Geometry¶
    

Bases: `ABC`

Geometry is the parent class for all geometry.

By decorating a method with abc.abstractmethod it means the objects that inherit from Geometry MUST implement those methods.

apply_scale(_scaling_)¶
    

Scale the mesh.

Parameters:
    

**scaling** (_float_ _or_ _(__3_ _,__)__float_) – Scale factor to apply to the mesh

_abstractmethod _apply_transform(_matrix : ArrayLike_) → [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")¶
    

apply_translation(_translation : ArrayLike_)¶
    

Translate the current mesh.

Parameters:
    

**translation** (_(__3_ _,__)__float_) – Translation in XYZ

_abstract property _bounds _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

_abstractmethod _copy()¶
    

_abstractmethod _export(_file_obj_ , _file_type =None_)¶
    

_abstract property _extents _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

_abstract property _identifier_hash _: str_¶
    

_abstract property _is_empty _: bool_¶
    

metadata _: dict_¶
    

_property _scale _: float_¶
    

A loosely specified “order of magnitude scale” for the geometry which always returns a value and can be used to make code more robust to large scaling differences.

It returns the diagonal of the axis aligned bounding box or if anything is invalid or undefined, 1.0.

Returns:
    

**scale** – Approximate order of magnitude scale of the geometry.

Return type:
    

float

_abstractmethod _show()¶
    

_property _source _: [LoadSource](trimesh.parent.html#trimesh.parent.LoadSource "trimesh.parent.LoadSource")_¶
    

Where and what was this current geometry loaded from?

Returns:
    

If loaded from a file, has the path, type, etc.

Return type:
    

source

_property _units _: str | None_¶
    

Definition of units for the mesh.

Returns:
    

**units** – Unit system mesh is in, or None if not defined

Return type:
    

str

_class _trimesh.PointCloud(_vertices_ , _colors =None_, _metadata =None_, _** kwargs_)¶
    

Bases: [`Geometry3D`](trimesh.parent.html#trimesh.parent.Geometry3D "trimesh.parent.Geometry3D")

Hold 3D points in an object which can be visualized in a scene.

__init__(_vertices_ , _colors =None_, _metadata =None_, _** kwargs_)¶
    

Load an array of points into a PointCloud object.

Parameters:
    

  * **vertices** (_(__n_ _,__3_ _)__float_) – Points in space

  * **colors** (_(__n_ _,__4_ _)__uint8_ _or_ _None_) – RGBA colors for each point

  * **metadata** (_dict_ _or_ _None_) – Metadata about points

apply_transform(_transform_)¶
    

Apply a homogeneous transformation to the PointCloud object in- place.

Parameters:
    

**transform** (_(__4_ _,__4_ _)__float_) – Homogeneous transformation to apply to PointCloud

_property _bounds¶
    

The axis aligned bounds of the PointCloud

Returns:
    

**bounds** – Minimum, Maximum verteex

Return type:
    

(2, 3) float

_property _centroid¶
    

The mean vertex position

Returns:
    

**centroid** – Mean vertex position

Return type:
    

(3,) float

_property _colors¶
    

Stored per- point color

Returns:
    

**colors** – Per- point RGBA color

Return type:
    

(len(self.vertices), 4) np.uint8

_property _convex_hull¶
    

A convex hull of every point.

Returns:
    

**convex_hull** – A watertight mesh of the hull of the points

Return type:
    

trimesh.Trimesh

copy()¶
    

Safely get a copy of the current point cloud.

Copied objects will have emptied caches to avoid memory issues and so may be slow on initial operations until caches are regenerated.

Current object will _not_ have its cache cleared.

Returns:
    

**copied** – Copy of current point cloud

Return type:
    

trimesh.PointCloud

export(_file_obj =None_, _file_type =None_, _** kwargs_)¶
    

Export the current pointcloud to a file object. If file_obj is a filename, file will be written there. Supported formats are xyz :param file_obj: str, file name where to save the pointcloud

> None, if you would like this function to return the export blob

Parameters:
    

**file_type** (_str_) – Which file type to export as. If file name is passed this is not required

_property _extents¶
    

The size of the axis aligned bounds

Returns:
    

**extents** – Edge length of axis aligned bounding box

Return type:
    

(3,) float

hash()¶
    

Get a hash of the current vertices.

Returns:
    

**hash** – Hash of self.vertices

Return type:
    

str

_property _identifier _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return a simple array representing this PointCloud that can be used to identify identical arrays.

Returns:
    

**identifier** – A flat array of data representing the cloud.

Return type:
    

(9,)

_property _identifier_hash _: str_¶
    

A hash of the PointCloud’s identifier that can be used to detect duplicates.

_property _is_empty¶
    

Are there any vertices defined or not.

Returns:
    

**empty** – True if no vertices defined

Return type:
    

bool

_property _kdtree¶
    

Return a scipy.spatial.cKDTree of the vertices of the mesh. Not cached as this lead to observed memory issues and segfaults.

Returns:
    

**tree** – Contains mesh.vertices

Return type:
    

scipy.spatial.cKDTree

merge_vertices()¶
    

Merge vertices closer than tol.merge (default: 1e-8)

_property _moment_inertia _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

query(_input_points_ , _** kwargs_)¶
    

Find the the closest points and associated attributes from this PointCloud. :param input_points: Input query points :type input_points: (n, 3) float :param kwargs: Arguments for proximity.query_from_points :type kwargs: dict :param result: Result of the query. :type result: proximity.NearestQueryResult

scene()¶
    

A scene containing just the PointCloud

Returns:
    

**scene** – Scene object containing this PointCloud

Return type:
    

trimesh.Scene

_property _shape¶
    

Get the shape of the pointcloud

Returns:
    

**shape** – Shape of vertex array

Return type:
    

(2,) int

show(_** kwargs_)¶
    

Open a viewer window displaying the current PointCloud

_property _vertices¶
    

Vertices of the PointCloud

Returns:
    

**vertices** – Points in the PointCloud

Return type:
    

(n, 3) float

_property _weights _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

If each point has a specific weight assigned to it.

Returns:
    

**weights** – A per-vertex weight.

Return type:
    

(n,)

_class _trimesh.Scene(_geometry : [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry") | [Iterable](trimesh.typed.html#trimesh.typed.Iterable "collections.abc.Iterable")[[Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")] | dict[str, [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")] | ArrayLike | None = None_, _base_frame : str = 'world'_, _metadata : dict | None = None_, _graph : [SceneGraph](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph "trimesh.scene.transforms.SceneGraph") | None = None_, _camera : [Camera](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera "trimesh.scene.cameras.Camera") | None = None_, _lights : [Sequence](trimesh.typed.html#trimesh.typed.Sequence "collections.abc.Sequence")[[Light](trimesh.scene.lighting.html#trimesh.scene.lighting.Light "trimesh.scene.lighting.Light")] | None = None_, _camera_transform : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[_ScalarT]] | None = None_)¶
    

Bases: [`Geometry3D`](trimesh.parent.html#trimesh.parent.Geometry3D "trimesh.parent.Geometry3D")

A simple scene graph which can be rendered directly via pyglet/openGL or through other endpoints such as a raytracer. Meshes are added by name, which can then be moved by updating transform in the transform tree.

__init__(_geometry : [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry") | [Iterable](trimesh.typed.html#trimesh.typed.Iterable "collections.abc.Iterable")[[Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")] | dict[str, [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")] | ArrayLike | None = None_, _base_frame : str = 'world'_, _metadata : dict | None = None_, _graph : [SceneGraph](trimesh.scene.transforms.html#trimesh.scene.transforms.SceneGraph "trimesh.scene.transforms.SceneGraph") | None = None_, _camera : [Camera](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera "trimesh.scene.cameras.Camera") | None = None_, _lights : [Sequence](trimesh.typed.html#trimesh.typed.Sequence "collections.abc.Sequence")[[Light](trimesh.scene.lighting.html#trimesh.scene.lighting.Light "trimesh.scene.lighting.Light")] | None = None_, _camera_transform : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[_ScalarT]] | None = None_)¶
    

Create a new Scene object.

Parameters:
    

  * **geometry** (_Trimesh_ _,_[_Path2D_](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D") _,__Path3D PointCloud_ _or_ _list_) – Geometry to initially add to the scene

  * **base_frame** – Name of base frame

  * **metadata** – Any metadata about the scene

  * **graph** – A passed transform graph to use

  * **camera** ([_Camera_](trimesh.scene.html#trimesh.scene.Camera "trimesh.scene.Camera") _or_ _None_) – A passed camera to use

  * **lights** (_[_[_trimesh.scene.lighting.Light_](trimesh.scene.lighting.html#trimesh.scene.lighting.Light "trimesh.scene.lighting.Light") _] or_ _None_) – A passed lights to use

  * **camera_transform** – Homogeneous (4, 4) camera transform in the base frame

add_geometry(_geometry : [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry") | [Iterable](trimesh.typed.html#trimesh.typed.Iterable "collections.abc.Iterable")[[Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")] | dict[str, [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")] | ArrayLike_, _node_name : str | None = None_, _geom_name : str | None = None_, _parent_node_name : str | None = None_, _transform : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[_ScalarT]] | None = None_, _metadata : dict | None = None_)¶
    

Add a geometry to the scene.

If the mesh has multiple transforms defined in its metadata, they will all be copied into the TransformForest of the current scene automatically.

Parameters:
    

  * **geometry** (_Trimesh_ _,_[_Path2D_](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D") _,__Path3D PointCloud_ _or_ _list_) – Geometry to initially add to the scene

  * **node_name** (_None_ _or_ _str_) – Name of the added node.

  * **geom_name** (_None_ _or_ _str_) – Name of the added geometry.

  * **parent_node_name** (_None_ _or_ _str_) – Name of the parent node in the graph.

  * **transform** (_None_ _or_ _(__4_ _,__4_ _)__float_) – Transform that applies to the added node.

  * **metadata** (_None_ _or_ _dict_) – Optional metadata for the node.

Returns:
    

**node_name** – Name of single node in self.graph (passed in) or None if node was not added (eg. geometry was null or a Scene).

Return type:
    

str

apply_transform(_transform_)¶
    

Apply a transform to all children of the base frame without modifying any geometry.

Parameters:
    

**transform** (_(__4_ _,__4_ _)_) – Homogeneous transformation matrix.

_property _area _: float_¶
    

What is the summed area of every geometry which has area.

Returns:
    

**area** – Summed area of every instanced geometry

Return type:
    

float

_property _bounds _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_¶
    

Return the overall bounding box of the scene.

Returns:
    

**bounds** – Position of [min, max] bounding box Returns None if no valid bounds exist

Return type:
    

(2, 3) float or None

_property _bounds_corners _: dict[str, ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]]_¶
    

Get the post-transform AABB for each node which has geometry defined.

Returns:
    

Bounds for each node with vertices:
    

{node_name : (2, 3) float}

Return type:
    

corners

_property _camera _: [Camera](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera "trimesh.scene.cameras.Camera")_¶
    

Get the single camera for the scene. If not manually set one will abe automatically generated.

Returns:
    

**camera** – Camera object defined for the scene

Return type:
    

[trimesh.scene.Camera](trimesh.scene.html#trimesh.scene.Camera "trimesh.scene.Camera")

camera_rays() → tuple[ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]], ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]], ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]]¶
    

Calculate the trimesh.scene.Camera origin and ray direction vectors. Returns one ray per pixel as set in camera.resolution

Returns:
    

  * **origin** (_(n, 3) float_) – Ray origins in space

  * **vectors** (_(n, 3) float_) – Ray direction unit vectors in world coordinates

  * **pixels** (_(n, 2) int_) – Which pixel does each ray correspond to in an image

_property _camera_transform¶
    

Get camera transform in the base frame.

Returns:
    

**camera_transform** – Camera transform in the base frame

Return type:
    

(4, 4) float

_property _center_mass _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[_ScalarT]]_¶
    

Find the center of mass for every instance in the scene.

Returns:
    

**center_mass** – The center of mass of the scene

Return type:
    

(3,) float

_property _centroid _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_¶
    

Return the center of the bounding box for the scene.

Returns:
    

**centroid** – Point for center of bounding box

Return type:
    

  3. float

convert_units(_desired : str_, _guess : bool = False_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

If geometry has units defined convert them to new units.

Returns a new scene with geometries and transforms scaled.

Parameters:
    

  * **desired** (_str_) – Desired final unit system: ‘inches’, ‘mm’, etc.

  * **guess** (_bool_) – Is the converter allowed to guess scale when models don’t have it specified in their metadata.

Returns:
    

**scaled** – Copy of scene with scaling applied and units set for every model

Return type:
    

trimesh.Scene

_property _convex_hull¶
    

The convex hull of the whole scene.

Returns:
    

**hull** – Trimesh object which is a convex hull of all meshes in scene

Return type:
    

trimesh.Trimesh

copy() → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Return a deep copy of the current scene

Returns:
    

**copied** – Copy of the current scene

Return type:
    

trimesh.Scene

delete_geometry(_names : set | str | [Sequence](trimesh.typed.html#trimesh.typed.Sequence "collections.abc.Sequence")_) → None¶
    

Delete one more multiple geometries from the scene and also remove any node in the transform graph which references it.

Parameters:
    

**name** (_hashable_) – Name that references self.geometry

dump(_concatenate : bool = False_) → list[[Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")]¶
    

Get a list of every geometry moved to its instance position, i.e. freezing or “baking” transforms.

Parameters:
    

**concatenate** – 

KWARG IS DEPRECATED FOR REMOVAL APRIL 2025 Concatenate results into single geometry. This keyword argument will make the type hint incorrect and you should replace Scene.dump(concatenate=True) with:

>   * Scene.to_geometry() for a Trimesh, Path2D or Path3D
> 
>   * Scene.to_mesh() for only Trimesh components.
> 
> 

Returns:
    

Copies of Scene.geometry transformed to their instance position.

Return type:
    

dumped

_property _duplicate_nodes _: list[list[str]]_¶
    

Return a sequence of node keys of identical meshes.

Will include meshes with different geometry but identical spatial hashes as well as meshes repeated by self.nodes.

Returns:
    

Keys of self.graph that represent identical geometry

Return type:
    

duplicates

explode(_vector =None_, _origin =None_) → None¶
    

Explode the current scene in-place around a point and vector.

Parameters:
    

  * **vector** (_(__3_ _,__)__float_ _or_ _float_) – Explode radially around a direction vector or spherically

  * **origin** (_(__3_ _,__)__float_) – Point to explode around

export(_file_obj =None_, _file_type =None_, _** kwargs_)¶
    

Export a snapshot of the current scene.

Parameters:
    

  * **file_obj** (_str_ _,__file-like_ _, or_ _None_) – File object to export to

  * **file_type** (_str_ _or_ _None_) – What encoding to use for meshes IE: dict, dict64, stl

Returns:
    

**export** – Only returned if file_obj is None

Return type:
    

bytes

_property _extents _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_¶
    

Return the axis aligned box size of the current scene or None if the scene is empty.

Returns:
    

Bounding box sides length or None for empty scene.

Return type:
    

extents

_property _geometry_identifiers _: dict[str, str]_¶
    

Look up geometries by identifier hash.

Returns:
    

{Identifier hash: key in self.geometry}

Return type:
    

identifiers

_property _has_camera _: bool_¶
    

_property _identifier_hash _: str_¶
    

Get a unique identifier for the scene.

_property _is_empty _: bool_¶
    

Does the scene have anything in it.

Returns:
    

True if nothing is in the scene

Return type:
    

is_empty

_property _is_valid _: bool_¶
    

Is every geometry connected to the root node.

Returns:
    

**is_valid** – Does every geometry have a transform

Return type:
    

bool

_property _lights _: list[[Light](trimesh.scene.lighting.html#trimesh.scene.lighting.Light "trimesh.scene.lighting.Light")]_¶
    

Get a list of the lights in the scene. If nothing is set it will generate some automatically.

Returns:
    

**lights** – Lights in the scene.

Return type:
    

[[trimesh.scene.lighting.Light](trimesh.scene.lighting.html#trimesh.scene.lighting.Light "trimesh.scene.lighting.Light")]

_property _moment_inertia¶
    

Return the moment of inertia of the current scene with respect to the center of mass of the current scene.

Returns:
    

**inertia** – Inertia with respect to cartesian axis at scene.center_mass

Return type:
    

(3, 3) float

moment_inertia_frame(_transform_)¶
    

Return the moment of inertia of the current scene relative to a transform from the base frame.

Parameters transform : (4, 4) float

> Homogeneous transformation matrix.

Returns:
    

**inertia** – Inertia tensor at requested frame.

Return type:
    

(3, 3) float

reconstruct_instances(_cost_threshold : float | floating = 1e-05_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

If a scene has been “baked” with meshes it means that the duplicate nodes have _corresponding vertices_ but are rigidly transformed to different places.

This means the problem of finding ab instance transform can use the procrustes analysis which is _very_ fast relative to more complicated registration problems that require ICP and nearest-point-on-surface calculations.

TODO : construct a parent non-geometry node for containing every group.

Parameters:
    

  * **scene**

  * **handle.** (_The scene to_)

  * **cost_threshold**

  * **mean** (_The maximum value for procrustes cost which is "squared_)

  * **value** (_vertex distance between pair ". If the fit is above this_)

  * **duplicate.** (_the instance will be left even if it is a_)

Returns:
    

  * _dedupe_

  * _A copy of the scene de-duplicated as much as possible._

rezero() → None¶
    

Move the current scene so that the AABB of the whole scene is centered at the origin.

Does this by changing the base frame to a new, offset base frame.

save_image(_resolution =None_, _** kwargs_) → bytes¶
    

Get a PNG image of a scene.

Parameters:
    

  * **resolution** (_(__2_ _,__)__int_) – Resolution to render image

  * ****kwargs** – Passed to SceneViewer constructor

Returns:
    

**png** – Render of scene as a PNG

Return type:
    

bytes

_property _scale _: float_¶
    

The approximate scale of the mesh

Returns:
    

**scale** – The mean of the bounding box edge lengths

Return type:
    

float

scaled(_scale : float | floating | ArrayLike_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Return a copy of the current scene, with meshes and scene transforms scaled to the requested factor.

Parameters:
    

**scale** (_float_ _or_ _(__3_ _,__)__float_) – Factor to scale meshes and transforms

Returns:
    

**scaled** – A copy of the current scene but scaled

Return type:
    

trimesh.Scene

set_camera(_angles =None_, _distance =None_, _center =None_, _resolution =None_, _fov =None_) → [Camera](trimesh.scene.cameras.html#trimesh.scene.cameras.Camera "trimesh.scene.cameras.Camera")¶
    

Create a camera object for self.camera, and add a transform to self.graph for it.

If arguments are not passed sane defaults will be figured out which show the mesh roughly centered.

Parameters:
    

  * **angles** (_(__3_ _,__)__float_) – Initial euler angles in radians

  * **distance** (_float_) – Distance from centroid

  * **center** (_(__3_ _,__)__float_) – Point camera should be center on

  * **camera** (_Camera object_) – Object that stores camera parameters

show(_viewer : None | [Callable](trimesh.typed.html#trimesh.typed.Callable "collections.abc.Callable") | Literal['gl', 'jupyter', 'marimo'] = None_, _** kwargs_)¶
    

Display the current scene.

Parameters:
    

  * **viewer** – What kind of viewer to use, such as gl to open a pyglet window jupyter for a jupyter notebook marimo’ for a marimo notebook None for a “best guess”

  * **kwargs** – Passed to viewer, such as smooth=False which will turn off automatic smooth shading

simplify_quadric_decimation(_percent : float | floating | None = None_, _face_count : int | integer | unsignedinteger | None = None_, _aggression : int | integer | unsignedinteger | None = None_) → None¶
    

Apply in-place mesh.simplify_quadric_decimation to any meshes in the scene.

Parameters:
    

  * **percent** – A number between 0.0 and 1.0 for how much

  * **face_count** – Target number of faces desired in the resulting mesh.

  * **aggression** – An integer between 0 and 10, the scale being roughly 0 is “slow and good” and 10 being “fast and bad.”

strip_visuals() → None¶
    

Strip visuals from every Trimesh geometry and set them to an empty ColorVisuals.

subscene(_node : str_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Get part of a scene that succeeds a specified node.

Parameters:
    

**node** – Hashable key in scene.graph

Returns:
    

Partial scene generated from current.

Return type:
    

subscene

to_geometry() → [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")¶
    

Concatenate geometry in the scene into a single like-typed geometry, applying the transforms and “baking” the result. May drop geometry if the scene has mixed geometry.

Returns:
    

Either a Trimesh, Path2D, or Path3D depending on what is in the scene.

Return type:
    

concat

to_mesh() → trimesh.Trimesh¶
    

Concatenate every mesh instances in the scene into a single mesh, applying transforms and “baking” the result. Will drop any geometry in the scene that is not a Trimesh object.

Returns:
    

All meshes in the scene concatenated into one.

Return type:
    

mesh

_property _triangles _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return a correctly transformed polygon soup of the current scene.

Returns:
    

**triangles** – Triangles in space

Return type:
    

(n, 3, 3) float

_property _triangles_node¶
    

Which node of self.graph does each triangle come from.

Returns:
    

**triangles_index** – Node name for each triangle

Return type:
    

(len(self.triangles),)

_property _units _: str | None_¶
    

Get the units for every model in the scene. If the scene has mixed units or no units this will return None.

Returns:
    

Units for every model in the scene or None if there are no units or mixed units

Return type:
    

units

_property _volume _: [float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")_¶
    

What is the summed volume of every geometry which has volume

Returns:
    

**volume** – Summed area of every instanced geometry

Return type:
    

float

_class _trimesh.Trimesh(_vertices : ArrayLike | None = None_, _faces : ArrayLike | None = None_, _face_normals : ArrayLike | None = None_, _vertex_normals : ArrayLike | None = None_, _face_colors : ArrayLike | None = None_, _vertex_colors : ArrayLike | None = None_, _face_attributes : dict[str, ArrayLike] | None = None_, _vertex_attributes : dict[str, ArrayLike] | None = None_, _metadata : dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")] | None = None_, _process : bool = True_, _validate : bool = False_, _merge_tex : bool | None = None_, _merge_norm : bool | None = None_, _use_embree : bool = True_, _initial_cache : dict[str, ndarray] | None = None_, _visual : [ColorVisuals](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals "trimesh.visual.color.ColorVisuals") | [TextureVisuals](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals "trimesh.visual.texture.TextureVisuals") | None = None_, _** kwargs_)¶
    

Bases: [`Geometry3D`](trimesh.parent.html#trimesh.parent.Geometry3D "trimesh.parent.Geometry3D")

__init__(_vertices : ArrayLike | None = None_, _faces : ArrayLike | None = None_, _face_normals : ArrayLike | None = None_, _vertex_normals : ArrayLike | None = None_, _face_colors : ArrayLike | None = None_, _vertex_colors : ArrayLike | None = None_, _face_attributes : dict[str, ArrayLike] | None = None_, _vertex_attributes : dict[str, ArrayLike] | None = None_, _metadata : dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")] | None = None_, _process : bool = True_, _validate : bool = False_, _merge_tex : bool | None = None_, _merge_norm : bool | None = None_, _use_embree : bool = True_, _initial_cache : dict[str, ndarray] | None = None_, _visual : [ColorVisuals](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals "trimesh.visual.color.ColorVisuals") | [TextureVisuals](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals "trimesh.visual.texture.TextureVisuals") | None = None_, _** kwargs_) → None¶
    

A Trimesh object contains a triangular 3D mesh.

Parameters:
    

  * **vertices** (_(__n_ _,__3_ _)__float_) – Array of vertex locations

  * **faces** (_(__m_ _,__3_ _) or_ _(__m_ _,__4_ _)__int_) – Array of triangular or quad faces (triangulated on load)

  * **face_normals** (_(__m_ _,__3_ _)__float_) – Array of normal vectors corresponding to faces

  * **vertex_normals** (_(__n_ _,__3_ _)__float_) – Array of normal vectors for vertices

  * **face_colors** (_(__n_ _,__3_ _|__4_ _)__uint8_) – Array of colors for faces

  * **vertex_colors** (_(__n_ _,__3_ _|__4_ _)__uint8_) – Array of colors for vertices

  * **face_attributes** (_dict_) – Attributes corresponding to faces

  * **vertex_attributes** (_dict_) – Attributes corresponding to vertices

  * **metadata** (_dict_) – Any metadata about the mesh

  * **process** (_bool_) – if True, Nan and Inf values will be removed immediately and vertices will be merged

  * **validate** (_bool_) – If True, degenerate and duplicate faces will be removed immediately, and some functions will alter the mesh to ensure consistent results.

  * **merge_tex** (_bool_) – If True textured meshes with UV coordinates will have vertices merged regardless of UV coordinates

  * **merge_norm** (_bool_) – If True, meshes with vertex normals will have vertices merged ignoring different normals

  * **use_embree** (_bool_) – If True try to use pyembree raytracer. If pyembree is not available it will automatically fall back to a much slower rtree/numpy implementation

  * **initial_cache** (_dict_) – A way to pass things to the cache in case expensive things were calculated before creating the mesh object.

  * **visual** ([_ColorVisuals_](trimesh.visual.html#trimesh.visual.ColorVisuals "trimesh.visual.ColorVisuals") _or_[ _TextureVisuals_](trimesh.visual.html#trimesh.visual.TextureVisuals "trimesh.visual.TextureVisuals")) – Assigned to self.visual

apply_transform(_matrix : ArrayLike_) → Self¶
    

Transform mesh by a homogeneous transformation matrix.

Does the bookkeeping to avoid recomputing things so this function should be used rather than directly modifying self.vertices if possible.

Parameters:
    

**matrix** (_(__4_ _,__4_ _)__float_) – Homogeneous transformation matrix

_property _area _: [float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")_¶
    

Summed area of all triangles in the current mesh.

Returns:
    

**area** – Surface area of mesh

Return type:
    

float

_property _area_faces _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The area of each face in the mesh.

Returns:
    

**area_faces** – Area of each face

Return type:
    

(n, ) float

_property _body_count _: int_¶
    

How many connected groups of vertices exist in this mesh. Note that this number may differ from result in mesh.split, which is calculated from FACE rather than vertex adjacency.

Returns:
    

**count** – Number of connected vertex groups

Return type:
    

int

_property _bounds _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_¶
    

The axis aligned bounds of the faces of the mesh.

Returns:
    

**bounds** – Bounding box with [min, max] coordinates If mesh is empty will return None

Return type:
    

(2, 3) float or None

_property _center_mass _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The point in space which is the center of mass/volume.

Returns:
    

**center_mass** – Volumetric center of mass of the mesh.

Return type:
    

(3, ) float

_property _centroid _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The point in space which is the average of the triangle centroids weighted by the area of each triangle.

This will be valid even for non-watertight meshes, unlike self.center_mass

Returns:
    

**centroid** – The average vertex weighted by face area

Return type:
    

(3, ) float

compute_stable_poses(_center_mass : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None = None_, _sigma : float | floating = 0.0_, _n_samples : int | integer | unsignedinteger = 1_, _threshold : float | floating = 0.0_) → tuple[ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]], ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]]¶
    

Computes stable orientations of a mesh and their quasi-static probabilities.

This method samples the location of the center of mass from a multivariate gaussian (mean at com, cov equal to identity times sigma) over n_samples. For each sample, it computes the stable resting poses of the mesh on a a planar workspace and evaluates the probabilities of landing in each pose if the object is dropped onto the table randomly.

This method returns the 4x4 homogeneous transform matrices that place the shape against the planar surface with the z-axis pointing upwards and a list of the probabilities for each pose. The transforms and probabilities that are returned are sorted, with the most probable pose first.

Parameters:
    

  * **center_mass** (_(__3_ _,__)__float_) – The object center of mass (if None, this method assumes uniform density and watertightness and computes a center of mass explicitly)

  * **sigma** (_float_) – The covariance for the multivariate gaussian used to sample center of mass locations

  * **n_samples** (_int_) – The number of samples of the center of mass location

  * **threshold** (_float_) – The probability value at which to threshold returned stable poses

Returns:
    

  * **transforms** (_(n, 4, 4) float_) – The homogeneous matrices that transform the object to rest in a stable pose, with the new z-axis pointing upwards from the table and the object just touching the table.

  * **probs** (_(n, ) float_) – A probability ranging from 0.0 to 1.0 for each pose

contains(_points : ArrayLike_) → ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[bool]]¶
    

Given an array of points determine whether or not they are inside the mesh. This raises an error if called on a non-watertight mesh.

Parameters:
    

**points** (_(__n_ _,__3_ _)__float_) – Points in cartesian space

Returns:
    

**contains** – Whether or not each point is inside the mesh

Return type:
    

(n, ) bool

convert_units(_desired : str_, _guess : bool = False_) → Self¶
    

Convert the units of the mesh into a specified unit.

Parameters:
    

  * **desired** (_string_) – Units to convert to (eg ‘inches’)

  * **guess** (_boolean_) – If self.units are not defined should we guess the current units of the document and then convert?

Returns:
    

**self** – Current mesh

Return type:
    

trimesh.Trimesh

convex_decomposition(_** kwargs_) → list[[Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")]¶
    

Compute an approximate convex decomposition of a mesh using pip install pyVHACD.

Returns:
    

  * _meshes_ – List of convex meshes that approximate the original

  * ****kwargs** (_VHACD keyword arguments_)

_property _convex_hull _: [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")_¶
    

Returns a Trimesh object representing the convex hull of the current mesh.

Returns:
    

**convex** – Mesh of convex hull of current mesh

Return type:
    

trimesh.Trimesh

copy(_include_cache : bool = False_, _include_visual : bool = True_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Safely return a copy of the current mesh.

By default, copied meshes will have emptied cache to avoid memory issues and so may be slow on initial operations until caches are regenerated.

Current object will _never_ have its cache cleared.

Parameters:
    

  * **include_cache** (_bool_) – If True, will shallow copy cached data to new mesh

  * **include_visual** (_bool_) – If True, will copy visual information

Returns:
    

**copied** – Copy of current mesh

Return type:
    

trimesh.Trimesh

_property _density _: float_¶
    

The density of the mesh used in inertia calculations.

Returns:
    

The density of the primitive.

Return type:
    

density

difference(_other : [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh") | [Sequence](trimesh.typed.html#trimesh.typed.Sequence "collections.abc.Sequence")[[Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")]_, _engine : Literal['manifold', 'blender', None] = None_, _check_volume : bool = True_, _** kwargs_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Boolean difference between this mesh and other meshes.

Parameters:
    

  * **other** – One or more meshes to difference with the current mesh.

  * **engine** – Which backend to use, the default recommendation is: pip install manifold3d.

  * **check_volume** – Raise an error if not all meshes are watertight positive volumes. Advanced users may want to ignore this check as it is expensive.

  * **kwargs** – Passed through to the engine.

Returns:
    

**difference** – Difference between self and other Trimesh objects

Return type:
    

trimesh.Trimesh

_property _edges _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Edges of the mesh (derived from faces).

Returns:
    

**edges** – List of vertex indices making up edges

Return type:
    

(n, 2) int

_property _edges_face _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Which face does each edge belong to.

Returns:
    

**edges_face** – Index of self.faces

Return type:
    

(n, ) int

_property _edges_sorted _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Edges sorted along axis 1

Returns:
    

**edges_sorted** – Same as self.edges but sorted along axis 1

Return type:
    

(n, 2)

_property _edges_sorted_tree _: cKDTree_¶
    

A KDTree for mapping edges back to edge index.

Returns:
    

**tree** – Tree when queried with edges will return their index in mesh.edges_sorted

Return type:
    

scipy.spatial.cKDTree

_property _edges_sparse _: coo_matrix_¶
    

Edges in sparse bool COO graph format where connected vertices are True.

Returns:
    

**sparse** – Sparse graph in COO format

Return type:
    

(len(self.vertices), len(self.vertices)) bool

_property _edges_unique _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

The unique edges of the mesh.

Returns:
    

**edges_unique** – Vertex indices for unique edges

Return type:
    

(n, 2) int

_property _edges_unique_inverse _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Return the inverse required to reproduce self.edges_sorted from self.edges_unique.

Useful for referencing edge properties: mesh.edges_unique[mesh.edges_unique_inverse] == m.edges_sorted

Returns:
    

**inverse** – Indexes of self.edges_unique

Return type:
    

(len(self.edges), ) int

_property _edges_unique_length _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

How long is each unique edge.

Returns:
    

**length** – Length of each unique edge

Return type:
    

(len(self.edges_unique), ) float

_property _euler_number _: int_¶
    

Return the Euler characteristic (a topological invariant) for the mesh In order to guarantee correctness, this should be called after remove_unreferenced_vertices

Returns:
    

**euler_number** – Topological invariant

Return type:
    

int

eval_cached(_statement : str_, _* args_) → [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")¶
    

Evaluate a statement and cache the result before returning.

Statements are evaluated inside the Trimesh object, and

Parameters:
    

  * **statement** (_str_) – Statement of valid python code

  * ***args** (_list_) – Available inside statement as args[0], etc

Returns:
    

**result**

Return type:
    

result of running eval on statement with args

Examples

r = mesh.eval_cached(‘np.dot(self.vertices, args[0])’, [0, 0, 1])

export(_file_obj : str | Path | [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom | dict | None = None_, _file_type : str | None = None_, _** kwargs_) → dict | bytes | str¶
    

Export the current mesh to a file object. If file_obj is a filename, file will be written there.

Supported formats are stl, off, ply, collada, json, dict, glb, dict64, msgpack.

Parameters:
    

  * **file_obj** (_open writeable file object_) – str, file name where to save the mesh None, return the export blob

  * **file_type** (_str_) – Which file type to export as, if file_name is passed this is not required.

Returns:
    

**exported** – Result of exporter

Return type:
    

bytes or str

_property _extents _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_¶
    

The length, width, and height of the axis aligned bounding box of the mesh.

Returns:
    

**extents** – Array containing axis aligned [length, width, height] If mesh is empty returns None

Return type:
    

(3, ) float or None

_property _face_adjacency _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Find faces that share an edge i.e. ‘adjacent’ faces.

Returns:
    

**adjacency** – Pairs of faces which share an edge

Return type:
    

(n, 2) int

Examples

In [1]: mesh = trimesh.load(‘models/featuretype.STL’)

In [2]: mesh.face_adjacency Out[2]: array([[ 0, 1],

> [ 2, 3], [ 0, 3], …, [1112, 949], [3467, 3475], [1113, 3475]])

In [3]: mesh.faces[mesh.face_adjacency[0]] Out[3]: TrackedArray([[ 1, 0, 408],

> [1239, 0, 1]], dtype=int64)

In [4]: import networkx as nx

In [5]: graph = nx.from_edgelist(mesh.face_adjacency)

In [6]: groups = nx.connected_components(graph)

_property _face_adjacency_angles _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return the unsigned angle between adjacent faces in radians.

Note that if you want a signed angle you can easily use the face_adjacency_convex attribute to get a signed angle with advanced indexing:

``` # get a sign per face_adacency pair from the “is it convex” boolean signs = np.array([-1.0, 1.0])[mesh.face_adjacency_convex.astype(np.int64)]

# apply the signs to the angles angles = mesh.face_adjacency_angles * signs ```

Returns:
    

**adjacency_angle** – Unsigned angle between adjacent faces corresponding with self.face_adjacency

Return type:
    

(len(self.face_adjacency), ) float

_property _face_adjacency_convex _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[bool]]_¶
    

Return faces which are adjacent and locally convex.

What this means is that given faces A and B, the one vertex in B that is not shared with A, projected onto the plane of A has a projection that is zero or negative.

Returns:
    

**are_convex** – Face pairs that are locally convex

Return type:
    

(len(self.face_adjacency), ) bool

_property _face_adjacency_edges _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Returns the edges that are shared by the adjacent faces.

Returns:
    

**edges** – Vertex indices which correspond to face_adjacency

Return type:
    

(n, 2) int

_property _face_adjacency_edges_tree _: cKDTree_¶
    

A KDTree for mapping edges back face adjacency index.

Returns:
    

**tree** – Tree when queried with SORTED edges will return their index in mesh.face_adjacency

Return type:
    

scipy.spatial.cKDTree

_property _face_adjacency_projections _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The projection of the non-shared vertex of a triangle onto its adjacent face

Returns:
    

**projections** – Dot product of vertex onto plane of adjacent triangle.

Return type:
    

(len(self.face_adjacency), ) float

_property _face_adjacency_radius _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The approximate radius of a cylinder that fits inside adjacent faces.

Returns:
    

**radii** – Approximate radius formed by triangle pair

Return type:
    

(len(self.face_adjacency), ) float

_property _face_adjacency_span _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The approximate perpendicular projection of the non-shared vertices in a pair of adjacent faces onto the shared edge of the two faces.

Returns:
    

**span** – Approximate span between the non-shared vertices

Return type:
    

(len(self.face_adjacency), ) float

_property _face_adjacency_tree _: Index_¶
    

An R-tree of face adjacencies.

Returns:
    

Where each edge in self.face_adjacency has a rectangular cell

Return type:
    

tree

_property _face_adjacency_unshared _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Return the vertex index of the two vertices not in the shared edge between two adjacent faces

Returns:
    

**vid_unshared** – Indexes of mesh.vertices

Return type:
    

(len(mesh.face_adjacency), 2) int

_property _face_angles _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Returns the angle at each vertex of a face.

Returns:
    

**angles** – Angle at each vertex of a face

Return type:
    

(len(self.faces), 3) float

_property _face_angles_sparse _: coo_matrix_¶
    

A sparse matrix representation of the face angles.

Returns:
    

**sparse** – Float sparse matrix with with shape: (len(self.vertices), len(self.faces))

Return type:
    

scipy.sparse.coo_matrix

_property _face_neighborhood _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Find faces that share a vertex i.e. ‘neighbors’ faces.

Returns:
    

**neighborhood** – Pairs of faces which share a vertex

Return type:
    

(n, 2) int

_property _face_normals _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return the unit normal vector for each face.

If a face is degenerate and a normal can’t be generated a zero magnitude unit vector will be returned for that face.

Returns:
    

**normals** – Normal vectors of each face

Return type:
    

(len(self.faces), 3) [float64](trimesh.typed.html#trimesh.typed.float64 "trimesh.typed.float64")

_property _faces _: [TrackedArray](trimesh.caching.html#trimesh.caching.TrackedArray "trimesh.caching.TrackedArray")_¶
    

The faces of the mesh.

This is regarded as core information which cannot be regenerated from cache and as such is stored in self._data which tracks the array for changes and clears cached values of the mesh altered.

Returns:
    

**faces** – References for self.vertices for triangles.

Return type:
    

(n, 3) [int64](trimesh.typed.html#trimesh.typed.int64 "trimesh.typed.int64")

_property _faces_sparse _: coo_matrix_¶
    

A sparse matrix representation of the faces.

Returns:
    

**sparse** – Has properties: dtype : bool shape : (len(self.vertices), len(self.faces))

Return type:
    

scipy.sparse.coo_matrix

_property _faces_unique_edges _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

For each face return which indexes in mesh.unique_edges constructs that face.

Returns:
    

**faces_unique_edges** – Indexes of self.edges_unique that construct self.faces

Return type:
    

(len(self.faces), 3) int

Examples

In [0]: mesh.faces[:2] Out[0]: TrackedArray([[ 1, 6946, 24224],

> [ 6946, 1727, 24225]])

In [1]: mesh.edges_unique[mesh.faces_unique_edges[:2]] Out[1]: array([[[ 1, 6946],

> > [ 6946, 24224], [ 1, 24224]],
> 
> [[ 1727, 6946],
>     
> 
> [ 1727, 24225], [ 6946, 24225]]])

_property _facets _: list[ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]]_¶
    

Return a list of face indices for coplanar adjacent faces.

Returns:
    

**facets** – Groups of indexes of self.faces

Return type:
    

(n, ) sequence of (m, ) int

_property _facets_area _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return an array containing the area of each facet.

Returns:
    

**area** – Total area of each facet (group of faces)

Return type:
    

(len(self.facets), ) float

_property _facets_boundary _: list[ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]]_¶
    

Return the edges which represent the boundary of each facet

Returns:
    

**edges_boundary** – Indices of self.vertices

Return type:
    

sequence of (n, 2) int

_property _facets_normal _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return the normal of each facet

Returns:
    

**normals** – A unit normal vector for each facet

Return type:
    

(len(self.facets), 3) float

_property _facets_on_hull _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[bool]]_¶
    

Find which facets of the mesh are on the convex hull.

Returns:
    

**on_hull** – is A facet on the meshes convex hull or not

Return type:
    

(len(mesh.facets), ) bool

_property _facets_origin _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return a point on the facet plane.

Returns:
    

**origins** – A point on each facet plane

Return type:
    

(len(self.facets), 3) float

fill_holes() → bool¶
    

Fill single triangle and single quad holes in the current mesh.

Returns:
    

**watertight** – Is the mesh watertight after the function completes

Return type:
    

bool

fix_normals(_multibody : bool | None = None_) → Self¶
    

Find and fix problems with self.face_normals and self.faces winding direction.

For face normals ensure that vectors are consistently pointed outwards, and that self.faces is wound in the correct direction for all connected components.

Parameters:
    

**multibody** (_None_ _or_ _bool_) – Fix normals across multiple bodies or if unspecified check the current Trimesh.body_count.

_property _identifier _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return a float vector which is unique to the mesh and is robust to rotation and translation.

Returns:
    

**identifier** – Identifying properties of the current mesh

Return type:
    

(7,) float

_property _identifier_hash _: str_¶
    

A hash of the rotation invariant identifier vector.

Returns:
    

**hashed** – Hex string of the SHA256 hash from the identifier vector at hand-tuned sigfigs.

Return type:
    

str

_property _integral_mean_curvature _: [float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")_¶
    

The integral mean curvature, or the surface integral of the mean curvature.

Returns:
    

**area** – Integral mean curvature of mesh

Return type:
    

float

intersection(_other : [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh") | [Sequence](trimesh.typed.html#trimesh.typed.Sequence "collections.abc.Sequence")[[Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")]_, _engine : Literal['manifold', 'blender', None] = None_, _check_volume : bool = True_, _** kwargs_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Boolean intersection between this mesh and other meshes.

Parameters:
    

  * **other** (_trimesh.Trimesh_ _, or_ _list_ _of_ _trimesh.Trimesh objects_) – Meshes to calculate intersections with

  * **engine** – Which backend to use, the default recommendation is: pip install manifold3d.

  * **check_volume** – Raise an error if not all meshes are watertight positive volumes. Advanced users may want to ignore this check as it is expensive.

  * **kwargs** – Passed through to the engine.

Returns:
    

**intersection** – Mesh of the volume contained by all passed meshes

Return type:
    

trimesh.Trimesh

invert() → Self¶
    

Invert the mesh in-place by reversing the winding of every face and negating normals without dumping the cache.

Alters self.faces by reversing columns, and negating self.face_normals and self.vertex_normals.

_property _is_convex _: bool_¶
    

Check if a mesh is convex or not.

Returns:
    

**is_convex** – Is mesh convex or not

Return type:
    

bool

_property _is_empty _: bool_¶
    

Does the current mesh have data defined.

Returns:
    

**empty** – If True, no data is set on the current mesh

Return type:
    

bool

_property _is_volume _: bool_¶
    

Check if a mesh has all the properties required to represent a valid volume, rather than just a surface.

These properties include being watertight, having consistent winding and outward facing normals.

Returns:
    

Does the mesh represent a volume

Return type:
    

valid

_property _is_watertight _: bool_¶
    

Check if a mesh is watertight by making sure every edge is included in two faces.

Returns:
    

**is_watertight** – Is mesh watertight or not

Return type:
    

bool

_property _is_winding_consistent _: bool_¶
    

Does the mesh have consistent winding or not. A mesh with consistent winding has each shared edge going in an opposite direction from the other in the pair.

Returns:
    

**consistent** – Is winding is consistent or not

Return type:
    

bool

_property _kdtree _: cKDTree_¶
    

Return a scipy.spatial.cKDTree of the vertices of the mesh. Not cached as this lead to observed memory issues and segfaults.

Returns:
    

**tree** – Contains mesh.vertices

Return type:
    

scipy.spatial.cKDTree

_property _mass _: [float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")_¶
    

Mass of the current mesh, based on specified density and volume. If the current mesh isn’t watertight this is garbage.

Returns:
    

**mass** – Mass of the current mesh

Return type:
    

float

_property _mass_properties _: [MassProperties](trimesh.triangles.html#trimesh.triangles.MassProperties "trimesh.triangles.MassProperties")_¶
    

Returns the mass properties of the current mesh.

Assumes uniform density, and result is probably garbage if mesh isn’t watertight.

Returns:
    

**properties** – With keys: ‘volume’ : in global units^3 ‘mass’ : From specified density ‘density’ : Included again for convenience (same as kwarg density) ‘inertia’ : Taken at the center of mass and aligned with global

> coordinate system

’center_mass’ : Center of mass location, in global coordinate system

Return type:
    

dict

merge_vertices(_merge_tex : bool | None = None_, _merge_norm : bool | None = None_, _digits_vertex : int | integer | unsignedinteger | None = None_, _digits_norm : int | integer | unsignedinteger | None = None_, _digits_uv : int | integer | unsignedinteger | None = None_) → None¶
    

Removes duplicate vertices grouped by position and optionally texture coordinate and normal.

Parameters:
    

  * **merge_tex** (_bool_) – If True textured meshes with UV coordinates will have vertices merged regardless of UV coordinates

  * **merge_norm** (_bool_) – If True, meshes with vertex normals will have vertices merged ignoring different normals

  * **digits_vertex** (_None_ _or_ _int_) – Number of digits to consider for vertex position

  * **digits_norm** (_int_) – Number of digits to consider for unit normals

  * **digits_uv** (_int_) – Number of digits to consider for UV coordinates

_property _moment_inertia _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return the moment of inertia matrix of the current mesh. If mesh isn’t watertight this is garbage. The returned moment of inertia is _axis aligned_ at the mesh’s center of mass mesh.center_mass. If you want the moment at any other frame including the origin call: mesh.moment_inertia_frame

Returns:
    

**inertia** – Moment of inertia of the current mesh at the center of mass and aligned with the cartesian axis.

Return type:
    

(3, 3) float

moment_inertia_frame(_transform : ArrayLike_) → ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]¶
    

Get the moment of inertia of this mesh with respect to an arbitrary frame, versus with respect to the center of mass as returned by mesh.moment_inertia.

For example if transform is an identity matrix np.eye(4) this will give the moment at the origin.

Uses the parallel axis theorum to move the center mass tensor to this arbitrary frame.

Parameters:
    

**transform** (_(__4_ _,__4_ _)__float_) – Homogeneous transformation matrix.

Returns:
    

**inertia** – Moment of inertia in the requested frame.

Return type:
    

(3, 3)

_property _mutable _: bool_¶
    

Is the current mesh allowed to be altered in-place?

Returns:
    

If data is allowed to be set for the mesh.

Return type:
    

mutable

nondegenerate_faces(_height : float | floating = 1e-08_) → ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[bool]]¶
    

Identify degenerate faces (faces without 3 unique vertex indices) in the current mesh.

Usage example for removing them: mesh.update_faces(mesh.nondegenerate_faces())

If a height is specified, it will identify any face with a 2D oriented bounding box with one edge shorter than that height.

If not specified, it will identify any face with a zero normal.

Parameters:
    

**height** (_float_) – If specified identifies faces with an oriented bounding box shorter than this on one side.

Returns:
    

**nondegenerate** – Mask that can be used to remove faces

Return type:
    

(len(self.faces), ) bool

outline(_face_ids : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]] | None = None_, _** kwargs_) → [Path3D](trimesh.path.path.html#trimesh.path.path.Path3D "trimesh.path.path.Path3D")¶
    

Given a list of face indexes find the outline of those faces and return it as a Path3D.

The outline is defined here as every edge which is only included by a single triangle.

Note that this implies a non-watertight mesh as the outline of a watertight mesh is an empty path.

Parameters:
    

  * **face_ids** (_(__n_ _,__)__int_) – Indices to compute the outline of. If None, outline of full mesh will be computed.

  * ****kwargs** (_passed to Path3D constructor_)

Returns:
    

**path** – Curve in 3D of the outline

Return type:
    

[Path3D](trimesh.path.html#trimesh.path.Path3D "trimesh.path.Path3D")

_property _principal_inertia_components _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return the principal components of inertia

Ordering corresponds to mesh.principal_inertia_vectors

Returns:
    

**components** – Principal components of inertia

Return type:
    

(3, ) float

_property _principal_inertia_transform _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

A transform which moves the current mesh so the principal inertia vectors are on the X,Y, and Z axis, and the centroid is at the origin.

Returns:
    

**transform** – Homogeneous transformation matrix

Return type:
    

(4, 4) float

_property _principal_inertia_vectors _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return the principal axis of inertia as unit vectors. The order corresponds to mesh.principal_inertia_components.

Returns:
    

**vectors** – Three vectors pointing along the principal axis of inertia directions

Return type:
    

(3, 3) float

process(_validate : bool = False_, _merge_tex : bool | None = None_, _merge_norm : bool | None = None_) → Self¶
    

Do processing to make a mesh useful.

Does this by:
    

  1. removing NaN and Inf values

  2. merging duplicate vertices

If validate:
    

  3. Remove triangles which have one edge of their 2D oriented bounding box shorter than tol.merge

  4. remove duplicated triangles

  5. Attempt to ensure triangles are consistently wound and normals face outwards.

Parameters:
    

  * **validate** (_bool_) – Remove degenerate and duplicate faces.

  * **merge_tex** (_bool_) – If True textured meshes with UV coordinates will have vertices merged regardless of UV coordinates

  * **merge_norm** (_bool_) – If True, meshes with vertex normals will have vertices merged ignoring different normals

Returns:
    

**self** – Current mesh

Return type:
    

trimesh.Trimesh

projected(_normal : ArrayLike_, _** kwargs_) → [Path2D](trimesh.path.path.html#trimesh.path.path.Path2D "trimesh.path.path.Path2D")¶
    

Project a mesh onto a plane and then extract the polygon that outlines the mesh projection on that plane.

Parameters:
    

  * **normal** (_(__3_ _,__)__float_) – Normal to extract flat pattern along

  * **origin** (_None_ _or_ _(__3_ _,__)__float_) – Origin of plane to project mesh onto

  * **ignore_sign** (_bool_) – Allow a projection from the normal vector in either direction: this provides a substantial speedup on watertight meshes where the direction is irrelevant but if you have a triangle soup and want to discard backfaces you should set this to False.

  * **rpad** (_float_) – Proportion to pad polygons by before unioning and then de-padding result by to avoid zero-width gaps.

  * **apad** (_float_) – Absolute padding to pad polygons by before unioning and then de-padding result by to avoid zero-width gaps.

  * **tol_dot** (_float_) – Tolerance for discarding on-edge triangles.

  * **precise** (_bool_) – Use the precise projection computation using shapely.

  * **precise_eps** (_float_) – Tolerance for precise triangle checks.

Returns:
    

**projected** – Outline of source mesh

Return type:
    

[trimesh.path.Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D")

_property _referenced_vertices _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[bool]]_¶
    

Which vertices in the current mesh are referenced by a face.

Returns:
    

**referenced** – Which vertices are referenced by a face

Return type:
    

(len(self.vertices), ) bool

register(_other : [Geometry3D](trimesh.parent.html#trimesh.parent.Geometry3D "trimesh.parent.Geometry3D") | ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[_ScalarT]]_, _** kwargs_) → tuple[ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]], [float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]¶
    

Align a mesh with another mesh or a PointCloud using the principal axes of inertia as a starting point which is refined by iterative closest point.

Parameters:
    

  * **other** (_trimesh.Trimesh_ _or_ _(__n_ _,__3_ _)__float_) – Mesh or points in space

  * **samples** (_int_) – Number of samples from mesh surface to align

  * **icp_first** (_int_) – How many ICP iterations for the 9 possible combinations of

  * **icp_final** (_int_) – How many ICP itertations for the closest candidate from the wider search

Returns:
    

  * **mesh_to_other** (_(4, 4) float_) – Transform to align mesh to the other object

  * **cost** (_float_) – Average square distance per point

remove_infinite_values() → None¶
    

Ensure that every vertex and face consists of finite numbers. This will remove vertices or faces containing np.nan and np.inf

Alters self.faces and self.vertices

remove_unreferenced_vertices() → None¶
    

Remove all vertices in the current mesh which are not referenced by a face.

rezero() → None¶
    

Translate the mesh so that all vertex vertices are positive and the lower bound of self.bounds will be exactly zero.

Alters self.vertices.

sample(_count : int | integer | unsignedinteger_, _return_index : bool = False_, _face_weight : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None = None_)¶
    

Return random samples distributed across the surface of the mesh

Parameters:
    

  * **count** (_int_) – Number of points to sample

  * **return_index** (_bool_) – If True will also return the index of which face each sample was taken from.

  * **face_weight** (_None_ _or_ _len_ _(__mesh.faces_ _)__float_) – Weight faces by a factor other than face area. If None will be the same as face_weight=mesh.area

Returns:
    

  * **samples** (_(count, 3) float_) – Points on surface of mesh

  * **face_index** (_(count, ) int_) – Index of self.faces

scene(_** kwargs_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Returns a Scene object containing the current mesh.

Returns:
    

**scene** – Contains just the current mesh

Return type:
    

[trimesh.scene.scene.Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")

section(_plane_normal : ArrayLike_, _plane_origin : ArrayLike_, _** kwargs_) → [Path3D](trimesh.path.path.html#trimesh.path.path.Path3D "trimesh.path.path.Path3D") | None¶
    

Returns a 3D cross section of the current mesh and a plane defined by origin and normal.

Parameters:
    

  * **plane_normal** (_(__3_ _,__)__float_) – Normal vector of section plane.

  * **plane_origin** (_(__3_ _,__)__float_) – Point on the cross section plane.

Returns:
    

Curve of intersection or None if it was not hit by plane.

Return type:
    

intersections

section_multiplane(_plane_origin : ArrayLike_, _plane_normal : ArrayLike_, _heights : ArrayLike_) → list[[Path2D](trimesh.path.path.html#trimesh.path.path.Path2D "trimesh.path.path.Path2D") | None]¶
    

Return multiple parallel cross sections of the current mesh in 2D.

Parameters:
    

  * **plane_origin** (_(__3_ _,__)__float_) – Point on the cross section plane

  * **plane_normal** – Normal vector of section plane

  * **heights** (_(__n_ _,__)__float_) – Each section is offset by height along the plane normal.

Returns:
    

**paths** – 2D cross sections at specified heights. path.metadata[‘to_3D’] contains transform to return 2D section back into 3D space.

Return type:
    

(n, ) [Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D") or None

show(_viewer : None | [Callable](trimesh.typed.html#trimesh.typed.Callable "collections.abc.Callable") | Literal['gl', 'jupyter', 'marimo'] = None_, _** kwargs_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Render the mesh in an opengl window. Requires pyglet.

Parameters:
    

  * **viewer** (_ViewerType_) – What kind of viewer to use, such as gl to open a pyglet window jupyter for a jupyter notebook marimo’ for a marimo notebook None for a “best guess”

  * **smooth** (_bool_) – Run smooth shading on mesh or not, large meshes will be slow

Returns:
    

**scene** – Scene with current mesh in it

Return type:
    

[trimesh.scene.Scene](trimesh.scene.html#trimesh.scene.Scene "trimesh.scene.Scene")

simplify_quadric_decimation(_percent : float | floating | None = None_, _face_count : int | integer | unsignedinteger | None = None_, _aggression : int | integer | unsignedinteger | None = None_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

A thin wrapper around pip install fast-simplification.

Parameters:
    

  * **percent** – A number between 0.0 and 1.0 for how much

  * **face_count** – Target number of faces desired in the resulting mesh.

  * **aggression** – An integer between 0 and 10, the scale being roughly 0 is “slow and good” and 10 being “fast and bad.”

Returns:
    

**simple** – Simplified version of mesh.

Return type:
    

trimesh.Trimesh

slice_plane(_plane_origin : ArrayLike_, _plane_normal : ArrayLike_, _cap : bool = False_, _face_index : ArrayLike | None = None_, _** kwargs_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Slice the mesh with a plane, returning a new mesh that is the portion of the original mesh to the positive normal side of the plane

plane_origin(3,) float
    

Point on plane to intersect with mesh

plane_normal(3,) float
    

Normal vector of plane to intersect with mesh

capbool
    

If True, cap the result with a triangulated polygon

face_index((m,) int)
    

Indexes of mesh.faces to slice. When no mask is provided, the default is to slice all faces.

Returns:
    

**new_mesh** – Subset of current mesh that intersects the half plane to the positive normal side of the plane

Return type:
    

trimesh.Trimesh or None

_property _smooth_shaded _: [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")_¶
    

Smooth shading in OpenGL relies on which vertices are shared, this function will disconnect regions above an angle threshold and return a non-watertight version which will look better in an OpenGL rendering context.

If you would like to use non-default arguments see graph.smooth_shade.

Returns:
    

**smooth_shaded** – Non watertight version of current mesh.

Return type:
    

trimesh.Trimesh

split(_** kwargs_) → list[[Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")]¶
    

Split a mesh into multiple meshes from face connectivity.

If only_watertight is true it will only return watertight meshes and will attempt to repair single triangle or quad holes.

Parameters:
    

  * **mesh** (_trimesh.Trimesh_) – The source multibody mesh to split

  * **only_watertight** – Only return watertight components and discard any connected component that isn’t fully watertight.

  * **repair** – If set try to fill small holes in a mesh, before the discard step in `only_watertight.

  * **adjacency** (_(__n_ _,__2_ _)__int_) – If passed will be used instead of mesh.face_adjacency

  * **engine** – Which graph engine to use for the connected components.

  * **kwargs** – Will be passed to mesh.submesh

Returns:
    

**meshes** – Results of splitting based on parameters.

Return type:
    

(m,) trimesh.Trimesh

subdivide(_face_index : ArrayLike | None = None_, _iterations : int | integer | unsignedinteger | None = None_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Subdivide a mesh with each subdivided face replaced with four smaller faces. Will return a copy of current mesh with subdivided faces.

Parameters:
    

  * **face_index** (_(__m_ _,__)__int_ _or_ _None_) – If None all faces of mesh will be subdivided If (m, ) int array of indices: only specified faces will be subdivided. Note that in this case the mesh will generally no longer be manifold, as the additional vertex on the midpoint will not be used by the adjacent faces to the faces specified, and an additional postprocessing step will be required to make resulting mesh watertight

  * **iterations** (_int_) – If passed will run subdivisions multiple times recursively. NOT COMPATIBLE with face_index and will raise a ValueError if both arguments are passed.

Returns:
    

**mesh** – The copy of current mesh with subdivided faces.

Return type:
    

trimesh.Trimesh

subdivide_loop(_iterations : int | integer | unsignedinteger | None = None_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Subdivide a mesh by dividing each triangle into four triangles and approximating their smoothed surface using loop subdivision. Loop subdivision often looks better on triangular meshes than catmul-clark, which operates primarily on quads.

Parameters:
    

  * **iterations** (_int_) – Number of iterations to run subdivision.

  * **multibody** (_bool_) – If True will try to subdivide for each submesh

Returns:
    

**mesh** – The copy of current mesh with subdivided faces.

Return type:
    

trimesh.Trimesh

subdivide_to_size(_max_edge : float | floating_, _max_iter : int | integer | unsignedinteger = 10_, _return_index : bool = False_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh") | tuple[[Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh"), ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]]¶
    

Subdivide a mesh until every edge is shorter than a specified length.

Will return a triangle soup, not a nicely structured mesh.

Parameters:
    

  * **max_edge** (_float_) – Maximum length of any edge in the result

  * **max_iter** (_int_) – The maximum number of times to run subdivision

  * **return_index** (_bool_) – If True, return index of original face for new faces

Returns:
    

**mesh** – The copy of current mesh with subdivided faces.

Return type:
    

trimesh.Trimesh

submesh(_faces_sequence : [Sequence](trimesh.typed.html#trimesh.typed.Sequence "collections.abc.Sequence")[ArrayLike]_, _only_watertight : bool = False_, _repair : bool = False_, _** kwargs_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh") | list[[Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")]¶
    

Return a subset of the mesh.

Parameters:
    

  * **faces_sequence** (_sequence_ _(__m_ _,__)__int_) – Face indices of mesh

  * **only_watertight** (_bool_) – Only return submeshes which are watertight

  * **repair** – Try to repair the submesh if it is not watertight

  * **append** (_bool_) – Return a single mesh which has the faces appended. if this flag is set, only_watertight is ignored

Returns:
    

**submesh** – Single mesh if append or list of submeshes

Return type:
    

Trimesh or (n,) Trimesh

_property _symmetry _: str | None_¶
    

Check whether a mesh has rotational symmetry around an axis (radial) or point (spherical).

Returns:
    

**symmetry** – What kind of symmetry does the mesh have.

Return type:
    

None, ‘radial’, ‘spherical’

_property _symmetry_axis _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_¶
    

If a mesh has rotational symmetry, return the axis.

Returns:
    

**axis** – Axis around which a 2D profile was revolved to create this mesh.

Return type:
    

(3, ) float

_property _symmetry_section _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_¶
    

If a mesh has rotational symmetry return the two vectors which make up a section coordinate frame.

Returns:
    

**section** – Vectors to take a section along

Return type:
    

(2, 3) float

to_dict() → dict[str, str | list[list[float]] | list[list[int]]]¶
    

Return a dictionary representation of the current mesh with keys that can be used as the kwargs for the Trimesh constructor and matches the schema in: trimesh/resources/schema/primitive/trimesh.schema.json

Returns:
    

**result** – Matches schema and Trimesh constructor.

Return type:
    

dict

_property _triangles _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Actual triangles of the mesh (points, not indexes)

Returns:
    

**triangles** – Points of triangle vertices

Return type:
    

(n, 3, 3) float

_property _triangles_center _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The center of each triangle (barycentric [1/3, 1/3, 1/3])

Returns:
    

**triangles_center** – Center of each triangular face

Return type:
    

(len(self.faces), 3) float

_property _triangles_cross _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The cross product of two edges of each triangle.

Returns:
    

**crosses** – Cross product of each triangle

Return type:
    

(n, 3) float

_property _triangles_tree _: Index_¶
    

An R-tree containing each face of the mesh.

Returns:
    

**tree** – Each triangle in self.faces has a rectangular cell

Return type:
    

rtree.index

union(_other : [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh") | [Sequence](trimesh.typed.html#trimesh.typed.Sequence "collections.abc.Sequence")[[Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")]_, _engine : Literal['manifold', 'blender', None] = None_, _check_volume : bool = True_, _** kwargs_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Boolean union between this mesh and other meshes.

Parameters:
    

  * **other** (_Trimesh_ _or_ _(__n_ _,__)__Trimesh_) – Other meshes to union

  * **engine** – Which backend to use, the default recommendation is: pip install manifold3d.

  * **check_volume** – Raise an error if not all meshes are watertight positive volumes. Advanced users may want to ignore this check as it is expensive.

  * **kwargs** – Passed through to the engine.

Returns:
    

**union** – Union of self and other Trimesh objects

Return type:
    

trimesh.Trimesh

unique_faces() → ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[bool]]¶
    

On the current mesh find which faces are unique.

Returns:
    

**unique** – A mask where the first occurrence of a unique face is true.

Return type:
    

(len(faces),) bool

unmerge_vertices() → None¶
    

Removes all face references so that every face contains three unique vertex indices and no faces are adjacent.

unwrap(_image: <module 'PIL.Image' from '/home/user/venv/lib/python3.14/site-packages/PIL/Image.py'> = None_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Returns a Trimesh object equivalent to the current mesh where the vertices have been assigned uv texture coordinates. Vertices may be split into as many as necessary by the unwrapping algorithm, depending on how many uv maps they appear in.

Requires pip install xatlas

Parameters:
    

**image** (_None_ _or_ _PIL.Image_) – Image to assign to the material

Returns:
    

**unwrapped** – Mesh with unwrapped uv coordinates

Return type:
    

trimesh.Trimesh

update_faces(_mask : ArrayLike_) → None¶
    

In many cases, we will want to remove specific faces. However, there is additional bookkeeping to do this cleanly. This function updates the set of faces with a validity mask, as well as keeping track of normals and colors.

Parameters:
    

**mask** – Mask to remove faces

update_vertices(_mask : ArrayLike_, _inverse : ArrayLike | None = None_) → None¶
    

Update vertices with a mask.

Parameters:
    

  * **mask** (_(__len_ _(__self.vertices_ _)__)__bool_) – Array of which vertices to keep

  * **inverse** (_(__len_ _(__self.vertices_ _)__)__int_) – Array to reconstruct vertex references such as output by np.unique

_property _vertex_adjacency_graph _: Graph_¶
    

Returns a networkx graph representing the vertices and their connections in the mesh.

Returns:
    

**graph** – Graph representing vertices and edges between them where vertices are nodes and edges are edges

Return type:
    

networkx.Graph

Examples

This is useful for getting nearby vertices for a given vertex, potentially for some simple smoothing techniques.

mesh = trimesh.primitives.Box() graph = mesh.vertex_adjacency_graph graph.neighbors(0) > [1, 2, 3, 4]

_property _vertex_defects _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return the vertex defects, or (2*pi) minus the sum of the angles of every face that includes that vertex.

If a vertex is only included by coplanar triangles, this will be zero. For convex regions this is positive, and concave negative.

Returns:
    

**vertex_defect** – Vertex defect at the every vertex

Return type:
    

(len(self.vertices), ) float

_property _vertex_degree _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Return the number of faces each vertex is included in.

Returns:
    

**degree** – Number of faces each vertex is included in

Return type:
    

(len(self.vertices), ) int

_property _vertex_faces _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

A representation of the face indices that correspond to each vertex.

Returns:
    

**vertex_faces** – Each row contains the face indices that correspond to the given vertex, padded with -1 up to the max number of faces corresponding to any one vertex Where n == len(self.vertices), m == max number of faces for a single vertex

Return type:
    

(n,m) int

_property _vertex_neighbors _: list[list[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

The vertex neighbors of each vertex of the mesh, determined from the cached vertex_adjacency_graph, if already existent.

Returns:
    

**vertex_neighbors** – Represents immediate neighbors of each vertex along the edge of a triangle

Return type:
    

(len(self.vertices), ) int

Examples

This is useful for getting nearby vertices for a given vertex, potentially for some simple smoothing techniques.
    
    
    >>> mesh = trimesh.primitives.Box()
    >>> mesh.vertex_neighbors[0]
    [1, 2, 3, 4]
    

_property _vertex_normals _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

The vertex normals of the mesh. If the normals were loaded we check to make sure we have the same number of vertex normals and vertices before returning them. If there are no vertex normals defined or a shape mismatch we calculate the vertex normals from the mean normals of the faces the vertex is used in.

Returns:
    

**vertex_normals** – Represents the surface normal at each vertex. Where n == len(self.vertices)

Return type:
    

(n, 3) float

_property _vertices _: [TrackedArray](trimesh.caching.html#trimesh.caching.TrackedArray "trimesh.caching.TrackedArray")_¶
    

The vertices of the mesh.

This is regarded as core information which cannot be generated from cache and as such is stored in self._data which tracks the array for changes and clears cached values of the mesh if this is altered.

Returns:
    

**vertices** – Points in cartesian space referenced by self.faces

Return type:
    

(n, 3) float

_property _visual _: [ColorVisuals](trimesh.visual.color.html#trimesh.visual.color.ColorVisuals "trimesh.visual.color.ColorVisuals") | [TextureVisuals](trimesh.visual.texture.html#trimesh.visual.texture.TextureVisuals "trimesh.visual.texture.TextureVisuals") | None_¶
    

Get the stored visuals for the current mesh.

Returns:
    

**visual** – Contains visual information about the mesh

Return type:
    

[ColorVisuals](trimesh.visual.html#trimesh.visual.ColorVisuals "trimesh.visual.ColorVisuals") or [TextureVisuals](trimesh.visual.html#trimesh.visual.TextureVisuals "trimesh.visual.TextureVisuals")

_property _volume _: [float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")_¶
    

Volume of the current mesh calculated using a surface integral. If the current mesh isn’t watertight this is garbage.

Returns:
    

**volume** – Volume of the current mesh

Return type:
    

float

voxelized(_pitch : float | floating | None_, _method : str = 'subdivide'_, _** kwargs_)¶
    

Return a VoxelGrid object representing the current mesh discretized into voxels at the specified pitch

Parameters:
    

  * **pitch** (_float_) – The edge length of a single voxel

  * **method** (implementation key. See trimesh.voxel.creation.voxelizers)

  * ****kwargs** (_additional kwargs passed to the specified implementation._)

Returns:
    

**voxelized** – Representing the current mesh

Return type:
    

VoxelGrid object

trimesh.available_formats() → set[str]¶
    

Get a list of all available loaders

Returns:
    

Extensions of all available loaders i.e. {‘stl’, ‘ply’, ‘dxf’}

Return type:
    

loaders

trimesh.load(_file_obj : str | Path | [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom | dict | None_, _file_type : str | None = None_, _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _force : str | None = None_, _allow_remote : bool = False_, _** kwargs_) → [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")¶
    

THIS FUNCTION IS DEPRECATED but there are no current plans for it to be removed.

For new code the typed load functions trimesh.load_scene or trimesh.load_mesh are recommended over trimesh.load which is a backwards-compatibility wrapper that mimics the behavior of the old function and can return any geometry type.

Parameters:
    

  * **file_obj** (_str_ _, or_ _file- like object_) – The source of the data to be loadeded

  * **file_type** (_str_) – What kind of file type do we have (eg: ‘stl’)

  * **resolver** (_trimesh.visual.Resolver_) – Object to load referenced assets like materials and textures

  * **force** (_None_ _or_ _str_) – For ‘mesh’: try to coerce scenes into a single mesh For ‘scene’: try to coerce everything into a scene

  * **allow_remote** – If True allow this load call to work on a remote URL.

  * **kwargs** (_dict_) – Passed to geometry __init__

Returns:
    

**geometry** – Loaded geometry as trimesh classes

Return type:
    

Trimesh, [Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D"), [Path3D](trimesh.path.html#trimesh.path.Path3D "trimesh.path.Path3D"), Scene

trimesh.load_mesh(_* args_, _** kwargs_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Load a file into a Trimesh object.

Parameters:
    

  * **file_obj** (_str_ _or_ _file object_) – File name or file with mesh data

  * **file_type** (_str_ _or_ _None_) – Which file type, e.g. ‘stl’

  * **kwargs** (_dict_) – Passed to Trimesh constructor

Returns:
    

Loaded geometry data.

Return type:
    

mesh

trimesh.load_path(_file_obj_ , _file_type : str | None = None_, _** kwargs_)¶
    

Load a file to a Path file_object.

Parameters:
    

  * **file_obj** – 

Accepts many types:
    
    * Path, Path2D, or Path3D file_objects

    * open file file_object (dxf or svg)

    * file name (dxf or svg)

    * shapely.geometry.Polygon

    * shapely.geometry.MultiLineString

    * dict with kwargs for Path constructor

    * (n, 2, (2|3)) float line segments

  * **file_type** – Type of file is required if file object is passed.

Returns:
    

**path** – Data as a native trimesh Path file_object

Return type:
    

[Path](trimesh.path.path.html#trimesh.path.path.Path "trimesh.path.path.Path"), [Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D"), Path3D file_object

trimesh.load_remote(_url : str_, _** kwargs_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Load a mesh at a remote URL into a local trimesh object.

This is a thin wrapper around:
    

trimesh.load_scene(file_obj=url, allow_remote=True, **kwargs)

Parameters:
    

  * **url** – URL containing mesh file

  * ****kwargs** – Passed to load_scene

Returns:
    

**loaded** – Loaded result

Return type:
    

Trimesh, [Path](trimesh.path.path.html#trimesh.path.path.Path "trimesh.path.path.Path"), Scene

trimesh.load_scene(_file_obj : str | Path | [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom | dict | None_, _file_type : str | None = None_, _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _allow_remote : bool = False_, _metadata : dict | None = None_, _** kwargs_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Load geometry into the trimesh.Scene container. This may contain any parent.Geometry object, including Trimesh, Path2D, Path3D, or a PointCloud.

Parameters:
    

  * **file_obj** (_str_ _, or_ _file- like object_) – The source of the data to be loadeded

  * **file_type** (_str_) – What kind of file type do we have (eg: ‘stl’)

  * **resolver** (_trimesh.visual.Resolver_) – Object to load referenced assets like materials and textures

  * **force** (_None_ _or_ _str_) – For ‘mesh’: try to coerce scenes into a single mesh For ‘scene’: try to coerce everything into a scene

  * **allow_remote** – If True allow this load call to work on a remote URL.

  * **kwargs** (_dict_) – Passed to geometry __init__

Returns:
    

**geometry** – Loaded geometry as trimesh classes

Return type:
    

Trimesh, [Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D"), [Path3D](trimesh.path.html#trimesh.path.Path3D "trimesh.path.Path3D"), Scene

trimesh.transform_points(_points : ArrayLike_, _matrix : ArrayLike_, _translate : bool = True_) → ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]¶
    

Returns points rotated by a homogeneous transformation matrix.

If points are (n, 2) matrix must be (3, 3) If points are (n, 3) matrix must be (4, 4)

Parameters:
    

  * **points** (_(__n_ _,__dim_ _)__float_) – Points where dim is 2 or 3.

  * **matrix** (_(__3_ _,__3_ _) or_ _(__4_ _,__4_ _)__float_) – Homogeneous rotation matrix.

  * **translate** (_bool_) – Apply translation from matrix or not.

Returns:
    

**transformed** – Transformed points.

Return type:
    

(n, dim) float

trimesh.unitize(_vectors_ , _check_valid =False_, _threshold =None_)¶
    

Unitize a vector or an array or row-vectors.

Parameters:
    

  * **vectors** (_(__n_ _,__m_ _) or_ _(__j_ _)__float_) – Vector or vectors to be unitized

  * **check_valid** (_bool_) – If set, will return mask of nonzero vectors

  * **threshold** (_float_) – Cutoff for a value to be considered zero.

Returns:
    

  * **unit** (_(n,m) or (j) float_) – Input vectors but unitized

  * **valid** (_(n,) bool or bool_) – Mask of nonzero vectors returned if check_valid

---

## trimesh.exchange.html

# trimesh.exchange¶

  * [trimesh.exchange.gltf](trimesh.exchange.gltf.html)
    * [trimesh.exchange.gltf.extensions](trimesh.exchange.gltf.extensions.html)
      * [gltf_extensions.py](trimesh.exchange.gltf.extensions.html#gltf-extensions-py)
      * [`MaterialContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext)
        * [`MaterialContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.data)
        * [`MaterialContext.images`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.images)
        * [`MaterialContext.parse_textures`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.parse_textures)
      * [`PrimitiveContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext)
        * [`PrimitiveContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.accessors)
        * [`PrimitiveContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.data)
        * [`PrimitiveContext.mesh_kwargs`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.mesh_kwargs)
        * [`PrimitiveContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.primitive)
      * [`PrimitiveExportContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext)
        * [`PrimitiveExportContext.buffer_items`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.buffer_items)
        * [`PrimitiveExportContext.include_normals`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.include_normals)
        * [`PrimitiveExportContext.mesh`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.mesh)
        * [`PrimitiveExportContext.name`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.name)
        * [`PrimitiveExportContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.primitive)
        * [`PrimitiveExportContext.tree`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.tree)
      * [`PrimitivePreprocessContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext)
        * [`PrimitivePreprocessContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.accessors)
        * [`PrimitivePreprocessContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.data)
        * [`PrimitivePreprocessContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.primitive)
        * [`PrimitivePreprocessContext.views`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.views)
      * [`TextureSourceContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext)
        * [`TextureSourceContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext.data)
      * [`handle_extensions()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.handle_extensions)
      * [`register_handler()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.register_handler)
    * [gltf/__init__.py](trimesh.exchange.gltf.html#gltf-init-py)
    * [`export_glb()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.export_glb)
    * [`export_gltf()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.export_gltf)
    * [`get_schema()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.get_schema)
    * [`load_glb()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.load_glb)
    * [`load_gltf()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.load_gltf)
    * [`validate()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.validate)
  * [trimesh.exchange.binvox](trimesh.exchange.binvox.html)
    * [`Binvox`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox)
      * [`Binvox.rle_data`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.rle_data)
      * [`Binvox.scale`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.scale)
      * [`Binvox.shape`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.shape)
      * [`Binvox.translate`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.translate)
    * [`Binvoxer`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer)
      * [`Binvoxer.SUPPORTED_INPUT_TYPES`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.SUPPORTED_INPUT_TYPES)
      * [`Binvoxer.SUPPORTED_OUTPUT_TYPES`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.SUPPORTED_OUTPUT_TYPES)
      * [`Binvoxer.__init__()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.__init__)
      * [`Binvoxer.file_type`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.file_type)
    * [`binvox_bytes()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.binvox_bytes)
    * [`binvox_header()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.binvox_header)
    * [`export_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.export_binvox)
    * [`load_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.load_binvox)
    * [`parse_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.parse_binvox)
    * [`voxel_from_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.voxel_from_binvox)
    * [`voxelize_mesh()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.voxelize_mesh)
  * [trimesh.exchange.cascade](trimesh.exchange.cascade.html)
    * [`load_step()`](trimesh.exchange.cascade.html#trimesh.exchange.cascade.load_step)
  * [trimesh.exchange.dae](trimesh.exchange.dae.html)
    * [`export_collada()`](trimesh.exchange.dae.html#trimesh.exchange.dae.export_collada)
    * [`load_collada()`](trimesh.exchange.dae.html#trimesh.exchange.dae.load_collada)
    * [`load_zae()`](trimesh.exchange.dae.html#trimesh.exchange.dae.load_zae)
  * [trimesh.exchange.export](trimesh.exchange.export.html)
    * [`export_dict()`](trimesh.exchange.export.html#trimesh.exchange.export.export_dict)
    * [`export_dict64()`](trimesh.exchange.export.html#trimesh.exchange.export.export_dict64)
    * [`export_mesh()`](trimesh.exchange.export.html#trimesh.exchange.export.export_mesh)
    * [`export_scene()`](trimesh.exchange.export.html#trimesh.exchange.export.export_scene)
    * [`scene_to_dict()`](trimesh.exchange.export.html#trimesh.exchange.export.scene_to_dict)
  * [trimesh.exchange.load](trimesh.exchange.load.html)
    * [`available_formats()`](trimesh.exchange.load.html#trimesh.exchange.load.available_formats)
    * [`load()`](trimesh.exchange.load.html#trimesh.exchange.load.load)
    * [`load_mesh()`](trimesh.exchange.load.html#trimesh.exchange.load.load_mesh)
    * [`load_remote()`](trimesh.exchange.load.html#trimesh.exchange.load.load_remote)
    * [`load_scene()`](trimesh.exchange.load.html#trimesh.exchange.load.load_scene)
    * [`mesh_formats()`](trimesh.exchange.load.html#trimesh.exchange.load.mesh_formats)
  * [trimesh.exchange.misc](trimesh.exchange.misc.html)
    * [`load_dict()`](trimesh.exchange.misc.html#trimesh.exchange.misc.load_dict)
    * [`load_meshio()`](trimesh.exchange.misc.html#trimesh.exchange.misc.load_meshio)
  * [trimesh.exchange.obj](trimesh.exchange.obj.html)
    * [`export_obj()`](trimesh.exchange.obj.html#trimesh.exchange.obj.export_obj)
    * [`load_obj()`](trimesh.exchange.obj.html#trimesh.exchange.obj.load_obj)
    * [`parse_mtl()`](trimesh.exchange.obj.html#trimesh.exchange.obj.parse_mtl)
  * [trimesh.exchange.off](trimesh.exchange.off.html)
    * [`export_off()`](trimesh.exchange.off.html#trimesh.exchange.off.export_off)
    * [`load_off()`](trimesh.exchange.off.html#trimesh.exchange.off.load_off)
  * [trimesh.exchange.ply](trimesh.exchange.ply.html)
    * [`export_draco()`](trimesh.exchange.ply.html#trimesh.exchange.ply.export_draco)
    * [`export_ply()`](trimesh.exchange.ply.html#trimesh.exchange.ply.export_ply)
    * [`load_draco()`](trimesh.exchange.ply.html#trimesh.exchange.ply.load_draco)
    * [`load_ply()`](trimesh.exchange.ply.html#trimesh.exchange.ply.load_ply)
  * [trimesh.exchange.stl](trimesh.exchange.stl.html)
    * [`HeaderError`](trimesh.exchange.stl.html#trimesh.exchange.stl.HeaderError)
    * [`export_stl()`](trimesh.exchange.stl.html#trimesh.exchange.stl.export_stl)
    * [`export_stl_ascii()`](trimesh.exchange.stl.html#trimesh.exchange.stl.export_stl_ascii)
    * [`load_stl()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl)
    * [`load_stl_ascii()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl_ascii)
    * [`load_stl_binary()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl_binary)
  * [trimesh.exchange.threedxml](trimesh.exchange.threedxml.html)
    * [threedxml.py](trimesh.exchange.threedxml.html#threedxml-py)
    * [`load_3DXML()`](trimesh.exchange.threedxml.html#trimesh.exchange.threedxml.load_3DXML)
    * [`print_element()`](trimesh.exchange.threedxml.html#trimesh.exchange.threedxml.print_element)
  * [trimesh.exchange.threemf](trimesh.exchange.threemf.html)
    * [`export_3MF()`](trimesh.exchange.threemf.html#trimesh.exchange.threemf.export_3MF)
    * [`load_3MF()`](trimesh.exchange.threemf.html#trimesh.exchange.threemf.load_3MF)
  * [trimesh.exchange.urdf](trimesh.exchange.urdf.html)
    * [`export_urdf()`](trimesh.exchange.urdf.html#trimesh.exchange.urdf.export_urdf)
  * [trimesh.exchange.xaml](trimesh.exchange.xaml.html)
    * [xaml.py](trimesh.exchange.xaml.html#xaml-py)
    * [`load_XAML()`](trimesh.exchange.xaml.html#trimesh.exchange.xaml.load_XAML)
  * [trimesh.exchange.xyz](trimesh.exchange.xyz.html)
    * [`export_xyz()`](trimesh.exchange.xyz.html#trimesh.exchange.xyz.export_xyz)
    * [`load_xyz()`](trimesh.exchange.xyz.html#trimesh.exchange.xyz.load_xyz)

## trimesh/exchange¶

Contains the importers and exporters for various mesh formats.

Note that _you should probably not be using these directly_ , if you call trimesh.load it will then call and wrap the result of the various loaders:

`` mesh = trimesh.load(file_name) ``

---

## trimesh.exchange.html

# trimesh.exchange¶

  * [trimesh.exchange.gltf](trimesh.exchange.gltf.html)
    * [trimesh.exchange.gltf.extensions](trimesh.exchange.gltf.extensions.html)
      * [gltf_extensions.py](trimesh.exchange.gltf.extensions.html#gltf-extensions-py)
      * [`MaterialContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext)
        * [`MaterialContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.data)
        * [`MaterialContext.images`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.images)
        * [`MaterialContext.parse_textures`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.parse_textures)
      * [`PrimitiveContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext)
        * [`PrimitiveContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.accessors)
        * [`PrimitiveContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.data)
        * [`PrimitiveContext.mesh_kwargs`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.mesh_kwargs)
        * [`PrimitiveContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.primitive)
      * [`PrimitiveExportContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext)
        * [`PrimitiveExportContext.buffer_items`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.buffer_items)
        * [`PrimitiveExportContext.include_normals`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.include_normals)
        * [`PrimitiveExportContext.mesh`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.mesh)
        * [`PrimitiveExportContext.name`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.name)
        * [`PrimitiveExportContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.primitive)
        * [`PrimitiveExportContext.tree`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.tree)
      * [`PrimitivePreprocessContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext)
        * [`PrimitivePreprocessContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.accessors)
        * [`PrimitivePreprocessContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.data)
        * [`PrimitivePreprocessContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.primitive)
        * [`PrimitivePreprocessContext.views`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.views)
      * [`TextureSourceContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext)
        * [`TextureSourceContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext.data)
      * [`handle_extensions()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.handle_extensions)
      * [`register_handler()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.register_handler)
    * [gltf/__init__.py](trimesh.exchange.gltf.html#gltf-init-py)
    * [`export_glb()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.export_glb)
    * [`export_gltf()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.export_gltf)
    * [`get_schema()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.get_schema)
    * [`load_glb()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.load_glb)
    * [`load_gltf()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.load_gltf)
    * [`validate()`](trimesh.exchange.gltf.html#trimesh.exchange.gltf.validate)
  * [trimesh.exchange.binvox](trimesh.exchange.binvox.html)
    * [`Binvox`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox)
      * [`Binvox.rle_data`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.rle_data)
      * [`Binvox.scale`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.scale)
      * [`Binvox.shape`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.shape)
      * [`Binvox.translate`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvox.translate)
    * [`Binvoxer`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer)
      * [`Binvoxer.SUPPORTED_INPUT_TYPES`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.SUPPORTED_INPUT_TYPES)
      * [`Binvoxer.SUPPORTED_OUTPUT_TYPES`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.SUPPORTED_OUTPUT_TYPES)
      * [`Binvoxer.__init__()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.__init__)
      * [`Binvoxer.file_type`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.Binvoxer.file_type)
    * [`binvox_bytes()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.binvox_bytes)
    * [`binvox_header()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.binvox_header)
    * [`export_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.export_binvox)
    * [`load_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.load_binvox)
    * [`parse_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.parse_binvox)
    * [`voxel_from_binvox()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.voxel_from_binvox)
    * [`voxelize_mesh()`](trimesh.exchange.binvox.html#trimesh.exchange.binvox.voxelize_mesh)
  * [trimesh.exchange.cascade](trimesh.exchange.cascade.html)
    * [`load_step()`](trimesh.exchange.cascade.html#trimesh.exchange.cascade.load_step)
  * [trimesh.exchange.dae](trimesh.exchange.dae.html)
    * [`export_collada()`](trimesh.exchange.dae.html#trimesh.exchange.dae.export_collada)
    * [`load_collada()`](trimesh.exchange.dae.html#trimesh.exchange.dae.load_collada)
    * [`load_zae()`](trimesh.exchange.dae.html#trimesh.exchange.dae.load_zae)
  * [trimesh.exchange.export](trimesh.exchange.export.html)
    * [`export_dict()`](trimesh.exchange.export.html#trimesh.exchange.export.export_dict)
    * [`export_dict64()`](trimesh.exchange.export.html#trimesh.exchange.export.export_dict64)
    * [`export_mesh()`](trimesh.exchange.export.html#trimesh.exchange.export.export_mesh)
    * [`export_scene()`](trimesh.exchange.export.html#trimesh.exchange.export.export_scene)
    * [`scene_to_dict()`](trimesh.exchange.export.html#trimesh.exchange.export.scene_to_dict)
  * [trimesh.exchange.load](trimesh.exchange.load.html)
    * [`available_formats()`](trimesh.exchange.load.html#trimesh.exchange.load.available_formats)
    * [`load()`](trimesh.exchange.load.html#trimesh.exchange.load.load)
    * [`load_mesh()`](trimesh.exchange.load.html#trimesh.exchange.load.load_mesh)
    * [`load_remote()`](trimesh.exchange.load.html#trimesh.exchange.load.load_remote)
    * [`load_scene()`](trimesh.exchange.load.html#trimesh.exchange.load.load_scene)
    * [`mesh_formats()`](trimesh.exchange.load.html#trimesh.exchange.load.mesh_formats)
  * [trimesh.exchange.misc](trimesh.exchange.misc.html)
    * [`load_dict()`](trimesh.exchange.misc.html#trimesh.exchange.misc.load_dict)
    * [`load_meshio()`](trimesh.exchange.misc.html#trimesh.exchange.misc.load_meshio)
  * [trimesh.exchange.obj](trimesh.exchange.obj.html)
    * [`export_obj()`](trimesh.exchange.obj.html#trimesh.exchange.obj.export_obj)
    * [`load_obj()`](trimesh.exchange.obj.html#trimesh.exchange.obj.load_obj)
    * [`parse_mtl()`](trimesh.exchange.obj.html#trimesh.exchange.obj.parse_mtl)
  * [trimesh.exchange.off](trimesh.exchange.off.html)
    * [`export_off()`](trimesh.exchange.off.html#trimesh.exchange.off.export_off)
    * [`load_off()`](trimesh.exchange.off.html#trimesh.exchange.off.load_off)
  * [trimesh.exchange.ply](trimesh.exchange.ply.html)
    * [`export_draco()`](trimesh.exchange.ply.html#trimesh.exchange.ply.export_draco)
    * [`export_ply()`](trimesh.exchange.ply.html#trimesh.exchange.ply.export_ply)
    * [`load_draco()`](trimesh.exchange.ply.html#trimesh.exchange.ply.load_draco)
    * [`load_ply()`](trimesh.exchange.ply.html#trimesh.exchange.ply.load_ply)
  * [trimesh.exchange.stl](trimesh.exchange.stl.html)
    * [`HeaderError`](trimesh.exchange.stl.html#trimesh.exchange.stl.HeaderError)
    * [`export_stl()`](trimesh.exchange.stl.html#trimesh.exchange.stl.export_stl)
    * [`export_stl_ascii()`](trimesh.exchange.stl.html#trimesh.exchange.stl.export_stl_ascii)
    * [`load_stl()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl)
    * [`load_stl_ascii()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl_ascii)
    * [`load_stl_binary()`](trimesh.exchange.stl.html#trimesh.exchange.stl.load_stl_binary)
  * [trimesh.exchange.threedxml](trimesh.exchange.threedxml.html)
    * [threedxml.py](trimesh.exchange.threedxml.html#threedxml-py)
    * [`load_3DXML()`](trimesh.exchange.threedxml.html#trimesh.exchange.threedxml.load_3DXML)
    * [`print_element()`](trimesh.exchange.threedxml.html#trimesh.exchange.threedxml.print_element)
  * [trimesh.exchange.threemf](trimesh.exchange.threemf.html)
    * [`export_3MF()`](trimesh.exchange.threemf.html#trimesh.exchange.threemf.export_3MF)
    * [`load_3MF()`](trimesh.exchange.threemf.html#trimesh.exchange.threemf.load_3MF)
  * [trimesh.exchange.urdf](trimesh.exchange.urdf.html)
    * [`export_urdf()`](trimesh.exchange.urdf.html#trimesh.exchange.urdf.export_urdf)
  * [trimesh.exchange.xaml](trimesh.exchange.xaml.html)
    * [xaml.py](trimesh.exchange.xaml.html#xaml-py)
    * [`load_XAML()`](trimesh.exchange.xaml.html#trimesh.exchange.xaml.load_XAML)
  * [trimesh.exchange.xyz](trimesh.exchange.xyz.html)
    * [`export_xyz()`](trimesh.exchange.xyz.html#trimesh.exchange.xyz.export_xyz)
    * [`load_xyz()`](trimesh.exchange.xyz.html#trimesh.exchange.xyz.load_xyz)

## trimesh/exchange¶

Contains the importers and exporters for various mesh formats.

Note that _you should probably not be using these directly_ , if you call trimesh.load it will then call and wrap the result of the various loaders:

`` mesh = trimesh.load(file_name) ``

---

## trimesh.exchange.gltf.html

# trimesh.exchange.gltf¶

  * [trimesh.exchange.gltf.extensions](trimesh.exchange.gltf.extensions.html)
    * [gltf_extensions.py](trimesh.exchange.gltf.extensions.html#gltf-extensions-py)
    * [`MaterialContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext)
      * [`MaterialContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.data)
      * [`MaterialContext.images`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.images)
      * [`MaterialContext.parse_textures`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.MaterialContext.parse_textures)
    * [`PrimitiveContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext)
      * [`PrimitiveContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.accessors)
      * [`PrimitiveContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.data)
      * [`PrimitiveContext.mesh_kwargs`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.mesh_kwargs)
      * [`PrimitiveContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveContext.primitive)
    * [`PrimitiveExportContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext)
      * [`PrimitiveExportContext.buffer_items`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.buffer_items)
      * [`PrimitiveExportContext.include_normals`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.include_normals)
      * [`PrimitiveExportContext.mesh`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.mesh)
      * [`PrimitiveExportContext.name`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.name)
      * [`PrimitiveExportContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.primitive)
      * [`PrimitiveExportContext.tree`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitiveExportContext.tree)
    * [`PrimitivePreprocessContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext)
      * [`PrimitivePreprocessContext.accessors`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.accessors)
      * [`PrimitivePreprocessContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.data)
      * [`PrimitivePreprocessContext.primitive`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.primitive)
      * [`PrimitivePreprocessContext.views`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.PrimitivePreprocessContext.views)
    * [`TextureSourceContext`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext)
      * [`TextureSourceContext.data`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.TextureSourceContext.data)
    * [`handle_extensions()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.handle_extensions)
    * [`register_handler()`](trimesh.exchange.gltf.extensions.html#trimesh.exchange.gltf.extensions.register_handler)

## gltf/__init__.py¶

Provides GLTF 2.0 exports of trimesh.Trimesh objects as GL_TRIANGLES, and trimesh.Path2D/Path3D as GL_LINES

trimesh.exchange.gltf.export_glb(_scene_ , _include_normals =None_, _unitize_normals =True_, _tree_postprocessor =None_, _buffer_postprocessor =None_, _extension_webp =False_, _extension_draco =False_)¶
    

Export a scene as a binary GLTF (GLB) file.

Parameters:
    

  * **scene** ([_trimesh.Scene_](trimesh.html#trimesh.Scene "trimesh.Scene")) – Input geometry

  * **extras** (_JSON serializable_) – Will be stored in the extras field.

  * **include_normals** (_bool_) – Include vertex normals in output file?

  * **tree_postprocessor** (_func_) – Custom function to (in-place) post-process the tree before exporting.

  * **extension_webp** (_bool_) – Export textures as webP using EXT_texture_webp extension.

  * **extension_draco** (_bool_) – Compress mesh data using Draco (KHR_draco_mesh_compression). Requires the dracox package to be installed.

Returns:
    

**exported** – Exported result in GLB 2.0

Return type:
    

bytes

trimesh.exchange.gltf.export_gltf(_scene_ , _include_normals =None_, _merge_buffers =False_, _unitize_normals =True_, _tree_postprocessor =None_, _embed_buffers =False_, _extension_webp =False_, _extension_draco =False_)¶
    

Export a scene object as a GLTF directory.

This puts each mesh into a separate file (i.e. a buffer) as opposed to one larger file.

Parameters:
    

  * **scene** ([_trimesh.Scene_](trimesh.html#trimesh.Scene "trimesh.Scene")) – Scene to be exported

  * **include_normals** (_None_ _or_ _bool_) – Include vertex normals

  * **merge_buffers** (_bool_) – Merge buffers into one blob.

  * **unitize_normals** – GLTF requires unit normals, however sometimes people want to include non-unit normals for shading reasons.

  * **resolver** ([_trimesh.resolvers.Resolver_](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver")) – If passed will use to write each file.

  * **tree_postprocesser** (_None_ _or_ _callable_) – Run this on the header tree before exiting.

  * **embed_buffers** (_bool_) – Embed the buffer into JSON file as a base64 string in the URI

  * **extension_webp** (_bool_) – Export textures as webP (using glTF’s EXT_texture_webp extension).

  * **extension_draco** (_bool_) – Compress mesh data using Draco (KHR_draco_mesh_compression). Requires the dracox package to be installed.

Returns:
    

**export** – Format: {file name : file data}

Return type:
    

dict

trimesh.exchange.gltf.get_schema()¶
    

Get a copy of the GLTF 2.0 schema with references resolved.

Returns:
    

**schema** – A copy of the GLTF 2.0 schema without external references.

Return type:
    

dict

trimesh.exchange.gltf.load_glb(_file_obj : [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom_, _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _ignore_broken : bool = False_, _merge_primitives : bool = False_, _skip_materials : bool = False_, _** mesh_kwargs_)¶
    

Load a GLTF file in the binary GLB format into a trimesh.Scene.

Implemented from specification: <https://github.com/KhronosGroup/glTF/tree/master/specification/2.0>

Parameters:
    

  * **file_obj** (_file- like object_) – Containing GLB data

  * **resolver** (_trimesh.visual.Resolver_) – Object which can be used to load other files by name

  * **ignore_broken** (_bool_) – If there is a mesh we can’t load and this is True don’t raise an exception but return a partial result

  * **merge_primitives** (_bool_) – If True, each GLTF ‘mesh’ will correspond to a single Trimesh object.

  * **skip_materials** (_bool_) – If true, will not load materials (if present).

Returns:
    

**kwargs** – Kwargs to instantiate a trimesh.Scene

Return type:
    

dict

trimesh.exchange.gltf.load_gltf(_file_obj : [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom | None = None_, _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _ignore_broken : bool = False_, _merge_primitives : bool = False_, _skip_materials : bool = False_, _** mesh_kwargs_)¶
    

Load a GLTF file, which consists of a directory structure with multiple files.

Parameters:
    

  * **file_obj** (_None_ _or_ _file-like_) – Object containing header JSON, or None

  * **resolver** (_trimesh.visual.Resolver_) – Object which can be used to load other files by name

  * **ignore_broken** (_bool_) – If there is a mesh we can’t load and this is True don’t raise an exception but return a partial result

  * **merge_primitives** (_bool_) – If True, each GLTF ‘mesh’ will correspond to a single Trimesh object

  * **skip_materials** (_bool_) – If true, will not load materials (if present).

  * ****mesh_kwargs** (_dict_) – Passed to mesh constructor

Returns:
    

**kwargs** – Arguments to create scene

Return type:
    

dict

trimesh.exchange.gltf.validate(_header_)¶
    

Validate a GLTF 2.0 header against the schema.

Returns result from: jsonschema.validate(header, schema=get_schema())

Parameters:
    

**header** (_dict_) – Populated GLTF 2.0 header

:raises err : jsonschema.exceptions.ValidationError: If the tree is an invalid GLTF2.0 header

---

## trimesh.exchange.gltf.extensions.html

# trimesh.exchange.gltf.extensions¶

## gltf_extensions.py¶

Extension registry for glTF import/export with scope-based handlers. Each scope has a TypedDict defining the context passed to handlers.

_class _trimesh.exchange.gltf.extensions.MaterialContext¶
    

Bases: `TypedDict`

Context for material scope handlers.

data _: dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")]_¶
    

images _: list_¶
    

parse_textures _: Callable[[...], dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")]]_¶
    

_class _trimesh.exchange.gltf.extensions.PrimitiveContext¶
    

Bases: `TypedDict`

Context for primitive scope handlers (post-load).

accessors _: list_¶
    

data _: dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")]_¶
    

mesh_kwargs _: dict_¶
    

primitive _: dict_¶
    

_class _trimesh.exchange.gltf.extensions.PrimitiveExportContext¶
    

Bases: `TypedDict`

Context for primitive_export scope handlers (during export).

buffer_items _: OrderedDict_¶
    

include_normals _: bool_¶
    

mesh _: [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")_¶
    

name _: str_¶
    

primitive _: dict_¶
    

tree _: dict_¶
    

_class _trimesh.exchange.gltf.extensions.PrimitivePreprocessContext¶
    

Bases: `TypedDict`

Context for primitive_preprocess scope handlers (pre-load).

accessors _: list_¶
    

data _: dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")]_¶
    

primitive _: dict_¶
    

views _: list_¶
    

_class _trimesh.exchange.gltf.extensions.TextureSourceContext¶
    

Bases: `TypedDict`

Context for texture_source scope handlers.

data _: dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")]_¶
    

trimesh.exchange.gltf.extensions.handle_extensions(_*_ , _extensions : dict[str, [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")] | None_, _scope : Literal['material', 'texture_source', 'primitive', 'primitive_preprocess', 'primitive_export']_, _** kwargs_) → [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")¶
    

Process extensions dict for a given scope, calling registered handlers.

Parameters:
    

  * **extensions** – The “extensions” dict from a glTF element, or None.

  * **scope** – Handler scope to invoke.

  * ****kwargs** – 

Scope-specific arguments that will be combined with extension data into a typed context dict. Required kwargs by scope:

>     * material: parse_textures, images
> 
>     * texture_source: (none)
> 
>     * primitive: primitive, mesh_kwargs, accessors
> 
>     * primitive_preprocess: primitive, accessors, views
> 
>     * primitive_export: mesh, name, tree, buffer_items, primitive, include_normals

Returns:
    

Dict of {extension_name: result} for most scopes. For scopes ending in “_source”, returns first non-None result. For “primitive” scope, automatically merges results into mesh_kwargs.

Return type:
    

results

trimesh.exchange.gltf.extensions.register_handler(_name : str_, _scope : Literal['material', 'texture_source', 'primitive', 'primitive_preprocess', 'primitive_export']_) → Callable[[Callable[[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")], [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")]], Callable[[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")], [Any](trimesh.typed.html#trimesh.typed.Any "typing.Any")]]¶
    

Decorator to register a handler for a glTF extension.

Parameters:
    

  * **name** – Extension name, e.g. “KHR_materials_pbrSpecularGlossiness”.

  * **scope** – Handler scope, e.g. “material”, “texture_source”, “primitive”.

Returns:
    

Function that registers the handler and returns it unchanged.

Return type:
    

decorator

Example
    
    
    >>> @register_handler("MY_extension", scope="material")
    ... def my_handler(context: MaterialContext) -> Optional[Dict]:
    ...     data = context["data"]
    ...     images = context["images"]
    ...     return {"baseColorFactor": [1, 0, 0, 1]}
    
  *[*]: Keyword-only parameters separator (PEP 3102)

---

## trimesh.exchange.binvox.html

# trimesh.exchange.binvox¶

Parsing functions for Binvox files.

<https://www.patrickmin.com/binvox/binvox.html>

Exporting meshes as binvox files requires the binvox executable to be in your path.

_class _trimesh.exchange.binvox.Binvox(_rle_data_ , _shape_ , _translate_ , _scale_)¶
    

Bases: `tuple`

rle_data¶
    

Alias for field number 0

scale¶
    

Alias for field number 3

shape¶
    

Alias for field number 1

translate¶
    

Alias for field number 2

_class _trimesh.exchange.binvox.Binvoxer(_dimension =32_, _file_type ='binvox'_, _z_buffer_carving =True_, _z_buffer_voting =True_, _dilated_carving =False_, _exact =True_, _bounding_box =None_, _remove_internal =False_, _center =False_, _rotate_x =0_, _rotate_z =0_, _wireframe =False_, _fit =False_, _block_id =None_, _use_material_block_id =False_, _use_offscreen_pbuffer =False_, _downsample_factor =None_, _downsample_threshold =None_, _verbose =False_, _binvox_path =None_)¶
    

Bases: `object`

Interface for binvox CL tool.

This class is responsible purely for making calls to the CL tool. It makes no attempt to integrate with the rest of trimesh at all.

Constructor args configure command line options.

Binvoxer.__call__ operates on the path to a mode file.

If using this interface in published works, please cite the references below.

See CL tool website for further details.

<https://www.patrickmin.com/binvox/>

@article{nooruddin03,
    

author = {Fakir S. Nooruddin and Greg Turk}, title = {Simplification and Repair of Polygonal Models Using Volumetric

> Techniques},

journal = {IEEE Transactions on Visualization and Computer Graphics}, volume = {9}, number = {2}, pages = {191–205}, year = {2003}

}

@Misc{binvox,
    

author = {Patrick Min}, title = {binvox}, howpublished = {{ t <http://www.patrickmin.com/binvox>} or

> { t <https://www.google.com/search?q=binvox>}},

year = {2004 - 2019}, note = {Accessed: yyyy-mm-dd}

}

SUPPORTED_INPUT_TYPES _ = ('ug', 'obj', 'off', 'dfx', 'xgl', 'pov', 'brep', 'ply', 'jot')_¶
    

SUPPORTED_OUTPUT_TYPES _ = ('binvox', 'hips', 'mira', 'vtk', 'raw', 'schematic', 'msh')_¶
    

__init__(_dimension =32_, _file_type ='binvox'_, _z_buffer_carving =True_, _z_buffer_voting =True_, _dilated_carving =False_, _exact =True_, _bounding_box =None_, _remove_internal =False_, _center =False_, _rotate_x =0_, _rotate_z =0_, _wireframe =False_, _fit =False_, _block_id =None_, _use_material_block_id =False_, _use_offscreen_pbuffer =False_, _downsample_factor =None_, _downsample_threshold =None_, _verbose =False_, _binvox_path =None_)¶
    

Configure the voxelizer.

Parameters:
    

  * **dimension** (_voxel grid size_ _(__max 1024 when not using exact_ _)_)

  * **file_type** (_str_) – 

Output file type, supported types are:
    

’binvox’ ‘hips’ ‘mira’ ‘vtk’ ‘raw’ ‘schematic’ ‘msh’

  * **z_buffer_carving** (_use z buffer based carving. At least one of_) – z_buffer_carving and z_buffer_voting must be True.

  * **z_buffer_voting** (_use z-buffer based parity voting method._)

  * **dilated_carving** (_stop carving 1 voxel before intersection._)

  * **exact** (_any voxel with part_ _of_ _a triangle gets set. Does not use_) – graphics card.

  * **bounding_box** (_6-element float list/tuple_ _of_ _min_ _,__max values_ _,_) – (minx, miny, minz, maxx, maxy, maxz)

  * **remove_internal** (_remove internal voxels if True. Note there is some odd_) – behaviour if boundary voxels are occupied.

  * **center** (_center model inside unit cube._)

  * **rotate_x** (_number_ _of_ _90 degree ccw rotations around x-axis before_) – voxelizing.

  * **rotate_z** (_number_ _of_ _90 degree cw rotations around z-axis before_) – voxelizing.

  * **wireframe** (_also render the model in wireframe_ _(__helps with thin parts_ _)__._)

  * **fit** (_only write voxels in the voxel bounding box._)

  * **block_id** (_when converting to schematic_ _,__use this as the block ID._)

  * **use_matrial_block_id** (_when converting from obj to schematic_ _,__parse_) – block ID from material spec “usemtl blockid_<id>” (ids 1-255 only).

  * **use_offscreen_pbuffer** (_use offscreen pbuffer instead_ _of_ _onscreen_) – window.

  * **downsample_factor** (_downsample voxels by this factor in each dimension._) – Must be a power of 2 or None. If not None/1 and core dumped errors occur, try slightly adjusting dimensions.

  * **downsample_threshold** (_when downsampling_ _,__destination voxel is on if_) – more than this number of voxels are on.

  * **verbose** (_bool_) – If False, silences stdout/stderr from subprocess call.

  * **binvox_path** (_str_) – Path to binvox executable. The default looks for an executable called binvox on your PATH.

_property _file_type¶
    

trimesh.exchange.binvox.binvox_bytes(_rle_data_ , _shape_ , _translate =(0, 0, 0)_, _scale =1_)¶
    

Get a binary representation of binvox data.

Parameters:
    

  * **rle_data** (_numpy array_) – Run-length encoded numpy array.

  * **shape** (_(__3_ _,__)__int_) – Shape of voxel grid.

  * **translate** (_(__3_ _,__)__float_) – Translation of voxels

  * **scale** (_float_) – Length of entire voxel grid.

Returns:
    

**data** – Suitable for writing to binary file

Return type:
    

bytes

trimesh.exchange.binvox.binvox_header(_shape_ , _translate_ , _scale_)¶
    

> Get a binvox header string.
> 
> shape: length 3 iterable of ints denoting shape of voxel grid. translate: length 3 iterable of floats denoting translation. scale: num length of entire voxel grid.
> 
> string including “data

“ line.

trimesh.exchange.binvox.export_binvox(_voxel_ , _axis_order ='xzy'_)¶
    

Export trimesh.voxel.VoxelGrid instance to bytes

Parameters:
    

  * **voxel** (trimesh.voxel.VoxelGrid) – Assumes axis ordering of xyz and encodes in binvox default xzy ordering.

  * **axis_order** (_str_) – Eements in (‘x’, ‘y’, ‘z’, 0, 1, 2), the order of axes to encode data (standard is ‘xzy’ for binvox). voxel data is assumed to be in order ‘xyz’.

Returns:
    

**result** – Representation according to binvox spec

Return type:
    

bytes

trimesh.exchange.binvox.load_binvox(_file_obj_ , _resolver =None_, _axis_order ='xzy'_, _file_type =None_)¶
    

Load trimesh VoxelGrid instance from file.

Parameters:
    

  * **file_obj** (_file-like object_) – Contains binvox data

  * **resolver** (_unused_)

  * **axis_order** (_str_) – Order of axes in encoded data. Binvox default is ‘xzy’, but ‘xyz’ may be faster where this is not relevant.

Returns:
    

**result** – Loaded voxel data

Return type:
    

[trimesh.voxel.VoxelGrid](trimesh.voxel.html#trimesh.voxel.VoxelGrid "trimesh.voxel.VoxelGrid")

trimesh.exchange.binvox.parse_binvox(_fp_ , _writeable =False_)¶
    

Read a binvox file, spec at <https://www.patrickmin.com/binvox/binvox.html>

Parameters:
    

**fp** (_file-object_) – File like object with binvox file

Returns:
    

  * **binvox** (_namedtuple_) – Containing data

  * **rle** (_numpy array_) – Run length encoded data

Raises:
    

**IOError** – If invalid binvox file

trimesh.exchange.binvox.voxel_from_binvox(_rle_data_ , _shape_ , _translate =None_, _scale =1.0_, _axis_order ='xzy'_)¶
    

Factory for building from data associated with binvox files.

Parameters:
    

  * **rle_data** (_numpy_) – Run-length-encoded of flat voxel values, or a trimesh.rle.RunLengthEncoding object. See trimesh.rle documentation for description of encoding

  * **shape** (_(__3_ _,__)__int_) – Shape of voxel grid.

  * **translate** (_(__3_ _,__)__float_) – Translation of voxels

  * **scale** (_float_) – Length of entire voxel grid.

  * **encoded_axes** (_iterable_) – With values in (‘x’, ‘y’, ‘z’, 0, 1, 2), where x => 0, y => 1, z => 2 denoting the order of axes in the encoded data. binvox by default saves in xzy order, but using xyz (or (0, 1, 2)) will be faster in some circumstances.

Returns:
    

**result** – Loaded voxels

Return type:
    

[VoxelGrid](trimesh.voxel.html#trimesh.voxel.VoxelGrid "trimesh.voxel.VoxelGrid")

trimesh.exchange.binvox.voxelize_mesh(_mesh_ , _binvoxer =None_, _export_type ='off'_, _** binvoxer_kwargs_)¶
    

Interface for voxelizing Trimesh object via the binvox tool.

Implementation simply saved the mesh in the specified export_type then runs the Binvoxer.__call__ (using either the supplied binvoxer or creating one via binvoxer_kwargs)

Parameters:
    

  * **mesh** (_Trimesh object to voxelize._)

  * **binvoxer** (_optional Binvoxer instance._)

  * **export_type** (_file type to export mesh as temporarily for Binvoxer to_) – operate on.

  * ****binvoxer_kwargs** (_kwargs for creating a new Binvoxer instance. If binvoxer_) – if provided, this must be empty.

Return type:
    

VoxelGrid object resulting.

---

## trimesh.exchange.cascade.html

# trimesh.exchange.cascade¶

trimesh.exchange.cascade.load_step(_file_obj : [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO")_, _file_type_ , _tol_linear : float | floating | int | integer | unsignedinteger | None = None_, _tol_angular : float | floating | int | integer | unsignedinteger | None = None_, _tol_relative : bool | None = False_, _merge_primitives : bool = True_, _** kwargs_) → dict¶
    

Use cascadio a packaged version of OpenCASCADE to load a STEP file using GLB as an intermediate.

Parameters:
    

  * **file_obj** – STEP file to load.

  * ****kwargs** – Passed to cascadio.step_to_glb

Returns:
    

Keyword arguments for a Scene.

Return type:
    

kwargs

---

## trimesh.exchange.dae.html

# trimesh.exchange.dae¶

trimesh.exchange.dae.export_collada(_mesh_ , _** kwargs_)¶
    

Export a mesh or a list of meshes as a COLLADA .dae file.

Parameters:
    

**mesh** (_Trimesh object_ _or_ _list_ _of_ _Trimesh objects_) – The mesh(es) to export.

Returns:
    

**export**

Return type:
    

str, string of COLLADA format output

trimesh.exchange.dae.load_collada(_file_obj_ , _resolver =None_, _ignore_broken =True_, _** kwargs_)¶
    

Load a COLLADA (.dae) file into a list of trimesh kwargs.

Parameters:
    

  * **file_obj** (_file object_) – Containing a COLLADA file

  * **resolver** (_trimesh.visual.Resolver_ _or_ _None_) – For loading referenced files, like texture images

  * **ignore_broken** (_bool_) – 

Ignores broken references during loading:
    

[collada.common.DaeUnsupportedError,
    

collada.common.DaeBrokenRefError]

  * **kwargs** – Passed to trimesh.Trimesh.__init__

Returns:
    

**loaded** – kwargs for Trimesh constructor

Return type:
    

list of dict

trimesh.exchange.dae.load_zae(_file_obj_ , _resolver =None_, _** kwargs_)¶
    

Load a ZAE file, which is just a zipped DAE file.

Parameters:
    

  * **file_obj** (_file object_) – Contains ZAE data

  * **resolver** (_trimesh.visual.Resolver_) – Resolver to load additional assets

  * **kwargs** (_dict_) – Passed to load_collada

Returns:
    

**loaded** – Results of loading

Return type:
    

dict

---

## trimesh.exchange.export.html

# trimesh.exchange.export¶

trimesh.exchange.export.export_dict(_mesh_ , _encoding =None_)¶
    

Export a mesh to a dict

Parameters:
    

  * **mesh** ([_trimesh.Trimesh_](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")) – Mesh to be exported

  * **encoding** (_str_ _or_ _None_) – Such as ‘base64’

Returns:
    

**export** – Data stored in dict

Return type:
    

dict

trimesh.exchange.export.export_dict64(_mesh_)¶
    

Export a mesh as a dictionary, with data encoded to base64.

trimesh.exchange.export.export_mesh(_mesh_ , _file_obj_ , _file_type =None_, _resolver =None_, _** kwargs_)¶
    

Export a Trimesh object to a file- like object, or to a filename

Parameters:
    

  * **file_obj** (_str_ _,__file-like_) – Where should mesh be exported to

  * **file_type** (_str_ _or_ _None_) – Represents file type (eg: ‘stl’)

  * **resolver** (_None_ _or_[ _trimesh.resolvers.Resolver_](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver")) – Resolver to write referenced assets to

Returns:
    

**exported** – Result of exporter

Return type:
    

bytes or str

trimesh.exchange.export.export_scene(_scene_ , _file_obj_ , _file_type =None_, _resolver =None_, _** kwargs_)¶
    

Export a snapshot of the current scene.

Parameters:
    

  * **file_obj** (_str_ _,__file-like_ _, or_ _None_) – File object to export to

  * **file_type** (_str_ _or_ _None_) – What encoding to use for meshes IE: dict, dict64, stl

Returns:
    

**export** – Only returned if file_obj is None

Return type:
    

bytes

trimesh.exchange.export.scene_to_dict(_scene_ , _use_base64 =False_, _include_metadata =True_)¶
    

Export a Scene object as a dict.

Parameters:
    

**scene** ([_trimesh.Scene_](trimesh.html#trimesh.Scene "trimesh.Scene")) – Scene object to be exported

Returns:
    

**as_dict** – Scene as a dict

Return type:
    

dict

---

## trimesh.exchange.load.html

# trimesh.exchange.load¶

trimesh.exchange.load.available_formats() → set[str]¶
    

Get a list of all available loaders

Returns:
    

Extensions of all available loaders i.e. {‘stl’, ‘ply’, ‘dxf’}

Return type:
    

loaders

trimesh.exchange.load.load(_file_obj : str | Path | [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom | dict | None_, _file_type : str | None = None_, _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _force : str | None = None_, _allow_remote : bool = False_, _** kwargs_) → [Geometry](trimesh.parent.html#trimesh.parent.Geometry "trimesh.parent.Geometry")¶
    

THIS FUNCTION IS DEPRECATED but there are no current plans for it to be removed.

For new code the typed load functions trimesh.load_scene or trimesh.load_mesh are recommended over trimesh.load which is a backwards-compatibility wrapper that mimics the behavior of the old function and can return any geometry type.

Parameters:
    

  * **file_obj** (_str_ _, or_ _file- like object_) – The source of the data to be loadeded

  * **file_type** (_str_) – What kind of file type do we have (eg: ‘stl’)

  * **resolver** (_trimesh.visual.Resolver_) – Object to load referenced assets like materials and textures

  * **force** (_None_ _or_ _str_) – For ‘mesh’: try to coerce scenes into a single mesh For ‘scene’: try to coerce everything into a scene

  * **allow_remote** – If True allow this load call to work on a remote URL.

  * **kwargs** (_dict_) – Passed to geometry __init__

Returns:
    

**geometry** – Loaded geometry as trimesh classes

Return type:
    

[Trimesh](trimesh.html#trimesh.Trimesh "trimesh.Trimesh"), [Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D"), [Path3D](trimesh.path.html#trimesh.path.Path3D "trimesh.path.Path3D"), [Scene](trimesh.html#trimesh.Scene "trimesh.Scene")

trimesh.exchange.load.load_mesh(_* args_, _** kwargs_) → [Trimesh](trimesh.base.html#trimesh.base.Trimesh "trimesh.base.Trimesh")¶
    

Load a file into a Trimesh object.

Parameters:
    

  * **file_obj** (_str_ _or_ _file object_) – File name or file with mesh data

  * **file_type** (_str_ _or_ _None_) – Which file type, e.g. ‘stl’

  * **kwargs** (_dict_) – Passed to Trimesh constructor

Returns:
    

Loaded geometry data.

Return type:
    

mesh

trimesh.exchange.load.load_remote(_url : str_, _** kwargs_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Load a mesh at a remote URL into a local trimesh object.

This is a thin wrapper around:
    

trimesh.load_scene(file_obj=url, allow_remote=True, **kwargs)

Parameters:
    

  * **url** – URL containing mesh file

  * ****kwargs** – Passed to load_scene

Returns:
    

**loaded** – Loaded result

Return type:
    

[Trimesh](trimesh.html#trimesh.Trimesh "trimesh.Trimesh"), [Path](trimesh.path.path.html#trimesh.path.path.Path "trimesh.path.path.Path"), [Scene](trimesh.html#trimesh.Scene "trimesh.Scene")

trimesh.exchange.load.load_scene(_file_obj : str | Path | [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom | dict | None_, _file_type : str | None = None_, _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _allow_remote : bool = False_, _metadata : dict | None = None_, _** kwargs_) → [Scene](trimesh.scene.scene.html#trimesh.scene.scene.Scene "trimesh.scene.scene.Scene")¶
    

Load geometry into the trimesh.Scene container. This may contain any parent.Geometry object, including Trimesh, Path2D, Path3D, or a PointCloud.

Parameters:
    

  * **file_obj** (_str_ _, or_ _file- like object_) – The source of the data to be loadeded

  * **file_type** (_str_) – What kind of file type do we have (eg: ‘stl’)

  * **resolver** (_trimesh.visual.Resolver_) – Object to load referenced assets like materials and textures

  * **force** (_None_ _or_ _str_) – For ‘mesh’: try to coerce scenes into a single mesh For ‘scene’: try to coerce everything into a scene

  * **allow_remote** – If True allow this load call to work on a remote URL.

  * **kwargs** (_dict_) – Passed to geometry __init__

Returns:
    

**geometry** – Loaded geometry as trimesh classes

Return type:
    

[Trimesh](trimesh.html#trimesh.Trimesh "trimesh.Trimesh"), [Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D"), [Path3D](trimesh.path.html#trimesh.path.Path3D "trimesh.path.Path3D"), [Scene](trimesh.html#trimesh.Scene "trimesh.Scene")

trimesh.exchange.load.mesh_formats() → set[str]¶
    

Get a list of mesh formats available to load.

Returns:
    

Extensions of available mesh loaders i.e. {‘stl’, ‘ply’}

Return type:
    

loaders

---

## trimesh.exchange.misc.html

# trimesh.exchange.misc¶

trimesh.exchange.misc.load_dict(_file_obj_ , _** kwargs_)¶
    

Load multiple input types into kwargs for a Trimesh constructor. Tries to extract keys: ‘faces’ ‘vertices’ ‘face_normals’ ‘vertex_normals’

Parameters:
    

  * **file_obj** (_dict_)

  * **forms** (_accepts multiple_) – 

-dict: has keys for vertices and faces as (n,3) numpy arrays -dict: has keys for vertices/faces (n,3) arrays encoded as dicts/base64

> with trimesh.util.array_to_encoded/trimesh.util.encoded_to_array

-str: json blob as dict with either straight array or base64 values -file object: json blob of dict

  * **file_type** (_not used_)

Returns:
    

**loaded** – -vertices: (n,3) float -faces: (n,3) int -face_normals: (n,3) float (optional)

Return type:
    

dict with keys

trimesh.exchange.misc.load_meshio(_file_obj_ , _file_type : str_, _** kwargs_)¶
    

Load a meshio-supported file into the kwargs for a Trimesh constructor.

Parameters:
    

  * **file_obj** (_file object_) – Contains a meshio file

  * **file_type** (_str_) – File extension, aka ‘vtk’

Returns:
    

**loaded** – kwargs for Trimesh constructor

Return type:
    

dict

---

## trimesh.exchange.obj.html

# trimesh.exchange.obj¶

trimesh.exchange.obj.export_obj(_mesh_ , _include_normals =None_, _include_color =True_, _include_texture =True_, _return_texture =False_, _write_texture =True_, _resolver =None_, _digits =8_, _mtl_name =None_, _header ='https://github.com/mikedh/trimesh'_)¶
    

Export a mesh as a Wavefront OBJ file. TODO: scenes with textured meshes

Parameters:
    

  * **mesh** ([_trimesh.Trimesh_](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")) – Mesh to be exported

  * **include_normals** (_Optional_ _[__bool_ _]_) – Include vertex normals in export. If None will only be included if vertex normals are in cache.

  * **include_color** (_bool_) – Include vertex color in export

  * **include_texture** (_bool_) – Include vt texture in file text

  * **return_texture** (_bool_) – If True, return a dict with texture files

  * **write_texture** (_bool_) – If True and a writable resolver is passed write the referenced texture files with resolver

  * **resolver** (_None_ _or_[ _trimesh.resolvers.Resolver_](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver")) – Resolver which can write referenced text objects

  * **digits** (_int_) – Number of digits to include for floating point

  * **mtl_name** (_None_ _or_ _str_) – If passed, the file name of the MTL file.

  * **header** (_str_ _or_ _None_) – Header string for top of file or None for no header.

Returns:
    

  * **export** (_str_) – OBJ format output

  * **texture** (_dict_) – Contains files that need to be saved in the same directory as the exported mesh: {file name : bytes}

trimesh.exchange.obj.load_obj(_file_obj : str | Path | [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom | dict | None_, _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _group_material : bool = True_, _skip_materials : bool = False_, _maintain_order : bool = False_, _metadata : dict | None = None_, _split_objects : bool = False_, _split_groups : bool = False_, _** kwargs_) → dict¶
    

Load a Wavefront OBJ file into kwargs for a trimesh.Scene object.

Parameters:
    

  * **file_obj** (_file like object_) – Contains OBJ data

  * **resolver** (_trimesh.visual.resolvers.Resolver_) – Allow assets such as referenced textures and material files to be loaded

  * **group_material** (_bool_) – Group faces that share the same material into the same mesh.

  * **skip_materials** – Don’t load any materials.

  * **maintain_order** – Make the strongest attempt possible to not reorder faces or vertices which may result in visual artifacts and other odd behavior. The OBJ data structure is quite different than the “flat matching array” used by Trimesh and GLTF so this may not be completely possible.

  * **split_objects** – Whenever the loader encounters an o directive in the OBJ file, split the loaded result into a new Trimesh object.

  * **split_groups** – Whenever the loader encounters a g directive in the OBJ file, split the loaded result into a new Trimesh object.

Returns:
    

**kwargs** – Keyword arguments which can be loaded by trimesh.exchange.load.load_kwargs into a trimesh.Scene

Return type:
    

dict

trimesh.exchange.obj.parse_mtl(_mtl_ , _resolver =None_)¶
    

Parse a loaded MTL file.

Parameters:
    

  * **mtl** (_str_ _or_ _bytes_) – Data from an MTL file

  * **resolver** (_trimesh.Resolver_) – Fetch assets by name from file system, web, or other

Returns:
    

**mtllibs** – Each dict has keys: newmtl, map_Kd, Kd

Return type:
    

list of dict

---

## trimesh.exchange.off.html

# trimesh.exchange.off¶

trimesh.exchange.off.export_off(_mesh_ , _digits =10_) → str¶
    

Export a mesh as an OFF file, a simple text format

Parameters:
    

  * **mesh** ([_trimesh.Trimesh_](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")) – Geometry to export

  * **digits** (_int_) – Number of digits to include on floats

Returns:
    

**export** – OFF format output

Return type:
    

str

trimesh.exchange.off.load_off(_file_obj_ , _** kwargs_) → dict¶
    

Load an OFF file into the kwargs for a Trimesh constructor.

Parameters:
    

**file_obj** (_file object_) – Contains an OFF file

Returns:
    

**loaded** – kwargs for Trimesh constructor

Return type:
    

dict

---

## trimesh.exchange.ply.html

# trimesh.exchange.ply¶

trimesh.exchange.ply.export_draco(_mesh_ , _bits =28_)¶
    

Export a mesh using Google’s Draco compressed format.

Only works if draco_encoder is in your PATH: <https://github.com/google/draco>

Parameters:
    

  * **mesh** (_Trimesh object_) – Mesh to export

  * **bits** (_int_) – Bits of quantization for position tol.merge=1e-8 is roughly 25 bits

Returns:
    

**data** – DRC file bytes

Return type:
    

str or bytes

trimesh.exchange.ply.export_ply(_mesh_ , _encoding ='binary'_, _vertex_normal : bool | None = None_, _include_attributes : bool = True_)¶
    

Export a mesh in the PLY format.

Parameters:
    

  * **mesh** ([_trimesh.Trimesh_](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")) – Mesh to export.

  * **encoding** (_str_) – PLY encoding: ‘ascii’ or ‘binary_little_endian’

  * **vertex_normal** (_None_ _or_ _include vertex normals_)

Returns:
    

**export**

Return type:
    

bytes of result

trimesh.exchange.ply.load_draco(_file_obj_ , _** kwargs_)¶
    

Load a mesh from Google’s Draco format.

Parameters:
    

**file_obj** (_file- like object_) – Contains data

Returns:
    

**kwargs** – Keyword arguments to construct a Trimesh object

Return type:
    

dict

trimesh.exchange.ply.load_ply(_file_obj_ , _resolver : [Resolver](trimesh.resolvers.html#trimesh.resolvers.Resolver "trimesh.resolvers.Resolver") | None = None_, _fix_texture : bool = True_, _prefer_color : str | None = None_, _skip_materials : bool = False_, _* args_, _** kwargs_)¶
    

Load a PLY file from an open file object.

Parameters:
    

  * **file_obj** (_an open file- like object_) – Source data, ASCII or binary PLY

  * **resolver** – Object which can resolve assets

  * **fix_texture** – If True, will re- index vertices and faces so vertices with different UV coordinates are disconnected.

  * **skip_materials** – If True, will not load texture (if present).

  * **prefer_color** – None, ‘vertex’, or ‘face’ Which kind of color to prefer if both defined

Returns:
    

**mesh_kwargs** – Data which can be passed to Trimesh constructor, eg: a = Trimesh(**mesh_kwargs)

Return type:
    

dict

---

## trimesh.exchange.stl.html

# trimesh.exchange.stl¶

_exception _trimesh.exchange.stl.HeaderError¶
    

Bases: `Exception`

trimesh.exchange.stl.export_stl(_mesh_) → bytes¶
    

Convert a Trimesh object into a binary STL file.

Parameters:
    

**mesh** – Trimesh object to export.

Returns:
    

Represents mesh in binary STL form

Return type:
    

export

trimesh.exchange.stl.export_stl_ascii(_mesh_) → str¶
    

Convert a Trimesh object into an ASCII STL file.

Parameters:
    

**mesh** ([_trimesh.Trimesh_](trimesh.html#trimesh.Trimesh "trimesh.Trimesh"))

Returns:
    

Mesh represented as an ASCII STL file

Return type:
    

export

trimesh.exchange.stl.load_stl(_file_obj : [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom_, _** kwargs_) → dict¶
    

Load a binary or an ASCII STL file from a file object.

Parameters:
    

**file_obj** – Containing STL data

Returns:
    

Keyword arguments for a Trimesh constructor with data loaded into properly shaped numpy arrays.

Return type:
    

loaded

trimesh.exchange.stl.load_stl_ascii(_file_obj : [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom_) → dict¶
    

Load an ASCII STL file from a file object.

Parameters:
    

**file_obj** (_open file- like object_) – Containing input data

Returns:
    

Keyword arguments for a Trimesh constructor with data loaded into properly shaped numpy arrays.

Return type:
    

loaded

trimesh.exchange.stl.load_stl_binary(_file_obj : [IO](trimesh.typed.html#trimesh.typed.IO "typing.IO") | BytesIO | StringIO | [BinaryIO](trimesh.typed.html#trimesh.typed.BinaryIO "typing.BinaryIO") | TextIO | BufferedRandom_) → dict¶
    

Load a binary STL file from a file object.

Parameters:
    

**file_obj** (_open file- like object_) – Containing STL data

Returns:
    

Keyword arguments for a Trimesh constructor with data loaded into properly shaped numpy arrays.

Return type:
    

loaded

---

## trimesh.exchange.threedxml.html

# trimesh.exchange.threedxml¶

## threedxml.py¶

Load 3DXML files, a scene format from Dassault products like Solidworks, Abaqus, Catia

trimesh.exchange.threedxml.load_3DXML(_file_obj_ , _* args_, _** kwargs_)¶
    

Load a 3DXML scene into kwargs. 3DXML is a CAD format that can be exported from Solidworks

Parameters:
    

**file_obj** (_file object_) – Open and containing 3DXML data

Returns:
    

**kwargs** – Can be passed to trimesh.exchange.load.load_kwargs

Return type:
    

dict

trimesh.exchange.threedxml.print_element(_element_)¶
    

Pretty-print an lxml.etree element.

Parameters:
    

**element** (_etree element_)

---

## trimesh.exchange.threemf.html

# trimesh.exchange.threemf¶

trimesh.exchange.threemf.export_3MF(_mesh_ , _batch_size =4096_, _compression =8_, _compresslevel =5_)¶
    

Converts a Trimesh object into a 3MF file.

Parameters:
    

  * **trimesh.trimesh** (_mesh_) – Mesh or Scene to export.

  * **batch_size** (_int_) – Number of nodes to write per batch.

  * **compression** (_zipfile.ZIP_*_) – Type of zip compression to use in this export.

  * **compresslevel** (_int_) – For Python > 3.7 specify the 0-9 compression level.

Returns:
    

**export** – Represents geometry as a 3MF file.

Return type:
    

bytes

trimesh.exchange.threemf.load_3MF(_file_obj_ , _postprocess =True_, _** kwargs_)¶
    

Load a 3MF formatted file into a Trimesh scene.

Parameters:
    

**file_obj** (_file-like_) – Contains 3MF formatted data

Returns:
    

**kwargs** – Constructor arguments for trimesh.Scene

Return type:
    

dict

---

## trimesh.exchange.urdf.html

# trimesh.exchange.urdf¶

trimesh.exchange.urdf.export_urdf(_mesh_ , _directory_ , _scale =1.0_, _color =None_, _** kwargs_)¶
    

Convert a Trimesh object into a URDF package for physics simulation. This breaks the mesh into convex pieces and writes them to the same directory as the .urdf file.

Parameters:
    

  * **mesh** ([_trimesh.Trimesh_](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")) – Input geometry

  * **directory** (_str_) – The directory path for the URDF package

Returns:
    

**mesh** – Multi-body mesh containing convex decomposition

Return type:
    

[Trimesh](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")

---

## trimesh.exchange.xaml.html

# trimesh.exchange.xaml¶

## xaml.py¶

Load 3D XAMl files, an export option from Solidworks.

trimesh.exchange.xaml.load_XAML(_file_obj_ , _* args_, _** kwargs_)¶
    

Load a 3D XAML file.

Parameters:
    

**file_obj** (_file object_) – Open XAML file.

Returns:
    

**result** – Kwargs for a Trimesh constructor.

Return type:
    

dict

---

## trimesh.exchange.xyz.html

# trimesh.exchange.xyz¶

trimesh.exchange.xyz.export_xyz(_cloud_ , _write_colors =True_, _delimiter =None_)¶
    

Export a PointCloud object to an XYZ format string.

Parameters:
    

  * **cloud** ([_trimesh.PointCloud_](trimesh.html#trimesh.PointCloud "trimesh.PointCloud")) – Geometry in space

  * **write_colors** (_bool_) – Write colors or not

  * **delimiter** (_None_ _or_ _str_) – What to separate columns with

Returns:
    

**export** – Pointcloud in XYZ format

Return type:
    

str

trimesh.exchange.xyz.load_xyz(_file_obj_ , _delimiter =None_, _** kwargs_)¶
    

Load an XYZ file into a PointCloud.

Parameters:
    

  * **file_obj** (_an open file-like object_) – Source data, ASCII XYZ

  * **delimiter** (_None_ _or_ _string_) – Characters used to separate the columns of the file If not passed will use whitespace or commas

Returns:
    

**kwargs** – Data which can be passed to PointCloud constructor

Return type:
    

dict

---

## trimesh.interfaces.html

# trimesh.interfaces¶

  * [trimesh.interfaces.blender](trimesh.interfaces.blender.html)
    * [`boolean()`](trimesh.interfaces.blender.html#trimesh.interfaces.blender.boolean)
    * [`unwrap()`](trimesh.interfaces.blender.html#trimesh.interfaces.blender.unwrap)
  * [trimesh.interfaces.generic](trimesh.interfaces.generic.html)
    * [`MeshScript`](trimesh.interfaces.generic.html#trimesh.interfaces.generic.MeshScript)
      * [`MeshScript.__init__()`](trimesh.interfaces.generic.html#trimesh.interfaces.generic.MeshScript.__init__)
      * [`MeshScript.run()`](trimesh.interfaces.generic.html#trimesh.interfaces.generic.MeshScript.run)

---

## trimesh.interfaces.blender.html

# trimesh.interfaces.blender¶

trimesh.interfaces.blender.boolean(_meshes : [Iterable](trimesh.typed.html#trimesh.typed.Iterable "collections.abc.Iterable")_, _operation : Literal['difference', 'union', 'intersection'] = 'difference'_, _use_exact : bool = True_, _use_self : bool = False_, _debug : bool = False_, _check_volume : bool = True_)¶
    

Run a boolean operation with multiple meshes using Blender.

Parameters:
    

  * **meshes** – List of mesh objects to be operated on

  * **operation** – Type of boolean operation (“difference”, “union”, “intersect”).

  * **use_exact** – Use the “exact” mode as opposed to the “fast” mode.

  * **use_self** – Whether to consider self-intersections.

  * **debug** – Provide additional output for troubleshooting.

  * **check_volume** – Raise an error if not all meshes are watertight positive volumes. Advanced users may want to ignore this check as it is expensive.

Returns:
    

The result of the boolean operation on the provided meshes.

Return type:
    

result

trimesh.interfaces.blender.unwrap(_mesh_ , _angle_limit : float = 66.0_, _island_margin : float = 0.0_, _debug : bool = False_)¶
    

Run an unwrap operation using blender.

---

## trimesh.interfaces.generic.html

# trimesh.interfaces.generic¶

_class _trimesh.interfaces.generic.MeshScript(_meshes_ , _script_ , _exchange ='stl'_, _debug =False_, _** kwargs_)¶
    

Bases: `object`

__init__(_meshes_ , _script_ , _exchange ='stl'_, _debug =False_, _** kwargs_)¶
    

run(_command_)¶

---

## trimesh.path.html

# trimesh.path¶

  * [trimesh.path.exchange](trimesh.path.exchange.html)
    * [trimesh.path.exchange.dxf](trimesh.path.exchange.dxf.html)
      * [`bulge_to_arcs()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.bulge_to_arcs)
      * [`convert_entities()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.convert_entities)
      * [`export_dxf()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.export_dxf)
      * [`get_key()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.get_key)
      * [`load_dxf()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.load_dxf)
    * [trimesh.path.exchange.export](trimesh.path.exchange.export.html)
      * [`export_dict()`](trimesh.path.exchange.export.html#trimesh.path.exchange.export.export_dict)
      * [`export_path()`](trimesh.path.exchange.export.html#trimesh.path.exchange.export.export_path)
    * [trimesh.path.exchange.load](trimesh.path.exchange.load.html)
      * [`load_path()`](trimesh.path.exchange.load.html#trimesh.path.exchange.load.load_path)
      * [`path_formats()`](trimesh.path.exchange.load.html#trimesh.path.exchange.load.path_formats)
    * [trimesh.path.exchange.misc](trimesh.path.exchange.misc.html)
      * [`dict_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.dict_to_path)
      * [`edges_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.edges_to_path)
      * [`faces_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.faces_to_path)
      * [`lines_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.lines_to_path)
      * [`linestrings_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.linestrings_to_path)
      * [`polygon_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.polygon_to_path)
    * [trimesh.path.exchange.svg_io](trimesh.path.exchange.svg_io.html)
      * [`element_transform()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.element_transform)
      * [`export_svg()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.export_svg)
      * [`svg_to_path()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.svg_to_path)
      * [`transform_to_matrices()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.transform_to_matrices)
  * [trimesh.path.arc](trimesh.path.arc.html)
    * [`ArcInfo`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo)
      * [`ArcInfo.__init__()`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.__init__)
      * [`ArcInfo.angles`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.angles)
      * [`ArcInfo.center`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.center)
      * [`ArcInfo.normal`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.normal)
      * [`ArcInfo.radius`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.radius)
      * [`ArcInfo.span`](trimesh.path.arc.html#trimesh.path.arc.ArcInfo.span)
    * [`arc_center()`](trimesh.path.arc.html#trimesh.path.arc.arc_center)
    * [`discretize_arc()`](trimesh.path.arc.html#trimesh.path.arc.discretize_arc)
    * [`to_threepoint()`](trimesh.path.arc.html#trimesh.path.arc.to_threepoint)
  * [trimesh.path.creation](trimesh.path.creation.html)
    * [`box_outline()`](trimesh.path.creation.html#trimesh.path.creation.box_outline)
    * [`circle()`](trimesh.path.creation.html#trimesh.path.creation.circle)
    * [`circle_pattern()`](trimesh.path.creation.html#trimesh.path.creation.circle_pattern)
    * [`grid()`](trimesh.path.creation.html#trimesh.path.creation.grid)
    * [`rectangle()`](trimesh.path.creation.html#trimesh.path.creation.rectangle)
  * [trimesh.path.curve](trimesh.path.curve.html)
    * [`binomial()`](trimesh.path.curve.html#trimesh.path.curve.binomial)
    * [`discretize_bezier()`](trimesh.path.curve.html#trimesh.path.curve.discretize_bezier)
    * [`discretize_bspline()`](trimesh.path.curve.html#trimesh.path.curve.discretize_bspline)
  * [trimesh.path.entities](trimesh.path.entities.html)
    * [entities.py](trimesh.path.entities.html#entities-py)
    * [`Arc`](trimesh.path.entities.html#trimesh.path.entities.Arc)
      * [`Arc.bounds()`](trimesh.path.entities.html#trimesh.path.entities.Arc.bounds)
      * [`Arc.center()`](trimesh.path.entities.html#trimesh.path.entities.Arc.center)
      * [`Arc.closed`](trimesh.path.entities.html#trimesh.path.entities.Arc.closed)
      * [`Arc.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Arc.discrete)
      * [`Arc.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Arc.is_valid)
      * [`Arc.length()`](trimesh.path.entities.html#trimesh.path.entities.Arc.length)
    * [`BSpline`](trimesh.path.entities.html#trimesh.path.entities.BSpline)
      * [`BSpline.__init__()`](trimesh.path.entities.html#trimesh.path.entities.BSpline.__init__)
      * [`BSpline.discrete()`](trimesh.path.entities.html#trimesh.path.entities.BSpline.discrete)
      * [`BSpline.to_dict()`](trimesh.path.entities.html#trimesh.path.entities.BSpline.to_dict)
    * [`Bezier`](trimesh.path.entities.html#trimesh.path.entities.Bezier)
      * [`Bezier.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Bezier.discrete)
    * [`Curve`](trimesh.path.entities.html#trimesh.path.entities.Curve)
      * [`Curve.nodes`](trimesh.path.entities.html#trimesh.path.entities.Curve.nodes)
    * [`Entity`](trimesh.path.entities.html#trimesh.path.entities.Entity)
      * [`Entity.__init__()`](trimesh.path.entities.html#trimesh.path.entities.Entity.__init__)
      * [`Entity.bounds()`](trimesh.path.entities.html#trimesh.path.entities.Entity.bounds)
      * [`Entity.closed`](trimesh.path.entities.html#trimesh.path.entities.Entity.closed)
      * [`Entity.copy()`](trimesh.path.entities.html#trimesh.path.entities.Entity.copy)
      * [`Entity.end_points`](trimesh.path.entities.html#trimesh.path.entities.Entity.end_points)
      * [`Entity.explode()`](trimesh.path.entities.html#trimesh.path.entities.Entity.explode)
      * [`Entity.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Entity.is_valid)
      * [`Entity.layer`](trimesh.path.entities.html#trimesh.path.entities.Entity.layer)
      * [`Entity.length()`](trimesh.path.entities.html#trimesh.path.entities.Entity.length)
      * [`Entity.metadata`](trimesh.path.entities.html#trimesh.path.entities.Entity.metadata)
      * [`Entity.nodes`](trimesh.path.entities.html#trimesh.path.entities.Entity.nodes)
      * [`Entity.reverse()`](trimesh.path.entities.html#trimesh.path.entities.Entity.reverse)
      * [`Entity.to_dict()`](trimesh.path.entities.html#trimesh.path.entities.Entity.to_dict)
    * [`Line`](trimesh.path.entities.html#trimesh.path.entities.Line)
      * [`Line.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Line.discrete)
      * [`Line.explode()`](trimesh.path.entities.html#trimesh.path.entities.Line.explode)
      * [`Line.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Line.is_valid)
      * [`Line.to_dict()`](trimesh.path.entities.html#trimesh.path.entities.Line.to_dict)
    * [`Text`](trimesh.path.entities.html#trimesh.path.entities.Text)
      * [`Text.__init__()`](trimesh.path.entities.html#trimesh.path.entities.Text.__init__)
      * [`Text.angle()`](trimesh.path.entities.html#trimesh.path.entities.Text.angle)
      * [`Text.closed`](trimesh.path.entities.html#trimesh.path.entities.Text.closed)
      * [`Text.discrete()`](trimesh.path.entities.html#trimesh.path.entities.Text.discrete)
      * [`Text.end_points`](trimesh.path.entities.html#trimesh.path.entities.Text.end_points)
      * [`Text.is_valid`](trimesh.path.entities.html#trimesh.path.entities.Text.is_valid)
      * [`Text.length()`](trimesh.path.entities.html#trimesh.path.entities.Text.length)
      * [`Text.nodes`](trimesh.path.entities.html#trimesh.path.entities.Text.nodes)
      * [`Text.normal`](trimesh.path.entities.html#trimesh.path.entities.Text.normal)
      * [`Text.origin`](trimesh.path.entities.html#trimesh.path.entities.Text.origin)
      * [`Text.plot()`](trimesh.path.entities.html#trimesh.path.entities.Text.plot)
      * [`Text.vector`](trimesh.path.entities.html#trimesh.path.entities.Text.vector)
  * [trimesh.path.intersections](trimesh.path.intersections.html)
    * [`line_line()`](trimesh.path.intersections.html#trimesh.path.intersections.line_line)
  * [trimesh.path.packing](trimesh.path.packing.html)
    * [packing.py](trimesh.path.packing.html#packing-py)
    * [`RectangleBin`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin)
      * [`RectangleBin.__init__()`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin.__init__)
      * [`RectangleBin.extents`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin.extents)
      * [`RectangleBin.insert()`](trimesh.path.packing.html#trimesh.path.packing.RectangleBin.insert)
    * [`bounds_overlap()`](trimesh.path.packing.html#trimesh.path.packing.bounds_overlap)
    * [`images()`](trimesh.path.packing.html#trimesh.path.packing.images)
    * [`meshes()`](trimesh.path.packing.html#trimesh.path.packing.meshes)
    * [`paths()`](trimesh.path.packing.html#trimesh.path.packing.paths)
    * [`polygons()`](trimesh.path.packing.html#trimesh.path.packing.polygons)
    * [`rectangles()`](trimesh.path.packing.html#trimesh.path.packing.rectangles)
    * [`rectangles_single()`](trimesh.path.packing.html#trimesh.path.packing.rectangles_single)
    * [`roll_transform()`](trimesh.path.packing.html#trimesh.path.packing.roll_transform)
    * [`visualize()`](trimesh.path.packing.html#trimesh.path.packing.visualize)
  * [trimesh.path.path](trimesh.path.path.html)
    * [path.py](trimesh.path.path.html#path-py)
    * [`Path`](trimesh.path.path.html#trimesh.path.path.Path)
      * [`Path.__init__()`](trimesh.path.path.html#trimesh.path.path.Path.__init__)
      * [`Path.apply_layer()`](trimesh.path.path.html#trimesh.path.path.Path.apply_layer)
      * [`Path.apply_transform()`](trimesh.path.path.html#trimesh.path.path.Path.apply_transform)
      * [`Path.bounds`](trimesh.path.path.html#trimesh.path.path.Path.bounds)
      * [`Path.centroid`](trimesh.path.path.html#trimesh.path.path.Path.centroid)
      * [`Path.colors`](trimesh.path.path.html#trimesh.path.path.Path.colors)
      * [`Path.convert_units()`](trimesh.path.path.html#trimesh.path.path.Path.convert_units)
      * [`Path.copy()`](trimesh.path.path.html#trimesh.path.path.Path.copy)
      * [`Path.dangling`](trimesh.path.path.html#trimesh.path.path.Path.dangling)
      * [`Path.discrete`](trimesh.path.path.html#trimesh.path.path.Path.discrete)
      * [`Path.entities`](trimesh.path.path.html#trimesh.path.path.Path.entities)
      * [`Path.explode()`](trimesh.path.path.html#trimesh.path.path.Path.explode)
      * [`Path.export()`](trimesh.path.path.html#trimesh.path.path.Path.export)
      * [`Path.extents`](trimesh.path.path.html#trimesh.path.path.Path.extents)
      * [`Path.fill_gaps()`](trimesh.path.path.html#trimesh.path.path.Path.fill_gaps)
      * [`Path.identifier_hash`](trimesh.path.path.html#trimesh.path.path.Path.identifier_hash)
      * [`Path.is_closed`](trimesh.path.path.html#trimesh.path.path.Path.is_closed)
      * [`Path.is_empty`](trimesh.path.path.html#trimesh.path.path.Path.is_empty)
      * [`Path.kdtree`](trimesh.path.path.html#trimesh.path.path.Path.kdtree)
      * [`Path.layers`](trimesh.path.path.html#trimesh.path.path.Path.layers)
      * [`Path.length`](trimesh.path.path.html#trimesh.path.path.Path.length)
      * [`Path.merge_vertices()`](trimesh.path.path.html#trimesh.path.path.Path.merge_vertices)
      * [`Path.paths`](trimesh.path.path.html#trimesh.path.path.Path.paths)
      * [`Path.process()`](trimesh.path.path.html#trimesh.path.path.Path.process)
      * [`Path.referenced_vertices`](trimesh.path.path.html#trimesh.path.path.Path.referenced_vertices)
      * [`Path.remove_duplicate_entities()`](trimesh.path.path.html#trimesh.path.path.Path.remove_duplicate_entities)
      * [`Path.remove_entities()`](trimesh.path.path.html#trimesh.path.path.Path.remove_entities)
      * [`Path.remove_invalid()`](trimesh.path.path.html#trimesh.path.path.Path.remove_invalid)
      * [`Path.remove_unreferenced_vertices()`](trimesh.path.path.html#trimesh.path.path.Path.remove_unreferenced_vertices)
      * [`Path.replace_vertex_references()`](trimesh.path.path.html#trimesh.path.path.Path.replace_vertex_references)
      * [`Path.rezero()`](trimesh.path.path.html#trimesh.path.path.Path.rezero)
      * [`Path.scene()`](trimesh.path.path.html#trimesh.path.path.Path.scene)
      * [`Path.to_dict()`](trimesh.path.path.html#trimesh.path.path.Path.to_dict)
      * [`Path.vertex_graph`](trimesh.path.path.html#trimesh.path.path.Path.vertex_graph)
      * [`Path.vertex_nodes`](trimesh.path.path.html#trimesh.path.path.Path.vertex_nodes)
      * [`Path.vertices`](trimesh.path.path.html#trimesh.path.path.Path.vertices)
    * [`Path2D`](trimesh.path.path.html#trimesh.path.path.Path2D)
      * [`Path2D.apply_obb()`](trimesh.path.path.html#trimesh.path.path.Path2D.apply_obb)
      * [`Path2D.apply_scale()`](trimesh.path.path.html#trimesh.path.path.Path2D.apply_scale)
      * [`Path2D.area`](trimesh.path.path.html#trimesh.path.path.Path2D.area)
      * [`Path2D.body_count`](trimesh.path.path.html#trimesh.path.path.Path2D.body_count)
      * [`Path2D.connected_paths()`](trimesh.path.path.html#trimesh.path.path.Path2D.connected_paths)
      * [`Path2D.convex_hull`](trimesh.path.path.html#trimesh.path.path.Path2D.convex_hull)
      * [`Path2D.enclosure`](trimesh.path.path.html#trimesh.path.path.Path2D.enclosure)
      * [`Path2D.enclosure_directed`](trimesh.path.path.html#trimesh.path.path.Path2D.enclosure_directed)
      * [`Path2D.enclosure_shell`](trimesh.path.path.html#trimesh.path.path.Path2D.enclosure_shell)
      * [`Path2D.extrude()`](trimesh.path.path.html#trimesh.path.path.Path2D.extrude)
      * [`Path2D.identifier`](trimesh.path.path.html#trimesh.path.path.Path2D.identifier)
      * [`Path2D.medial_axis()`](trimesh.path.path.html#trimesh.path.path.Path2D.medial_axis)
      * [`Path2D.obb`](trimesh.path.path.html#trimesh.path.path.Path2D.obb)
      * [`Path2D.path_valid`](trimesh.path.path.html#trimesh.path.path.Path2D.path_valid)
      * [`Path2D.plot_discrete()`](trimesh.path.path.html#trimesh.path.path.Path2D.plot_discrete)
      * [`Path2D.plot_entities()`](trimesh.path.path.html#trimesh.path.path.Path2D.plot_entities)
      * [`Path2D.polygons_closed`](trimesh.path.path.html#trimesh.path.path.Path2D.polygons_closed)
      * [`Path2D.polygons_full`](trimesh.path.path.html#trimesh.path.path.Path2D.polygons_full)
      * [`Path2D.rasterize()`](trimesh.path.path.html#trimesh.path.path.Path2D.rasterize)
      * [`Path2D.root`](trimesh.path.path.html#trimesh.path.path.Path2D.root)
      * [`Path2D.sample()`](trimesh.path.path.html#trimesh.path.path.Path2D.sample)
      * [`Path2D.show()`](trimesh.path.path.html#trimesh.path.path.Path2D.show)
      * [`Path2D.simplify()`](trimesh.path.path.html#trimesh.path.path.Path2D.simplify)
      * [`Path2D.simplify_spline()`](trimesh.path.path.html#trimesh.path.path.Path2D.simplify_spline)
      * [`Path2D.split()`](trimesh.path.path.html#trimesh.path.path.Path2D.split)
      * [`Path2D.to_3D()`](trimesh.path.path.html#trimesh.path.path.Path2D.to_3D)
      * [`Path2D.triangulate()`](trimesh.path.path.html#trimesh.path.path.Path2D.triangulate)
    * [`Path3D`](trimesh.path.path.html#trimesh.path.path.Path3D)
      * [`Path3D.convex_hull`](trimesh.path.path.html#trimesh.path.path.Path3D.convex_hull)
      * [`Path3D.identifier`](trimesh.path.path.html#trimesh.path.path.Path3D.identifier)
      * [`Path3D.show()`](trimesh.path.path.html#trimesh.path.path.Path3D.show)
      * [`Path3D.to_2D()`](trimesh.path.path.html#trimesh.path.path.Path3D.to_2D)
      * [`Path3D.to_planar()`](trimesh.path.path.html#trimesh.path.path.Path3D.to_planar)
  * [trimesh.path.polygons](trimesh.path.polygons.html)
    * [`edges_to_polygons()`](trimesh.path.polygons.html#trimesh.path.polygons.edges_to_polygons)
    * [`enclosure_tree()`](trimesh.path.polygons.html#trimesh.path.polygons.enclosure_tree)
    * [`identifier()`](trimesh.path.polygons.html#trimesh.path.polygons.identifier)
    * [`medial_axis()`](trimesh.path.polygons.html#trimesh.path.polygons.medial_axis)
    * [`paths_to_polygons()`](trimesh.path.polygons.html#trimesh.path.polygons.paths_to_polygons)
    * [`plot()`](trimesh.path.polygons.html#trimesh.path.polygons.plot)
    * [`polygon_bounds()`](trimesh.path.polygons.html#trimesh.path.polygons.polygon_bounds)
    * [`polygon_obb()`](trimesh.path.polygons.html#trimesh.path.polygons.polygon_obb)
    * [`polygon_scale()`](trimesh.path.polygons.html#trimesh.path.polygons.polygon_scale)
    * [`polygons_obb()`](trimesh.path.polygons.html#trimesh.path.polygons.polygons_obb)
    * [`projected()`](trimesh.path.polygons.html#trimesh.path.polygons.projected)
    * [`random_polygon()`](trimesh.path.polygons.html#trimesh.path.polygons.random_polygon)
    * [`repair_invalid()`](trimesh.path.polygons.html#trimesh.path.polygons.repair_invalid)
    * [`resample_boundaries()`](trimesh.path.polygons.html#trimesh.path.polygons.resample_boundaries)
    * [`sample()`](trimesh.path.polygons.html#trimesh.path.polygons.sample)
    * [`second_moments()`](trimesh.path.polygons.html#trimesh.path.polygons.second_moments)
    * [`stack_boundaries()`](trimesh.path.polygons.html#trimesh.path.polygons.stack_boundaries)
    * [`transform_polygon()`](trimesh.path.polygons.html#trimesh.path.polygons.transform_polygon)
  * [trimesh.path.raster](trimesh.path.raster.html)
    * [raster.py](trimesh.path.raster.html#raster-py)
    * [`rasterize()`](trimesh.path.raster.html#trimesh.path.raster.rasterize)
  * [trimesh.path.repair](trimesh.path.repair.html)
    * [repair.py](trimesh.path.repair.html#repair-py)
    * [`fill_gaps()`](trimesh.path.repair.html#trimesh.path.repair.fill_gaps)
  * [trimesh.path.segments](trimesh.path.segments.html)
    * [segments.py](trimesh.path.segments.html#segments-py)
    * [`clean()`](trimesh.path.segments.html#trimesh.path.segments.clean)
    * [`colinear_pairs()`](trimesh.path.segments.html#trimesh.path.segments.colinear_pairs)
    * [`extrude()`](trimesh.path.segments.html#trimesh.path.segments.extrude)
    * [`length()`](trimesh.path.segments.html#trimesh.path.segments.length)
    * [`parameters_to_segments()`](trimesh.path.segments.html#trimesh.path.segments.parameters_to_segments)
    * [`resample()`](trimesh.path.segments.html#trimesh.path.segments.resample)
    * [`segments_to_parameters()`](trimesh.path.segments.html#trimesh.path.segments.segments_to_parameters)
    * [`split()`](trimesh.path.segments.html#trimesh.path.segments.split)
    * [`to_svg()`](trimesh.path.segments.html#trimesh.path.segments.to_svg)
    * [`unique()`](trimesh.path.segments.html#trimesh.path.segments.unique)
  * [trimesh.path.simplify](trimesh.path.simplify.html)
    * [`fit_circle_check()`](trimesh.path.simplify.html#trimesh.path.simplify.fit_circle_check)
    * [`is_circle()`](trimesh.path.simplify.html#trimesh.path.simplify.is_circle)
    * [`merge_colinear()`](trimesh.path.simplify.html#trimesh.path.simplify.merge_colinear)
    * [`points_to_spline_entity()`](trimesh.path.simplify.html#trimesh.path.simplify.points_to_spline_entity)
    * [`resample_spline()`](trimesh.path.simplify.html#trimesh.path.simplify.resample_spline)
    * [`simplify_basic()`](trimesh.path.simplify.html#trimesh.path.simplify.simplify_basic)
    * [`simplify_spline()`](trimesh.path.simplify.html#trimesh.path.simplify.simplify_spline)
  * [trimesh.path.traversal](trimesh.path.traversal.html)
    * [`PathSample`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample)
      * [`PathSample.__init__()`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample.__init__)
      * [`PathSample.sample()`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample.sample)
      * [`PathSample.truncate()`](trimesh.path.traversal.html#trimesh.path.traversal.PathSample.truncate)
    * [`closed_paths()`](trimesh.path.traversal.html#trimesh.path.traversal.closed_paths)
    * [`discretize_path()`](trimesh.path.traversal.html#trimesh.path.traversal.discretize_path)
    * [`resample_path()`](trimesh.path.traversal.html#trimesh.path.traversal.resample_path)
    * [`split()`](trimesh.path.traversal.html#trimesh.path.traversal.split)
    * [`vertex_graph()`](trimesh.path.traversal.html#trimesh.path.traversal.vertex_graph)
    * [`vertex_to_entity_path()`](trimesh.path.traversal.html#trimesh.path.traversal.vertex_to_entity_path)
  * [trimesh.path.util](trimesh.path.util.html)
    * [`concatenate()`](trimesh.path.util.html#trimesh.path.util.concatenate)

## trimesh.path¶

Handle 2D and 3D vector paths such as those contained in an SVG or DXF file.

_class _trimesh.path.Path2D(_entities : ArrayLike | [Iterable](trimesh.typed.html#trimesh.typed.Iterable "collections.abc.Iterable")[[Entity](trimesh.path.entities.html#trimesh.path.entities.Entity "trimesh.path.entities.Entity")] | None = None_, _vertices : ArrayLike | None = None_, _metadata : [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _process : bool = True_, _colors : ArrayLike | None = None_, _vertex_attributes : [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _** kwargs_)¶
    

Bases: [`Path`](trimesh.path.path.html#trimesh.path.path.Path "trimesh.path.path.Path")

Hold multiple vector curves (lines, arcs, splines, etc) in 3D.

apply_obb()¶
    

Transform the current path so that its OBB is axis aligned and OBB center is at the origin.

Returns:
    

**obb** – Homogeneous transformation matrix

Return type:
    

(3, 3) float

apply_scale(_scale_)¶
    

Apply a 2D scale to the current Path2D.

Parameters:
    

**scale** (_float_ _or_ _(__2_ _,__)__float_) – Scale to apply in-place.

_property _area¶
    

Return the area of the polygons interior.

Returns:
    

**area** – Total area of polygons minus interiors

Return type:
    

float

_property _body_count¶
    

Returns a count of the number of unconnected polygons that may contain other curves but aren’t contained themselves.

Returns:
    

**body_count** – Number of unconnected independent polygons.

Return type:
    

int

connected_paths(_path_id_ , _include_self =False_)¶
    

Given an index of self.paths find other paths which overlap with that path.

Parameters:
    

  * **path_id** (_int_) – Index of self.paths

  * **include_self** (_bool_) – Should the result include path_id or not

Returns:
    

**path_ids** – Indexes of self.paths that overlap input path_id

Return type:
    

(n, ) int

_property _convex_hull _: [Path2D](trimesh.path.path.html#trimesh.path.path.Path2D "trimesh.path.path.Path2D")_¶
    

Return a convex hull of the 2D path.

Returns:
    

A convex hull of included vertices from this path.

Return type:
    

hull

_property _enclosure¶
    

Undirected graph object of polygon enclosure.

Returns:
    

**enclosure** – Enclosure graph of self.polygons by index.

Return type:
    

networkx.Graph

_property _enclosure_directed¶
    

Directed graph of polygon enclosure.

Returns:
    

**enclosure_directed** – Directed graph: child nodes are fully contained by their parent node.

Return type:
    

networkx.DiGraph

_property _enclosure_shell¶
    

A dictionary of path indexes which are ‘shell’ paths, and values of ‘hole’ paths.

Returns:
    

**corresponding** – {index of self.paths of shell : [indexes of holes]}

Return type:
    

dict

extrude(_height_ , _** kwargs_)¶
    

Extrude the current 2D path into a 3D mesh.

Parameters:
    

  * **height** (_float_ _,__how far to extrude the profile_)

  * **kwargs** (_passed directly to meshpy.triangle.build:_) – 

triangle.build(mesh_info,
    

verbose=False, refinement_func=None, attributes=False, volume_constraints=True, max_volume=None, allow_boundary_steiner=True, allow_volume_steiner=True, quality_meshing=True, generate_edges=None, generate_faces=False, min_angle=None)

Returns:
    

**mesh**

Return type:
    

trimesh object representing extruded polygon

_property _identifier¶
    

A unique identifier for the path.

Returns:
    

**identifier** – Unique identifier

Return type:
    

(5,) float

medial_axis(_resolution =None_, _clip =None_)¶
    

Find the approximate medial axis based on a voronoi diagram of evenly spaced points on the boundary of the polygon.

Parameters:
    

  * **resolution** (_None_ _or_ _float_) – Distance between each sample on the polygon boundary

  * **clip** (_None_ _, or_ _(__2_ _,__)__float_) – Min, max number of samples

Returns:
    

**medial** – Contains only medial axis of Path

Return type:
    

Path2D object

_property _obb¶
    

Get a transform that centers and aligns the OBB of the referenced vertices with the XY axis.

Returns:
    

**obb** – Homogeneous transformation matrix

Return type:
    

(3, 3) float

_property _path_valid¶
    

returns: **path_valid** – Indexes of self.paths self.polygons_closed
    

which are valid polygons.

Return type:
    

(n,) bool

plot_discrete(_show =False_, _annotations =True_)¶
    

Plot the closed curves of the path.

plot_entities(_show =False_, _annotations =True_, _color =None_)¶
    

Plot the entities of the path with no notion of topology.

Parameters:
    

  * **show** (_bool_) – Open a window immediately or not

  * **annotations** (_bool_) – Call an entities custom plot function.

  * **color** (_str_) – Override entity colors and make them all this color.

_property _polygons_closed _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[_ScalarT]]_¶
    

Cycles in the vertex graph, as shapely.geometry.Polygons. These are polygon objects for every closed circuit, with no notion of whether a polygon is a hole or an area. Every polygon in this list will have an exterior, but NO interiors.

Returns:
    

**polygons_closed**

Return type:
    

(n,) list of shapely.geometry.Polygon objects

_property _polygons_full _: list_¶
    

A list of shapely.geometry.Polygon objects with interiors created by checking which closed polygons enclose which other polygons.

Returns:
    

**full** – Polygons containing interiors

Return type:
    

(len(self.root),) shapely.geometry.Polygon

rasterize(_pitch =None_, _origin =None_, _resolution =None_, _fill =True_, _width =None_, _** kwargs_)¶
    

Rasterize a Path2D object into a boolean image (“mode 1”).

Parameters:
    

  * **pitch** (_float_ _or_ _(__2_ _,__)__float_) – Length(s) in model space of pixel edges

  * **origin** (_(__2_ _,__)__float_) – Origin position in model space

  * **resolution** (_(__2_ _,__)__int_) – Resolution in pixel space

  * **fill** (_bool_) – If True will return closed regions as filled

  * **width** (_int_) – If not None will draw outline this wide (pixels)

Returns:
    

**raster** – Rasterized version of closed regions.

Return type:
    

PIL.Image object, mode 1

_property _root _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]]_¶
    

Which indexes of self.paths/self.polygons_closed are root curves, also known as ‘shell’ or ‘exterior.

Returns:
    

**root** – List of indexes

Return type:
    

(n,) int

sample(_count_ , _** kwargs_)¶
    

Use rejection sampling to generate random points inside a polygon.

Parameters:
    

  * **count** (_int_) – Number of points to return If there are multiple bodies, there will be up to count * bodies points returned

  * **factor** (_float_) – How many points to test per loop IE, count * factor

  * **max_iter** (_int_ _,_) – Maximum number of intersection loops to run, total points sampled is count * factor * max_iter

Returns:
    

**hit** – Random points inside polygon

Return type:
    

(n, 2) float

show(_annotations =True_)¶
    

Plot the current Path2D object using matplotlib.

simplify(_** kwargs_)¶
    

Return a version of the current path with colinear segments merged, and circles entities replacing segmented circular paths.

Returns:
    

**simplified**

Return type:
    

Path2D object

simplify_spline(_smooth =0.0002_, _verbose =False_)¶
    

Convert paths into b-splines.

Parameters:
    

  * **smooth** (_float_) – How much the spline should smooth the curve

  * **verbose** (_bool_) – Print detailed log messages

Returns:
    

**simplified** – Discrete curves replaced with splines

Return type:
    

Path2D

split(_** kwargs_)¶
    

If the current Path2D consists of n ‘root’ curves, split them into a list of n Path2D objects

Returns:
    

**split** – Each connected region and interiors

Return type:
    

(n,) list of Path2D objects

to_3D(_transform =None_)¶
    

Convert 2D path to 3D path on the XY plane.

Parameters:
    

**transform** (_(__4_ _,__4_ _)__float_) – If passed, will transform vertices. If not passed and ‘to_3D’ is in self.metadata that transform will be used.

Returns:
    

**path_3D** – 3D version of current path

Return type:
    

Path3D

triangulate(_** kwargs_)¶
    

Create a region- aware triangulation of the 2D path.

Parameters:
    

****kwargs** (_dict_) – Passed to trimesh.creation.triangulate_polygon

Returns:
    

  * **vertices** (_(n, 2) float_) – 2D vertices of triangulation

  * **faces** (_(n, 3) int_) – Indexes of vertices for triangles

_class _trimesh.path.Path3D(_entities : ArrayLike | [Iterable](trimesh.typed.html#trimesh.typed.Iterable "collections.abc.Iterable")[[Entity](trimesh.path.entities.html#trimesh.path.entities.Entity "trimesh.path.entities.Entity")] | None = None_, _vertices : ArrayLike | None = None_, _metadata : [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _process : bool = True_, _colors : ArrayLike | None = None_, _vertex_attributes : [Mapping](trimesh.typed.html#trimesh.typed.Mapping "collections.abc.Mapping") | None = None_, _** kwargs_)¶
    

Bases: [`Path`](trimesh.path.path.html#trimesh.path.path.Path "trimesh.path.path.Path")

Hold multiple vector curves (lines, arcs, splines, etc) in 3D.

_property _convex_hull¶
    

Return a convex hull of the 3D path.

Returns:
    

**hull** – A mesh of the convex hull of the 3D path.

Return type:
    

[trimesh.Trimesh](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")

_property _identifier _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

Return a simple identifier for the 3D path.

show(_** kwargs_)¶
    

Show the current Path3D object.

to_2D(_to_2D : ArrayLike | None = None_, _normal : ArrayLike | None = None_, _check : bool = True_) → tuple[[Path2D](trimesh.path.path.html#trimesh.path.path.Path2D "trimesh.path.path.Path2D"), ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]]¶
    

Check to see if current vectors are all coplanar.

If they are, return a Path2D and a transform which will transform the 2D representation back into 3 dimensions

Parameters:
    

  * **to_2D** (_(__4_ _,__4_ _)__float_) – Homogeneous transformation matrix to apply, if not passed a plane will be fitted to vertices.

  * **normal** (_(__3_ _,__)__float_ _or_ _None_) – Normal of direction of plane to use.

  * **check** – Raise a ValueError if points aren’t coplanar.

Returns:
    

  * _planar_ – Current path transformed onto plane

  * **to_3D** (_(4, 4) float_) – Homeogenous transformations to move planar back into the original 3D frame.

to_planar(_* args_, _** kwargs_)¶
    

DEPRECATED: replace path.to_planar->`path.to_2D), removal 1/1/2026

---

## trimesh.path.exchange.html

# trimesh.path.exchange¶

  * [trimesh.path.exchange.dxf](trimesh.path.exchange.dxf.html)
    * [`bulge_to_arcs()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.bulge_to_arcs)
    * [`convert_entities()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.convert_entities)
    * [`export_dxf()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.export_dxf)
    * [`get_key()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.get_key)
    * [`load_dxf()`](trimesh.path.exchange.dxf.html#trimesh.path.exchange.dxf.load_dxf)
  * [trimesh.path.exchange.export](trimesh.path.exchange.export.html)
    * [`export_dict()`](trimesh.path.exchange.export.html#trimesh.path.exchange.export.export_dict)
    * [`export_path()`](trimesh.path.exchange.export.html#trimesh.path.exchange.export.export_path)
  * [trimesh.path.exchange.load](trimesh.path.exchange.load.html)
    * [`load_path()`](trimesh.path.exchange.load.html#trimesh.path.exchange.load.load_path)
    * [`path_formats()`](trimesh.path.exchange.load.html#trimesh.path.exchange.load.path_formats)
  * [trimesh.path.exchange.misc](trimesh.path.exchange.misc.html)
    * [`dict_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.dict_to_path)
    * [`edges_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.edges_to_path)
    * [`faces_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.faces_to_path)
    * [`lines_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.lines_to_path)
    * [`linestrings_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.linestrings_to_path)
    * [`polygon_to_path()`](trimesh.path.exchange.misc.html#trimesh.path.exchange.misc.polygon_to_path)
  * [trimesh.path.exchange.svg_io](trimesh.path.exchange.svg_io.html)
    * [`element_transform()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.element_transform)
    * [`export_svg()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.export_svg)
    * [`svg_to_path()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.svg_to_path)
    * [`transform_to_matrices()`](trimesh.path.exchange.svg_io.html#trimesh.path.exchange.svg_io.transform_to_matrices)

---

## trimesh.path.exchange.dxf.html

# trimesh.path.exchange.dxf¶

trimesh.path.exchange.dxf.bulge_to_arcs(_lines_ , _bulge_ , _bulge_idx_ , _is_closed =False_, _metadata =None_)¶
    

Polylines can have “vertex bulge” which means the polyline has an arc tangent to segments, rather than meeting at a vertex.

From Autodesk reference: The bulge is the tangent of one fourth the included angle for an arc segment, made negative if the arc goes clockwise from the start point to the endpoint. A bulge of 0 indicates a straight segment, and a bulge of 1 is a semicircle.

Parameters:
    

  * **lines** (_(__n_ _,__2_ _)__float_) – Polyline vertices in order

  * **bulge** (_(__m_ _,__)__float_) – Vertex bulge value

  * **bulge_idx** (_(__m_ _,__)__float_) – Which index of lines is bulge associated with

  * **is_closed** (_bool_) – Is segment closed

  * **metadata** (_None_ _, or_ _dict_) – Entity metadata to add

Returns:
    

  * **vertices** (_(a, 2) float_) – New vertices for poly-arc

  * **entities** (_(b,) entities.Entity_) – New entities, either line or arc

trimesh.path.exchange.dxf.convert_entities(_blob_ , _blob_raw =None_, _blocks =None_, _return_name =False_)¶
    

Convert a chunk of entities into trimesh entities.

Parameters:
    

  * **blob** (_(__n_ _,__2_ _)__str_) – Blob of entities uppercased

  * **blob_raw** (_(__n_ _,__2_ _)__str_) – Blob of entities not uppercased

  * **blocks** (_None_ _or_ _dict_) – Blocks referenced by INSERT entities

  * **return_name** (_bool_) – If True return the first ‘2’ value

trimesh.path.exchange.dxf.export_dxf(_path_ , _only_layers =None_)¶
    

Export a 2D path object to a DXF file.

Parameters:
    

  * **path** ([_trimesh.path.path.Path2D_](trimesh.path.path.html#trimesh.path.path.Path2D "trimesh.path.path.Path2D")) – Input geometry to export

  * **only_layers** (_None_ _or_ _set_) – If passed only export the layers specified

Returns:
    

**export** – Path formatted as a DXF file

Return type:
    

str

trimesh.path.exchange.dxf.get_key(_blob_ , _field_ , _code_)¶
    

Given a loaded (n, 2) blob and a field name get a value by code.

trimesh.path.exchange.dxf.load_dxf(_file_obj_ , _** kwargs_)¶
    

Load a DXF file to a dictionary containing vertices and entities.

Parameters:
    

**file_obj** (_file_ _or_ _file- like object_ _(__has object.read method_ _)_)

Returns:
    

**result**

Return type:
    

dict, keys are entities, vertices and metadata

---

## trimesh.path.exchange.export.html

# trimesh.path.exchange.export¶

trimesh.path.exchange.export.export_dict(_path_)¶
    

Export a path as a dict of kwargs for the Path constructor.

trimesh.path.exchange.export.export_path(_path_ , _file_type =None_, _file_obj =None_, _** kwargs_)¶
    

Export a Path object to a file- like object, or to a filename

Parameters:
    

  * **file_obj** (_None_ _,__str_ _, or_ _file object_) – A filename string or a file-like object

  * **file_type** (_None_ _or_ _str_) – File type, e.g.: ‘svg’, ‘dxf’

  * **kwargs** (_passed to loader_)

Returns:
    

**exported** – Data exported

Return type:
    

str or bytes

---

## trimesh.path.exchange.load.html

# trimesh.path.exchange.load¶

trimesh.path.exchange.load.load_path(_file_obj_ , _file_type : str | None = None_, _** kwargs_)¶
    

Load a file to a Path file_object.

Parameters:
    

  * **file_obj** – 

Accepts many types:
    
    * Path, Path2D, or Path3D file_objects

    * open file file_object (dxf or svg)

    * file name (dxf or svg)

    * shapely.geometry.Polygon

    * shapely.geometry.MultiLineString

    * dict with kwargs for Path constructor

    * (n, 2, (2|3)) float line segments

  * **file_type** – Type of file is required if file object is passed.

Returns:
    

**path** – Data as a native trimesh Path file_object

Return type:
    

[Path](trimesh.path.path.html#trimesh.path.path.Path "trimesh.path.path.Path"), [Path2D](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D"), Path3D file_object

trimesh.path.exchange.load.path_formats() → set[str]¶
    

Get a list of supported path formats.

Returns:
    

Extensions of loadable formats, i.e. {‘svg’, ‘dxf’}

Return type:
    

loaders

---

## trimesh.path.exchange.misc.html

# trimesh.path.exchange.misc¶

trimesh.path.exchange.misc.dict_to_path(_as_dict_)¶
    

Turn a pure dict into a dict containing entity objects that can be sent directly to a Path constructor.

Parameters:
    

**as_dict** (_dict_) – Has keys: ‘vertices’, ‘entities’

Returns:
    

**kwargs** – Has keys: ‘vertices’, ‘entities’

Return type:
    

dict

trimesh.path.exchange.misc.edges_to_path(_edges : ArrayLike_, _vertices : ArrayLike_, _** kwargs_) → dict¶
    

Given an edge list of indices and associated vertices representing lines, generate kwargs for a Path object.

Parameters:
    

  * **edges** (_(__n_ _,__2_ _)__int_) – Vertex indices of line segments

  * **vertices** (_(__m_ _,__dimension_ _)__float_) – Vertex positions where dimension is 2 or 3

Returns:
    

**kwargs** – Kwargs for Path constructor

Return type:
    

dict

trimesh.path.exchange.misc.faces_to_path(_mesh_ , _face_ids =None_, _** kwargs_)¶
    

Given a mesh and face indices find the outline edges and turn them into a Path3D.

Parameters:
    

  * **mesh** ([_trimesh.Trimesh_](trimesh.html#trimesh.Trimesh "trimesh.Trimesh")) – Triangulated surface in 3D

  * **face_ids** (_(__n_ _,__)__int_) – Indexes referencing mesh.faces

Returns:
    

**kwargs** – Kwargs for Path3D constructor

Return type:
    

dict

trimesh.path.exchange.misc.lines_to_path(_lines : ArrayLike_, _index : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[int64](trimesh.typed.html#trimesh.typed.int64 "numpy.int64")]] | None = None_) → dict¶
    

Turn line segments into argument to be used for a Path2D or Path3D.

Parameters:
    

  * **lines** (_(__n_ _,__2_ _,__dimension_ _) or_ _(__n_ _,__dimension_ _)__float_) – Line segments or connected polyline curve in 2D or 3D

  * **index** (_(__n_ _,__)_[_int64_](trimesh.typed.html#trimesh.typed.int64 "trimesh.typed.int64")) – If passed save an index for each line segment.

Returns:
    

**kwargs** – kwargs for Path constructor

Return type:
    

Dict

trimesh.path.exchange.misc.linestrings_to_path(_multi_) → dict¶
    

Load shapely LineString objects into arguments to create a Path2D or Path3D.

Parameters:
    

**multi** (_shapely.geometry.LineString_ _or_ _MultiLineString_) – Input 2D or 3D geometry

Returns:
    

**kwargs** – Keyword arguments for Path2D or Path3D constructor

Return type:
    

Dict

trimesh.path.exchange.misc.polygon_to_path(_polygon_)¶
    

Load shapely Polygon objects into a trimesh.path.Path2D object

Parameters:
    

**polygon** (_shapely.geometry.Polygon_) – Input geometry

Returns:
    

**kwargs** – Keyword arguments for Path2D constructor

Return type:
    

dict

---

## trimesh.path.exchange.svg_io.html

# trimesh.path.exchange.svg_io¶

trimesh.path.exchange.svg_io.element_transform(_element_ , _max_depth =10_)¶
    

Find a transformation matrix for an XML element.

Parameters:
    

  * **e** (_lxml.etree.Element_) – Element to search upwards from.

  * **max_depth** (_int_) – Maximum depth to search for transforms.

trimesh.path.exchange.svg_io.export_svg(_drawing_ , _return_path =False_, _only_layers =None_, _digits =None_, _** kwargs_)¶
    

Export a Path2D object into an SVG file.

Parameters:
    

  * **drawing** ([_Path2D_](trimesh.path.html#trimesh.path.Path2D "trimesh.path.Path2D")) – Source geometry

  * **return_path** (_bool_) – If True return only path string not wrapped in XML

  * **only_layers** (_None_ _or_ _set_) – If passed only export the specified layers

  * **digits** (_None_ _or_ _int_) – Number of digits for floating point values

Returns:
    

**as_svg** – XML formatted SVG, or path string

Return type:
    

str

trimesh.path.exchange.svg_io.svg_to_path(_file_obj =None_, _file_type =None_, _path_string =None_)¶
    

Load an SVG file into a Path2D object.

Parameters:
    

  * **file_obj** (_open file object_) – Contains SVG data

  * **file_type** (_None_) – Not used

  * **path_string** (_None_ _or_ _str_) – If passed, parse a single path string and ignore file_obj.

Returns:
    

**loaded** – With kwargs for Path2D constructor

Return type:
    

dict

trimesh.path.exchange.svg_io.transform_to_matrices(_transform : str_) → ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]¶
    

Convert an SVG transform string to an array of matrices.

i.e. “rotate(-10 50 100)
    

translate(-36 45.5) skewX(40) scale(1 0.5)”

Parameters:
    

**transform** (_str_) – Contains transformation information in SVG form

Returns:
    

**matrices** – Multiple transformation matrices from input transform string

Return type:
    

(n, 3, 3) float

---

## trimesh.path.arc.html

# trimesh.path.arc¶

_class _trimesh.path.arc.ArcInfo(_radius : float_, _center : numpy.ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], numpy.dtype[[numpy.float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_, _normal : numpy.ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "trimesh.typed.Any"), ...], numpy.dtype[[numpy.float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None = None_, _angles : numpy.ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "trimesh.typed.Any"), ...], numpy.dtype[[numpy.float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None = None_, _span : float | numpy.floating | int | numpy.integer | numpy.unsignedinteger | None = None_)¶
    

Bases: `object`

__init__(_radius : float_, _center : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_, _normal : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None = None_, _angles : ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None = None_, _span : float | floating | int | integer | unsignedinteger | None = None_) → None¶
    

angles _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_ _ = None_¶
    

center _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]]_¶
    

normal _: ndarray[tuple[[Any](trimesh.typed.html#trimesh.typed.Any "typing.Any"), ...], dtype[[float64](trimesh.typed.html#trimesh.typed.float64 "numpy.float64")]] | None_ _ = None_¶
    

radius _: float_¶
    

span _: float | floating | int | integer | unsignedinteger | None_ _ = None_¶
    

trimesh.path.arc.arc_center(_points : ArrayLike_, _return_normal : bool = True_, _return_angle : bool = True_) → ArcInfo¶
    

Given three points on a 2D or 3D arc find the center, radius, normal, and angular span.

Parameters:
    

  * **points** (_(__3_ _,__dimension_ _)__float_) – Points in space, where dimension is either 2 or 3

  * **return_normal** (_bool_) – If True calculate the 3D normal unit vector

  * **return_angle** (_bool_) – If True calculate the start and stop angle and span

Returns:
    

Arc center, radius, and other information.

Return type:
    

info

trimesh.path.arc.discretize_arc(_points_ , _close =False_, _scale =1.0_)¶
    

Returns a version of a three point arc consisting of line segments.

Parameters:
    

  * **points** (_(__3_ _,__d_ _)__float_) – Points on the arc where d in [2,3]

  * **close** (_boolean_) – If True close the arc into a circle

  * **scale** (_float_) – What is the approximate overall drawing scale Used to establish order of magnitude for precision

Returns:
    

**discrete** – Connected points in space

Return type:
    

(m, d) float

trimesh.path.arc.to_threepoint(_center_ , _radius_ , _angles =None_)¶
    

For 2D arcs, given a center and radius convert them to three points on the arc.

Parameters:
    

  * **center** (_(__2_ _,__)__float_) – Center point on the plane

  * **radius** (_float_) – Radius of arc

  * **angles** (_(__2_ _,__)__float_) – Angles in radians for start and end angle if not specified, will default to (0.0, pi)

Returns:
    

**three** – Arc control points

Return type:
    

(3, 2) float