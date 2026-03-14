# Class: Pod::Config
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Config

        show all
      

    Defined in:
    lib/cocoapods/config.rb
  
## Overview

Stores the global configuration of CocoaPods.

## Defined Under Namespace

      **Modules:** Mixin
    
  
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        DEFAULTS =
          
  
    

The default settings for the configuration.

Users can specify custom settings in ‘~/.cocoapods/config.yaml`. An example of the contents of this file might look like:

```
---
skip_repo_update: true
new_version_message: false

```

```
{
  :verbose             => false,
  :silent              => false,
  :skip_download_cache => !ENV['COCOAPODS_SKIP_CACHE'].nil?,

  :new_version_message => ENV['COCOAPODS_SKIP_UPDATE_MESSAGE'].nil?,

  :cache_root          => Pathname.new(Dir.home) + 'Library/Caches/CocoaPods',
}
```

## UI collapse

-
  
      #**allow_root**  ⇒ Boolean 

      (also: #allow_root?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether CocoaPods is allowed to run as root.

-
  
      #**new_version_message**  ⇒ Boolean 

      (also: #new_version_message?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether a message should be printed when a new version of CocoaPods is available.

-
  
      #**silent**  ⇒ Boolean 

      (also: #silent?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether CocoaPods should produce not output.

## Installation collapse

-
  
      #**skip_download_cache**  ⇒ Boolean 

      (also: #skip_download_cache?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether the installer should skip the download cache.

## Cache collapse

-
  
      #**cache_root**  ⇒ Pathname 

The directory where CocoaPods should cache remote data and other expensive to compute information.

## Initialization collapse

-
  
      #**verbose**  ⇒ Boolean 

Whether CocoaPods should provide detailed output about the performed actions.

## Paths collapse

-
  
      #**installation_root**  ⇒ Pathname 

      (also: #project_root)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

The root of the CocoaPods installation where the Podfile is located.

-
  
      #**podfile**  ⇒ Podfile, Nil 

-
  
      #**repos_dir**  ⇒ Pathname 

The directory where the CocoaPods sources are stored.

-
  
      #**sandbox_root**  ⇒ Pathname 

      (also: #project_pods_root)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

The root of the sandbox.

## Singleton collapse

-
  
      .**instance**  ⇒ Config 

The current config instance creating one if needed.

##

      UI
      collapse
    

    

      
        
-
  
      #**verbose?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether CocoaPods should provide detailed output about the performed actions.

##

      Initialization
      collapse
    

    

      
        
-
  
      #**initialize**(use_user_settings = true)  ⇒ Config 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Config.

##

      Paths
      collapse
    

    

      
        
-
  
      #**default_podfile_path**  ⇒ Pathname 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the path of the default Podfile pods.

-
  
      #**default_test_podfile_path**  ⇒ Pathname 

Returns the path of the default Podfile test pods.

-
  
      #**home_dir**  ⇒ Pathname 

The directory where repos, templates and configuration files are stored.

-
  
      #**lockfile**  ⇒ Lockfile, Nil 

-
  
      #**lockfile_path**  ⇒ Object 

Returns the path of the Lockfile.

-
  
      #**podfile_path**  ⇒ Pathname, Nil 

Returns the path of the Podfile.

-
  
      #**sandbox**  ⇒ Sandbox 

The sandbox of the current project.

-
  
      #**search_index_file**  ⇒ Pathname 

The file to use to cache the search data.

-
  
      #**sources_manager**  ⇒ Source::Manager 

The source manager for the spec repos in `repos_dir`.

-
  
      #**templates_dir**  ⇒ Pathname 

The directory where the CocoaPods templates are stored.

##

      Private helpers
      collapse
    

    

      
        
-
  
      #**exclude_from_backup**(dir)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Excludes the given dir from Time Machine backups.

-
  
      #**podfile_path_in_dir**(dir)  ⇒ Pathname, Nil 

Returns the path of the Podfile in the given dir if any exists.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**with_changes**(changes) { ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Applies the given changes to the config for the duration of the given block.

## Constructor Details

###
  
    #**initialize**(use_user_settings = true)  ⇒ Config 
  

  

  

  
    

Returns a new instance of Config.

```

105
106
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
```

```
# File 'lib/cocoapods/config.rb', line 105

def initialize(use_user_settings = true)
  configure_with(DEFAULTS)

  unless ENV['CP_HOME_DIR'].nil?
    @cache_root = home_dir + 'cache'
  end

  if use_user_settings && user_settings_file.exist?
    require 'yaml'
    user_settings_contents = File.read(user_settings_file)
    user_settings = YAML.safe_load(user_settings_contents)
    configure_with(user_settings)
  end

  unless ENV['CP_CACHE_DIR'].nil?
    @cache_root = Pathname.new(ENV['CP_CACHE_DIR']).expand_path
  end
end
```

## Class Attribute Details

###
  
    .**instance**  ⇒ Config 
  

  

  

  
    

Returns the current config instance creating one if needed.

Returns:

-

the current config instance creating one if needed.

```

343
344
345
```

```
# File 'lib/cocoapods/config.rb', line 343

def self.instance
  @instance ||= new
end
```

## Instance Attribute Details

###
  
    #**allow_root**  ⇒ Boolean 
  

  
    Also known as:
    allow_root?
    
  

  

  
    

Returns Whether CocoaPods is allowed to run as root.

Returns:

-

Whether CocoaPods is allowed to run as root.

```

65
66
67
```

```
# File 'lib/cocoapods/config.rb', line 65

def allow_root
  @allow_root
end
```

###
  
    #**cache_root**  ⇒ Pathname 
  

  

  

  
    

Returns The directory where CocoaPods should cache remote data and other expensive to compute information.

Returns:

-

The directory where CocoaPods should cache remote data and other expensive to compute information.

```

92
93
94
```

```
# File 'lib/cocoapods/config.rb', line 92

def cache_root
  @cache_root
end
```

###
  
    #**installation_root**  ⇒ Pathname 
  

  
    Also known as:
    project_root
    
  

  

  
    

Returns the root of the CocoaPods installation where the Podfile is located.

Returns:

-

the root of the CocoaPods installation where the Podfile is located.

```

165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
```

```
# File 'lib/cocoapods/config.rb', line 165

def installation_root
  @installation_root ||= begin
    current_dir = Pathname.new(Dir.pwd.unicode_normalize(:nfkc))
    current_path = current_dir
    until current_path.root?
      if podfile_path_in_dir(current_path)
        installation_root = current_path
        unless current_path == current_dir
          UI.puts("[in #{current_path}]")
        end
        break
      else
        current_path = current_path.parent
      end
    end
    installation_root || current_dir
  end
end
```

###
  
    #**new_version_message**  ⇒ Boolean 
  

  
    Also known as:
    new_version_message?
    
  

  

  
    

Returns Whether a message should be printed when a new version of CocoaPods is available.

Returns:

-

Whether a message should be printed when a new version of CocoaPods is available.

```

71
72
73
```

```
# File 'lib/cocoapods/config.rb', line 71

def new_version_message
  @new_version_message
end
```

###
  
    #**podfile**  ⇒ Podfile, Nil 
  

  

  

  
    

Returns:

-

The Podfile to use for the current execution.

-

If no Podfile is available.

```

205
206
207
```

```
# File 'lib/cocoapods/config.rb', line 205

def podfile
  @podfile ||= Podfile.from_file(podfile_path) if podfile_path
end
```

###
  
    #**repos_dir**  ⇒ Pathname 
  

  

  

  
    

Returns the directory where the CocoaPods sources are stored.

Returns:

-

the directory where the CocoaPods sources are stored.

```

143
144
145
```

```
# File 'lib/cocoapods/config.rb', line 143

def repos_dir
  @repos_dir ||= Pathname.new(ENV['CP_REPOS_DIR'] || (home_dir + 'repos')).expand_path
end
```

###
  
    #**sandbox_root**  ⇒ Pathname 
  

  
    Also known as:
    project_pods_root
    
  

  

  
    

Returns The root of the sandbox.

Returns:

-

The root of the sandbox.

```

189
190
191
```

```
# File 'lib/cocoapods/config.rb', line 189

def sandbox_root
  @sandbox_root ||= installation_root + 'Pods'
end
```

###
  
    #**silent**  ⇒ Boolean 
  

  
    Also known as:
    silent?
    
  

  

  
    

Returns Whether CocoaPods should produce not output.

Returns:

-

Whether CocoaPods should produce not output.

```

60
61
62
```

```
# File 'lib/cocoapods/config.rb', line 60

def silent
  @silent
end
```

###
  
    #**skip_download_cache**  ⇒ Boolean 
  

  
    Also known as:
    skip_download_cache?
    
  

  

  
    

Returns Whether the installer should skip the download cache.

Returns:

-

Whether the installer should skip the download cache.

```

80
81
82
```

```
# File 'lib/cocoapods/config.rb', line 80

def skip_download_cache
  @skip_download_cache
end
```

###
  
    #**verbose**  ⇒ Boolean 
  

  

  

  
    

Returns Whether CocoaPods should provide detailed output about the performed actions.

Returns:

-

Whether CocoaPods should provide detailed output about the performed actions.

```

55
56
57
```

```
# File 'lib/cocoapods/config.rb', line 55

def verbose
  @verbose
end
```

## Instance Method Details

###
  
    #**default_podfile_path**  ⇒ Pathname 
  

  

  

  
    
  
    **Note:**
    

The file is expected to be named Podfile.default

Returns the path of the default Podfile pods.

Returns:

-

```

244
245
246
```

```
# File 'lib/cocoapods/config.rb', line 244

def default_podfile_path
  @default_podfile_path ||= templates_dir + 'Podfile.default'
end
```

###
  
    #**default_test_podfile_path**  ⇒ Pathname 
  

  

  

  
    
  
    **Note:**
    

The file is expected to be named Podfile.test

Returns the path of the default Podfile test pods.

Returns:

-

```

254
255
256
```

```
# File 'lib/cocoapods/config.rb', line 254

def default_test_podfile_path
  @default_test_podfile_path ||= templates_dir + 'Podfile.test'
end
```

###
  
    #**exclude_from_backup**(dir)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Excludes the given dir from Time Machine backups.

Parameters:

-

The directory to exclude from Time Machine backups.

```

330
331
332
333
```

```
# File 'lib/cocoapods/config.rb', line 330

def exclude_from_backup(dir)
  return if Gem.win_platform?
  system('tmutil', 'addexclusion', dir.to_s, %i(out err) => File::NULL)
end
```

###
  
    #**home_dir**  ⇒ Pathname 
  

  

  

  
    

Returns the directory where repos, templates and configuration files are stored.

Returns:

-

the directory where repos, templates and configuration files are stored.

```

137
138
139
```

```
# File 'lib/cocoapods/config.rb', line 137

def home_dir
  @home_dir ||= Pathname.new(ENV['CP_HOME_DIR'] || '~/.cocoapods').expand_path
end
```

###
  
    #**lockfile**  ⇒ Lockfile, Nil 
  

  

  

  
    

Returns:

-

The Lockfile to use for the current execution.

-

If no Lockfile is available.

```

213
214
215
```

```
# File 'lib/cocoapods/config.rb', line 213

def lockfile
  @lockfile ||= Lockfile.from_file(lockfile_path) if lockfile_path
end
```

###
  
    #**lockfile_path**  ⇒ Object 
  

  

  

  
    
  
    **Note:**
    

The Lockfile is named `Podfile.lock`.

Returns the path of the Lockfile.

```

234
235
236
```

```
# File 'lib/cocoapods/config.rb', line 234

def lockfile_path
  @lockfile_path ||= installation_root + 'Podfile.lock'
end
```

###
  
    #**podfile_path**  ⇒ Pathname, Nil 
  

  

  

  
    
  
    **Note:**
    

The Podfile can be named either `CocoaPods.podfile.yaml`, `CocoaPods.podfile` or `Podfile`.  The first two are preferred as they allow to specify an OS X UTI.

Returns the path of the Podfile.

Returns:

-

-

```

226
227
228
```

```
# File 'lib/cocoapods/config.rb', line 226

def podfile_path
  @podfile_path ||= podfile_path_in_dir(installation_root)
end
```

###
  
    #**podfile_path_in_dir**(dir)  ⇒ Pathname, Nil 
  

  

  

  
    

Returns the path of the Podfile in the given dir if any exists.

Parameters:

-

The directory where to look for the Podfile.

Returns:

-

The path of the Podfile.

-

If not Podfile was found in the given dir

```

313
314
315
316
317
318
319
320
321
```

```
# File 'lib/cocoapods/config.rb', line 313

def podfile_path_in_dir(dir)
  PODFILE_NAMES.each do |filename|
    candidate = dir + filename
    if candidate.file?
      return candidate
    end
  end
  nil
end
```

###
  
    #**sandbox**  ⇒ Sandbox 
  

  

  

  
    

Returns The sandbox of the current project.

Returns:

-

The sandbox of the current project.

```

198
199
200
```

```
# File 'lib/cocoapods/config.rb', line 198

def sandbox
  @sandbox ||= Sandbox.new(sandbox_root)
end
```

###
  
    #**search_index_file**  ⇒ Pathname 
  

  

  

  
    

Returns The file to use to cache the search data.

Returns:

-

The file to use to cache the search data.

```

260
261
262
```

```
# File 'lib/cocoapods/config.rb', line 260

def search_index_file
  cache_root + 'search_index.json'
end
```

###
  
    #**sources_manager**  ⇒ Source::Manager 
  

  

  

  
    

Returns the source manager for the spec repos in `repos_dir`.

Returns:

-

the source manager for the spec repos in `repos_dir`

```

151
152
153
154
```

```
# File 'lib/cocoapods/config.rb', line 151

def sources_manager
  return @sources_manager if @sources_manager && @sources_manager.repos_dir == repos_dir
  @sources_manager = Source::Manager.new(repos_dir)
end
```

###
  
    #**templates_dir**  ⇒ Pathname 
  

  

  

  
    

Returns the directory where the CocoaPods templates are stored.

Returns:

-

the directory where the CocoaPods templates are stored.

```

158
159
160
```

```
# File 'lib/cocoapods/config.rb', line 158

def templates_dir
  @templates_dir ||= Pathname.new(ENV['CP_TEMPLATES_DIR'] || (home_dir + 'templates')).expand_path
end
```

###
  
    #**verbose?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether CocoaPods should provide detailed output about the performed actions.

Returns:

-

Whether CocoaPods should provide detailed output about the performed actions.

```

56
57
58
```

```
# File 'lib/cocoapods/config.rb', line 56

def verbose
  @verbose
end
```

###
  
    #**with_changes**(changes) { ... } ⇒ Object 
  

  

  

  
    

Applies the given changes to the config for the duration of the given block.

Parameters:

-

the changes to merge temporarily with the current config

Yields:

-

is called while the changes are applied

```

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
```

```
# File 'lib/cocoapods/config.rb', line 34

def with_changes(changes)
  old = {}
  changes.keys.each do |key|
    key = key.to_sym
    old[key] = send(key) if respond_to?(key)
  end
  configure_with(changes)
  yield if block_given?
ensure
  configure_with(old)
end
```
