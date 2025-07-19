# scene_2.py

def play_scene():
    """
    Scene 2 Template:
    - Section A (Choice 1)
    - Section B (Choice 2)
    - Returns the name of the next scene (e.g., "scene_3") or "quit".
    """

    print("\n=== SCENE 2 ===")
    print("Section A: [the camp]")
    
    choice_a = input("You can choose 'be friends' the area or 'steal': ").lower().strip()

    if choice_a == "be friends":
        print("You go to camp and be friends with the man")
        # Placeholder logic
    elif choice_a == "steal":
        print("You decide to steal the man's money")
        # Placeholder logic
   
    print("\n--- Moving to Section B of Scene 2 ---")
    print("Section B: [going to the boat]")
    
    choice_b = input("you'go on the boat' or 'eat something'").lower().strip()

    if choice_b == "go on the boat":
        print("you go on the boat and sail to an island")
        return "scene_3"
    elif choice_b == "eat something":
        print("you eat something first then you go to the boat")
        return "scene_3"
    

