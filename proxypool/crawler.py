# -*- coding:utf-8 -*-

import json
import re
from pyquery import PyQuery as pq
from .utils import get_page

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        print(attrs['__CrawlFunc__'])
        return type.__new__(cls, name, bases, attrs)

class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        print('*' * 50)
        print(callback)
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    # def crawl_daili66(self, page_count=4):
    #     """
    #     获取代理66
    #     :param page_count: 页码
    #     :return: 代理
    #     """
    #     params = {
    #         'getnum': 20,
    #         'isp': 0,
    #         'anonymoustype': 3,
    #         'start': '',
    #         'ports': '',
    #         'export': '',
    #         'ipaddress': '',
    #         'area': '',
    #         'proxytype': 0,
    #         'api': '66ip'
    #     }
    #     #start_url = 'http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip'
    #     start_url = 'http://www.66ip.cn/nmtq.php?'
    #     html = get_page(url=start_url, params=params)
    #     pattern = re.compile(r'\d+\.\d+\.\d+\.\d+:\d+', re.S)
    #     result = re.findall(pattern, html)
    #     return result

    def crawl_kxdaili(self):
        for i in range(1, 5):
            start_url =  'http://www.kxdaili.com/dailiip/1/{}.html#ip'.format(i)
            html = get_page(start_url)
            pattern = re.compile(r'<td>(\d+.\d+.\d+.\d+)</td>.*?<td>(\d+)</td>', re.S)
            ip_ports = re.findall(pattern, html)
            for ip, port in ip_ports:
                proxy = ip + ':' + port
                yield proxy


    # def crawl_ip181(self):
    #     start_url = 'http://www.ip181.com/'
    #     html = get_page(start_url)
    #     pattern = re.compile(r'<td>(\d+.\d+.\d+.\d+)</td>.*?<td>(\d+)</td>', re.S)
    #     ip_ports = re.findall(pattern, html)
    #     for ip, port in ip_ports:
    #         proxy = ip + ':' + port
    #         yield proxy

    # def crawl_ip3366(self):
    #     for i in range(1, 4):
    #         start_url = 'http://www.ip3366.net/?stype=1&page={}'.format(i)
    #         html = get_page(start_url)
    #         if html:
    #             pattern = re.compile(r'<td>(\d+.\d+.\d+.\d+)</td>.*?<td>(\d+)</td>', re.S)
    #             ip_ports = re.findall(pattern, html)
    #             for ip, port in ip_ports:
    #                 proxy = ip + ':' + port
    #                 yield proxy


    # def crawl_iphai(self):
    #     start_url = 'http://www.iphai.com/'
    #     html = get_page(start_url)
    #     if html:
    #         pattern = re.compile(r'<td>\s+(\d+.\d+.\d+.\d+)\s+</td>.*?<td>\s+(\d+)\s+</td>', re.S)
    #         ip_ports = re.findall(pattern, html)
    #         for ip, port in ip_ports:
    #             proxy = ip + ':' + port
    #             yield proxy


    # def crawl_89ip(self):
    #     start_url = 'http://www.89ip.cn/apijk/?&tqsl=30&sxa=&sxb=&tta=&ports=&ktip=&cf=1'
    #     html = get_page(start_url)
    #     if html:
    #         pattern = re.compile(r'(\d+.\d+.\d+.\d+:\d+)', re.S)
    #         ip_ports = re.findall(pattern, html)
    #         for ip_port in ip_ports:
    #             yield ip_port

    # def crawl_data5u(self):
    #     start_url = 'http://www.data5u.com/free/gngn/index.shtml'
    #     headers = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #         'Accept-Encoding': 'gzip, deflate',
    #         'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    #         'Cache-Control': 'max-age=0',
    #         'Connection': 'keep-alive',
    #         'Cookie': 'JSESSIONID=47AA0C887112A2D83EE040405F837A86',
    #         'Host': 'www.data5u.com',
    #         'Referer': 'http://www.data5u.com/free/index.shtml',
    #         'Upgrade-Insecure-Requests': '1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    #     }
    #     html = get_page(start_url, options=headers)
    #     if html:
    #         ip_address = re.compile(r'<span><li>(\d+.\d+.\d+.\d+)</li>.*?<li class="port.*?>(\d+)</li>', re.S)
    #         re_ip_address = ip_address.findall(html)
    #         for host, port  in re_ip_address:
    #             result = host + ':' + port
    #             yield result.replace(' ', '')
