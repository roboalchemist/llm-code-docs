# Module: SimpleForm::Components::Labels
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/components/labels.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**label**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_target**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_text**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**label**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/simple_form/components/labels.rb', line 29

def label(wrapper_options = nil)
  label_options = merge_wrapper_options(label_html_options, wrapper_options)

  if generate_label_for_attribute?
    @builder.label(label_target, label_text, label_options)
  else
    template.label_tag(nil, label_text, label_options)
  end
end
```

    
  

    
      
  
### 
  
    #**label_html_options**  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
51
52
53
54
55
56
57
58
59
```

    
    
      

```
# File 'lib/simple_form/components/labels.rb', line 48

def label_html_options
  label_html_classes = SimpleForm.additional_classes_for(:label) {
    [input_type, required_class, disabled_class, SimpleForm.label_class].compact
  }

  label_options = html_options_for(:label, label_html_classes)
  if options.key?(:input_html) && options[:input_html].key?(:id)
    label_options[:for] = options[:input_html][:id]
  end

  label_options
end
```

    
  

    
      
  
### 
  
    #**label_target**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/simple_form/components/labels.rb', line 44

def label_target
  attribute_name
end
```

    
  

    
      
  
### 
  
    #**label_text**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
42
```

    
    
      

```
# File 'lib/simple_form/components/labels.rb', line 39

def label_text(wrapper_options = nil)
  label_text = options[:label_text] || SimpleForm.label_text
  label_text.call(html_escape(raw_label_text), required_label_text, options[:label].present?).strip.html_safe
end
```