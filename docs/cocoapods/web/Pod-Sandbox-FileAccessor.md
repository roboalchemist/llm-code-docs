# Class: Pod::Sandbox::FileAccessor
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Sandbox::FileAccessor

        show all
      

    Defined in:
    lib/cocoapods/sandbox/file_accessor.rb
  
## Overview

    **Note:**
    

The FileAccessor always returns absolute paths.

Resolves the file patterns of a specification against its root directory, taking into account any exclude pattern and the default extensions to use for directories.

##

      Constant Summary
      collapse
    

    
      
        HEADER_EXTENSIONS =
          
        
        

```
Xcodeproj::Constants::HEADER_FILES_EXTENSIONS

```

        SOURCE_FILE_EXTENSIONS =
          
        
        

```
(%w(.m .mm .i .c .cc .cxx .cpp .c++ .swift) + HEADER_EXTENSIONS).uniq.freeze

```

        GLOB_PATTERNS =
          
        
        

```
{
  :readme              => 'readme{*,.*}'.freeze,
  :license             => 'licen{c,s}e{*,.*}'.freeze,
  :source_files        => "*{#{SOURCE_FILE_EXTENSIONS.join(',')}}".freeze,
  :public_header_files => "*{#{HEADER_EXTENSIONS.join(',')}}".freeze,
  :podspecs            => '*.{podspec,podspec.json}'.freeze,
  :docs                => 'doc{s}{*,.*}/**/*'.freeze,
}.freeze

```

## Instance Attribute Summary collapse

-
  
      #**path_list**  ⇒ Sandbox::PathList 

      readonly
    
    
  
  
  
  
  

  
    

The directory where the source of the Pod is located.

-
  
      #**spec_consumer**  ⇒ Specification::Consumer 

      readonly
    
    
  
  
  
  
  

  
    

The consumer of the specification for which the file patterns should be resolved.

##

      Paths
      collapse
    

    

      
        
-
  
      .**all_files**(file_accessors)  ⇒ Array<Pathname> 
    

    
  
  
  
  
  
  
  
  

  
    

The list of all file accessors that a target will integrate into the project.

-
  
      .**vendored_frameworks_headers**(framework)  ⇒ Array<Pathname> 

The paths of the headers included in the vendored framework.

-
  
      .**vendored_frameworks_headers_dir**(framework)  ⇒ Pathname 

The path of the header directory of the vendored framework.

-
  
      .**vendored_xcframework_headers**(target_name, framework_path)  ⇒ Array<Pathname> 

The paths to all the headers included in the vendored xcframework.

-
  
      #**arc_source_files**  ⇒ Array<Pathname> 

The source files of the specification that use ARC.

-
  
      #**developer_files**  ⇒ Array<Pathname> 

Paths to include for local pods to assist in development.

-
  
      #**docs**  ⇒ Array<Pathname> 

The paths of auto-detected docs.

-
  
      #**headers**  ⇒ Array<Pathname> 

The headers of the specification.

-
  
      #**license**  ⇒ Pathname 

The path of the license file as indicated in the specification or auto-detected.

-
  
      #**module_map**  ⇒ Pathname, Nil 

The path of the custom module map file of the specification, if specified.

-
  
      #**non_arc_source_files**  ⇒ Array<Pathname> 

The source files of the specification that do not use ARC.

-
  
      #**on_demand_resources**  ⇒ Hash{String => Hash] The expanded paths of the on demand resources specified keyed by their tag including their category. 

Hash{String => Hash] The expanded paths of the on demand resources specified keyed by their tag including their category.

-
  
      #**on_demand_resources_files**  ⇒ Array<Pathname> 

The expanded paths of the on demand resources.

-
  
      #**other_source_files**  ⇒ Array<Pathname] the source files that do not match any of the recognized file extensions 

Array<Pathname] the source files that do not match any of the recognized file extensions.

-
  
      #**prefix_header**  ⇒ Pathname 

The of the prefix header file of the specification.

-
  
      #**preserve_paths**  ⇒ Array<Pathname> 

The files of the specification to preserve.

-
  
      #**private_headers**  ⇒ Array<Pathname> 

The private headers of the specification.

-
  
      #**project_headers**  ⇒ Array<Pathname> 

The project headers of the specification.

-
  
      #**public_headers**(include_frameworks = false)  ⇒ Array<Pathname> 

The public headers of the specification.

-
  
      #**readme**  ⇒ Pathname? 

The path of the auto-detected README file.

-
  
      #**resource_bundle_files**  ⇒ Array<Pathname> 

The paths of the files which should be included in resources bundles by the Pod.

-
  
      #**resource_bundles**  ⇒ Hash{String => Array<Pathname>} 

A hash that describes the resource bundles of the Pod.

-
  
      #**resources**  ⇒ Array<Pathname> 

The resources of the specification.

-
  
      #**source_files**  ⇒ Array<Pathname> 

The source files of the specification.

-
  
      #**spec_license**  ⇒ Pathname 

The path of the license file specified in the specification, if it exists.

-
  
      #**specs**  ⇒ Array<Pathname> 

The paths of auto-detected podspecs.

-
  
      #**vendored_dynamic_artifacts**  ⇒ Array<Pathname> 

The paths of the dynamic binary artifacts that come shipped with the Pod.

-
  
      #**vendored_dynamic_frameworks**  ⇒ Array<Pathname> 

The paths of the dynamic framework bundles that come shipped with the Pod.

-
  
      #**vendored_dynamic_libraries**  ⇒ Array<Pathname> 

The paths of the dynamic libraries that come shipped with the Pod.

-
  
      #**vendored_dynamic_xcframeworks**  ⇒ Array<Pathname> 

The paths of the dynamic xcframework bundles that come shipped with the Pod.

-
  
      #**vendored_frameworks**  ⇒ Array<Pathname> 

The paths of the framework bundles that come shipped with the Pod.

-
  
      #**vendored_frameworks_headers**  ⇒ Array<Pathname> 

The paths of the framework headers that come shipped with the Pod.

-
  
      #**vendored_libraries**  ⇒ Array<Pathname> 

The paths of the library bundles that come shipped with the Pod.

-
  
      #**vendored_static_artifacts**  ⇒ Array<Pathname> 

The paths of the static binary artifacts that come shipped with the Pod.

-
  
      #**vendored_static_frameworks**  ⇒ Array<Pathname> 

The paths of the static (fake) framework bundles that come shipped with the Pod.

-
  
      #**vendored_static_libraries**  ⇒ Array<Pathname> 

The paths of the static libraries that come shipped with the Pod.

-
  
      #**vendored_static_xcframeworks**  ⇒ Array<Pathname> 

The paths of the static xcframework bundles that come shipped with the Pod.

-
  
      #**vendored_xcframeworks**  ⇒ Array<Pathname> 

The paths of vendored .xcframework bundles that come shipped with the Pod.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(path_list, spec_consumer)  ⇒ FileAccessor 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

-
  
      #**inspect**  ⇒ String 

A string suitable for debugging.

-
  
      #**platform_name**  ⇒ Specification 

The platform used to consume the specification.

-
  
      #**root**  ⇒ Pathname 

The directory which contains the files of the Pod.

-
  
      #**spec**  ⇒ Specification 

The specification.

## Constructor Details

###
  
    #**initialize**(path_list, spec_consumer)  ⇒ FileAccessor 
  

  

  

  
    

Initialize a new instance

Parameters:

-

@see #path_list

-

@see #spec_consumer

```

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
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 39

def initialize(path_list, spec_consumer)
  if path_list.is_a?(PathList)
    @path_list = path_list
  else
    @path_list = PathList.new(path_list)
  end
  @spec_consumer = spec_consumer

  unless @spec_consumer
    raise Informative, 'Attempt to initialize File Accessor without a specification consumer.'
  end
end

```

## Instance Attribute Details

###
  
    #**path_list**  ⇒ Sandbox::PathList  (readonly)
  

  

  

  
    

Returns the directory where the source of the Pod is located.

Returns:

-

the directory where the source of the Pod is located.

```

27
28
29
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 27

def path_list
  @path_list
end

```

###
  
    #**spec_consumer**  ⇒ Specification::Consumer  (readonly)
  

  

  

  
    

Returns the consumer of the specification for which the file patterns should be resolved.

Returns:

-

the consumer of the specification for which the file patterns should be resolved.

```

32
33
34
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 32

def spec_consumer
  @spec_consumer
end

```

## Class Method Details

###
  
    .**all_files**(file_accessors)  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The list of all file accessors that a target will integrate into the project.

Parameters:

-

The list of all file accessors to compute.

Returns:

-

The list of all file accessors that a target will integrate into the project.

```

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
232
233
234
235
236
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 221

def self.all_files(file_accessors)
  files = [
    file_accessors.map(&:vendored_frameworks),
    file_accessors.map(&:vendored_libraries),
    file_accessors.map(&:resource_bundle_files),
    file_accessors.map(&:license),
    file_accessors.map(&:prefix_header),
    file_accessors.map(&:preserve_paths),
    file_accessors.map(&:readme),
    file_accessors.map(&:resources),
    file_accessors.map(&:on_demand_resources_files),
    file_accessors.map(&:source_files),
    file_accessors.map(&:module_map),
  ]
  files.flatten.compact.uniq
end

```

###
  
    .**vendored_frameworks_headers**(framework)  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the headers included in the vendored framework.

Parameters:

-

The vendored framework to search into.

Returns:

-

The paths of the headers included in the vendored framework.

```

253
254
255
256
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 253

def self.vendored_frameworks_headers(framework)
  headers_dir = vendored_frameworks_headers_dir(framework)
  Pathname.glob(headers_dir + '**/' + GLOB_PATTERNS[:public_header_files])
end

```

###
  
    .**vendored_frameworks_headers_dir**(framework)  ⇒ Pathname 
  

  

  

  
    

Returns The path of the header directory of the vendored framework.

Parameters:

-

The vendored framework to search into.

Returns:

-

The path of the header directory of the vendored framework.

```

243
244
245
246
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 243

def self.vendored_frameworks_headers_dir(framework)
  dir = framework + 'Headers'
  dir.directory? ? dir.realpath : dir
end

```

###
  
    .**vendored_xcframework_headers**(target_name, framework_path)  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths to all the headers included in the vendored xcframework.

Parameters:

-

The target name this .xcframework belongs to

-

The path to the .xcframework

Returns:

-

The paths to all the headers included in the vendored xcframework

```

267
268
269
270
271
272
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 267

def self.vendored_xcframework_headers(target_name, framework_path)
  xcframework = Xcode::XCFramework.new(target_name, framework_path)
  xcframework.slices.flat_map do |slice|
    vendored_frameworks_headers(slice.path)
  end
end

```

## Instance Method Details

###
  
    #**arc_source_files**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns the source files of the specification that use ARC.

Returns:

-

the source files of the specification that use ARC.

```

91
92
93
94
95
96
97
98
99
100
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 91

def arc_source_files
  case spec_consumer.requires_arc
  when TrueClass
    source_files
  when FalseClass
    []
  else
    paths_for_attribute(:requires_arc) & source_files
  end
end

```

###
  
    #**developer_files**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns Paths to include for local pods to assist in development.

Returns:

-

Paths to include for local pods to assist in development

```

419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 419

def developer_files
  podspecs = specs
  result = [module_map, prefix_header]

  if license_path = spec_consumer.license[:file]
    license_path = root + license_path
    unless File.exist?(license_path)
      UI.warn "A license was specified in podspec `#{spec.name}` but the file does not exist - #{license_path}"
    end
  end

  if podspecs.size <= 1
    result += [license, readme, podspecs, docs]
  else
    # Manually add non-globbing files since there are multiple podspecs in the same folder
    result << podspec_file
    if license_file = spec_license
      absolute_path = root + license_file
      result << absolute_path if File.exist?(absolute_path)
    end
  end
  result.compact.flatten.sort
end

```

###
  
    #**docs**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of auto-detected docs.

Returns:

-

The paths of auto-detected docs

```

403
404
405
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 403

def docs
  path_list.glob([GLOB_PATTERNS[:docs]])
end

```

###
  
    #**headers**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns the headers of the specification.

Returns:

-

the headers of the specification.

```

118
119
120
121
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 118

def headers
  extensions = HEADER_EXTENSIONS
  source_files.select { |f| extensions.include?(f.extname) }
end

```

###
  
    #**inspect**  ⇒ String 
  

  

  

  
    

Returns A string suitable for debugging.

Returns:

-

A string suitable for debugging.

```

72
73
74
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 72

def inspect
  "<#{self.class} spec=#{spec.name} platform=#{platform_name} root=#{root}>"
end

```

###
  
    #**license**  ⇒ Pathname 
  

  

  

  
    

Returns The path of the license file as indicated in the specification or auto-detected.

Returns:

-

The path of the license file as indicated in the specification or auto-detected.

```

383
384
385
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 383

def license
  spec_license || path_list.glob([GLOB_PATTERNS[:license]]).first
end

```

###
  
    #**module_map**  ⇒ Pathname, Nil 
  

  

  

  
    

Returns The path of the custom module map file of the specification, if specified.

Returns:

-

The path of the custom module map file of the specification, if specified.

```

389
390
391
392
393
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 389

def module_map
  if module_map = spec_consumer.module_map
    path_list.root + module_map
  end
end

```

###
  
    #**non_arc_source_files**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns the source files of the specification that do not use ARC.

Returns:

-

the source files of the specification that do not use ARC.

```

105
106
107
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 105

def non_arc_source_files
  source_files - arc_source_files
end

```

###
  
    #**on_demand_resources**  ⇒ Hash{String => Hash] The expanded paths of the on demand resources specified
keyed by their tag including their category.
  
Returns Hash{String => Hash] The expanded paths of the on demand resources specified keyed by their tag including their category.

Returns:

-

Hash{String => Hash] The expanded paths of the on demand resources specified keyed by their tag including their category.

```

349
350
351
352
353
354
355
356
357
358
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 349

def on_demand_resources
  result = {}
  spec_consumer.on_demand_resources.each do |tag_name, file_patterns|
    paths = expanded_paths(file_patterns[:paths],
                           :exclude_patterns => spec_consumer.exclude_files,
                           :include_dirs => true)
    result[tag_name] = { :paths => paths, :category => file_patterns[:category] }
  end
  result
end

```

###
  
    #**on_demand_resources_files**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The expanded paths of the on demand resources.

Returns:

-

The expanded paths of the on demand resources.

```

362
363
364
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 362

def on_demand_resources_files
  on_demand_resources.values.flat_map { |v| v[:paths] }
end

```

###
  
    #**other_source_files**  ⇒ Array<Pathname] the source files that do not match any of the
recognized file extensions
  
Returns Array<Pathname] the source files that do not match any of the recognized file extensions.

Returns:

-

Array<Pathname] the source files that do not match any of the recognized file extensions

```

111
112
113
114
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 111

def other_source_files
  extensions = SOURCE_FILE_EXTENSIONS
  source_files.reject { |f| extensions.include?(f.extname) }
end

```

###
  
    #**platform_name**  ⇒ Specification 
  

  

  

  
    

Returns the platform used to consume the specification.

Returns:

-

the platform used to consume the specification.

```

66
67
68
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 66

def platform_name
  spec_consumer.platform_name
end

```

###
  
    #**prefix_header**  ⇒ Pathname 
  

  

  

  
    

Returns The of the prefix header file of the specification.

Returns:

-

The of the prefix header file of the specification.

```

368
369
370
371
372
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 368

def prefix_header
  if file = spec_consumer.prefix_header_file
    path_list.root + file
  end
end

```

###
  
    #**preserve_paths**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns the files of the specification to preserve.

Returns:

-

the files of the specification to preserve.

```

162
163
164
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 162

def preserve_paths
  paths_for_attribute(:preserve_paths, true)
end

```

###
  
    #**private_headers**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The private headers of the specification.

Returns:

-

The private headers of the specification.

```

150
151
152
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 150

def private_headers
  private_header_files
end

```

###
  
    #**project_headers**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The project headers of the specification.

Returns:

-

The project headers of the specification.

```

144
145
146
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 144

def project_headers
  project_header_files
end

```

###
  
    #**public_headers**(include_frameworks = false)  ⇒ Array<Pathname> 
  

  

  

  
    

Returns the public headers of the specification.

Parameters:

-

        *(defaults to: false)*

Whether or not to include the headers of the vendored frameworks. Defaults to not include them.

Returns:

-

the public headers of the specification.

```

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
140
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 129

def public_headers(include_frameworks = false)
  public_headers = public_header_files
  project_headers = project_header_files
  private_headers = private_header_files
  if public_headers.nil? || public_headers.empty?
    header_files = headers
  else
    header_files = public_headers
  end
  header_files += vendored_frameworks_headers if include_frameworks
  header_files - project_headers - private_headers
end

```

###
  
    #**readme**  ⇒ Pathname? 
  

  

  

  
    

Returns The path of the auto-detected README file.

Returns:

-

The path of the auto-detected README file.

```

376
377
378
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 376

def readme
  path_list.glob([GLOB_PATTERNS[:readme]]).first
end

```

###
  
    #**resource_bundle_files**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the files which should be included in resources bundles by the Pod.

Returns:

-

The paths of the files which should be included in resources bundles by the Pod.

```

342
343
344
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 342

def resource_bundle_files
  resource_bundles.values.flatten
end

```

###
  
    #**resource_bundles**  ⇒ Hash{String => Array<Pathname>} 
  

  

  

  
    

Returns A hash that describes the resource bundles of the Pod. The keys represent the name of the bundle while the values the path of the resources.

Returns:

-

A hash that describes the resource bundles of the Pod. The keys represent the name of the bundle while the values the path of the resources.

```

328
329
330
331
332
333
334
335
336
337
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 328

def resource_bundles
  result = {}
  spec_consumer.resource_bundles.each do |name, file_patterns|
    paths = expanded_paths(file_patterns,
                           :exclude_patterns => spec_consumer.exclude_files,
                           :include_dirs => true)
    result[name] = paths
  end
  result
end

```

###
  
    #**resources**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns the resources of the specification.

Returns:

-

the resources of the specification.

```

156
157
158
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 156

def resources
  paths_for_attribute(:resources, true)
end

```

###
  
    #**root**  ⇒ Pathname 
  

  

  

  
    

Returns the directory which contains the files of the Pod.

Returns:

-

the directory which contains the files of the Pod.

```

54
55
56
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 54

def root
  path_list.root if path_list
end

```

###
  
    #**source_files**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns the source files of the specification.

Returns:

-

the source files of the specification.

```

84
85
86
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 84

def source_files
  paths_for_attribute(:source_files)
end

```

###
  
    #**spec**  ⇒ Specification 
  

  

  

  
    

Returns the specification.

Returns:

-

the specification.

```

60
61
62
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 60

def spec
  spec_consumer.spec
end

```

###
  
    #**spec_license**  ⇒ Pathname 
  

  

  

  
    

Returns The path of the license file specified in the specification, if it exists.

Returns:

-

The path of the license file specified in the specification, if it exists

```

410
411
412
413
414
415
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 410

def spec_license
  if file = spec_consumer.license[:file]
    absolute_path = root + file
    absolute_path if File.exist?(absolute_path)
  end
end

```

###
  
    #**specs**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of auto-detected podspecs.

Returns:

-

The paths of auto-detected podspecs

```

397
398
399
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 397

def specs
  path_list.glob([GLOB_PATTERNS[:podspecs]])
end

```

###
  
    #**vendored_dynamic_artifacts**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the dynamic binary artifacts that come shipped with the Pod.

Returns:

-

The paths of the dynamic binary artifacts that come shipped with the Pod.

```

313
314
315
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 313

def vendored_dynamic_artifacts
  vendored_dynamic_libraries + vendored_dynamic_frameworks
end

```

###
  
    #**vendored_dynamic_frameworks**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the dynamic framework bundles that come shipped with the Pod.

Returns:

-

The paths of the dynamic framework bundles that come shipped with the Pod.

```

176
177
178
179
180
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 176

def vendored_dynamic_frameworks
  (vendored_frameworks - vendored_xcframeworks).select do |framework|
    Xcode::LinkageAnalyzer.dynamic_binary?(framework + framework.basename('.*'))
  end
end

```

###
  
    #**vendored_dynamic_libraries**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the dynamic libraries that come shipped with the Pod.

Returns:

-

The paths of the dynamic libraries that come shipped with the Pod.

```

297
298
299
300
301
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 297

def vendored_dynamic_libraries
  vendored_libraries.select do |library|
    Xcode::LinkageAnalyzer.dynamic_binary?(library)
  end
end

```

###
  
    #**vendored_dynamic_xcframeworks**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the dynamic xcframework bundles that come shipped with the Pod.

Returns:

-

The paths of the dynamic xcframework bundles that come shipped with the Pod.

```

194
195
196
197
198
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 194

def vendored_dynamic_xcframeworks
  vendored_xcframeworks.select do |path|
    Xcode::XCFramework.new(spec.name, path).build_type == BuildType.dynamic_framework
  end
end

```

###
  
    #**vendored_frameworks**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the framework bundles that come shipped with the Pod.

Returns:

-

The paths of the framework bundles that come shipped with the Pod.

```

169
170
171
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 169

def vendored_frameworks
  paths_for_attribute(:vendored_frameworks, true)
end

```

###
  
    #**vendored_frameworks_headers**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the framework headers that come shipped with the Pod.

Returns:

-

The paths of the framework headers that come shipped with the Pod.

```

277
278
279
280
281
282
283
284
285
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 277

def vendored_frameworks_headers
  paths = (vendored_frameworks - vendored_xcframeworks).flat_map do |framework|
    self.class.vendored_frameworks_headers(framework)
  end.uniq
  paths.concat Array.new(vendored_xcframeworks.flat_map do |framework|
    self.class.vendored_xcframework_headers(spec.name, framework)
  end)
  paths
end

```

###
  
    #**vendored_libraries**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the library bundles that come shipped with the Pod.

Returns:

-

The paths of the library bundles that come shipped with the Pod.

```

290
291
292
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 290

def vendored_libraries
  paths_for_attribute(:vendored_libraries)
end

```

###
  
    #**vendored_static_artifacts**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the static binary artifacts that come shipped with the Pod.

Returns:

-

The paths of the static binary artifacts that come shipped with the Pod.

```

320
321
322
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 320

def vendored_static_artifacts
  vendored_static_libraries + vendored_static_frameworks + vendored_static_xcframeworks
end

```

###
  
    #**vendored_static_frameworks**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the static (fake) framework bundles that come shipped with the Pod.

Returns:

-

The paths of the static (fake) framework bundles that come shipped with the Pod.

```

203
204
205
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 203

def vendored_static_frameworks
  vendored_frameworks - vendored_dynamic_frameworks - vendored_xcframeworks
end

```

###
  
    #**vendored_static_libraries**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the static libraries that come shipped with the Pod.

Returns:

-

The paths of the static libraries that come shipped with the Pod.

```

306
307
308
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 306

def vendored_static_libraries
  vendored_libraries - vendored_dynamic_libraries
end

```

###
  
    #**vendored_static_xcframeworks**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of the static xcframework bundles that come shipped with the Pod.

Returns:

-

The paths of the static xcframework bundles that come shipped with the Pod.

```

185
186
187
188
189
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 185

def vendored_static_xcframeworks
  vendored_xcframeworks.select do |path|
    Xcode::XCFramework.new(spec.name, path).build_type == BuildType.static_framework
  end
end

```

###
  
    #**vendored_xcframeworks**  ⇒ Array<Pathname> 
  

  

  

  
    

Returns The paths of vendored .xcframework bundles that come shipped with the Pod.

Returns:

-

The paths of vendored .xcframework bundles that come shipped with the Pod.

```

210
211
212
213
214
```

```
# File 'lib/cocoapods/sandbox/file_accessor.rb', line 210

def vendored_xcframeworks
  vendored_frameworks.select do |framework|
    File.extname(framework) == '.xcframework'
  end
end

```
