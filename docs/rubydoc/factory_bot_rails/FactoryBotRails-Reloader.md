# Class: FactoryBotRails::Reloader
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- FactoryBotRails::Reloader
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/factory_bot_rails/reloader.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(app)  ⇒ Reloader 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Reloader.

  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(app)  ⇒ Reloader 
  

  

  

  
    

Returns a new instance of Reloader.

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/factory_bot_rails/reloader.rb', line 7

def initialize(app)
  @app = app
  @paths = DefinitionFilePaths.new(FactoryBot.definition_file_paths)
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
```

    
    
      

```
# File 'lib/factory_bot_rails/reloader.rb', line 12

def run
  return unless @paths.any?

  register_reloader(build_reloader)
end

```