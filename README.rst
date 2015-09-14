Drupal 8 - Content Management Framework
=======================================

`Drupal`_ is an open source content management platform licensed under
the GPL. Equipped with a powerful blend of features, Drupal can support
a variety of websites ranging from personal blogs, corporate brochures
and large community-driven websites.

**Note:**
Drupal 8 is the current development version of Drupal. The version
included in this appliance is beta. It is not recommended that you use
this appliance for production; use only for testing and development.
Following the final stable release of Drupal8 this appliance will be
released without this notice. This appliance also includes the
development version of Drush (currently required for Drupal8
compatibility).

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Drupal 8 configurations:
   
   - Installed from upstream source code to /var/www/drupal8
   - Includes drush for command line administration and configuration.

- Bundled popular Drupal 8 modules and dependencies (installed to
  /var/www/drupal8/modules - new default for Drupal8):
   
   - `Panels`_: Drag and drop customized layouts for pages, nodes and
     blocks.
   - `Backup and migrate`_: Backup and restore your Drupal site
     on-demand or on a schedule.
   - `Devel`_: A suite of helper modules for Drupal module and theme
     developers.
   - `Drush`_: a command line shell and Unix scripting interface for
     Drupal.
   - `Imce`_: Powerful image file uploader and browser, with support for
     on the fly resizing.
   - `Recaptcha`_: Thwart spammers by adding image or text based
     CAPTCHAs to your site.
   - `PathAuto`_: Auto-generate search engine friendly URLs (SEO).
   - `GlobalRedirect`_: Alias 301 redirects, prevents duplicate content.
     (SEO)
   - `Webform`_: Create forms and questionnaires.
   - `Logintoboggan`_: Improves Drupal's login system.
   - `Admin menu`_: Adds dropdown administration menu to the top of the
     screen.
   - `Colorbox`_: Images, iframed or inline content etc. can be
     displayed in a overlay above the current page.
   - `Google analytics`_: Adds Google Analytics js tracking code to all
     your site's pages.
   - `Advanced\_help`_: Improves the Drupal help system.
   - `Rules`_: Lets you define conditionally executed actions based on
     occurring events.
   - `Token`_: Provides a shared API for replacement of textual
     placeholders with actual data.
   - `Link`_: Support URL link field in custom content types.
   - `Date`_: Support Date field in custom content types.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, Adminer: username **root**
-  Drupal 8: username **admin**

.. _Drupal: http://drupal.org
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Panels: http://drupal.org/project/panels
.. _Backup and migrate: http://drupal.org/project/backup_migrate
.. _Devel: http://drupal.org/project/devel
.. _Drush: http://drupal.org/project/drush
.. _Imce: http://drupal.org/project/imce
.. _Recaptcha: http://drupal.org/project/recaptcha
.. _PathAuto: http://drupal.org/project/pathauto
.. _GlobalRedirect: http://drupal.org/project/globalredirect
.. _Webform: http://drupal.org/project/webform
.. _Logintoboggan: http://drupal.org/project/logintoboggan
.. _Admin menu: http://drupal.org/project/admin_menu
.. _Colorbox: http://drupal.org/project/colorbox
.. _Google analytics: http://drupal.org/project/google_analytics
.. _Advanced\_help: http://drupal.org/project/advanced_help
.. _Rules: http://drupal.org/project/rules
.. _Token: http://drupal.org/project/token
.. _Link: http://drupal.org/project/link
.. _Date: http://drupal.org/project/date
.. _Adminer: http://www.adminer.org
