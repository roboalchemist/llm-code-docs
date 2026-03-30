# Class: Fabrication::Generator::Mongoid
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Fabrication::Generator::Mongoid
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/generator/mongoid.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**supports?**(klass)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**build_instance**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#_klass, #build, #build_instance_with_constructor_override, #build_instance_with_init_callback, #create, #execute_callbacks, #execute_deprecated_callbacks, #initialize, #method_missing, #respond_to_missing?, #set_attributes, #to_hash, #to_params

  
## Constructor Details

  
    

This class inherits a constructor from Fabrication::Generator::Base
  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
      in the class Fabrication::Generator::Base
    
  
  

  
    
## Class Method Details

    
      
  
### 
  
    .**supports?**(klass)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/fabrication/generator/mongoid.rb', line 4

def self.supports?(klass)
  defined?(::Mongoid) && klass.ancestors.include?(::Mongoid::Document)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**build_instance**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
13
14
```

    
    
      

```
# File 'lib/fabrication/generator/mongoid.rb', line 8

def build_instance
  self._instance = if resolved_class.respond_to?(:protected_attributes)
                     resolved_class.new(_attributes, without_protection: true)
                   else
                     resolved_class.new(_attributes)
                   end
end
```