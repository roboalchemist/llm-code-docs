# Source: https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric.md.txt

# FirebasePerformance Framework Reference

# FIRHTTPMetric


    @interface FIRHTTPMetric : NSObject <https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable.html>

Instances of `HTTPMetric` can be used to record HTTP network request information.
- `
  ``
  ``
  `

  ### [-initWithURL:HTTPMethod:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(im)initWithURL:HTTPMethod:)

  `
  `  
  Creates HTTPMetric object for a network request.  

  #### Declaration

  Objective-C  

      - (nullable instancetype)initWithURL:(nonnull NSURL *)URL
                                HTTPMethod:(https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Enums/FIRHTTPMethod.html)httpMethod;

  #### Parameters

  |--------------------|---------------------------------------------|
  | ` `*URL*` `        | The URL for which the metrics are recorded. |
  | ` `*httpMethod*` ` | HTTP method used by the request.            |

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(im)init)

  `
  `  
  Unavailable  
  Use `init(url:httpMethod:)` for Swift and `initWithURL:HTTPMethod:` for Objective-C.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [responseCode](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(py)responseCode)

  `
  `  
  @brief HTTP Response code. Values are greater than 0.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSInteger responseCode;

- `
  ``
  ``
  `

  ### [requestPayloadSize](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(py)requestPayloadSize)

  `
  `  
  @brief Size of the request payload.  

  #### Declaration

  Objective-C  

      @property (nonatomic) long requestPayloadSize;

- `
  ``
  ``
  `

  ### [responsePayloadSize](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(py)responsePayloadSize)

  `
  `  
  @brief Size of the response payload.  

  #### Declaration

  Objective-C  

      @property (nonatomic) long responsePayloadSize;

- `
  ``
  ``
  `

  ### [responseContentType](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(py)responseContentType)

  `
  `  
  @brief HTTP Response content type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *responseContentType;

- `
  ``
  ``
  `

  ### [-start](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(im)start)

  `
  `  
  Marks the start time of the request.  

  #### Declaration

  Objective-C  

      - (void)start;

- `
  ``
  ``
  `

  ### [-stop](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric#/c:objc(cs)FIRHTTPMetric(im)stop)

  `
  `  
  Marks the end time of the response and queues the network request metric on the device for
  transmission. Check the logs if the metric is valid.  

  #### Declaration

  Objective-C  

      - (void)stop;