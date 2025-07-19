# scene_4.py

def play_scene():
    """
    Scene 4 Template (Often a 'final' or 'climax' scene):
    - Section A (Choice 1)
    - Section B (Choice 2)
    - Returns "quit" if the story ends, or maybe loops back to an earlier scene.
    """

    print("\n=== SCENE 4 ===")
    print("Section A: [Set the stage for a final confrontation or resolution]")
    
    choice_a = input("make new friends or sit alone and cant find food").lower().strip()

    if choice_a == "live":
        print("he will make friends  ")
        # Placeholder logic
    elif choice_a == "sick":
        print("sit alone and cant find food")
        # Placeholder logic

    print("\n--- Moving to Section B of Scene 4 ---")
    print("Section B: [Provide the final decision or resolution]")
    
    choice_b = input("either live at the island or risk and go home")

    if choice_b == "live":
        print("stay in the island his whole life with his friends")
        print("This might be the end of your journey!")
        return "quit"
    elif choice_b == "turn back":
        print(" he will make a boat and turn to his home.")
        return "quit"
    else:
        print("No action taken. Fate decides for you. The adventure concludes.")
        return "quit"

