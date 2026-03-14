# Module: Pod::Executable
  
    Included in:
    Command::Lib::Create, Command::Repo, Command::Repo::Push, Generator::BridgeSupport, Installer::PodSourcePreparer, Source
  
  

  
  
    Defined in:
    lib/cocoapods/executable.rb
  
## Overview

Module which provides support for running executables.

In a class it can be used as:

```
extend Executable
executable :git

```

This will create two methods `git` and `git!` both accept a command but the later will raise on non successful executions. The methods return the output of the command.

## Defined Under Namespace

      **Classes:** Indenter
    
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**capture_command**(executable, command, capture: :merge, env: {}, **kwargs)  ⇒ (String, Process::Status) 
    

    
  
  
  
  
  
  
  
  

  
    

Runs the given command, capturing the desired output.

-
  
      .**capture_command!**(executable, command, **kwargs)  ⇒ (String, Process::Status) 

Runs the given command, capturing the desired output.

-
  
      .**execute_command**(executable, command, raise_on_failure = true)  ⇒ String 

Executes the given command displaying it if in verbose mode.

-
  
      .**which**(program)  ⇒ String, Nil 

Returns the absolute path to the binary with the given name on the current `PATH`, or `nil` if none is found.

-
  
      .**which!**(program)  ⇒ String 

Returns the absolute path to the binary with the given name on the current `PATH`, or raises if none is found.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**executable**(name)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Creates the methods for the executable with the given name.

## Class Method Details

###
  
    .**capture_command**(executable, command, capture: :merge, env: {}, **kwargs)  ⇒ (String, Process::Status) 
  

  

  

  
    

Runs the given command, capturing the desired output.

Parameters:

-

        executable

        (String)
      
      
      
        —
        

The binary to use.

-

        command

        (Array<#to_s>)
      
      
      
        —
        

The command to send to the binary.

-

        capture

        (Symbol)
      
      
        *(defaults to: :merge)*
      
      
        —
        

Whether it should raise if the command fails.

-

        env

        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

Environment variables to be set for the command.

Returns:

-

        ((String, Process::Status))

        —
        

The desired captured output from the command, and the status from running the command.

Raises:

-

If the executable could not be located.

```

142
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
153
154
```

```
# File 'lib/cocoapods/executable.rb', line 142

def self.capture_command(executable, command, capture: :merge, env: {}, **kwargs)
  bin = which!(executable)

  require 'open3'
  command = command.map(&:to_s)
  case capture
  when :merge then Open3.capture2e(env, [bin, bin], *command, **kwargs)
  when :both then Open3.capture3(env, [bin, bin], *command, **kwargs)
  when :out then Open3.capture3(env, [bin, bin], *command, **kwargs).values_at(0, -1)
  when :err then Open3.capture3(env, [bin, bin], *command, **kwargs).drop(1)
  when :none then Open3.capture3(env, [bin, bin], *command, **kwargs).last
  end
end
```

###
  
    .**capture_command!**(executable, command, **kwargs)  ⇒ (String, Process::Status) 
  

  

  

  
    

Runs the given command, capturing the desired output.

Parameters:

-

        executable

        (String)
      
      
      
        —
        

The binary to use.

-

        command

        (Array<#to_s>)
      
      
      
        —
        

The command to send to the binary.

-

        capture

        (Symbol)
      
      
      
        —
        

Whether it should raise if the command fails.

-

        env

        (Hash)
      
      
      
        —
        

Environment variables to be set for the command.

Returns:

-

        ((String, Process::Status))

        —
        

The desired captured output from the command, and the status from running the command.

Raises:

-

If the executable could not be located.

-

If running the command fails

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
```

```
# File 'lib/cocoapods/executable.rb', line 160

def self.capture_command!(executable, command, **kwargs)
  capture_command(executable, command, **kwargs).tap do |result|
    result = Array(result)
    status = result.last
    unless status.success?
      output = result[0..-2].join
      raise Informative, "#{executable} #{command.join(' ')}\n\n#{output}".strip
    end
  end
end
```

###
  
    .**execute_command**(executable, command, raise_on_failure = true)  ⇒ String 
  

  

  

  
    

Executes the given command displaying it if in verbose mode.

Parameters:

-

        executable

        (String)
      
      
      
        —
        

The binary to use.

-

        command

        (Array<#to_s>)
      
      
      
        —
        

The command to send to the binary.

-

        raise_on_failure

        (Boolean)
      
      
        *(defaults to: true)*
      
      
        —
        

Whether it should raise if the command fails.

Returns:

-

        (String)

        —
        

the output of the command (STDOUT and STDERR).

Raises:

-

If the executable could not be located.

-

If the command fails and the `raise_on_failure` is set to true.

```

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
79
80
```

```
# File 'lib/cocoapods/executable.rb', line 48

def self.execute_command(executable, command, raise_on_failure = true)
  bin = which!(executable)

  command = command.map(&:to_s)
  if File.basename(bin) == 'tar.exe'
    # Tar on Windows needs --force-local
    command.push('--force-local')
  end
  full_command = "#{bin} #{command.join(' ')}"

  if Config.instance.verbose?
    UI.message("$ #{full_command}")
    stdout = Indenter.new(STDOUT)
    stderr = Indenter.new(STDERR)
  else
    stdout = Indenter.new
    stderr = Indenter.new
  end

  status = popen3(bin, command, stdout, stderr)
  stdout = stdout.join
  stderr = stderr.join
  output = stdout + stderr
  unless status.success?
    if raise_on_failure
      raise Informative, "#{full_command}\n\n#{output}"
    else
      UI.message("[!] Failed: #{full_command}".red)
    end
  end

  output
end
```

###
  
    .**which**(program)  ⇒ String, Nil 
  

  

  

  
    

Returns the absolute path to the binary with the given name on the current `PATH`, or `nil` if none is found.

Parameters:

-

        program

        (String)
      
      
      
        —
        

The name of the program being searched for.

Returns:

-

        (String, Nil)

        —
        

The absolute path to the given program, or `nil` if it wasn’t found in the current `PATH`.

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
```

```
# File 'lib/cocoapods/executable.rb', line 91

def self.which(program)
  program = program.to_s
  paths = ENV.fetch('PATH') { '' }.split(File::PATH_SEPARATOR)
  paths.unshift('./')
  paths.uniq!
  paths.each do |path|
    bin = File.expand_path(program, path)
    if Gem.win_platform?
      bin += '.exe'
    end
    if File.file?(bin) && File.executable?(bin)
      return bin
    end
  end
  nil
end
```

###
  
    .**which!**(program)  ⇒ String 
  

  

  

  
    

Returns the absolute path to the binary with the given name on the current `PATH`, or raises if none is found.

Parameters:

-

        program

        (String)
      
      
      
        —
        

The name of the program being searched for.

Returns:

-

        (String)

        —
        

The absolute path to the given program.

```

116
117
118
119
120
```

```
# File 'lib/cocoapods/executable.rb', line 116

def self.which!(program)
  which(program).tap do |bin|
    raise Informative, "Unable to locate the executable `#{program}`" unless bin
  end
end
```

## Instance Method Details

###
  
    #**executable**(name)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Creates the methods for the executable with the given name.

Parameters:

-

        name

        (Symbol)
      
      
      
        —
        

the name of the executable.

```

21
22
23
24
25
26
27
28
29
```

```
# File 'lib/cocoapods/executable.rb', line 21

def executable(name)
  define_method(name) do |*command|
    Executable.execute_command(name, Array(command).flatten, false)
  end

  define_method(name.to_s + '!') do |*command|
    Executable.execute_command(name, Array(command).flatten, true)
  end
end
```
