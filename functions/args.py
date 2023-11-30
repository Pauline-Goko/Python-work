def hello(*names):
    for name in names:
        print(f"Hello {name}")
        
        #positional argument with single asterick
def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
        
    return answer
    
    
# write a function that accepts any number of integers and returns
# the result of multiplying all of them

def multiply(*numberss):
    answer = 1
    for num in numberss:
        answer *=num
        
    return answer


    #keyword argument with double astericks   
def student_attributes(**kwargs):
      for key,value in kwargs.items():
          print(f"{key} : {value}")
          
          
def my_country(country="Burundi"):
     print(f"Hello from {country}")
      
           
         