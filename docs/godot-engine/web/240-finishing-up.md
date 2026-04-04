# Finishing up

# Finishing up
We have now completed all the functionality for our game. Below are some
remaining steps to add a bit more "juice" to improve the game experience.
Feel free to expand the gameplay with your own ideas.

## Background
The default gray background is not very appealing, so let's change its color.
One way to do this is to use aColorRectnode. Make it
the first node underMainso that it will be drawn behind the other nodes.ColorRectonly has one property:Color. Choose a color you like and
select "Layout" -> "Anchors Preset" -> "Full Rect" either in the toolbar at the top of the viewport or in the inspector so that it covers the screen.
You could also add a background image, if you have one, by using aTextureRectnode instead.

## Sound effects
Sound and music can be the single most effective way to add appeal to the game
experience. In your game'sartfolder, you have two sound files: "House In a
Forest Loop.ogg" for background music, and "gameover.wav" for when the player
loses.
Add twoAudioStreamPlayernodes as children ofMain. Name one of themMusicand the otherDeathSound. On each one,
click on theStreamproperty, select "Load", and choose the corresponding
audio file.
All audio is automatically imported with theLoopsetting disabled.
If you want the music to loop seamlessly, click on the Stream file arrow,
selectMakeUnique, then click on the Stream file and check theLoopbox.
To play the music, add$Music.play()in thenew_game()function and$Music.stop()in thegame_over()function.
Finally, add$DeathSound.play()in thegame_over()function.
```
func game_over():
    ...
    $Music.stop()
    $DeathSound.play()

func new_game():
    ...
    $Music.play()
```
```
public void GameOver()
{
    ...
    GetNode<AudioStreamPlayer>("Music").Stop();
    GetNode<AudioStreamPlayer>("DeathSound").Play();
}

public void NewGame()
{
    ...
    GetNode<AudioStreamPlayer>("Music").Play();
}
```

## Keyboard shortcut
Since the game is played with keyboard controls, it would be convenient if we
could also start the game by pressing a key on the keyboard. We can do this with
the "Shortcut" property of theButtonnode.
In a previous lesson, we created four input actions to move the character. We
will create a similar input action to map to the start button.
Select "Project" -> "Project Settings" and then click on the "Input Map"
tab. In the same way you created the movement input actions, create a new
input action calledstart_gameand add a key mapping for theEnterkey.
Now would be a good time to add controller support if you have one available.
Attach or pair your controller and then under each input action that you wish
to add controller support for, click on the "+" button and press the corresponding
button, d-pad, or stick direction that you want to map to the respective input action.
In theHUDscene, select theStartButtonand find itsShortcutproperty in the Inspector. Create a newShortcutresource
by clicking within the box, open theEventsarray and add a new array element
to it by clicking onArray[InputEvent] (size 0).
Create a newInputEventActionand select thestart_gameaction.
Now when the start button appears, you can either click it or pressEnterto start the game.
And with that, you completed your first 2D game in Godot.
You got to make a player-controlled character, enemies that spawn randomly
around the game board, count the score, implement a game over and replay, user
interface, sounds, and more. Congratulations!
There's still much to learn, but you can take a moment to appreciate what you
achieved.
And when you're ready, you can move on toYour first 3D gameto learn
to create a complete 3D game from scratch, in Godot.

## Sharing the finished game with others
If you want people to try out your game without having to install Godot, you'll
need to export the project for each operating system you want the game to be
playable on. SeeExporting projectsfor instructions.
After exporting the project, compress the exported executable and PCK file (not
the raw project files) to a ZIP file, then upload this ZIP file to a file
sharing website.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.