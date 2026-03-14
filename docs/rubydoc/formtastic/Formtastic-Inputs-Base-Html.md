# Module: Formtastic::Inputs::Base::Html
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/html.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**dom_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dom_index**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  abstract
  
  

  
    

Defines how the instance of an input should be rendered to a HTML string.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**dom_id**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/formtastic/inputs/base/html.rb', line 31

def dom_id
  [
    builder.dom_id_namespace,
    sanitized_object_name,
    dom_index,
    association_primary_key || sanitized_method_name
  ].reject { |x| x.blank? }.join('_')
end
```

    
  

    
      
  
### 
  
    #**dom_index**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
43
44
45
46
47
48
49
```

    
    
      

```
# File 'lib/formtastic/inputs/base/html.rb', line 40

def dom_index
  if builder.options.has_key?(:index)
    builder.options[:index]
  elsif !builder.auto_index.blank?
    # TODO there's no coverage for this case, not sure how to create a scenario for it
    builder.auto_index
  else
    +""
  end
end
```

    
  

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
25
26
27
28
29
```

    
    
      

```
# File 'lib/formtastic/inputs/base/html.rb', line 22

def input_html_options
  {
    :id => dom_id,
    :required => required_attribute?,
    :autofocus => autofocus?,
    :readonly => readonly?
  }.merge(options[:input_html] || {}).merge(error_aria_attributes)
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
  **This method is abstract.**
  

Implement this method in your input class to describe how the input should render itself.

Defines how the instance of an input should be rendered to a HTML string.

  

  
  
    
#### Examples:

    
      
        
##### 

A basic label and text field input inside a standard wrapping might look like this:

      
      

```
def to_html
  input_wrapping do
    label_html <<
    builder.text_field(method, input_html_options)
  end
end
```

    
  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/formtastic/inputs/base/html.rb', line 18

def to_html
  raise NotImplementedError
end
```