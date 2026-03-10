# Source: https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/llms.txt

# AWS Elemental Statmux Upgrade Guide

- [About this Guide](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/about-sm-cg.html)
- [Downloading Software](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/detailed-dl-sm-upg.html)
- [Document History](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/doc-history.html)

## [Upgrades in AWS Elemental Statmux](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/upgrades-sm-upg.html)

- [Step A: Get Ready](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/upgrades-sm-upg-single-ver-version.html): The following steps prepare you for upgrading.
- [Step B: Copy the AWS Elemental Statmux Installer](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/upgrades-sm-upg-single-locate-sw.html)
- [Step D: Upgrade the Node](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/upgrades-sm-upg-single-up-cond.html): The upgrade steps that you take depend on the version that you're upgrading to.


## [Downgrades in AWS Elemental Statmux](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/downgrades-sm-upg.html)

- [Step A: Get Ready](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/downgrades-sm-upg-ready-dn.html): The following steps prepare you for downgrading.
- [Step B: Copy the AWS Elemental Installer](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/downgrades-sm-upg-locate-sw-dn.html): Locate and copy the installer for AWS Elemental Statmux.
- [Step C: Downgrade the Node](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/downgrades-sm-upg-dg-node.html): The downgrade steps that you take depend on the version that you're downgrading to.


## [Performing a Clean Install](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg.html)

- [Step A: Get Ready](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg-ready.html)
- [Step B: Install (Kickstart) the Operating System Software](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg-install.html): You must install a configured operating system from an .iso file onto each physical machine that will be running AWS Elemental software.
- [Step C: Restore Copied Files](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg-restore.html): Now that your operating system is reinstalled, restore the files that you copied back onto the AWS Elemental Statmux hardware unit, to /home/elemental.
- [Step D: Install the AWS Elemental Software](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg-install-sw.html): These steps must be performed on each system where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH.

### [Step E: Install the License Files](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg-install-lic.html)

At this point, the software is installed but it is not yet enabled.

- [Step a: Retrieve Activation Code](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/install-sm-ig-licensing-ret-act.html): You should have received an email containing an activation code.
- [Step b: Generate a License Activation Key File](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/install-sm-ig-licensing-gen-lic.html): The operating system that you installed on your hardware has a utility you can use to generate an activation key file.
- [Step c: Download Licenses from the AWS Elemental User Community](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/install-sm-ig-licensing-dl-lic.html)
- [Step d: Install the License Files](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/install-sm-ig-licensing-lic-files.html): Now that you have a .tgz compressed license file for each instance of the software you are running, you must point the software to it.
- [Step F: Configure the Node](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg-config.html): Now that each system has the appropriate software installed, see the following guides to complete configuration:
