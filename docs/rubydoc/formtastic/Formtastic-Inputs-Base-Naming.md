# Module: Formtastic::Inputs::Base::Naming
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/naming.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**as**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**attributized_method_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**humanized_method_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sanitized_method_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sanitized_object_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**as**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/inputs/base/naming.rb', line 7

def as
  self.class.name.split("::")[-1].underscore.gsub(/_input$/, '')
end
```

    
  

    
      
  
### 
  
    #**attributized_method_name**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/formtastic/inputs/base/naming.rb', line 19

def attributized_method_name
  method.to_s.gsub(/_id$/, '').to_sym
end
```

    
  

    
      
  
### 
  
    #**humanized_method_name**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/naming.rb', line 23

def humanized_method_name
  if builder.label_str_method != :humanize
    # Special case where label_str_method should trump the human_attribute_name
    # TODO: is this actually a desired bheavior, or should we ditch label_str_method and
    # rely purely on :human_attribute_name.
    method.to_s.send(builder.label_str_method)
  elsif object && object.class.respond_to?(:human_attribute_name)
    object.class.human_attribute_name(method.to_s)
  else
    method.to_s.send(builder.label_str_method)
  end
end
```

    
  

    
      
  
### 
  
    #**input_name**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/formtastic/inputs/base/naming.rb', line 36

def input_name
  association_primary_key
end
```

    
  

    
      
  
### 
  
    #**sanitized_method_name**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/formtastic/inputs/base/naming.rb', line 15

def sanitized_method_name
  @sanitized_method_name ||= method.to_s.gsub(/[\?\/\-]$/, '')
end
```

    
  

    
      
  
### 
  
    #**sanitized_object_name**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/formtastic/inputs/base/naming.rb', line 11

def sanitized_object_name
  object_name.to_s.gsub(/\]\[|[^-a-zA-Z0-9:.]/, "_").sub(/_$/, "")
end
```