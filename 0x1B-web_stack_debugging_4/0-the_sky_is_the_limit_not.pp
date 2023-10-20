# Puppet file to fix low ULIMIT in nginx server

exec { 'fix_ulimit':
  command => "/bin/sed -i 's/15/8192/g' /etc/default/nginx",
}

exec { 'nginx_restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
