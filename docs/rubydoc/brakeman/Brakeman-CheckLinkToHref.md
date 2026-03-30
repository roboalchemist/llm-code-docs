# Class: Brakeman::CheckLinkToHref
  
  
  

  
  
    Inherits:
    
      CheckLinkTo
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- CheckCrossSiteScripting
          
            
- CheckLinkTo
          
            
- Brakeman::CheckLinkToHref
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_link_to_href.rb
  
  

## Overview

  
    

Checks for calls to link_to which pass in potentially hazardous data to the second argument.  While this argument must be html_safe to not break the html, it must also be url safe as determined by calling a :url_safe_method.  This prevents attacks such as javascript:evil() or data:<encoded XSS> which is html_safe, but not safe as an href Props to Nick Green for the idea.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CHECK_INSIDE_METHODS =
          
        
        

```
[:url_for, :h, :sanitize]
```

      
    
  

  
  
  
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
  
    
      #**call_on_params?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_argument?**(url_arg)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**decorated_model?**(method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignore_call?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignore_interpolation?**(arg, suspect)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Ignore situations where the href is an interpolated string with something before the user input.

  

      
        
- 
  
    
      #**ignore_model_call?**(url_arg, exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignored_method?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**model_find_call?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from CheckLinkTo

  

#actually_process_call, #check_argument, #check_matched, #check_method, #check_user_input, #process_call, #warn_xss

  
  
  
  
  
  
  
  
  
### Methods inherited from CheckCrossSiteScripting

  

#actually_process_call, #cgi_escaped?, #check_for_immediate_xss, #form_builder_method?, #haml_escaped?, #html_safe_call?, #ignored_model_method?, #initialize, #likely_model_attribute?, #process_call, #process_case, #process_cookies, #process_dstr, #process_escaped_output, #process_format, #process_format_escaped, #process_if, #process_output, #process_params, #process_render, #raw_call?, #safe_input_attribute?, #setup, #xml_escaped?

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_call, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
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
  
    #**call_on_params?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

146
147
148
149
150
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 146

def call_on_params? exp
  call? exp and
  params? exp.target and
  exp.method != :[]
end
```

    
  

    
      
  
### 
  
    #**check_argument?**(url_arg)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

81
82
83
84
85
86
87
88
89
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 81

def check_argument? url_arg
  return unless call? url_arg

  target = url_arg.target
  method = url_arg.method

  CHECK_INSIDE_METHODS.include? method or
    cgi_escaped? target, method
end
```

    
  

    
      
  
### 
  
    #**decorated_model?**(method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

128
129
130
131
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 128

def decorated_model? method
  tracker.config.has_gem? :draper and
    method == :decorate
end
```

    
  

    
      
  
### 
  
    #**ignore_call?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 124

def ignore_call? target, method
  decorated_model? method or super
end
```

    
  

    
      
  
### 
  
    #**ignore_interpolation?**(arg, suspect)  ⇒ Boolean 
  

  

  

  
    

Ignore situations where the href is an interpolated string with something before the user input

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 108

def ignore_interpolation? arg, suspect
  return unless string_interp? arg
  return true unless arg[1].chomp.empty? # plain string before interpolation

  first_interp = arg.find_nodes(:evstr).first
  return unless first_interp

  first_interp[1].deep_each do |e|
    if suspect == e
      return false
    end
  end

  true
end
```

    
  

    
      
  
### 
  
    #**ignore_model_call?**(url_arg, exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

91
92
93
94
95
96
97
98
99
100
101
102
103
104
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 91

def ignore_model_call? url_arg, exp
  return true unless call? exp

  target = exp.target
  method = exp.method

  return true unless model_find_call? target

  return true unless method.to_s =~ /url|uri|link|page|site/

  ignore_call? target, method or
    IGNORE_MODEL_METHODS.include? method or
    ignore_interpolation? url_arg, exp
end
```

    
  

    
      
  
### 
  
    #**ignored_method?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

133
134
135
136
137
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 133

def ignored_method? target, method
  @ignore_methods.include? method or
    method.to_s =~ /_path$/ or
    (target.nil? and method.to_s =~ /_url$/)
end
```

    
  

    
      
  
### 
  
    #**model_find_call?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

139
140
141
142
143
144
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 139

def model_find_call? exp
  return unless call? exp

  MODEL_METHODS.include? exp.method or
    exp.method.to_s =~ /^find_by_/
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
69
70
71
72
73
74
75
76
77
```

    
    
      

```
# File 'lib/brakeman/checks/check_link_to_href.rb', line 32

def process_result result
  call = result[:call]
  @matched = false

  url_arg = if result[:block]
              process call.first_arg
            else
              process call.second_arg
            end

  if check_argument? url_arg
    url_arg = url_arg.first_arg
  end

  return if call? url_arg and ignore_call? url_arg.target, url_arg.method

  if input = has_immediate_user_input?(url_arg)
    message = msg("Unsafe ", msg_input(input), " in ", msg_code("link_to"), " href")

    unless duplicate? result or call_on_params? url_arg or ignore_interpolation? url_arg, input.match
      add_result result
      warn :result => result,
        :warning_type => "Cross-Site Scripting",
        :warning_code => :xss_link_to_href,
        :message => message,
        :user_input => input,
        :confidence => :high,
        :link_path => "link_to_href",
        :cwe_id => [79]
    end
  elsif not tracker.options[:ignore_model_output] and input = has_immediate_model?(url_arg)
    return if ignore_model_call? url_arg, input or duplicate? result
    add_result result

    message = msg("Potentially unsafe model attribute in ", msg_code("link_to"), " href")

    warn :result => result,
      :warning_type => "Cross-Site Scripting",
      :warning_code => :xss_link_to_href,
      :message => message,
      :user_input => input,
      :confidence => :weak,
      :link_path => "link_to_href",
      :cwe_id => [79]
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_link_to_href.rb', line 14

def run_check
  @ignore_methods = Set[:button_to, :check_box,
                         :field_field, :fields_for, :hidden_field,
                         :hidden_field, :hidden_field_tag, :image_tag, :label,
                         :mail_to, :polymorphic_url, :radio_button, :select, :slice,
                         :submit_tag, :text_area, :text_field,
                         :text_field_tag, :url_encode, :u,
                         :will_paginate].merge(tracker.options[:url_safe_methods] || [])

  @models = tracker.models.keys
  @inspect_arguments = tracker.options[:check_arguments]

  methods = tracker.find_call :target => false, :method => :link_to
  methods.each do |call|
    process_result call
  end
end
```