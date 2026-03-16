# Class: Capybara::Driver::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Driver::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/driver/base.rb
  
  

  
## Direct Known Subclasses

  

RackTest::Driver, Selenium::Driver

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**session**  ⇒ Object 
    

    
  
  
  
  
    
    
      writeonly
    
  
  
  
  
  

  
    

Sets the attribute session.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**accept_modal**(type, **options, &blk)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Execute the block, and then accept the modal opened.

  

      
        
- 
  
    
      #**active_element**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**close_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_window_handle**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dismiss_modal**(type, **options, &blk)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Execute the block, and then dismiss the modal opened.

  

      
        
- 
  
    
      #**evaluate_async_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**evaluate_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**execute_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_css**(query, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_xpath**(query, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**frame_title**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**frame_url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fullscreen_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**go_back**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**go_forward**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**invalid_element_errors**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**maximize_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**needs_server?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**no_such_window_error**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**open_new_window**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**refresh**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**resize_window_to**(handle, width, height)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**response_headers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**save_screenshot**(path, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_keys**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**session_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**status_code**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**switch_to_frame**(frame)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**switch_to_window**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**visit**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wait?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**window_handles**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**window_size**(handle)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**session=**(value)  ⇒ Object 
  

  

  

  
    

Sets the attribute session

  

  

Parameters:

  
    
- 
      
        value
      
      
        
      
      
      
        —
        

the value to set the attribute session to.

      
    
  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 4

def session=(value)
  @session = value
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**accept_modal**(type, **options, &blk)  ⇒ String 
  

  

  

  
    

Execute the block, and then accept the modal opened.

  

  

Parameters:

  
    
- 
      
        type
      
      
        (:alert, :confirm, :prompt)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :wait
          (Numeric)
          
            
          
          
            — 

How long to wait for the modal to appear after executing the block.

          
        
      
        
- 
          :text
          (String, Regexp)
          
            
          
          
            — 

Text to verify is in the message shown in the modal

          
        
      
        
- 
          :with
          (String)
          
            
          
          
            — 

Text to fill in in the case of a prompt

          
        
      
    

  
    
    

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

the message shown in the modal

      
    
  

Raises:

  
    
- 
      
      
        (Capybara::ModalNotFound)
      
      
      
        —
        

if modal dialog hasn't been found

      
    
  

  
    
      

```

138
139
140
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 138

def accept_modal(type, **options, &blk)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#accept_modal'
end

```

    
  

    
      
  
### 
  
    #**active_element**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 66

def active_element
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#active_element'
end

```

    
  

    
      
  
### 
  
    #**close_window**(handle)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

108
109
110
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 108

def close_window(handle)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#close_window'
end

```

    
  

    
      
  
### 
  
    #**current_url**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 6

def current_url
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**current_window_handle**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

88
89
90
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 88

def current_window_handle
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#current_window_handle'
end

```

    
  

    
      
  
### 
  
    #**dismiss_modal**(type, **options, &blk)  ⇒ String 
  

  

  

  
    

Execute the block, and then dismiss the modal opened.

  

  

Parameters:

  
    
- 
      
        type
      
      
        (:alert, :confirm, :prompt)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :wait
          (Numeric)
          
            
          
          
            — 

How long to wait for the modal to appear after executing the block.

          
        
      
        
- 
          :text
          (String, Regexp)
          
            
          
          
            — 

Text to verify is in the message shown in the modal

          
        
      
    

  
    
    

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

the message shown in the modal

      
    
  

Raises:

  
    
- 
      
      
        (Capybara::ModalNotFound)
      
      
      
        —
        

if modal dialog hasn't been found

      
    
  

  
    
      

```

151
152
153
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 151

def dismiss_modal(type, **options, &blk)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#dismiss_modal'
end

```

    
  

    
      
  
### 
  
    #**evaluate_async_script**(script, *args)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 46

def evaluate_async_script(script, *args)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#evaluate_script_asnyc'
end

```

    
  

    
      
  
### 
  
    #**evaluate_script**(script, *args)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 42

def evaluate_script(script, *args)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#evaluate_script'
end

```

    
  

    
      
  
### 
  
    #**execute_script**(script, *args)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 38

def execute_script(script, *args)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#execute_script'
end

```

    
  

    
      
  
### 
  
    #**find_css**(query, **options)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 22

def find_css(query, **options)
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**find_xpath**(query, **options)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 18

def find_xpath(query, **options)
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**frame_title**  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 78

def frame_title
  find_xpath('/html/head/title').map(&:all_text).first.to_s
end

```

    
  

    
      
  
### 
  
    #**frame_url**  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
85
86
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 82

def frame_url
  evaluate_script('document.location.href')
rescue Capybara::NotSupportedByDriverError
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#frame_title'
end

```

    
  

    
      
  
### 
  
    #**fullscreen_window**(handle)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

104
105
106
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 104

def fullscreen_window(handle)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#fullscreen_window'
end

```

    
  

    
      
  
### 
  
    #**go_back**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 30

def go_back
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#go_back'
end

```

    
  

    
      
  
### 
  
    #**go_forward**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 34

def go_forward
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#go_forward'
end

```

    
  

    
      
  
### 
  
    #**html**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 26

def html
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**invalid_element_errors**  ⇒ Object 
  

  

  

  
    
      

```

155
156
157
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 155

def invalid_element_errors
  []
end

```

    
  

    
      
  
### 
  
    #**maximize_window**(handle)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 100

def maximize_window(handle)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#maximize_window'
end

```

    
  

    
      
  
### 
  
    #**needs_server?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

165
166
167
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 165

def needs_server?
  false
end

```

    
  

    
      
  
### 
  
    #**no_such_window_error**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 124

def no_such_window_error
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#no_such_window_error'
end

```

    
  

    
      
  
### 
  
    #**open_new_window**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

116
117
118
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 116

def open_new_window
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#open_new_window'
end

```

    
  

    
      
  
### 
  
    #**refresh**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 14

def refresh
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**reset!**  ⇒ Object 
  

  

  

  
    
      

```

163
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 163

def reset!; end

```

    
  

    
      
  
### 
  
    #**resize_window_to**(handle, width, height)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

96
97
98
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 96

def resize_window_to(handle, width, height)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#resize_window_to'
end

```

    
  

    
      
  
### 
  
    #**response_headers**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 54

def response_headers
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#response_headers'
end

```

    
  

    
      
  
### 
  
    #**save_screenshot**(path, **options)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 50

def save_screenshot(path, **options)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#save_screenshot'
end

```

    
  

    
      
  
### 
  
    #**send_keys**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 62

def send_keys(*)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#send_keys'
end

```

    
  

    
      
  
### 
  
    #**session_options**  ⇒ Object 
  

  

  

  
    
      

```

169
170
171
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 169

def session_options
  session&.config || Capybara.session_options
end

```

    
  

    
      
  
### 
  
    #**status_code**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 58

def status_code
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#status_code'
end

```

    
  

    
      
  
### 
  
    #**switch_to_frame**(frame)  ⇒ Object 
  

  

  

  
    

  

  

Parameters:

  
    
- 
      
        frame
      
      
        (Capybara::Node::Element, :parent, :top)
      
      
      
        —
        

The iframe element to switch to

      
    
  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 74

def switch_to_frame(frame)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#switch_to_frame'
end

```

    
  

    
      
  
### 
  
    #**switch_to_window**(handle)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

120
121
122
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 120

def switch_to_window(handle)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#switch_to_window'
end

```

    
  

    
      
  
### 
  
    #**visit**(path)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 10

def visit(path)
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**wait?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

159
160
161
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 159

def wait?
  false
end

```

    
  

    
      
  
### 
  
    #**window_handles**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

112
113
114
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 112

def window_handles
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#window_handles'
end

```

    
  

    
      
  
### 
  
    #**window_size**(handle)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Capybara::NotSupportedByDriverError)
      
      
      
    
  

  
    
      

```

92
93
94
```

    
    
      

```
# File 'lib/capybara/driver/base.rb', line 92

def window_size(handle)
  raise Capybara::NotSupportedByDriverError, 'Capybara::Driver::Base#window_size'
end

```