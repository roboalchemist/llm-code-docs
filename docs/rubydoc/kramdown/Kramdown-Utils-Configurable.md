# Module: Kramdown::Utils::Configurable
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Converter
  
  

  
  
    Defined in:
    lib/kramdown/utils/configurable.rb
  
  

## Overview

  
    

Methods for registering configurable extensions.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**configurable**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new configurable extension called `name`.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**configurable**(name)  ⇒ Object 
  

  

  

  
    

Create a new configurable extension called `name`.

Three methods will be defined on the calling object which allow to use this configurable extension:
configurables

Returns a hash of hashes that is used to store all configurables of the object.
<name>(ext_name)

Return the configured extension `ext_name`.
add_<name>(ext_name, data=nil, &block)

Define an extension `ext_name` by specifying either the data as argument or by using a block.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/utils/configurable.rb', line 28

def configurable(name)
  unless respond_to?(:configurables)
    singleton_class.send(:define_method, :configurables) do
      @_configurables ||= Hash.new {|h, k| h[k] = {} }
    end
  end
  singleton_class.send(:define_method, name) do |data|
    configurables[name][data]
  end
  singleton_class.send(:define_method, "add_#{name}".intern) do |data, *args, &block|
    configurables[name][data] = args.first || block
  end
end

```