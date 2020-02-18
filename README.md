# Running Apps With Docker
I am practicing the various Docker uses, one of them being that I can run applications of different languages and extensions 
with Docker.

How This Application Works:
  - Run the Python server and the route /html will take you to a page that renders some raw HTML
  - When route /html is triggered, it will call 4 Dockerfiles that each run a program written in a different language
  - Once the Dockerfiles run, the code inside them will output something to the console
