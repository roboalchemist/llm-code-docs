# Source: https://novita.ai/docs/guides/kohya_ss-gui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Transform Your Stable Diffusion Experience with Kohya_SS GUI on Novita AI. 

# Run Kohya_SS GUI on Novita AI

Kohya\_SS GUI offers a user-friendly Gradio interface for Kohya's Stable Diffusion trainers. It has strong Linux support through community installations, with limited but possible macOS compatibility. Combining Novita AI with Kohya\_SS GUI streamlines AI model training workflows, removing hardware limitations and creating an optimized environment for diffusion model fine-tuning.

This guide will show you how to deploy and run Kohya\_SS GUI on Novita AI's platform.

## How to Run Kohya\_ss: GUI on Novita AI

Step 1: Access GPU Instance Control Panel

* Navigate to the `GPU menu` in the top navigation bar.
* Click `Get Started` to enter the GPU Instance control interface.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step1AccessGPUInstanceControlPanel.jpg?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=ae638187047dd0adf6700fbeedd7facd" alt="images/Step1AccessGPUInstanceControlPanel.jpg" width="3840" height="1941" data-path="images/Step1AccessGPUInstanceControlPanel.jpg" />
</Frame>

Step 2: Select Kohya\_ss:GUI Template

* Locate and select the `Kohya_ss:GUI` official template.
* Click `Deploy` button under the 4090 GPU card option to enter the instance creation page.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step2SelectKohya_ssGUITemplate.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=07ef1cf322b09306119cd9235be8a7d4" alt="images/Step2SelectKohya_ssGUITemplate.png" width="3841" height="1905" data-path="images/Step2SelectKohya_ssGUITemplate.png" />
</Frame>

Step 3: Configure Disk Parameters and Review Configuration Settings

* On the left panel, adjust the disk settings as needed:
  * Set appropriate system disk size;
  * Configure local disk capacity based on your storage needs.
* Check the right panel for configuration options:
  * Verify image settings are correct;
  * Confirm startup commands are properly configured;
  * Ensure ports and environment variables meet your requirements.
* Confirm all settings are correct and then click the `Next` button to advance to the final confirmation page.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step3ConfigureDiskParametersandReviewConfigurationSettings.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=682f057986ba5c59d5b4f87db9c51761" alt="images/Step3ConfigureDiskParametersandReviewConfigurationSettings.png" width="3841" height="1905" data-path="images/Step3ConfigureDiskParametersandReviewConfigurationSettings.png" />
</Frame>

Step 4: Proceed to Confirmation and Deploy Your Instance

* Review the complete instance configuration summary.
* Verify the cost details displayed on this page.
* Click `Deploy` to initiate the deployment process.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step4ProceedtoConfirmationandDeployYourInstance.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=66846408e8d230a9e3c2497a86944ed8" alt="images/Step4ProceedtoConfirmationandDeployYourInstance.png" width="3841" height="1717" data-path="images/Step4ProceedtoConfirmationandDeployYourInstance.png" />
</Frame>

Step 5: Wait as the System Creates Your Instance

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step5WaitastheSystemCreatesYourInstance.jpg?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=2a4fd55b0bc5d39997cdb10ace54d88b" alt="images/Step5WaitastheSystemCreatesYourInstance.jpg" width="1434" height="1102" data-path="images/Step5WaitastheSystemCreatesYourInstance.jpg" />
</Frame>

Step 6: Monitor Deployment Progress and Track Image Download

* After deployment, the system will automatically redirect you to the instance management page.
* Your new instance will display `Pulling` status while downloading the image.
* After clicking the arrow icon next to your instance name, the instance details panel will be expanded with the image download progress in real-time.
* Once image downloading completes, instance will change status from `Pulling` to `Running`.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step6MonitorDeploymentProgressandTrackImageDownload.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=8f2d5e2bc6ba2f1ef3059e11c9a9745b" alt="images/Step6MonitorDeploymentProgressandTrackImageDownload.png" width="1555" height="409" data-path="images/Step6MonitorDeploymentProgressandTrackImageDownload.png" />
</Frame>

Step 7: Check Instance Logs

* Click the `Logs` button on your instance and select `Instance Logs` from the available options.
* Observe the Kohya\_ss service startup process in the logs and wait for confirmation that all services have loaded successfully.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step7CheckInstanceLogs.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=1c0d285d27092766146df663e8fe3e98" alt="images/Step7CheckInstanceLogs.png" width="2283" height="1420" data-path="images/Step7CheckInstanceLogs.png" />
</Frame>

Step 8: Connect to Your Instance

* Close the logs view when ready and click the `Connect` button to view connection options.
* View various connection methods: SSH, TCP, and HTTP of your instance.
* For Kohya\_SS GUI access, focus on the HTTP connection details. Therefore, in the Connection Options section, click `Connect to HTTP Service` and access to a new browser tab or window.

<Frame>
  ### &#x20; <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step8-1ConnecttoYourInstance.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=6cc3f1846be91a2d099871b98da23229" alt="images/Step8-1ConnecttoYourInstance.png" width="2136" height="782" data-path="images/Step8-1ConnecttoYourInstance.png" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step8-2ConnecttoYourInstance.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=3493475ecd61abe9f68b1a1becaf4251" alt="images/Step8-2ConnecttoYourInstance.png" width="1373" height="971" data-path="images/Step8-2ConnecttoYourInstance.png" />
</Frame>

Step 9: Begin Using Your Instance

* Allow a few moments for the web interface to fully load and get ready to run Kohya\_ss:GUI on Novita AI.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step9BeginUsingYourInstance.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=777e1b0937e91ac1d64f468fe8b71938" alt="images/Step9BeginUsingYourInstance.png" width="3841" height="1905" data-path="images/Step9BeginUsingYourInstance.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).