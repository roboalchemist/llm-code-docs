# Source: https://docs.silabs.com/openthread/3.0.0/bootloader-user-guide-gsdk-4/06-getting-started-with-the-gecko-bootloader.md

# Source: https://docs.silabs.com/openthread/3.0.0/bootloader-user-guide-series3-and-higher/06-getting-started-with-the-gecko-bootloader.md

# Getting Started with the Gecko Bootloader

This section describes how to build a Gecko Bootloader from one of the provided examples. These instructions assume that you have installed Simplicity Studio 5, the SiSDK and associated utilities as described in the SDK’s quick start guide, and that you are familiar with generating, compiling, and flashing an example application in the relevant version.

1. Create a project based on the Gecko Bootloader example of your choice. The project opens with a tab describing the example.  
   ![screenshot](/bootloader-user-guide-series3-and-higher/0.2/images/sld737-image12.png)
2. Click the project (*.slcp) tab to move to the Project Configurator interface.  
   ![screenshot](/bootloader-user-guide-series3-and-higher/0.2/images/sld737-image13.png)
3. The Software Components tab shows the list of available components that can be installed in the project.  
   ![screenshot](/bootloader-user-guide-series3-and-higher/0.2/images/sld737-image14.png)
4. The **Storage Slot Setup** component allows you to configure storage slots to be used if a storage component is also installed. The default configuration matches the target part and bootloader type. This component supports a maximum of three storage slots.  
   ![screenshot](/bootloader-user-guide-series3-and-higher/0.2/images/sld737-image15.png)
5. Click the **Build** (hammer) icon.
6. After the build is complete, the bootloader binaries are available in the **artifact** folder as depicted in the image below.  
   ![screenshot](/bootloader-user-guide-series3-and-higher/0.2/images/sld737-image16.png)

The image containing only a bootloader must be used to create a GBL file for bootloader upgrade.