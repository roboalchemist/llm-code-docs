# Module: Capybara::DSL
  
  
  

  

  
  
  
  
  
      Includes:
      DSLRSpecProxyInstaller
  
  
  

  
  
    Included in:
    Capybara
  
  

  
  
    Defined in:
    lib/capybara/rspec/matcher_proxies.rb,

  lib/capybara/dsl.rb

  
  

## Overview

  
    

:nocov:

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**extended**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**included**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**page**  ⇒ Capybara::Session 
    

    
  
  
  
  
  
  
  
  

  
    

Shortcut to accessing the current session.

  

      
        
- 
  
    
      #**using_session**(name_or_session, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Shortcut to working in a different session.

  

      
        
- 
  
    
      #**using_wait_time**(seconds, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Shortcut to using a different wait time.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from DSLRSpecProxyInstaller

  

prepended

  
    
## Class Method Details

    
      
  
### 
  
    .**extended**(base)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/capybara/dsl.rb', line 12

def self.extended(base)
  warn 'extending the main object with Capybara::DSL is not recommended!' if base == TOPLEVEL_BINDING.eval('self')
  super
end

```

    
  

    
      
  
### 
  
    .**included**(base)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/capybara/dsl.rb', line 7

def self.included(base)
  warn 'including Capybara::DSL in the global scope is not recommended!' if base == Object
  super
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**page**  ⇒ Capybara::Session 
  

  

  

  
    

Shortcut to accessing the current session.

```
class MyClass
  include Capybara::DSL

  def has_header?
    page.has_css?('h1')
  end
end

```

  

  

Returns:

  
    
- 
      
      
        (Capybara::Session)
      
      
      
        —
        

The current session object

      
    
  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/capybara/dsl.rb', line 45

def page
  Capybara.current_session
end

```

    
  

    
      
  
### 
  
    #**using_session**(name_or_session, &block)  ⇒ Object 
  

  

  

  
    

Shortcut to working in a different session.

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/capybara/dsl.rb', line 21

def using_session(name_or_session, &block)
  Capybara.using_session(name_or_session, &block)
end

```

    
  

    
      
  
### 
  
    #**using_wait_time**(seconds, &block)  ⇒ Object 
  

  

  

  
    

Shortcut to using a different wait time.

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/capybara/dsl.rb', line 27

def using_wait_time(seconds, &block)
  page.using_wait_time(seconds, &block)
end

```