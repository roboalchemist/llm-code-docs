# Module: Formtastic::Inputs::Base::Numeric
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    NumberInput, RangeInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/numeric.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**in_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**max_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**min_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**step_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**in_option**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/formtastic/inputs/base/numeric.rb', line 39

def in_option
  options[:in]
end
```

    
  

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

6
7
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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/numeric.rb', line 6

def input_html_options
  defaults = super

  # override rails default size - does not apply to numeric inputs
  #@todo document/spec
  defaults[:size] = nil
  
  if in_option
    defaults[:min] = in_option.to_a.min
    defaults[:max] = in_option.to_a.max
  else
    defaults[:min]  ||= min_option
    defaults[:max]  ||= max_option
  end
  defaults[:step] ||= step_option
  defaults
end
```

    
  

    
      
  
### 
  
    #**max_option**  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
37
```

    
    
      

```
# File 'lib/formtastic/inputs/base/numeric.rb', line 34

def max_option
  return options[:max] if options.key?(:max)
  validation_max
end
```

    
  

    
      
  
### 
  
    #**min_option**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
```

    
    
      

```
# File 'lib/formtastic/inputs/base/numeric.rb', line 29

def min_option
  return options[:min] if options.key?(:min)
  validation_min
end
```

    
  

    
      
  
### 
  
    #**step_option**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
```

    
    
      

```
# File 'lib/formtastic/inputs/base/numeric.rb', line 24

def step_option
  return options[:step] if options.key?(:step)
  validation_step
end
```

    
  

    
      
  
### 
  
    #**wrapper_html_options**  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
46
```

    
    
      

```
# File 'lib/formtastic/inputs/base/numeric.rb', line 43

def wrapper_html_options
  new_class = [super[:class], "numeric", "stringish"].compact.join(" ")
  super.merge(:class => new_class)
end
```