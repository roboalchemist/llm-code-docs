# Class: Prawn::Images::PNG
  
  
  

  
  
    Inherits:
    
      Image
      
        

          
- Object
          
            
- Image
          
            
- Prawn::Images::PNG
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/images/png.rb
  
  

## Overview

  
    

A convenience class that wraps the logic for extracting the parts of a PNG image that we need to embed them in a PDF.

  

  

  
## Extension API collapse

  

    
      
- 
  
    
      #**alpha_channel**  ⇒ String? 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Extracted alpha-channel.

  

    
      
- 
  
    
      #**bits**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Bits per sample or per palette index.

  

    
      
- 
  
    
      #**color_type**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Color type.

  

    
      
- 
  
    
      #**compression_method**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Compression method.

  

    
      
- 
  
    
      #**filter_method**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Filter method.

  

    
      
- 
  
    
      #**height**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Image height in pixels.

  

    
      
- 
  
    
      #**img_data**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Image data.

  

    
      
- 
  
    
      #**interlace_method**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Interlace method.

  

    
      
- 
  
    
      #**palette**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Palette data.

  

    
      
- 
  
    
      #**scaled_height**  ⇒ Number 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Scaled height of the image in PDF points.

  

    
      
- 
  
    
      #**scaled_width**  ⇒ Number 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Scaled width of the image in PDF points.

  

    
      
- 
  
    
      #**transparency**  ⇒ Hash{Symbol => String} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Transparency data.

  

    
      
- 
  
    
      #**width**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Image width in pixels.

  

    
  

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      .**can_render?**(image_blob)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Can this image handler process this image?.

  

      
        
- 
  
    
      #**alpha_channel?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is there an alpha-channel in this image?.

  

      
        
- 
  
    
      #**build_pdf_object**(document)  ⇒ PDF::Core::Reference 
    

    
  
  
  
  
  
  
  
  

  
    

Build a PDF object representing this image in `document`, and return a Reference to it.

  

      
        
- 
  
    
      #**colors**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Number of color components to each pixel.

  

      
        
- 
  
    
      #**initialize**(data)  ⇒ PNG 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Process a new PNG image.

  

      
        
- 
  
    
      #**min_pdf_version**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the minimum PDF version required to support this image.

  

      
        
- 
  
    
      #**split_alpha_channel!**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Split the alpha channel data from the raw image data in images where it’s required.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Image

  

#calc_image_dimensions

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(data)  ⇒ PNG 
  

  

  

  
    

Process a new PNG image

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

A binary string of PNG data.

      
    
  

  
    
      

```

75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 75

def initialize(data)
  super()
  data = StringIO.new(data.dup)

  data.read(8) # Skip the default header

  @palette = +''
  @img_data = +''
  @transparency = {}

  loop do
    chunk_size = data.read(4).unpack1('N')
    section = data.read(4)
    case section
    when 'IHDR'
      # we can grab other interesting values from here (like width,
      # height, etc)
      values = data.read(chunk_size).unpack('NNCCCCC')

      @width = values[0]
      @height = values[1]
      @bits = values[2]
      @color_type = values[3]
      @compression_method = values[4]
      @filter_method = values[5]
      @interlace_method = values[6]
    when 'PLTE'
      @palette << data.read(chunk_size)
    when 'IDAT'
      @img_data << data.read(chunk_size)
    when 'tRNS'
      # This chunk can only occur once and it must occur after the
      # PLTE chunk and before the IDAT chunk
      @transparency = {}
      case @color_type
      when 3
        @transparency[:palette] = data.read(chunk_size).unpack('C*')
      when 0
        # Greyscale. Corresponding to entries in the PLTE chunk.
        # Grey is two bytes, range 0 .. (2 ^ bit-depth) - 1
        grayval = data.read(chunk_size).unpack1('n')
        @transparency[:grayscale] = grayval
      when 2
        # True colour with proper alpha channel.
        @transparency[:rgb] = data.read(chunk_size).unpack('nnn')
      end
    when 'IEND'
      # we've got everything we need, exit the loop
      break
    else
      # unknown (or un-important) section, skip over it
      data.seek(data.pos + chunk_size)
    end

    data.read(4) # Skip the CRC
  end

  @img_data = Zlib::Inflate.inflate(@img_data)
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**alpha_channel**  ⇒ String?  (readonly)
  

  

  

  
    

Extracted alpha-channel.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 54

def alpha_channel
  @alpha_channel
end

```

    
  

    
      
      
      
  
### 
  
    #**bits**  ⇒ Integer  (readonly)
  

  

  

  
    

Bits per sample or per palette index.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 34

def bits
  @bits
end

```

    
  

    
      
      
      
  
### 
  
    #**color_type**  ⇒ Integer  (readonly)
  

  

  

  
    

Color type.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 38

def color_type
  @color_type
end

```

    
  

    
      
      
      
  
### 
  
    #**compression_method**  ⇒ Integer  (readonly)
  

  

  

  
    

Compression method.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 42

def compression_method
  @compression_method
end

```

    
  

    
      
      
      
  
### 
  
    #**filter_method**  ⇒ Integer  (readonly)
  

  

  

  
    

Filter method.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 46

def filter_method
  @filter_method
end

```

    
  

    
      
      
      
  
### 
  
    #**height**  ⇒ Integer  (readonly)
  

  

  

  
    

Image height in pixels.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 30

def height
  @height
end

```

    
  

    
      
      
      
  
### 
  
    #**img_data**  ⇒ String  (readonly)
  

  

  

  
    

Image data.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 18

def img_data
  @img_data
end

```

    
  

    
      
      
      
  
### 
  
    #**interlace_method**  ⇒ Integer  (readonly)
  

  

  

  
    

Interlace method.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 50

def interlace_method
  @interlace_method
end

```

    
  

    
      
      
      
  
### 
  
    #**palette**  ⇒ String  (readonly)
  

  

  

  
    

Palette data.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 14

def palette
  @palette
end

```

    
  

    
      
      
      
  
### 
  
    #**scaled_height**  ⇒ Number 
  

  

  

  
    

Scaled height of the image in PDF points.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 62

def scaled_height
  @scaled_height
end

```

    
  

    
      
      
      
  
### 
  
    #**scaled_width**  ⇒ Number 
  

  

  

  
    

Scaled width of the image in PDF points.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 58

def scaled_width
  @scaled_width
end

```

    
  

    
      
      
      
  
### 
  
    #**transparency**  ⇒ Hash{Symbol => String}  (readonly)
  

  

  

  
    

Transparency data.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 22

def transparency
  @transparency
end

```

    
  

    
      
      
      
  
### 
  
    #**width**  ⇒ Integer  (readonly)
  

  

  

  
    

Image width in pixels.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 26

def width
  @width
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**can_render?**(image_blob)  ⇒ Boolean 
  

  

  

  
    

Can this image handler process this image?

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 68

def self.can_render?(image_blob)
  image_blob[0, 8].unpack('C*') == [137, 80, 78, 71, 13, 10, 26, 10]
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**alpha_channel?**  ⇒ Boolean 
  

  

  

  
    

Is there an alpha-channel in this image?

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

165
166
167
168
169
170
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 165

def alpha_channel?
  return true if color_type == 4 || color_type == 6
  return @transparency.any? if color_type == 3

  false
end

```

    
  

    
      
  
### 
  
    #**build_pdf_object**(document)  ⇒ PDF::Core::Reference 
  

  

  

  
    

Build a PDF object representing this image in `document`, and return a Reference to it.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 177

def build_pdf_object(document)
  if compression_method != 0
    raise Errors::UnsupportedImageType,
      'PNG uses an unsupported compression method'
  end

  if filter_method != 0
    raise Errors::UnsupportedImageType,
      'PNG uses an unsupported filter method'
  end

  if interlace_method != 0
    raise Errors::UnsupportedImageType,
      'PNG uses unsupported interlace method'
  end

  # some PNG types store the colour and alpha channel data together,
  # which the PDF spec doesn't like, so split it out.
  split_alpha_channel!

  case colors
  when 1
    color = :DeviceGray
  when 3
    color = :DeviceRGB
  else
    raise Errors::UnsupportedImageType,
      "PNG uses an unsupported number of colors (#{png.colors})"
  end

  # build the image dict
  obj = document.ref!(
    Type: :XObject,
    Subtype: :Image,
    Height: height,
    Width: width,
    BitsPerComponent: bits,
  )

  # append the actual image data to the object as a stream
  obj << img_data

  obj.stream.filters << {
    FlateDecode: {
      Predictor: 15,
      Colors: colors,
      BitsPerComponent: bits,
      Columns: width,
    },
  }

  # sort out the colours of the image
  if palette.empty?
    obj.data[:ColorSpace] = color
  else
    # embed the colour palette in the PDF as a object stream
    palette_obj = document.ref!({})
    palette_obj << palette

    # build the color space array for the image
    obj.data[:ColorSpace] = [
      :Indexed,
      :DeviceRGB,
      (palette.size / 3) - 1,
      palette_obj,
    ]
  end

  # *************************************
  # add transparency data if necessary
  # *************************************

  # For PNG color types 0, 2 and 3, the transparency data is stored in
  # a dedicated PNG chunk, and is exposed via the transparency attribute
  # of the PNG class.
  if transparency[:grayscale]
    # Use Color Key Masking (spec section 4.8.5)
    # - An array with N elements, where N is two times the number of color
    #   components.
    val = transparency[:grayscale]
    obj.data[:Mask] = [val, val]
  elsif transparency[:rgb]
    # Use Color Key Masking (spec section 4.8.5)
    # - An array with N elements, where N is two times the number of color
    #   components.
    rgb = transparency[:rgb]
    obj.data[:Mask] = rgb.map { |x| [x, x] }.flatten
  end

  # For PNG color types 4 and 6, the transparency data is stored as
  # a alpha channel mixed in with the main image data. The PNG class
  # separates it out for us and makes it available via the alpha_channel
  # attribute
  if alpha_channel?
    smask_obj = document.ref!(
      Type: :XObject,
      Subtype: :Image,
      Height: height,
      Width: width,
      BitsPerComponent: bits,
      ColorSpace: :DeviceGray,
      Decode: [0, 1],
    )
    smask_obj.stream << alpha_channel

    smask_obj.stream.filters << {
      FlateDecode: {
        Predictor: 15,
        Colors: 1,
        BitsPerComponent: bits,
        Columns: width,
      },
    }
    obj.data[:SMask] = smask_obj
  end

  obj
end

```

    
  

    
      
  
### 
  
    #**colors**  ⇒ Integer 
  

  

  

  
    

Number of color components to each pixel.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

138
139
140
141
142
143
144
145
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 138

def colors
  case color_type
  when 0, 3, 4
    1
  when 2, 6
    3
  end
end

```

    
  

    
      
  
### 
  
    #**min_pdf_version**  ⇒ Float 
  

  

  

  
    

Returns the minimum PDF version required to support this image.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

299
300
301
302
303
304
305
306
307
308
309
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 299

def min_pdf_version
  if bits > 8
    # 16-bit color only supported in 1.5+ (ISO 32000-1:2008 8.9.5.1)
    1.5
  elsif alpha_channel?
    # Need transparency for SMask
    1.4
  else
    1.0
  end
end

```

    
  

    
      
  
### 
  
    #**split_alpha_channel!**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Split the alpha channel data from the raw image data in images where it’s required.

  

  

  
    
      

```

152
153
154
155
156
157
158
159
160
```

    
    
      

```
# File 'lib/prawn/images/png.rb', line 152

def split_alpha_channel!
  if alpha_channel?
    if color_type == 3
      generate_alpha_channel
    else
      split_image_data
    end
  end
end

```