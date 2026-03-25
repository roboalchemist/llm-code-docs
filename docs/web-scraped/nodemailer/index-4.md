# Source: https://ethereal.email/

Title: Ethereal Email

URL Source: https://ethereal.email/

Markdown Content:
This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://ethereal.email/%7B%7B%20revealButtonHref%20%7D%7D)

// Use at least Nodemailer v4.1.0
const nodemailer=require('nodemailer');

// Generate SMTP service account from ethereal.email
nodemailer.createTestAccount((err,account)=>{
if(err){
console.error('Failed to create a testing account. '+err.message);
return process.exit(1);
}

console.log('Credentials obtained, sending message...');

// Create a SMTP transporter object
let transporter=nodemailer.createTransport({
host: account.smtp.host,
port: account.smtp.port,
secure: account.smtp.secure,
auth: {
user: account.user,
pass: account.pass
}
});

// Message object
let message={
from: 'Sender Name <sender@example.com>',
to: 'Recipient <recipient@example.com>',
subject: 'Nodemailer is unicode friendly ✔',
text: 'Hello to myself!',
html: '<p><b>Hello</b> to myself!</p>'
};

transporter.sendMail(message,(err,info)=>{
if(err){
console.log('Error occurred. '+err.message);
return process.exit(1);
}

console.log('Message sent: %s',info.messageId);
// Preview only available when sending through an Ethereal account
console.log('Preview URL: %s',nodemailer.getTestMessageUrl(info));
});
});
