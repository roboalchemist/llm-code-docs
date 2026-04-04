:github_url: hide



# Lightmapper

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [LightmapperRD<class_LightmapperRD>]

Abstract class extended by lightmappers, for use in [LightmapGI<class_LightmapGI>].


## Description

This class should be extended by custom lightmapper classes. Lightmappers can then be used with [LightmapGI<class_LightmapGI>] to provide fast baked global illumination in 3D.

Godot contains a built-in GPU-based lightmapper [LightmapperRD<class_LightmapperRD>] that uses compute shaders, but custom lightmappers can be implemented by C++ modules.

