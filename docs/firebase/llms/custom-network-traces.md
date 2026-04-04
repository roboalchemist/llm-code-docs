# Source: https://firebase.google.com/docs/perf-mon/custom-network-traces.md.txt

<br />

iOS+AndroidFlutter  

<br />

Performance Monitoringcollects*traces*to help you monitor the performance of your app. A trace is a report of performance data captured between two points in time in your app.

The[network request traces automatically collected byPerformance Monitoring](https://firebase.google.com/docs/perf-mon/network-traces)include most network requests for your app. However, some requests might not be reported or you might use a different library to make network requests. In these cases, you can use thePerformance MonitoringAPI to manually instrument***custom network request traces***. Custom network request traces are only supported for Apple and Android apps.

The default metrics for a custom network request trace are the same as those for the network request traces automatically collected byPerformance Monitoring, specifically response time, response and request payload size, and success rate. Custom network request traces do not support adding custom metrics.

In your code, you define the beginning and the end of a custom network request trace using the APIs provided by thePerformance MonitoringSDK.

Custom network request traces appear in theFirebaseconsole alongside the network requests thatPerformance Monitoringcaptures automatically (in the*Network requests*subtab of the traces table).

## Add custom network request traces

Use thePerformance MonitoringHTTPMetric API ([Swift](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/HTTPMetric)\|[Obj-C](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric)) to add custom network request traces to monitor specific network requests.

To manually instrument custom network requests inPerformance Monitoring, add code similar to the following:  

### Swift

<br />

**Note:**This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.  

    guard let metric = HTTPMetric(url: "https://www.google.com", httpMethod: .get) else { return }

    metric.start()
    guard let url = URL(string: "https://www.google.com") else { return }
    let request: URLRequest = URLRequest(url:url)
    let session = URLSession(configuration: .default)
    let dataTask = session.dataTask(with: request) { (urlData, response, error) in
            if let httpResponse = response as? HTTPURLResponse {
             metric.responseCode = httpResponse.statusCode
            }
            metric.stop()
    }
    dataTask.resume()

### Objective-C

<br />

**Note:**This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.  

    @property (nonatomic) FIRHTTPMetric *metric;

    - (void)beginManualNetworkInstrumentation {
      self.metric =
          [[FIRHttpMetric alloc] initWithURL:[NSURL URLWithString:@"https://www.google.com"]
                                  HTTPMethod:FIRHTTPMethodGET];

      [self.metric start];

      NSURLRequest *request =
          [NSURLRequest requestWithURL:[NSURL URLWithString:@"https://www.google.com"]];
      NSURLConnection *connection = [[NSURLConnection alloc] initWithRequest:request
                                                                    delegate:self];
      [connection resume];
    }

    - (void)connection:(NSURLConnection *)connection
        didReceiveResponse:(NSURLResponse *) response {
      NSHTTPURLResponse* httpResponse = (NSHTTPURLResponse*)response
      self.metric.responseCode = httpResponse.statusCode;
      [self.metric stop];
    }

Custom network request traces also support adding custom attributes ([Swift](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable#setvalue_:forattribute:)\|[Obj-C](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable#-setvalue:forattribute:)) but not custom metrics.

## Next steps

- [Set up alerts](https://firebase.google.com/docs/perf-mon/alerts)for network requests that are degrading the performance of your app. For example, you can configure an email alert for your team if the*response time*for a specific URL pattern exceeds a threshold that you set.