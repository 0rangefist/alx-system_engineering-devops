# This manifest sets the soft and hard limits for user 'holberton'

exec { 'add_limits_holberton':
  command => 'echo "holberton soft nofile 8192" >> /etc/security/limits.conf &&
              echo "holberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => '/bin:/usr/bin',
}
