# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/batch-processing/batch-processing-pricing.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/batch-processing/batch-processing-pricing.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/batch-processing/batch-processing-pricing.md

# Source: https://docs.roboflow.com/deploy/batch-processing/batch-processing-pricing.md

# Batch Processing Pricing

The table below describes the cost for processing data using [Batch Processing](https://docs.roboflow.com/deploy/batch-processing). For credit pricing, please see [roboflow.com/pricing](https://roboflow.com/pricing).

| Workflow Description                                                            | Dataset Size                    | Machine Type | Charge                                             |
| ------------------------------------------------------------------------------- | ------------------------------- | ------------ | -------------------------------------------------- |
| Single Model - YOLOv8 Nano `(image size = 640)` - Object Detection              | 100k images                     | GPU          | 0.04 credit / 1k images                            |
| Single Model - YOLOv8 Nano `(image size = 1280)`- Object Detection              | 100k images                     | GPU          | 0.06 credit / 1k images                            |
| Single Model - YOLOv8 Medium `(image size = 640)` - Object Detection            | 100k images                     | GPU          | 0.06 credit / 1k images                            |
| Single Model - YOLOv8 Medium `(image size = 1280)` - Object Detection           | 100k images                     | GPU          | 0.1 credit / 1k images                             |
| Single Model - YOLOv8 Large `(image size = 640)` - Object Detection             | 100k images                     | GPU          | 0.08 credit / 1k images                            |
| Single Model - YOLOv8 Large `(image size = 1280)` - Object Detection            | 100k images                     | GPU          | 0.18 credit / 1k images                            |
| Single Model - Roboflow Instant - Object Detection                              | 30k images                      | GPU          | 0.33 credit / 1k images                            |
| Single Model - Florence-2 - Object Detection + Region Captioning                | 30k images                      | GPU          | 0.5 credit / 1k images                             |
| Two stage - YoloV8 Nano + crop + YoloV8 Nano `(image size = 640)` - OD          | 10k images                      | GPU          | 0.25 credit / 1k images                            |
| Two stage - YoloV8 Nano + crop + YoloV8 Large `(image size = 640)` - OD + OD    | 10k images                      | GPU          | 0.30 credit / 1k images                            |
| Two stage - YoloV8 Nano + crop + CLIP `(image size = 640)` - OD + Embeddings    | 10k images                      | GPU          | 0.25 credit / 1k images                            |
| Two stage - YoloV8 Nano + crop + Classifier `(image size = 640)` - OD + CLS     | 10k images                      | GPU          | 0.20 credit / 1k images                            |
| Two stage - YoloV8 Nano + crop + SAM 2 `(image size = 640)` - OD + Segmentation | 10k images                      | GPU          | 0.40 credit / 1k images                            |
| Single Model - YOLOv8 Nano `(image size = 640)` - Object Detection              | 4 videos, each 1h @ 30 fps 480p | GPU          | 1 credit / video hour, 0.01 credit / 1k frames     |
| Single Model - YOLOv8 Nano `(image size = 640)` - Object Detection + tracking   | 32 videos, each 1m @ 10 fps HD  | CPU          | 1.8 credit / video hour, 0.05 credit / 1k frames   |
| Two stage - YoloV8 Nano + crop + Classifier `(image size = 640)` - OD + CLS     | 2 videos, each 1h @ 30 fps 480p | GPU          | 4.6 credits / video hour, 0.046 credit / 1k frames |
