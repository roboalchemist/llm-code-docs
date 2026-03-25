homebrew

# Function brew

Source

```
pub fn brew(cmd: &str) -> Result<String>
```

##### Examples found in repository?

examples/brew.rs (line 6)

```
5fn main() {
6    let out = brew::brew("--prefix").unwrap();
7
8    let out1 = Brew::default()
9        .set_cmd("--prefix")
10        .output()
11        .unwrap();
12
13    let mut b2 = Brew::new("--prefix");
14    b2.set_env_no_auto_update();
15    let out2 = b2.output().unwrap();
16
17
18    assert_eq!(out, out1);
19    assert_eq!(out2, out1);
20}
```
