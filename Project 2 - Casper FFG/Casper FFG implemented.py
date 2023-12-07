import random

#Having a class of validators so that we cna easily store their id, stake deposited and how they vote.
class Validator:
    def __init__(self, id, deposit):
        self.id = id
        self.deposit = deposit
    def cast_vote(self, cur_n):
        return cur_n * 2 + 1 if random.random() < 0.5 else cur_n * 2 + 2



#as defined in the assignment.
rounds = 10

#creating all the validators given to us.
deposits = [500, 100, 300, 250, 150, 500, 600, 350, 200, 150]
validators = [Validator(idx, deposit) for idx, deposit in enumerate(deposits)]

#Calculating total stake to calculate who has majority.
total_deposit = sum(v.deposit for v in validators)

#Creating the checkpoint tree.
tree = {i: [] for i in range(2 ** (rounds + 1) - 1)}
blockchain = []
finalized_validators = {}

for round in range(rounds):
    votes = {}
    
    for valids in validators:
        vote = valids.cast_vote(round)
        votes[vote] = votes.get(vote, 0) + valids.deposit
        if vote in tree:
            tree[vote].append(valids.id)

    # Determine supermajority link
    supermajority_link = max(votes, key=votes.get)
    blockchain.append(supermajority_link)
    finalized_validators[supermajority_link] = tree[supermajority_link]


#Printing the validators of each checkpoint after Casper FFG algorithm.

print("\n")
print(" .PRINTING THE SUPERMAJORITY LINKS, THEIR VALIDATORS AND THE BLOCKCHAIN THUS FORMED.")

for checkpoint in blockchain:
    validator_ids = finalized_validators[checkpoint]
    print(f"Validators IDs who all finalized checkpoint {checkpoint} are : {validator_ids}\n")
    print("-------- \n")

print("Blockchain thus formed by the 10 supermajority links: ")
print(">>>>>>",blockchain,"<<<<<<<")
print("======================================================")