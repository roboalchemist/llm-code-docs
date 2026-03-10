# Source: https://docs.aws.amazon.com/elemental-cf2/latest/installguide/llms.txt

# AWS Elemental Conductor File Installation Guide

- [About This Guide](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/about-cf-ig.html)
- [Downloading Software](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/detailed-dl-cf-ig.html)
- [System Requirements for Virtual Machines (VMs)](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/vm-req.html)
- [Install Error Messages](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/errors-cf-ig.html)
- [Document History](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/doc-history.html)

## [Installing Node-locked Licenses on Qualified Hardware](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig.html)

- [Step A: Prepare Hardware and Download Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-prep.html)
- [Step B: Install (Kickstart) the Operating System Software](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-install-ks.html): You must install a configured operating system from an .iso file onto each physical machine that will be running AWS Elemental software.
- [Step C: Install the AWS Elemental Software](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-install-sw.html): These steps must be performed on each node where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH.

### [Step D: Set Up Licensing](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-licensing.html)

At this point, the software is installed but it is not yet enabled.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-licensing-gen-lic.html): The operating system that you installed on your hardware has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-licensing-dl-lic.html)
- [Step d: Install the License Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-licensing-lic-files.html): Now that you have a .tgz compressed license file for each instance of the software you are running, you must point the software to it.
- [Step E: Complete Node Configuration](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-complete.html): You have now installed and performed the basic configuration of AWS Elemental Conductor File.


## [Installing Node-locked Licenses on a Virtual Machine (VM)](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig.html)

- [Step A: Prepare the Hardware and Download Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-prep.html)
- [Step B: Deploy the VM](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-install-vm.html): Perform these steps from your workstation.
- [Step C: Install the AWS Elemental Software](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-install-sw.html)

### [Step D: Set-up Licensing](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-licensing.html)

Install a valid license file for each AWS Elemental system using the following steps described in the following table.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-licensing-gen-lic.html): The operating system that you installed on your virtual machine (VM) has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-licensing-dl-lic.html)
- [Step d: Install the License Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-licensing-lic-files.html): Now that you have a .tgz compressed license file for each instance of the software you are running, you must point the software to it.
- [Step E: Complete Node Configuration](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-cf-ig-complete.html): You have now installed and performed the basic configuration of AWS Elemental Conductor File.


## [Installing Pooled Licenses on a Virtual Machine (VM)](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig.html)

- [Step A: Prepare the Hardware and Download Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-prep.html)
- [Step B: Deploy the VM and Install the Conductor File Software](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-install-vm.html): Set-up the AWS Elemental Conductor File nodes before setting up the worker AWS Elemental Server nodes.

### [Step C: Set-up Licensing](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-licensing.html)

Install a valid license file for each AWS Elemental system using the following steps described in the following table.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-licensing-gen-lic.html): The operating system that you installed on your virtual machine (VM) has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-licensing-dl-lic.html)
- [Step d: Install the License Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-licensing-lic-files.html): Now that you have a .tgz compressed license file for each instance of the software you are running, you must point the software to it.
- [Step D: Deploy the VM and Install the Worker Software](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-install-vm-w.html): After you've installed the AWS Elemental Conductor File nodes, perform these steps on each individual blade that you're adding to the cluster in order to deploy a VM and install the AWS Elemental Server worker software.
- [Step E: Verify that Workers Receive Licenses](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-ver.html): Before going into production, it is a good idea to verify that the AWS Elemental Server node can obtain a license from AWS Elemental Conductor File.
- [Step F: Complete Node Configuration](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-complete.html): You have now installed and performed basic configuration of AWS Elemental Conductor File and AWS Elemental Server.


## [Installing Node-locked Licenses on a Kernel-based Virtual Machine (KVM)](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig.html)

- [Step A: Prepare the Hardware and Download Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-prep.html)
- [Step B: Deploy the KVM](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-install-vm.html): Perform these steps from your workstation.
- [Step C: Enable CPU Passthrough](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-passthrough.html): Enable CPU passthrough so that the KVM can tell what CPU you're using.
- [Step D: Install the AWS Elemental Software](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-install-sw.html)

### [Step E: Set-up Licensing](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-licensing.html)

Install a valid license file for each AWS Elemental system using the steps described in the table.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-licensing-gen-lic.html): The operating system that you installed on your virtual machine (VM) has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-licensing-dl-lic.html)
- [Step d: Install the License Files](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-licensing-lic-files.html): Now that you have a .tgz compressed license file for each instance of the software you are running, you must point the software to it.
- [Step F: Complete Node Configuration](https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-complete.html): You have now installed and performed the basic configuration of AWS Elemental Conductor File.
