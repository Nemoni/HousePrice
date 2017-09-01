import urllib.request


class Downloader(object):
    def download(self, url):
        # print('before open', url)
        if url is None:
            return
        response = urllib.request.urlopen(url)
        print('download url:%s' % url)
        return response.read()
