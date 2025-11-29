label start:
    #This is the beginning video
    $ renpy.movie_cutscene("videos/1.mp4")
    
    #The first scene
    define ship = "photos/0.jpg"
    scene ship
    show ship at center