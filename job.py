from bs4 import BeautifulSoup
import requests
import time
import re


def createList(data):
    ls = data.split(",")
    length = len(ls)
    for i in range(length):
        ls[i] = ls[i].strip()
        ls[i].lower()
    return ls


print("Enter your skills")
data = input(">")
skills = createList(data)

print("Enter your experience level")
exp = input(">")

print("Put some skills that you are not unfamiliar with")
data = input(">")
print(f"Filtering out {data}")
unfamiliar_skill = createList(data)


def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords="
    for i in range(len(skills)):
        url = url + skills[i]
        if i != (len(skills) - 1):
            url = url + "%2C"
    url = url + "&txtLocation="
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text

        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(
                " ", ""
            )
            job_skills = (
                job.find("span", class_="srp-skills").text.replace(" ", "").lower()
            )
            more_info = job.header.h2.a["href"]
            years = job.li.text
            min_exp = min_exp = re.search(r"\d+", years).group()

            flag = 1
            for i in range(len(unfamiliar_skill)):
                if unfamiliar_skill[i] in job_skills:
                    flag = 0
            if exp < min_exp:
                flag = 0
            if flag:
                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"\nRequired Skills: {job_skills.strip()}")
                    f.write(f"\nMore Info: {more_info}")
                print(f"File saved: {index}")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait * 60)
