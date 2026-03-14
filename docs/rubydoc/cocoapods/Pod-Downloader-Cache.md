# Class: Pod::Downloader::Cache
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Downloader::Cache
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/downloader/cache.rb
  
  

## Overview

  
    

The class responsible for managing Pod downloads, transparently caching them in a cache directory.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**root**  ⇒ Pathname 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The root directory where this cache store its downloads.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**lock**(location, lock_type)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a .lock file at `location`, aquires a lock of type `lock_type`, checks that it is valid, and executes passed block while holding on to that lock.

  

      
        
- 
  
    
      .**read_lock**(location, &block)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Convenience method for acquiring a shared lock to safely read from the cache.

  

      
        
- 
  
    
      .**valid_lock?**(file, filename)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Checks that the lock is on a file that still exists on the filesystem.

  

      
        
- 
  
    
      .**write_lock**(location, &block)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Convenience method for acquiring an exclusive lock to safely write to the cache.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**cache_descriptors_per_pod**  ⇒ Hash<String, Hash<Symbol, String>> 
    

    
  
  
  
  
  
  
  
  

  
    

A hash whose keys are the pod name And values are a hash with the following keys: :spec_file : path to the spec file :name      : name of the pod :version   : pod version :release   : boolean to tell if that’s a release pod :slug      : the slug path where the pod cache is located.

  

      
        
- 
  
    
      #**download_pod**(request)  ⇒ Response 
    

    
  
  
  
  
  
  
  
  

  
    

Downloads the Pod from the given `request`.

  

      
        
- 
  
    
      #**initialize**(root)  ⇒ Cache 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root)  ⇒ Cache 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        root
      
      
        (Pathname, String)
      
      
      
        —
        

see #root

      
    
  

  
    
      

```

20
21
22
23
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 20

def initialize(root)
  @root = Pathname(root)
  ensure_matching_version
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**root**  ⇒ Pathname  (readonly)
  

  

  

  
    

Returns The root directory where this cache store its downloads.

  

  

Returns:

  
    
- 
      
      
        (Pathname)
      
      
      
        —
        

The root directory where this cache store its downloads.

      
    
  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 13

def root
  @root
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**lock**(location, lock_type)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Creates a .lock file at `location`, aquires a lock of type `lock_type`, checks that it is valid, and executes passed block while holding on to that lock. Afterwards, the .lock file is deleted, which is why validation of the lock is necessary, as you might have a lock on a file that doesn’t exist on the filesystem anymore.

  

  

Parameters:

  
    
- 
      
        location
      
      
        (Pathname)
      
      
      
        —
        

the path to require a lock for.

      
    
  
    
- 
      
        lock_type
      
      
        (locking_constant)
      
      
      
        —
        

the type of lock, either exclusive (File::LOCK_EX) or shared (File::LOCK_SH).

      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

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
130
131
132
133
134
135
136
137
138
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 117

def self.lock(location, lock_type)
  raise ArgumentError, 'no block given' unless block_given?
  lockfile = "#{location}.lock"
  f = nil
  loop do
    f.close if f
    f = File.open(lockfile, File::CREAT, 0o644)
    f.flock(lock_type)
    break if Cache.valid_lock?(f, lockfile)
  end
  begin
    yield location
  ensure
    if lock_type == File::LOCK_SH
      f.flock(File::LOCK_EX)
      File.delete(lockfile) if Cache.valid_lock?(f, lockfile)
    else
      File.delete(lockfile)
    end
    f.close
  end
end
```

    
  

    
      
  
### 
  
    .**read_lock**(location, &block)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Convenience method for acquiring a shared lock to safely read from the cache. See `Cache.lock` for more details.

  

  

Parameters:

  
    
- 
      
        location
      
      
        (Pathname)
      
      
      
        —
        

the path to require a lock for.

      
    
  
    
- 
      
        &block
      
      
        (block)
      
      
      
        —
        

the block to execute inside the lock.

      
    
  

  
    
      

```

83
84
85
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 83

def self.read_lock(location, &block)
  Cache.lock(location, File::LOCK_SH, &block)
end
```

    
  

    
      
  
### 
  
    .**valid_lock?**(file, filename)  ⇒ Boolean 
  

  

  

  
    

Checks that the lock is on a file that still exists on the filesystem.

  

  

Parameters:

  
    
- 
      
        file
      
      
        (File)
      
      
      
        —
        

the actual file that we have a lock for.

      
    
  
    
- 
      
        filename
      
      
        (String)
      
      
      
        —
        

the filename of the file that we have a lock for.

      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

true if `filename` still exists and is the same file as `file`

      
    
  

  
    
      

```

151
152
153
154
155
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 151

def self.valid_lock?(file, filename)
  file.stat.ino == File.stat(filename).ino
rescue Errno::ENOENT
  false
end
```

    
  

    
      
  
### 
  
    .**write_lock**(location, &block)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Convenience method for acquiring an exclusive lock to safely write to the cache. See `Cache.lock` for more details.

  

  

Parameters:

  
    
- 
      
        location
      
      
        (Pathname)
      
      
      
        —
        

the path to require a lock for.

      
    
  
    
- 
      
        &block
      
      
        (block)
      
      
      
        —
        

the block to execute inside the lock.

      
    
  

  
    
      

```

98
99
100
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 98

def self.write_lock(location, &block)
  Cache.lock(location, File::LOCK_EX, &block)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**cache_descriptors_per_pod**  ⇒ Hash<String, Hash<Symbol, String>> 
  

  

  

  
    

Returns A hash whose keys are the pod name And values are a hash with the following keys: :spec_file : path to the spec file :name      : name of the pod :version   : pod version :release   : boolean to tell if that’s a release pod :slug      : the slug path where the pod cache is located.

  

  

Returns:

  
    
- 
      
      
        (Hash<String, Hash<Symbol, String>>)
      
      
      
        —
        

A hash whose keys are the pod name And values are a hash with the following keys: :spec_file : path to the spec file :name      : name of the pod :version   : pod version :release   : boolean to tell if that’s a release pod :slug      : the slug path where the pod cache is located

      
    
  

  
    
      

```

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
69
70
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 50

def cache_descriptors_per_pod
  specs_dir = root + 'Specs'
  release_specs_dir = specs_dir + 'Release'
  return {} unless specs_dir.exist?

  spec_paths = specs_dir.find.select { |f| f.fnmatch('*.podspec.json') }
  spec_paths.reduce({}) do |hash, spec_path|
    spec = Specification.from_file(spec_path)
    hash[spec.name] ||= []
    is_release = spec_path.to_s.start_with?(release_specs_dir.to_s)
    request = Downloader::Request.new(:spec => spec, :released => is_release)
    hash[spec.name] << {
      :spec_file => spec_path,
      :name => spec.name,
      :version => spec.version,
      :release => is_release,
      :slug => root + request.slug,
    }
    hash
  end
end
```

    
  

    
      
  
### 
  
    #**download_pod**(request)  ⇒ Response 
  

  

  

  
    

Downloads the Pod from the given `request`

  

  

Parameters:

  
    
- 
      
        request
      
      
        (Request)
      
      
      
        —
        

the request to be downloaded.

      
    
  

Returns:

  
    
- 
      
      
        (Response)
      
      
      
        —
        

the response from downloading `request`

      
    
  

  
    
      

```

32
33
34
35
36
37
38
39
```

    
    
      

```
# File 'lib/cocoapods/downloader/cache.rb', line 32

def download_pod(request)
  cached_pod(request) || uncached_pod(request)
rescue Informative
  raise
rescue
  UI.puts("\n[!] Error installing #{request.name}".red)
  raise
end
```