from selenium import webdriver
from bs4 import BeautifulSoup
import telegram


token = '5478587674:AAFEqet3djg6ajTh0VAXnwfnG85nCcFsQWM'
bot = telegram.Bot(token)
id = 1295404222
bot = telegram.Bot(token)

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# options.add_argument("--enable-javascript") # please turn javascript on and reload the page 때문에 넣어봤는데 안됨 
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)

"""
url='https://opga009.com/bbs/login.php' #들어가려는 사이트 주소
driver.get(url)  #사이트 접속

driver.find_element_by_id('login_id').send_keys('mynamehaha') #id로 찾음, 개발자 도구로 login_id가지고 있다는거 알아내고 그거로 접근. send_key로 아이디 myname haha를 쏴줌 
driver.find_element_by_id('login_pw').send_keys('123123')

driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div/div[2]/div[1]/div/div/form/button').click() # 로그인 버튼 클릭. xpath로 접근. 버튼에 우클릭 하고 xpath 찾기 하면됨. click함수로 클릭시킴.
#1.26 이거 element값 바뀌어서 다시 xpath따서 변경해줌

"""
# 로그인 부분(바운스는 로그인 안해도 출근부 조회 가능해서 그냥 다 주석 처리)

url='https://opga101.com/bbs/board.php?bo_table=op_partner_posting&wr_id=537552&uptime=1662922019&cat=18&cat2=&addrName=&sub_bs=&_stx=%EC%84%A0%EB%A6%89-%EB%B0%94%EC%9A%B4%EC%8A%A4'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
example=soup.find('h1', {'class': False, 'id': False})
bot.sendMessage('@바운스', text=example.get_text())

