# Source: https://help.aikido.dev/virtual-machine-scanning/local-vm-scanning/setting-up-the-local-vm-scanner-windows.md

# Setting Up the Local VM Scanner on Windows

Aikido VM Scanner is a single-package that installs on your system, automatically scanning and identifying dependencies to provide a detailed view into your environment.

### Prerequisites

* Minimum system requirements: at least 1GB RAM.
* Preferred system requirements: at least 2GB RAM and 4 CPUs.
* Ensure you have admin privileges on your system
* Make sure to use the appropriate commands for your system or cloud provider
* [On Windows, ensure that PowerShell is installed and enabled](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5)

### Installation and Upgrade

Start PowerShell in admin mode, replace `AIKIDO_TOKEN` with [valid token from Local VM scanning page in Aikido](https://app.aikido.dev/settings/integrations/vm-scan-agent). You can also specify the following optional parameters:

* `VM_TYPE` as one of: `production`, `staging` or `development`.
* `OUTPUT` as one of: `stdout`, `stderr` or `none` .

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri "https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/v1.4.0/AikidoVmScanner.msi" -OutFile "AikidoVmScanner.msi"
msiexec /i AikidoVmScanner.msi /qn /norestart AIKIDO_TOKEN=REPLACE_ME VM_TYPE=production OUTPUT=stderr
```

<table><thead><tr><th width="99.64453125">Hash</th><th>AikidoVmScanner.msi</th></tr></thead><tbody><tr><td>MD5</td><td>9f2af33ccc6b7dc53fa6b23c6c31a04c</td></tr><tr><td>SHA256</td><td>b93ab7e61c0c1c7b666623210da02e0827eae15efe9399f8ee6f1b12d1ede3e5</td></tr></tbody></table>

If you have an automated process for installation and you always want to be on the latest version, you can use the following link:

* <https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/latest/AikidoVmScanner.msi>

The VM Scanner Agent runs once a day, at a random time between **4:00 AM - 8:00 AM** (machine time).&#x20;

After install, **a first scan will start automatically**. If you want to run it on demand, you can manually execute it with the following command in a PowerShell with admin privileges.&#x20;

```powershell
& 'C:\Program Files\AikidoVmScanner\AikidoVmScanner.exe'
```

### Uninstall

Start PowerShell in admin mode and run:

```powershell
msiexec.exe /x (Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "AikidoVmScanner*" }).IdentifyingNumber /qn /norestart
```

### Logs

Logs are available here, along with the last generated SBOM:  `C:\ProgramData\AikidoVmScanner\Logs`
