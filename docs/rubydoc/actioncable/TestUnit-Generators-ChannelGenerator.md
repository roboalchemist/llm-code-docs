# Class: TestUnit::Generators::ChannelGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::NamedBase
      
        

          
- Object
          
            
- Rails::Generators::NamedBase
          
            
- TestUnit::Generators::ChannelGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rails/generators/test_unit/channel_generator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_test_files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_test_files**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/rails/generators/test_unit/channel_generator.rb', line 12

def create_test_files
  template "channel_test.rb", File.join("test/channels", class_path, "#{file_name}_channel_test.rb")
end
```