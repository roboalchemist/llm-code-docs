# Class: Capybara::Selenium::Driver
  
  
  

  
  
    Inherits:
    
      Driver::Base
      
        

          
- Object
          
            
- Driver::Base
          
            
- Capybara::Selenium::Driver
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Find
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/driver.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** ChromeDriver, EdgeDriver, FirefoxDriver, InternetExplorerDriver, SafariDriver, W3CFirefoxDriver
    
  
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_OPTIONS =
          
        
        

```
{
  browser: :firefox,
  clear_local_storage: nil,
  clear_session_storage: nil
}.freeze
```

      
        SPECIAL_OPTIONS =
          
        
        

```
%i[browser clear_local_storage clear_session_storage timeout native_displayed].freeze
```

      
        CAPS_VERSION =
          
        
        

```
Gem::Requirement.new('< 4.8.0')
```

      
    
  

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**selenium_webdriver_version**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute selenium_webdriver_version.

  

    
      
- 
  
    
      .**specializations**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute specializations.

  

    
  

  
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
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**load_selenium**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**register_specialization**(browser_name, specialization)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**accept_modal**(_type, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**active_element**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**browser**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**close_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_window_handle**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dismiss_modal**(_type, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**evaluate_async_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**evaluate_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**execute_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**frame_obscured_at?**(x:, y:)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fullscreen_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**go_back**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**go_forward**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(app, **options)  ⇒ Driver 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Driver.

  

      
        
- 
  
    
      #**invalid_element_errors**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**maximize_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**needs_server?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**no_such_window_error**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**open_new_window**(kind = :tab)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**quit**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**refresh**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**resize_window_to**(handle, width, height)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**save_screenshot**(path, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_keys**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**switch_to_frame**(frame)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**switch_to_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**title**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**visit**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wait?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**window_handles**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**window_size**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Find

  

#find_css, #find_xpath

  
  
  
  
  
  
  
  
  
### Methods inherited from Driver::Base

  

#find_css, #find_xpath, #frame_title, #frame_url, #response_headers, #session_options, #status_code

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(app, **options)  ⇒ Driver 
  

  

  

  
    

Returns a new instance of Driver.

  

  

  
    
      

```

83
84
85
86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 83

def initialize(app, **options)
  super()
  self.class.load_selenium
  @app = app
  @browser = nil
  @exit_status = nil
  @frame_handles = Hash.new { |hash, handle| hash[handle] = [] }
  @options = DEFAULT_OPTIONS.merge(options)
  @node_class = ::Capybara::Selenium::Node
end
```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**selenium_webdriver_version**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute selenium_webdriver_version.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 20

def selenium_webdriver_version
  @selenium_webdriver_version
end
```

    
  

    
      
      
      
  
### 
  
    .**specializations**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute specializations.

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 55

def specializations
  @specializations
end
```

    
  

    
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**app**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute app.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 17

def app
  @app
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 17

def options
  @options
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**load_selenium**  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
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
35
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
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 22

def load_selenium
  require 'selenium-webdriver'
  require 'capybara/selenium/patches/atoms'
  require 'capybara/selenium/patches/is_displayed'

  # Look up the version of `selenium-webdriver` to
  # see if it's a version we support.
  #
  # By default, we use Gem.loaded_specs to determine
  # the version number. However, in some cases, such
  # as when loading `selenium-webdriver` outside of
  # Rubygems, we fall back to referencing
  # Selenium::WebDriver::VERSION. Ideally we'd
  # use the constant in all cases, but earlier versions
  # of `selenium-webdriver` didn't provide the constant.
  @selenium_webdriver_version =
    if Gem.loaded_specs['selenium-webdriver']
      Gem.loaded_specs['selenium-webdriver'].version
    else
      Gem::Version.new(Selenium::WebDriver::VERSION)
    end

  unless Gem::Requirement.new('>= 4.8').satisfied_by? @selenium_webdriver_version
    warn "Warning: You're using an unsupported version of selenium-webdriver, please upgrade to 4.8+."
  end

  @selenium_webdriver_version
rescue LoadError => e
  raise e unless e.message.include?('selenium-webdriver')

  raise LoadError, "Capybara's selenium driver is unable to load `selenium-webdriver`, please install the gem and add `gem 'selenium-webdriver'` to your Gemfile if you are using bundler."
end
```

    
  

    
      
  
### 
  
    .**register_specialization**(browser_name, specialization)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 57

def register_specialization(browser_name, specialization)
  @specializations ||= {}
  @specializations[browser_name] = specialization
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**accept_modal**(_type, **options)  ⇒ Object 
  

  

  

  
    
      

```

264
265
266
267
268
269
270
271
272
273
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 264

def accept_modal(_type, **options)
  yield if block_given?
  modal = find_modal(**options)

  modal.send_keys options[:with] if options[:with]

  message = modal.text
  modal.accept
  message
end
```

    
  

    
      
  
### 
  
    #**active_element**  ⇒ Object 
  

  

  

  
    
      

```

142
143
144
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 142

def active_element
  build_node(native_active_element)
end
```

    
  

    
      
  
### 
  
    #**browser**  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 63

def browser
  unless @browser
    options[:http_client] ||= begin
      require 'capybara/selenium/patches/persistent_client'
      if options[:timeout]
        ::Capybara::Selenium::PersistentClient.new(read_timeout: options[:timeout])
      else
        ::Capybara::Selenium::PersistentClient.new
      end
    end
    processed_options = options.except(*SPECIAL_OPTIONS)

    @browser = Selenium::WebDriver.for(options[:browser], processed_options)

    specialize_driver
    setup_exit_handler
  end
  @browser
end
```

    
  

    
      
  
### 
  
    #**close_window**(handle)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

235
236
237
238
239
240
241
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 235

def close_window(handle)
  raise ArgumentError, 'Not allowed to close the primary window' if handle == window_handles.first

  within_given_window(handle) do
    browser.close
  end
end
```

    
  

    
      
  
### 
  
    #**current_url**  ⇒ Object 
  

  

  

  
    
      

```

120
121
122
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 120

def current_url
  browser.current_url
end
```

    
  

    
      
  
### 
  
    #**current_window_handle**  ⇒ Object 
  

  

  

  
    
      

```

205
206
207
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 205

def current_window_handle
  browser.window_handle
end
```

    
  

    
      
  
### 
  
    #**dismiss_modal**(_type, **options)  ⇒ Object 
  

  

  

  
    
      

```

275
276
277
278
279
280
281
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 275

def dismiss_modal(_type, **options)
  yield if block_given?
  modal = find_modal(**options)
  message = modal.text
  modal.dismiss
  message
end
```

    
  

    
      
  
### 
  
    #**evaluate_async_script**(script, *args)  ⇒ Object 
  

  

  

  
    
      

```

136
137
138
139
140
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 136

def evaluate_async_script(script, *args)
  browser.manage.timeouts.script_timeout = Capybara.default_max_wait_time
  result = browser.execute_async_script(script, *native_args(args))
  unwrap_script_result(result)
end
```

    
  

    
      
  
### 
  
    #**evaluate_script**(script, *args)  ⇒ Object 
  

  

  

  
    
      

```

131
132
133
134
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 131

def evaluate_script(script, *args)
  result = execute_script("return #{script}", *args)
  unwrap_script_result(result)
end
```

    
  

    
      
  
### 
  
    #**execute_script**(script, *args)  ⇒ Object 
  

  

  

  
    
      

```

127
128
129
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 127

def execute_script(script, *args)
  browser.execute_script(script, *native_args(args))
end
```

    
  

    
      
  
### 
  
    #**frame_obscured_at?**(x:, y:)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

178
179
180
181
182
183
184
185
186
187
188
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 178

def frame_obscured_at?(x:, y:)
  frame = @frame_handles[current_window_handle].last
  return false unless frame

  switch_to_frame(:parent)
  begin
    frame.base.obscured?(x: x, y: y)
  ensure
    switch_to_frame(frame)
  end
end
```

    
  

    
      
  
### 
  
    #**fullscreen_window**(handle)  ⇒ Object 
  

  

  

  
    
      

```

229
230
231
232
233
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 229

def fullscreen_window(handle)
  within_given_window(handle) do
    browser.manage.window.full_screen
  end
end
```

    
  

    
      
  
### 
  
    #**go_back**  ⇒ Object 
  

  

  

  
    
      

```

102
103
104
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 102

def go_back
  browser.navigate.back
end
```

    
  

    
      
  
### 
  
    #**go_forward**  ⇒ Object 
  

  

  

  
    
      

```

106
107
108
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 106

def go_forward
  browser.navigate.forward
end
```

    
  

    
      
  
### 
  
    #**html**  ⇒ Object 
  

  

  

  
    
      

```

110
111
112
113
114
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 110

def html
  browser.page_source
rescue Selenium::WebDriver::Error::JavascriptError => e
  raise unless e.message.include?('documentElement is null')
end
```

    
  

    
      
  
### 
  
    #**invalid_element_errors**  ⇒ Object 
  

  

  

  
    
      

```

297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 297

def invalid_element_errors
  @invalid_element_errors ||=
    [
      ::Selenium::WebDriver::Error::StaleElementReferenceError,
      ::Selenium::WebDriver::Error::ElementNotInteractableError,
      ::Selenium::WebDriver::Error::InvalidSelectorError, # Work around chromedriver go_back/go_forward race condition
      ::Selenium::WebDriver::Error::ElementClickInterceptedError,
      ::Selenium::WebDriver::Error::NoSuchElementError, # IE
      ::Selenium::WebDriver::Error::InvalidArgumentError # IE
    ].tap do |errors|
      if defined?(::Selenium::WebDriver::Error::DetachedShadowRootError)
        errors.push(::Selenium::WebDriver::Error::DetachedShadowRootError)
      end
    end
end
```

    
  

    
      
  
### 
  
    #**maximize_window**(handle)  ⇒ Object 
  

  

  

  
    
      

```

222
223
224
225
226
227
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 222

def maximize_window(handle)
  within_given_window(handle) do
    browser.manage.window.maximize
  end
  sleep 0.1 # work around for https://code.google.com/p/selenium/issues/detail?id=7405
end
```

    
  

    
      
  
### 
  
    #**needs_server?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

125
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 125

def needs_server?; true; end
```

    
  

    
      
  
### 
  
    #**no_such_window_error**  ⇒ Object 
  

  

  

  
    
      

```

313
314
315
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 313

def no_such_window_error
  Selenium::WebDriver::Error::NoSuchWindowError
end
```

    
  

    
      
  
### 
  
    #**open_new_window**(kind = :tab)  ⇒ Object 
  

  

  

  
    
      

```

247
248
249
250
251
252
253
254
255
256
257
258
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 247

def open_new_window(kind = :tab)
  if browser.switch_to.respond_to?(:new_window)
    handle = current_window_handle
    browser.switch_to.new_window(kind)
    switch_to_window(handle)
  else
    browser.manage.new_window(kind)
  end
rescue NoMethodError, Selenium::WebDriver::Error::WebDriverError
  # If not supported by the driver or browser default to using JS
  browser.execute_script('window.open();')
end
```

    
  

    
      
  
### 
  
    #**quit**  ⇒ Object 
  

  

  

  
    
      

```

283
284
285
286
287
288
289
290
291
292
293
294
295
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 283

def quit
  @browser&.quit
rescue Selenium::WebDriver::Error::SessionNotCreatedError, Errno::ECONNREFUSED,
       Selenium::WebDriver::Error::InvalidSessionIdError
  # Browser must have already gone
rescue Selenium::WebDriver::Error::UnknownError => e
  unless silenced_unknown_error_message?(e.message) # Most likely already gone
    # probably already gone but not sure - so warn
    warn "Ignoring Selenium UnknownError during driver quit: #{e.message}"
  end
ensure
  @browser = nil
end
```

    
  

    
      
  
### 
  
    #**refresh**  ⇒ Object 
  

  

  

  
    
      

```

98
99
100
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 98

def refresh
  browser.navigate.refresh
end
```

    
  

    
      
  
### 
  
    #**reset!**  ⇒ Object 
  

  

  

  
    
      

```

155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 155

def reset!
  # Use instance variable directly so we avoid starting the browser just to reset the session
  return unless @browser

  navigated = false
  timer = Capybara::Helpers.timer(expire_in: 10)
  begin
    # Only trigger a navigation if we haven't done it already, otherwise it
    # can trigger an endless series of unload modals
    reset_browser_state unless navigated
    navigated = true
    # Ensure the page is empty and trigger an UnhandledAlertError for any modals that appear during unload
    wait_for_empty_page(timer)
  rescue *unhandled_alert_errors
    # This error is thrown if an unhandled alert is on the page
    # Firefox appears to automatically dismiss this alert, chrome does not
    # We'll try to accept it
    accept_unhandled_reset_alert
    # try cleaning up the browser again
    retry
  end
end
```

    
  

    
      
  
### 
  
    #**resize_window_to**(handle, width, height)  ⇒ Object 
  

  

  

  
    
      

```

216
217
218
219
220
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 216

def resize_window_to(handle, width, height)
  within_given_window(handle) do
    browser.manage.window.resize_to(width, height)
  end
end
```

    
  

    
      
  
### 
  
    #**save_screenshot**(path, **options)  ⇒ Object 
  

  

  

  
    
      

```

151
152
153
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 151

def save_screenshot(path, **options)
  browser.save_screenshot(path, **options)
end
```

    
  

    
      
  
### 
  
    #**send_keys**(*args)  ⇒ Object 
  

  

  

  
    
      

```

146
147
148
149
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 146

def send_keys(*args)
  # Should this call the specialized nodes rather than native???
  native_active_element.send_keys(*args)
end
```

    
  

    
      
  
### 
  
    #**switch_to_frame**(frame)  ⇒ Object 
  

  

  

  
    
      

```

190
191
192
193
194
195
196
197
198
199
200
201
202
203
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 190

def switch_to_frame(frame)
  handles = @frame_handles[current_window_handle]
  case frame
  when :top
    handles.clear
    browser.switch_to.default_content
  when :parent
    handles.pop
    browser.switch_to.parent_frame
  else
    handles << frame
    browser.switch_to.frame(frame.native)
  end
end
```

    
  

    
      
  
### 
  
    #**switch_to_window**(handle)  ⇒ Object 
  

  

  

  
    
      

```

260
261
262
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 260

def switch_to_window(handle)
  browser.switch_to.window handle
end
```

    
  

    
      
  
### 
  
    #**title**  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 116

def title
  browser.title
end
```

    
  

    
      
  
### 
  
    #**visit**(path)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 94

def visit(path)
  browser.navigate.to(path)
end
```

    
  

    
      
  
### 
  
    #**wait?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

124
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 124

def wait?; true; end
```

    
  

    
      
  
### 
  
    #**window_handles**  ⇒ Object 
  

  

  

  
    
      

```

243
244
245
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 243

def window_handles
  browser.window_handles
end
```

    
  

    
      
  
### 
  
    #**window_size**(handle)  ⇒ Object 
  

  

  

  
    
      

```

209
210
211
212
213
214
```

    
    
      

```
# File 'lib/capybara/selenium/driver.rb', line 209

def window_size(handle)
  within_given_window(handle) do
    size = browser.manage.window.size
    [size.width, size.height]
  end
end
```