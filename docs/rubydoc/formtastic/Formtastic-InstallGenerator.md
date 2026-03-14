# Class: Formtastic::InstallGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::Base
      
        

          
- Object
          
            
- Rails::Generators::Base
          
            
- Formtastic::InstallGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/formtastic/install/install_generator.rb
  
  

## Overview

  
    

Copies a config initializer to config/initializers/formtastic.rb

!!!shell
  $ rails generate formtastic:install

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**copy_files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**copy_scaffold_template**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**copy_files**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/generators/formtastic/install/install_generator.rb', line 14

def copy_files
  copy_file 'formtastic.rb', 'config/initializers/formtastic.rb'
end
```

    
  

    
      
  
### 
  
    #**copy_scaffold_template**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
21
```

    
    
      

```
# File 'lib/generators/formtastic/install/install_generator.rb', line 18

def copy_scaffold_template
  engine = options[:template_engine]
  copy_file "_form.html.#{engine}", "lib/templates/#{engine}/scaffold/_form.html.#{engine}"
end
```