# Source: https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/

Title: Migrate from VCL | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)
4. [Developer guides](https://www.fastly.com/documentation/guides/compute/developer-guides/)

If you already have [VCL services](https://www.fastly.com/documentation/guides/full-site-delivery/fastly-vcl) with Fastly, all the logic you wrote in [VCL](https://www.fastly.com/documentation/reference/vcl) can be accomplished in Compute services, in any supported language. This page provides the equivalent Compute service code for the most common patterns we see in VCL.

This guide is intended as a quick-start for an initial migration to the Compute platform, not to be a comprehensive library of code examples. If the pattern you are trying to migrate is not here or you are looking to do something more complex, you might find a code example in our [examples library](https://www.fastly.com/documentation/solutions/examples).

For more information about each of the languages with official SDK support, see [choosing a language](https://www.fastly.com/documentation/guides/compute/#choose-a-language-to-use).

[](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#boilerplate)Boilerplate
--------------------------------------------------------------------------------------------------------

The examples below assume that you start with the default [starter kit](https://www.fastly.com/documentation/solutions/starters) for your chosen language when building your application. This is the default when you run [fastly compute init](https://www.fastly.com/documentation/reference/cli/compute/init/).

[](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#naming-conventions)Naming conventions
----------------------------------------------------------------------------------------------------------------------

These examples use a common set of naming conventions to draw parallels with VCL:

* `req`: For the incoming client request
* `beReq`: For a custom request built from scratch or by copying `req`
* `beResp`: For the return value of an origin fetch
* `resp`: For a custom response built from scratch or by copying a `beResp`

[](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#configuration)Configuration
------------------------------------------------------------------------------------------------------------

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#load-configuration-data-from-a-separate-file)Load configuration data from a separate file

1. Fastly VCL

`table settings {  "section.key": "some-value"}declare local var.some_value STRING;set var.some_value = table.lookup(  settings,  "section.key");`

1. Rust
2. JavaScript
3. Go

`// Using the config crate: https://docs.rs/configuse config::{Config, FileFormat};use fastly::{Error, Request, Response};#[fastly::main]fn main(_req: Request) -> Result<Response, Error> {    let config_builder = Config::builder().add_source(config::File::from_str(        include_str!("config.toml"), // assumes the existence of src/config.toml        FileFormat::Toml,    ));    let settings = config_builder.build()?;    let some_value = settings.get_string("section.key")?;    Ok(Response::from_body(some_value.as_str()))}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#load-configuration-data-from-a-dictionary)Load configuration data from a dictionary

1. Fastly VCL

`declare local var.some_value STRING;set var.some_value = table.lookup(  example_dictionary,  "key_name");`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response, ConfigStore};#[fastly::main]fn main(_req: Request) -> Result<Response, Error> {    let settings = ConfigStore::open("example_config_store");    let some_value = match settings.get("key_name") {      Some(value) => value,      _ => panic!("Value not set")    };    Ok(Response::from_body(some_value))}`

[](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#requests)Requests
--------------------------------------------------------------------------------------------------

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#add-a-header-to-a-client-request)Add a header to a client request

1. Fastly VCL

`# constant valueset req.http.Accept-Encoding = "br";# dynamic valueset req.http.Accept-Encoding = var.accept_encoding;`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    let accept_encoding = "br";    // constant value    req.set_header("Accept-Encoding", "br");    // dynamic value    req.set_header("Accept-Encoding", accept_encoding);    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#sort-and-sanitize-a-query-string)Sort and sanitize a query string

1. Fastly VCL

`set req.url = querystring.filter_except(req.url,  "a" + querystring.filtersep() +  "b" + querystring.filtersep() +  "c");set req.url = querystring.sort(req.url);`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    let mut qs: Vec<(String, String)> = req.get_query()?;    qs.retain(|param| ["a", "b", "c"].contains(&param.0.as_str()));    qs.sort_by(|(a, _), (b, _)| a.cmp(b));    req.set_query(&qs)?;    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#extract-a-query-string-parameter-from-the-request)Extract a query string parameter from the request

1. Fastly VCL

`declare local var.field STRING;set var.field = subfield(req.url.qs, "paramName", "&");`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};use std::collections::HashMap;#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    // assuming a request http://example.com?paramName=someValue    let params: HashMap<String, String> = req.get_query()?;    assert_eq!(params["paramName"], "someValue");    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#remove-a-header-from-a-client-request)Remove a header from a client request

1. Fastly VCL

`unset req.http.Some-Header;`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    req.remove_header("some-header");    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#modify-a-request-url-path)Modify a request URL path

1. Fastly VCL

`set req.url = "/new/path" + if(req.url.qs == "", "", "?") + req.url.qs;`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    req.set_path("/new/path");    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#check-for-header-presence-on-a-client-request)Check for header presence on a client request

1. Fastly VCL

`if (req.http.Some-Header) {  # ... do something ...}`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    if req.contains_header("some-header") {        // ... do something ...    }    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#check-whether-a-request-header-value-contains-a-substring)Check whether a request header value contains a substring

1. Fastly VCL

`if (std.strstr(req.http.foo, "someValue")) {  # ... do something ...}`

1. Rust
2. JavaScript
3. Go

`use fastly::http::HeaderValue;use fastly::{Error, Request, Response};fn header_val(header: Option<&HeaderValue>) -> &str {    match header {        Some(h) => h.to_str().unwrap_or(""),        None => "",    }}#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    if header_val(req.get_header("some-header")).contains("someValue") {        // ... do something ...    }    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#extract-constituent-parts-of-a-request)Extract constituent parts of a request

1. Fastly VCL

`declare local var.req_method STRING;declare local var.req_url STRING;declare local var.req_header STRING;declare local var.req_protocol STRING;set var.req_method = req.method;set var.req_url = req.url;set var.req_header = req.http.My-Header;set var.req_body = req.body;set var.req_protocol = if (fastly_info.is_h2, "2", "1.1");`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    let method = req.get_method();    let url = req.get_url();    let my_header = req.get_header("my-header");    let version = req.get_version();    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#identify-a-clients-geolocation-information)Identify a client's geolocation information

1. Fastly VCL

`declare local var.country_code STRING;declare local var.country_name STRING;declare local var.city STRING;set var.country_code = client.geo.country_code;set var.country_name = client.geo.country_name;set var.city = client.geo.city;`

1. Rust
2. JavaScript
3. Go

`use fastly::geo::geo_lookup;use fastly::{Error, Request, Response};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    let client_ip = req.get_client_ip_addr().unwrap();    let geo = geo_lookup(client_ip).unwrap();    let country_code = geo.country_code();    let country_name = geo.country_name();    let city_name = geo.city();    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#send-data-to-a-log-endpoint)Send data to a log endpoint

1. Fastly VCL

`log "syslog " + req.service_id + " request_logger :: " + now.sec + " " + client.ip + " " + req.url + " " + req.http.user-agent;`

1. Rust
2. JavaScript
3. Go

`use fastly::http::StatusCode;use fastly::{Error, Request, Response};use std::time::{SystemTime, UNIX_EPOCH};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    log_fastly::init_simple("request_logger", log::LevelFilter::Info);    let service_id = std::env::var("FASTLY_SERVICE_ID").unwrap_or("-".to_string());    let since_epoch = SystemTime::now().duration_since(UNIX_EPOCH)?.as_secs();    let client_ip = req        .get_client_ip_addr()        .map(|ip| ip.to_string())        .unwrap_or_else(String::new);    let req_url = req.get_url_str();    let user_agent = req        .get_header("USER_AGENT")        .map(|header| header.to_str())        .transpose()?        .unwrap_or("");    log::info!(        "fastly_service_id: {service_id}, since_epoch: {since_epoch}, client_ip: {client_ip}, request_url: {req_url}, user_agent: {user_agent}"    );    Ok(Response::from_status(StatusCode::OK).with_body("Welcome to Fastly Compute"))}`

Cargo.toml

TOML

`[dependencies]  fastly = "^0.11.0"  log-fastly = "^0.11.0"  log = "^0.4.17"`

[](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#backends)Backends
--------------------------------------------------------------------------------------------------

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#route-requests-to-backends-based-on-url-path-match)Route requests to backends based on URL path match

1. Fastly VCL

`if (req.url.path == "/") {  set req.backend = F_origin_0;} else if (req.url.path ~ "^/other/") {  set req.backend = F_origin_1;} else {  set req.backend = F_origin_2;}`

1. Rust
2. JavaScript
3. Go

`use fastly::http::Method;use fastly::{Error, Request, Response};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    match (req.get_method(), req.get_path()) {        (&Method::GET, "/") => Ok(req.send("backend_one")?),        (&Method::GET, path) if path.starts_with("/other/") => Ok(req.send("backend_two")?),        _ => Ok(req.send("default_backend")?),    }}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#retry-a-request-on-error-using-a-different-backend)Retry a request on error, using a different backend

1. Fastly VCL

`# not achievable for POST requests# because after a restart the body of a POST request will not be preservedsub vcl_recv {  set req.backend = F_Host_1;  if (req.restarts == 1) {    set req.backend = F_Host_2;  }}sub vcl_fetch {   if (req.restarts == 0 && beresp.status >= 500 && beresp.status < 600 && (req.method == "GET" or req.method == "HEAD")) {     restart;   }}`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    let body_bytes = req.take_body_bytes();    req.set_body(body_bytes.as_slice());    let mut beresp = req.send("backend_one")?;    if beresp.get_status().is_server_error() {        let mut retry_req = beresp.take_backend_request().unwrap();        retry_req.set_body(body_bytes);        let beresp_retry = retry_req.send("backend_two")?;        if !beresp_retry.get_status().is_server_error() {            return Ok(beresp_retry);        }    }    Ok(beresp)}`

[](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#responses)Responses
----------------------------------------------------------------------------------------------------

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#build-a-response-from-scratch)Build a response from scratch

1. Fastly VCL

`set obj.status = 200;synthetic "Hello world";return(deliver);`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(_req: Request) -> Result<Response, Error> {    let res = Response::from_body("Hello world");    Ok(res)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#build-an-image-response)Build an image response

1. Fastly VCL

`synthetic.base64 "R0lGODlh...=";`

1. Rust
2. JavaScript
3. Go

`use fastly::{mime, Error, Request, Response};#[fastly::main]fn main(_req: Request) -> Result<Response, Error> {    let res = Response::from_body(include_bytes!("fastly.jpg").as_ref())        .with_content_type(mime::IMAGE_JPEG)        .with_header("cache-control", "private, no-store");    Ok(res)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#add-a-header-to-a-response)Add a header to a response

1. Fastly VCL

`# constant valueset resp.http.Some-Header = "someValue";# dynamic valueset resp.http.Set-Cookie = "origin-session=" + var.session + "; HttpOnly";`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    // constant value    let mut res = req.send("example_backend")?;    res.set_header("some-header", "bar");    // dynamic value    let session = String::from("some-session-id");    res.set_header("set-cookie", format!("origin-session={}; HttpOnly", session));    Ok(res)}`

[](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#controlling-the-cache)Controlling the cache
----------------------------------------------------------------------------------------------------------------------------

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#explicitly-set-a-ttl)Explicitly set a TTL

1. Fastly VCL

`set beresp.ttl = 60s;`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    // You can use individual helper methods, like`set_ttl`,    // to modify individual cache override settings.    req.set_ttl(60);    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#force-a-pass)Force a `pass`

1. Fastly VCL

`return(pass);`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    // drop all overrides and force pass    req.set_pass(true);    Ok(req.send("example_backend")?)}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#explicitly-set-stale-while-revalidate)Explicitly set stale-while-revalidate

1. Fastly VCL

`set beresp.stale_while_revalidate = 60s;`

1. Rust
2. JavaScript
3. Go

`use fastly::{Error, Request, Response};#[fastly::main]fn main(mut req: Request) -> Result<Response, Error> {    req.set_stale_while_revalidate(60);    Ok(req.send("example_backend")?)}`

### On this page

* [Boilerplate](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#boilerplate)
* [Naming conventions](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#naming-conventions)
* [Configuration](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#configuration)
  * [Load configuration data from a separate file](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#load-configuration-data-from-a-separate-file)
  * [Load configuration data from a dictionary](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#load-configuration-data-from-a-dictionary)

* [Requests](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#requests)
  * [Add a header to a client request](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#add-a-header-to-a-client-request)
  * [Sort and sanitize a query string](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#sort-and-sanitize-a-query-string)
  * [Extract a query string parameter from the request](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#extract-a-query-string-parameter-from-the-request)
  * [Remove a header from a client request](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#remove-a-header-from-a-client-request)
  * [Modify a request URL path](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#modify-a-request-url-path)
  * [Check for header presence on a client request](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#check-for-header-presence-on-a-client-request)
  * [Check whether a request header value contains a substring](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#check-whether-a-request-header-value-contains-a-substring)
  * [Extract constituent parts of a request](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#extract-constituent-parts-of-a-request)
  * [Identify a client's geolocation information](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#identify-a-clients-geolocation-information)
  * [Send data to a log endpoint](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#send-data-to-a-log-endpoint)

* [Backends](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#backends)
  * [Route requests to backends based on URL path match](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#route-requests-to-backends-based-on-url-path-match)
  * [Retry a request on error, using a different backend](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#retry-a-request-on-error-using-a-different-backend)

* [Responses](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#responses)
  * [Build a response from scratch](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#build-a-response-from-scratch)
  * [Build an image response](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#build-an-image-response)
  * [Add a header to a response](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#add-a-header-to-a-response)

* [Controlling the cache](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#controlling-the-cache)
  * [Explicitly set a TTL](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#explicitly-set-a-ttl)
  * [Force a pass](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#force-a-pass)
  * [Explicitly set stale-while-revalidate](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate/#explicitly-set-stale-while-revalidate)
