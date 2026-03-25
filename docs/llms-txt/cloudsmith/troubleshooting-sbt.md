# Source: https://help.cloudsmith.io/docs/troubleshooting-sbt.md

# Troubleshooting sbt

**Q. sbt maintains plain text passwords in settings.xml and credential files. How do we prevent exposure of such passwords?**

The underlying Maven toolchain supports encrypted credentials. You can also use interpolation from environment variables instead so that you don't store them in configuration files. We also support authentication by de-privileged [entitlement tokens](docs:entitlement-tokens) (i.e. read-only specific access) to minimize exposure.

## Still Need Help?

Contact us [here](https://support.cloudsmith.com). We're always happy to help!