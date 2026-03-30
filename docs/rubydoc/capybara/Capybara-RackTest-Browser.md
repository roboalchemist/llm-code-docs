# Class: Capybara::RackTest::Browser
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::RackTest::Browser
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Rack::Test::Methods
  
  
  

  

  
  
    Defined in:
    lib/capybara/rack_test/browser.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**current_host**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute current_host.

  

    
      
- 
  
    
      #**driver**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute driver.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**app**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**build_uri**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dom**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find**(format, selector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**follow**(method, path, **attributes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(driver)  ⇒ Browser 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Browser.

  

      
        
- 
  
    
      #**last_request**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**last_response**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process**(method, path, attributes = {}, env = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_and_follow_redirects**(method, path, attributes = {}, env = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**refresh**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset_cache!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset_host!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**submit**(method, path, attributes, content_type: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**title**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**visit**(path, **attributes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(driver)  ⇒ Browser 
  

  

  

  
    

Returns a new instance of Browser.

  

  

  
    
      

```

9
10
11
12
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 9

def initialize(driver)
  @driver = driver
  @current_fragment = nil
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**current_host**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute current_host.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 7

def current_host
  @current_host
end

```

    
  

    
      
      
      
  
### 
  
    #**driver**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute driver.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 6

def driver
  @driver
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**app**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 14

def app
  driver.app
end

```

    
  

    
      
  
### 
  
    #**build_uri**(path)  ⇒ Object 
  

  

  

  
    
      

```

84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 84

def build_uri(path)
  uri = URI.parse(path)
  base_uri = base_relative_uri_for(uri)

  uri.path = base_uri.path + uri.path unless uri.absolute? || uri.path.start_with?('/')

  if base_uri.absolute?
    base_uri.merge(uri)
  else
    uri.scheme ||= @current_scheme
    uri.host ||= @current_host
    uri.port ||= @current_port unless uri.default_port == @current_port
    uri
  end
end

```

    
  

    
      
  
### 
  
    #**current_url**  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
103
104
105
106
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 100

def current_url
  uri = build_uri(last_request.url)
  uri.fragment = @current_fragment if @current_fragment
  uri.to_s
rescue Rack::Test::Error
  ''
end

```

    
  

    
      
  
### 
  
    #**dom**  ⇒ Object 
  

  

  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 117

def dom
  @dom ||= Capybara::HTML(html)
end

```

    
  

    
      
  
### 
  
    #**find**(format, selector)  ⇒ Object 
  

  

  

  
    
      

```

121
122
123
124
125
126
127
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 121

def find(format, selector)
  if format == :css
    dom.css(selector, Capybara::RackTest::CSSHandlers.new)
  else
    dom.xpath(selector)
  end.map { |node| Capybara::RackTest::Node.new(self, node) }
end

```

    
  

    
      
  
### 
  
    #**follow**(method, path, **attributes)  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
51
52
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 48

def follow(method, path, **attributes)
  return if fragment_or_script?(path)

  process_and_follow_redirects(method, path, attributes, 'HTTP_REFERER' => referer_url)
end

```

    
  

    
      
  
### 
  
    #**html**  ⇒ Object 
  

  

  

  
    
      

```

129
130
131
132
133
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 129

def html
  last_response.body
rescue Rack::Test::Error
  ''
end

```

    
  

    
      
  
### 
  
    #**last_request**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

139
140
141
142
143
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 139

def last_request
  raise Rack::Test::Error if @new_visit_request

  super
end

```

    
  

    
      
  
### 
  
    #**last_response**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

145
146
147
148
149
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 145

def last_response
  raise Rack::Test::Error if @new_visit_request

  super
end

```

    
  

    
      
  
### 
  
    #**options**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 18

def options
  driver.options
end

```

    
  

    
      
  
### 
  
    #**process**(method, path, attributes = {}, env = {})  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
77
78
79
80
81
82
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 74

def process(method, path, attributes = {}, env = {})
  method = method.downcase
  new_uri = build_uri(path)
  @current_scheme, @current_host, @current_port = new_uri.select(:scheme, :host, :port)
  @current_fragment = new_uri.fragment || @current_fragment
  reset_cache!
  @new_visit_request = false
  send(method, new_uri.to_s, attributes, env.merge(options[:headers] || {}))
end

```

    
  

    
      
  
### 
  
    #**process_and_follow_redirects**(method, path, attributes = {}, env = {})  ⇒ Object 
  

  

  

  
    
      

```

54
55
56
57
58
59
60
61
62
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
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 54

def process_and_follow_redirects(method, path, attributes = {}, env = {})
  @current_fragment = build_uri(path).fragment
  process(method, path, attributes, env)
  return unless driver.follow_redirects?

  driver.redirect_limit.times do
    if last_response.redirect?
      if [307, 308].include? last_response.status
        process(last_request.request_method, last_response['Location'], last_request.params, env)
      else
        process(:get, last_response['Location'], {}, env)
      end
    end
  end

  if last_response.redirect? # rubocop:disable Style/GuardClause
    raise Capybara::InfiniteRedirectError, "redirected more than #{driver.redirect_limit} times, check for infinite redirects."
  end
end

```

    
  

    
      
  
### 
  
    #**refresh**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 29

def refresh
  reset_cache!
  request(last_request.fullpath, last_request.env)
end

```

    
  

    
      
  
### 
  
    #**reset_cache!**  ⇒ Object 
  

  

  

  
    
      

```

113
114
115
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 113

def reset_cache!
  @dom = nil
end

```

    
  

    
      
  
### 
  
    #**reset_host!**  ⇒ Object 
  

  

  

  
    
      

```

108
109
110
111
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 108

def reset_host!
  uri = URI.parse(driver.session_options.app_host || driver.session_options.default_host)
  @current_scheme, @current_host, @current_port = uri.select(:scheme, :host, :port)
end

```

    
  

    
      
  
### 
  
    #**submit**(method, path, attributes, content_type: nil)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 34

def submit(method, path, attributes, content_type: nil)
  path = request_path if path.nil? || path.empty?
  uri = build_uri(path)
  uri.query = '' if method.to_s.casecmp('get').zero?
  env = { 'HTTP_REFERER' => referer_url }
  env['CONTENT_TYPE'] = content_type if content_type
  process_and_follow_redirects(
    method,
    uri.to_s,
    attributes,
    env
  )
end

```

    
  

    
      
  
### 
  
    #**title**  ⇒ Object 
  

  

  

  
    
      

```

135
136
137
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 135

def title
  dom.title
end

```

    
  

    
      
  
### 
  
    #**visit**(path, **attributes)  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
25
26
27
```

    
    
      

```
# File 'lib/capybara/rack_test/browser.rb', line 22

def visit(path, **attributes)
  @new_visit_request = true
  reset_cache!
  reset_host!
  process_and_follow_redirects(:get, path, attributes)
end

```