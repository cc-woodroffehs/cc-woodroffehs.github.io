FROM ruby:2.1-onbuild

RUN gem install jekyll
EXPOSE 4000

ADD https://github.com/cc-woodroffehs/cc-woodroffehs.github.io/archive/master.zip

RUN unzip master.zip && cd cc-woodroffehs.github.io-master/ && jekyll serve
RUN echo "Run jekyll serve in the folder to restar the webserver"
