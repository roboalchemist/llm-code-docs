iced
# Module application 
Source 
## Re-exports§
`pub use timed::timed;`
## Modules§
timedAn `Application` that receives an `Instant` in update logic.
## Structs§
ApplicationThe underlying definition and configuration of an iced application.
## Traits§
BootFnThe logic to initialize the `State` of some `Application`.IntoBootThe initial state of some `Application`.ThemeFnThe theme logic of some `Application`.TitleFnThe title logic of some `Application`.UpdateFnThe update logic of some `Application`.ViewFnThe view logic of some `Application`.
## Functions§
applicationCreates an iced `Application` given its boot, update, and view logic.