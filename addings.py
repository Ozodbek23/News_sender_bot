import httpx
from bs4 import BeautifulSoup

# response = httpx.get("https://qalampir.uz/")
# html_code = response.text
#
# soup = BeautifulSoup(html_code , "html.parser")
#
# # print(soup.find_all("div" , {"class" : "article__pic"})[1].find('img').get('src'))
# data_daryo = soup.find_all("article" , {"class" : "article__small border"})
# for data in data_daryo:
#     title_n = data.find("div" , {"class" : "article__info border"}).title
#     print(title_n)



from datetime import datetime
# for i in range(2):
#     print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))



import os



# =============KUN.UZ================
#
# def get_data():
#     html_code = httpx.get("https://kun.uz/").text
#     soup = BeautifulSoup(html_code, "html.parser")
#     data_list = soup.find_all("div", {"class": "small-news"})
#
#     for i in data_list:
#         img_url = i.img.get('src')
#         img_response = httpx.get(img_url)
#         created_at = i.span.text
#         title = i.find('a', {'class':"small-news__title"}).text
#         img_name = f"images/{img_url.rsplit('/', 1)[1]}"
#         # with open( img_name, "wb") as f:
#         #     f.write(img_response.content)
#             # f.write(img_response.content)


# get_data()



# =============Qalampir.UZ================


# def get_data():
#     html_code = httpx.get("https://qalampir.uz/").text
#     soup = BeautifulSoup(html_code, "html.parser")
#     data_list = soup.find_all("div", {"class": "news-card"})
#
#
#     counter=0
#     for i in data_list:
#         if counter==5:
#             break
#         counter+=1
#         img_url = i.img.get('src')
#         img_response = httpx.get(img_url)
#         created_at = i.find('span', {"class": "date"}).text
#         title = i.find('a', {'class':"news-card-content-text"}).text
#         img_name = f"images/{img_url.rsplit('/', 1)[1]}"
#         print(img_url)
#         # with open( img_name, "wb") as f:
#         #     f.write(img_response.content)
#         #     f.write(img_response.content)
#
#
# get_data()





# =============Daryo.UZ================


def get_data():
    html_code = httpx.get("https://daryo.uz/").text
    soup = BeautifulSoup(html_code, "html.parser")
    data_list = soup.find_all("article", {"class": "article__small border"})

    counter=0
    for i in data_list:
        if counter==5:
            break
        counter+=1
        img_url = "https://daryo.uz"+str(i.find('div' , {"class": "article__pic"}).img.get('src'))
        # img_response = httpx.get(img_url)
        created_at = i.find('time', {"class": "meta-date"}).text
        title = i.find('a', {'class':"article__link"}).text
        img_name = f"images/{img_url.rsplit('/', 1)[1]}"
        # with open( img_name, "wb") as f:
        #     f.write(img_response.content)
        #     f.write(img_response.content)
get_data()