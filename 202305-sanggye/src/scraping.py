# 참고한 사이트 : https://velog.io/@moon_happy/%EC%97%B0%EC%98%88%EC%9D%B8-%EC%82%AC%EC%A7%84-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0
# 실행 전 설치할 파이썬 라이브러리
# pip install requests bs4 selenium pillow
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import io
import time

# 검색할 키워드 리스트
listm=['apple fruit', 'banana fruit','orange fruit']

# 수집할 이미지 갯수 지정
img_number = 10

# 이미지 검색
for i in listm:
  options = Options()
  # 검색어 설정
  search_name = i
  # 검색어를 이용한 구글 이미지 검색 url
  url = f'https://www.google.com/search?q={search_name}&source=lnms&tbm=isch'
  # 크롬 드라이버 실행 (다운로드 받은 드라이버 파일을 같은 폴더에 넣어야 함)
  service = Service()
  driver = webdriver.Chrome(service=service, options=options)
  # url 접속
  driver.get(url)
  # 페이지 로드를 위한 대기 시간
  time.sleep(2)
  # 이미지 로딩을 위한 스크롤 다운
  last_height = driver.execute_script("return document.body.scrollHeight")
  while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(1)
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height
  # 이미지 링크 추출
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  img_tags = soup.find_all('img')
  urls = []
  for img in img_tags:
      try:
          url = img['src']
          if 'http' in url:
              urls.append(url)
              print(url)
      except:
          pass
  # 이미지 다운로드
  os.makedirs(f'./images/{search_name}', exist_ok=True)
  count = 0
  for url in urls:
      try:
          response = requests.get(url, stream=True)
          # 이미지 사이즈 확인
          img = Image.open(io.BytesIO(response.content))
          width, height = img.size
          # 이미지 크기가 20, 20 이상인 경우에만 저장
          if width >= 20 and height >= 20:
              file_name = f'./images/{search_name}/{count}.jpg'
              with open(file_name, 'wb') as out_file:
                  out_file.write(response.content)
              print(f'{file_name} saved')
              count += 1
              if count == img_number:
                  break
      except:
          pass
  # 크롬 드라이버 종료
  driver.quit()