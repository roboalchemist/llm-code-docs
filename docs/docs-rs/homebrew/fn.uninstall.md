homebrew

# Function uninstall

Source

```
pub fn uninstall(name: &str) -> Result<String>
```

##### Examples found in repository?

examples/install.rs (line 22)

```
4fn main() {
5    // 更新
6    // let out = brew::update().unwrap();
7    brew::update_spawn().unwrap();
8
9    // 下载
10    // let out = brew::install("gotop").unwrap();
11    brew::install_spawn("gotop").unwrap();
12
13    // 升级
14    // let out = brew::upgrade("gotop").unwrap();
15    brew::upgrade_spawn("gotop").unwrap();
16
17    // 重新下载
18    // let out = brew::reinstall("gtop").unwrap();
19    brew::reinstall_spawn("gtop").unwrap();
20
21    // 卸载
22    let out = brew::uninstall("gotop").unwrap();
23    println!("{out}");
24}
```
