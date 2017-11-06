# IDEA_drive

## What is this for
This is a lib used to work with the IDEA Drives from Haydon Kerk. Great for
quick prototyping of stepper drives.

[Drive Link](http://www.haydonkerkpittman.com/products/drives/steppermotorprogrammabledrives/acm4806e-acm4826e)
[Protocol Doc](http://www.haydonkerkpittman.com/-/media/ametekhaydonkerk/downloads/products/drives/idea_drive_communication_manual.pdf?la=en)

## What is included?
Currently a python lib that only requires the pyserial lib. Simply import it
and call what functions are needed.

Also included is a minimum protocol use in C. Simply pass in buffer, and write
that buffer to a serial or rs485 device.


## Is this complete?
Nope, there are a lot of features the IDEA drives have that I didn't use and aren't in the lib. 

Another item is some of the queries need format out of the response to return 
important info. Example: query the current position and there will be a prefix and suffix wrapped
around the position info.

## License
MIT

## Authors
mr337
