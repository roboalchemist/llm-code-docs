# Source: https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric.md.txt

# FirebasePerformance Framework Reference

# HTTPMetric

    class HTTPMetric : NSObject, https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable.html

Instances of `HTTPMetric` can be used to record HTTP network request information.
- `
  ``
  ``
  `

  ### [init(url:httpMethod:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(im)initWithURL:HTTPMethod:)

  `
  `  
  Creates HTTPMetric object for a network request.  

  #### Declaration

  Swift  

      init?(url URL: URL, httpMethod: https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Enums/HTTPMethod.html)

  #### Parameters

  |--------------------|---------------------------------------------|
  | ` `*URL*` `        | The URL for which the metrics are recorded. |
  | ` `*httpMethod*` ` | HTTP method used by the request.            |

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(im)init)

  `
  `  
  Unavailable  
  Use [init(url:httpMethod:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric.html#/c:objc(cs)FIRHTTPMetric(im)initWithURL:HTTPMethod:) for Swift and `initWithURL:HTTPMethod:` for Objective-C.
- `
  ``
  ``
  `

  ### [responseCode](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(py)responseCode)

  `
  `  
  @brief HTTP Response code. Values are greater than 0.  

  #### Declaration

  Swift  

      var responseCode: Int { get set }

- `
  ``
  ``
  `

  ### [requestPayloadSize](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(py)requestPayloadSize)

  `
  `  
  @brief Size of the request payload.  

  #### Declaration

  Swift  

      var requestPayloadSize: Int { get set }

- `
  ``
  ``
  `

  ### [responsePayloadSize](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(py)responsePayloadSize)

  `
  `  
  @brief Size of the response payload.  

  #### Declaration

  Swift  

      var responsePayloadSize: Int { get set }

- `
  ``
  ``
  `

  ### [responseContentType](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(py)responseContentType)

  `
  `  
  @brief HTTP Response content type.  

  #### Declaration

  Swift  

      var responseContentType: String? { get set }

- `
  ``
  ``
  `

  ### [start()](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(im)start)

  `
  `  
  Marks the start time of the request.  

  #### Declaration

  Swift  

      func start()

- `
  ``
  ``
  `

  ### [stop()](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric#/c:objc(cs)FIRHTTPMetric(im)stop)

  `
  `  
  Marks the end time of the response and queues the network request metric on the device for
  transmission. Check the logs if the metric is valid.  

  #### Declaration

  Swift  

      func stop()