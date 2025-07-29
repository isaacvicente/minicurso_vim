import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATABASE.csv SEQUENCES.txt")
        sys.exit(1)

    # Read database file into a variable
    with open(sys.argv[1]) as database_file:
        database_reader = csv.DictReader(database_file)
        # Initialize our list of dictionaries (with the name's key and all of STRs' keys as well)
        database = []
        # Each row of the database_reader is a dictionary itself
        for row in database_reader:
            # Create a list of dictionaries, wherein each list represents a person's info (their name and their STRs)
            database.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as sequences_file:
        sequences = sequences_file.read()

    # Find longest match of each STR in DNA sequence

    # Initialize our STRs dict, in which each STR has the longest match value found in the sequence given by the user
    STRs = {}
    for list in database:
        for key in list:
            # Recall that each list is a dict itself
            # An example we would have: {'name': 0, 'AGATC': 2, 'AATG': 8, 'TATC': 3}
            # (of course that the STR "name" doesn't exist, so its longest match is 0)
            STRs[key] = longest_match(sequences, key)

    # Check database for matching profiles

    # Initiliaze our match variable to False, as we didn't match anything yet
    match = False
    # Think a list as a person with their information (the name key and all the STRs keys)
    for list in database:
        for key in list:
            # Skip the "name" key, as we're only comparing STRs
            if key != "name":
                # Update match to True if we found a match between the database and a person's STRs
                if STRs[key] == int(list[key]):
                    match = True
                # If we didn't match, update match to False and break the inner loop, so we go to the next list (i.e., person)
                else:
                    match = False
                    break
        # If we passed through a list and matched all of the STRs, print the person's name
        if match:
            print(list["name"])
            # Break the main loop, as we already found the person
            break

    # If not match at all, print "No match"
    if not match:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

