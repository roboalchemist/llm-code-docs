# Class: FactoryBotRails::Generators::NonRSpecGenerator
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- FactoryBotRails::Generators::NonRSpecGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/factory_bot_rails/generators/non_rspec_generator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(generators)  ⇒ NonRSpecGenerator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of NonRSpecGenerator.

  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(generators)  ⇒ NonRSpecGenerator 
  

  

  

  
    

Returns a new instance of NonRSpecGenerator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/factory_bot_rails/generators/non_rspec_generator.rb', line 4

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
14
```

    
    
      

```
# File 'lib/factory_bot_rails/generators/non_rspec_generator.rb', line 8

def run
  @generators.test_framework(
    test_framework,
    fixture: false,
    fixture_replacement: :factory_bot
  )
end
```