# Class: Formtastic::InputGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::NamedBase
      
        

          
- Object
          
            
- Rails::Generators::NamedBase
          
            
- Formtastic::InputGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/formtastic/input/input_generator.rb
  
  

## Overview

  
    

!!!shell
  $ rails generate formtastic:input FlexibleText --extend string

  

  
  
    
#### Examples:

    
      
        
##### 

Extend an existing input behavior

      
      

```

```

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
```

    
    
      

```
# File 'lib/generators/formtastic/input/input_generator.rb', line 28

def create
  normalize_file_name
  define_extension_sentence
  template "input.rb", "app/inputs/#{name.underscore}_input.rb"
end

```