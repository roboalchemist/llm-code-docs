# Source: https://docs.aws.amazon.com/dlami/latest/devguide/llms.txt

# AWS Deep Learning AMIs Developer Guide

> This guide demonstrates how to launch AWS Deep Learning AMIs, use the installed deep learning frameworks, and run a Jupyter notebook server for deep learning tutorials.

- [Requirements for P6 instances](https://docs.aws.amazon.com/dlami/latest/devguide/p6-support-dlami.html)
- [DLAMI Support Policy](https://docs.aws.amazon.com/dlami/latest/devguide/support-policy.html)
- [Important changes](https://docs.aws.amazon.com/dlami/latest/devguide/important-changes.html)
- [Related information](https://docs.aws.amazon.com/dlami/latest/devguide/resources.html)
- [Deprecated features](https://docs.aws.amazon.com/dlami/latest/devguide/deprecations.html)
- [Document history](https://docs.aws.amazon.com/dlami/latest/devguide/doc-history.html)

## [What is the DLAMI?](https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html)

- [Example use cases](https://docs.aws.amazon.com/dlami/latest/devguide/use-cases.html): The following are examples of some common use cases for AWS Deep Learning AMIs (DLAMI).
- [Features](https://docs.aws.amazon.com/dlami/latest/devguide/features.html): The features of AWS Deep Learning AMIs (DLAMI) include preinstalled deep learning frameworks, GPU software, model servers, and model visualization tools.


## [DLAMI Release Notes](https://docs.aws.amazon.com/dlami/latest/devguide/appendix-ami-release-notes.html)

- [Base AMI with Single CUDA (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-with-single-cuda-ami-amazon-linux-2023.html)
- [Base AMI with Single CUDA (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-with-single-cuda-ami-ubuntu-22-04.html)
- [Base GPU AMI (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-gpu-ami-amazon-linux-2023.html)
- [Base GPU AMI (Ubuntu 24.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-gpu-ami-ubuntu-24-04.html)
- [Base GPU AMI (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-gpu-ami-ubuntu-22-04.html)
- [Base GPU AMI (Amazon Linux 2)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-gpu-ami-amazon-linux-2.html)
- [Base Qualcomm AMI (Amazon Linux 2)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-base-qualcomm-ami-amazon-linux-2.html)

- [ARM64 Base AMI with Single CUDA (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-with-single-cuda-ami-amazon-linux-2023.html)
- [ARM64 Base AMI with Single CUDA (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-with-single-cuda-ami-ubuntu-22-04.html)
- [ARM64 Base GPU AMI (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-gpu-ami-amazon-linux-2023.html)
- [ARM64 Base GPU AMI (Ubuntu 24.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-gpu-ami-ubuntu-24-04.html)
- [ARM64 Base GPU AMI (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-gpu-ami-ubuntu-22-04.html)
- [ARM64 Base GPU AMI (Amazon Linux 2)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-base-gpu-ami-amazon-linux-2.html)

- [GPU PyTorch 2.9 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.9-amazon-linux-2023.html)
- [GPU PyTorch 2.9 (Ubuntu 24.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.9-ubuntu-24-04.html)
- [GPU PyTorch 2.8 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.8-amazon-linux-2023.html)
- [GPU PyTorch 2.8 (Ubuntu 24.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.8-ubuntu-24-04.html)
- [GPU PyTorch 2.7 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.7-amazon-linux-2023.html)
- [GPU PyTorch 2.7 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.7-ubuntu-22-04.html)
- [GPU PyTorch 2.6 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.6-amazon-linux-2023.html)
- [GPU PyTorch 2.6 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.6-ubuntu-22-04.html)

- [ARM64 AMI GPU Pytorch 2.9 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.9-amazon-linux-2023.html)
- [ARM64 AMI GPU Pytorch 2.9 (Ubuntu 24.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.9-ubuntu-24-04.html)
- [ARM64 AMI GPU PyTorch 2.8 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.8-amazon-linux-2023.html)
- [ARM64 AMI GPU PyTorch 2.8 (Ubuntu 24.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.8-ubuntu-24-04.html)
- [ARM64 AMI GPU PyTorch 2.7 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.7-amazon-linux-2023.html)
- [ARM64 AMI GPU PyTorch 2.7 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.7-ubuntu-22-04.html)
- [ARM64 AMI GPU PyTorch 2.6 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.6-amazon-linux-2023.html)
- [ARM64 AMI GPU PyTorch 2.6 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.6-ubuntu-22-04.html)

- [GPU TensorFlow 2.18 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-tensorflow-2.18-amazon-linux-2023.html)
- [GPU TensorFlow 2.18 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-tensorflow-2.18-ubuntu-22-04.html)

- [Multi Framework DLAMI (Amazon Linux 2)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-multiframework-ami-amazon-linux-2.html)


## [Getting started](https://docs.aws.amazon.com/dlami/latest/devguide/getting-started.html)

### [Choosing a DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/choose-dlami.html)

Choose the appropriate AWS Deep Learning AMIs for your use case.

- [CUDA Installations and Framework Bindings](https://docs.aws.amazon.com/dlami/latest/devguide/overview-cuda.html): Select a CUDA installation for your DLAMI.
- [Base](https://docs.aws.amazon.com/dlami/latest/devguide/overview-base.html): Select a base installation for your DLAMI.
- [Conda](https://docs.aws.amazon.com/dlami/latest/devguide/overview-conda.html): Select a Conda DLAMI.
- [Architecture](https://docs.aws.amazon.com/dlami/latest/devguide/overview-architecture.html): Select either an x86-based or Arm64-based architecture for your DLAMI.
- [OS](https://docs.aws.amazon.com/dlami/latest/devguide/overview-os.html): Select an operating system for your DLAMI.

### [Choosing an instance](https://docs.aws.amazon.com/dlami/latest/devguide/instance-select.html)

Choose an instance type for your AWS Deep Learning AMIs.

- [GPU](https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html): Choose a GPU instance for your DLAMI that suits your specific deep learning goals.
- [CPU](https://docs.aws.amazon.com/dlami/latest/devguide/cpu.html): Choose a CPU instance for your DLAMI that suits your specific deep learning goals.
- [Inferentia](https://docs.aws.amazon.com/dlami/latest/devguide/inferentia.html): Choose an AWS Deep Learning AMIs with Inferentia for high-performance inference predictions.
- [Trainium](https://docs.aws.amazon.com/dlami/latest/devguide/trainium.html): Choose an AWS Deep Learning AMIs with Trainium for high-performance inference predictions.
- [Using DLAMIs with Image Builder](https://docs.aws.amazon.com/dlami/latest/devguide/using-dlami-with-image-builder.html): Learn how to use AWS Deep Learning AMIs with EC2 Image Builder.


## [Setting up](https://docs.aws.amazon.com/dlami/latest/devguide/setup.html)

- [Finding a DLAMI ID](https://docs.aws.amazon.com/dlami/latest/devguide/find-dlami-id.html): Learn how to find the ID of the DLAMI of your choice.
- [Launching an instance](https://docs.aws.amazon.com/dlami/latest/devguide/launch.html): Learn how to launch a DLAMI instance using the Amazon EC2 console or the AWS CLI.
- [Connecting to an instance](https://docs.aws.amazon.com/dlami/latest/devguide/setup-connect.html): Learn how to connect to a DLAMI instance after you launch it.

### [Setting up Jupyter](https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter.html)

Set up a Jupyter Notebook server to run deep learning tutorials on a DLAMI instance.

- [Securing server](https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter-secure.html): Learn how to secure your Jupyter Notebook server on a DLAMI instance using a custom password and SSL encryption.
- [Starting server](https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter-start-server.html): Learn how to start your Jupyter Notebook server on a DLAMI instance using an SSL certificate.
- [Connecting client](https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter-connect.html): After you start the Jupyter Notebook server on your DLAMI instance, configure your Windows, macOS, or Linux client to connect to the server.
- [Logging in](https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter-login.html): After you connect your client to the Jupyter Notebook server on your DLAMI instance, you can log in to the server.
- [Cleaning up](https://docs.aws.amazon.com/dlami/latest/devguide/setup-cleanup.html): Learn how to stop or terminate your DLAMI instance on Amazon EC2 when you're done using it.


## [Using a DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/using.html)

- [Conda DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-conda.html): Run through some Conda environments and test the frameworks.
- [Base DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-base.html): How to use the Deep Learning Base AMI.
- [Jupyter Notebooks](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-jupyter.html): Tutorials and examples ship with each of the deep learning projects' source and in most cases they will run on any DLAMI.

### [Tutorials](https://docs.aws.amazon.com/dlami/latest/devguide/tutorials.html)

DLAMI tutorials.

### [Activating Frameworks](https://docs.aws.amazon.com/dlami/latest/devguide/activating.html)

How to activate and test the different frameworks on a DLAMI.

- [PyTorch](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-pytorch.html)
- [TensorFlow 2](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-tensorflow-2.html): Learn how to use TensorFlow 2 with the Deep Learning AMI with Conda.

### [Elastic Fabric Adapter](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-efa.html)

An Elastic Fabric Adapter (EFA) is a network device that you can attach to your DLAMI instance to accelerate High Performance Computing (HPC) applications.

- [Launching a AWS Deep Learning AMIs Instance](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-efa-launching.html): The latest Base DLAMI is ready to use with EFA and comes with the required drivers, kernel modules, libfabric, openmpi and the NCCL OFI plugin for GPU instances.
- [Using EFA](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-efa-using.html): The following section describes how to use EFA to run multi-node applications on the AWS Deep Learning AMIs.

### [GPU Monitoring and Optimization](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu.html)

How to manage and optimize the GPUs on your DLAMI.

### [Monitoring](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu-monitoring.html)

Tools for monitoring the GPUs in your DLAMI.

- [CloudWatch](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu-monitoring-gpumon.html): A GPU monitoring utility that integrates with CloudWatch.

### [Optimization](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu-opt.html)

Optimization tools to improve GPU performance.

- [Preprocessing](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu-opt-preprocessing.html): Preprocessing tools to improve GPU utilization.
- [Training](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu-opt-training.html): Tips for mixed-precision training.

### [AWS Inferentia](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia.html)

AWS InferentiaÂ is a custom machine learning chip designed by AWS that you can use for high-performance inference predictions.Â In order to use the chip, set up an Amazon Elastic Compute Cloud instance and use the AWS Neuron software development kit (SDK) to invoke the Inferentia chip.

- [Launching DLAMI with Neuron](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-launching.html): Launch a DLAMI instance with AWS Neuron.

### [Using DLAMI with AWS Neuron](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-using.html)

A typical workflow with the AWS Neuron SDK is to compile a previously trained machine learning model on a compilation server.

- [TensorFlow and AWS Neuron Compiler](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-tf-neuron.html): This tutorial shows how to use the AWS Neuron compiler to compile the Keras ResNet-50 model and export it as a saved model in SavedModel format.
- [Using AWS Neuron TensorFlow Serving](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-tf-neuron-serving.html): This tutorial shows how to construct a graph and add an AWS Neuron compilation step before exporting the saved model to use with TensorFlow Serving.
- [Using MXNet-Neuron and the AWS Neuron Compiler](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-mxnet-neuron.html): The MXNet-Neuron compilation API provides a method to compile a model graph that you can run on an AWS Inferentia device.
- [Using MXNet-Neuron Model Serving](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-mxnet-neuron-serving.html): Use a pre-trained MXNet model for real-time classification with AWS Neuron.
- [Using PyTorch-Neuron and the AWS Neuron Compiler](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-pytorch-neuron.html): The PyTorch-Neuron compilation API provides a method to compile a model graph that you can run on an AWS Inferentia device.

### [ARM64 DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-arm64.html)

The AWS Deep Learning AMIs supports images on Arm64 processor-based GPUs.

- [Use a ARM64 GPU PyTorch DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-arm64-pytorch.html): Get started with the Arm64 processor-based GPU AWS Deep Learning AMIs, optimized for PyTorch.
- [Inference](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inference.html): How to run inference on your DLAMI.

### [Model Serving](https://docs.aws.amazon.com/dlami/latest/devguide/model-serving.html)

How to serve models on a DLAMI.

- [TensorFlow Serving](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-tfserving.html): TensorFlow Serving is a flexible, high-performance serving system for machine learning models.
- [TorchServe](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-torchserve.html): TorchServe is a flexible tool for serving deep learning models that have been exported from PyTorch.


## [Upgrading Your DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/upgrading.html)

- [DLAMI Upgrade](https://docs.aws.amazon.com/dlami/latest/devguide/upgrading-dlami.html): Learn how to upgrade the DLAMI that you use to a newer version by using Amazon EBS.
- [Software Updates](https://docs.aws.amazon.com/dlami/latest/devguide/updating-software.html): Tips on upgrading your AWS Deep Learning AMIs framework or software.
- [Release Notifications](https://docs.aws.amazon.com/dlami/latest/devguide/release-notifications.html): Receive notifications for DLAMI releases


## [Security](https://docs.aws.amazon.com/dlami/latest/devguide/security.html)

- [Data protection](https://docs.aws.amazon.com/dlami/latest/devguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Deep Learning AMIs.
- [Identity and access management](https://docs.aws.amazon.com/dlami/latest/devguide/security-iam.html): How to authenticate requests and manage access to your DLAMI resources.
- [Compliance validation](https://docs.aws.amazon.com/dlami/latest/devguide/dlami-compliance.html): Learn which AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/dlami/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Deep Learning AMIs features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/dlami/latest/devguide/infrastructure-security.html): Learn how AWS Deep Learning AMIs isolates service traffic.

### [Monitoring](https://docs.aws.amazon.com/dlami/latest/devguide/monitoring.html)

Learn how to configure GPU monitoring tools and usage tracking settings for your DLAMI instance.

- [Usage tracking](https://docs.aws.amazon.com/dlami/latest/devguide/monitoring-opt-out.html): Add an Amazon EC2 tag to your DLAMI instance to opt out of usage tracking.


## [DLAMI Support Policy Table](https://docs.aws.amazon.com/dlami/latest/devguide/dlami-support-policy-table.html)

- [Base GPU AMI (Ubuntu 20.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-base-gpu-ami-ubuntu-20.04.html)

- [GPU PyTorch 2.5 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.5-ubuntu-22-04.html)
- [GPU PyTorch 2.5 (Amazon Linux 2023)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-pytorch-2.5-amazon-linux-2023.html)
- [ARM64 AMI GPU PyTorch 2.5 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-gpu-pytorch-2.5-ubuntu-22-04.html)
- [GPU PyTorch 2.4 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-ami-gpu-pytorch-2.4-ubuntu-22-04.html): For help getting started, see .
- [ARM64 AMI GPU PyTorch 2.4 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-arm64-ami-gpu-pytorch-2.4-ubuntu-22-04.html): For help getting started, see .

- [GPU TensorFlow 2.17 (Ubuntu 22.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-x86-gpu-tensorflow-2.17-ubuntu-22-04.html)
- [GPU TensorFlow 2.16 (Amazon Linux 2)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-ami-gpu-tensorflow-2.16-amazon-linux-2.html): For help getting started, see .
- [GPU TensorFlow 2.16 (Ubuntu 20.04)](https://docs.aws.amazon.com/dlami/latest/devguide/aws-deep-learning-ami-gpu-tensorflow-2.16-ubuntu-20-04.html): For help getting started, see .
