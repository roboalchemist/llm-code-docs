# Class: Pod::Sandbox::HeadersStore
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Sandbox::HeadersStore

        show all
      

    Defined in:
    lib/cocoapods/sandbox/headers_store.rb
  
## Overview

Provides support for managing a header directory. It also keeps track of the header search paths.

## Defined Under Namespace

      **Classes:** SEARCH_PATHS_KEY
    
  
## Instance Attribute Summary collapse

-
  
      #**sandbox**  ⇒ Sandbox 

      readonly
    
    
  
  
  
  
  

  
    

The sandbox where this header directory is stored.

##

      Adding headers
      collapse
    

    

      
        
-
  
      #**add_file**(namespace, relative_header_path, mkdir: true)  ⇒ Pathname 
    

    
  
  
  
  
  
  
  
  

  
    

Adds a header to the directory.

-
  
      #**add_files**(namespace, relative_header_paths)  ⇒ Array<Pathname> 

Adds headers to the directory.

-
  
      #**add_search_path**(path, platform)  ⇒ void 

Adds an header search path to the sandbox.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**implode!**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Removes the entire root directory.

-
  
      #**implode_path!**(path)  ⇒ void 

Removes the directory at the given path relative to the root.

-
  
      #**initialize**(sandbox, relative_path, visibility_scope)  ⇒ HeadersStore 

    constructor
  
  
  
  
  
  

  
    

A new instance of HeadersStore.

-
  
      #**root**  ⇒ Pathname 

The absolute path of this header directory.

-
  
      #**search_paths**(platform, target_name = nil, use_modular_headers = false)  ⇒ Array<String> 

All the search paths of the header directory in xcconfig format.

## Constructor Details

###
  
    #**initialize**(sandbox, relative_path, visibility_scope)  ⇒ HeadersStore 
  

  

  

  
    

Returns a new instance of HeadersStore.

Parameters:

-

        @see

        (Sandbox)
      
      
      
        —
        

# sandbox

-

        relative_path

        (String)
      
      
      
        —
        

the relative path to the sandbox root and hence to the Pods project.

-

        visibility_scope

        (Symbol)
      
      
      
        —
        

the header visibility scope to use in this store. Can be `:private` or `:public`.

```

28
29
30
31
32
33
34
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 28

def initialize(sandbox, relative_path, visibility_scope)
  @sandbox       = sandbox
  @relative_path = relative_path
  @search_paths  = []
  @search_paths_cache = {}
  @visibility_scope = visibility_scope
end

```

## Instance Attribute Details

###
  
    #**sandbox**  ⇒ Sandbox  (readonly)
  

  

  

  
    

Returns the sandbox where this header directory is stored.

Returns:

-

        (Sandbox)

        —
        

the sandbox where this header directory is stored.

```

17
18
19
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 17

def sandbox
  @sandbox
end

```

## Instance Method Details

###
  
    #**add_file**(namespace, relative_header_path, mkdir: true)  ⇒ Pathname 
  

  

  

  
    
  
    **Note:**
    

This method does *not* add the file to the search paths.

Adds a header to the directory.

Parameters:

-

        namespace

        (Pathname)
      
      
      
        —
        

the path where the header file should be stored relative to the headers directory.

-

        relative_header_path

        (Pathname)
      
      
      
        —
        

the path of the header file relative to the Pods project (`PODS_ROOT` variable of the xcconfigs).

Returns:

-

        (Pathname)

```

132
133
134
135
136
137
138
139
140
141
142
143
144
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 132

def add_file(namespace, relative_header_path, mkdir: true)
  namespaced_path = root + namespace
  namespaced_path.mkpath if mkdir

  absolute_source = (sandbox.root + relative_header_path)
  source = absolute_source.relative_path_from(namespaced_path)
  if Gem.win_platform?
    FileUtils.ln(absolute_source, namespaced_path, :force => true)
  else
    FileUtils.ln_sf(source, namespaced_path)
  end
  namespaced_path + relative_header_path.basename
end

```

###
  
    #**add_files**(namespace, relative_header_paths)  ⇒ Array<Pathname> 
  

  

  

  
    
  
    **Note:**
    

This method does *not* add the files to the search paths.

Adds headers to the directory.

Parameters:

-

        namespace

        (Pathname)
      
      
      
        —
        

the path where the header file should be stored relative to the headers directory.

-

        relative_header_paths

        (Array<Pathname>)
      
      
      
        —
        

the path of the header file relative to the Pods project (`PODS_ROOT` variable of the xcconfigs).

Returns:

-

        (Array<Pathname>)

```

111
112
113
114
115
116
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 111

def add_files(namespace, relative_header_paths)
  root.join(namespace).mkpath unless relative_header_paths.empty?
  relative_header_paths.map do |relative_header_path|
    add_file(namespace, relative_header_path, :mkdir => false)
  end
end

```

###
  
    #**add_search_path**(path, platform)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Adds an header search path to the sandbox.

Parameters:

-

        path

        (Pathname)
      
      
      
        —
        

the path to add.

-

        platform

        (String)
      
      
      
        —
        

the platform the search path applies to

```

156
157
158
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 156

def add_search_path(path, platform)
  @search_paths << { :platform => platform.name, :path => File.join(@relative_path, path) }
end

```

###
  
    #**implode!**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Removes the entire root directory.

```

75
76
77
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 75

def implode!
  root.rmtree if root.exist?
end

```

###
  
    #**implode_path!**(path)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Removes the directory at the given path relative to the root.

Parameters:

-

        path

        (Pathname)
      
      
      
        —
        

The path used to join with #root and remove.

```

86
87
88
89
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 86

def implode_path!(path)
  path = root.join(path)
  path.rmtree if path.exist?
end

```

###
  
    #**root**  ⇒ Pathname 
  

  

  

  
    

Returns the absolute path of this header directory.

Returns:

-

        (Pathname)

        —
        

the absolute path of this header directory.

```

11
12
13
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 11

def root
  sandbox.headers_root + @relative_path
end

```

###
  
    #**search_paths**(platform, target_name = nil, use_modular_headers = false)  ⇒ Array<String> 
  

  

  

  
    

Returns All the search paths of the header directory in xcconfig format. The paths are specified relative to the pods root with the ‘$PODS_ROOT` variable.

Parameters:

-

        platform

        (Platform)
      
      
      
        —
        

the platform for which the header search paths should be returned.

-

        target_name

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

the target for which the header search paths should be returned. Can be `nil` in which case all headers that match the platform will be returned.

-

        use_modular_headers

        (Boolean)
      
      
        *(defaults to: false)*
      
      
        —
        

whether the search paths generated should use modular (stricter) style.

Returns:

-

        (Array<String>)

        —
        

All the search paths of the header directory in xcconfig format. The paths are specified relative to the pods root with the ‘$PODS_ROOT` variable.

```

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
69
```

```
# File 'lib/cocoapods/sandbox/headers_store.rb', line 52

def search_paths(platform, target_name = nil, use_modular_headers = false)
  key = SEARCH_PATHS_KEY.new(platform.name, target_name, use_modular_headers)
  if (cached = @search_paths_cache[key])
    return cached
  end
  search_paths = @search_paths.select do |entry|
    matches_platform = entry[:platform] == platform.name
    matches_target = target_name.nil? || (File.basename(entry[:path]) == target_name)
    matches_platform && matches_target
  end
  headers_dir = root.relative_path_from(sandbox.root).dirname
  @search_paths_cache[key] = search_paths.flat_map do |entry|
    paths = []
    paths << "${PODS_ROOT}/#{headers_dir}/#{@relative_path}" if !use_modular_headers || @visibility_scope == :public
    paths << "${PODS_ROOT}/#{headers_dir}/#{entry[:path]}" if !use_modular_headers || @visibility_scope == :private
    paths
  end.tap(&:uniq!).freeze
end

```
