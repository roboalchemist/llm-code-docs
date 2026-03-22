# Module: Capybara::Selenium::Driver::FirefoxDriver
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/driver_specializations/firefox_driver.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**extended**(driver)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**extended**(driver)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
10
```

    
    
      

```
# File 'lib/capybara/selenium/driver_specializations/firefox_driver.rb', line 6

def self.extended(driver)
  driver.extend Capybara::Selenium::Driver::W3CFirefoxDriver
  bridge = driver.send(:bridge)
  bridge.extend Capybara::Selenium::IsDisplayed unless bridge.send(:commands, :is_element_displayed)
end

```