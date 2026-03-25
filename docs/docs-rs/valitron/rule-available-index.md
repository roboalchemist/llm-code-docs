valitron::rule

# Module available

Source Available on **crate feature `full`** only.

## Re-exports§

`pub use compare::Egt;``pub use compare::Elt;``pub use compare::Gt;``pub use compare::Lt;``pub use confirm::Confirm;``pub use contains::Contains;``pub use email::Email;``pub use end_with::EndsWith;``pub use length::Length;``pub use not::Not;``pub use range::Range;``pub use regex::Regex;``pub use required::Required;``pub use start_with::StartWith;``pub use trim::Trim;`

## Modules§

comparecompare number fieldsconfirmUsual used by password confirm inputcontainsRequire string to contain provided parameter, the parameter support `String`, `&str` or `char`,
and verified data only support `String` or `&'static str` , other types always return false.emailValue must be a valid email address, supported `String`, and other types always return false.end_withRequire string to ends with provided parameter, the parameter support `String`, `&str` or `char`,
and verified data only support `String` or `&'static str` , other types always return false.lengthLength validate rule, support `String`, `Array`, `Vec`, `HashMap`, `BTreeMap`. other types always return false.notReverse existing rulesrangeRange validate rule, support `u8`, `u16`, `u32`, `u64`, `i8`,
`i16`, `i32`, `i64`, `f32`, `f64` and char. other types always return false.regexvalidater value by regex, supported `String`, other types always return false.requiredValue can not be empty, supported `Vec`, `String`, `HashMap`
or `BTreeMap`. other types always return true.start_withRequire string to start with provided parameter, the parameter support `String`, `&str` or `char`,
and verified data only support `String` or `&'static str` , other types always return false.trimModifies a string by leading and trailing whitespace removed,
and this alway return true

## Structs§

MessageError message, it is returned when build-in rules validate fail

## Enums§

MessageKind
