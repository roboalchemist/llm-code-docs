# Class: Pod::Command::Spec::Lint
  
    Inherits:
    
      Pod::Command::Spec
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Spec

- Pod::Command::Spec::Lint

        show all
      

    Defined in:
    lib/cocoapods/command/spec/lint.rb
  
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

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Lint 
  

  

  

  
    

Returns a new instance of Lint.

```

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
61
62
63
64
65
66
```

```
# File 'lib/cocoapods/command/spec/lint.rb', line 44

def initialize(argv)
  @quick           = argv.flag?('quick')
  @allow_warnings  = argv.flag?('allow-warnings')
  @clean           = argv.flag?('clean', true)
  @fail_fast       = argv.flag?('fail-fast', false)
  @subspecs        = argv.flag?('subspecs', true)
  @only_subspec    = argv.option('subspec')
  @use_frameworks  = !argv.flag?('use-libraries')
  @use_modular_headers = argv.flag?('use-modular-headers')
  @use_static_frameworks = argv.flag?('use-static-frameworks')
  @source_urls     = argv.option('sources', Pod::TrunkSource::TRUNK_REPO_URL).split(',')
  @platforms       = argv.option('platforms', '').split(',')
  @private         = argv.flag?('private', false)
  @swift_version   = argv.option('swift-version', nil)
  @skip_import_validation = argv.flag?('skip-import-validation', false)
  @skip_tests      = argv.flag?('skip-tests', false)
  @test_specs      = argv.option('test-specs', nil)&.split(',')
  @analyze         = argv.flag?('analyze', false)
  @podspecs_paths  = argv.arguments!
  @configuration   = argv.option('configuration', nil)
  @validation_dir = argv.option('validation-dir', nil)
  super
end

```

## Class Method Details

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/cocoapods/command/spec/lint.rb', line 17

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
    ['--platforms=ios,macos', 'Lint against specific platforms (defaults to all platforms supported by the ' \
      'podspec). Multiple platforms must be comma-delimited'],
    ['--private', 'Lint skips checks that apply only to public specs'],
    ['--swift-version=VERSION', 'The `SWIFT_VERSION` that should be used to lint the spec. ' \
     'This takes precedence over the Swift versions specified by the spec or a `.swift-version` file'],
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

68
69
70
71
72
73
74
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
```

```
# File 'lib/cocoapods/command/spec/lint.rb', line 68

def run
  UI.puts
  failure_reasons = []
  podspecs_to_lint.each do |podspec|
    validator                = Validator.new(podspec, @source_urls, @platforms)
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
    validator.configuration = @configuration
    validator.validation_dir = @validation_dir
    validator.validate
    failure_reasons << validator.failure_reason

    unless @clean
      UI.puts "Pods workspace available at `#{validator.validation_dir}/App.xcworkspace` for inspection."
      UI.puts
    end
  end

  count = podspecs_to_lint.count
  UI.puts "Analyzed #{count} #{'podspec'.pluralize(count)}.\n\n"

  failure_reasons.compact!
  if failure_reasons.empty?
    lint_passed_message = count == 1 ? "#{podspecs_to_lint.first.basename} passed validation." : 'All the specs passed validation.'
    UI.puts lint_passed_message.green << "\n\n"
  else
    raise Informative, if count == 1
                         "The spec did not pass validation, due to #{failure_reasons.first}."
                       else
                         "#{failure_reasons.count} out of #{count} specs failed validation."
                       end
  end
  podspecs_tmp_dir.rmtree if podspecs_tmp_dir.exist?
end

```
