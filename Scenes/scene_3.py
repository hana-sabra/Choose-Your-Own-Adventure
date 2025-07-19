# scene_3.py

def play_scene():
    """
    Scene 3 Template:
    - Section A (Choice 1)
    - Section B (Choice 2)
    - Returns "scene_4", "quit", or another scene name.
    """

    print("\n=== SCENE 3 ===")
    print("Section A: You're now on the boat, rowing without somewhere in sight - hoping to get away.\
          You suddenly realize you're starving, you look around for food or drink but come up empty.")
    
    choice_a = input("Do you try risking going in the water and catching a fish(1)\
                  or Do you try eating the moss on your boat(2)?").lower().strip()

    if choice_a == 1:
        print("You go in the freezing water and find a school or little, vulnerable fish - easy to catch.\
            You take a handful of them and are forced to to eat them raw, but atleast you're not starving")
        # Placeholder logic
    elif choice_a == 2:
        print("You eat the moss on your boat, despite it tasting disgusting, but atleast you're not starving")
        # Placeholder logic
    
    print("\n--- Moving to Section B of Scene 3 ---")
    print("Section B: A storm hits your boat. Youu have choice but to sit through it, rendered helpless.")
    
    choice_b = input("Do you continue rowing(1), or rest till the storm passes through(2)? ").lower().strip()

    if choice_b == 1:
        print("The boat starts to fill with water, sinking. You have to continue to the island by swimming.")
        return "scene_4"
    elif choice_b == 2:
        print("Suddenly, a giant octupus crashes into your boat, destroying it completly.\
            You have to continue to the island by swimming")
        return "scene_4"
    

