# Nearest¶

An example showing nearest point queries, sampling the volume of box primitives generated from the oriented bounds and using PointCloud objects for visualization.
    
    
    import numpy as np
    
    import trimesh
    
    
    
    # load a large- ish PLY model with colors
    mesh = trimesh.load("../models/cycloidal.ply")
    
    
    
    # we can sample the volume of Box primitives
    points = mesh.bounding_box_oriented.sample_volume(count=10)
    
    
    
    # find the closest point on the mesh to each random point
    (closest_points, distances, triangle_id) = mesh.nearest.on_surface(points)
    # distance from point to surface of meshdistances
    
    
    
    # create a PointCloud object out of each (n,3) list of points
    cloud_original = trimesh.points.PointCloud(points)
    cloud_close = trimesh.points.PointCloud(closest_points)
    
    # create a unique color for each point
    cloud_colors = np.array([trimesh.visual.random_color() for i in points])
    
    # set the colors on the random point and its nearest point to be the same
    cloud_original.vertices_color = cloud_colors
    cloud_close.vertices_color = cloud_colors
    
    # create a scene containing the mesh and two sets of points
    scene = trimesh.Scene([mesh, cloud_original, cloud_close])
    
    # show the scene we are using
    scene.show()