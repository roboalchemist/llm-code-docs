homebrew

# Function repository

Source

```
pub fn repository() -> Result<String>
```

##### Examples found in repository?

examples/config.rs (line 24)

```
2fn main() {
3    let cfg = homebrew::config().unwrap();
4    println!("{cfg:#?}");
5
6    let cfg = homebrew::env().unwrap();
7    println!("{cfg:#?}");
8
9    let out = homebrew::env_shell().unwrap();
10    println!("{out}");
11
12    let out = homebrew::prefix().unwrap();
13    println!("{out}");
14
15    let out = homebrew::caskroom().unwrap();
16    println!("{out}");
17
18    let out = homebrew::cellar().unwrap();
19    println!("{out}");
20
21    let out = homebrew::cache().unwrap();
22    println!("{out}");
23
24    let out = homebrew::repository().unwrap();
25    println!("{out}");
26
27}
```
