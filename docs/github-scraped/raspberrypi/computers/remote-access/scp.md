[[scp]]
## Share files with SCP

Secure Copy Protocol (`scp`) sends files over SSH. You can use `scp` to copy files between your Raspberry Pi and another computer.

To use `scp`, xref:remote-access.adoc#ip-address[find your Raspberry Pi's IP address].

### Copy files to your Raspberry Pi

To copy a file named `myfile.txt` from your personal computer to a user's home folder on your Raspberry Pi, run the following command from the directory containing `myfile.txt`, replacing the `<username>` placeholder with the username you use to log in to your Raspberry Pi and the `<pi*ip*address>` placeholder with your Raspberry Pi's IP address:

```console
$ scp myfile.txt <username>@<pi*ip*address>:
```

To copy a file to a specific directory, append the directory path after the `:` in the `scp` command. Create the folder before you run `scp`, since `scp` won't create folders automatically. For instance, the following command copies a file named `myfile.txt` into the `project/` directory within a user's home folder:

```console
$ scp myfile.txt <username>@<pi*ip*address>:project/
```

### Copy files from your Raspberry Pi

To copy a file named `myfile.txt` from a user's home directory on a Raspberry Pi to the current directory on another computer, run the following command:

```console
$ scp <username>@<pi*ip*address>:myfile.txt .
```

### Copy multiple files with one command

To copy multiple files, list the file names in a single command, separated by spaces:

```console
$ scp myfile.txt myfile2.txt <username>@<pi*ip*address>:
```

Alternatively, use a wildcard to copy all files matching a particular filter. The following command copies all files that end with `.txt`:

```console
$ scp **.txt <username>@<pi*ip*address>:
```

The following command copies all files that start with `m`:

```console
$ scp m** <username>@<pi*ip*address>:
```

The following command copies all files that start with `m` and end with `.txt`:

```console
$ scp m*.txt <username>@<pi*ip*address>:
```

[NOTE]
====
To copy files with names that contain spaces, enclose the file name in quotes:

```console
$ scp "my file.txt" <username>@<pi*ip*address>:
```

====

### Copy a folder

To copy a folder and all of its contents, pass the folder name with the `-r` (recursive) flag:

```console
$ scp -r project/ <username>@<pi*ip*address>:
```