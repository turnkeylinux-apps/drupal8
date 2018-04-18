#!/bin/bash -e

while getopts e:p:d: option
    do
        case "${option}"
        in
        e) EMAIL=${OPTARG};;
        p) PASSWORD=${OPTARG};;
        d) DOMAIN=${OPTARG};;
    esac
done

sed -i '/\/\/ For UNIX support/a return static::canonicalize("/root");' /var/www/drupal8/vendor/webmozart/path-util/src/Path.php

/var/www/drupal8/vendor/bin/drush -y config-set contact.form.feedback recipients $EMAIL &> /dev/null
/var/www/drupal8/vendor/bin/drush -y config-set update.settings notification.emails.0 $EMAIL &> /dev/null
/var/www/drupal8/vendor/bin/drush -y config-set system.site mail $EMAIL &> /dev/null
/var/www/drupal8/vendor/bin/drush user-password admin $PASSWORD &> /dev/null
sed -i "/^\$settings\['trusted_host_patterns'\]/{n;s|.*|     '^$DOMAIN$',|}" /var/www/drupal8/web/sites/default/settings.php
/var/www/drupal8/vendor/bin/drush cache-rebuild &> /dev/null
