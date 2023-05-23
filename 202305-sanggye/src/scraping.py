from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import urllib.request

# 크롬 브라우저 창 크기 설정하고 실행하기
options = Options()
options.add_argument('--window-size=1024,768')
driver = webdriver.Chrome(options=options)

# 구글 이미지 검색 페이지로 이동하기
driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

# 이미지 검색 창에서 키워드 이미지 검색하기
elem = driver.find_element_by_name('q')
elem.send_keys('삼육고등학교')
elem.send_keys(Keys.RETURN)

# 검색된 페이지를 아래로 스크롤 다운하여 더 많은 이미지 불러오기
body = driver.find_element_by_tag_name('body')
for i in range(50):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

# 검색한 이미지 파일에 해당하는 class selector 를 찾아 저장하기
images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')

# 해당 이미지를 클릭하여 나온 큰 이미지의 URL 주소를 이용하여 다운로드 받아 .jpg 파일로 저장하기
for i, image in enumerate(images):
    image.click()
    time.sleep(1)
    imgUrl = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')
    urllib.request.urlretrieve(imgUrl, str(i) + '.jpg')

# 브라우저 종료하기
driver.close()