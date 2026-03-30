# Source: https://docs.flux.ai/reference/polygons-reference.md

# Polygons

Polygons allow you to create custom copper shapes that are tied to specific nets. This reference guide covers the key aspects of working with polygons in your PCB designs.

![](https://uploads.developerhub.io/prod/86Yw/mozs0xharr0q0x1mjrvnwb351rs8ni30x0ek18gitb66hs3qr76ivev1dum5ckfj.jpg)

For step-by-step instructions on creating and editing polygons, see the [Working with Polygons](https://docs.flux.ai/flux/tutorials/working-with-polygons) tutorial.

## Polygon Rules

The following [rules](https://docs.flux.ai/flux/reference/layout-rules-types) can be configured for polygons in the Inspector panel:

| Rule | Description | 
| ---- | ---- | 
| [Polygon Shape](https://docs.flux.ai/flux/reference/layout-rules-types#polygon-shape) | The shape of the polygon, defined using SVG path syntax. | 
| [Connected Layers](https://docs.flux.ai/flux/reference/layout-rules-types#connected-layers) | The copper layers the polygon appears on | 
| [Trace Width](https://docs.flux.ai/flux/reference/layout-rules-types#trace-width) | Determines the minimum feature size for the polygon | 
| [Fill Stitching Density](https://docs.flux.ai/flux/reference/layout-rules-types#fill-stitching-density) | Controls the density of via stitching if applied | 
| [Fill Stitching Offset](https://docs.flux.ai/flux/reference/layout-rules-types#fill-stitching-offset) | Controls the offset of via stitching if applied | 
| [Keep Out](https://docs.flux.ai/flux/reference/layout-rules-types#keep-out) | Prevents copper pour in specified areas | 


## Polygon Hierarchy and Priority

When multiple polygons overlap, Flux uses a size-based priority system to determine which polygon takes precedence:

1. **All polygons take priority over [Copper fills](https://docs.flux.ai/flux/reference/reference-ground-fills)**
2. **Smaller polygons take priority** over larger polygons
3. Polygons of the same net will merge unless they have different properties

This automatic priority system allows you to:

- Create complex copper structures with cutouts by using smaller polygons
- Implement split planes for different power domains
- Design sophisticated RF structures with controlled impedance
- Create thermal relief patterns around component pads