from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print('***\tWelcome to the Secret Auction program\t***\n')

additional_bidder = 'yes'
bidder_profiles = []

while additional_bidder == 'yes':
  bidder_name = input('What is your name?:\t')
  bid_amount = input('What is your bid amount?:\t$')
  additional_bidder = input('Are there any more bidders? Type "yes" or "no":\t')
  clear()

  bidder_profiles.append({
    'name': bidder_name,
    'bid': int(bid_amount)
  })

highest_bid = 0
highest_bidder = ''
for bidder in bidder_profiles:
  if bidder['bid'] > highest_bid:
    highest_bid = bidder['bid']
    highest_bidder = bidder['name']

print(f'\n***\tCongratulations {highest_bidder}, your bid of ${highest_bid} won!\t***')