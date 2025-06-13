import json
import random

def intro():
    print("""
🌌 Echoes of the Forgotten Sky 🌌

You wake up on the cold floor of a massive glass chamber, floating high above the Earth.
The sky is shattered — cracks run across it like broken glass. A robotic voice echoes:
"Candidate #42, consciousness restored. 3 paths detected. Choose wisely."

You don’t remember your name. But one thing is certain — you were not supposed to be here.
The world outside is unrecognizable, and inside, secrets buried in your mind begin to unravel.
""")

def present_choices(scene_data):
    print(f"\n{scene_data['description']}\n")
    for i, choice in enumerate(scene_data['choices'], 1):
        print(f"{i}. {choice['text']}")

    while True:
        try:
            user_choice = int(input("\nChoose an option (1/2/3): ")) - 1
            if 0 <= user_choice < len(scene_data['choices']):
                return scene_data['choices'][user_choice]['next']
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a number.")

def play_game():
    story = {
        "scene_1": {
            "description": "You wake up in a cold, sterile dome of glass. Cracks in the sky reveal swirling black space. A voice says: 'Candidate #42, consciousness restored. Proceed.'",
            "choices": [
                {"text": "Approach the glowing console", "next": "scene_2_console"},
                {"text": "Look out the cracked sky-window", "next": "scene_3_window"},
                {"text": "Check your reflection in the wall", "next": "scene_4_memory"}
            ]
        },
        "scene_2_console": {
            "description": "You stand before a holographic console. It's waiting for your command. Old logs suggest the chamber is part of a program called SkyCore—built to preserve the best minds of humanity in a digital matrix after Earth fell to war and climate disaster.",
            "choices": [
                {"text": "Access memory logs", "next": "scene_5_flashback"},
                {"text": "Run diagnostics", "next": "scene_6_glitch"},
                {"text": "Trigger emergency escape", "next": "ending_loop"}
            ]
        },
        "scene_3_window": {
            "description": "You press your face to the glass. The Earth below is broken into massive floating plates. You see another chamber—cracked open. A figure floats in stasis across the way. Something about them feels familiar.",
            "choices": [
                {"text": "Send a signal", "next": "scene_7_sibling"},
                {"text": "Break the glass", "next": "ending_void"},
                {"text": "Return to the console", "next": "scene_2_console"}
            ]
        },
        "scene_4_memory": {
            "description": "Your reflection is glitching—flickering into someone else. A familiar face... your sister. Her memories flood into you: promises, laughter, the decision to enter SkyCore against her plea.",
            "choices": [
                {"text": "Touch the reflection", "next": "scene_5_flashback"},
                {"text": "Ignore it", "next": "scene_2_console"},
                {"text": "Ask the voice about her", "next": "scene_7_sibling"}
            ]
        },
        "scene_5_flashback": {
            "description": "A vision emerges. Earth in flames. You and your sister—engineers of SkyCore—arguing about its true purpose. She feared it would trap humanity. You believed it could save consciousness from extinction. Did you make the right choice?",
            "choices": [
                {"text": "Override the AI", "next": "scene_8_final_decision"},
                {"text": "Search for her consciousness", "next": "scene_7_sibling"}
            ]
        },
        "scene_6_glitch": {
            "description": "The system crashes. The sky flickers red. A warning: 'Core unstable. Memory desync detected.' Time fractures around you. Versions of yourself walk the halls. Some cry. Some scream. All are trapped.",
            "choices": [
                {"text": "Force reboot", "next": "ending_loop"},
                {"text": "Let it collapse", "next": "ending_truth"}
            ]
        },
        "scene_7_sibling": {
            "description": "You find her: Candidate #12. Her chamber is half-decayed, her mind suspended in limbo. She speaks: 'You finally woke up. We can still undo this... or rule it.'",
            "choices": [
                {"text": "Transfer her into your space", "next": "scene_8_final_decision"},
                {"text": "Merge with her", "next": "ending_merge"},
                {"text": "Set her free", "next": "ending_rebirth"}
            ]
        },
        "scene_8_final_decision": {
            "description": "The system pulses: 'Core command override authorized.' You and your sister now control the fate of SkyCore. 3 choices lie ahead—each irreversible.",
            "choices": [
                {"text": "Awaken", "next": "ending_rebirth"},
                {"text": "Stay and protect others", "next": "ending_merge"},
                {"text": "Delete all data, end SkyCore", "next": "ending_truth"}
            ]
        },
        "ending_loop": {
            "ending": "🔁 BAD END – The Loop: You trigger escape prematurely. The AI resets your mind. You become Candidate #43. You’ve done this 42 times already."
        },
        "ending_void": {
            "ending": "🕳️ BAD END – The Void: You break the glass. Vacuum pulls you into the abyss. Your code floats, fragmented, lost between stars."
        },
        "ending_merge": {
            "ending": "💠 TRUE END – Merge: You and your sister unify your minds. As SkyCore’s new overseers, you guide billions of digital souls across generations, evolving into beings of pure thought. You are the new gods of the forgotten sky."
        },
        "ending_rebirth": {
            "ending": "🌍 GOOD END – Rebirth: You awaken in a shattered city buried beneath ash and roots. Your sister's hand grips yours. Life remains. Hope returns. The age of machines ends with your awakening."
        },
        "ending_truth": {
            "ending": "🧠 SECRET END – The Truth: You delete SkyCore. All memories, all minds—gone. But in that silence, Earth stirs. A child born in the ruins finds a single preserved log: ‘We were here.’ A new future begins."
        }
    }

    current_scene = 'scene_1'
    while True:
        scene = story[current_scene]
        if 'ending' in scene:
            print(f"\n🔚 {scene['ending']}")
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again == 'yes':
                current_scene = 'scene_1'
                intro()
                continue
            else:
                print("\nThanks for playing Echoes of the Forgotten Sky.")
                break
        current_scene = present_choices(scene)

if __name__ == '__main__':
    intro()
    play_game()