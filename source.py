# -*- coding: utf-8 -*-

import json
import urllib



# ツイート投稿用のURL
url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=3d7b9b87e2cdb691&lat=34.67&lng=135.52&range=5&order=4"



req = urllib.urlopen(url)


print(req)
