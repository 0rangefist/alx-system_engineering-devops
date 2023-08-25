# execute a kill command
exec {'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
