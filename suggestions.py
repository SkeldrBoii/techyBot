async def suggest(message):
    if message.content.startswith("b!suggest"):
        try:
            reportcontent = message.content.split(None, 1)[1]
            reportchannel = client.get_channel(880142632716746783)
            reporter = message.author
            successMsg = discord.Embed(color=0x00ff1a)
            successMsg.add_field(name="Successfull", value="Suggestion submitted!", inline=False)
            successMsg.set_footer(icon_url=message.author.avatar_url, text='\nRequested by:\n{0}'.format(message.author))
            await message.channel.send(embed=successMsg)
            reportFinal = discord.Embed(title="Suggestion by " + str(reporter), description=str(reportcontent), timestamp=datetime.datetime.now(datetime.timezone.utc), inline=False, color=0xff0000)
            await reportchannel.send(embed=reportFinal)
        except IndexError:
            errorMsg = discord.Embed(title="Incorrect syntax", description="Usage: b!suggest [suggestion]", inline=False, color=0xff0000)
            errorMsg.set_footer(icon_url=message.author.avatar_url, text='\nRequested by:\n{0}'.format(message.author))
            await message.channel.send(embed=errorMsg)    
    
    

