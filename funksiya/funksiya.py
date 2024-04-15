import aiohttp


async def downloader_media(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.botdownloader.uz/insta?url={url}") as response:
                return await response.json()
    except Exception as e:
        print(e)
        return False
