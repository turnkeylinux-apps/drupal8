#!/usr/bin/python
"""Set Drupal8 admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache

from dialog_wrapper import Dialog
from mysqlconf import MySQL

from executil import system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Drupal8 Password",
            "Enter new password for the Drupal8 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Drupal8 Email",
            "Enter email address for the Drupal8 'admin' account.",

            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    m = MySQL()
    m.execute('UPDATE drupal8.users_field_data SET mail=\"%s\" WHERE name=\"admin\";' % email)
    m.execute('UPDATE drupal8.users_field_data SET init=\"%s\" WHERE name=\"admin\";' % email)
    system("/usr/local/bin/drush -y config-set contact.form.feedback recipients %s" % email)
    system("/usr/local/bin/drush -y config-set update.settings notification.emails.0 %s" % email)
    system("/usr/local/bin/drush -y config-set system.site mail %s" % email)
    system("/usr/local/bin/drush cache-rebuild")
    system("/usr/local/bin/drush user-password admin --password='%s'" % password)

if __name__ == "__main__":
    main()

