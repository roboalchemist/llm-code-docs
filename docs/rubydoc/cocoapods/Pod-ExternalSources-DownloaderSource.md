# Class: Pod::ExternalSources::DownloaderSource
  
    Inherits:
    
      AbstractExternalSource
      
        

          
- Object

- AbstractExternalSource

- Pod::ExternalSources::DownloaderSource

        show all
      

    Defined in:
    lib/cocoapods/external_sources/downloader_source.rb
  
## Overview

    **Note:**
    

The podspec must be in the root of the repository and should have a name matching the one of the dependency.

Provides support for fetching a specification file from a source handled by the downloader. Supports all the options of the downloader

## Instance Attribute Summary

### Attributes inherited from AbstractExternalSource

# can_cache, #name, #params, #podfile_path

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**description**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**fetch**(sandbox)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from AbstractExternalSource

# ==, #initialize

## Constructor Details

This class inherits a constructor from Pod::ExternalSources::AbstractExternalSource
  
## Instance Method Details

###
  
    #**description**  ⇒ Object 
  

  

  

  
    

See Also:
  
- AbstractExternalSource#description

```

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
# File 'lib/cocoapods/external_sources/downloader_source.rb', line 18

def description
  strategy = Downloader.strategy_from_options(params)
  options = params.dup
  url = options.delete(strategy)
  result = "from `#{url}`"
  options.each do |key, value|
    result << ", #{key} `#{value}`"
  end
  result
end
```

###
  
    #**fetch**(sandbox)  ⇒ Object 
  

  

  

  
    

See Also:
  
- AbstractExternalSource#fetch

```

12
13
14
```

```
# File 'lib/cocoapods/external_sources/downloader_source.rb', line 12

def fetch(sandbox)
  pre_download(sandbox)
end
```
