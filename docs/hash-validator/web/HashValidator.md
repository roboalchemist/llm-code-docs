# Module: HashValidator
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator.rb,

  lib/hash_validator/version.rb,
 lib/hash_validator/validators.rb,
 lib/hash_validator/validations.rb,
 lib/hash_validator/configuration.rb,
 lib/hash_validator/validators/many_validator.rb,
 lib/hash_validator/validators/multiple_validator.rb,
 lib/hash_validator/validators/optional_validator.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** Validations, Validator
    
  
    
      **Classes:** Base, Configuration
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
"2.0.1"
```

      
        @@validators =
          
        
        

```
[]
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**add_validator**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**configure** {|config| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**many**(validation)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**multiple**(*validations)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**optional**(validation)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**remove_validator**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**validate**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**validator_for**(rhs)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**add_validator**(*args)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
18
19
20
21
22
23
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
39
40
41
42
43
44
45
46
47
48
```

    
    
      

```
# File 'lib/hash_validator/validators.rb', line 12

def self.add_validator(*args)
  validator = case args.length
  when 1
    # Instance-based validator (existing behavior)
    validator_instance = args[0]
    unless validator_instance.is_a?(HashValidator::Validator::Base)
      raise StandardError.new("validators need to inherit from HashValidator::Validator::Base")
    end
    validator_instance
  when 2
    # Dynamic validator with options
    name = args[0]
    options = args[1]

    if options.is_a?(Hash)
      if options[:pattern]
        # Pattern-based validator
        HashValidator::Validator::DynamicPatternValidator.new(name, options[:pattern], options[:error_message])
      elsif options[:func]
        # Function-based validator
        HashValidator::Validator::DynamicFuncValidator.new(name, options[:func], options[:error_message])
      else
        raise ArgumentError, "Options hash must contain either :pattern or :func key"
      end
    else
      raise ArgumentError, "Second argument must be an options hash with :pattern or :func key"
    end
  else
    raise ArgumentError, "add_validator expects 1 argument (validator instance) or 2 arguments (name, options)"
  end

  if @@validators.detect { |v| v.name == validator.name }
    raise StandardError.new("validators need to have unique names")
  end

  @@validators << validator
end
```

    
  

    
      
  
### 
  
    .**configure** {|config| ... } ⇒ Object 
  

  

  

  
    

  

  

Yields:

  
    
- 
      
      
        (config)
      
      
      
    
  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/hash_validator/configuration.rb', line 14

def self.configure
  config = Configuration.new
  yield(config) if block_given?
end
```

    
  

    
      
  
### 
  
    .**many**(validation)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/hash_validator.rb', line 12

def self.many(validation)
  Validations::Many.new(validation)
end
```

    
  

    
      
  
### 
  
    .**multiple**(*validations)  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/hash_validator.rb', line 16

def self.multiple(*validations)
  Validations::Multiple.new(validations)
end
```

    
  

    
      
  
### 
  
    .**optional**(validation)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/hash_validator.rb', line 8

def self.optional(validation)
  Validations::Optional.new(validation)
end
```

    
  

    
      
  
### 
  
    .**remove_validator**(name)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/hash_validator/validators.rb', line 7

def self.remove_validator(name)
  name = name.to_s
  @@validators.reject! { |v| v.name == name }
end
```

    
  

    
      
  
### 
  
    .**validate**(*args)  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator.rb', line 4

def self.validate(*args)
  Base.validate(*args)
end
```

    
  

    
      
  
### 
  
    .**validator_for**(rhs)  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/hash_validator/validators.rb', line 50

def self.validator_for(rhs)
  @@validators.detect { |v| v.should_validate?(rhs) } || raise(StandardError.new("Could not find valid validator for: #{rhs}"))
end
```