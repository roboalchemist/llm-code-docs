### Index ¶

- Constants

- Variables

- 
        func ColourspaceIsSupported(buf []byte) (bool, error)

- 
        func DetermineImageTypeName(buf []byte) string

- 
        func ImageTypeName(t ImageType) string

- 
        func Initialize()

- 
        func IsSVGImage(buf []byte) bool

- 
        func IsTypeNameSupported(t string) bool

- 
        func IsTypeNameSupportedSave(t string) bool

- 
        func IsTypeSupported(t ImageType) bool

- 
        func IsTypeSupportedSave(t ImageType) bool

- 
        func MaxSize() int

- 
        func Read(path string) ([]byte, error)

- 
        func Resize(buf []byte, o Options) ([]byte, error)

- 
        func SetMaxsize(s int) error

- 
        func Shutdown()

- 
        func VipsCacheDropAll()

- 
        func VipsCacheSetMax(maxCacheSize int)

- 
        func VipsCacheSetMaxMem(maxCacheMem int)

- 
        func VipsDebugInfo()

- 
        func VipsIsTypeSupported(t ImageType) bool

- 
        func VipsIsTypeSupportedSave(t ImageType) bool

- 
        func VipsVectorSetEnabled(enable bool)

- 
        func Write(path string, buf []byte) error

- 
          type Angle

- 
          type Color

- 
          type Direction

- 
          type EXIF

- 
          type Extend

- 
          type GaussianBlur

- 
          type Gravity

- 
          type Image

- 

  - 
            func NewImage(buf []byte) *Image

- 

  - 
            func (i *Image) AutoRotate() ([]byte, error)

  - 
            func (i *Image) Colourspace(c Interpretation) ([]byte, error)

  - 
            func (i *Image) ColourspaceIsSupported() (bool, error)

  - 
            func (i *Image) Convert(t ImageType) ([]byte, error)

  - 
            func (i *Image) Crop(width, height int, gravity Gravity) ([]byte, error)

  - 
            func (i *Image) CropByHeight(height int) ([]byte, error)

  - 
            func (i *Image) CropByWidth(width int) ([]byte, error)

  - 
            func (i *Image) Enlarge(width, height int) ([]byte, error)

  - 
            func (i *Image) EnlargeAndCrop(width, height int) ([]byte, error)

  - 
            func (i *Image) Extract(top, left, width, height int) ([]byte, error)

  - 
            func (i *Image) Flip() ([]byte, error)

  - 
            func (i *Image) Flop() ([]byte, error)

  - 
            func (i *Image) ForceResize(width, height int) ([]byte, error)

  - 
            func (i *Image) Gamma(exponent float64) ([]byte, error)

  - 
            func (i *Image) Image() []byte

  - 
            func (i *Image) Interpretation() (Interpretation, error)

  - 
            func (i *Image) Length() int

  - 
            func (i *Image) Metadata() (ImageMetadata, error)

  - 
            func (i *Image) Process(o Options) ([]byte, error)

  - 
            func (i *Image) Resize(width, height int) ([]byte, error)

  - 
            func (i *Image) ResizeAndCrop(width, height int) ([]byte, error)

  - 
            func (i *Image) Rotate(a Angle) ([]byte, error)

  - 
            func (i *Image) Size() (ImageSize, error)

  - 
            func (i *Image) SmartCrop(width, height int) ([]byte, error)

  - 
            func (i *Image) Thumbnail(pixels int) ([]byte, error)

  - 
            func (i *Image) Trim() ([]byte, error)

  - 
            func (i *Image) Type() string

  - 
            func (i *Image) Watermark(w Watermark) ([]byte, error)

  - 
            func (i *Image) WatermarkImage(w WatermarkImage) ([]byte, error)

  - 
            func (i *Image) Zoom(factor int) ([]byte, error)

- 
          type ImageMetadata

- 

  - 
            func Metadata(buf []byte) (ImageMetadata, error)

- 
          type ImageSize

- 

  - 
            func Size(buf []byte) (ImageSize, error)

- 
          type ImageType

- 

  - 
            func DetermineImageType(buf []byte) ImageType

- 
          type Interpolator

- 

  - 
            func (i Interpolator) String() string

- 
          type Interpretation

- 

  - 
            func ImageInterpretation(buf []byte) (Interpretation, error)

- 
          type Options

- 
          type Sharpen

- 
          type SupportedImageType

- 

  - 
            func IsImageTypeSupportedByVips(t ImageType) SupportedImageType

- 
          type VipsMemoryInfo

- 

  - 
            func VipsMemory() VipsMemoryInfo

- 
          type Watermark

- 
          type WatermarkImage

### Constants ¶

  
    
      View Source
      

```
const (
	Make                    = "exif-ifd0-Make"
	Model                   = "exif-ifd0-Model"
	Orientation             = "exif-ifd0-Orientation"
	XResolution             = "exif-ifd0-XResolution"
	YResolution             = "exif-ifd0-YResolution"
	ResolutionUnit          = "exif-ifd0-ResolutionUnit"
	Software                = "exif-ifd0-Software"
	Datetime                = "exif-ifd0-DateTime"
	YCbCrPositioning        = "exif-ifd0-YCbCrPositioning"
	Compression             = "exif-ifd1-Compression"
	ExposureTime            = "exif-ifd2-ExposureTime"
	FNumber                 = "exif-ifd2-FNumber"
	ExposureProgram         = "exif-ifd2-ExposureProgram"
	ISOSpeedRatings         = "exif-ifd2-ISOSpeedRatings"
	ExifVersion             = "exif-ifd2-ExifVersion"
	DateTimeOriginal        = "exif-ifd2-DateTimeOriginal"
	DateTimeDigitized       = "exif-ifd2-DateTimeDigitized"
	ComponentsConfiguration = "exif-ifd2-ComponentsConfiguration"
	ShutterSpeedValue       = "exif-ifd2-ShutterSpeedValue"
	ApertureValue           = "exif-ifd2-ApertureValue"
	BrightnessValue         = "exif-ifd2-BrightnessValue"
	ExposureBiasValue       = "exif-ifd2-ExposureBiasValue"
	MeteringMode            = "exif-ifd2-MeteringMode"
	Flash                   = "exif-ifd2-Flash"
	FocalLength             = "exif-ifd2-FocalLength"
	SubjectArea             = "exif-ifd2-SubjectArea"
	MakerNote               = "exif-ifd2-MakerNote"
	SubSecTimeOriginal      = "exif-ifd2-SubSecTimeOriginal"
	SubSecTimeDigitized     = "exif-ifd2-SubSecTimeDigitized"
	ColorSpace              = "exif-ifd2-ColorSpace"
	PixelXDimension         = "exif-ifd2-PixelXDimension"
	PixelYDimension         = "exif-ifd2-PixelYDimension"
	SensingMethod           = "exif-ifd2-SensingMethod"
	SceneType               = "exif-ifd2-SceneType"
	ExposureMode            = "exif-ifd2-ExposureMode"
	WhiteBalance            = "exif-ifd2-WhiteBalance"
	FocalLengthIn35mmFilm   = "exif-ifd2-FocalLengthIn35mmFilm"
	SceneCaptureType        = "exif-ifd2-SceneCaptureType"
	GPSLatitudeRef          = "exif-ifd3-GPSLatitudeRef"
	GPSLatitude             = "exif-ifd3-GPSLatitude"
	GPSLongitudeRef         = "exif-ifd3-GPSLongitudeRef"
	GPSLongitude            = "exif-ifd3-GPSLongitude"
	GPSAltitudeRef          = "exif-ifd3-GPSAltitudeRef"
	GPSAltitude             = "exif-ifd3-GPSAltitude"
	GPSSpeedRef             = "exif-ifd3-GPSSpeedRef"
	GPSSpeed                = "exif-ifd3-GPSSpeed"
	GPSImgDirectionRef      = "exif-ifd3-GPSImgDirectionRef"
	GPSImgDirection         = "exif-ifd3-GPSImgDirection"
	GPSDestBearingRef       = "exif-ifd3-GPSDestBearingRef"
	GPSDestBearing          = "exif-ifd3-GPSDestBearing"
	GPSDateStamp            = "exif-ifd3-GPSDateStamp"
)
```

    
  

Common EXIF fields for data extraction

    
      View Source
      

```
const (
	// Quality defines the default JPEG quality to be used.
	Quality = 75
)
```

    
  

    
      View Source
      

```
const Version = "1.1.9"
```

    
  

Version represents the current package semantic version.

    
      View Source
      

```
const VipsMajorVersion = int(C.VIPS_MAJOR_VERSION)
```

    
  

VipsMajorVersion exposes the current libvips major version number

    
      View Source
      

```
const VipsMinorVersion = int(C.VIPS_MINOR_VERSION)
```

    
  

VipsMinorVersion exposes the current libvips minor version number

    
      View Source
      

```
const VipsVersion = string(C.VIPS_VERSION)
```

    
  

VipsVersion exposes the current libvips semantic version

  
### Variables ¶

  
    
      View Source
      

```
var ColorBlack = Color{0, 0, 0}
```

    
  

ColorBlack is a shortcut to black RGB color representation.

    
      View Source
      

```
var (
	// ErrExtractAreaParamsRequired defines a generic extract area error
	ErrExtractAreaParamsRequired = errors.New("extract area width/height params are required")
)
```

    
  

    
      View Source
      

```
var ImageTypes = map[ImageType]string{
	JPEG:   "jpeg",
	PNG:    "png",
	WEBP:   "webp",
	TIFF:   "tiff",
	GIF:    "gif",
	PDF:    "pdf",
	SVG:    "svg",
	MAGICK: "magick",
	HEIF:   "heif",
	AVIF:   "avif",
}
```

    
  

ImageTypes stores as pairs of image types supported and its alias names.

    
      View Source
      

```
var SupportedImageTypes = map[ImageType]SupportedImageType{}
```

    
  

SupportedImageTypes stores the optional image type supported
by the current libvips compilation.
Note: lazy evaluation as demand is required due
to bootstrap runtime limitation with C/libvips world.

    
      View Source
      

```
var WatermarkFont = "sans 10"
```

    
  

WatermarkFont defines the default watermark font to be used.

  
### Functions ¶

  
	  
  
  
    
#### 
      func ColourspaceIsSupported ¶
  
    
  

    
    
      

```
func ColourspaceIsSupported(buf []byte) (bool, error)
```

    
  

ColourspaceIsSupported checks if the image colourspace is supported by libvips.

  

        
	  
  
  
    
#### 
      func DetermineImageTypeName ¶
  
    
  

    
    
      

```
func DetermineImageTypeName(buf []byte) string
```

    
  

DetermineImageTypeName determines the image type format by name (jpeg, png, webp or tiff)

  

        
	  
  
  
    
#### 
      func ImageTypeName ¶
  
    
  

    
    
      

```
func ImageTypeName(t ImageType) string
```

    
  

ImageTypeName is used to get the human friendly name of an image format.

  

        
	  
  
  
    
#### 
      func Initialize ¶
  
    
  

    
    
      

```
func Initialize()
```

    
  

Initialize is used to explicitly start libvips in thread-safe way.
Only call this function if you have previously turned off libvips.

  

        
	  
  
  
    
#### 
      func IsSVGImage ¶
  
    
      added in
      v1.0.3
    
  

    
    
      

```
func IsSVGImage(buf []byte) bool
```

    
  

IsSVGImage returns true if the given buffer is a valid SVG image.

  

        
	  
  
  
    
#### 
      func IsTypeNameSupported ¶
  
    
  

    
    
      

```
func IsTypeNameSupported(t string) bool
```

    
  

IsTypeNameSupported checks if a given image type name is supported

  

        
	  
  
  
    
#### 
      func IsTypeNameSupportedSave ¶
  
    
      added in
      v1.0.7
    
  

    
    
      

```
func IsTypeNameSupportedSave(t string) bool
```

    
  

IsTypeNameSupportedSave checks if a given image type name is supported for
saving

  

        
	  
  
  
    
#### 
      func IsTypeSupported ¶
  
    
  

    
    
      

```
func IsTypeSupported(t ImageType) bool
```

    
  

IsTypeSupported checks if a given image type is supported

  

        
	  
  
  
    
#### 
      func IsTypeSupportedSave ¶
  
    
      added in
      v1.0.7
    
  

    
    
      

```
func IsTypeSupportedSave(t ImageType) bool
```

    
  

IsTypeSupportedSave checks if a given image type is support for saving

  

        
	  
  
  
    
#### 
      func MaxSize ¶
  
    
      added in
      v1.0.0
    
  

    
    
      

```
func MaxSize() int
```

    
  

MaxSize returns maxSize.

  

        
	  
  
  
    
#### 
      func Read ¶
  
    
  

    
    
      

```
func Read(path string) ([]byte, error)
```

    
  

Read reads all the content of the given file path
and returns it as byte buffer.

  

        
	  
  
  
    
#### 
      func Resize ¶
  
    
  

    
    
      

```
func Resize(buf []byte, o Options) ([]byte, error)
```

    
  

Resize is used to transform a given image as byte buffer
with the passed options.

  

        
	  
  
  
    
#### 
      func SetMaxsize ¶
  
    
      added in
      v1.1.8
    
  

    
    
      

```
func SetMaxsize(s int) error
```

    
  

SetMaxSize sets maxSize.

  

        
	  
  
  
    
#### 
      func Shutdown ¶
  
    
  

    
    
      

```
func Shutdown()
```

    
  

Shutdown is used to shutdown libvips in a thread-safe way.
You can call this to drop caches as well.
If libvips was already initialized, the function is no-op

  

        
	  
  
  
    
#### 
      func VipsCacheDropAll ¶
  
    
      added in
      v1.0.10
    
  

    
    
      

```
func VipsCacheDropAll()
```

    
  

VipsCacheDropAll drops the vips operation cache, freeing the allocated memory.

  

        
	  
  
  
    
#### 
      func VipsCacheSetMax ¶
  
    
      added in
      v1.0.10
    
  

    
    
      

```
func VipsCacheSetMax(maxCacheSize int)
```

    
  

VipsCacheSetMax sets the maximum number of operations to keep in the vips operation cache.

  

        
	  
  
  
    
#### 
      func VipsCacheSetMaxMem ¶
  
    
      added in
      v1.0.10
    
  

    
    
      

```
func VipsCacheSetMaxMem(maxCacheMem int)
```

    
  

VipsCacheSetMaxMem Sets the maximum amount of tracked memory allowed before the vips operation cache
begins to drop entries.

  

        
	  
  
  
    
#### 
      func VipsDebugInfo ¶
  
    
  

    
    
      

```
func VipsDebugInfo()
```

    
  

VipsDebugInfo outputs to stdout libvips collected data. Useful for debugging.

  

        
	  
  
  
    
#### 
      func VipsIsTypeSupported ¶
  
    
      added in
      v1.0.3
    
  

    
    
      

```
func VipsIsTypeSupported(t ImageType) bool
```

    
  

VipsIsTypeSupported returns true if the given image type
is supported by the current libvips compilation.

  

        
	  
  
  
    
#### 
      func VipsIsTypeSupportedSave ¶
  
    
      added in
      v1.0.7
    
  

    
    
      

```
func VipsIsTypeSupportedSave(t ImageType) bool
```

    
  

VipsIsTypeSupportedSave returns true if the given image type
is supported by the current libvips compilation for the
save operation.

  

        
	  
  
  
    
#### 
      func VipsVectorSetEnabled ¶
  
    
      added in
      v1.1.6
    
  

    
    
      

```
func VipsVectorSetEnabled(enable bool)
```

    
  

VipsVectorSetEnabled enables or disables SIMD vector instructions. This can give speed-up,
but can also be unstable on some systems and versions.

  

        
	  
  
  
    
#### 
      func Write ¶
  
    
  

    
    
      

```
func Write(path string, buf []byte) error
```

    
  

Write writes the given byte buffer into disk
to the given file path.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Angle ¶
  
    
  

    
    
      

```
type Angle int
```

    
  

Angle represents the image rotation angle value.

    
      

```
const (
	// D0 represents the rotation angle 0 degrees.
	D0 Angle = 0
	// D45 represents the rotation angle 45 degrees.
	D45 Angle = 45
	// D90 represents the rotation angle 90 degrees.
	D90 Angle = 90
	// D135 represents the rotation angle 135 degrees.
	D135 Angle = 135
	// D180 represents the rotation angle 180 degrees.
	D180 Angle = 180
	// D235 represents the rotation angle 235 degrees.
	D235 Angle = 235
	// D270 represents the rotation angle 270 degrees.
	D270 Angle = 270
	// D315 represents the rotation angle 315 degrees.
	D315 Angle = 315
)
```