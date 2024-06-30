import discord
from discord.ext import commands
import datetime
import time
from utils import rpc, log

import config_selfbot
import langs


class RichPresenceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.today_date = datetime.datetime.today()

    @commands.command()
    async def rpc_details(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_details", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Details: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_name(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_name", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Name: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_state(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_state", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| State: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_url(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("streaming_url", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Stream URL: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_large_image(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("large_image", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Large Image: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_large_text(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("large_text", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Large image text: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_small_image(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("small_image", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Small Image: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_small_text(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("small_text", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Small image text: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_button_text_one(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_button_one", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️| Button One Text: `{message_content}`", delete_after=config_selfbot.deltime)

    @commands.command()
    async def rpc_button_text_two(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_button_two", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        try:
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=activity,
                                           afk=True,
                                           idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
        except Exception as e:
            log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               edit_settings=False)
                log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

        await ctx.message.edit(f"🕹️|Button Text Two: `{message_content}`", delete_after=config_selfbot.deltime)

    """ # WAITING FOR DISCORD.PY-SELF TO ADD BUTTON LINKS
    @commands.command()
    async def rpc_button_link_one(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        rpc.edit_variable_json("activity_button_one_answer", message_content)
        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                       activity=activity,
                                       afk=True,
                                       idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day),
                                       edit_settings=False)

        await ctx.message.edit(f"🕹️| Button One Link: `{message_content}`")
        await asyncio.sleep(deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_button_link_two(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        rpc.edit_variable_json("activity_button_two_answer", message_content)
        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                    timestamps={"start": time.time()},
                                    assets=assets,
                                    application_id=config_selfbot.application_id,
                                    buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                       activity=activity,
                                       afk=True,
                                       idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day),
                                       edit_settings=False)

        await bot.change_presence(status=config_selfbot.status_activity if rpc.read_variable_json("status_activity") == "VOID" else rpc.read_variable_json("status_activity"),
                                afk=afk,
                                activity=selfcord.Activity.Game(name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                                                    buttons={config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"): config_selfbot.activity_button_one_answer if rpc.read_variable_json("activity_button_one_answer") == "VOID" else rpc.read_variable_json("activity_button_one_answer"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two"): config_selfbot.activity_button_two_answer if rpc.read_variable_json("activity_button_two_answer") == "VOID" else rpc.read_variable_json("activity_button_two_answer")},
                                                                    key=config_selfbot.image_key if rpc.read_variable_json("image_key") == "VOID" else rpc.read_variable_json("image_key"), 
                                                                    application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                    )
                                                                    )
        await ctx.message.edit(f"🕹️| Button Link Two: `{message_content}`")
        await asyncio.sleep(deltime)
        await ctx.message.delete()
    """

    @commands.command()
    async def rpc_type(self, ctx: commands.Context):
        choice = ctx.message.content.split()[1]
        if choice.lower().startswith("play"):
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
                try:
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=activity,
                                                   edit_settings=False)
                    log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
                except Exception as e:
                    log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

            await ctx.message.edit("🎮 **Type:** \"Game\".", delete_after=config_selfbot.deltime)
        elif choice.lower().startswith("watch"):
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
                try:
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=activity,
                                                   edit_settings=False)
                    log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
                except Exception as e:
                    log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

            await ctx.message.edit("📺 **Type:** \"Watching\".", delete_after=config_selfbot.deltime)
        elif choice.lower().startswith("compet"):
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.competing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
                try:
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=activity,
                                                   edit_settings=False)
                    log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
                except Exception as e:
                    log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

            await ctx.message.edit("🎉 **Type:** \"Competing\".", delete_after=config_selfbot.deltime)
        elif choice.lower().startswith("listen"):
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.listening,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
                try:
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=activity,
                                                   edit_settings=False)
                    log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
                except Exception as e:
                    log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

            await ctx.message.edit("🎧 **Type:** \"Listening\".", delete_after=config_selfbot.deltime)
        elif choice.lower().startswith("stream"):
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.streaming,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        url=config_selfbot.streaming_url if rpc.read_variable_json("streaming_url") == "VOID" else rpc.read_variable_json("streaming_url"),
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
                try:
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=activity,
                                                   edit_settings=False)
                    log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
                except Exception as e:
                    log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

            await ctx.message.edit("⭕ **Type:** \"Stream\".", delete_after=config_selfbot.deltime)
        elif choice.lower() == "xbox":
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=None,
                                        application_id=438122941302046720,
                                        buttons=None)

            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                log.alert(f"Failed to set custom Rich Presence: {e}. Re-trying withouth push-notifications-keeping...")
                try:
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=activity,
                                                   edit_settings=False)
                    log.success("Rich Presence successfully set (withouth push-notifications-keeping).")
                except Exception as e:
                    log.alert(f"Failed to set custom Rich Presence.\nError: {e} . Please check the 'Issues' category into the GitHub's README for further help.")

            await ctx.message.edit("🎮 **Type:** \"Xbox\".", delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(f"❌ {langs.incorrect[config_selfbot.lang]} (`play` / `watch` / `listen` / `stream` / `competing` / `xbox`)", delete_after=config_selfbot.deltime)