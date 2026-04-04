# Source: https://docs.flux.ai/reference/reference-inspector-properties.md

# Properties

Parts typically carry additional metadata like designator, value, part number, etc. The properties menu allows users to load this type of information for each part. To edit a property, click to select the target element and the "Properties" menu will appear on the right-side panel.

![](https://uploads.developerhub.io/prod/86Yw/57qu0dicyvx9zsv42inbj2lciu38jbq0ecybss0nd4z09qgrgh1eva80bvcs26f5.png)

If the property you need to modify is already in the list, type the new value in the text box. Otherwise, click the "Edit" button to create a new property. 

![Editing a part's properties](https://uploads.developerhub.io/prod/86Yw/fmjb4c3mz2r5jrkzuvddilbmn20i086jm78slhsa3vea7b63dm4dgrj0dlhyz0b6.gif)

## Visibility

Most properties will be hidden from the schematic canvas by default. To make them visible:

1. Select the part you'd like to make the property visible.
2. Open the "Inspector" menu on the right and scroll down to "Properties".
3. Click on the eye-like icon to show or hide the property.

## Formulas

You can also use a formula to calculate a value by adding the "=" sign. For example, if you type "=10*13", the result will be a value of 130.

## Special Properties

Some properties have additional functions in Flux. Modifying these properties configures specific behaviors in the app.

### BoM Management

These properties allow you to configure your bill of materials (BoM) and the corresponding email notifications. Learn more about these properties in this [tutorial.](https://docs.flux.ai/flux/tutorials/components-procurement)

![](https://uploads.developerhub.io/prod/86Yw/v00pcf7rz9aackjuolh5o5pb4ei53gh5p62almzjwphzpl2nh83ofctnr03gtb0x.png)

#### Property: Exclude from BoM

- **Applicable** **to**: elements
- **Use case:** Components with this property will be removed from the Bill of Materials.

#### Property: Manufacturer Part Number

- **Applicable to**: elements
- **Use case:** Flux uses the information in this property to search for availability across suppliers. Learn more [here.](https://docs.flux.ai/flux/reference/reference-inspector-pricing-and-availability)

#### Property: Preferred Distributors

- **Applicable to:** Project or Element
- **Use case:** Sets the distributor from which to look for pricing and availability. We currently support DigiKey, LCSC and Mouser. 

#### Property: Manufacturing Quantity Target

- **Applicable to:** projects
- **Use case:**  Sets the number of boards to be manufactured. This will be used in email alerts to check the availability of parts.

#### Property: Price Change Threshold

- **Applicable to:** projects and elements
- **Unit**: %
- **Use case:** Sets the minimum change threshold for pricing alerts.

#### Property: Lead Time Change Threshold

- **Applicable** **to**: Project or Element
- **Unit**: %
- **Use** **case**:  Sets the percentage that the lead time must change since the last notification for it to be included in the next notification email.

### PCB Layout Management

#### Property: Exclude from PCB

- **Applicable** **to**:  Element
- **Use** **case**: Components with this property will be excluded from the PCB layout.

### High-Speed Routing

These properties configure impedance matching and length tuning capabilities. [Learn more.](https://docs.flux.ai/flux/tutorials/advanced-routing)

**Applicable properties: Bus Type, Bus Group, Pair Role, Controlled Impedance Pair, Controlled Impedance, Controlled Impedance Tolerance, PN Skew Max, Pin Delay and Pair to Pair Skew Max**

- **Applicable to**: Element
- **Use case:** Defines the use of impedance control and differential pair routing. [Learn more.](https://docs.flux.ai/flux/reference/impedance-control#manual--setup)

### Symbol Configuration

These properties configure how the pins will be aligned with the symbol. _Remember that you need to [publish the part to the library](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library) and place it on a project in order to see its symbol._

![](https://uploads.developerhub.io/prod/86Yw/nb2kcogxvsj2coizj5uuopva3xgwprzrynawv2fvzyc8la8v6dyf477csr62zn5q.png)

#### Property: Pin Number

- **Applicable** **to**: Terminals
- **Use** **case**: Defines the pin number of said terminal. The assigned pin number will be assigned in the PCB editor as well.

#### Property: Pin Orientation

- **Applicable** **to**: Terminals
- **Use** **case**: Defines the pin orientation in the symbol. For example `Pin Orientation = left` locates the target pin on the left side of the symbol, `Pin Orientation = right` locates the target pin on the right side of the symbol,

#### Property: Pin Group

- **Applicable** **to**: Terminals
- **Use** **case**:  Terminals with the same Pin Group property will be grouped closer together in the symbol. If a terminal's Pin Group property is left empty, they will not be grouped in the final symbol, and will have a larger gap between them.

#### Property: Section

- **Applicable** **to**: Terminals
- **Use** **case**: Terminals with the same Section property will be located in a specific section in the symbol, labeled the same as the Section property. If a part has multiple sections, each will be labeled accordingly and they will be separated with horizontal dividers.

#### Property: Terminal Order

- **Applicable to**: Terminals in parts with _default_ symbol
- **Use** **case**: Defines the pin position in the default symbol. For example, in a 4 pin symbol, `Terminal Order = 1` is the top left pin in the symbol, `Terminal Order = 2` is the bottom left pin, `Terminal Order = 3` is the top right pin and `Terminal Order = 4` is the bottom right pin.

#### Property: Symbol Pin Position

- **Applicable** **to**: Terminals in parts with _custom_ symbol
- **Use** **case**: Defines the position of the pin in a custom symbol. To learn more about how to configure a custom symbol, check out this [tutorial](https://docs.flux.ai/flux/tutorials/tutorial-creating-a-part-from-scratch#2--creating-a-symbol)

#### Property: Sub-symbol Designator Suffix

- **Applicable** **to**: Terminals in parts with _parametric_ symbols
- **Use** **case**: Splits the symbol into multiple parts, each with its own suffix To learn more about how to configure a multi-part symbol, check out this [tutorial.](https://docs.flux.ai/flux/tutorials/working-with-symbols#multi-part-symbols)

### Impedance Control

Learn more about impedance control in this [tutorial](https://docs.flux.ai/flux/tutorials/advanced-routing)

#### Property: Part type

- **Applicable** to**:** Parts
- **Use** **case:** Selecting one of the following part types, automatically configures impedance control for the appropriate pins. Works with part types USB A, USB B, USB C, HDMI, PCIe x1, PCIe x2, PCIe x4, PCIe x8, PCIe x16, Ethernet

### Licenses

Consider adding a license property when sharing or making your project public.

#### Property: License

- **Applicable** **to**: Any project or part
- **Use** **case**: Defines the type of license that applies to the project or part. Any license can be added, but Flux come preloaded with a few options:
    - [http://solderpad.org/licenses/SHL-2.1/](http://solderpad.org/licenses/SHL-2.1/)
    - [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
    - [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)
    - [https://ohwr.org/project/cernohl/wikis/home](https://ohwr.org/project/cernohl/wikis/home)
    - [https://tapr.org/the-tapr-open-hardware-license/](https://tapr.org/the-tapr-open-hardware-license/)