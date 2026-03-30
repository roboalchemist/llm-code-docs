# Plugin Check_Port

## Description

This plugin adds an incoming port status indicator to the bottom bar.

![](images/PluginCheck_Port/check_port.png)

When right-clicking on the indicator > "Check Port Status", you can check the port status again.

## NOTES

- By default, this plugin uses [YouGetSignal](https://www.yougetsignal.com/tools/open-ports/) website to check the port status. You can change this in the "conf.php" plugin's file.
- For rtorrent version less than 0.8.9, it's impossible to find out via the API which port is actually used from a port range configuration ; the very first port is checked.
