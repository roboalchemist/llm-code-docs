# Source: https://help.cloudsmith.io/docs/troubleshooting-maven.md

# Troubleshooting Maven

**Q. Maven maintains plain text passwords in settings.xml and credential files. How do we prevent exposure of such passwords?**

The Maven tooling chain supports encrypted credentials. You can also use interpolation from environment variables instead so that you don't store them in configuration files. We also support authentication by de-privileged [entitlement tokens](docs:entitlement-tokens) (i.e. read-only specific access) to minimise exposure.

***

**Q. Why does Cloudsmith keep all snapshot versions of a .jar, and not only the last one? Usually, we only want the last version.**

Mainly, it is because some people do it one way, and others do it another. Some people utilise or want to keep the chain of snapshots, so we keep them to facilitate those customers. For others, they'll need to delete them manually (or automatically with a retention policy)

***

**Q. My uploaded Maven artifact version was renamed from`X.X.X-SNAPSHOT` to `X.X.X-20190815.205452-1`.  Can I set it so that it doesn’t rename?**

Snapshots are handled differently from release artifacts because there can be many snapshots of the same version, which is why it got renamed. If you uploaded `1.0.0-SNAPSHOT` multiple times, it would let you, and it would sync as `1.0.0-<DATETIME>-1` , then `1.0.0.-<DATETIME>-2` and so on.

It isn't possible (yet) to disable this behaviour. However, despite what the UI says, you should still be able to refer to your package in dependencies as `1.0.0-SNAPSHOT` and it will pick up the latest version of `1.0.0-SNAPSHOT` uploaded. This is pretty standard for Maven-based repositories but might be surprising unless you know about it.

## Still Need Help?

Contact us [here](https://support.cloudsmith.com). We're always happy to help!