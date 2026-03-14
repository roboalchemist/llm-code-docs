# Source: https://help.cloudsmith.io/docs/troubleshooting-redhat.md

# Troubleshooting Redhat

**Q. I don't see packages that are available in my repository when I do`yum list`, even after clearing my yum cache and updating?**

It may be possible that you already have a package installed with the same version as that which is available from the repository. In this case, you need to do `yum list available --showduplicates` to see all available packages.

**Q. I'm having trouble pulling`noarch` packages?**\
The noarch index in RedHat is separate, unlike in Debian where it is blended into all arch-specific repositories. The reason for this is that it follows the standard layout for RedHat repositories. If you use our automated repository setup scripts, they configure two repositories when setting up a machine, one for the arch-specific and another for noarch, which will enable you to install `noarch` packages.

If you are manually setting up a Cloudsmith RedHat repository, or using something like Ansible, please be sure to configure the`noarch` repository also.

Contact us [here](https://support.cloudsmith.com). We're always happy to help!