# Class: Brakeman::CheckRender
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckRender
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_render.rb
  
  

## Overview

  
    

Check calls to render() for dangerous values

  

  

  
## Direct Known Subclasses

  

CheckRenderRCE

  
## Constant Summary

  
  
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
  
    
      #**check_for_dynamic_path**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check if path to action or file is determined dynamically.

  

      
        
- 
  
    
      #**known_renderable_class?**(class_name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_render_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**renderable?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**safe_param?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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

  
    

This class inherits a constructor from Brakeman::BaseCheck
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check_for_dynamic_path**(result)  ⇒ Object 
  

  

  

  
    

Check if path to action or file is determined dynamically

  

  

  
    
      

```

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
53
54
55
56
57
58
59
60
```

    
    
      

```
# File 'lib/brakeman/checks/check_render.rb', line 31

def check_for_dynamic_path result
  view = result[:call][2]

  if sexp? view and original? result
    return if renderable?(view)

    if input = has_immediate_user_input?(view)
      if string_interp? view
        confidence = :medium
      else
        confidence = :high
      end
    else
      return
    end

    return if input.type == :model #skip models
    return if safe_param? input.match

    message = msg("Render path contains ", msg_input(input))

    warn :result => result,
      :warning_type => "Dynamic Render Path",
      :warning_code => :dynamic_render_path,
      :message => message,
      :user_input => input,
      :confidence => confidence,
      :cwe_id => [22]
  end
end
```

    
  

    
      
  
### 
  
    #**known_renderable_class?**(class_name)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

87
88
89
90
91
92
93
94
95
96
```

    
    
      

```
# File 'lib/brakeman/checks/check_render.rb', line 87

def known_renderable_class? class_name
  klass = tracker.find_class(class_name)
  return false if klass.nil?
  knowns = [
    :"ViewComponent::Base",
    :"ViewComponentContrib::Base",
    :"Phlex::HTML"
  ]
  knowns.any? { |k| klass.ancestor? k }
end
```

    
  

    
      
  
### 
  
    #**process_render_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_render.rb', line 15

def process_render_result result
  return unless node_type? result[:call], :render

  case result[:call].render_type
  when :partial, :template, :action, :file
    check_for_dynamic_path(result)
  when :inline
  when :js
  when :json
  when :text
  when :update
  when :xml
  end
end
```

    
  

    
      
  
### 
  
    #**renderable?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

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
# File 'lib/brakeman/checks/check_render.rb', line 75

def renderable? exp
  return false unless call?(exp) and constant?(exp.target)

  if exp.method == :with_content
    exp = exp.target
  end

  return false unless constant?(exp.target)
  target_class_name = class_name(exp.target)
  known_renderable_class?(target_class_name) or tracker.find_method(:render_in, target_class_name)
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
12
13
```

    
    
      

```
# File 'lib/brakeman/checks/check_render.rb', line 9

def run_check
  tracker.find_call(:target => nil, :method => :render).each do |result|
    process_render_result result
  end
end
```

    
  

    
      
  
### 
  
    #**safe_param?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_render.rb', line 62

def safe_param? exp
  if params? exp and call? exp
    method_name = exp.method

    if method_name == :[]
      arg = exp.first_arg
      symbol? arg and [:controller, :action].include? arg.value
    else
      boolean_method? method_name
    end
  end
end
```