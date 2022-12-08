import requests
api_key = 'AIzaSyArjip2dPu0_wDBLGqPNtSSjiMThTW3ycE'
test_url = input('Enter your url: ')
pagespeed_api = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'

res_pagespeed = requests.get(pagespeed_api)
if res_pagespeed.status_code == 200:
    data = res_pagespeed.json()
    print(data)

else:
    print('Response code:', res_pagespeed.status_code )