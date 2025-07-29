#include <cs50.h>
#include <strings.h>
#include <stdio.h>
#include <ctype.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
	{
		candidates[i].name = argv[i + 1];
		candidates[i].votes = 0;
	}

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // Compare the name typed by the user with the candidates names, ignoring case
        if (strcasecmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes ++;
            return true;
        }
    }
    // If any candidate was found, so the candidate name typed by the user is invalid
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int higher = 0;
    // Let's compare the number of votes of which one
    for (int i = 0; i < candidate_count - 1; i++)
    {
        if (i == 0)
        {
            // If they are equal, doesn't matter if its the index of 'i' or 'i + 1'
            if (candidates[i].votes >= candidates[i + 1].votes)
            {
                higher = candidates[i].votes;
            }
            if (candidates[i + 1].votes > candidates[i].votes)
            {
                higher = candidates[i + 1].votes;
            }
        }
        else
        {
            // If a candidate's votes number is higher than the 'higher' variable, the 'higher' receives that value
            if (candidates[i].votes > higher)
            {
                higher = candidates[i].votes;
            }
            if (candidates[i + 1].votes > higher)
            {
                higher = candidates[i + 1].votes;
            }
        }
    }
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == higher)
        {
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}
