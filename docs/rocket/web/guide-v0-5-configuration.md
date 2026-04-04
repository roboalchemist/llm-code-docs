# Source: https://rocket.rs/guide/v0.5/configuration/

Title: Configuration - Rocket Web Framework

URL Source: https://rocket.rs/guide/v0.5/configuration/

Markdown Content:
Rocket's configuration system is flexible. Based on [Figment](https://docs.rs/figment/0.10/figment), it allows you to configure your application the way _you_ want while also providing with a sensible set of defaults.

[](https://rocket.rs/guide/v0.5/configuration/#overview "anchor")Overview
-------------------------------------------------------------------------

Rocket's configuration system is based on Figment's [`Provider`](https://docs.rs/figment/0.10/figment/trait.Provider.html)s, types which provide configuration data. Rocket's [`Config`](https://api.rocket.rs/v0.5/rocket/struct.Config.html) and [`Config::figment()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.figment), as well as Figment's [`Toml`](https://docs.rs/figment/0.10/figment/providers/struct.Toml.html) and [`Json`](https://docs.rs/figment/0.10/figment/providers/struct.Json.html), are some examples of providers. Providers can be combined into a single [`Figment`](https://docs.rs/figment/0.10/figment/struct.Figment.html) provider from which any configuration structure that implements [`Deserialize`](https://api.rocket.rs/v0.5/rocket/serde/trait.Deserialize.html) can be extracted.

Rocket expects to be able to extract a [`Config`](https://api.rocket.rs/v0.5/rocket/struct.Config.html) structure from the provider it is configured with. This means that no matter which configuration provider Rocket is asked to use, it must be able to read the following configuration values:

| key | kind | description | debug/release default |
| --- | --- | --- | --- |
| `address` | `IpAddr` | IP address to serve on | `127.0.0.1` |
| `port` | `u16` | Port to serve on. | `8000` |
| `workers`* | `usize` | Number of threads to use for executing futures. | cpu core count |
| `max_blocking`* | `usize` | Limit on threads to start for blocking tasks. | `512` |
| `ident` | `string`, `false` | If and how to identify via the `Server` header. | `"Rocket"` |
| `ip_header` | `string`, `false` | IP header to inspect to get [client's real IP](https://api.rocket.rs/v0.5/rocket/request/struct.Request.html#method.real_ip). | `"X-Real-IP"` |
| `keep_alive` | `u32` | Keep-alive timeout seconds; disabled when `0`. | `5` |
| `log_level` | [`LogLevel`](https://api.rocket.rs/v0.5/rocket/config/enum.LogLevel.html) | Max level to log. (off/normal/debug/critical) | `normal`/`critical` |
| `cli_colors` | `bool` | Whether to use colors and emoji when logging. | `true` |
| `secret_key` | [`SecretKey`](https://api.rocket.rs/v0.5/rocket/config/struct.SecretKey.html) | Secret key for signing and encrypting values. | `None` |
| `tls` | [`TlsConfig`](https://api.rocket.rs/v0.5/rocket/config/struct.TlsConfig.html) | TLS configuration, if any. | `None` |
| `limits` | [`Limits`](https://api.rocket.rs/v0.5/rocket/data/struct.Limits.html) | Streaming read size limits. | [`Limits::default()`](https://api.rocket.rs/v0.5/rocket/data/struct.Limits.html#impl-Default-for-Limits) |
| `limits.$name` | `&str`/`uint` | Read limit for `$name`. | form = "32KiB" |
| `ctrlc` | `bool` | Whether `ctrl-c` initiates a server shutdown. | `true` |
| `shutdown`* | [`Shutdown`](https://api.rocket.rs/v0.5/rocket/config/struct.Shutdown.html) | Graceful shutdown configuration. | [`Shutdown::default()`](https://api.rocket.rs/v0.5/rocket/config/struct.Shutdown.html#fields) |

* Note: the `workers`, `max_blocking`, and `shutdown.force` configuration parameters are only read from the [default provider](https://rocket.rs/guide/v0.5/configuration/#default-provider).

### [](https://rocket.rs/guide/v0.5/configuration/#profiles "anchor")Profiles

Configurations can be arbitrarily namespaced by [`Profile`](https://docs.rs/figment/0.10/figment/struct.Profile.html)s. Rocket's [`Config`](https://api.rocket.rs/v0.5/rocket/struct.Config.html) and [`Config::figment()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.figment) providers automatically set the configuration profile to "debug" when compiled in "debug" mode and "release" when compiled in release mode, but you can arbitrarily name and set profiles to your desire. For example, with the [default provider](https://rocket.rs/guide/v0.5/configuration/#default-provider), you can set the selected profile via `ROCKET_PROFILE`. This results in Rocket preferring the values in the `ROCKET_PROFILE` profile.

In addition to any profiles you declare, there are two meta-profiles, `default` and `global`, which can be used to provide values that apply to _all_ profiles. Values provided in a `default` profile are used as fall-back values when the selected profile doesn't contain a requested value, while values in the `global` profile supplant any values with the same name in any profile.

[](https://rocket.rs/guide/v0.5/configuration/#default-provider "anchor")Default Provider
-----------------------------------------------------------------------------------------

Rocket's default configuration provider is [`Config::figment()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.figment); this is the provider that's used when calling [`rocket::build()`](https://api.rocket.rs/v0.5/rocket/fn.custom.html).

The default figment reads from and merges, at a per-key level, the following sources in ascending priority order:

1. [`Config::default()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.default), which provides default values for all parameters.
2. `Rocket.toml`_or_ TOML file path in `ROCKET_CONFIG` environment variable.
3. `ROCKET_` prefixed environment variables.

The selected profile is the value of the `ROCKET_PROFILE` environment variable, or if it is not set, "debug" when compiled in debug mode and "release" when compiled in release mode. With the exception of `log_level`, which changes from `normal` in debug to `critical` in release, all of the default configuration values are the same in all profiles. What's more, all configuration values _have_ defaults, so no configuration is needed to get started.

As a result of `Config::figment()`, without any effort, Rocket can be configured via a `Rocket.toml` file and/or via environment variables, the latter of which take precedence over the former.

### [](https://rocket.rs/guide/v0.5/configuration/#rocket-toml "anchor")Rocket.toml

Rocket searches for `Rocket.toml` or the filename in a `ROCKET_CONFIG` environment variable starting at the current working directory. If it is not found, the parent directory, its parent, and so on, are searched until the file is found or the root is reached. If the path set in `ROCKET_CONFIG` is absolute, no such search occurs and the set path is used directly.

The file is assumed to be _nested_, so each top-level key declares a profile and its values the value for the profile. The following is an example of what such a file might look like:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20[default]address = "0.0.0.0"limits = { form = "64 kB", json = "1 MiB" }[debug]port = 8000 limits = { json = "10MiB" }[nyc]port = 9001[release]port = 9999 ip_header = false secret_key = "hPrYyЭRiMyµ5sBB1π+CMæ1køFsåqKvBiQJxBVHQk="

The following is a `Rocket.toml` file with all configuration options set for demonstration purposes. You **do not** and _should not_ set a value for configuration options needlessly, preferring to use the default value when sensible.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28[default]address = "127.0.0.1"port = 8000 workers = 16 max_blocking = 512 keep_alive = 5 ident = "Rocket"ip_header = "X-Real-IP" log_level = "normal"temp_dir = "/tmp"cli_colors = true secret_key = "hPrYyЭRiMyµ5sBB1π+CMæ1køFsåqKvBiQJxBVHQk="[default.limits]form = "64 kB"json = "1 MiB"msgpack = "2 MiB""file/jpg" = "5 MiB"[default.tls]certs = "path/to/cert-chain.pem"key = "path/to/key.pem"[default.shutdown]ctrlc = true signals = ["term", "hup"]grace = 5 mercy = 5

### [](https://rocket.rs/guide/v0.5/configuration/#environment-variables "anchor")Environment Variables

Rocket reads all environment variable names prefixed with `ROCKET_` using the string after the `_` as the name of a configuration value as the value of the parameter as the value itself. Environment variables take precedence over values in `Rocket.toml`. Values are parsed as loose form of TOML syntax. Consider the following examples:

1
2
3
4
5
6
7
8
9
10
11 ROCKET_FLOAT=3.14 ROCKET_ARRAY=[1,"b",3.14]ROCKET_STRING=Hello ROCKET_STRING="Hello There"ROCKET_KEEP_ALIVE=1 ROCKET_IDENT=Rocket ROCKET_IDENT="Hello Rocket"ROCKET_IDENT=false ROCKET_TLS={certs="abc",key="foo/bar"}ROCKET_LIMITS={form="64 KiB"}

[](https://rocket.rs/guide/v0.5/configuration/#configuration-parameters "anchor")Configuration Parameters
---------------------------------------------------------------------------------------------------------

### [](https://rocket.rs/guide/v0.5/configuration/#secret-key "anchor")Secret Key

The `secret_key` parameter configures a cryptographic key to use when encrypting application values. In particular, the key is used to encrypt [private cookies](https://rocket.rs/guide/v0.5/requests/#private-cookies), which are available only when the `secrets` crate feature is enabled.

Generating a string suitable for use as a `secret_key` configuration value is usually done through tools like `openssl`. Using `openssl`, a 256-bit base64 key can be generated with the command `openssl rand -base64 32`.

When compiled in debug mode, a fresh key is generated automatically. In release mode, Rocket requires you to set a secret key if the `secrets` feature is enabled. Failure to do so results in a hard error at launch time. The value of the parameter may either be a 256-bit base64 or hex string or a slice of 32 bytes.

### [](https://rocket.rs/guide/v0.5/configuration/#limits "anchor")Limits

The `limits` parameter configures the maximum amount of data Rocket will accept for a given data type. The value is expected to be a dictionary table where each key corresponds to a data type and each value corresponds to the maximum size in bytes Rocket should accept for that type. Rocket can parse both integers (`32768`) or SI unit based strings (`"32KiB"`) as limits.

By default, Rocket specifies a `32 KiB` limit for incoming forms. Since Rocket requires specifying a read limit whenever data is read, external data guards may also choose to have a configure limit via the `limits` parameter. The [`Json`](https://api.rocket.rs/v0.5/rocket/serde/json/struct.Json.html) type, for instance, uses the `limits.json` parameter.

### [](https://rocket.rs/guide/v0.5/configuration/#tls "anchor")TLS

Rocket includes built-in, native support for TLS >= 1.2 (Transport Layer Security). To enable TLS support:

1. Enable the `tls` crate feature in `Cargo.toml`:

1
2[dependencies]rocket = { version = "0.5.1", features = ["tls"] }

1. Configure a TLS certificate chain and private key via the `tls.key` and `tls.certs` configuration parameters. With the default provider, this can be done via `Rocket.toml` as:

1
2
3[default.tls]key = "path/to/key.pem" certs = "path/to/certs.pem"

The `tls` parameter is expected to be a dictionary that deserializes into a [`TlsConfig`](https://api.rocket.rs/v0.5/rocket/config/struct.TlsConfig.html) structure:

| key | required | type |
| --- | --- | --- |
| `key` | **_yes_** | Path or bytes to DER-encoded ASN.1 PKCS#1/#8 or SEC1 key. |
| `certs` | **_yes_** | Path or bytes to DER-encoded X.509 TLS cert chain. |
| `ciphers` | no | Array of [`CipherSuite`](https://api.rocket.rs/v0.5/rocket/config/enum.CipherSuite.html)s to enable. |
| `prefer_server_cipher_order` | no | Boolean for whether to [prefer server cipher suites](https://api.rocket.rs/v0.5/rocket/config/struct.TlsConfig.html#method.with_preferred_server_cipher_order). |
| `mutual` | no | A map with [mutual TLS](https://rocket.rs/guide/v0.5/configuration/#mutual-tls) configuration. |

When specified via TOML or other serialized formats, each [`CipherSuite`](https://api.rocket.rs/v0.5/rocket/config/enum.CipherSuite.html) is written as a string representation of the respective variant. For example, `CipherSuite::TLS_AES_256_GCM_SHA384` is `"TLS_AES_256_GCM_SHA384"`. In TOML, the defaults (with an arbitrary `certs` and `key`) are written:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15[default.tls]certs = "/ssl/cert.pem"key = "/ssl/key.pem"prefer_server_cipher_order = false ciphers = [ "TLS_CHACHA20_POLY1305_SHA256", "TLS_AES_256_GCM_SHA384", "TLS_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256", "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",]

### [](https://rocket.rs/guide/v0.5/configuration/#mutual-tls "anchor")Mutual TLS

Rocket supports mutual TLS client authentication. Configuration works in concert with the [`mtls`](https://api.rocket.rs/v0.5/rocket/mtls/index.html) module, which provides a request guard to validate, verify, and retrieve client certificates in routes.

By default, mutual TLS is disabled and client certificates are not required, validated or verified. To enable mutual TLS, the `mtls` feature must be enabled and support configured via the `tls.mutual` config parameter:

1. Enable the `mtls` crate feature in `Cargo.toml`:

1
2[dependencies]rocket = { version = "0.5.1", features = ["mtls"] }

This implicitly enables the `tls` feature.

1. Configure a CA certificate chain via the `tls.mutual.ca_certs` configuration parameter. With the default provider, this can be done via `Rocket.toml` as:

1
2
3[default.tls.mutual]ca_certs = "path/to/ca_certs.pem" mandatory = true

The `tls.mutual` parameter is expected to be a dictionary that deserializes into a [`MutualTls`](https://api.rocket.rs/v0.5/rocket/config/struct.MutualTls.html) structure:

| key | required | type |
| --- | --- | --- |
| `ca_certs` | **_yes_** | Path or bytes to DER-encoded X.509 TLS cert chain. |
| `mandatory` | no | Boolean controlling whether the client _must_ authenticate. |

Rocket reports if TLS and/or mTLS are enabled at launch time:

1
2
3🔧 Configured for debug. ... >> tls: enabled w/mtls

Once mutual TLS is properly enabled, the [`mtls::Certificate`](https://api.rocket.rs/v0.5/rocket/mtls/struct.Certificate.html) request guard can be used to retrieve validated, verified client certificates:

1
2
3
4
5
6 use rocket::mtls::Certificate;#[get("/auth")]fn auth(cert: Certificate<'_>) { }

The [TLS example](https://github.com/rwf2/Rocket/tree/v0.5/examples/tls) illustrates a fully configured TLS server with mutual TLS.

Rocket's built-in TLS supports only TLS 1.2 and 1.3.

This may not be suitable for production use requiring legacy support.

### [](https://rocket.rs/guide/v0.5/configuration/#workers "anchor")Workers

The `workers` parameter sets the number of threads used for parallel task execution; there is no limit to the number of concurrent tasks. Due to a limitation in upstream async executers, unlike other values, the `workers` configuration value cannot be reconfigured or be configured from sources other than those provided by [`Config::figment()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.figment). In other words, only the values set by the `ROCKET_WORKERS` environment variable or in the `workers` property of `Rocket.toml` will be considered - all other `workers` values are ignored.

The `max_blocking` parameter sets an upper limit on the number of threads the underlying `async` runtime will spawn to execute potentially blocking, synchronous tasks via [`spawn_blocking`](https://docs.rs/tokio/1/tokio/task/fn.spawn_blocking.html) or equivalent. Similar to the `workers` parameter, `max_blocking` cannot be reconfigured or be configured from sources other than those provided by [`Config::figment()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.figment). Unlike `workers`, threads corresponding to `max_blocking` are not always active and will exit if idling. In general, the default value of `512` should not be changed unless physical or virtual resources are scarce. Rocket only executes work on blocking threads when required such as when performing file system I/O via [`TempFile`](https://api.rocket.rs/v0.5/rocket/fs/enum.TempFile.html) or wrapping synchronous work via [`rocket_sync_db_pools`](https://api.rocket.rs/v0.5/rocket_sync_db_pools/index.html).

Your application can extract any configuration that implements [`Deserialize`](https://api.rocket.rs/v0.5/rocket/serde/trait.Deserialize.html) from the configured provider, which is exposed via [`Rocket::figment()`](https://api.rocket.rs/v0.5/rocket/struct.Rocket.html#method.figment):

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22 use rocket::serde::Deserialize;#[launch]fn rocket() -> _{ let rocket = rocket::build(); let figment = rocket.figment(); #[derive(Deserialize)] #[serde(crate = "rocket::serde")] struct Config { port: u16, custom: Vec<String>, } let config: Config = figment.extract().expect("config"); let custom: Vec<String> = figment.extract_inner("custom").expect("custom"); rocket }

Both values recognized by Rocket and values _not_ recognized by Rocket can be extracted. This means you can configure values recognized by your application in Rocket's configuration sources directly. The next section describes how you can customize configuration sources by supplying your own `Provider`.

Because it is common to store configuration in managed state, Rocket provides an `AdHoc` fairing that 1) extracts a configuration from the configured provider, 2) pretty prints any errors, and 3) stores the value in managed state:

1
2
3
4
5
6
7
8
9
10
11
12
13 use rocket::{State, fairing::AdHoc};#[get("/custom")]fn custom(config: &State<Config>) -> String { config.custom.get(0).cloned().unwrap_or("default".into())}#[launch]fn rocket() ->_ { rocket::build() .mount("/", routes![custom]) .attach(AdHoc::config::<Config>())}

[](https://rocket.rs/guide/v0.5/configuration/#custom-providers "anchor")Custom Providers
-----------------------------------------------------------------------------------------

A custom provider can be set via [`rocket::custom()`](https://api.rocket.rs/v0.5/rocket/fn.custom.html), which replaces calls to [`rocket::build()`](https://api.rocket.rs/v0.5/rocket/fn.custom.html). The configured provider can be built on top of [`Config::figment()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.figment), [`Config::default()`](https://api.rocket.rs/v0.5/rocket/struct.Config.html#method.default), both, or neither. The [Figment](https://docs.rs/figment/0.10/figment) documentation has full details on instantiating existing providers like [`Toml`](https://docs.rs/figment/0.10/figment/providers/struct.Toml.html) and [`Json`](https://docs.rs/figment/0.10/figment/providers/struct.Json.html) as well as creating custom providers for more complex cases.

You may need to depend on `figment` and `serde` directly.

Rocket reexports `figment` and `serde` from its crate root, so you can refer to `figment` types via `rocket::figment` and `serde` types via `rocket::serde`. However, Rocket does not enable all features from either crate. As such, you may need to import crates directly:

`figment = { version = "0.10", features = ["env", "toml", "json"] }`

As a first example, we override configuration values at runtime by merging figment's tuple providers with Rocket's default provider:

1
2
3
4
5
6
7
8
9
10 use rocket::data::{Limits, ToByteUnit};#[launch]fn rocket() -> _ { let figment = rocket::Config::figment() .merge(("port", 1111)) .merge(("limits", Limits::new().limit("json", 2.mebibytes()))); rocket::custom(figment).mount("/", routes![])}

More involved, consider an application that wants to use Rocket's defaults for [`Config`](https://api.rocket.rs/v0.5/rocket/struct.Config.html), but not its configuration sources, while allowing the application to be configured via an `App.toml` file that uses top-level keys as profiles (`.nested()`), `APP_` environment variables as global overrides (`.global()`), and `APP_PROFILE` to configure the selected profile:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30 use rocket::serde::{Serialize, Deserialize};use rocket::fairing::AdHoc;use figment::{Figment, Profile, providers::{Format, Toml, Serialized, Env}};#[derive(Debug, Deserialize, Serialize)]#[serde(crate = "rocket::serde")]struct Config { app_value: usize, }impl Default for Config { fn default() -> Config { Config { app_value: 3, } }}#[launch]fn rocket() -> _{ let figment = Figment::from(rocket::Config::default()) .merge(Serialized::defaults(Config::default())) .merge(Toml::file("App.toml").nested()) .merge(Env::prefixed("APP_").global()) .select(Profile::from_env_or("APP_PROFILE", "default")); rocket::custom(figment) .mount("/", routes![]) .attach(AdHoc::config::<Config>())}

Rocket will extract its configuration from the configured provider. This means that if values like `port` and `address` are configured in `Config`, `App.toml` or `APP_` environment variables, Rocket will make use of them. The application can also extract its configuration, done here via the `Adhoc::config()` fairing.

* * *
