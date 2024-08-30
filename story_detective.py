import time
import os

class Story:
    def __init__(self, story) -> None:
        self.story = story
        
    def story_section(story):
        os.system("cls")
        for char in story:
            print(char, end = "", flush = True)
            time.sleep(0.01)
        
# Chapter 0 - Intro

chapter_0_intro = """The dim light of morning seeped through the blinds of the cluttered office, casting elongated shadows over the empty bottles strewn across the desk. 
You stirred from uneasy sleep, your head pounding with the remnants of the alcohol you had imbibed to numb the ever-present anxiety gnawing at your mind. 
The relentless tide of unpaid bills loomed, and the meager income from the odd jobs you managed to scrounge together barely kept you afloat. 

As your vision cleared, you became aware of a figure standing before you—a man dressed in a black suit that seemed to absorb the that shady dim light. 
His presence was disquieting, made more so by the strange, intricate ornaments that adorned him,
He spoke with a measured eloquence, offering you a position—night watchman at an old mansion. 
The prospect, though cloaked in unease, was tempting in your desperate circumstances. 
Yet, despite the subtle alarm that tingled in the back of your mind, you knew you had little choice but to heed his words.\n"""

# Chapter 1 - The Forest - Arrival

chapter_1_arrival = """The car rattled and groaned beneath you, its engine struggling with every mile as you drove through the desolate countryside. 
The vehicle, much like your life, was on its last legs, wheezing its way toward an inevitable end. Hours bled into each other, 
the endless stretch of road before you offering little more than the hum of tires on asphalt and the creeping anxiety of an uncertain destination. 
The sun, once a distant beacon, now dipped below the horizon, casting the landscape in a deepening twilight. 
Finally, just as the last traces of daylight began to fade, you spotted an old, weathered road sign—its letters barely legible, 
but enough to confirm you were headed in the right direction.

The further you drove, the more the world around you seemed to close in. 
Darkness descended rapidly, and a thick fog began to rise from the earth, swirling around the car like some spectral shroud. 
The air grew heavier, and the silence of the encroaching forest pressed against the windows, filling the cabin with an oppressive stillness. 
Then, without warning, the car shuddered violently, and the engine sputtered to a halt. 
You slammed your fist against the steering wheel, cursing the rusted hunk of metal that had finally given up the ghost.

Frustration boiled over, and you kicked open the door, stepping into the cold, damp air. 
With a sense of resignation, you pulled your gear from the trunk—what little you had—and slung it over your shoulder. 
The forest loomed ahead, its tall, ancient trees standing like silent sentinels in the fog. 
With no other choice, you began your journey on foot, the only sound your own footsteps crunching against the leaf-strewn path 
as you ventured deeper into the unknown.\n"""

# Chapter 1 - The Forest - The Fox / Choice 1

chapter_1_the_fox_choice = """As you trudged through the dense forest, the fog thickening with every step. 
You couldn't shake the feeling that the silence around you was unnatural — too complete, as if the woods themselves were holding their breath. 
The only sound was the rustle of leaves underfoot and the occasional snap of a twig. 
But then, just as you were beginning to think the eerie quiet might be your mind playing tricks on you, 
you heard something—a faint rustling in the trees behind you.\n"""

chapter_1_the_fox_choice_1 = """As you cautiously follow the source of the noise, your flashlight cuts through the thick fog, illuminating 
the gnarled roots and twisted branches that seem to close in around you. The rustling continues, now louder, coming from just ahead. 
You approach slowly, every sense on high alert, bracing for whatever might be lurking in the darkness.

Suddenly, your beam catches a pair of glowing eyes peering out from the underbrush. 
Your heart skips a beat, but then the creature steps into the light—a small, sleek fox, its reddish fur matted and damp from the fog. 
It freezes for a moment, as startled by your presence as you are by its. You exhale slowly, 
realizing that this was the source of the noise that had unnerved you so.

The fox, sensing no threat, quickly darts off into the woods, disappearing as silently as it had appeared. 
Despite the innocent resolution, the eerie atmosphere of the forest lingers, leaving you with the unsettling feeling that not all is as it seems. 
The encounter with the fox, though harmless, does little to dispel the sense of dread that continues to hang heavy in the air.\n"""

chapter_1_the_fox_choice_2 = """Sensing the growing unease, you choose to ignore the sound, dismissing it as an animal or the wind. 
However, the tension compels you to quicken your pace, your senses heightened and your hand instinctively resting on your trusted sidearm, 
hopefully ready for anything that might leap out of the shadows.\n"""

chapter_1_the_fox_choice_3 = """Deciding that safety is paramount, you swiftly step off the path and find cover behind a 
tree using the shadows to conceal yourself. From this vantage point, you wait in silence, trying to see if the sound reveals its source, 
while preparing to confront whatever might be trailing you.\n

As you wait in the shadows, your heart pounding in your chest, the rustling grows closer, the sound of leaves and twigs crunching underfoot. Your grip tightens around your flashlight, 
every muscle in your body tensed and ready. Then, out of the fog, a small shape emerges, darting between the trees with a swift, graceful motion. 

A fox.

As the fox disappears into the underbrush, you let out a slow breath, but the tension in your body doesn't fully ease. 
The forest remains cloaked in an unsettling silence, and despite recognizing the harmless creature, the feeling of unease lingers, stronger than before. 
Something about the encounter feels off, as if the fox was just a small part of a larger, unseen presence lurking in the shadows. 
The forest, with its oppressive darkness and thickening fog, feels more menacing than ever. You step back onto the path and continue your journey, but the weight of dread hangs heavy in the air, 
a nagging sense that something still isn't right.\n"""

chapter_1_the_fox_choice_2_alternative = """As you quickened your pace, the unsettling rustling behind you faded, swallowed by the dense fog and the oppressive silence of the forest. 
You pushed forward, the cobblestone path beneath your feet becoming more uneven with each step, your heart pounding not just from exertion but from the growing sense of dread gnawing at your mind. 
The forest seemed to close in around you, the trees taller, their branches twisted and reaching like claws. Every instinct told you to keep moving, to leave this place behind as quickly as possible. 
But just as you began to believe you had escaped whatever was lurking in the shadows, a low, menacing growl pierced the silence, freezing you in your tracks. You turned, and there it was—a night hound, emerging from the darkness, its eyes glowing with a feral hunger. 
The beast was massive, muscles rippling under its coarse fur, and its jaws dripped with saliva, eager for blood. There was no escape now. The fight you had tried to outrun had found you, and you knew you would have to face this monstrous creature head-on if you wanted to survive."""

chapter_1_cobblestone_path = """You take a moment to steady yourself before pressing on. The ground grows firmer, the earth giving way to something harder, uneven. As you look down, you realize the path is slowly transforming into cobblestones, 
though they are old and worn, many of them cracked or half-buried in the soil. The cobblestones are slick with moisture, and you have to watch your step as you continue.
The forest remains dense on either side, the trees standing like silent sentinels, their twisted branches intertwining above, blocking out what little light remains. 
As you walk, you can't shake the feeling that the cobblestones beneath your feet are more than just old, neglected stones. Through the cracks and moss, you catch glimpses of strange shapes, 
almost familiar symbols etched into the stone. You pause, crouching down to examine one more closely, but it's just a weathered crack, a trick of the mind. Shaking off the creeping unease, 
you stand and continue on, though the sense of something ancient and hidden beneath the surface lingers, just out of reach, as if the forest is whispering secrets it isn't ready to reveal.\n"""

chapter_1_cobblestone_path_fight = """You pause, hearing a faint rustling in the underbrush ahead, and for a moment, 
you think it's the fox again, perhaps returning to investigate you in turn. Your guard drops slightly as you step forward, 
expecting to see the small, familiar shape darting between the trees. But as the fog parts, what emerges is no fox. A hulking figure, 
dark as the night itself, steps into view—its eyes glowing with a malevolent fire. The creature is massive, its fur bristling with an unnatural energy, 
muscles rippling beneath its coarse, matted pelt. Its maw gapes open, revealing rows of jagged teeth, each one dripping with saliva.

You freeze, mesmerized by the sheer terror radiating from this night hound, a beast you've never seen before, 
but whose intent is unmistakably clear. Every instinct screams at you to run, but you're rooted to the spot, 
paralyzed by the monstrous presence before you. Then, with a guttural snarl, the creature charges, and you snap back to reality — 
there's no escaping this. You have to fight. Your hand instinctively grips the handle of your weapon, and with a burst of adrenaline, 
you prepare to face this ferocious beast, knowing that only one of you will leave this encounter alive.\n"""

chapter_1_cobblestone_path_fight_outcome_success = """The night hound collapses at your feet, its monstrous form crumpling into the dirt with a final, guttural howl. 
Your chest heaves, breath coming in ragged gasps, and your weapon shakes in your trembling hands. 
The adrenaline slowly ebbs, and as the fog begins to clear from your mind, you blink and look around. 
The ferocious beast is gone, vanished without a trace, as if it had never been there at all. 
You're standing alone in the silent, darkened forest, the eerie stillness pressing in on you once more. 
Confusion washes over you, and you question your own senses—how could something so real, so terrifying, have been nothing more than a figment of your imagination? 
The vividness of the encounter leaves you shaken to your core. 
A cold dread settles in your stomach as you realize that whatever is happening here, it's far beyond your understanding. 
Regret gnaws at you, and for the first time, you seriously consider that taking the job as a night watchman at this cursed mansion might have been a terrible mistake.\n"""

chapter_1_cobblestone_path_fight_outcome_failure = """You fought desperately against the encroaching darkness, 
but with a final shuddering breath, you felt the cold grip of death claim you, leaving your body to collapse lifelessly on the slick cobblestones, consumed by the silence of the ancient woods.\n"""