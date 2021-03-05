from Player import Player
from AiStuff import MainAi
from one import *

choice = input("Do you want to play AI or 1 v 1? Enter AI or 1: ")
if choice == "AI":
    MainAi.runAI()
elif choice == "one":
    runOne()
