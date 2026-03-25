cargo

# Module ops

Source

## Modules§

cargo_addCore of cargo-add commandcargo_configImplementation of `cargo config` subcommand.cargo_removeCore of cargo-remove commandtreeImplementation of `cargo tree`.

## Structs§

CleanContextCleanOptionsCompileOptionsContains information about how a package should be compiled.DocOptionsStrongly typed options for the `cargo doc` command.ExportInfoThis is the structure that is serialized and displayed to the user.FetchOptionsFixOptionsInstallTrackerOn-disk tracking for which package installed which binary.NewOptionsOutputMetadataOptionsOwnersOptionsPackageOptsPublishOptsReportRebuildsOptionsReportSessionsOptionsReportTimingsOptionsTestOptionsUnitGeneratorThe context needed for generating root units,
which are packages the user has requested to compile.UpdateOptionsVendorOptionsWorkspaceResolveResult for `resolve_ws_with_opts`.

## Enums§

CompileFilterFilter to apply to the root package to select which Cargo targets will be built.
(examples, bins, benches, tests, …)EditionFixModeThe behavior of `--edition` migration.FilterRuleIndicates which Cargo targets will be selected to be built.LibRuleIndicates whether or not the library target gets included.NewProjectKindOutputFormatFormat of rustdoc `--output-format`.PackageMessageFormatMessage format for `cargo package`.PackagesRepresents the selected packages that will be built.RegistryCredentialConfigRegistry settings loaded from config files.RegistryOrIndexRepresents either `--registry` or `--index` argument, which is mutually exclusive.VersionControl

## Functions§

add_overridesRead the `paths` configuration variable to discover all path overrides that
have been configured.check_yankedcleanCleans various caches.compileCompiles!compile_with_execLike `compile` but allows specifying a custom `Executor`
that will be able to intercept build calls and add custom logic.compile_wsLike `compile_with_exec` but without warnings from manifest parsing.create_bcxPrepares all required information for the actual compilation.docMain method for `cargo doc`.fetchExecutes `cargo fetch`.fixfix_editionPerforms the actions for the `-Zfix-edition` flag.fix_exec_rustcEntry point for `cargo` running as a proxy for `rustc`.fix_get_proxy_lock_addrProvide the lock address when running in proxy modegenerate_lockfileget_resolved_packagesinfoinitinstallinstall_listDisplay a list of installed binaries.load_pkg_lockfilemodify_ownersnewoutput_metadataLoads the manifest, resolves the dependencies of the package to the concrete
used versions - considering overrides - and writes all dependencies in a JSON
format to stdout.packagePackages an entire workspace.pkgidprintExecutes `rustc --print <VALUE>`.print_lockfile_changesPrints lockfile change statuses.publishread_packageregistry_loginregistry_logoutreport_rebuildsreport_sessionsreport_timingsresolve_all_featuresGets all of the features enabled for a package, plus its dependencies’
features.resolve_rootDetermines the root directory where installation is done.resolve_to_stringGenerate a toml String of Cargo.lock from a Resolve.resolve_with_previousResolves all dependencies for a package using an optional previous instance
of resolve to guide the resolution process.resolve_wsResolves all dependencies for the workspace using the previous
lock file as a guide if present.resolve_ws_with_optsResolves dependencies for some packages of the workspace,
taking into account `paths` overrides and activated features.runrun_benchesCompiles and runs benchmarks.run_testsCompiles and runs tests.searchuninstallupdate_lockfileupgrade_manifestsvendorwrite_manifest_upgradesUpdate manifests with upgraded versions, and write to disk. Based on
cargo-edit. Returns true if any file has changed.write_pkg_lockfileEnsure the resolve result is written to fiskyank
