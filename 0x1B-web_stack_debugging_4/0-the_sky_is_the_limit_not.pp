# Puppet file to fix low ULIMIT in nginx server

file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"-n 8192\"\n",
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/default/nginx'],
}
