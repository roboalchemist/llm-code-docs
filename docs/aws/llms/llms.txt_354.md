# Source: https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/llms.txt

# AWS Elemental Live Upgrade Guide

> AWS Elemental Live is a real-time video service that lets you create live outputs for broadcast and streaming delivery. This Upgrade Guide describes how to upgrade and downgrade AWS Elemental Live, including kickstarting the operationg system (when necessary).

- [About this guide](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/about-lv-cg.html)
- [Reference: Downloading software](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/detailed-dl-lv-upg.html)
- [Document History](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/doc-history.html)

## [Upgrades in Elemental Live](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-upg.html)

- [Step A: Get ready to upgrade](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-upg-single-ver-version.html): The following steps prepare you for upgrading.
- [Step B: Kickstart the OS](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-step-kickstart.html): Your upgrade might require that you re-install (kickstart) the operating system.
- [Step C: Copy the installer](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-upg-single-locate-sw.html)
- [Step D: Upgrade the software](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-upg-single-up-cond.html): These steps must be performed on the Elemental Live hardware unit.
- [Step E: Restore the database](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-restore-database.html): If you upgraded the operating system, you should have backed up the Elemental Live database.
- [Step F: Upgrade the license](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-upg-lic.html): The new version of the software might include a feature that is in an add-on package.


## [Downgrades in Elemental Live](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/downgrades-lv-upg.html)

- [Step A: Get ready to downgrade](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/downgrades-lv-upg-ready-dn.html): The following steps prepare you for downgrading AWS Elemental Live.
- [Step B: Copy the AWS Elemental installer](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/downgrades-lv-upg-locate-sw-dn.html): Locate and copy the installer for Elemental Live.
- [Step C: Downgrade the node](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/downgrades-lv-upg-dg-node.html): When you downgrade AWS Elemental Live , run the installer with the --downgrade switch for each node.
