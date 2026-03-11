# Source: https://docs.flux.ai/reference/passive-component-consolidation.md

# Passive Component Consolidation



Optimize your Bill of Materials by consolidating similar passive components into fewer part numbers, reducing procurement complexity and manufacturing costs.

## Overview

The Passive Component Consolidation feature uses AI to analyze your Bill of Materials (BOM) and identify opportunities to simplify passive component selection. By finding components with similar values that can be replaced with a single Manufacturer Part Number (MPN), you can reduce costs through volume discounts, simplify procurement, and streamline manufacturing—all while maintaining circuit functionality.

This feature is particularly valuable during the design-for-manufacturing phase, where optimizing the BOM can lead to significant cost savings in production.

### What It Does

Flux analyzes passive components in your design (resistors, capacitors, and inductors) to find:

- Components with marginally close values that could use the same part
- Groups of components within ±50% value tolerance with the same package code
- Single MPN replacements that can satisfy multiple component requirements
- Cost reduction opportunities through component standardization

## How to Access

You can access Passive Component Consolidation through the context menu:

1. Right-click anywhere on your schematic canvas
2. Navigate to **Flux** → **Passive Components Consolidation**
3. Flux will analyze your BOM and provide recommendations

The feature is located in the "Manufacture" section of the Flux menu, alongside other production-readiness tools like FMEA generation and test plan creation.

## How Flux Analyzes Your BOM

When you run Passive Component Consolidation, Flux performs a comprehensive 6-step analysis:

### 1. Component Identification

Flux extracts all passive components from your design, capturing:
- Designator (e.g., R1, C3, L5)
- Component value (e.g., 10kΩ, 0.1µF, 100nH)
- Package code (e.g., 0603, 0805, 1206)
- Current Manufacturer Part Number (MPN)

### 2. Value and Package Grouping

Components are grouped based on:
- **Value tolerance**: Components within ±50% of each other
- **Package compatibility**: Same package code to ensure footprint compatibility
- **Component type**: Resistors, capacitors, and inductors are analyzed separately

### 3. MPN Analysis

For each group, Flux:
- Checks if all components use the same MPN
- Identifies groups with multiple different MPNs
- Evaluates part availability and specifications

### 4. Single MPN Recommendations

Flux cross-references specifications to find a single MPN that can:
- Replace all components in a group
- Meet or exceed all electrical requirements
- Maintain the same package size
- Provide better availability or cost advantages

### 5. Comparison Table Generation

Results are presented in a clear comparison table showing:
- Original component designators and values
- Current MPNs being used
- Recommended consolidated MPN
- Specification comparison
- Estimated cost impact

### 6. Implementation Guidance

Flux provides:
- Clear recommendations for which components to consolidate
- Justification for each suggested change
- Considerations for voltage ratings and other critical specifications
- Expected benefits from each consolidation

## Example Use Cases

### Example 1: Multiple Resistor Manufacturers

**Before consolidation:**
- R1, R2, R3: 10kΩ ±1%, 0603 → Each from different manufacturers
- Three different MPNs in BOM
- Small quantity orders for each MPN

**After consolidation:**
- R1, R2, R3: 10kΩ ±1%, 0603 → Single manufacturer (e.g., Yageo RC0603FR-0710KL)
- One MPN in BOM
- Volume pricing on larger quantity

**Result:** 15-25% cost reduction through volume discounts

### Example 2: Similar Capacitor Values

**Before consolidation:**
- C1: 0.1µF, 0805, 50V
- C2: 0.12µF, 0805, 50V
- C3: 0.15µF, 0805, 50V
- Three different MPNs

**After consolidation:**
- C1, C2, C3: 0.1µF, 0805, 50V → Single MPN
- Design validated that 0.1µF works for all three locations

**Result:** Simplified BOM, reduced inventory, maintained circuit performance

### Example 3: Pull-up Resistor Standardization

**Before consolidation:**
- R10: 4.7kΩ, 0603
- R11: 5.1kΩ, 0603
- R12: 4.3kΩ, 0603

**After consolidation:**
- R10, R11, R12: 4.7kΩ, 0603 → Single MPN
- All values within acceptable tolerance for pull-up application

**Result:** Three line items reduced to one

## Benefits

### Cost Reduction

- **Volume discounts**: Larger quantities of fewer parts qualify for better pricing
- **Reduced inventory**: Less variety means lower carrying costs
- **Simplified procurement**: Fewer purchase orders and vendor relationships

### Manufacturing Efficiency

- **Fewer pick-and-place stops**: Reduced component variety speeds up assembly
- **Lower setup costs**: Fewer unique parts means less machine configuration time
- **Reduced error risk**: Simpler BOM reduces assembly mistakes

### Supply Chain Advantages

- **Better availability**: Standardizing on common parts improves stock availability
- **Easier sourcing**: Fewer unique parts to source during component shortages
- **Simplified inventory management**: Less warehouse space and tracking overhead

### Design Flexibility

- **Maintained functionality**: All consolidations preserve circuit performance
- **Future design reuse**: Standardized component library across projects
- **Faster future designs**: Pre-approved component list for common values

## Tips for Effective Use

### When to Run Consolidation

- **After initial component selection**: Once you've selected components that meet specifications
- **Before finalizing design**: During design-for-manufacturing review
- **When optimizing costs**: As part of value engineering efforts
- **Before production**: One final check before committing to manufacturing

### Review Recommendations Carefully

- **Verify voltage ratings**: Ensure consolidated parts meet or exceed voltage requirements
- **Check temperature coefficients**: Important for precision circuits
- **Consider tolerance**: Verify ±1% vs ±5% doesn't affect performance
- **Validate power ratings**: Especially critical for resistors

### Best Practices

- **Start with obvious groups**: Begin with clear consolidation opportunities like pull-up resistors
- **Consider availability**: Check that recommended parts are readily available
- **Think long-term**: Choose parts that will be available for product lifetime
- **Document decisions**: Keep notes on why certain consolidations were accepted or rejected
- **Test after changes**: Validate circuit performance after any modifications

### Communication with Team

- **Share recommendations**: Discuss consolidation opportunities with your team
- **Get approval**: Ensure changes are reviewed before implementation
- **Update documentation**: Reflect consolidation decisions in design notes
- **Consider manufacturing input**: Consult with assembly team on part preferences

## Limitations

### Component Scope

- **Passive components only**: Currently analyzes resistors, capacitors, and inductors
- **MPN required**: Components must have Manufacturer Part Numbers assigned
- **Standard packages**: Works best with common package sizes (0402, 0603, 0805, etc.)

### Specification Verification

- **Voltage ratings**: You must verify voltage ratings meet requirements
- **Temperature coefficients**: Important specs must be manually validated
- **Power ratings**: Critical parameters require engineer review
- **Specialized components**: High-precision or specialized parts may not be suitable for consolidation

### Design Considerations

- **Critical circuits**: Precision or safety-critical circuits may need specific parts
- **EMI/EMC requirements**: Consolidation shouldn't compromise electromagnetic compatibility
- **Thermal management**: Ensure consolidated parts handle thermal requirements
- **Mechanical constraints**: Verify physical dimensions work in all locations

### User Approval Required

- **Not automatic**: All changes require your explicit approval
- **Engineering judgment**: You must validate technical suitability
- **Performance validation**: Testing recommended after consolidation
- **Documentation updates**: You're responsible for updating design documentation

## Related Features

Enhance your manufacturing workflow with these complementary features:

- [Flux](https://docs.flux.ai/flux/reference/copilot) - Learn about all AI-powered design assistance capabilities
- [AI Testing & Debugging](https://docs.flux.ai/flux/tutorials/ai-testing-debugging) - Generate FMEA reports and test plans for manufacturing readiness
- [AI Design Reviews](https://docs.flux.ai/flux/tutorials/ai-design-reviews) - Validate design decisions before production
- [BOM Export](https://docs.flux.ai/flux/reference/gerber-export) - Export optimized BOM for manufacturing
- [Getting Started with Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Master Flux fundamentals

## Frequently Asked Questions

### Can I consolidate active components?

Currently, Passive Component Consolidation focuses exclusively on resistors, capacitors, and inductors. Active components like ICs, transistors, and diodes have more complex specifications that require individual selection.

### Will consolidation affect circuit performance?

Flux only suggests consolidations within ±50% value tolerance and same package size. However, you should always verify that suggested changes maintain circuit functionality, especially for precision or timing-critical circuits.

### How do I accept or reject recommendations?

Flux presents recommendations in the chat interface. You can review each suggestion and choose to accept or decline. Changes are only made to your design with your explicit approval.

### Can I undo consolidation changes?

Yes, all Flux actions can be undone using the standard undo functionality (Ctrl+Z) or through your project's version history.

### Does this work with custom components?

The feature works best when components have MPNs assigned. For custom components or those without MPNs, consolidation recommendations may be limited.

### How much cost savings can I expect?

Savings vary based on your design, but typical consolidation efforts can reduce BOM costs by 10-30% through volume discounts and simplified procurement. The largest savings come from designs with many similar passive components.

## Next Steps

Now that you understand Passive Component Consolidation, explore these related topics:

- Learn how to [generate comprehensive test plans](https://docs.flux.ai/flux/tutorials/ai-testing-debugging) for your design
- Discover [AI-powered design reviews](https://docs.flux.ai/flux/tutorials/ai-design-reviews) to catch issues early
- Master [Flux's other tools](https://docs.flux.ai/flux/reference/copilot) for faster PCB design
- Explore [BOM optimization strategies](https://docs.flux.ai/flux/tutorials/copilot-use-cases) for cost-effective manufacturing
