#! /usr/bin/env python
import xml.etree.ElementTree as et
import sys
import time
import socket
import StringIO
import zipfile

# parse input
data = StringIO.StringIO(sys.stdin.read())
z = zipfile.ZipFile(data)
zmember =  z.namelist()[0]
xml = StringIO.StringIO(z.read(zmember))
root = et.parse(xml)
result = ''

# print metadata
org = root.find('./report_metadata/org_name').text
org_mail = root.find('./report_metadata/email').text
begin = time.ctime(float(root.find('./report_metadata/date_range/begin').text))
end = time.ctime(float(root.find('./report_metadata/date_range/end').text))

print "Organization: " + org + " (" + org_mail + ")"
print begin + " - " + end

# print policy
# TODO: not really that important - i know my own policy

# print records
for row in root.findall('./record/row'):
	num = row.find('./count').text
	src = row.find('./source_ip').text
	src_domain = socket.gethostbyaddr(src)[0]
	dkim = row.find('./policy_evaluated/dkim').text
	spf = row.find('./policy_evaluated/spf').text
	print
	print num + " Mails from " + src_domain + " (" + src + ")"
	print "DKIM: " + dkim
	print "SPF: " + spf
