def madLibs():
    story = """
            This story slays me. Saunders <Verb> meaning out of nothing,
            slowly, it seems—although in a <Noun> this short there’s <Adjective> room for
            slowness—and then <Verb> it all away from you in the end, leaving you gutted
            and empty, which is just the sort of abject cruelty you really want from a writer.
            """
    print(story)
    verb1 = input("Enter Verb #1: ")
    noun1 = input("Enter Noun #1: ")
    adjective1 = input("Enter Adjective #1: ")
    verb2 = input("Enter Verb #2: ")
    story2 = (
            "This story slays me. Saunders " + verb1 + " meaning out of nothing, " +
            "slowly, it seems—although in a " + noun1 + " this short there’s " + adjective1 + " room for " +
            "slowness—and then " + verb2 + " it all away from you in the end, leaving you gutted " +
            "and empty, which is just the sort of abject cruelty you really want from a writer.")

    print(story2)
madLibs()
wait = input("")
