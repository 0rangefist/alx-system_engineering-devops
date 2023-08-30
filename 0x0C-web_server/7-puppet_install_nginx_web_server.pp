# Puppet config for nginx server

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
  listen 80;
  server_name _;

  location /redirect_me {
    return 301 "https://www.example.com/your-target-url";
  }

  location / {
    return 200 "Hello World!";
  }
}
',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
