cargo::core::compiler

# Struct BuildRunner

Source

```
pub struct BuildRunner<'a, 'gctx> {}
```

## Fields§

§`bcx: &'a BuildContext<'a, 'gctx>`

Mostly static information about the build task.
§`compilation: Compilation<'gctx>`

A large collection of information about the result of the entire compilation.
§`build_script_outputs: Arc<Mutex<BuildScriptOutputs>>`

Output from build scripts, updated after each build script runs.
§`build_explicit_deps: HashMap<Unit, BuildDeps>`

Dependencies (like rerun-if-changed) declared by a build script.
This is *only* populated from the output from previous runs.
If the build script hasn’t ever been run, then it must be run.
§`fingerprints: HashMap<Unit, Arc<Fingerprint>>`

Fingerprints used to detect if a unit is out-of-date.
§`mtime_cache: HashMap<PathBuf, FileTime>`

Cache of file mtimes to reduce filesystem hits.
§`checksum_cache: HashMap<PathBuf, Checksum>`

Cache of file checksums to reduce filesystem reads.
§`compiled: HashSet<Unit>`

A set used to track which units have been compiled.
A unit may appear in the job graph multiple times as a dependency of
multiple packages, but it only needs to run once.
§`build_scripts: HashMap<Unit, Arc<BuildScripts>>`

Linking information for each `Unit`.
See `build_map` for details.
§`jobserver: Client`

Job server client to manage concurrency with other processes.
§`lto: HashMap<Unit, Lto>`

Map of the LTO-status of each unit. This indicates what sort of
compilation is happening (only object, only bitcode, both, etc), and is
precalculated early on.
§`metadata_for_doc_units: HashMap<Unit, Metadata>`

Map of Doc/Docscrape units to metadata for their -Cmetadata flag.
See `Context::find_metadata_units` for more details.
§`failed_scrape_units: Arc<Mutex<HashSet<UnitHash>>>`

Set of metadata of Docscrape units that fail before completion, e.g.
because the target has a type error. This is in an Arc<Mutex<..>>
because it is continuously updated as the job progresses.
§`lock_manager: Arc<LockManager>`

Manages locks for build units when fine grain locking is enabled.

## Implementations§
