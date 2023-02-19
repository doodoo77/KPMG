#!pip install openai

import os
import openai

# OpenAI setup
My_OpenAI_key = "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"
openai.api_key = My_OpenAI_key

# ABSA function
def analysis_comment(temperature=0.5):

    # few-shot 예제 불러오기
    file_r = open('../ABSA_examples.txt','r', encoding='UTF-8')
    examples = file_r.read()
    file_r.close()

    # 코멘트 입력
    comment = input("코멘트를 입력하세요: ")
    text = examples + comment

    # ABSA 분석
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=temperature,
    max_tokens=512,
    )

    absa_text = response["choices"][0]["text"].strip()    
        
    # 분석 결과 저장
    file_w = open("../ABSA_output.txt", "w", encoding='UTF-8') 
    file_w.write(absa_text)
    file_w.close()
    
    # 분석 결과 출력
    print(absa_text)


# 이 사람은 작업 그룹을 이끄는 데 매우 효과적이며 참가자 간의 갈등을 해결할 수 있습니다. 하지만 반복적으로 점심 시간을 초과하여 업무 일정에 방해가 됩니다.
analysis_comment()