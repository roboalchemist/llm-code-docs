# Module: Capybara::Selenium::Node::Html5Drag
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/extensions/html5_drag.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**drag_to**(element, html5: nil, delay: 0.05, drop_modifiers: [])  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Implement methods to emulate HTML5 drag and drop.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**drag_to**(element, html5: nil, delay: 0.05, drop_modifiers: [])  ⇒ Object 
  

  

  

  
    

Implement methods to emulate HTML5 drag and drop

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/selenium/extensions/html5_drag.rb', line 7

def drag_to(element, html5: nil, delay: 0.05, drop_modifiers: [])
  drop_modifiers = Array(drop_modifiers)

  driver.execute_script MOUSEDOWN_TRACKER
  scroll_if_needed { browser_action.click_and_hold(native).perform }
  html5 = !driver.evaluate_script(LEGACY_DRAG_CHECK, self) if html5.nil?
  if html5
    perform_html5_drag(element, delay, drop_modifiers)
  else
    perform_legacy_drag(element, drop_modifiers)
  end
end
```