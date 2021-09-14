import multiprocessing
from multiprocessing import Process
def square(n):
       print("The number squares to ",n**2)
def cube(n):
       print("The number cubes to ",n**3)
if __name__=="__main__":
   p1=Process(target=square,args=(7,))
   p2=Process(target=cube,args=(7,))
   p1.start()
   p2.start()
   p1.join()
   p2.join()
   print("Completed")