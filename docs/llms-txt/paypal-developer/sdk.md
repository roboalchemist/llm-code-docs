# Integrate 3D Secure using Hosted Fields

Enable 3D Secure for advanced credit and debit cards. This integration uses the JavaScript SDK.

If you have PayPal Checkout integration, you don't need to integrate 3D Secure. PayPal handles 3D secure authentication for PayPal Checkout integrations.

## Know before you code

### Important: This JavaScript SDK documentation uses the legacy HostedFields component. If you are integrated with the CardFields component, see [Integrate 3D Secure using Card Fields](/docs/checkout/advanced/customize/3d-secure/sdk) for those integration steps.

To trigger the authentication, pass a contingencies parameter with `3D_SECURE`, `SCA_ALWAYS`, or `SCA_WHEN_REQUIRED` as the value where you submit the advanced credit and debit card payments instance.

`SCA_ALWAYS` and `3D_SECURE` triggers an authentication for every transaction, while `SCA_WHEN_REQUIRED` triggers an authentication only when the regional compliance mandate such as PSD2 is required.

The `3D_SECURE` option is deprecated. For new integrations, trigger authentication for every transaction by passing `SCA_ALWAYS` as the contingencies parameter.

## Update the advanced card fields code

To trigger the authentication, pass a contingencies parameter with `3D_SECURE`, `SCA_ALWAYS`, or `SCA_WHEN_REQUIRED` as the value where you submit the advanced credit and debit card payments instance.

`SCA_ALWAYS` and `3D_SECURE` triggers an authentication for every transaction, while `SCA_WHEN_REQUIRED` triggers an authentication only when the regional compliance mandate such as PSD2 is required.

The `3D_SECURE` option is deprecated. For new integrations, trigger authentication for every transaction by passing `SCA_ALWAYS` as the contingencies parameter.

1. // Check eligibility for advanced credit and debit card payments
2. if(paypal.HostedFields.isEligible()){
3. // render the card fields
4. paypal.HostedFields.render({
5. createOrder:()=>{
6. // add logic to return an order ID from your server
7. },
8. fields:{
9. number:{
10. selector:'#card-number',
11. placeholder:'card number'
12. },
13. cvv:{
14. selector:'#cvv',
15. placeholder:'CVV'
16. },
17. expirationDate:{
18. selector:'#expiration-date',
19. placeholder:'mm/yyyy'
20. }
21. }
22. })
23. }).then(function(hf){
24. document.querySelector('#my-sample-form').addEventListener('submit',(event)=>{
25. event.preventDefault();
26. hf.submit({
27. // Trigger 3D Secure authentication
28. contingencies:['SCA_WHEN_REQUIRED']
29. }).then(function(payload){
30. /** sample payload
31. * {
32. * "orderId": "0BS14434UR665304G",
33. * "liabilityShift":  Possible,
34. * }
35. */
36. // Needed only when 3D Secure contingency applied
37. if(payload.liabilityShift=="POSSIBLE"){
38. // 3D Secure passed successfully
39. }else if(payload.liabilityShift){
40. // Handle buyer confirmed 3D Secure successfully
41. }
42. });
43. });
44. });

## See Also

[Response parameters](/docs/checkout/advanced/customize/3d-secure/response-parameters/)  
Learn more about handling 3D Secure responses.

[Optional](/docs/checkout/advanced/customize/3d-secure/test/)  
Simulate 3D Secure scenarios and responses.