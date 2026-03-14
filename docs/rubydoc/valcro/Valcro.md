# Module: Valcro
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/valcro.rb,

  lib/valcro/error.rb,
 lib/valcro/runner.rb,
 lib/valcro/version.rb,
 lib/valcro/error_list.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
      **Classes:** Error, ErrorList, Runner
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
"0.2.1"
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**included**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_messages**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**valid?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validation_runner**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**included**(base)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/valcro.rb', line 8

def self.included(base)
  base.extend ClassMethods
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_messages**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/valcro.rb', line 20

def error_messages
  errors.to_s
end
```

    
  

    
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/valcro.rb', line 12

def errors
  @error_list ||= Valcro::ErrorList.new
end
```

    
  

    
      
  
### 
  
    #**valid?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/valcro.rb', line 16

def valid?
  !errors.any?
end
```

    
  

    
      
  
### 
  
    #**validate**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
```

    
    
      

```
# File 'lib/valcro.rb', line 24

def validate
  validation_runner.clear!
  self.class.validators.each do |validator_class|
    validator = if validator_class.respond_to?(:build)
      validator_class.build(self)
    else
      validator_class.new(self)
    end
    validation_runner.add_validator validator
  end
  self.class.validation_blocks.each do |validation_block|
    instance_eval(&validation_block)
  end
  validation_runner.validate
end
```

    
  

    
      
  
### 
  
    #**validation_runner**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/valcro.rb', line 40

def validation_runner
  @validation_runner ||= Valcro::Runner.new(errors)
end
```