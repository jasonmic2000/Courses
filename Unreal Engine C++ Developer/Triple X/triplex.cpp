#include <iostream>
#include <ctime>

void PrintIntroduction(int Difficulty)
{
    //Print welcome messages
    std::cout << "\nYou are a secret agent breaking into a level " << Difficulty;
    std::cout << " secure server room...\nEnter the correct code to continue...\n\n";
}

bool PlayGame(int Difficulty)
{
    PrintIntroduction(Difficulty);

    //Declare 3-digit code
    const int CodeA = rand() % Difficulty + Difficulty;
    const int CodeB = rand() % Difficulty + Difficulty;
    const int CodeC = rand() % Difficulty + Difficulty;

    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;

    //Print CodeSum and CodeProduct
    std::cout << "There are 3 numbers in the code\n";
    std::cout << "The codes add-up to: " << CodeSum;
    std::cout << "\nThe product of the codes is: " << CodeProduct;
    
    //Store player guess
    int GuessA, GuessB, GuessC;
    std::cout << "\n\nEnter your guess: ";
    std::cin >> GuessA >> GuessB >> GuessC;
    
    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    //Check if player guess is correct
    if(GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "\n*** Great work! You've extracted a file! Keep going agent! ***\n";
        return true;
    }
    else
    {
        std::cout << "\n*** Incorrect code! Try Again! ***\n";
        return false;
    }
}

int main()
{
    srand(time(NULL)); // create random sequence based on time of day

    int Difficulty = 1;
    const int MaxDifficulty = 5;
    
    while (Difficulty <= MaxDifficulty) // Loop game until all levels are completed
    {
        bool bLevelComplete = PlayGame(Difficulty);
        std::cin.clear(); // Clears any errors
        std::cin.ignore(); // Discards the buffer

        if (bLevelComplete)
        {
            // increase difficulty
            ++Difficulty;
        }
        
    }
    
    std::cout << "*** Good job agent! You got all the files! Now get out of there! ***\n";

    return 0;
}