[[rsync]]
## Synchronise folders between computers with `rsync`

You can use `rsync` to synchronise folders between computers. For example, you could use `rsync` to transfer new pictures taken by your Raspberry Pi to your personal computer automatically.

Before you can configure `rsync`, determine values for the following:

** `<pi*ip*address>`: your Raspberry Pi's local IP address: see xref:remote-access.adoc#ip-address[Find your Raspberry Pi's IP address] for more information
** `<pi*username>`: the username you use to log into your Raspberry Pi
** `<pi*folder*name>`: the name of the folder you want to copy files from on your Raspberry Pi
** `<pc*folder*name>`: the name of the folder you would like to synchronise on your personal computer

To configure `rsync` to synchronise files, complete the following steps on your personal computer, replacing placeholders in the commands with the values you determined above:

1. Create the folder you would like to synchronise to:
+
```console
$ mkdir <pc*folder*name>
```
1. Synchronise files to the folder with `rsync`:
+
```console
$ rsync -avz -e ssh <pi*username>@<pi*ip*address>:<pi*folder*name>/ <pc*folder*name>/
```

This command copies all files from the selected folder on your Raspberry Pi to the selected folder on your personal computer. If you run the command multiple times, `rsync` keeps track of the files you have already downloaded and skips them. If you delete or modify an already synchronised file on the Raspberry Pi, `rsync` updates the files on your personal computer accordingly.