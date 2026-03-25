# Module: Brakeman
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman.rb,

  lib/brakeman/logger.rb,
 lib/brakeman/version.rb,
 lib/brakeman/app_tree.rb,
 lib/brakeman/messages.rb,
 lib/brakeman/file_path.rb,
 lib/brakeman/processor.rb,
 lib/brakeman/commandline.rb,
 lib/brakeman/file_parser.rb,
 lib/brakeman/report/pager.rb,
 lib/brakeman/tracker/model.rb,
 lib/brakeman/tracker/config.rb,
 lib/brakeman/tracker/library.rb,
 lib/brakeman/tracker/template.rb,
 lib/brakeman/tracker/constants.rb,
 lib/brakeman/tracker/collection.rb,
 lib/brakeman/tracker/controller.rb,
 lib/brakeman/tracker/file_cache.rb,
 lib/brakeman/parsers/rails_erubi.rb,
 lib/brakeman/tracker/method_info.rb,
 lib/brakeman/report/ignore/config.rb,
 lib/brakeman/parsers/haml_embedded.rb,
 lib/brakeman/parsers/template_parser.rb,
 lib/brakeman/report/ignore/interactive.rb,
 lib/brakeman/processors/lib/render_path.rb,
 lib/brakeman/processors/lib/safe_call_helper.rb,
 lib/brakeman/codeclimate/engine_configuration.rb,
 lib/brakeman/processors/lib/file_type_detector.rb,
 lib/brakeman/processors/lib/call_conversion_helper.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** CallConversionHelper, Codeclimate, ControllerMethods, FakeHamlFilter, Logger, Messages, ModelMethods, ModuleHelper, Options, ProcessorHelper, RenderHelper, RouteHelper, SafeCallHelper, Util, WarningCodes
    
  
    
      **Classes:** ASTFile, AliasProcessor, AppTree, BaseCheck, BaseProcessor, BasicProcessor, CallIndex, CheckBasicAuth, CheckBasicAuthTimingAttack, CheckCSRFTokenForgeryCVE, CheckContentTag, CheckCookieSerialization, CheckCreateWith, CheckCrossSiteScripting, CheckDefaultRoutes, CheckDeserialize, CheckDetailedExceptions, CheckDigestDoS, CheckDivideByZero, CheckDynamicFinders, CheckEOLRails, CheckEOLRuby, CheckEscapeFunction, CheckEvaluation, CheckExecute, CheckFileAccess, CheckFileDisclosure, CheckFilterSkipping, CheckForceSSL, CheckForgerySetting, CheckHeaderDoS, CheckI18nXSS, CheckJRubyXML, CheckJSONEncoding, CheckJSONEntityEscape, CheckJSONParsing, CheckLinkTo, CheckLinkToHref, CheckMailTo, CheckMassAssignment, CheckMimeTypeDoS, CheckModelAttrAccessible, CheckModelAttributes, CheckModelSerialize, CheckNestedAttributes, CheckNestedAttributesBypass, CheckNumberToCurrency, CheckPageCachingCVE, CheckPathname, CheckPermitAttributes, CheckQuoteTableName, CheckRansack, CheckRedirect, CheckRegexDoS, CheckRender, CheckRenderDoS, CheckRenderInline, CheckRenderRCE, CheckResponseSplitting, CheckReverseTabnabbing, CheckRouteDoS, CheckSQL, CheckSQLCVEs, CheckSSLVerify, CheckSafeBufferManipulation, CheckSanitizeConfigCve, CheckSanitizeMethods, CheckSecrets, CheckSelectTag, CheckSelectVulnerability, CheckSend, CheckSendFile, CheckSessionManipulation, CheckSessionSettings, CheckSimpleFormat, CheckSingleQuotes, CheckSkipBeforeFilter, CheckSprocketsPathTraversal, CheckStripTags, CheckSymbolDoS, CheckSymbolDoSCVE, CheckTemplateInjection, CheckTranslateBug, CheckUnsafeReflection, CheckUnsafeReflectionMethods, CheckUnscopedFind, CheckValidationRegex, CheckVerbConfusion, CheckWeakHash, CheckWeakRSAKey, CheckWithoutProtection, CheckXMLDoS, CheckYAMLParsing, Checks, Collection, Commandline, Config, ConfigAliasProcessor, ConfigProcessor, Constant, Constants, Controller, ControllerAliasProcessor, ControllerProcessor, DependencyError, Differ, EOLCheck, ErbTemplateProcessor, Erubi, ErubiTemplateProcessor, FileCache, FileParser, FilePath, FileTypeDetector, FindAllCalls, FindCall, FindReturnValue, GemProcessor, Haml6TemplateProcessor, HamlTemplateProcessor, IgnoreConfig, InteractiveIgnorer, Library, LibraryProcessor, MethodInfo, MissingChecksError, Model, ModelProcessor, NoApplication, NoBrakemanError, OutputProcessor, Pager, Processor, Rails2ConfigProcessor, Rails2RoutesProcessor, Rails3ConfigProcessor, Rails3RoutesProcessor, Rails4ConfigProcessor, RenderPath, Report, RescanReport, Rescanner, RouteAliasProcessor, RoutesProcessor, Scanner, SexpProcessor, SlimTemplateProcessor, Template, TemplateAliasProcessor, TemplateParser, TemplateProcessor, Tracker, Warning
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        Warnings_Found_Exit_Code =
          
  
    

This exit code is used when warnings are found and the –exit-on-warn option is set

  

  

        
        

```
3

```

      
        No_App_Found_Exit_Code =
          
  
    

Exit code returned when no Rails application is detected

  

  

        
        

```
4

```

      
        Not_Latest_Version_Exit_Code =
          
  
    

Exit code returned when brakeman was outdated

  

  

        
        

```
5

```

      
        Missing_Checks_Exit_Code =
          
  
    

Exit code returned when user requests non-existent checks

  

  

        
        

```
6

```

      
        Errors_Found_Exit_Code =
          
  
    

Exit code returned when errors were found and the –exit-on-error option is set

  

  

        
        

```
7

```

      
        Empty_Ignore_Note_Exit_Code =
          
  
    

Exit code returned when an ignored warning has no note and –ensure-ignore-notes is set

  

  

        
        

```
8

```

      
        Obsolete_Ignore_Entries_Exit_Code =
          
  
    

Exit code returned when at least one obsolete ignore entry is present and `--ensure-no-obsolete-ignore-entries` is set.

  

  

        
        

```
9

```

      
        CONFIG_FILES =
          
        
        

```
begin
  [
    File.expand_path("~/.brakeman/config.yml"),
    File.expand_path("/etc/brakeman/config.yml")
  ]
rescue ArgumentError
  # In case $HOME or $USER aren't defined for use of `~`
  [
    File.expand_path("/etc/brakeman/config.yml")
  ]
end

```

      
        Version =
          
        
        

```
"8.0.4"

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**add_external_checks**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**alert**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**announce**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**check_for_missing_checks**(included_checks, excluded_checks, enabled_checks)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**cleanup**(newline = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**compare**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Compare JSON output from a previous scan and return the diff of the two scans.

  

      
        
- 
  
    
      .**config_file**(custom_location, app_path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**debug**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**debug=**(val)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**default_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Default set of options.

  

      
        
- 
  
    
      .**dump_config**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Output configuration to YAML.

  

      
        
- 
  
    
      .**ensure_latest**(days_old: 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns quit message unless the latest version of Brakeman matches the current version.

  

      
        
- 
  
    
      .**filter_warnings**(tracker, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**get_output_formats**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Determine output formats based on options or options.

  

      
        
- 
  
    
      .**ignore_file_entries_with_empty_notes**(file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of alert fingerprints for any ignored warnings without notes found in the specified ignore file (if it exists).

  

      
        
- 
  
    
      .**list_checks**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Output list of checks (for `-k` option).

  

      
        
- 
  
    
      .**load_brakeman_dependency**(name, allow_fail = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**load_options**(line_options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Load options from YAML file.

  

      
        
- 
  
    
      .**logger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**logger=**(log)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**process_step**(description)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**quiet=**(val)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**rescan**(tracker, files, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Rescan a subset of files in a Rails application.

  

      
        
- 
  
    
      .**run**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Run Brakeman scan.

  

      
        
- 
  
    
      .**scan**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Run a scan.

  

      
        
- 
  
    
      .**set_default_logger**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**set_options**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets up options for run, checks given application path.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**add_external_checks**(options)  ⇒ Object 
  

  

  

  
    
      

```

644
645
646
647
648
```

    
    
      

```
# File 'lib/brakeman.rb', line 644

def self.add_external_checks options
  options[:additional_checks_path].each do |path|
    Brakeman::Checks.initialize_checks path
  end if options[:additional_checks_path]
end

```

    
  

    
      
  
### 
  
    .**alert**(message)  ⇒ Object 
  

  

  

  
    
      

```

544
545
546
```

    
    
      

```
# File 'lib/brakeman.rb', line 544

def self.alert message
  logger.alert message
end

```

    
  

    
      
  
### 
  
    .**announce**(message)  ⇒ Object 
  

  

  

  
    
      

```

540
541
542
```

    
    
      

```
# File 'lib/brakeman.rb', line 540

def self.announce message
  logger.announce message
end

```

    
  

    
      
  
### 
  
    .**check_for_missing_checks**(included_checks, excluded_checks, enabled_checks)  ⇒ Object 
  

  

  

  
    
      

```

650
651
652
653
654
655
656
657
658
```

    
    
      

```
# File 'lib/brakeman.rb', line 650

def self.check_for_missing_checks included_checks, excluded_checks, enabled_checks
  checks = included_checks.to_a + excluded_checks.to_a + enabled_checks.to_a

  missing = Brakeman::Checks.missing_checks(checks)

  unless missing.empty?
    raise MissingChecksError, "Could not find specified check#{missing.length > 1 ? 's' : ''}: #{missing.map {|c| "`#{c}`"}.join(', ')}"
  end
end

```

    
  

    
      
  
### 
  
    .**cleanup**(newline = true)  ⇒ Object 
  

  

  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/brakeman.rb', line 122

def self.cleanup(newline = true)
  @logger.cleanup(newline) if @logger
end

```

    
  

    
      
  
### 
  
    .**compare**(options)  ⇒ Object 
  

  

  

  
    

Compare JSON output from a previous scan and return the diff of the two scans

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
```

    
    
      

```
# File 'lib/brakeman.rb', line 553

def self.compare options
  require 'json'
  require 'brakeman/differ'
  raise ArgumentError.new("Comparison file doesn't exist") unless File.exist? options[:previous_results_json]

  begin
    previous_results = JSON.parse(File.read(options[:previous_results_json]), :symbolize_names => true)[:warnings]
  rescue JSON::ParserError
    self.alert "Error parsing comparison file: #{options[:previous_results_json]}"
    exit!
  end

  tracker = run(options)
  new_report = JSON.parse(tracker.report.to_json, symbolize_names: true)

  new_results = new_report[:warnings]
  obsolete_ignored = tracker.unused_fingerprints

  Brakeman::Differ.new(new_results, previous_results).diff.tap do |diff|
    diff[:obsolete] = obsolete_ignored
  end
end

```

    
  

    
      
  
### 
  
    .**config_file**(custom_location, app_path)  ⇒ Object 
  

  

  

  
    
      

```

218
219
220
221
222
```

    
    
      

```
# File 'lib/brakeman.rb', line 218

def self.config_file custom_location, app_path
  app_config = File.expand_path(File.join(app_path, "config", "brakeman.yml"))
  supported_locations = [File.expand_path(custom_location || ""), app_config] + CONFIG_FILES
  supported_locations.detect {|f| File.file?(f) }
end

```

    
  

    
      
  
### 
  
    .**debug**(message)  ⇒ Object 
  

  

  

  
    
      

```

548
549
550
```

    
    
      

```
# File 'lib/brakeman.rb', line 548

def self.debug message
  logger.debug message
end

```

    
  

    
      
  
### 
  
    .**debug=**(val)  ⇒ Object 
  

  

  

  
    
      

```

660
661
662
```

    
    
      

```
# File 'lib/brakeman.rb', line 660

def self.debug= val
  @debug = val
end

```

    
  

    
      
  
### 
  
    .**default_options**  ⇒ Object 
  

  

  

  
    

Default set of options

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman.rb', line 225

def self.default_options
  { :assume_all_routes => true,
    :check_arguments => true,
    :collapse_mass_assignment => false,
    :combine_locations => true,
    :engine_paths => ["engines/*"],
    :exit_on_error => true,
    :exit_on_warn => true,
    :highlight_user_input => true,
    :html_style => "#{File.expand_path(File.dirname(__FILE__))}/brakeman/format/style.css",
    :ignore_model_output => false,
    :ignore_redirect_to_model => true,
    :message_limit => 100,
    :min_confidence => 2,
    :output_color => true,
    :pager => true,
    :parallel_checks => true,
    :parser_timeout => 10,
    :use_prism => true,
    :relative_path => false,
    :report_progress => true,
    :safe_methods => Set.new,
    :show_ignored => false,
    :sql_safe_methods => Set.new,
    :skip_checks => Set.new,
    :skip_vendor => true,
  }
end

```

    
  

    
      
  
### 
  
    .**dump_config**(options)  ⇒ Object 
  

  

  

  
    

Output configuration to YAML

  

  

  
    
      

```

384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
```

    
    
      

```
# File 'lib/brakeman.rb', line 384

def self.dump_config options
  require 'yaml'
  if options[:create_config].is_a? String
    file = options[:create_config]
  else
    file = nil
  end

  options.delete :create_config

  if options[:logger]
    @logger = options.delete(:logger)
  else
    set_default_logger(options)
  end

  options.each do |k,v|
    if v.is_a? Set
      options[k] = v.to_a
    end
  end

  if file
    File.open file, "w" do |f|
      YAML.dump options, f
    end

    announce "Output configuration to #{file}"
  else
    $stdout.puts YAML.dump(options)
  end
end

```

    
  

    
      
  
### 
  
    .**ensure_latest**(days_old: 0)  ⇒ Object 
  

  

  

  
    

Returns quit message unless the latest version of Brakeman matches the current version.

Optionally checks that the latest version is at least the specified number of days old.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman.rb', line 422

def self.ensure_latest(days_old: 0)
  require 'date'

  current = Brakeman::Version
  latest = Gem.latest_spec_for('brakeman')
  release_date = latest.date.to_date
  latest_version = latest.version.to_s

  if (Date.today - latest.date.to_date) >= days_old
    if current != latest_version
      return "Brakeman #{current} is not the latest version #{latest_version}"
    else
      false
    end
  else
    false
  end
end

```

    
  

    
      
  
### 
  
    .**filter_warnings**(tracker, options)  ⇒ Object 
  

  

  

  
    
      

```

614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
```

    
    
      

```
# File 'lib/brakeman.rb', line 614

def self.filter_warnings tracker, options
  require 'brakeman/report/ignore/config'
  config = nil

  app_tree = Brakeman::AppTree.from_options(options)

  if options[:ignore_file]
    file = options[:ignore_file]
  elsif app_tree.exists? "config/brakeman.ignore"
    file = app_tree.expand_path("config/brakeman.ignore")
  elsif not options[:interactive_ignore]
    return
  end

  process_step "Filtering warnings..." do
    if options[:interactive_ignore]
      require 'brakeman/report/ignore/interactive'
      logger.cleanup
      config = InteractiveIgnorer.new(file, tracker.warnings).start
    else
      logger.announce "Using '#{file}' to filter warnings"
      config = IgnoreConfig.new(file, tracker.warnings)
      config.read_from_file
      config.filter_ignored
    end
  end

  tracker.ignored_filter = config
end

```

    
  

    
      
  
### 
  
    .**get_output_formats**(options)  ⇒ Object 
  

  

  

  
    

Determine output formats based on options or options

  

  

  
    
      

```

256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
```

    
    
      

```
# File 'lib/brakeman.rb', line 256

def self.get_output_formats options
  #Set output format
  if options[:output_format] && options[:output_files] && options[:output_files].size > 1
    raise ArgumentError, "Cannot specify output format if multiple output files specified"
  end
  if options[:output_format]
    get_formats_from_output_format options[:output_format]
  elsif options[:output_files]
    get_formats_from_output_files options[:output_files]
  else
    begin
      self.load_brakeman_dependency 'terminal-table', :allow_fail
      return [:to_s]
    rescue LoadError
      return [:to_json]
    end
  end
end

```

    
  

    
      
  
### 
  
    .**ignore_file_entries_with_empty_notes**(file)  ⇒ Object 
  

  

  

  
    

Returns an array of alert fingerprints for any ignored warnings without notes found in the specified ignore file (if it exists).

  

  

  
    
      

```

604
605
606
607
608
609
610
611
612
```

    
    
      

```
# File 'lib/brakeman.rb', line 604

def self.ignore_file_entries_with_empty_notes file
  return [] unless file

  require 'brakeman/report/ignore/config'

  config = IgnoreConfig.new(file, nil)
  config.read_from_file
  config.already_ignored_entries_with_empty_notes.map { |i| i[:fingerprint] }
end

```

    
  

    
      
  
### 
  
    .**list_checks**(options)  ⇒ Object 
  

  

  

  
    

Output list of checks (for `-k` option)

  

  

  
    
      

```

362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
```

    
    
      

```
# File 'lib/brakeman.rb', line 362

def self.list_checks options
  require 'brakeman/scanner'

  add_external_checks options

  if options[:list_optional_checks]
    $stderr.puts "Optional Checks:"
    checks = Checks.optional_checks
  else
    $stderr.puts "Available Checks:"
    checks = Checks.checks
  end

  format_length = 30

  $stderr.puts "-" * format_length
  checks.each do |check|
    $stderr.printf("%-#{format_length}s%s\n", check.name, check.description)
  end
end

```

    
  

    
      
  
### 
  
    .**load_brakeman_dependency**(name, allow_fail = false)  ⇒ Object 
  

  

  

  
    
      

```

576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
```

    
    
      

```
# File 'lib/brakeman.rb', line 576

def self.load_brakeman_dependency name, allow_fail = false
  return if @loaded_dependencies.include? name

  unless @vendored_paths
    path_load = "#{File.expand_path(File.dirname(__FILE__))}/../bundle/load.rb"

    if File.exist? path_load
      require path_load
    end

    @vendored_paths = true
  end

  begin
    require name
  rescue LoadError => e
    if allow_fail
      raise e
    else
      $stderr.puts e.message
      $stderr.puts "Please install the appropriate dependency: #{name}."
      exit!(-1)
    end
  end
end

```

    
  

    
      
  
### 
  
    .**load_options**(line_options)  ⇒ Object 
  

  

  

  
    

Load options from YAML file

  

  

  
    
      

```

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
190
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
```

    
    
      

```
# File 'lib/brakeman.rb', line 168

def self.load_options line_options
  custom_location = line_options[:config_file]
  app_path = line_options[:app_path]

  #Load configuration file
  if config = config_file(custom_location, app_path)
    require 'yaml'
    options = YAML.safe_load_file config, permitted_classes: [Symbol], symbolize_names: true

    if options
      options.each { |k, v| options[k] = Set.new v if v.is_a? Array }

      # After parsing the yaml config file for options, convert any string keys into symbols.
      options.keys.select {|k| k.is_a? String}.map {|k| k.to_sym }.each {|k| options[k] = options[k.to_s]; options.delete(k.to_s) }

      # Brakeman.logger is probably not set yet
      logger = Brakeman::Logger.get_logger(options.merge(line_options))

      unless line_options[:allow_check_paths_in_config]
        if options.include? :additional_checks_path
          options.delete :additional_checks_path

          logger.alert 'Ignoring additional check paths in config file. Use --allow-check-paths-in-config to allow'
        end
      end

      logger.alert "Using configuration in #{config}"
      options
    else
      logger = Brakeman::Logger.get_logger(line_options)
      logger.alert "Empty configuration file: #{config}"
      {}
    end
  else
    {}
  end
end

```

    
  

    
      
  
### 
  
    .**logger**  ⇒ Object 
  

  

  

  
    
      

```

110
111
112
```

    
    
      

```
# File 'lib/brakeman.rb', line 110

def self.logger
  @logger
end

```

    
  

    
      
  
### 
  
    .**logger=**(log)  ⇒ Object 
  

  

  

  
    
      

```

114
115
116
```

    
    
      

```
# File 'lib/brakeman.rb', line 114

def self.logger= log
  @logger = log
end

```

    
  

    
      
  
### 
  
    .**process_step**(description)  ⇒ Object 
  

  

  

  
    
      

```

668
669
670
```

    
    
      

```
# File 'lib/brakeman.rb', line 668

def self.process_step(description, &)
  logger.context(description, &)
end

```

    
  

    
      
  
### 
  
    .**quiet=**(val)  ⇒ Object 
  

  

  

  
    
      

```

664
665
666
```

    
    
      

```
# File 'lib/brakeman.rb', line 664

def self.quiet= val
  @quiet = val
end

```

    
  

    
      
  
### 
  
    .**rescan**(tracker, files, options = {})  ⇒ Object 
  

  

  

  
    

Rescan a subset of files in a Rails application.

A full scan must have been run already to use this method. The returned Tracker object from Brakeman.run is used as a starting point for the rescan.

Options may be given as a hash with the same values as Brakeman.run. Note that these options will be merged into the Tracker.

This method returns a RescanReport object with information about the scan. However, the Tracker object will also be modified as the scan is run.

  

  

  
    
      

```

529
530
531
532
533
534
535
536
537
538
```

    
    
      

```
# File 'lib/brakeman.rb', line 529

def self.rescan tracker, files, options = {}
  require 'brakeman/rescanner'

  options = tracker.options.merge options

  @quiet = !!tracker.options[:quiet]
  @debug = !!tracker.options[:debug]

  Rescanner.new(options, tracker.processor, files).recheck
end

```

    
  

    
      
  
### 
  
    .**run**(options)  ⇒ Object 
  

  

  

  
    

Run Brakeman scan. Returns Tracker object.

Options:

```
* :app_path - path to root of Rails app (required)
* :additional_checks_path - array of additional directories containing additional out-of-tree checks to run
* :additional_libs_path - array of additional application relative lib directories (ex. app/mailers) to process
* :assume_all_routes - assume all methods are routes (default: true)
* :check_arguments - check arguments of methods (default: true)
* :collapse_mass_assignment - report unprotected models in single warning (default: false)
* :combine_locations - combine warning locations (default: true)
* :config_file - configuration file
* :escape_html - escape HTML by default (automatic)
* :exit_on_error - only affects Commandline module (default: true)
* :exit_on_warn - only affects Commandline module (default: true)
* :github_repo - github repo to use for file links (user/repo[/path][@ref])
* :highlight_user_input - highlight user input in reported warnings (default: true)
* :html_style - path to CSS file
* :ignore_model_output - consider models safe (default: false)
* :interprocedural - limited interprocedural processing of method calls (default: false)
* :message_limit - limit length of messages
* :min_confidence - minimum confidence (0-2, 0 is highest)
* :output_files - files for output
* :output_formats - formats for output (:to_s, :to_tabs, :to_csv, :to_html)
* :parallel_checks - run checks in parallel (default: true)
* :parser_timeout - set timeout for parsing an individual file (default: 10 seconds)
* :print_report - if no output file specified, print to stdout (default: false)
* :quiet - suppress most messages (default: true)
* :rails3 - force Rails 3 mode (automatic)
* :rails4 - force Rails 4 mode (automatic)
* :rails5 - force Rails 5 mode (automatic)
* :rails6 - force Rails 6 mode (automatic)
* :report_routes - show found routes on controllers (default: false)
* :run_checks - array of checks to run (run all if not specified)
* :safe_methods - array of methods to consider safe
* :show_ignored - Display warnings that are usually ignored
* :sql_safe_methods - array of sql sanitization methods to consider safe
* :skip_vendor - do not process vendor/ directory (default: true)
* :skip_checks - checks not to run (run all if not specified)
* :absolute_paths - show absolute path of each file (default: false)
* :summary_only - only output summary section of report for plain/table (:summary_only, :no_summary, true)

```

Alternatively, just supply a path as a string.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman.rb', line 81

def self.run options
  if not $stderr.tty? and options[:report_progress].nil?
    options[:report_progress] = false
  end

  options = set_options options

  @quiet = !!options[:quiet]
  @debug = !!options[:debug]

  if @quiet
    options[:report_progress] = false
  end

  @logger = options[:logger] || set_default_logger(options)

  if options[:use_prism]
    begin
      require 'prism'
    rescue LoadError => e
      Brakeman.alert "Asked to use Prism, but failed to load: #{e}"
    end
  end

  Brakeman.announce "Brakeman v#{Brakeman::Version}"

  scan options
end

```

    
  

    
      
  
### 
  
    .**scan**(options)  ⇒ Object 
  

  

  

  
    

Run a scan. Generally called from Brakeman.run instead of directly.

  

  

  
    
      

```

442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
```

    
    
      

```
# File 'lib/brakeman.rb', line 442

def self.scan options
  #Load scanner
  scanner, tracker = nil

  process_step 'Loading scanner' do
    begin
      require 'brakeman/scanner'
    rescue LoadError
      raise NoBrakemanError, 'Cannot find lib/ directory.'
    end

    add_external_checks options

    #Start scanning
    scanner = Scanner.new options
    tracker = scanner.tracker

    check_for_missing_checks options[:run_checks], options[:skip_checks], options[:enable_checks]
  end

  logger.announce "Scanning #{tracker.app_path}"
  scanner.process

  tracker.run_checks

  self.filter_warnings tracker, options

  if options[:output_files]
    process_step 'Generating report' do
      write_report_to_files tracker, options[:output_files]
    end
  elsif options[:print_report]
    process_step 'Generating report' do
      write_report_to_formats tracker, options[:output_formats]
    end
  end

  tracker
end

```

    
  

    
      
  
### 
  
    .**set_default_logger**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

118
119
120
```

    
    
      

```
# File 'lib/brakeman.rb', line 118

def self.set_default_logger(options = {})
  @logger = Brakeman::Logger.get_logger(options)
end

```

    
  

    
      
  
### 
  
    .**set_options**(options)  ⇒ Object 
  

  

  

  
    

Sets up options for run, checks given application path

  

  

  
    
      

```

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
140
141
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
155
156
157
158
159
160
161
162
163
164
165
```

    
    
      

```
# File 'lib/brakeman.rb', line 127

def self.set_options options
  if options.is_a? String
    options = { :app_path => options }
  end

  if options[:quiet] == :command_line
    command_line = true
    options.delete :quiet
  end

  options = default_options.merge(load_options(options)).merge(options)

  if options[:quiet].nil? and not command_line
    options[:quiet] = true
  end

  if options[:rails4]
    options[:rails3] = true
  elsif options[:rails5]
    options[:rails3] = true
    options[:rails4] = true
  elsif options[:rails6]
    options[:rails3] = true
    options[:rails4] = true
    options[:rails5] = true
  end

  options[:output_formats] = get_output_formats options
  options[:github_url] = get_github_url options

  # Use ENV value only if option was not already explicitly set
  # (i.e. prefer commandline option over environment variable).
  if options[:gemfile].nil? and ENV['BUNDLE_GEMFILE'] and not ENV['BUNDLE_GEMFILE'].empty?
    options[:gemfile] = ENV['BUNDLE_GEMFILE']
  end

  options
end

```