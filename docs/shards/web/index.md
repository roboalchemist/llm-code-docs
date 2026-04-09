shards 0.1.1 - Docs.rs

                    Docs.rs
                

    
-

                shards-0.1.1
            
        
    

                
                

                    
-
                        docs.rs

- About docs.rs
- Badges
- Builds
- Metadata
- Shorthand URLs
- Download
- Rustdoc JSON
- Build queue
- Privacy policy

-
                        Rust
                        

                            
  - Rust website

  - The Book

  - Standard Library API Reference

  - Rust by Example

  - The Cargo Guide

  - Clippy Documentation

#

                    shards 0.1.1
                    
                

                
                rust bindings and utility in order to use shards

                
                    

                        
                        
-

                                 Crate
                            
                        

                        
                        
-

                                 Source
                            
                        

                        
                        
-

                                 Builds
                            
                        

                        
                        
-

                                Feature flags
                            
                        
                    

                
            
    

        
            
                
                    

- Size

-
                                Source code size: 265.69 kB
                                    This is the summed size of all the files inside the crates.io package for this release.
                                    
                                
                            
- Ø build duration
-
                                    all releases: 36s
                                        Average build duration of **successful** builds in releases after 2024-10-23.
                                        
                                    
                                
- Links

-

                                 crates.io

- Dependencies

-

-
                approx ^0.5.1
                
                    *normal*
                    
                
            
        
-
                compile-time-crc32 ^0.1.2
                
                    *normal*
                    
                
            
        
-
                futures ^0.3
                
                    *normal*
                    
                
            
        
-
                futures-util ^0.3
                
                    *normal*
                    
                
            
        
-
                git-version ^0.3.9
                
                    *normal*
                    
                
            
        
-
                half ^2.2.1
                
                    *normal*
                    
                
            
        
-
                lazy_static ^1.5.0
                
                    *normal*
                    
                
            
        
-
                serde ^1.0
                
                    *normal*
                    
                
            
        
-
                shards-macro ^0.1.0
                
                    *normal*
                    
                
            
        
-
                ctor ^0.2.8
                
                    *dev*
                    
                
            
        
-
                bindgen ^0.69
                
                    *build*
                    
                
            
        
-
                dlopen ^0.1.8
                
                    *normal*
                    
                        *optional*
                    
                
            
        
                                

                            
                        

                        
- Versions

-

-
            **0.1.1** (2025-02-20)
        
        
         
        
-
            **0.1.0** (2022-06-13)
        
                                

                            
                        

                        
                        
- Owners

-

                        docs.rs failed to build shards-0.1.1

                        Please check the
                        build logs for more information.
                        

                        See Builds for ideas on how to fix a failed build,
                        or Metadata for how to configure docs.rs builds.
                        

                        If you believe this is docs.rs' fault, open an issue.
                    
                        Visit the last successful build:
                        
                            shards-0.1.0
                        
                    
# Shards in rust

## Implementing a new shard

To create a new shards and register it to the system, do the following.

### Create a struct

The struct should contain any field necessary for the shard, especially parameters. They don't need to be `pub`.

```
struct MyShard {
  my_param: ParamVar,
  my_shards: ShardsVar,
  my_bool: bool,
}

```

### Implement the Default trait

All declared fields should be given a default value. Avoid using `..Default::default()` and initialize all fields.

```
impl Default for MyShard {
  fn default() -> Self {
    Self {
      my_param: ParamVar::default(),
      my_shards: ShardsVar::default(),
      my_bool: false,
    }
  }
}

```

Note that `ParamVar::default()` is equivalent to setting `nil` in the textual language. That parameter will have the `None` type by default. To specify a different default value (for instance an integer), use the `Paramvar::new()` constructor:

```
impl Default for MyShard {
  fn default() -> Self {
    Self {
      my_param: ParamVar::new(42.into()),
      my_shards: ShardsVar::default(),
      my_bool: false,
    }
  }
}

```

### Implement the Shard trait (required)

The trait is defined in `rust/src/shard.rs`. Some functions have a default implementation. At minimum the following must be implemented:

```
impl LegacyShard for MyShard {
  fn registerName() -> &'static str
  where
    Self: Sized,
  {
    todo!()
  }

  fn hash() -> u32
  where
    Self: Sized,
  {
    todo!()
  }

  fn name(&mut self) -> &str {
    todo!()
  }

  fn inputTypes(&mut self) -> &Types {
    todo!()
  }

  fn outputTypes(&mut self) -> &Types {
    todo!()
  }

  fn activate(&mut self, context: &Context, input: &Var) -> Result<Var, &str> {
    todo!()
  }
}

```

#### Implement `registerName()`, `hash()`, `name()`

These functions are used to identify the shard by name.

```
  fn registerName() -> &'static str
  where
    Self: Sized,
  {
    cstr!("MyShard")
  }

  fn hash() -> u32
  where
    Self: Sized,
  {
    compile_time_crc32::crc32!("MyShard-rust-0x20200101")
  }

  fn name(&mut self) -> &str {
    "MyShard"
  }

```

*Note: `registerName()` and `name()` are very similar. The `&str` returned by `registerName()` is used on the C++ side and thus is requires to be null-terminated, which is made possible with the `cstr!` macro.*

#### Implement `inputTypes()`, `outputTypes()`

These functions define the accepted input types and the expected output types of the shard. It can be any type including `None` and `Any`.

```
  fn inputTypes(&mut self) -> &Types {
    &ANY_TYPES
  }

  fn outputTypes(&mut self) -> &Types {
    &ANY_TYPES
  }

```

*Note: a shard that doesn't use its input could be accepting and producing `None`. However, it limits the usability of that shard, and we usually prefer to have the input "pass through", in which case we accept `Any` type and return the same.*

#### Implement `activate()`

This function is called every tick of the wire owning an instance of this shard. This is where the main logic should be implemented.

It receives the `input` of the shard and should return an output (it can be `Var::default()`, which is the equivalent of `None`).

```
  fn activate(&mut self, context: &Context, input: &Var) -> Result<Var, &str> {
    if !self.my_shards.is_empty() {
      let mut output = Var::default();
      let wire_state = self.my_shards.activate(context, self.my_param.get(), &mut output);
      if wire_state == WireState::Error {
        return Err("Failed to activate contents");
      }
    }

    // input passthrough
    Ok(*input)
  }

```

### Implement the Shard trait (parameters)

If the shards has parameters, additional functions should be implemented.

```

impl LegacyShard for MyShard {
  fn parameters(&mut self) -> Option<&Parameters> {
    None
  }

  fn setParam(&mut self, _index: i32, _value: &Var) -> Result<(), &str> {
    Ok(())
  }

  fn getParam(&mut self, _index: i32) -> Var {
    Var::default()
  }

  fn warmup(&mut self, _context: &Context) -> Result<(), &str> {
    Ok(())
  }

  fn cleanup(&mut self) -> Result<(), &str> {
    Ok(())
  }
}

```

#### Implement `parameters()`

If the shard has parameters, this function should return of description of them. Usually this is done in two steps:

- Define a static variable to hold the description.

- Return an immutable ref of that variable in the `parameters()` function.

```
lazy_static! {
  static ref MY_PARAMETERS: Parameters = vec![
    (
      cstr!("MyParam"),
      cstr!("The integer parameter"),
      INT_TYPES_SLICE,
    )
      .into(),
    (
      cstr!("Shards"),
      cstr!("The inner shards"),
      &SHARDS_OR_NONE_TYPES[..],
    )
      .into(),
    (
      cstr!("MyBool"),
      cstr!("Some boolean value"),
      BOOL_TYPES_SLICE,
    )
      .into(),
  ];
}

impl LegacyShard for MyShard {
  fn parameters(&mut self) -> Option<&Parameters> {
    Some(&MY_PARAMETERS)
  }
}

```

#### Implement `setParam()`, `getParam()`

Since the shard has parameters, we need to implement their getters and setters. The parameter index matches the order of definition in the `Parameters` struct returned by `parameters()`.

```
  fn setParam(&mut self, index: i32, value: &Var) -> Result<(), &str> {
    match index {
      0 => self.my_param.set_param(value),
      1 => self.my_shards.set_param(value),
      2 => Ok(self.my_bool = value.try_into()?),
      _ => Err("Invalid parameter index"),
    }
  }

  fn getParam(&mut self, index: i32) -> Var {
    match index {
      0 => self.my_param.get_param(),
      1 => self.my_shards.get_param(),
      2 => self.my_bool.into(),
      _ => Var::default(),
    }
  }

```

#### Implement `warmup()`, `cleanup()`

Some parameters are saved as `ParamVar` or `ShardsVar`. Those types need special care to manage the underlying memory.

```
  fn warmup(&mut self, ctx: &Context) -> Result<(), &str> {
    self.my_param.warmup(ctx);
    if !self.my_shards.is_empty() {
      self.my_shards.warmup(ctx)?;
    }

    Ok(())
  }

  fn cleanup(&mut self) -> Result<(), &str> {
    if !self.my_shards.is_empty() {
      self.my_shards.cleanup();
    }
    self.my_param.cleanup();

    Ok(())
  }

```

*Note: by convention `cleanup()` uses the reverse order of `warmup()`. This prevents some potential issues with dependent resources, though it might occur only in rare cases.*

### Implement the Shard trait (other)

Finally, if the shard has other shards as parameters, has additional type checks, or if it should expose variables; then other functions might need to be implemented.

#### Implement `hasCompose()`, `compose()`

```
  fn hasCompose() -> bool {
    true
  }

  fn compose(&mut self, data: &InstanceData) -> Result<Type, &str> {
    if !self.my_shards.is_empty() {
      self.my_shards.compose(&data)?;
    }

    // passthrough the input
    Ok(data.inputType)
  }

```

*Note: to save processing, the `compose()` function is only called if the `hasCompose()` function returns `true`. Therefore, each time `compose()` needs to be implemented, so does `hasCompose()`.*

#### Implement `exposedVariables()`

Implement this function when a shard can receive a variable as parameter that doesn't exist (i.e. is not declared elsewhere). In this case, the shard will expose that variable for other shards to use.

```
  fn exposedVariables(&mut self) -> Option<&ExposedTypes> {
    if self.my_param.is_variable() && self.should_expose {
      self.exposing.clear();

      let exp_info = ExposedInfo {
        exposedType: common_type::int,
        name: self.my_param.get_name(),
        help: shccstr!("The exposed variable"),
        declared: true,
        ..ExposedInfo::default()
      };

      self.exposing.push(exp_info);
      Some(&self.exposing)
    } else {
      None
    }
  }

```

The `exposed` vector needs to be owned by the shard. Hence, it must be defined as a field and properly initialized in the `Default` impl.

```
struct MyShard {
  exposed: ExposedTypes,
  should_expose: bool,
}

impl Default for MyShard {
  fn default() -> Self {
    Self {
      exposed: Vec::new(),
      should_expose: false,
    }
  }
}

```

In addition, the variable should only be exposed if it doesn't exist yet. We can check whether that's the case during compose:

```
  fn compose(&mut self, data: &InstanceData) -> Result<Type, &str> {
    if self.my_param.is_variable() {
      self.should_expose = true; // assume we expose a new variable

      let shared: ExposedTypes = data.shared.into();
      for var in shared {
        let (a, b) = unsafe {
          (
            CStr::from_ptr(var.name),
            CStr::from_ptr(self.my_param.get_name()),
          )
        };
        if CStr::cmp(a, b) == Ordering::Equal {
          self.should_expose = false;
          let t = common_type::int;
          if var.exposedType.basicType != t.basicType {
            return Err("MyShard: incorrect type of variable.");
          }
          break;
        }
      }
    }

    // passthrough the input
    Ok(data.inputType)
  }

```

#### Implement `requiredVariables()`

In a similar but opposite way to `exposedVariables()`, a shard might require that a variable exists.

```
  fn requiredVariables(&mut self) -> Option<&ExposedTypes> {
    self.requiring.clear();
    let exp_info = ExposedInfo {
      exposedType: common_type::int,
      name: self.my_param.get_name(),
      help: shccstr!("The integer parameter"),
      ..ExposedInfo::default()
    };
    self.requiring.push(exp_info);
    Some(&self.requiring)
  }

```

The `requiring` vector needs to be owned by the shard. Hence, it must be defined as a field and properly initialized in the `Default` impl.

```
struct MyShard {
  requiring: ExposedTypes,
}

impl Default for MyShard {
  fn default() -> Self {
    Self {
      requiring: Vec::new(),
    }
  }
}

```

*Note: exposing and requiring the same variable is illogical and likely a bug that needs to be fixed.*

### Register the shard

Once a shard is ready, it must be registered. Usually it is done in a `registerShards()` function defined in a `mod.rs` file:

```
pub fn registerShards() {
  register_legacy_shard::<MyShard>();
}

```

That function itself is eventually called from, `registerRustShards()` defined in `rust/src/lib.rs` (either directly or through other functions).
