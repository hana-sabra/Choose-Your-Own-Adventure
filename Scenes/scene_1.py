# scene_1.py

def play_scene():
    """
    Scene 1 Template:
    - Section A (Choice 1)
    - Section B (Choice 2)
    - Returns the name of the next scene (e.g., "scene_2") or "quit".
    """
    
    print("\n=== SCENE 1 ===")
    print("Section A: [You wake up and find yourself in the forest and the atmosphere is so quiet it makes you uncomfortable...then you decide to explore.after a short period of time you find an empty camp but it looks like someone was there since there was a fire set up there.]")
    
    # Example of a first choice for Section A
    choice_a = input("You can choose 'explore' or 'exit': ").lower().strip()
    
    if choice_a == "explore":
        print("You decide to look around the area, searching for anything of interest...but, you feel a presence of someone behind you *Clank* 'Who are you??!'")
        # Placeholder for story/logic
    elif choice_a == "exit":
        print("You decide to leave and u stummble against an animal eating his prey then you think that going to the camp is your only option..")
        # Placeholder for story/logic
    else:
        print("Invalid choice. Let's assume you explore anyway.")

    print("\n--- Moving to Section B of Scene 1 ---")
    print("Section B: [As you look around, a rugged man suddenly steps out from the trees, pointing a gun at you. His clothes are torn, and his eyes wild. He snarls, 'Who are you?!']")

    # Example of a second choice for Section B
    choice_b = input("Do you 'confront' the stranger or 'attack' him? ").lower().strip()

    if choice_b == "confront":
        print("You raise your hands, trying to calm things down. 'I'm lost,' you say cautiously. The man eyes you suspiciously but gestures with the gun.")
        print("'Back to the camp. Now.' You don’t argue.")
        return "scene_2"

    elif choice_b == "attack":
        print("You feint to the side, ready to fight, but he’s faster than you expected. 'Nice try,' he grunts, then jerks his head. 'To the camp. Move.'")
        print("With no better option, you follow him through the trees toward the camp.")
        return "scene_2"

    else:
        print("Unclear response. The man growls and motions with his weapon. 'Enough. Move it.' You’re led back to the camp in tense silence.")
        return "scene_2"

