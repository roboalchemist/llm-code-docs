# P3 Colors

Understand the P3 wide color gamut and its availability across CE.SDK platforms.

P3 colors are not currently supported on Web platforms. Use [sRGB colors](sveltekit/colors/for-screen/srgb-e6f59b/) instead.

P3 enables more vibrant reds, greens, and other colors beyond the standard sRGB gamut. This is valuable for displays that support the DCI-P3 color space, including modern Apple devices and high-end monitors.

## What is P3?[#](#what-is-p3)

The DCI-P3 color space was developed for digital cinema and has been widely adopted in consumer displays, particularly by Apple since 2016. P3 covers roughly 25% more visible colors than sRGB, especially in the red, orange, and green-cyan regions.

Key differences from sRGB:

*   **Gamut size**: P3 encompasses a larger color range
*   **Primary colors**: P3 red and green are more saturated
*   **Backwards compatibility**: P3 content on sRGB displays is automatically converted

P3 colors only appear more vibrant on P3-capable displays. On sRGB displays, colors are converted and may appear less saturated.

## Platform Support[#](#platform-support)

**Supported platforms:**

*   **Android**: `supportsP3()` and `checkP3Support()` APIs
*   **iOS/Swift**: `supportsP3()` and `checkP3Support()` APIs

**Not supported:**

*   Browser
*   Server (Node.js)

On Web platforms, CE.SDK uses sRGB as the working color space. The Web binding supports sRGB, CMYK, and Spot Colors.

## P3 vs sRGB: When to Use Each[#](#p3-vs-srgb-when-to-use-each)

| Use Case | Recommended |
| --- | --- |
| Native mobile apps (Apple devices) | P3 |
| Photo/video editing with color accuracy | P3 |
| Web applications | sRGB |
| Cross-platform consistency | sRGB |

## Next Steps[#](#next-steps)

*   [sRGB Colors](sveltekit/colors/for-screen/srgb-e6f59b/) — Apply sRGB colors for screen output
*   [Color Conversion](sveltekit/colors/conversion-bcd82b/) — Convert between color spaces

---



[Source](https:/img.ly/docs/cesdk/sveltekit/colors/for-print/spot-c3a150)