# Slide and Catch Part 2 Blackbelt

The game will be a slide and catch game. The player is Wednesday the Black Cat and has the goal of collecting 10 leaves in 10 seconds. If they are successful, they win. If they fail to collect 10 leaves, they lose. If they catch an apple, 1 point is subtracted from their score. 

## Assets

1. Wednesday.png taken by Marianne Adams in December 2023
2. FallScene.png taken by Marianne Adams at Legion Park October 24, 2022
3. FallLeaf.png from https://openclipart.org/detail/257622/leaf by NicholasJudy456
4. Apple.png from https://openclipart.org/detail/217047/apple by cwleondard.

## Game Class

### Initializing

Define new class called Game. Game utilizes simpleGE.Scene. Initialize Scene. Add "FallScene.png" as background image. 

Initialize Wednesday class. We only want 1 Wednesday.

Initialize Leaves. We want 10 leaves. 

Initialize Apples. We want 2 apples. 

Initialize score label. 

Initialize time label

Make list of sprites--sprites included in the game will be Wednesday, leaves, apples, score label, and time label. 

### Process Method

Start For loop. Check if Wednesday collides with leaf, if yes, reset and add 1 to score. Reload score label with new score. 

Start For loop. Check if Wednesday collides with apple, if yes, reset and subtract 1 from score. Reload score label with new score. 

Display time left. If time left is less than 0, display final score. If final score is less than 10, lose. If final score is greater than or equal to 10, win. Stop scene. 

## Wednesday Class 

### Initializing

Define new class called Wednesday. Wednesday utilizes simpleGE.Sprite and the scene. Add "Wednesday.png" and scale size to 75 x 75. Position starts at (320, 400) with moveSpeed 5.

### Process Method

Check if left arrow key is pressed. If left arrow pressed, move speed is negative. Check if right arrow key is pressed. If right arrow pressed, move speed is positive. 

## Leaf Class

### Initializing

Define new class called Leaf. Leaf uses simpleGE.Sprite and the scene. Add "FallLeaf.png" and scale size to (30, 30). Set min speed to 3 and max speed to 8. Call reset method.

### Reset Method

Leaf x position gets a random integer between 0 and screen width. Leaf y position gets 0. Leaf's dy (ie, speed) gets a random integer between the min speed and the max speed. 

### CheckBounds Method

Check if the bottom of the image is greater than the screen height. If so, reset.

## Apple Class

### Initializing

Define new class called Apple. Apple uses simpleGE.Sprite and the scene. Add "Apple.png" and scale size to (30, 30). Set min speed to 3 and max speed to 8. Call reset method.

### Reset Method

Apple x position gets a random integer between 0 and screen width. Apple y position gets 0. Apple's dy (speed) gets a random integer between the min speed and the max speed. 

### CheckBounds Method

Check if the bottom of the image is greater than the screen height. If so, reset. 

## LblScore Class

LblScore class uses simpleGE.Label. Label text will read "Score: 0". Label centered at (100, 30). 

## LblTime Class

LblTime class uses simpleGE.Label. Label text will read "Time Left: 10". Label centered at (500, 30). 

## Instructions Class

### Initializing

Instructions takes simpleGE.Scene and score. Set background image to "FallScene.png". Default response is "Play". Use simpleGE.Multilabel and store in self.instructions. Display label text: 

> You are Wednesday the Black Cat. Move with the left and right arrow key and catch 10 leaves while avoiding apples to win. Good luck!\

Center instructions at (320, 240).  Size instructions to (500, 250). 

Display previous score and center at (320, 400). 

Create Play button using simpleGE.Button(). Button text should read "Play (up)". Center button at (100, 400). 

Create Quit button using simpleGE.Button(). Button text should read "Quit (down)". Center button at (550, 400). 

Add list of sprites. 

### Process Method

#### Define Button Behavior

If "Quit" button is clicked, response gets "Quit" and instructions scene ends. If "Play" button is clicked, response gets "Play" and instructions scene ends. 

#### Define Arrow Key Behavior

If up key is pressed, response gets "Play" and instructions scene ends. If down key is pressed, response gets "Quit" and instructions scene ends.

## Win Class

### Initializing 
Win takes simpleGE.Scene and score. Set background image to "FallScene.png". Use simpeGE.multilabel stored in self.win. Textbox should read:

> Congratulations! You won!

Center at (320, 240). Set size to (500, 250). 

Display score in a label centered at (320, 400). 

Create "Play Again" button with simpleGE.button(). Button should read "Play Again (up)". Center at (100, 400). Create "Quit" button with simpleGE.button(). Button should read "Quit (down)". Center at (550, 400). 

Add list of sprites.

### Process Method

Check for button click or key press. Similar to Instructions class. 

## Lose Class

Lose takes simpleGE.Scene and score. Set background image to "FallScene.png". Use simpleGE.multilabel stored in self.lose. Textbox should read:

> Uh-oh! You lost!

Center at (320, 240). Set size to (500, 250). 

Display score in label centered at (320, 400). 

Create "Play Again" button with simpleGE.button(). Button should read "Play Again (up)". Center at (100, 400). Create "Quit" button with simpleGE.button(). Button should read "Quit (down)". Center at (550, 400). 

Add list of sprites.

### Process Method

Check for button click or key press. Similar to Instructions class. 

## Main 

Sentry variable keepGoing. Initial score 0. Start while keepGoing loop. Display instructions. If "Play", play the game. If "Win", display Win screen. If "lose", display Lose screen. Otherwise, keepGoing gets false. 



