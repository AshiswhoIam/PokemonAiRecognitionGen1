# PokemonAiRecognitionGen1
This repository will be for the creation of a Pokemon AI recognition model

Step 1 Gathering & cleaning of data, for now the aim is to gather 100~ different images for each pokemon.

Primary data source being used: https://www.kaggle.com/datasets/mikoajkolman/pokemon-images-first-generation17000-files
Used https://www.kaggle.com/datasets/lantian773030/pokemonclassification/code for the 7missing pokemons
Images added from cards, shows and google images.

Nidoran Male and Female manually done.

Cleaning out duplicates for now and adding personal images.
Most of the duplicates have been deleted as well as some of the data augmented data.
Gifs have been cleared, might do some file conversion maybe.


So far 18/151 is done 2/13
Update its 2/15 12:44am 31/151 is done
Update its 2/16 12:09am 47/151 is done
Update its 2/16 8:54 65/151 is done
Update its 2/17 12:29am 73/151 is done
Update its 2/17 8:05pm 90/151 is done
Update its 2/17 10:58pm 95/151 is done
Update its 2/18 6:20pm 114/151 is done
Update its 2/18 11:14pm 132/151 is done 10 left means there is 9pokemon files missing.
Update 2/19 10:00pm 151/151 are done just need to go over each file convert the gifs, also labeled nidoran with M and F will have to take care of that after.

Hitmonlee missing 1 image, squirtle had an extra.

~first model had about 0.71%acc only using 1 epoch
using 5epoch 3.71%
with 10 epochs - > 9.9%

Next making changes adding another layer 512 and lowering learning rate 0.0005->0.0002 + making it 20epochs OVERfitted
adding early stoppage


Tensorflow 2.4.0
Python 3.7.16
Cuda 11.0
Cudnn 8.1.0