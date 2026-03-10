# Source: https://docs.aws.amazon.com/elemental-server/latest/installguide/llms.txt

# AWS Elemental Server Installation Guide

> AWS Elemental Server provides fast, reliable video processing for file-based transcoding workflows. It performs simultaneous, faster-than-real-time conversion of multiple video files to create mezzanine deliverables, traditional on-demand assets, and adaptive bitrate outputs for delivery to TVs, PCs, and mobile devices. This Installation Guide describes how to install nodes on appliances and virtual machines (VMs).

- [About This Guide](https://docs.aws.amazon.com/elemental-server/latest/installguide/about-srvr-ig.html)
- [Downloading Software](https://docs.aws.amazon.com/elemental-server/latest/installguide/detailed-dl-srvr-ig.html)
- [System Requirements for Virtual Machines (VMs)](https://docs.aws.amazon.com/elemental-server/latest/installguide/vm-req.html)
- [Install Error Messages](https://docs.aws.amazon.com/elemental-server/latest/installguide/errors-srvr-ig.html)
- [Document History](https://docs.aws.amazon.com/elemental-server/latest/installguide/doc-history.html)

## [Installing Node-locked Licenses on Qualified Hardware](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig.html)

- [Step A: Prepare Hardware and Download Files](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-prep.html)
- [Step B: Install (Kickstart) the Operating System Software](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-install-ks.html): You must install a configured operating system from an .iso file onto each physical machine that will be running AWS Elemental software.
- [Step C: Install the AWS Elemental Software](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-install-sw.html): These steps must be performed on each node where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH.

### [Step D: Set-Up Licensing](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-licensing.html)

At this point, the software is installed but it is not yet enabled.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-licensing-gen-lic.html): The operating system that you installed on your hardware has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-licensing-dl-lic.html)
- [Step d: Install the License Files](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-licensing-lic-files.html): Now that you have a .tgz compressed license file for each instance of the software you are running, you must point the software to it.
- [Step E: Complete Node Configuration](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-complete.html): You have now installed and performed basic configuration of AWS Elemental Server.


## [Installing Node-locked Licenses on a Virtual Machine (VM)](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig.html)

- [Step A: Prepare Hardware and Download Files](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-prep.html)
- [Step B: Deploy the VM](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-install-vm.html): Perform these steps from your workstation.
- [Step C: Install the AWS Elemental Software](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-install-sw.html)

### [Step D: Set-up Licensing](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-licensing.html)

Install a valid license file for each AWS Elemental system using the following steps described in the following table.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-licensing-gen-lic.html): The operating system that you installed on your virtual machine (VM) has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-licensing-dl-lic.html)
- [Step d: Install the License Files](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-licensing-lic-files.html): Now that you have a .tgz compressed license file for each instance of the software you are running, you must point the software to it.
- [Step E: Complete Node Configuration](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-complete.html): You have now installed and performed basic configuration of AWS Elemental Server.


## [Installing Node-locked Licenses on a Kernel-based Virtual Machine (KVM)](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig.html)

- [Step A: Prepare Hardware and Download Files](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-prep.html)
- [Step B: Deploy the VM](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-install-vm.html): Perform these steps from your workstation.
- [Step C: Enable CPU Passthrough](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-passthrough.html): Enable CPU passthrough so that the KVM can tell what CPU you're using.
- [Step D: Install the AWS Elemental Software](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-install-sw.html)

### [Step E: Set-up Licensing](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-licensing.html)

Install a valid license file for each AWS Elemental system using the following steps described in the following table.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-licensing-gen-lic.html): The operating system that you installed on your virtual machine (VM) has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-licensing-dl-lic.html)
- [Step F: Complete Node Configuration](https://docs.aws.amazon.com/elemental-server/latest/installguide/install-kvm-srvr-ig-complete.html): You have now installed and performed basic configuration of AWS Elemental Server.
