# Source: https://docs.gtk.org/gio-unix/

Title: GioUnix-2.0

URL Source: https://docs.gtk.org/gio-unix/

Markdown Content:
### Namespace

Unix-specific APIs in Gio

#### Dependencies [](https://docs.gtk.org/gio-unix/#dependencies)

**GLib**—2.0 The base utility library
[Browse documentation](https://docs.gtk.org/glib/)
**GModule**—2.0 Portable API for dynamically loading modules
[Browse documentation](https://docs.gtk.org/gmodule/)
**GObject**—2.0 The base type system library
[Browse documentation](https://docs.gtk.org/gobject/)
**Gio**—2.0 A library of useful classes for I/O, networking and IPC
[Browse documentation](https://docs.gtk.org/gio/)

*   [UNIX Mounts](https://docs.gtk.org/gio-unix/unix-mounts.html)
*   [Classes Hierarchy](https://docs.gtk.org/gio-unix/classes_hierarchy.html)

[DesktopAppInfo](https://docs.gtk.org/gio-unix/class.DesktopAppInfo.html "DesktopAppInfo")`GDesktopAppInfo` is an implementation of `GAppInfo` based on desktop files.
[FDMessage](https://docs.gtk.org/gio-unix/class.FDMessage.html "FDMessage")This `GSocketControlMessage` contains a `GUnixFDList`. It may be sent using `g_socket_send_message()` and received using `g_socket_receive_message()` over UNIX sockets (ie: sockets in the `G_SOCKET_FAMILY_UNIX` family). The file descriptors are copied between processes by the kernel.
[InputStream](https://docs.gtk.org/gio-unix/class.InputStream.html "InputStream")`GUnixInputStream` implements `GInputStream` for reading from a UNIX file descriptor, including asynchronous operations. (If the file descriptor refers to a socket or pipe, this will use `poll()` to do asynchronous I/O. If it refers to a regular file, it will fall back to doing asynchronous I/O in another thread.).
[MountMonitor](https://docs.gtk.org/gio-unix/class.MountMonitor.html "MountMonitor")Watches for changes to the set of mount entries and mount points in the system.
[OutputStream](https://docs.gtk.org/gio-unix/class.OutputStream.html "OutputStream")`GUnixOutputStream` implements `GOutputStream` for writing to a UNIX file descriptor, including asynchronous operations. (If the file descriptor refers to a socket or pipe, this will use `poll()` to do asynchronous I/O. If it refers to a regular file, it will fall back to doing asynchronous I/O in another thread.).

[DesktopAppInfoLookup](https://docs.gtk.org/gio-unix/iface.DesktopAppInfoLookup.html "DesktopAppInfoLookup")`GDesktopAppInfoLookup` is an opaque data structure and can only be accessed using the following functions.

deprecated: 2.28
[FileDescriptorBased](https://docs.gtk.org/gio-unix/iface.FileDescriptorBased.html "FileDescriptorBased")`GFileDescriptorBased` is an interface for file descriptor based IO.

since: 2.24

[MountEntry](https://docs.gtk.org/gio-unix/struct.MountEntry.html "MountEntry")Defines a Unix mount entry (e.g. `/media/cdrom`). This corresponds roughly to a mtab entry.
[MountPoint](https://docs.gtk.org/gio-unix/struct.MountPoint.html "MountPoint")Defines a Unix mount point (e.g. `/dev`). This corresponds roughly to a fstab entry.

[DesktopAppLaunchCallback](https://docs.gtk.org/gio-unix/callback.DesktopAppLaunchCallback.html "DesktopAppLaunchCallback")During invocation, `g_desktop_app_info_launch_uris_as_manager()` may create one or more child processes. This callback is invoked once for each, providing the process ID.

[is_mount_path_system_internal](https://docs.gtk.org/gio-unix/func.is_mount_path_system_internal.html "is_mount_path_system_internal")Determines if `mount_path` is considered an implementation of the OS.
[is_system_device_path](https://docs.gtk.org/gio-unix/func.is_system_device_path.html "is_system_device_path")Determines if `device_path` is considered a block device path which is only used in implementation of the OS.

since: 2.56
[is_system_fs_type](https://docs.gtk.org/gio-unix/func.is_system_fs_type.html "is_system_fs_type")Determines if `fs_type` is considered a type of file system which is only used in implementation of the OS.

since: 2.56
[mount_at](https://docs.gtk.org/gio-unix/func.mount_at.html "mount_at")Gets a `GUnixMountEntry` for a given mount path.

deprecated: 2.84
[mount_compare](https://docs.gtk.org/gio-unix/func.mount_compare.html "mount_compare")Compares two Unix mounts.

deprecated: 2.84
[mount_copy](https://docs.gtk.org/gio-unix/func.mount_copy.html "mount_copy")Makes a copy of `mount_entry`.

deprecated: 2.84 since: 2.54
[mount_entries_changed_since](https://docs.gtk.org/gio-unix/func.mount_entries_changed_since.html "mount_entries_changed_since")Checks if the Unix mounts have changed since a given Unix time.
[mount_entries_get](https://docs.gtk.org/gio-unix/func.mount_entries_get.html "mount_entries_get")Gets a list of `GUnixMountEntry` instances representing the Unix mounts.

since: 2.84
[mount_entries_get_from_file](https://docs.gtk.org/gio-unix/func.mount_entries_get_from_file.html "mount_entries_get_from_file")Gets an array of `GUnixMountEntry`s containing the Unix mounts listed in `table_path`.

since: 2.84
[mount_for](https://docs.gtk.org/gio-unix/func.mount_for.html "mount_for")Gets a `GUnixMountEntry` for a given file path.

deprecated: 2.84 since: 2.52
[mount_free](https://docs.gtk.org/gio-unix/func.mount_free.html "mount_free")Frees a Unix mount.

deprecated: 2.84
[mount_get_device_path](https://docs.gtk.org/gio-unix/func.mount_get_device_path.html "mount_get_device_path")Gets the device path for a Unix mount.

deprecated: 2.84
[mount_get_fs_type](https://docs.gtk.org/gio-unix/func.mount_get_fs_type.html "mount_get_fs_type")Gets the filesystem type for the Unix mount.

deprecated: 2.84
[mount_get_mount_path](https://docs.gtk.org/gio-unix/func.mount_get_mount_path.html "mount_get_mount_path")Gets the mount path for a Unix mount.

deprecated: 2.84
[mount_get_options](https://docs.gtk.org/gio-unix/func.mount_get_options.html "mount_get_options")Gets a comma separated list of mount options for the Unix mount.

deprecated: 2.84 since: 2.58
[mount_get_root_path](https://docs.gtk.org/gio-unix/func.mount_get_root_path.html "mount_get_root_path")Gets the root of the mount within the filesystem.

deprecated: 2.84 since: 2.60
[mount_guess_can_eject](https://docs.gtk.org/gio-unix/func.mount_guess_can_eject.html "mount_guess_can_eject")Guesses whether a Unix mount entry can be ejected.

deprecated: 2.84
[mount_guess_icon](https://docs.gtk.org/gio-unix/func.mount_guess_icon.html "mount_guess_icon")Guesses the icon of a Unix mount entry.

deprecated: 2.84
[mount_guess_name](https://docs.gtk.org/gio-unix/func.mount_guess_name.html "mount_guess_name")Guesses the name of a Unix mount entry.

deprecated: 2.84
[mount_guess_should_display](https://docs.gtk.org/gio-unix/func.mount_guess_should_display.html "mount_guess_should_display")Guesses whether a Unix mount entry should be displayed in the UI.

deprecated: 2.84
[mount_guess_symbolic_icon](https://docs.gtk.org/gio-unix/func.mount_guess_symbolic_icon.html "mount_guess_symbolic_icon")Guesses the symbolic icon of a Unix mount entry.

deprecated: 2.84 since: 2.34
[mount_is_readonly](https://docs.gtk.org/gio-unix/func.mount_is_readonly.html "mount_is_readonly")Checks if a Unix mount is mounted read only.

deprecated: 2.84
[mount_is_system_internal](https://docs.gtk.org/gio-unix/func.mount_is_system_internal.html "mount_is_system_internal")Checks if a Unix mount is a system mount.

deprecated: 2.84
[mount_points_changed_since](https://docs.gtk.org/gio-unix/func.mount_points_changed_since.html "mount_points_changed_since")Checks if the Unix mount points have changed since a given Unix time.
[mount_points_get](https://docs.gtk.org/gio-unix/func.mount_points_get.html "mount_points_get")Gets a list of `GUnixMountPoint` instances representing the Unix mount points.
[mount_points_get_from_file](https://docs.gtk.org/gio-unix/func.mount_points_get_from_file.html "mount_points_get_from_file")Gets an array of `GUnixMountPoint`s containing the Unix mount points listed in `table_path`.

since: 2.82
[mounts_changed_since](https://docs.gtk.org/gio-unix/func.mounts_changed_since.html "mounts_changed_since")Checks if the Unix mounts have changed since a given Unix time.

deprecated: 2.84
[mounts_get](https://docs.gtk.org/gio-unix/func.mounts_get.html "mounts_get")Gets a list of `GUnixMountEntry` instances representing the Unix mounts.

deprecated: 2.84
[mounts_get_from_file](https://docs.gtk.org/gio-unix/func.mounts_get_from_file.html "mounts_get_from_file")Gets an array of `GUnixMountEntry`s containing the Unix mounts listed in `table_path`.

deprecated: 2.84 since: 2.82
