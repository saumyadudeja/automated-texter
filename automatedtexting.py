from twilio.rest import Client
import schedule,time,random

GENERIC_TEXT_QUOTES = [
"You are lovely! I can't believe I get to spend the rest of my life with you, Saumya!",
"Thinking about you...",
"Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresa, Leonardo Da Vinci, Thomas Jefferson, and Albert Einstein.",
"Work hard, be kind, and amazing things will happen",
"Never stop doing your best just because someone doesn’t give you credit.",
"Work hard for what you want because it won’t come to you without a fight. You have to be strong and courageous and know that you can do anything you put your mind to. If somebody puts you down or criticizes you, just keep on believing in yourself and turn it into something positive.",
"Opportunity is missed by most people because it is dressed in overalls and looks like work.",
"Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.",
"If you work on something a little bit every day, you end up with something that is massive.",
"The big secret in life is that there is no secret. Whatever your goal, you can get there if you’re willing to work.",
"At any given moment you have the power to say: this is not how the story is going to end.",
"Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it.",
"We can do anything we want to if we stick to it long enough.",
"Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.",
"I hated every minute of training, but I said, ‘Don’t quit. Suffer now and live the rest of your life as a champion.",
"Success is liking yourself, liking what you do, and liking how you do it.",
"Today is your opportunity to build the tomorrow you want.",
"You don’t need to see the whole staircase, just take the first step.",
"It’s never too late to be what you might’ve been.",
"Twenty years from now you’ll be more disappointed by the things you did not do than the ones you did.",
"You can’t go back and change the beginning, but you can start where you are and change the ending."
]
#'Hiket':'+4917674726252',
#'Keyur':'+4917643634973'"""
twilio_phone = '+14253210082'
my_names_dict={'Saumya':'+4915215424368',
                'Aman':'+12039369613',
                'Dad':'+919971822900',
                'Rishu':'+4915216088805'
                }
quote = "Opportunity is missed by most people because it is dressed in overalls and looks like work."
account_sid = 'AC30b81c2358657d2bc5f3f5f1f5e52688'
auth_token = 'd6983b7cadbd82163c5124009da7c255'
client = Client(account_sid, auth_token)
# def send_message_to_me(quote):
#quote = GENERIC_TEXT_QUOTES[random.randint(0,len(GENERIC_TEXT_QUOTES)-1)]
for key,value in  my_names_dict.items():
    client.messages.create(
                     to=value,
                     from_=twilio_phone,
                     body="Good morning "+key+"! Here's your quote for today: " +quote
                 )

#schedule.every(5).minutes.do(send_message,quote)
#schedule.every(30).minutes.do(send_message,GENERIC_TEXT_QUOTES)
print('done!')

# while 1:
#     schedule.run_pending()
#     time.sleep(1)
#"Saumya, you created this!",
# "Hey Saumya! Just a reminder that you shine like a star",
# "You are so cool Saumya, that you can win a game of chess by just looking at the board",
# "All our dreams can come true Saumya, if we have the courage to pursue them.",
# "The best time to plant a tree was 20 years ago. The second best time is now,Saumya.",
# "Dear Saumya, If people are doubting how far you can go, go so far that you can’t hear them anymore.",
# "It’s no use going back to yesterday, because you was a different person then, Saumya",
# "If we have the attitude that it’s going to be a great day it usually is, Saumya",
# "Magic is believing in yourself. If you can make that happen, you can make anything happen, Saumya.",
# "Just remember that I love you, Saumya!",
