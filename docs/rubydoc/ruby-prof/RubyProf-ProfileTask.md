# Class: RubyProf::ProfileTask
  
  
  

  
  
    Inherits:
    
      Rake::TestTask
      
        

          
- Object
          
            
- Rake::TestTask
          
            
- RubyProf::ProfileTask
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/task.rb
  
  

## Overview

  
    

Define a task library for profiling unit tests with ruby-prof.

All of the options provided by the Rake:TestTask are supported except the loader which is set to ruby-prof.  For detailed information please refer to the Rake:TestTask documentation.

ruby-prof specific options include:

```
output_dir - For each file specified an output
             file with profile information will be
             written to the output directory.
             By default, the output directory is
             called "profile" and is created underneath
             the current working directory.

printer - Specifies the output printer.  Valid values include
          :flat, :graph, :graph_html and :call_tree.

min_percent - Methods that take less than the specified percent
              will not be written out.

```

Example:

```
require 'ruby-prof/task'

RubyProf::ProfileTask.new do |t|
  t.test_files = FileList['test/test*.rb']
  t.output_dir = "c:/temp"
  t.printer = :graph
  t.min_percent = 10
end

```

If rake is invoked with a “TEST=filename” command line option, then the list of test files will be overridden to include only the filename specified on the command line.  This provides an easy way to run just one test.

If rake is invoked with a “TESTOPTS=options” command line option, then the given options are passed to the test process after a ‘–’.  This allows Test::Unit options to be passed to the test suite.

Examples:

```
rake profile                           # run tests normally
rake profile TEST=just_one_file.rb     # run just one test file.
rake profile TESTOPTS="-v"             # run in verbose mode
rake profile TESTOPTS="--runner=fox"   # use the fox test runner

```

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**min_percent**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute min_percent.

  

    
      
- 
  
    
      #**output_dir**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute output_dir.

  

    
      
- 
  
    
      #**printer**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute printer.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**clean_output_directory**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**create_output_directory**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**define**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create the tasks defined by this task lib.

  

      
        
- 
  
    
      #**initialize**(name = :profile)  ⇒ ProfileTask 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ProfileTask.

  

      
        
- 
  
    
      #**option_list**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**output_directory**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_script**(script_path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Run script.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name = :profile)  ⇒ ProfileTask 
  

  

  

  
    

Returns a new instance of ProfileTask.

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 65

def initialize(name = :profile)
  super(name)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**min_percent**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute min_percent.

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 62

def min_percent
  @min_percent
end
```

    
  

    
      
      
      
  
### 
  
    #**output_dir**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute output_dir.

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 61

def output_dir
  @output_dir
end
```

    
  

    
      
      
      
  
### 
  
    #**printer**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute printer.

  

  

  
    
      

```

63
64
65
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 63

def printer
  @printer
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**clean_output_directory**  ⇒ Object 
  

  

  

  
    
      

```

136
137
138
139
140
141
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 136

def clean_output_directory
  if File.exist?(output_directory)
    files = Dir.glob(output_directory + '/*')
    FileUtils.rm(files)
  end
end
```

    
  

    
      
  
### 
  
    #**create_output_directory**  ⇒ Object 
  

  

  

  
    
      

```

130
131
132
133
134
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 130

def create_output_directory
  if not File.exist?(output_directory)
    Dir.mkdir(output_directory)
  end
end
```

    
  

    
      
  
### 
  
    #**define**  ⇒ Object 
  

  

  

  
    

Create the tasks defined by this task lib.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 70

def define
  lib_path = @libs.join(File::PATH_SEPARATOR)
  desc "Profile" + (@name==:profile ? "" : " for #{@name}")

  task @name do
    create_output_directory

    @ruby_opts.unshift( "-I#{lib_path}" )
    @ruby_opts.unshift( "-w" ) if @warning
    @ruby_opts.push("-S ruby-prof")
    @ruby_opts.push("--printer #{@printer}")
    @ruby_opts.push("--min_percent #{@min_percent}")

    file_list.each do |file_path|
      run_script(file_path)
    end
  end
  self
end
```

    
  

    
      
  
### 
  
    #**option_list**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

143
144
145
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 143

def option_list # :nodoc:
  ENV['OPTIONS'] || @options.join(" ") || ""
end
```

    
  

    
      
  
### 
  
    #**output_directory**  ⇒ Object 
  

  

  

  
    
      

```

126
127
128
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 126

def output_directory
  File.expand_path(@output_dir)
end
```

    
  

    
      
  
### 
  
    #**run_script**(script_path)  ⇒ Object 
  

  

  

  
    

Run script

  

  

  
    
      

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
120
121
122
123
124
```

    
    
      

```
# File 'lib/ruby-prof/task.rb', line 91

def run_script(script_path)
  run_code = ''
  RakeFileUtils.verbose(@verbose) do
    file_name = File.basename(script_path, File.extname(script_path))
    case @printer
      when :flat, :graph, :call_tree
        file_name += ".txt"
      when :graph_html
        file_name += ".html"
      else
        file_name += ".txt"
    end

    output_file_path = File.join(output_directory, file_name)

    command_line = @ruby_opts.join(" ") +
                  " --file=" + output_file_path +
                  " " + script_path

    puts "ruby " + command_line
    # We have to catch the exeption to continue on.  However,
    # the error message will have been output to STDERR
    # already by the time we get here so we don't have to
    # do that again
    begin
      ruby command_line
    rescue => e
      STDOUT << e << "\n"
      STDOUT.flush
    end
    puts ""
    puts ""
  end
end
```