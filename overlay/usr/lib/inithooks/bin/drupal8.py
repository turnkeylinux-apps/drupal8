#!/usr/bin/python3
"""Set Drupal8 admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively
    --domain=   unless provided, will ask interactively
                DEFAULT=www.example.com
"""

import sys
import getopt
import inithooks_cache
import pipes
import time

from dialog_wrapper import Dialog
from mysqlconf import MySQL

import subprocess

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

DEFAULT_DOMAIN="www.example.com"

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email=', 'domain='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    domain = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val
        elif opt == '--domain':
            domain = val
            
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
    
    if not domain:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')
            
        domain = d.get_input(
            "Drupal8 Domain",
            "Enter the domain to serve Drupal8.",
            DEFAULT_DOMAIN)
            
    if domain == "DEFAULT":
        domain = DEFAULT_DOMAIN
                
    inithooks_cache.write('APP_DOMAIN', domain)

    print("Progress...")
    m = MySQL()
    m.execute('UPDATE drupal8.users_field_data SET mail=\"%s\" WHERE name=\"admin\";' % email)
    m.execute('UPDATE drupal8.users_field_data SET init=\"%s\" WHERE name=\"admin\";' % email)
    domain = domain.replace('.','\\\\\.')
    subprocess.run([
	'/usr/lib/inithooks/bin/drupalconf.sh',
	'-e', email,
	'-p', password,
	'-d', domain
    ])
    
if __name__ == "__main__":
    main()
