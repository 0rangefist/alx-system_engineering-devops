# Puppet config for nginx server

# install nginx
package { 'nginx':
  ensure => installed,
}

# start the service
service { 'nginx':
  ensure => running,
  enable => true,
}

# create the index file with content "Hello World!"
# and notify the nginx service to restart
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# create the nginx default config with basic settings,
# a 301 redirect and notify nginx service to restart
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
  listen 80;

  add_header X-Served-By $hostname;

  server_name _;

  root /var/www/html;
  index index.html index.nginx-debian.html;

  location / {
    # First attempt to serve request as file, then
    # as directory, then fall back to displaying a 404.
    try_files $uri $uri/ =404;
  }

  location /redirect_me {
    return 301 "https://www.example.com/your-target-url";
  }
}
',
  require => [File['/var/www/html/index.html'], Package['nginx']],
  notify  => Service['nginx'],
}
