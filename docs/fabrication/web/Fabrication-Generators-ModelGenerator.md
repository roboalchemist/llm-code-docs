# Class: Fabrication::Generators::ModelGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::NamedBase
      
        

          
- Object
          
            
- Rails::Generators::NamedBase
          
            
- Fabrication::Generators::ModelGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rails/generators/fabrication/model/model_generator.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**source_root**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_fabrication_file**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**source_root**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/rails/generators/fabrication/model/model_generator.rb', line 21

def self.source_root
  File.expand_path(File.join(File.dirname(__FILE__), 'templates'))
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_fabrication_file**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
15
16
17
18
19
```

    
    
      

```
# File 'lib/rails/generators/fabrication/model/model_generator.rb', line 11

def create_fabrication_file
  copy_attributes_from_model if attributes.empty?
  template_file = File.join(
    options[:dir],
    class_path,
    "#{file_name}_fabricator.#{options[:extension]}"
  )
  template 'fabricator.erb', template_file
end
```