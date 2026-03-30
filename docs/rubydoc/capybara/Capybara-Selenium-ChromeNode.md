# Class: Capybara::Selenium::ChromeNode
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Driver::Node
          
            
- Node
          
            
- Capybara::Selenium::ChromeNode
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      FileInputClickEmulation, Html5Drag
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/nodes/chrome_node.rb
  
  

  
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
  
    
      #**click**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**disabled?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**drop**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**select_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_keys**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**set_file**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

rubocop:disable Naming/AccessorMethodName.

  

      
        
- 
  
    
      #**set_text**(value, clear: nil, **_unused)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**visible?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#[], #all_text, #content_editable?, #double_click, #drag_to, #hover, #multiple?, #obscured?, #path, #readonly?, #rect, #right_click, #selected?, #set, #shadow_root, #style, #tag_name, #unselect_option, #value, #visible_text

  
  
  
  
  
  
  
  
  
### Methods included from Scroll

  

#scroll_by, #scroll_to

  
  
  
  
  
  
  
  
  
### Methods included from Find

  

#find_css, #find_xpath

  
  
  
  
  
  
  
  
  
### Methods included from Node::WhitespaceNormalizer

  

#normalize_spacing, #normalize_visible_spacing

  
  
  
  
  
  
  
  
  
### Methods inherited from Driver::Node

  

#==, #[], #all_text, #checked?, #double_click, #drag_to, #hover, #initialize, #inspect, #multiple?, #obscured?, #path, #readonly?, #rect, #right_click, #scroll_by, #scroll_to, #selected?, #set, #shadow_root, #style, #tag_name, #trigger, #unselect_option, #value, #visible_text

  
## Constructor Details

  
    

This class inherits a constructor from Capybara::Driver::Node
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**click**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 33

def click(*, **)
  super
rescue ::Selenium::WebDriver::Error::ElementClickInterceptedError
  raise
rescue ::Selenium::WebDriver::Error::WebDriverError => e
  # chromedriver 74 (at least on mac) raises the wrong error for this
  if e.message.include?('element click intercepted')
    raise ::Selenium::WebDriver::Error::ElementClickInterceptedError, e.message
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

46
47
48
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 46

def disabled?
  driver.evaluate_script("arguments[0].matches(':disabled, select:disabled *')", self)
end
```

    
  

    
      
  
### 
  
    #**drop**(*args)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 29

def drop(*args)
  html5_drop(*args)
end
```

    
  

    
      
  
### 
  
    #**select_option**  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
53
54
55
56
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 50

def select_option
  # To optimize to only one check and then click
  selected_or_disabled = driver.evaluate_script(<<~JS, self)
    arguments[0].matches(':disabled, select:disabled *, :checked')
  JS
  click unless selected_or_disabled
end
```

    
  

    
      
  
### 
  
    #**send_keys**(*args)  ⇒ Object 
  

  

  

  
    
      

```

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
82
83
84
85
86
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 70

def send_keys(*args)
  args.chunk { |inp| inp.is_a?(String) && inp.match?(/\p{Emoji Presentation}/) }
      .each do |contains_emoji, inputs|
    if contains_emoji
      inputs.join.grapheme_clusters.chunk { |gc| gc.match?(/\p{Emoji Presentation}/) }
            .each do |emoji, clusters|
        if emoji
          driver.send(:execute_cdp, 'Input.insertText', text: clusters.join)
        else
          super(clusters.join)
        end
      end
    else
      super(*inputs)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**set_file**(value)  ⇒ Object 
  

  

  

  
    

rubocop:disable Naming/AccessorMethodName

  

  

  
    
      

```

17
18
19
20
21
22
23
24
25
26
27
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 17

def set_file(value) # rubocop:disable Naming/AccessorMethodName
  # In Chrome 75+ files are appended (due to WebDriver spec - why?) so we have to clear here if its multiple and already set
  if browser_version >= 75.0
    driver.execute_script(<<~JS, self)
      if (arguments[0].multiple && arguments[0].files.length){
        arguments[0].value = null;
      }
    JS
  end
  super
end
```

    
  

    
      
  
### 
  
    #**set_text**(value, clear: nil, **_unused)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
13
14
15
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 10

def set_text(value, clear: nil, **_unused)
  super.tap do
    # React doesn't see the chromedriver element clear
    send_keys(:space, :backspace) if value.to_s.empty? && clear.nil?
  end
end
```

    
  

    
      
  
### 
  
    #**visible?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/chrome_node.rb', line 58

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