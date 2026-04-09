# Module: Capybara::Node::DocumentMatchers
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Document, Simple
  
  

  
  
    Defined in:
    lib/capybara/node/document_matchers.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**assert_no_title**(title, **options)  ⇒ true 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the page doesn't have the given title.

  

      
        
- 
  
    
      #**assert_title**(title, **options)  ⇒ true 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the page has the given title.

  

      
        
- 
  
    
      #**has_no_title?**(title, **options)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Checks if the page doesn't have the given title.

  

      
        
- 
  
    
      #**has_title?**(title, **options)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Checks if the page has the given title.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**assert_no_title**(string, **options)  ⇒ true 
    
      #**assert_no_title**(regexp, **options)  ⇒ true 
    
  

  

  

  
    

Asserts that the page doesn't have the given title.

  

  
  

Overloads:
  

    
      
      
- 
        #**assert_no_title**(string, **options)  ⇒ true 
        
  
    

  

  

Parameters:

  
    
  - 
      
        string
      
      
        (String)
      
      
      
        —
        

The string that title should include

      
    
  

      
    
      
      
- 
        #**assert_no_title**(regexp, **options)  ⇒ true 
        
  
    

  

  

Parameters:

  
    
  - 
      
        regexp
      
      
        (Regexp)
      
      
      
        —
        

The regexp that title should match to

      
    
  

      
    
  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :wait
          (Numeric)
          
            
              — default:
              Capybara.default_max_wait_time
            
          
          
            — 

Maximum time that Capybara will wait for title to eq/match given string/regexp argument

          
        
      
        
- 
          :exact
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

When passed a string should the match be exact or just substring

          
        
      
    

  

Returns:

  
    
- 
      
      
        (true)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (Capybara::ExpectationNotMet)
      
      
      
        —
        

if the assertion hasn't succeeded during wait time

      
    
  

  
    
      

```

32
33
34
35
36
```

    
    
      

```
# File 'lib/capybara/node/document_matchers.rb', line 32

def assert_no_title(title, **options)
  _verify_title(title, options) do |query|
    raise Capybara::ExpectationNotMet, query.negative_failure_message if query.resolves_for?(self)
  end
end
```

    
  

    
      
  
### 
  
    
      #**assert_title**(string, **options)  ⇒ true 
    
      #**assert_title**(regexp, **options)  ⇒ true 
    
  

  

  

  
    

Asserts that the page has the given title.

  

  
  

Overloads:
  

    
      
      
- 
        #**assert_title**(string, **options)  ⇒ true 
        
  
    

  

  

Parameters:

  
    
  - 
      
        string
      
      
        (String)
      
      
      
        —
        

The string that title should include

      
    
  

      
    
      
      
- 
        #**assert_title**(regexp, **options)  ⇒ true 
        
  
    

  

  

Parameters:

  
    
  - 
      
        regexp
      
      
        (Regexp)
      
      
      
        —
        

The regexp that title should match to

      
    
  

      
    
  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :wait
          (Numeric)
          
            
              — default:
              Capybara.default_max_wait_time
            
          
          
            — 

Maximum time that Capybara will wait for title to eq/match given string/regexp argument

          
        
      
        
- 
          :exact
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

When passed a string should the match be exact or just substring

          
        
      
    

  

Returns:

  
    
- 
      
      
        (true)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (Capybara::ExpectationNotMet)
      
      
      
        —
        

if the assertion hasn't succeeded during wait time

      
    
  

  
    
      

```

19
20
21
22
23
```

    
    
      

```
# File 'lib/capybara/node/document_matchers.rb', line 19

def assert_title(title, **options)
  _verify_title(title, options) do |query|
    raise Capybara::ExpectationNotMet, query.failure_message unless query.resolves_for?(self)
  end
end
```

    
  

    
      
  
### 
  
    
      #**has_no_title?**(string, **options)  ⇒ Boolean 
    
      #**has_no_title?**(regexp, **options)  ⇒ Boolean 
    
  

  

  

  
    

Checks if the page doesn't have the given title.

  

  
  

Overloads:
  

    
      
      
- 
        #**has_no_title?**(string, **options)  ⇒ Boolean 
        
  
    

  

  

Parameters:

  
    
  - 
      
        string
      
      
        (String)
      
      
      
        —
        

The string that title should include

      
    
  

      
    
      
      
- 
        #**has_no_title?**(regexp, **options)  ⇒ Boolean 
        
  
    

  

  

Parameters:

  
    
  - 
      
        regexp
      
      
        (Regexp)
      
      
      
        —
        

The regexp that title should match to

      
    
  

      
    
  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :wait
          (Numeric)
          
            
              — default:
              Capybara.default_max_wait_time
            
          
          
            — 

Maximum time that Capybara will wait for title to eq/match given string/regexp argument

          
        
      
        
- 
          :exact
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

When passed a string should the match be exact or just substring

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/capybara/node/document_matchers.rb', line 54

def has_no_title?(title, **options)
  make_predicate(options) { assert_no_title(title, **options) }
end
```

    
  

    
      
  
### 
  
    
      #**has_title?**(string, **options)  ⇒ Boolean 
    
      #**has_title?**(regexp, **options)  ⇒ Boolean 
    
  

  

  

  
    

Checks if the page has the given title.

  

  
  

Overloads:
  

    
      
      
- 
        #**has_title?**(string, **options)  ⇒ Boolean 
        
  
    

  

  

Parameters:

  
    
  - 
      
        string
      
      
        (String)
      
      
      
        —
        

The string that title should include

      
    
  

      
    
      
      
- 
        #**has_title?**(regexp, **options)  ⇒ Boolean 
        
  
    

  

  

Parameters:

  
    
  - 
      
        regexp
      
      
        (Regexp)
      
      
      
        —
        

The regexp that title should match to

      
    
  

      
    
  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :wait
          (Numeric)
          
            
              — default:
              Capybara.default_max_wait_time
            
          
          
            — 

Maximum time that Capybara will wait for title to eq/match given string/regexp argument

          
        
      
        
- 
          :exact
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

When passed a string should the match be exact or just substring

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara/node/document_matchers.rb', line 44

def has_title?(title, **options)
  make_predicate(options) { assert_title(title, **options) }
end
```