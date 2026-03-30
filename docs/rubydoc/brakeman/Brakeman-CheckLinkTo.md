# Class: Brakeman::CheckLinkTo
  
  
  

  
  
    Inherits:
    
      CheckCrossSiteScripting
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- CheckCrossSiteScripting
          
            
- Brakeman::CheckLinkTo
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_link_to.rb
  
  

## Overview

  
    

Checks for calls to link_to in versions of Ruby where link_to did not escape the first argument.

See rails.lighthouseapp.com/projects/8994/tickets/3518-link_to-doesnt-escape-its-input

  

  

  
## Direct Known Subclasses

  

CheckLinkToHref

  
## Constant Summary

  
  
### Constants inherited
     from CheckCrossSiteScripting

  

Brakeman::CheckCrossSiteScripting::CGI, Brakeman::CheckCrossSiteScripting::FORM_BUILDER, Brakeman::CheckCrossSiteScripting::HAML_HELPERS, Brakeman::CheckCrossSiteScripting::IGNORE_LIKE, Brakeman::CheckCrossSiteScripting::IGNORE_MODEL_METHODS, Brakeman::CheckCrossSiteScripting::MODEL_METHODS, Brakeman::CheckCrossSiteScripting::URI, Brakeman::CheckCrossSiteScripting::XML_HELPER

  
  
  
### Constants inherited
     from BaseCheck

  

BaseCheck::CONFIDENCE

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Instance Attribute Summary

  
  
### Attributes inherited from BaseCheck

  

#tracker, #warnings

  
  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**actually_process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_argument**(result, exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check the argument for possible xss exploits.

  

      
        
- 
  
    
      #**check_matched**(result, matched = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check if we should warn about the matched result.

  

      
        
- 
  
    
      #**check_method**(result, argument)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check if we should warn about the specified method.

  

      
        
- 
  
    
      #**check_user_input**(result, argument)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check we should warn about the user input.

  

      
        
- 
  
    
      #**process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warn_xss**(result, message, user_input, confidence)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a warn for this xss.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from CheckCrossSiteScripting

  

#cgi_escaped?, #check_for_immediate_xss, #form_builder_method?, #haml_escaped?, #html_safe_call?, #ignore_call?, #ignored_method?, #ignored_model_method?, #initialize, #likely_model_attribute?, #process_case, #process_cookies, #process_dstr, #process_escaped_output, #process_format, #process_format_escaped, #process_if, #process_output, #process_params, #process_render, #raw_call?, #safe_input_attribute?, #setup, #xml_escaped?

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #initialize, #process, processors, #scope

  
## Constructor Details

  
    

This class inherits a constructor from Brakeman::CheckCrossSiteScripting
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**actually_process_call**(exp)  ⇒ Object 
  

  

  

  
    
      

```

120
121
122
123
124
125
126
127
128
129
130
131
132
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 120

def actually_process_call exp
  return if @matched

  target = exp.target
  target = process target.dup if sexp? target

  #Bare records create links to the model resource,
  #not a string that could have injection
  #TODO: Needs test? I think this is broken?
  return exp if model_name? target and context == [:call, :arglist]

  super
end
```

    
  

    
      
  
### 
  
    #**check_argument**(result, exp)  ⇒ Object 
  

  

  

  
    

Check the argument for possible xss exploits

  

  

  
    
      

```

61
62
63
64
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 61

def check_argument result, exp
  argument = process(exp)
  !check_user_input(result, argument) && !check_method(result, argument) && !check_matched(result, @matched)
end
```

    
  

    
      
  
### 
  
    #**check_matched**(result, matched = nil)  ⇒ Object 
  

  

  

  
    

Check if we should warn about the matched result

  

  

  
    
      

```

90
91
92
93
94
95
96
97
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 90

def check_matched(result, matched = nil)
  return false unless matched
  return false if matched.type == :model and tracker.options[:ignore_model_output]

  message = msg("Unescaped ", msg_input(matched), " in ", msg_code("link_to"))

  warn_xss(result, message, @matched, :medium)
end
```

    
  

    
      
  
### 
  
    #**check_method**(result, argument)  ⇒ Object 
  

  

  

  
    

Check if we should warn about the specified method

  

  

  
    
      

```

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
87
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 77

def check_method(result, argument)
  return false if tracker.options[:ignore_model_output]
  match = has_immediate_model?(argument)
  return false unless match
  method = match.method
  return false if IGNORE_MODEL_METHODS.include? method

  confidence = :medium
  confidence = :high if likely_model_attribute? match
  warn_xss(result, msg("Unescaped model attribute in ", msg_code("link_to")), match, confidence)
end
```

    
  

    
      
  
### 
  
    #**check_user_input**(result, argument)  ⇒ Object 
  

  

  

  
    

Check we should warn about the user input

  

  

  
    
      

```

67
68
69
70
71
72
73
74
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 67

def check_user_input(result, argument)
  input = has_immediate_user_input?(argument)
  return false unless input

  message = msg("Unescaped ", msg_input(input), " in ", msg_code("link_to"))

  warn_xss(result, message, input, :high)
end
```

    
  

    
      
  
### 
  
    #**process_call**(exp)  ⇒ Object 
  

  

  

  
    
      

```

114
115
116
117
118
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 114

def process_call exp
  @mark = true
  actually_process_call exp
  exp
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
53
54
55
56
57
58
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 32

def process_result result
  return if duplicate? result

  #Have to make a copy of this, otherwise it will be changed to
  #an ignored method call by the code above.
  call = result[:call]

  first_arg = call.first_arg
  second_arg = call.second_arg

  @matched = false

  #Skip if no arguments(?) or first argument is a hash
  return if first_arg.nil? or hash? first_arg

  if version_between? "2.0.0", "2.2.99"
    check_argument result, first_arg

    if second_arg and not hash? second_arg
      check_argument result, second_arg
    end
  elsif second_arg
    #Only check first argument if there is a second argument
    #in Rails 2.3.x
    check_argument result, first_arg
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
22
23
24
25
26
27
28
29
30
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 12

def run_check
  return unless version_between?("2.0.0", "2.9.9") and not tracker.config.escape_html?

  @ignore_methods = Set[:button_to, :check_box, :escapeHTML, :escape_once,
                         :field_field, :fields_for, :h, :hidden_field,
                         :hidden_field, :hidden_field_tag, :image_tag, :label,
                         :mail_to, :radio_button, :select,
                         :submit_tag, :text_area, :text_field,
                         :text_field_tag, :url_encode, :u, :url_for,
                         :will_paginate].merge tracker.options[:safe_methods]

  @known_dangerous = []
  #Ideally, I think this should also check to see if people are setting
  #:escape => false
  @models = tracker.models.keys
  @inspect_arguments = tracker.options[:check_arguments]

  tracker.find_call(:target => false, :method => :link_to).each {|call| process_result call}
end
```

    
  

    
      
  
### 
  
    #**warn_xss**(result, message, user_input, confidence)  ⇒ Object 
  

  

  

  
    

Create a warn for this xss

  

  

  
    
      

```

100
101
102
103
104
105
106
107
108
109
110
111
112
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to.rb', line 100

def warn_xss(result, message, user_input, confidence)
  add_result(result)
  warn :result => result,
    :warning_type => "Cross-Site Scripting",
    :warning_code => :xss_link_to,
    :message => message,
    :user_input => user_input,
    :confidence => confidence,
    :link_path => "link_to",
    :cwe_id => [79]

  true
end
```