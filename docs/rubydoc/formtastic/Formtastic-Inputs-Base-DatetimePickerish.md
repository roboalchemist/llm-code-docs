# Module: Formtastic::Inputs::Base::DatetimePickerish
  
  
  

  

  
  
  
  
  
      Includes:
      Placeholder
  
  
  

  
  
    Included in:
    DatePickerInput, DatetimePickerInput, TimePickerInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/datetime_pickerish.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**default_maxlength**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_step**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**extra_input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html_input_type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**maxlength**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**step**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Placeholder

  

#placeholder_text

  
    
## Instance Method Details

    
      
  
### 
  
    #**default_maxlength**  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 52

def default_maxlength
  default_size
end
```

    
  

    
      
  
### 
  
    #**default_size**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 12

def default_size
  raise NotImplementedError
end
```

    
  

    
      
  
### 
  
    #**default_step**  ⇒ Object 
  

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 56

def default_step
  1
end
```

    
  

    
      
  
### 
  
    #**extra_input_html_options**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 24

def extra_input_html_options
  {
    :type => html_input_type, 
    :size => size, 
    :maxlength => maxlength, 
    :step => step,
    :value => value
  }
end
```

    
  

    
      
  
### 
  
    #**html_input_type**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 8

def html_input_type
  raise NotImplementedError
end
```

    
  

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 20

def input_html_options
  super.merge(extra_input_html_options)
end
```

    
  

    
      
  
### 
  
    #**maxlength**  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
49
50
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 46

def maxlength
  return options[:maxlength] if options.key?(:maxlength)
  return options[:input_html][:maxlength] if options[:input_html] && options[:input_html].key?(:maxlength)
  default_size
end
```

    
  

    
      
  
### 
  
    #**size**  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
37
38
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 34

def size
  return options[:size] if options.key?(:size)
  return options[:input_html][:size] if options[:input_html] && options[:input_html].key?(:size)
  default_size
end
```

    
  

    
      
  
### 
  
    #**step**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
43
44
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 40

def step
  return step_from_macro(options[:input_html][:step]) if options[:input_html] && options[:input_html][:step] && options[:input_html][:step].is_a?(Symbol)
  return options[:input_html][:step] if options[:input_html] && options[:input_html].key?(:step)
  default_step
end
```

    
  

    
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/formtastic/inputs/base/datetime_pickerish.rb', line 16

def value
  raise NotImplementedError
end
```