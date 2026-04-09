# Class: Capybara::Node::Document
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Capybara::Node::Document
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      DocumentMatchers
  
  
  

  

  
  
    Defined in:
    lib/capybara/node/document.rb
  
  

## Overview

  
    

A Document represents an HTML document. Any operation
performed on it will be performed on the entire document.

  

  

  

See Also:
  

    
      
- Capybara::Node
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#base, #query_scope, #session

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**evaluate_script**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**execute_script**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**scroll_to**(*args, quirks: false, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**text**(type = nil, normalize_ws: false)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The text of the document.

  

      
        
- 
  
    
      #**title**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The title of the document.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from DocumentMatchers

  

#assert_no_title, #assert_title, #has_no_title?, #has_title?

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#find_css, #find_xpath, #initialize, #reload, #session_options, #synchronize, #to_capybara_node

  
  
  
  
  
  
  
  
  
### Methods included from Minitest::Expectations

  

#must_have_all_of_selectors, #must_have_ancestor, #must_have_any_of_selectors, #must_have_button, #must_have_checked_field, #must_have_content, #must_have_css, #must_have_current_path, #must_have_element, #must_have_field, #must_have_link, #must_have_none_of_selectors, #must_have_select, #must_have_selector, #must_have_sibling, #must_have_style, #must_have_table, #must_have_text, #must_have_title, #must_have_unchecked_field, #must_have_xpath, #must_match_style, #wont_have_button, #wont_have_checked_field, #wont_have_content, #wont_have_css, #wont_have_current_path, #wont_have_element, #wont_have_field, #wont_have_link, #wont_have_select, #wont_have_selector, #wont_have_table, #wont_have_text, #wont_have_title, #wont_have_unchecked_field, #wont_have_xpath

  
  
  
  
  
  
  
  
  
### Methods included from Matchers

  

#==, #assert_all_of_selectors, #assert_ancestor, #assert_any_of_selectors, #assert_matches_selector, #assert_matches_style, #assert_no_ancestor, #assert_no_selector, #assert_no_sibling, #assert_no_text, #assert_none_of_selectors, #assert_not_matches_selector, #assert_selector, #assert_sibling, #assert_style, #assert_text, #has_ancestor?, #has_button?, #has_checked_field?, #has_css?, #has_element?, #has_field?, #has_link?, #has_no_ancestor?, #has_no_button?, #has_no_checked_field?, #has_no_css?, #has_no_element?, #has_no_field?, #has_no_link?, #has_no_select?, #has_no_selector?, #has_no_sibling?, #has_no_table?, #has_no_text?, #has_no_unchecked_field?, #has_no_xpath?, #has_select?, #has_selector?, #has_sibling?, #has_style?, #has_table?, #has_text?, #has_unchecked_field?, #has_xpath?, #matches_css?, #matches_selector?, #matches_style?, #matches_xpath?, #not_matches_css?, #not_matches_selector?, #not_matches_xpath?

  
  
  
  
  
  
  
  
  
### Methods included from Actions

  

#attach_file, #check, #choose, #click_button, #click_link, #click_link_or_button, #fill_in, #select, #uncheck, #unselect

  
  
  
  
  
  
  
  
  
### Methods included from Finders

  

#all, #ancestor, #find, #find_button, #find_by_id, #find_field, #find_link, #first, #sibling

  
## Constructor Details

  
    

This class inherits a constructor from Capybara::Node::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**evaluate_script**(*args)  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/capybara/node/document.rb', line 39

def evaluate_script(*args)
  find(:xpath, '/html').evaluate_script(*args)
end

```

    
  

    
      
  
### 
  
    #**execute_script**(*args)  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/capybara/node/document.rb', line 35

def execute_script(*args)
  find(:xpath, '/html').execute_script(*args)
end

```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/capybara/node/document.rb', line 15

def inspect
  %(#<Capybara::Document>)
end

```

    
  

    
      
  
### 
  
    #**scroll_to**(*args, quirks: false, **options)  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/capybara/node/document.rb', line 43

def scroll_to(*args, quirks: false, **options)
  find(:xpath, quirks ? '//body' : '/html').scroll_to(*args, **options)
end

```

    
  

    
      
  
### 
  
    #**text**(type = nil, normalize_ws: false)  ⇒ String 
  

  

  

  
    

Returns The text of the document.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The text of the document

      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/capybara/node/document.rb', line 23

def text(type = nil, normalize_ws: false)
  find(:xpath, '/html').text(type, normalize_ws: normalize_ws)
end

```

    
  

    
      
  
### 
  
    #**title**  ⇒ String 
  

  

  

  
    

Returns The title of the document.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The title of the document

      
    
  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/capybara/node/document.rb', line 31

def title
  session.driver.title
end

```