## Setting up the environment
This jekyll blog runs on ruby version 2.7.0. In order to get things up and running one should:
 1. Clone this repository 
 2. [install rbenv](https://github.com/rbenv/rbenv#installation) and set the local version of ruby to 2.7.0
 2. [Install bundler](https://bundler.io/) just do `$ gem install bundler`
 3. Then `$ bundle install` will generate the ruby virtual environment
 
 Call jekyll through bundler, for example to serve the site locally do
 ```zsh
> bundle exec jekyll serve
```

## Todo
 - remove jagged edges
 - enable comments
 - see if you can fix font-size of titles
