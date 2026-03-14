# Class: Pod::HooksManager::Hook
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::HooksManager::Hook
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/hooks_manager.rb
  
  

## Overview

  
    

Represents a single registered hook.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**block**  ⇒ Proc 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The block.

  

    
      
- 
  
    
      #**name**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The name of the hook.

  

    
      
- 
  
    
      #**plugin_name**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The name of the plugin that registered the hook.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name, plugin_name, block)  ⇒ Hook 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, plugin_name, block)  ⇒ Hook 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        name
      
      
        (String)
      
      
      
        —
        

@see #name.

      
    
  
    
- 
      
        plugin_name
      
      
        (String)
      
      
      
        —
        

@see #plugin_name.

      
    
  
    
- 
      
        block
      
      
        (Proc)
      
      
      
        —
        

@see #block.

      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

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
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 45

def initialize(name, plugin_name, block)
  raise ArgumentError, 'Missing name' unless name
  raise ArgumentError, 'Missing plugin_name' unless plugin_name
  raise ArgumentError, 'Missing block' unless block

  @name = name
  @plugin_name = plugin_name
  @block = block
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**block**  ⇒ Proc  (readonly)
  

  

  

  
    

Returns The block.

  

  

Returns:

  
    
- 
      
      
        (Proc)
      
      
      
        —
        

The block.

      
    
  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 35

def block
  @block
end
```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ String  (readonly)
  

  

  

  
    

Returns The name of the hook.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The name of the hook.

      
    
  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 30

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**plugin_name**  ⇒ String  (readonly)
  

  

  

  
    

Returns The name of the plugin that registered the hook.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The name of the plugin that registered the hook.

      
    
  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/cocoapods/hooks_manager.rb', line 25

def plugin_name
  @plugin_name
end
```