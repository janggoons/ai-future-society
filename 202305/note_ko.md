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
* 과일 분류 웹 서비스 제작
* 과일 분류 웹 서비스 개선
* 나만의 인공지능 웹 서비스 설계
* 나만의 인공지능 웹 서비스 개발
* 공유 및 논의

---
<!--
_class: lead
_paginate: false
-->
# 과일 분류 모델 학습
1. 과일 분류 학습을 위한 데이터를 수집할 수 있다.
2. 지도학습을 통해 모델을 학습시킬 수 있다.

---
![bg right:20% contain](https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80)
## 사람은 과일을 어떻게 구분할까?
- 사람의 눈으로 과일을 볼 수 있다.
- 과일의 모습과 이전에 본 과일의 모습을 기억하여,
- 기억 속의 과일의 색, 모양, 향, 맛 등을 비교하여 과일을 구분한다.
- 사람 뇌의 뉴런들이 어떤 일을 하여 기억하고, 비교한다.

---
![bg right:20% contain](https://cdn.pixabay.com/photo/2015/11/28/10/52/binary-1066983_1280.jpg)
## 컴퓨터는 과일을 어떻게 구분할까?
- 컴퓨터에 연결된 카메라로 과일을 볼 수 있다.
- 과일의 모습은 숫자(0과 1로 된 이진수)로 저장되고, 
- 숫자들을 잘 계산하여, 대표되는 값을 찾고, 이 값 들과 다른 과일 이미지의 대표값과 비교한다.
- 컴퓨터가 수 많은 숫자들을 계산하고, 값을 비교한다.

---
![bg contain](https://mblogthumb-phinf.pstatic.net/MjAxNjEwMjRfMzkg/MDAxNDc3MzAzODcyNTQ5.ggZaroU1baErQDST2_tCNL0dyaX39MkzX82O-e0Y3sgg.idDEyFLI_BDSa_1KPZ8flst-TzgXdOmDfeGndF3kImcg.JPEG.msnayana/%EC%BB%A8%EB%B2%8C%EB%A5%98%EC%85%98.jpg?type=w2)
## 컴퓨터가 사물을 인식하는 한 가지 방법(CNN)

---
## 컴퓨터가 사물을 인식하는 한 가지 방법(CNN)
* convo

---
## 과일 분류 모델 만들기
* 머신러닝 machine learning
  - 기계가 사람 처럼, 새로운 것을 배우는 과정을 머신러닝 이라고 한다.
  - 한 번 학습하면 과일의 이름을 기억할 수 있다.
  - 새로운 과일을 보여준다면, 이름을 알 수 있을까?

---
## 과일 분류 모델 만들기
* 컴퓨터에게 과일을 학습시키자.
  - 학습할 과일을 준비한 뒤, 
  - 컴퓨터에게 과일의 이름을 알려주고 기억하게 한다.
  - 조금 다른 모습의 같은 과일을 보여주고,
  - 과일의 이름을 맞추도록 한다.

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

---
## 과일 분류 웹앱 만들기
* 웹앱 web application
  - 웹 브라우저에서 실행되는 소프트웨어
* 준비하기
  - Export Model > Upload my model > (업로드 완료 후) 공유용 링크 복사

---
![bg contain](img/02.png)

---
## 과일 분류 웹앱 만들기
* 준비하기
  - 샘플 웹 앱 이동 > https://tm-image-demo.glitch.me/
  - Remix this site on Glitch 클릭하기

---
## 과일 분류 웹앱 만들기
* 코드 수정하기
  - index.html 선택하기
  - 복사한 모델의 URL 주소를 변경하기
    - let URL = '새로운 url 주소';
  - 완성된 웹 앱 확인하기
    - PREVIEW

---
## 과일 분류 웹앱 개선하기
* chatGPT 를 이용하여 코드 개선하기
  - chatGPT https://chat.openai.com/
  - chatGPT 는 미리 학습된 모델을 이용하는 대화형 인공지능 서비스
  - chatGPT 를 프로그래머라고 생각하고, 코드 개선을 요청하자.
  - 목표는, 우리가 만든 과일 분류 모델에 맞도록 설명을 수정하는 것이다.

---
<style scoped>
li {
  font-size: 28px;
}
</style>
## 과일 분류 웹앱 개선하기
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
## 과일 분류 웹앱 개선하기
* chatGPT 는 그럴듯한 답변을 해준다. (Hallucination)
* 답변을 그대로 믿지 말고 꼭, 확인해야 한다.

---
## 지도학습 Supervised Learning
* 지도 학습은, 
  - 정답을 알려주고 학습하는 방법 입니다.
* 다른 학습 방법은,
  - 정답을 알려주지 않고 학습 하는 방법은 비지도 학습 Unsupervised Learning
  - 규칙만 알려주고 이기는 방향으로 학습하는 방법은 강화 학습 Reinforcement Learning

---
## 지도학습 Supervised Learning
* 사람의 학습과 컴퓨터 학습의 차이는 무엇일까요?
  - 사람은 적은 수의 경험과 사례로도 학습할 수 있다. 사람은 잘 알지 못하는 분야에 대해서 엉뚱하게 상상하거나, 가설을 세우고 검증하는 과정에서 다양한 실패를 통해 새로운 정보를 발견할 수 있다.
  - 컴퓨터는 사람보다 훨씬 많은 학습 데이터가 필요하다. 컴퓨터는 제공되는 데이터가 아주 많다면, 보다 정확하게 분류하는 모델을 만들 수 있다. 사람보다 빠르고 때로는 더 정확하게 분류한다. 

---
## 논의하기
* 컴퓨터, 인공지능, 프로그램을 사용한다는 것은,
  - 내가 살고 있는 사회 세상은 어떻게 변화될까?
  - 어떤 일이 없어질까? 어떤 일을 할 수 있을까? 
  - 컴퓨터는 우리를 이롭게 하는 것일까? 불편하게 하는 것일까?
* 앞으로 무엇을 어떻게 가르쳐야 할까?
  - 프로그래밍 언어와 코드 작성하는 방법을 가르쳐야 할까?
  - 해야 되는 것과 하지 말아야 할 것은 무엇일까?

---
<!--
_class: lead
_paginate: false
-->
# Thanks! 🎉 
