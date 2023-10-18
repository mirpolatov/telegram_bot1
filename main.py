from aiogram import Dispatcher, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
import asyncio
import keyboard_button as kb

#

# from datetime import datetime
#
# from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

#
# engine = create_engine('postgresql://postgres:1@localhost:5432/tg_bot')
#
# Base = declarative_base()

#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(String(255))
#     username = Column(String(255), nullable=True)
#     first_name = Column(String(255), nullable=True)
#     datetime_add = Column(DateTime, default=datetime.utcnow)
#
#
# class Reklama_image(Base):
#     __tablename__ = 'reklama_image'
#
#     id = Column(Integer, primary_key=True)
#     photo = Column(String(300))
#     text = Column(Text)
#
#
# class Reklama_video(Base):
#     __tablename__ = 'reklama_video'
#     id = Column(Integer, primary_key=True)
#     video = Column(String(300))
#     text = Column(Text)
#
#
# Session = sessionmaker(bind=engine)
# session = Session()
# # Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# '==============================================================================='

token = Bot(token='6541034640:AAH0YNRdMzILMsNY_Nk5QZkKPGrjb0IdUK0')
dp = Dispatcher()


class Form(StatesGroup):
    photo = State()
    text = State()


class Form1(StatesGroup):
    video = State()
    text = State()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    if message.from_user.id == 698920892 or message.from_user.id == 1930798399:
        await message.answer('Hello admin', reply_markup=kb.main_rp)

        # users = User(user_id=message.from_user.id, username=message.from_user.username,
        #                  first_name=message.from_user.first_name)
        #     session.add(users)
        #     session.commit()
        #     await message.answer('Salom Admin ', reply_markup=kb.main_rp)
        # else:
        #     users = User(user_id=message.from_user.id, username=message.from_user.username,
        #                  first_name=message.from_user.first_name)
        #     session.add(users)
        #     session.commit()
    else:
        await message.answer_photo(
            photo='https://img.freepik.com/premium-photo/portrait-brutal-man-construction-helmet-industrial-theme_949828-5001.jpg?size=626&ext=jpg&ga=GA1.2.7780508.1692694161&semt=sph',
            caption="Assalomu alekum.\n  🇺🇿Vatanga xizmat ustalari. \n  🏠Tom yopamiz tez va sifatli \n 🩸Boyoq qilamiz \n 🌪 ora qazish. \n🏠 Qum suvoq. \n   💦 rodmint. \n  ⚡️ Elektrika. \n  🏞 Aboy. \n   Kafel. \n  🪚 Tarket. \n  🏠 Travertin.  \n  📏 Tyaga. \n  📉 Gipskardon. \n ⚡️ Plastik. \n ⚡️ Nalivnoy pol. \n🔑 Pod klyuch  hzmatlarimiz. bor, sfatli.  \n  Murojat uchun, \n ☎️ + 998991884050  \n ☎️ + 998901884050   \n",
            reply_markup=kb.countries_button)


@dp.message(F.text == 'Rasmli reklama qoyish')
async def rek_photo(message: Message, state: FSMContext):
    if message.from_user.id == 698920892 or message.from_user.id == 1930798399:
        await state.set_state(Form.photo)
        await message.answer('Rasm qoshing ')
    else:
        await message.answer('Siz admin emassiz ❌')


p = None


@dp.message(Form.photo)
async def rek_photo(message: Message, state: FSMContext):
    global p
    p = message.photo[-1].file_id
    await state.set_state(Form.text)
    # p = Reklama_image(photo=photo)
    await message.answer('Tekst qoshing ')


t = None


@dp.message(Form.text)
async def rek_text(message: Message, state: FSMContext):
    global t
    t = message.text
    # session.add(p)
    # session.commit()
    await message.answer_photo(photo=p, caption=t, reply_markup=kb.countries_button)
    await state.clear()


# '==============================================================================================================='

@dp.message(F.text == 'Videoli reklam qoyish')
async def rek_video(message: Message, state: FSMContext):
    if message.from_user.id == 698920892 or message.from_user.id == 1930798399:
        await state.set_state(Form1.video)
        await message.answer('Video qoshing ')
    else:
        await message.answer('Siz admin emassiz ❌')


v = None


@dp.message(Form1.video)
async def rek_video(message: Message, state: FSMContext):
    global v
    v = message.video.file_id
    await state.set_state(Form1.text)
    # v = Reklama_video(video=video)
    await message.answer('Videoga matn yozing')


t1 = None


@dp.message(Form1.text)
async def rek_text(message: Message, state: FSMContext):
    global t1
    t1 = message.text
    # session.add(v)
    # session.commit()
    await message.answer_video(video=v, caption=t1, reply_markup=kb.countries_button)
    await state.clear()


#
async def main():
    await dp.start_polling(token)


if __name__ == '__main__':
    asyncio.run(main())

#
#
#
# -1731508961


# @dp.message(F.text == 'Reklamani guruhlarga tarqatish')
# async def send_ad(message: Message):
#     send_rek = session.query(Reklama_image).all()
#     chat_id = [-4089381708, -1001886565758, -1001731508961]
#     for j in chat_id:
#         for i in send_rek:
#             ad_photo = i.photo
#             ad_text = i.text
#             await token.send_photo(j, ad_photo, caption=ad_text, reply_markup=kb.countries_button)
#             await message.answer("Reklama muvaffaqiyatli jo'natildi!")
