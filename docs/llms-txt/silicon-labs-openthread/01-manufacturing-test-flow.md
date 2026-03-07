# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-overview/01-manufacturing-test-flow.md

# Manufacturing Test Flow

PCB manufacturing testing has two primary objectives: verifying components are placed properly on the boards and verifying functionality of the boards. The overall goal is to maximize test coverage while minimizing test costs.

Manufacturing testing parallels the product lifecycle in that each phase is unique and builds on the previous phase. The following figure shows the traditional product lifecycle and how the different phases of the manufacturing process align with it.

![Product Lifecycle](/mfg-test-overview/0.1/images/sld869-image1.jpg)

Silicon Labs recommends four phases of testing products according to the product lifecycle. Each phase has a purpose and builds off the previous stages.

1. Prototype: The objective of this phase is to fully verify the design on a small number of devices.
2. Characterization: This phase verifies the functionality of the product.

Once the product has been fully characterized, volume testing is next. The two phases of volume manufacturing testing are low-volume and high-volume.

1. Low-volume: This phase contains a subset of the tests run during the characterization phase but with reduced test time and coverage.
2. High-volume: This phase is a much faster test, which allows for ease of test and scalability.

The objective of these manufacturing test phases is to verify that components are placed properly on the boards. The tradeoffs for these phases discussed the next sections are the type of testing, test coverage, data collection, test application, test time, and test cost.

## Phase 1 - Prototype Testing

The first phase of manufacturing test involves initial prototype testing, also known as design verification/validation. This involves product that has gone through its “first build” on a new product introduction (NPI) assembly line. This phase incorporates bench tests with test equipment and usually is not automated. Prototype testing usually involves the engineering design team. Therefore it is time consuming and expensive, but it is very important in verifying the product functionality.

As part of design verification, the product should be tested over the full environmental product requirements including temperature range and voltage supply range. The product should also be subjected to certification and compliance testing, which may include FCC, ETSI, CE, and any applicable protocol-specific compliance testing. Finally, this phase includes general qualification testing, according to JEDEC standards.

Phase I tradeoffs are as follows:

- Volume: First 5-50 boards
- Type of Testing: Bench test with test equipment, not necessarily automated
- Test Coverage: Full design verification
- Data Collection: Not necessarily automated but very detailed
- Test Application: Standalone application
- Test Time: Hours per device (or months for some qualification tests)
- Test Cost: Expensive

## Phase II - Characterization Testing

The second phase of testing in the product lifecycle is characterization testing. The objective of this phase is to verify functionality and repeatability. During this phase, the hardware is manufactured in higher volume (on an NPI line or production assembly line). The assembled product is fully characterized with automated test programs to determine design performance and manufacturability, as well as to collect valuable test data to be used to help with setting test limits in later phases. This phase also provides yield expectations and provides valuable design for manufacturability (DFM) and design for test (DFT) feedback to the engineering design team.

Phase II tradeoffs are as follows:

- Volume: Next 500 to 1,000 boards, depending on the customer
- Type of Testing: Automated with test equipment
- Test Coverage: Full design verification
- Data Collection: Automated, datalogs
- Test Application: Standalone application or application test mode
- Test Time: 10–30 minutes per device
- Test Cost: Expensive

## Phase III - Low Volume Manufacturing Testing

The third phase is low-volume manufacturing. The objective of the volume manufacturing test phases (Phases III and IV) involves the verification of component placement. During this phase, a subset of the characterization testing may be performed. Test data from the characterization stage is used to help determine which tests may be reduced or eliminated. Test time during this stage is more important than the characterization stage because volumes are increased, but is still not crucial. In addition, yield analysis should be done on a continual basis with appropriate feedback provided to the engineering design team.

Phase III tradeoffs are as follows:

- Volume: Next 1,000 boards
- Type of Testing: Automated with subset of test equipment
- Test Coverage: Subset of characterization tests
- Data Collection: Automated, datalogs
- Test Application: Standalone application or application test mode
- Test Time: 2–5 minutes per device
- Test Cost: Moderate

## Phase IV - High Volume Manufacturing Testing

The fourth and final phase is high-volume manufacturing. During this phase, test time is crucial and only minimal testing may be required depending on the customer and the application. A Golden Node application (a known good device that can be used in test for repeatable measurements) can be developed to transmit and receive packets to and from a device under test (DUT) to verify basic functionality. To further reduce test time, a manufacturing library can be used to allow for a test mode within the application itself, thus avoiding multiple programming steps.

Phase IV tradeoffs are as follows:

- Volume: After 1,000 to 2,000 boards
- Type of Testing: Automated with subset of test equipment
- Test Coverage: Minimal, basic functionality
- Data Collection: Minimal data, still automated
- Test Application: Application test mode
- Test Time: Less than 1 minute per device
- Test Cost: Minimal
