# Source: https://gpiozero.readthedocs.io/en/stable/changelog.html

Title: 26. Changelog — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/changelog.html

Markdown Content:
26.1. Release 2.0.1 (2024-02-15)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-2-0-1-2024-02-15 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

*   Fixed Python 3.12 compatibility, and clarify that 3.9 is the lowest supported version in our CI configuration ([#1113](https://github.com/gpiozero/gpiozero/issues/1113))

26.2. Release 2.0 (2023-09-12)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-2-0-2023-09-12 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

*   Removed Python 2.x support; many thanks to Fangchen Li for a substantial amount of work on this! ([#799](https://github.com/gpiozero/gpiozero/issues/799)[#896](https://github.com/gpiozero/gpiozero/issues/896))

*   Removed RPIO pin implementation

*   Made [`gpiozero.pins.lgpio.LGPIOFactory`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.pins.lgpio.LGPIOFactory "gpiozero.pins.lgpio.LGPIOFactory") the default factory; the former default, [`gpiozero.pins.rpigpio.RPiGPIOFactory`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.pins.rpigpio.RPiGPIOFactory "gpiozero.pins.rpigpio.RPiGPIOFactory"), is now the second place preference

*   Added [Backwards Compatibility](https://gpiozero.readthedocs.io/en/stable/compat.html) chapter

*   Added **pintest** utility

*   Added Raspberry Pi 5 board data

26.3. Release 1.6.2 (2021-03-18)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-6-2-2021-03-18 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

*   Correct docs referring to 1.6.0 as the last version supporting Python 2

Warning

This is the last release to support Python 2

26.4. Release 1.6.1 (2021-03-17)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-6-1-2021-03-17 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

*   Fix missing font files for 7-segment displays

26.5. Release 1.6.0 (2021-03-14)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-6-0-2021-03-14 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

*   Added [`RotaryEncoder`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder "gpiozero.RotaryEncoder") class (thanks to Paulo Mateus) ([#482](https://github.com/gpiozero/gpiozero/issues/482), [#928](https://github.com/gpiozero/gpiozero/issues/928))

*   Added support for multi-segment character displays with [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay") and [`LEDMultiCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDMultiCharDisplay "gpiozero.LEDMultiCharDisplay") along with “font” support using [`LEDCharFont`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharFont "gpiozero.LEDCharFont") (thanks to Martin O’Hanlon) ([#357](https://github.com/gpiozero/gpiozero/issues/357), [#485](https://github.com/gpiozero/gpiozero/issues/485), [#488](https://github.com/gpiozero/gpiozero/issues/488), [#493](https://github.com/gpiozero/gpiozero/issues/493), [#930](https://github.com/gpiozero/gpiozero/issues/930))

*   Added [`Pibrella`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella "gpiozero.Pibrella") class (thanks to Carl Monk) ([#773](https://github.com/gpiozero/gpiozero/issues/773), [#798](https://github.com/gpiozero/gpiozero/issues/798))

*   Added [`TrafficpHat`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficpHat "gpiozero.TrafficpHat") class (thanks to Ryan Walmsley) ([#845](https://github.com/gpiozero/gpiozero/issues/845), [#846](https://github.com/gpiozero/gpiozero/issues/846))

*   Added support for the [lgpio](http://abyz.me.uk/lg/py_lgpio.html) library as a pin factory ([`LGPIOFactory`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.pins.lgpio.LGPIOFactory "gpiozero.pins.lgpio.LGPIOFactory")) (thanks to Joan for lg) ([#927](https://github.com/gpiozero/gpiozero/issues/927))

*   Allow [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") to pass [`pin_factory`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.pin_factory "gpiozero.Device.pin_factory") to its child [`OutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice "gpiozero.OutputDevice") objects (thanks to Yisrael Dov Lebow) ([#792](https://github.com/gpiozero/gpiozero/issues/792))

*   Small SPI exception fix (thanks to Maksim Levental) ([#762](https://github.com/gpiozero/gpiozero/issues/762))

*   Warn users when using default pin factory for Servos and Distance Sensors (thanks to Sofiia Kosovan and Daniele Procida at the EuroPython sprints) ([#780](https://github.com/gpiozero/gpiozero/issues/780), [#781](https://github.com/gpiozero/gpiozero/issues/781))

*   Added [`pulse_width`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.pulse_width "gpiozero.Servo.pulse_width") property to [`Servo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo "gpiozero.Servo") (suggested by Daniele Procida at the PyCon UK sprints) ([#795](https://github.com/gpiozero/gpiozero/issues/795), [#797](https://github.com/gpiozero/gpiozero/issues/797))

*   Added event-driven functionality to [internal devices](https://gpiozero.readthedocs.io/en/stable/api_internal.html) ([#941](https://github.com/gpiozero/gpiozero/issues/941))

*   Allowed [`Energenie`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie "gpiozero.Energenie") sockets preserve their state on construction (thanks to Jack Wearden) ([#865](https://github.com/gpiozero/gpiozero/issues/865))

*   Added source tools `scaled_half()` and `scaled_full()`

*   Added complete Pi 4 support to [`NativeFactory`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.pins.native.NativeFactory "gpiozero.pins.native.NativeFactory") (thanks to Andrew Scheller) ([#920](https://github.com/gpiozero/gpiozero/issues/920), [#929](https://github.com/gpiozero/gpiozero/issues/929), [#940](https://github.com/gpiozero/gpiozero/issues/940))

*   Updated add-on boards to use BOARD numbering ([#349](https://github.com/gpiozero/gpiozero/issues/349), [#860](https://github.com/gpiozero/gpiozero/issues/860))

*   Fixed [`ButtonBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard "gpiozero.ButtonBoard") release events ([#761](https://github.com/gpiozero/gpiozero/issues/761))

*   Add ASCII art diagrams to **pinout** for Pi 400 and CM4 ([#932](https://github.com/gpiozero/gpiozero/issues/932))

*   Cleaned up software SPI (thanks to Andrew Scheller and Kyle Morgan) ([#777](https://github.com/gpiozero/gpiozero/issues/777), [#895](https://github.com/gpiozero/gpiozero/issues/895), [#900](https://github.com/gpiozero/gpiozero/issues/900))

*   Added USB3 and Ethernet speed attributes to [`pi_info()`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "gpiozero.pi_info")

*   Various docs updates

26.6. Release 1.5.1 (2019-06-24)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-5-1-2019-06-24 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

*   Added Raspberry Pi 4 data for [`pi_info()`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "gpiozero.pi_info") and **pinout**

*   Minor docs updates

26.7. Release 1.5.0 (2019-02-12)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-5-0-2019-02-12 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

*   Introduced pin event timing to increase accuracy of certain devices such as the HC-SR04 [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor"). ([#664](https://github.com/gpiozero/gpiozero/issues/664), [#665](https://github.com/gpiozero/gpiozero/issues/665))

*   Further improvements to [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor") (ignoring missed edges). ([#719](https://github.com/gpiozero/gpiozero/issues/719))

*   Allow `source` to take a device object as well as `values` or other `values`. See [Source/Values](https://gpiozero.readthedocs.io/en/stable/source_values.html). ([#640](https://github.com/gpiozero/gpiozero/issues/640))

*   Added internal device classes [`LoadAverage`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage "gpiozero.LoadAverage") and [`DiskUsage`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage "gpiozero.DiskUsage") (thanks to Jeevan M R for the latter). ([#532](https://github.com/gpiozero/gpiozero/issues/532), [#714](https://github.com/gpiozero/gpiozero/issues/714))

*   Added support for [colorzero](https://colorzero.readthedocs.io/en/stable) with [`RGBLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED "gpiozero.RGBLED") (this adds a new dependency). ([#655](https://github.com/gpiozero/gpiozero/issues/655))

*   Added [`TonalBuzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "gpiozero.TonalBuzzer") with [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") API for specifying frequencies raw or via MIDI or musical notes. ([#681](https://github.com/gpiozero/gpiozero/issues/681), [#717](https://github.com/gpiozero/gpiozero/issues/717))

*   Added [`PiHutXmasTree`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiHutXmasTree "gpiozero.PiHutXmasTree"). ([#502](https://github.com/gpiozero/gpiozero/issues/502))

*   Added [`PumpkinPi`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PumpkinPi "gpiozero.PumpkinPi") and [`JamHat`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.JamHat "gpiozero.JamHat") (thanks to Claire Pollard). ([#680](https://github.com/gpiozero/gpiozero/issues/680), [#681](https://github.com/gpiozero/gpiozero/issues/681), [#717](https://github.com/gpiozero/gpiozero/issues/717))

*   Ensured gpiozero can be imported without a valid pin factory set. ([#591](https://github.com/gpiozero/gpiozero/issues/591), [#713](https://github.com/gpiozero/gpiozero/issues/713))

*   Reduced import time by not computing default pin factory at the point of import. ([#675](https://github.com/gpiozero/gpiozero/issues/675), [#722](https://github.com/gpiozero/gpiozero/issues/722))

*   Added support for various pin numbering mechanisms. ([#470](https://github.com/gpiozero/gpiozero/issues/470))

*   [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") instances now use [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") for non-PWM pins.

*   Allow non-PWM use of [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot"). ([#481](https://github.com/gpiozero/gpiozero/issues/481))

*   Added optional `enable` init param to [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor"). ([#366](https://github.com/gpiozero/gpiozero/issues/366))

*   Added `--xyz` option to **pinout** command line tool to open [pinout.xyz](https://pinout.xyz/) in a web browser. ([#604](https://github.com/gpiozero/gpiozero/issues/604))

*   Added 3B+, 3A+ and CM3+ to Pi model data. ([#627](https://github.com/gpiozero/gpiozero/issues/627), [#704](https://github.com/gpiozero/gpiozero/issues/704))

*   Minor improvements to [`Energenie`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie "gpiozero.Energenie"), thanks to Steve Amor. ([#629](https://github.com/gpiozero/gpiozero/issues/629), [#634](https://github.com/gpiozero/gpiozero/issues/634))

*   Allow [`SmoothedInputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice "gpiozero.SmoothedInputDevice"), [`LightSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor "gpiozero.LightSensor") and [`MotionSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor "gpiozero.MotionSensor") to have pull-up configured. ([#652](https://github.com/gpiozero/gpiozero/issues/652))

*   Allow input devices to be pulled up or down externally, thanks to Philippe Muller. ([#593](https://github.com/gpiozero/gpiozero/issues/593), [#658](https://github.com/gpiozero/gpiozero/issues/658))

*   Minor changes to support Python 3.7, thanks to Russel Winder and Rick Ansell. ([#666](https://github.com/gpiozero/gpiozero/issues/666), [#668](https://github.com/gpiozero/gpiozero/issues/668), [#669](https://github.com/gpiozero/gpiozero/issues/669), [#671](https://github.com/gpiozero/gpiozero/issues/671), [#673](https://github.com/gpiozero/gpiozero/issues/673))

*   Added [`zip_values()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.zip_values "gpiozero.tools.zip_values") source tool.

*   Correct row/col numbering logic in [`PinInfo`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo "gpiozero.PinInfo"). ([#674](https://github.com/gpiozero/gpiozero/issues/674))

*   Many additional tests, and other improvements to the test suite.

*   Many documentation corrections, additions and clarifications.

*   Automatic documentation class hierarchy diagram generation.

*   Automatic copyright attribution in source files.

26.8. Release 1.4.1 (2018-02-20)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-4-1-2018-02-20 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

This release is mostly bug-fixes, but a few enhancements have made it in too:

*   Added `curve_left` and `curve_right` parameters to [`Robot.forward()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.forward "gpiozero.Robot.forward") and [`Robot.backward()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.backward "gpiozero.Robot.backward"). ([#306](https://github.com/gpiozero/gpiozero/issues/306) and [#619](https://github.com/gpiozero/gpiozero/issues/619))

*   Fixed [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor") returning incorrect readings after a long pause, and added a lock to ensure multiple distance sensors can operate simultaneously in a single project. ([#584](https://github.com/gpiozero/gpiozero/issues/584), [#595](https://github.com/gpiozero/gpiozero/issues/595), [#617](https://github.com/gpiozero/gpiozero/issues/617), [#618](https://github.com/gpiozero/gpiozero/issues/618))

*   Added support for phase/enable motor drivers with [`PhaseEnableMotor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "gpiozero.PhaseEnableMotor"), [`PhaseEnableRobot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PhaseEnableRobot "gpiozero.PhaseEnableRobot"), and descendants, thanks to Ian Harcombe! ([#386](https://github.com/gpiozero/gpiozero/issues/386))

*   A variety of other minor enhancements, largely thanks to Andrew Scheller! ([#479](https://github.com/gpiozero/gpiozero/issues/479), [#489](https://github.com/gpiozero/gpiozero/issues/489), [#491](https://github.com/gpiozero/gpiozero/issues/491), [#492](https://github.com/gpiozero/gpiozero/issues/492))

26.9. Release 1.4.0 (2017-07-26)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-4-0-2017-07-26 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

*   Pin factory is now [configurable from device constructors](https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-pin-factory) as well as command line. NOTE: this is a backwards incompatible change for manual pin construction but it’s hoped this is (currently) a sufficiently rare use case that this won’t affect too many people and the benefits of the new system warrant such a change, i.e. the ability to use remote pin factories with HAT classes that don’t accept pin assignations ([#279](https://github.com/gpiozero/gpiozero/issues/279))

*   Major work on SPI, primarily to support remote hardware SPI ([#421](https://github.com/gpiozero/gpiozero/issues/421), [#459](https://github.com/gpiozero/gpiozero/issues/459), [#465](https://github.com/gpiozero/gpiozero/issues/465), [#468](https://github.com/gpiozero/gpiozero/issues/468), [#575](https://github.com/gpiozero/gpiozero/issues/575))

*   Pin reservation now works properly between GPIO and SPI devices ([#459](https://github.com/gpiozero/gpiozero/issues/459), [#468](https://github.com/gpiozero/gpiozero/issues/468))

*   Lots of work on the documentation: [source/values chapter](https://gpiozero.readthedocs.io/en/stable/source_values.html), better charts, more recipes, [remote GPIO configuration](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html), mock pins, better PDF output ([#484](https://github.com/gpiozero/gpiozero/issues/484), [#469](https://github.com/gpiozero/gpiozero/issues/469), [#523](https://github.com/gpiozero/gpiozero/issues/523), [#520](https://github.com/gpiozero/gpiozero/issues/520), [#434](https://github.com/gpiozero/gpiozero/issues/434), [#565](https://github.com/gpiozero/gpiozero/issues/565), [#576](https://github.com/gpiozero/gpiozero/issues/576))

*   Support for [`StatusZero`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusZero "gpiozero.StatusZero") and [`StatusBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusBoard "gpiozero.StatusBoard") HATs ([#558](https://github.com/gpiozero/gpiozero/issues/558))

*   Added **pinout** command line tool to provide a simple reference to the GPIO layout and information about the associated Pi ([#497](https://github.com/gpiozero/gpiozero/issues/497), [#504](https://github.com/gpiozero/gpiozero/issues/504)) thanks to Stewart Adcock for the initial work

*   [`pi_info()`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "gpiozero.pi_info") made more lenient for new (unknown) Pi models ([#529](https://github.com/gpiozero/gpiozero/issues/529))

*   Fixed a variety of packaging issues ([#535](https://github.com/gpiozero/gpiozero/issues/535), [#518](https://github.com/gpiozero/gpiozero/issues/518), [#519](https://github.com/gpiozero/gpiozero/issues/519))

*   Improved text in factory fallback warnings ([#572](https://github.com/gpiozero/gpiozero/issues/572))

26.10. Release 1.3.2 (2017-03-03)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-3-2-2017-03-03 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

*   Added new Pi models to stop [`pi_info()`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "gpiozero.pi_info") breaking

*   Fix issue with [`pi_info()`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "gpiozero.pi_info") breaking on unknown Pi models

26.11. Release 1.3.1 (2016-08-31 … later)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-3-1-2016-08-31-later "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Fixed hardware SPI support which Dave broke in 1.3.0. Sorry!

*   Some minor docs changes

26.12. Release 1.3.0 (2016-08-31)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-3-0-2016-08-31 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

*   Added [`ButtonBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard "gpiozero.ButtonBoard") for reading multiple buttons in a single class ([#340](https://github.com/gpiozero/gpiozero/issues/340))

*   Added [`Servo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo "gpiozero.Servo") and [`AngularServo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo "gpiozero.AngularServo") classes for controlling simple servo motors ([#248](https://github.com/gpiozero/gpiozero/issues/248))

*   Lots of work on supporting easier use of internal and third-party pin implementations ([#359](https://github.com/gpiozero/gpiozero/issues/359))

*   [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") now has a proper [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.value "gpiozero.Robot.value") attribute ([#305](https://github.com/gpiozero/gpiozero/issues/305))

*   Added [`CPUTemperature`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature "gpiozero.CPUTemperature") as another demo of “internal” devices ([#294](https://github.com/gpiozero/gpiozero/issues/294))

*   A temporary work-around for an issue with [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor") was included but a full fix is in the works ([#385](https://github.com/gpiozero/gpiozero/issues/385))

*   More work on the documentation ([#320](https://github.com/gpiozero/gpiozero/issues/320), [#295](https://github.com/gpiozero/gpiozero/issues/295), [#289](https://github.com/gpiozero/gpiozero/issues/289), etc.)

Not quite as much as we’d hoped to get done this time, but we’re rushing to make a Raspbian freeze. As always, thanks to the community - your suggestions and PRs have been brilliant and even if we don’t take stuff exactly as is, it’s always great to see your ideas. Onto 1.4!

26.13. Release 1.2.0 (2016-04-10)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-2-0-2016-04-10 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

*   Added [`Energenie`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie "gpiozero.Energenie") class for controlling Energenie plugs ([#69](https://github.com/gpiozero/gpiozero/issues/69))

*   Added [`LineSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor "gpiozero.LineSensor") class for single line-sensors ([#109](https://github.com/gpiozero/gpiozero/issues/109))

*   Added [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor") class for HC-SR04 ultra-sonic sensors ([#114](https://github.com/gpiozero/gpiozero/issues/114))

*   Added [`SnowPi`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.SnowPi "gpiozero.SnowPi") class for the Ryanteck Snow-pi board ([#130](https://github.com/gpiozero/gpiozero/issues/130))

*   Added [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") (and related properties) to [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") ([#115](https://github.com/gpiozero/gpiozero/issues/115))

*   Fixed issues with installing GPIO Zero for python 3 on Raspbian Wheezy releases ([#140](https://github.com/gpiozero/gpiozero/issues/140))

*   Added support for lots of ADC chips (MCP3xxx family) ([#162](https://github.com/gpiozero/gpiozero/issues/162)) - many thanks to pcopa and lurch!

*   Added support for pigpiod as a pin implementation with [`PiGPIOPin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.pins.pigpio.PiGPIOPin "gpiozero.pins.pigpio.PiGPIOPin") ([#180](https://github.com/gpiozero/gpiozero/issues/180))

*   Many refinements to the base classes mean more consistency in composite devices and several bugs squashed ([#164](https://github.com/gpiozero/gpiozero/issues/164), [#175](https://github.com/gpiozero/gpiozero/issues/175), [#182](https://github.com/gpiozero/gpiozero/issues/182), [#189](https://github.com/gpiozero/gpiozero/issues/189), [#193](https://github.com/gpiozero/gpiozero/issues/193), [#229](https://github.com/gpiozero/gpiozero/issues/229))

*   GPIO Zero is now aware of what sort of Pi it’s running on via [`pi_info()`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "gpiozero.pi_info") and has a fairly extensive database of Pi information which it uses to determine when users request impossible things (like pull-down on a pin with a physical pull-up resistor) ([#222](https://github.com/gpiozero/gpiozero/issues/222))

*   The source/values system was enhanced to ensure normal usage doesn’t stress the CPU and lots of utilities were added ([#181](https://github.com/gpiozero/gpiozero/issues/181), [#251](https://github.com/gpiozero/gpiozero/issues/251))

And I’ll just add a note of thanks to the many people in the community who contributed to this release: we’ve had some great PRs, suggestions, and bug reports in this version. Of particular note:

*   Schelto van Doorn was instrumental in adding support for numerous ADC chips

*   Alex Eames generously donated a RasPiO Analog board which was extremely useful in developing the software SPI interface (and testing the ADC support)

*   Andrew Scheller squashed several dozen bugs (usually a day or so after Dave had introduced them ;)

As always, many thanks to the whole community - we look forward to hearing from you more in 1.3!

26.14. Release 1.1.0 (2016-02-08)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-1-0-2016-02-08 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

*   Documentation converted to reST and expanded to include generic classes and several more recipes ([#80](https://github.com/gpiozero/gpiozero/issues/80), [#82](https://github.com/gpiozero/gpiozero/issues/82), [#101](https://github.com/gpiozero/gpiozero/issues/101), [#119](https://github.com/gpiozero/gpiozero/issues/119), [#135](https://github.com/gpiozero/gpiozero/issues/135), [#168](https://github.com/gpiozero/gpiozero/issues/168))

*   New [`CamJamKitRobot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CamJamKitRobot "gpiozero.CamJamKitRobot") class with the pre-defined motor pins for the new CamJam EduKit

*   New [`LEDBarGraph`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph "gpiozero.LEDBarGraph") class (many thanks to Martin O’Hanlon!) ([#126](https://github.com/gpiozero/gpiozero/issues/126), [#176](https://github.com/gpiozero/gpiozero/issues/176))

*   New [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") implementation abstracts out the concept of a GPIO pin paving the way for alternate library support and IO extenders in future ([#141](https://github.com/gpiozero/gpiozero/issues/141))

*   New [`LEDBoard.blink()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.blink "gpiozero.LEDBoard.blink") method which works properly even when background is set to `False` ([#94](https://github.com/gpiozero/gpiozero/issues/94), [#161](https://github.com/gpiozero/gpiozero/issues/161))

*   New [`RGBLED.blink()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.blink "gpiozero.RGBLED.blink") method which implements (rudimentary) color fading too! ([#135](https://github.com/gpiozero/gpiozero/issues/135), [#174](https://github.com/gpiozero/gpiozero/issues/174))

*   New `initial_value` attribute on [`OutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice "gpiozero.OutputDevice") ensures consistent behaviour on construction ([#118](https://github.com/gpiozero/gpiozero/issues/118))

*   New `active_high` attribute on [`PWMOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "gpiozero.PWMOutputDevice") and [`RGBLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED "gpiozero.RGBLED") allows use of common anode devices ([#143](https://github.com/gpiozero/gpiozero/issues/143), [#154](https://github.com/gpiozero/gpiozero/issues/154))

*   Loads of new ADC chips supported (many thanks to GitHub user pcopa!) ([#150](https://github.com/gpiozero/gpiozero/issues/150))

26.15. Release 1.0.0 (2015-11-16)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-1-0-0-2015-11-16 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

*   Debian packaging added ([#44](https://github.com/gpiozero/gpiozero/issues/44))

*   [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") class added ([#58](https://github.com/gpiozero/gpiozero/issues/58))

*   `TemperatureSensor` removed pending further work ([#93](https://github.com/gpiozero/gpiozero/issues/93))

*   [`Buzzer.beep()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.beep "gpiozero.Buzzer.beep") alias method added ([#75](https://github.com/gpiozero/gpiozero/issues/75))

*   [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") PWM devices exposed, and [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") motor devices exposed ([#107](https://github.com/gpiozero/gpiozero/issues/107))

26.16. Release 0.9.0 (2015-10-25)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-9-0-2015-10-25 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Fourth public beta

*   Added source and values properties to all relevant classes ([#76](https://github.com/gpiozero/gpiozero/issues/76))

*   Fix names of parameters in [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") constructor ([#79](https://github.com/gpiozero/gpiozero/issues/79))

*   Added wrappers for LED groups on add-on boards ([#81](https://github.com/gpiozero/gpiozero/issues/81))

26.17. Release 0.8.0 (2015-10-16)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-8-0-2015-10-16 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Third public beta

*   Added generic [`AnalogInputDevice`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice "gpiozero.AnalogInputDevice") class along with specific classes for the [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") and [`MCP3004`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3004 "gpiozero.MCP3004") ([#41](https://github.com/gpiozero/gpiozero/issues/41))

*   Fixed [`DigitalOutputDevice.blink()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.blink "gpiozero.DigitalOutputDevice.blink") ([#57](https://github.com/gpiozero/gpiozero/issues/57))

26.18. Release 0.7.0 (2015-10-09)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-7-0-2015-10-09 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Second public beta

26.19. Release 0.6.0 (2015-09-28)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-6-0-2015-09-28 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

First public beta

26.20. Release 0.5.0 (2015-09-24)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-5-0-2015-09-24 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

26.21. Release 0.4.0 (2015-09-23)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-4-0-2015-09-23 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

26.22. Release 0.3.0 (2015-09-22)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-3-0-2015-09-22 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

26.23. Release 0.2.0 (2015-09-21)[](https://gpiozero.readthedocs.io/en/stable/changelog.html#release-0-2-0-2015-09-21 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Initial release
