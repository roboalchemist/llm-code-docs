# Class: Prawn::Images::Image
  Abstract
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Images::Image
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/images/image.rb
  
  

## Overview

  
    
  **This class is abstract.**
  

Base class for image info objects

  

  

  
## Direct Known Subclasses

  

JPG, PNG

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      #**calc_image_dimensions**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Calculate the final image dimensions from provided options.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**calc_image_dimensions**(options)  ⇒ Object 
  

  

  

  
    

Calculate the final image dimensions from provided options.

  

  

  
    
      

```

14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
```

    
    
      

```
# File 'lib/prawn/images/image.rb', line 14

def calc_image_dimensions(options)
  w = options[:width] || width
  h = options[:height] || height

  if options[:width] && !options[:height]
    wp = w / Float(width)
    w = width * wp
    h = height * wp
  elsif options[:height] && !options[:width]
    hp = h / Float(height)
    w = width * hp
    h = height * hp
  elsif options[:scale]
    w = width * options[:scale]
    h = height * options[:scale]
  elsif options[:fit]
    bw, bh = options[:fit]
    bp = bw / Float(bh)
    ip = width / Float(height)
    if ip > bp
      w = bw
      h = bw / ip
    else
      h = bh
      w = bh * ip
    end
  end
  self.scaled_width = w
  self.scaled_height = h

  [w, h]
end
```