# Ray¶

An example showing simple ray-mesh queries.
    
    
    import numpy as np
    
    import trimesh
    
    
    
    # test on a sphere primitive
    mesh = trimesh.creation.icosphere()
    
    
    
    # create some rays
    ray_origins = np.array([[0, 0, -3], [2, 2, -3]])
    ray_directions = np.array([[0, 0, 1], [0, 0, 1]])
    
    
    
    # check out the docstring for intersects_location queries
    mesh.ray.intersects_location.__doc__
    
    
    
    'nReturn the location of where a ray hits a surface.nnParametersn----------nray_origins : (n, 3) floatn  Origins of raysnray_directions : (n, 3) floatn  Direction (vector) of raysnnReturnsn---------nlocations : (m) sequence of (p, 3) floatn  Intersection pointsnindex_ray : (m,) intn  Indexes of raynindex_tri : (m,) intn  Indexes of mesh.facesn'
    
    
    # run the mesh- ray query
    locations, index_ray, index_tri = mesh.ray.intersects_location(
        ray_origins=ray_origins, ray_directions=ray_directions
    )
    
    
    
    # the rays hit the mesh at coordinateslocations
    
    
    
    # the rays with index_ray hit the triangles stored at mesh.faces[index_tri]len(index_ray)
    
    
    
    # stack rays into line segments for visualization as Path3D
    ray_visualize = trimesh.load_path(
        np.hstack((ray_origins, ray_origins + ray_directions * 5.0)).reshape(-1, 2, 3)
    )
    
    
    
    # unmerge so viewer doesn't smooth
    mesh.unmerge_vertices()
    # make mesh white- ish
    mesh.visual.face_colors = [255, 255, 255, 255]
    mesh.visual.face_colors[index_tri] = [255, 0, 0, 255]
    
    
    
    # create a visualization scene with rays, hits, and mesh
    scene = trimesh.Scene([mesh, ray_visualize])
    
    
    
    # show the visualization
    scene.show()