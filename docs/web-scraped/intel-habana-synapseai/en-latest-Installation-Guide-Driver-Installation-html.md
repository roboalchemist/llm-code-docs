# Source: https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html

Title: Driver and Software Installation — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html

Markdown Content:
Driver and Software Installation[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#driver-and-software-installation "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following sections describe how to obtain and install Intel® Gaudi® software and drivers.

Installation Options[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#installation-options "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------

The following lists the available options for driver and software installation:

*   **Install driver and software**: Installs all the packages automatically using `habanalabs-installer.sh` script. This is the recommended installation method.

*   **Upgrade driver and software**: Enables upgrading an existing installation to the latest version.

*   **Custom driver and software installation**: Allows installing each package manually for a fine-grained control over the installation process.

Note

*   Make sure to review the currently supported versions and operating systems listed in the [Support Matrix](https://docs.habana.ai/en/latest/Support_Matrix/Support_Matrix.html#support-matrix).

*   Driver and software installation is not required if you are using the Intel Gaudi Base Operator for Kubernetes or OpenShift.

*   Installing the package with internet connection available allows the network to download and install the required dependencies for the Intel Gaudi software package (apt get, yum, dnf install or pip install etc.).

Install Driver and Software[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#install-driver-and-software "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Install the driver and software using `habanalabs-installer.sh` script. For further details on the package installers included, see [Intel Gaudi Software Installers](https://docs.habana.ai/en/latest/Installation_Guide/Installers_Appendix.html#software-installers) table. For OpenCloudOS, make sure the dkms package version is [3.3.0-1.el8](https://dl.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/d/dkms-3.3.0-1.el8.noarch.rpm) before running the below command.

> wget -nv https://vault.habana.ai/artifactory/gaudi-installer/1.23.0/habanalabs-installer.sh
> chmod +x habanalabs-installer.sh
> ./habanalabs-installer.sh install --type base
> 
> [![Image 1: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)

Note

    *   Make sure to update Linux kernel to the latest supported version **before** starting the installation of `habanalabs-installer.sh` script. If the kernel is updated **during** the driver installation, the script might fail. To resolve this, reboot the server to load the updated kernel, then rerun the `habanalabs-installer.sh` script to install the drivers.

    *   For further instructions on how to control the script attributes, refer to the help guide using `./habanalabs-installer.sh --help` command.

    *   Adding `--skip-driver-load` option to the installation command skips loading the drivers.

    *   The installation sets the number of huge pages automatically.

    *   `habanalabs-container-runtime` and `habanalabs-qual-workloads` are not automatically installed with the `habanalabs-installer.sh`. Make sure to install them as shown in the steps below. Additionally, `habanalabs-tools` is not automatically installed. If you are using TPC and writing your own kernels, refer to [TPC Tools Installation Guide](https://docs.habana.ai/en/latest/TPC/TPC_Tools_Installation/TPC_Tools_Installation_Guide.html#tpc-tools-installation) to install `habanalabs-tools` package.

2.   If needed, update the FW as described in [Firmware Upgrade](https://docs.habana.ai/en/latest/Installation_Guide/Firmware_and_Platform_Components/Firmware_Upgrade.html#system-unboxing-main).

3.   Install **optional** packages:

Ubuntu24.04.2/22.04.5

Install `habanalabs-container-runtime`. package. This package is required for running workloads in containers. Both Docker and Kubernetes are supported:

 sudo apt install -y habanalabs-container-runtime

[![Image 2: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
Install `habanalabs-qual-workloads` package. This package is required for running ResNet-50 training stress test plugin:

 sudo apt install -y habanalabs-qual-workloads

[![Image 3: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
Install Python and MPI dependencies. This is required for running power stress and EDP tests:

 ./habanalabs-installer.sh install -t deps -y -v

[![Image 4: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
Install `ethtool` if you are running a multi-server scale-out and need to bring up the accelerator interfaces:

 sudo apt install -y ethtool

[![Image 5: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)  
Navix9.4/ OpenCloudOS9.2/ RHEL9.4/9.6/ TencentOS 3.1

Install `habanalabs-container-runtime`. package. This package is required for running workloads in containers. Both Docker and Kubernetes are supported:

 sudo dnf install -y habanalabs-container-runtime

[![Image 6: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
Install `habanalabs-qual-workloads` package. This package is required for running ResNet-50 training stress test plugin:

 sudo dnf install -y habanalabs-qual-workloads

[![Image 7: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
Install Python and MPI dependencies. This is required for running power stress and EDP tests:

 ./habanalabs-installer.sh install -t deps -y -v

[![Image 8: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
Install `ethtool` if you are running a multi-server scale-out and need to bring up the accelerator interfaces:

 sudo dnf install -y ethtool

[![Image 9: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)   

### Bring up Accelerator Interfaces[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#bring-up-accelerator-interfaces "Permalink to this headline")

If you are running a multi-server scale-out and have the accelerator interfaces physically connected, make sure the network interfaces are brought up. These interfaces need to be brought up every time the kernel module is loaded or unloaded and reloaded. A reference on how to bring up the interfaces is provided in the [manage_network_ifs.sh](https://github.com/HabanaAI/Setup_and_Install/tree/main/utils#manage_network_ifs). Note that the script can be found at `/opt/habanalabs/qual/[gaudi3,gaudi2,gaudi1]/bin/`.

1.   Bring up accelerator interfaces:

> # manage_network_ifs.sh requires ethtool
> /opt/habanalabs/qual/[gaudi3,gaudi2,gaudi1]/bin/manage_network_ifs.sh --up
> 
> [![Image 10: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)

2.   Check the accelerator interfaces status:

/opt/habanalabs/qual/[gaudi3,gaudi2,gaudi1]/bin/manage_network_ifs.sh --status

[![Image 11: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
Output example:

accel0
3 ports up (2, 3, 7)
accel1
3 ports up (17, 20, 21)
accel2
3 ports up (14, 15, 19)
accel3
3 ports up (5, 8, 9)
accel4
3 ports up (17, 20, 21)
accel5
3 ports up (2, 3, 7)
accel6
3 ports up (5, 8, 9)
accel7
3 ports up (14, 15, 19)

[![Image 12: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) Note

The `accel[Number]` label indicates the index assigned to the OAM by the OS, which may change after a reboot or driver reload. The label corresponds to the `AIP`, `accel[Number]`, and `index` labels that the `hl-smi` tool outputs. For more details, see [System Management Interface Tool (hl-smi)](https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/System_Management_Interface_Tool.html#system-management-tools). 

### Set Environment Variables[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#set-environment-variables "Permalink to this headline")

To ensure proper operation, the following environment variables must be set:

export HABANALABS_HLTHUNK_TESTS_BIN_PATH=/opt/habanalabs/src/hl-thunk/tests/
export HABANA_LOGS=/var/log/habana_logs/
export RDMA_CORE_ROOT=/opt/habanalabs/rdma-core/src
export HABANA_PLUGINS_LIB_PATH=/usr/lib/habanatools/habana_plugins
export GC_KERNEL_PATH=/usr/lib/habanalabs/libtpc_kernels.so
export RDMA_CORE_LIB=/opt/habanalabs/rdma-core/src/build/lib
export HABANA_SCAL_BIN_PATH=/opt/habanalabs/engines_fw
export DATA_LOADER_AEON_LIB_PATH=/usr/lib/habanalabs/libaeon.so
export __python_cmd=python3

[![Image 13: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)

If these variables are already defined in the system-provided scripts, run the following command in your environment:

source /etc/profile.d/habanalabs*.sh

[![Image 14: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)

The command automatically exports all the variables listed above.

### Enable IOMMU Passthrough[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#enable-iommu-passthrough "Permalink to this headline")

Enabling IOMMU passthrough is required only for Ubuntu 24.04.2/22.04.5 with Linux kernel 6.8. Skip this section if a different OS or kernel version is used.

To enable IOMMU passthrough:

1.   Add `GRUB_CMDLINE_LINUX_DEFAULT="iommu=pt intel_iommu=on"` to `/etc/default/grub`.

2.   Run `sudo update-grub`.

3.   Reboot the system.

For more details, see [Ubuntu documentation](https://bugs.launchpad.net/ubuntu/+source/linux-gcp-6.8/+bug/2085904).

### Set CPU Setting to Performance[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#set-cpu-setting-to-performance "Permalink to this headline")

**BIOS Configuration Requirement for CPU Frequency Scaling**

To enable the operating system to manage CPU performance states dynamically, the system BIOS must expose and allow control over CPU frequency scaling features. Specifically, the BIOS must support ACPI CPU frequency scaling interfaces and not restrict access to performance states (P-states) or governors. This ensures that the OS can read and modify the CPU frequency governor settings via `cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`. Without proper BIOS support, this interface may be unavailable or return errors, preventing the OS from applying desired power or performance policies.

The below is an example of setting the CPU to performance for Ubuntu:

#Get setting:
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

#Set setting:
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

[![Image 15: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)

Note

The CPU settings must be updated on bare metal before starting the container.

#### Update CPU Settings[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#update-cpu-settings "Permalink to this headline")

This section describes how to update CPU settings on Gaudi 3 using Sapphire and Granite Rapids to optimize performance.

1.   Set Energy Perf BIAS:

wrmsr -a 0x1b0 0x0

[![Image 16: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
2.   Set the Core Frequency (HWP):

wrmsr -a 0x774 0x2708

[![Image 17: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 

Note

*   When using a Supermicro SYS-822GA-NGR3 system, update the BIOS to version 1.3 or newer to access the BIOS settings below.

*   Enumerated lists that are auto-numbered start with `#.`.

1.   Disable SubNUMA in BIOS by navigating to **Advanced → Chipset Configuration → Uncore Configuration → SNC [Disabled]**.

2.   Disable the C6 state:

Note

The C6P state may not be supported on all systems. To view the available states, run the following:

> cat /sys/devices/system/cpu/cpu*/cpuidle/state*/name
> 
> [![Image 18: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 

Runtime Setup

echo 1 | tee /sys/devices/system/cpu/cpu*/cpuidle/state2/disable

[![Image 19: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
BIOS Setup

    1.   Disable C1 to C1E Promotion by navigating to **Advanced → CPU Configuration → Advanced Power Management Configuration → CPU C State Control → C1 to C1E Promotion [Disabled]**.

    2.   Disable ACPI C6x Enumeration by navigating to **Advanced → CPU Configuration → Advanced Power Management Configuration → CPU C State Control → ACPI C6x Enumeration [Disabled]**.

    3.   Set Package C State by navigating to **Advanced → CPU Configuration → Advanced Power Management Configuration → Package C State Control → Package C State [C0/C1 state]**.

3.   Set Latency Optimized Mode (LOM). This can be done either by cloning [Intel® PCM API](https://github.com/intel/pcm.git) or in BIOS:

pcm.git

> cd ~
> git clone --recursive https://github.com/intel/pcm
> cd pcm
> git submodule update --init --recursive
> mkdir build
> cd build
> cmake ..
> cmake --build .
> sudo cp ./bin/pcm-tpmi /usr/local/bin/pcm-tpmi
> cd ~/pcm/scripts
> sudo bash ./bhs-power-mode.sh --latency-optimized-mode
> 
> [![Image 20: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)

For more details, see [Building PCM Tools](https://github.com/intel/pcm/blob/master/README.md#building-pcm-tools). 
BIOS Setup

Navigate to **Advanced → CPU Configuration → Advanced Power Management Configuration → Latency Optimized Mode [Enabled]**. 
4.   Set Energy Perf BIAS:

Runtime Setup

echo 0 | sudo tee /sys/devices/system/cpu/cpu*/power/energy_perf_bias

[![Image 21: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 
BIOS Setup

    1.   Disable Workload Profile by navigating to **Advanced → CPU Configuration → Advanced Power Management Configuration → Workload Profile [Disabled]**.

    2.   Configure Power Performance Tuning by navigating to **Advanced → CPU Configuration → Advance Power Management Configuration → Power Performance Tuning [BIOS Controls EPB]**.

    3.   Configure ENERGY_PERF_BIAS_CFG Mode by navigating to **Advanced → CPU Configuration → Advanced Power Management Configuration → ENERGY_PERF_BIAS_CFG Mode [Performance]**.

5.   Set the Core Frequency (HWP)

wrmsr -a 0x774 0x2708

[![Image 22: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html) 

Upgrade Driver and Software[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#upgrade-driver-and-software "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Upgrade the driver and software:

> wget -nv https://vault.habana.ai/artifactory/gaudi-installer/1.23.0/habanalabs-installer.sh
>  chmod +x habanalabs-installer.sh
>  ./habanalabs-installer.sh upgrade --type base
> 
> [![Image 23: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)

2.   Perform Steps 2 from the previous section [Install Driver and Software](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#install-intel-gaudi-sw-stack) to complete the upgrade.

Custom Driver and Software Installation[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#custom-driver-and-software-installation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To install each package individually, refer to [Custom Driver and Software Installation](https://docs.habana.ai/en/latest/Installation_Guide/Custom_Driver_and_Software_Installation.html#custom-driver-and-software-installation).

Note

While you can install each package manually, using the `habanalabs-installer.sh` script is the recommended method for installation. For further details, see [Driver and Software Installation](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#driver-installation).

Open Source Components and Source Code[¶](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#open-source-components-and-source-code "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following table lists the open-source components, with direct links to their respective source code repositories and supporting documentation.

| Component | Source Code |
| --- | --- |
| gaudi-metric-exporter | [https://hub.docker.com/r/intel/gaudi-metric-exporter](https://hub.docker.com/r/intel/gaudi-metric-exporter) |
| Intel Gaudi Device Plugin | [https://hub.docker.com/r/intel/gaudi-device-plugin](https://hub.docker.com/r/intel/gaudi-device-plugin) |
| Chromium | [https://vault.habana.ai/artifactory/misc/chromium/chromium-third-parties-srcs.tar.gz](https://vault.habana.ai/artifactory/misc/chromium/chromium-third-parties-srcs.tar.gz) |
| gohlml | [https://github.com/HabanaAI/gohlml](https://github.com/HabanaAI/gohlml) |
| hlml | [https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/hl-smi-SA.tgz](https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/hl-smi-SA.tgz) |
| hl-smi | [https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/hl-smi-SA.tgz](https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/hl-smi-SA.tgz) |
| hl-smi-async | [https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/hl-smi-SA.tgz](https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/hl-smi-SA.tgz) |
| hl-fw-loader | [https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/fwl-SA.tgz](https://vault.habana.ai/artifactory/misc/fw-tools-sources/1.23.0/fwl-SA.tgz) |
| Intel Gaudi Docker Images | [https://vault.habana.ai/artifactory/misc/source_packages/1.23.0-695/pytorch-installer/](https://vault.habana.ai/artifactory/misc/source_packages/1.23.0-695/pytorch-installer/) |
| hl_qual | N/A |
