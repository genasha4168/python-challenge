# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
totalVotes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
candidateVotes = {}

# Winning Candidate and Winning Count Tracker
winner_count = 0
winner = ""

# Open the CSV file and process it
with open(file_to_load) as electionData:
    reader = csv.reader(electionData)

    # Skip the header row
    header = next(reader)

    
    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        totalVotes = totalVotes + 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidates:
            candidates.append(candidate)                                # First appearance of the candidate in the file
            candidateVotes[candidate] = 1                               # Set vote counter to 1 for the candidate
        else:
            # Add a vote to the candidate's count
            candidateVotes[candidate] = candidateVotes[candidate] + 1   # Incriment the vote counter for the candidate 

# print(totalVotes)
# print(candidates)
# print(candidateVotes)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results \n")
    print("--------------- \n")
    print("Total Votes: %d\n" % totalVotes) 
    print("--------------- \n")

    # Write the total vote count to the text file
    txt_file.write("Election Results \n")
    txt_file.write("--------------- \n")
    txt_file.write("Total Votes: %d\n" % totalVotes)
    txt_file.write("--------------- \n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidateVotes:

        # Get the vote count and calculate the percentage
        votes = candidateVotes[candidate]
        votePercentage = float(votes)/float(totalVotes)*100

        # Update the winning candidate if this one has more votes
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voterOutput = f"{candidate}: {votePercentage:.3f}% ({votes})\n"

        # Print and save each candidate's vote count and percentage
        print(voterOutput)
        txt_file.write(voterOutput)

    # Generate and print the winning candidate summary
    winningSummary = (
        f"Winner: {winner}"
    )

    # Save the winning candidate summary to the text file
    print(winningSummary)
    txt_file.write(winningSummary)