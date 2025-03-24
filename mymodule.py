from random import choice

# This is a user defined module.

language = "Python"

def randomfunfact():
    funfacts = [
        "Python is a programming language.",
        "Python can be used for rapid prototyping, or for production-ready software development.",
        "Python can be used on a server to create web applications."
    ]
    
    index = choice("012")
    print(funfacts[int(index)])
    
   
# The below line indicate that now randomfunfact() will run  
if __name__ =="__main__":
    randomfunfact()