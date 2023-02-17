import os
import openai

My_OpenAI_key = "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"
openai.api_key = My_OpenAI_key

def analysis_comment(temperature=0.5):

    # few-shot 예제 불러오기
    f = open('/content/drive/MyDrive/KPMG/ABSA/examples.txt','r')
    examples = f.read()

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

    # 분석 결과 출력
    print(response["choices"][0]["text"].strip())
    
    # 이 사람은 작업 그룹을 이끄는 데 매우 효과적이며 참가자 간의 갈등을 해결할 수 있습니다. 하지만 반복적으로 점심 시간을 초과하여 업무 일정에 방해가 됩니다.
analysis_comment()
