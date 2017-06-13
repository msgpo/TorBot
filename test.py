import sys

from stem.connection import connect

if __name__ == '__main__':
  controller = connect("Narayanan123")

  if not controller:
    sys.exit(1)  # unable to get a connection

  print ("Working")
  controller.close()