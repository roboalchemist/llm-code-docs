# Class: Pod::Command
  
    Inherits:
    
      CLAide::Command
      
        

          
- Object

- CLAide::Command

- Pod::Command

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Options, Pod::Config::Mixin
  
    Defined in:
    lib/cocoapods/command.rb,

  lib/cocoapods/command/env.rb,
 lib/cocoapods/command/ipc.rb,
 lib/cocoapods/command/lib.rb,
 lib/cocoapods/command/init.rb,
 lib/cocoapods/command/list.rb,
 lib/cocoapods/command/repo.rb,
 lib/cocoapods/command/spec.rb,
 lib/cocoapods/command/cache.rb,
 lib/cocoapods/command/setup.rb,
 lib/cocoapods/command/update.rb,
 lib/cocoapods/command/install.rb,
 lib/cocoapods/command/ipc/list.rb,
 lib/cocoapods/command/ipc/repl.rb,
 lib/cocoapods/command/ipc/spec.rb,
 lib/cocoapods/command/lib/lint.rb,
 lib/cocoapods/command/outdated.rb,
 lib/cocoapods/command/repo/add.rb,
 lib/cocoapods/command/spec/cat.rb,
 lib/cocoapods/command/repo/lint.rb,
 lib/cocoapods/command/repo/list.rb,
 lib/cocoapods/command/repo/push.rb,
 lib/cocoapods/command/spec/edit.rb,
 lib/cocoapods/command/spec/lint.rb,
 lib/cocoapods/command/cache/list.rb,
 lib/cocoapods/command/lib/create.rb,
 lib/cocoapods/command/spec/which.rb,
 lib/cocoapods/command/cache/clean.rb,
 lib/cocoapods/command/ipc/podfile.rb,
 lib/cocoapods/command/repo/remove.rb,
 lib/cocoapods/command/repo/update.rb,
 lib/cocoapods/command/spec/create.rb,
 lib/cocoapods/command/repo/add_cdn.rb,
 lib/cocoapods/command/ipc/podfile_json.rb,
 lib/cocoapods/command/options/repo_update.rb,
 lib/cocoapods/command/ipc/update_search_index.rb,
 lib/cocoapods/command/options/project_directory.rb

## Direct Known Subclasses

Cache, Env, IPC, Init, Install, Lib, List, Outdated, Repo, Setup, Spec, Update

## Defined Under Namespace

      **Modules:** Options
    
  
    
      **Classes:** Cache, Env, IPC, Init, Install, Lib, List, Outdated, Repo, Setup, Spec, Update
    
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**ensure_not_root_or_allowed!**(argv, uid = Process.uid, is_windows = Gem.win_platform?)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Ensure root user.

-
  
      .**options**  ⇒ Object 

-
  
      .**report_error**(exception)  ⇒ Object 

-
  
      .**run**(argv)  ⇒ Object 

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**ensure_master_spec_repo_exists!**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Ensure that the master spec repo exists.

-
  
      #**initialize**(argv)  ⇒ Command 

    constructor
  
  
  
  
  
  

  
    

A new instance of Command.

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Command 
  

  

  

  
    
  
    **TODO:**
    

If a command is run inside another one some settings which where true might return false.

    **TODO:**
    

We should probably not even load colored unless needed.

    **TODO:**
    

Move silent flag to CLAide.

    **Note:**
    

It is important that the commands don’t override the default settings if their flag is missing (i.e. their value is nil)

Returns a new instance of Command.

```

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
# File 'lib/cocoapods/command.rb', line 85

def initialize(argv)
  super
  config.silent = argv.flag?('silent', config.silent)
  config.allow_root = argv.flag?('allow-root', config.allow_root)
  config.verbose = self.verbose? unless verbose.nil?
  unless self.ansi_output?
    Colored2.disable!
    String.send(:define_method, :colorize) { |string, _| string }
  end
end

```

## Class Method Details

###
  
    .**ensure_not_root_or_allowed!**(argv, uid = Process.uid, is_windows = Gem.win_platform?)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Ensure root user

```

100
101
102
103
```

```
# File 'lib/cocoapods/command.rb', line 100

def self.ensure_not_root_or_allowed!(argv, uid = Process.uid, is_windows = Gem.win_platform?)
  root_allowed = argv.include?('--allow-root') || !ENV['COCOAPODS_ALLOW_ROOT'].nil?
  help! 'You cannot run CocoaPods as root.' unless root_allowed || uid != 0 || is_windows
end

```

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
43
44
45
```

```
# File 'lib/cocoapods/command.rb', line 40

def self.options
  [
    ['--allow-root', 'Allows CocoaPods to run as root'],
    ['--silent', 'Show nothing'],
  ].concat(super)
end

```

###
  
    .**report_error**(exception)  ⇒ Object 
  

  

  

  
    
      

```

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
71
72
73
```

```
# File 'lib/cocoapods/command.rb', line 57

def self.report_error(exception)
  case exception
  when Interrupt
    puts '[!] Cancelled'.red
    Config.instance.verbose? ? raise : exit(1)
  when SystemExit
    raise
  else
    if ENV['COCOA_PODS_ENV'] != 'development'
      puts UI::ErrorReport.report(exception)
      UI::ErrorReport.search_for_exceptions(exception)
      exit 1
    else
      raise exception
    end
  end
end

```

###
  
    .**run**(argv)  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
50
51
52
53
54
55
```

```
# File 'lib/cocoapods/command.rb', line 47

def self.run(argv)
  ensure_not_root_or_allowed! argv
  verify_minimum_git_version!
  verify_xcode_license_approved!

  super(argv)
ensure
  UI.print_warnings
end

```

## Instance Method Details

###
  
    #**ensure_master_spec_repo_exists!**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Ensure that the master spec repo exists

```

109
110
111
112
113
```

```
# File 'lib/cocoapods/command.rb', line 109

def ensure_master_spec_repo_exists!
  unless config.sources_manager.master_repo_functional?
    Setup.new(CLAide::ARGV.new([])).run
  end
end

```
