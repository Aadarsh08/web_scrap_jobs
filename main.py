from bs4 import BeautifulSoup
import requests
import time
print("Put some skill which you are familiar with")
familiar_skill = input(">")
print("Filtering out")
def find_jobs():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&txtLocation=&cboWorkExp1=-1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_="srp-job-bx")
    for index,job in enumerate(jobs):
        company_name = job.h4.text
        more_info = job.h3.a['href']
        skills = soup.find('div', class_="srp-keyskills").text
        if familiar_skill in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f" Comapany name : {company_name}\n")
                f.write(f"Required skills : {skills}\n")
                f.write(f"More info: {more_info}")
            print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait*60)
