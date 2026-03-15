# KiCad 9.0 PCB Calculator Tools Documentation

## Overview

The KiCad PCB Calculator provides a set of utilities to help you find the values of components or other parameters of a layout.

## Available Calculator Tools

### 1. Regulators

Assists users in determining resistor values for linear and low-dropout voltage regulators. The calculator supports two regulator types:

- **Standard Type**: Calculates output voltage using reference voltage and resistor values
- **3-Terminal Type**: Accounts for quiescent current from the adjust pin

Users input regulator parameters and select which value to calculate.

### 2. RF-Attenuators

Determines resistor values for four attenuator configurations:

- PI attenuator
- Tee attenuator
- Bridged Tee attenuator
- Resistive Splitter

Input requirements include desired attenuation (dB) and impedance values (Ohms).

### 3. E-Series Resistors

Helps to identify combinations of standard E-series resistors that meet a required resistance. Users can exclude unavailable component values from calculations.

### 4. Color-Code

Translates resistor color bands into resistance values. Supports three tolerance levels: 10%, 5%, and ≤2%.

### 5. TransLine (Transmission Lines)

Analyzes frequency-dependent transmission line characteristics across multiple configurations:

- Microstrip lines
- Coplanar waveguides
- Rectangular waveguides
- Coaxial lines
- Coupled microstrip lines
- Stripline
- Twisted pairs

### 6. Via Size

Calculates electrical and thermal properties of plated through-hole vias.

### 7. Track Width

Determines trace width for PCB conductors based on current and acceptable temperature rise, using IPC-2221 standards.

### 8. Electrical Spacing

Provides minimum clearance recommendations between conductors at specified voltages (DC or AC peaks).

### 9. Board Classes

References IPC-6011 and IPC-6012B standards:

**Performance Classes**:

- General (Class 1)
- Dedicated Service (Class 2)
- High Reliability (Class 3)

**PCB Types**:

- Single-sided through multilayer metal core boards with optional blind/buried vias

---

**Documentation Version**: Based on KiCad 9.0.8
**License**: GNU GPL v3 or Creative Commons Attribution 3.0+
