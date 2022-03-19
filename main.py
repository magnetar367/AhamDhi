import abilities as ab


def get_response(msg):  # ~Fixed

    choice = 0
    for i in ab.keyword:
        if choice == 0:
            for j in ab.keyword[i]:
                if j in msg.lower():
                    choice = i
                    key = j  # for future purposes like choice 1
                    break
    else:
        for z in ab.nonab_key:
            if choice == 0:
                for j in ab.nonab_key[z]:
                    if j in msg.lower():
                        choice = z
                        break

        if choice == 0:
            if ("how" in msg.lower() or "what" in msg.lower()) and "?" in msg:
                return ab.feeling()
            elif len(msg.lower()) >= 2 and msg.lower()[0] in "hy" and msg.lower().split(" ")[0] != "hear":
                return ab.greeting()

    # Performing the activities
    if choice == 1:

        return ab.powers()

    elif choice == 2:#Wikihow

        website = lambda x: (lambda y: ("+".join(y[y.index(key)+1:])))(x.partition(key))
        ab.wikihow(website(msg.lower()))
        return "Maybe these references might help you tackle this problem. You might want to check it out."

    elif choice == 3:#Motivational SOng

        ab.music()
        return "This song might boost you up"

    elif choice == 4:#Quotes
        return ab.quote()

    elif choice == 5:
        ab.audioplay()
        return "Okay then listen to me carefully;)"

    elif choice == 6:

        return ab.gratitude()

    elif choice == 7:
        return ab.byebye()

    elif choice =="hotline":
        file=key+".txt"
        with open(file,"r") as f:
            return f.read()

    else:

        return ab.dont_know()