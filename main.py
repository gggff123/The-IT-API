from fastapi import FastAPI
app=FastAPI()
#main logic
#homepage

@app.get("/")
def home():
    return {"message":"Hello welcome to the 'IT' API.For more info visit /docs."}

#character api
@app.get("/characters")
def get_charac():
    return [
        {"name":"Bill Denbrough","role/position":"The Leader","primary fear":"Georgies Ghost","description":"Driven by the guilt of his brothers death; a natural leader with a severe stutter who becomes a horror novelist"},
        {"name":"Beverly Marsh","role/position":"The Markswoman","primary fear":"Blood / Her Father","description":"The resilient heart of the group; she deals with an abusive home life and later becomes a successful fashion designer."},
        {"name":"Ben Hanscom","role/position":"The Builder","primary fear":"The Mummy","description":"A brilliant, lonely boy with a talent for engineering and history who grows up to be a world-renowned architect."},
        {"name":"Richie Tozier","role/position":"The Distractor","primary fear":"Werewolf / Paul Bunyan","description":"The fast-talking Trashmouth who uses jokes and Voices to hide his fear; later becomes a famous radio DJ."},
        {"name":"Eddie Kaspbrak","role/position":"The Medic","primary fear":"The Leper / Disease","description":"A hypochondriac kept in a state of constant anxiety by his mother; he possesses a surprising amount of medical knowledge."},
        {"name":"Mike Hanlon","role/position":"The Sentinel","primary fear":"Giant Bird / Fire","description":"The town historian and the only member to stay behind in Derry to watch for ITs return as the local librarian."},
        {"name":"Stanley Uris","role/position":"The Analyst","primary fear":"Flute Player / Logic","description":"The most logical and fragile member; his inability to rationalize the supernatural leads to a tragic adult outcome."},
        {"name":"Pennywise (IT)","role/position":"The Antagonist","primary fear":"N/A (Shape-shifter)","description":"An ancient cosmic predator from the Macroverse that feeds on fear; its true essence is the Deadlights."},
        {"name":"George Denbrough","role/position":"The Catalyst","primary fear":"N/A (Victim)","description":"Bills 6-year-old brother whose murder in the rain starts the story; he is often used as a spectral lure by IT."},
        {"name":"Henry Bowers","role/position":"Human Enforcer","primary fear":"Authority / Madness","description":"A psychopathic bully driven to complete insanity and murder by his fathers abuse and IT's telepathic whispers."},
        {"name":"Patrick Hockstetter","role/position":"The Wildcard","primary fear":"Leech-like Swarms","description":"A true sociopath with disturbing habits (like the refrigerator incident) who is feared even by his own friends."},
        {"name":"Belch Huggins","role/position":"The Tank","primary fear":"Frankenstein's Monster","description":"The physically massive muscle of the Bowers gang; known for his loyalty to Henry and his sheer strength."},
        {"name":"Victor Criss","role/position":"The Lieutenant","primary fear":"Henry's Volatility","description":"The most sane member of the bullies who follows along due to peer pressure and a fear of being Henry's next target."} 
    ]
#search
@app.get("/character-search")
def search(name:str):
    if  name=="Bill Denbrough"or name=="bill denbrough":
        return {"name":"Bill Denbrough","role/position":"The Leader","primary fear":"Georgies Ghost","description":"Driven by the guilt of his brothers death; a natural leader with a severe stutter who becomes a horror novelist","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/f/fa/Bill_Denbrough_2017.png/revision/latest?cb=20180922014852"}
    elif name=="Beverly Marsh"or name=="Beverly Marsh".lower():
        return {"name":"Beverly Marsh","role/position":"The Markswoman","primary fear":"Blood / Her Father","description":"The resilient heart of the group; she deals with an abusive home life and later becomes a successful fashion designer.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/0/00/Superthumb.jpg/revision/latest?cb=20180711164905"}
    elif name=="Ben Hanscom"or name=="Ben Hanscom".lower():
        return {"name":"Ben Hanscom","role/position":"The Builder","primary fear":"The Mummy","description":"A brilliant, lonely boy with a talent for engineering and history who grows up to be a world-renowned architect.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/0/0a/Ben.jpg/revision/latest?cb=20181123131759"}
    elif name=="Richie Tozier"or name=="Richie Tozier".lower():
        return  {"name":"Richie Tozier","role/position":"The Distractor","primary fear":"Werewolf / Paul Bunyan","description":"The fast-talking Trashmouth who uses jokes and Voices to hide his fear; later becomes a famous radio DJ.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/1/16/Richie-0.jpg/revision/latest?cb=20190822190122"}
    elif name=="Eddie Kaspbrak"or name=="Eddie Kaspbrak".lower():
        return {"name":"Eddie Kaspbrak","role/position":"The Medic","primary fear":"The Leper / Disease","description":"A hypochondriac kept in a state of constant anxiety by his mother; he possesses a surprising amount of medical knowledge.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/2/21/DMtDAtxVAAAxu2Z.jpg/revision/latest?cb=20180809123717"}
    elif name=="Mike Hanlon"or name=="Mike Hanlon".lower():
        return  {"name":"Mike Hanlon","role/position":"The Sentinel","primary fear":"Giant Bird / Fire","description":"The town historian and the only member to stay behind in Derry to watch for ITs return as the local librarian.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/e/e9/Mike_Hanlon.jpg/revision/latest?cb=20180830000056"}
    elif name=="Stanley Uris"or name=="Stanley Uris".lower():
        return {"name":"Stanley Uris","role/position":"The Analyst","primary fear":"Flute Player / Logic","description":"The most logical and fragile member; his inability to rationalize the supernatural leads to a tragic adult outcome.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/1/17/Stan.jpg/revision/latest?cb=20180811151024"}
    elif name=="Pennywise"or name=="Pennywise".lower():
        return {"name":"Pennywise (IT)","role/position":"The Antagonist","primary fear":"N/A (Shape-shifter)","description":"An ancient cosmic predator from the Macroverse that feeds on fear; its true essence is the Deadlights.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/2/29/Pennywise_%28IT%29.jpg/revision/latest?cb=20191218032337"}
    elif name=="George Denbrough"or name=="George Denbrough".lower():
        return  {"name":"George Denbrough","role/position":"The Catalyst","primary fear":"N/A (Victim)","description":"Bills 6-year-old brother whose murder in the rain starts the story; he is often used as a spectral lure by IT.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/b/ba/Georgie.png/revision/latest?cb=20210307154124"}
    elif name=="Henry Bowers"or name=="Henry Bowers".lower():
        return    {"name":"Henry Bowers","role/position":"Human Enforcer","primary fear":"Authority / Madness","description":"A psychopathic bully driven to complete insanity and murder by his fathers abuse and IT's telepathic whispers.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/5/5a/Henrybowersfilm2017.png/revision/latest/scale-to-width-down/1000?cb=20260215105624"}
    elif name=="Patrick Hockstetter"or name=="Patrick Hockstetter".lower():
        return  {"name":"Patrick Hockstetter","role/position":"The Wildcard","primary fear":"Leech-like Swarms","description":"A true sociopath with disturbing habits (like the refrigerator incident) who is feared even by his own friends.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/e/e3/Patrick-hockstetter.jpg/revision/latest?cb=20181129130131"}
    elif name=="Belch Huggins"or name=="Belch Huggins".lower():
        return  {"name":"Belch Huggins","role/position":"The Tank","primary fear":"Frankenstein's Monster","description":"The physically massive muscle of the Bowers gang; known for his loyalty to Henry and his sheer strength.","img_url":"https://static.wikia.nocookie.net/warner-bros-entertainment/images/d/dc/It2017blech.JPG/revision/latest?cb=20200908143800"}
    elif name=="Victor Criss"or name=="Victor Criss".lower():
        return  {"name":"Victor Criss","role/position":"The Lieutenant","primary fear":"Henry's Volatility","description":"The most sane member of the bullies who follows along due to peer pressure and a fear of being Henry's next target.","img_url":"https://static.wikia.nocookie.net/stephenking/images/c/cf/Victorcriss2017.png/revision/latest?cb=20260212053942"}
    else:
        return {"error":"Not found"},404
