import asyncio
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='.')

# 생성된 토큰을 입력해준다.

# 봇이 구동되었을 때 보여지는 코드
@bot.event
async def on_ready():
    print('--------------------------------------')
    print("개발자 시원이#0105")
    print("ㅤ")
    print("봇 준비완료")
    print("ㅤ")
    print(bot.user.name)
    print("ㅤ")
    print(bot.user.id)
    print("ㅤ")
    print('--------------------------------------')
    game = discord.Game("우리집 관리")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command(pass_context=True)
async def 닉네임변경(ctx, user: str = None, nick=None):
    if not nick:
        return await ctx.send(f'{ctx.author.mention}, 변경할 닉네임을 적어주세요.')
    if not user:
        return await ctx.send(f'{ctx.author.mention}, 변경할 사용자를 멘션하거나 id를 적어주세요')
    try:
        member = await commands.MemberConverter().convert(ctx, user)
        await member.edit(nick=nick)
    except discord.ext.commands.errors.MissingRequiredArgument:
        return await ctx.send(f'{ctx.author.mention}, 변경할 사용자를 멘션하거나 id를 적어주세요')
    embed = discord.Embed(title='닉네임 변경', description=f'{member.mention}님의 별명이 관리자의 의해 변경되었습니다.\n\n변경된 닉네임: {nick}', color=0x00ff00)
    embed.set_footer(text=f'변경자: {ctx.author.name}')
    await ctx.send(embed=embed)

# 봇이 특정 메세지를 받고 인식하는 코드


client.run(token)