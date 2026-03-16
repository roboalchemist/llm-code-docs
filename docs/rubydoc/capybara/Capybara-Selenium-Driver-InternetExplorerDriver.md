# Module: Capybara::Selenium::Driver::InternetExplorerDriver
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/driver_specializations/internet_explorer_driver.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**switch_to_frame**(frame)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**switch_to_frame**(frame)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/capybara/selenium/driver_specializations/internet_explorer_driver.rb', line 6

def switch_to_frame(frame)
  return super unless frame == :parent

  # iedriverserver has an issue if the current frame is removed from within it
  # so we have to move to the default_content and iterate back through the frames
  handles = @frame_handles[current_window_handle]
  browser.switch_to.default_content
  handles.tap(&:pop).each { |fh| browser.switch_to.frame(fh.native) }
end

```