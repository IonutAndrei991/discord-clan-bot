import os
import discord
from discord.ext import commands

CLAN_ROLES = {
    "TT": 1516874575147696148,
    "HKM": 1516876407114826000,
    "OAS": 1516887413929283594,
    "FENA": 1516889849142181958,
    "57.A": 1516890466111459560,
    "MIAU": 1516890844588933323,
    "666": 1516907204765024428
}

CHANNEL_ID = 1516883820157206668

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

posted = False


class ClanView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def set_clan(self, interaction: discord.Interaction, clan_name: str):
        member = interaction.user
        guild = interaction.guild

        # remove old roles
        for role_id in CLAN_ROLES.values():
            role = guild.get_role(role_id)
            if role and role in member.roles:
                await member.remove_roles(role)

        # add new role
        role = guild.get_role(CLAN_ROLES[clan_name])
        if role:
            await member.add_roles(role)

        await interaction.response.send_message(
            f"✔️ You selected: {clan_name}",
            ephemeral=True
        )

    @discord.ui.button(label="TT", style=discord.ButtonStyle.primary)
    async def tt(self, interaction, button):
        await self.set_clan(interaction, "TT")

    @discord.ui.button(label="HKM", style=discord.ButtonStyle.primary)
    async def hkm(self, interaction, button):
        await self.set_clan(interaction, "HKM")

    @discord.ui.button(label="OAS", style=discord.ButtonStyle.primary)
    async def oas(self, interaction, button):
        await self.set_clan(interaction, "OAS")

    @discord.ui.button(label="FENA", style=discord.ButtonStyle.primary)
    async def fena(self, interaction, button):
        await self.set_clan(interaction, "FENA")

    @discord.ui.button(label="57.A", style=discord.ButtonStyle.primary)
    async def f57a(self, interaction, button):
        await self.set_clan(interaction, "57.A")

    @discord.ui.button(label="MIAU", style=discord.ButtonStyle.primary)
    async def miau(self, interaction, button):
        await self.set_clan(interaction, "MIAU")

    @discord.ui.button(label="666", style=discord.ButtonStyle.prtimary)
    async def sixsixsix(self, interaction, button):
        await self.set_clan(interaction, "666")


@bot.event
async def on_ready():
    global posted

    if posted:
        return

    print(f"Bot online: {bot.user}")

    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found")
        return

    await channel.send("🎯 Select your clan tag here:", view=ClanView())
    posted = True


bot.run(os.getenv("DISCORD_TOKEN"))
