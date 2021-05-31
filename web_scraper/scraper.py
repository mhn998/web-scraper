from typing import final
import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all("a" ,text='citation needed')
    print(f"{len(citations)} resources needs citation")
    return f"{len(citations)} resources needs citation"

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content , 'html.parser')
    citations = soup.find_all("a", text="citation needed")
    lst = []
    for p in citations:
        if not p in lst:
            lst.append(p)
    # print(lst)
    count , report = 1 , []
    for i in lst:
        section = i.find_parent('p')
        report.append(f'{count}) citation needed for -> {section.text}')
        count+= 1
    # final_answer = print(*report)
    return report

# get_citations_needed_count(URL)
# get_citations_needed_report(URL)






    