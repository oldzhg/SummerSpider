# coding: utf-8
import json
import requests
import sys
import urllib.parse
import urllib3


def get_json(id, limit, offset):
    url = 'https://imsummer.cn/api/v4/user/nearbies'
    payload = {
        'lat': '28.71729575497495',  # 东经
        'lng': '115.8206745934282',  # 西经
        'offset': offset,
        # 'q[city_id_eq]': '42142e4d-5ccd-4835-bdb7-546f7da12d06',  # 信阳市
        'q[school_id_eq]': id,
        'scope': 'global'
    }
    headers = {
        'Host': 'imsummer.cn',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'platform': 'ios',
        'Accept': '*/*',
        'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8',
        'Authorization': 'ixXzAgmV9NRz187GQHtv2S52',  # 抓包替换掉
        'Accept-Encoding': 'gzip, deflate'
    }

    r = requests.get(url, params=payload, headers=headers, verify=False)  # ssl验证关闭
    r = json.dumps(json.loads(r.content), indent=4, separators=(',', ': '), ensure_ascii=False)  # 格式化

    if r:
        with open("near.json", 'w') as f:
            f.write(r)
            f.close()
            return 1
    else:
        print("无符合当前条件用户的信息！")
        return 0


if __name__ == '__main__':
    schools = [  # 大陆高校
        '4c0b467a-2b3e-4e29-8300-0e03c995978f'  # 东华理工大学
    ]

    # 禁用安全请求警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    get_json(schools[0], 30, 0)

    print("Done!")
