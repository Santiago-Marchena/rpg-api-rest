from models import Character
import random

characters = []
current_id = 1

def create_character(data):
    global current_id
    c = Character(current_id, data["name"], data["skin_color"], data["race"],
                  data["strength"], data["agility"], data["magic"], data["knowledge"])
    characters.append(c)
    current_id += 1
    return c

def get_all():
    return characters

def get_by_id(id):
    return next((c for c in characters if c.id == id), None)

def update_character(id, data):
    c = get_by_id(id)
    if not c:
        return None
    for k,v in data.items():
        setattr(c,k,v)
    return c

def delete_character(id):
    global characters
    characters = [c for c in characters if c.id != id]

def battle(id1,id2):
    c1 = get_by_id(id1)
    c2 = get_by_id(id2)
    if not c1 or not c2:
        return None

    def attack(a,d):
        dmg = a.strength*1.5 + a.magic*1.2 + a.knowledge*0.5
        dodge = random.random() < (d.agility/100)
        if dodge:
            return 0, f"{d.name} esquivó"
        return dmg, f"{a.name} hace {round(dmg,2)} daño"

    hp1, hp2 = 100+c1.knowledge, 100+c2.knowledge
    log=[]
    turn=1

    while hp1>0 and hp2>0 and turn<=10:
        dmg,msg = attack(c1,c2)
        hp2 -= dmg
        log.append(f"Turno {turn}: {msg}")
        if hp2<=0: break

        dmg,msg = attack(c2,c1)
        hp1 -= dmg
        log.append(f"Turno {turn}: {msg}")
        turn+=1

    winner = c1.name if hp1>hp2 else c2.name

    return {
        "winner": winner,
        "hp1": round(hp1,2),
        "hp2": round(hp2,2),
        "log": log
    }
