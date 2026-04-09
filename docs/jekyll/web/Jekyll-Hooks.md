# Module: Jekyll::Hooks
  
    Defined in:
    lib/jekyll/hooks.rb
  
  

  
    
##

      Constant Summary
      collapse
    

    
      
        DEFAULT_PRIORITY =
          
        
        

```
20
```

        PRIORITY_MAP =
          
  
    

compatibility layer for octopress-hooks users

```
{
  :low    => 10,
  :normal => 20,
  :high   => 30,
}.freeze
```

        NotAvailable =
          
        
        

```
Class.new(RuntimeError)
```

        Uncallable =
          
        
        

```
Class.new(RuntimeError)
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**insert_hook**(owner, event, priority, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**priority_value**(priority)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ensure the priority is a Fixnum.

-
  
      .**register**(owners, event, priority: DEFAULT_PRIORITY, &block)  ⇒ Object 

register hook(s) to be called later, public API.

-
  
      .**register_one**(owner, event, priority, &block)  ⇒ Object 

register a single hook to be called later, internal API.

-
  
      .**trigger**(owner, event, *args)  ⇒ Object 

interface for Jekyll core components to trigger hooks.

## Class Method Details

###
  
    .**insert_hook**(owner, event, priority, &block)  ⇒ Object 
  

  

  

  
    
      

```

90
91
92
93
```

```
# File 'lib/jekyll/hooks.rb', line 90

def self.insert_hook(owner, event, priority, &block)
  @hook_priority[block] = [-priority, @hook_priority.size]
  @registry[owner][event] << block
end
```

###
  
    .**priority_value**(priority)  ⇒ Object 
  

  

  

  
    

Ensure the priority is a Fixnum

```

64
65
66
67
68
```

```
# File 'lib/jekyll/hooks.rb', line 64

def self.priority_value(priority)
  return priority if priority.is_a?(Integer)

  PRIORITY_MAP[priority] || DEFAULT_PRIORITY
end
```

###
  
    .**register**(owners, event, priority: DEFAULT_PRIORITY, &block)  ⇒ Object 
  

  

  

  
    

register hook(s) to be called later, public API

```

57
58
59
60
61
```

```
# File 'lib/jekyll/hooks.rb', line 57

def self.register(owners, event, priority: DEFAULT_PRIORITY, &block)
  Array(owners).each do |owner|
    register_one(owner, event, priority_value(priority), &block)
  end
end
```

###
  
    .**register_one**(owner, event, priority, &block)  ⇒ Object 
  

  

  

  
    

register a single hook to be called later, internal API

Raises:

-

        (Uncallable)

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
80
81
82
83
84
85
86
87
88
```

```
# File 'lib/jekyll/hooks.rb', line 71

def self.register_one(owner, event, priority, &block)
  @registry[owner] ||= {
    :post_init    => [],
    :pre_render   => [],
    :post_convert => [],
    :post_render  => [],
    :post_write   => [],
  }

  unless @registry[owner][event]
    raise NotAvailable, "Invalid hook. #{owner} supports only the following hooks " \
                        "#{@registry[owner].keys.inspect}"
  end

  raise Uncallable, "Hooks must respond to :call" unless block.respond_to? :call

  insert_hook owner, event, priority, &block
end
```

###
  
    .**trigger**(owner, event, *args)  ⇒ Object 
  

  

  

  
    

interface for Jekyll core components to trigger hooks

```

96
97
98
99
100
101
102
103
104
105
```

```
# File 'lib/jekyll/hooks.rb', line 96

def self.trigger(owner, event, *args)
  # proceed only if there are hooks to call
  hooks = @registry.dig(owner, event)
  return if hooks.nil? || hooks.empty?

  # sort and call hooks according to priority and load order
  hooks.sort_by { |h| @hook_priority[h] }.each do |hook|
    hook.call(*args)
  end
end
```
