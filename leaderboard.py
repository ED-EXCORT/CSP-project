# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# Set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# Return names in the leaderboard file
def get_names(file_name):
    leaderboard_file = open(file_name, "r")  # Be sure you have created this

    # Use a for loop to iterate through the content of the file, one line at a time
    # Note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
    names = []
    for line in leaderboard_file:
        leader_name = ""
        index = 0

        # TODO 1: Use a while loop to read the leader name from the line (format is "leader_name,leader_score")
        while (line[index] != ","):
            leader_name += line[index]
            index += 1

        # TODO 2: Add the player name to the names list
        names.append(leader_name)

    leaderboard_file.close()

    # TODO 6: Return the names list in place of the empty list
    return names

# Return scores from the leaderboard file
def get_scores(file_name):
    leaderboard_file = open(file_name, "r")  # Be sure you have created this

    scores = []
    for line in leaderboard_file:
        leader_score = ""    
        index = 0

        # TODO 3: Use a while loop to index beyond the comma, skipping the player's name
        while line[index] != ",":
            index += 1
        # Move index one step forward to skip the comma
        index += 1

        # TODO 4: Use a while loop to get the score
        while line[index] != "\n" and index < len(line):
            leader_score += line[index]
            index += 1

        # TODO 5: Add the player score to the scores list
        scores.append(int(leader_score))

    leaderboard_file.close()

    # TODO 7: Return the scores in place of the empty list
    return scores

# Update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

    index = 0
    # TODO 8: Loop through all the scores in the existing leaderboard list
    for i in range(len(leader_scores)):
        # TODO 9: Check if this is the position to insert new score at
        if player_score > leader_scores[i]:
            index = i
            break
        else:
            index = len(leader_scores)

    # TODO 10: Insert new player and score
    leader_names.insert(index, player_name)
    leader_scores.insert(index, player_score)

    # TODO 11: Keep both lists at 5 elements only (top 5 players)
    leader_names = leader_names[:5]
    leader_scores = leader_scores[:5]

    # TODO 12: Store the latest leaderboard back in the file
    leaderboard_file = open(file_name, "w")  # This mode opens the file and erases its contents for a fresh start
 
    # TODO 13: Loop through all the leaderboard elements and write them to the file
    for i in range(len(leader_names)):
        leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")

    leaderboard_file.close()

# Draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  
    # Clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160,100)
    turtle_object.hideturtle()
    turtle_object.down()

    # Loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    for index in range(len(leader_names)):
        turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
        turtle_object.down()
  
    # Move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # TODO 14: Display message about player making/not making leaderboard
    if high_scorer:
        turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
    else:
        turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)

    # Move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()
  
    # TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
    if player_score >= gold_score:
        turtle_object.write("You earned a gold medal!", font=font_setup)
    elif player_score >= silver_score:
        turtle_object.write("You earned a silver medal!", font=font_setup)
    elif player_score >= bronze_score:
        turtle_object.write("You earned a bronze medal!", font=font_setup)