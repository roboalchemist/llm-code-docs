# Source: https://docs.syncfusion.com/extension/wpf-extension/toolbox-configuration.md

# Source: https://docs.syncfusion.com/extension/windowsforms-extension/toolbox-configuration.md

# Source: https://docs.syncfusion.com/uwp/visual-studio-integration/toolbox-configuration.md

# Source: https://docs.syncfusion.com/windowsforms/visual-studio-integration/toolbox-configuration.md

# Source: https://docs.syncfusion.com/wpf/visual-studio-integration/toolbox-configuration.md

# Toolbox Configuration

The Syncfusion Toolbox Installer utility incorporates the SyncfusionÂ® WPF components into the Visual Studio .NET toolbox.

N> Toolbox configuration support is not available for the Visual Studio Express Edition. However, you can manually configure the SyncfusionÂ® controls into the Visual Studio Express Toolbox. To do so, refer to the [Manual Toolbox Configuration](https://help.syncfusion.com/common/faq/how-to-configure-the-toolbox-of-visual-studio-manually).

If the <b>âConfigure SyncfusionÂ® Controls in Visual Studioâ</b> checkbox is selected from the installer UI while installing the SyncfusionÂ® WPF installer, SyncfusionÂ® components will be automatically configured in the Visual Studio toolbox.

To add the SyncfusionÂ® WPF components via the Syncfusion Toolbox Installer, perform the following steps:

1. To launch Toolbox configuration utility, follow either one of the options below:

   **Option 1:**   
   Open the Syncfusion Control Panel, click **Add On and Utilities > Toolbox Installer**.
   
   ![Add On and Utilities in Toolbox Installer for WPF](toolbox-configuration_images/wpf-toolbox-installer-add-on-and-utilities.png)
   
   **Option 2:**  
   Click **Syncfusion menu** and choose **Essential StudioÂ® for WPF > Toolbox Configuration...** in **Visual Studio**

   ![Toolbox Installer via Syncfusion menu](toolbox-configuration_images/syncfusion-menu-toolbox.png)

   N> From Visual Studio 2019, Syncfusion menu is available under Extensions in Visual Studio menu.

   ![Toolbox Installer via Syncfusion menu](toolbox-configuration_images/syncfusion-menu-toolbox-2019.png)

2. Toolbox Installer will be opened.

   ![Toolbox Installer for WPF](toolbox-configuration_images/wpf-toolbox-configuration.png)

   The following options are available in Toolbox Configuration:

   * Install VS2015 â Configures Framework 4.6.2 Syncfusion controls in VS 2015 toolbox.
   * Install VS2017 â Configures Framework 4.6.2 Syncfusion controls in VS 2017 toolbox.
   * Install VS2019 â Configures Framework 4.6.2 Syncfusion controls in VS 2019 toolbox
   * Install VS2022 â Configures Framework 4.6.2 Syncfusion controls in VS 2022 toolbox.
   * Install VS2026 â Configures Framework 4.6.2 Syncfusion controls in VS 2026 toolbox.
   
    N> You can also configure Syncfusion controls from a lower version Framework assembly to higher version of Visual Studio.
   
3. The successful configuration of Toolbox is indicated by an Information message. Click OK.

   ![Toolbox Installer Syncfusion menu in visual studio](toolbox-configuration_images/toolbox-installer-in-syncfusion-menu-in-visual-studio.png)
   
   
   N> * If your installed controls are not reflected properly in the Visual Studio Toolbox, you'll have to reset the Toolbox.
   * This tool configures only the controls that are located under {Installed Location}\Assemblies\{Framework version}. 

## Configuring toolbox for WPF in Visual Studio 2026

From 2025 Volume 3 SP 2, SyncfusionÂ® started providing toolbox support for .NET Framework in Visual Studio 2026 Toolbox. After installing the SyncfusionÂ® WPF installer, SyncfusionÂ® controls will be automatically configured in the Visual Studio 2026 toolbox for WPF projects.

## Configuring toolbox for WPF in Visual Studio 2022   

From 2021 Volume 4, SyncfusionÂ® started providing toolbox support for .NET Framework in Visual Studio 2022 Toolbox. After installing the SyncfusionÂ® WPF installer, SyncfusionÂ® controls will be automatically configured in the Visual Studio 2022 toolbox for WPF projects.

N> * SyncfusionÂ® WPF .NET 5.0 controls will be compatible with .NET 6.0, on installing the SyncfusionÂ® WPF installer, our .NET 5.0 controls will be configured the toolbox for .NET 6.0 projects too.
   
## Configuring toolbox for WPF .NET 8.0\9.0\10.0 projects

From 2025 Volume 3 SP 2 Release, SyncfusionÂ® started providing toolbox support for WPF .NET 8.0\9.0\10.0 framework in Visual Studio 2026. SyncfusionÂ® controls will be automatically configured in the Visual Studio 2026 toolbox for WPF .NET 8.0\9.0\10.0 projects.

## Configuring toolbox for WPF .NET 5.0 projects

From 2021 Volume 1, SyncfusionÂ® started providing toolbox support for the WPF .NET 5.0 framework in Visual Studio. After installing the SyncfusionÂ® WPF installer, SyncfusionÂ® controls will be automatically configured in the Visual Studio toolbox for WPF.NET 5.0 projects.

N> * SyncfusionÂ® included this toolbox support for .NET 5.0 WPF platform from 2021 Volume 1 release version v19.1.0.54 only. 
* If the project was created with TargetFramework.NET Core 3.1 and then changed to.NET 5.0 after installing the WPF setup, you must restart Visual Studio to see the SyncfusionÂ® controls in the Visual Studio Toolbox. 
* Visual Studio 2019 16.7 Preview 2 and later is required.

### Upgrading the SyncfusionÂ® WPF toolbox .NET 5.0 controls without installing the build

You can upgrade the SyncfusionÂ® WPF toolbox for .NET 5.0 control with NuGet packages downloaded from [nuget.org](https://www.nuget.org/). Download ["Syncfusion.UI.WPF.NET"](https://www.nuget.org/packages/Syncfusion.UI.WPF.NET/) package from nuget.org in your machine.

Use the following steps to add the SyncfusionÂ® WPF controls through SyncfusionÂ® NuGet packages:

**step 1:** 
   
   Extract **"Syncfusion.UI.WPF.NET"** package by using the below commands.
	
   Open Command prompt from nuget.exe path and run the following commands
	
   **Command:** {nuget.exe path} add "F:\Syncfusion\Syncfusion.UI.WPF.NET.{version}.nupkg" -Source "F:\Syncfusion\Expand" -expand
	
   **Example:** F:\Syncfusion>nuget.exe add "F:\Syncfusion\Syncfusion.UI.WPF.NET.19.1.0.50.nupkg" -Source "F:\Syncfusion" -expand
	
   ![Toolbox Installer for WPF application](toolbox-configuration_images/wpf-net-50-toolbox-package-extract.png)
	
**step 2:** 

   Open **"Syncfusion Toolbox for WPF.config"** file from the following location.
	
   **Location:** "C:\Program Files (x86)\NuGet\Config\Syncfusion Toolbox for WPF.config"
	
   ![Toolbox Installer for WPF application](toolbox-configuration_images/wpf-net-50-toolbox.png)

   Or you can create this file in the same location by using the XML format given below
    
{% tabs %}
{% highlight XML %}
     <?xml version="1.0" encoding="utf-8"?>
      <configuration>
        <fallbackPackageFolders>
          <add key="Syncfusion Toolbox Local NuGet Packages {version}" value="F:\Syncfusion" />
        </fallbackPackageFolders>
      </configuration>
{% endhighlight %}
{% endtabs %}
	
**step 3:**
   
   Update extracted SyncfusionÂ® NuGet package path in **value** attribute.
	
   **Example:**
   ![Toolbox Installer for WPF application](toolbox-configuration_images/wpf-net-50-toolbox-package-update.png)
	
**step 4:**
   
   Now restart the Visual Studio 2019 to get populate the latest SyncfusionÂ® controls in Toolbox.

## Configuring toolbox for .NET Core 3.1 projects

The SyncfusionÂ® NuGet packages must be installed in the WPF .NET Core application before the SyncfusionÂ® toolbox can be configured. The corresponding NuGet packages for SyncfusionÂ® components will be configured in the Visual Studio toolbox after installing the SyncfusionÂ® NuGet packages in the .NET Core application.  

Please refer the documentation [link](../installation/install-nuget-packages), to learn more about how to use the SyncfusionÂ® components using the SyncfusionÂ® NuGet packages in .NET Core application.
   
