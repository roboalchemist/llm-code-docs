homebrew

# Struct Formula

Source

```
pub struct Formula {}
```

## Fields§

§`name: String`§`full_name: String`§`tap: String`§`oldnames: Vec<String>`§`aliases: Vec<String>`§`versioned_formulae: Vec<String>`§`desc: String`§`license: Option<String>`§`homepage: String`§`versions: Versions`§`urls: Urls`§`revision: i32`§`version_scheme: i32`§`bottle: Bottle`§`pour_bottle_only_if: Option<String>`§`keg_only: bool`§`keg_only_reason: Option<KegOnlyReason>`§`options: Vec<Options>`§`build_dependencies: Vec<String>`§`dependencies: Vec<String>`§`test_dependencies: Vec<String>`§`recommended_dependencies: Vec<String>`§`optional_dependencies: Vec<String>`§`uses_from_macos: Vec<UsesFromMacOs>`§`uses_from_macos_bounds: Vec<UsesFromMacOsBounds>`§`requirements: Vec<Requirement>`§`conflicts_with: Vec<String>`§`conflicts_with_reasons: Vec<Option<String>>`§`link_overwrite: Vec<String>`§`caveats: Option<String>`§`installed: Vec<Installed>`§`linked_keg: Option<String>`§`pinned: bool`§`outdated: bool`§`deprecated: bool`§`deprecation_date: Option<String>`§`deprecation_reason: Option<String>`§`deprecation_replacement: Option<String>`§`disabled: bool`§`disable_date: Option<String>`§`disable_reason: Option<String>`§`disable_replacement: Option<String>`§`post_install_defined: bool`§`service: Option<Service>`§`tap_git_head: Option<String>`§`ruby_source_path: Option<String>`§`ruby_source_checksum: RubySourceChecksum`§`head_dependencies: Option<HeadDependencies>`

## Implementations§
