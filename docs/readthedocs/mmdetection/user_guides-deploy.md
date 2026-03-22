# Model Deployment

The deployment of OpenMMLab codebases, including MMDetection, MMPretrain and so on are supported by MMDeploy [https://github.com/open-mmlab/mmdeploy].
The latest deployment guide for MMDetection can be found from here [https://mmdeploy.readthedocs.io/en/dev-1.x/04-supported-codebases/mmdet.html].

This tutorial is organized as follows:

- 

Installation

- 

Convert model

- 

Model specification

- 

Model inference

  - 

Backend model inference

  - 

SDK model inference

- 

Supported models

## Installation

Please follow the guide [https://mmdetection.readthedocs.io/en/latest/get_started.html] to install mmdet. And then install mmdeploy from source by following this [https://mmdeploy.readthedocs.io/en/1.x/get_started.html#installation] guide.

Note

If you install mmdeploy prebuilt package, please also clone its repository by ‘git clone https://github.com/open-mmlab/mmdeploy.git –depth=1’ to get the deployment config files.