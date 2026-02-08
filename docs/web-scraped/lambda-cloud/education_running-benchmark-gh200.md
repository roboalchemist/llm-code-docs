# Running a PyTorch®-based benchmark on an NVIDIA GH200 instance -

Source: https://docs.lambda.ai/education/running-benchmark-gh200/

---

[on-demand cloud](../../tags/#tag:on-demand-cloud)

# Running a PyTorch®-based benchmark on an NVIDIA GH200 instance

This tutorial describes how to run an NGC-based benchmark on an On-Demand Cloud (ODC) instance backed with the NVIDIA GH200 Grace Hopper Superchip. The tutorial also outlines how to run the benchmark on other ODC instance types to compare performance. The benchmark uses a variety of PyTorch® examples from NVIDIA's [Deep Learning Examples](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch) repository.

## Prerequisites

To run this tutorial successfully, you'll need the following:

- A GitHub account and some familiarity with a Git-based workflow.
- The following tools and libraries installed on the machine or instance you plan to benchmark. These tools and libraries are installed by default on your ODC instances:
  - NVIDIA driver
  - Docker
  - Git
  - nvidia-container-toolkit
  - Python

## Setting up your environment

### Launch your GH200 instance

Begin by launching a GH200 instance:

- In the Lambda Cloud console, navigate to the [SSH keys page](https://cloud.lambda.ai/ssh-keys), click **Add SSH Key**, and then add or generate a SSH key.
- Navigate to the [Instances page](https://cloud.lambda.ai/instances) and click **Launch Instance**.
- Follow the steps in the instance launch wizard.
  - *Instance type:* Select **1x GH200 (96 GB)**.
  - *Region:* Select an available region.
  - *Filesystem:* Don't attach a filesystem.
  - *SSH key:* Use the key you created in step 1.
- Click **Launch instance**.

- Review the EULAs. If you agree to them, click **I agree to the above** to start launching your new instance. Instances can take up to five minutes to fully launch.

### Set the required environment variables

Next, set the environment variables you need to run the benchmark:

- In the Lambda Cloud console, navigate to the [Instances page](https://cloud.lambda.ai/instances), find the row for your instance, and then click **Launch** in the **Cloud IDE** column. JupyterLab opens in a new window.
- In JupyterLab's **Launcher** tab, under **Other**, click **Terminal** to open a new terminal.
- Open your `.bashrc` file for editing:

```bash
nano ~/.bashrc
```
