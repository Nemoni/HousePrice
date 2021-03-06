class URLManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.data = {}

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            print('add url to list:%s' % url)
        '''else:
            print('in', url)
            print('new_urls:', self.new_urls)
            print('old_urls:', self.old_urls)'''

    def has_new_url(self):
        return len(self.new_urls)

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        print('get url from url list:%s' % url)
        return url

    def add_new_urls(self, new_urls):
        if new_urls is None:
            return
        for url in new_urls:
            self.add_new_url(url)
            #print('before add', url)
