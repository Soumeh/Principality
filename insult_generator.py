from random import choice
    main = ['well played (noun)', 'you are (adjct) (noun)', 'you are (adjct) (noun)', 'eat a (noun) (noun)',
    insults = {
    "noun": ['nerd', 'weakling', 'dork', 'donkey', 'maggot', 'cretin', 'jerk', 'idiot', 'fool', 'butt', 'nerd', 'freak', 'buffoon', 'tool',
    "adjct": ['french', 'stupid', 'weak', 'dumb', 'fat', 'ugly', 'thick', 'daft', 'long', 'tiny', 'bumbling', 'absolute']
    }
    if not safe:
        main += ['i will (verb) your mother', '(verb) yourself', '(verb) you', 'i (verb) in your room', 'choke on a (noun) and (verb)']
    for key, key_insults in insults.items():
        key = '(' + key + ')'
        while key in insult:
            insult = insult.replace(key, choice(key_insults), 1)
    remove_characters = choice(range(-2, 3))
    while remove_characters > 0:
        insult = insult.replace(insult[choice(range(len(insult)))], '', 1)
        remove_characters -= 1
    return insult