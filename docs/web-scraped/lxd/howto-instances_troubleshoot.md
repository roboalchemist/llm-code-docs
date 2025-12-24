# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/instances_troubleshoot/

[]

# How to troubleshoot failing instances[¶](#how-to-troubleshoot-failing-instances "Link to this heading")

If your instance fails to start and ends up in an error state, this usually indicates a bigger issue related to either the image that you used to create the instance or the server configuration.

To troubleshoot the problem, complete the following steps:

1.  Save the relevant log files and debug information:

    Instance log

    :   Display the instance log:

        ::: 
        ::: 
        CLI
        API
        UI
        :::

        ::: 
        ::: 
        ::: highlight
            lxc info <instance_name> --show-log
        :::
        :::
        :::

        ::: 
        ::: 
        ::: highlight
            lxc query --request GET /1.0/instances/<instance_name>/logs/lxc.log
        :::
        :::
        :::

        ::: 
        Navigate to the instance detail page and switch to the [Logs] tab to view the available log files.
        :::
        :::

    Console log

    :   Display the console log:

        ::: 
        ::: 
        CLI
        API
        UI
        :::

        ::: 
        ::: 
        ::: highlight
            lxc console <instance_name> --show-log
        :::
        :::

        This command is available only for containers.
        :::

        ::: 
        ::: 
        ::: highlight
            lxc query --request GET /1.0/instances/<instance_name>/console
        :::
        :::

        This endpoint is available only for containers.
        :::

        ::: 
        Navigate to the instance detail page and switch to the [Console] tab to view the console. The console is displayed only when the instance is running.
        :::
        :::

    Detailed server information

    :   The LXD snap includes a tool that collects the relevant server information for debugging. Enter the following command to run it:

        ::: 
        ::: highlight
            sudo lxd.buginfo
        :::
        :::

2.  Reboot the machine that runs your LXD server.

3.  Try starting your instance again. If the error occurs again, compare the logs to check if it is the same error.

    If it is, and if you cannot figure out the source of the error from the log information, open a question in the [forum](https://discourse.ubuntu.com/c/lxd/126). Make sure to include the log files you collected.

## Troubleshooting examples[¶](#troubleshooting-examples "Link to this heading")

See the following sections for some typical methods of troubleshooting an instance.

### Debug [`systemd`] [`init`][¶](#debug-systemd-init "Link to this heading")

Here is how to enable [`systemd`] [debug level messages](https://systemd.io/DEBUGGING/) for the [`c1`] container:

    lxc config set c1 raw.lxc 'lxc.init.cmd = /sbin/init systemd.log_level=debug'

    lxc start c1

Now that the container has started, you can check for the debug messages in the journal:

    lxc exec c1 -- journalctl

### Emergency [`systemd`] shell[¶](#emergency-systemd-shell "Link to this heading")

Here is how to get an [`emergency`] shell on an instance using [`systemd`]:

    lxc config set c1 raw.lxc 'lxc.init.cmd = /sbin/init emergency'

    lxc start c1

Now that the container has started, you can enter the emergency shell using the console (hit the [Enter] key once in):

    lxc console c1

### Issue starting RHEL 7 container[¶](#issue-starting-rhel-7-container "Link to this heading")

In this example, let's investigate a RHEL 7 system in which [`systemd`] cannot start.

[`user@host:~$`]` `

[[`lxc`]` `[`console`]` `[`--show-log`]` `[`rhel7`]` `]

    Console log:

    Failed to insert module 'autofs4'
    Failed to insert module 'unix'
    Failed to mount sysfs at /sys: Operation not permitted
    Failed to mount proc at /proc: Operation not permitted
    [!!!!!!] Failed to mount API filesystems, freezing.

The errors here say that [`/sys`] and [`/proc`] cannot be mounted - which is correct in an unprivileged container. However, LXD mounts these file systems automatically if it can.

The [[container requirements]](../../container-environment/) specify that every container must come with an empty [`/dev`], [`/proc`] and [`/sys`] directory, and that [`/sbin/init`] must exist. If those directories don't exist, LXD cannot mount them, and [`systemd`] will then try to do so. As this is an unprivileged container, [`systemd`] does not have the ability to do this, and it then freezes.

So you can see the environment before anything is changed, and you can explicitly change the init system in a container using the [[`raw.lxc`]](../../reference/instance_options/#instance-raw:raw.lxc) configuration parameter. This is equivalent to setting [`init=/bin/bash`] on the Linux kernel command line.

    lxc config set rhel7 raw.lxc 'lxc.init.cmd = /bin/bash'

Here is what it looks like:

[`user@host:~$`]` `

[[`lxc`]` `[`config`]` `[`set`]` `[`rhel7`]` `[`raw.lxc`]` `[`'lxc.init.cmd`]` `[`=`]` `[`/bin/bash'`]` `]

[`user@host:~$`]` `

[[`lxc`]` `[`start`]` `[`rhel7`]` `]

[`user@host:~$`]` `

[[`lxc`]` `[`console`]` `[`--show-log`]` `[`rhel7`]` `]

    Console log:

    [root@rhel7 /]#

Now that the container has started, you can check it and see that things are not running as well as expected:

[`user@host:~$`]` `

[[`lxc`]` `[`exec`]` `[`rhel7`]` `[`--`]` `[`bash`]` `]

    [root@rhel7 ~]# ls
    [root@rhel7 ~]# mount
    mount: failed to read mtab: No such file or directory
    [root@rhel7 ~]# cd /
    [root@rhel7 /]# ls /proc/
    sys
    [root@rhel7 /]# exit

Because LXD tries to auto-heal, it created some of the directories when it was starting up. Shutting down and restarting the container fixes the problem, but the original cause is still there - the template does not contain the required files.