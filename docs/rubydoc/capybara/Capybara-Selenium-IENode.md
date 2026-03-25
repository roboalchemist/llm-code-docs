# Class: Capybara::Selenium::IENode
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Driver::Node
          
            
- Node
          
            
- Capybara::Selenium::IENode
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/nodes/ie_node.rb
  
  

  
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
  
    
      #**disabled?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#[], #all_text, #click, #content_editable?, #double_click, #drag_to, #drop, #hover, #multiple?, #obscured?, #path, #readonly?, #rect, #right_click, #select_option, #selected?, #send_keys, #set, #shadow_root, #style, #tag_name, #unselect_option, #value, #visible?, #visible_text

  
  
  
  
  
  
  
  
  
### Methods included from Scroll

  

#scroll_by, #scroll_to

  
  
  
  
  
  
  
  
  
### Methods included from Find

  

#find_css, #find_xpath

  
  
  
  
  
  
  
  
  
### Methods included from Node::WhitespaceNormalizer

  

#normalize_spacing, #normalize_visible_spacing

  
  
  
  
  
  
  
  
  
### Methods inherited from Driver::Node

  

#==, #[], #all_text, #checked?, #click, #double_click, #drag_to, #drop, #hover, #initialize, #inspect, #multiple?, #obscured?, #path, #readonly?, #rect, #right_click, #scroll_by, #scroll_to, #select_option, #selected?, #send_keys, #set, #shadow_root, #style, #tag_name, #trigger, #unselect_option, #value, #visible?, #visible_text

  
## Constructor Details

  
    

This class inherits a constructor from Capybara::Driver::Node
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**disabled?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

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
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/capybara/selenium/nodes/ie_node.rb', line 6

def disabled?
  # super
  # optimize to one script call
  driver.evaluate_script "    arguments[0].msMatchesSelector('\n      :disabled,\n      select:disabled *,\n      optgroup:disabled *,\n      fieldset[disabled],\n      fieldset[disabled] > *:not(legend),\n      fieldset[disabled] > *:not(legend) *,\n      fieldset[disabled] > legend:nth-of-type(n+2),\n      fieldset[disabled] > legend:nth-of-type(n+2) *\n    ')\n  JS\nend\n".delete("\n"), self

```