# The Reformed Devs Monthly Challenge

## October 2019

### Background

Birthed out of our Slack org, The Reformed Devs have begun monthly coding challenges for its members, hoping to encourage critical thinking and problem and solving and foster community. You can see our previous challenges here:

* [April 2019](https://github.com/plusuncold/longest-word-test)
* [May 2019](https://github.com/plusuncold/rainfall-calc-challenge)
* [June 2019](https://github.com/ReformedDevs/challenge-2019-06)
* [July 2019](https://github.com/ReformedDevs/challenge-2019-07)
* [September 2019](https://github.com/ReformedDevs/challenge-2019-09)

### This Month's Challenge

#### Problem

Given a random string of letters whose length is between 4 and 7, inclusive, what is the highest scoring valid word that you can make using the group of letters? Scoring is based on Scrabble letter point values (see `data/letters.json`). Word validity will be based on a dictionary included in the repo (`data/dictionary.txt`).

Inputs will be given as a lowercase string. Dictionary file is all lowercase as well.

Examples:

Given the input letters `abc` your max score would be 7. A=1, B=3, C=3, and there are multiple words that can be formed using all letters.

Given the letters `iisq`, your max score would be 10. I=1, S=1, Q=10, and none of the multi letter words that can be formed score higher than just Q itself.

#### Timing

What should be timed? Generally speaking, nearly everything. Historically the following are excluded from your timer: Importing libraries/modules, setting constants, setting test input, printing the solution. Everything else should be inside your timer, including loading the dictionary.

#### Output

Running your solution should output your info in the following format: `username, language, word formed, score, time in ms, notes`.

Using the first example from above, example output might be: `specs, Python3, cab, 7, 130, these are the notes`.

#### Scoring

**Important**: Make sure your solution can take an input. The letters to handle will be sent as a string in a BASH variable. See example folder for details on how this will work.

Each solution will be run 5 times with same input and the time and solution recorded. Any solution that doesn't submit the same score every time for the same input will be counted as invalid.

There will be 5 randomized valid inputs (i.e. each solution will be run 25 times.) The times will be averaged. Ranking will be based on average time. If your calculated highest score is not the same as the rest of the solutions, your solution will be counted invalid.

A dump of all solution data will be put into a JSON file in this directory, and the Leaderboard and Oops sections will be updated below with summary data.

### Solution Setup

Put each of your submitted solutions in its own directory at the root of the project. Any directory that is named `alphanumeric-alphanumeric` will be picked up by the test container, but general convention is use `yourlanguage-yourname/handle`.

Your solution directory should include the following:

* `build.sh` file (only if you need to build/compile your solution)
* `run.sh` file (a shell file that has the command to execute your solution)
  * **Important**: Make sure your solution can take an input. The letters to handle will be sent as a string in a BASH variable. See example folder for details on how this will work.
* the file(s) needed to build and run your solution.

See the `example` directory for more guidance.

*Note*: You might need to update the Docker build file if your language is not yet supported (see below.) If you need help, ask in #monthly-challenge in Slack.

### Running the Tests (I.e. Docker and Stuff)

The Docker image is now moved to its own repo and is hosted on Dockerhub.

* [Source](https://github.com/ReformedDevs/challenge-docker)
* [Dockerhub](https://hub.docker.com/r/drewpearce/trd-challenge)

The image tagged 2019.10 currently supports these languages:

* C/C++
* .NET
* Node 11
* Python 3.6
* Ruby
* Rust

If you want to add support for another language, you can make a PR to the Source repo referenced above. If you need help, come on over to the #monthly-challenge channel on our Slack.

You can build the container locally by running `./build_docker.sh`.

You can run the container lcoally by running `./run_docker.sh` after building the container.

You can run the tests locally (assuming you have all the language support installed) by running `python(3) run_solutions.py`.

If you only want to run specific directories on a local run (i.e. just test your solution), run `python(3) run_solutions.py comma-separated,list-of,solution-dirs`.

### Leaderboard

__Test timestamp__: 2019-10-14T13:49

__Inputs__: _deuabi, amubhmz, rwjolup, ldaseta, qijc_

Author | Language | Word | Score | Time (ms) | Notes
--- | --- | --- | --- | --- | ---
plusuncold | C++ | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 6.6 | 
pard68 | Rust | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 17.21393064 | Give me `iter()` or give me death
patrickcarver | Crystal | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 50.84 | your face is a abide
cork | Node | daube, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 61.43886184 | Put some FP and async on it
cco3 | javascript | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 62.0 | sparse arrays
zombeej | Node | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 62.64621536 | aannngggeerrrr
specs | Python 3 | daube, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 74.893798828125 | strolling down the yeet
pard68 | Python3 | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 89.72478251999974 | snek can snek into snek
Kyle Nweeia | Python 3 | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 98.5962341199984 | 
basking2 | ruby | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 104.04958984375 | ARG: ["deuabi"]
cco3 | javascript | abide, za, jowl, estadal, q | 8, 11, 14, 8, 10 | 157.87999999999997 | obscure

