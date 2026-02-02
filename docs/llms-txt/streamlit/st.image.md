# st.image

Display an image or list of images.

## Function signature

```jsx
st.image(image, caption=None, width="content", use_column_width=None, clamp=False, channels="RGB", output_format="auto", *, use_container_width=None)
```

## Parameters

- **image** (numpy.ndarray, BytesIO, str, Path, or list of these)
  - The image to display. This can be one of the following:
    - A URL (string) for a hosted image.
    - A path to a local image file. The path can be a `str` or `Path` object. Paths can be absolute or relative to the working directory (where you execute `streamlit run`).
    - An SVG string like `<svg <span class="pre">xmlns=...</span></svg>`.
    - A byte array defining an image. This includes monochrome images of shape (w,h) or (w,h,1), color images of shape (w,h,3), or RGBA images of shape (w,h,4), where w and h are the image width and height, respectively.
    - A list of any of the above. Streamlit displays the list as a row of images that overflow to additional rows as needed.

- **caption** (str or list of str)
  - Image caption(s). If this is `None` (default), no caption is displayed. If `image` is a list of multiple images, `caption` must be a list of captions (one caption for each image) or `None`.
  - Captions can optionally contain GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).
  - See the `body` parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

- **width** ("content", "stretch", or int)
  - The width of the image element. This can be one of the following:
    - `"content"` (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    - `"stretch"`: The width of the element matches the width of the parent container.
    - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
  - When using an SVG image without a default width, use `"stretch"` or an integer.

- **use_column_width** ("auto", "always", "never", or bool)
  - If `"auto"`, set the image's width to its natural size, but do not exceed the width of the column. If `"always"` or `True`, set the image's width to the column width. If `"never"` or `False`, set the image's width to its natural size. Note: if set, `use_column_width` takes precedence over the `width` parameter.

- **clamp** (bool)
  - Whether to clamp image pixel values to a valid range (0-255 per channel). This is only used for byte array images; the parameter is ignored for image URLs and files. If this is `False` (default) and an image has an out-of-range value, a `RuntimeError` will be raised.

- **channels** ("RGB" or "BGR")
  - The color format when `image` is an `nd.array`. This is ignored for other image types. If this is `"RGB"` (default), `image[:, :, 0]` is the red channel, `image[:, :, 1]` is the green channel, and `image[:, :, 2]` is the blue channel. For images coming from libraries like OpenCV, you should set this to `"BGR"` instead.

- **output_format** ("JPEG", "PNG", or "auto")
  - The output format to use when transferring the image data. If this is `"auto"` (default), Streamlit identifies the compression type based on the type and format of the image. Photos should use the `"JPEG"` format for lossy compression while diagrams should use the `"PNG"` format for lossless compression.

- **use_container_width** (bool)
  - Whether to override `width` with the width of the parent container. If `use_container_width` is `False` (default), Streamlit sets the image's width according to `width`. If `use_container_width` is `True`, Streamlit sets the width of the image to match the width of the parent container.

## Example

```jsx
import streamlit as st
st.image("sunrise.jpg", caption="Sunrise by the mountains")
```

## Additional Information

Display an image or list of images.

## Notes

## Version

Streamlit Version

- Version 1.52.0
- Version 1.51.0
- Version 1.50.0
- Version 1.49.0
- Version 1.48.0
- Version 1.47.0
- Version 1.46.0
- Version 1.45.0
- Version 1.44.0
- Version 1.43.0
- Version 1.42.0
- Version 1.41.0
- Version 1.40.0
- Version 1.39.0
- Version 1.38.0
- Version 1.37.0
- Version 1.36.0
- Version 1.35.0
- Version 1.34.0
- Version 1.33.0
- Version 1.32.0
- Version 1.31.0
- Version 1.30.0
- Version 1.29.0
- Version 1.28.0
- Version 1.27.0
- Version 1.26.0
- Version 1.25.0
- Version 1.24.0
- Version 1.23.0
- Version 1.22.0

## Built with

Streamlit Version

- Version 1.52.0
- Version 1.51.0
- Version 1.50.0
- Version 1.49.0
- Version 1.48.0
- Version 1.47.0
- Version 1.46.0
- Version 1.45.0
- Version 1.44.0
- Version 1.43.0
- Version 1.42.0
- Version 1.41.0
- Version 1.40.0
- Version 1.39.0
- Version 1.38.0
- Version 1.37.0
- Version 1.36.0
- Version 1.35.0
- Version 1.34.0
- Version 1.33.0
- Version 1.32.0
- Version 1.31.0
- Version 1.30.0
- Version 1.29.0
- Version 1.28.0
- Version 1.27.0
- Version 1.26.0
- Version 1.25.0
- Version 1.24.0
- Version 1.23.0
- Version 1.22.0

## Contact Us

[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)

## Community

[Community](https://discuss.streamlit.io)

## Newsletter

[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

## © 2025 Snowflake Inc.