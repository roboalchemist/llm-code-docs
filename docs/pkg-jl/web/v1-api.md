# Source: https://pkgdocs.julialang.org/v1/api/

Title: 13. API Reference · Pkg.jl

URL Source: https://pkgdocs.julialang.org/v1/api/

Markdown Content:
This section describes the functional API for interacting with Pkg.jl. It is recommended to use the functional API, rather than the Pkg REPL mode, for non-interactive usage, for example in scripts.

[General API Reference](https://pkgdocs.julialang.org/v1/api/#General-API-Reference)[](https://pkgdocs.julialang.org/v1/api/)[](https://pkgdocs.julialang.org/v1/api/#General-API-Reference "Permalink")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Certain options are generally useful and can be specified in any API call. You can specify these options by setting keyword arguments.

### [Redirecting output](https://pkgdocs.julialang.org/v1/api/#Redirecting-output)[](https://pkgdocs.julialang.org/v1/api/)[](https://pkgdocs.julialang.org/v1/api/#Redirecting-output "Permalink")

Use the `io::IOBuffer` keyword argument to redirect Pkg output. For example, `Pkg.add("Example"; io=devnull)` will discard any output produced by the `add` call.

[Package API Reference](https://pkgdocs.julialang.org/v1/api/#Package-API-Reference)[](https://pkgdocs.julialang.org/v1/api/)[](https://pkgdocs.julialang.org/v1/api/#Package-API-Reference "Permalink")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the Pkg REPL mode, packages (with associated version, UUID, URL etc) are parsed from strings, for example `"Package#master"`,`"Package@v0.1"`, `"www.mypkg.com/MyPkg#my/feature"`.

In the functional API, it is possible to use strings as arguments for simple commands (like `Pkg.add(["PackageA", "PackageB"])`, but more complicated commands, which e.g. specify URLs or version range, require the use of a more structured format over strings. This is done by creating an instance of [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec) which is passed in to functions.

[`Pkg.add`](https://pkgdocs.julialang.org/v1/api/#Pkg.add) — Function

```
Pkg.add(pkg::Union{String, Vector{String}}; preserve=PRESERVE_TIERED, target::Symbol=:deps)
Pkg.add(pkg::Union{PackageSpec, Vector{PackageSpec}}; preserve=PRESERVE_TIERED, target::Symbol=:deps)
```

Add a package to the current project. This package will be available by using the `import` and `using` keywords in the Julia REPL, and if the current project is a package, also inside that package.

If the active environment is a package (the Project has both `name` and `uuid` fields) compat entries will be added automatically with a lower bound of the added version.

To add as a weak dependency (in the `[weakdeps]` field) set the kwarg `target=:weakdeps`. To add as an extra dep (in the `[extras]` field) set `target=:extras`.

**Resolution Tiers**

`Pkg` resolves the set of packages in your environment using a tiered algorithm. The `preserve` keyword argument allows you to key into a specific tier in the resolve algorithm. The following table describes the argument values for `preserve` (in order of strictness):

| Value | Description |
| --- | --- |
| `PRESERVE_ALL_INSTALLED` | Like `PRESERVE_ALL` and only add those already installed |
| `PRESERVE_ALL` | Preserve the state of all existing dependencies (including recursive dependencies) |
| `PRESERVE_DIRECT` | Preserve the state of all existing direct dependencies |
| `PRESERVE_SEMVER` | Preserve semver-compatible versions of direct dependencies |
| `PRESERVE_NONE` | Do not attempt to preserve any version information |
| `PRESERVE_TIERED_INSTALLED` | Like `PRESERVE_TIERED` except `PRESERVE_ALL_INSTALLED` is tried first |
| `PRESERVE_TIERED` | Use the tier that will preserve the most version information while |
|  | allowing version resolution to succeed (this is the default) |

To change the default strategy to `PRESERVE_TIERED_INSTALLED` set the env var `JULIA_PKG_PRESERVE_TIERED_INSTALLED` to true.

After the installation of new packages the project will be precompiled. For more information see `pkg> ?precompile`.

With the `PRESERVE_ALL_INSTALLED` strategy the newly added packages will likely already be precompiled, but if not this may be because either the combination of package versions resolved in this environment has not been resolved and precompiled before, or the precompile cache has been deleted by the LRU cache storage (see `JULIA_MAX_NUM_PRECOMPILE_FILES`).

The `PRESERVE_TIERED_INSTALLED` and `PRESERVE_ALL_INSTALLED` strategies requires at least Julia 1.9.

The `target` kwarg requires at least Julia 1.11.

**Examples**

```
Pkg.add("Example") # Add a package from registry
Pkg.add("Example", target=:weakdeps) # Add a package as a weak dependency
Pkg.add("Example", target=:extras) # Add a package to the `[extras]` list
Pkg.add("Example"; preserve=Pkg.PRESERVE_ALL) # Add the `Example` package and strictly preserve existing dependencies
Pkg.add(name="Example", version="0.3") # Specify version; latest release in the 0.3 series
Pkg.add(name="Example", version="0.3.1") # Specify version; exact release
Pkg.add(url="https://github.com/JuliaLang/Example.jl", rev="master") # From url to remote gitrepo
Pkg.add(url="/remote/mycompany/juliapackages/OurPackage") # From path to local gitrepo
Pkg.add(url="https://github.com/Company/MonoRepo", subdir="juliapkgs/Package.jl)") # With subdir
```

After the installation of new packages the project will be precompiled. See more at [Environment Precompilation](https://pkgdocs.julialang.org/v1/environments/#Environment-Precompilation).

See also [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec), [`Pkg.develop`](https://pkgdocs.julialang.org/v1/api/#Pkg.develop).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L123-L186)[`Pkg.develop`](https://pkgdocs.julialang.org/v1/api/#Pkg.develop) — Function

```
Pkg.develop(pkg::Union{String, Vector{String}}; io::IO=stderr, preserve=PRESERVE_TIERED, installed=false)
Pkg.develop(pkgs::Union{PackageSpec, Vector{PackageSpec}}; io::IO=stderr, preserve=PRESERVE_TIERED, installed=false)
```

Make a package available for development by tracking it by path. If `pkg` is given with only a name or by a URL, the package will be downloaded to the location specified by the environment variable `JULIA_PKG_DEVDIR`, with `joinpath(DEPOT_PATH[1],"dev")` being the default.

If `pkg` is given as a local path, the package at that path will be tracked.

The preserve strategies offered by `Pkg.add` are also available via the `preserve` kwarg. See [`Pkg.add`](https://pkgdocs.julialang.org/v1/api/#Pkg.add) for more information.

**Examples**

```
# By name
Pkg.develop("Example")

# By url
Pkg.develop(url="https://github.com/JuliaLang/Compat.jl")

# By path
Pkg.develop(path="MyJuliaPackages/Package.jl")
```

See also [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec), [`Pkg.add`](https://pkgdocs.julialang.org/v1/api/#Pkg.add).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L418-L446)[`Pkg.activate`](https://pkgdocs.julialang.org/v1/api/#Pkg.activate) — Function

```
Pkg.activate([s::String]; shared::Bool=false, io::IO=stderr)
Pkg.activate(; temp::Bool=false, shared::Bool=false, io::IO=stderr)
```

Activate the environment at `s`. The active environment is the environment that is modified by executing package commands. The logic for what path is activated is as follows:

*   If `shared` is `true`, the first existing environment named `s` from the depots in the depot stack will be activated. If no such environment exists, create and activate that environment in the first depot.
*   If `temp` is `true` this will create and activate a temporary environment which will be deleted when the julia process is exited.
*   If `s` is an existing path, then activate the environment at that path.
*   If `s` is a package in the current project and `s` is tracking a path, then activate the environment at the tracked path.
*   Otherwise, `s` is interpreted as a non-existing path, which is then activated.

If no argument is given to `activate`, then use the first project found in `LOAD_PATH` (ignoring `"@"`). For the default value of `LOAD_PATH`, the result is to activate the `@v#.#` environment.

**Examples**

```
Pkg.activate()
Pkg.activate("local/path")
Pkg.activate("MyDependency")
Pkg.activate(; temp=true)
```

See also [`LOAD_PATH`](https://docs.julialang.org/en/v1/base/constants/#Base.LOAD_PATH).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L600-L631)[`Pkg.rm`](https://pkgdocs.julialang.org/v1/api/#Pkg.rm) — Function

```
Pkg.rm(pkg::Union{String, Vector{String}}; mode::PackageMode = PKGMODE_PROJECT)
Pkg.rm(pkg::Union{PackageSpec, Vector{PackageSpec}}; mode::PackageMode = PKGMODE_PROJECT)
```

Remove a package from the current project. If `mode` is equal to `PKGMODE_MANIFEST` also remove it from the manifest including all recursive dependencies of `pkg`.

See also [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec), [`PackageMode`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageMode).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L224-L233)[`Pkg.update`](https://pkgdocs.julialang.org/v1/api/#Pkg.update) — Function

```
Pkg.update(; level::UpgradeLevel=UPLEVEL_MAJOR, mode::PackageMode = PKGMODE_PROJECT, preserve::PreserveLevel)
Pkg.update(pkg::Union{String, Vector{String}})
Pkg.update(pkg::Union{PackageSpec, Vector{PackageSpec}})
```

If no positional argument is given, update all packages in the manifest if `mode` is `PKGMODE_MANIFEST` and packages in both manifest and project if `mode` is `PKGMODE_PROJECT`. If no positional argument is given, `level` can be used to control by how much packages are allowed to be upgraded (major, minor, patch, fixed).

If packages are given as positional arguments, the `preserve` argument can be used to control what other packages are allowed to update:

*   `PRESERVE_ALL` (default): Only allow `pkg` to update.
*   `PRESERVE_DIRECT`: Only allow `pkg` and indirect dependencies that are not a direct dependency in the project to update.
*   `PRESERVE_NONE`: Allow `pkg` and all its indirect dependencies to update.

After any package updates the project will be precompiled. See more at [Environment Precompilation](https://pkgdocs.julialang.org/v1/environments/#Environment-Precompilation).

See also [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec), [`PackageMode`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageMode), [`UpgradeLevel`](https://pkgdocs.julialang.org/v1/api/#Pkg.UpgradeLevel).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L250-L266)[`Pkg.test`](https://pkgdocs.julialang.org/v1/api/#Pkg.test) — Function

```
Pkg.test(; kwargs...)
Pkg.test(pkg::Union{String, Vector{String}; kwargs...)
Pkg.test(pkgs::Union{PackageSpec, Vector{PackageSpec}}; kwargs...)
```

**Keyword arguments:**

*   `coverage::Union{Bool,String}=false`: enable or disable generation of coverage statistics for the tested package. If a string is passed it is passed directly to `--code-coverage` in the test process so e.g. "user" will test all user code.
*   `allow_reresolve::Bool=true`: allow Pkg to reresolve the package versions in the test environment
*   `julia_args::Union{Cmd, Vector{String}}`: options to be passed the test process.
*   `test_args::Union{Cmd, Vector{String}}`: test arguments (`ARGS`) available in the test process.

`allow_reresolve` requires at least Julia 1.9.

Passing a string to `coverage` requires at least Julia 1.9.

Run the tests for package `pkg`, or for the current project (which thus needs to be a package) if no positional argument is given to `Pkg.test`. A package is tested by running its `test/runtests.jl` file.

The tests are run by generating a temporary environment with only the `pkg` package and its (recursive) dependencies in it. If a manifest file exists and the `allow_reresolve` keyword argument is set to `false`, the versions in the manifest file are used. Otherwise a feasible set of packages is resolved and installed.

During the tests, test-specific dependencies are active, which are given in the project file as e.g.

```
[extras]
Test = "8dfed614-e22c-5e08-85e1-65c5234f0b40"

[targets]
test = ["Test"]
```

The tests are executed in a new process with `check-bounds=yes` and by default `startup-file=no`. If using the startup file (`~/.julia/config/startup.jl`) is desired, start julia with `--startup-file=yes`. Inlining of functions during testing can be disabled (for better coverage accuracy) by starting julia with `--inline=no`. The tests can be run as if different command line arguments were passed to julia by passing the arguments instead to the `julia_args` keyword argument, e.g.

`Pkg.test("foo"; julia_args=["--inline"])`
To pass some command line arguments to be used in the tests themselves, pass the arguments to the `test_args` keyword argument. These could be used to control the code being tested, or to control the tests in some way. For example, the tests could have optional additional tests:

```
if "--extended" in ARGS
    @test some_function()
end
```

which could be enabled by testing with

`Pkg.test("foo"; test_args=["--extended"])`

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L269-L329)[`Pkg.build`](https://pkgdocs.julialang.org/v1/api/#Pkg.build) — Function

```
Pkg.build(; verbose = false, io::IO=stderr)
Pkg.build(pkg::Union{String, Vector{String}}; verbose = false, io::IO=stderr)
Pkg.build(pkgs::Union{PackageSpec, Vector{PackageSpec}}; verbose = false, io::IO=stderr)
```

Run the build script in `deps/build.jl` for `pkg` and all of its dependencies in depth-first recursive order. If no argument is given to `build`, the current project is built, which thus needs to be a package. This function is called automatically on any package that gets installed for the first time. `verbose = true` prints the build output to `stdout`/`stderr` instead of redirecting to the `build.log` file.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L348-L361)[`Pkg.pin`](https://pkgdocs.julialang.org/v1/api/#Pkg.pin) — Function

```
Pkg.pin(pkg::Union{String, Vector{String}}; io::IO=stderr, all_pkgs::Bool=false)
Pkg.pin(pkgs::Union{PackageSpec, Vector{PackageSpec}}; io::IO=stderr, all_pkgs::Bool=false)
```

Pin a package to the current version (or the one given in the `PackageSpec`) or to a certain git revision. A pinned package is never automatically updated: if `pkg` is tracking a path, or a repository, those remain tracked but will not update. To get updates from the origin path or remote repository the package must first be freed.

The `all_pkgs` kwarg was introduced in julia 1.7.

**Examples**

```
# Pin a package to its current version
Pkg.pin("Example")

# Pin a package to a specific version
Pkg.pin(name="Example", version="0.3.1")

# Pin all packages in the project
Pkg.pin(all_pkgs = true)
```

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L364-L387)[`Pkg.free`](https://pkgdocs.julialang.org/v1/api/#Pkg.free) — Function

```
Pkg.free(pkg::Union{String, Vector{String}}; io::IO=stderr, all_pkgs::Bool=false)
Pkg.free(pkgs::Union{PackageSpec, Vector{PackageSpec}}; io::IO=stderr, all_pkgs::Bool=false)
```

If `pkg` is pinned, remove the pin. If `pkg` is tracking a path, e.g. after [`Pkg.develop`](https://pkgdocs.julialang.org/v1/api/#Pkg.develop), go back to tracking registered versions. To free all dependencies set `all_pkgs=true`.

The `all_pkgs` kwarg was introduced in julia 1.7.

**Examples**

```
# Free a single package (remove pin or stop tracking path)
Pkg.free("Package")

# Free multiple packages
Pkg.free(["PackageA", "PackageB"])

# Free all packages in the project
Pkg.free(all_pkgs = true)
```

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L390-L414)[`Pkg.instantiate`](https://pkgdocs.julialang.org/v1/api/#Pkg.instantiate) — Function

`Pkg.instantiate(; verbose = false, workspace=false, io::IO=stderr, julia_version_strict=false)`
If a `Manifest.toml` file exists in the active project, download all the packages declared in that manifest. Otherwise, resolve a set of feasible packages from the `Project.toml` files and install them. `verbose = true` prints the build output to `stdout`/`stderr` instead of redirecting to the `build.log` file. `workspace=true` will also instantiate all projects in the workspace. If no `Project.toml` exist in the current active project, create one with all the dependencies in the manifest and instantiate the resulting project. `julia_version_strict=true` will turn manifest version check failures into errors instead of logging warnings.

After packages have been installed the project will be precompiled. See more at [Environment Precompilation](https://pkgdocs.julialang.org/v1/environments/#Environment-Precompilation).

The `julia_version_strict` keyword argument requires at least Julia 1.12.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L503-L522)[`Pkg.resolve`](https://pkgdocs.julialang.org/v1/api/#Pkg.resolve) — Function

`Pkg.resolve(; io::IO=stderr)`
Update the current manifest with potential changes to the dependency graph from packages that are tracking a path.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L525-L530)[`Pkg.gc`](https://pkgdocs.julialang.org/v1/api/#Pkg.gc) — Function

`Pkg.gc(; collect_delay::Period=Day(7), io::IO=stderr)`
Garbage-collect package and artifact installations by sweeping over all known `Manifest.toml` and `Artifacts.toml` files, noting those that have been deleted, and then finding artifacts and packages that are thereafter not used by any other projects, marking them as "orphaned". This method will only remove orphaned objects (package versions, artifacts, and scratch spaces) that have been continually un-used for a period of `collect_delay`; which defaults to seven days.

To disable automatic garbage collection, you can set the environment variable `JULIA_PKG_GC_AUTO` to `"false"` before starting Julia or call `API.auto_gc(false)`.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L332-L344)[`Pkg.status`](https://pkgdocs.julialang.org/v1/api/#Pkg.status) — Function

```
Pkg.status([pkgs...]; outdated::Bool=false, mode::PackageMode=PKGMODE_PROJECT, diff::Bool=false,
           compat::Bool=false, extensions::Bool=false, workspace::Bool=false, io::IO=stdout)
```

Print out the status of the project/manifest.

Packages marked with `⌃` have new versions that can be installed, e.g. via [`Pkg.update`](https://pkgdocs.julialang.org/v1/api/#Pkg.update). Those marked with `⌅` have new versions available, but cannot be installed due to compatibility conflicts with other packages. To see why, set the keyword argument `outdated=true`.

Setting `outdated=true` will only show packages that are not on the latest version, their maximum version and why they are not on the latest version (either due to other packages holding them back due to compatibility constraints, or due to compatibility in the project file). As an example, a status output like:

```
julia> Pkg.status(; outdated=true)
Status `Manifest.toml`
⌃ [a8cc5b0e] Crayons v2.0.0 [<v3.0.0], (<v4.0.4)
⌅ [b8a86587] NearestNeighbors v0.4.8 (<v0.4.9) [compat]
⌅ [2ab3a3ac] LogExpFunctions v0.2.5 (<v0.3.0): SpecialFunctions
```

means that the latest version of Crayons is 4.0.4 but the latest version compatible with the `[compat]` section in the current project is 3.0.0. The latest version of NearestNeighbors is 0.4.9 but due to compat constrains in the project it is held back to 0.4.8. The latest version of LogExpFunctions is 0.3.0 but SpecialFunctions is holding it back to 0.2.5.

If `mode` is `PKGMODE_PROJECT`, print out status only about the packages that are in the project (explicitly added). If `mode` is `PKGMODE_MANIFEST`, print status also about those in the manifest (recursive dependencies). If there are any packages listed as arguments, the output will be limited to those packages.

Setting `ext=true` will show dependencies with extensions and what extension dependencies of those that are currently loaded.

Setting `diff=true` will, if the environment is in a git repository, limit the output to the difference as compared to the last git commit.

Setting `workspace=true` will show the (merged) status of packages in the workspace.

See [`Pkg.project`](https://pkgdocs.julialang.org/v1/api/#Pkg.project) and [`Pkg.dependencies`](https://pkgdocs.julialang.org/v1/api/#Pkg.dependencies) to get the project/manifest status as a Julia object instead of printing it.

The `⌃` and `⌅` indicators were added in Julia 1.8. The `outdated` keyword argument requires at least Julia 1.8.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L533-L584)[`Pkg.compat`](https://pkgdocs.julialang.org/v1/api/#Pkg.compat) — Function

`Pkg.compat()`
Interactively edit the [compat] entries within the current Project.

`Pkg.compat(pkg::String, compat::String)`
Set the [compat] string for the given package within the current Project.

See [Compatibility](https://pkgdocs.julialang.org/v1/compatibility/#Compatibility) for more information on the project [compat] section.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L587-L597)[`Pkg.precompile`](https://pkgdocs.julialang.org/v1/api/#Pkg.precompile) — Function

```
Pkg.precompile(; strict::Bool=false, timing::Bool=false)
Pkg.precompile(pkg; strict::Bool=false, timing::Bool=false)
Pkg.precompile(pkgs; strict::Bool=false, timing::Bool=false)
```

Precompile all or specific dependencies of the project in parallel.

Set `timing=true` to show the duration of the precompilation of each dependency.

Errors will only throw when precompiling the top-level dependencies, given that not all manifest dependencies may be loaded by the top-level dependencies on the given system. This can be overridden to make errors in all dependencies throw by setting the kwarg `strict` to `true`

This method is called automatically after any Pkg action that changes the manifest. Any packages that have previously errored during precompilation won't be retried in auto mode until they have changed. To disable automatic precompilation set `ENV["JULIA_PKG_PRECOMPILE_AUTO"]=0`. To manually control the number of tasks used set `ENV["JULIA_NUM_PRECOMPILE_TASKS"]`.

Specifying packages to precompile requires at least Julia 1.8.

Timing mode requires at least Julia 1.9.

**Examples**

```
Pkg.precompile()
Pkg.precompile("Foo")
Pkg.precompile(["Foo", "Bar"])
```

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L189-L221)[`Pkg.offline`](https://pkgdocs.julialang.org/v1/api/#Pkg.offline) — Function

`Pkg.offline(b::Bool=true)`
Enable (`b=true`) or disable (`b=false`) offline mode.

In offline mode Pkg tries to do as much as possible without connecting to internet. For example, when adding a package Pkg only considers versions that are already downloaded in version resolution.

To work in offline mode across Julia sessions you can set the environment variable `JULIA_PKG_OFFLINE` to `"true"` before starting Julia.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L634-L645)[`Pkg.why`](https://pkgdocs.julialang.org/v1/api/#Pkg.why) — Function

```
Pkg.why(pkg::Union{String, Vector{String}}; workspace::Bool=false)
Pkg.why(pkg::Union{PackageSpec, Vector{PackageSpec}}; workspace::Bool=false)
```

Show the reason why this package is in the manifest. The output is all the different ways to reach the package through the dependency graph starting from the dependencies. If `workspace` is true, this will consider all projects in the workspace and not just the active one.

This function requires at least Julia 1.9.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L236-L247)[`Pkg.dependencies`](https://pkgdocs.julialang.org/v1/api/#Pkg.dependencies) — Function

`Pkg.dependencies()::Dict{UUID, PackageInfo}`
This feature is considered experimental.

Query the dependency graph of the active project. The result is a `Dict` that maps a package UUID to a `PackageInfo` struct representing the dependency (a package).

**`PackageInfo` fields**

| Field | Description |
| --- | --- |
| `name` | The name of the package |
| `version` | The version of the package (this is `Nothing` for stdlibs) |
| `tree_hash` | A file hash of the package directory tree |
| `is_direct_dep` | The package is a direct dependency |
| `is_pinned` | Whether a package is pinned |
| `is_tracking_path` | Whether a package is tracking a path |
| `is_tracking_repo` | Whether a package is tracking a repository |
| `is_tracking_registry` | Whether a package is being tracked by registry i.e. not by path nor by repository |
| `git_revision` | The git revision when tracking by repository |
| `git_source` | The git source when tracking by repository |
| `source` | The directory containing the source code for that package |
| `dependencies` | The dependencies of that package as a vector of UUIDs |

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L456-L480)[`Pkg.respect_sysimage_versions`](https://pkgdocs.julialang.org/v1/api/#Pkg.respect_sysimage_versions) — Function

`Pkg.respect_sysimage_versions(b::Bool=true)`
Enable (`b=true`) or disable (`b=false`) respecting versions that are in the sysimage (enabled by default).

If this option is enabled, Pkg will only install packages that have been put into the sysimage (e.g. via PackageCompiler) at the version of the package in the sysimage. Also, trying to add a package at a URL or `develop` a package that is in the sysimage will error.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L648-L658)[`Pkg.project`](https://pkgdocs.julialang.org/v1/api/#Pkg.project) — Function

`Pkg.project()::ProjectInfo`
This feature is considered experimental.

Request a `ProjectInfo` struct which contains information about the active project.

**`ProjectInfo` fields**

| Field | Description |
| --- | --- |
| name | The project's name |
| uuid | The project's UUID |
| version | The project's version |
| ispackage | Whether the project is a package (has a name and uuid) |
| dependencies | The project's direct dependencies as a `Dict` which maps dependency name to dependency UUID |
| path | The location of the project file which defines the active project |

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L483-L500)[`Pkg.undo`](https://pkgdocs.julialang.org/v1/api/#Pkg.undo) — Function

`undo()`
Undoes the latest change to the active project. Only states in the current session are stored, up to a maximum of 50 states.

See also: [`redo`](https://pkgdocs.julialang.org/v1/api/#Pkg.redo).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L735-L742)[`Pkg.redo`](https://pkgdocs.julialang.org/v1/api/#Pkg.redo) — Function

`redo()`
Redoes the changes from the latest [`undo`](https://pkgdocs.julialang.org/v1/api/#Pkg.undo).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L745-L749)[`Pkg.setprotocol!`](https://pkgdocs.julialang.org/v1/api/#Pkg.setprotocol!) — Function

```
setprotocol!(;
    domain::AbstractString = "github.com",
    protocol::Union{Nothing, AbstractString}=nothing
)
```

Set the protocol used to access hosted packages when `add`ing a url or `develop`ing a package. Defaults to delegating the choice to the package developer (`protocol === nothing`). Other choices for `protocol` are `"https"` or `"git"`.

**Examples**

```
julia> Pkg.setprotocol!(domain = "github.com", protocol = "ssh")

# Use HTTPS for GitHub (default, good for most users)  
julia> Pkg.setprotocol!(domain = "github.com", protocol = "https")

# Reset to default (let package developer decide)
julia> Pkg.setprotocol!(domain = "github.com", protocol = nothing)

# Set protocol for custom domain without specifying protocol
julia> Pkg.setprotocol!(domain = "gitlab.mycompany.com")

# Use Git protocol for a custom domain
julia> Pkg.setprotocol!(domain = "gitlab.mycompany.com", protocol = "git")
```

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L706-L732)[`Pkg.PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec) — Type

```
PackageSpec(name::String, [uuid::UUID, version::VersionNumber])
PackageSpec(; name, url, path, subdir, rev, version, mode, level)
```

A `PackageSpec` is a representation of a package with various metadata. This includes:

*   The `name` of the package.
*   The package's unique `uuid`.
*   A `version` (for example when adding a package). When upgrading, can also be an instance of the enum [`UpgradeLevel`](https://pkgdocs.julialang.org/v1/api/#Pkg.UpgradeLevel). If the version is given as a `String` this means that unspecified versions are "free", for example `version="0.5"` allows any version `0.5.x` to be installed. If given as a `VersionNumber`, the exact version is used, for example `version=v"0.5.3"`.
*   A `url` and an optional git `rev`ision. `rev` can be a branch name or a git commit SHA1.
*   A local `path`. This is equivalent to using the `url` argument but can be more descriptive.
*   A `subdir` which can be used when adding a package that is not in the root of a repository.

Most functions in Pkg take a `Vector` of `PackageSpec` and do the operation on all the packages in the vector.

Many functions that take a `PackageSpec` or a `Vector{PackageSpec}` can be called with a more concise notation with `NamedTuple`s. For example, `Pkg.add` can be called either as the explicit or concise versions as:

| Explicit | Concise |
| --- | --- |
| `Pkg.add(PackageSpec(name="Package"))` | `Pkg.add(name = "Package")` |
| `Pkg.add(PackageSpec(url="www.myhost.com/MyPkg")))` | `Pkg.add(url="www.myhost.com/MyPkg")` |
| `Pkg.add([PackageSpec(name="Package"), PackageSpec(path="/MyPkg"])` | `Pkg.add([(;name="Package"), (;path="/MyPkg")])` |

Below is a comparison between the REPL mode and the functional API:

| `REPL` | `API` |
| --- | --- |
| `Package` | `PackageSpec("Package")` |
| `Package@0.2` | `PackageSpec(name="Package", version="0.2")` |
| - | `PackageSpec(name="Package", version=v"0.2.1")` |
| `Package=a67d...` | `PackageSpec(name="Package", uuid="a67d...")` |
| `Package#master` | `PackageSpec(name="Package", rev="master")` |
| `local/path#feature` | `PackageSpec(path="local/path"; rev="feature")` |
| `www.mypkg.com` | `PackageSpec(url="www.mypkg.com")` |
| `--major Package` | `PackageSpec(name="Package", version=UPLEVEL_MAJOR)` |

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L661-L703)[`Pkg.PackageMode`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageMode) — Type

`PackageMode`
An enum with the instances

*   `PKGMODE_MANIFEST`
*   `PKGMODE_PROJECT`

Determines if operations should be made on a project or manifest level. Used as an argument to [`Pkg.rm`](https://pkgdocs.julialang.org/v1/api/#Pkg.rm), [`Pkg.update`](https://pkgdocs.julialang.org/v1/api/#Pkg.update) and [`Pkg.status`](https://pkgdocs.julialang.org/v1/api/#Pkg.status).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L91-L101)[`Pkg.UpgradeLevel`](https://pkgdocs.julialang.org/v1/api/#Pkg.UpgradeLevel) — Type

`UpgradeLevel`
An enum with the instances

*   `UPLEVEL_FIXED`
*   `UPLEVEL_PATCH`
*   `UPLEVEL_MINOR`
*   `UPLEVEL_MAJOR`

Determines how much a package is allowed to be updated. Used as an argument to [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec) or as an argument to [`Pkg.update`](https://pkgdocs.julialang.org/v1/api/#Pkg.update).

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L105-L117)
[Registry API Reference](https://pkgdocs.julialang.org/v1/api/#Registry-API-Reference)[](https://pkgdocs.julialang.org/v1/api/)[](https://pkgdocs.julialang.org/v1/api/#Registry-API-Reference "Permalink")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The functional API for registries uses [`RegistrySpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.RegistrySpec)s, similar to [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec).

[`Pkg.RegistrySpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.RegistrySpec) — Type

```
RegistrySpec(name::String)
RegistrySpec(; name, uuid, url, path)
```

A `RegistrySpec` is a representation of a registry with various metadata, much like [`PackageSpec`](https://pkgdocs.julialang.org/v1/api/#Pkg.PackageSpec). This includes:

*   The `name` of the registry.
*   The registry's unique `uuid`.
*   The `url` to the registry.
*   A local `path`.

Most registry functions in Pkg take a `Vector` of `RegistrySpec` and do the operation on all the registries in the vector.

Many functions that take a `RegistrySpec` can be called with a more concise notation with keyword arguments. For example, `Pkg.Registry.add` can be called either as the explicit or concise versions as:

| Explicit | Concise |
| --- | --- |
| `Pkg.Registry.add(RegistrySpec(name="General"))` | `Pkg.Registry.add(name = "General")` |
| `Pkg.Registry.add(RegistrySpec(url="https://github.com/JuliaRegistries/General.git")))` | `Pkg.Registry.add(url = "https://github.com/JuliaRegistries/General.git")` |

Below is a comparison between the REPL mode and the functional API::

| `REPL` | `API` |
| --- | --- |
| `MyRegistry` | `RegistrySpec("MyRegistry")` |
| `MyRegistry=a67d...` | `RegistrySpec(name="MyRegistry", uuid="a67d...")` |
| `local/path` | `RegistrySpec(path="local/path")` |
| `www.myregistry.com` | `RegistrySpec(url="www.myregistry.com")` |

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Pkg.jl#L752-L784)[`Pkg.Registry.add`](https://pkgdocs.julialang.org/v1/api/#Pkg.Registry.add) — Function

`Pkg.Registry.add(registry::RegistrySpec)`
Add new package registries.

The no-argument `Pkg.Registry.add()` will install the default registries.

**Examples**

```
Pkg.Registry.add("General")
Pkg.Registry.add(uuid = "23338594-aafe-5451-b93e-139f81909106")
Pkg.Registry.add(url = "https://github.com/JuliaRegistries/General.git")
```

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Registry/Registry.jl#L28-L41)[`Pkg.Registry.rm`](https://pkgdocs.julialang.org/v1/api/#Pkg.Registry.rm) — Function

```
Pkg.Registry.rm(registry::String)
Pkg.Registry.rm(registry::RegistrySpec)
```

Remove registries.

**Examples**

```
Pkg.Registry.rm("General")
Pkg.Registry.rm(uuid = "23338594-aafe-5451-b93e-139f81909106")
```

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Registry/Registry.jl#L288-L299)[`Pkg.Registry.update`](https://pkgdocs.julialang.org/v1/api/#Pkg.Registry.update) — Function

```
Pkg.Registry.update()
Pkg.Registry.update(registry::RegistrySpec)
Pkg.Registry.update(registry::Vector{RegistrySpec})
```

Update registries. If no registries are given, update all available registries.

**Examples**

```
Pkg.Registry.update()
Pkg.Registry.update("General")
Pkg.Registry.update(uuid = "23338594-aafe-5451-b93e-139f81909106")
```

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Registry/Registry.jl#L372-L386)[`Pkg.Registry.status`](https://pkgdocs.julialang.org/v1/api/#Pkg.Registry.status) — Function

`Pkg.Registry.status()`
Display information about available registries.

**Examples**

`Pkg.Registry.status()`

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Registry/Registry.jl#L560-L569)
[Artifacts API Reference](https://pkgdocs.julialang.org/v1/api/#Artifacts-Reference)[](https://pkgdocs.julialang.org/v1/api/)[](https://pkgdocs.julialang.org/v1/api/#Artifacts-Reference "Permalink")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Pkg.Artifacts.create_artifact`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.create_artifact) — Function

`create_artifact(f::Function)`
Creates a new artifact by running `f(artifact_path)`, hashing the result, and moving it to the artifact store (`~/.julia/artifacts` on a typical installation). Returns the identifying tree hash of this artifact.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L22-L28)[`Pkg.Artifacts.remove_artifact`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.remove_artifact) — Function

`remove_artifact(hash::SHA1; honor_overrides::Bool=false)`
Removes the given artifact (identified by its SHA1 git tree hash) from disk. Note that if an artifact is installed in multiple depots, it will be removed from all of them. If an overridden artifact is requested for removal, it will be silently ignored; this method will never attempt to remove an overridden artifact.

In general, we recommend that you use `Pkg.gc()` to manage artifact installations and do not use `remove_artifact()` directly, as it can be difficult to know if an artifact is being used by another package.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L104-L115)[`Pkg.Artifacts.verify_artifact`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.verify_artifact) — Function

`verify_artifact(hash::SHA1; honor_overrides::Bool=false)`
Verifies that the given artifact (identified by its SHA1 git tree hash) is installed on- disk, and retains its integrity. If the given artifact is overridden, skips the verification unless `honor_overrides` is set to `true`.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L131-L137)[`Pkg.Artifacts.bind_artifact!`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.bind_artifact!) — Function

```
bind_artifact!(artifacts_toml::String, name::String, hash::SHA1;
               platform::Union{AbstractPlatform,Nothing} = nothing,
               download_info::Union{Vector{Tuple},Nothing} = nothing,
               lazy::Bool = false,
               force::Bool = false)
```

Writes a mapping of `name` ->`hash` within the given `(Julia)Artifacts.toml` file. If `platform` is not `nothing`, this artifact is marked as platform-specific, and will be a multi-mapping. It is valid to bind multiple artifacts with the same name, but different `platform`s and `hash`'es within the same `artifacts_toml`. If `force` is set to `true`, this will overwrite a pre-existant mapping, otherwise an error is raised.

`download_info` is an optional vector that contains tuples of URLs and a hash. These URLs will be listed as possible locations where this artifact can be obtained. If `lazy` is set to `true`, even if download information is available, this artifact will not be downloaded until it is accessed via the `artifact"name"` syntax, or `ensure_artifact_installed()` is called upon it.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L182-L200)[`Pkg.Artifacts.unbind_artifact!`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.unbind_artifact!) — Function

`unbind_artifact!(artifacts_toml::String, name::String; platform = nothing)`
Unbind the given `name` from an `(Julia)Artifacts.toml` file. Silently fails if no such binding exists within the file.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L278-L283)[`Pkg.Artifacts.download_artifact`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.download_artifact) — Function

```
download_artifact(tree_hash::SHA1, tarball_url::String, tarball_hash::String;
                  verbose::Bool = false, io::IO=stderr)
```

Download/install an artifact into the artifact store. Returns `true` on success, returns an error object on failure.

As of Julia 1.8 this function returns the error object rather than `false` when failure occurs

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L306-L316)[`Pkg.Artifacts.ensure_artifact_installed`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.ensure_artifact_installed) — Function

```
ensure_artifact_installed(name::String, artifacts_toml::String;
                          platform::AbstractPlatform = HostPlatform(),
                          pkg_uuid::Union{Base.UUID,Nothing}=nothing,
                          verbose::Bool = false,
                          quiet_download::Bool = false,
                          io::IO=stderr)
```

Ensures an artifact is installed, downloading it via the download information stored in `artifacts_toml` if necessary. Throws an error if unable to install.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L409-L419)[`Pkg.Artifacts.ensure_all_artifacts_installed`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.ensure_all_artifacts_installed) — Function

```
ensure_all_artifacts_installed(artifacts_toml::String;
                               platform = HostPlatform(),
                               pkg_uuid = nothing,
                               include_lazy = false,
                               verbose = false,
                               quiet_download = false,
                               io::IO=stderr)
```

Installs all non-lazy artifacts from a given `(Julia)Artifacts.toml` file. `package_uuid` must be provided to properly support overrides from `Overrides.toml` entries in depots.

If `include_lazy` is set to `true`, then lazy packages will be installed as well.

This function is deprecated and should be replaced with the following snippet:

```
artifacts = select_downloadable_artifacts(artifacts_toml; platform, include_lazy)
for name in keys(artifacts)
    ensure_artifact_installed(name, artifacts[name], artifacts_toml; platform=platform)
end
```

This function is deprecated in Julia 1.6 and will be removed in a future version. Use `select_downloadable_artifacts()` and `ensure_artifact_installed()` instead.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L544-L568)[`Pkg.Artifacts.archive_artifact`](https://pkgdocs.julialang.org/v1/api/#Pkg.Artifacts.archive_artifact) — Function

`archive_artifact(hash::SHA1, tarball_path::String; honor_overrides::Bool=false)`
Archive an artifact into a tarball stored at `tarball_path`, returns the SHA256 of the resultant tarball as a hexadecimal string. Throws an error if the artifact does not exist. If the artifact is overridden, throws an error unless `honor_overrides` is set.

[source](https://github.com/JuliaLang/Pkg.jl/blob/69926e385c878253d62e2588a19b252277196ebf/src/Artifacts.jl#L155-L161)
