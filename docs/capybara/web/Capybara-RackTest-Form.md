# Class: Capybara::RackTest::Form
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Driver::Node
          
            
- Node
          
            
- Capybara::RackTest::Form
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rack_test/form.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** NilUploadedFile, ParamsHash
    
  

  
## Constant Summary

  
  
### Constants inherited
     from Node

  

Node::BLOCK_ELEMENTS

  
  
  
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
  
    
      #**multipart?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**params**(button)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**submit**(button)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#[], #all_text, #checked?, #click, #disabled?, #find_css, #find_xpath, #path, #readonly?, #select_option, #selected?, #set, #style, #tag_name, #unselect_option, #value, #visible?, #visible_text

  
  
  
  
  
  
  
  
  
### Methods included from Node::WhitespaceNormalizer

  

#normalize_spacing, #normalize_visible_spacing

  
  
  
  
  
  
  
  
  
### Methods inherited from Driver::Node

  

#==, #[], #all_text, #checked?, #click, #disabled?, #double_click, #drag_to, #drop, #hover, #initialize, #inspect, #multiple?, #obscured?, #path, #readonly?, #rect, #right_click, #scroll_by, #scroll_to, #select_option, #selected?, #send_keys, #set, #shadow_root, #style, #tag_name, #trigger, #unselect_option, #value, #visible?, #visible_text

  
## Constructor Details

  
    

This class inherits a constructor from Capybara::Driver::Node
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**multipart?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/capybara/rack_test/form.rb', line 60

def multipart?
  self[:enctype] == 'multipart/form-data'
end
```

    
  

    
      
  
### 
  
    #**params**(button)  ⇒ Object 
  

  

  

  
    
      

```

23
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
47
48
49
50
51
52
```

    
    
      

```
# File 'lib/capybara/rack_test/form.rb', line 23

def params(button)
  form_element_types = %i[input select textarea button]
  form_elements_xpath = XPath.generate do |xp|
    xpath = xp.descendant(*form_element_types).where(!xp.attr(:form))
    xpath += xp.anywhere(*form_element_types).where(xp.attr(:form) == native[:id]) if native[:id]
    xpath.where(!xp.attr(:disabled))
  end.to_s

  form_elements = native.xpath(form_elements_xpath).reject { |el| submitter?(el) && (el != button.native) }

  form_params = form_elements.each_with_object({}.compare_by_identity) do |field, params|
    case field.name
    when 'input', 'button' then add_input_param(field, params)
    when 'select' then add_select_param(field, params)
    when 'textarea' then add_textarea_param(field, params)
    end
  end

  form_params.each_with_object(make_params) do |(name, value), params|
    merge_param!(params, name, value)
  end.to_params_hash

  # form_elements.each_with_object(make_params) do |field, params|
  #   case field.name
  #   when 'input', 'button' then add_input_param(field, params)
  #   when 'select' then add_select_param(field, params)
  #   when 'textarea' then add_textarea_param(field, params)
  #   end
  # end.to_params_hash
end
```

    
  

    
      
  
### 
  
    #**submit**(button)  ⇒ Object 
  

  

  

  
    
      

```

54
55
56
57
58
```

    
    
      

```
# File 'lib/capybara/rack_test/form.rb', line 54

def submit(button)
  action = button&.[]('formaction') || native['action']
  method = button&.[]('formmethod') || request_method
  driver.submit(method, action.to_s, params(button), content_type: native['enctype'])
end
```