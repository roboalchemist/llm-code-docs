# Class: Prawn::ImageHandler
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::ImageHandler
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/image_handler.rb
  
  

## Overview

  
    

ImageHandler provides a way to register image processors with Prawn.

  

  

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      #**find**(image_blob)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Find an image handler for an image.

  

      
        
- 
  
    
      #**initialize**  ⇒ ImageHandler 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ImageHandler.

  

      
        
- 
  
    
      #**register**(handler)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Register an image handler.

  

      
        
- 
  
    
      #**register!**(handler)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Register an image handler with the highest priority.

  

      
        
- 
  
    
      #**unregister**(handler)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Unregister an image handler.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ImageHandler 
  

  

  

  
    

Returns a new instance of ImageHandler.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/prawn/image_handler.rb', line 16

def initialize
  @handlers = []
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find**(image_blob)  ⇒ Object 
  

  

  

  
    

Find an image handler for an image.

  

  

Parameters:

  
    
- 
      
        image_blob
      
      
        (String)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (Prawn::Errors::UnsupportedImageType)
      
      
      
        —
        

If no image handler were found for the image.

      
    
  

  
    
      

```

52
53
54
55
56
57
58
59
```

    
    
      

```
# File 'lib/prawn/image_handler.rb', line 52

def find(image_blob)
  handler = @handlers.find { |h| h.can_render?(image_blob) }

  return handler if handler

  raise Prawn::Errors::UnsupportedImageType,
    'image file is an unrecognised format'
end

```

    
  

    
      
  
### 
  
    #**register**(handler)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Register an image handler.

  

  

Parameters:

  
    
- 
      
        handler
      
      
        (Object)
      
      
      
    
  

  
    
      

```

24
25
26
27
```

    
    
      

```
# File 'lib/prawn/image_handler.rb', line 24

def register(handler)
  @handlers.delete(handler)
  @handlers.push(handler)
end

```

    
  

    
      
  
### 
  
    #**register!**(handler)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Register an image handler with the highest priority.

  

  

Parameters:

  
    
- 
      
        handler
      
      
        (Object)
      
      
      
    
  

  
    
      

```

33
34
35
36
```

    
    
      

```
# File 'lib/prawn/image_handler.rb', line 33

def register!(handler)
  @handlers.delete(handler)
  @handlers.unshift(handler)
end

```

    
  

    
      
  
### 
  
    #**unregister**(handler)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Unregister an image handler.

  

  

Parameters:

  
    
- 
      
        handler
      
      
        (Object)
      
      
      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/prawn/image_handler.rb', line 42

def unregister(handler)
  @handlers.reject! { |h| h == handler }
end

```