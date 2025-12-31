# Source: https://fly.io/docs/rails/cookbooks/api/Dockerfile1/

\# syntax = docker/dockerfile:1 FROM node:slim AS react RUN npx create-react-app client RUN node \--version \> client/.node-version COPY \<\<-\"EOF\" client/src/App.js import logo from \'./logo.svg\'; import \'./App.css\'; import React,  from \'react\'; function App() : \$\`).join(\', \') ) }); }); return (

![logo](%7Blogo%7D)

); } export default App; EOF RUN cd client; npm run build FROM ruby:slim AS build RUN apt-get update &&\\ apt-get install \--yes build-essential git RUN gem install rails RUN rails new demo \--minimal \--skip-active-record \--api FROM ruby:slim COPY \--from=build /demo /demo COPY \--from=build /usr/local/bundle /usr/local/bundle COPY \--from=react /client/build /demo/public COPY \--from=react /client/.node-version /demo WORKDIR demo RUN bin/rails generate controller Api versions COPY \<\<-\"EOF\" app/controllers/api_controller.rb class ApiController \< ApplicationController def versions render json:  end end EOF ENV RAILS_ENV=production ENV RAILS_SERVE_STATIC_FILES=true EXPOSE 3000 CMD bin/rails server