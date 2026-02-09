# Source: https://docs.sandboxes.cloud/docs/copy-files.md

# Copy files between local and cloud

During development, it's often needed to copy some input files from your local machine to the Crafting workspaces or copy results files back. In this page, we describe how to copy files between local and cloud.

It can be simply done via `cs scp` command from the Crafting CLI, which is a simple wrapper of the `scp` command

```shell
$ cs scp <LOCAL-FILE> <SANDBOX/WORKSPACE>:<REMOTE-PATH> # copy file from local to cloud
$ cs scp <SANDBOX/WORKSPACE>:<REMOTE-FILE> <LOCAL-PATH> # copy file from cloud to local
```

Details of `cs scp` can be found [here](https://docs.sandboxes.cloud/docs/command-line-tool#scp)

To sync directories between local machine and Crafting workspace, there are other tool integration like `cs rsync`, `cs mutagen` available, please see [Code sync for hybrid development](https://docs.sandboxes.cloud/docs/code-sync) for their usage, and reference can be found [here](https://docs.sandboxes.cloud/docs/command-line-tool)