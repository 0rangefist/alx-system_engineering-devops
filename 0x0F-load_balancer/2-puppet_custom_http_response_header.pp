# Puppet config for nginx server

# update OS
exec { 'apt update':
        command => '/usr/bin/apt update',
}

# install nginx
package { 'nginx':
        ensure  => 'installed',
        require => Exec['apt update']
}

# add custom index.html
file {'/var/www/html/index.html':
        content => 'Hello World!'
}

# add 301 redirect
exec {'redirect':
        command  => 'sed -i "24i\        rewrite ^/redirect_me https://example.com permanent;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

# add custom response header
exec {'response header':
        command  => 'sed -i "25i\        add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

# ensure nginx service is running
service {'nginx':
        ensure  => running,
        require => Package['nginx']
}
