# Class: Pod::ExternalSources::AbstractExternalSource
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::ExternalSources::AbstractExternalSource
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/external_sources/abstract_external_source.rb
  
  

## Overview

  
    

Abstract class that defines the common behaviour of external sources.

  

  

  
## Direct Known Subclasses

  

DownloaderSource, PathSource, PodspecSource

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**can_cache**  ⇒ Boolean 
    

    
      (also: #can_cache?)
    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Whether the source is allowed to touch the cache.

  

    
      
- 
  
    
      #**name**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The name of the Pod described by this external source.

  

    
      
- 
  
    
      #**params**  ⇒ Hash{Symbol => String} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The hash representation of the external source.

  

    
      
- 
  
    
      #**podfile_path**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The path where the podfile is defined to resolve relative paths.

  

    
  

  
    
## 
      Subclasses hooks
      collapse
    

    

      
        
- 
  
    
      #**description**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

A string representation of the source suitable for UI.

  

      
        
- 
  
    
      #**fetch**(_sandbox)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Fetches the external source from the remote according to the params.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**==**(other)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether an external source source is equal to another according to the #name and to the #params.

  

      
        
- 
  
    
      #**initialize**(name, params, podfile_path, can_cache = true)  ⇒ AbstractExternalSource 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, params, podfile_path, can_cache = true)  ⇒ AbstractExternalSource 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        name
      
      
        (String)
      
      
      
        —
        

@see #name

      
    
  
    
- 
      
        params
      
      
        (Hash)
      
      
      
        —
        

@see #params

      
    
  
    
- 
      
        podfile_path
      
      
        (String)
      
      
      
        —
        

@see #podfile_path

      
    
  
    
- 
      
        can_cache
      
      
        (Boolean)
      
      
        *(defaults to: true)*
      
      
        —
        

@see #can_cache

      
    
  

  
    
      

```

32
33
34
35
36
37
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 32

def initialize(name, params, podfile_path, can_cache = true)
  @name = name
  @params = params
  @podfile_path = podfile_path
  @can_cache = can_cache
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**can_cache**  ⇒ Boolean  (readonly)
  

  
    Also known as:
    can_cache?
    
  

  

  
    

Returns Whether the source is allowed to touch the cache.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the source is allowed to touch the cache.

      
    
  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 22

def can_cache
  @can_cache
end

```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ String  (readonly)
  

  

  

  
    

Returns the name of the Pod described by this external source.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

the name of the Pod described by this external source.

      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 8

def name
  @name
end

```

    
  

    
      
      
      
  
### 
  
    #**params**  ⇒ Hash{Symbol => String}  (readonly)
  

  

  

  
    

Returns the hash representation of the external source.

  

  

Returns:

  
    
- 
      
      
        (Hash{Symbol => String})
      
      
      
        —
        

the hash representation of the external source.

      
    
  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 13

def params
  @params
end

```

    
  

    
      
      
      
  
### 
  
    #**podfile_path**  ⇒ String  (readonly)
  

  

  

  
    

Returns the path where the podfile is defined to resolve relative paths.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

the path where the podfile is defined to resolve relative paths.

      
    
  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 18

def podfile_path
  @podfile_path
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**==**(other)  ⇒ Boolean 
  

  

  

  
    

Returns whether an external source source is equal to another according to the #name and to the #params.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

whether an external source source is equal to another according to the #name and to the #params.

      
    
  

  
    
      

```

42
43
44
45
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 42

def ==(other)
  return false if other.nil?
  name == other.name && params == other.params
end

```

    
  

    
      
  
### 
  
    #**description**  ⇒ String 
  

  

  

  
    

Returns a string representation of the source suitable for UI.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

a string representation of the source suitable for UI.

      
    
  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 64

def description
  raise 'Abstract method'
end

```

    
  

    
      
  
### 
  
    #**fetch**(_sandbox)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Fetches the external source from the remote according to the params.

  

  

Parameters:

  
    
- 
      
        _sandbox
      
      
        (Sandbox)
      
      
      
        —
        

the sandbox where the specification should be stored.

      
    
  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/cocoapods/external_sources/abstract_external_source.rb', line 58

def fetch(_sandbox)
  raise 'Abstract method'
end

```