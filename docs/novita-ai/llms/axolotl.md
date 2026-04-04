# Source: https://novita.ai/docs/guides/axolotl.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Axolotl on Novita AI

> Discover how to fine-tune large language models (LLMs) effortlessly with Axolotl on Novita AI.

Axolotl offers a robust, flexible framework for training LLMs using advanced techniques, supporting various model architectures and training strategies. Ideal for researchers and developers, Axolotl combined with Novita AI’s powerful, hardware-free infrastructure streamlines workflows, removing local hardware constraints.

This guide provides a step-by-step process to deploy and run Axolotl on Novita AI, unlocking the full potential of your AI model training projects.

## How to Use Axolotl:main-latest on Novita AI

Step 1: Access [**the GPU Instance Console**](https://novita.ai/gpus)

* Click `Get Started` to access the GPU Instance console.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step1-AccesstheGPUInstanceConsole.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=28625df2e2e6f1232c8107762cfc6ed6" alt="Step1 Accessthe GPU Instance Console Pn" width="3840" height="1941" data-path="images/Step1-AccesstheGPUInstanceConsole.png" />
</Frame>

Step 2: Choose a Template and GPU Type

* Browse various official templates and GPU card options.
* Select [**the Axolotl:main-latest template**](https://novita.ai/gpus-console?templateId=311).
* Click `Deploy` under the 4090 GPU card to proceed to the instance creation page.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step2-ChooseaTemplateandGPUType.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=3e15b2cbd4b915cd6c6df292fca60e29" alt="Step2 Choosea Templateand GPU Type Pn" width="3841" height="1412" data-path="images/Step2-ChooseaTemplateandGPUType.png" />
</Frame>

Step 3: Adjust Disk and Configuration Parameters

* In the `Disk` section, adjust the size of the system disk and local disk.
* In the `Configuration` section, modify settings such as the image, startup commands, ports, and environment variables.
* Check the box for Start Jupyter Notebook to launch Jupyter.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step3-AdjustDiskandConfigurationParameters.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=5f7ad58a188a14c676e26db9b05ba2d8" alt="Step3 Adjust Diskand Configuration Parameters Pn" width="3841" height="1905" data-path="images/Step3-AdjustDiskandConfigurationParameters.png" />
</Frame>

Step 4: Confirm Configuration and Deploy

* Review the instance configuration and costs on the confirmation page.
* Click `Deploy` to start the deployment process.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step4-ConfirmConfigurationandDeploy.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=d7cc24bc299612b7f5e94a7f9578ebf5" alt="Step4 Confirm Configurationand Deploy Pn" width="3841" height="1905" data-path="images/Step4-ConfirmConfigurationandDeploy.png" />
</Frame>

Step 5: Wait for Deployment to Complete

* Wait for the instance to finish deploying.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step5-WaitforDeploymenttoComplete.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=d1bde3687d206d330aa7ae8bd07356cf" alt="Step5 Waitfor Deploymentto Complete Pn" width="1434" height="1102" data-path="images/Step5-WaitforDeploymenttoComplete.png" />
</Frame>

Step 6: Manage and Monitor Instances

* Once deployment is complete, the system will redirect you to the `Instance Management` page.
* Locate your newly created instance, which will initially show a Pulling status (indicating the image is being downloaded).
* Click the small arrow on the right side of the instance to view details.
* Monitor the image pull progress. Once complete, the instance will transition to Running status.
* Click `Logs` to view deployment logs.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step6-ManageandMonitorInstances.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=ea8a23135307454deb057dfb51f32652" alt="Step6 Manageand Monitor Instances Pn" width="3832" height="712" data-path="images/Step6-ManageandMonitorInstances.png" />
</Frame>

Step 7: Check Instance Logs

* Go to the `Instance Logs` tab to check if the service is starting.
* Wait for the service to finish initializing.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step7-CheckInstanceLogs.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=5aece56043a7a85239b9c168b15b442f" alt="Step7 Check Instance Logs Pn" width="1280" height="816" data-path="images/Step7-CheckInstanceLogs.png" />
</Frame>

Step 8: Connect to Jupyter Lab

* Close the logs page.
* Click `Connect` to open the connection information page.
* Locate the `Connection Options` section and click `Connect to Jupyter Lab` to access the Jupyter interface.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step8-ConnecttoJupyterLab.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=cf66856fabd630d6f248d7959c8ba7ac" alt="Step8 Connectto Jupyter Lab Pn" width="1280" height="400" data-path="images/Step8-ConnecttoJupyterLab.png" />
</Frame>

Step 9: Access Jupyter Lab

* Wait for the Jupyter Lab web interface to load.
* Open `Terminal` to run an official example and verify the service is working correctly.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step9-AccessJupyterLab.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=c36adb44cdaf47173b8e301e97547332" alt="Step9 Access Jupyter Lab Pn" width="1280" height="635" data-path="images/Step9-AccessJupyterLab.png" />
</Frame>

Step 10: Run a Fine-Tuning Example

* Execute the official example code to perform a fine-tuning task.

```bash  theme={"system"}
# Fetch axolotl examples
axolotl fetch examples

# Or, specify a custom path
axolotl fetch examples --dest path/to/folder

# Train a model using LoRA
axolotl train examples/llama-3/lora-1b.yml
```

**Note:** You can't change the default mount path for the network volume in the console. It can only be set when creating an instance or via OpenAPI. Set your desired mount path during instance creation when attaching a volume.


Built with [Mintlify](https://mintlify.com).