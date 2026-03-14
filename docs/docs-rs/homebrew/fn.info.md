homebrew

# Function info

Source

```
pub fn info(name: &str) -> Result<Package>
```

##### Examples found in repository?

examples/info.rs (line 26)

```
25fn main() {
26    let pkg = brew::info("wget").unwrap();
27    let json = serde_json::to_string_pretty(&pkg).unwrap();
28    println!("{json}");
29    println!("package name: {}", pkg.name);
30    println!("package is_installed: {}", pkg.is_installed());
31}
```
