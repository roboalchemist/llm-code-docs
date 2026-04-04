# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeCalendarEvent


    @interface FIRVisionBarcodeCalendarEvent : NSObject

A calendar event extracted from a QR code.
- `
  ``
  ``
  `

  ### [eventDescription](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(py)eventDescription)

  `
  `  
  Calendar event description.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *eventDescription;

- `
  ``
  ``
  `

  ### [location](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(py)location)

  `
  `  
  Calendar event location.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *location;

- `
  ``
  ``
  `

  ### [organizer](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(py)organizer)

  `
  `  
  Clendar event organizer.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *organizer;

- `
  ``
  ``
  `

  ### [status](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(py)status)

  `
  `  
  Calendar event status.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *status;

- `
  ``
  ``
  `

  ### [summary](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(py)summary)

  `
  `  
  Calendar event summary.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *summary;

- `
  ``
  ``
  `

  ### [start](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(py)start)

  `
  `  
  Calendar event start date.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSDate *start;

- `
  ``
  ``
  `

  ### [end](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(py)end)

  `
  `  
  Calendar event end date.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSDate *end;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent#/c:objc(cs)FIRVisionBarcodeCalendarEvent(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;