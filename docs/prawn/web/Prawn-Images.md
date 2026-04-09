# Module: Prawn::Images
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Document
  
  

  
  
    Defined in:
    lib/prawn/images.rb,

  lib/prawn/images/jpg.rb,
 lib/prawn/images/png.rb,
 lib/prawn/images/image.rb

  
  

## Overview

  
    

rubocop: disable Style/Documentation

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Image, JPG, PNG
    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**build_image_object**(file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Builds an info object (Prawn::Images::*) and a PDF reference representing the given image.

  

      
        
- 
  
    
      #**embed_image**(pdf_obj, info, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a PDF image resource `pdf_obj` that has been added to the page’s resources and an `info` object (the pair returned from #build_image_object), embed the image according to the `options` given.

  

      
        
- 
  
    
      #**image**(file, options = {})  ⇒ Prawn::Images::Image 
    

    
  
  
  
  
  
  
  
  

  
    

Add the image at `file` to the current page.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**build_image_object**(file)  ⇒ Object 
  

  

  

  
    

Builds an info object (Prawn::Images::*) and a PDF reference representing the given image. Return a pair: [pdf_obj, info].

  

  

  
    
      

```

72
73
74
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
```

    
    
      

```
# File 'lib/prawn/images.rb', line 72

def build_image_object(file)
  image_content = verify_and_read_image(file)
  image_sha1 = Digest::SHA1.hexdigest(image_content)

  # if this image has already been embedded, just reuse it
  if image_registry[image_sha1]
    info = image_registry[image_sha1][:info]
    image_obj = image_registry[image_sha1][:obj]
  else
    # Build the image object
    info = Prawn.image_handler.find(image_content).new(image_content)

    # Bump PDF version if the image requires it
    if info.respond_to?(:min_pdf_version)
      renderer.min_version(info.min_pdf_version)
    end

    # Add the image to the PDF and register it in case we see it again.
    image_obj = info.build_pdf_object(self)
    image_registry[image_sha1] = { obj: image_obj, info: info }
  end

  [image_obj, info]
end
```

    
  

    
      
  
### 
  
    #**embed_image**(pdf_obj, info, options)  ⇒ Object 
  

  

  

  
    

Given a PDF image resource `pdf_obj` that has been added to the page’s resources and an `info` object (the pair returned from #build_image_object), embed the image according to the `options` given.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/images.rb', line 102

def embed_image(pdf_obj, info, options)
  # find where the image will be placed and how big it will be
  w, h = info.calc_image_dimensions(options)

  if options[:at]
    x, y = map_to_absolute(options[:at])
  else
    x, y = image_position(w, h, options)
    move_text_position(h)
  end

  # add a reference to the image object to the current page
  # resource list and give it a label
  label = "I#{next_image_id}"
  state.page.xobjects[label] = pdf_obj

  cm_params = PDF::Core.real_params([w, 0, 0, h, x, y - h])
  renderer.add_content("\nq\n#{cm_params} cm\n/#{label} Do\nQ")
end
```

    
  

    
      
  
### 
  
    #**image**(file, options = {})  ⇒ Prawn::Images::Image 
  

  

  

  
    

Add the image at `file` to the current page. Currently only JPG and PNG files are supported. (Note that processing PNG images with alpha channels can be processor and memory intensive.)

If only one of `:width` or `:height` are provided, the image will be scaled proportionally. When both are provided, the image will be stretched to fit the dimensions without maintaining the aspect ratio.

  

  
  
    
#### Examples:

    
      
      

```
Prawn::Document.generate("image2.pdf", page_layout: :landscape) do
  pigs = "#{Prawn::DATADIR}/images/pigs.jpg"
  image pigs, at: [50,450], width: 450

  dice = "#{Prawn::DATADIR}/images/dice.png"
  image dice, at: [50, 450], scale: 0.75
end
```

    
  

Parameters:

  
    
- 
      
        file
      
      
        (String, IO)
      
      
      
        —
        

Path to file or an object that responds to `#read` and `#rewind`.

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :at
          (Array(Number, Number))
          
            
          
          
            — 

The location of the top left corner of the image. If provided, the image will be place in the current page but the text position will not be changed.

          
        
      
        
- 
          :position
          (:left, :center, :right, Number)
          
            
          
          
            — 

Horizontal position relative to the current bounding box.

          
        
      
        
- 
          :vposition
          (:topm :center, :bottom, Number)
          
            
          
          
            — 

Vertical position relative to the current bounding box.

          
        
      
        
- 
          :height
          (Number)
          
            
              — default:
              actual height of the image
            
          
          
            — 

The height of the image.

          
        
      
        
- 
          :width
          (Number)
          
            
              — default:
              actual width of the image
            
          
          
            — 

The width of the image.

          
        
      
        
- 
          :scale
          (Number)
          
            
          
          
            — 

Scale the dimensions of the image proportionally.

          
        
      
        
- 
          :fit
          (Array(Number, Number))
          
            
          
          
            — 

Scale the dimensions of the image proportionally to fit inside the rectangle of specified size (width, height).

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Prawn::Images::Image)
      
      
      
        —
        

An image handler. All image handlers provided by Prawn are subclasses of Image. This object can be used to check the image dimensions and get other format-specific information.

      
    
  

  

See Also:
  

    
      
- PNG
    
      
- JPG
    
  

  
    
      

```

56
57
58
59
60
61
62
63
64
65
66
```

    
    
      

```
# File 'lib/prawn/images.rb', line 56

def image(file, options = {})
  Prawn.verify_options(
    %i[at position vposition height width scale fit],
    options,
  )

  pdf_obj, info = build_image_object(file)
  embed_image(pdf_obj, info, options)

  info
end
```