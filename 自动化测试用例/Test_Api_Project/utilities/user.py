"""
settings配置文件，与WEB端自动化类似，settings文件中存放整个项目的配置，如：被测项目域名、数据库地址、redis地址、APP版本号、
请求头等
"""
#env config
ENV = 'test'

APP_VERSION = '1.1.0'

HEADERS = {'content-type':'application/x-www-form-urlencoded; charset = UTF-8'}

#test url test config
API_TEST_BASE_URL = "http://dev.ncme.org.cn/weixin"

#redis config
REDIS_HOST = ''
REDIS_PORT = ''

#mysql config
DB_HOST = ''
DB_PORT = ''
DB_USER = ''
DB_PASSWORD = ''



