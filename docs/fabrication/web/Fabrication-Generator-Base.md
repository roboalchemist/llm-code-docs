# Class: Fabrication::Generator::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Generator::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/generator/base.rb
  
  

  
## Direct Known Subclasses

  

ActiveRecord, Mongoid, Sequel

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**supports?**(_resolved_class)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**_klass**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**build**(attributes = [], callbacks = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**build_instance**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**build_instance_with_constructor_override**(callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**build_instance_with_init_callback**(callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**create**(attributes = [], callbacks = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**execute_callbacks**(callbacks)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**execute_deprecated_callbacks**(callbacks, callback_type, replacement_callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(resolved_class)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**method_missing**(method_name, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**respond_to_missing?**(method_name, _include_private = false)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**set_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_hash**(attributes = [], _callbacks = [])  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_params**(attributes = [])  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(resolved_class)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

91
92
93
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 91

def initialize(resolved_class)
  self.resolved_class = resolved_class
end
```

    
  

  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(method_name, *args)  ⇒ Object 
  

  

  

  
    
      

```

99
100
101
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 99

def method_missing(method_name, *args, &)
  _attributes.fetch(method_name) { super }
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**supports?**(_resolved_class)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 4

def self.supports?(_resolved_class)
  true
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**_klass**  ⇒ Object 
  

  

  

  
    
      

```

103
104
105
106
107
108
109
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 103

def _klass
  Fabrication::Support.log_deprecation(
    'The `_klass` method in fabricator definitions has been replaced by `resolved_class`'
  )

  resolved_class
end
```

    
  

    
      
  
### 
  
    #**build**(attributes = [], callbacks = {})  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
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
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 8

def build(attributes = [], callbacks = {})
  process_attributes(attributes)

  if callbacks[:initialize_with]
    build_instance_with_constructor_override(callbacks[:initialize_with])
  elsif callbacks[:on_init]
    Fabrication::Support.log_deprecation(
      'The on_init callback has been replaced by initialize_with. Please see the documentation for usage'
    )
    build_instance_with_init_callback(callbacks[:on_init])
  else
    build_instance
  end
  execute_callbacks(callbacks[:after_build])
  _instance
end
```

    
  

    
      
  
### 
  
    #**build_instance**  ⇒ Object 
  

  

  

  
    
      

```

80
81
82
83
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 80

def build_instance
  self._instance = resolved_class.new
  set_attributes
end
```

    
  

    
      
  
### 
  
    #**build_instance_with_constructor_override**(callback)  ⇒ Object 
  

  

  

  
    
      

```

70
71
72
73
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 70

def build_instance_with_constructor_override(callback)
  self._instance = instance_exec(_transient_attributes, &callback)
  set_attributes
end
```

    
  

    
      
  
### 
  
    #**build_instance_with_init_callback**(callback)  ⇒ Object 
  

  

  

  
    
      

```

75
76
77
78
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 75

def build_instance_with_init_callback(callback)
  self._instance = resolved_class.new(*callback.call(_transient_attributes))
  set_attributes
end
```

    
  

    
      
  
### 
  
    #**create**(attributes = [], callbacks = {})  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 25

def create(attributes = [], callbacks = {})
  build(attributes, callbacks)
  execute_deprecated_callbacks(callbacks, :before_validation, :before_create)
  execute_deprecated_callbacks(callbacks, :after_validation, :before_create)
  execute_deprecated_callbacks(callbacks, :before_save, :before_create)
  execute_callbacks(callbacks[:before_create])
  persist
  execute_callbacks(callbacks[:after_create])
  execute_deprecated_callbacks(callbacks, :after_save, :after_create)
  _instance
end
```

    
  

    
      
  
### 
  
    #**execute_callbacks**(callbacks)  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 48

def execute_callbacks(callbacks)
  callbacks&.each { |callback| _instance.instance_exec(_instance, _transient_attributes, &callback) }
end
```

    
  

    
      
  
### 
  
    #**execute_deprecated_callbacks**(callbacks, callback_type, replacement_callback)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 37

def execute_deprecated_callbacks(callbacks, callback_type, replacement_callback)
  if callbacks[callback_type]
    Fabrication::Support.log_deprecation(
      "Using #{callback_type} is deprecated but you can replace it " \
      "with #{replacement_callback} with the same result."
    )
  end

  execute_callbacks(callbacks[callback_type])
end
```

    
  

    
      
  
### 
  
    #**respond_to_missing?**(method_name, _include_private = false)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

95
96
97
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 95

def respond_to_missing?(method_name, _include_private = false)
  _attributes.key?(method_name)
end
```

    
  

    
      
  
### 
  
    #**set_attributes**  ⇒ Object 
  

  

  

  
    
      

```

85
86
87
88
89
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 85

def set_attributes
  _attributes.each do |k, v|
    _instance.send(:"#{k}=", v)
  end
end
```

    
  

    
      
  
### 
  
    #**to_hash**(attributes = [], _callbacks = [])  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
61
62
63
64
65
66
67
68
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 57

def to_hash(attributes = [], _callbacks = [])
  process_attributes(attributes)
  Fabrication::Support.hash_class.new.tap do |hash|
    _attributes.map do |name, value|
      if value.respond_to?(:id)
        hash["#{name}_id"] = value.id
      else
        hash[name] = value
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**to_params**(attributes = [])  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
```

    
    
      

```
# File 'lib/fabrication/generator/base.rb', line 52

def to_params(attributes = [])
  process_attributes(attributes)
  _attributes.respond_to?(:with_indifferent_access) ? _attributes.with_indifferent_access : _attributes
end
```