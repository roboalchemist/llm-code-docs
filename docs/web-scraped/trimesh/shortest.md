# Shortest¶

Given a mesh and two vertex indices find the shortest path between the two vertices while only traveling along edges of the mesh using a distance-weighted graph search.

    import networkx as nx

    import trimesh

    # test on a sphere mesh
    mesh = trimesh.primitives.Sphere()

    # edges without duplication
    edges = mesh.edges_unique

    # the actual length of each unique edge
    length = mesh.edges_unique_length

    # create the graph with edge attributes for length
    g = nx.Graph()
    for edge, L in zip(edges, length):
        g.add_edge(*edge, length=L)

    # arbitrary indices of mesh.vertices to test with
    start = 0
    end = int(len(mesh.vertices) / 2.0)

    # run the shortest path query using length for edge weight
    path = nx.shortest_path(g, source=start, target=end, weight="length")

    # VISUALIZE RESULT
    # make the sphere white
    mesh.visual.face_colors = [255, 255, 255, 255]
    # Path3D with the path between the points
    path_visual = trimesh.load_path(mesh.vertices[path])

    # create a scene with the mesh, path, and points
    scene = trimesh.Scene([path_visual, mesh])

    scene.show()
