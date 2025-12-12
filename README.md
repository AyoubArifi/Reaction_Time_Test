# Reaction Time Test

A Python-based reaction time test built with Pygame.\
The task presents visual stimuli after randomized delays and records
the participant’s responses over 40 trials.\
The script collects participant name, handles early key presses,
provides on-screen feedback, and exports all reaction times
to a structured CSV file for further analysis.

## Features

-   Collects participant name before starting the task\
-   Random delay (1--3 seconds) before each stimulus\
-   Red circle stimulus displayed in fullscreen\
-   Measures reaction times with high precision\
-   Handles early key presses\
-   40 trials by default (can be changed)\
-   Saves results into a structured CSV file\
-   Clean, minimal interface using Pygame

## How to Run the Experiment

### 1. Install Python dependencies

    pip install pygame

### 2. Run the script

    python reaction_time_test.py

## How the Experiment Works

  Stage                 Description
  --------------------- -----------------------------------------------
  **1. Name Input**     Participant enters their name
  **2. Start Screen**   Press SPACE to begin
  **3. Random Delay**   Screen stays white for 1--3 seconds
  **4. Stimulus**       A red circle appears in the center
  **5. Response**       Participant presses SPACE as fast as possible
  **6. Feedback**       Reaction time displayed for 0.5 seconds
  **7. Repeat**         Runs for 40 trials(can be changed in the via code)

## Output: CSV File

After the experiment ends, a CSV file is created:

    <participant_name>_reaction_times.csv

It contains:

  Trial   Reaction Time (s)
  ------- -------------------
  1       0.421
  2       0.389
  ...     ...

## Settings You Can Modify

Inside `reaction_time_test.py`:

  Variable     Purpose              Default
  ------------ -------------------- ----------
  MAX_TRIALS   Number of trials     40
  radius       Circle size          80
  delay        Random delay range   1--3 sec

## Requirements

-   Pygame

## License

MIT License --- free to use, modify, and share.

## Author
    Ayoub Arifi
Developed by ایوب (Ayub)
