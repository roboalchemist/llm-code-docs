# Module: Capybara::Selenium::Driver::ChromeDriver
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/driver_specializations/chrome_driver.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**extended**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**fullscreen_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**resize_window_to**(handle, width, height)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**extended**(base)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
12
```

    
    
      

```
# File 'lib/capybara/selenium/driver_specializations/chrome_driver.rb', line 7

def self.extended(base)
  bridge = base.send(:bridge)
  bridge.extend Capybara::Selenium::ChromeLogs unless bridge.respond_to?(:log)
  bridge.extend Capybara::Selenium::IsDisplayed unless bridge.send(:commands, :is_element_displayed)
  base.options[:native_displayed] = false if base.options[:native_displayed].nil?
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**fullscreen_window**(handle)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
19
20
21
22
23
```

    
    
      

```
# File 'lib/capybara/selenium/driver_specializations/chrome_driver.rb', line 14

def fullscreen_window(handle)
  within_given_window(handle) do
    super
  rescue NoMethodError => e
    raise unless e.message.include?('full_screen_window')

    result = bridge.http.call(:post, "session/#{bridge.session_id}/window/fullscreen", {})
    result['value']
  end
end
```

    
  

    
      
  
### 
  
    #**reset!**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
39
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
50
51
52
53
54
55
```

    
    
      

```
# File 'lib/capybara/selenium/driver_specializations/chrome_driver.rb', line 36

def reset!
  # Use instance variable directly so we avoid starting the browser just to reset the session
  return unless @browser

  switch_to_window(window_handles.first)
  window_handles.slice(1..).each { |win| close_window(win) }
  return super if chromedriver_version < 73

  timer = Capybara::Helpers.timer(expire_in: 10)
  begin
    clear_storage unless uniform_storage_clear?
    @browser.navigate.to('about:blank')
    wait_for_empty_page(timer)
  rescue *unhandled_alert_errors
    accept_unhandled_reset_alert
    retry
  end

  execute_cdp('Storage.clearDataForOrigin', origin: '*', storageTypes: storage_types_to_clear)
end
```

    
  

    
      
  
### 
  
    #**resize_window_to**(handle, width, height)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
28
29
30
31
32
33
34
```

    
    
      

```
# File 'lib/capybara/selenium/driver_specializations/chrome_driver.rb', line 25

def resize_window_to(handle, width, height)
  super
rescue Selenium::WebDriver::Error::UnknownError => e
  raise unless e.message.include?('failed to change window state')

  # Chromedriver doesn't wait long enough for state to change when coming out of fullscreen
  # and raises unnecessary error. Wait a bit and try again.
  sleep 0.25
  super
end
```