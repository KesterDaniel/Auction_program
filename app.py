# silent auction program
all_bids = {}

def save_bid():
  bidder_name = input("What is your name?: ")
  bid_amount = int(input("What's your bid?: $"))
  all_bids[bidder_name] = bid_amount

def bid_time():
  end_bid = False
  save_bid()
  while end_bid == False:
    choice = input("Are there other bidders. Type 'yes' or 'no': ")
    if choice == "yes":
      save_bid()
    else:
      end_bid = True

  max_bid = 0
  max_bidder = ""
  for bid in all_bids:
    current_bid = all_bids[bid]
    if current_bid > max_bid:
      max_bid = current_bid
      max_bidder = bid
  
  print(f"The winner is {max_bidder} with ${max_bid}")

bid_time()
