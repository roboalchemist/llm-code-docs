# Class: Capybara::Config
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Config
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/config.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        OPTIONS =
          
        
        

```
%i[
  app reuse_server threadsafe server default_driver javascript_driver use_html5_parsing allow_gumbo
].freeze
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**app**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute app.

  

    
      
- 
  
    
      #**default_driver**  ⇒ Symbol 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The name of the driver to use by default.

  

    
      
- 
  
    
      #**javascript_driver**  ⇒ Symbol 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The name of the driver used when JavaScript is needed.

  

    
      
- 
  
    
      #**reuse_server**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

rubocop:disable Style/BisectedAttrAccessor.

  

    
      
- 
  
    
      #**server**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Return the proc that Capybara will call to run the Rack application.

  

    
      
- 
  
    
      #**session_options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

rubocop:disable Style/BisectedAttrAccessor.

  

    
      
- 
  
    
      #**threadsafe**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

rubocop:disable Style/BisectedAttrAccessor.

  

    
      
- 
  
    
      #**use_html5_parsing**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute use_html5_parsing.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**allow_gumbo**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**allow_gumbo=**(val)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**deprecate**(method, alternate_method, once: false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Config 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Config.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Config 
  

  

  

  
    

Returns a new instance of Config.

  

  

  
    
      

```

22
23
24
25
```

    
    
      

```
# File 'lib/capybara/config.rb', line 22

def initialize
  @session_options = Capybara::SessionConfig.new
  @javascript_driver = nil
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**app**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute app.

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/capybara/config.rb', line 14

def app
  @app
end
```

    
  

    
      
      
      
  
### 
  
    #**default_driver**  ⇒ Symbol 
  

  

  

  
    

Returns The name of the driver to use by default.

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
        —
        

The name of the driver to use by default

      
    
  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/capybara/config.rb', line 74

def default_driver
  @default_driver || :rack_test
end
```

    
  

    
      
      
      
  
### 
  
    #**javascript_driver**  ⇒ Symbol 
  

  

  

  
    

Returns The name of the driver used when JavaScript is needed.

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
        —
        

The name of the driver used when JavaScript is needed

      
    
  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/capybara/config.rb', line 82

def javascript_driver
  @javascript_driver || :selenium
end
```

    
  

    
      
      
      
  
### 
  
    #**reuse_server**  ⇒ Object 
  

  

  

  
    

rubocop:disable Style/BisectedAttrAccessor

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/capybara/config.rb', line 15

def reuse_server
  @reuse_server
end
```

    
  

    
      
      
      
  
### 
  
    #**server**  ⇒ Object 
  

  

  

  
    

Return the proc that Capybara will call to run the Rack application.
The block returned receives a rack app, port, and host/ip and should run a Rack handler
By default, Capybara will try to use puma.

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/capybara/config.rb', line 43

def server
  @server
end
```

    
  

    
      
      
      
  
### 
  
    #**session_options**  ⇒ Object  (readonly)
  

  

  

  
    

rubocop:disable Style/BisectedAttrAccessor

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/capybara/config.rb', line 15

def session_options
  @session_options
end
```

    
  

    
      
      
      
  
### 
  
    #**threadsafe**  ⇒ Object 
  

  

  

  
    

rubocop:disable Style/BisectedAttrAccessor

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/capybara/config.rb', line 15

def threadsafe
  @threadsafe
end
```

    
  

    
      
      
      
  
### 
  
    #**use_html5_parsing**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute use_html5_parsing.

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/capybara/config.rb', line 14

def use_html5_parsing
  @use_html5_parsing
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**allow_gumbo**  ⇒ Object 
  

  

  

  
    
      

```

99
100
101
102
```

    
    
      

```
# File 'lib/capybara/config.rb', line 99

def allow_gumbo
  deprecate('allow_gumbo', 'use_html5_parsing')
  use_html5_parsing
end
```

    
  

    
      
  
### 
  
    #**allow_gumbo=**(val)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
```

    
    
      

```
# File 'lib/capybara/config.rb', line 94

def allow_gumbo=(val)
  deprecate('allow_gumbo=', 'use_html5_parsing=')
  self.use_html5_parsing = val
end
```

    
  

    
      
  
### 
  
    #**deprecate**(method, alternate_method, once: false)  ⇒ Object 
  

  

  

  
    
      

```

86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/capybara/config.rb', line 86

def deprecate(method, alternate_method, once: false)
  @deprecation_notified ||= {}
  unless once && @deprecation_notified[method]
    Capybara::Helpers.warn "DEPRECATED: ##{method} is deprecated, please use ##{alternate_method} instead: #{Capybara::Helpers.filter_backtrace(caller)}"
  end
  @deprecation_notified[method] = true
end
```