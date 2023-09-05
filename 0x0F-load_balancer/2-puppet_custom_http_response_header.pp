# Puppet config for nginx server
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  exec { 'allow_firewall_http':
    command => 'ufw allow Nginx HTTP',
    unless  => 'ufw status | grep "Nginx HTTP"',
    require => Service['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => 'file',
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/var/www/html/404.html':
    ensure  => 'file',
    content => "Ceci n'est pas une page",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => "
server {
  listen 80;
  add_header X-Served-By ${hostname};
  server_name _;

  root /var/www/html;
  index index.html index.nginx-debian.html;

  location / {
    try_files ${uri} ${uri}/ =404;
  }

  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }

  location /404.html {
    root /var/www/html;
  }
}
",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Restart nginx if config file is modified
  exec { 'restart_nginx':
    command     => 'service nginx restart',
    refreshonly => true,
    subscribe   => File['/etc/nginx/sites-available/default'],
  }
