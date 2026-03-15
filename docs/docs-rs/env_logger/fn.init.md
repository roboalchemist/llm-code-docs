env_logger
# Function init 
Source 

```
pub fn init()
```

##### Examples found in repository?
examples/syslog_friendly_format.rs (line 22)

```
3fn main() {
4    match std::env::var("RUST_LOG_STYLE") {
5        Ok(s) if s == "SYSTEMD" => env_logger::builder()
6            .format(|buf, record| {
7                writeln!(
8                    buf,
9                    "<{}>{}: {}",
10                    match record.level() {
11                        log::Level::Error => 3,
12                        log::Level::Warn => 4,
13                        log::Level::Info => 6,
14                        log::Level::Debug => 7,
15                        log::Level::Trace => 7,
16                    },
17                    record.target(),
18                    record.args()
19                )
20            })
21            .init(),
22        _ => env_logger::init(),
23    };
24}
```