cargo::core::compiler

# Struct BuildContext

Source

```
pub struct BuildContext<'a, 'gctx> {}
```

## Fields§

§`ws: &'a Workspace<'gctx>`

The workspace the build is for.
§`gctx: &'gctx GlobalContext`

The cargo context.
§`logger: Option<&'a BuildLogger>`

Build logger for `-Zbuild-analysis`.
§`profiles: Profiles`

This contains a collection of compiler flags presets.
§`build_config: &'a BuildConfig`

Configuration information for a rustc build.
§`extra_compiler_args: HashMap<Unit, Vec<String>>`

Extra compiler args for either `rustc` or `rustdoc`.
§`packages: PackageSet<'gctx>`

Package downloader.

This holds ownership of the `Package` objects.
§`target_data: RustcTargetData<'gctx>`

Information about rustc and the target platform.
§`roots: Vec<Unit>`

The root units of `unit_graph` (units requested on the command-line).
§`unit_graph: UnitGraph`

The dependency graph of units to compile.
§`unit_to_index: HashMap<Unit, UnitIndex>`

A map from unit to index.
§`scrape_units: Vec<Unit>`

Reverse-dependencies of documented units, used by the `rustdoc --scrape-examples` flag.
§`all_kinds: HashSet<CompileKind>`

The list of all kinds that are involved in this build

## Implementations§
