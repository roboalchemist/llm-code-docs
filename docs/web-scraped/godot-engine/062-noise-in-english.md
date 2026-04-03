# Noise in English

# Noise
Inherits:Resource<RefCounted<Object
Inherited By:FastNoiseLite
Abstract base class for noise generators.

## Description
This class defines the interface for noise generation libraries to inherit from.
A defaultget_seamless_image()implementation is provided for libraries that do not provide seamless noise. This function requests a larger image from theget_image()method, reverses the quadrants of the image, then uses the strips of extra width to blend over the seams.
Inheriting noise classes can optionally override this function to provide a more optimal algorithm.

## Methods

| Image | get_image(width:int, height:int, invert:bool= false, in_3d_space:bool= false, normalize:bool= true)const |
|---|---|
| Array[Image] | get_image_3d(width:int, height:int, depth:int, invert:bool= false, normalize:bool= true)const |
| float | get_noise_1d(x:float)const |
| float | get_noise_2d(x:float, y:float)const |
| float | get_noise_2dv(v:Vector2)const |
| float | get_noise_3d(x:float, y:float, z:float)const |
| float | get_noise_3dv(v:Vector3)const |
| Image | get_seamless_image(width:int, height:int, invert:bool= false, in_3d_space:bool= false, skirt:float= 0.1, normalize:bool= true)const |
| Array[Image] | get_seamless_image_3d(width:int, height:int, depth:int, invert:bool= false, skirt:float= 0.1, normalize:bool= true)const |

Image
get_image(width:int, height:int, invert:bool= false, in_3d_space:bool= false, normalize:bool= true)const
Array[Image]
get_image_3d(width:int, height:int, depth:int, invert:bool= false, normalize:bool= true)const
float
get_noise_1d(x:float)const
float
get_noise_2d(x:float, y:float)const
float
get_noise_2dv(v:Vector2)const
float
get_noise_3d(x:float, y:float, z:float)const
float
get_noise_3dv(v:Vector3)const
Image
get_seamless_image(width:int, height:int, invert:bool= false, in_3d_space:bool= false, skirt:float= 0.1, normalize:bool= true)const
Array[Image]
get_seamless_image_3d(width:int, height:int, depth:int, invert:bool= false, skirt:float= 0.1, normalize:bool= true)const

## Method Descriptions
Imageget_image(width:int, height:int, invert:bool= false, in_3d_space:bool= false, normalize:bool= true)const🔗
Returns anImagecontaining 2D noise values.
Note:Withnormalizeset tofalse, the default implementation expects the noise generator to return values in the range-1.0to1.0.
Array[Image]get_image_3d(width:int, height:int, depth:int, invert:bool= false, normalize:bool= true)const🔗
Returns anArrayofImages containing 3D noise values for use withImageTexture3D.create().
Note:Withnormalizeset tofalse, the default implementation expects the noise generator to return values in the range-1.0to1.0.
floatget_noise_1d(x:float)const🔗
Returns the 1D noise value at the given (x) coordinate.
floatget_noise_2d(x:float, y:float)const🔗
Returns the 2D noise value at the given position.
floatget_noise_2dv(v:Vector2)const🔗
Returns the 2D noise value at the given position.
floatget_noise_3d(x:float, y:float, z:float)const🔗
Returns the 3D noise value at the given position.
floatget_noise_3dv(v:Vector3)const🔗
Returns the 3D noise value at the given position.
Imageget_seamless_image(width:int, height:int, invert:bool= false, in_3d_space:bool= false, skirt:float= 0.1, normalize:bool= true)const🔗
Returns anImagecontaining seamless 2D noise values.
Note:Withnormalizeset tofalse, the default implementation expects the noise generator to return values in the range-1.0to1.0.
Array[Image]get_seamless_image_3d(width:int, height:int, depth:int, invert:bool= false, skirt:float= 0.1, normalize:bool= true)const🔗
Returns anArrayofImages containing seamless 3D noise values for use withImageTexture3D.create().
Note:Withnormalizeset tofalse, the default implementation expects the noise generator to return values in the range-1.0to1.0.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.