# Albumentations Documentation

Source: https://albumentations.ai/llms-full.txt

---

# Albumentations

> Albumentations is the fastest and most feature-rich Python library for image augmentation.
> Used by 50,000+ ML practitioners and integrated into major frameworks (PyTorch, TensorFlow, Keras).
> MIT-licensed, open source, actively maintained by the Albumentations Team.

## Key pages

- [Documentation](https://albumentations.ai/docs): Full documentation
- [API Reference](https://albumentations.ai/docs/api-reference): All transforms
- [Transforms & Targets](https://albumentations.ai/docs/reference/supported-targets-by-transform): Which transforms support images, masks, bboxes, keypoints, 3D
- [Benchmarks](https://albumentations.ai/docs/benchmarks): Performance comparisons
- [Release Notes](https://albumentations.ai/docs/releases): Version history and changelogs
- [Blog](https://albumentations.ai/blog): Tutorials and release notes
- [GitHub](https://github.com/albumentations-team/albumentations): Source code
- [PyPI](https://pypi.org/project/albumentations/): Package on PyPI

## Documentation

### [Installation](https://albumentations.ai/docs/1-introduction/installation)
title: "Installation | Albumentations",

### [Getting Started with Albumentations](https://albumentations.ai/docs/1-introduction)
title: "Getting Started with Albumentations | Albumentations",

### [What Is Image Augmentation?](https://albumentations.ai/docs/1-introduction/what-are-image-augmentations)
title: "What Is Image Augmentation? | Albumentations",

### [Core Concepts in Albumentations](https://albumentations.ai/docs/2-core-concepts)
title: "Core Concepts in Albumentations | Albumentations",

### [Pipelines: Composing Multiple Augmentations](https://albumentations.ai/docs/2-core-concepts/pipelines)
title: "Pipelines: Composing Multiple Augmentations | Albumentations",

### [Setting Probabilities for Transforms in Augmentation Pipelines](https://albumentations.ai/docs/2-core-concepts/probabilities)
title: "Setting Probabilities for Transforms in Augmentation Pipelines | Albumentations",

### [Working with Multiple Data Targets](https://albumentations.ai/docs/2-core-concepts/targets)
title: "Working with Multiple Data Targets | Albumentations",

### [Transforms: The Building Blocks of Augmentation](https://albumentations.ai/docs/2-core-concepts/transforms)
title: "Transforms: The Building Blocks of Augmentation | Albumentations",

### [Bounding Box Augmentation for Object Detection](https://albumentations.ai/docs/3-basic-usage/bounding-boxes-augmentations)
title: "Bounding Box Augmentation for Object Detection | Albumentations",

### [Choosing Augmentations for Model Generalization](https://albumentations.ai/docs/3-basic-usage/choosing-augmentations)
title: "Choosing Augmentations for Model Generalization | Albumentations",

### [Image Classification with Albumentations](https://albumentations.ai/docs/3-basic-usage/image-classification)
title: "Image Classification with Albumentations | Albumentations",

### [Keypoints augmentation](https://albumentations.ai/docs/3-basic-usage/keypoint-augmentations)
title: "Keypoints augmentation | Albumentations",

### [Oriented Bounding Boxes (OBB)](https://albumentations.ai/docs/3-basic-usage/oriented-bounding-boxes)
type: "article",

### [Basic Usage Guides](https://albumentations.ai/docs/3-basic-usage)
title: "Basic Usage Guides | Albumentations",

### [Optimizing Augmentation Pipelines for Speed](https://albumentations.ai/docs/3-basic-usage/performance-tuning)
title: "Optimizing Augmentation Pipelines for Speed | Albumentations",

### [Semantic Segmentation with Albumentations](https://albumentations.ai/docs/3-basic-usage/semantic-segmentation)
title: "Semantic Segmentation with Albumentations | Albumentations",

### [Video Augmentation with Albumentations](https://albumentations.ai/docs/3-basic-usage/video-augmentation)
title: "Video Augmentation with Albumentations | Albumentations",

### [Introduction to 3D Medical Image Augmentation](https://albumentations.ai/docs/3-basic-usage/volumetric-augmentation)
title: "Introduction to 3D Medical Image Augmentation | Albumentations",

### [Using Additional Targets in Albumentations](https://albumentations.ai/docs/4-advanced-guides/additional-targets)
title: "Using Additional Targets in Albumentations | Albumentations",

### [Creating Custom Albumentations Transforms](https://albumentations.ai/docs/4-advanced-guides/creating-custom-transforms)
title: "Creating Custom Albumentations Transforms | Albumentations",

### [Advanced Guides](https://albumentations.ai/docs/4-advanced-guides)
title: "Advanced Guides | Albumentations",

### [Reproducibility in Albumentations](https://albumentations.ai/docs/4-advanced-guides/reproducibility)
title: "Reproducibility in Albumentations | Albumentations",

### [Serialization of Augmentation Pipelines](https://albumentations.ai/docs/4-advanced-guides/serialization)
title: "Serialization of Augmentation Pipelines | Albumentations",

### [Test Time Augmentation (TTA)](https://albumentations.ai/docs/4-advanced-guides/test-time-augmentation)
type: "article",

### [Benchmarks](https://albumentations.ai/docs/benchmarks)
];

### [Coding Guidelines](https://albumentations.ai/docs/contributing/coding-guidelines)
title: "Coding Guidelines | Albumentations",

### [Setting Up Your Development Environment](https://albumentations.ai/docs/contributing/environment-setup)
title: "Setting Up Your Development Environment | Albumentations",

### [Contributing to AlbumentationsX](https://albumentations.ai/docs/contributing)
title: "Contributing to AlbumentationsX | Albumentations",

### [Defining a simple augmentation pipeline for image augmentation](https://albumentations.ai/docs/examples/example)
title: "Defining a simple augmentation pipeline for image augmentation | Albumentations",

### [Using Albumentations to augment bounding boxes for object detection tasks](https://albumentations.ai/docs/examples/example-bboxes)
title: "Using Albumentations to augment bounding boxes for object detection tasks | Albumentations",

### [How to use Albumentations for detection tasks if you need to keep all bounding boxes](https://albumentations.ai/docs/examples/example-bboxes2)
title: "How to use Albumentations for detection tasks if you need to keep all bounding boxes | Albumentations",

### [Load the image from the disk](https://albumentations.ai/docs/examples/example-chromatic-aberration)
title: "Load the image from the disk | Albumentations",

### [D4 transform](https://albumentations.ai/docs/examples/example-d4)
title: "D4 transform | Albumentations",

### [Morphological Transform](https://albumentations.ai/docs/examples/example-documents)
title: "Morphological Transform | Albumentations",

### [Domain adaptation transforms](https://albumentations.ai/docs/examples/example-domain-adaptation)
title: "Domain adaptation transforms | Albumentations",

### [RandomGridShuffle](https://albumentations.ai/docs/examples/example-gridshuffle)
title: "RandomGridShuffle | Albumentations",

### [Example on how load and save from Hugging Face Hub](https://albumentations.ai/docs/examples/example-hfhub)
title: "Example on how load and save from Hugging Face Hub | Albumentations",

### [Using Albumentations for a semantic segmentation task](https://albumentations.ai/docs/examples/example-kaggle-salt)
title: "Using Albumentations for a semantic segmentation task | Albumentations",

### [Using Albumentations to augment keypoints](https://albumentations.ai/docs/examples/example-keypoints)
title: "Using Albumentations to augment keypoints | Albumentations",

### [Mosaic Transform Example](https://albumentations.ai/docs/examples/example-mosaic)
title: "Mosaic Transform Example | Albumentations",

### [Applying the same augmentation with the same parameters to multiple images, masks, bounding boxes, or keypoints](https://albumentations.ai/docs/examples/example-multi-target)
title: "Applying the same augmentation with the same parameters to multiple images, masks, bounding boxes, or keypoints | Albumentations",

### [OBB Augmentation with Affine Transform: Boats Example](https://albumentations.ai/docs/examples/example-obb-affine-boats)
title: "OBB Augmentation with Affine Transform: Boats Example | Albumentations",

### [Overlay Elements](https://albumentations.ai/docs/examples/example-overlayelements)
title: "Overlay Elements | Albumentations",

### [Example on how to write on top of images](https://albumentations.ai/docs/examples/example-textimage)
title: "Example on how to write on top of images | Albumentations",

### [Custom Albumentations augmentations and Ultralytics as the project's dependency](https://albumentations.ai/docs/examples/example-ultralytics)
title: "Custom Albumentations augmentations and Ultralytics as the project's dependency | Albumentations",

### [Weather augmentations in Albumentations](https://albumentations.ai/docs/examples/example-weather-transforms)
title: "Weather augmentations in Albumentations | Albumentations",

### [example-xymasking](https://albumentations.ai/docs/examples/example-xymasking)
title: "example_xymasking | Albumentations",

### [Face Landmark Detection with AlbumentationsX: Keypoint Label Swapping](https://albumentations.ai/docs/examples/face-landmarks-tutorial)
title: "Face Landmark Detection with AlbumentationsX: Keypoint Label Swapping | Albumentations",

### [Keras + Albumentations: Cats vs Dogs Classification](https://albumentations.ai/docs/examples/keras-cats-dogs-classification)
title: "Keras + Albumentations: Cats vs Dogs Classification | Albumentations",

### [Semantic Segmentation with Pretrained U-Net in Keras + Albumentations](https://albumentations.ai/docs/examples/keras-pretrained-segmentation)
title: "Semantic Segmentation with Pretrained U-Net in Keras + Albumentations | Albumentations",

### [Migrating from torchvision to Albumentations](https://albumentations.ai/docs/examples/migrating-from-torchvision-to-albumentations)
title: "Migrating from torchvision to Albumentations | Albumentations",

### [PyTorch and Albumentations for image classification](https://albumentations.ai/docs/examples/pytorch-classification)
title: "PyTorch and Albumentations for image classification | Albumentations",

### [PyTorch and Albumentations for semantic segmentation](https://albumentations.ai/docs/examples/pytorch-semantic-segmentation)
title: "PyTorch and Albumentations for semantic segmentation | Albumentations",

### [Debugging an augmentation pipeline with ReplayCompose](https://albumentations.ai/docs/examples/replay)
title: "Debugging an augmentation pipeline with ReplayCompose | Albumentations",

### [How to save and load parameters of an augmentation pipeline](https://albumentations.ai/docs/examples/serialization)
title: "How to save and load parameters of an augmentation pipeline | Albumentations",

### [Showcase. Cool augmentation examples on diverse set of images from various real-world tasks.](https://albumentations.ai/docs/examples/showcase)
title: "Showcase. Cool augmentation examples on diverse set of images from various real-world tasks. | Albumentations",

### [Frequently Asked Questions](https://albumentations.ai/docs/faq)
title: "Frequently Asked Questions | Albumentations",

### [Albumentations License Guide](https://albumentations.ai/docs/license)
title: "Albumentations License Guide | Albumentations",

### [Welcome to Albumentations Documentation!](https://albumentations.ai/docs)
title: "Welcome to Albumentations Documentation! | Albumentations",

### [Transform Library Comparison Guide](https://albumentations.ai/docs/torchvision-kornia2albumentations)
title: "Transform Library Comparison Guide | Albumentations",

## Blog

### [The Label Consistency Problem in Keypoint Augmentation](https://albumentations.ai/blog/2025/04-label-consistency-in-keypoint-augmentation)
When you flip a face horizontally, the left eye becomes the right eye - but your model doesn't know that. Learn how AlbumentationsX's label_mapping feature automatically swaps and reorders keypoint labels during augmentation, reducing landmark detection error by 33%.

### [Input Normalization: What We Know, What We Don't, and Why It Works Anyway](https://albumentations.ai/blog/2025/03-the-mystery-of-input-normalization)
A deep dive into input normalization: the solid mathematics for simple cases, the empirical evidence for complex networks, and the fascinating gap between what we can prove and what actually works.

### [The Art and Science of Dithering: How We Taught Computers to Lie About Colors (And Why That's Beautiful)](https://albumentations.ai/blog/2025/02-the-art-and-science-of-dithering)
From newspaper halftones to modern pixel art masterpieces, discover the fascinating world of dithering - a technique that creates the impossible illusion of millions of colors using only a handful. A journey through time, mathematics, and the art of beautiful deception.

### [AlbumentationsX: A Fork with Dual Licensing](https://albumentations.ai/blog/2025/01-albumentationsx-dual-licensing)
AlbumentationsX is a fork of the Albumentations library with dual licensing (AGPL/Commercial). Learn why the change was made and how it affects open-source and commercial users.

## Release Notes

### [Albumentations 2.0.20](https://albumentations.ai/docs/releases/2.0.20)
Release notes for Albumentations 2.0.20 (2026-03-01)

### [Albumentations 2.0.19](https://albumentations.ai/docs/releases/2.0.19)
Release notes for Albumentations 2.0.19 (2026-02-28)

### [\ud83d\udee0 Albumentations 2.0.18 Release Notes](https://albumentations.ai/docs/releases/2.0.18)
Release notes for \ud83d\udee0 Albumentations 2.0.18 Release Notes (2026-02-23)

### [\ud83d\udee0 Albumentations 2.0.17 Release Notes](https://albumentations.ai/docs/releases/2.0.17)
Release notes for \ud83d\udee0 Albumentations 2.0.17 Release Notes (2026-02-15)

### [\ud83d\udee0 Albumentations 2.0.16 Release Notes](https://albumentations.ai/docs/releases/2.0.16)
Release notes for \ud83d\udee0 Albumentations 2.0.16 Release Notes (2026-01-30)

### [\ud83d\udee0 Albumentations 2.0.15 Release Notes](https://albumentations.ai/docs/releases/2.0.15)
Release notes for \ud83d\udee0 Albumentations 2.0.15 Release Notes (2026-01-28)

### [\ud83d\udee0 Albumentations 2.0.14 Release Notes](https://albumentations.ai/docs/releases/2.0.14)
Release notes for \ud83d\udee0 Albumentations 2.0.14 Release Notes (2026-01-14)

### [\ud83d\udee0 Albumentations 2.0.13 Release Notes](https://albumentations.ai/docs/releases/2.0.13)
Release notes for \ud83d\udee0 Albumentations 2.0.13 Release Notes (2025-11-15)

### [\ud83d\udee0 Albumentations 2.0.12 Release Notes](https://albumentations.ai/docs/releases/2.0.12)
Release notes for \ud83d\udee0 Albumentations 2.0.12 Release Notes (2025-10-08)

### [\ud83d\udee0 Albumentations 2.0.11 Release Notes](https://albumentations.ai/docs/releases/2.0.11)
Release notes for \ud83d\udee0 Albumentations 2.0.11 Release Notes (2025-09-14)

### [\ud83d\udee0 Albumentations 2.0.10 Release Notes](https://albumentations.ai/docs/releases/2.0.10)
Release notes for \ud83d\udee0 Albumentations 2.0.10 Release Notes (2025-08-22)

### [\ud83d\udee0 Albumentations 2.0.9 Release Notes](https://albumentations.ai/docs/releases/2.0.9)
Release notes for \ud83d\udee0 Albumentations 2.0.9 Release Notes (2025-06-25)

## API Reference

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/blur/functional)
API reference for albumentations.augmentations.blur.functional

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/blur/transforms)
API reference for albumentations.augmentations.blur.transforms

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/crops/functional)
API reference for albumentations.augmentations.crops.functional

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/crops/transforms)
API reference for albumentations.augmentations.crops.transforms

### [channel_dropout](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/channel_dropout)
API reference for albumentations.augmentations.dropout.channel_dropout

### [coarse_dropout](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/coarse_dropout)
API reference for albumentations.augmentations.dropout.coarse_dropout

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/functional)
API reference for albumentations.augmentations.dropout.functional

### [grid_dropout](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/grid_dropout)
API reference for albumentations.augmentations.dropout.grid_dropout

### [grid_mask](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/grid_mask)
API reference for albumentations.augmentations.dropout.grid_mask

### [mask_dropout](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/mask_dropout)
API reference for albumentations.augmentations.dropout.mask_dropout

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/transforms)
API reference for albumentations.augmentations.dropout.transforms

### [xy_masking](https://albumentations.ai/docs/api-reference/albumentations/augmentations/dropout/xy_masking)
API reference for albumentations.augmentations.dropout.xy_masking

### [distortion](https://albumentations.ai/docs/api-reference/albumentations/augmentations/geometric/distortion)
API reference for albumentations.augmentations.geometric.distortion

### [flip](https://albumentations.ai/docs/api-reference/albumentations/augmentations/geometric/flip)
API reference for albumentations.augmentations.geometric.flip

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/geometric/functional)
API reference for albumentations.augmentations.geometric.functional

### [pad](https://albumentations.ai/docs/api-reference/albumentations/augmentations/geometric/pad)
API reference for albumentations.augmentations.geometric.pad

### [resize](https://albumentations.ai/docs/api-reference/albumentations/augmentations/geometric/resize)
API reference for albumentations.augmentations.geometric.resize

### [rotate](https://albumentations.ai/docs/api-reference/albumentations/augmentations/geometric/rotate)
API reference for albumentations.augmentations.geometric.rotate

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/geometric/transforms)
API reference for albumentations.augmentations.geometric.transforms

### [domain_adaptation](https://albumentations.ai/docs/api-reference/albumentations/augmentations/mixing/domain_adaptation)
API reference for albumentations.augmentations.mixing.domain_adaptation

### [domain_adaptation_functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/mixing/domain_adaptation_functional)
API reference for albumentations.augmentations.mixing.domain_adaptation_functional

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/mixing/functional)
API reference for albumentations.augmentations.mixing.functional

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/mixing/transforms)
API reference for albumentations.augmentations.mixing.transforms

### [lambda_transform](https://albumentations.ai/docs/api-reference/albumentations/augmentations/other/lambda_transform)
API reference for albumentations.augmentations.other.lambda_transform

### [type_transform](https://albumentations.ai/docs/api-reference/albumentations/augmentations/other/type_transform)
API reference for albumentations.augmentations.other.type_transform

### [dithering_functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/pixel/dithering_functional)
API reference for albumentations.augmentations.pixel.dithering_functional

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/pixel/functional)
API reference for albumentations.augmentations.pixel.functional

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/pixel/transforms)
API reference for albumentations.augmentations.pixel.transforms

### [transform](https://albumentations.ai/docs/api-reference/albumentations/augmentations/spectrogram/transform)
API reference for albumentations.augmentations.spectrogram.transform

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/text/functional)
API reference for albumentations.augmentations.text.functional

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/text/transforms)
API reference for albumentations.augmentations.text.transforms

### [functional](https://albumentations.ai/docs/api-reference/albumentations/augmentations/transforms3d/functional)
API reference for albumentations.augmentations.transforms3d.functional

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/augmentations/transforms3d/transforms)
API reference for albumentations.augmentations.transforms3d.transforms

### [utils](https://albumentations.ai/docs/api-reference/albumentations/augmentations/utils)
API reference for albumentations.augmentations.utils

### [bbox_utils](https://albumentations.ai/docs/api-reference/albumentations/core/bbox_utils)
API reference for albumentations.core.bbox_utils

### [cache_utils](https://albumentations.ai/docs/api-reference/albumentations/core/cache_utils)
API reference for albumentations.core.cache_utils

### [composition](https://albumentations.ai/docs/api-reference/albumentations/core/composition)
API reference for albumentations.core.composition

### [hub_mixin](https://albumentations.ai/docs/api-reference/albumentations/core/hub_mixin)
API reference for albumentations.core.hub_mixin

### [keypoints_utils](https://albumentations.ai/docs/api-reference/albumentations/core/keypoints_utils)
API reference for albumentations.core.keypoints_utils

### [label_manager](https://albumentations.ai/docs/api-reference/albumentations/core/label_manager)
API reference for albumentations.core.label_manager

### [pydantic](https://albumentations.ai/docs/api-reference/albumentations/core/pydantic)
API reference for albumentations.core.pydantic

### [serialization](https://albumentations.ai/docs/api-reference/albumentations/core/serialization)
API reference for albumentations.core.serialization

### [transforms_interface](https://albumentations.ai/docs/api-reference/albumentations/core/transforms_interface)
API reference for albumentations.core.transforms_interface

### [type_definitions](https://albumentations.ai/docs/api-reference/albumentations/core/type_definitions)
API reference for albumentations.core.type_definitions

### [utils](https://albumentations.ai/docs/api-reference/albumentations/core/utils)
API reference for albumentations.core.utils

### [validation](https://albumentations.ai/docs/api-reference/albumentations/core/validation)
API reference for albumentations.core.validation

### [transforms](https://albumentations.ai/docs/api-reference/albumentations/pytorch/transforms)
API reference for albumentations.pytorch.transforms

