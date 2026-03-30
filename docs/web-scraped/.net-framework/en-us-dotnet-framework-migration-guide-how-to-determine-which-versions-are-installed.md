# Source: https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed

Title: Determine which .NET Framework versions are installed - .NET Framework

URL Source: https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed

Markdown Content:
You can install and run multiple versions of .NET Framework on a computer.

* If you want to check the versions on your _own_ computer, the easiest way is through **Control Panel**>**Programs**>**Programs and Features**, or in **Settings** under **Apps**>**Installed apps**. You can also use [these community-maintained tools](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#community-maintained-tools).
* If you're an app developer, you might need to know which .NET Framework versions are installed on the app user's computer. The [registry](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#registry) contains a list of the versions of .NET Framework installed on the computer. You can also query the [`RuntimeInformation.FrameworkDescription` property](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#runtimeinformationframeworkdescription-property).
* To find the CLR version, which is versioned separately, see [Find CLR versions](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#find-clr-versions).

.NET Framework consists of two main components, which are versioned separately:

* A set of assemblies, which are collections of types and resources that provide the functionality for your apps. .NET Framework and the assemblies share the same version number. For example, .NET Framework versions include 4.5, 4.6.1, and 4.7.2.
* The common language runtime (CLR), which manages and executes your app's code. A single CLR version typically supports multiple .NET Framework versions. For example, CLR version 4.0.30319._xxxxx_ where _xxxxx_ is less than 42000, supports .NET Framework versions 4 through 4.5.2. CLR version greater than or equal to 4.0.30319.42000 supports .NET Framework versions starting with .NET Framework 4.6.

Community-maintained tools are available to help detect which .NET Framework versions are installed:

* [https://github.com/jmalarcon/DotNetVersions](https://github.com/jmalarcon/DotNetVersions)
* [https://github.com/EliteLoser/DotNetVersionLister](https://github.com/EliteLoser/DotNetVersionLister)

To programmatically query for which .NET version your app is running on, you can use the [RuntimeInformation.FrameworkDescription](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.runtimeinformation.frameworkdescription#system-runtime-interopservices-runtimeinformation-frameworkdescription) property. If the app is running on .NET Framework, the output will be similar to:

```
.NET Framework 4.8.4250.0
```

By comparison, if the app is running on .NET Core or .NET 5+, the output will be similar to:

```
.NET Core 3.1.9
.NET 5.0.0
```

You can use the registry to detect which .NET Framework version is installed. The keys are different for .NET Framework 1.0-4.0 and .NET Framework 4.5+. You can use Registry Editor, PowerShell, or code to check the registry.

* [.NET Framework 4.5 and later versions](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#net-framework-45-and-later-versions)
  * [Registry Editor](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#use-registry-editor)
  * [Query using code](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#query-the-registry-using-code)
  * [Query using PowerShell](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#query-the-registry-using-powershell)

* [.NET Framework 1.0-4.0](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#net-framework-10-40)
  * [Registry Editor](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#use-registry-editor-older-framework-versions)
  * [Query using code](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#query-the-registry-using-code-older-framework-versions)
  * [Query using PowerShell](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#query-the-registry-using-powershell-older-framework-versions)

The version of .NET Framework (4.5 and later) installed on a machine is listed in the registry at **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full**. If the **Full** subkey is missing, then .NET Framework 4.5 or above isn't installed.

Note

The **NET Framework Setup** subkey in the registry path does _not_ begin with a period.

The **Release** REG_DWORD value in the registry represents the version of .NET Framework installed.

| .NET Framework version | Value of **Release** |
| --- | --- |
| .NET Framework 4.5 | All Windows operating systems: **378389** |
| .NET Framework 4.5.1 | On Windows 8.1 and Windows Server 2012 R2: **378675** On all other Windows operating systems: **378758** |
| .NET Framework 4.5.2 | All Windows operating systems: **379893** |
| .NET Framework 4.6 | On Windows 10: **393295** On all other Windows operating systems: **393297** |
| .NET Framework 4.6.1 | On Windows 10 November Update systems: **394254** On all other Windows operating systems (including Windows 10): **394271** |
| .NET Framework 4.6.2 | On Windows 10 Anniversary Update and Windows Server 2016: **394802** On all other Windows operating systems (including other Windows 10 operating systems): **394806** |
| .NET Framework 4.7 | On Windows 10 Creators Update: **460798** On all other Windows operating systems (including other Windows 10 operating systems): **460805** |
| .NET Framework 4.7.1 | On Windows 10 Fall Creators Update and Windows Server, version 1709: **461308** On all other Windows operating systems (including other Windows 10 operating systems): **461310** |
| .NET Framework 4.7.2 | On Windows 10 April 2018 Update and Windows Server, version 1803: **461808** On all Windows operating systems other than Windows 10 April 2018 Update and Windows Server, version 1803: **461814** |
| .NET Framework 4.8 | On Windows 10 May 2019 Update and Windows 10 November 2019 Update: **528040** On Windows 10 May 2020 Update, October 2020 Update, May 2021 Update, November 2021 Update, and 2022 Update: **528372** On Windows 11 and Windows Server 2022: **528449** On all other Windows operating systems (including other Windows 10 operating systems): **528049** |
| .NET Framework 4.8.1 | On Windows 11 2025 Update: **533509** On Windows 11 2022 Update and Windows 11 2023 Update: **533320** All other Windows operating systems: **533325** |

To determine whether a _minimum_ version of .NET Framework is present, check for a **Release** REG_DWORD value that's greater than or equal to the corresponding value listed in the following table. For example, if your application runs under .NET Framework 4.8 or a later version, test for a **Release** REG_DWORD value that's _greater than or equal to_ 528040.

| .NET Framework version | Minimum value |
| --- | --- |
| .NET Framework 4.5 | 378389 |
| .NET Framework 4.5.1 | 378675 |
| .NET Framework 4.5.2 | 379893 |
| .NET Framework 4.6 | 393295 |
| .NET Framework 4.6.1 | 394254 |
| .NET Framework 4.6.2 | 394802 |
| .NET Framework 4.7 | 460798 |
| .NET Framework 4.7.1 | 461308 |
| .NET Framework 4.7.2 | 461808 |
| .NET Framework 4.8 | 528040 |
| .NET Framework 4.8.1 | 533320 |

1. From the **Start** menu, choose **Run**, enter _regedit_, and then select **OK**.

(You must have administrative credentials to run regedit.)

1. In the Registry Editor, open the following subkey: **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full**. If the **Full** subkey isn't present, then you don't have .NET Framework 4.5 or later installed.

2. Check for a REG_DWORD entry named **Release**. If it exists, then you have .NET Framework 4.5 or later installed. Its value corresponds to a particular version of .NET Framework. In the following figure, for example, the value of the **Release** entry is 528040, which is the release key for .NET Framework 4.8.

![Image 1: A screenshot of the RegEdit tool showing the registry entry for .NET Framework 4.5](https://learn.microsoft.com/en-us/dotnet/framework/install/media/how-to-determine-which-versions-are-installed/clr-installdir.png)

Use PowerShell commands to check the value of the **Release** entry of the **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full** subkey.

The following examples check the value of the **Release** entry to determine whether .NET Framework 4.6.2 or later is installed. This code returns `True` if it's installed and `False` otherwise.

```
(Get-ItemPropertyValue -LiteralPath 'HKLM:SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full' -Name Release) -ge 394802
```

1. Use the [RegistryKey.OpenBaseKey](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.registrykey.openbasekey) and [RegistryKey.OpenSubKey](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.registrykey.opensubkey) methods to access the **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full** subkey in the Windows registry.

Important

If the app you're running is 32-bit and running in 64-bit Windows, the registry paths will be different than previously listed. The 32-bit registry is available in the *_HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\*_ subkey. For example, the registry subkey for .NET Framework 4.5 is **HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\NET Framework Setup\NDP\v4\Full**.
2.   Check the **Release** REG_DWORD value to determine the installed version. To be forward-compatible, check for a value greater than or equal to the value listed in the [.NET Framework version table](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#version_table).

The following example checks the value of the **Release** entry in the registry to find the versions of .NET Framework 4.5-4.8.1 that are installed.

Tip

Add the directive `using Microsoft.Win32` or `Imports Microsoft.Win32` at the top of your code file if you haven't already done so.

```
const string subkey = @"SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full\";

using (RegistryKey baseKey = RegistryKey.OpenBaseKey(RegistryHive.LocalMachine, RegistryView.Registry32))
using (RegistryKey ndpKey = baseKey.OpenSubKey(subkey))
{
    if (ndpKey != null && ndpKey.GetValue("Release") != null)
        Console.WriteLine($".NET Framework Version: {CheckFor45PlusVersion((int)ndpKey.GetValue("Release"))}");
    else
        Console.WriteLine(".NET Framework Version 4.5 or later is not detected.");
}

// Checking the version using >= enables forward compatibility.
string CheckFor45PlusVersion(int releaseKey)
{
    if (releaseKey >= 533320) return "4.8.1 or later";
    if (releaseKey >= 528040) return "4.8";
    if (releaseKey >= 461808) return "4.7.2";
    if (releaseKey >= 461308) return "4.7.1";
    if (releaseKey >= 460798) return "4.7";
    if (releaseKey >= 394802) return "4.6.2";
    if (releaseKey >= 394254) return "4.6.1";
    if (releaseKey >= 393295) return "4.6";
    if (releaseKey >= 379893) return "4.5.2";
    if (releaseKey >= 378675) return "4.5.1";
    if (releaseKey >= 378389) return "4.5";

    // This code should never execute. A non-null release key should mean
    // that 4.5 or later is installed.
    return "No 4.5 or later version detected";
}
```

The example displays output like the following:

```
.NET Framework Version: 4.6.1
```

The following example uses PowerShell to check the value of the **Release** entry in the registry to find the versions of .NET Framework 4.5-4.8.1 that are installed:

```
$release = Get-ItemPropertyValue -LiteralPath 'HKLM:SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full' -Name Release
switch ($release) {
    { $_ -ge 533320 } { $version = '4.8.1 or later'; break }
    { $_ -ge 528040 } { $version = '4.8'; break }
    { $_ -ge 461808 } { $version = '4.7.2'; break }
    { $_ -ge 461308 } { $version = '4.7.1'; break }
    { $_ -ge 460798 } { $version = '4.7'; break }
    { $_ -ge 394802 } { $version = '4.6.2'; break }
    { $_ -ge 394254 } { $version = '4.6.1'; break }
    { $_ -ge 393295 } { $version = '4.6'; break }
    { $_ -ge 379893 } { $version = '4.5.2'; break }
    { $_ -ge 378675 } { $version = '4.5.1'; break }
    { $_ -ge 378389 } { $version = '4.5'; break }
    default { $version = $null; break }
}

if ($version) {
    Write-Host -Object ".NET Framework Version: $version"
} else {
    Write-Host -Object '.NET Framework Version 4.5 or later is not detected.'
}
```

This example follows the recommended practice for version checking:

* It checks whether the value of the **Release** entry is _greater than or equal to_ the value of the known release values.
* It checks in order from most recent version to earliest version.

Each version of .NET Framework from 1.1 to 4.0 is listed as a subkey at **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP**. The following table lists the path to each .NET Framework version. For most versions, there's an **Install** REG_DWORD value of `1` to indicate this version is installed. In these subkeys, there's also a **Version** REG_SZ value that contains a version string.

Note

The **NET Framework Setup** subkey in the registry path does _not_ begin with a period.

| Framework Version | Registry Subkey | Value |
| --- | --- | --- |
| 1.0 | **HKLM\Software\Microsoft\.NETFramework\Policy\v1.0\3705** | **Install** REG_SZ equals `1` |
| 1.1 | **HKLM\Software\Microsoft\NET Framework Setup\NDP\v1.1.4322** | **Install** REG_DWORD equals `1` |
| 2.0 | **HKLM\Software\Microsoft\NET Framework Setup\NDP\v2.0.50727** | **Install** REG_DWORD equals `1` |
| 3.0 | **HKLM\Software\Microsoft\NET Framework Setup\NDP\v3.0\Setup** | **InstallSuccess** REG_DWORD equals `1` |
| 3.5 | **HKLM\Software\Microsoft\NET Framework Setup\NDP\v3.5** | **Install** REG_DWORD equals `1` |
| 4.0 Client Profile | **HKLM\Software\Microsoft\NET Framework Setup\NDP\v4\Client** | **Install** REG_DWORD equals `1` |
| 4.0 Full Profile | **HKLM\Software\Microsoft\NET Framework Setup\NDP\v4\Full** | **Install** REG_DWORD equals `1` |

Important

If the app you're running is 32-bit and running in 64-bit Windows, the registry paths will be different than previously listed. The 32-bit registry is available in the *_HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\*_ subkey. For example, the registry subkey for .NET Framework 3.5 is **HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\NET Framework Setup\NDP\v3.5**.

Notice that the registry path to the .NET Framework 1.0 subkey is different from the others.

1. From the **Start** menu, choose **Run**, enter _regedit_, and then select **OK**.

You must have administrative credentials to run regedit.

1. Open the subkey that matches the version you want to check. Use the table in the [.NET Framework 1.0-4.0](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#net-framework-10-40) section.

The following figure shows the subkey and its **Version** value for .NET Framework 3.5.

![Image 2: A screenshot of the RegEdit tool showing the registry entry for .NET Framework 3.5](https://learn.microsoft.com/en-us/dotnet/framework/install/media/how-to-determine-which-versions-are-installed/net-4-and-earlier.png)

Use the [Microsoft.Win32.RegistryKey](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.registrykey) class to access the **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP** subkey in the Windows registry.

Important

If the app you're running is 32-bit and running in 64-bit Windows, the registry paths will be different than previously listed. The 32-bit registry is available in the *_HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\*_ subkey. For example, the registry subkey for .NET Framework 3.5 is **HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\NET Framework Setup\NDP\v3.5**.

The following example finds the versions of .NET Framework 1-4 that are installed:

```
// Open the registry key for the .NET Framework entry. Dispose this object when done.
RegistryKey ndpKey =
    RegistryKey.OpenBaseKey(RegistryHive.LocalMachine, RegistryView.Registry32)
        .OpenSubKey(@"SOFTWARE\Microsoft\NET Framework Setup\NDP\");

foreach (string versionKeyName in ndpKey.GetSubKeyNames())
{
    // Skip .NET Framework 4.5 version information.
    if (versionKeyName == "v4")
        continue;

    if (versionKeyName.StartsWith("v"))
    {
        RegistryKey versionKey = ndpKey.OpenSubKey(versionKeyName);

        // Get the .NET Framework version value.
        string name = versionKey.GetValue("Version", "").ToString();

        // Get the service pack (SP) number.
        string sp = versionKey.GetValue("SP", "").ToString();

        // Get the installation flag.
        string install = versionKey.GetValue("Install", "").ToString();

        if (string.IsNullOrEmpty(install))
        {
            // No install info; it must be in a child subkey.
            Console.WriteLine($"{versionKeyName}  {name}");
        }
        else if (install == "1")
        {
            // Install = 1 means the version is installed.
            if (!string.IsNullOrEmpty(sp))
                Console.WriteLine($"{versionKeyName}  {name}  SP{sp}");
            else
                Console.WriteLine($"{versionKeyName}  {name}");
        }

        if (!string.IsNullOrEmpty(name))
        {
            versionKey.Dispose();
            continue;
        }

        // Iterate through the subkeys of the version subkey.
        foreach (string subKeyName in versionKey.GetSubKeyNames())
        {
            RegistryKey subKey = versionKey.OpenSubKey(subKeyName);
            name = subKey.GetValue("Version", "").ToString();

            if (!string.IsNullOrEmpty(name))
                sp = subKey.GetValue("SP", "").ToString();

            install = subKey.GetValue("Install", "").ToString();

            if (string.IsNullOrEmpty(install))
            {
                // No install info; it must be later.
                Console.WriteLine($"  {versionKeyName}  {name}");
            }
            else if (install == "1")
            {
                if (!string.IsNullOrEmpty(sp))
                    Console.WriteLine($"  {subKeyName}  {name}  SP{sp}");
                else
                    Console.WriteLine($"  {subKeyName}  {name}");
            }

            // Clean up the subkey object.
            subKey.Dispose();
        }

        versionKey.Dispose();
    }
}

ndpKey.Dispose();
```

The example displays output similar to the following:

```
v2.0.50727  2.0.50727.4927  SP2
v3.0  3.0.30729.4926  SP2
v3.5  3.5.30729.4926  SP1
v4.0
  Client  4.0.0.0
```

The following example uses PowerShell to check the value of the **Release** entry in the registry to find the versions of .NET Framework 1-4 that are installed:

```
Get-ChildItem -Path 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' |
Where-Object { ($_.PSChildName -ne "v4") -and ($_.PSChildName -like 'v*') } |
ForEach-Object {
    $name = $_.Version
    $sp = $_.SP
    $install = $_.Install
    if (-not $install) {
        Write-Host -Object "$($_.PSChildName)  $($name)"
    }
    elseif ($install -eq '1') {
        if (-not $sp) {
            Write-Host -Object "$($_.PSChildName)  $($name)"
        }
        else {
            Write-Host -Object "$($_.PSChildName)  $($name) SP$($sp)"
        }
}
    if (-not $name) {
        $parentName = $_.PSChildName
        Get-ChildItem -LiteralPath $_.PSPath |
        Where-Object {
            if ($_.Property -contains 'Version') { $name = $((Get-ItemProperty -Path "Registry::$_").Version) }
            if ($name -and ($_.Property -contains 'SP')) { $sp = $((Get-ItemProperty -Path "Registry::$_").SP) }
            if ($_.Property -contains 'Install') { $install = $((Get-ItemProperty -Path "Registry::$_").Install) }
            if (-not $install) {
                Write-Host -Object "  $($parentName)  $($name)"
            }
            elseif ($install -eq '1') {
                if (-not $sp) {
                    Write-Host -Object "  $($_.PSChildName)  $($name)"
                }
                else {
                    Write-Host -Object "  $($_.PSChildName)  $($name) SP$($sp)"
                }
            }
        }
    }
}
```

The .NET Framework CLR installed with .NET Framework is versioned separately. There are two ways to detect the version of the .NET Framework CLR:

* [The Clrver.exe tool](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#the-clrverexe-tool)
* [The `Environment.Version` property](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#the-environmentversion-property)

Use the [CLR Version tool (Clrver.exe)](https://learn.microsoft.com/en-us/dotnet/framework/tools/clrver-exe-clr-version-tool) to determine which versions of the CLR are installed on a computer. Open [Visual Studio Developer Command Prompt or Visual Studio Developer PowerShell](https://learn.microsoft.com/en-us/visualstudio/ide/reference/command-prompt-powershell) and enter `clrver`.

Sample output:

```
Versions installed on the machine:
v2.0.50727
v4.0.30319
```

Important

For .NET Framework 4.5 and later versions, don't use the [Environment.Version](https://learn.microsoft.com/en-us/dotnet/api/system.environment.version#system-environment-version) property to detect the version of the CLR. Instead, query the registry as described in [.NET Framework 4.5 and later versions](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#net-framework-45-and-later-versions).

1. Query the [Environment.Version](https://learn.microsoft.com/en-us/dotnet/api/system.environment.version#system-environment-version) property to retrieve a [Version](https://learn.microsoft.com/en-us/dotnet/api/system.version) object.

The returned `System.Version` object identifies the version of the runtime that's currently executing the code. It doesn't return assembly versions or other versions of the runtime that may have been installed on the computer.

For .NET Framework versions 4, 4.5, 4.5.1, and 4.5.2, the string representation of the returned [Version](https://learn.microsoft.com/en-us/dotnet/api/system.version) object has the form 4.0.30319._xxxxx_, where _xxxxx_ is less than 42000. For .NET Framework 4.6 and later versions, it has the form 4.0.30319.42000.

1. After you have the **Version** object, query it as follows:

    *   For the major release identifier (for example, _4_ for version 4.0), use the [Version.Major](https://learn.microsoft.com/en-us/dotnet/api/system.version.major#system-version-major) property.
    *   For the minor release identifier (for example, _0_ for version 4.0), use the [Version.Minor](https://learn.microsoft.com/en-us/dotnet/api/system.version.minor#system-version-minor) property.
    *   For the entire version string (for example, _4.0.30319.18010_), use the [Version.ToString](https://learn.microsoft.com/en-us/dotnet/api/system.version.tostring) method. This method returns a single value that reflects the version of the runtime that's executing the code. It doesn't return assembly versions or other runtime versions that may be installed on the computer.

The following example uses the [Environment.Version](https://learn.microsoft.com/en-us/dotnet/api/system.environment.version#system-environment-version) property to retrieve CLR version information:

```
Console.WriteLine($"Version: {Environment.Version}");
```

The example displays output similar to the following:

```
Version: 4.0.30319.18010
```

* [How to: Determine which .NET Framework updates are installed](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-net-framework-updates-are-installed)
* [Troubleshoot: Determine which versions and service packs of .NET Framework are installed](https://learn.microsoft.com/en-us/troubleshoot/developer/dotnet/framework/general/determine-dotnet-versions-service-pack-levels)
* [Install .NET Framework for developers](https://learn.microsoft.com/en-us/dotnet/framework/install/guide-for-developers)
* [.NET Framework versions and dependencies](https://learn.microsoft.com/en-us/dotnet/framework/install/versions-and-dependencies)
