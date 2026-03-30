# Class: Formtastic::StylesheetsGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::Base
      
        

          
- Object
          
            
- Rails::Generators::Base
          
            
- Formtastic::StylesheetsGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/formtastic/stylesheets/stylesheets_generator.rb
  
  

## Overview

  
    

Copies a stylesheet into to app/assets/stylesheets/formtastic.css

!!!shell
  $ rails generate formtastic:stylesheets

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**copy_files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**copy_files**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/generators/formtastic/stylesheets/stylesheets_generator.rb', line 11

def copy_files
  copy_file "formtastic.css", "app/assets/stylesheets/formtastic.css"
end
```