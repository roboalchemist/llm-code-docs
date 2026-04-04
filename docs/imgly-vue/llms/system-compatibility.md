# System Compatibility

CE.SDK runs entirely on clients and makes use of hardware acceleration provided within that environment. Therefore, the user’s hardware always acts as an upper bound of what’s achievable.

The editor’s performance scales with scene complexity. We generally found scenes with up to 200 blocks well usable, but complex blocks like auto-sizing text or high-resolution image fills may affect performance negatively. This is always constrained by the processing power available on the user’s device, so for low-end devices, the experience may suffer earlier. Therefore, it’s generally desirable to keep scenes only as complex as needed.

## Hardware Limitations[#](#hardware-limitations)

Each device has a limited amount of high performance hardware decoders and encoders. If the maximum number is reached it will fall back to (slow) software de- and encoding. Therefore users may encounter slow export performance when trying to export in parallel with other software that utilizes encoders and decoders, e.g. Zoom, Teams or video content in other tabs / apps. This, unfortunately, is a limitation of hardware, operating system and browser and cannot be solved.

## Recommended Hardware[#](#recommended-hardware)

| Platform | Hardware |
| --- | --- |
| Desktop | A notebook or desktop released in the last 7 years and at least 4GB of memory. |
| Mobile (Apple) | iPhone 8, iPad (6th gen) or newer |
| Mobile (Android) | Phones & tablets released in the last 4 years |

## Video[#](#video)

Our video feature introduces additional requirements and we generally distinguish playback (decoding) and export (encoding) capabilities. On the web, certain browser features directly depend on the host operating system. For video, this currently introduces the following limitations:

*   Transparency in H.265 videos is **not supported** on Windows hosts.
*   **Chrome on Linux** generally doesn’t ship with encoder support for H.264 & AAC, which can cause video exports to fail even though decoding of non-free codecs is supported.
*   **Chromium** although technically the base of Chrome doesn’t include any codecs for licensing reasons and therefore can’t be used for video editing. It does fall back to system-provided media libraries on e.g. macOS, but support is not guaranteed in any way.
*   Video is **not supported** on mobile browsers on any platform due to technical limitations which result in performance issues.

## Export Limitations[#](#export-limitations)

The export size is limited by the hardware capabilities of the device, e.g., due to the maximum texture size that can be allocated. The maximum possible export size can be queried via API, see [export guide](vue/export-save-publish/export/overview-9ed3a8/) .

---



[Source](https:/img.ly/docs/cesdk/vue/colors-a9b79c)