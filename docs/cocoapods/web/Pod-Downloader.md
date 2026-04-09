# Module: Pod::Downloader
  
    Defined in:
    lib/cocoapods/downloader.rb,

  lib/cocoapods/downloader/cache.rb,
 lib/cocoapods/downloader/request.rb,
 lib/cocoapods/downloader/response.rb

## Defined Under Namespace

      **Classes:** Base, Cache, DownloaderError, Request, Response
    
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**download**(request, target, can_cache: true, cache_path: Config.instance.cache_root + 'Pods')  ⇒ Response 
    

    
  
  
  
  
  
  
  
  

  
    

Downloads a pod from the given `request` to the given `target` location.

-
  
      .**download_request**(request, target)  ⇒ Response, Hash<String,Specification> 

Performs the download from the given `request` to the given `target` location.

## Class Method Details

###
  
    .**download**(request, target, can_cache: true, cache_path: Config.instance.cache_root + 'Pods')  ⇒ Response 
  

  

  

  
    

Downloads a pod from the given `request` to the given `target` location.

Parameters:

-

the request that describes this pod download.

-

the location to which this pod should be downloaded. If `nil`, then the pod will only be cached.

-

        *(defaults to: true)*

whether caching is allowed.

-

        *(defaults to: Config.instance.cache_root + 'Pods')*

the path used to cache pod downloads.

Returns:

-

The download response for this download.

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
```

```
# File 'lib/cocoapods/downloader.rb', line 29

def self.download(
  request,
  target,
  can_cache: true,
  cache_path: Config.instance.cache_root + 'Pods'
)
  can_cache &&= !Config.instance.skip_download_cache

  request = preprocess_request(request)

  if can_cache
    raise ArgumentError, 'Must provide a `cache_path` when caching.' unless cache_path
    cache = Cache.new(cache_path)
    result = cache.download_pod(request)
  else
    raise ArgumentError, 'Must provide a `target` when caching is disabled.' unless target

    require 'cocoapods/installer/pod_source_preparer'
    result, = download_request(request, target)
    Installer::PodSourcePreparer.new(result.spec, result.location).prepare!
  end

  if target && result.location && target != result.location
    UI.message "Copying #{request.name} from `#{result.location}` to #{UI.path target}", '> ' do
      Cache.read_lock(result.location) do
        FileUtils.rm_rf target
        FileUtils.cp_r(result.location, target)
      end
    end
  end
  result
end

```

###
  
    .**download_request**(request, target)  ⇒ Response, Hash<String,Specification> 
  

  

  

  
    

Performs the download from the given `request` to the given `target` location.

Parameters:

-

the request that describes this pod download.

-

the location to which this pod should be downloaded. If `nil`, then the pod will only be cached.

Returns:

-

The download response for this download, and the specifications for this download grouped by name.

```

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
89
90
91
92
93
94
```

```
# File 'lib/cocoapods/downloader.rb', line 75

def self.download_request(request, target)
  result = Response.new
  result.checkout_options = download_source(target, request.params)
  result.location = target

  if request.released_pod?
    result.spec = request.spec
    podspecs = { request.name => request.spec }
  else
    podspecs = Sandbox::PodspecFinder.new(target).podspecs
    podspecs[request.name] = request.spec if request.spec
    podspecs.each do |name, spec|
      if request.name == name
        result.spec = spec
      end
    end
  end

  [result, podspecs]
end

```
