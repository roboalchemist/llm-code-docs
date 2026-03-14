# Class: Pod::Command::Repo::Lint
  
  
  

  
  
    Inherits:
    
      Pod::Command::Repo
      
        

          
- Object
          
            
- CLAide::Command
          
            
- Pod::Command
          
            
- Pod::Command::Repo
          
            
- Pod::Command::Repo::Lint
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/command/repo/lint.rb
  
  

  
    
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
    

    
  
  
  
  
  
  
  
  

  
    

Run the command.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command::Repo

  

#dir

  
  
  
  
  
  
  
  
  
### Methods included from Executable

  

capture_command, capture_command!, #executable, execute_command, which, which!

  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command

  

#ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

  
  
  
  
  
  
  
  
  
### Methods included from Pod::Config::Mixin

  

#config

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(argv)  ⇒ Lint 
  

  

  

  
    

Returns a new instance of Lint.

  

  

  
    
      

```

23
24
25
26
27
```

    
    
      

```
# File 'lib/cocoapods/command/repo/lint.rb', line 23

def initialize(argv)
  @name = argv.shift_argument
  @only_errors = argv.flag?('only-errors')
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
```

    
    
      

```
# File 'lib/cocoapods/command/repo/lint.rb', line 17

def self.options
  [
    ['--only-errors', 'Lint presents only the errors'],
  ].concat(super)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    
  
    **TODO:**
    

Part of this logic needs to be ported to cocoapods-core so web services can validate the repo.

  

  
    **TODO:**
    

add UI.print and enable print statements again.

  

Run the command

  

  

  
    
      

```

36
37
38
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
71
72
73
74
75
76
77
78
```

    
    
      

```
# File 'lib/cocoapods/command/repo/lint.rb', line 36

def run
  sources = if @name
              if File.exist?(@name)
                [Source.new(Pathname(@name))]
              else
                config.sources_manager.sources([@name])
              end
            else
              config.sources_manager.all
            end

  sources.each do |source|
    source.verify_compatibility!
    UI.puts "\nLinting spec repo `#{source.name}`\n".yellow

    validator = Source::HealthReporter.new(source.repo)
    validator.pre_check do |_name, _version|
      UI.print '.'
    end
    report = validator.analyze
    UI.puts
    UI.puts

    report.pods_by_warning.each do |message, versions_by_name|
      UI.puts "-> #{message}".yellow
      versions_by_name.each { |name, versions| UI.puts "  - #{name} (#{versions * ', '})" }
      UI.puts
    end

    report.pods_by_error.each do |message, versions_by_name|
      UI.puts "-> #{message}".red
      versions_by_name.each { |name, versions| UI.puts "  - #{name} (#{versions * ', '})" }
      UI.puts
    end

    UI.puts "Analyzed #{report.analyzed_paths.count} podspecs files.\n\n"
    if report.pods_by_error.count.zero?
      UI.puts 'All the specs passed validation.'.green << "\n\n"
    else
      raise Informative, "#{report.pods_by_error.count} podspecs failed validation."
    end
  end
end

```