#!/usr/bin/python3

import argparse
import mechanicalsoup
import sys
import os
from getpass import getpass

parser = argparse.ArgumentParser(description="Create performance report from" +
                                             " Unisphere")
parser.add_argument("-u", "--username", help="Unisphere user", type=str,
                    required=True)
parser.add_argument("-s", "--server", help="Unisphere server", type=str,
                    required=True)
parser.add_argument("-p", "--port", help="Unisphere port", type=str,
                    required=False, default="8443")
parser.add_argument("-v", "--verbose", help="Verbose output. Add " +
                    "additional v to increase level.",
                    action="count", default=0)
args = parser.parse_args()

args.password = getpass("Password:")

print(args)

scriptpath = os.path.dirname(os.path.abspath(sys.argv[0]))
certfile = scriptpath + "/certificates/" + args.server + ".pem"

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='Mozilla/5.0 (Windows NT 6.3; Win64; x64) ' +
               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
               'Chrome/78.0.3904.108 Safari/537.36',
)

browser.set_verbose(args.verbose)

browser.open("https://" + args.server + ":" + args.port +
             "/univmax/component/em_smc/src/main/ts/common/login/Login.html",
             verify=certfile)

browser.select_form('form[name="loginform"]')
browser["uName"] = args.username
browser["pWrd"] = args.password

response = browser.submit_selected()
print(response.text)
