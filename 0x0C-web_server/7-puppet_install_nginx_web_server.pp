# Puppet config for nginx server

# Install nginx
package { 'nginx':
  ensure => 'installed',
}

# Allow firewall connetion on HTTP Port 80
exec { 'permit_http':
  command => 'ufw allow "Nginx HTTP"',
  require => Package['nginx'],
}

# Create index.html file with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure redirect 301
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => inline_template("
<% if ! File.read('/etc/nginx/sites-available/default').include?('location /redirect_me {') %>
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
<% end %>
  "),
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => 'running',
  enable => true,
}
