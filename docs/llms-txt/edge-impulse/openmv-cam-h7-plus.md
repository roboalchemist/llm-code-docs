# Source: https://docs.edgeimpulse.com/hardware/boards/openmv-cam-h7-plus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Open MV Cam H7 Plus

The OpenMV Cam is a small and low-power development board with a Cortex-M7 microcontroller supporting MicroPython, a μSD card socket and a camera module capable of taking 5MP images - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models through the studio and the OpenMV IDE.

<Frame caption="The OpenMV Cam H7 Plus">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6c14f3f-9b8e557-new-cam-v5-angle-web_grande.jpg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=b58d30ea19abb376660b236d6f6b5a2f" width="600" height="600" data-path=".assets/images/6c14f3f-9b8e557-new-cam-v5-angle-web_grande.jpg" />
</Frame>

### Connecting to Edge Impulse

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. [OpenMV IDE](https://openmv.io/pages/download).

<Warning>
  **Problems installing the CLI?**

  See the [installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Next steps: building a machine learning model

With all the software in place it's time to connect the development board to Edge Impulse. To make this easy we've put some tutorials together which takes you through all the steps to acquire data, train a model, and deploy this model back to your device.

* [Image classification](/tutorials/end-to-end/image-classification) - end-to-end tutorial.
* [Detecting objects using FOMO](/tutorials/end-to-end/object-detection-centroids).
* [Collecting image data with the OpenMV Cam H7 Plus](/tutorials/topics/data/collect-image-data-studio) - collecting datasets using the OpenMV IDE.
* [Running your impulse on your OpenMV camera](/hardware/deployments/run-openmv) - run your trained impulse on the OpenMV Cam H7 Plus.


Built with [Mintlify](https://mintlify.com).