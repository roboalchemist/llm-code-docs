## Camera settings

### `disable*camera*led`

Setting `disable*camera*led` to `1` prevents the red camera LED from turning on when recording video or taking a still picture. This is useful for preventing reflections, for example when the camera is facing a window.

### `awb*auto*is*greyworld`

Setting `awb*auto*is*greyworld` to `1` allows libraries or applications that do not support the greyworld option internally to capture valid images and videos with NoIR cameras. It switches auto awb mode to use the greyworld algorithm. This should only be needed for NoIR cameras, or when the High Quality camera has had its xref:../accessories/camera.adoc#filter-removal[IR filter removed].