# -*- coding: utf-8 -*-
import re
import urllib.parse
from bs4 import BeautifulSoup


class Parser(object):
    def _parse_urls(self, url, soup):
        new_urls = set()
        nodes_data_href = soup.find_all('li', attrs={'data-href': re.compile('/chengdu/[a-z]*/\d+-\d+\.html')})
        nodes_href = soup.find_all('a', attrs={'href': re.compile('/chengdu/[a-z]*/\d+-\d+\.html')})
        # nodes = soup.find_all('li', href=re.compile(r'/chengdu/[a-z]*/\d+-\d+\.html'))
        for node in nodes_data_href:
            new_url = node['data-href']
            full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(full_url)
            # print(node.name, node['data-href'])
        for node in nodes_href:
            new_url = node['href']
            full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(full_url)
        print('parsed new urls,count:%d:%s' % (len(new_urls), new_urls))
        return new_urls

    def _parse_data(self, url, soup):
        data = {}
        data['url'] = url
        location_node = soup.find('div', class_='which')
        community = location_node.find('a', class_='hs-name').get_text()
        address = location_node.find('p', class_='address').get_text()
        data['community'] = community
        data['address'] = address
        info_node = soup.find('div', class_='hs-infor')
        area = info_node.find('span', class_='name').get_text()
        total_price = info_node.find('span', class_='price').get_text()
        average_price = info_node.find('span', class_='cont').get_text()
        data['area'] = area
        data['total_price'] = total_price
        data['average_price'] = average_price
        print('parsed new data:%s' % data)
        return data

    def parse(self, url, html):
        if url is None or html is None:
            return
        soup = BeautifulSoup(html, 'html.parser')
        # print(html)
        new_urls = self._parse_urls(url, soup)
        new_data = self._parse_data(url, soup)
        return new_urls, new_data
