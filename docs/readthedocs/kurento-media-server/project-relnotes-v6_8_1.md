# 6.8.1 (Oct 2018)

Release 6.8.0 contained a critical bug that was immediately patched into 6.8.1, so these Release Notes include changes from both versions.

This release goes hand-in-hand with a new version of **OpenVidu**, Kurento’s sister project. Check OpenVidu 2.5.0 Release Notes [https://medium.com/@openvidu/openvidu-2-5-0-voice-and-video-filters-45c0fb8e52e0] if you are interested in building any of the common use cases that are covered by that project, such as conference calls and video chat rooms.

## Added

- 

Log messages that come from *GLib*-based libraries are now integrated into the general Kurento logging system.

Previous to this addition, the only way to obtain debug logs from the *libnice* library was to run KMS directly on console; even after enabling debug logging, the relevant messages would not appear in the Kurento logs because *libnice* was just printing its messages in the standard output.

Starting from KMS 6.8.0, all messages will be redirected to Kurento logs, located at `/var/log/kurento-media-server/`. Remember that specific 3rd-party libraries such as *libnice* still require that their logging functions are explicitly enabled; check libnice for more details.

- 

**Hub** and **HubPort** elements now support for DATA streams. This means that a WebRTC DataChannels stream can be processed through a *Hub*, for example a **Composite**, and the DATA stream will be available for the element to process.

- 

Thanks to the previous addition, **Composite** element has now support for merging multiple DataChannel streams.

- 

**GStreamerFilter** is now able to set its inner element’s properties “on the fly” during runtime. For example, if you used a **coloreffects** filter, before this addition you would need to configure the video parameters beforehand, and they would stay the same during the whole execution of the Kurento pipeline. Now, it is possible to change the filter’s properties at any time, during the execution of the pipeline.

The OpenVidu project is using this capability to offer real-time audio/video filtering during WebRTC calls; check Voice and video filters [https://openvidu.io/docs/advanced-features/filters/] for more details.

## Changed

- 

Output logs now use standard format ISO 8601 for all timestamps. This affects both log files names, and their contents:

Log files will now be named such as this:

```
2018-06-14T194426.00000.pid13006.log

```