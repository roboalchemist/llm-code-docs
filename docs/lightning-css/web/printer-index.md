lightningcss

# Module printer

Source

## Structs§

PrinterA `Printer` represents a destination to output serialized CSS, as used in
the ToCss trait. It can wrap any destination that
implements std::fmt::Write, such as a String.PrinterOptionsOptions that control how CSS is serialized to a string.PseudoClassesA mapping of user action pseudo classes to replace with class names.
