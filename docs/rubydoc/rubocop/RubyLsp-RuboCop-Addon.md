# Class: RubyLsp::RuboCop::Addon
  
    Inherits:
    
      Addon
      
        

          
- Object

- Addon

- RubyLsp::RuboCop::Addon

        show all
      

    Defined in:
    lib/ruby_lsp/rubocop/addon.rb
  
## Overview

A Ruby LSP add-on for RuboCop.

##

      Constant Summary
      collapse
    

    
      
        RESTART_WATCHERS =
          
        
        

```
%w[.rubocop.yml .rubocop_todo.yml .rubocop].freeze
```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**activate**(global_state, message_queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**deactivate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**  ⇒ Addon 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Addon.

-
  
      #**name**  ⇒ Object 

-
  
      #**register_additional_file_watchers**(global_state, message_queue)  ⇒ Object 

rubocop:disable Metrics/MethodLength.

-
  
      #**version**  ⇒ Object 

-
  
      #**workspace_did_change_watched_files**(changes)  ⇒ Object 

rubocop:enable Metrics/MethodLength.

## Constructor Details

###
  
    #**initialize**  ⇒ Addon 
  

  

  

  
    

Returns a new instance of Addon.

```

13
14
15
16
```

```
# File 'lib/ruby_lsp/rubocop/addon.rb', line 13

def initialize
  super
  @runtime_adapter = nil
end
```

## Instance Method Details

###
  
    #**activate**(global_state, message_queue)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/ruby_lsp/rubocop/addon.rb', line 26

def activate(global_state, message_queue)
  ::RuboCop::LSP::Logger.log(
    "Activating RuboCop LSP addon #{::RuboCop::Version::STRING}.", prefix: '[RuboCop]'
  )

  @runtime_adapter = RuntimeAdapter.new(message_queue)
  global_state.register_formatter('rubocop', @runtime_adapter)
  register_additional_file_watchers(global_state, message_queue)

  ::RuboCop::LSP::Logger.log(
    "Initialized RuboCop LSP addon #{::RuboCop::Version::STRING}.", prefix: '[RuboCop]'
  )
end
```

###
  
    #**deactivate**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

```
# File 'lib/ruby_lsp/rubocop/addon.rb', line 40

def deactivate
  @runtime_adapter = nil
end
```

###
  
    #**name**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

```
# File 'lib/ruby_lsp/rubocop/addon.rb', line 18

def name
  'RuboCop'
end
```

###
  
    #**register_additional_file_watchers**(global_state, message_queue)  ⇒ Object 
  

  

  

  
    

rubocop:disable Metrics/MethodLength

```

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
```

```
# File 'lib/ruby_lsp/rubocop/addon.rb', line 45

def register_additional_file_watchers(global_state, message_queue)
  return unless global_state.supports_watching_files

  message_queue << Request.new(
    id: 'rubocop-file-watcher',
    method: 'client/registerCapability',
    params: Interface::RegistrationParams.new(
      registrations: [
        Interface::Registration.new(
          id: 'workspace/didChangeWatchedFilesRuboCop',
          method: 'workspace/didChangeWatchedFiles',
          register_options: Interface::DidChangeWatchedFilesRegistrationOptions.new(
            watchers: [
              Interface::FileSystemWatcher.new(
                glob_pattern: "**/{#{RESTART_WATCHERS.join(',')}}",
                kind: Constant::WatchKind::CREATE | Constant::WatchKind::CHANGE | Constant::WatchKind::DELETE
              )
            ]
          )
        )
      ]
    )
  )
end
```

###
  
    #**version**  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
```

```
# File 'lib/ruby_lsp/rubocop/addon.rb', line 22

def version
  ::RuboCop::Version::STRING
end
```

###
  
    #**workspace_did_change_watched_files**(changes)  ⇒ Object 
  

  

  

  
    

rubocop:enable Metrics/MethodLength

```

71
72
73
74
75
76
77
78
79
```

```
# File 'lib/ruby_lsp/rubocop/addon.rb', line 71

def workspace_did_change_watched_files(changes)
  if (changed_config_file = changed_config_file(changes))
    @runtime_adapter.reload_config

    ::RuboCop::LSP::Logger.log(<<~MESSAGE, prefix: '[RuboCop]')
      Re-initialized RuboCop LSP addon #{::RuboCop::Version::STRING} due to #{changed_config_file} change.
    MESSAGE
  end
end
```
