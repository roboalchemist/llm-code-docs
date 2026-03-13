stomp 0.11.0 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                stomp-0.11.0
            
        
    

                
                

                    
- 
                        docs.rs
                        

  -  About docs.rs
  -  Badges
  -  Builds
  -  Metadata
  -  Shorthand URLs
  -  Download
  -  Rustdoc JSON
  -  Build queue
  -  Privacy policy
                        

                    
                

                

- 
                        Rust
                        

                            
  - Rust website
                            
  - The Book

                            
  - Standard Library API Reference

                            
  - Rust by Example

                            
  - The Cargo Guide

                            
  - Clippy Documentation
                        

                    
                

                
                
                    
                        
                    

                    
                    
                    
                
            
        
    

    
    
        
            
                

                
                
# 
                    stomp 0.11.0
                    
                

                
                A full STOMP 1.2 client implementation. Allows programs to interact with message queueing services like ActiveMQ and RabbitMQ.

                
                    

                        
                        
- 
                                
                                 Crate
                            
                        

                        
                        
- 
                            
                                
                                 Source
                            
                        

                        
                        
- 
                            
                                
                                 Builds
                            
                        

                        
                        
- 
                            
                                
                                Feature flags
                            
                        
                    

                
            
    

        
            
                
                    

- Links
                        
- 
                                
                                    
                                    
                                        
                                            zslayton/stomp-rs
                                        
                                        

                                         90
                                         29
                                         15

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                mio ^0.3
                
                    *normal*
                    
                
            
        
  - 
                log ^0.3
                
                    *normal*
                    
                
            
        
  - 
                unicode-segmentation ^0.1
                
                    *normal*
                    
                
            
        
  - 
                lifeguard ^0.3
                
                    *normal*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.11.0** (2015-08-24)
        
        
         
        
  - 
            **0.10.2** (2015-07-29)
        
        
         
        
  - 
            **0.10.1** (2015-05-29)
        
        
         
        
  - 
            **0.10.0** (2015-05-27)
        
        
         
        
  - 
            **0.9.0** (2015-04-29)
        
        
         
        
  - 
            **0.8.4** (2015-04-05)
        
        
         
        
  - 
            **0.8.3** (2015-03-29)
        
        
         
        
  - 
            **0.8.2** (2015-03-25)
        
        
         
        
  - 
            **0.8.1** (2015-03-04)
        
        
         
        
  - 
            **0.8.0** (2015-02-08)
        
        
         
        
  - 
            **0.7.0** (2015-02-08)
        
        
         
        
  - 
            **0.6.0** (2015-02-05)
        
        
         
        
  - 
            **0.5.2** (2015-02-01)
        
        
         
        
  - 
            **0.5.1** (2015-01-30)
        
        
         
        
  - 
            **0.5.0** (2015-01-27)
        
        
         
        
  - 
            **0.4.0** (2015-01-25)
        
        
         
        
  - 
            **0.3.7** (2015-01-11)
        
        
         
        
  - 
            **0.3.6** (2015-01-06)
        
        
         
        
  - 
            **0.3.5** (2015-01-06)
        
        
         
        
  - 
            **0.3.4** (2014-12-21)
        
        
         
        
  - 
            **0.3.3** (2014-11-23)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                
                    
                        docs.rs failed to build stomp-0.11.0
                        

                        Please check the
                        build logs for more information.
                        

                        See Builds for ideas on how to fix a failed build,
                        or Metadata for how to configure docs.rs builds.
                        

                        If you believe this is docs.rs' fault, open an issue.
                    
# stomp-rs  

`stomp-rs` provides a full STOMP 1.2 client implementation for the Rust programming language. This allows programs written in Rust to interact with message queueing services like ActiveMQ, RabbitMQ, HornetQ and OpenMQ.

-  Connect

-  Subscribe

-  Send

-  Acknowledge (Auto/Client/ClientIndividual)

-  Transactions

-  Receipts

-  Disconnect

-  Heartbeats

The APIs for `stomp-rs` are not yet stable and are likely to fluctuate before v1.0.

## Examples

### Connect / Subscribe / Send

```
extern crate stomp;
use stomp::frame::Frame;
use stomp::subscription::AckOrNack::Ack;

fn main() {
  
  let destination = "/topic/messages";
  let mut message_count: u64 = 0;

  let mut session = match stomp::session("127.0.0.1", 61613).start() {
      Ok(session) => session,
      Err(error)  => panic!("Could not connect to the server: {}", error)
   };
  
  session.subscription(destination, |frame: &Frame| {
    message_count += 1;
    println!("Received message #{}:\n{}", message_count, frame);
    Ack
  }).start();
  
  session.message(destination, "Animal").send();
  session.message(destination, "Vegetable").send();
  session.message(destination, "Mineral").send();
  
  session.listen(); // Loops infinitely, awaiting messages

  session.disconnect();
}

```

### Session Configuration

```
use stomp::header::header::Header;
use stomp::connection::{HeartBeat, Credentials};
// ...
let mut session = match stomp::session("127.0.0.1", 61613)
  .with(Credentials("sullivan", "m1k4d0"))
  .with(HeartBeat(5000, 2000))
  .with(Header::new("custom-client-id", "hmspna4"))
  .start() {
      Ok(session) => session,
      Err(error)  => panic!("Could not connect to the server: {}", error)
   };

```

### Message Configuration

```
use stomp::header::{Header, SuppressedHeader, ContentType};
// ...
session.message(destination, "Hypoteneuse".as_bytes())
  .with(ContentType("text/plain"))
  .with(Header::new("persistent", "true"))
  .with(SuppressedHeader("content-length")
  .send();

```

### Subscription Configuration

```
use stomp::subscription::AckMode;
use stomp::header::Header;
use stomp::frame::Frame;
// ...
  let id = session.subscription(destination, |frame: &Frame| {
    message_count += 1;
    println!("Received message #{}:\n{}", message_count, frame);
    Ack
  })
  .with(AckMode::Client)
  .with(Header::new("custom-subscription-header", "lozenge"))
  .start();

```

### Transactions

```
match session.begin_transaction() {
  Ok(mut transaction) => {
    transaction.message(destination, "Animal").send();
    transaction.message(destination, "Vegetable").send();
    transaction.message(destination, "Mineral").send();
    transaction.commit();
},
  Err(error)  => panic!("Could not connect to the server: {}", error)
};

```

### Handling RECEIPT frames

If you include a ReceiptHandler in your message, the client will request that the server send a receipt when it has successfully processed the frame.

```
session.message(destination, "text/plain", "Hypoteneuse".as_bytes())
  .with(ReceiptHandler::new(|frame: &Frame| println!("Got a receipt for 'Hypoteneuse'.")))
  .send();

```

### Handling ERROR frames

To handle errors, you can register an error handler

```
session.on_error(|frame: &Frame| {
  panic!("ERROR frame received:\n{}", frame);
});

```

### Manipulating inbound and outbound frames

In some cases, brokers impose rules or restrictions which may make it necessary
directly modify frames in ways that are not conveniently exposed by the API. In such
cases, you can use the `on_before_send` and `on_before_receive` methods to specify a
callback to perform this custom logic prior to the sending or receipt of each frame.

For example:

```
// Require that all NACKs include a header specifying an optional requeue policy
session.on_before_send(|frame: &mut Frame| {
  if frame.command == "NACK" {
    frame.headers.push(Header::new("requeue", "false"));
  }
});

session.on_before_receive(|frame: &mut Frame| {
  if frame.command == "MESSAGE" {
    // Modify the frame
  }
});

```

### Cargo.toml

```
[package]

name = "stomp_test"
version = "0.0.1"
authors = ["your_name_here"]

[[bin]]

name = "stomp_test"

[dependencies.stomp]

stomp = "*"

```

keywords: `Stomp`, `Rust`, `rust-lang`, `rustlang`, `cargo`, `ActiveMQ`, `RabbitMQ`, `HornetQ`, `OpenMQ`, `Message Queue`, `MQ`