#!/usr/bin/python
#coding=utf-8
#Filename:driver.py
import io
import datetime
import PyRSS2Gen
from time import strptime
from time import mktime

def to_redis():
    """"""
    pass

def to_file(item_list, conf):
    """"""
    try:
        lines = [conf['file_template']%proxy for proxy in item_list]
        with io.open(conf['file_path'] + conf['filename'], 'w', encoding='utf-8') as fp:
            fp.writelines(lines)
    except Exception , e:
        raise e

def to_rss(item_list, conf):
    """"""
    try:
        rss = PyRSS2Gen.RSS2(
            title = conf['title'],
            link =  conf['link'],
            description = conf['description'],
            lastBuildDate = datetime.datetime.now(),
            items = [
                PyRSS2Gen.RSSItem(
                    title = item['title'],
                    link = item['url'],
                    description = item['content'],
                    guid = PyRSS2Gen.Guid(item['url']),
                    pubDate = datetime.datetime.fromtimestamp(mktime(parse_time(item['date'])))
                    )  for item in item_list
            ])
        rss.write_xml(open(conf['file_path'] + conf['rss_name'], "w"))
    except Exception , e:
        raise e

def parse_time(time_string):
    """"""
    time_string = time_string.strip()
    dt = datetime.datetime.now()
    if time_string:
        idx = time_string.find("-")
        if idx > -1:
            idx = time_string.find("-", idx + 1)
            if idx > -1:
                pass
            else:
                time_string = "%d-%s" %(dt.year, time_string)
        else:
            time_string = "%d-%d-%d %s" %(dt.year , dt.month , dt.day, time_string)
    return strptime(time_string, '%Y-%m-%d %H:%M')

if __name__ == '__main__':
    print parse_time("03-10 10:25")
    print parse_time("2014-10-28 19:03")
    print parse_time("19:03")
    print type(datetime.datetime(2003, 9, 6, 21, 49))
