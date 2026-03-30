# Class: Fabrication::Schematic::Evaluator
  
  
  

  
  
    Inherits:
    
      BasicObject
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/schematic/evaluator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**after_build**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**after_create**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**after_save**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**after_validation**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_create**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_save**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_validation**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**init_with**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize_with**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**method_missing**(method_name, *args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**on_init**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process**(definition)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**respond_to_missing?**(_method_name, _include_private = false)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**transient**(*field_names)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(method_name, *args, &block)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
18
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 13

def method_missing(method_name, *args, &block)
  params = ::Fabrication::Support.extract_options!(args)
  value = args.first
  block = @_definition.generate_value(method_name, params) if args.empty? && !block
  @_definition.append_or_update_attribute(method_name, value, params, &block)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**after_build**(&block)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 20

def after_build(&block)
  @_definition.callbacks[:after_build] ||= []
  @_definition.callbacks[:after_build] << block
end
```

    
  

    
      
  
### 
  
    #**after_create**(&block)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
48
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 45

def after_create(&block)
  @_definition.callbacks[:after_create] ||= []
  @_definition.callbacks[:after_create] << block
end
```

    
  

    
      
  
### 
  
    #**after_save**(&block)  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
53
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 50

def after_save(&block)
  @_definition.callbacks[:after_save] ||= []
  @_definition.callbacks[:after_save] << block
end
```

    
  

    
      
  
### 
  
    #**after_validation**(&block)  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
33
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 30

def after_validation(&block)
  @_definition.callbacks[:after_validation] ||= []
  @_definition.callbacks[:after_validation] << block
end
```

    
  

    
      
  
### 
  
    #**before_create**(&block)  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
43
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 40

def before_create(&block)
  @_definition.callbacks[:before_create] ||= []
  @_definition.callbacks[:before_create] << block
end
```

    
  

    
      
  
### 
  
    #**before_save**(&block)  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
38
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 35

def before_save(&block)
  @_definition.callbacks[:before_save] ||= []
  @_definition.callbacks[:before_save] << block
end
```

    
  

    
      
  
### 
  
    #**before_validation**(&block)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
28
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 25

def before_validation(&block)
  @_definition.callbacks[:before_validation] ||= []
  @_definition.callbacks[:before_validation] << block
end
```

    
  

    
      
  
### 
  
    #**init_with**(*args)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 63

def init_with(*args)
  args
end
```

    
  

    
      
  
### 
  
    #**initialize_with**(&block)  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 59

def initialize_with(&block)
  @_definition.callbacks[:initialize_with] = block
end
```

    
  

    
      
  
### 
  
    #**on_init**(&block)  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 55

def on_init(&block)
  @_definition.callbacks[:on_init] = block
end
```

    
  

    
      
  
### 
  
    #**process**(definition)  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
7
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 4

def process(definition, &)
  @_definition = definition
  instance_eval(&)
end
```

    
  

    
      
  
### 
  
    #**respond_to_missing?**(_method_name, _include_private = false)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 9

def respond_to_missing?(_method_name, _include_private = false)
  true
end
```

    
  

    
      
  
### 
  
    #**transient**(*field_names)  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
70
71
72
73
74
75
```

    
    
      

```
# File 'lib/fabrication/schematic/evaluator.rb', line 67

def transient(*field_names)
  field_names.each do |field_name|
    if field_name.is_a?(::Hash)
      field_name.each_pair { |name, value| @_definition.append_or_update_attribute(name, value, transient: true) }
    else
      @_definition.append_or_update_attribute(field_name, nil, transient: true)
    end
  end
end
```