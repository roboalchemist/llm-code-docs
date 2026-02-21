# Quick Start¶

A simple example showing various properties of Trimesh objects.

    import numpy as np

    import trimesh

    # load a file by name or from a buffer
    mesh = trimesh.load_mesh("../models/featuretype.STL")
    # to keep the raw data intact, disable any automatic processing
    # mesh = trimesh.load_mesh('../models/featuretype.STL', process=False)

    # is the current mesh watertight?
    mesh.is_watertight

    True

    # what's the euler number for the mesh?
    mesh.euler_number

    -16

    # the convex hull is another Trimesh object that is available as a property
    # lets compare the volume of our mesh with the volume of its convex hull
    np.divide(mesh.volume, mesh.convex_hull.volume)

    np.float64(0.7792407744466933)

    # since the mesh is watertight, it means there is a
    # volumetric center of mass which we can set as the origin for our mesh
    mesh.vertices -= mesh.center_mass

    # what's the moment of inertia for the mesh?
    mesh.moment_inertia

    array([[ 6.93059627e+00, -1.43877613e-03, -1.49424850e-01],
           [-1.43877613e-03,  2.19191960e+01, -1.25194047e-04],
           [-1.49424850e-01, -1.25194047e-04,  2.62344872e+01]])

    # if there are multiple bodies in the mesh we can split the mesh by
    # connected components of face adjacency
    # since this example mesh is a single watertight body we get a list of one mesh
    mesh.split()

    [<trimesh.Trimesh(vertices.shape=(1722, 3), faces.shape=(3476, 3))>]

    # preview mesh in a pyglet window from a terminal, or inline in a notebook
    mesh.show()

    # facets are groups of coplanar adjacent faces
    # set each facet to a random color
    # colors are 8 bit RGBA by default (n,4) np.uint8
    for facet in mesh.facets:
        mesh.visual.face_colors[facet] = trimesh.visual.random_color()

    # transform method can be passed a (4,4) matrix and will cleanly apply the transform
    mesh.apply_transform(trimesh.transformations.random_rotation_matrix())

    <trimesh.Trimesh(vertices.shape=(1722, 3), faces.shape=(3476, 3))>

    # an axis aligned bounding box is available
    mesh.bounding_box.primitive.extents

    TrackedArray([3.78807526, 5.03348884, 4.78503672])

    # a minimum volume oriented bounding box is available
    mesh.bounding_box_oriented.primitive.extents

    TrackedArray([1.375, 2.5  , 5.   ])

    mesh.bounding_box_oriented.primitive.transform

    TrackedArray([[-0.67424373, -0.68281158, -0.28136052, -0.09861276],
                  [-0.4509702 ,  0.68237687, -0.57531529, -0.06892324],
                  [ 0.58482585, -0.26101752, -0.768016  ,  0.07754459],
                  [ 0.        ,  0.        ,  0.        ,  1.        ]])

    # the bounding box is a trimesh.primitives.Box object, which subclasses
    # Trimesh and lazily evaluates to fill in vertices and faces when requested
    mesh.bounding_box_oriented.show()

    # bounding spheres and bounding cylinders of meshes are also
    # available, and will be the minimum volume version of each
    # except in certain degenerate cases, where they will be no worse
    # than a least squares fit version of the primitive.
    (
        mesh.bounding_box_oriented.volume,
        mesh.bounding_cylinder.volume,
        mesh.bounding_sphere.volume,
    )

    (17.18750000000002, np.float64(28.506929187287298), 95.8943899752207)
