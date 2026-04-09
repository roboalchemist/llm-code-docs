# Class: Fabrication::Generator::Sequel
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Fabrication::Generator::Sequel
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/generator/sequel.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**supports?**(klass)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(klass)  ⇒ Sequel 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Sequel.

  

      
        
- 
  
    
      #**persist**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**set_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#_klass, #build, #build_instance, #build_instance_with_constructor_override, #build_instance_with_init_callback, #create, #execute_callbacks, #execute_deprecated_callbacks, #method_missing, #respond_to_missing?, #to_hash, #to_params

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(klass)  ⇒ Sequel 
  

  

  

  
    

Returns a new instance of Sequel.

  

  

  
    
      

```

4
5
6
7
```

    
    
      

```
# File 'lib/fabrication/generator/sequel.rb', line 4

def initialize(klass)
  super
  load_instance_hooks
end
```

    
  

  

  
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

9
10
11
```

    
    
      

```
# File 'lib/fabrication/generator/sequel.rb', line 9

def self.supports?(klass)
  defined?(::Sequel::Model) && klass.ancestors.include?(::Sequel::Model)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**persist**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/fabrication/generator/sequel.rb', line 23

def persist
  _instance.save(raise_on_failure: true)
end
```

    
  

    
      
  
### 
  
    #**set_attributes**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/fabrication/generator/sequel.rb', line 13

def set_attributes
  _attributes.each do |field_name, value|
    if value.is_a?(Array) && (association = association_for(field_name))
      set_association(association, field_name, value)
    else
      set_attribute(field_name, value)
    end
  end
end
```