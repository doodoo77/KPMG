# KPMG
<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=KPMG&fontSize=90" />



## 기술 

### 1) 욕설, 비난 필터링을 위한 윤리성 검사 (Text classification)

: Text_classification.py를 통해서 구현함

: 이를 구현하기 위한 NLP Task은 문장을 특정한 목적에 따라 숫자로 분류하는 Text classification

: BERT계열의 KcELECTRA 모델로 학습 윤리성 검사를 구현하였음

: 윤리성이 어긋난 문장에는 1, 윤리성에 어긋나지 않은 문장에는 0을 부여함


<img src="https://user-images.githubusercontent.com/97869551/219622157-8a0d1527-05b6-4d59-84d6-415793249c86.png" width="400" height="150"/>


---

### 2) 소프트 스킬 추출 및 감성분석을 위한 ABSA (Aspect-Based Sentiment Analysis)

: ABSA.py를 통해서 구현함

: 이를 구현하기 위한 NLP Task는 한문장에서 특정 측면에 해당하는 내용을 대상으로 감성분석하는 Aspect-Based Sentiment Analysis

: GPT-3 모델에 few-shot learning을 적용해 소프트 스킬 추출 및 감성분석을 진행함

: "창의성"과 같은 소프트 스킬을 추출하고, 문장 내에서 해당 소프트 스킬이 긍정으로 쓰였는지 부정으로 쓰였는지 판단함

<img src="https://user-images.githubusercontent.com/97869551/219627353-72b4df40-eb85-40a0-916c-a9f7476a7e06.png" width="800" height="150"/>

---

### 3) Narrative 피드백 제공을 위한 자연어 생성(Natural Language Generation)

: xx.py를 통해서 구현함

: 이를 구현하기 위한 NLP Task는 사전에 정해놓은 템플릿에 따라 자연어 생성을 하는 Template-based NLG

: GPT-3 모델을 사용하여 Narrative 피드백을 제공함

: GPT-3 모델의 출력인 (segment, aspect, and sentiment)를 바탕으로 "당신의 [segment]를 통해 [aspect]가 [sentiment]하게 보여지고 있어요!" 와 같은 Narrative를 제공함 

<img src="https://user-images.githubusercontent.com/97869551/219631071-1369ea8f-c3e4-44b8-a251-ac87677a6772.png" width="800" height="250"/>


---
