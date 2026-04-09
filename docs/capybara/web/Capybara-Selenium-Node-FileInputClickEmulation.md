# Module: Capybara::Selenium::Node::FileInputClickEmulation
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/extensions/file_input_click_emulation.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**click**(keys = [], **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**click**(keys = [], **options)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
8
9
10
11
```

    
    
      

```
# File 'lib/capybara/selenium/extensions/file_input_click_emulation.rb', line 5

def click(keys = [], **options)
  super
rescue Selenium::WebDriver::Error::InvalidArgumentError
  return emulate_click if attaching_file? && visible_file_field?

  raise
end

```