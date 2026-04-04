# Source: https://docs.silabs.com/openthread/3.0.0/openthread-single-band-proprietary-sub-ghz/02-building-an-openthread-sample-app-for-proprietary-sub-ghz.md

# Building an OpenThread Sample App for Proprietary Sub-GHz

To build an OpenThread sample application for sub-GHz, you need Simplicity Studio and the Gecko SDK 3.2 (or higher) development environment with the OpenThread SDK package installed.

This section assumes that you have installed Simplicity Studio and the OpenThread SDK, and that you are familiar with Simplicity Studio and configuring, building, and flashing applications. If not, see the [OpenThread Quick-Start Guide](/openthread/3.0.0/openthread-quick-start-guide).

1. Connect your target development hardware (supporting proprietary sub-GHz as discussed in [Hardware Limitations](./index#hardware-limitations)), open Simplicity Studio's File menu, and select **New > Silicon Labs Project Wizard**. The Target, SDK, and Toolchain Selection dialog opens. Your target hardware should be populated. Click **NEXT**.
2. The Example Project Selection dialog opens. Use the **Technology Type** and **Keyword** filters to search for a specific example, for example **ot-cli-ftd**. Select it and click **NEXT**.  
   > **Note**: If you do not see the application, your connected hardware may not be compatible. To verify, in the Launcher Perspectives My Products view enter EFR32MGxx and select one of the boards. Go to the Examples tab, filter by Thread technology and verify you can see the app.
3. The Project Configuration dialog opens. Here you can rename your project, change the default project file location, and determine if you will link to or copy project files. Note that if you change any linked resource, it is changed for any other project that references it. Unless you know you want to modify SDK resources, use the default selection. Click **FINISH**. The Simplicity IDE opens with the **ot-cli-ftd** project open in the Project Configurator.
4. To configure proprietary sub-GHz support, on the **SOFTWARE COMPONENTS** tab, select **Installed Components** and select the **Platform Abstraction** component under OpenThread. Note that you can also search for a component by name in the search field.  
   ![Platform Abstraction](/openthread-single-band-proprietary-sub-ghz/0.2/images/sld699-image1.png)
5. Click **Configure** and enable the **Proprietary Sub-GHz Support** configuration option.  
   ![Proprietary Sub-GHz Support](/openthread-single-band-proprietary-sub-ghz/0.2/images/sld699-image2.png)  
   > **Note**: If you do not see the **Configure** control or the **Proprietary Sub-GHz Support** configuration option associated with the Platform Abstraction component, your hardware may not be compatible with the proprietary radio specifications discussed above.
6. Build the project. The generated ot-cli-ftd.s37 image may now be uploaded to your board using a Simplicity Studio tool such as the flash programmer or Simplicity Commander.
