from aiogram import types
from aiogram.dispatcher import FSMContext
import httpx
from aiogram.dispatcher.filters import Text
from bs4 import BeautifulSoup

from bot.dispacher import dp
from bot.buttons.reply import qalampir_news, daryo_news
from db.models import News_Daryo, News_Qalampir


@dp.message_handler(Text(qalampir_news) , state="news_site_set")
async def qalampir_func(msg : types.Message , state : FSMContext):
    html_code = httpx.get("https://qalampir.uz/").text
    soup = BeautifulSoup(html_code, "html.parser")
    data_list = soup.find_all("div", {"class": "news-card"})

    counter=0
    for i in data_list:
        if counter==5:
            break
        counter+=1
        img_url = i.img.get('src')
        created_at = i.find('span', {"class": "date"}).text
        title = i.find('a', {'class':"news-card-content-text"}).text
        img_name = f"images/{img_url.rsplit('/', 1)[1]}"
        async with state.proxy() as data:
            data['title'] = title.strip()
            data['img_url'] = img_url
            data['created_at'] = created_at
            data['img_name'] = img_name
            data = dict(data)
            News_Qalampir().insert_into(**data)

        await msg.bot.send_photo(msg.chat.id , img_url)
        await msg.answer(f"Title : {title.strip()} \n Created time : {created_at}")


@dp.message_handler(Text(daryo_news) , state="news_site_set")
async def daryo_func(msg:types.Message , state: FSMContext):
    html_code = httpx.get("https://daryo.uz/").text
    soup = BeautifulSoup(html_code, "html.parser")
    data_list = soup.find_all("article", {"class": "article__small border"})

    counter=0
    for i in data_list:
        if counter==5:
            break
        counter+=1
        img_url = "https://daryo.uz" + str(i.find('div', {"class": "article__pic"}).img.get('src'))
        if "None" in img_url:
            counter-=1
        else:
            created_at = i.find('time', {"class": "meta-date"}).text
            title = i.find('a', {'class':"article__link"}).text
            img_name = f"images/{img_url.rsplit('/', 1)[1]}"
            async with state.proxy() as data:
                data['title'] = title.strip()
                data['img_url'] = img_url
                data['created_at'] = created_at
                data['img_name'] = img_name
            data = dict(data)
            News_Daryo().insert_into(**data)

            await msg.bot.send_photo(msg.chat.id , img_url)
            await msg.answer(f"Title : {title.strip()} \n Created time : {created_at}")
