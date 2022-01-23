import json

for i in range(1, 51):
    document = []
    sentence = []
    form = []

    with open('C:\Git\국립국어원 개체명 분석 말뭉치 2020(버전 1.0)\EXNE21051700'+ str(i).zfill(2) +'.JSON', 'r', encoding = 'utf-8') as json_file:
        json_data = json.load(json_file)
        json_document = json_data['document']

    for i in range (0, len(json_document)):
        document.append(json_document[i])

    for i in range (0, len(document)):
        sentence.append(document[i]['sentence'])

    for i in range (0, len(sentence)):
        for j in range(0, len(sentence[i])):
            form.append(sentence[i][j]['form'])

    try:
        dataset = open(r'C:\Git\undergraduate\ner\dataset.txt', 'a', encoding = 'utf-8')

        for i in range (0, len(form)):
            dataset.write(form[i] + '\n')

        dataset.close()
    except:
        dataset = open(r'C:\Git\undergraduate\ner\dataset.txt', 'w', encoding = 'utf-8')

        for i in range (0, len(form)):
            dataset.write(form[i] + '\n')

        dataset.close()
