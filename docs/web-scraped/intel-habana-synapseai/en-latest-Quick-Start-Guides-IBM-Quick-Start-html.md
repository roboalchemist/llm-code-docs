# Source: https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html

Title: IBM Cloud Quick Start Guide — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html

Markdown Content:
IBM Cloud Quick Start Guide[¶](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html#ibm-cloud-quick-start-guide "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

This document provides instructions for setting up the Intel® Gaudi® 3 AI accelerator instance on the IBM Cloud®, installing Intel Gaudi driver and software, and running inference using the Optimum for Intel Gaudi library and the vLLM Inference Server.

Create a Gaudi 3 Instance[¶](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html#create-a-gaudi-3-instance "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the below step-by-step instructions to launch a Gaudi 3 instance on the IBM Cloud.

1.   From the IBM Cloud console, go to “Infrastructure > Compute > Virtual server instances”:

![Image 1: ../_images/Virtural_Services.png](https://docs.habana.ai/en/latest/_images/Virtural_Services.png)

2.   Select the region and click “Create”. For additional information on availability in a region, refer to [this page](https://cloud.ibm.com/docs/vpc?topic=vpc-accelerated-profile-family&interface=ui#gaudi-3-profiles):

![Image 2: ../_images/Region_Create.png](https://docs.habana.ai/en/latest/_images/Region_Create.png)

3.   Confirm your geography, Region, and Zone. Name the instance, and select a “gaudi3” resource group:

![Image 3: ../_images/Location_and_Details.png](https://docs.habana.ai/en/latest/_images/Location_and_Details.png)

4.   Navigate down to “Server configuration”, click “Change image” and select your desired image. After your image is selected, click “Change profile”:

![Image 4: ../_images/Server_Configuration.png](https://docs.habana.ai/en/latest/_images/Server_Configuration.png)

5.   In the left-hand side navigation check the “GPU” box. Select the GPU gx3d-160x1792x8gaudi3 profile from the available GPUs, and click “Save”:

![Image 5: ../_images/Select_Instance_Profile.png](https://docs.habana.ai/en/latest/_images/Select_Instance_Profile.png)

6.   Create or select an SSH key that was previously created. Boot drive is pre-configured, but you can add additional data drives by clicking “Create” and filling out the size of the drive:

![Image 6: ../_images/SSH_keys.png](https://docs.habana.ai/en/latest/_images/SSH_keys.png)

7.   Under “Networking”, you can either use the default generated VPC or create your own by clicking “Create VPC”. The “Virtual network interface” is preselected and is recommended:

![Image 7: ../_images/Networking.png](https://docs.habana.ai/en/latest/_images/Networking.png)

8.   You can add up to 15 interfaces, with a maximum total server bandwidth of 150 Gbps:

![Image 8: ../_images/Bandwidth.png](https://docs.habana.ai/en/latest/_images/Bandwidth.png)

9.   Click “Create virtual server” and begin provisioning. Note that due to the size of the virtual server, it may take up to 20 minutes to complete starting up:

> ![Image 9: ../_images/Create_Virtual_Server.png](https://docs.habana.ai/en/latest/_images/Create_Virtual_Server.png)

1.   Navigate to “Infrastructure > Network > Floating IPs”:

![Image 10: ../_images/Floating_IPs.png](https://docs.habana.ai/en/latest/_images/Floating_IPs.png)

2.   To reserve your Floating IP, select the region that you deployed the “Virtual server instances”, fill in the Floating IP name, and click “Reserve”:

![Image 11: ../_images/Reserve_Floating_IP.png](https://docs.habana.ai/en/latest/_images/Reserve_Floating_IP.png)

3.   Now that you have a Floating IP, bind it to the “Virtual server instances”. Click on the name of the reserved IP:

![Image 12: ../_images/Floating_IP_details.png](https://docs.habana.ai/en/latest/_images/Floating_IP_details.png)

4.   From the “Actions” dropdown menu, click “Bind”:

![Image 13: ../_images/Bind.png](https://docs.habana.ai/en/latest/_images/Bind.png)

5.   From the dropdown menu, select the Virtual server instance you want to bind the Floating IP to and click “Bind”:

![Image 14: ../_images/Bind_Floating_IP.png](https://docs.habana.ai/en/latest/_images/Bind_Floating_IP.png)

6.   You now have a fully deployed Gaudi 3 instance with a Floating IP attached:

![Image 15: ../_images/Binding_completed.png](https://docs.habana.ai/en/latest/_images/Binding_completed.png)

1.   Using the Floating IP address that you created, ping your instance to make sure that it’s up and running:

ping <public-ip-address>

[![Image 16: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
2.   Because you created your instance with a public SSH key, you can now connect to it directly by using your private key:

ssh -i <path-to-private-key-file> root@<public-ip-address>

[![Image 17: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 

System Setup - RHEL[¶](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html#system-setup-rhel "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------

From your Gaudi instance, verify that all the Gaudi 3 devices are connected:

lspci -d 1da3: -nn

[![Image 18: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)

The output should appear as follows:

a3:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
ad:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
b7:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
c1:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
cb:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
d5:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
df:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
e9:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)

[![Image 19: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)

Note

The system is pre-installed with RHEL 9.4 OS. The following instructions are intended for RHEL 9.4 but also apply to RHEL 9.2.

This section provides two installation options for the Intel Gaudi driver and software. Follow the appropriate installation steps based on your system requirements.

Using the Pre-installed Kernel (recommended)

> 1.   Verify the installed kernel version:
> 
> sudo dnf list installed | grep kernel
> 
> [![Image 20: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> The output should appear as follows:
> 
> kernel-core.x86_64            5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-modules.x86_64         5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-modules-core.x86_64    5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-tools.x86_64           5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-tools-libs.x86_64      5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> 
> [![Image 21: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) Note
> 
> 
> The output example displays the kernel version installed on RHEL 9.4. The output may vary depending on the RHEL version in use. 
> 2.   Verify the available kernel packages that match the kernel version retrieved in Step 1.
> 
> sudo dnf list --showduplicates | grep 5.14.0-427.50.1.el9_4
> 
> [![Image 22: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 3.   Install the kernel development and header packages. Ensure they match the currently installed kernel version:
> 
> sudo dnf install kernel-devel-5.14.0-427.50.1.el9_4.x86_64 kernel-devel-matched-5.14.0-427.50.1.el9_4.x86_64 kernel-headers-5.14.0-427.50.1.el9_4.x86_64
> 
> [![Image 23: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 4.   Install the `wget` utility:
> 
> sudo dnf install -y wget
> 
> [![Image 24: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 5.   Download the `habanalabs-installer.sh` script:
> 
>    sudo wget -nv https://vault.habana.ai/artifactory/gaudi-installer/1.23.0/habanalabs-installer.sh
>    sudo chmod +x habanalabs-installer.sh
> 
> [![Image 25: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 6.   Install the EPEL repository:
> 
> sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm --nogpgcheck
> 
> [![Image 26: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> The EPEL repository provides access to extra packages that are not included in the default RHEL repositories.
> 
> 7.   Install Intel Gaudi driver and software:
> 
> sudo ./habanalabs-installer.sh install --type base
> 
> [![Image 27: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 8.   Click “Y” when you see `Prepare installation` to finish the installation - it will not complete until you confirm.

To verify that the installation is successful, follow the steps outlined in the [System Verifications and Final Tests](https://docs.habana.ai/en/latest/Installation_Guide/System_Verification_and_Final_Tests.html#system-verification) section.

Using the Latest Kernel (optional)

> 1.   Install the EPEL repository:
> 
> sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm --nogpgcheck
> 
> [![Image 28: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> The EPEL repository provides access to extra packages that are not included in the default RHEL repositories.
> 
> 2.   Verify the installed kernel version:
> 
> sudo dnf list installed | grep kernel
> 
> [![Image 29: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> The output should appear as follows:
> 
> kernel-core.x86_64            5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-modules.x86_64         5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-modules-core.x86_64    5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-tools.x86_64           5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> kernel-tools-libs.x86_64      5.14.0-427.50.1.el9_4    @rhel-9-for-x86_64-baseos-eus-rpms
> 
> [![Image 30: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) Note
> 
> 
> The output example displays the kernel version installed on RHEL 9.4. The output may vary depending on the RHEL version in use. 
> 3.   Verify the available kernel packages that match the kernel version retrieved in Step 2.
> 
> sudo dnf list --showduplicates | grep 5.14.0-427.50.1.el9_4
> 
> [![Image 31: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 4.   Install the kernel development and header packages. Ensure they match the currently installed kernel version:
> 
> sudo dnf install kernel-devel-5.14.0-427.50.1.el9_4.x86_64 kernel-devel-matched-5.14.0-427.50.1.el9_4.x86_64 kernel-headers-5.14.0-427.50.1.el9_4.x86_64
> 
> [![Image 32: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 5.   Reboot the system:
> 
> sudo reboot
> 
> [![Image 33: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 6.   After 10 minutes, log in to your machine and update the software package manager (dnf) and kernels:
> 
> sudo dnf update –y
> 
> [![Image 34: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 7.   Install the `wget` utility:
> 
> sudo dnf install -y wget
> 
> [![Image 35: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 8.   Download the `habanalabs-installer.sh` script:
> 
>    sudo wget -nv https://vault.habana.ai/artifactory/gaudi-installer/1.23.0/habanalabs-installer.sh
>    sudo chmod +x habanalabs-installer.sh
> 
> [![Image 36: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 9.   Install Intel Gaudi driver and software:
> 
> sudo ./habanalabs-installer.sh install --type base
> 
> [![Image 37: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
> 10.   Click “Y” when you see `Prepare installation` to finish the installation - it will not complete until you confirm.

To verify that the installation is successful, follow the steps outlined in the [System Verifications and Final Tests](https://docs.habana.ai/en/latest/Installation_Guide/System_Verification_and_Final_Tests.html#system-verification) section.

The following steps are required only once to set up the Docker engine, Gaudi container runtime, and the Gaudi container itself.

Note

The steps below are based on the [recommended](https://docs.docker.com/engine/install/rhel/#install-using-the-repository) method from the official Docker website.

1.   Remove the existing Docker packages:

sudo dnf remove docker \
            docker-client \
            docker-client-latest \
            docker-common \
            docker-latest \
            docker-latest-logrotate \
            docker-logrotate \
            docker-engine \
            podman \
            runc

[![Image 38: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
2.   Install the `dnf-plugins-core` package:

sudo dnf -y install dnf-plugins-core

[![Image 39: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
3.   Add the Docker repository in the `config-manager`:

sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

[![Image 40: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
4.   Install the Docker packages:

sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

[![Image 41: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
5.   Start the Docker engine:

sudo systemctl enable --now docker

[![Image 42: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
6.   Verify that the installation is successful by running the `hello-world` image:

sudo docker run hello-world

[![Image 43: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
7.   Install `habanalabs-container-runtime` package. This package is required for running workloads in containers. Both Docker and Kubernetes are supported:

sudo dnf install -y habanalabs-container-runtime

[![Image 44: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
8.   Register `habana-container-runtime` by adding the following to `etc/docker/daemon.json` as mentioned in the [Docker Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Docker_Installation.html#docker-installation) section:

sudo tee /etc/docker/daemon.json <<EOF
{
   "runtimes": {
      "habana": {
            "path": "/usr/bin/habana-container-runtime",
            "runtimeArgs": []
      }
   }
}
EOF

[![Image 45: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
9.   Add your user to the Docker group:

sudo usermod -aG docker $USER

[![Image 46: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
10.   Reload daemon:

sudo systemctl daemon-reload

[![Image 47: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
11.   Restart the Docker service:

sudo systemctl restart docker

[![Image 48: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
12.   Install the latest Gaudi Docker container:

sudo docker run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none \
-v /run/:/run -v /dev/shm:/dev/shm --cap-add=sys_nice --net=host --ipc=host \
vault.habana.ai/gaudi-docker/1.23.0/rhel9.4/habanalabs/pytorch-installer-2.9.0:latest

[![Image 49: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
The **no hostkeys available** message can be safely ignored. You should now be inside the container.

System Setup - Ubuntu[¶](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html#system-setup-ubuntu "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------

From your Gaudi instance, verify that all the Gaudi 3 devices are connected:

lspci -d 1da3: -nn

[![Image 50: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)

The output should appear as follows:

a3:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
ad:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
b7:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
c1:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
cb:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
d5:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
df:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)
e9:00.0  Processing accelerators [1200]:  Habana Labs Ltd.  Device [1da3:1060]  (rev 01)

[![Image 51: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)

Note

The system is pre-installed with Ununtu 24.04.2 OS. The following instructions are intended for Ubuntu 24.04.2 but also apply to Ubuntu 22.04.5.

1.   Update apt and upgrade the packages. If a menu appears, select OK and continue:

sudo apt update && sudo apt -y upgrade

[![Image 52: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
2.   Reboot the system:

sudo reboot

[![Image 53: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
3.   After 10 minutes, reconnect to the system and download the `habanalabs-installer.sh` script:

   wget -nv https://vault.habana.ai/artifactory/gaudi-installer/1.23.0/habanalabs-installer.sh
   chmod +x habanalabs-installer.sh

[![Image 54: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
4.   Install Intel Gaudi driver and software:

./habanalabs-installer.sh install --type base

[![Image 55: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
Click “Y” when asked if you wish to install.

5.   Reboot the system:

sudo reboot

[![Image 56: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 

Note

*   The installation process takes approximately 7 minutes to complete.

*   You may see this error message after the installation:

W: GPG error: https://vault.habana.ai/artifactory/debian noble InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 16DF67E63BA2D625
E: The repository 'https://vault.habana.ai/artifactory/debian noble InRelease' is not signed.

[![Image 57: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
Ignore it and move to the next Step.

To verify that the installation is successful, follow the steps outlined in the [System Verifications and Final Tests](https://docs.habana.ai/en/latest/Installation_Guide/System_Verification_and_Final_Tests.html#system-verification) section.

The following steps are required only once to set up the Docker engine, Gaudi container runtime, and the Gaudi container itself.

Note

The steps below are based on the [recommended](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) method from the official Docker website.

1.   Update the `apt` repository:

> 1.   Add Docker’s official GPG key:
> 
> sudo apt-get update
> sudo apt-get install ca-certificates curl
> sudo install -m 0755 -d /etc/apt/keyrings
> sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
> sudo chmod a+r /etc/apt/keyrings/docker.asc
> 
> [![Image 58: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)

    1.   Add the repository to `apt` sources:

echo \
“deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
(. /etc/os-release && echo “${UBUNTU_CODENAME:- $VERSION_CODENAME}”) stable” | \
sudo tee /etc/apt/sources.list.d/docker.list> /dev/null
sudo apt-get update

[![Image 59: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 

2.   Install the Docker packages:

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

[![Image 60: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
Click “Y” when asked if you wish to install.

3.   Install `habanalabs-container-runtime` package. This package is required for running workloads in containers. Both Docker and Kubernetes are supported:

sudo apt install -y habanalabs-container-runtime

[![Image 61: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
4.   Register `habana-container-runtime` by adding the following to `etc/docker/daemon.json` as mentioned in the [Docker Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Docker_Installation.html#docker-installation) section:

sudo tee /etc/docker/daemon.json <<EOF
{
   "runtimes": {
      "habana": {
            "path": "/usr/bin/habana-container-runtime",
            "runtimeArgs": []
      }
   }
}
EOF

[![Image 62: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
5.   Verify that the contents of the file match the above output:

sudo cat /etc/docker/daemon.json

[![Image 63: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
6.   Add your user to the Docker group:

sudo usermod -aG docker $USER

[![Image 64: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
7.   Reload daemon:

sudo systemctl daemon-reload

[![Image 65: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
8.   Restart the Docker service:

sudo systemctl restart docker

[![Image 66: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
9.   Install the latest Gaudi Docker container:

sudo docker run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e
OMPI_MCA_btl_vader_single_copy_mechanism=none -v /opt/datasets:/datasets
--cap-add=sys_nice --net=host --ipc=host
vault.habana.ai/gaudi-docker/1.23.0/ubuntu24.04/habanalabs/pytorch-installer-2.9.0:latest

[![Image 67: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
The **no hostkeys available** message can be safely ignored. You should now be inside the container.

Run Inference[¶](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html#run-inference "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------

After setting up the Docker container in the previous section, follow the instructions below to run inference workloads inside the Docker container terminal. The examples below demonstrate how to run inference on a single card using the Optimum for Intel Gaudi library, and on multiple cards using the vLLM Inference Server with the Llama 3.2-1B and Granite 34B-code-instruct-8K models, respectively. For additional models tested on IBM with Gaudi 3, refer to the [IBM FM Benchmarking Framework GitHub repository](https://github.com/IBM/fmwork/tree/gaudi3_v1.20.0_RC1).

1.   Install the Optimum for Intel Gaudi library:

pip install --upgrade-strategy eager optimum[habana]

[![Image 68: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
2.   Clone the `optimum-habana` repository for running the example code:

cd root && git clone https://github.com/huggingface/optimum-habana

[![Image 69: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
3.   Check the latest branch of `optimum-habana`. Note that the branch version number is different from Gaudi software version number:

 cd optimum-habana && git checkout v1.20.0

[![Image 70: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
4.   Install the requirements for running text generation task:

cd examples/text-generation &&
pip install -r requirements.txt &&
pip install -r requirements_lm_eval.txt

[![Image 71: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
5.   Create your own user account and obtain an HF_TOKEN from the [Hugging Face website](https://huggingface.co/settings/tokens). Then, export the HF_TOKEN environment variable and insert your token as shown below:

export HF_TOKEN=<INSERT YOUR OWN HF_TOKEN HERE>

[![Image 72: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
6.   Set up the `HF_HOME` environment variable to point to `/dev/shm` where the model checkpoints are downloaded:

export HF_HOME=/dev/shm

[![Image 73: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
7.   Run inference:

ENABLE_LB_BUNDLE_ALL_COMPUTE_MME=0 ENABLE_EXPERIMENTAL_FLAGS=1 python ../gaudi_spawn.py \
--world_size 1 run_generation.py \
--model_name_or_path NousResearch/Llama-3.2-1B \
--max_new_tokens 2048 \
--bf16 \
--use_hpu_graphs \
--use_kv_cache \
--batch_size 1 \
--do_sample \
--use_flash_attention \
--flash_attention_causal_mask

[![Image 74: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 

The final output should appear as follows:

> Stats:
> ----------------------------------------------------------------------------------
> Input tokens
> Throughput (including tokenization) = 192.1497924325992 tokens/second
> Memory allocated                    = 9.88 GB
> Max memory allocated                = 9.9 GB
> Total memory available              = 126.06 GB
> Graph compilation duration          = 32.885373371012975 seconds
> ----------------------------------------------------------------------------------
> 
> [![Image 75: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)

1.   Install vllm-fork:

cd /root
git clone https://github.com/HabanaAI/vllm-fork.git
cd vllm-fork
git checkout v0.9.0.1+Gaudi-1.22.0
pip install -r requirements-hpu.txt
python3 setup.py develop
pip install datasets

[![Image 76: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) Note

You may see this error message after running `pip install -r requirements-hpu.txt`:

### Received error:
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
neural-compressor-pt 3.3 requires numpy==1.23.5; python_version < "3.12", but you have numpy 1.26.4 which is incompatible.

[![Image 77: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
Ignore it and move to the next Step. 
2.   Create your own user account and obtain an HF_TOKEN from the [Hugging Face website](https://huggingface.co/settings/tokens). Then, export the HF_TOKEN environment variable and insert your token as shown below:

export HF_TOKEN=<INSERT YOUR OWN HF_TOKEN HERE>

[![Image 78: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
3.   Set up environment variables:

export ENABLE_EXPERIMENTAL_FLAGS=1
export HCL_SCALEUP_SIMB_COUNT=13
export HF_HOME=/dev/shm

[![Image 79: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
4.   Launch the vLLM Server using the IBM Granite 34B-code-instruct-8K model and **allow 20 minutes** for it to initialize and warm up:

vllm serve ibm-granite/granite-34b-code-instruct-8k \
   --port 8080 \
   --swap-space 16 \
   --disable-log-requests \
   --block-size 128 \
   --tensor-parallel-size 8 2>&1 | tee server_granite34b_vllm.log

[![Image 80: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
**After around 20 minutes**, the following output should appear when your server is ready:

> INFO 02-27 22:13:00 launcher.py:27] Route: /invocations, Methods: POST
> INFO:     Started server process [18027]
> INFO:     Waiting for application startup.
> INFO:     Application startup complete.
> INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
> 
> [![Image 81: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)

5.   Wait for the server to get fully ready as shown in the above screenshot. Then, **in a separate terminal**, SSH into the instance and connect to the Docker:

sudo docker ps
sudo docker exec -it <gaudi container id> bash

[![Image 82: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
6.   In the Docker container, switch to the benchmarks subdirectory:

cd /root/vllm-fork/benchmarks

[![Image 83: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 
7.   Run inference:

ENABLE_EXPERIMENTAL_FLAGS=1 \
HCL_SCALEUP_SIMB_COUNT=13 \
python3 benchmark_serving.py \
   --backend vllm \
   --port 8080 \
   --model ibm-granite/granite-34b-code-instruct-8k \
   --dataset-name sonnet \
   --dataset-path sonnet.txt \
   --sonnet-input-len 1024 \
   --sonnet-output-len 1024 \
   --trust-remote-code 2>&1 | tee client_benchmark_granite34b_vllm.log

[![Image 84: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html) 

The final output should appear as follows:

============ Serving Benchmark Result ============
Successful requests:                     1000
Benchmark duration (s):                  180.71
Total input tokens:                      1028593
Total generated tokens:                  762666
Request throughput (req/s):              5.53
Output token throughput (tok/s):         4220.35
Total Token throughput (tok/s):          9912.26
---------------Time to First Token----------------
Mean TTFT (ms):                          64007.19
Median TTFT (ms):                        64302.62
P99 TTFT (ms):                           143460.93
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          57.47
Median TPOT (ms):                        56.23
P99 TPOT (ms):                           116.77
---------------Inter-token Latency----------------
Mean ITL (ms):                           54.17
Median ITL (ms):                         39.87
P99 ITL (ms):                            228.03
==================================================

[![Image 85: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)
