#### > This option file is used in:
#### >   podman create, run
#### > If file is edited, make sure the changes
#### > are applicable to all of those.

#### **--systemd**=*true* | *false* | *always*

Run container in systemd mode. The default is **true**.

- **true** enables systemd mode only when the command executed inside the container is *systemd*, */usr/sbin/init*,
*/sbin/init* or */usr/local/sbin/init*.

- **false** disables systemd mode.

- **always** enforces the systemd mode to be enabled.

Running the container in systemd mode causes the following changes:

- Podman mounts tmpfs file systems on the following directories
  - */run*
  - */run/lock*
  - */tmp*
  - */sys/fs/cgroup/systemd* (on a cgroup v1 system)
  - */var/lib/journal*
- Podman sets the default stop signal to **SIGRTMIN+3**.
- Podman sets **container_uuid** environment variable in the container to the
first 32 characters of the container ID.
- Podman does not mount virtual consoles (*/dev/tty\d+*) when running with **--privileged**.
- On cgroup v2, */sys/fs/cgroup* is mounted writable.

This allows systemd to run in a confined container without any modifications.

Note that on **SELinux** systems, systemd attempts to write to the cgroup
file system. Containers writing to the cgroup file system are denied by default.
The **container_manage_cgroup** boolean must be enabled for this to be allowed on an SELinux separated system.

```
setsebool -P container_manage_cgroup true
```
