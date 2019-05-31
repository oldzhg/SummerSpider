# coding: utf-8
import json
import requests
import urllib3


def get_json(id):
    url = 'https://imsummer.cn/api/v4/users/' + id
    # url = 'https://imsummer.cn/api/v3/user/transcript'
    headers = {
        'Host': 'imsummer.cn',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'platform': 'ios',
        'Accept': '*/*',
        'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8',
        'Authorization': 'ixXzAgmV9NRz187GQHtv2S52',
        'Accept-Encoding': 'gzip, deflate'
    }

    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    r = requests.get(url, headers=headers, timeout=1, verify=False)
    r = json.dumps(json.loads(r.content), indent=4, separators=(',', ': '), ensure_ascii=False)  # 格式化

    if r:
        with open("user.json", 'w') as f:
            f.write(r)
            f.close()
            return 1
    else:
        print("无该用户的信息！")
        return 0


if __name__ == '__main__':
    # 禁用安全请求警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    userid = "c29217e5-57cb-4b25-a9d6-3af6f8096b4f"  # 用户id
    get_json(userid)
    print("Done!")
