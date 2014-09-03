#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
import re, sys
from xml.sax.saxutils import escape
#from titlecase import titlecase

if len(sys.argv) > 1 and len(sys.argv[1].strip()):
	text = sys.argv[1]
else:
	text = sys.stdin.read()


space_clean = re.sub('[^A-Za-z0-9]+', ' ', text)
usc_clean = re.sub('[^A-Za-z0-9]+', '_', text)

variations = {
  'space': escape(space_clean, {'"': '&quot;', '\n': '&#10;'} ),
  'usc': escape(usc_clean, {'"': '&quot;', '\n': '&#10;'} )
}



print """<?xml version="1.0"?>
<items>
 <item arg="%(space)s">
    <title>%(space)s</title>
    <subtitle>Replace with Space</subtitle>
    <icon>space.png</icon>
  </item>
<item arg="%(usc)s">
    <title>%(usc)s</title>
    <subtitle>Replace with _</subtitle>
    <icon>usc.png</icon>
  </item>
</items>""" % variations

