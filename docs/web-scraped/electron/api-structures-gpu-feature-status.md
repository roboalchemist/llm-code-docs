# Source: https://www.electronjs.org/docs/latest/api/structures/gpu-feature-status

# GPUFeatureStatus Object

- `2d_canvas` string - Canvas.
- `flash_3d` string - Flash.
- `flash_stage3d` string - Flash Stage3D.
- `flash_stage3d_baseline` string - Flash Stage3D Baseline profile.
- `gpu_compositing` string - Compositing.
- `multiple_raster_threads` string - Multiple Raster Threads.
- `native_gpu_memory_buffers` string - Native GpuMemoryBuffers.
- `rasterization` string - Rasterization.
- `video_decode` string - Video Decode.
- `video_encode` string - Video Encode.
- `vpx_decode` string - VPx Video Decode.
- `webgl` string - WebGL.
- `webgl2` string - WebGL2.

Possible values:

- `disabled_software` - Software only. Hardware acceleration disabled (yellow)
- `disabled_off` - Disabled (red)
- `disabled_off_ok` - Disabled (yellow)
- `unavailable_software` - Software only, hardware acceleration unavailable (yellow)
- `unavailable_off` - Unavailable (red)
- `unavailable_off_ok` - Unavailable (yellow)
- `enabled_readback` - Hardware accelerated but at reduced performance (yellow)
- `enabled_force` - Hardware accelerated on all pages (green)
- `enabled` - Hardware accelerated (green)
- `enabled_on` - Enabled (green)
- `enabled_force_on` - Force enabled (green)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/gpu-feature-status.md)