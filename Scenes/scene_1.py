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
    print("Section B: [The man is threating you with his gun, he looks furious andd crazy.he asks  'who are you' as you feel feel the distrust in his voice.]")
    
    # Example of a second choice for Section B
    choice_b = input("Do you 'confront' the strange  or 'attack' him? ").lower().strip()
    
    if choice_b == "confront":
        print("You answer his questions but, he doesn't look like he would trust you")
        # Decide the next scene
        return "scene_2"
    elif choice_b == "attack":
        print("You try to buy yourself time to do something by answering his questions and acting dumb then  that you saw in the distance animal makes a sounds you take this disattraction to your advantage and attack him ")
        # Possibly go to a different scene or move forward
        return "scene_2"
    else:
        print("Not sure what that means. Let's assume you follow the noise anyway.")
        return "scene_2"
