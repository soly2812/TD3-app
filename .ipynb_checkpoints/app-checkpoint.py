{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ba2bc0b1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "# app.py\n",
    "import pygame\n",
    "import sys\n",
    "\n",
    "# Initialize Pygame\n",
    "pygame.init()\n",
    "\n",
    "# Set up display\n",
    "width, height = 800, 600\n",
    "screen = pygame.display.set_mode((width, height))\n",
    "pygame.display.set_caption(\"Bouncing Ball\")\n",
    "\n",
    "# Set up colors\n",
    "white = (255, 255, 255)\n",
    "\n",
    "# Set up the ball\n",
    "ball_radius = 20\n",
    "ball_color = (0, 128, 255)\n",
    "ball_x, ball_y = width // 2, height // 2\n",
    "ball_speed_x, ball_speed_y = 5, 5\n",
    "\n",
    "# Main game loop\n",
    "while True:\n",
    "    for event in pygame.event.get():\n",
    "        if event.type == pygame.QUIT:\n",
    "            pygame.quit()\n",
    "            sys.exit()\n",
    "\n",
    "    # Update ball position\n",
    "    ball_x += ball_speed_x\n",
    "    ball_y += ball_speed_y\n",
    "\n",
    "    # Bounce off the sides of the box\n",
    "    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:\n",
    "        ball_speed_x = -ball_speed_x\n",
    "    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:\n",
    "        ball_speed_y = -ball_speed_y\n",
    "\n",
    "    # Clear the screen\n",
    "    screen.fill(white)\n",
    "\n",
    "    # Draw the ball\n",
    "    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)\n",
    "\n",
    "    # Update the display\n",
    "    pygame.display.flip()\n",
    "\n",
    "    # Control the frame rate\n",
    "    pygame.time.Clock().tick(30)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c7e31e15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pygame\n",
      "  Downloading pygame-2.5.2-cp39-cp39-win_amd64.whl (10.8 MB)\n",
      "Installing collected packages: pygame\n",
      "Successfully installed pygame-2.5.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "#pip install pygame"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
