cargo::util

# Module context

Source

## Structs§

BuildTargetConfigConfiguration for `build.target`.CargoBuildAnalysisMetrics collection for build analysis.CargoBuildConfigThe `[build]` table.CargoFutureIncompatConfigThe `[future-incompat-report]` stableCargoHttpConfigThe `[http]` table.CargoNetConfigThe `[net]` table.CargoResolverConfigThe `[resolver]` table.CargoSshConfigConfigErrorInternal error for serde errors.ConfigKeyKey for a configuration variable.ConfigRelativePathUse with the `get` API to fetch a string that will be converted to a
`PathBuf`. Relative paths are converted to absolute paths based on the
location of the config file.CredentialCacheValueA previously generated authentication token and the data needed to determine if it can be reused.EnvConfigValueConfiguration value for environment variables in `[env]` section.GlobalContextConfiguration information for cargo. This is not specific to a build, it is information
relating to cargo itself.PathAndArgsA config type that is a program to run.ProgressConfigThe `term.progress` configuration.SslVersionConfigRangeStringListA type to deserialize a list of strings from a toml file.TargetCfgConfigConfig definition of a `[target.'cfg(…)']` table.TargetConfigConfig definition of a `[target]` table or `[host]`.TermConfigThe `[term]` table.ValueA type which can be deserialized as a configuration value which records
where it was deserialized from.

## Enums§

BracketTypeCargoFutureIncompatFrequencyConfigConfigValueSimilar to `toml::Value` but includes the source location where it is defined.DefinitionLocation where a config value is defined.FeatureUnificationIncompatibleRustVersionsJobsConfigConfiguration for `jobs` in `build` section. There are two
ways to configure: An integer or a simple string expression.ProgressWhenResolveTemplateErrorSslVersionConfigConfiguration for `ssl-version` in `http` section
There are two ways to configure:WarningHandlingWhether warnings should warn, be allowed, or cause an error.

## Constants§

TOP_LEVEL_CONFIG_KEYS

## Functions§

homedirsave_credentials

## Type Aliases§

EnvConfigOptValue
