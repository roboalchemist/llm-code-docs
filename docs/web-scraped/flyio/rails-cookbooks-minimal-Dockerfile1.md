# Source: https://fly.io/docs/rails/cookbooks/minimal/Dockerfile1/

\# syntax = docker/dockerfile:1 FROM ruby RUN gem install rails RUN rails new demo \--minimal \--skip-active-record COPY \<\<-\"EOF\" /demo/config/routes.rb Rails.application.routes.draw  EOF WORKDIR demo ENV RAILS_ENV=production EXPOSE 3000 CMD bin/rails server