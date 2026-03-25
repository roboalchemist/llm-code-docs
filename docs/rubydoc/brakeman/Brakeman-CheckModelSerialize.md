# Class: Brakeman::CheckModelSerialize
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckModelSerialize
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_model_serialize.rb
  
  

  
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
  
    
      #**check_for_serialize**(model)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

High confidence warning on serialized, unprotected attributes.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_for_serialize**(model)  ⇒ Object 
  

  

  

  
    

High confidence warning on serialized, unprotected attributes. Medium confidence warning for serialized, protected attributes.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_model_serialize.rb', line 27

def check_for_serialize model
  if serialized_attrs = model.options[:serialize]
    attrs = Set.new

    serialized_attrs.each do |arglist|
      arglist.each do |arg|
        attrs << arg if symbol? arg
      end
    end

    if unsafe_attrs = model.attr_accessible
      attrs.delete_if { |attr| not unsafe_attrs.include? attr.value }
    elsif protected_attrs = model.attr_protected
      safe_attrs = Set.new

      protected_attrs.each do |arglist|
        arglist.each do |arg|
          safe_attrs << arg if symbol? arg
        end
      end

      attrs.delete_if { |attr| safe_attrs.include? attr }
    end

    if attrs.empty?
      confidence = :medium
    else
      confidence = :high
    end

    warn :model => model,
      :warning_type => "Remote Code Execution",
      :warning_code => :CVE_2013_0277,
      :message => msg("Serialized attributes are vulnerable in ", msg_version(rails_version), ", upgrade to ", msg_version(@upgrade_version), " or patch"),
      :confidence => confidence,
      :link => "https://groups.google.com/d/topic/rubyonrails-security/KtmwSbEpzrU/discussion",
      :file => model.file,
      :line => model.top_line,
      :cwe_id => [502]
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
22
23
```

    
    
      

```
# File 'lib/brakeman/checks/check_model_serialize.rb', line 8

def run_check
  @upgrade_version = case
                    when version_between?("2.0.0", "2.3.16")
                      "2.3.17"
                    when version_between?("3.0.0", "3.0.99")
                      "3.2.11"
                    else
                      nil
                    end

  return unless @upgrade_version

  tracker.models.each do |_name, model|
    check_for_serialize model
  end
end
```