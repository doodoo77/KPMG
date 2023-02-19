#!pip install openai

import os
import openai

# OpenAI setup
My_OpenAI_key = "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"
openai.api_key = My_OpenAI_key

# NLG funciton
def generate_feedback(temperature=0):

    # few-shot 예제 불러오기
    file_r = open('../NLG_examples.txt','r', encoding='UTF-8')
    examples = file_r.read()
    file_r.close()

    # ABSA 분석 결과 불러오기
    file_absa = open('../ABSA_output.txt','r', encoding='UTF-8')
    absa = file_absa.read()
    text = examples + absa
    file_absa.close()

    # Narrative 피드백 생성
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=temperature,
    max_tokens=512,
    )

    narrative_feedback = response["choices"][0]["text"].strip()    
        
    # Narrative 피드백 저장
    file_w = open("NLG_output.txt", "w", encoding='UTF-8') 
    file_w.write(narrative_feedback)
    file_w.close()
    
    # Narrative 피드백 출력
    print(narrative_feedback)


generate_feedback()