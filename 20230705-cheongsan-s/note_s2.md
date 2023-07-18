---
marp: true
theme: gaia
class: invert
paginate: true

---
<!-- 
_class: lead
-->
# 나만의 인공지능 웹 서비스 제작
인공지능의 머신러닝을 이용하여, 
나만의 인공지능 웹 서비스를 제작하고, 
나와 사회에 미칠 영향을 고민한다.

장윤재(janggoons@syu.ac.kr)
SW융합교육원, 삼육대학교

---
## 목차
* 과일 분류 모델 학습
* 과일 분류 웹 서비스 제작 및 개선
* 나만의 인공지능 웹 서비스 설계 및 개발
* 인공지능의 개념
* 공유 및 논의

---
## 학습목표
* 인공지능 기술을 이용하여 분류 모델을 학습시킬 수 있다.
* 인공지능 기술을 활용한 웹 서비스를 제작할 수 있다.
* 인공지능 기술 활용에 대한 나의 생각을 설명할 수 있다.

## 학습 내용
* 과일 분류 웹 서비스 제작
* 나만의 인공지능 웹 서비스 제작
* 인공지능 기술 활용에 대한 고민

---
<!--
_class: lead
_paginate: false
-->
# 과일 분류 모델 학습
1. 과일 분류 학습을 위한 데이터를 수집할 수 있다.
2. 지도학습을 통해 모델을 학습시킬 수 있다.

---
![bg](https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80)

---
## 사람은 과일을 어떻게 구분할까?
- 사람의 눈으로 과일을 볼 수 있다.
- 과일의 모습과 이전에 본 과일의 모습을 기억하여,
- 기억 속의 과일의 색, 모양, 향, 맛 등을 비교하여 과일을 구분한다.
- 사람 뇌의 뉴런들이 어떤 일을 하여 기억하고, 비교한다.

---
![bg](https://cdn.pixabay.com/photo/2015/11/28/10/52/binary-1066983_1280.jpg)

---
## 컴퓨터는 과일을 어떻게 구분할까?
- 컴퓨터에 연결된 카메라로 과일을 볼 수 있다.
- 과일의 모습은 숫자(0과 1로 된 이진수)로 저장되고, 
- 숫자들을 잘 계산하여, 대표되는 값을 찾고, 이 값 들과 다른 과일 이미지의 대표값과 비교한다.
- 컴퓨터가 수 많은 숫자들을 계산하고, 값을 비교한다.

---



---
![bg contain](https://mblogthumb-phinf.pstatic.net/MjAxNjEwMjRfMzkg/MDAxNDc3MzAzODcyNTQ5.ggZaroU1baErQDST2_tCNL0dyaX39MkzX82O-e0Y3sgg.idDEyFLI_BDSa_1KPZ8flst-TzgXdOmDfeGndF3kImcg.JPEG.msnayana/%EC%BB%A8%EB%B2%8C%EB%A5%98%EC%85%98.jpg?type=w2)
## 컴퓨터가 사물을 인식하는 한 가지 방법 (CNN)

---
![bg right:30% contain](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Yann_LeCun_-_2018_%28cropped%29.jpg/440px-Yann_LeCun_-_2018_%28cropped%29.jpg)
## 합성곱 신경망 (CNN)
* Convolutional Neural Network
  - 주로 이미지, 영상 데이터를 처리할 때 사용하는 딥러닝 모델
  - 인식할 데이터의 전체가 아닌 부분, 주변과의 관계를 집중하여 연산 과정을 효율적으로 처리하는 방법
  - 1989년 얀 르쿤, “Backpropagation applied to handwritten zip code recognition" 에서 처음 소개

---
## 과일 분류 모델 학습
* 머신러닝 machine learning
  - 기계가 사람 처럼, 새로운 것을 배우는 과정을 머신러닝 이라고 한다.
  - 한 번 학습하면 과일의 이름을 기억할 수 있다.
  - 새로운 과일을 보여준다면, 이름을 알 수 있을까?

---
## 과일 분류 모델 학습
* 컴퓨터에게 과일을 학습시키자.
  - 학습할 과일을 준비한 뒤, 
  - 컴퓨터에게 과일의 이름을 알려주고 기억하게 한다.
  - 조금 다른 모습의 같은 과일을 보여주고,
  - 과일의 이름을 맞추도록 한다.

---
## 데이터 수집
* 이미지 데이터를 수집하는 방법은,
  - 웹캠을 이용하여 사물을 직접 촬영하거나,
  - 이미지 파일을 수집한다.
* 이미지 파일 수집
  - 미리 수집된 저장소 활용
  - 직접 수집(스크래핑) -> [파이썬으로 구글 이미지 스크래핑 하기](https://github.com/janggoons/ai-future-society/blob/main/202305-sanggye/src/scraping.py)

---
![bg contain](img/01.png)
## [Teachable Machine](https://teachablemachine.withgoogle.com/)

---
## [Teachable Machine](https://teachablemachine.withgoogle.com/)
* 컴퓨터 학습시키기
  - 구분(class)할 이름 지정
  - 구분(class)별로 이미지 촬영(또는 업로드)
  - 모델 학습(Train Model) 클릭

--- 
## [Teachable Machine](https://teachablemachine.withgoogle.com/)
* 잘 학습했는지 확인하기
  - Preview > 각각의 이미지를 보여주고 잘 분류하는지 확인
  - 분류가 잘 안되면 이미지 데이터를 추가하고, 다시 학습시킨다.
* 언제 잘 인식하고, 언제 잘 인식하지 못하는가?
  - 웹캠으로 촬영 한다면 배경은?
  - 사물은 정지한 상태로 촬영해야 할까?
  - 몇 개의 데이터를 수집해야 할까?
  
---
## [Teachable Machine](https://teachablemachine.withgoogle.com/)
* 새로운 과일 추가하기
  - 구분(class) 추가하기
  - 데이터 수집하기 (웹캠, 또는 이미지 파일 업로드)
  - 모델 학습하기
  - 학습 결과 확인하기

---
<!--
_class: lead
_paginate: false
-->
# 과일 분류 웹 서비스 제작 및 개선
1. 과일 분류 모델을 이용하여 웹 서비스를 제작할 수 있다. 
2. 제작한 웹 서비스를 개선할 수 있다.


---
## 과일 분류 웹 서비스 만들기
* 준비하기
  - Export Model > Upload my model > 
  (업로드 완료 후) 공유용 링크 복사

---
![bg contain](img/02.png)

---
## 과일 분류 웹 서비스 만들기
* 준비하기
  - 샘플 웹 서비스 이동 > https://tm-image-demo.glitch.me/
  - Remix this site on Glitch 클릭하기
* Glitch 서비스는,
  - 웹 브라우저에서 웹 페이지를 만들고 수정하고 배포할 수 있는 서비스
  - 계정 없이도 사용할 수 있으나, 계정이 있으면 배포한 프로젝트를 유지할 수 있으며, 무료 또는 유로 버전이 있음

---
## 과일 분류 웹 서비스 만들기
* 코드 수정하기
  - index.html 선택하기
  - 복사한 모델의 URL 주소를 변경하기
    - let URL = '새로운 url 주소';
  - 완성된 웹 앱 확인하기
    - PREVIEW

---
![bg right:30% 80%](https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/1024px-ChatGPT_logo.svg.png)
## 과일 분류 웹 서비스 개선하기
* html, css, javascript 을 이용하여 코드 개선
* 인공지능 기술(챗봇)을 이용하여 코드 개선하기
  - chatGPT https://chat.openai.com/
  - chatGPT 는 미리 학습된 모델을 이용하는 대화형 인공지능 서비스
  - chatGPT 를 프로그래머라고 생각하고, 코드 개선을 요청하자.


---
## 인공지능 기술의 활용
* 인공지능 기술을 활용한다는 것은, 마치 다른 사람과 **함께 일을 한다는 것**이다.
* 누군가와 함께 일 하기 위해 갖춰야 할 능력은,
  - 기본적인 문제해결 능력 + 
  - 의사소통 능력(상대방의 언어로 설명하고 이해할 수 있는 능력) +
  - 배려, 기다림, 격려, ...

---
<style scoped>
li {
  font-size: 28px;
}
</style>
## 과일 분류 웹 서비스 개선하기
* chatGPT 에게 수정할 코드를 알려주기
  - "we are going to edit the html code."
  - "the html code to be modified is as follows."
* 화면에 보여지는 내용을 찾기
  - "tell me what to show on screen in this html code."
  - "in the model session, let me know what content is displayed on the screen."
* 화면에 보여지는 내용 수정하기
  - "Modify the phrases "Fruit classification web app" and "Show the fruit on the webcam" to be displayed on the screen. And show only the modified code from the previous code."

---
![bg contain](img/chatgpt-01.png)

---
![](img/chatgpt-02.png)
![](img/chatgpt-03.png)

---
![bg contain](img/chatgpt-04.png)

---
![bg contain](img/chatgpt-05.png)

---
![bg contain](img/chatgpt-06.png)


---
## 과일 분류 웹 서비스 개선하기
* chatGPT 는 그럴듯한 답변을 해준다. 
  - 질문을 이해하고 답하는 것이 아니라, 확률이 높은 단어를 연결하는 것이다.
  - 이를 인공 환각증상 (Hallucination) 이라고 한다.
  - 학습한 데이터의 편견(bias), 부족, 또는 모델의 한계 등으로 인해 발생한다.
* 답변을 그대로 믿지 말고 꼭, 확인해야 한다.

---
## 지도학습 Supervised Learning
* 지도 학습은, 
  - 정답을 알려주고 학습하는 방법 입니다.
* 다른 학습 방법은,
  - 비지도 학습 Unsupervised Learning, 정답을 알려주지 않고 학습 하는 방법
  - 강화 학습 Reinforcement Learning, 규칙만 알려주고 이기는 방향으로 학습하는 방법

---
<!--
_class: lead
_paginate: false
-->
# 나만의 인공지능 웹 서비스 설계 및 개발
1. 인공지능 웹 서비스를 설계할 수 있다.
2. 설계한 웹 서비스를 개발 및 개선할 수 있다.

---
## 프로젝트 설계하기
* 어떤 분류 모델을 만들 것인가?
* 연습장에 간단하게 스케치하기
* 아이디어 스케치를 기록하기

---
## 프로젝트 개발하기
* 분류 모델 학습하기
  - 데이터 수집 > 모델 학습 > 결과 검증
* 인공지능 웹 서비스 제작하기
  - 분류 모델 업로드 > 분류 모델 연결
* 또 다른 도구 활용하기
  - [Dancing with AI](https://dancingwithai.media.mit.edu/)

---
## 프로젝트 개선하기
* 웹 페이지 수정하기
  - 직접 수정하거나,
  - 인공지능과 함께 수정하거나
* 또는 프로젝트 수정하기(Dancing with AI)

---
## 프로젝트 공유 준비하기
* 공유 준비하기
  - 아이디어 스케치
  - 프로젝트 소개 문서
  - 시연 영상

---
<!--
_class: lead
_paginate: false
-->
# 공유 및 논의
1. 제작한 웹 서비스를 설명할 수 있다.
2. 인공지능 기술 활용에 대한 자신의 생각을 설명할 수 있다.

---
## 프로젝트 공유하기
* 프로젝트 소개 문서와 시연 영상 공유
* 긍정적인 피드백
* 개인 회고 작성

---
## 논의하기
* 인공지능 기술을 사용한다는 것은, 
  - 나와 내가 살고 있는 사회를 어떻게 변화시킬까?
  - 어떤 일이 없어질까? 어떤 일을 새롭게 할 수 있을까?
  - 사용해야 할까? 사용하지 말아야 할까?
  - 나는 무엇을 준비해야 할까?

---
<!--
_class: lead
_paginate: false
-->
# 인공지능의 개념
1. 인공지능의 개념을 설명할 수 있다.
2. 인공지능 기술을 활용하기 위해 필요한 능력을 설명할 수 있다.

---
## 지능 intelligence
* 지능이란, 지식을 다룰 수 있는 능력

* 지능을 구현하는 요인
  - 언어 language : 지식을 표현하는 방법
  - 학습 learning : 다른 사람이 표현한 지식을 내 것으로 만드는 방법
  - 추론 reasoning : 학습한 지식을 바탕으로 새로운 지식을 만드는 방법

---
## 인공지능 artificial intelligence
* 인공지능이란, 
  - 인간의 지능을 컴퓨팅 시스템으로 구현한 것
  - 기계를 인간 행동의 지식에서와 같이 행동하게 만드는 것
  - 인간처럼 사고하고, 행동하는 시스템

* 인공지능을 구현하는 요인
  - 언어 : 지식을 컴퓨터가 기억 및 처리하도록 다루는 방법
  - 학습 : 사람의 사고 방식을 기계에게 가르치는 방법
  - 추론 : 학습한 모델로 새로운 지식을 만드는 방법

---
![bg contain](https://www.azquotes.com/picture-quotes/quote-a-computer-would-deserve-to-be-called-intelligent-if-it-could-deceive-a-human-into-believing-alan-turing-29-79-78.jpg)

---
![bg left:60% 80%](https://ia800804.us.archive.org/BookReader/BookReaderImages.php?zip=/17/items/MIND--COMPUTING-MACHINERY-AND-INTELLIGENCE/MIND_jp2.zip&file=MIND_jp2/MIND_0000.jp2&id=MIND--COMPUTING-MACHINERY-AND-INTELLIGENCE&scale=2&rotate=0)

A. M. TURING, COMPUTING MACHINERY AND INTELLIGENCE, Mind, Volume 59, Issue 236, October 1950, Pages 433–460, https://doi.org/10.1093/mind/LIX.236.433




---
## 요약하기
* 과일 분류 모델 학습
  - 이미지 분류 모델 학습, 지도학습, 합성곱 신경망
* 과일 분류 웹 서비스 제작 및 개선
  - 웹 서비스 제작, 인공지능과 협업하여 코드 개선 
* 나만의 인공지능 웹 서비스 설계 및 개발
  - 설계 > 개발 > 개선

---
<!--
_class: lead
_paginate: false
-->
# Thanks! 🎉
"The best way to predict the future is to invent it." - [Alan Kay](https://www.ted.com/speakers/alan_kay)