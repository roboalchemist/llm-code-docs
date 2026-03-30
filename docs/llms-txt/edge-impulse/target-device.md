# Source: https://docs.edgeimpulse.com/studio/projects/dashboard/target-device.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Target device

The target configuration tool allows you to define your **Target device** and **Application budget** according to your project's requirements. This flow is designed to help you optimize your impulse, processing, learn block, or imported model for your specific target hardware, ensuring that your impulse will run efficiently on your device or custom architecture.&#x20;

The configuration form can be accessed from the top-level navigation. The form allows you to select from a range of processor types, architectures, and clock rates. For a custom device, you could for example select **Low-end MCU** and specify the clock rate, RAM, ROM, and maximum allowed latency for your application.

<Frame caption="Target-driven Default Settings">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tdf-no-launcher-1.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=b1705297a44a49885938cde7b2745389" width="896" height="1000" data-path=".assets/images/tdf-no-launcher-1.png" />
</Frame>

### Accessing the configuration panel

By default, the form shows 'Cortex-M4F 80MHz' as the target device. You can change this by clicking on **Change Target device**. You can select from a range of processor types, architectures, and clock rates. For a custom device, you could for example select **Low-end MCU** and specify the clock rate, RAM, ROM, and maximum allowed latency for your application.

1. Navigate to the top-level menu in Edge Impulse Studio.
2. Click on **Change Target Device** to open the configuration panel.

### Configure your target device and application budget

Lets walk you through some of the current options for configuring your device and application budget:

* **Target Device:** Select the type of target device you are configuring from options like "Custom" or specific development boards.
* **Processor Type Selection:** Selecting a processor type dynamically adjusts available architecture options and fields to suit your hardware:
  * **For Low-end MCU:** This option allows you to specify clock rate, RAM, and ROM, suitable for 'Cortex-M' architectures.
  * **For AI Accelerators:** Selecting this disables the clock rate field, reflecting the unique requirements of AI accelerator devices.
* **Custom Device Configuration:** Choosing to configure a custom device opens fields to precisely define its capabilities, ensuring your project setup is accurately tailored to your hardware.

#### Special options for Custom Targets:

The form allows you to select from a range of processor types, architectures, and clock rates. For a custom device, you could for example select **Low-end MCU** and specify the clock rate, RAM, ROM, and maximum allowed latency for your application.

<Frame caption="Custom Targets">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tdf-no-launcher-2.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=de5b04af757801e1623b8c00ee6cafca" width="896" height="1000" data-path=".assets/images/tdf-no-launcher-2.png" />
</Frame>

* **Custom:** Select this for custom hardware specifications or devices not listed in Edge Impulse, allowing for a customized hardware profile. Selection Options

**Processor Type & Architecture**

Choose from a variety of processor types and architectures. Your selection determines which options and fields are available to accurately configure your device. Estimations for GPU, AI accelerator, or NPU devices are not computed using clock speed, or but rather the device's unique capabilities.

* **Processor Type:** Selections range from various processor types. Choosing **GPU, AI accelerator' or NPU** deactivates the clock speed option, as it's irrelevant for device estimation.
* **Processor Architecture (Optional):** Specify your device's architecture to refine its configuration (e.g., Cortex-M0+, Cortex-M4F, Cortex-M7).
* **Clock Rate (Optional):** Set the clock rate for relevant processor types to estimate operational capabilities accurately. The units shown will be indicated by the | MHz | GHz as relevant to the scale of processor. As previously stated the clock rate field is disabled for GPU, AI accelerator, or NPU devices.
* **Accelerator:** If the device supports hardware acceleration, select from available options such as Arm Cortex-U55, NVIDIA Jetson Nano, and others.
* **Device ID (Optional):** Provide a unique identifier for your custom device model or chip architecture variant for easy recognition and setup.
* **Custom Device Name (Optional):** Provide a unique name for your custom device to easily identify it in your project.

**Application Budget - RAM, ROM, and Latency**

The application budget section allows you to specify the maximum allowed latency, RAM, and ROM for your application. These values are used to estimate the performance of your model on your target device.

* **RAM:** Specify the amount of RAM available on your device in kilobytes (kB).
* **ROM:** Specify the amount of ROM available on your device in kilobytes (kB).
* **Latency:** Specify the maximum allowed latency for your application in milliseconds (ms).

<Frame caption="Save">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tdf-reset-save.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=5f0ed4e4bb8889c7c4b33109e1a2c1da" width="1600" height="164" data-path=".assets/images/tdf-reset-save.png" />
</Frame>

* **Save Target:** Save your custom device and application budget configuration to apply it to your project.

After customizing your target device and application budget, click **Save target**. With the target device set, navigate to the EON Tuner to see the configuration in action. The target device can be seen at the top level of navigation on all screens within your project. Your custom device name (e.g., 'my first mcu') and the specified parameters (100 ms latency, 256 kB RAM, 1024 kB ROM) are visible. The target device configuration is also taken into account during the performance estimation for deployment.

<Frame caption="Navigating to EON Tuner with Updated Target Device">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tdf-eon-tuner.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=705d6d87b2608b72d44e0a0540297a1f" width="1600" height="777" data-path=".assets/images/tdf-eon-tuner.png" />
</Frame>

### Top-level Navigation

Once saved the target device can be seen at the top level of navigation on all screens within your project. Your custom device name (e.g., 'my first mcu') and the specified parameters (100 ms latency, 256 kB RAM, 1024 kB ROM) are visible. The target device configuration is also taken into account during the performance estimation for deployment.

<Frame caption="Top-level Navigation">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tdf-custom-name-title-bar.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=31ae4b192a17875d4fbd68918bdab8ff" width="1600" height="82" data-path=".assets/images/tdf-custom-name-title-bar.png" />
</Frame>

#### Additional functionalities:

There are some additional considerations for targets mentioned in the tabs below, particularly for their generated binaries models and deployment formats.

<Tabs>
  <Tab title="Ethos Enabled Targets">
    For Ethos enabled targets, you can select them as profiling targets. After training, the Vela compiled model will be available on the dashboard. This feature is exclusive to Ethos enabled targets. These assets are only available in our studio, when deploying and selecting the deployment format, the library will include the Vela compiled model converted to a C header. While this is sufficient for most users, those needing the binary file directly on the flash may find it inconvenient to convert it back from a C header.

    * **Key Differences:**
      * **C++ Library:** The library will include the Vela compiled model converted to a C header.
      * **Vela Library:** The Vela compiled model will be available on the dashboard.
  </Tab>

  <Tab title="Vela for Non-Ethos Enabled Targets">
    C2 and IMIX users, who need Vela compiled models using other non standard inferencing engine that need to be converted to TFLite files instead of the C++ library.

    * **Key Differences:**
      * **Deployment Format:** The deployment format will include the TFLite model.
  </Tab>

  <Tab title="Think Silicon - NEOX Targets">
    When selecting the Neox target as a profiling target, the training pipeline involves training a float model, which is then converted to an int8 model using a custom quantizer, rather than the TensorFlow framework's quantizer.

    * **Key Differences:**
      * **Deployment Format:** The deployment format will include the int8 model.
      * **Custom Quantizer:** The int8 model is generated using a custom quantizer.
  </Tab>
</Tabs>

### Summary

The target-driven flow in Edge Impulse Studio allows you to configure your target device and application budget according to your project's requirements. This flow is designed to help you optimize your impulse for your specific target hardware, ensuring that your impulse will run efficiently on your device.

We hope this feature is helpful, and intuitive. If you have any questions or suggestions, feel free to reach out to us at [forum.edgeimpulse.com](https://forum.edgeimpulse.com/). We're always happy to hear from you!


Built with [Mintlify](https://mintlify.com).