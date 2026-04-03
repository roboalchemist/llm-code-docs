- 

    Libraries »
    wdm (0.2.0)

    » 
    Index » 
    File: README

# 

Windows Directory Monitor (WDM) is a thread-safe ruby library which can be used to monitor directories for changes on Windows.

It's mostly implemented in C and uses the Win32 API for a better performance.

## 

If you are using Bundler, add the following line to your application's Gemfile:

`gem 'wdm'
`

Although wdm is only usable on Windows, it can be installed on Linux and Macos as well, so that no :platform option is necessary.
Then execute:

`$ bundle
`

Or install it yourself as:

`$ gem install wdm
`

## 

For a simple example on how to use WDM, you can take a look at the `example` directory of the repository.

## 

You can find a comparison of different ruby libraries for watching directory changes on Windows in the `benchmark` directory of the repository.

## 

### 

To start watching directories, you need an instance of `WDM::Monitor`:

`require "wdm"
monitor = WDM::Monitor.new
`

After that, register a callback for each directory you want to watch:

`# Watch a single directory
monitor.watch('C:\Users\Maher\Desktop') { |change|  puts change.path }

# Watch a directory with its subdirectories
monitor.watch_recursively('C:\Users\Maher\Projects\my_project') { |change|  puts change.path }
`

Both `Monitor#watch` and `Monitor#watch_recursively` can take a series of options after the first parameter to specify the watching options:

`# Report changes to directories in the watched directory (Ex.: Addition of an empty directory)
monitor.watch('C:\Users\Maher\Desktop', :default, :directories)
`

The supported options are:

Value
Meaning

:default
The default set of options for watching directories. It's a combination of the :files, :directories and the :last_write options.

:files
Any file name change in the watched directory or subtree causes a change notification wait operation to return. Changes include renaming, creating, or deleting a file.

:directories
Any directory-name change in the watched directory or subtree causes a change notification wait operation to return. Changes include creating or deleting a directory.

:attributes
Any attribute change in the watched directory or subtree causes a change notification wait operation to return.

:size
Any file-size change in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change in file size only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.

:last_write
Any change to the last write-time of files in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change to the last write-time only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.

:last_access
Any change to the last access time of files in the watched directory or subtree causes a change notification wait operation to return.

:creation
Any change to the creation time of files in the watched directory or subtree causes a change notification wait operation to return.

:security
Any security-descriptor change in the watched directory or subtree causes a change notification wait operation to return.

These options map to the filters that `ReadDirectoryChangesW` takes in its `dwNotifyFilter` parameter. You can find more info on the docs page of `ReadDirectoryChangesW`. 

Now all that's left to be done is to run the monitor:

`monitor.run!
`

The `Monitor#run!` method blocks the process. Since monitors are thread-safe, you can run them in a thread if you don't want to block your main one:

`worker_thread = Thread.new { monitor.run! }

# The process won't block; it will continue with the next line of code...
`

When you are done with the monitor, don't forget to stop it. Here is a snippet to always stop the monitor when the ruby process exits:

`at_exit { monitor.stop }
`

### 

The passed argument to the block is an instance of `WDM::Change`. This class has two methods: 

`Change#path`: The absolute path to the change.

- `Change#type`: This can be one of the following values: `:added`, `:modified`, `:removed`, `:renamed_old_file` or `:renamed_new_file`.

## 

Download the source, then run the following:

`$ bundle exec rake compile
`

To get debug messages, you need to enable them like so:

`$ bundle exec rake clean compile -- --with-cflags=-DWDM_DEBUG_ENABLED=TRUE
`

### 

```
`$ bundle exec rake spec
`
```

## 

- Fork it

- Create your feature branch (`git checkout -b my-new-feature`)

- Add a spec for your change

- Commit your changes (`git commit -am 'Added some feature'`)

- Push to the branch (`git push origin my-new-feature`)

- Create new Pull Request

- Ensure CI runs green.

## 

Maher Sallam

  Generated on Wed Mar 25 23:39:28 2026 by
  yard
  0.9.38 (ruby-3.4.3).