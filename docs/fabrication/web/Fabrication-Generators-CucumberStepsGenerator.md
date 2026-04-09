# Class: Fabrication::Generators::CucumberStepsGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::Base
      
        

          
- Object
          
            
- Rails::Generators::Base
          
            
- Fabrication::Generators::CucumberStepsGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rails/generators/fabrication/cucumber_steps/cucumber_steps_generator.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**source_root**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**source_root**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/rails/generators/fabrication/cucumber_steps/cucumber_steps_generator.rb', line 10

def self.source_root
  File.expand_path(File.join(File.dirname(__FILE__), 'templates'))
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/rails/generators/fabrication/cucumber_steps/cucumber_steps_generator.rb', line 6

def generate
  template 'fabrication_steps.rb', 'features/step_definitions/fabrication_steps.rb'
end
```