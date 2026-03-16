# Class: Capybara::RackTest::Driver
  
  
  

  
  
    Inherits:
    
      Driver::Base
      
        

          
- Object
          
            
- Driver::Base
          
            
- Capybara::RackTest::Driver
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rack_test/driver.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_OPTIONS =
          
        
        

```
{
  respect_data_method: false,
  follow_redirects: true,
  redirect_limit: 5
}.freeze
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**app**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute app.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**browser**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**delete**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dom**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_css**(selector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_xpath**(selector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**follow**(method, path, **attributes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**follow_redirects?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**get**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**header**(key, value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(app, **options)  ⇒ Driver 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Driver.

  

      
        
- 
  
    
      #**invalid_element_errors**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**post**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**put**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**redirect_limit**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**refresh**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**request**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**response**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**response_headers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**status_code**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**submit**(method, path, attributes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**title**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**visit**(path, **attributes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Driver::Base

  

#accept_modal, #active_element, #close_window, #current_window_handle, #dismiss_modal, #evaluate_async_script, #evaluate_script, #execute_script, #frame_title, #frame_url, #fullscreen_window, #go_back, #go_forward, #maximize_window, #needs_server?, #no_such_window_error, #open_new_window, #resize_window_to, #save_screenshot, #send_keys, #session_options, #switch_to_frame, #switch_to_window, #wait?, #window_handles, #window_size

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(app, **options)  ⇒ Driver 
  

  

  

  
    

Returns a new instance of Driver.

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

17
18
19
20
21
22
23
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 17

def initialize(app, **options)
  raise ArgumentError, 'rack-test requires a rack application, but none was given' unless app

  super()
  @app = app
  @options = DEFAULT_OPTIONS.merge(options)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**app**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute app.

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 15

def app
  @app
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 15

def options
  @options
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**browser**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 25

def browser
  @browser ||= Capybara::RackTest::Browser.new(self)
end
```

    
  

    
      
  
### 
  
    #**current_url**  ⇒ Object 
  

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 61

def current_url
  browser.current_url
end
```

    
  

    
      
  
### 
  
    #**delete**  ⇒ Object 
  

  

  

  
    
      

```

104
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 104

def delete(...); browser.delete(...); end
```

    
  

    
      
  
### 
  
    #**dom**  ⇒ Object 
  

  

  

  
    
      

```

89
90
91
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 89

def dom
  browser.dom
end
```

    
  

    
      
  
### 
  
    #**find_css**(selector)  ⇒ Object 
  

  

  

  
    
      

```

77
78
79
80
81
82
83
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 77

def find_css(selector)
  browser.find(:css, selector)
rescue Nokogiri::CSS::SyntaxError
  raise unless selector.include?(' i]')

  raise ArgumentError, "This driver doesn't support case insensitive attribute matching when using CSS base selectors"
end
```

    
  

    
      
  
### 
  
    #**find_xpath**(selector)  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 73

def find_xpath(selector)
  browser.find(:xpath, selector)
end
```

    
  

    
      
  
### 
  
    #**follow**(method, path, **attributes)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 57

def follow(method, path, **attributes)
  browser.follow(method, path, attributes)
end
```

    
  

    
      
  
### 
  
    #**follow_redirects?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 29

def follow_redirects?
  @options[:follow_redirects]
end
```

    
  

    
      
  
### 
  
    #**get**  ⇒ Object 
  

  

  

  
    
      

```

101
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 101

def get(...); browser.get(...); end
```

    
  

    
      
  
### 
  
    #**header**(key, value)  ⇒ Object 
  

  

  

  
    
      

```

105
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 105

def header(key, value); browser.header(key, value); end
```

    
  

    
      
  
### 
  
    #**html**  ⇒ Object 
  

  

  

  
    
      

```

85
86
87
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 85

def html
  browser.html
end
```

    
  

    
      
  
### 
  
    #**invalid_element_errors**  ⇒ Object 
  

  

  

  
    
      

```

107
108
109
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 107

def invalid_element_errors
  [Capybara::RackTest::Errors::StaleElementReferenceError]
end
```

    
  

    
      
  
### 
  
    #**post**  ⇒ Object 
  

  

  

  
    
      

```

102
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 102

def post(...); browser.post(...); end
```

    
  

    
      
  
### 
  
    #**put**  ⇒ Object 
  

  

  

  
    
      

```

103
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 103

def put(...); browser.put(...); end
```

    
  

    
      
  
### 
  
    #**redirect_limit**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 33

def redirect_limit
  @options[:redirect_limit]
end
```

    
  

    
      
  
### 
  
    #**refresh**  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 49

def refresh
  browser.refresh
end
```

    
  

    
      
  
### 
  
    #**request**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 41

def request
  browser.last_request
end
```

    
  

    
      
  
### 
  
    #**reset!**  ⇒ Object 
  

  

  

  
    
      

```

97
98
99
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 97

def reset!
  @browser = nil
end
```

    
  

    
      
  
### 
  
    #**response**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 37

def response
  browser.last_response
end
```

    
  

    
      
  
### 
  
    #**response_headers**  ⇒ Object 
  

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 65

def response_headers
  response.headers
end
```

    
  

    
      
  
### 
  
    #**status_code**  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 69

def status_code
  response.status
end
```

    
  

    
      
  
### 
  
    #**submit**(method, path, attributes)  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 53

def submit(method, path, attributes)
  browser.submit(method, path, attributes)
end
```

    
  

    
      
  
### 
  
    #**title**  ⇒ Object 
  

  

  

  
    
      

```

93
94
95
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 93

def title
  browser.title
end
```

    
  

    
      
  
### 
  
    #**visit**(path, **attributes)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/capybara/rack_test/driver.rb', line 45

def visit(path, **attributes)
  browser.visit(path, **attributes)
end
```