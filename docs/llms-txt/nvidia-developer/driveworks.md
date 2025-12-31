# Source: https://developer.nvidia.com/drive/driveworks.md

# NVIDIA DriveWorks SDK

The NVIDIA® DriveWorks Software Development Kit (SDK) provides a suite of accelerated algorithms and versatile tools to bootstrap software development for Autonomous Vehicles.

  
  

## DriveWorks at a Glance

The DriveWorks SDK contains a comprehensive set of modules, tools and samples that solve typical tasks and workloads for AV development. Developers can use DriveWorks for their applications and leverage the computing power of NVIDIA DRIVE AGX™ SoCs.

 ![DriveWorks acceleration libraries and tools](https://developer.nvidia.com/downloads/drive/images/driveworks.png)
  
  

## Featured Modules
  

### Sensor Abstraction Layer

NVIDIA DriveWorks provides a Sensor Abstraction Layer that supports capturing of data from various sources. It is designed to provide the following features:

- Abstraction between physical sensor models and software applications
- A unified, compact sensor interface definition
- Raw sensor serialization for recording
- Virtual sensors to enable replay
- Abstraction over DriveOS core components: NVIDIA CUDA®, NvMedia, and NvStreams

 ![DriveWorks comes with Compute Graph Framework and STM Scheduler](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/revamp-driveworks-sensor-abstraction-layer-630x354.jpg)

* * *

### Image Processing

 ![DriveWorks Image Processing modules](https://developer-blogs.nvidia.com/wp-content/uploads/2019/08/featuretracking-624x404.png)

The Image Processing Library provides structures and algorithms to efficiently process image data. It features the following algorithms:

- Image Preprocessing: Rectification, Color Correction
- Image Features: Extraction and Feature History
- Image Filtering: Recursive Gaussian filter, Box filter, and Convolution filter
- Area Tracking: Templates, 2D Bounding Boxes
- Stereo: Rectification and Disparity Estimation

* * *

### Point Cloud Processing

The DriveWorks Point Cloud Processing Library is built specifically for Point Cloud data as transmitted by LiDAR sensors. It provides the following GPU-accelerated algorithms:

- Accumulation of a Point Clouds over time
- Stitching to combine Point Clouds
- Range Image (Depth Map) creation
- (Ground) Plane extraction via RANSAC algorithm
- Point Cloud filter by attribute

 ![DriveWorks provides image and point cloud processing modules](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/revamp-driveworks-image-point-cloud-processing-630x354.jpg)

* * *

### Dynamic Calibration

 ![Static calibration tools and self-calibration](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/revamp-driveworks-calibration-630x354.jpg)

The Calibration Module supports Dynamic Calibration for Camera, Radar, LiDAR and IMU sensors that are compatible with the DriveWorks Sensor Abstraction Layer.

  

Dynamic Calibration is a process where sensor parameters are re-estimated at runtime based on sensor measurements and vehicle motion. This process compensates for the effects of environmental changes or mechanical stress—such as changes in road gradient, tire pressure, or vehicle loading—which can affect the extrinsic parameters (position and orientation) of sensors during a vehicle&#39;s operation.

* * *

### Egomotion

The Egomotion module uses a motion model to track and predict the vehicle’s pose based on sensor inputs.

  

It supports two types of motion models: an odometry-only model and, if an IMU is available, a model based on IMU and odometry. During run-time, the module takes measurements as input and internally updates the current estimation of the vehicle pose. The module can be queried for vehicle motion between any two points in time.

 ![DriveWorks Egomotion module uses a motion model to track and predict a vehicle’s pose](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/revamp-driveworks-egomotion-630x354.jpg)

* * *

## Resources

[![DRIVE SDK Downloads](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/m48-download-96px-grn.svg)](https://developer.nvidia.com/drive/downloads)

[Downloads](https://developer.nvidia.com/drive/downloads)

[![Developer Forums](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/m48-question-support-96px-grn.svg) ](https://forums.developer.nvidia.com/drive-agx)

[Forums](https://forums.developer.nvidia.com/drive-agx)

[![Developer Blog](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/m48-communication-news-flash-share-96px-grn.svg)](https://developer.nvidia.com/blog/tag/nvidia-drive/)

[Blog](https://developer.nvidia.com/blog/tag/nvidia-drive/)

[![NVIDIA Webinars](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/drive/images/m48-announcement-megaphone-96px-grn.svg)](https://developer.nvidia.com/drive/training)

[Webinars](https://developer.nvidia.com/drive/training)

Peek under the hood to experience NVIDIA’s latest autonomous driving innovations via DRIVE Labs and DRIVE Dispatch.

  
[View DRIVE Videos](https://www.nvidia.com/en-us/self-driving-cars/drive-videos/)

