# Class: Capybara::Selenium::FirefoxNode
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Driver::Node
          
            
- Node
          
            
- Capybara::Selenium::FirefoxNode
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      FileInputClickEmulation, Html5Drag
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/nodes/firefox_node.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Node::WhitespaceNormalizer

  

Node::WhitespaceNormalizer::BREAKING_SPACES, Node::WhitespaceNormalizer::EMPTY_LINES, Node::WhitespaceNormalizer::LEADING_SPACES, Node::WhitespaceNormalizer::LEFT_TO_RIGHT_MARK, Node::WhitespaceNormalizer::LINE_SEPERATOR, Node::WhitespaceNormalizer::NON_BREAKING_SPACE, Node::WhitespaceNormalizer::PARAGRAPH_SEPERATOR, Node::WhitespaceNormalizer::REMOVED_CHARACTERS, Node::WhitespaceNormalizer::RIGHT_TO_LEFT_MARK, Node::WhitespaceNormalizer::SQUEEZED_SPACES, Node::WhitespaceNormalizer::TRAILING_SPACES, Node::WhitespaceNormalizer::ZERO_WIDTH_SPACE

  
## Instance Attribute Summary

  
  
### Attributes inherited from Driver::Node

  

#driver, #initial_cache, #native

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**click**(keys = [], **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**disabled?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**drop**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**focused?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hover**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**select_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_keys**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**set_file**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

rubocop:disable Naming/AccessorMethodName.

  

      
        
- 
  
    
      #**visible?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#[], #all_text, #content_editable?, #double_click, #drag_to, #multiple?, #obscured?, #path, #readonly?, #rect, #right_click, #selected?, #set, #shadow_root, #style, #tag_name, #unselect_option, #value, #visible_text

  
  
  
  
  
  
  
  
  
### Methods included from Scroll

  

#scroll_by, #scroll_to

  
  
  
  
  
  
  
  
  
### Methods included from Find

  

#find_css, #find_xpath

  
  
  
  
  
  
  
  
  
### Methods included from Node::WhitespaceNormalizer

  

#normalize_spacing, #normalize_visible_spacing

  
  
  
  
  
  
  
  
  
### Methods inherited from Driver::Node

  

#==, #[], #all_text, #checked?, #double_click, #drag_to, #initialize, #inspect, #multiple?, #obscured?, #path, #readonly?, #rect, #right_click, #scroll_by, #scroll_to, #selected?, #set, #shadow_root, #style, #tag_name, #trigger, #unselect_option, #value, #visible_text

  
## Constructor Details

  
    

This class inherits a constructor from Capybara::Driver::Node
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**click**(keys = [], **options)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
13
14
15
16
17
18
19
20
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 10

def click(keys = [], **options)
  super
rescue ::Selenium::WebDriver::Error::ElementNotInteractableError
  if tag_name == 'tr'
    warn 'You are attempting to click a table row which has issues in geckodriver/marionette - ' \
         'see https://github.com/mozilla/geckodriver/issues/1228 - Your test should probably be ' \
         'clicking on a table cell like a user would. Clicking the first cell in the row instead.'
    return find_css('th:first-child,td:first-child')[0].click(keys, **options)
  end
  raise
end

```

    
  

    
      
  
### 
  
    #**disabled?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 22

def disabled?
  driver.evaluate_script("arguments[0].matches(':disabled, select:disabled *')", self)
end

```

    
  

    
      
  
### 
  
    #**drop**(*args)  ⇒ Object 
  

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 56

def drop(*args)
  html5_drop(*args)
end

```

    
  

    
      
  
### 
  
    #**focused?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 43

def focused?
  driver.evaluate_script('arguments[0] == document.activeElement', self)
end

```

    
  

    
      
  
### 
  
    #**hover**  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 60

def hover
  return super unless browser_version >= 65.0

  # work around issue 2156 - https://github.com/teamcapybara/capybara/issues/2156
  scroll_if_needed { browser_action.move_to(native, 0, 0).move_to(native).perform }
end

```

    
  

    
      
  
### 
  
    #**select_option**  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
70
71
72
73
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 67

def select_option
  # To optimize to only one check and then click
  selected_or_disabled = driver.evaluate_script("    arguments[0].matches(':disabled, select:disabled *, :checked')\n  JS\n  click unless selected_or_disabled\nend\n", self)

```

    
  

    
      
  
### 
  
    #**send_keys**(*args)  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
50
51
52
53
54
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 47

def send_keys(*args)
  # https://github.com/mozilla/geckodriver/issues/846
  return super(*args.map { |arg| arg == :space ? ' ' : arg }) if args.none?(Array)

  native.click unless focused?

  _send_keys(args).perform
end

```

    
  

    
      
  
### 
  
    #**set_file**(value)  ⇒ Object 
  

  

  

  
    

rubocop:disable Naming/AccessorMethodName

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 26

def set_file(value) # rubocop:disable Naming/AccessorMethodName
  # By default files are appended so we have to clear here if its multiple and already set
  driver.execute_script("    if (arguments[0].multiple && arguments[0].files.length){\n      arguments[0].value = null;\n    }\n  JS\n  return super if browser_version >= 62.0\n\n  # Workaround lack of support for multiple upload by uploading one at a time\n  path_names = value.to_s.empty? ? [] : Array(value)\n  if (fd = bridge.file_detector) && !driver.browser.respond_to?(:upload)\n    path_names.map! { |path| upload(fd.call([path])) || path }\n  end\n  path_names.each { |path| native.send_keys(path) }\nend\n", self)

```

    
  

    
      
  
### 
  
    #**visible?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

75
76
77
78
79
80
81
82
83
84
85
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/firefox_node.rb', line 75

def visible?
  return super unless native_displayed?

  begin
    bridge.send(:execute, :is_element_displayed, id: native_id)
  rescue Selenium::WebDriver::Error::UnknownCommandError
    # If the is_element_displayed command is unknown, no point in trying again
    driver.options[:native_displayed] = false
    super
  end
end

```