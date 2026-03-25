# Source: https://docs.axonius.com/docs/network-inspector-troubleshooting.md

# Network Inspector Troubleshooting

This topic provides troubleshooting information that can be useful when operating the Axonius Network Inspector device.

## No link through the fiber optic interface

Use the checklist below to resolve any SPAN connection issue on the fiber optic interface.

1. Check and adjust the physical connections:
   * **Hardware match** - Ensure that the fiber transceivers (SFP/SFP+) and cables are compatible at both ends of the connection. Confirm that you are using multimode transceivers with multimode cables, and single-mode transceivers with single-mode cables.
   * **Plug check** - Unplug and re-plug the transceivers to ensure that they are securely seated in the ports.
   * **Cleanness** - Check for and clean any dust from the transceiver and cable ends (using compressed air or any other applicable method).
   * **Cable replacement** - Try replacing the existing fiber cable with a known-good one.
   * **Transceivers replacement** - Use the two Axonius-provided transceivers on both ends (on the Axonius Network Inspector server and the switch).
2. Adjust the configuration:
   * **Fixed speed** - Instead of the auto-negotiate setting, configure a fixed link speed on both the server and the switch.

<Callout icon="❗️">
  Important

  Any changes to the configuration of the Axonius Network Inspector device must be made by an Axonius support engineer during a remote support call.
</Callout>

## Server is not responsive during initial connection

If during the initial connection of the server you are unable to connect to the management interface, or the server does not boot properly, perform the following steps.

<Callout icon="📘" theme="info">
  Note

  It is possible that a hardware component moved during the shipment.
</Callout>

1. Completely power down the server.
2. Disconnect all power supplies (PSUs) and network cables from the back of the unit.
3. Wait at least 30 seconds to allow any residual charge to dissipate.
4. With the power disconnected, carefully reseat the following hardware components, by unplugging each one and plugging it back in firmly:

<Callout icon="❗️">
  Important

  Ensure that each component is reseated in its original slot. Ensure it is fully and securely seated to make proper contact.
</Callout>

* **Power supply unit (PSU)** - Check both the primary and any secondary PSUs.
* **Hard disk drive (HDD)** - Remove any hard disk drive (one or more) by opening its brackets on the front panel, and then reinsert the drive until it clicks into place.
* **PCI Express (PCIe) cards** - Carefully reseat any installed PCI Express cards.

5. Reconnect the power supplies and network cables.
6. Wait two minutes for the iDRAC to fully initialize before powering on the system.
7. Power the system back on and check for a successful boot.

If the server still does not respond after these steps, contact technical support for further assistance.

## Server becomes unresponsive after normal operation

If the server was previously working but is now unresponsive and does not boot or reboot, it is possible that a power issue is preventing it from starting correctly. A full power drain can often resolve this by clearing any residual charge from the system's components.

Since the steps for a power drain can vary slightly between server models, follow the detailed instructions provided on <Anchor label="Dell's official support website" target="_blank" href="https://www.dell.com/support/kbdoc/en-in/000175625/how-do-i-reset-and-drain-power-of-my-dell-poweredge-server">Dell's official support website</Anchor>.