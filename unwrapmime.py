#! /usr/bin/env python
import sys
import StringIO
import zipfile
import email
import base64

def unwrap(d):
	s = d.getvalue()
	# read first line (this is the border)
	boundary = s.split('\n')[0]
	# parse each section seperately
	sections = s.split(boundary)[1:-1]
	for section in sections:
		# check content-disposition
		cd = section.strip().split('\n')[0]
		if not "attachment" in cd:
			continue
		# extract body
		body = section.strip().split('\n\n')[1]
		# base64 decode
		return base64.b64decode(body)

# read stdin
data = StringIO.StringIO(sys.stdin.read())

# unwrap mime data (if necessary)
try:
	z = zipfile.ZipFile(data)
except:
	data = StringIO.StringIO(unwrap(data))

# print zipfile
print data.getvalue()
