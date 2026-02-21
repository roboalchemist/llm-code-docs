# Manifold3D Documentation

This directory contains documentation for [Manifold3D](https://github.com/elalish/manifold), a geometry processing library for 3D manifold meshes.

## Contents

- **WASM Developer Guide**: JavaScript/TypeScript API documentation for the WebAssembly version
- **ManifoldCAD User Guide**: User guide for the ManifoldCAD web application
- **Using Manifold**: Tutorial on using the Manifold library
- **Manifold Examples**: Code examples and usage patterns
- **Manifold API Reference**: Complete API reference
- **Manifold Class**: Detailed documentation of the Manifold class

## Resources

- Official Website: https://manifoldcad.org
- GitHub Repository: https://github.com/elalish/manifold
- PyPI Package: https://pypi.org/project/manifold3d/
- Algorithm Documentation: https://github.com/elalish/manifold/wiki/Manifold-Library
- Blog Posts: https://elalish.blogspot.com/search/label/Manifold

## Features

Manifold is a geometry library dedicated to creating and operating on manifold triangle meshes:

- **Guaranteed manifold output**: Reliable, robust geometry processing
- **Boolean operations**: Mesh Boolean (union, difference, intersection) with guaranteed manifoldness
- **Multiple language bindings**: C++, Python, JavaScript/TypeScript, Java, C#, Julia, OCaml, Swift, and more
- **High performance**: Extensive use of parallelization for efficient processing
- **Vertex properties**: Support for arbitrary vertex properties and material mapping
- **3D formats**: Support for 3MF, glTF, OBJ, and other formats

## Primary Goals

1. **Reliability**: Guaranteed manifold output without caveats or edge cases
2. **Performance**: Efficient algorithms with parallelization and pipelining

## Installation

### Python

```bash
pip install manifold3d
```

### JavaScript/TypeScript

```bash
npm install manifold-3d
```

### C++

Via vcpkg:

```bash
vcpkg install manifold
```

## Quick Start - Python

```python
import manifold3d

# Create a cube
cube = manifold3d.Manifold.cube([1, 1, 1])

# Create a sphere
sphere = manifold3d.Manifold.sphere(radius=0.5)

# Boolean operations
result = cube + sphere  # union
result = cube - sphere  # difference
result = cube & sphere  # intersection

# Export to file
result.export("output.3mf")
```

## About

Manifold was created by Emmett Lalish and is now maintained by the community. The project is used in many CAD tools, 3D modeling applications, and geometry processing pipelines, including OpenSCAD, Blender, Godot Engine, and many others.

---

Documentation generated from official sources at https://manifoldcad.org
