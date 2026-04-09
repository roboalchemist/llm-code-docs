# Module: Fabrication
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication.rb,

  lib/fabrication/config.rb,
 lib/fabrication/railtie.rb,
 lib/fabrication/support.rb,
 lib/fabrication/version.rb,
 lib/fabrication/sequencer.rb,
 lib/fabrication/transform.rb,
 lib/fabrication/syntax/make.rb,
 lib/fabrication/generator/base.rb,
 lib/fabrication/generator/sequel.rb,
 lib/fabrication/schematic/runner.rb,
 lib/fabrication/generator/mongoid.rb,
 lib/fabrication/schematic/manager.rb,
 lib/fabrication/schematic/attribute.rb,
 lib/fabrication/schematic/evaluator.rb,
 lib/fabrication/schematic/definition.rb,
 lib/fabrication/generator/active_record.rb,
 lib/fabrication/cucumber/step_fabricator.rb,
 lib/fabrication/errors/unfabricatable_error.rb,
 lib/fabrication/errors/infinite_recursion_error.rb,
 lib/fabrication/errors/unknown_fabricator_error.rb,
 lib/fabrication/errors/misplaced_fabricate_error.rb,
 lib/fabrication/errors/duplicate_fabricator_error.rb,
 lib/rails/generators/fabrication/model/model_generator.rb,
 lib/rails/generators/fabrication/cucumber_steps/cucumber_steps_generator.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** Config, Cucumber, Generator, Generators, Schematic, Support, Syntax
    
  
    
      **Classes:** DuplicateFabricatorError, InfiniteRecursionError, MisplacedFabricateError, Railtie, Sequencer, Transform, UnfabricatableError, UnknownFabricatorError
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
'3.0.0'.freeze
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**clear_definitions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**configure**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**manager**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**schematics**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**clear_definitions**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
42
```

    
    
      

```
# File 'lib/fabrication.rb', line 39

def self.clear_definitions
  manager.clear
  Sequencer.clear
end
```

    
  

    
      
  
### 
  
    .**configure**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/fabrication.rb', line 44

def self.configure(&)
  Fabrication::Config.configure(&)
end
```

    
  

    
      
  
### 
  
    .**manager**  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/fabrication.rb', line 48

def self.manager
  Fabrication::Schematic::Manager.instance
end
```

    
  

    
      
  
### 
  
    .**schematics**  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
```

    
    
      

```
# File 'lib/fabrication.rb', line 52

def self.schematics
  Support.log_deprecation('Fabrication.schematics has been replaced by ' \
                          'Fabrication.manager and will be removed in 3.0.0.')
  manager
end
```