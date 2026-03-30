homebrew

# Function info_all

Source

```
pub fn info_all() -> Result<Package>
```

##### Examples found in repository?

examples/info_all.rs (line 8)

```
7fn main() {
8    let pkg = brew::info_all().unwrap();
9    // println!("Formula package total:\t {}", pkg.formulae().len());
10    let mut formula_count = 0;
11    for p in pkg.formulae().iter() {
12        if p.is_installed() {
13            formula_count += 1;
14        }
15    }
16    println!("Formula package total: {} installed:\t {formula_count}", pkg.formulae().len());
17
18    let mut cask_count = 0;
19    for cask in pkg.casks().iter() {
20        if cask.is_installed() {
21            cask_count += 1;
22        }
23    }
24    println!("Cask package total: {} installed:\t {cask_count}", pkg.casks().len());
25}
```
