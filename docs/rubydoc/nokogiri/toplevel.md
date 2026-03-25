# Top Level Namespace
  
  
  

  

  
  
  
  
  

  

  

## Defined Under Namespace

  
    
      **Modules:** Nokogiri, XSD
    
  
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        PACKAGE_ROOT_DIR =
          
  
    

helpful constants

  

  

        
        

```
File.expand_path(File.join(File.dirname(__FILE__), "..", ".."))

```

      
        REQUIRED_LIBXML_VERSION =
          
        
        

```
"2.9.2"

```

      
        RECOMMENDED_LIBXML_VERSION =
          
        
        

```
"2.12.0"

```

      
        REQUIRED_MINI_PORTILE_VERSION =
          
  
    

keep this version in sync with the one in the gemspec

  

  

        
        

```
"~> 2.8.2"

```

      
        REQUIRED_PKG_CONFIG_VERSION =
          
        
        

```
"~> 1.1"

```

      
        OTHER_LIBRARY_VERSIONS =
          
  
    

Keep track of what versions of what libraries we build against

  

  

        
        

```
{}

```

      
        NOKOGIRI_HELP_MESSAGE =
          
        
        

```
"USAGE: ruby \#{$PROGRAM_NAME} [options]\n\n  Flags that are always valid:\n\n    --use-system-libraries\n    --enable-system-libraries\n        Use system libraries instead of building and using the packaged libraries.\n\n    --disable-system-libraries\n        Use the packaged libraries, and ignore the system libraries. This is the default on most\n        platforms, and overrides `--use-system-libraries` and the environment variable\n        `NOKOGIRI_USE_SYSTEM_LIBRARIES`.\n\n    --disable-clean\n        Do not clean out intermediate files after successful build.\n\n    --prevent-strip\n        Take steps to prevent stripping the symbol table and debugging info from the shared\n        library, potentially overriding RbConfig's CFLAGS/LDFLAGS/DLDFLAGS.\n\n\n  Flags only used when using system libraries:\n\n    General:\n\n      --with-opt-dir=DIRECTORY\n          Look for headers and libraries in DIRECTORY.\n\n      --with-opt-lib=DIRECTORY\n          Look for libraries in DIRECTORY.\n\n      --with-opt-include=DIRECTORY\n          Look for headers in DIRECTORY.\n\n\n    Related to libxml2:\n\n      --with-xml2-dir=DIRECTORY\n          Look for xml2 headers and library in DIRECTORY.\n\n      --with-xml2-lib=DIRECTORY\n          Look for xml2 library in DIRECTORY.\n\n      --with-xml2-include=DIRECTORY\n          Look for xml2 headers in DIRECTORY.\n\n      --with-xml2-source-dir=DIRECTORY\n          (dev only) Build libxml2 from the source code in DIRECTORY\n\n      --disable-xml2-legacy\n          Do not build libxml2 with zlib, liblzma, or HTTP support. This will become the default\n          in a future version of Nokogiri.\n\n\n    Related to libxslt:\n\n      --with-xslt-dir=DIRECTORY\n          Look for xslt headers and library in DIRECTORY.\n\n      --with-xslt-lib=DIRECTORY\n          Look for xslt library in DIRECTORY.\n\n      --with-xslt-include=DIRECTORY\n          Look for xslt headers in DIRECTORY.\n\n      --with-xslt-source-dir=DIRECTORY\n          (dev only) Build libxslt from the source code in DIRECTORY\n\n\n    Related to libexslt:\n\n      --with-exslt-dir=DIRECTORY\n          Look for exslt headers and library in DIRECTORY.\n\n      --with-exslt-lib=DIRECTORY\n          Look for exslt library in DIRECTORY.\n\n      --with-exslt-include=DIRECTORY\n          Look for exslt headers in DIRECTORY.\n\n\n    Related to iconv:\n\n      --with-iconv-dir=DIRECTORY\n          Look for iconv headers and library in DIRECTORY.\n\n      --with-iconv-lib=DIRECTORY\n          Look for iconv library in DIRECTORY.\n\n      --with-iconv-include=DIRECTORY\n          Look for iconv headers in DIRECTORY.\n\n\n    Related to zlib (ignored if `--disable-xml2-legacy` is used):\n\n      --with-zlib-dir=DIRECTORY\n          Look for zlib headers and library in DIRECTORY.\n\n      --with-zlib-lib=DIRECTORY\n          Look for zlib library in DIRECTORY.\n\n      --with-zlib-include=DIRECTORY\n          Look for zlib headers in DIRECTORY.\n\n\n  Flags only used when building and using the packaged libraries:\n\n    --disable-static\n        Do not statically link packaged libraries, instead use shared libraries.\n\n    --enable-cross-build\n        Enable cross-build mode. (You probably do not want to set this manually.)\n\n\n  Environment variables used:\n\n    NOKOGIRI_USE_SYSTEM_LIBRARIES\n        Equivalent to `--enable-system-libraries` when set, even if nil or blank.\n\n    AR\n        Use this path to invoke the library archiver instead of `RbConfig::CONFIG['AR']`\n\n    CC\n        Use this path to invoke the compiler instead of `RbConfig::CONFIG['CC']`\n\n    CPPFLAGS\n        If this string is accepted by the C preprocessor, add it to the flags passed to the C preprocessor\n\n    CFLAGS\n        If this string is accepted by the compiler, add it to the flags passed to the compiler\n\n    LD\n        Use this path to invoke the linker instead of `RbConfig::CONFIG['LD']`\n\n    LDFLAGS\n        If this string is accepted by the linker, add it to the flags passed to the linker\n\n    LIBS\n        Add this string to the flags passed to the linker\n"

```

      
        LOCAL_PACKAGE_RESPONSE =
          
        
        

```
Object.new

```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**abort_could_not_find_library**(lib)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**aix?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**chdir_for_build**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**concat_flags**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**config_clean?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

utility functions.

  

      
        
- 
  
    
      #**config_cross_build?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**config_static?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**config_system_libraries?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**config_with_xml2_legacy?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**copy_packaged_libraries_headers**(to_path:, from_recipes:)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**darwin?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**do_clean**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**do_help**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ensure_func**(func, headers = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ensure_package_configuration**(opt: nil, pc: nil, lib:, func:, headers:)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**gnome_source**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**have_libxml_headers?**(version = nil)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**have_package_configuration**(opt: nil, pc: nil, lib:, func:, headers:)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

set up mkmf to link against the library if we can find it.

  

      
        
- 
  
    
      #**iconv_configure_flags**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**libflag_to_filename**(ldflag)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**local_have_library**(lib, func = nil, headers = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**needs_darwin_linker_hack**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

In ruby 3.2, symbol resolution changed on Darwin, to introduce the `-bundle_loader` flag to resolve symbols against the ruby binary.

  

      
        
- 
  
    
      #**nix?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**Nokogiri**(*args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse a document contained in `args`.

  

      
        
- 
  
    
      #**openbsd?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**preserving_globals**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_recipe**(name, version, static_p, cross_p, cacheable_p = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sh_export_path**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**solaris?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**truffle?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**try_link_iconv**(using = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**try_package_configuration**(pc)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

wrapper around MakeMakefil#pkg_config and the PKGConfig gem.

  

      
        
- 
  
    
      #**unix?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**windows?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**zlib_source**(version_string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**abort_could_not_find_library**(lib)  ⇒ Object 
  

  

  

  
    
      

```

319
320
321
322
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 319

def abort_could_not_find_library(lib)
  callers = caller(1..2).join("\n")
  abort("-----\n#{callers}\n#{lib} is missing. Please locate mkmf.log to investigate how it is failing.\n-----")
end

```

    
  

    
      
  
### 
  
    #**aix?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

208
209
210
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 208

def aix?
  RbConfig::CONFIG["target_os"].include?("aix")
end

```

    
  

    
      
  
### 
  
    #**chdir_for_build**(&block)  ⇒ Object 
  

  

  

  
    
      

```

324
325
326
327
328
329
330
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 324

def chdir_for_build(&block)
  # When using rake-compiler-dock on Windows, the underlying Virtualbox shared
  # folders don't support symlinks, but libiconv expects it for a build on
  # Linux. We work around this limitation by using the temp dir for cooking.
  build_dir = /mingw|mswin|cygwin/.match?(ENV["RCD_HOST_RUBY_PLATFORM"].to_s) ? "/tmp" : "."
  Dir.chdir(build_dir, &block)
end

```

    
  

    
      
  
### 
  
    #**concat_flags**(*args)  ⇒ Object 
  

  

  

  
    
      

```

224
225
226
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 224

def concat_flags(*args)
  args.compact.join(" ")
end

```

    
  

    
      
  
### 
  
    #**config_clean?**  ⇒ Boolean 
  

  

  

  
    

utility functions

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

169
170
171
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 169

def config_clean?
  enable_config("clean", true)
end

```

    
  

    
      
  
### 
  
    #**config_cross_build?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

178
179
180
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 178

def config_cross_build?
  enable_config("cross-build")
end

```

    
  

    
      
  
### 
  
    #**config_static?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

173
174
175
176
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 173

def config_static?
  default_static = !truffle?
  enable_config("static", default_static)
end

```

    
  

    
      
  
### 
  
    #**config_system_libraries?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

182
183
184
185
186
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 182

def config_system_libraries?
  enable_config("system-libraries", ENV.key?("NOKOGIRI_USE_SYSTEM_LIBRARIES")) do |_, default|
    arg_config("--use-system-libraries", default)
  end
end

```

    
  

    
      
  
### 
  
    #**config_with_xml2_legacy?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

188
189
190
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 188

def config_with_xml2_legacy?
  enable_config("xml2-legacy", true)
end

```

    
  

    
      
  
### 
  
    #**copy_packaged_libraries_headers**(to_path:, from_recipes:)  ⇒ Object 
  

  

  

  
    
      

```

557
558
559
560
561
562
563
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 557

def copy_packaged_libraries_headers(to_path:, from_recipes:)
  FileUtils.rm_rf(to_path, secure: true)
  FileUtils.mkdir(to_path)
  from_recipes.each do |recipe|
    FileUtils.cp_r(Dir[File.join(recipe.path, "include/*")], to_path)
  end
end

```

    
  

    
      
  
### 
  
    #**darwin?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

200
201
202
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 200

def darwin?
  RbConfig::CONFIG["target_os"].include?("darwin")
end

```

    
  

    
      
  
### 
  
    #**do_clean**  ⇒ Object 
  

  

  

  
    
      

```

570
571
572
573
574
575
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
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 570

def do_clean
  root = Pathname(PACKAGE_ROOT_DIR)
  pwd  = Pathname(Dir.pwd)

  # Skip if this is a development work tree
  unless (root + ".git").exist?
    message("Cleaning files only used during build.\n")

    # (root + 'tmp') cannot be removed at this stage because
    # nokogiri.so is yet to be copied to lib.

    # clean the ports build directory
    Pathname.glob(pwd.join("tmp", "*", "ports")) do |dir|
      FileUtils.rm_rf(dir, verbose: true)
    end

    if config_static?
      # ports installation can be safely removed if statically linked.
      FileUtils.rm_rf(root + "ports", verbose: true)
    else
      FileUtils.rm_rf(root + "ports" + "archives", verbose: true)
    end
  end

  exit!(0)
end

```

    
  

    
      
  
### 
  
    #**do_help**  ⇒ Object 
  

  

  

  
    
      

```

565
566
567
568
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 565

def do_help
  print(NOKOGIRI_HELP_MESSAGE)
  exit!(0)
end

```

    
  

    
      
  
### 
  
    #**ensure_func**(func, headers = nil)  ⇒ Object 
  

  

  

  
    
      

```

308
309
310
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 308

def ensure_func(func, headers = nil)
  have_func(func, headers) || abort_could_not_find_library(func)
end

```

    
  

    
      
  
### 
  
    #**ensure_package_configuration**(opt: nil, pc: nil, lib:, func:, headers:)  ⇒ Object 
  

  

  

  
    
      

```

303
304
305
306
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 303

def ensure_package_configuration(opt: nil, pc: nil, lib:, func:, headers:)
  have_package_configuration(opt: opt, pc: pc, lib: lib, func: func, headers: headers) ||
    abort_could_not_find_library(lib)
end

```

    
  

    
      
  
### 
  
    #**gnome_source**  ⇒ Object 
  

  

  

  
    
      

```

242
243
244
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 242

def gnome_source
  "https://download.gnome.org"
end

```

    
  

    
      
  
### 
  
    #**have_libxml_headers?**(version = nil)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

361
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
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 361

def have_libxml_headers?(version = nil)
  source = if version.nil?
    "      #include <libxml/xmlversion.h>\n    SRC\n  else\n    version_int = format(\"%d%2.2d%2.2d\", *version.split(\".\"))\n    <<~SRC\n      #include <libxml/xmlversion.h>\n      #if LIBXML_VERSION < \#{version_int}\n      #  error libxml2 is older than \#{version}\n      #endif\n    SRC\n  end\n\n  try_cpp(source)\nend\n"

```

    
  

    
      
  
### 
  
    #**have_package_configuration**(opt: nil, pc: nil, lib:, func:, headers:)  ⇒ Object 
  

  

  

  
    

set up mkmf to link against the library if we can find it

  

  

  
    
      

```

286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 286

def have_package_configuration(opt: nil, pc: nil, lib:, func:, headers:)
  if opt
    dir_config(opt)
    dir_config("opt")
  end

  # see if we have enough path info to do this without trying any harder
  unless ENV.key?("NOKOGIRI_TEST_PKG_CONFIG")
    return true if local_have_library(lib, func, headers)
  end

  try_package_configuration(pc) if pc

  # verify that we can compile and link against the library
  local_have_library(lib, func, headers)
end

```

    
  

    
      
  
### 
  
    #**iconv_configure_flags**  ⇒ Object 
  

  

  

  
    
      

```

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
416
417
418
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
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 400

def iconv_configure_flags
  # give --with-iconv-dir and --with-opt-dir first priority
  ["iconv", "opt"].each do |target|
    config = preserving_globals { dir_config(target) }
    next unless config.any? && try_link_iconv("--with-#{target}-* flags") { dir_config(target) }

    idirs, ldirs = config.map do |dirs|
      Array(dirs).flat_map do |dir|
        dir.split(File::PATH_SEPARATOR)
      end if dirs
    end

    return [
      "--with-iconv=yes",
      *("CPPFLAGS=#{idirs.map { |dir| "-I" + dir }.join(" ")}" if idirs),
      *("LDFLAGS=#{ldirs.map { |dir| "-L" + dir }.join(" ")}" if ldirs),
    ]
  end

  if try_link_iconv
    return ["--with-iconv=yes"]
  end

  config = preserving_globals { pkg_config("libiconv") }
  if config && try_link_iconv("pkg-config libiconv") { pkg_config("libiconv") }
    cflags, ldflags, libs = config

    return [
      "--with-iconv=yes",
      "CPPFLAGS=#{cflags}",
      "LDFLAGS=#{ldflags}",
      "LIBS=#{libs}",
    ]
  end

  abort_could_not_find_library("libiconv")
end

```

    
  

    
      
  
### 
  
    #**libflag_to_filename**(ldflag)  ⇒ Object 
  

  

  

  
    
      

```

354
355
356
357
358
359
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 354

def libflag_to_filename(ldflag)
  case ldflag
  when /\A-l(.+)/
    "lib#{Regexp.last_match(1)}.#{$LIBEXT}"
  end
end

```

    
  

    
      
  
### 
  
    #**local_have_library**(lib, func = nil, headers = nil)  ⇒ Object 
  

  

  

  
    
      

```

228
229
230
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 228

def local_have_library(lib, func = nil, headers = nil)
  have_library(lib, func, headers) || have_library("lib#{lib}", func, headers)
end

```

    
  

    
      
  
### 
  
    #**needs_darwin_linker_hack**  ⇒ Object 
  

  

  

  
    

In ruby 3.2, symbol resolution changed on Darwin, to introduce the `-bundle_loader` flag to resolve symbols against the ruby binary.

This makes it challenging to build a single extension that works with both a ruby with `--enable-shared` and one with ‘–disable-shared. To work around that, we choose to add `-flat_namespace` to the link line (later in this file).

The `-flat_namespace` line introduces its own behavior change, which is that (similar to on Linux), any symbols in the extension that are exported may now be resolved by shared libraries loaded by the Ruby process. Specifically, that means that libxml2 and libxslt, which are statically linked into the nokogiri bundle, will resolve (at runtime) to a system libxml2 loaded by Ruby on Darwin. And it appears that often Ruby on Darwin does indeed load the system libxml2, and that messes with our assumptions about whether we’re running with a patched libxml2 or a vanilla libxml2.

We choose to use `-load_hidden` in this case to prevent exporting those symbols from libxml2 and libxslt, which ensures that they will be resolved to the static libraries in the bundle. In other words, when we use `load_hidden`, what happens in the extension stays in the extension.

See github.com/rake-compiler/rake-compiler-dock/issues/87 for more info.

Anyway, this method is the logical bit to tell us when to turn on these workarounds.

  

  

  
    
      

```

619
620
621
622
623
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 619

def needs_darwin_linker_hack
  config_cross_build? &&
    darwin? &&
    Gem::Requirement.new(">= 3.2").satisfied_by?(Gem::Version.new(RbConfig::CONFIG["ruby_version"].split("+").first))
end

```

    
  

    
      
  
### 
  
    #**nix?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

216
217
218
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 216

def nix?
  ENV.key?("NIX_CC")
end

```

    
  

    
      
  
### 
  
    #**Nokogiri**(*args, &block)  ⇒ Object 
  

  

  

  
    

Parse a document contained in `args`.  Nokogiri will try to guess what type of document you are attempting to parse.  For more information, see Nokogiri.parse

To specify the type of document, use Nokogiri.XML, Nokogiri.HTML4, or Nokogiri.HTML5.

  

  

  
    
      

```

108
109
110
111
112
113
114
```

    
    
      

```
# File 'lib/nokogiri.rb', line 108

def Nokogiri(*args, &block)
  if block
    Nokogiri::HTML4::Builder.new(&block).doc.root
  else
    Nokogiri.parse(*args)
  end
end

```

    
  

    
      
  
### 
  
    #**openbsd?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

204
205
206
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 204

def openbsd?
  RbConfig::CONFIG["target_os"].include?("openbsd")
end

```

    
  

    
      
  
### 
  
    #**preserving_globals**  ⇒ Object 
  

  

  

  
    
      

```

312
313
314
315
316
317
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 312

def preserving_globals
  values = [$arg_config, $INCFLAGS, $CFLAGS, $CPPFLAGS, $LDFLAGS, $DLDFLAGS, $LIBPATH, $libs].map(&:dup)
  yield
ensure
  $arg_config, $INCFLAGS, $CFLAGS, $CPPFLAGS, $LDFLAGS, $DLDFLAGS, $LIBPATH, $libs = values
end

```

    
  

    
      
  
### 
  
    #**process_recipe**(name, version, static_p, cross_p, cacheable_p = true)  ⇒ Object 
  

  

  

  
    
      

```

438
439
440
441
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
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
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
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 438

def process_recipe(name, version, static_p, cross_p, cacheable_p = true)
  require "rubygems"
  gem("mini_portile2", REQUIRED_MINI_PORTILE_VERSION) # gemspec is not respected at install time
  require "mini_portile2"
  message("Using mini_portile version #{MiniPortile::VERSION}\n")

  unless ["libxml2", "libxslt"].include?(name)
    OTHER_LIBRARY_VERSIONS[name] = version
  end

  MiniPortile.new(name, version).tap do |recipe|
    def recipe.port_path
      "#{@target}/#{RUBY_PLATFORM}/#{@name}/#{@version}"
    end

    # We use 'host' to set compiler prefix for cross-compiling. Prefer host_alias over host. And
    # prefer i686 (what external dev tools use) to i386 (what ruby's configure.ac emits).
    recipe.host = RbConfig::CONFIG["host_alias"].empty? ? RbConfig::CONFIG["host"] : RbConfig::CONFIG["host_alias"]
    recipe.host = recipe.host.gsub("i386", "i686")

    recipe.target = File.join(PACKAGE_ROOT_DIR, "ports") if cacheable_p
    recipe.configure_options << "--libdir=#{File.join(recipe.path, "lib")}"

    yield recipe

    env = Hash.new do |hash, key|
      hash[key] = (ENV[key]).to_s
    end

    recipe.configure_options.flatten!

    recipe.configure_options.delete_if do |option|
      case option
      when /\A(\w+)=(.*)\z/
        env[Regexp.last_match(1)] = if env.key?(Regexp.last_match(1))
          concat_flags(env[Regexp.last_match(1)], Regexp.last_match(2))
        else
          Regexp.last_match(2)
        end
        true
      else
        false
      end
    end

    if static_p
      recipe.configure_options += [
        "--disable-shared",
        "--enable-static",
      ]
      env["CFLAGS"] = concat_flags(env["CFLAGS"], "-fPIC")
    else
      recipe.configure_options += [
        "--enable-shared",
        "--disable-static",
      ]
    end

    if cross_p
      recipe.configure_options += [
        "--target=#{recipe.host}",
        "--host=#{recipe.host}",
      ]
    end

    if RbConfig::CONFIG["target_cpu"] == "universal"
      ["CFLAGS", "LDFLAGS"].each do |key|
        unless env[key].include?("-arch")
          env[key] = concat_flags(env[key], RbConfig::CONFIG["ARCH_FLAG"])
        end
      end
    end

    recipe.configure_options += env.map do |key, value|
      "#{key}=#{value.strip}"
    end

    checkpoint = "#{recipe.target}/#{recipe.name}-#{recipe.version}-#{RUBY_PLATFORM}.installed"
    if File.exist?(checkpoint) && !recipe.source_directory
      message("Building Nokogiri with a packaged version of #{name}-#{version}.\n")
    else
      message("        ---------- IMPORTANT NOTICE ----------\n        Building Nokogiri with a packaged version of \#{name}-\#{version}.\n        Configuration options: \#{recipe.configure_options.shelljoin}\n      EOM\n\n      unless recipe.patch_files.empty?\n        message(\"The following patches are being applied:\\n\")\n\n        recipe.patch_files.each do |patch|\n          message(format(\"  - %s\\n\", File.basename(patch)))\n        end\n      end\n\n      message(<<~EOM) if name != \"libgumbo\"\n\n        The Nokogiri maintainers intend to provide timely security updates, but if\n        this is a concern for you and want to use your OS/distro system library\n        instead, then abort this installation process and install nokogiri as\n        instructed at:\n\n          https://nokogiri.org/tutorials/installing_nokogiri.html#installing-using-standard-system-libraries\n\n      EOM\n\n      message(<<~EOM) if name == \"libxml2\"\n        Note, however, that nokogiri cannot guarantee compatibility with every\n        version of libxml2 that may be provided by OS/package vendors.\n\n      EOM\n\n      chdir_for_build { recipe.cook }\n      FileUtils.touch(checkpoint)\n    end\n    recipe.activate\n  end\nend\n")

```

    
  

    
      
  
### 
  
    #**sh_export_path**(path)  ⇒ Object 
  

  

  

  
    
      

```

332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 332

def sh_export_path(path)
  # because libxslt 1.1.29 configure.in uses AC_PATH_TOOL which treats ":"
  # as a $PATH separator, we need to convert windows paths from
  #
  #   C:/path/to/foo
  #
  # to
  #
  #   /C/path/to/foo
  #
  # which is sh-compatible, in order to find things properly during
  # configuration
  return path unless windows?

  match = Regexp.new("^([A-Z]):(/.*)").match(path)
  if match && match.length == 3
    return File.join("/", match[1], match[2])
  end

  path
end

```

    
  

    
      
  
### 
  
    #**solaris?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

196
197
198
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 196

def solaris?
  RbConfig::CONFIG["target_os"].include?("solaris")
end

```

    
  

    
      
  
### 
  
    #**truffle?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

220
221
222
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 220

def truffle?
  RUBY_ENGINE == "truffleruby"
end

```

    
  

    
      
  
### 
  
    #**try_link_iconv**(using = nil)  ⇒ Object 
  

  

  

  
    
      

```

379
380
381
382
383
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
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 379

def try_link_iconv(using = nil)
  checking_for(using ? "iconv using #{using}" : "iconv") do
    ["", "-liconv"].any? do |opt|
      preserving_globals do
        yield if block_given?

        try_link("          #include <stdlib.h>\n          #include <iconv.h>\n          int main(void)\n          {\n              iconv_t cd = iconv_open(\"\", \"\");\n              iconv(cd, NULL, NULL, NULL, NULL);\n              return EXIT_SUCCESS;\n          }\n        SRC\n      end\n    end\n  end\nend\n", opt)

```

    
  

    
      
  
### 
  
    #**try_package_configuration**(pc)  ⇒ Object 
  

  

  

  
    

wrapper around MakeMakefil#pkg_config and the PKGConfig gem

  

  

  
    
      

```

252
253
254
255
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
274
275
276
277
278
279
280
281
282
283
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 252

def try_package_configuration(pc)
  unless ENV.key?("NOKOGIRI_TEST_PKG_CONFIG_GEM")
    # try MakeMakefile#pkg_config, which uses the system utility `pkg-config`.
    return if checking_for("#{pc} using `pkg_config`", LOCAL_PACKAGE_RESPONSE) do
      pkg_config(pc)
    end
  end

  # `pkg-config` probably isn't installed, which appears to be the case for lots of freebsd systems.
  # let's fall back to the pkg-config gem, which knows how to parse .pc files, and wrap it with the
  # same logic as MakeMakefile#pkg_config
  begin
    require "rubygems"
    gem("pkg-config", REQUIRED_PKG_CONFIG_VERSION)
    require "pkg-config"

    checking_for("#{pc} using pkg-config gem version #{PKGConfig::VERSION}", LOCAL_PACKAGE_RESPONSE) do
      if PKGConfig.have_package(pc)
        cflags  = PKGConfig.cflags(pc)
        ldflags = PKGConfig.libs_only_L(pc)
        libs    = PKGConfig.libs_only_l(pc)

        Logging.message("pkg-config gem found package configuration for %s\n", pc)
        Logging.message("cflags: %s\nldflags: %s\nlibs: %s\n\n", cflags, ldflags, libs)

        [cflags, ldflags, libs]
      end
    end
  rescue LoadError
    message("Please install either the `pkg-config` utility or the `pkg-config` rubygem.\n")
  end
end

```

    
  

    
      
  
### 
  
    #**unix?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

212
213
214
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 212

def unix?
  !(windows? || solaris? || darwin?)
end

```

    
  

    
      
  
### 
  
    #**windows?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

192
193
194
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 192

def windows?
  RbConfig::CONFIG["target_os"].match?(/mingw|mswin/)
end

```

    
  

    
      
  
### 
  
    #**zlib_source**(version_string)  ⇒ Object 
  

  

  

  
    
      

```

232
233
234
235
236
237
238
239
240
```

    
    
      

```
# File 'ext/nokogiri/extconf.rb', line 232

def zlib_source(version_string)
  # As of 2022-12, I'm starting to see failed downloads often enough from zlib.net that I want to
  # change the default to github.
  if ENV["NOKOGIRI_USE_CANONICAL_ZLIB_SOURCE"]
    "https://zlib.net/fossils/zlib-#{version_string}.tar.gz"
  else
    "https://github.com/madler/zlib/releases/download/v#{version_string}/zlib-#{version_string}.tar.gz"
  end
end

```