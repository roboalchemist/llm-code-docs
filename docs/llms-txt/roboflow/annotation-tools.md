# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/annotation-tools.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/annotation-tools.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/annotation-tools.md

# Source: https://docs.roboflow.com/annotate/annotation-tools.md

# Roboflow Annotate

Roboflow Annotate provides a fast, robust interface through which you can annotate images.

You can annotate images using bounding boxes and polygons.

### Annotation Methods

You can annotate images by:

* Manually drawing bounding boxes/polygons/
* Using [AI Labeling](https://docs.roboflow.com/annotate/ai-labeling)&#x20;

### Bounding Boxes vs. Polygons vs. Masks

With the option between drawing bounding boxes and polygons, you may wonder: what is the difference between these two annotation types?

Bounding boxes -- boxes drawn around an object of interest in an image -- are easier to draw than polygons, thus taking up less annotation time. Polygons, on the other hand, are more precise, and may lead to a slight increase in performance.

For segmentation tasks, you need to use polygons or masks, since you are training your model to segment specific items from an image with precision. Masks provide the highest fidelity for complex boundaries when you need pixel-perfect control.&#x20;

This section of the Roboflow documentation shows how to annotate images using each of the above methods.

### Project Types and Annotations

Different model types require specific annotation formats. The table below shows which annotations are compatible with each project type. When\
possible, Roboflow automatically converts annotations to the required format (e.g., polygons to bounding boxes for object detection).

| Project Type          | Supported Annotations          |
| --------------------- | ------------------------------ |
| Object Detection      | Bounding Box, Polygon, Mask\*  |
| Instance Segmentation | Polygon, Mask                  |
| Semantic Segmentation | Polygon, Mask                  |
| Keypoint Detection    | Keypoints (skeleton)           |
| Classification        | None (image-level labels only) |

*\*Polygons and masks are converted to bounding boxes automatically.*\ <br>

**Key Differences**

* Instance vs Semantic Segmentation: Instance distinguishes individual objects; Semantic treats all objects of the same class as one entity.
* Single vs Multi-Label Classification: Single assigns one class per image; Multi-Label allows multiple classes per image.
