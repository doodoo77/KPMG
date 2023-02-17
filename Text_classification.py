import numpy as np 
import pandas as pd

import os
for dirname, _, filenames in os.walk('../KPMG/korean-hate-speech-detection/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
        
from transformers import pipeline

# 유해한 문장 필터링을 위한 모델을 불러오기
pipe = pipeline('text-classification', model='beomi/beep-KcELECTRA-base-hate', device=0)

#예시
pipe("안녕하세요")

#비속어 감지 데이터셋 불러오기
df = pd.read_csv('../KPMG/korean-hate-speech-detection/test.hate.no_label.csv')

df['label'] = df['comments'].map(lambda x: pipe(x)[0]['label'])
df.label.value_counts()

# 라벨별로 무해한 문장은 0, 유해한 문장들은 1,2로 라벨링하기
LABEL_DIC = {
    'none': 0,
    'offensive': 1,
    'hate': 2,
}
df['label'] = df['label'].map(lambda x: LABEL_DIC[x])

df.to_csv('./submission.csv', index=None)
!head -n 10 submission.csv
