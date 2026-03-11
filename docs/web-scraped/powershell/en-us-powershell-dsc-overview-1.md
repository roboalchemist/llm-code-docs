# Source: https://learn.microsoft.com/en-us/powershell/dsc/overview?view=dsc-2.0

Title: Desired State Configuration 2.0 - PowerShell

URL Source: https://learn.microsoft.com/en-us/powershell/dsc/overview?view=dsc-2.0

Markdown Content:
With the release of PowerShell 7.2, the **PSDesiredStateConfiguration** module is no longer included in the PowerShell package. Separating DSC into its own module allows us to invest and develop DSC independent of PowerShell and reduces the size of the PowerShell package. Users of DSC can enjoy the benefit of upgrading DSC without the need to upgrade PowerShell, accelerating time to deployment of new DSC features. Users that want to continue using DSC v2 can download **PSDesiredStateConfiguration** 2.0.7 from the PowerShell Gallery.

Users working with non-Windows environments can expect cross-platform features in DSC v3. For more information about the future of DSC, see the [PowerShell Team blog](https://devblogs.microsoft.com/powershell/powershell-team-2021-investments/#dsc-for-powershell-7).

To install **PSDesiredStateConfiguration** 2.0.7 from the PowerShell Gallery:

```
Install-Module -Name PSDesiredStateConfiguration -Repository PSGallery -MaximumVersion 2.99
```

Important

Be sure to include the parameter **MaximumVersion** or you could install version 3 (or higher) of **PSDesireStateConfiguration** that contains significant differences.

DSC 2.0 is supported for use with [Azure machine configuration](https://learn.microsoft.com/en-us/azure/governance/machine-configuration/overview). Other scenarios, such as directly calling DSC Resources with `Invoke-DscResource`, may be functional but aren't the primary intended use of this version.

If you aren't using Azure machine configuration, you should use DSC 1.1.machine

There are several major changes in DSC 2.0.

The only way to use DSC Resources in 2.0 is with the `Invoke-DscResource` cmdlet or Azure machine configuration.

The following cmdlets have been removed:

*   `Disable-DscDebug`
*   `Enable-DscDebug`
*   `Get-DscConfiguration`
*   `Get-DscConfigurationStatus`
*   `Get-DscLocalConfigurationManager`
*   `Publish-DscConfiguration`
*   `Remove-DscConfigurationDocument`
*   `Restore-DscConfiguration`
*   `Set-DscLocalConfigurationManager`
*   `Start-DscConfiguration`
*   `Stop-DscConfiguration`
*   `Test-DscConfiguration`
*   `Update-DscConfiguration`

The following features have been removed:

*   The pull server
*   The local configuration manager (LCM)

The following features aren't supported:

*   Multi-system DSC Configurations
*   Cross-system dependencies (the `WaitFor*` DSC Resources)
*   Rebooting behavior for DSC Resources
*   Adding parameters to DSC Configuration blocks
*   Using flow control statements in DSC Configuration blocks
*   Using credentials in DSC Configuration blocks
*   Using the **ConfigurationData** parameter with a DSC Configuration
*   Using the `Node` keyword in a DSC Configuration
*   Using composite DSC Configurations (DSC Configurations that nest another DSC Configuration inside them)

The built-in DSC Resources have been removed. The [PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/overview?view=dsc-2.0) module includes replacements for some removed DSC Resources. Refer to the following table for the status of the DSC Resources.

| DSC Resource | Status |
| --- | --- |
| `Archive` | Replaced by the [Archive DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/archive/archive?view=dsc-2.0). |
| `Environment` | Replaced by the [Environment DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/environment/environment?view=dsc-2.0). |
| `File` | Removed. This DSC Resource isn't available in DSC v2 and later. |
| `Group` | Replaced by the [Group DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/group/group?view=dsc-2.0). |
| `GroupSet` | Replaced by the [GroupSet DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/groupset/groupset?view=dsc-2.0). |
| `Log` | Removed. This DSC Resource isn't available in DSC v2 and later. |
| `Package` | Partially replaced by the [MsiPackage DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/msipackage/msipackage?view=dsc-2.0). |
| `ProcessSet` | Replaced by the [ProcessSet DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/processset/processset?view=dsc-2.0). |
| `Registry` | Replaced by the [Registry DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/registry/registry?view=dsc-2.0). |
| `Script` | Replaced by the [Script DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/script/script?view=dsc-2.0). |
| `Service` | Replaced by the [Service DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/service/service?view=dsc-2.0). |
| `ServiceSet` | Replaced by the [ServiceSet DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/serviceset/serviceset?view=dsc-2.0). |
| `User` | Replaced by the [User DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/user/user?view=dsc-2.0). |
| `WaitForAll` | Removed. This DSC Resource isn't available in DSC v2 and later. |
| `WaitForAny` | Removed. This DSC Resource isn't available in DSC v2 and later. |
| `WaitForSome` | Removed. This DSC Resource isn't available in DSC v2 and later. |
| `WindowsFeature` | Replaced by the [WindowsFeature DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/windowsfeature/windowsfeature?view=dsc-2.0). |
| `WindowsFeatureSet` | Replaced by the [WindowsFeatureSet DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/windowsfeatureset/windowsfeatureset?view=dsc-2.0). |
| `WindowsOptionalFeature` | Replaced by the [WindowsOptionalFeature DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/windowsoptionalfeature/windowsoptionalfeature?view=dsc-2.0). |
| `WindowsOptionalFeatureSet` | Replaced by the [WindowsOptionalFeatureSet DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/windowsoptionalfeatureset/windowsoptionalfeatureset?view=dsc-2.0). |
| `WindowsPackageCab` | Replaced by the [WindowsPackageCab DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/windowspackagecab/windowspackagecab?view=dsc-2.0). |
| `WindowsProcess` | Replaced by the [WindowsProcess DSC Resource in PSDscResources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/resources/windowsprocess/windowsprocess?view=dsc-2.0). |
