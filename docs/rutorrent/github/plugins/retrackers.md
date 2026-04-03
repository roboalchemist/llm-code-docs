# Plugin Retrackers

## Introduction

This plugin appends specified trackers to the trackers list of all newly added torrents.
By the way, torrents may be added by any way - not just via ruTorrent.

After the plugin is installed an additional section "Retrackers" will appear in the Settings dialog.

![](images/PluginRetrackers/retrackers.png)

Format of the trackers list is the same as for [µTorrent](http://www.utorrent.com) - different groups of trackers must be separated by an empty line. All listed trackers will be added to existing ones beginning from trackers group 1.
Usually modifications of the the trackers list for private torrents are not welcome. But if you really want it - reset the tick in the dialog window.

## How does it work

After first start of ruTorrent with installed Retrackers plugin, ruTorrent registers it's own hook for the "New torrent added" event.
Then as this event occurs a special script changes the list of trackers in the torrent.

Once again - the processing will be started until first start of ruTorrent.
I.e. there will not be any useful action between start of rtorrent and then first start of ruTorrent.
To avoid this you need to add a special string to the rtorrent configuration file (see [How to start plugins with rtorrent] for details).

To change the list of trackers manually, use plugin [Edit].
