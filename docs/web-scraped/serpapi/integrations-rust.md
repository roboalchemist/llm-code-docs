# Source: https://serpapi.com/integrations/rust

Title: SerpApi: Rust Integration

URL Source: https://serpapi.com/integrations/rust

Markdown Content:
*   ```
// [dependencies]
// serpapi-search-rust="0.1.0"
// tokio = { version = "1", features = ["full"] }

use serpapi_search_rust::serp_api_search::SerpApiSearch;
use std::collections::HashMap;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
  let mut params = HashMap::<String, String>::new();
  params.insert("q".to_string(), "Coffee".to_string());
  params.insert("location".to_string(), "Austin, Texas, United States".to_string());
  params.insert("hl".to_string(), "en".to_string());
  params.insert("gl".to_string(), "us".to_string());
  params.insert("google_domain".to_string(), "google.com".to_string());

  let search = SerpApiSearch::google(params, "secret_api_key".to_string());

  let results = search.json().await?;
  println!("results received");
  println!("--- JSON ---");
  println!(" - results: {}", results);

  print!("ok");
  Ok(())
}
```

SerpApi Search in Rust
----------------------

[![Image 1: CI](https://github.com/serpapi/serpapi-search-rust/actions/workflows/ci.yml/badge.svg)](https://github.com/serpapi/serpapi-search-rust/actions/workflows/ci.yml)[![Image 2: serpapi-search-rust](https://img.shields.io/crates/v/serpapi-search-rust.svg)](https://crates.io/crates/serpapi-search-rust)

This Rust package enables to scrape and parse search results from Google, Bing, Baidu, Yandex, Yahoo, Ebay, Apple, Youtube, Naver, Home depot and more. It's powered by [SerpApi](https://serpapi.com/) which delivered a consistent JSON format accross search engines. SerpApi.com enables to do localized search, leverage advanced search engine features and a lot more... A completed documentation is available at [SerpApi](https://serpapi.com/).

To install in your rust application, update Cargo.toml

```
serpapi-search-rust="0.1.0"
```

Basic application.

```
use serpapi_search_rust::serp_api_search::SerpApiSearch;
use std::collections::HashMap;
use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // read secret api key from environment variable
    // To get the key simply copy/paste from https://serpapi.com/dashboard.
    let api_key = match env::var_os("API_KEY") {
        Some(v) => v.into_string().unwrap(),
        None => panic!("$API_KEY is not set"),
    };

    println!("let's search about coffee on google");
    let mut params = HashMap::<String, String>::new();
    params.insert("q".to_string(), "coffee".to_string());
    params.insert("location".to_string(), "Austin, TX, Texas, United States".to_string());

    // initialize the search engine
    let search = SerpApiSearch::google(params, api_key);

    // search returns a JSON as serde_json::Value which can be accessed like a HashMap.
    println!("waiting...");
    let results = search.json().await?;
    let organic_results = results["organic_results"].as_array().unwrap();
    println!("results received");
    println!("--- JSON ---");
    println!(" - number of organic results: {}", organic_results.len());
    println!(" - organic_results first result description: {}", results["organic_results"][0]["about_this_result"]["source"]["description"]);
    let places = results["local_results"]["places"].as_array().unwrap();
    println!("number of local_results: {}", places.len());
    println!(" - local_results first address: {}", places[0]["address"]);

    // search returns text
    println!("--- HTML search ---");
    let raw = search.html().await?;
    print!(" - raw HTML size {} bytes\n", raw.len());
    print!(" - async search completed with {}\n", results["search_parameters"]["engine"]);

    // // edit the location in the search
    // println!("--- JSON search with a different location ---");
    // params = HashMap::<String, String>::new();
    // params.insert("location".to_string(), "Destin, Florida, United States".to_string());
    // search = SerpApiSearch::google(params, api_key);
    // let results = search.json().await?;
    // println!(">> search_parameters: {}", results["search_parameters"]);
    // let places = results["local_results"]["places"].as_array().unwrap();
    // println!("number of local_results: {}\n", places.len());
    // println!("local_results first address: {}\n", places[0]["address"]);

    print!("ok");
    Ok(())
}
```

To run an example:

```
cargo build --example google_search_example
```

file: (examples/google_search_example.rs)

The keyword google can be replaced by any supported search engine:

*   google
*   baidu
*   bing
*   duckduckgo
*   yahoo
*   yandex
*   ebay
*   youtube
*   walmart
*   home_depot
*   apple_app_store
*   naver

To run test.

```
cargo test
```

For more information how to build a paramaters HashMap see [serpapi.com documentation](https://serpapi.com/search-api)

### Technical features

*   Dynamic JSON decoding using Serde JSON
*   Asyncronous HTTP request handle method using tokio and reqwest
*   Async tests using Tokio

### TODO

*   [ ] more test to close code coverage (each search engine)
*   [ ] add more examples
*   [ ] better documentation

### Free Plan · 250 searches / month

[Get started](https://serpapi.com/users/sign_up?plan=free)

They trust us
-------------

You are in good company. Join them.

![Image 3: Nvidia](https://serpapi.com/assets/they_trust_us/nvidia-f6aef93c646a6c2a270355bdc6f4ef2c3bd2387ba13fe96e1df0f252671047c5.svg)

![Image 4: Shopify](https://serpapi.com/assets/they_trust_us/shopify-3c81ac3bcad10eec68700a6d803fb53bf82b4b86718efd46ada57c251e6881e1.svg)

![Image 5: Perplexity](https://serpapi.com/assets/they_trust_us/perplexity-91ee04700ccfae8810e002b6b9f2fa7fd1b754dc246d58e6c29de45013b48825.svg)

![Image 6: Adobe](https://serpapi.com/assets/they_trust_us/adobe-54213e56d564e8174ec2de6aa5f91907aebadc38215f4c3597d1e9b83cce127a.svg)

![Image 7: Samsung](https://serpapi.com/assets/they_trust_us/samsung-586d5e2accb43c4a87afc4e8a5bcb22ac51c9a610deffc8cc1e678dc7ec41473.svg)

![Image 8: KPMG](https://serpapi.com/assets/they_trust_us/kpmg-6148c3dd449898c254f9734003ae845410af3c5ff89affcc8498cf8335a64d24.svg)

![Image 9: Ahrefs](https://serpapi.com/assets/they_trust_us/ahrefs-d7e94eea8486aa9827442c32cd2bb84c2ccf16f34e465cd8fde9918ac2b08d0b.svg)

![Image 10: Grubhub](https://serpapi.com/assets/they_trust_us/grubhub-412503dc714c1cea29fc6312ce8e6241a840644d39c7d3676e979cbcaedfaaa5.svg)

![Image 11: AI21 Labs](https://serpapi.com/assets/they_trust_us/ai21_labs-99130e54735f2d15b7a8a987851c9c14cfa3f9d5fa1f0dc94d70ac35db517e15.svg)

![Image 12: United Nations](https://serpapi.com/assets/they_trust_us/un-db425e5e8b13851ed1a242c3667ae82af4ce459865fb471e801a5954a444ab75.svg)

![Image 13: Thomson Reuters](https://serpapi.com/assets/they_trust_us/thomson_reuters-737571a18eea2623d86ddd80cf83a9dd8fb56a603c8c03bc294f204ca12fcdd5.svg)

![Image 14: Morgan Stanley](https://serpapi.com/assets/they_trust_us/morgan_stanley-385a9779ff55c01a07d9f6b35b683d4f91b74839e67c399597599cfe40b5b406.svg)

![Image 15: BrightLocal](https://serpapi.com/assets/they_trust_us/bright_local-7f79a54553c8a2c4b4c15c5dbd31a0d1625bcd093737145c303623cbe79e8625.svg)

![Image 16: Experian](https://serpapi.com/assets/they_trust_us/experian-8773285de164ba7496a8912fd50c1aa7b14cbb018b686eb1d6d6609ab508e966.svg)

![Image 17: Uber](https://serpapi.com/assets/they_trust_us/uber-16c024118381073d81895b415fb90891dd7ebdaa7c4b6fb2ba26988ec5f2e84c.svg)
