# Class: Brakeman::CheckFileAccess
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckFileAccess
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_file_access.rb
  
  

## Overview

  
    

Checks for user input in methods which open or manipulate files

  

  

  
## Direct Known Subclasses

  

CheckSendFile

  
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
  
    
      #**called_on_tempfile?**(file_name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

When using Tempfile, there is no risk of unauthorized file access, since Tempfile adds a unique string onto the end of every provided filename, and ensures that the filename does not already exist in the system.

  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sanitized?**(file)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**temp_file_method?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**called_on_tempfile?**(file_name)  ⇒ Boolean 
  

  

  

  
    

When using Tempfile, there is no risk of unauthorized file access, since Tempfile adds a unique string onto the end of every provided filename, and ensures that the filename does not already exist in the system.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/brakeman/checks/check_file_access.rb', line 71

def called_on_tempfile? file_name
  call?(file_name) && file_name.target == s(:const, :Tempfile)
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_file_access.rb', line 29

def process_result result
  return unless original? result
  call = result[:call]

  file_name = call.first_arg

  return if called_on_tempfile?(file_name) || sanitized?(file_name)

  if match = has_immediate_user_input?(file_name)
    confidence = :high
  elsif match = has_immediate_model?(file_name)
    match = Match.new(:model, match)
    confidence = :medium
  elsif tracker.options[:check_arguments] and
    match = include_user_input?(file_name)

    #Check for string building in file name
    if call?(file_name) and (file_name.method == :+ or file_name.method == :<<)
      confidence = :high
    else
      confidence = :weak
    end
  end

  if match and not temp_file_method? match.match

    message = msg(msg_input(match), " used in file name")

    warn :result => result,
      :warning_type => "File Access",
      :warning_code => :file_access,
      :message => message,
      :confidence => confidence,
      :code => call,
      :user_input => match,
      :cwe_id => [22]
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

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
21
22
23
24
25
26
27
```

    
    
      

```
# File 'lib/brakeman/checks/check_file_access.rb', line 10

def run_check
  Brakeman.debug "Finding possible file access"
  methods = tracker.find_call :targets => [:Dir, :File, :IO, :Kernel, :"Net::FTP", :"Net::HTTP", :PStore, :Pathname, :Shell], :methods => [:[], :chdir, :chroot, :delete, :entries, :foreach, :glob, :install, :lchmod, :lchown, :link, :load, :load_file, :makedirs, :move, :new, :open, :read, :readlines, :rename, :rmdir, :safe_unlink, :symlink, :syscopy, :sysopen, :truncate, :unlink]

  methods.concat tracker.find_call :target => :YAML, :methods => [:load_file, :parse_file]
  methods.concat tracker.find_call :target => nil, :method => [:open]

  Brakeman.debug "Finding calls to load()"
  methods.concat tracker.find_call :target => false, :method => :load

  Brakeman.debug "Finding calls using FileUtils"
  methods.concat tracker.find_call :target => :FileUtils

  Brakeman.debug "Processing found calls"
  methods.each do |call|
    process_result call
  end
end
```

    
  

    
      
  
### 
  
    #**sanitized?**(file)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

75
76
77
78
79
```

    
    
      

```
# File 'lib/brakeman/checks/check_file_access.rb', line 75

def sanitized? file
  call?(file) &&
    call?(file.target) &&
    class_name(file.target.target) == :"ActiveStorage::Filename"
end
```

    
  

    
      
  
### 
  
    #**temp_file_method?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_file_access.rb', line 81

def temp_file_method? exp
  if call? exp
    return true if exp.call_chain.include? :tempfile

    params? exp.target and exp.method == :path
  end
end
```