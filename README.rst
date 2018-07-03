Drupal 8 - Content Management Framework
=======================================

`Drupal`_ is an open source content management platform licensed under
the GPL. Equipped with a powerful blend of features, Drupal can support
a variety of websites ranging from personal blogs, corporate brochures
and large community-driven websites.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Drupal 8 configurations:
   
   - Installed (using drush) from upstream source code to /var/www/drupal8

     **Security note**: Updates to Drupal may require supervision so
     they **ARE NOT** configured to install automatically. See below for
     updating Drupal.

   - Includes drush for command line administration and configuration.

   - Drupal security update alerts delivered to your inbox - requires
     `Security Alerts`_ ('secalerts') be enabled on firstboot with a valid
     email address.

- Bundled Drupal 8 modules and dependencies (installed to 
  /var/www/drupal8/modules - new default for Drupal8):

   - `Field group`_: Allows fields to be grouped together.
   - `Google analytics`_: Adds Google Analytics js tracking code to all
     your site's pages.
   - `Honeypot`_: A honeypot for deterring spam bots from completing
     forms on your site  (additionally uses timestamp method).
   - `Imce`_: Powerful image file uploader and browser, with support for
     on the fly resizing.
   - `PathAuto`_: Auto-generate search engine friendly URLs (SEO).
   - `Token`_: Provides a shared API for replacement of textual
     placeholders with actual data.

   Note: Only some modules are enabled by default. To enable/disable 
     modules, navigate to **Administer > Modules** (or
     http://example.com/admin/modules). Some modules may require
     additional configuration and/or permissions settings.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Supervised Manual Drupal Update
-------------------------------

It is possible to check for and install updates from the Drupal Admin
UI:: **Admin > Reports > Avaialble Updates**

Or from the command line::

    drush pm-refresh
    drush pm-update --security-only --simulate
    drush pm-update --security-only

We also recommend that you  subscribe to the drupal.org security
newsletter (create a user account on drupal.org and within your drupal.org
profile:: **Edit > My newsletter** tab).

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Adminer: username **adminer**
-  Drupal 8: username **admin**

.. _Drupal: http://drupal.org
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Security Alerts: https://www.turnkeylinux.org/docs/automatic-security-alerts
.. _Field group: https://www.drupal.org/project/field_group
.. _Google analytics: https://www.drupal.org/project/google_analytics
.. _Honeypot: https://www.drupal.org/project/honeypot
.. _Imce: http://drupal.org/project/imce
.. _PathAuto: http://drupal.org/project/pathauto
.. _Token: http://drupal.org/project/token
.. _Adminer: http://www.adminer.org

