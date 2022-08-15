from loader import dp
from aiogram.types import ContentType, Message, InputFile, MediaGroup

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)

#photo_file_id = 'AgACAgQAAxkBAAICV2L1QMpPY2xw_UpqX8iaBwV982rPAALQuzEb5iOpU-T7nzaStK-AAQADAgADbQADKQQ'
photo_file_id_1 = 'AgACAgQAAxkBAAICeGL1Rh0pW9yKePC_63O8del6o3VHAALduzEb5iOpU77q3ub39WNuAQADAgADeAADKQQ'
photo_file_id_2 = ''
video_file_id='BAACAgQAAxkBAAICY2L1Q6ayiaUsFUsBBKxy7Ig1i75GAALCDwAC5iOpU4tTtxdMGjDzKQQ'
photo_bytes = InputFile(path_or_bytesio='media/fenek.jpg')


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    #We should pass whether photo_file_ud, photo_url or photo_bytes
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes)

@dp.message_handler(text='/video')
async def send_video(message: Message):
    chat_id = message.from_user.id
    #We should pass whether photo_file_ud, photo_url or photo_bytes
    await dp.bot.send_video(chat_id=chat_id, video=video_file_id)

@dp.message_handler(text='/album')
async def send_album(message: Message):
    album=MediaGroup()
    album.attach_photo(photo=photo_file_id_1)
    album.attach_photo(photo=photo_bytes)
    album.attach_video(video=video_file_id, caption='Descr')
    await message.answer_media_group(media=album)