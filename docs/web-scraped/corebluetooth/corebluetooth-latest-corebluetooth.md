# Source: https://docs.rs/corebluetooth/latest/corebluetooth/

Title: corebluetooth 0.1.0 - Docs.rs

URL Source: https://docs.rs/corebluetooth/latest/corebluetooth/

Markdown Content:
docs.rs failed to build corebluetooth-0.1.0

 Please check the [build logs](https://docs.rs/crate/corebluetooth/latest/builds) for more information.

 See [Builds](https://docs.rs/about/builds) for ideas on how to fix a failed build, or [Metadata](https://docs.rs/about/metadata) for how to configure docs.rs builds.

 If you believe this is docs.rs' fault, [open an issue](https://github.com/rust-lang/docs.rs/issues/new/choose).

corebluetooth
-------------

A safe wrapper for Apple's [CoreBluetooth framework](https://developer.apple.com/documentation/corebluetooth).

This crate provides a safe, delegate-based API for CoreBluetooth. It aims to be a thin wrapper around the underlying framework, while providing a more idiomatic Rust interface. All CoreBluetooth operations are performed on a `dispatch` queue, and results are delivered via a delegate trait that you implement.

For most applications, it is recommended to use the [`corebluetooth-async`](https://docs.rs/crate/corebluetooth-async) crate, which provides a higher-level `async` API on top of this one.

Example
-------

This example shows how to scan for peripherals and print their advertisement data.

```
use corebluetooth::{
    advertisement_data::AdvertisementData,
    central_manager::{CentralManager, CentralManagerDelegate},
    error::Error,
    peripheral::{Peripheral, PeripheralDelegate},
    CBManagerState,
};
use dispatch_executor::MainThreadMarker;
use std::time::SystemTime;

fn main() {
     Delegate-based APIs require a run loop. For this example, we don't start one,
     so this program will start and then exit.
    let mtm = MainThreadMarker::new().unwrap();
    let _manager = CentralManager::main_thread(
        Box::new(Delegate),
        false,         None,          mtm,
    );
}

struct Delegate;

impl CentralManagerDelegate for Delegate {
    fn new_peripheral_delegate(&self) -> Box<dyn PeripheralDelegate> {
        Box::new(PeripheralDelegateImpl)
    }

    fn did_update_state(&self, central: CentralManager) {
        if central.state() == CBManagerState::PoweredOn {
            println!("Bluetooth is powered on, starting scan.");
                        central.scan(None, false, None);
        }
    }

    fn did_discover(
        &self,
        _central: CentralManager,
        peripheral: Peripheral,
        advertisement_data: AdvertisementData,
        rssi: i16,
    ) {
        if let Some(name) = peripheral.name() {
            println!(
                "Discovered peripheral '{}' (RSSI: {}) with advertisement data: {:?}",
                name, rssi, advertisement_data
            );
        }
    }

    fn did_connect(&self, _central: CentralManager, peripheral: Peripheral) {
        println!("Connected to peripheral: {:?}", peripheral.name());
    }

    fn did_fail_to_connect(
        &self,
        _central: CentralManager,
        peripheral: Peripheral,
        error: Error,
    ) {
        println!(
            "Failed to connect to peripheral: {:?}, error: {}",
            peripheral.name(),
            error
        );
    }

    fn did_disconnect(
        &self,
        _central: CentralManager,
        peripheral: Peripheral,
        _timestamp: Option<SystemTime>,
        _is_reconnecting: bool,
        error: Option<Error>,
    ) {
        println!(
            "Disconnected from peripheral: {:?}, error: {:?}",
            peripheral.name(),
            error
        );
    }
}

struct PeripheralDelegateImpl;

impl PeripheralDelegate for PeripheralDelegateImpl {}
```
