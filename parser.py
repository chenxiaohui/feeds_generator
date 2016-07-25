#!/usr/bin/python
#coding=utf-8
#Filename:parser.py
import datetime
from urllib2 import urlopen, Request
from config import *
import lxml.html.soupparser as soupparser
from driver import to_rss
#from pprint import pprint


def parse(conf):
    """
    parse html and get proxy list
    """
    try:
        result = []
        req = Request(conf['url'], headers=conf['hdr'])
        html = urlopen(req)
        dom = soupparser.fromstring(html)
        items = dom.xpath(conf['xpath'])

        for item in items:
            result.append(conf['parse_func'](item.getchildren()))
        if 'mock' in conf.keys():
            result.insert(0, conf['mock'])
        return result
    except Exception , e:
        raise e

def refresh(conf):
    """
    refresh and update proxy list
    """
    try:
        item_list = parse(conf)
        #to_file(item_list, conf)
        to_rss(item_list, conf)
    except Exception , e:
        raise e

if __name__ == "__main__":
    refresh(smzdm_shenjiage_conf)
    refresh(smzdm_baicaidang_conf)
    refresh(smzdm_shoumanwu_conf)
    print "refresh succeed. time: " + str(datetime.datetime.now())
