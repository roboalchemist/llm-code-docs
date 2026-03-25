# Class: Brakeman::CheckRenderInline
  
  
  

  
  
    Inherits:
    
      CheckCrossSiteScripting
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- CheckCrossSiteScripting
          
            
- Brakeman::CheckRenderInline
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_render_inline.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CONTENT_TYPES =
          
        
        

```
["text/html", "text/javascript", "application/javascript"]
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
  
    
      #**check_render**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**content_type_set?**(opts)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from CheckCrossSiteScripting

  

#actually_process_call, #cgi_escaped?, #check_for_immediate_xss, #form_builder_method?, #haml_escaped?, #html_safe_call?, #ignore_call?, #ignored_method?, #ignored_model_method?, #initialize, #likely_model_attribute?, #process_call, #process_case, #process_cookies, #process_dstr, #process_escaped_output, #process_format, #process_format_escaped, #process_if, #process_output, #process_params, #process_render, #raw_call?, #safe_input_attribute?, #setup, #xml_escaped?

  
  
  
  
  
  
  
  
  
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
  
    #**check_render**(result)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_render_inline.rb', line 14

def check_render result
  return unless original? result

  call = result[:call]

  if node_type? call, :render and
    (call.render_type == :text or call.render_type == :inline)

    unless call.render_type == :text and content_type_set? call[3]
      render_value = call[2]

      if input = has_immediate_user_input?(render_value)
        warn :result => result,
          :warning_type => "Cross-Site Scripting",
          :warning_code => :cross_site_scripting_inline,
          :message => msg("Unescaped ", msg_input(input), " rendered inline"),
          :user_input => input,
          :confidence => :high,
          :cwe_id => [79]
      elsif input = has_immediate_model?(render_value)
        warn :result => result,
          :warning_type => "Cross-Site Scripting",
          :warning_code => :cross_site_scripting_inline,
          :message => "Unescaped model attribute rendered inline",
          :user_input => input,
          :confidence => :medium,
          :cwe_id => [79]
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**content_type_set?**(opts)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

48
49
50
51
52
53
54
```

    
    
      

```
# File 'lib/brakeman/checks/check_render_inline.rb', line 48

def content_type_set? opts
  if hash? opts
    content_type = hash_access(opts, :content_type)

    string? content_type and not CONTENT_TYPES.include? content_type.value
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
10
11
12
```

    
    
      

```
# File 'lib/brakeman/checks/check_render_inline.rb', line 6

def run_check
  setup

  tracker.find_call(:target => nil, :method => :render).each do |result|
    check_render result
  end
end
```