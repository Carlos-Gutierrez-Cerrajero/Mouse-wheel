# Mouse-wheel

## Description
<p id="Description">
  A small script I wrote when my mouse wheel gave up on me to tide me over while I got a new mouse. Allows the user to bind any key to simulate mouse wheel movements. It doesn't have a mouse wheel click event binding because that still worked for me, but it should be easy enough to add if needed.
</p>

## Dependencies
<p id="Dependencies">
  Language: Python 3<br>
  Modules: <a href="https://pypi.org/project/keyboard/">keyboard</a> and <a href="https://pypi.org/project/mouse/">mouse</a> (logging and time as well, but those are part of the standard library).
</p>

## Usage
<p id="Usage">
  Run mouse_wheel.py<br>
  The program will ask to bind a key to mouse wheel up and a key to mouse wheel down. From then on, the program will trigger a mouse wheel up or down event when the chosen key is pressed. Close program when finished.<br>
  <b>WARNING</b>: The program does not remove the original key input. In other words, binding "mouse wheel up" to "Z", means that pressing the Z key will send both a "Z" event <i>and</i> a "mouse wheel up" event
</p>
