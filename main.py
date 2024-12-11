import requests
import json
from bs4 import BeautifulSoup as bs
url = "https://mgkct.minskedu.gov.by/%D0%BE-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%B4%D0%B6%D0%B5/%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B8%D0%B2"
page = requests.get(url)
teachers = []
soup = bs(page.text, "html.parser")
data = soup.findAll('div', class_='content taj')
for teacher in data:
    name = teacher.find("h3", class_="").text
    post = teacher.find("li", class_="tss").text
    teachers.append({"teacher_name": name, "Post": post[11:]})
for idx,teacher  in enumerate(teachers, 1):
    print(f'{idx}. Teacher: {teachers[idx-1]["teacher_name"]}; Post: {teachers[idx-1]["Post"]};')

def save_to_json(teachers,file="data.json"):
    with open(file,"w",encoding="utf-8")as f:
        json.dump(teachers, f, ensure_ascii=False, indent=4)

save_to_json(teachers)

def html(file="data.json",file_html="index.html"):
    with open(file,"r",encoding="utf-8")as f:
        teachers=json.load(f)
    
    html_cont='''
    <html>
    <head>
        <title>Список преподавателей МГКЦТ</title>
         <style>
            body {
                color: #000000;
            }
            table {
                background: #fff;
            }
            th, td {
                padding: 20px;
                border: 1px solid #000000;
                text-align: ceb;
            }
            th {
                background-color: #f2f2f2;
                color: #333;
            }
            h1 {
                text-align: center;
                margin-bottom: 40px;
            }
            p {
                text-align: center;
                margin-top: 40px;
            }
            a {
                color: #ff7e5f;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Список преподавателей МГКЦТ</h1>
            <table>
                <tr>
                    <th>№</th>
                    <th>ФИО преподавателя</th>
                    <th>Должность</th>
                </tr>
    '''

    # Добавление цитат в таблицу
    for idx, teacher in enumerate(teachers, 1):
        html_cont += f'''
        <tr>
            <td><h3>{idx}</h3></td>
            <td><h3>{teacher["teacher_name"]}</h3></td>
            <td><h3>{teacher["Post"]}<h3></td>
        </tr>
        '''

    # Завершение HTML-контента
    html_cont += '''
            </table>
        </div>
    </body>
    </html>
    '''

    # Запись HTML-контента в файл
    with open(file_html, "w", encoding="utf-8") as f:
        f.write(html_cont)
html()