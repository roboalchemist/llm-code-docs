# Class: FactoryBotRails::Generator
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- FactoryBotRails::Generator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/factory_bot_rails/generator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**factory_bot_disabled?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generator**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(config)  ⇒ Generator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Generator.

  

      
        
- 
  
    
      #**rails_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**test_framework**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(config)  ⇒ Generator 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/factory_bot_rails/generator.rb', line 7

def initialize(config)
  @generators = config.app_generators
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**factory_bot_disabled?**  ⇒ Boolean 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/factory_bot_rails/generator.rb', line 29

def factory_bot_disabled?
  rails_options[:factory_bot] == false
end
```

    
  

    
      
  
### 
  
    #**generator**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
20
21
22
23
```

    
    
      

```
# File 'lib/factory_bot_rails/generator.rb', line 15

def generator
  return Generators::NullGenerator if factory_bot_disabled?

  if test_framework == :rspec
    Generators::RSpecGenerator
  else
    Generators::NonRSpecGenerator
  end
end
```

    
  

    
      
  
### 
  
    #**rails_options**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/factory_bot_rails/generator.rb', line 33

def rails_options
  @generators.options[:rails]
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
# File 'lib/factory_bot_rails/generator.rb', line 11

def run
  generator.new(@generators).run
end
```

    
  

    
      
  
### 
  
    #**test_framework**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/factory_bot_rails/generator.rb', line 25

def test_framework
  rails_options[:test_framework]
end
```