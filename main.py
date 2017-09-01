import ctrl_spider

if __name__ == "__main__":
    root_url = 'http://xf.fangdd.com/chengdu/huxing/22824-96400.html'
    obj_spider = ctrl_spider.SpiderMain()
    obj_spider.crawl(root_url)
