lipgloss
# Module security 
Source 
## Constants§
MAX_ANSI_SEQ_LENMaximum number of bytes to scan when parsing a single ANSI escape sequence.
This prevents unbounded scanning in the presence of malformed or unterminated
sequences (e.g., an ESC without a terminating byte), mitigating potential DoS.MAX_DIMENSIONMaximum allowed dimension value for width, height, padding, margin, and tab width.
This prevents excessive memory allocation from malicious or erroneous input.MAX_RENDER_MEMORY_BUDGETMaximum total memory budget for a single render operation (in bytes).
This provides an additional safety net against cumulative allocations.MAX_REPEAT_COUNTMaximum allowed string repetition count to prevent memory exhaustion.
This is used by safe_repeat and other allocation functions.
## Functions§
is_safe_allocationChecks if a memory allocation of the given size would exceed safe limits.safe_repeatSafely repeats a character with bounds checking to prevent memory exhaustion.safe_str_repeatSafely repeats a string with bounds checking to prevent memory exhaustion.validate_dimensionValidates that a dimension value is within safe bounds.validate_tab_widthValidates tab width allowing the special sentinel -1 (keep tabs as-is).