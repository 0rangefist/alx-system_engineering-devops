# This puppet fixes a typo in wp-settings.php
exec { 'fix_typo':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
