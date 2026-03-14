webrtc::api
# Module interceptor_registry 
Source 
## Functions§
configure_nackconfigure_nack will setup everything necessary for handling generating/responding to nack messages.configure_rtcp_reportsconfigure_rtcp_reports will setup everything necessary for generating Sender and Receiver Reportsconfigure_twccconfigure_twcc will setup everything necessary for adding
a TWCC header extension to outgoing RTP packets and generating TWCC reports.configure_twcc_receiver_onlyconfigure_twcc_receiver will setup everything necessary for generating TWCC reports.configure_twcc_sender_onlyconfigure_twcc_sender will setup everything necessary for adding
a TWCC header extension to outgoing RTP packets. This will allow the remote peer to generate TWCC reports.register_default_interceptorsregister_default_interceptors will register some useful interceptors.
If you want to customize which interceptors are loaded, you should copy the
code from this method and remove unwanted interceptors.