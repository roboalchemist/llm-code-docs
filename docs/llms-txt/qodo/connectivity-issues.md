# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/troubleshooting/connectivity-issues.md

# Connectivity Issues

Use this guide to quickly diagnose connectivity issues with the Qodo IDE Plugin platform.

### **1. Quick Server Connectivity Test**

Run the following `curl` command to verify that your machine can reach the Qodo IDE Plugin server:

```bash
curl -v https://qodo-platform.qodo.ai/health
```

### **2. How to Interpret the Results**

#### **Success**

* Look for these indicators in the response:
  * `HTTP/2 200` or `HTTP/1.1 200 OK`
  * A message similar to:

    ```json
    {"status":"healthy"}
    ```
  * Connection completes without timing out

#### **Example Successful Output:**

```
* Connected to qodo-platform.qodo.ai (203.0.113.1) port 443
* SSL connection using TLSv1.3
> GET /health HTTP/2
< HTTP/2 200
{"status":"healthy"}
```

***

#### **Common Issues and What They Mean**

1. **Cannot reach the server at all**
   * Example output:

     ```
     Failed to connect to qodo-platform.qodo.ai
     ```
   * **Likely Cause:** Local network or firewall blocking access.
2. **Server is reachable but responding with errors**
   * Example output:

     ```
     < HTTP/2 500
     < HTTP/2 503
     ```
   * **Likely Cause:** Our server is experiencing temporary issues.

***

### **3. Windows Users Without curl**

You can run the test using PowerShell:

```powershell
Invoke-WebRequest -Uri https://qodo-platform.qodo.ai/health -Method GET
```

Look for a `200` status code and a `{"status":"healthy"}` response.

***

### 4. Next steps

#### **If you cannot connect at all:**

* Check your internet connection
* Ensure your firewall or VPN allows traffic to `qodo-platform.qodo.ai` over port 443

#### **If you receive 500 or 503 errors:**

* Check our status page: <https://status.qodo.ai/>.

#### **If the issue persists:**

[Contact our support team](https://www.qodo.ai/contact/) or try to [get help from our official Discord Community](https://discord.com/invite/kG35uSHDBc).
