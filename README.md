# PokemonAiRecognitionGen1
This repository will be for the creation of a Pokemon AI recognition model

Step 1 Gathering & cleaning of data, for now the aim is to gather 100~ different images for each pokemon.

Primary data source being used: https://www.kaggle.com/datasets/mikoajkolman/pokemon-images-first-generation17000-files
Used https://www.kaggle.com/datasets/lantian773030/pokemonclassification/code for the 7missing pokemons
Images added from cards, shows and google images.

Nidoran Male and Female manually done.

Cleaning out duplicates for now and adding personal images.
Most of the duplicates have been deleted as well as some of the data augmented data.
Gifs have been cleared
Some Data augmentation was later done for more accuracy.
Note: can probably get better results if data is more properly cropped.

Currently During Model training data is still overfitting results getting better as more modifications done.
So far the best model is of  73.18% accuracy model#11 was renamed to become main.
Can View Track.txt for tryouts.

List of things to do now:
Tryout random image from internet like guessing game for the ai.
Mybe more trials.

Good progress being made so far from 11 ->13, model 11 only ided 100pokemons now model 13 is only missing 10

Versions used for model training:
Tensorflow 2.4.0
Python 3.7.16
Cuda 11.0
Cudnn 8.1.0
(swapped to other env for other functionalities sometimes)