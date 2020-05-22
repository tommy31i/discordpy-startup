# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzA4MTYxMjQzNTgzNjEwOTIx.Xrd-5w.Enjjcrf8tjIjI9Njevm3LlkaBsA'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/82':
        await message.channel.send('にゃう...')
    if message.content == '/あのバカども':
        await message.channel.send('https://cms2.suzuka-ct.ac.jp/cc/course/mod/attendance/view.php?id=20212')
   # if message.content == '/':
   #    await message.channel.send('にゃう...')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)