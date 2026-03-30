# Top Level Namespace
  
  
  

  

  
  
  
  
  

  

  

## Defined Under Namespace

  
    
      **Modules:** Fabrication, FabricationMethods
    
  
    
      **Classes:** Fabricate
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**Fabricate**(name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**Fabricator**(name, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

rubocop:disable Naming/MethodName.

  

      
        
- 
  
    
      #**with_ivars**(fabricator)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**Fabricate**(name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/fabrication.rb', line 64

def Fabricate(name, overrides = {}, &)
  Fabricate.create(name, overrides, &)
end
```

    
  

    
      
  
### 
  
    #**Fabricator**(name, options = {})  ⇒ Object 
  

  

  

  
    

rubocop:disable Naming/MethodName

  

  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/fabrication.rb', line 60

def Fabricator(name, options = {}, &)
  Fabrication.manager.register(name, options, &)
end
```

    
  

    
      
  
### 
  
    #**with_ivars**(fabricator)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
12
13
```

    
    
      

```
# File 'lib/rails/generators/fabrication/cucumber_steps/templates/fabrication_steps.rb', line 7

def with_ivars(fabricator)
  @they = yield fabricator
  model = @they.last.class.to_s.underscore
  instance_variable_set(:"@#{model.pluralize}", @they)
  instance_variable_set(:"@#{model.singularize}", @they.last)
  Fabrication::Cucumber::Fabrications[model.singularize.gsub(/\W+/, '_').downcase] = @they.last
end
```