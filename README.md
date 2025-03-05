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

Keeping Track=>
Stats 32batch, 4 cv layers,l2=0.005,lr=0.00005,drop = 0.4

Current trial => Test accuracy: 43.40%
Test Loss: 3.4019
loss: 0.6550 - accuracy: 0.9936 - val_loss: 3.3664 - val_accuracy: 0.4428



Now we change and try =>
Stats 64batch, 4 cv layers,l2=0.001,lr=0.0001,drop = 0.3 + extra dense layer

loss: 0.7143 - accuracy: 0.9741 - val_loss: 2.8477 - val_accuracy: 0.5373
Test accuracy: 53.07%
Test Loss: 2.8312

Now we change and try =>
Stats 64batch,5 cv layers,l2=0.0005,lr=0.0002,drop = 0.2 + extra dense layer+convextra+lr schedeuler
GOOD NEWS
- loss: 0.2907 - accuracy: 0.9946 - val_loss: 1.9350 - val_accuracy: 0.6724
Test accuracy: 64.19%
Test Loss: 1.9604

Stoppped around 18/30


Now we change and try =>
From the previous try added 1 more dense layer, more patience adjusted Lr rate sonner


- loss: 0.1854 - accuracy: 0.9997 - val_loss: 1.4380 - val_accuracy: 0.7135
Test accuracy: 69.80%
Test Loss: 1.4253

Stoppped around 25/30 epoch



Now we change and try =>
1024->768 0.3 droupout  LReg to 0.001

- loss: 0.3544 - accuracy: 0.9962 - val_loss: 1.5703 - val_accuracy: 0.7007

Test accuracy: 68.83%
Test Loss: 1.5818

Now we change and try => 
increase in dropoout to 0.4 and kernel 5x5 for 1st and 0.0001 lr

loss: 0.7444 - accuracy: 0.9182 - val_loss: 1.6642 - val_accuracy: 0.6675
Test accuracy: 66.75%
Test Loss: 1.6762

This is better model is learning better doing less overfitting less memo

Now we change and try => 
adding one more cv layer512, learning rate to 0.0002 and 0.5 dropout, patience to 4 epoch to 40
- loss: 0.6883 - accuracy: 0.8831 - val_loss: 1.6740 - val_accuracy: 0.6512
Test accuracy: 65.39%
Test Loss: 1.6714

Now we change and try => 

epoch 45 , taking off 1 cv layer, increase learning to 0.0003  l2 is 0.0005

- loss: 0.6691 - accuracy: 0.8637 - val_loss: 1.4780 - val_accuracy: 0.6790
Test accuracy: 67.02%
Test Loss: 1.4883

Now we change and try => 

drop 0.4, 50epochs, learning rate to 0.0002, 4layers this time nvm 4 layers way too low


using .6

 - loss: 0.8852 - accuracy: 0.7886 - val_loss: 1.5368 - val_accuracy: 0.6706

Test accuracy: 65.17%
Test Loss: 1.5684

Tensorflow 2.4.0
Python 3.7.16
Cuda 11.0
Cudnn 8.1.0