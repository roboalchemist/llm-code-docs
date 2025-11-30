# Source: https://www.electronjs.org/docs/latest/api/structures/color-space

On this page

# ColorSpace Object

- `primaries` string - The color primaries of the color space. Can be one of the following values:

  - `bt709` - BT709 primaries (also used for sRGB)
  - `bt470m` - BT470M primaries
  - `bt470bg` - BT470BG primaries
  - `smpte170m` - SMPTE170M primaries
  - `smpte240m` - SMPTE240M primaries
  - `film` - Film primaries
  - `bt2020` - BT2020 primaries
  - `smptest428-1` - SMPTEST428-1 primaries
  - `smptest431-2` - SMPTEST431-2 primaries
  - `p3` - P3 primaries
  - `xyz-d50` - XYZ D50 primaries
  - `adobe-rgb` - Adobe RGB primaries
  - `apple-generic-rgb` - Apple Generic RGB primaries
  - `wide-gamut-color-spin` - Wide Gamut Color Spin primaries
  - `ebu-3213-e` - EBU 3213-E primaries
  - `custom` - Custom primaries
  - `invalid` - Invalid primaries

- `transfer` string - The transfer function of the color space. Can be one of the following values:

  - `bt709` - BT709 transfer function
  - `bt709-apple` - BT709 Apple transfer function
  - `gamma18` - Gamma 1.8 transfer function
  - `gamma22` - Gamma 2.2 transfer function
  - `gamma24` - Gamma 2.4 transfer function
  - `gamma28` - Gamma 2.8 transfer function
  - `smpte170m` - SMPTE170M transfer function
  - `smpte240m` - SMPTE240M transfer function
  - `linear` - Linear transfer function
  - `log` - Log transfer function
  - `log-sqrt` - Log Square Root transfer function
  - `iec61966-2-4` - IEC61966-2-4 transfer function
  - `bt1361-ecg` - BT1361 ECG transfer function
  - `srgb` - sRGB transfer function
  - `bt2020-10` - BT2020-10 transfer function
  - `bt2020-12` - BT2020-12 transfer function
  - `pq` - PQ (Perceptual Quantizer) transfer function
  - `smptest428-1` - SMPTEST428-1 transfer function
  - `hlg` - HLG (Hybrid Log-Gamma) transfer function
  - `srgb-hdr` - sRGB HDR transfer function
  - `linear-hdr` - Linear HDR transfer function
  - `custom` - Custom transfer function
  - `custom-hdr` - Custom HDR transfer function
  - `scrgb-linear-80-nits` - scRGB Linear 80 nits transfer function
  - `invalid` - Invalid transfer function

- `matrix` string - The color matrix of the color space. Can be one of the following values:

  - `rgb` - RGB matrix
  - `bt709` - BT709 matrix
  - `fcc` - FCC matrix
  - `bt470bg` - BT470BG matrix
  - `smpte170m` - SMPTE170M matrix
  - `smpte240m` - SMPTE240M matrix
  - `ycocg` - YCoCg matrix
  - `bt2020-ncl` - BT2020 NCL matrix
  - `ydzdx` - YDzDx matrix
  - `gbr` - GBR matrix
  - `invalid` - Invalid matrix

- `range` string - The color range of the color space. Can be one of the following values:

  - `limited` - Limited color range (RGB values ranging from 16 to 235)
  - `full` - Full color range (RGB values from 0 to 255)
  - `derived` - Range defined by the transfer function and matrix
  - `invalid` - Invalid range

## Common `ColorSpace` definitions[â€‹](#common-colorspace-definitions "Direct link to common-colorspace-definitions") 

### Standard Color Spaces[â€‹](#standard-color-spaces "Direct link to Standard Color Spaces") 

**sRGB**:

``` 
const cs = 
```

**Display P3**:

``` 
const cs = 
```

**XYZ D50**:

``` 
const cs = 
```

### HDR Color Spaces[â€‹](#hdr-color-spaces "Direct link to HDR Color Spaces") 

**Extended sRGB** (extends sRGB to all real values):

``` 
const cs = 
```

**scRGB Linear** (linear transfer function for all real values):

``` 
const cs = 
```

**scRGB Linear 80 Nits** (with an SDR white level of 80 nits):

``` 
const cs = 
```

**HDR10** (BT.2020 primaries with PQ transfer function):

``` 
const cs = 
```

**HLG** (BT.2020 primaries with HLG transfer function):

``` 
const cs = 
```

### Video Color Spaces[â€‹](#video-color-spaces "Direct link to Video Color Spaces") 

**Rec. 601** (SDTV):

``` 
const cs = 
```

**Rec. 709** (HDTV):

``` 
const cs = 
```

**JPEG** (typical color space for JPEG images):

``` 
const cs = 
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/color-space.md)