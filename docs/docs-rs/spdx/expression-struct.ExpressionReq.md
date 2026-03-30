spdx::expression
# Struct ExpressionReq 
Source 

```
pub struct ExpressionReq {
    pub req: LicenseReq,
    pub span: Range<u32>,
}
```

## Fields§
§`req: LicenseReq`

The license requirement
§`span: Range<u32>`

The span in the original license expression string containing the requirement

## Trait Implementations§