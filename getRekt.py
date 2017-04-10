def run(thorin, incoming):
    try:
        target = incoming.message.text.split(" ")[incoming.message.text.split(" ").index("get_rekt") + 1]
        return target + "get Rekt, son!"
    except:
        return "Nobody's getting Rekt on my watch!"


# I realize this is just a carbon copy of shots_fired, just my first foray into the program.
