#!/usr/bin/python
#coding=utf-8
#Filename:config.py
import re
seg=u"\t"
#def innertext(element):
    #""""""
    #return ''.join([text for text in element.itertext()])
def clean(text):
    """"""
    return re.sub('[\t\ \n\r]','',text)

common_conf = {
    'timeout':10,
    'hdr' : {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
}

smzdm_conf = dict(common_conf, **{
    'xpath': '//div[@class="list list_preferential "]',
    'file_template':u"%(title)s" + seg + u"%(url)s" + seg + u"%(pic)s"+ seg + u"%(content)s" + seg + u"%(date)s" + seg + u"%(direct_url)s\n",
    'parse_func':lambda item : {
        'title':item[0].getchildren()[0].text_content(),
        'url': item[1].attrib['href'],
        'pic': item[1].getchildren()[0].attrib['src'],
        'content': clean(item[2].getchildren()[1].text_content()),
        'direct_url': item[2].xpath(".//div[@class='buy']/a")[0].attrib['href'],
        'date': item[2].getchildren()[0].getchildren()[0].text,
    },
    'file_path':'/usr/share/nginx/html/',
    #'mock': {
        #'title':'mock',
        #'url': 'http://cxh.me',
        #'pic': 'http://cxh.me',
        #'content': 'mock item',
        #'direct_url': 'http://cxh.me',
        #'date': '12:34'
    #},
})

smzdm_shenjiage_conf = dict(smzdm_conf, **{
    'url' : 'http://www.smzdm.com/tag/%E7%A5%9E%E4%BB%B7%E6%A0%BC',
    'filename':'shenjiage.xml',
    'title' : u"神价格",
    'description' : u"神价格",
    'link' : "http://182.92.76.83/shenjiage.xml",
    'rss_name':'shenjiage.xml',
})

smzdm_baicaidang_conf = dict(smzdm_conf , **{
    'url' : 'http://www.smzdm.com/tag/%E7%99%BD%E8%8F%9C%E5%85%9A',
    'filename':'baicaidang.xml',
    'title' : u"白菜党",
    'link' : "http://182.92.76.83/baicaidang.xml",
    'description' : u"白菜党",
    'rss_name':'baicaidang.xml',
})

smzdm_shoumanwu_conf = dict(smzdm_conf , **{
    'url' : 'http://www.smzdm.com/tag/%E6%89%8B%E6%85%A2%E6%97%A0',
    'filename':'shoumanwu.xml',
    'title' : u"手慢无",
    'link' : "http://182.92.76.83/shoumanwu.xml",
    'description' : u"手慢无",
    'rss_name':'shoumanwu.xml',
})
