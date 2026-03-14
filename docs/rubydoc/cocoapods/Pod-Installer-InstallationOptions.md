# Class: Pod::Installer::InstallationOptions
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Installer::InstallationOptions
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/installer/installation_options.rb
  
  

## Overview

  
    

Represents the installation options the user can customize via a `Podfile`.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all_options**  ⇒ Array<Symbol> 
    

    
  
  
  
  
  
  
  
  

  
    

The names of all known installation options.

  

      
        
- 
  
    
      .**defaults**  ⇒ Hash<Symbol,Object> 
    

    
  
  
  
  
  
  
  
  

  
    

All known installation options and their default values.

  

      
        
- 
  
    
      .**from_podfile**(podfile)  ⇒ Self 
    

    
  
  
  
  
  
  
  
  

  
    

Parses installation options from a podfile.

  

      
        
- 
  
    
      .**option**(name, default, boolean: true)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Defines a new installation option.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
      (also: #eql)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clean**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to clean the sources of the pods during installation.

  

      
        
- 
  
    
      #**deduplicate_targets**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to deduplicate pod targets.

  

      
        
- 
  
    
      #**deterministic_uuids**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to generate deterministic UUIDs when creating the Pods project.

  

      
        
- 
  
    
      #**disable_input_output_paths**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to disable the input & output paths of the CocoaPods script phases (Copy Frameworks & Copy Resources).

  

      
        
- 
  
    
      #**generate_multiple_pod_projects**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to generate a project per pod target.

  

      
        
- 
  
    
      #**hash**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**incremental_installation**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to enable only regenerating targets and their associate projects that have changed since the previous installation.

  

      
        
- 
  
    
      #**initialize**(options = {})  ⇒ InstallationOptions 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initializes the installation options with a hash of options from a Podfile.

  

      
        
- 
  
    
      #**integrate_targets**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to integrate the installed pods into the user project.

  

      
        
- 
  
    
      #**lock_pod_sources**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to lock the source files of pods.

  

      
        
- 
  
    
      #**parallel_pod_download_thread_pool_size**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The size of the thread pool to use when downloading pods in parallel.

  

      
        
- 
  
    
      #**parallel_pod_downloads**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to download pods in parallel before beginning the installation process.

  

      
        
- 
  
    
      #**preserve_pod_file_structure**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to preserve the file structure of all Pods, including externally sourced pods.

  

      
        
- 
  
    
      #**share_schemes_for_development_pods**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to share Xcode schemes for development pods.

  

      
        
- 
  
    
      #**skip_pods_project_generation**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to skip generating the `Pods.xcodeproj` and perform only dependency resolution and downloading.

  

      
        
- 
  
    
      #**to_h**(include_defaults: true)  ⇒ Hash 
    

    
  
  
  
  
  
  
  
  

  
    

The options, keyed by option name.

  

      
        
- 
  
    
      #**warn_for_multiple_pod_sources**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to emit a warning when multiple sources contain a Pod with the same name and version.

  

      
        
- 
  
    
      #**warn_for_unused_master_specs_repo**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether to emit a warning if a project is not explicitly specifying the git based master specs repo and can instead use CDN which is the default.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options = {})  ⇒ InstallationOptions 
  

  

  

  
    

Initializes the installation options with a hash of options from a Podfile.

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

the options to parse.

      
    
  

Raises:

  
    
- 
      
      
        (Informative)
      
      
      
        —
        

if `options` contains any unknown keys.

      
    
  

  
    
      

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
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 71

def initialize(options = {})
  options = ActiveSupport::HashWithIndifferentAccess.new(options)
  unknown_keys = options.keys - self.class.all_options.map(&:to_s)
  raise Informative, "Unknown installation options: #{unknown_keys.to_sentence}." unless unknown_keys.empty?
  self.class.defaults.each do |key, default|
    value = options.fetch(key, default)
    send("#{key}=", value)
  end
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**all_options**  ⇒ Array<Symbol> 
  

  

  

  
    

Returns the names of all known installation options.

  

  

Returns:

  
    
- 
      
      
        (Array<Symbol>)
      
      
      
        —
        

the names of all known installation options.

      
    
  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 60

def self.all_options
  defaults.keys
end
```

    
  

    
      
  
### 
  
    .**defaults**  ⇒ Hash<Symbol,Object> 
  

  

  

  
    

Returns all known installation options and their default values.

  

  

Returns:

  
    
- 
      
      
        (Hash<Symbol,Object>)
      
      
      
        —
        

all known installation options and their default values.

      
    
  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 54

def self.defaults
  @defaults ||= {}
end
```

    
  

    
      
  
### 
  
    .**from_podfile**(podfile)  ⇒ Self 
  

  

  

  
    

Parses installation options from a podfile.

  

  

Parameters:

  
    
- 
      
        podfile
      
      
        (Podfile)
      
      
      
        —
        

the podfile to parse installation options from.

      
    
  

Returns:

  
    
- 
      
      
        (Self)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (Informative)
      
      
      
        —
        

if `podfile` does not specify a `CocoaPods` install.

      
    
  

  
    
      

```

19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 19

def self.from_podfile(podfile)
  name, options = podfile.installation_method
  unless name.downcase == 'cocoapods'
    raise Informative, "Currently need to specify a `cocoapods` install, you chose `#{name}`."
  end
  new(options)
end
```

    
  

    
      
  
### 
  
    .**option**(name, default, boolean: true)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Defines a new installation option.

  

  

Parameters:

  
    
- 
      
        name
      
      
        (#to_s)
      
      
      
        —
        

the name of the option.

      
    
  
    
- 
      
        default
      
      
        
      
      
      
        —
        

the default value for the option.

      
    
  
    
- 
      
        boolean
      
      
        (Boolean)
      
      
        *(defaults to: true)*
      
      
        —
        

whether the option has a boolean value.

      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

43
44
45
46
47
48
49
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 43

def self.option(name, default, boolean: true)
  name = name.to_s
  raise ArgumentError, "The `#{name}` option is already defined" if defaults.key?(name)
  defaults[name] = default
  attr_accessor name
  alias_method "#{name}?", name if boolean
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  
    Also known as:
    eql
    
  

  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 94

def ==(other)
  other.is_a?(self.class) && to_h == other.to_h
end
```

    
  

    
      
  
### 
  
    #**clean**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to true.

  

Whether to clean the sources of the pods during installation

Cleaning removes any files not used by the pod as specified by the podspec and the platforms that the project supports

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the clean option for installation.

      
    
  

  

See Also:
  

    
      
- Pod::Installer::InstallationOptions.{PodSourceInstaller{PodSourceInstaller#clean!}
    
  

  
    
      

```

111
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 111

option :clean, true
```

    
  

    
      
  
### 
  
    #**deduplicate_targets**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to true.

  

Whether to deduplicate pod targets

Target deduplication adds suffixes to pod targets for the cases where a pod is included in multiple targets that have different requirements. For example, a pod named ‘MyPod’ with a subspec ‘SubA’ that is included in two targets as follows:

```
target 'MyTargetA' do
  pod 'MyPod/SubA'
end

target 'MyTargetB' do
  pod 'MyPod'
end

```

will result in two Pod targets: `MyPod` and `MyPod-SubA`

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the deduplicate_targets option for installation.

      
    
  

  
    
      

```

129
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 129

option :deduplicate_targets, true
```

    
  

    
      
  
### 
  
    #**deterministic_uuids**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to true.

  

Whether to generate deterministic UUIDs when creating the Pods project

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the deterministic_uuids option for installation.

      
    
  

  

See Also:
  

    
      
- Pod::Installer::InstallationOptions.{Xcodeproj{Xcodeproj#generate_uuid}
    
  

  
    
      

```

135
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 135

option :deterministic_uuids, true
```

    
  

    
      
  
### 
  
    #**disable_input_output_paths**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to false.

  

Whether to disable the input & output paths of the CocoaPods script phases (Copy Frameworks & Copy Resources)

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the disable_input_output_paths option for installation.

      
    
  

  

See Also:
  

    
      
- https://github.com/CocoaPods/CocoaPods/issues/8073
    
  

  
    
      

```

171
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 171

option :disable_input_output_paths, false
```

    
  

    
      
  
### 
  
    #**generate_multiple_pod_projects**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to false.

  

Whether to generate a project per pod target. Instead of creating 1 `Pods.xcodeproj`, this option will generate a project for every pod target that will be nested under the `Pods.xcodeproj`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the generate_multiple_pod_projects option for installation.

      
    
  

  
    
      

```

183
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 183

option :generate_multiple_pod_projects, false
```

    
  

    
      
  
### 
  
    #**hash**  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 100

def hash
  to_h.hash
end
```

    
  

    
      
  
### 
  
    #**incremental_installation**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to false.

  

Whether to enable only regenerating targets and their associate projects that have changed since the previous installation.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the incremental_installation option for installation.

      
    
  

  
    
      

```

188
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 188

option :incremental_installation, false
```

    
  

    
      
  
### 
  
    #**integrate_targets**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to true.

  

Whether to integrate the installed pods into the user project

If set to false, Pods will be downloaded and installed to the `Pods/` directory but they will not be integrated into your project.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the integrate_targets option for installation.

      
    
  

  
    
      

```

142
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 142

option :integrate_targets, true
```

    
  

    
      
  
### 
  
    #**lock_pod_sources**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

There is a performance penalty to locking the pods during installation. If this is significantly impacting the duration of ‘pod install` for your project, you can try setting this to `false`

  

  
    **Note:**
    

this option defaults to true.

  

Whether to lock the source files of pods. Xcode will prompt to unlock the files when attempting to modify their contents

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the lock_pod_sources option for installation.

      
    
  

  
    
      

```

150
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 150

option :lock_pod_sources, true
```

    
  

    
      
  
### 
  
    #**parallel_pod_download_thread_pool_size**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to 40.

  

The size of the thread pool to use when downloading pods in parallel. Only takes effect when `parallel_pod_downloads` is `true`.

Default: 40

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the parallel_pod_download_thread_pool_size option for installation.

      
    
  

  
    
      

```

203
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 203

option(:parallel_pod_download_thread_pool_size, 40, :boolean => false)
```

    
  

    
      
  
### 
  
    #**parallel_pod_downloads**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to false.

  

Whether to download pods in parallel before beginning the installation process

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the parallel_pod_downloads option for installation.

      
    
  

  
    
      

```

196
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 196

option :parallel_pod_downloads, false
```

    
  

    
      
  
### 
  
    #**preserve_pod_file_structure**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to false.

  

Whether to preserve the file structure of all Pods, including externally sourced pods.

By default, the file structure of Pod sources is preserved only for development pods. Setting `:preserve_pod_file_structure` to `true` will *always* preserve the file structure.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the preserve_pod_file_structure option for installation.

      
    
  

  
    
      

```

178
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 178

option :preserve_pod_file_structure, false
```

    
  

    
      
  
### 
  
    #**share_schemes_for_development_pods**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to false.

  

Whether to share Xcode schemes for development pods.

Schemes for development pods are created automatically but are not shared by default.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the share_schemes_for_development_pods option for installation.

      
    
  

  
    
      

```

165
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 165

option :share_schemes_for_development_pods, false
```

    
  

    
      
  
### 
  
    #**skip_pods_project_generation**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to false.

  

Whether to skip generating the `Pods.xcodeproj` and perform only dependency resolution and downloading.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the skip_pods_project_generation option for installation.

      
    
  

  
    
      

```

192
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 192

option :skip_pods_project_generation, false
```

    
  

    
      
  
### 
  
    #**to_h**(include_defaults: true)  ⇒ Hash 
  

  

  

  
    

Returns the options, keyed by option name.

  

  

Parameters:

  
    
- 
      
        include_defaults
      
      
        (Boolean)
      
      
        *(defaults to: true)*
      
      
        —
        

whether values that match the default for their option should be included. Defaults to `true`.

      
    
  

Returns:

  
    
- 
      
      
        (Hash)
      
      
      
        —
        

the options, keyed by option name.

      
    
  

  
    
      

```

86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 86

def to_h(include_defaults: true)
  self.class.defaults.reduce(ActiveSupport::HashWithIndifferentAccess.new) do |hash, (option, default)|
    value = send(option)
    hash[option] = value if include_defaults || value != default
    hash
  end
end
```

    
  

    
      
  
### 
  
    #**warn_for_multiple_pod_sources**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to true.

  

Whether to emit a warning when multiple sources contain a Pod with the same name and version

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the warn_for_multiple_pod_sources option for installation.

      
    
  

  
    
      

```

154
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 154

option :warn_for_multiple_pod_sources, true
```

    
  

    
      
  
### 
  
    #**warn_for_unused_master_specs_repo**  ⇒ Boolean 
  

  

  

  
    
  
    **Note:**
    

this option defaults to true.

  

Whether to emit a warning if a project is not explicitly specifying the git based master specs repo and can instead use CDN which is the default.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

the warn_for_unused_master_specs_repo option for installation.

      
    
  

  
    
      

```

159
```

    
    
      

```
# File 'lib/cocoapods/installer/installation_options.rb', line 159

option :warn_for_unused_master_specs_repo, true
```