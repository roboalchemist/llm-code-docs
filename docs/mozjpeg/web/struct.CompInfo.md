mozjpeg
# Struct CompInfo 
Source 

```
#[repr(C)]pub struct CompInfo {
    pub component_id: i32,
    pub component_index: i32,
    pub h_samp_factor: i32,
    pub v_samp_factor: i32,
    pub quant_tbl_no: i32,
    pub dc_tbl_no: i32,
    pub ac_tbl_no: i32,
    pub width_in_blocks: u32,
    pub height_in_blocks: u32,
    pub quant_table: *mut JQUANT_TBL,
    /* private fields */
}
```

## Fields§
§`component_id: i32`

identifier for this component (0..255)
§`component_index: i32`

its index in SOF or cinfo->comp_info[]
§`h_samp_factor: i32`

horizontal sampling factor (1..4)
§`v_samp_factor: i32`

vertical sampling factor (1..4)
§`quant_tbl_no: i32`

quantization table selector (0..3)
§`dc_tbl_no: i32`

DC entropy table selector (0..3)

These values may vary between scans.
For compression, they must be supplied by parameter setup;
for decompression, they are read from the SOS marker.
The decompressor output side may not use these variables.
§`ac_tbl_no: i32`

AC entropy table selector (0..3)
§`width_in_blocks: u32`§`height_in_blocks: u32`§`quant_table: *mut JQUANT_TBL`
## Trait Implementations§