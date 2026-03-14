# Class: Pod::Installer::Analyzer
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Installer::Analyzer

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Config::Mixin
  
    Defined in:
    lib/cocoapods/installer/analyzer.rb,

  lib/cocoapods/installer/analyzer/pod_variant.rb,
 lib/cocoapods/installer/analyzer/specs_state.rb,
 lib/cocoapods/installer/analyzer/analysis_result.rb,
 lib/cocoapods/installer/analyzer/pod_variant_set.rb,
 lib/cocoapods/installer/analyzer/sandbox_analyzer.rb,
 lib/cocoapods/installer/analyzer/target_inspector.rb,
 lib/cocoapods/installer/analyzer/podfile_dependency_cache.rb,
 lib/cocoapods/installer/analyzer/target_inspection_result.rb,
 lib/cocoapods/installer/analyzer/locking_dependency_analyzer.rb

## Overview

Analyzes the Podfile, the Lockfile, and the sandbox manifest to generate the information relative to a CocoaPods installation.

## Defined Under Namespace

      **Modules:** LockingDependencyAnalyzer
    
  
    
      **Classes:** AnalysisResult, PodVariant, PodVariantSet, PodfileDependencyCache, SandboxAnalyzer, SpecsState, TargetInspectionResult, TargetInspector
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        IOS_64_BIT_ONLY_VERSION =
          
  
    

Returns The version of iOS which requires binaries with only 64-bit architectures.

Returns:

-

        (String)

        —
        

The version of iOS which requires binaries with only 64-bit architectures

```
Version.new('11.0')
```

        IOS_64_BIT_ONLY_PROJECT_VERSION =
          
  
    

Xcode 10 will automatically select the correct architectures based on deployment target

Returns:

-

        (Integer)

        —
        

The Xcode object version until which 64-bit architectures should be manually specified

```
50
```

## Instance Attribute Summary collapse

-
  
      #**has_dependencies**  ⇒ Boolean 

      (also: #has_dependencies?)
    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Whether the analysis has dependencies and thus sources must be configured.

-
  
      #**installation_options**  ⇒ InstallationOptions 

      readonly
    
    
  
  
  
  
  

  
    

The installation options specified by the Podfile.

-
  
      #**lockfile**  ⇒ Lockfile? 

      readonly
    
    
  
  
  
  
  

  
    

The Lockfile, if available, that stores the information about the Pods previously installed.

-
  
      #**plugin_sources**  ⇒ Array<Source> 

      readonly
    
    
  
  
  
  
  

  
    

Sources provided by plugins or `nil`.

-
  
      #**podfile**  ⇒ Podfile 

      readonly
    
    
  
  
  
  
  

  
    

The Podfile specification that contains the information of the Pods that should be installed.

-
  
      #**pods_to_update**  ⇒ Hash, ... 

      readonly
    
    
  
  
  
  
  

  
    

Pods that have been requested to be updated or true if all Pods should be updated.

-
  
      #**sandbox**  ⇒ Sandbox 

      readonly
    
    
  
  
  
  
  

  
    

The sandbox to use for this analysis.

-
  
      #**sources_manager**  ⇒ Source::Manager 

      readonly
    
    
  
  
  
  
  

  
    

The sources manager to use when resolving dependencies.

##

      Analysis steps
      collapse
    

    

      
        
-
  
      .**requires_64_bit_archs?**(platform, object_version)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether the platform requires 64-bit architectures.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**analyze**(allow_fetches = true)  ⇒ AnalysisResult 
    

    
  
  
  
  
  
  
  
  

  
    

Performs the analysis.

-
  
      #**initialize**(sandbox, podfile, lockfile = nil, plugin_sources = nil, has_dependencies = true, pods_to_update = false, sources_manager = Source::Manager.new(config.repos_dir))  ⇒ Analyzer 

    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

-
  
      #**sources**  ⇒ Array<Source> 

Returns the sources used to query for specifications.

-
  
      #**update_repositories**  ⇒ Object 

Updates the git source repositories.

### Methods included from Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(sandbox, podfile, lockfile = nil, plugin_sources = nil, has_dependencies = true, pods_to_update = false, sources_manager = Source::Manager.new(config.repos_dir))  ⇒ Analyzer 
  

  

  

  
    

Initialize a new instance

Parameters:

-

        sandbox

        (Sandbox)
      
      
      
        —
        

@see #sandbox

-

        podfile

        (Podfile)
      
      
      
        —
        

@see #podfile

-

        lockfile

        (Lockfile, nil)
      
      
        *(defaults to: nil)*
      
      
        —
        

@see #lockfile

-

        plugin_sources

        (Array<Source>)
      
      
        *(defaults to: nil)*
      
      
        —
        

@see #plugin_sources

-

        has_dependencies

        (Boolean)
      
      
        *(defaults to: true)*
      
      
        —
        

@see #has_dependencies

-

        pods_to_update

        (Hash, Boolean, nil)
      
      
        *(defaults to: false)*
      
      
        —
        

@see #pods_to_update

-

        sources_manager

        (Source::Manager)
      
      
        *(defaults to: Source::Manager.new(config.repos_dir))*
      
      
        —
        

@see #sources_manager

```

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
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 76

def initialize(sandbox, podfile, lockfile = nil, plugin_sources = nil, has_dependencies = true,
               pods_to_update = false, sources_manager = Source::Manager.new(config.repos_dir))
  @sandbox  = sandbox
  @podfile  = podfile
  @lockfile = lockfile
  @plugin_sources = plugin_sources
  @has_dependencies = has_dependencies
  @pods_to_update = pods_to_update
  @installation_options = podfile.installation_options
  @podfile_dependency_cache = PodfileDependencyCache.from_podfile(podfile)
  @sources_manager = sources_manager
  @path_lists = {}
  @result = nil
end
```

## Instance Attribute Details

###
  
    #**has_dependencies**  ⇒ Boolean  (readonly)
  

  
    Also known as:
    has_dependencies?
    
  

  

  
    
  
    **Note:**
    

This is used by the ‘pod lib lint` command to prevent update of specs when not needed.

Returns Whether the analysis has dependencies and thus sources must be configured.

Returns:

-

        (Boolean)

        —
        

Whether the analysis has dependencies and thus sources must be configured.

```

50
51
52
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 50

def has_dependencies
  @has_dependencies
end
```

###
  
    #**installation_options**  ⇒ InstallationOptions  (readonly)
  

  

  

  
    

Returns the installation options specified by the Podfile.

Returns:

-

        (InstallationOptions)

        —
        

the installation options specified by the Podfile

```

60
61
62
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 60

def installation_options
  @installation_options
end
```

###
  
    #**lockfile**  ⇒ Lockfile?  (readonly)
  

  

  

  
    

Returns The Lockfile, if available, that stores the information about the Pods previously installed.

Returns:

-

        (Lockfile, nil)

        —
        

The Lockfile, if available, that stores the information about the Pods previously installed.

```

40
41
42
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 40

def lockfile
  @lockfile
end
```

###
  
    #**plugin_sources**  ⇒ Array<Source>  (readonly)
  

  

  

  
    

Returns Sources provided by plugins or `nil`.

Returns:

-

        (Array<Source>)

        —
        

Sources provided by plugins or `nil`.

```

44
45
46
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 44

def plugin_sources
  @plugin_sources
end
```

###
  
    #**podfile**  ⇒ Podfile  (readonly)
  

  

  

  
    

Returns The Podfile specification that contains the information of the Pods that should be installed.

Returns:

-

        (Podfile)

        —
        

The Podfile specification that contains the information of the Pods that should be installed.

```

36
37
38
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 36

def podfile
  @podfile
end
```

###
  
    #**pods_to_update**  ⇒ Hash, ...  (readonly)
  

  

  

  
    

Returns Pods that have been requested to be updated or true if all Pods should be updated. This can be false if no pods should be updated.

Returns:

-

        (Hash, Boolean, nil)

        —
        

Pods that have been requested to be updated or true if all Pods should be updated. This can be false if no pods should be updated.

```

56
57
58
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 56

def pods_to_update
  @pods_to_update
end
```

###
  
    #**sandbox**  ⇒ Sandbox  (readonly)
  

  

  

  
    

Returns The sandbox to use for this analysis.

Returns:

-

        (Sandbox)

        —
        

The sandbox to use for this analysis.

```

32
33
34
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 32

def sandbox
  @sandbox
end
```

###
  
    #**sources_manager**  ⇒ Source::Manager  (readonly)
  

  

  

  
    

Returns the sources manager to use when resolving dependencies.

Returns:

-

        (Source::Manager)

        —
        

the sources manager to use when resolving dependencies

```

64
65
66
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 64

def sources_manager
  @sources_manager
end
```

## Class Method Details

###
  
    .**requires_64_bit_archs?**(platform, object_version)  ⇒ Boolean 
  

  

  

  
    

Returns Whether the platform requires 64-bit architectures.

Parameters:

-

        platform

        (Platform)
      
      
      
        —
        

The platform to build against

-

        object_version

        (String, Nil)
      
      
      
        —
        

The user project’s object version, or nil if not available

Returns:

-

        (Boolean)

        —
        

Whether the platform requires 64-bit architectures

```

1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 1142

def requires_64_bit_archs?(platform, object_version)
  return false unless platform
  case platform.name
  when :osx
    true
  when :ios
    if (version = object_version)
      platform.deployment_target >= IOS_64_BIT_ONLY_VERSION && version.to_i < IOS_64_BIT_ONLY_PROJECT_VERSION
    else
      platform.deployment_target >= IOS_64_BIT_ONLY_VERSION
    end
  when :watchos
    false
  when :tvos
    false
  end
end
```

## Instance Method Details

###
  
    #**analyze**(allow_fetches = true)  ⇒ AnalysisResult 
  

  

  

  
    

Performs the analysis.

The Podfile and the Lockfile provide the information necessary to compute which specification should be installed. The manifest of the sandbox returns which specifications are installed.

Parameters:

-

        allow_fetches

        (Boolean)
      
      
        *(defaults to: true)*
      
      
        —
        

whether external sources may be fetched

Returns:

-

        (AnalysisResult)

```

102
103
104
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
139
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 102

def analyze(allow_fetches = true)
  return @result if @result
  validate_podfile!
  validate_lockfile_version!
  if installation_options.integrate_targets?
    target_inspections = inspect_targets_to_integrate
  else
    verify_platforms_specified!
    target_inspections = {}
  end
  podfile_state = generate_podfile_state

  store_existing_checkout_options
  if allow_fetches == :outdated
    # special-cased -- we're only really resolving for outdated, rather than doing a full analysis
  elsif allow_fetches == true
    fetch_external_sources(podfile_state)
  elsif !dependencies_to_fetch(podfile_state).all?(&:local?)
    raise Informative, 'Cannot analyze without fetching dependencies since the sandbox is not up-to-date. Run `pod install` to ensure all dependencies have been fetched.' \
      "\n    The missing dependencies are:\n    \t#{dependencies_to_fetch(podfile_state).reject(&:local?).join("\n    \t")}"
  end

  locked_dependencies = generate_version_locking_dependencies(podfile_state)
  resolver_specs_by_target = resolve_dependencies(locked_dependencies)
  validate_platforms(resolver_specs_by_target)
  specifications = generate_specifications(resolver_specs_by_target)
  aggregate_targets, pod_targets = generate_targets(resolver_specs_by_target, target_inspections)
  sandbox_state = generate_sandbox_state(specifications)
  specs_by_target = resolver_specs_by_target.each_with_object({}) do |rspecs_by_target, hash|
    hash[rspecs_by_target[0]] = rspecs_by_target[1].map(&:spec)
  end
  specs_by_source = Hash[resolver_specs_by_target.values.flatten(1).group_by(&:source).map do |source, specs|
    [source, specs.map(&:spec).uniq]
  end]
  sources.each { |s| specs_by_source[s] ||= [] }
  @result = AnalysisResult.new(podfile_state, specs_by_target, specs_by_source, specifications, sandbox_state,
                               aggregate_targets, pod_targets, @podfile_dependency_cache)
end
```

###
  
    #**sources**  ⇒ Array<Source> 
  

  

  

  
    

Returns the sources used to query for specifications.

When no explicit Podfile sources or plugin sources are defined, this defaults to the master spec repository.

Returns:

-

        (Array<Source>)

        —
        

the sources to be used in finding specifications, as specified by the podfile or all sources.

```

161
162
163
164
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
183
184
185
186
187
188
189
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 161

def sources
  @sources ||= begin
    sources = podfile.sources
    plugin_sources = @plugin_sources || []

    # Add any sources specified using the :source flag on individual dependencies.
    dependency_sources = podfile_dependencies.map(&:podspec_repo).compact
    all_dependencies_have_sources = dependency_sources.count == podfile_dependencies.count

    if all_dependencies_have_sources
      sources = dependency_sources
    elsif has_dependencies? && sources.empty? && plugin_sources.empty?
      sources = [Pod::TrunkSource::TRUNK_REPO_URL] + dependency_sources
    else
      sources += dependency_sources
    end

    result = sources.uniq.map do |source_url|
      sources_manager.find_or_create_source_with_url(source_url)
    end
    unless plugin_sources.empty?
      result.insert(0, *plugin_sources)
      plugin_sources.each do |source|
        sources_manager.add_source(source)
      end
    end
    result
  end
end
```

###
  
    #**update_repositories**  ⇒ Object 
  

  

  

  
    

Updates the git source repositories.

```

143
144
145
146
147
148
149
150
151
152
```

```
# File 'lib/cocoapods/installer/analyzer.rb', line 143

def update_repositories
  sources.each do |source|
    if source.updateable?
      sources_manager.update(source.name, true)
    else
      UI.message "Skipping `#{source.name}` update because the repository is not an updateable repository."
    end
  end
  @specs_updated = true
end
```
