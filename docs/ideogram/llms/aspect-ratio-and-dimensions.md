# Source: https://docs.ideogram.ai/using-ideogram/generation-settings/aspect-ratio-and-dimensions.md

# Aspect Ratio and Dimensions

Aspect Ratio controls the proportions of your generated images. Depending on the Ideogram model version, you can choose from different preset and custom ratio options. See [Available Models](https://docs.ideogram.ai/using-ideogram/generation-settings/available-models) for version-specific capabilities.

To select a specific aspect ratio:

1. Select the [Prompt Box](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/prompt-box) to expand it (if not already expanded) and display the generation settings.
2. Select  **Aspect Ratio** (displayed as the actual aspect ratio, such as <kbd>**1:1**</kbd>) to view the available formats.

<figure><picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FpqPJlXdGwOrRfrhgoZPW%2FPB%20v3%20-%20Aspect%20Ratio%20-%20Dark%402x.png?alt=media&#x26;token=7faa5a61-0da0-4c1d-9eed-e0c1ccf84ec3" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2Fq7TorINT1Mg7enCAi7KX%2FPB%20v3%20-%20Aspect%20Ratio%20-%20Light%402x.png?alt=media&#x26;token=0c70609f-6ceb-40f0-a3d2-e8bb581f8010" alt="Aspect Ratio dropdown showing available preset formats." width="563"></picture><figcaption><p>Aspect ratio dropdown showing the available format options.</p></figcaption></figure>

## Default Aspect Ratios and Sizes

The table below shows the available default aspect ratios for each model and the size of the generated images they produce.

|     Aspect Ratio     | Dimensions (v1.0) | Dimensions (v2.0, v2a, v3.0) |
| :------------------: | :---------------: | :--------------------------: |
|  <kbd>**1:3**</kbd>  |     512 x 1536    |          512 x 1536          |
|  <kbd>**1:2**</kbd>  |      — N/A —      |          704 x 1408          |
|  <kbd>**9:16**</kbd> |     720 x 1280    |          736 x 1312          |
| <kbd>**10:16**</kbd> |     768 x 1232    |          800 x 1280          |
|  <kbd>**2:3**</kbd>  |     768 x 1152    |          832 x 1248          |
|  <kbd>**3:4**</kbd>  |     768 x 1024    |          864 x 1152          |
|  <kbd>**4:5**</kbd>  |      — N/A —      |          896 x 1120          |
|  <kbd>**1:1**</kbd>  |    1024 x 1024    |          1024 x 1024         |
|  <kbd>**5:4**</kbd>  |      — N/A —      |          1120 x 896          |
|  <kbd>**4:3**</kbd>  |     1024 x 768    |          1152 x 864          |
|  <kbd>**3:2**</kbd>  |     1152 x 768    |          1248 x 832          |
| <kbd>**16:10**</kbd> |     1232 x 768    |          1280 x 800          |
|  <kbd>**16:9**</kbd> |     1280 x 720    |          1312 x 736          |
|  <kbd>**2:1**</kbd>  |      — N/A —      |          1408 x 704          |
|  <kbd>**3:1**</kbd>  |     1536 x 512    |          1536 x 512          |

## Common Presets

### Vertical

* <kbd>**1:3**</kbd> – Very tall banner.
* <kbd>**1:2**</kbd> – Tall vertical format. Sometimes used in artworks or creative compositions. *Version 2.0 and higher.*
* <kbd>**9:16**</kbd> *–* Ideal for vertical display on smartphones and some social networking sites.
* <kbd>**10:16**</kbd> *–* Portrait format originally used in early Ideogram versions 0.1 and 0.2.
* <kbd>**2:3**</kbd> *–* Portrait format mainly used in digital photography and poster printing.
* <kbd>**3:4**</kbd> *–* Portrait aspect ratio mainly used in film photography.
* <kbd>**4:5**</kbd> *–* Common portrait ratio used in film photography.

### Square

* <kbd>**1:1**</kbd> *–* A square format, often used in social media and image sites.

### Horizontal

* <kbd>**5:4**</kbd> *–* Landscape aspect ratio mainly used in film photography.
* <kbd>**4:3**</kbd> *–* Landscape format, used by old traditional standard definition television. Also used in film photography.
* <kbd>**3:2**</kbd> *–* Popular landscape format used in digital photography and printing.
* <kbd>**16:10**</kbd> *–* Landscape format originally used in now retired Ideogram versions 0.1 and 0.2.
* <kbd>**16:9**</kbd> *–* Landscape format commonly used in modern horizontal screens, including TV.
* <kbd>**2:1**</kbd> *–* Large banner. Commonly used for 360° equirectangular panoramas.
* <kbd>**3:1**</kbd> *–* Very large banner.

## Custom Aspect Ratios

You can create a custom aspect ratio when the default options don’t meet your needs.

In versions 2.0 and later, users on the **Basic Plan** or higher can use custom aspect ratios in two ways:

1. Use the **Slider** under the *aspect ratio preview* to access continuous ratio values beyond the presets.
2. Select **Custom** to manually enter the desired aspect ratio or pixel dimensions. The interface automatically adjusts to the nearest supported ratio between <kbd>**1:3**</kbd> and <kbd>**3:1**</kbd>.

<figure><picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FdBh1W6VCHkqceDWIFCG9%2FPB%20v3%20-%20Aspect%20Ratio%20-%20Dark%402x.png?alt=media&#x26;token=35636dbb-9b25-4bd6-907c-3bb6195a4f0d" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FiMRsyZ4T4QzImryUMsjm%2FPB%20v3%20-%20Aspect%20Ratio%20-%20Light%402x.png?alt=media&#x26;token=e1749e40-ea4e-4b4d-8bc0-11ecce241fca" alt="Screenshot of the Aspect Ratio slider with numeric entry fields." width="563"></picture><figcaption><p>Aspect Ratio preview with the slider control and custom entry fields.</p></figcaption></figure>

The table below lists all supported custom aspect ratios and their corresponding pixel dimensions, arranged from the widest to the tallest.

|     Aspect Ratio     | Pixel dimensions |
| :------------------: | :--------------: |
|  <kbd>**3:1**</kbd>  |    1536 x 512    |
|  <kbd>**8:3**</kbd>  |    1536 x 576    |
|  <kbd>**23:9**</kbd> |    1472 x 576    |
|  <kbd>**22:9**</kbd> |    1408 x 576    |
|  <kbd>**12:5**</kbd> |    1536 x 640    |
| <kbd>**23:10**</kbd> |    1472 x 640    |
|  <kbd>**11:5**</kbd> |    1408 x 640    |
| <kbd>**21:10**</kbd> |    1344 x 640    |
| <kbd>**23:11**</kbd> |    1472 x 704    |
|  <kbd>**2:1**</kbd>  |    1408 x 704    |
| <kbd>**21:11**</kbd> |    1344 x 704    |
| <kbd>**20:11**</kbd> |    1280 x 704    |
|  <kbd>**16:9**</kbd> |    1312 x 736    |
|  <kbd>**7:4**</kbd>  |    1344 x 768    |
| <kbd>**19:11**</kbd> |    1216 x 704    |
|  <kbd>**5:3**</kbd>  |    1280 x 768    |
| <kbd>**18:11**</kbd> |    1152 x 704    |
| <kbd>**16:10**</kbd> |    1280 x 800    |
| <kbd>**19:12**</kbd> |    1216 x 768    |
|  <kbd>**3:2**</kbd>  |    1248 x 832    |
| <kbd>**19:13**</kbd> |    1216 x 832    |
| <kbd>**17:12**</kbd> |    1088 x 768    |
| <kbd>**18:13**</kbd> |    1152 x 832    |
|  <kbd>**4:3**</kbd>  |    1152 x 864    |
| <kbd>**17:13**</kbd> |    1088 x 832    |
|  <kbd>**9:7**</kbd>  |    1152 x 896    |
|  <kbd>**5:4**</kbd>  |    1120 x 896    |
| <kbd>**16:13**</kbd> |    1024 x 832    |
| <kbd>**17:14**</kbd> |    1088 x 896    |
| <kbd>**15:13**</kbd> |     960 x 832    |
|  <kbd>**8:7**</kbd>  |    1024 x 896    |
| <kbd>**17:15**</kbd> |    1088 x 960    |
| <kbd>**15:14**</kbd> |     960 x 896    |
| <kbd>**16:15**</kbd> |    1024 x 960    |
|  <kbd>**1:1**</kbd>  |    1024 x 1024   |
| <kbd>**15:16**</kbd> |    960 x 1024    |
| <kbd>**14:15**</kbd> |     896 x 960    |
| <kbd>**15:17**</kbd> |    960 x 1088    |
|  <kbd>**7:8**</kbd>  |    896 x 1024    |
| <kbd>**13:15**</kbd> |     832 x 960    |
| <kbd>**14:17**</kbd> |    896 x 1088    |
| <kbd>**13:16**</kbd> |    832 x 1024    |
|  <kbd>**4:5**</kbd>  |    896 x 1120    |
|  <kbd>**7:9**</kbd>  |    896 x 1152    |
| <kbd>**13:17**</kbd> |    832 x 1088    |
|  <kbd>**3:4**</kbd>  |    864 x 1152    |
| <kbd>**13:18**</kbd> |    832 x 1152    |
| <kbd>**12:17**</kbd> |    768 x 1088    |
| <kbd>**13:19**</kbd> |    832 x 1216    |
|  <kbd>**2:3**</kbd>  |    832 x 1248    |
| <kbd>**12:19**</kbd> |    768 x 1216    |
| <kbd>**10:16**</kbd> |    800 x 1280    |
| <kbd>**11:18**</kbd> |    704 x 1152    |
|  <kbd>**3:5**</kbd>  |    768 x 1280    |
| <kbd>**11:19**</kbd> |    704 x 1216    |
|  <kbd>**4:7**</kbd>  |    768 x 1344    |
|  <kbd>**9:16**</kbd> |    736 x 1312    |
| <kbd>**11:20**</kbd> |    704 x 1280    |
| <kbd>**11:21**</kbd> |    704 x 1344    |
|  <kbd>**1:2**</kbd>  |    704 x 1408    |
| <kbd>**11:23**</kbd> |    704 x 1472    |
| <kbd>**10:21**</kbd> |    640 x 1344    |
|  <kbd>**5:11**</kbd> |    640 x 1408    |
| <kbd>**10:23**</kbd> |    640 x 1472    |
|  <kbd>**5:12**</kbd> |    640 x 1536    |
|  <kbd>**9:22**</kbd> |    576 x 1408    |
|  <kbd>**9:23**</kbd> |    576 x 1472    |
|  <kbd>**3:8**</kbd>  |    576 x 1536    |
|  <kbd>**1:3**</kbd>  |    512 x 1536    |
