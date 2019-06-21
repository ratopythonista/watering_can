import telepot

token='657888879:AAHjmVXaQ74oQYN6IBMOfBmmVJl2tTsG97I'
bot = telepot.Bot(token=token)

users = set()

def get_users():
	for update in bot.getUpdates(offset=-1):
		users.add(update['message']['chat']['id'])

def send_pic(pic):
	for user in users:
		bot.sendPhoto(user, open(pic, 'rb'))
