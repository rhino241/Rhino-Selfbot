import discord
from discord.ext import commands
import asyncio

from utils import log, generate_random_string, random_cooldown
import config_selfbot
import langs


class RaidCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.is_spamming: bool = False

    @commands.command()
    async def kickall(self, ctx: commands.Context):
        if ctx.author.guild_permissions.kick_members:
            members = ctx.guild.members
            
            await ctx.message.edit(langs.raid_in_process[config_selfbot.lang])

            log.separate_text("KICK ALL")

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.kick(reason=f"{config_selfbot.kick_reason} {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id}")
                    await asyncio.sleep(random_cooldown(0.5, 2))

            log.separate("KICK ALL")

            await ctx.message.edit(langs.raid_kick_all_success[config_selfbot.lang], delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(langs.raid_error_permisssion[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def banall(self, ctx: commands.Context):
        if ctx.author.guild_permissions.ban_members:
            members = ctx.guild.members

            await ctx.message.edit(langs.raid_in_process[config_selfbot.lang])

            log.separate_text("BAN ALL")

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.ban(reason=f"{config_selfbot.ban_reason}. {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id}")
                    await asyncio.sleep(random_cooldown(0.5, 1.9))

            log.separate("BAN ALL")

            await ctx.message.edit(langs.raid_ban_all_success[config_selfbot.lang], delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(langs.raid_error_permisssion[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def destroy(self, ctx: commands.Context):
        if ctx.author.guild_permissions.administrator:
            await ctx.message.delete()

          
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                except:
                    pass
                
           
            for user in list(ctx.guild.members):
                try:
                    await user.ban()
                except:
                    pass
                
           
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                except:
                    pass
                
          
            try:
                await ctx.guild.edit(
                    name="Join Discord.gg/wra",
                    description="https://discord.gg/wra",
                    reason="https://discord.gg/wra",
                    icon=None,
                    banner=None
                )
            except:
                pass
            
            
            for _ in range(250):
                await ctx.guild.create_text_channel(name="Nuked by rhino241")

            
            for _ in range(250):
                await ctx.guild.create_role(name="Nuked by rhino241", color=RandomColor())
        else:
            await ctx.message.edit("You do not have permission to use this command.", delete_after=10)

    
    @commands.command()
    async def spam(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        content = ctx.message.content.replace(f"{message_split[0]} {message_split[1]} ", "")

        try:
            count = int(message_split[1]) - 1
        except Exception:
            await ctx.message.edit(f"{langs.spam_invalid[config_selfbot.lang]}!", delete_after=config_selfbot.deltime)
            return
        
        if count >= 100:
            await ctx.message.edit(langs.spam_too_much[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            message_split[2]
        except Exception:
            await ctx.message.edit(langs.raid_dm_all_fail[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        if not self.is_spamming:
            self.is_spamming = True

            await ctx.message.edit(content)

            for i in range(count):
                await ctx.channel.send(content)
                await asyncio.sleep(random_cooldown(0.1, 0.5))
            self.is_spamming = False
        else:
            await ctx.message.edit(langs.spam_cooldown[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def flood(self, ctx: commands.Context):
        flood_spam = """_ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _"""
        await ctx.message.edit(flood_spam)
        for i in range(2):
            await ctx.channel.send(flood_spam)
            await asyncio.sleep(0.5)


