import html_downloader
import html_parser
import outputer
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.URLManager()
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.outputer = outputer.Outputer()

    def crawl(self, root_url):
        _circle_count = 0
        print('in crawl')
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url() and _circle_count < 10:
            try:
                print('-------------------round:%d------------------' % _circle_count)
                url = self.urls.get_new_url()
                html = self.downloader.download(url)
                new_urls, new_data = self.parser.parse(url, html)
                self.urls.add_new_urls(new_urls)
                self.outputer.add_data(new_data)
                _circle_count += 1
            except:
                print('crawl failed')

        self.outputer.output()
