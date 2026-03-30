# Class: FactoryBotRails::FactoryValidator
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- FactoryBotRails::FactoryValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/factory_bot_rails/factory_validator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_validator**(validator)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(validators = [])  ⇒ FactoryValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of FactoryValidator.

  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(validators = [])  ⇒ FactoryValidator 
  

  

  

  
    

Returns a new instance of FactoryValidator.

  

  

  
    
      

```

3
4
5
```

    
    
      

```
# File 'lib/factory_bot_rails/factory_validator.rb', line 3

def initialize(validators = [])
  @validators = Array(validators)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_validator**(validator)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/factory_bot_rails/factory_validator.rb', line 7

def add_validator(validator)
  @validators << validator
end
```

    
  

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/factory_bot_rails/factory_validator.rb', line 11

def run
  ActiveSupport::Notifications.subscribe("factory_bot.compile_factory", &validate_compiled_factory)
end
```