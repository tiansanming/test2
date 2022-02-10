import gevent
from gevent import monkey
from gevent import pool

monkey.patch_all()
import requests
import pymongo
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time

proxies = {
    "https": "***.***.*.***:*****",
}

###########格式化发布时间############
def dateFormate(date):
    date = date.replace("+0000 ", "")
    fmt = '%a %b %d %H:%M:%S %Y'
    formated_date = datetime.datetime.strptime(date, fmt)
    return formated_date


###########获取当前日期#############
def get_now_time():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    return now_time


def stamp_strft_datetiem(date):
    return int(time.mktime(date.timetuple())) * 1000


############通过selenium来获取token##############
############通过requests获取不到token#############
def get_token():
    url = "https://twitter.com/search"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    ## chrome_options.add_argument("--proxy-server=http://192.168.1.107:15001")
    driver = webdriver.Chrome(executable_path="E:\soft\driver\chromedriver_win32\chromedriver.exe", options=chrome_options)
    driver.get(url)
    cookiesList = driver.get_cookies()
    cookies = {}
    for cookie in cookiesList:
        cookies[cookie.get("name")] = cookie.get("value")
    driver.quit()
    print(cookies)
    return cookies['gt']


def start_spider(keyword, start_time, page_size):
    # romote_client = pymongo.MongoClient("mongodb://admin:admin123456@192.168.1.107:27017/admin")
    # romote_db = romote_client.myWork
    # romote_collection = romote_db.Twitter_Data
    params = {
        'include_profile_interstitial_type': '1',
        'include_blocking': '1',
        'include_blocked_by': '1',
        'include_followed_by': '1',
        'include_want_retweets': '1',
        'include_mute_edge': '1',
        'include_can_dm': '1',
        'include_can_media_tag': '1',
        'skip_status': '1',
        'cards_platform': 'Web-12',
        'include_cards': '1',
        'include_composer_source': 'true',
        'include_ext_alt_text': 'true',
        'include_reply_count': '1',
        'tweet_mode': 'extended',
        'include_entities': 'true',
        'include_user_entities': 'true',
        'include_ext_media_color': 'true',
        'include_ext_media_availability': 'true',
        'send_error_codes': 'true',
        'simple_quoted_tweets': 'true',
        #'tweet_search_mode': 'live',  ####根据最新的搜索条件
        'count': '100',
        'query_source': 'typed_query',
        'pc': '1',
        'spelling_corrections': '1',
        'ext': 'mediaStats,highlightedLabel,cameraMoment',
        'spelling_corrections': '1',
    }
    headers = {
        'authority': 'api.twitter.com',
        'x-twitter-client-language': 'zh-cn',
        ########关键关键关键########
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'sec-fetch-dest': 'empty',
        'x-guest-token': '',  #################关键关键关键关键关键关键########################
        'x-twitter-active-user': 'yes',
        'accept': '*/*',
        'origin': 'https://twitter.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    #url = "https://api.twitter.com/2/search/adaptive.json"
    url = "https://twitter.com/i/api/2/search/adaptive.json"
    token_value = get_token()
    headers["x-guest-token"] = token_value
    params["q"] = keyword + ' until:{}-12-31 since:{}-01-01'.format(str(start_time), str(start_time)),
    for i in range(0, page_size):
        response = requests.get(url, headers=headers, params=params, proxies=proxies)
        jsonData = response.json()
        print(jsonData)
        if 'errors' in jsonData:
            while True:
                try:
                    token_value = get_token()
                    break
                except Exception as e:
                    print(e, "--" * 50)
                    pass
            headers["x-guest-token"] = token_value
            continue
        contents = jsonData.get("globalObjects").get("tweets")
        users = jsonData.get("globalObjects").get("users")
        if contents == {}:
            break
        print(len(contents))
        for info in contents.values():
            item = {}
            item["authorId"] = info.get("user_id_str")
            user_id_str = info.get("user_id_str")
            item["authorName"] = users.get(user_id_str).get("name")
            item["id"] = info.get("id_str")
            item["postdateOrigin"] = info.get("created_at")
            item["postDateString"] = str(dateFormate(info.get("created_at")))
            item["postDate"] = stamp_strft_datetiem(dateFormate(info.get("created_at")))
            item["postYear"] = int(item["postDateString"].split("-")[0])
            item["content"] = info.get("full_text")
            item["title"] = ""
            item["commentCount"] = info.get("reply_count")
            item["shareCount"] = info.get("retweet_count")
            item["likeCount"] = info.get("favorite_count")
            item["keyWord"] = keyword
            item["link"] = "https://twitter.com/" + users.get(user_id_str).get("screen_name") + "/status/" + info.get(
                "id_str")
            item["dataUrl"] = url
            item["crawlSource"] = "twitter"
            item["postSource"] = ""
            m = hashlib.md5()
            m.update((keyword + item["content"]).encode("utf-8"))
            item["_id"] = m.hexdigest()

            # flag = romote_collection.save(item)
            # print(flag)
            print(item)
        instructions = jsonData.get("timeline").get("instructions")
        if 0 == i:
            scrollCursorValue = instructions[0].get("addEntries").get("entries")[-1].get("content").get(
                "operation").get("cursor").get("value")
            params['cursor'] = scrollCursorValue
        else:
            scrollCursorValue = instructions[-1].get("replaceEntry").get("entry").get("content").get("operation").get(
                "cursor").get("value")
            params['cursor'] = scrollCursorValue


def main(pool, keyword, year, task_value, page_size):
    tasks = []
    for start_year in range(year, year - task_value, -1):
        print(start_year)
        tasks.append(pool.spawn(start_spider, keyword, start_year, page_size))
    gevent.joinall(tasks)


if __name__ == "__main__":
    pool = pool.Pool(20)
    main(pool, "baby doge", 2021, 2, 10000)