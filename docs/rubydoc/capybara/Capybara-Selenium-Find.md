# Module: Capybara::Selenium::Find
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Driver, Node
  
  

  
  
    Defined in:
    lib/capybara/selenium/extensions/find.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find_css**(selector, uses_visibility: false, texts: [], styles: nil, position: false, **_options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_xpath**(selector, uses_visibility: false, styles: nil, position: false, **_options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find_css**(selector, uses_visibility: false, texts: [], styles: nil, position: false, **_options)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/capybara/selenium/extensions/find.rb', line 10

def find_css(selector, uses_visibility: false, texts: [], styles: nil, position: false, **_options)
  find_by(:css, selector, uses_visibility: uses_visibility, texts: texts, styles: styles, position: position)
end

```

    
  

    
      
  
### 
  
    #**find_xpath**(selector, uses_visibility: false, styles: nil, position: false, **_options)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/capybara/selenium/extensions/find.rb', line 6

def find_xpath(selector, uses_visibility: false, styles: nil, position: false, **_options)
  find_by(:xpath, selector, uses_visibility: uses_visibility, texts: [], styles: styles, position: position)
end

```