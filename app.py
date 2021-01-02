players = [
    {
        "name": "Pawel",
        "score": 0,
        "is_active": True      
        
    },

    {
        "name": "Ala",
        "score": 0,
        "is_active": False      
        
    },

    {
        "name": "Jan",
        "score": 0,
        "is_active": False     
        
    }
]

def get_idx_of_active_player():
    active_player = {}
    
    for player in players:
        if player["is_active"] == True:
            active_player = player
            
        
    return players.index(active_player)
    
def update_score(amount):
    current_idx = get_idx_of_active_player()
    if amount == 0:
        players[current_idx]["score"]  = 0
    else:
        
        players[current_idx]["score"] += amount
        
    
    

def next_player():
    current_idx = get_idx_of_active_player()
    players [current_idx ]["is_active"] = False
    
    next_idx = 0 if current_idx == 2 else current_idx +1
    players[next_idx]["is_active"] = True


get_idx_of_active_player()

wheel = [100, 200, 300, 100, 500, 1000, 0, -1]

from random import randint

def shuffle_wheel ():
    return wheel[randint(0, len(wheel) -1)]
    
    

shuffle_wheel()

next_player()
get_idx_of_active_player()

update_score(shuffle_wheel())
next_player()
update_score(4)
players



sentences = [
    {
        "sentence": "Baba z wozu koniom lżej",
        "category": "powiedzenie"
    },
    {
        "sentence": "jak kuba bogu tak bog kubie",
        "category": "powiedzenie"
    },
    
    {
        "sentence": "kto rano wstaje ten chodzi niewyspany",
        "category": "powiedzenie"
    }
      
]

def get_random_sentence():
    return sentences[randint(0, len(sentences)-1)]

get_random_sentence()

def convert_sentence(sentence):
    print(sentence)
    sen = "".join([ "_" if x != " " else f'\u25A0' for x in sentence])
    return sen
    
    
     
    
def show_dashboard(sentence):
    print(sentence)

sen = get_random_sentence()
sen_converted = convert_sentence(sen["sentence"])
show_dashboard(sen_converted)

vowel = ["a", "i", "e", "o", "y", "u"]

def guess_letter():
    global sen_converted
    print("podaj spolgloske:")
    letter = input()
    sen_converted_list = list(sen_converted)
    counter = 0
    
    if letter.lower() in vowel:
        print("nie podales spolgloski, tracicsz kolejke")
        return
    
    for idx, sen_letter in enumerate(sen["sentence"]):
        if sen_letter.lower() == letter.lower() and sen_converted_list[idx] == "_":
            sen_converted_list[idx] = sen_letter
            counter +=1
            
   

        
    sen_converted = "".join(sen_converted_list)
   
    return(counter)

guess_letter()




sen_converted

def show_board():
    frame = f"+{'-' * 30}+"
    frame_player = f" | {' | '.join([player['name'] for player in players])} |"
    frame_score = f" | {' | '.join([str(player['score']) for player in players])} |"
    frame_active = f" | {' | '.join([ 'x' if player['is_active'] else ' ' for player in players])} |"
    
    
    banner = "\n".join([frame, frame_player, frame_score, frame_active, frame])
    print(banner)                    
                         
                         

show_board()

sen = get_random_sentence()
sen_converted = convert_sentence(sen["sentence"])
    
def play():
    show_board()
    show_dashboard(sen_converted)
    
    amount = shuffle_wheel()
    print(amount)
    if amount == -1:
        
        next_player()
        play()
        return
    
    if amount == 0:
        update_score(0)
        next_player()
        play()
        return
    
    count = guess_letter()
    
    if count == 0:
        
        print('nic nie trafiles')
        next_player()
        play()
        return
    
    update_score(amount * count)
    print (f"wygrales:{amount * count}")
           
    play()
    return
    
    

play()




