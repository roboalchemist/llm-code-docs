# Source: https://doc.keepnetlabs.com/next-generation-product/platform/quishing-simulator/settings/excluding-ip-address.md

# Excluding IP Address

The **Exclude** **IP** **Address** feature is designed to prevent false positive reporting due to security applications that analyze the links in the email in cooperation. It is designed as an alternative option to prevent false positive reporting. The permanent solution is to allow list SMTP IP addresses of the platform to prevent false positive reporting but sometimes admins are not able to configure it on security applications.

You can add the individual IPv4/IPv6 addresses or ranges of IPv4/IPv6 addresses to prevent false positive reporting.

## **How to exclude an IP address**

The following steps explain how to add Individual IP Addresses, range of IP addresses or Batch IP Addresses to exclude from reporting.

### **Add Individual IP Addresses**

* Go to **Quishing Simulator > Settings > Exclude IP addresses** menu.
* You can add individual IPv4/IPv6 addresses using the following example format.
  * 192.168.1.1
  * 192.168.1.1/32
  * 2001:0db8:85a3:0000:0000:8a2e:0370:7334
  * 2001:0db8:85a3:0000:0000:8a2e:0370:7334/128
* Click the **Save** **Changes** button.

### Add a Range of IP Addresses

* Go to **Quishing Simulator > Settings > Exclude IP addresses** menu.
* You can add a range of IPv4/IPv6 addresses using the following example format.
  * 192.168.1.1/24
  * 2001:0db8:85a3:0000:0000:8a2e:0370:7334/124
* Click the **Save Changes** button.

### **Add Batch IP Addresses**

* Go to **Quishing Simulator > Settings > Exclude IP addresses** menu.
* You can add IPv4/IPv6 addresses by using the batch option with the following example format.
  * 192.168.1.1/24
  * 192.168.1.1/32
  * 192.168.1.1
  * 2001:0db8:85a3:0000:0000:8a2e:0370:7334/124
  * 2001:0db8:85a3:0000:0000:8a2e:0370:7334/128
  * 2001:0db8:85a3:0000:0000:8a2e:0370:7334
* Click the **Save Changes** button.

{% hint style="info" %}
Please make sure that IP addresses are separated by a line break or comma.
{% endhint %}

## **FAQ**

### **Q: After I added the IP address, will the platform exclude any data that is received from the added IP address for previous reports?**

A: Yes, after adding the IP addresses, the platform will exclude any data related to IP addresses for previous and future reports.

### **Q: After I removed the IP address, will the platform restore the excluded previous data that is received from the added IP address to the reports?**

A: Yes, after removing the IP addresses, the platform will restore the excluded data related to IP addresses to all reports back.
