import requests
import random
import string

e_sub = []




#获取机场试用订阅
def get_sub_url():
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    # V2B_SUB_REL_URL = '/api/v1/user/getSubscribe'
    home_urls = (
        'https://xn--4gqu8thxjfje.com',
        'https://dash.vmssr.co',
        'https://www.ckcloud.xyz',
        'https://fastestcloud.xyz',
        'https://user.bafang.vip',
        'https://cloud.hhygj.xyz',
        'https://feiniaoyun.top', 
        'https://www.dgycom.com',
        'https://xn--sjq02ggyfdmt.com',
        'https://satou.moe',
        'https://fly10086.top',
        'https://party668.com',
        'https://www.t3acc.top',
        'https://seeworld.pro'
    )
    times = 1
    for current_url in home_urls:
        i = 0
        while i < times:
            header = {
                'Referer': current_url,
                'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            form_data = {
                'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
                'password': 'autosub_v2b',
                'invite_code': '',
                'email_code': ''
            }
            if current_url == 'https://xn--4gqu8thxjfje.com':
                try:
                    fan_res = requests.post(
                        'https://xn--4gqu8thxjfje.com/api/v1/passport/auth/login', data=form_data, headers=header)
                    auth_data = fan_res.json()["data"]["auth_data"]
                    print(auth_data)
                    fan_header = {
                        'Host': 'meal.leftright.buzz',
                        'Origin': 'https://xn--4gqu8thxjfje.com',
                        'Authorization': ''.join(auth_data),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                        'Referer': 'https://xn--4gqu8thxjfje.com/',
                    }
                    fan_data = {
                        'period': 'onetime_price',
                        'plan_id': '1',
                    }
                    fan_res_n = requests.post(
                        'https://xn--4gqu8thxjfje.com/api/v1/user/order/save', headers=fan_header, data=fan_data)
                    print(fan_res_n.json()["data"])
                    fan_data_n = {
                        'trade_no':fan_res_n.json()["data"],
                        #'method': '1',
                    }
                    fan_res_pay = requests.post(
                        'https://xn--4gqu8thxjfje.com/api/v1/user/order/checkout', data=fan_data_n, headers=fan_header)
                    print("获取饭小溪订阅成功。。。",fan_res_pay.text)
                
                except Exception as result:
                    print(result)
                    break
            try:
                response = requests.post(
                    current_url+V2B_REG_REL_URL, data=form_data, headers=header)
                subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
                e_sub.append(subscription_url)
                print("add:"+subscription_url)
            except:
                print("获取订阅失败")
            i += 1

get_sub_url()
