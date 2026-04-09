# Class: FactoryBotRails::Generators::RSpecGenerator
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- FactoryBotRails::Generators::RSpecGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/factory_bot_rails/generators/rspec_generator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(generators)  ⇒ RSpecGenerator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RSpecGenerator.

  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(generators)  ⇒ RSpecGenerator 
  

  

  

  
    

Returns a new instance of RSpecGenerator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/factory_bot_rails/generators/rspec_generator.rb', line 4

def initialize(generators)
  @generators = generators
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
13
```

    
    
      

```
# File 'lib/factory_bot_rails/generators/rspec_generator.rb', line 8

def run
  @generators.fixture_replacement(
    fixture_replacement_setting,
    dir: factory_bot_directory
  )
end
```