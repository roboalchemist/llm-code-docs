# Class: FactoryBot::Generators::ModelGenerator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Rails::Generators::NamedBase
          
            
- Base
          
            
- FactoryBot::Generators::ModelGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/factory_bot/model/model_generator.rb
  
  

  
## Direct Known Subclasses

  

AuthenticationGenerator

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_fixture_file**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#explicit_class_option, #factory_name, source_root

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_fixture_file**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
33
34
```

    
    
      

```
# File 'lib/generators/factory_bot/model/model_generator.rb', line 28

def create_fixture_file
  if File.exist?(factories_file)
    insert_factory_into_existing_file
  else
    create_factory_file
  end
end
```