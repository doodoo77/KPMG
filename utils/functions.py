import os
import numpy as np
import pandas as pd
from transformers import pipeline


class Loader:
    """ 텍스트 데이터 경로 로더 """
    
    def __init__(self, purpose, task):
        self.purpose = purpose
        self.task = task
        
    def get_path(self, root:str='./data'):
        file_name = self.purpose + '_' + self.task + '.txt'
        return os.path.join(root, file_name)
        
        
class TextClassification():
    """ KcELECTRA 분류기를 사용한 윤리성 검사 """
    
    def __init__(self, input_path):
        self.input_path = input_path
        
        
    def get_label(self):
        input_text = open(self.input_path, 'r', encoding='UTF-8').read()
        
        pipe = pipeline('text-classification', model='beomi/beep-KcELECTRA-base-hate')
        return pipe(input_text)

    
class FewshotGPT3():
    """ GPT-3를 활용한 few-shot learning """
    
    def __init__(self, input_path, examples_path, output_path):
        self.input_path = input_path
        self.examples_path = examples_path
        self.output_path = output_path
    
    def few_shot(self, temperature):
        
        input_text = open(self.input_path, 'r', encoding='UTF-8').read()
        examples_text = open(self.examples_path, 'r', encoding='UTF-8').read()
        prompt = examples_text + input_text

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=512,
        )

        result = response["choices"][0]["text"].strip()
        
        open(self.output_path, 'w', encoding='UTF-8').write(result)