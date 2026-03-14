# Module: Pod::ExternalSources
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/external_sources.rb,

  lib/cocoapods/external_sources/path_source.rb,
 lib/cocoapods/external_sources/podspec_source.rb,
 lib/cocoapods/external_sources/downloader_source.rb,
 lib/cocoapods/external_sources/abstract_external_source.rb

  
  

## Overview

  
    

Provides support for initializing the correct concrete class of an external source.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** AbstractExternalSource, DownloaderSource, PathSource, PodspecSource
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**concrete_class_from_params**(params)  ⇒ Class 
    

    
  
  
  
  
  
  
  
  

  
    

Get the class to represent the defined source type of a dependency.

  

      
        
- 
  
    
      .**from_dependency**(dependency, podfile_path, can_cache)  ⇒ AbstractExternalSource 
    

    
  
  
  
  
  
  
  
  

  
    

Instantiate a matching AbstractExternalSource for a given dependency.

  

      
        
- 
  
    
      .**from_params**(params, dependency, podfile_path, can_cache)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**concrete_class_from_params**(params)  ⇒ Class 
  

  

  

  
    

Get the class to represent the defined source type of a dependency

  

  

Parameters:

  
    
- 
      
        params
      
      
        (Array<Symbol>)
      
      
      
        —
        

the source params of the dependency

      
    
  

Returns:

  
    
- 
      
      
        (Class)
      
      
      
    
  

  
    
      

```

47
48
49
50
51
52
53
54
55
```

    
    
      

```
# File 'lib/cocoapods/external_sources.rb', line 47

def self.concrete_class_from_params(params)
  if params.key?(:podspec)
    PodspecSource
  elsif params.key?(:path)
    PathSource
  elsif Downloader.strategy_from_options(params)
    DownloaderSource
  end
end
```

    
  

    
      
  
### 
  
    .**from_dependency**(dependency, podfile_path, can_cache)  ⇒ AbstractExternalSource 
  

  

  

  
    

Instantiate a matching AbstractExternalSource for a given dependency.

  

  

Parameters:

  
    
- 
      
        dependency
      
      
        (Dependency)
      
      
      
        —
        

the dependency

      
    
  
    
- 
      
        podfile_path
      
      
        (String)
      
      
      
        —
        

@see AbstractExternalSource#podfile_path

      
    
  
    
- 
      
        can_cache
      
      
        (Boolean)
      
      
      
        —
        

@see AbstractExternalSource#can_cache

      
    
  

Returns:

  
    
- 
      
      
        (AbstractExternalSource)
      
      
      
        —
        

an initialized instance of the concrete external source class associated with the option specified in the hash.

      
    
  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/cocoapods/external_sources.rb', line 26

def self.from_dependency(dependency, podfile_path, can_cache)
  from_params(dependency.external_source, dependency, podfile_path, can_cache)
end
```

    
  

    
      
  
### 
  
    .**from_params**(params, dependency, podfile_path, can_cache)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/cocoapods/external_sources.rb', line 30

def self.from_params(params, dependency, podfile_path, can_cache)
  name = dependency.root_name
  if klass = concrete_class_from_params(params)
    klass.new(name, params, podfile_path, can_cache)
  else
    msg = "Unknown external source parameters for `#{name}`: `#{params}`"
    raise Informative, msg
  end
end
```