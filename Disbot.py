import discord
import random
from keep_me_alive import keep_alive

client = discord.Client()

happy_messages = ["You’re off to great places",
                  "Your success mountain is waiting, so get on your way.",
                  "You always pass failure on the way to success.",
                  "No one is perfect - that’s why pencils have erasers.",
                  "Winning doesn’t always mean being first. Winning means you’re doing better than you’ve done before.",
                  "You’re braver than you believe, and stronger than you seem, and smarter than you think.",
                  "It always seems impossible until it is done."
                  "Keep your face to the sunshine and you cannot see a shadow.",
                  "Once you replace negative thoughts with positive ones, you’ll start having positive results.",
                  "Positive thinking will let you do everything better than negative thinking will.",
                  "Winning is fun, but those moments that you can touch someone’s life in a very positive way are "
                  "better. "
                  ]
Bot_greetings_1 = ["hey bot", "hey boi", "hey doge boi", "hey doge bot", "hello bot", "hello boi", "hello doge boi",
                   "hello doge bot", "hi bot", "hi boi", "hi doge boi", "hi doge bot", "hey doge", "hi doge",
                   "hello doge", "poda"]

Bot_greetings_2 = ["good job doge", "well done doge", "you are a good boi doge"]

Doge_greetings = ["Hello master", "I was waiting for you", "hello", "hi", "Wat do you want idiot", "shut up"]

Doge_happy = ["Awww thank you!", "thank you master", "I will always obey you!"]

SunTzuQuotes = ["Be extremely subtle, even to the point of formlessness",
                "Let your plans be dark as night, and when you're ready,"
                " fall like a thunderbolt",
                "All men can see the tactics whereby I conquer, But what none can see is the strategy out of which "
                "victory is evolved",
                "The opportunity of defeating the enemy is provided by the enemy himself",
                "If you know the enemy and know yourself, you need not fear the results of 100 battles",
                "Appear weak when you are strong and strong when you are weak", "Dying is for losers",
                "Sweat more during peace", "get rekt noob",
                "Whatever you do, dont reveal all your techniques all in a youtube video you moron",
                "All war is deception",
                "don't believe everything a bot says"]
ROB_greetings = ["Hello Wide Putin", "How u doin?", "I am kim jong un", "trump is better than u", ]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return
    for word in Bot_greetings_2:
        if word in msg:
            await message.channel.send(random.choice(Doge_happy))
    if msg.startswith(',suntzu quote'):
        await message.channel.send(random.choice(SunTzuQuotes))
    if msg.startswith(",w"):
        a = msg.split()
        question = ' '.join(a[1:])
        app_id = "G8A6RW-HKU2XLX97K"
        k = wolframalpha.Client(app_id)
        res = k.query(question)
        answer = next(res.results).text
        await message.channel.send(answer)
    if "inspirational" in msg:
        await message.channel.send(random.choice(happy_messages))
    if "wish wide putin" in msg:
        for i in range(5):
            await message.channel.send("hello wide putin, I am going to kill you when you sleep tonight")
    if "say" in msg:
        if "right now" in msg:
            a = msg.split()
            b = a[1]
            await message.channel.send(b)
    if "doge" in msg:
        if "are you okay" in msg:
            await message.channel.send("Yes master, I am fine")
        else:
            for word in Bot_greetings_1:
                if word in msg:
                    await message.channel.send(random.choice(Doge_greetings))
    if "doge" in msg:
        if "source code" in msg:
            await message.channel.send()


keep_alive()
client.run("ODI3MTY0NDkyNDYyNDI0MTI0.YGXC9g.OEAgs4yPoCoCJ135SqY8-elmeWk")
