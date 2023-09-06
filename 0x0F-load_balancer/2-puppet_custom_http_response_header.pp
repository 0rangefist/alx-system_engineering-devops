# Puppet config for nginx server

# make sure package repos are up to date
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
}

# install nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

# start the service
service { 'nginx':
  ensure => running,
  enable => true,
}

# add config file with custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
  listen 80 default_server;

  server_name _;
 
  add_header X-Served-By $hostname;

  root /var/www/html;
  index index.html index.nginx-debian.html;

  location / {
    # First attempt to serve request as file, then
    # as directory, then fall back to displaying a 404.
    try_files $uri $uri/ =404;
  }
}
',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
