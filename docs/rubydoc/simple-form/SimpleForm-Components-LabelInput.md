# Module: SimpleForm::Components::LabelInput
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/label_input.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**label_input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**label_input**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
15
16
17
```

    
    
      

```
# File 'lib/simple_form/components/label_input.rb', line 11

def label_input(wrapper_options = nil)
  if options[:label] == false
    deprecated_component(:input, wrapper_options)
  else
    deprecated_component(:label, wrapper_options) + deprecated_component(:input, wrapper_options)
  end
end
```