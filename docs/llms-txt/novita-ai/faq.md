# Source: https://novita.ai/docs/guides/faq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQ

Here are some frequently asked questions about Novita AI. Before contacting our support team, please check the FAQs below to help you quickly find solutions.

## <Icon icon="microchip" /> GPU Instance

### 1. How to check the price of the GPU instances?

You can check the price of GPU instances and their configurations (container disk, volume disk, network volume, etc.) on the <a href="https://novita.ai/gpu-instance/pricing" target="_blank">Pricing Page</a>.

### 2. When does the billing for GPU instance start?

Billing starts when the instance status changes to "**Pulling**" status.

### 3. Introduction of container disk, volume disk, and network volume.

* **Container Disk**
  * Does not support dynamic expansion, can only specify capacity when creating an instance;
  * Mount directory: `/` (cannot be customized);
  * Data will be saved when saving the image;
  * Supports **60GB** free quota, charges will apply for the excess part, for details refer to: [Billing Instructions](/guides/gpu-instance-pricing)

* **Volume Disk**
  * Supports dynamic expansion;
  * Default mount directory: `/workspace` (customizable);
  * Data will **not** be saved when saving the image;
  * Read and write speed is the same as the container disk;
  * Volume Disk capacity requires additional charges, for details refer to: [Billing Instructions](/guides/gpu-instance-pricing).

* **Network Volume**
  * Supports dynamic expansion;
  * Default mount directory: `/network` (customizable);
  * Network volume has an independent lifecycle, unrelated to the instance, even if the instance is deleted, the network volume data still exists;
  * Overall read and write speed is slower than the container disk or volume disk (depending on specific usage);
  * Network volume capacity requires additional charges, for details refer to: [Billing Instructions](/guides/gpu-instance-pricing)

### 4. Why can't the instance be restarted after it stops?

After the instance stops, the resources belonging to the instance may have been preempted. In this case, it is recommended to first [save the image](/guides/gpu-instance-save-image) based on the target instance, and then create a new instance based on the saved image before.

<Warning>
  After saving the instance image, the data on the container disk will be saved with the image, but the data on the volume disk will not. It is recommended to use the [network volume](/guides/gpu-instance-quickstart-manage-network-volume) for data with high persistence requirements.
</Warning>

### 5. How to handle abnormal instance status?

First, try to troubleshoot the problem through the "System Logs" and "Instance Logs" of the instance. If the problem cannot be resolved, you can <a href="https://discord.gg/YyPRAzwp7P" target="_blank">contact us</a>.

<Frame>
  <img src="https://cf-images.novitai.com/docs/v2/gpu_instance_faq_logs.png/docs" height="150" />
</Frame>

### 6. No instance specifications with a specified CUDA version.

CUDA versions are backward compatible. For example, if your service relies on CUDA version 12.1, you can choose an instance specification with a CUDA version greater than or equal to 12.1.

### 7. What is the maximum CUDA version supported by the platform?

You can check the allowed CUDA versions in the "Filter" module at the bottom right corner of the <a href="https://novita.ai/gpu-instance/console/explore" target="_blank">Explore</a>.

<Frame>
  <img width="250" src="https://cf-images.novitai.com/docs/v2/gpu_instance_faq_filter_cuda.png/docs" />
</Frame>

### 8. How to diagnose the "Save Image" failure?

First, try to troubleshoot the problem through the logs of the <a href="https://novita.ai/gpu-instance/console/jobs" target="_blank">"Save Image"</a> task. If you are saving the image to a private repository address, please check whether your <a href="https://novita.ai/gpu-instance/console/settings" target="_blank">Container Registry Auth Configuration</a> is correct. If the problem cannot be resolved, you can <a href="https://discord.gg/YyPRAzwp7P" target="_blank">contact us</a>.

<Frame>
  <img src="https://cf-images.novitai.com/docs/v2/gpu_instance_faq_jobs_logs.png/docs" height="220" />
</Frame>

### 9. Can dedicated IP be supported?

Yes. Currently, this capability is not open to the public. If you have such requirements, please <a href="https://discord.gg/YyPRAzwp7P" target="_blank">contact us</a>.

### 10. How to check the GPU usage of the instance?

Due to the PID isolation of Docker containers, the `nvidia-smi` command cannot be used to view the process. You can install the `py3nvml` library and use the shell command to check the GPU usage:

```bash  theme={"system"}
# Install the py3nvml library.
$ pip install py3nvml
# Check the GPU usage.
$ py3smi
Fri Sep 20 12:17:39 2024
+-----------------------------------------------------------------------------+
| NVIDIA-SMI                        Driver Version: 550.54.14                 |
+---------------------------------+---------------------+---------------------+
| GPU Fan  Temp Perf Pwr:Usage/Cap|        Memory-Usage | GPU-Util Compute M. |
+=================================+=====================+=====================+
|   5 35%   28C    8   11W / 450W |   353MiB / 24564MiB |       0%    Default |
+---------------------------------+---------------------+---------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
| GPU        Owner      PID      Uptime  Process Name                   Usage |
+=============================================================================+
+-----------------------------------------------------------------------------+
```

## <Icon icon="credit-card" /> Payments

### 1. How can I avoid top-up failures?

Top-up failures are generally caused by two main reasons:

* **Rejection from the card issuer.** This may occur for the following reasons. Please check or contact your card issuer for details:
  * The corresponding payment channel is not activated.
  * The credit card has expired or been frozen.
  * The credit card balance is insufficient.
  * The card number is incorrect.
  * The security code is incorrect.

* **Risk control measures from the payment channel.** Please check and make any necessary adjustments:
  * The device ID is associated with a high number of cards.
  * The number of cards declined using this email address is very high.
  * The time since this card was first seen on the Stripe network with this device ID is very short.
  * The authorization rate associated with this email address is very low.
  * The name on the email address does not match the name on the card.


Built with [Mintlify](https://mintlify.com).