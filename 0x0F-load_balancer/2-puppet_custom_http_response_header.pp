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

# add custom header
file_line { 'custom_header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}