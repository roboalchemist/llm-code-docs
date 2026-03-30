# Plugin DataDir

## Description
The plugin is intended for replacement of the current torrent data directory on another. Such operation is required, for example, if the torrent data directory has been moved manually. It is also possible to move downloaded torrent's data.

After plugin installation there will be a new item `Save to...` in the context menu of the downloading area which shows a dialogue `Torrent data directory`. In this dialogue you can specify a new path to the torrent data.

![](images/PluginDataDir/datadir1.png)

![](images/PluginDataDir/datadir2.png)

## How it works

The plugin can change the data directory for another and also move torrent data files.

It is required to specify the **base** directory of the data (without subdirectory stored in torrent file), by analogy to directory choice at addition of new torrent.

Any additional manipulations with re-hashing are not made. rtorrent re-hash torrent data by itself if detects changes of size or modification time of torrent data files.
From this the following follows:
- if the data directory has been simply moved, change of the torrent data directory would not lead to re-hashing.
- if the data directory has been copied, re-hashing would be done (modification time has varied).

For comfortable directory choice on the host for completed downloads it is recommended to install the service plugin [_getdir]. There will be a possibility of navigation on host file system.

It is recommended to install php extention [sysvsem.so](http://ru.php.net/manual/en/sem.installation.php) to prevent simultaneous data moving with group operation.
