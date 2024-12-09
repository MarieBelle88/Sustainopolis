# Default and initialization setup
define Female = Character('Guide', color="#E03B8B")

image bg city_thriving = Transform("city_thriving.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_economic_powerhouse = Transform("city_economic_powerhouse.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_environmental_haven = Transform("city_environmental_haven.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_social_paradise = Transform("city_social_paradise.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_in_crisis = Transform("city_in_crisis.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_econ_social = Transform("city_econ_social.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_econ_env = Transform("city_econ_env.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_social_env = Transform("city_social_env.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_neutral = Transform("city_neutral.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)
image bg city_neutral = Transform("city_neutral.jpg", size=(1280, 600), xalign=0.5, yalign=1.0)

init:
    # Define the available languages
    $ languages = ["English", "Deutsch"]

# Initialize scores
default env_sustainability = 50
default econ_prosperity = 50
default social_equity = 50

# Define intro music
define intro_music = "SwitchWithMeTheme.wav"

# Initialize global variables for reaction message
default reaction_text = ""

# Dashboard screen with no reaction text
screen dashboard():
    frame:
        xalign 0.0  # Aligns the dashboard to the left
        yalign 0.5
        xpadding 10
        ypadding 10

        vbox:
            spacing 10
            text "Dashboard" size 22 color "#FFFFFF" xalign 0.5

            text "Environmental Sustainability" size 16 color "#00FF00"
            hbox:
                bar value VariableValue("env_sustainability", min=0, max=100) xmaximum 200
            
            text "Economic Prosperity" size 16 color "#FFFF00"
            hbox:
                bar value VariableValue("econ_prosperity", min=0, max=100) xmaximum 200
            
            text "Social Equity" size 16 color "#FF00FF"
            hbox:
                bar value VariableValue("social_equity", min=0, max=100) xmaximum 200

            # Removed the line displaying reaction_text from the dashboard
            # text reaction_text color "#FFFFFF" size 16

# Function to update scores
init python:
    def update_scores(env=0, econ=0, social=0, reaction_message=""):
        global env_sustainability, econ_prosperity, social_equity, reaction_text
        # Update scores
        env_sustainability = max(0, min(100, env_sustainability + env))
        econ_prosperity = max(0, min(100, econ_prosperity + econ))
        social_equity = max(0, min(100, social_equity + social))
        
        # Store reaction message
        reaction_text = reaction_message

    def reset_scores():
        global env_sustainability, econ_prosperity, social_equity, reaction_text
        # Reset all scores to default values
        env_sustainability = 50
        econ_prosperity = 50
        social_equity = 50
        reaction_text = ""  # Reset reaction message
        

label start:
    # Reset scores at the start
    $ reset_scores()
    
    # Play intro music
    play music intro_music

    
        
    # Show introduction screen
    "Welcome to Sustainopolis, a city full of promise and potential. As its leader, you face the challenge of building a thriving, sustainable future while balancing competing priorities. Every decision you make will shape the city’s economy, environment, and the lives of its citizens."
    #"Created by the Sustainopolis Team. In partnership with Global Goals"
    "Your goal is to guide Sustainopolis toward progress, ensuring prosperity, sustainability, and equality. Along the way, you’ll face tough choices—each with consequences that affect the city’s trajectory. Will you create a beacon of innovation and harmony or struggle to maintain balance?"
    "The future of Sustainopolis lies in your hands. Lead wisely."
    # Ask for the player's name
    $ player_name = renpy.input("What is your name?")
    if not player_name:
        $ player_name = "Leader"
    
    Female "[player_name], welcome to Sustainopolis! Let's begin!"
    jump questions

label questions:
    show screen dashboard
    
    # social
    menu:
        "As the city’s leader, you’re facing rising demands for affordable housing. How will you address this challenge while considering sustainability?"

        "Implement a green affordable housing initiative. Require all new affordable housing developments to be energy-efficient, using renewable materials and solar panels.":
            $ update_scores(env=10, econ=-10, social=10)
            "Your initiative reduces long-term energy costs and improves housing quality, but the high upfront expenses strain the city’s budget."

        "Encourage private developers to build affordable housing by offering tax breaks, with no green mandates.":
            $ update_scores(env=-10, econ=15, social=10)
            "The housing shortage eases quickly, but critics worry about the use of unsustainable materials and a lack of long-term benefits."

        "Invest in rehabilitating existing buildings into affordable housing. Focus on retrofitting older structures with moderate energy-efficient improvements.":
            $ update_scores(env=10, econ=-5, social=10)
            "Citizens gain access to affordable housing quickly, while retrofitting helps reduce urban waste. However, the project costs limit broader investments."


    # economy
    menu:
        "Your city has a significant budget surplus this year. How will you allocate the funds?"

        "Establish a city fund to attract large corporations and startups with financial incentives.":
            $ update_scores(env=-5, econ=15, social=10)
            "The city fund attracts major corporations, boosting the local economy and job creation. However, citizens express concern over potential neglect of public services."

        "Provide tax relief for middle- and low-income households to stimulate local spending.":
            $ update_scores(env=0, econ=10, social=15)
            "Local businesses thrive as citizens have more disposable income. However, critics argue the city missed an opportunity to invest in long-term development."

        "Create a savings reserve for future infrastructure or emergency needs.":
            $ update_scores(env=0, econ=10, social=5)
            "The city secures a financial safety net, strengthening its stability. However, some citizens are frustrated by the lack of immediate improvements."

        "Use the surplus to pay down city debt, freeing up funds for long-term projects.":
            $ update_scores(env=0, econ=10, social=-5)
            "Paying off debt improves the city’s credit rating, making future projects more affordable. However, citizens see little immediate benefit."


    # env
    menu:
        "Your citizens request more greenery in your city, but land is scarce. What is your course of action?"

        "Expand existing parks, renovating them with updated gardens, spaces, and playgrounds.":
            $ update_scores(env=15, econ=-5, social=10)
            "Improved parks enhance recreational areas without consuming additional land. However, citizens may be concerned about temporary disruptions during renovations."

        "Create green urbanism by merging nature with urban living, such as vertical gardens and roof gardens.":
            $ update_scores(env=15, econ=-8, social=15)
            "Innovative approaches maximize greenery in limited spaces, but infrastructure changes are costly and disruptive."

        "Abolish car parks or car-centric areas to repurpose land for new parks.":
            $ update_scores(env=15, econ=-8, social=10)
            "Converting car-centric areas creates significant green spaces but faces resistance from car owners and causes financial losses."

        "Don’t change the situation and focus on other policies.":
            $ update_scores(env=-10, econ=0, social=-5)
            "Ignoring the need for greenery worsens environmental issues and frustrates citizens looking for better recreational areas."

    # social
    menu:
        "You’ve been asked to fund a citywide green education initiative aimed at teaching sustainable living practices in schools and communities."

        "Fully fund the program. Provide grants for schools, hire sustainability experts, and run public workshops.":
            $ update_scores(env=15, econ=-10, social=20)
            "The program empowers citizens with knowledge and skills to adopt sustainable practices, but the high cost diverts resources from other projects."

        "Partially fund the program. Focus only on schools and limit community outreach efforts to reduce costs.":
            $ update_scores(env=15, econ=-8, social=15)
            "Schools benefit from the initiative, but limited funding leaves some community groups feeling neglected."

        "Reject the initiative. Redirect funds to immediate infrastructure needs instead.":
            $ update_scores(env=-20, econ=15, social=-20)
            "The city saves money for infrastructure, but citizens criticize the lack of commitment to sustainable education."


    # eco
    menu:
        "Unemployment is rising in your city due to an economic downturn. What is your strategy to create jobs?"

        "Launch a public works program to improve city infrastructure and provide immediate employment.":
            $ update_scores(env=-5, econ=15, social=15)
            "The program creates jobs quickly and improves infrastructure, but critics warn the increased spending might strain the budget long-term."

        "Offer financial incentives to local businesses for hiring more workers.":
            $ update_scores(env=0, econ=10, social=10)
            "Businesses respond by hiring more employees, but the city loses revenue due to the incentives, slowing future growth opportunities."

        "Partner with universities and industries to create job training programs.":
            $ update_scores(env=0, econ=10, social=15)
            "Job training programs upskill citizens and improve long-term employment prospects, but critics argue it doesn’t address immediate unemployment."

        "Reduce business taxes across the board to stimulate hiring.":
            $ update_scores(env=-15, econ=10, social=10)
            "Lower taxes encourage businesses to expand, but the reduced revenue limits the city’s ability to fund other services."


    # env
    menu:
        "Your city has rising air pollution. What is your immediate response?"

        "Invest in a fleet of electric public buses.":
            $ update_scores(env=15, econ=-5, social=10)
            "Electric buses reduce emissions and improve public transit, but the initial investment is costly."

        "Introduce car-free zones in key urban areas.":
            $ update_scores(env=15, econ=-5, social=15)
            "Car-free zones drastically cut emissions and enhance walkability but may hinder access to some businesses."

        "Encourage citizens to use public transport with subsidies.":
            $ update_scores(env=10, econ=-5, social=10)
            "Subsidies make public transport more accessible, reducing car usage but at the cost of city finances."

        "Do nothing; pollution isn’t a priority right now.":
            $ update_scores(env=-20, econ=0, social=-10)
            "Failing to address pollution worsens environmental and health issues, frustrating citizens."


    # social
    menu:
        "The city’s public transportation network is limited, causing heavy reliance on private vehicles. How will you address this issue?"

        "Invest in an eco-friendly public transportation system. Expand routes and prioritize electric buses and trains.":
            $ update_scores(env=25, econ=-10, social=15)
            "Your investment significantly improves accessibility and equity, reducing congestion. However, the high cost strains the city’s budget."

        "Subsidize electric vehicles (EVs) for private citizens instead. Encourage residents to switch from gas-powered cars.":
            $ update_scores(env=15, econ=-10, social=5)
            "Wealthier citizens benefit from the subsidies, but the traffic problem persists, leaving low-income communities underserved."

        "Encourage carpooling and biking. Launch awareness campaigns and install bike lanes to promote eco-friendly commuting.":
            $ update_scores(env=15, econ=-5, social=15)
            "The initiative promotes healthy and eco-friendly transportation options, but its moderate impact on traffic limits broad satisfaction."


    # eco
    menu:
        "Your city’s economy depends heavily on one industry that’s becoming unstable. What do you do?"

        "Invest in diversifying the economy by promoting other industries like technology and tourism.":
            $ update_scores(env=0, econ=20, social=10)
            "New industries bring innovation and stability to the city’s economy, but critics highlight the high upfront costs of diversification."

        "Provide financial aid to stabilize the existing dominant industry.":
            $ update_scores(env=-5, econ=10, social=5)
            "The industry stabilizes, saving jobs in the short term, but dependency on a single sector remains a long-term risk."

        "Attract foreign investment to develop a new economic sector.":
            $ update_scores(env=-5, econ=20, social=5)
            "Foreign investors bring capital and create jobs, but some citizens worry about external influence on local policies."

        "Do nothing and let the market correct itself naturally.":
            $ update_scores(env=0, econ=-10, social=-15)
            "The city’s economic instability grows, causing widespread job losses and public criticism of your inaction."

    #env
    menu:
        "Waste management is becoming a problem in your city. How will you address it?"

        "Mandate a city-wide recycling program with penalties for non-compliance.":
            $ update_scores(env=12, econ=-8, social=8)
            "Strict recycling rules reduce landfill waste and instill accountability but increase administrative costs."

        "Partner with private waste management companies for better processing.":
            $ update_scores(env=10, econ=-6, social=8)
            "Private partnerships bring efficient systems but add costs to the city budget."

        "Encourage citizen-led initiatives, such as composting and DIY recycling.":
            $ update_scores(env=10, econ=-5, social=10)
            "Citizen empowerment fosters sustainability with minimal government spending, though participation may be uneven."

        "Build a landfill outside the city without further measures.":
            $ update_scores(env=-15, econ=5, social=-10)
            "A landfill provides a short-term solution but worsens long-term waste issues and morale."

    #social
    menu:
        "Residents in certain parts of the city lack reliable access to clean drinking water. What’s your plan to address this issue?"

        "Build a sustainable water purification plant. Use renewable energy to power the facility, ensuring long-term access to clean water.":
            $ update_scores(env=15, econ=-10, social=15)
            "Your investment ensures equitable access to clean water, but critics warn of the high upfront cost and delays in implementation."

        "Subsidize water filters for affected households. Provide financial assistance for low-income families to purchase water filters.":
            $ update_scores(env=5, econ=-10, social=15)
            "Households quickly gain access to clean water, but systemic issues in water quality remain unresolved."

        "Enforce stricter industrial regulations. Fine polluting companies and invest in water quality monitoring systems.":
            $ update_scores(env=15, econ=-5, social=10)
            "Your regulations improve water safety and trust, but some industries express dissatisfaction with the stricter oversight."


    #eco
    menu:
        "A neighboring city offers lower taxes and is luring businesses away. How do you respond?"

        "Lower business taxes to match or undercut the neighboring city’s rates.":
            $ update_scores(env=0, econ=10, social=-5)
            "The lower taxes retain businesses, but the city’s revenue drops, limiting funds for public projects."

        "Invest in city infrastructure and amenities to attract businesses despite higher taxes.":
            $ update_scores(env=-5, econ=10, social=10)
            "Businesses recognize the value of a well-equipped city and stay, but the high cost of infrastructure strains the budget temporarily."

        "Create a partnership with the neighboring city to jointly promote economic growth.":
            $ update_scores(env=0, econ=5, social=5)
            "The partnership fosters regional cooperation and shared benefits, but growth is slower than pursuing independent initiatives."

        "Focus on retaining local businesses by offering targeted incentives.":
            $ update_scores(env=0, econ=10, social=5)
            "The city retains many local businesses, but critics argue that selective incentives could exclude smaller enterprises."

    #env
    menu:
        "A large corporation wants to build a factory in your city, offering jobs but at the cost of potential pollution. Do you approve their plan?"

        "Approve with strict environmental regulations.":
            $ update_scores(env=5, econ=10, social=10)
            "The factory brings jobs and economic growth while ensuring minimal environmental impact. However, strict regulations may increase operational costs, reducing the corporation's enthusiasm."

        "Approve with minimal restrictions to attract investment.":
            $ update_scores(env=-10, econ=20, social=5)
            "The factory boosts the economy and creates jobs but increases pollution, leading to potential long-term environmental degradation."

        "Reject the proposal outright to protect the environment.":
            $ update_scores(env=10, econ=-10, social=-5)
            "The city preserves its natural resources, but citizens miss out on potential job opportunities and economic benefits, causing mixed reactions."

    #social
    menu:
        "Citizens feel excluded from decisions on urban planning and development. How will you address this growing dissatisfaction?"

        "Create a citizen advisory board to provide input on major projects.":
            $ update_scores(env=5, econ=-5, social=20)
            "The advisory board empowers citizens and builds trust, but some developers complain about delays due to extended consultations."

        "Launch regular town hall meetings and surveys to collect citizen feedback.":
            $ update_scores(env=0, econ=0, social=10)
            "Citizens appreciate the opportunity to voice their opinions, but the lack of direct influence in decisions limits satisfaction."

        "Appoint a single citizen representative to the urban planning committee to streamline feedback.":
            $ update_scores(env=0, econ=0, social=5)
            "The appointment adds a layer of inclusivity but is criticized for not being representative of the broader community."

        "Maintain the current approach, focusing decisions solely on expert recommendations.":
            $ update_scores(env=0, econ=5, social=-15)
            "Development projects progress faster, but citizens feel increasingly alienated and distrustful of city leadership."

    #eco
    menu:
        "The city’s income inequality is growing, with the wealthy gaining significantly more than the poor. What do you do?"

        "Increase taxes on high-income earners and use the revenue for public services.":
            $ update_scores(env=0, econ=10, social=15)
            "Public services improve, and inequality decreases. However, wealthy individuals and businesses express dissatisfaction and consider relocating."

        "Focus on creating affordable access to education and job training for low-income groups.":
            $ update_scores(env=0, econ=10, social=10)
            "Education programs empower citizens and reduce inequality long-term, but the delayed results frustrate some communities."

        "Provide direct cash assistance to low-income households.":
            $ update_scores(env=0, econ=-5, social=15)
            "Households experience immediate relief, improving their quality of life. However, critics question the sustainability of this approach."

        "Do nothing, assuming economic growth will eventually trickle down.":
            $ update_scores(env=0, econ=-10, social=-15)
            "Income inequality worsens, sparking public outrage and protests against your leadership."

    #env
    menu:
        "Your city faces rising energy demands, but traditional energy sources are environmentally taxing. What is your plan?"

        "Invest in renewable energy infrastructure, like solar and wind farms.":
            $ update_scores(env=15, econ=-20, social=10)
            "Renewable energy ensures a sustainable and clean supply but requires significant upfront investment, delaying short-term economic benefits."

        "Encourage citizens to adopt energy-efficient practices with incentives.":
            $ update_scores(env=10, econ=-10, social=5)
            "Providing incentives encourages responsible energy use, though subsidies strain the city’s financial resources."

        "Build new natural gas plants for immediate energy supply.":
            $ update_scores(env=-5, econ=5, social=10)
            "Natural gas plants meet energy needs quickly and efficiently but contribute to emissions, albeit at a lower rate than coal plants."

        "Do nothing and manage with current energy infrastructure.":
            $ update_scores(env=-15, econ=0, social=-10)
            "Relying on the current infrastructure leads to energy shortages, blackouts, and citizen dissatisfaction, hindering overall quality of life."

    jump results


    

label results:
    show screen dashboard
    
    Female "Let's see how you've done!"
    
    # Score ranges for areas
    $ low = 50
    $ medium = 60
    $ high = 62
    
    # Determine the ending based on scores
    if econ_prosperity >= high and env_sustainability >= high and social_equity >= high:
        show bg city_thriving with dissolve
        "Under your leadership, Sustainopolis has become a global model of sustainability. The economy thrives, the environment flourishes, and citizens enjoy equality and opportunity. Your balanced vision has secured a prosperous future for generations, inspiring cities worldwide."    
    elif econ_prosperity >= high and env_sustainability <= low and social_equity <= low:
        show bg city_economic_powerhouse with dissolve
        "Sustainopolis is a booming economic hub, attracting businesses and driving innovation. However, environmental degradation and growing inequality cast a shadow over its success. The city’s future depends on addressing these critical challenges."
    
    elif env_sustainability >= high and econ_prosperity <= low and social_equity <= low:
        show bg city_environmental_haven with dissolve
        "Sustainopolis has become a green utopia, renowned for its pristine environment and sustainable living. However, economic struggles and growing inequality have left many citizens behind. Without a stronger economy and social cohesion, its future remains fragile."
    
    elif social_equity >= high and econ_prosperity <= low and env_sustainability <= low:
        show bg city_social_paradise with dissolve
        "Sustainopolis is celebrated for its fairness and equality. Every citizen enjoys access to housing, education, and healthcare. However, the weak economy and neglected environment strain the city’s long-term sustainability. Tough decisions lie ahead."
    
    elif econ_prosperity <= low and env_sustainability <= low and social_equity <= low:
        show bg city_in_crisis with dissolve
        "Sustainopolis has faltered under your leadership. Economic stagnation, environmental collapse, and growing inequality have left the city in turmoil. Once full of promise, it now serves as a stark reminder of the consequences of unbalanced leadership."
    
    elif econ_prosperity >= high and social_equity >= high and env_sustainability <= low:
        show bg city_econ_social with dissolve
        "Sustainopolis thrives with economic prosperity and social equity. Jobs are plentiful, and citizens enjoy a high quality of life. Yet, the environment suffers from neglect, with pollution and climate risks threatening the city’s future stability."
    
    elif econ_prosperity >= high and env_sustainability >= high and social_equity <= low:
        show bg city_econ_env with dissolve
        "Sustainopolis is a shining example of economic growth and environmental stewardship. The city prospers, running on clean energy and innovation. However, inequality has deepened, leaving many citizens behind. Achieving balance remains a challenge."
    
    elif social_equity >= high and env_sustainability >= high and econ_prosperity <= low:
        show bg city_social_env with dissolve
        "Sustainopolis is a green and inclusive city where nature and community thrive together. However, the weak economy struggles to support its ambitious vision. To ensure long-term success, economic resilience must be a future priority."
    
    else:
        show bg city_neutral with dissolve
        "Sustainopolis is doing well, but there’s still room for improvement!"
    
    hide bg 
    menu:

        "Restart the game":
            $ reset_scores()  # Reset scores before restarting
            scene black with dissolve  # Clear the current scene and show a black screen with a dissolve transition
            jump start  # Jump to the start of the game

        "Exit":
            return  # Exit the game


