# Source: https://fly.io/docs/rails/cookbooks/databases/Dockerfile1/

\# syntax = docker/dockerfile:1 FROM ruby:slim as build RUN apt-get update &&\\ apt-get install \--yes build-essential git pkg-config redis RUN gem install rails RUN rails new demo \--css tailwind FROM ruby:slim COPY \--from=build /demo /demo COPY \--from=build /usr/local/bundle /usr/local/bundle WORKDIR demo RUN bin/rails generate model Visitor counter:integer &&\\ bin/rails generate channel counter COPY \<\<-\"EOF\" app/controllers/visitors_controller.rb class VisitorsController \< ApplicationController def counter \@visitor = Visitor.find_or_create_by(id: 1) \@visitor.update! counter: \@visitor.counter.to_i + 1 \@visitor.broadcast_replace_later_to \'counter\', partial: \'visitors/counter\' end end EOF COPY \<\<-\"EOF\" app/views/visitors/counter.html.erb \<%= turbo_stream_from \'counter\' %\>

![The monochrome white Fly.io brandmark on a navy background](https://fly.io/static/images/brand/brandmark-light.svg)

\<%= render \"counter\", visitor: \@visitor %\>

EOF COPY \<\<-\"EOF\" app/views/visitors/\_counter.html.erb \<%= turbo_frame_tag(dom_id visitor) do %\> \<%= visitor.counter.to_i %\> \<% end %\> EOF COPY \<\<-\"EOF\" config/routes.rb Rails.application.routes.draw  EOF ENV RAILS_ENV=production RUN bin/rails assets:precompile RUN bin/rails db:prepare EXPOSE 3000 ENV RAILS_LOG_TO_STDOUT=true ENV RAILS_SERVE_STATIC_FILES=true CMD bin/rails server