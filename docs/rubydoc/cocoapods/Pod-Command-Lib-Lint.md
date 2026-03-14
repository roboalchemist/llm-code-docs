# Class: Pod::Command::Lib::Lint
  
    Inherits:
    
      Pod::Command::Lib
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Lib

- Pod::Command::Lib::Lint

        show all
      

    Defined in:
    lib/cocoapods/command/lib/lint.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ Lint 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Lint.

-
  
      #**run**  ⇒ Object 

-
  
      #**validate!**  ⇒ Object 

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Lint 
  

  

  

  
    

Returns a new instance of Lint.

```

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
# File 'lib/cocoapods/command/lib/lint.rb', line 45

def initialize(argv)
  @quick               = argv.flag?('quick')
  @allow_warnings      = argv.flag?('allow-warnings')
  @clean               = argv.flag?('clean', true)
  @fail_fast           = argv.flag?('fail-fast', false)
  @subspecs            = argv.flag?('subspecs', true)
  @only_subspec        = argv.option('subspec')
  @use_frameworks      = !argv.flag?('use-libraries')
  @use_modular_headers = argv.flag?('use-modular-headers')
  @use_static_frameworks = argv.flag?('use-static-frameworks')
  @source_urls         = argv.option('sources', Pod::TrunkSource::TRUNK_REPO_URL).split(',')
  @platforms           = argv.option('platforms', '').split(',')
  @private             = argv.flag?('private', false)
  @swift_version       = argv.option('swift-version', nil)
  @include_podspecs    = argv.option('include-podspecs', nil)
  @external_podspecs   = argv.option('external-podspecs', nil)
  @skip_import_validation = argv.flag?('skip-import-validation', false)
  @skip_tests          = argv.flag?('skip-tests', false)
  @test_specs          = argv.option('test-specs', nil)&.split(',')
  @analyze             = argv.flag?('analyze', false)
  @podspecs_paths      = argv.arguments!
  @configuration       = argv.option('configuration', nil)
  @validation_dir      = argv.option('validation-dir', nil)
  super
end

```

## Class Method Details

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
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
28
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
```

```
# File 'lib/cocoapods/command/lib/lint.rb', line 15

def self.options
  [
    ['--quick', 'Lint skips checks that would require to download and build the spec'],
    ['--allow-warnings', 'Lint validates even if warnings are present'],
    ['--subspec=NAME', 'Lint validates only the given subspec'],
    ['--no-subspecs', 'Lint skips validation of subspecs'],
    ['--no-clean', 'Lint leaves the build directory intact for inspection'],
    ['--fail-fast', 'Lint stops on the first failing platform or subspec'],
    ['--use-libraries', 'Lint uses static libraries to install the spec'],
    ['--use-modular-headers', 'Lint uses modular headers during installation'],
    ['--use-static-frameworks', 'Lint uses static frameworks during installation'],
    ["--sources=#{Pod::TrunkSource::TRUNK_REPO_URL}", 'The sources from which to pull dependent pods ' \
      "(defaults to #{Pod::TrunkSource::TRUNK_REPO_URL}). Multiple sources must be comma-delimited"],
    ['--platforms=ios,macos,visionos', 'Lint against specific platforms (defaults to all platforms supported by the ' \
      'podspec). Multiple platforms must be comma-delimited'],
    ['--private', 'Lint skips checks that apply only to public specs'],
    ['--swift-version=VERSION', 'The `SWIFT_VERSION` that should be used to lint the spec. ' \
     'This takes precedence over the Swift versions specified by the spec or a `.swift-version` file'],
    ['--include-podspecs=**/*.podspec', 'Additional ancillary podspecs which are used for linting via :path'],
    ['--external-podspecs=**/*.podspec', 'Additional ancillary podspecs which are used for linting '\
      'via :podspec. If there are --include-podspecs, then these are removed from them'],
    ['--skip-import-validation', 'Lint skips validating that the pod can be imported'],
    ['--skip-tests', 'Lint skips building and running tests during validation'],
    ['--test-specs=test-spec1,test-spec2,etc', 'List of test specs to run'],
    ['--analyze', 'Validate with the Xcode Static Analysis tool'],
    ['--configuration=CONFIGURATION', 'Build using the given configuration (defaults to Release)'],
    ['--validation-dir', 'The directory to use for validation. If none is specified a temporary directory will be used.'],
  ].concat(super)
end

```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

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
95
96
97
98
99
100
101
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
```

```
# File 'lib/cocoapods/command/lib/lint.rb', line 75

def run
  UI.puts
  podspecs_to_lint.each do |podspec|
    validator                = Validator.new(podspec, @source_urls, @platforms)
    validator.local          = true
    validator.quick          = @quick
    validator.no_clean       = !@clean
    validator.fail_fast      = @fail_fast
    validator.allow_warnings = @allow_warnings
    validator.no_subspecs    = !@subspecs || @only_subspec
    validator.only_subspec   = @only_subspec
    validator.use_frameworks = @use_frameworks
    validator.use_modular_headers = @use_modular_headers
    validator.use_static_frameworks = @use_static_frameworks
    validator.ignore_public_only_results = @private
    validator.swift_version = @swift_version
    validator.skip_import_validation = @skip_import_validation
    validator.skip_tests = @skip_tests
    validator.test_specs = @test_specs
    validator.analyze = @analyze
    validator.include_podspecs = @include_podspecs
    validator.external_podspecs = @external_podspecs
    validator.configuration = @configuration
    validator.validation_dir = @validation_dir
    validator.validate

    unless @clean
      UI.puts "Pods workspace available at `#{validator.validation_dir}/App.xcworkspace` for inspection."
      UI.puts
    end
    if validator.validated?
      UI.puts "#{validator.spec.name} passed validation.".green
    else
      spec_name = podspec
      spec_name = validator.spec.name if validator.spec
      message = "#{spec_name} did not pass validation, due to #{validator.failure_reason}."

      if @clean
        message << "\nYou can use the `--no-clean` option to inspect " \
          'any issue.'
      end
      raise Informative, message
    end
  end
end

```

###
  
    #**validate!**  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
```

```
# File 'lib/cocoapods/command/lib/lint.rb', line 71

def validate!
  super
end

```
