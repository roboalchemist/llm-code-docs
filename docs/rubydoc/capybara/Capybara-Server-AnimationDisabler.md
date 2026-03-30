# Class: Capybara::Server::AnimationDisabler
  
  
  Private

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Server::AnimationDisabler
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/server/animation_disabler.rb
  
  

  
    

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**selector_for**(css_or_bool)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**call**(env)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**initialize**(app)  ⇒ AnimationDisabler 
    

    
  
  
  
    constructor
  
  
  
  
  
  private

  
    

A new instance of AnimationDisabler.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(app)  ⇒ AnimationDisabler 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of AnimationDisabler.

  

  

  
    
      

```

17
18
19
20
21
22
```

    
    
      

```
# File 'lib/capybara/server/animation_disabler.rb', line 17

def initialize(app)
  @app = app
  @disable_css_markup = format(DISABLE_CSS_MARKUP_TEMPLATE,
                               selector: self.class.selector_for(Capybara.disable_animation))
  @disable_js_markup = +DISABLE_JS_MARKUP_TEMPLATE
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**selector_for**(css_or_bool)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

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
15
```

    
    
      

```
# File 'lib/capybara/server/animation_disabler.rb', line 6

def self.selector_for(css_or_bool)
  case css_or_bool
  when String
    css_or_bool
  when true
    '*'
  else
    raise CapybaraError, 'Capybara.disable_animation supports either a String (the css selector to disable) or a boolean'
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**call**(env)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/server/animation_disabler.rb', line 24

def call(env)
  status, headers, body = @app.call(env)
  return [status, headers, body] unless html_content?(headers)

  nonces = directive_nonces(headers).transform_values { |nonce| "nonce=\"#{nonce}\"" if nonce && !nonce.empty? }
  response = Rack::Response.new([], status, headers)

  body.each { |html| response.write insert_disable(html, nonces) }
  body.close if body.respond_to?(:close)

  response.finish
end
```