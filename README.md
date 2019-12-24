# Virtual Mouse
OS Required: This project can be made to run smootly on ubuntu  . Running this on mac  will raise problems as some functions in modules are not supported . Project smootly runs on mac based ubuntu , but we shall also install camera  boot drivers as web camera permission is not given to ubuntu .

MODULES :
  Project is supported by opencv version 3.4.5.20. (the latest update was made on Jan 9 2019, 3.4.5.20 was updated to 4).Some functions were changed and modified in 4 . 
  We can install opencv 3.4.5.20 using                          pip install opencv-python==3.4.5.20
  We can install pynput module (version 1.4) using              pip install pynput
  We can install pyautogui module(version 0.9.39)  using        pip install PyAutoGUI

To run the program firstly we shall  tape a dark -green coloured tape(rectangle shaped around 1 inch ) on our finger .
More details in the images folder

Precautions shall be taken that no object in the surroundings match to the color .(Sometimes the black color of our hair gets identified as dark green (based on brightness,webcam specifications))

When you run the program , a tab appears (webcam application opens ) and you can see three rectangles . For more details screenshots are available in image folder . 

As you move your taped fingers in those boxes the cursor of mouse moves, left click right click happens 

For Moving the mouse:
	If we move any dark green object,preferably a small piece of tape applied on fingers in the blue rectangle , mouse goes to that position(the top left vertex of the rectangle) . 

For Single click (LEFT CLICK) :
	By holding our hand at the position where we want to left click( in the blue box ) we shall also bring another finger(taped with dark green ) on to left  pink box  
	Single click is not more reliable in this project as we humans are not too accurate or fast to remove the hand just after it is clicked , as our hand remains there(even if it is a millisecond) rleft click happens again which will turnout to be double click.

For Double click :
	As said, even if we try to do single click double click happens, but double click also happens when you first place the mouse on the  position where we want to double click  using a taped finger , and then bring another taped finger in the blue rectangle .

For Right Click :
	This also has its limitations. Right click is well defined only in windows .Though it doesnt works in ubuntu or mac , it can we achieved by doing the same  as that of left click but the second taped finger shall be brought in the right box.  
  
  This project is not user-friendly as our hands (fingers) keep shaking and do not stay in the correct position . Bringing in other finger for other operations sometimes disturb the position of cursor . A lot of care shall be taken for clicks.
