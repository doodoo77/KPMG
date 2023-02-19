from utils.functions import Loader, TextClassification, FewshotGPT3
import os
import numpy as np
import pandas as pd

# OpenAI 
import openai

My_OpenAI_key = "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"
openai.api_key = My_OpenAI_key


def main():
    
    # 윤리성 검사    
    if TextClassification(Loader('example', 'tc').get_path()) == 0:
    
        # 소프트 스킬 추출 및 감성 분석
        FewshotGPT3(
            Loader('example', 'tc').get_path(),
            Loader('fewshot', 'absa').get_path(),
            Loader('result', 'absa').get_path(),
        ).few_shot(temperature=0.5)

        # Narrative 피드백 생성
        FewshotGPT3(
            Loader('result', 'absa').get_path(),
            Loader('fewshot', 'nlg').get_path(),
            Loader('result', 'nlg').get_path(),
        ).few_shot(temperature=0)
    

if __name__ == '__main__':
    main()