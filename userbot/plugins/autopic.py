import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio
import shutil

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

@command(pattern="^.autopic ?(tilt)", outgoing=True)
async def autopic(event):
    input_str = event.pattern_match.group(1)
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -5
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        if input_str == "tilt":
            file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n ⚡I IZ VIDHAYAK⚡ \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((50, 250), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 5
            await asyncio.sleep(65)
        except:
            return
