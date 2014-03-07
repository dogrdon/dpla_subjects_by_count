#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

html = requests.get("http://dp.la/subjects").content
dom = lxml.html.fromstring(html)

#.pop-columns
data = []
#count_list = []
for entry in dom.cssselect('.pop-columns section ul li'):
    #data = {
    #    'subject' : entry.cssselect('a')
    #}
    data.append({'subject': entry.cssselect('a')[0].text_content(),
                 'count': entry.cssselect('span')[0].text_content()
    })
    #count_list.append() 
    
#print data_list
#print count_list

#data = dict(zip(data_list, count_list))

print data

# Saving data:

#scraperwiki.sql.save(unique_keys, data)

scraperwiki.sqlite.save(unique_keys=["subject"], data=data, table_name="dpla_subjects")
