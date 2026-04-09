# Class: Prawn::Images::JPG
  
  
  

  
  
    Inherits:
    
      Image
      
        

          
- Object
          
            
- Image
          
            
- Prawn::Images::JPG
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/images/jpg.rb
  
  

## Overview

  
    

A convenience class that wraps the logic for extracting the parts of a JPG image that we need to embed them in a PDF.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** FormatError
    
  

  
    
## 
      Extension API
      collapse
    

    
      
        JPEG_SOF_BLOCKS =
          
        
        

```
[
  0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE,
  0xCF,
].freeze

```

      
    
  

  
## Extension API collapse

  

    
      
- 
  
    
      #**bits**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Sample Precision in bits.

  

    
      
- 
  
    
      #**channels**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Number of image components (channels).

  

    
      
- 
  
    
      #**height**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Image height in pixels.

  

    
      
- 
  
    
      #**scaled_height**  ⇒ Number 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Scaled height of the image in PDF points.

  

    
      
- 
  
    
      #**scaled_width**  ⇒ Number 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Scaled width of the image in PDF points.

  

    
      
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
  
    
      #**build_pdf_object**(document)  ⇒ PDF::Core::Reference 
    

    
  
  
  
  
  
  
  
  

  
    

Build a PDF object representing this image in `document`, and return a Reference to it.

  

      
        
- 
  
    
      #**initialize**(data)  ⇒ JPG 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Process a new JPG image.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Image

  

#calc_image_dimensions

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(data)  ⇒ JPG 
  

  

  

  
    

Process a new JPG image.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

A binary string of JPEG data.

      
    
  

  
    
      

```

58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 58

def initialize(data)
  super()
  @data = data
  d = StringIO.new(@data)
  d.binmode

  c_marker = 0xff # Section marker.
  d.seek(2) # Skip the first two bytes of JPEG identifier.
  loop do
    marker, code, length = d.read(4).unpack('CCn')
    raise FormatError, 'JPEG marker not found!' if marker != c_marker

    if JPEG_SOF_BLOCKS.include?(code)
      @bits, @height, @width, @channels = d.read(6).unpack('CnnC')
      break
    end

    d.seek(length - 2, IO::SEEK_CUR)
  end
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**bits**  ⇒ Integer  (readonly)
  

  

  

  
    

Sample Precision in bits.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 27

def bits
  @bits
end

```

    
  

    
      
      
      
  
### 
  
    #**channels**  ⇒ Integer  (readonly)
  

  

  

  
    

Number of image components (channels).

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 31

def channels
  @channels
end

```

    
  

    
      
      
      
  
### 
  
    #**height**  ⇒ Integer  (readonly)
  

  

  

  
    

Image height in pixels.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 23

def height
  @height
end

```

    
  

    
      
      
      
  
### 
  
    #**scaled_height**  ⇒ Number 
  

  

  

  
    

Scaled height of the image in PDF points.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 39

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

35
36
37
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 35

def scaled_width
  @scaled_width
end

```

    
  

    
      
      
      
  
### 
  
    #**width**  ⇒ Integer  (readonly)
  

  

  

  
    

Image width in pixels.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 19

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

51
52
53
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 51

def self.can_render?(image_blob)
  image_blob[0, 3].unpack('C*') == [255, 216, 255]
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**build_pdf_object**(document)  ⇒ PDF::Core::Reference 
  

  

  

  
    

Build a PDF object representing this image in `document`, and return a Reference to it.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/images/jpg.rb', line 84

def build_pdf_object(document)
  color_space =
    case channels
    when 1
      :DeviceGray
    when 3
      :DeviceRGB
    when 4
      :DeviceCMYK
    else
      raise ArgumentError, 'JPG uses an unsupported number of channels'
    end

  obj = document.ref!(
    Type: :XObject,
    Subtype: :Image,
    ColorSpace: color_space,
    BitsPerComponent: bits,
    Width: width,
    Height: height,
  )

  # add extra decode params for CMYK images. By swapping the
  # min and max values from the default, we invert the colours. See
  # section 4.8.4 of the spec.
  if color_space == :DeviceCMYK
    obj.data[:Decode] = [1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]
  end

  obj.stream << @data
  obj.stream.filters << :DCTDecode
  obj
end

```