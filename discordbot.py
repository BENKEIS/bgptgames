import discord
import asyncio
import random
import os



client = discord.Client()

 #トークン
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("/tip bgpt 200 @🎮BGPT-GAMES"):

      if client.user != message.author:
       path=r"https://res.cloudinary.com/markbasser/image/upload/v1588046170/bgptgames/top"
       m = "【!bgpt】:point_left::point_left:Now enter this Command!```!bgpt```:point_up_2:このｺﾏﾝﾄﾞ“!bgpt”入力\n☑_Click on the hidden **BlackText** to see the result._\n☑_**黒塗**に結果_\n\n**BGPT GAMES NOW!**"+message.author.mention


       dirs = os.listdir( path )
       file = random.choice(dirs)
       image = image = path + "\\" + file

       await message.channel.send(m,file=discord.File(image))

       def check(m): #メッセージ内容をチェックする
            return m.content == "!bgpt" and m.author.id == message.author.id


       msg = await client.wait_for('message', check=check) 

       kakuritu = random.randint(1,100)
       if kakuritu>=98 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\1"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **ISo sorry！** ||  \n  --- ||    _**YOU LOST**_    ||---  \n || :skull_crossbones: 残念 **-200** BGPT ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=70 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\2"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **Sorry！**  ||\n  --- ||  _**You Lost**_  || --- \n ||:ghost: 残念 **-150** BGPT \n\n/tip bgpt 50 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=50 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\3"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **It's a shame！** || \n  --- || _ **You Lost**_  || --- \n ||:smiling_imp: 残念 **-100** BGPT \n\n/tip bgpt 100 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=30 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\4"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Even Fight！**  || \n  --- || _**Break Even!**_ || --- \n ||:smirk: **+-0** BGPT \n\n/tip bgpt 200 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=15 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\5"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations** :star2: ||  \n  --- || :star2: **You WIN** :star2: || --- \n || :smiley: **+100** BGPT \n\n/tip bgpt 300 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=10 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\6"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations** :star2:  ||  \n  --- || :dizzy::star2:**You WIN**:star2::dizzy: || --- \n || :dizzy::star_struck: ☆ **+500** BGPT ☆ \n\n/tip bgpt 700 {message.author.mention}  ||||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=7 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\7"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations!**:partying_face::tada: ||  \n  --- || :tada::star2::tada:**You Great Victory**:tada::star2::tada: ||--- \n || :tada::star2::tada: ☆☆ **+1000** BGPT ☆☆ \n\n/tip bgpt 1200 {message.author.mention}  ||||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=1 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\8"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations**:partying_face::tada: ||  \n  :partying_face:||:tada::star2::partying_face:**You Great Victory**:star2::partying_face::tada:||:partying_face:  \n  :partying_face:||:partying_face:☆☆☆ **+3000** BGPT ☆☆☆:partying_face:||:partying_face:||\n\n/tip bgpt 3200 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=0.4 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\9"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || :star2::tada::partying_face: **Congratulations!** :partying_face::tada::star2: ||   \n  --- :partying_face:||:tada::star2::tada:**☆You☆Great☆Victory☆**:tada::star2::tada:||:partying_face: --- \n  :partying_face:||:tada::star2::tada::partying_face::tada: ☆☆☆☆☆ **+7777.77** BGPT ☆☆☆☆☆:tada::partying_face::tada::star2::tada:||:partying_face: ||\n\n/tip bgpt 7977.77 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=40 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\10"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **For the time being！** || \n   --- ||    **You WON!**   || --- \n  :thinking: || 残念 **-200** || BGPT \n  :thinking: ||  ** 29coin :cut_of_meat: 29292.929 Get!** \n:meat_on_bone:  :cut_of_meat:\n\n/tip 29coin 29292.929 {message.author.mention}  || ")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=50 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\11"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **It's a shame！**  ||\n  --- ||   _**You Lost**_   || --- \n || :smiling_imp:  残念 **-200** BGPT || \n || **KenjCoin +50000 Get!** \n\n/tip kenj 50000 {message.author.mention}   ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=5 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\12"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **YOU Congratulations！**  ||\n  --- :star2::tada:** YOU WIN** :tada::star2: --- \n || :partying_face::tada::star2: **+77.77777 BEN** :star2::tada::partying_face: \n\n/tip BEN 77.77777 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=0.2 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\13"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || :star2::tada::partying_face: **Congratulations!** :partying_face::tada::star2: ||   \n   :partying_face:||:tada::star2::tada:**☆You☆Great☆Victory☆**:tada::star2::tada:||:partying_face:  \n  :partying_face::tada:||:star2::tada::star2::partying_face::tada: ☆☆☆☆☆ **+777.7777** BEN ☆☆☆☆☆ :tada::partying_face::star2::tada::star2:||:tada::partying_face: ||\n\n/tip BEN 7777.777 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=3 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\14"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  :smiling_imp:**OH MY GOD!**:smiling_imp:  ||\n  --- ||  _**You Lost**_  || --- \n  ||:ghost: 残念 :skull_crossbones:**--200** BGPT +93149.31:skull_crossbones:dappuncoin\n\n/tip dappuncoin 93149.31 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=30 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\15"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **ThankYou!**  ||\n  --- ||  _**Your🌈☔I**_  || --- \n ||Your Tip Rained:umbrella: into an active user. @everyone is grateful. Thank you! \n\n/rain BGPT 200 ActiveUserOnly {message.author.mention}  ||\n <:BGPT02:698471366004965406><:good01:699581068285706301>🌈☔It Rains")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=20 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\16"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **Thanks♡**  ||\n  --- ||  _**You Rain**_  || --- \n ||<:good01:699581068285706301> -200 BGPT→**400 JPYN** RAIN  \n\n /rain JPNY 50 ActiveUserOnly  || \n <:JPYNdisco:698471276498649168>🌈☔It Rains<:jhlo:700932650944299098>  ||")  # f文字列（フォーマット済み文字列リテラル）
       
       
               
       dirs = os.listdir( path )
       file = random.choice(dirs)
       image = image = path + "\\" + file

       await message.channel.send(message.author.mention,file=discord.File(image),delete_after=30.0)


@client.event
async def on_message(message):
    if message.content.startswith("/tip bgpt 200 <@703768008098709596>"):

      if client.user != message.author:
       path=r"https://res.cloudinary.com/markbasser/image/upload/v1588046170/bgptgames/top"
       m = "【!bgpt】:point_left::point_left:Now enter this Command!```!bgpt```:point_up_2:このｺﾏﾝﾄﾞ“!bgpt”入力\n☑_Click on the hidden **BlackText** to see the result._\n☑_**黒塗**に結果_\n\n**BGPT GAMES NOW!**"+message.author.mention


       dirs = os.listdir( path )
       file = random.choice(dirs)
       image = image = path + "\\" + file

       await message.channel.send(m,file=discord.File(image))

       def check(m): #メッセージ内容をチェックする
            return m.content == "!bgpt" and m.author.id == message.author.id


       msg = await client.wait_for('message', check=check) 

       kakuritu = random.randint(1,100)
       if kakuritu>=98 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\1"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **ISo sorry！** ||  \n  --- ||    _**YOU LOST**_    ||---  \n || :skull_crossbones: 残念 **-200** BGPT ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=70 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\2"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **Sorry！**  ||\n  --- ||  _**You Lost**_  || --- \n ||:ghost: 残念 **-150** BGPT \n\n/tip bgpt 50 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=50 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\3"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **It's a shame！** || \n  --- || _ **You Lost**_  || --- \n ||:smiling_imp: 残念 **-100** BGPT \n\n/tip bgpt 100 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=30 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\4"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Even Fight！**  || \n  --- || _**Break Even!**_ || --- \n ||:smirk: **+-0** BGPT \n\n/tip bgpt 200 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=15 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\5"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations** :star2: ||  \n  --- || :star2: **You WIN** :star2: || --- \n || :smiley: **+100** BGPT \n\n/tip bgpt 300 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=10 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\6"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations** :star2:  ||  \n  --- || :dizzy::star2:**You WIN**:star2::dizzy: || --- \n || :dizzy::star_struck: ☆ **+500** BGPT ☆ \n\n/tip bgpt 700 {message.author.mention}  ||||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=7 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\7"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations!**:partying_face::tada: ||  \n  --- || :tada::star2::tada:**You Great Victory**:tada::star2::tada: ||--- \n || :tada::star2::tada: ☆☆ **+1000** BGPT ☆☆ \n\n/tip bgpt 1200 {message.author.mention}  ||||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=1 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\8"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **Congratulations**:partying_face::tada: ||  \n  :partying_face:||:tada::star2::partying_face:**You Great Victory**:star2::partying_face::tada:||:partying_face:  \n  :partying_face:||:partying_face:☆☆☆ **+3000** BGPT ☆☆☆:partying_face:||:partying_face:||\n\n/tip bgpt 3200 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=0.4 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\9"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || :star2::tada::partying_face: **Congratulations!** :partying_face::tada::star2: ||   \n  --- :partying_face:||:tada::star2::tada:**☆You☆Great☆Victory☆**:tada::star2::tada:||:partying_face: --- \n  :partying_face:||:tada::star2::tada::partying_face::tada: ☆☆☆☆☆ **+7777.77** BGPT ☆☆☆☆☆:tada::partying_face::tada::star2::tada:||:partying_face: ||\n\n/tip bgpt 7977.77 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=40 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\10"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || **For the time being！** || \n   --- ||    **You WON!**   || --- \n  :thinking: || 残念 **-200** || BGPT \n  :thinking: ||  ** 29coin :cut_of_meat: 29292.929 Get!** \n:meat_on_bone:  :cut_of_meat:\n\n/tip 29coin 29292.929 {message.author.mention}  || ")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=50 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\11"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **It's a shame！**  ||\n  --- ||   _**You Lost**_   || --- \n || :smiling_imp:  残念 **-200** BGPT || \n || **KenjCoin +50000 Get!** \n\n/tip kenj 50000 {message.author.mention}   ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=5 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\12"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **YOU Congratulations！**  ||\n  --- :star2::tada:** YOU WIN** :tada::star2: --- \n || :partying_face::tada::star2: **+77.77777 BEN** :star2::tada::partying_face: \n\n/tip BEN 77.77777 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=0.2 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\13"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  || :star2::tada::partying_face: **Congratulations!** :partying_face::tada::star2: ||   \n   :partying_face:||:tada::star2::tada:**☆You☆Great☆Victory☆**:tada::star2::tada:||:partying_face:  \n  :partying_face::tada:||:star2::tada::star2::partying_face::tada: ☆☆☆☆☆ **+777.7777** BEN ☆☆☆☆☆ :tada::partying_face::star2::tada::star2:||:tada::partying_face: ||\n\n/tip BEN 7777.777 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=3 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\14"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  :smiling_imp:**OH MY GOD!**:smiling_imp:  ||\n  --- ||  _**You Lost**_  || --- \n  ||:ghost: 残念 :skull_crossbones:**--200** BGPT +93149.31:skull_crossbones:dappuncoin\n\n/tip dappuncoin 93149.31 {message.author.mention}  ||")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=30 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\15"
                await message.channel.send(f"**<:BGPT02:698471366004965406> 200_BGPT(Max BET)_**  \n:white_check_mark:  ||  **ThankYou!**  ||\n  --- ||  _**Your🌈☔I**_  || --- \n ||Your Tip Rained:umbrella: into an active user. @everyone is grateful. Thank you! \n\n/rain BGPT 200 ActiveUserOnly {message.author.mention}  ||\n <:BGPT02:698471366004965406><:good01:699581068285706301>🌈☔It Rains")  # f文字列（フォーマット済み文字列リテラル）
       elif kakuritu>=20 :
                path=r"C:\Users\MAKOTO\Desktop\BGPT-SLOT\tuika\16"

       
               
       dirs = os.listdir( path )
       file = random.choice(dirs)
       image = image = path + "\\" + file

       await message.channel.send(message.author.mention,file=discord.File(image),delete_after=30.0)




client.run(token)


