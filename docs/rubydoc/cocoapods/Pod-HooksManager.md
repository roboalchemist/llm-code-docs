# Module: Pod::HooksManager
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/hooks_manager.rb
  
  

## Overview

  
    

Provides support for the hook system of CocoaPods. The system is designed especially for plugins. Interested clients can register to notifications by name.

The blocks, to prevent compatibility issues, will receive one and only one argument: a context object. This object should be simple storage of information (a typed hash). Notifications senders are responsible to indicate the class of the object associated with their notification name.

Context object should not remove attribute accessors to not break compatibility with the plugins (this promise will be honoured strictly from CocoaPods 1.0).

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Hook
    
  

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**registrations**  ⇒ Hash{Symbol => Array<Hook>} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The list of the hooks that are registered for each hook name.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**hooks_to_run**(name, whitelisted_plugins = nil)  ⇒ Array<Hook> 
    

    
  
  
  
  
  
  
  
  

  
    

Returns all the hooks to run for the given event name and set of whitelisted plugins.

  

      
        
- 
  
    
      .**register**(plugin_name, hook_name, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Registers a block for the hook with the given name.

  

      
        
- 
  
    
      .**run**(name, context, whitelisted_plugins = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Runs all the registered blocks for the hook with the given name.

  

      
    

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**registrations**  ⇒ Hash{Symbol => Array<Hook>}  (readonly)
  

  

  

  
    

Returns The list of the hooks that are registered for each hook name.

  

  

Returns:

  
    
- 
      
      
        (Hash{Symbol => Array<Hook>})
      
      
      
        —
        

The list of the hooks that are registered for each hook name.

      
    
  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 60

def registrations
  @registrations
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**hooks_to_run**(name, whitelisted_plugins = nil)  ⇒ Array<Hook> 
  

  

  

  
    

Returns all the hooks to run for the given event name and set of whitelisted plugins

  

  

Returns:

  
    
- 
      
      
        (Array<Hook>)
      
      
      
        —
        

the hooks to run

      
    
  

  

See Also:
  

    
      
- #run
    
  

  
    
      

```

86
87
88
89
90
91
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 86

def hooks_to_run(name, whitelisted_plugins = nil)
  return [] unless registrations
  hooks = registrations.fetch(name, [])
  return hooks unless whitelisted_plugins
  hooks.select { |hook| whitelisted_plugins.key?(hook.plugin_name) }
end

```

    
  

    
      
  
### 
  
    .**register**(plugin_name, hook_name, &block)  ⇒ Object 
  

  

  

  
    

Registers a block for the hook with the given name.

  

  

Parameters:

  
    
- 
      
        plugin_name
      
      
        (String)
      
      
      
        —
        

The name of the plugin the hook comes from.

      
    
  
    
- 
      
        hook_name
      
      
        (Symbol)
      
      
      
        —
        

The name of the notification.

      
    
  
    
- 
      
        block
      
      
        (Proc)
      
      
      
        —
        

The block.

      
    
  

  
    
      

```

73
74
75
76
77
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 73

def register(plugin_name, hook_name, &block)
  @registrations ||= {}
  @registrations[hook_name] ||= []
  @registrations[hook_name] << Hook.new(hook_name, plugin_name, block)
end

```

    
  

    
      
  
### 
  
    .**run**(name, context, whitelisted_plugins = nil)  ⇒ Object 
  

  

  

  
    

Runs all the registered blocks for the hook with the given name.

  

  

Parameters:

  
    
- 
      
        name
      
      
        (Symbol)
      
      
      
        —
        

The name of the hook.

      
    
  
    
- 
      
        context
      
      
        (Object)
      
      
      
        —
        

The context object which should be passed to the blocks.

      
    
  
    
- 
      
        whitelisted_plugins
      
      
        (Hash<String, Hash>)
      
      
        *(defaults to: nil)*
      
      
        —
        

The plugins that should be run, in the form of a hash keyed by plugin name, where the values are the custom options that should be passed to the hook’s block if it supports taking a second argument.

      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

107
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
123
124
125
126
127
128
129
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 107

def run(name, context, whitelisted_plugins = nil)
  raise ArgumentError, 'Missing name' unless name
  raise ArgumentError, 'Missing options' unless context

  hooks = hooks_to_run(name, whitelisted_plugins)
  return if hooks.empty?

  UI.message "- Running #{name.to_s.tr('_', ' ')} hooks" do
    hooks.each do |hook|
      UI.message "- #{hook.plugin_name} from " \
                  "`#{hook.block.source_location.first}`" do
        block = hook.block
        if block.arity > 1
          user_options = whitelisted_plugins[hook.plugin_name]
          user_options = user_options.with_indifferent_access if user_options
          block.call(context, user_options)
        else
          block.call(context)
        end
      end
    end
  end
end

```