#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from lxml import *
from lxml import etree
from lxml import html
import requests
import re
import json
import dateutil.parser

def main():
    root = html.parse(open('Status.xls', "r"))
    root.xpath('//tr/td//text()')
    elements = root.xpath('.//row/cell//text()')
    try:
        # skip first line
        for i in range(2, len(elements) - 3, 2):
            dt = dateutil.parser.parse(elements[i], yearfirst=True).__format__("%Y-%m-%d")
            amount = re.sub('[^0-9]', '', elements[i + 1][:-6])
            sql = ('INSERT INTO RAW_SYR ("TIMESTAMP", "DAILY") VALUES ("%s",%s);' % (dt, ''.join(amount.split())))
            print(sql)
    except Exception as e:
        print("error: %s" % e)

if __name__ == '__main__':
    print('\n')
    main()
