import json
from aiogram import Bot, Dispatcher, executor, types
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

# @dp.message_handler(commands="start")
# async def start(message: types.Message):
# 	await message.reply("Парсинг проектов на kwork")

@dp.message_handler(commands="all_project")
async def get_all_news(message: types.Message):
	with open("news_dict.json", encoding='utf-8') as file:
		news_dict = json.load(file)

	for k, v in sorted(news_dict.items()):
		news = f"{v['article_url']}\n" \
			   f"{v['article_title']}\n" \
			   f"{v['article_price']}\n"

		await message.answer(news)


if __name__ == '__main__':
	executor.start_polling(dp)