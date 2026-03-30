cargo::ops

# Struct ReportTimingsOptions

Source

```
pub struct ReportTimingsOptions<'gctx> {
    pub open_result: bool,
    pub gctx: &'gctx GlobalContext,
    pub id: Option<RunId>,
}
```

## Fields§

§`open_result: bool`

Whether to attempt to open the browser after the report is generated
§`gctx: &'gctx GlobalContext`§`id: Option<RunId>`

## Auto Trait Implementations§

§

### impl<'gctx> Freeze for ReportTimingsOptions<'gctx>
