# Trimesh Documentation

Trimesh is a lightweight Python library for loading and working with triangular meshes.
The goal of the library is to provide a simple interface to common tasks.

## Documentation Contents

- **index.md** - Main documentation index
- **install.md** - Installation guide
- **quick_start.md** - Quick start tutorial
- **formats.md** - Supported geometry formats
- **examples.md** - Example code
- **api_reference.md** - Complete API reference

## Key Features

- Load mesh files (STL, OBJ, PLY, DAE, glTF, etc.)
- Convert between 3D geometry formats
- Compute mesh properties (volume, surface area, center of mass)
- Check mesh validity
- Perform mesh operations (merge, split, slice)
- Ray-mesh intersections
- Voxelization
- Convex hulls
- Support for point clouds

## Usage

```python
import trimesh

# Load a mesh
mesh = trimesh.load('model.stl')

# Get basic properties
print(mesh.volume)
print(mesh.bounds)
print(mesh.center_mass)

# Apply transformations
mesh.apply_scale(2.0)
mesh.apply_translation([1, 2, 3])

# Save the mesh
mesh.export('output.ply')
```

For more information, see the official documentation at https://trimesh.org/
