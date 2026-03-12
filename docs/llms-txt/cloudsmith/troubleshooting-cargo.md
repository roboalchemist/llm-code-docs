# Source: https://help.cloudsmith.io/docs/troubleshooting-cargo.md

# Troubleshooting Cargo

**Q. It's not working...**\
Cargo's cache can become corrupted. If this happens, you can often fix the issue by manually deleting the cache directories. The folders to remove are:

* `~/.cargo/registry`
* `~/.cargo/git`

If you previously set an override for `$CARGO_HOME`, the cache may be in a non-standard location.

## Still Need Help?

Contact us [here](https://support.cloudsmith.com). We're always happy to help!