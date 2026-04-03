# Plugin Cpuload

## Description

This plugin adds a CPU Load usage bar to the bottom toolbar.

![CPU Load plugin screenshot](images/PluginCpuload/cpuload.png)

## How it Works

The plugin is purely for cosmetic use. It's pretty generalized in it's current state, and should not be taken as 100% accurate.
The formula for cpuload, currently is

```text
min(load_average[0]*100/processors_count,100)
```

where `load_average[0]` - count of processes in run queue in the last minute.

processors_count is always 1 for non-Linux systems.
