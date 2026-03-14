# Class: Pod::Installer
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Installer
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Config::Mixin
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/installer.rb,

  lib/cocoapods/installer/xcode.rb,
 lib/cocoapods/installer/analyzer.rb,
 lib/cocoapods/installer/podfile_validator.rb,
 lib/cocoapods/installer/pod_source_preparer.rb,
 lib/cocoapods/installer/sandbox_dir_cleaner.rb,
 lib/cocoapods/installer/analyzer/pod_variant.rb,
 lib/cocoapods/installer/analyzer/specs_state.rb,
 lib/cocoapods/installer/installation_options.rb,
 lib/cocoapods/installer/pod_source_installer.rb,
 lib/cocoapods/installer/pod_source_downloader.rb,
 lib/cocoapods/installer/target_uuid_generator.rb,
 lib/cocoapods/installer/xcode/target_validator.rb,
 lib/cocoapods/installer/user_project_integrator.rb,
 lib/cocoapods/installer/analyzer/analysis_result.rb,
 lib/cocoapods/installer/analyzer/pod_variant_set.rb,
 lib/cocoapods/installer/analyzer/sandbox_analyzer.rb,
 lib/cocoapods/installer/analyzer/target_inspector.rb,
 lib/cocoapods/installer/pre_install_hooks_context.rb,
 lib/cocoapods/installer/base_install_hooks_context.rb,
 lib/cocoapods/installer/post_install_hooks_context.rb,
 lib/cocoapods/installer/pre_integrate_hooks_context.rb,
 lib/cocoapods/installer/project_cache/project_cache.rb,
 lib/cocoapods/installer/post_integrate_hooks_context.rb,
 lib/cocoapods/installer/xcode/pods_project_generator.rb,
 lib/cocoapods/installer/project_cache/target_metadata.rb,
 lib/cocoapods/installer/source_provider_hooks_context.rb,
 lib/cocoapods/installer/project_cache/target_cache_key.rb,
 lib/cocoapods/installer/sandbox_header_paths_installer.rb,
 lib/cocoapods/installer/analyzer/podfile_dependency_cache.rb,
 lib/cocoapods/installer/analyzer/target_inspection_result.rb,
 lib/cocoapods/installer/xcode/multi_pods_project_generator.rb,
 lib/cocoapods/installer/project_cache/project_cache_version.rb,
 lib/cocoapods/installer/xcode/pods_project_generator_result.rb,
 lib/cocoapods/installer/xcode/single_pods_project_generator.rb,
 lib/cocoapods/installer/analyzer/locking_dependency_analyzer.rb,
 lib/cocoapods/installer/project_cache/project_cache_analyzer.rb,
 lib/cocoapods/installer/project_cache/project_metadata_cache.rb,
 lib/cocoapods/installer/project_cache/project_installation_cache.rb,
 lib/cocoapods/installer/user_project_integrator/target_integrator.rb,
 lib/cocoapods/installer/project_cache/project_cache_analysis_result.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/target_installer.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/project_generator.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/pods_project_writer.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/pod_target_installer.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/pod_target_integrator.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/target_installer_helper.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_installer.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/target_installation_result.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/pod_target_dependency_installer.rb,
 lib/cocoapods/installer/user_project_integrator/target_integrator/xcconfig_integrator.rb,
 lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb

  
  

## Overview

  
    

The Installer is responsible of taking a Podfile and transform it in the Pods libraries. It also integrates the user project so the Pods libraries can be used out of the box.

The Installer is capable of doing incremental updates to an existing Pod installation.

The Installer gets the information that it needs mainly from 3 files:

```
- Podfile: The specification written by the user that contains
  information about targets and Pods.
- Podfile.lock: Contains information about the pods that were previously
  installed and in concert with the Podfile provides information about
  which specific version of a Pod should be installed. This file is
  ignored in update mode.
- Manifest.lock: A file contained in the Pods folder that keeps track of
  the pods installed in the local machine. This files is used once the
  exact versions of the Pods has been computed to detect if that version
  is already installed. This file is not intended to be kept under source
  control and is a copy of the Podfile.lock.

```

The Installer is designed to work in environments where the Podfile folder is under source control and environments where it is not. The rest of the files, like the user project and the workspace are assumed to be under source control.

  

  

## Defined Under Namespace

  
    
      **Modules:** ProjectCache
    
  
    
      **Classes:** Analyzer, BaseInstallHooksContext, InstallationOptions, PodSourceDownloader, PodSourceInstaller, PodSourcePreparer, PodfileValidator, PostInstallHooksContext, PostIntegrateHooksContext, PreInstallHooksContext, PreIntegrateHooksContext, SandboxDirCleaner, SandboxHeaderPathsInstaller, SourceProviderHooksContext, TargetUUIDGenerator, UserProjectIntegrator, Xcode
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        MASTER_SPECS_REPO_GIT_URL =
          
        
        

```
'https://github.com/CocoaPods/Specs.git'.freeze

```

      
    
  

  
## Installation results collapse

  

    
      
- 
  
    
      #**aggregate_targets**  ⇒ Array<AggregateTarget> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The model representations of an aggregation of pod targets generated for a target definition in the Podfile as result of the analyzer.

  

    
      
- 
  
    
      #**analysis_result**  ⇒ Analyzer::AnalysisResult 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The result of the analysis performed during installation.

  

    
      
- 
  
    
      #**generated_aggregate_targets**  ⇒ Array<AggregateTarget> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The list of aggregate targets that were generated from the installation.

  

    
      
- 
  
    
      #**generated_pod_targets**  ⇒ Array<PodTarget> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The list of pod targets that were generated from the installation.

  

    
      
- 
  
    
      #**generated_projects**  ⇒ Array<Project> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The list of projects generated from the installation.

  

    
      
- 
  
    
      #**installed_specs**  ⇒ Array<Specification> 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The specifications that were installed.

  

    
      
- 
  
    
      #**pod_target_subprojects**  ⇒ Array<Pod::Project> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The subprojects nested under pods_project.

  

    
      
- 
  
    
      #**pod_targets**  ⇒ Array<PodTarget> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The model representations of pod targets generated as result of the analyzer.

  

    
      
- 
  
    
      #**pods_project**  ⇒ Pod::Project 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The `Pods/Pods.xcodeproj` project.

  

    
      
- 
  
    
      #**target_installation_results**  ⇒ Array<Hash{String, TargetInstallationResult}> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The installation results produced by the pods project generator.

  

    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**clean_install**  ⇒ Boolean 
    

    
      (also: #clean_install?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

when incremental installation is enabled.

  

    
      
- 
  
    
      #**deployment**  ⇒ Boolean 
    

    
      (also: #deployment?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether installation should verify that there are no Podfile or Lockfile changes.

  

    
      
- 
  
    
      #**has_dependencies**  ⇒ Boolean 
    

    
      (also: #has_dependencies?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether it has dependencies.

  

    
      
- 
  
    
      #**lockfile**  ⇒ Lockfile 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The Lockfile that stores the information about the Pods previously installed on any machine.

  

    
      
- 
  
    
      #**podfile**  ⇒ Podfile 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The Podfile specification that contains the information of the Pods that should be installed.

  

    
      
- 
  
    
      #**repo_update**  ⇒ Boolean 
    

    
      (also: #repo_update?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether the spec repos should be updated.

  

    
      
- 
  
    
      #**sandbox**  ⇒ Sandbox 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The sandbox where the Pods should be installed.

  

    
      
- 
  
    
      #**update**  ⇒ Hash, ... 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Pods that have been requested to be updated or true if all Pods should be updated.

  

    
      
- 
  
    
      #**use_default_plugins**  ⇒ Boolean 
    

    
      (also: #use_default_plugins?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Whether default plugins should be used during installation.

  

    
  

  
    
## 
      Hooks
      collapse
    

    

      
        
- 
  
    
      #**development_pod_targets**(targets = pod_targets)  ⇒ Array<PodTarget> 
    

    
  
  
  
  
  
  
  
  

  
    

The targets of the development pods generated by the installation process.

  

      
    

  
    
## 
      Convenience Methods
      collapse
    

    

      
        
- 
  
    
      .**targets_from_sandbox**(sandbox, podfile, lockfile)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**analyze_project_cache**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**download_dependencies**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(sandbox, podfile, lockfile = nil)  ⇒ Installer 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**install!**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Installs the Pods.

  

      
        
- 
  
    
      #**integrate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**prepare**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**resolve_dependencies**  ⇒ Analyzer 
    

    
  
  
  
  
  
  
  
  

  
    

The analyzer used to resolve dependencies.

  

      
        
- 
  
    
      #**show_skip_pods_project_generation_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**stage_sandbox**(sandbox, pod_targets)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Stages the sandbox after analysis.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Config::Mixin

  

#config

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(sandbox, podfile, lockfile = nil)  ⇒ Installer 
  

  

  

  
    

Initialize a new instance

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 76

def initialize(sandbox, podfile, lockfile = nil)
  @sandbox  = sandbox || raise(ArgumentError, 'Missing required argument `sandbox`')
  @podfile  = podfile || raise(ArgumentError, 'Missing required argument `podfile`')
  @lockfile = lockfile

  @use_default_plugins = true
  @has_dependencies = true
  @pod_installers = []
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**aggregate_targets**  ⇒ Array<AggregateTarget>  (readonly)
  

  

  

  
    
      

```

386
387
388
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 386

def aggregate_targets
  @aggregate_targets
end

```

    
  

    
      
      
      
  
### 
  
    #**analysis_result**  ⇒ Analyzer::AnalysisResult  (readonly)
  

  

  

  
    
      

```

367
368
369
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 367

def analysis_result
  @analysis_result
end

```

    
  

    
      
      
      
  
### 
  
    #**clean_install**  ⇒ Boolean 
  

  
    Also known as:
    clean_install?
    
  

  

  
    

when incremental installation is enabled.

  

  

  
    
      

```

118
119
120
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 118

def clean_install
  @clean_install
end

```

    
  

    
      
      
      
  
### 
  
    #**deployment**  ⇒ Boolean 
  

  
    Also known as:
    deployment?
    
  

  

  
    
      

```

112
113
114
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 112

def deployment
  @deployment
end

```

    
  

    
      
      
      
  
### 
  
    #**generated_aggregate_targets**  ⇒ Array<AggregateTarget>  (readonly)
  

  

  

  
    
      

```

403
404
405
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 403

def generated_aggregate_targets
  @generated_aggregate_targets
end

```

    
  

    
      
      
      
  
### 
  
    #**generated_pod_targets**  ⇒ Array<PodTarget>  (readonly)
  

  

  

  
    
      

```

399
400
401
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 399

def generated_pod_targets
  @generated_pod_targets
end

```

    
  

    
      
      
      
  
### 
  
    #**generated_projects**  ⇒ Array<Project>  (readonly)
  

  

  

  
    
      

```

395
396
397
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 395

def generated_projects
  @generated_projects
end

```

    
  

    
      
      
      
  
### 
  
    #**has_dependencies**  ⇒ Boolean 
  

  
    Also known as:
    has_dependencies?
    
  

  

  
    
      

```

95
96
97
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 95

def has_dependencies
  @has_dependencies
end

```

    
  

    
      
      
      
  
### 
  
    #**installed_specs**  ⇒ Array<Specification> 
  

  

  

  
    
      

```

407
408
409
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 407

def installed_specs
  @installed_specs
end

```

    
  

    
      
      
      
  
### 
  
    #**lockfile**  ⇒ Lockfile  (readonly)
  

  

  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 68

def lockfile
  @lockfile
end

```

    
  

    
      
      
      
  
### 
  
    #**pod_target_subprojects**  ⇒ Array<Pod::Project>  (readonly)
  

  

  

  
    
      

```

380
381
382
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 380

def pod_target_subprojects
  @pod_target_subprojects
end

```

    
  

    
      
      
      
  
### 
  
    #**pod_targets**  ⇒ Array<PodTarget>  (readonly)
  

  

  

  
    
      

```

391
392
393
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 391

def pod_targets
  @pod_targets
end

```

    
  

    
      
      
      
  
### 
  
    #**podfile**  ⇒ Podfile  (readonly)
  

  

  

  
    
      

```

63
64
65
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 63

def podfile
  @podfile
end

```

    
  

    
      
      
      
  
### 
  
    #**pods_project**  ⇒ Pod::Project  (readonly)
  

  

  

  
    
      

```

376
377
378
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 376

def pods_project
  @pods_project
end

```

    
  

    
      
      
      
  
### 
  
    #**repo_update**  ⇒ Boolean 
  

  
    Also known as:
    repo_update?
    
  

  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 100

def repo_update
  @repo_update
end

```

    
  

    
      
      
      
  
### 
  
    #**sandbox**  ⇒ Sandbox  (readonly)
  

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 58

def sandbox
  @sandbox
end

```

    
  

    
      
      
      
  
### 
  
    #**target_installation_results**  ⇒ Array<Hash{String, TargetInstallationResult}>  (readonly)
  

  

  

  
    
      

```

372
373
374
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 372

def target_installation_results
  @target_installation_results
end

```

    
  

    
      
      
      
  
### 
  
    #**update**  ⇒ Hash, ... 
  

  

  

  
    
      

```

91
92
93
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 91

def update
  @update
end

```

    
  

    
      
      
      
  
### 
  
    #**use_default_plugins**  ⇒ Boolean 
  

  
    Also known as:
    use_default_plugins?
    
  

  

  
    
      

```

106
107
108
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 106

def use_default_plugins
  @use_default_plugins
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**targets_from_sandbox**(sandbox, podfile, lockfile)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Informative)
      
      
      
    
  

  
    
      

```

1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 1093

def self.targets_from_sandbox(sandbox, podfile, lockfile)
  raise Informative, 'You must run `pod install` to be able to generate target information' unless lockfile

  new(sandbox, podfile, lockfile).instance_exec do
    plugin_sources = run_source_provider_hooks
    analyzer = create_analyzer(plugin_sources)
    analyze(analyzer)
    if analysis_result.podfile_needs_install?
      raise Pod::Informative, 'The Podfile has changed, you must run `pod install`'
    elsif analysis_result.sandbox_needs_install?
      raise Pod::Informative, 'The `Pods` directory is out-of-date, you must run `pod install`'
    end

    aggregate_targets
  end
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**analyze_project_cache**  ⇒ Object 
  

  

  

  
    
      

```

191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 191

def analyze_project_cache
  user_projects = aggregate_targets.map(&:user_project).compact.uniq
  object_version = user_projects.min_by { |p| p.object_version.to_i }.object_version.to_i unless user_projects.empty?

  if !installation_options.incremental_installation
    # Run entire installation.
    ProjectCache::ProjectCacheAnalysisResult.new(pod_targets, aggregate_targets, {},
                                                 analysis_result.all_user_build_configurations, object_version)
  else
    UI.message 'Analyzing Project Cache' do
      @installation_cache = ProjectCache::ProjectInstallationCache.from_file(sandbox, sandbox.project_installation_cache_path)
      @metadata_cache = ProjectCache::ProjectMetadataCache.from_file(sandbox, sandbox.project_metadata_cache_path)
      @project_cache_version = ProjectCache::ProjectCacheVersion.from_file(sandbox.project_version_cache_path)

      force_clean_install = clean_install || project_cache_version.version != Version.create(VersionMetadata.project_cache_version)
      cache_result = ProjectCache::ProjectCacheAnalyzer.new(sandbox, installation_cache, analysis_result.all_user_build_configurations,
                                                            object_version, plugins, pod_targets, aggregate_targets, installation_options.to_h, :clean_install => force_clean_install).analyze
      aggregate_targets_to_generate = cache_result.aggregate_targets_to_generate || []
      pod_targets_to_generate = cache_result.pod_targets_to_generate
      (aggregate_targets_to_generate + pod_targets_to_generate).each do |target|
        UI.message "- Regenerating #{target.label}"
      end
      cache_result
    end
  end
end

```

    
  

    
      
  
### 
  
    #**development_pod_targets**(targets = pod_targets)  ⇒ Array<PodTarget> 
  

  

  

  
    
      

```

1056
1057
1058
1059
1060
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 1056

def development_pod_targets(targets = pod_targets)
  targets.select do |pod_target|
    sandbox.local?(pod_target.pod_name)
  end
end

```

    
  

    
      
  
### 
  
    #**download_dependencies**  ⇒ Object 
  

  

  

  
    
      

```

256
257
258
259
260
261
262
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 256

def download_dependencies
  UI.section 'Downloading dependencies' do
    install_pod_sources
    run_podfile_pre_install_hooks
    clean_pod_sources
  end
end

```

    
  

    
      
  
### 
  
    #**install!**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Installs the Pods.

The installation process is mostly linear with a few minor complications to keep in mind:

- 

The stored podspecs need to be cleaned before the resolution step otherwise the sandbox might return an old podspec and not download the new one from an external source.

- 

The resolver might trigger the download of Pods from external sources necessary to retrieve their podspec (unless it is instructed not to do it).

  

  

  
    
      

```

160
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
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 160

def install!
  prepare
  resolve_dependencies
  download_dependencies
  validate_targets
  clean_sandbox
  if installation_options.skip_pods_project_generation?
    show_skip_pods_project_generation_message
    run_podfile_post_install_hooks
  else
    integrate
  end
  write_lockfiles
  perform_post_install_actions
end

```

    
  

    
      
  
### 
  
    #**integrate**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/cocoapods/installer.rb', line 181

def integrate
  run_podfile_pre_integrate_hooks
  generate_pods_project
  if installation_options.integrate_targets?
    integrate_user_project
  else
    UI.section 'Skipping User Project Integration'
  end
end

```

    
  

    
      
  
### 
  
    #**prepare**  ⇒ Object 
  

  

  

  
    
      

```

218
219
220
221
222
223
224
225
226
227
228
229
230
231
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 218

def prepare
  # Raise if pwd is inside Pods
  if Dir.pwd.start_with?(sandbox.root.to_path)
    message = 'Command should be run from a directory outside Pods directory.'
    message << "\n\n\tCurrent directory is #{UI.path(Pathname.pwd)}\n"
    raise Informative, message
  end
  UI.message 'Preparing' do
    deintegrate_if_different_major_version
    sandbox.prepare
    ensure_plugins_are_installed!
    run_plugins_pre_install_hooks
  end
end

```

    
  

    
      
  
### 
  
    #**resolve_dependencies**  ⇒ Analyzer 
  

  

  

  
    
      

```

235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 235

def resolve_dependencies
  plugin_sources = run_source_provider_hooks
  analyzer = create_analyzer(plugin_sources)

  UI.section 'Updating local specs repositories' do
    analyzer.update_repositories
  end if repo_update?

  UI.section 'Analyzing dependencies' do
    analyze(analyzer)
    validate_build_configurations
  end

  UI.section 'Verifying no changes' do
    verify_no_podfile_changes!
    verify_no_lockfile_changes!
  end if deployment?

  analyzer
end

```

    
  

    
      
  
### 
  
    #**show_skip_pods_project_generation_message**  ⇒ Object 
  

  

  

  
    
      

```

176
177
178
179
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 176

def show_skip_pods_project_generation_message
  UI.section 'Skipping Pods Project Creation'
  UI.section 'Skipping User Project Integration'
end

```

    
  

    
      
  
### 
  
    #**stage_sandbox**(sandbox, pod_targets)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Stages the sandbox after analysis.

  

  

  
    
      

```

274
275
276
```

    
    
      

```
# File 'lib/cocoapods/installer.rb', line 274

def stage_sandbox(sandbox, pod_targets)
  SandboxHeaderPathsInstaller.new(sandbox, pod_targets).install!
end

```