# Source: https://docs.roboflow.com/changelog/explore-by-month/february-2026/mask-area-measurement-workflow-block.md

# Mask Area Measurement Workflow Block

The new Mask Area Measurement block improves the experience when calculating the size of detected objects within a Workflow pipeline. For instance segmentation predictions, it computes the precise pixel area by counting non-zero mask pixels and properly handling holes. For standard object detection, it computes the area using bounding box dimensions (width × height).

By connecting the block to an object or segmentation model, you can apply a calibration value to convert pixel areas into real-world units (such as cm² or mm²). This block integrates with upstream perspective correction or camera calibration blocks, and downstream filtering blocks, enabling automated size-based filtering and quality control checks.&#x20;

[Learn more about using the Mask Area Measurement block](https://inference.roboflow.com/workflows/blocks/mask_area_measurement/)
