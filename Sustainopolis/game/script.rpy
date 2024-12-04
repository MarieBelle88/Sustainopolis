define Female = Character('Female', color="#E03B8B")

image bg park_resized = Transform("park_no_fence_day.jpg", size=(1280, 720), xalign=0.5, yalign=0)
image bg city_neutral = Transform("city_neutral.jpg", size=(1280, 720), xalign=0.5, yalign=0)
image bg city_struggling = Transform("city_struggling.jpg", size=(1280, 720), xalign=0.5, yalign=0)
image bg city_thriving = Transform("city_thriving.jpg", size=(1280, 720), xalign=0.5, yalign=0)
image female smiling = "female_smiling.png"

# Initialize scores
default env_sustainability = 50
default econ_prosperity = 50
default social_equity = 50

# Define intro music
define intro_music = "SwitchWithMeTheme.wav"

# Function to update scores
init python:
    def update_scores(env=0, econ=0, social=0):
        global env_sustainability, econ_prosperity, social_equity
        env_sustainability = max(0, min(100, env_sustainability + env))
        econ_prosperity = max(0, min(100, econ_prosperity + econ))
        social_equity = max(0, min(100, social_equity + social))

label start:
    # Play intro music
    play music intro_music
    
    # Show introduction screen
    show bg park_resized with dissolve
       
    "Can you build a sustainable future? Lead your city into a greener, fairer, and more prosperous tomorrow."
    "Created by the Sustainopolis Team. In partnership with Global Goals"
    "Your Mission: You are the newly elected Leader of Sustainopolis, a fictional city at a crossroads..."
    "Welcome to Sustainopolis! It’s 2030. Extreme weather events, rising inequality, and economic pressures are challenging cities worldwide."
    
    # Ask for the player's name
    $ player_name = renpy.input("What is your name?")
    if not player_name:
        $ player_name = "Leader"
    show female_smiling
    Female "[player_name], welcome to Sustainopolis!"

    jump social_questions

label social_questions:
    # Show the character on the left side of the screen
    show female_smiling at left
    
    # Display the introduction text
    Female "Let's begin with a question on social policies."
    
    # Hide the character briefly, if needed
    hide female_smiling
    
    
    
    # Display the options for the player to choose from
    menu:
        Female "As the city’s leader, you’re facing rising demands for affordable housing. How will you address this challenge while considering sustainability?"
        "Implement a green affordable housing initiative":
            $ update_scores(env=20, econ=-10, social=15)
        
        "Encourage private developers to build affordable housing by offering tax breaks, with no green mandates.":
            $ update_scores(env=-15, econ=15, social=10)
        
        "Invest in rehabilitating existing buildings into affordable housing.":
            $ update_scores(env=10, econ=-5, social=10)
    
    jump environmental_questions


label environmental_questions:
    # Show the character on the left side of the screen
    show female_smiling at left
    Female "Now let's tackle an environmental issue."
    
    # Hide character briefly if needed
    hide female_smiling
    
    
    # Display the options for the player to choose from
    menu:
        Female "Your citizens request more greenery in your city, but land is scarce. What is your course of action?"

        "Expand existing parks, renovating them with updated gardens, spaces, and playgrounds.":
            $ update_scores(env=10, econ=-5, social=8)
            
        "Create green urbanism by merging nature with urban living.":
            $ update_scores(env=15, econ=-15, social=10)
        
        "Abolish car parks or car-centric areas to repurpose land for new parks.":
            $ update_scores(env=12, econ=-10, social=5)
        
        "Don't change the situation and focus on other policies.":
            $ update_scores(env=-10, econ=0, social=-5)
    
    jump economic_questions

label economic_questions:
    # Show the character on the left side of the screen
    show female_smiling at left
    Female "Finally, let's address an economic challenge."
    
    # Hide character briefly if needed
    hide female_smiling
    
    
    # Display the options for the player to choose from
    menu:
        Female "Your city is experiencing a slowdown in economic growth. You decide to launch an economic stimulus package. What is your approach?"
        
    
        "Invest in large-scale infrastructure projects.":
            $ update_scores(env=-10, econ=20, social=10)

        "Introduce traffic rerouting and public transport incentives.":
            $ update_scores(env=5, econ=-5, social=15)
                
        "Expedite construction by allocating additional funds.":
            $ update_scores(env=-5, econ=-10, social=5)
    
    jump results


label results: 
    # Show character on the screen
    show female_smiling
    
    # Display the introductory message
    Female "Let's see how you've done!"
    
    # Hide the park background and character with dissolve
    hide bg park_resized with dissolve
    hide female_smiling 
    
    # Show different backgrounds depending on the scores
    if env_sustainability >= 70 and econ_prosperity >= 70 and social_equity >= 70:
        # Display a thriving city background
        show bg city_thriving with dissolve
        "Congratulations! Sustainopolis thrives under your leadership."
    
    elif env_sustainability < 30 or econ_prosperity < 30 or social_equity < 30:
        # Display a struggling city background
        show bg city_struggling with dissolve
        "Oh no, Sustainopolis struggles under your policies. Better luck next time!"
    
    else:
        # Display a neutral city background
        show bg city_neutral with dissolve
        "Sustainopolis is doing well, but there’s still room for improvement!"
    
    # Hide the character after showing the results
    hide female_smiling with dissolve

    menu:
        "Restart the game":
            return

        "Exit":
            return

