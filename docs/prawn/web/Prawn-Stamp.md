# Module: Prawn::Stamp
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Document
  
  

  
  
    Defined in:
    lib/prawn/stamp.rb
  
  

## Overview

  
    

This module is used to create content that will be included multiple times in a document. Using a stamp has three advantages over creating content anew each time it is placed on the page:

- 

Faster document creation.

- 

Smaller final document.

- 

Faster display on subsequent displays of the repeated element because the viewer application can cache the rendered results.

  

  
  
    
#### Examples:

    
      
      

```
pdf.create_stamp("my_stamp") {
  pdf.fill_circle([10, 15], 5)
  pdf.draw_text("hello world", at: [20, 10])
}
pdf.stamp("my_stamp")

```

    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**create_stamp**(name) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a re-usable stamp.

  

      
        
- 
  
    
      #**stamp**(name)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Renders the stamp.

  

      
        
- 
  
    
      #**stamp_at**(name, point)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Renders the stamp at a position offset from the initial coords at which the elements of the stamp was created.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_stamp**(name) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Creates a re-usable stamp.

  

  
  
    
#### Examples:

    
      
      

```
pdf.create_stamp("my_stamp") {
  pdf.fill_circle([10, 15], 5)
  pdf.draw_text("hello world", at: [20, 10])
}

```

    
  

Parameters:

  
    
- 
      
      
      
      
        
        

Stamp name.

      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
        
        

Stamp content.

      
    
  

Raises:

  
    
- 
      
      
      
      
        
        

if a stamp already exists in this document with this name.

      
    
  
    
- 
      
      
      
      
        
        

if name is empty.

      
    
  

  
    
      

```

74
75
76
77
78
```

    
    
      

```
# File 'lib/prawn/stamp.rb', line 74

def create_stamp(name, &block)
  dictionary = create_stamp_dictionary(name)

  state.page.stamp_stream(dictionary, &block)
end

```

    
  

    
      
  
### 
  
    #**stamp**(name)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Renders the stamp.

  

  
  
    
#### Examples:

    
      
      

```
pdf.create_stamp("my_stamp") {
  pdf.fill_circle([10, 15], 5)
  pdf.text("hello world", at: [20, 10])
}
pdf.stamp("my_stamp")

```

    
  

Parameters:

  
    
- 
      
      
      
      
    
  

Raises:

  
    
- 
      
      
      
      
        
        

if name is empty.

      
    
  
    
- 
      
      
      
      
        
        

if no stamp has been created with this name.

      
    
  

  
    
      

```

35
36
37
38
39
40
```

    
    
      

```
# File 'lib/prawn/stamp.rb', line 35

def stamp(name)
  dictionary_name, dictionary = stamp_dictionary(name)
  renderer.add_content("/#{dictionary_name} Do")
  update_annotation_references(dictionary.data[:Annots])
  state.page.xobjects.merge!(dictionary_name => dictionary)
end

```

    
  

    
      
  
### 
  
    #**stamp_at**(name, point)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Renders the stamp at a position offset from the initial coords at which the elements of the stamp was created.

  

  
  
    
#### Examples:

    
      
      

```
pdf.create_stamp("circle") do
  pdf.fill_circle([0, 0], 25)
end
# draws a circle at 100, 100
pdf.stamp_at("circle", [100, 100])

```

    
  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
    
  

  

See Also:
  

    
      
- for exceptions that might be raised.
    
  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/prawn/stamp.rb', line 56

def stamp_at(name, point)
  translate(point[0], point[1]) { stamp(name) }
end

```