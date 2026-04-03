:github_url: hide



# LightmapperRD

**Inherits:** [Lightmapper<class_Lightmapper>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

The built-in GPU-based lightmapper for use with [LightmapGI<class_LightmapGI>].


## Description

LightmapperRD ("RD" stands for [RenderingDevice<class_RenderingDevice>]) is the built-in GPU-based lightmapper for use with [LightmapGI<class_LightmapGI>]. On most dedicated GPUs, it can bake lightmaps much faster than most CPU-based lightmappers. LightmapperRD uses compute shaders to bake lightmaps, so it does not require CUDA or OpenCL libraries to be installed to be usable.

\ **Note:** This lightmapper requires the GPU to support the [RenderingDevice<class_RenderingDevice>] backend (Forward+ and Mobile renderers). When using the Compatibility renderer, baking will use a temporary [RenderingDevice<class_RenderingDevice>]. Support for [RenderingDevice<class_RenderingDevice>] is not required to *render* lightmaps that were already baked beforehand.

