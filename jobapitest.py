from careerjet_api_client import CareerjetAPIClient

cj  =  CareerjetAPIClient("en_GB");

result_json = cj.search({
                        'location'    : 'seattle',
                        'keywords'    : 'python no experience',
                        'affid'       : 'xxxx',
                        'user_ip'     : 'xxxx',
                        'url'         : 'http://localhost',
                        'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                      });
print(result_json)
