# Source: https://stackblitz.com/edit/socketio-base?file=index.js

Title: Socket.IO base project - StackBlitz

URL Source: https://stackblitz.com/edit/socketio-base?file=index.js

Markdown Content:
Socket.IO base project - StackBlitz
===============

[StackBlitz](https://stackblitz.com/)

Fork

Share

[![Image 1](https://avatars.githubusercontent.com/u/13031701)](https://stackblitz.com/@darrachequesne)

Socket.IO base project

Sign in Get started

Project

Search

Ports in use

Settings

Switch to Light Theme

Enter Zen Mode

Open in bolt.new | AI

Project
-------

Download Project

#### Info

[![Image 2](https://avatars.githubusercontent.com/u/13031701)darrachequesne](https://stackblitz.com/@darrachequesne)

### Socket.IO base project

Starter project for Socket.IO

48.5K views 915 forks

#### Files

.stackblitzrc

Rename

Delete

index.html

Rename

Delete

index.js

Rename

Delete

package-lock.json

Rename

Delete

package.json

Rename

Delete

Ask bolt.new

StackBlitz’s AI pair programming assistant

![Image 3: Bolt prompt](https://c.staticblitz.com/assets/pack/media/bolt-prompt-8610f67e9db2a.png)

[](https://x.com/boltdotnew)[](https://github.com/stackblitz/core)[](https://discord.gg/stackblitz)[**Something broken? File a bug!**](https://github.com/stackblitz/webcontainer-core/issues/new)

index.js

Format Document

Split Editor

More Actions…

Close all

Close saved

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

const{readFileSync}=require('fs');

const{createServer}=require('http');

const{Server}=require('socket.io');

const httpServer=createServer((req,res)=>{

if(req.url!=='/'){

res.writeHead(404);

res.end('Not found');

return;

}

//reload the file every time

const content=readFileSync('index.html');

const length=Buffer.byteLength(content);

res.writeHead(200,{

'Content-Type':'text/html',

'Content-Length':length

});

res.end(content);

});

const io=new Server(httpServer,{

//Socket.IO options

});

io.on('connection',socket=>{

console.log(`connect${socket.id}`);

socket.on('disconnect',reason=>{

console.log(`disconnect${socket.id}due to${reason}`);

});

});

httpServer.listen(3000);

Enter to Rename, ⇧Enter to Preview

Terminal

Terminal_1

#### Terminal_1

Close Preview

Booting WebContainer

1.   Booting WebContainer

Create a new project
--------------------

*   Popular
*   Frontend
*   Backend
*   Fullstack
*   Docs, Blogs & Slides
*   Creative
*   Mobile & VR
*   Vanilla
*   Native Languages

[Astro Basics Node.js](https://stackblitz.com/fork/github/withastro/astro/tree/latest/examples/basics?file=README.md&title=Astro%20Starter%20Kit:%20Basics)[Next.js Node.js](https://stackblitz.com/fork/github/stackblitz/starters/tree/main/nextjs?title=Next.js%20Starter&description=The%20React%20framework%20for%20production)[Nuxt Node.js](https://stackblitz.com/fork/github/nuxt/starter/tree/v3-stackblitz)[React TypeScript](https://stackblitz.com/fork/github/vitejs/vite/tree/main/packages/create-vite/template-react-ts?file=index.html&terminal=dev)[Vanilla JavaScript](https://stackblitz.com/fork/github/vitejs/vite/tree/main/packages/create-vite/template-vanilla?file=index.html&terminal=dev)[Vanilla TypeScript](https://stackblitz.com/fork/github/vitejs/vite/tree/main/packages/create-vite/template-vanilla-ts?file=index.html&terminal=dev)[Static HTML/JS/CSS](https://stackblitz.com/fork/github/stackblitz/starters/tree/main/static?title=Static%20Starter&description=HTML/CSS/JS%20Starter&file=script.js,styles.css,index.html&terminalHeight=10)[Node.js Blank project](https://stackblitz.com/fork/github/stackblitz/starters/tree/main/node?title=node.new%20Starter&description=Starter%20project%20for%20Node.js%2C%20a%20JavaScript%20runtime%20built%20on%20Chrome%27s%20V8%20JavaScript%20engine)[Angular TypeScript](https://stackblitz.com/fork/github/stackblitz/starters/tree/main/angular?template=node&title=Angular%20Starter&description=An%20angular-cli%20project%20based%20on%20%40angular%2Fanimations%2C%20%40angular%2Fcommon%2C%20%40angular%2Fcompiler%2C%20%40angular%2Fcore%2C%20%40angular%2Fforms%2C%20%40angular%2Fplatform-browser%2C%20%40angular%2Fplatform-browser-dynamic%2C%20%40angular%2Frouter%2C%20core-js%2C%20rxjs%2C%20tslib%20and%20zone.js)[Vue JavaScript](https://stackblitz.com/fork/github/vitejs/vite/tree/main/packages/create-vite/template-vue?file=index.html&terminal=dev)[WebContainer API Node.js](https://stackblitz.com/fork/github/stackblitz/webcontainer-api-starter)

Publish a package
=================

Are you trying to publish ?

Cancel Confirm

Allow access to localhost resource
==================================

Request to:

More information Method: undefined
Headers:

Warning

Allowing access to your localhost resources can lead to security issues such as unwanted request access or data leaks through your localhost.

- [x] Do not ask me again 

Block Allow

Out of memory error
===================

This browser tab is running out of memory. Free up memory by closing other StackBlitz tabs and then refresh the page.

OK[Learn more](https://developer.stackblitz.com/codeflow/working-in-codeflow-ide#out-of-memory-error)
