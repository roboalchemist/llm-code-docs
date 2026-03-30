# Module: Formtastic::Actions::Buttonish
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    ButtonAction, InputAction
  
  

  
  
    Defined in:
    lib/formtastic/actions/buttonish.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**extra_button_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**supported_methods**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**extra_button_html_options**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
13
14
```

    
    
      

```
# File 'lib/formtastic/actions/buttonish.rb', line 10

def extra_button_html_options
  {
    :type => method
  }
end
```

    
  

    
      
  
### 
  
    #**supported_methods**  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/formtastic/actions/buttonish.rb', line 6

def supported_methods
  [:submit, :reset]
end
```